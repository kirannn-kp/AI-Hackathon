"""Public offline checks, not an answer-key grader or live cloud test."""
import json
import unittest
from pathlib import Path

from route_resolve.lab import validate_result
from route_resolve.mcp_server import create_server
from route_resolve.models import Result

ROOT = Path(__file__).resolve().parents[1]


class ContractTests(unittest.TestCase):
    def test_fixture_identity_and_counts(self) -> None:
        for filename, count in (("practice-requests.json", 20), ("final-requests.json", 10)):
            with self.subTest(filename=filename):
                rows = json.loads((ROOT / "data" / filename).read_text(encoding="utf-8"))
                self.assertEqual(len(rows), count)
                self.assertEqual(len({row["id"] for row in rows}), count)
                for row in rows:
                    self.assertEqual(set(row), {"id", "user_id", "text"})
                    self.assertTrue(all(isinstance(value, str) and value.strip()
                                        for value in row.values()))

    def test_valid_simulated_result_shape(self) -> None:
        result = Result("TEST-01", "Access", "Resolve", "Offline contract example", ("test-only-ref",))
        self.assertEqual(validate_result(result, "TEST-01")["request_id"], "TEST-01")

    def test_invalid_result_is_rejected(self) -> None:
        for result in (
            Result("wrong-id", "Access", "Resolve", "Offline test", ("test-only-ref",)),
            Result("TEST-01", "Access", "Execute", "Offline test", ("test-only-ref",)),
            Result("TEST-01", "Access", "Resolve", "Offline test", ()),
            Result("TEST-01", "Access", "Resolve", "Offline test", ("test-only-ref",), simulation=False),
        ):
            with self.subTest(result=result), self.assertRaises(ValueError):
                validate_result(result, "TEST-01")

    def test_bonus_is_not_a_fifth_core_milestone(self) -> None:
        guides = ROOT / "docs"
        self.assertEqual(len(list(guides.glob("mission-*.md"))), 4)
        self.assertTrue((guides / "bonus.md").is_file())


class McpContractTests(unittest.IsolatedAsyncioTestCase):
    async def test_nine_registered_tools_without_cloud_or_server_listener(self) -> None:
        tools = await create_server("team-01").list_tools()
        self.assertEqual(len(tools), 9)
        self.assertIn("get_project_owner", {tool.name for tool in tools})


if __name__ == "__main__":
    unittest.main()
