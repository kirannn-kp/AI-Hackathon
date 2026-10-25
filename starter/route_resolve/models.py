from dataclasses import dataclass
from typing import Literal

Category = Literal["Access", "Procurement", "DataSharing"]
Outcome = Literal["Resolve", "Execute", "Route", "Escalate"]


@dataclass(frozen=True)
class Result:
    request_id: str
    category: Category
    outcome: Outcome
    explanation: str
    citations: tuple[str, ...]
    action_id: str | None = None
    simulation: bool = True
