# Mission 02 - Save an agent, inspect tools and test your code (40 minutes)

## What you are going to do

Save a reusable portal agent, discover the supplied local tools from Python,
and write small offline tests for your triage implementation.

**You finish with:** your named portal agent, one actual MCP diagnostic and two
tests you can explain.
**You learn:** agent configuration, tools and application tests solve different
problems. Portal instructions do not automatically update your Python code.

**Where:** Foundry, VS Code and the same configured PowerShell terminal.
**Why:** your application needs verified facts, not just plausible generated text.

## Step 1 - Save your own portal agent (8 minutes)

From the model playground, use **Save as agent**, give it a unique name such as
`team-XX-initials-intake`, then **Create and open playground**. Stay in your
assigned project. If the UI differs, ask the coordinator rather than creating
resources. Remove automatically attached Web search.

Add the instructions you tested in Mission 01. Send one complete request and
one missing-field request: "Please give me access." Note the saved version.

**You should see:** your named agent and real responses.
**What you learn:** the saved remote agent persists configuration; your local
`client.as_agent` object is a different runtime, not a synchronized copy.

## Step 2 - Read the tool implementation; do not edit it (7 minutes)

Open `starter/route_resolve/mcp_server.py` and find `get_project_owner`.
Follow its call into `starter/route_resolve/tools.py`. Find the Phoenix fixture
and the explicit error for an unknown project.
Read `lab.py`'s `inspect_tools`: locate `ClientSession`, `list_tools` and
`call_tool`. These are supplied plumbing, **not files to modify**.

Predict the difference between `Phoenix` and `Project Phoenix` as tool arguments.

**You should see:** tool registration, actual synthetic records and error handling.
**What you learn:** a tool is ordinary code behind a declared interface.

## Step 3 - Run a real local MCP diagnostic (5 minutes)

```powershell
.\.venv\Scripts\python -m route_resolve.lab tools --tool get_project_owner --project Phoenix
.\.venv\Scripts\python -m route_resolve.lab tools --tool check_user_access --user-id user-02 --project Phoenix --role Reader
```

The runner starts its own local stdio server for each diagnostic. No cloud
approval flag is needed for these local calls. Inspect tool names and actual
results. This is not evidence that the portal called a remote MCP server.

**You should see:** tool discovery and real local tool results.
**What you learn:** local facts, cloud model calls and hosted tools have distinct
authentication and runtime boundaries.

## Step 4 - Write two offline tests with Copilot (15 minutes)

Create your own `tests/test_intake.py`; do not edit supplied contract tests.
Keep test execution offline by mocking the narrow model-call boundary you
introduced in Mission 01.

1. A response with an unsupported category must be rejected explicitly.
2. A missing project must remain missing; it must not turn into `Phoenix`.

Use synthetic model-response doubles and label them as such. Run:

```powershell
.\.venv\Scripts\python -m unittest discover -s tests -p test_intake.py -v
```

If your design mixes calling and validation, extract a small validation helper
in `agents.py`. Do not replace the live implementation with a fake.
Explain why these tests prove local validation, not live model reliability.

**You should see:** two executed tests and, if needed, a small corrective edit.
**What you learn:** repeatable offline tests reduce expensive trial-and-error.

## Step 5 - Review the change (5 minutes)

Have the reviewer explain the fake dependency, each expected assertion and the
actual test output. Record one limitation. Rotate roles before Mission 03.

**You should see:** tests that can fail for the intended reason.
**What you learn:** green output is useful only if the assertion checks the requirement.

## Checkpoint - show the coordinators

- [ ] Show your saved portal agent and distinguish it from local construction.
- [ ] Point to tool registration and the actual diagnostic result.
- [ ] Show two offline tests and explain what they do not prove.

## Optional Copilot prompts

```text
Explain inspect_tools in lab.py and the registered get_project_owner tool
without editing supplied files. Help me write tests/test_intake.py for my
triage validation, with no network calls. Explain exactly what is mocked.
Do not weaken supplied contracts or replace my live implementation.
```

## Troubleshooting

| Problem | Next step |
|---|---|
| Missing MCP import | Use the prepared .venv and approved extras from setup |
| Unknown synthetic project | Inspect the argument; use Phoenix exactly |
| Test unexpectedly calls Azure | Stop and mock the correct model-call boundary |
| Portal agent absent | Ask for coordinator help; do not create a new project |

Next: [Mission 03](mission-03.md).

Reference: [Agent Framework MCP tools](https://learn.microsoft.com/en-us/agent-framework/agents/tools/).
