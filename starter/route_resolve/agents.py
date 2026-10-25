from .models import Result


def triage(request: str) -> dict[str, object]:
    """Return category, urgency and missing_fields using the configured Foundry model."""
    raise NotImplementedError("Challenge 02: implement structured triage, not a keyword router.")


def retrieve_policy(category: str, request: str) -> dict[str, object]:
    """Use the team's Foundry IQ knowledge base and preserve returned citations."""
    raise NotImplementedError("Challenge 03: retrieve policy evidence with citations.")


def resolve(request: str) -> Result:
    """Hand off to a specialist, call mock MCP tools and explain the final outcome."""
    raise NotImplementedError("Challenge 04: implement bounded specialist handoff.")
