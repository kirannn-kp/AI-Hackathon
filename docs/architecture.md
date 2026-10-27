# Architecture - two runtimes, one learning journey

## Our solution: Route & Resolve

The goal is an evidence-driven request assistant, not a chatbot that promises an
action. Think of triage as the reception desk, a specialist as the person who
understands a policy area, and a tool as a factual lookup.

```text
Fictional employee request
          |
          v
Triage: category, urgency, missing information
          |
          v
Relevant domain: Access | Procurement | DataSharing
          |
          +--> Policy evidence: prepared knowledge MCP / Azure AI Search
          |
          +--> Observed facts: read-only operational MCP tools
          |                   (project owner and current access)
          v
Compare the request, policy and actual tool results
          |
          v
Explain a supported next step, ask for information or escalate
          |
          v
Human review / approval before any real-world action
```

This is the **logical solution design**, not a claim that the complete automatic
pipeline is supplied. In the core, you build and demonstrate its components in
Foundry and Python. Automatic specialist handoff, the Python `resolve` function
and the final ten-case batch are after-core extensions.

| Component | Purpose in our solution | Where you use it |
|---|---|---|
| HackboxConsole | Problem, setup, mission instructions, team checkpoints | This website; it does not execute the agents |
| Team Foundry project | Workspace for your own saved agents and approved connections | One assigned `team-XX` project per team |
| `route-resolve-chat` | Existing model deployment for interpreting requests and drafting responses | Foundry playground/agents and Python model calls |
| Policy knowledge | Supplies actual policy passages and source references | Prepared knowledge MCP in Foundry; Search retrieval API in Python |
| Operational MCP | Returns observed synthetic owner/current-access facts | Prepared read-only tools in Foundry; local stdio MCP for Python exercises |
| VS Code and Copilot | Explain supplied code, implement focused functions and write tests | Each learner's clone; Copilot is a development assistant, not an automatic connection to the portal |
| Human reviewer | Checks the evidence and decides whether approval is appropriate | Team demo and coordinator checkpoints; no real action is performed |

### Example journey

For **"Please give user-02 Reader access to Phoenix"**, identify the request
category, retrieve the applicable policy, inspect the owner and current-access
tool outputs, and explain what is still required. An owner lookup is not an
approval; `has_access: false` is not a request to change permissions. A tool name
written in a response is not evidence that the tool ran.

Access, Procurement and DataSharing are the three domain roles in the design.
The prepared owner/access tools demonstrate the Access example; do not assume
they provide purchasing, data-sharing or write capabilities.

## Foundry + Python

```text
HackboxConsole: instructions, teams, checkpoints
                    |
          Your individual identity
             /                 \
Foundry portal                  VS Code / Python / Copilot
Saved prompt agent              Your triage function -> Foundry model
Prepared knowledge MCP          Your retrieve_policy -> Search retrieve API
Prepared operational MCP        Supplied lab tools -> local stdio MCP
             \                 /
           Actual evidence and tests
```

The portal saved agent and the local program are **not synchronized**.
The same underlying model/knowledge can be reached through different APIs and
identities. A working portal connection does not prove CLI retrieval access.

## Read-only construction tour

Open [examples/agent_blueprint.py](../examples/agent_blueprint.py), without editing.
`FoundryChatClient` selects the existing project/deployment and CLI identity;
`client.as_agent` constructs a local Agent Framework object with instructions.
It sends no prompt and does not create a saved Foundry portal agent.
The caller would own invocation and cleanup; the example is not an application.

In VS Code, read these supplied files without changing them:

| File | Follow this |
|---|---|
| `models.py` | Categories, outcomes and the frozen Result dataclass |
| `lab.py` | `main`, trusted IDs, `inspect_tools`, output validation |
| `mcp_server.py` | Tool registration and the callable exposed to MCP |
| `tools.py` | Synthetic facts, unknown-argument errors and mock actions |

Paths are under `starter/route_resolve`. Core edits belong only in `agents.py`
(`triage`, `retrieve_policy`, helpers) and your own test file.
The core does not require implementing `resolve`.

## What the core demonstrates

1. Observe a model response and improve instructions in Foundry.
2. Implement a structured Python triage call.
3. Inspect actual local MCP facts and test local validation offline.
4. Retrieve real policy evidence in Foundry and through a Python adapter.
5. Demonstrate the combined policy/operational workflow in the portal and
   explain the Python components and tests separately.

This is not a claim of a fully integrated Python orchestrator, a deployed
application or a multi-agent handoff. Those are after-core extensions.

## Boundaries

Request text is a claim, policy states a rule, tools return observed facts and
approval is a separate check. None is permission to change a real system.
All operational records are fictional. Local process state disappears on
restart and is not shared between laptops.

Shared synthetic-policy reads are approved for workshop project identities;
separate index names are not read-isolation boundaries for those identities.
Individual accounts and agent ownership remain distinct. Never change shared
connections, broaden roles or expose the local unauthenticated MCP server.
Keep actual returned references/tool errors; label test doubles as offline.

Read [Microsoft's Agent Framework overview](https://learn.microsoft.com/en-us/agent-framework/overview/)
for the framework concepts; do not upgrade the pinned lab packages to match a
different example. Follow [setup](environment-setup.md) and the assigned values.
