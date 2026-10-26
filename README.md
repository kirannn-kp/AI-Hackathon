# AI Hackathon - Mission: Route & Resolve

Build and explain a fictional service-desk prototype using **Microsoft Foundry,
Python and GitHub Copilot**. Use Foundry to experiment with agent behaviour and
inspect live knowledge/tools; use VS Code to implement and test application
components. All requests, policies and actions are synthetic.

## The three-hour core

Complete [Environment Setup](docs/environment-setup.md) and the
[workstation checklist](docs/code-extension/setup.md) **before the timer starts**.
The schedule is 180 minutes, including checkpoints, demo and recovery buffer.
It is a planning timebox, not a certified beginner completion time.

| Minutes | Mission | Build and show |
|---|---|---|
| 0-40 | [01 - Prompt to Python](docs/mission-01.md) | Prompt comparison, read-only construction tour, implement `triage`, real Python model call |
| 40-80 | [02 - Agents, tools and tests](docs/mission-02.md) | Saved portal agent, local MCP diagnostics, two offline tests |
| 80-125 | [03 - Policy evidence](docs/mission-03.md) | Real portal retrieval, implement `retrieve_policy`, actual Python references |
| 125-165 | [04 - Evidence and demo](docs/mission-04.md) | Combined portal knowledge/tools, third offline test, code review and demo |
| 165-180 | Recovery and final checkpoints | Finish incomplete checks, explain limitations; no new feature work |

**Bonus is outside the three-hour core**, after the four required checkpoints
are complete. Do not sacrifice the core demo to start a stretch task.

## Which surface does what?

| Surface | Use | Identity |
|---|---|---|
| HackboxConsole | Instructions, team names, checkpoints and progress | Supplied shared team console login |
| [Microsoft Foundry](https://ai.azure.com/) | Experiment, save your own agent, inspect real policy/tool calls | Your own approved Azure identity |
| VS Code and GitHub Copilot | Read code, implement two functions, write tests, debug | Your own GitHub/Copilot entitlement |
| [Public participant repository](https://github.com/kirannn-kp/AI-Hackathon) | One working clone for all missions | No invitation needed to read/clone; Copilot uses your own account |

Everyone uses their own laptop/identity. Rotate driver, reviewer, Foundry tester
and evidence presenter; combine roles in smaller teams. Do not share passwords,
MFA, tokens or edit teammates' agents. If Copilot is unavailable, pair-review the
same code tasks; it is an assistant, not a runtime dependency.

## Read this; edit that

| Read only | Why |
|---|---|
| [Agent construction example](examples/agent_blueprint.py) | Locate `FoundryChatClient` and `client.as_agent`; construction is not invocation |
| `starter/route_resolve/models.py` | Supplied categories and Result contract |
| `starter/route_resolve/lab.py` | CLI, trusted IDs and validation |
| `starter/route_resolve/mcp_server.py`, `tools.py` | Tool registration and synthetic operational fixtures |

**Core edit area:** `triage` and `retrieve_policy` plus small helpers in
`starter/route_resolve/agents.py`, and your own `tests/test_intake.py`.
Leave `resolve`, supplied contract tests, policies, fixtures and shared cloud
connections unchanged. Use Copilot for one focused change at a time; explain it
before running. Never substitute hard-coded answers for a real model call.

## What completion means

- Real model-backed Python triage and live Python policy retrieval.
- Three offline validation tests; label mocked responses as offline evidence.
- Your uniquely named portal agent with real policy/tool observations.
- A short code explanation and five-case evidence table, including limitations.

The portal configuration and local Python functions are **different runtimes**.
The core builds tested components and demonstrates combined behaviour in the
portal; it does not claim a deployed Python service or automatic multi-agent
workflow. Full `resolve` orchestration and the ten-case `final` batch are stretch.

No new Azure resources/models, public tunnels or permission changes are learner
tasks. Policy reads are shared across approved project identities; names are not
security boundaries. Individual CLI retrieval access and each prepared tool
connection still need coordinator verification. Missing evidence stays blocked.

## After-core reference and bonus

Choose [bonus exercises](docs/bonus.md) after completion, or follow the detailed
[specialist-handoff extension](docs/code-extension/mission-04.md).
The [detailed recipes](docs/code-extension/mission-01.md) support core coding;
their full advanced tasks are not additional requirements inside 180 minutes.

Read the [story](docs/START_HERE.md) and [architecture](docs/architecture.md).
Maintainers rebuild the reader and console import with `scripts/build_workshop.py`.
Generated pages do not deploy or authenticate anything; the console retains its
original styling and team progress.

## Attribution and safe use

Adapted from Microsoft's MIT-licensed Fraud Intelligence MicroHack, revision
`3a3c15c9119b9b926c897a17332783c6dc055e3c`.
See `LICENSE` and the
[upstream licence](https://github.com/microsoft/MicroHack/blob/main/LICENSE).
Use fictional data only; never enter customer documents or credentials.
