# Architecture - two runtimes, one learning journey

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
