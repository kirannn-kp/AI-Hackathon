"""Attach one existing workshop connection to a saved portal agent; never invoke it."""
from __future__ import annotations

import argparse
import os
import re
from typing import TYPE_CHECKING
from urllib.parse import urlsplit

if TYPE_CHECKING:
    from azure.ai.projects import AIProjectClient

TOOL_NAMES = {
    "policy": ["knowledge_base_retrieve"],
    "operations": [
        "get_project_owner", "check_user_access", "lookup_supplier",
        "check_partner", "request_info",
    ],
}


def validate_target(team_id: str, endpoint: str, agent_name: str) -> None:
    if not re.fullmatch(r"team-\d{2}", team_id):
        raise ValueError("Set your assigned TEAM_ID, such as team-01.")
    parsed = urlsplit(endpoint)
    if (
        parsed.scheme != "https"
        or not parsed.hostname
        or not parsed.hostname.endswith(".services.ai.azure.com")
        or parsed.path.rstrip("/") != f"/api/projects/{team_id}"
        or parsed.username
        or parsed.password
        or parsed.query
        or parsed.fragment
    ):
        raise ValueError("FOUNDRY_PROJECT_ENDPOINT must address your assigned TEAM_ID project.")
    if not agent_name.startswith(f"{team_id}-") or not re.fullmatch(r"[a-zA-Z0-9-]+", agent_name):
        raise ValueError("Use your own saved agent name, beginning with your team ID.")


def connect(client: AIProjectClient, team_id: str, agent_name: str, kind: str) -> str:
    from azure.ai.projects.models import MCPTool, PromptAgentDefinition

    if kind not in TOOL_NAMES:
        raise ValueError("Choose policy or operations.")
    suffix = "policy-knowledge" if kind == "policy" else "operations"
    connection_name = f"{team_id}-{suffix}"
    connection = client.connections.get(connection_name, include_credentials=False)
    if connection.type != "RemoteTool" or not connection.target.startswith("https://"):
        raise ValueError("The prepared connection must be an HTTPS RemoteTool.")
    latest = next(iter(client.agents.list_versions(
        agent_name, limit=1, order="desc", include_drafts=False,
    )), None)
    if latest is None or not isinstance(latest.definition, PromptAgentDefinition):
        raise ValueError("Save your own prompt agent before connecting a tool.")
    definition = PromptAgentDefinition(latest.definition.as_dict())
    tools = list(definition.tools or [])
    for tool in tools:
        if isinstance(tool, MCPTool) and tool.project_connection_id == connection_name:
            allowed = tool.allowed_tools
            names = allowed if isinstance(allowed, list) else getattr(allowed, "tool_names", None)
            if (
                tool.server_url != connection.target
                or tool.require_approval != "always"
                or names is None
                or set(names) != set(TOOL_NAMES[kind])
            ):
                raise ValueError("Existing tool settings differ; review them instead of overwriting.")
            return latest.version
    tools.append(MCPTool(
        server_label=connection_name.replace("-", "_"),
        server_url=connection.target,
        project_connection_id=connection_name,
        allowed_tools=TOOL_NAMES[kind],
        require_approval="always",
    ))
    definition.tools = tools
    saved = client.agents.create_version(
        agent_name, definition=definition,
        metadata=latest.metadata, description=latest.description,
    )
    return saved.version


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent-name", required=True, help="Your own saved team-prefixed agent.")
    parser.add_argument("--connection", choices=TOOL_NAMES, required=True)
    parser.add_argument("--apply", action="store_true", help="Allow saving a new portal-agent version.")
    args = parser.parse_args()
    if not args.apply:
        parser.error("Add --apply only when you intend to update your own saved agent.")
    team_id = os.environ["TEAM_ID"]
    endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
    validate_target(team_id, endpoint, args.agent_name)
    from azure.ai.projects import AIProjectClient
    from azure.identity import AzureCliCredential

    with AzureCliCredential(process_timeout=15) as credential:
        with AIProjectClient(endpoint=endpoint, credential=credential, retry_total=0) as client:
            version = connect(client, team_id, args.agent_name, args.connection)
    print(f"Prepared {args.connection} connection attached: {args.agent_name}, version {version}.")
    print("Refresh Foundry, select this version, and inspect Setup > Knowledge/Tools or the read-only YAML.")
    print("No model was invoked, no credentials retrieved, and no shared connection or role changed.")


if __name__ == "__main__":
    main()
