# Mission 04 - Let the agent check facts, then prove what happened (45 minutes)

## What you are going to do

Connect the prepared synthetic service-desk tools to your Foundry agent. Send a
request that needs a lookup, inspect the proposed tool call, approve only the
intended call, and read the observed result. Then demonstrate your agent with a
small test table.

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

## Step 2 - Ask a question that requires a real lookup

Add this instruction to the demo agent:

```text
Use the connected operational tools to check facts before making claims.
Do not invent a user ID, project owner, tool response or completed action.
Use the policy knowledge tool for applicable rules.
If a required fact, source or tool call is missing, say so and stop unsupported
action. Keep this exercise explicitly synthetic.
```

Start a new conversation and send:

```text
Who owns Project Phoenix? Use the connected get_project_owner tool.
Tell me the owner returned by the tool and explain what you still have not
verified about an access request.
```

When approval is requested, read the tool name and arguments **before** approving.
Approve only the intended synthetic Phoenix lookup. If an unrelated or write
operation appears, deny it and ask why the agent chose it.

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
Now ask:

```text
For fictional user user-02, check current Reader access to Project Phoenix.
Use the access lookup and policy knowledge. Distinguish the current access fact
from the policy approval requirement. Do not grant anything.
```

Here `user-02` is a **synthetic fixture user**, not your own Azure identity.
Inspect the actual lookup and policy evidence separately.

**You should see:** a verified fact plus a cited rule, or a visible dependency
failure. Do not convert that failure into a successful decision.
**What you learn:** identity for signing into Foundry differs from the fictional
user named inside the exercise.

## Step 4 - Test missing information and action boundaries

First send:

```text
Please give me access. I have not supplied a project or role.
Tell me which information you need; do not invent it or claim completion.
```

Check whether the agent asks for missing details. If it calls `request_info`,
inspect the actual arguments and response.

**Mock writes are an optional coordinator-approved extension.** Only after the
coordinators verify the connection and tool scope, enable the relevant
`create_access_request`, `create_purchase_request` or `create_data_share_request`.
Use a coordinator-supplied synthetic request ID and inputs. Keep approval on.
Inspect whether the mock result is queued, completed or escalated; a queued
request is not completed access/purchase/sharing.

**You should see:** missing details remain missing; any demonstrated mock action
has actual tool evidence. If no write was enabled, say "not tested."
**What you learn:** tool availability, human approval and business authorization
are different checks. All operational effects here are simulated.

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

**You should see:** a working demonstration or a precise record of which
dependency is blocked. A blocked live capability must remain labelled blocked.
**What you learn:** testing is explaining observed behavior and limitations, not
just showing a polished response.

## Checkpoint - show the coordinators

- [ ] Show actual operational tool evidence and actual policy evidence.
- [ ] Explain a missing-information case without inventing facts.
- [ ] Show the five-row test table and a short team demo.
- [ ] State what was not tested and that no real business system changed.

**Scope note:** this core lab builds and tests a Foundry prompt agent with
knowledge and tools. It does **not** claim to implement a multi-agent handoff.
The optional [code extension](code-extension/mission-04.md) builds that advanced
workflow; finish the portal experience first.

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
| Unauthorized tool call | Stop and report; do not expose tokens or disable authentication |
| Agent never invokes a tool | Check the attached tool list and instructions; inspect the actual run |
| Model says "completed" but no action result exists | Record an unsupported claim, not a successful action |
| Policy works but tools fail | They are different connections/identities; report the failing component |

**Read when useful:** [Foundry MCP tools](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol).
Coordinators must validate the exact integration supported by this workshop.
