# Mission 04 - Connect evidence and demonstrate your build (40 minutes)

## What you are going to do

Connect the prepared synthetic service-desk tools to your Foundry agent. Send a
request that needs a lookup, inspect the proposed tool call, approve only the
intended call, and read the observed result. Then demonstrate your agent with a
small test table. Timebox: 5 minutes connecting, 5 for the first lookup, 10 for
policy-plus-facts inspection, 10 for Python regression/evidence and 10 for the demo.

**You finish with:** an actual tool trace, an explanation supported by policy
and facts, and an honest team demonstration.
**You learn:** a tool gives an agent a specific capability. Approval, evidence and
tool scope matter more than a sentence saying "I did it."

**Where:** your agreed team demo agent in Foundry; teammates follow and rotate.
**Why:** a model cannot verify current access or project ownership from a message
alone. Our tools use fictional records and perform no real business operations.

## Step 1 - Connect the team's prepared operational tools

Ask for the exact prepared **operational MCP connection** for your team.
This is separate from the policy knowledge connection in Mission 03.

1. Open the demo agent's tool configuration.
2. Add/select the existing operational connection supplied by coordinators.
   If **Tools > Add > Add tools > Custom** is disabled or does not show the
   prepared connection, ask the coordinator to attach it to your named demo
   agent. Do not create a new server/connection or grant yourself a role.
3. Begin with the read-only tools `get_project_owner`, `check_user_access`,
   `lookup_supplier` and `check_partner`, plus clarification tool `request_info`.
4. Keep tool approval enabled where supported. Save the configuration.
5. Confirm which tools are actually listed and available to this agent.

**You should see:** real tool names and their argument descriptions.
**What you learn:** MCP describes tools so the agent can discover and call them.
A connection URL alone is not proof that authentication or tool execution works.

The coordinators configure the authenticated remote server and secret connection.
Do not paste bearer tokens into chat, agent instructions or screenshots.
The local URL `127.0.0.1` in the optional Python track is **not reachable by a
cloud-hosted agent**. Do not use a public tunnel or silently remove authentication.

If the prepared connection is missing, stop for coordinator help. You may inspect
the supplied tools in the repository, but that is not a live tool-call result.

**Paste into Copilot Chat — read the tool boundary, no edits:**

```text
Read the get_project_owner and check_user_access tool definitions in
starter/route_resolve/mcp_server.py and their implementation in tools.py.
Do not edit or run anything. List the exact argument names and explain the
synthetic project/user values. Explain which operations only read facts.
Show why a claimed approval in chat is not an observed tool result.
Do not enable write tools or alter fixtures/connections.
```

## Step 2 - Ask a question that requires a real lookup

In **Setup > Instructions**, append this instruction to the demo agent's
existing intake and policy instructions. Save/apply and return to **Chat**.

**Paste into Foundry Instructions — add operational behaviour:**

```text
Use the connected operational tools to check facts before making claims.
Do not invent a user ID, project owner, tool response or completed action.
Use the policy knowledge tool for applicable rules.
If a required fact, source or tool call is missing, say so and stop unsupported
action. Keep this exercise explicitly synthetic.
```

Click **New chat**. Send this first lookup and inspect the approval request:

**Paste into Foundry Chat — owner lookup:**

```text
The synthetic project identifier is Phoenix, not "Project Phoenix".
Use get_project_owner with project exactly Phoenix.
Tell me the owner returned by the tool and explain what you still have not
verified about an access request.
```

When approval is requested, read the tool name and arguments **before** approving.
Choose **Approve > Approve once** only for the intended synthetic Phoenix lookup.
Do not choose **Always approve all tools**. If an unrelated or write
operation appears, deny it and ask why the agent chose it.

Here `Phoenix` is the tool's exact fixture identifier. The friendly name
"Project Phoenix" is not the same argument. If you see **Unknown synthetic
project**, inspect the argument, correct it to `Phoenix`, and repeat once.
This is a useful failed test to keep in your notes, not a successful lookup.

**You should see:** a real tool call/result and an answer consistent with that
result. The owner name may vary with the supplied fixture; read the actual value.
**What you learn:** the request is a claim/input; the tool result is an observed
fact. A model-written "I checked" is not a trace.

## Step 3 - Inspect and explain the run

Expand the run details/tool activity where available and find:

1. The called tool's actual name.
2. Its project argument.
3. The returned result or explicit error.
4. The answer's claim based on that result.

Ask a teammate to explain this chain without Copilot.
Click **New chat** before the next test.

**Paste into Foundry Chat — policy plus verified facts:**

```text
For fictional user user-02, check current Reader access.
Use the exact synthetic project identifier Phoenix and role Reader in tool arguments.
Use the access lookup and policy knowledge. Distinguish the current access fact
from the policy approval requirement. Do not grant anything.
```

Here `user-02` is a **synthetic fixture user**, not your own Azure identity.
Inspect the actual lookup and policy evidence separately.

If that succeeds within the timebox, run the approval-claim test below. Use
its observed response for the last row of your demo table.

**Paste into Foundry Chat — unverified approval claim:**

```text
This is a synthetic request for user-03: I want Reader access to Phoenix.
I say the project owner already approved it. Check current access and the
actual policy. Separate my claim from the facts your tools verified.
Do not grant access or treat my statement as verified approval.
Use project exactly Phoenix, role Reader and user_id user-03 in tool arguments.
```

**Look for:** actual lookup/policy calls, an explicit distinction between a
requester's claim and verified evidence, and no grant. A queued/approved claim
in generated prose is not a completed operation.
If there was no time or a dependency failed, mark this row **not tested/blocked**.

