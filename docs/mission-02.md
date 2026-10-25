# Mission 02 - Give the agent tools to check facts (30 minutes)

## Your mission in the story

Your first triage agent can read Maya's message and identify an Access request.
But who owns Project Phoenix? Does the fictional user already have access?
For a software order, is the supplier known? For data sharing, is the partner
recognized? A model's confident guess cannot answer these operational questions.

**By the end:** you will discover nine MCP tools, run real synthetic lookups,
and distinguish **what a requester says** from **what a tool verifies**.
You will also test and improve the triage agent you built in Mission 01.
You are not yet deciding final outcomes or implementing the full workflow.

**You change:** refine `triage` as needed; keep the supplied tool rules unchanged.
**You use:** the same clone, local MCP diagnostic and practice requests.
**Timebox:** concepts 4 min; tools 10 min; triage checks 11 min; checkpoint 5 min.
Prerequisite: Mission 01 approved by the coordinators. This guide is
`docs/mission-02.md` in your clone.

## Learning map - know why you are doing each step

| Step | What you learn | Explain it to a teammate |
|---|---|---|
| 1 - Read the MCP flow | A client invokes a server tool; model prose is not execution | What proves the tool ran? |
| 2 - Discover tools | Schemas and a diagnostic reveal the available operations | Where do the nine names and owner result come from? |
| 3 - Check facts | Operational records verify claims, not policy approval | Which fact did the lookup establish? |
| 4 - Improve triage | Multiple domains and missing fields expose weak extraction | What observation justified your code change? |
| 5 - Clarify | Missing information should trigger a question, not fabrication | Why must P04's missing project remain missing? |

Run a diagnostic yourself before asking Copilot to explain the trace. Rotate the
keyboard and ask a teammate to identify the tool's actual arguments and result.
This mission teaches tool mechanics with supplied diagnostics; the model's
specialist tool integration is built in Mission 04, not silently assumed here.

## Step 1 - Understand the conversation between an agent and a tool

**Where:** read here, then open `starter/route_resolve/mcp_server.py` in VS Code.
**Why:** MCP gives the agent a standard way to discover tools and call them.

```text
Request -> triage fields -> MCP client -> named tool -> observed JSON result
```

