import argparse
import logging
import os
from dataclasses import asdict

from mcp.server.fastmcp import FastMCP

from .tools import MockOperations


def create_server(team_id: str) -> FastMCP:
    operations = MockOperations(team_id)
    server = FastMCP("Route & Resolve synthetic operations", host="127.0.0.1", port=8000)
    server.add_tool(operations.check_user_access)
    server.add_tool(operations.get_project_owner)
    server.add_tool(operations.lookup_supplier)
    server.add_tool(operations.check_partner)
    server.add_tool(operations.lookup_status)
    server.add_tool(operations.request_info)

    @server.tool()
    def create_access_request(
        request_id: str, user_id: str, project: str, role: str,
    ) -> dict[str, object]:
        """Simulate an access request; the server enforces the fictional approval policy."""
        return asdict(operations.create_access_request(request_id, user_id, project, role))

    @server.tool()
    def create_purchase_request(
        request_id: str, user_id: str, supplier: str, amount_eur: str,
    ) -> dict[str, object]:
        """Simulate a software purchase request; never places real orders."""
        return asdict(operations.create_purchase_request(request_id, user_id, supplier, amount_eur))

    @server.tool()
    def create_data_share_request(
        request_id: str, user_id: str, partner: str, classification: str,
    ) -> dict[str, object]:
        """Simulate a data-sharing request; never transmits data."""
        return asdict(operations.create_data_share_request(
            request_id, user_id, partner, classification))

    return server


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--transport", choices=("stdio", "streamable-http"), default="stdio")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    create_server(os.environ["TEAM_ID"]).run(transport=args.transport)


if __name__ == "__main__":
    main()
