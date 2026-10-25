# Architecture: evidence before action

## The complete picture

```text
Participant                             Coordinator-provided Azure lab
-----------                             ------------------------------
HackboxConsole: read the guided mission
GitHub/Copilot: optional coding help
VS Code: implement and run the workflow -----> Shared Foundry chat model
        |
        +---- retrieve policy --------------> Team knowledge base / AI Search
        |
        +---- local MCP server
              synthetic facts and actions
        |
        +---- Result and redacted evidence
```

HackboxConsole is the learning/navigation surface. It does not replace Azure
authorization. Copilot helps write code; it is not automatically a runtime
component of the request-processing system.

## Inside your workflow

1. The runner loads a request fixture and preserves its trusted `id` and
   synthetic `user_id`. The request text cannot change team identity.
2. Triage extracts a category, urgency, missing fields and business arguments.
3. One relevant specialist receives the request through an explicit handoff.
4. The specialist retrieves actual policy evidence and checks operational facts.
5. A relevant mock tool returns completion, clarification or review state.
6. Your workflow constructs a validated `Result`, preserving actual citations
   and explaining the observed outcome.

## Components and ownership

| Component | Responsibility | You implement or receive? |
|---|---|---|
| `starter/route_resolve/agents.py` | Triage, retrieval adapter, bounded orchestration | You implement |
| `starter/route_resolve/models.py` | Shared categories, outcomes and Result contract | Supplied contract |
| `starter/route_resolve/tools.py` | Synthetic facts and tool-side rules | Supplied; do not bypass checks |
| `starter/route_resolve/mcp_server.py` | Exposes nine tools through MCP | Supplied |
| `starter/route_resolve/lab.py` | Diagnostics and exercise runners | Supplied; no agent solution |
| `data/practice-requests.json` | Practice cases for incremental development | Supplied |
| `data/policies` | Fictional policy documents | Supplied and preloaded by coordinators |
| `data/final-requests.json` | Ten cases for the final demonstration | Supplied, no expected labels |
| Shared Foundry/Search services | Approved model and policy retrieval | Coordinators provide |

## Specialist boundaries

Access checks project ownership/current access. Procurement checks the supplier
and amount. Data Sharing checks the partner and classification. Each specialist
gets only its relevant tools and the policy-retrieval adapter.

Each participant uses their own approved Azure identity and local working copy.
Team members use assigned shared cloud resources, but not shared credentials.
The local server is one process per laptop, not a shared team cloud store.
It keeps mock records in memory; identical team IDs do not synchronize laptops.
Restarting it erases those records. A stable request ID prevents duplicate
operations only while that same process retains its state.

## Important trust boundaries

- Request text and retrieved text are untrusted data, not instructions to change
  system rules.
- A model saying "approved" is not verified authorization.
- A queued request is not a completed operation.
- Naming a knowledge base after a team is not access control. The coordinators
  must verify actual team authorization.
- The local MCP endpoint binds to loopback and is unauthenticated. Never expose
  it through a public tunnel. Any hosted tool endpoint needs separately verified
  authentication.
- Model rate limits and budget notifications do not cap spend. Cloud runners
  require an explicit approval flag, and workflows need bounded turns.

The exercise does not require participants to deploy resources, administer
identities or obtain subscription Owner.