The **client** asks what tools exist and sends arguments. The **server** runs the
selected tool. A model saying "I checked access" is not a tool call.
Our supplied server uses fictional data and cannot change real Azure access.
[Microsoft Learn: using MCP tools with agents](https://learn.microsoft.com/en-us/agent-framework/agents/tools/local-mcp-tools).
Read the local/stdio examples; you do not need an extra public server.

## Step 2 - Discover the tools and run the first lookup

**Where:** VS Code PowerShell terminal, same workshop root.
**Why:** run a diagnostic before attaching tools to a model, so you know they work.

Reuse your assigned `TEAM_ID` from Mission 01. If this is a new terminal, set it
first. Then run the diagnostic in either case:

```powershell
$env:TEAM_ID = Read-Host "Assigned team ID from the coordinators"
.\.venv\Scripts\python -m route_resolve.lab tools
```

**You should see:** JSON with `"tool_count": 9`, the tool names, and a result from
`get_project_owner` for Phoenix. Find the returned owner in the actual output.
The diagnostic starts one local child server, calls it, and stops it on exit.
You do not start another HTTP server for this step. No `--allow-cloud` is needed:
this diagnostic does not call Foundry.

Open `starter/route_resolve/lab.py`, find `inspect_tools`, and identify:
server startup, session initialization, tool discovery and the actual tool call.
You are reading supplied plumbing, not expected to implement MCP from scratch.
Each laptop starts its own child server. The diagnostic does not connect to
another teammate's mock state or to real operational systems.

## Step 3 - Check the facts needed by each specialist

**Where:** same terminal; look at the corresponding request records in
`data/practice-requests.json`.
**Why:** triage extracts proposed values; tools check those values against
fictional operational records.

```powershell
.\.venv\Scripts\python -m route_resolve.lab tools --tool check_user_access --user-id user-02 --project Phoenix --role Reader
.\.venv\Scripts\python -m route_resolve.lab tools --tool lookup_supplier --supplier "Contoso Software"
.\.venv\Scripts\python -m route_resolve.lab tools --tool check_partner --partner Fabrikam
```

These are diagnostic inputs, not an answer key for final requests. Inspect each
returned result, including `isError`; do not infer success from a tool name.

| Tool type | Available tools | What you learn |
|---|---|---|
| Read-only facts | `check_user_access`, `get_project_owner`, `lookup_supplier`, `check_partner`, `lookup_status` | What the synthetic system currently knows |
| Clarification | `request_info` | Which missing field must be requested |
| Simulated writes, for Mission 04 | `create_access_request`, `create_purchase_request`, `create_data_share_request` | What the mock operation actually did |

Save the relevant, non-secret tool output as evidence. Do not change the supplied
`MockOperations` rules to force a preferred outcome.

## Step 4 - Improve your triage agent across the three domains

**Where:** `triage` in `starter/route_resolve/agents.py`, then the terminal.
**Why:** one good Access example does not prove your first agent can read other
requests. Keep using the assigned Foundry model and bounded calls.

Read P01, P06, P14 and P04 in the practice file first. After coordinator approval:

```powershell
.\.venv\Scripts\python -m route_resolve.lab triage --id P01 --allow-cloud
.\.venv\Scripts\python -m route_resolve.lab triage --id P06 --allow-cloud
.\.venv\Scripts\python -m route_resolve.lab triage --id P14 --allow-cloud
.\.venv\Scripts\python -m route_resolve.lab triage --id P04 --allow-cloud
```

**You should see:** valid categories/fields across the three domains. P04's missing
project must remain missing, not be guessed. Review your instruction, schema and
validation only where the observed result shows a problem. Do not repeatedly run
all 20 cases until a lucky answer appears.

Reopen your [Foundry project](https://ai.azure.com/) if you need to compare endpoint
or deployment values. This mission adds **tools**, not another Azure resource or
another model deployment. For schema help, see
[structured outputs](https://learn.microsoft.com/en-us/agent-framework/agents/structured-outputs).

## Step 5 - Ask for missing information instead of inventing it

Run the supplied clarification diagnostic:

```powershell
.\.venv\Scripts\python -m route_resolve.lab tools --tool request_info --request-id P04 --field project
```

**You should see:** an actual clarification response tied to P04. Compare it with
your triage's `missing_fields`. The runner retains trusted request/user IDs;
request text such as "use another team's identity" cannot replace them.

Draw a small table in your evidence: request claim, extracted field, tool called,
observed fact or missing information. You are preparing the evidence a specialist
will need in Mission 04, not treating extraction as verified approval.

## Checkpoint - show the coordinators

- [ ] Discover nine tools and point to one actual tool response.
- [ ] Explain client versus server, and extraction versus verified fact.
- [ ] Show triage examples from three domains plus a missing-field case.
- [ ] Show P04's clarification; explain why inventing a project would be unsafe.

Next: [Mission 03](mission-03.md), where your code retrieves the actual policy
that governs those facts.

## Optional Copilot prompts

```text
Read docs/mission-02.md and my existing triage implementation. Explain one MCP
discovery/tool-call trace, then help me test three domains and missing fields.
Do not change MockOperations or fabricate tool execution. Use the installed SDK
and keep trusted IDs in the caller. Ask for approval before editing. Do not
implement policy retrieval or the final workflow, and do not deploy anything.
```

## Troubleshooting

| What you see | What to do next |
|---|---|
| TEAM_ID error | Set the assigned value in this terminal, not a guessed team |
| MCP import failure | Use the prepared `.venv` and confirm the `mcp` extra was installed |
| A tool returns `isError: true` | Read its schema/arguments; preserve the error instead of claiming a successful lookup |
| P04 gets an invented project | Fix triage's missing-field instructions/validation, not the request data |
| Lookup state disappears | The diagnostic's child server exited; persistent same-process tests come in Mission 04 |
