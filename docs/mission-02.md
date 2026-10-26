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

**The story so far:** In Mission 01, your service desk learned to recognise an
access request and spot missing information. Now imagine another colleague
arrives with a purchase request tomorrow. You need the assistant's instructions
to be reusable, and you need checks that catch bad intake output before anyone
uses it. You will also meet the tools that can answer factual questions later.
Your Python triage and the portal agent remain two separate pieces of this build.

## Step 1 - Save your own portal agent (8 minutes)

**Why this step matters:** A useful conversation is not yet a reusable service.
Saving the agent keeps its name and instructions so you can return to it in
Missions 03 and 04. The two requests below check whether that saved behaviour
handles both missing information and a different business category; they do
not give the agent permission to grant access or buy anything.

From the model playground, use **Save as agent**, give it a unique name such as
`team-XX-initials-intake`, then **Create and open playground**. Stay in your
assigned project. If the UI differs, ask the coordinator rather than creating
resources. Remove automatically attached Web search.

Open **Setup > Instructions** and retain the intake instructions from Mission 01.
Save/apply them and note your agent name/version. Return to **Chat**.

**Paste into Foundry Chat — missing information test:**

```text
Please give me access.
```

**Look for:** a request for the missing project and role, not made-up values or
"done". The agent has no verified user identity or operational tools yet.

Choose **New chat** before the second test.

**Paste into Foundry Chat — another domain:**

```text
I need a EUR 600 software licence from Contoso Software.
```

**Look for:** `Procurement`, the supplied supplier/amount, and no claim of purchase
or verified approval. Write one sentence comparing its behaviour with the first
request. These two observations are your saved-agent tests, not screenshots of
the configuration screen alone.

**You should see:** your named agent and real responses.
**What you learn:** the saved remote agent persists configuration; your local
`client.as_agent` object is a different runtime, not a synchronized copy.

## Step 2 - Read the tool implementation; do not edit it (7 minutes)

**Why this step matters:** Knowing that a request concerns Phoenix is different
from knowing who owns Phoenix or whether a person already has access. Those
facts live in records, not in the request itself. Reading one supplied tool
shows how an assistant can ask ordinary code for a specific fact instead of
inventing it. You will connect the hosted versions in Mission 04.

Open `starter/route_resolve/mcp_server.py` and find `get_project_owner`.
Follow its call into `starter/route_resolve/tools.py`. Find the Phoenix fixture
and the explicit error for an unknown project.
Read `lab.py`'s `inspect_tools`: locate `ClientSession`, `list_tools` and
`call_tool`. These are supplied plumbing, **not files to modify**.

Predict the difference between `Phoenix` and `Project Phoenix` as tool arguments.

**Paste into Copilot Chat — read only:**

```text
Do not edit or run code. Open starter/route_resolve/mcp_server.py and locate
get_project_owner. Follow its call into tools.py. Then open inspect_tools in
lab.py and show ClientSession, list_tools and call_tool.
Explain the journey from a tool name and arguments to a returned fixture value.
Why might Phoenix succeed while Project Phoenix fails? Show the real code
location supporting your answer, not a guessed explanation.
```

**You should see:** tool registration, actual synthetic records and error handling.
**What you learn:** a tool is ordinary code behind a declared interface.

## Step 3 - Run a real local MCP diagnostic (5 minutes)

**Why this step matters:** Before asking a model to choose a tool, you check the
tool directly. That gives you a result you can recognise and helps you separate
an argument mistake from an agent mistake. These commands exercise your local
synthetic service-desk records; they do not yet test the remote Foundry connection.

```powershell
.\.venv\Scripts\python -m route_resolve.lab tools --tool get_project_owner --project Phoenix
.\.venv\Scripts\python -m route_resolve.lab tools --tool check_user_access --user-id user-02 --project Phoenix --role Reader
```

The runner starts its own local stdio server for each diagnostic. No cloud
approval flag is needed for these local calls. Inspect tool names and actual
results. This is not evidence that the portal called a remote MCP server.

In the JSON, find `called`, `tools`, and `result`. Expand the returned text or
structured content. `get_project_owner` should return a fixture owner; the second
command returns an access fact, not a policy decision. If you cannot locate the
value, use this prompt before changing anything.

**Paste into Copilot Chat — explain actual output:**

```text
Here is the actual output of my route_resolve.lab tools command: [paste below].
Without editing code, identify the called tool, the returned fact and any error.
Explain why this local stdio MCP result does not prove a cloud portal tool ran.
Do not make up missing output or change the fixture.
```

**You should see:** tool discovery and real local tool results.
**What you learn:** local facts, cloud model calls and hosted tools have distinct
authentication and runtime boundaries.

## Step 4 - Write two offline tests with Copilot (15 minutes)

**Why this step matters:** Your intake component will see incomplete or
unexpected answers, not just the successful Phoenix example. These tests check
two promises you want the service desk to keep every time: reject an unknown
category and do not invent a missing project. Because the model is replaced by
a clearly labelled test double, you can repeat these checks without cloud calls.

Create your own `tests/test_intake.py`; do not edit supplied contract tests.
Keep test execution offline by mocking the narrow model-call boundary you
introduced in Mission 01.

1. A response with an unsupported category must be rejected explicitly.
2. A missing project must remain missing; it must not turn into `Phoenix`.

**Paste into Copilot Chat — create only our offline tests:**

```text
Read my triage implementation and validation helper in
starter/route_resolve/agents.py. Create tests/test_intake.py using unittest.
Do not edit supplied tests/test_contracts.py, lab.py, models.py or examples.

Write two offline tests:
1. A synthetic model response with category "Other" is explicitly rejected.
2. A synthetic Access response with missing project preserves that missing
   value and does not fill in Phoenix.
Use the schema my implementation actually accepts. Mock its narrow model-call
boundary, or test the validation helper directly. Neither test may call Azure.
Explain each assertion and exactly which dependency is fake.
If validation is currently mixed with I/O, propose a small extraction in my
agents.py first; do not replace the live model call or weaken its checks.
Do not run cloud commands or implement retrieve_policy/resolve.
```

Use synthetic model-response doubles and label them as such. Run:

```powershell
.\.venv\Scripts\python -m unittest discover -s tests -p test_intake.py -v
```

If your design mixes calling and validation, extract a small validation helper
in `agents.py`. Do not replace the live implementation with a fake.
Explain why these tests prove local validation, not live model reliability.
**Check:** the terminal reports two tests passing. If it reports zero tests,
that is not completion; check the filename and `test_` method names with Copilot.

**You should see:** two executed tests and, if needed, a small corrective edit.
**What you learn:** repeatable offline tests reduce expensive trial-and-error.

## Step 5 - Review the change (5 minutes)

**Why this step matters:** A passing test is only useful if the team knows what
would make it fail. The reviewer checks that your two safety promises are
actually being tested, not just that the terminal is green. This gives the next
person a trustworthy starting point before you add company knowledge.

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

**How the story continues:** You now have reusable portal instructions, a
working intake component and two local safety tests. But neither a category nor
a project-owner lookup tells the desk which company rule applies. In Mission 03
you will give the same saved agent a policy source, compare its answer before
and after, and build the Python route to that evidence.

Reference: [Agent Framework MCP tools](https://learn.microsoft.com/en-us/agent-framework/agents/tools/).