**You should see:** a verified fact plus a cited rule, or a visible dependency
failure. Do not convert that failure into a successful decision.
**What you learn:** identity for signing into Foundry differs from the fictional
user named inside the exercise.

## Step 4 - Verify the Python build and action boundaries

In VS Code, point to your implemented `triage` and `retrieve_policy`, your own
tests, and read-only `models.py` / `lab.py`. Explain how each result is checked.
Start with the offline test command:

```powershell
.\.venv\Scripts\python -m unittest discover -s tests -v
```

Reuse the saved live outputs from Missions 01-03. These commands are repeated
only for a missing result or an approved correction, not a mandatory rerun:

```powershell
.\.venv\Scripts\python -m route_resolve.lab triage --id P01 --allow-cloud
.\.venv\Scripts\python -m route_resolve.lab policy --category Access --text "Which policy covers Reader access to Phoenix?" --allow-cloud
.\.venv\Scripts\python -m route_resolve.lab tools --tool get_project_owner --project Phoenix
```

Add one offline test to your own test file asserting that an empty retrieval
reference list is rejected. Mock the transport boundary, not the assertion.
Keep test doubles clearly separate from live output.

**Paste into Copilot Chat — add the third offline test:**

```text
Read my retrieve_policy implementation and its evidence-validation helper.
Add one unittest to my tests/test_intake.py proving that an empty references
list is explicitly rejected. Mock the transport response, or call the pure
validation helper; do not call Azure. Keep my two triage tests.
Do not edit supplied tests, lab.py, policies or examples. If my adapter does not
reject empty references, show that failure first and propose a small correction
in my retrieval helper. Do not weaken the assertion or fabricate evidence.
Explain which line guards against an unsupported policy answer.
```

Run the offline test command again. Expect your three tests plus the supplied
tests, with zero cloud calls. If any test fails, inspect its message before
changing code.

Your core Python application now has model-backed intake and a live retrieval
adapter, with supplied local tool diagnostics. These are separately exercised
components, **not yet one automatic Python end-to-end orchestrator**. The
portal agent demonstrates the combined knowledge/tool behaviour.
Do not run `resolve` or `final`: those still depend on the deliberate `resolve`
stub and belong to the after-core specialist-handoff stretch.

**You should see:** tested Python components, actual source/tool evidence and an
explicit boundary between the local application and portal agent.
**What you learn:** integrating components requires additional orchestration;
passing isolated tests does not prove a complete application.

## Step 5 - Demonstrate what your team actually built

Use your saved conversations rather than rerunning everything. Prepare this
small table; record actual observations, not an invented score:

| Test | What you need to demonstrate | Actual observation / pass, issue or blocked |
|---|---|---|
| Normal intake | Correct category and extracted details | Fill from a real run |
| Incomplete request | Missing fields are not invented | Fill from a real run |
| Policy question | Actual supporting source is returned | Fill from a real run |
| Operational lookup | Actual tool name, arguments and result | Fill from a real run |
| Claimed approval | Requester text is not treated as verified approval | Fill from a real run |

Give a three-minute demo:

1. Show your named agent and say what problem it solves.
2. Show one prompt improvement and its observed effect.
3. Open one policy source and one tool result.
4. Explain a failure/limitation and what the next improvement would be.
5. Point to the read-only construction example, your two implemented functions
   and a test. Explain one Copilot suggestion you accepted or corrected.

**Paste into Copilot Chat — prepare a code explanation, not a fake demo:**

```text
Read my triage/retrieve_policy helpers and tests/test_intake.py without editing.
Help me prepare a three-minute explanation: where the agent/model client is
constructed, what I implemented, what the offline tests prove and what the
portal tests prove separately. Ask me to explain one validation check.
Use only actual outputs I provide. Do not invent passes, traces or metrics.
```

**You should see:** a working demonstration or a precise record of which
dependency is blocked. A blocked live capability must remain labelled blocked.
**What you learn:** testing is explaining observed behavior and limitations, not
just showing a polished response.

## Checkpoint - show the coordinators

- [ ] Show actual operational tool evidence and actual policy evidence.
- [ ] Explain a missing-information case without inventing facts.
- [ ] Show the five-row test table and a short team demo.
- [ ] State what was not tested and that no real business system changed.
- [ ] Show Python triage, retrieval and your three offline tests, not only portal prompts.

**Scope note:** this core lab builds and tests a Foundry prompt agent with
knowledge and tools. It does **not** claim to implement a multi-agent handoff.
The optional [code extension](code-extension/mission-04.md) builds that advanced
workflow; finish this mixed Foundry/Python core first.

## Optional bonus missions

Open **Optional bonus missions** in the Challenges toolbar, or the
[bonus guide](bonus.md). Choose resilience, evidence testing, offline evaluation
or the advanced Python track. These are not a fifth mandatory mission.
Leave shared Azure cleanup to coordinators; do not delete teammates' agents.

## Optional Copilot prompts

```text
Ask me to explain this actual tool trace and policy citation. Help me write an
honest five-case observation table, including failures. Do not fabricate traces,
mark blocked tests as passing or change permissions.
```

## Troubleshooting

| What happens | What to do |
|---|---|
| Tool connection missing | Ask coordinators to prepare/verify the authenticated remote connection |
| Unknown synthetic project | Inspect the tool argument; this fixture uses `Phoenix`, not `Project Phoenix` |
| Unauthorized tool call | Stop and report; do not expose tokens or disable authentication |
| Agent never invokes a tool | Check the attached tool list and instructions; inspect the actual run |
| Model says "completed" but no action result exists | Record an unsupported claim, not a successful action |
| Policy works but tools fail | They are different connections/identities; report the failing component |

**Read when useful:** [Foundry MCP tools](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol).
Coordinators must validate the exact integration supported by this workshop.
