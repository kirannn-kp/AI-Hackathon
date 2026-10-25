import hashlib
import json
import logging
import re
from dataclasses import asdict
from decimal import Decimal, InvalidOperation
from threading import Lock

from .models import Category, Outcome, Result

logger = logging.getLogger(__name__)
PROJECTS = {
    "Phoenix": {"owner": "owner-phoenix", "members": ("user-01", "user-02")},
    "Atlas": {"owner": "owner-atlas", "members": ("user-03",)},
}
USERS = ("user-01", "user-02", "user-03")
PARTNERS = ("Fabrikam",)
POLICIES = {
    "Access": ("ACCESS-001", "data/policies/access.md"),
    "Procurement": ("BUY-001", "data/policies/procurement.md"),
    "DataSharing": ("SHARE-001", "data/policies/data-sharing.md"),
}


class MockOperations:
    """One trusted team context per process; every write remains a simulation."""

    def __init__(self, team_id: str) -> None:
        if re.fullmatch(r"team-\d{2}", team_id) is None:
            raise ValueError("TEAM_ID must have the form team-01.")
        self.team_id = team_id
        self._records: dict[str, tuple[str, Result]] = {}
        self._lock = Lock()

    def check_user_access(self, user_id: str, project: str, role: str) -> dict[str, object]:
        self._validate_user(user_id)
        self.get_project_owner(project)
        return {
            "user_id": user_id,
            "project": project,
            "role": role,
            "has_access": user_id == "user-01" and project == "Phoenix" and role == "Reader",
        }

    def get_project_owner(self, project: str) -> dict[str, str]:
        if project not in PROJECTS:
            raise ValueError(f"Unknown synthetic project: {project!r}.")
        return {"project": project, "owner": str(PROJECTS[project]["owner"])}

    def lookup_supplier(self, supplier: str) -> dict[str, object]:
        if not supplier.strip():
            raise ValueError("Supplier is required.")
        return {"supplier": supplier, "approved": supplier == "Contoso Software"}

    def check_partner(self, partner: str) -> dict[str, object]:
        if not partner.strip():
            raise ValueError("Partner is required.")
        return {"partner": partner, "approved": partner in PARTNERS}

    @staticmethod
    def _validate_user(user_id: str) -> None:
        if user_id not in USERS:
            raise ValueError(f"Unknown synthetic user: {user_id!r}.")

    def _record(self, request_id: str, payload: dict[str, str], result: Result) -> Result:
        if not request_id.strip():
            raise ValueError("Request ID is required.")
        fingerprint = json.dumps(payload, sort_keys=True)
        with self._lock:
            previous = self._records.get(request_id)
            if previous:
                if previous[0] != fingerprint:
                    raise ValueError("Request ID already used with different arguments.")
                return previous[1]
            self._records[request_id] = (fingerprint, result)
        logger.info("Mock operation recorded: team=%s request=%s outcome=%s",
                    self.team_id, request_id, result.outcome)
        return result

    def _result(
        self, request_id: str, category: Category, outcome: Outcome, explanation: str,
        payload: dict[str, str],
    ) -> Result:
        policy_id, path = POLICIES[category]
        digest = hashlib.sha256(f"{self.team_id}:{request_id}".encode()).hexdigest()[:16]
        action_id = f"MOCK-{digest}" if outcome in ("Execute", "Route") else None
        if outcome not in ("Resolve", "Execute", "Route", "Escalate"):
            raise ValueError(f"Invalid outcome: {outcome}.")
        result = Result(request_id, category, outcome, explanation,
                        (f"{policy_id}: {path}",), action_id)
        return self._record(request_id, payload, result)

    def create_access_request(
        self, request_id: str, user_id: str, project: str, role: str,
    ) -> Result:
        self._validate_user(user_id)
        self.get_project_owner(project)
        if role not in ("Reader", "Contributor", "Owner"):
            raise ValueError("Role must be Reader, Contributor, or Owner.")
        payload = {"category": "Access", "user": user_id, "project": project, "role": role}
        if role == "Owner":
            outcome, text = "Escalate", "Privileged access requires security review; no grant made."
        elif self.check_user_access(user_id, project, role)["has_access"]:
            outcome, text = "Resolve", "The requested Reader access already exists in the fixture."
        elif role == "Reader" and user_id in PROJECTS[project]["members"]:
            outcome, text = "Execute", "Simulated standard Reader access request completed; no Azure permission changed."
        else:
            outcome, text = "Route", "Mock request queued for project-owner approval; access is not granted."
        return self._result(request_id, "Access", outcome, text, payload)

    def create_purchase_request(
        self, request_id: str, user_id: str, supplier: str, amount_eur: str,
    ) -> Result:
        self._validate_user(user_id)
        try:
            amount = Decimal(amount_eur)
        except InvalidOperation as exc:
            raise ValueError("Amount must be a decimal EUR value.") from exc
        exponent = amount.as_tuple().exponent
        if not amount.is_finite() or amount <= 0 or not isinstance(exponent, int) or exponent < -2:
            raise ValueError("Amount must be positive, finite, and have at most two decimal places.")
        approved = self.lookup_supplier(supplier)["approved"]
        payload = {"category": "Procurement", "user": user_id,
                   "supplier": supplier, "amount": str(amount.normalize())}
        if not approved or amount > 1000:
            outcome, text = "Escalate", "Finance review required; no purchase has been made."
        elif amount > 100:
            outcome, text = "Route", "Mock request queued for manager approval; no purchase has been made."
        else:
            outcome, text = "Execute", "Simulated low-value software request recorded; no real order placed."
        return self._result(request_id, "Procurement", outcome, text, payload)

    def create_data_share_request(
        self, request_id: str, user_id: str, partner: str, classification: str,
    ) -> Result:
        self._validate_user(user_id)
        if classification not in ("Public", "Internal", "Confidential"):
            raise ValueError("Classification must be Public, Internal, or Confidential.")
        approved = self.check_partner(partner)["approved"]
        payload = {"category": "DataSharing", "user": user_id,
                   "partner": partner, "classification": classification}
        if not approved or classification == "Confidential":
            outcome, text = "Escalate", "Security/legal review required; no data has been shared."
        elif classification == "Internal":
            outcome, text = "Route", "Mock request queued for data-owner approval; no data has been shared."
        else:
            outcome, text = "Execute", "Simulated Public-data sharing request recorded; no data was transmitted."
        return self._result(request_id, "DataSharing", outcome, text, payload)

    def lookup_status(self, request_id: str) -> dict[str, object]:
        if request_id not in self._records:
            raise ValueError("Request not found in this team's mock store.")
        return asdict(self._records[request_id][1])

    @staticmethod
    def request_info(request_id: str, field: str) -> dict[str, object]:
        if not request_id.strip() or not field.strip():
            raise ValueError("Request ID and missing field are required.")
        return {"request_id": request_id, "outcome": "Route",
                "missing_field": field, "simulation": True}
