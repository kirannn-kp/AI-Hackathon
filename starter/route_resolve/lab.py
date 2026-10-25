"""Workshop runners and diagnostics, not implementations of the agent exercises."""
import argparse
import asyncio
import json
import os
import re
import sys
from dataclasses import asdict
from pathlib import Path

from .agents import resolve, retrieve_policy, triage
from .models import Result

CATEGORIES = ("Access", "Procurement", "DataSharing")
OUTCOMES = ("Resolve", "Execute", "Route", "Escalate")


def read_records(filename: str) -> list[dict[str, str]]:
    records = json.loads((Path("data") / filename).read_text(encoding="utf-8"))
    if not isinstance(records, list) or not records:
        raise ValueError(f"{filename} must contain a nonempty request list.")
    for record in records:
        if not isinstance(record, dict) or any(
            not isinstance(record.get(key), str) or not record[key].strip()
            for key in ("id", "user_id", "text")
        ):
            raise ValueError(f"{filename} contains an invalid request record.")
    if len({record["id"] for record in records}) != len(records):
        raise ValueError(f"{filename} contains duplicate request IDs.")
    return records


def validate_result(result: Result, request_id: str) -> dict[str, object]:
    if not isinstance(result, Result):
        raise TypeError("resolve must return the Result dataclass.")
    if result.request_id != request_id or result.category not in CATEGORIES:
        raise ValueError("Result must preserve the request ID and a valid category.")
    if result.outcome not in OUTCOMES or result.simulation is not True:
        raise ValueError("Result must have a valid outcome and simulation:true.")
    if not isinstance(result.explanation, str) or not result.explanation.strip():
        raise ValueError("A nonempty explanation is required.")
    if not isinstance(result.citations, tuple) or not result.citations or any(
        not isinstance(item, str) or not item.strip() for item in result.citations
    ):
        raise ValueError("Citations must be a nonempty tuple of reference strings.")
    if result.action_id is not None and (
        not isinstance(result.action_id, str) or not result.action_id.strip()
    ):
        raise ValueError("An action ID, when supplied, must be a nonempty string.")
    if result.outcome == "Execute" and result.action_id is None:
        raise ValueError("Execute requires an observed mock action ID.")
    return asdict(result)


async def inspect_tools(args: argparse.Namespace) -> dict[str, object]:
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client

    team_id = os.environ.get("TEAM_ID", "")
    if not re.fullmatch(r"team-\d{2}", team_id):
        raise ValueError("Set the assigned TEAM_ID, for example team-01.")
    arguments = {
        "get_project_owner": {"project": args.project},
        "check_user_access": {"user_id": args.user_id, "project": args.project, "role": args.role},
        "lookup_supplier": {"supplier": args.supplier},
        "check_partner": {"partner": args.partner},
        "request_info": {"request_id": args.request_id, "field": args.field},
    }
    parameters = StdioServerParameters(
        command=sys.executable, args=["-m", "route_resolve.mcp_server"],
        env={"TEAM_ID": team_id},
    )
    async with stdio_client(parameters) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            listed = await session.list_tools()
            result = await session.call_tool(args.tool, arguments[args.tool])
            if result.isError:
                raise RuntimeError(f"MCP rejected the diagnostic: {result.content}")
            return {
                "tool_count": len(listed.tools),
                "tools": [tool.name for tool in listed.tools],
                "called": args.tool,
                "result": result.model_dump(mode="json"),
            }


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(description=__doc__)
    subcommands = command.add_subparsers(dest="command", required=True)
    subcommands.add_parser("check", help="Check local imports without calling a model.")
    tools = subcommands.add_parser("tools", help="Discover and call one local MCP diagnostic.")
    tools.add_argument("--tool", choices=(
        "get_project_owner", "check_user_access", "lookup_supplier", "check_partner", "request_info",
    ), default="get_project_owner")
    tools.add_argument("--project", default="Phoenix")
    tools.add_argument("--user-id", default="user-02")
    tools.add_argument("--role", default="Reader")
    tools.add_argument("--supplier", default="Contoso Software")
    tools.add_argument("--partner", default="Fabrikam")
    tools.add_argument("--request-id", default="LOCAL-CHECK")
    tools.add_argument("--field", default="project")
    for name in ("triage", "policy", "resolve", "final"):
        cloud = subcommands.add_parser(name, help=f"Run the {name} exercise after facilitator approval.")
        cloud.add_argument("--allow-cloud", action="store_true",
                           help="Confirm facilitator approval of billable shared-service calls.")
        if name in ("triage", "resolve"):
            cloud.add_argument("--id", required=True, help="Practice request ID, e.g. P01.")
        elif name == "policy":
            cloud.add_argument("--category", choices=CATEGORIES, required=True)
            cloud.add_argument("--text", required=True)
        else:
            cloud.add_argument("--output", type=Path, default=Path("evidence/final-results.jsonl"))
    return command


def main() -> None:
    command = parser()
    args = command.parse_args()
    if not Path("pyproject.toml").is_file():
        command.error("Run from the workshop repository root, containing pyproject.toml.")
    if args.command == "check":
        if sys.version_info < (3, 12):
            command.error("Python 3.12 or newer is required.")
        print("Contracts ready")
        print("Local imports passed. Agent stubs are intentional; cloud access is not tested.")
        return
    if args.command == "tools":
        print(json.dumps(asyncio.run(inspect_tools(args)), indent=2))
        return
    if not args.allow_cloud:
        command.error("Cloud calls are blocked. Ask the facilitator before adding --allow-cloud.")
    try:
        if args.command == "final":
            if args.output.exists():
                raise FileExistsError("Keep prior results; choose a new --output before rerunning.")
            records = read_records("final-requests.json")
            if len(records) != 10:
                raise ValueError("Expected ten final requests.")
            results = [validate_result(resolve(json.dumps(row)), row["id"]) for row in records]
            args.output.parent.mkdir(parents=True, exist_ok=True)
            with args.output.open("x", encoding="utf-8") as stream:
                stream.write("\n".join(json.dumps(result) for result in results) + "\n")
            print(f"Wrote {len(results)} results to {args.output}. Shape checked; facilitator review is still required.")
        elif args.command == "policy":
            result = retrieve_policy(args.category, args.text)
            if not isinstance(result, dict) or not result.get("references"):
                raise ValueError("Actual retrieved policy references are required.")
            print(json.dumps(result, indent=2))
        else:
            rows = read_records("practice-requests.json")
            row = next((item for item in rows if item["id"] == args.id), None)
            if row is None:
                raise ValueError(f"Unknown practice request ID: {args.id}")
            if args.command == "resolve":
                result = validate_result(resolve(json.dumps(row)), row["id"])
            else:
                extracted = triage(row["text"])
                if not isinstance(extracted, dict) or extracted.get("category") not in CATEGORIES:
                    raise ValueError("Triage must return a dictionary with a valid category.")
                missing = extracted.get("missing_fields")
                urgency = extracted.get("urgency")
                if (not isinstance(urgency, str)
                        or not urgency.strip()
                        or not isinstance(extracted.get("arguments"), dict)
                        or not isinstance(missing, list)
                        or any(not isinstance(field, str) or not field.strip() for field in missing)):
                    raise ValueError("Triage requires urgency, arguments and a missing_fields list.")
                result = {"request_id": row["id"], "user_id": row["user_id"], "triage": extracted}
            print(json.dumps(result, indent=2))
    except NotImplementedError as error:
        command.exit(2, f"Exercise not implemented yet: {error}\nOpen the current mission guide and implement only that function.\n")


if __name__ == "__main__":
    main()
