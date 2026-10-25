# Mission 04 - Hand off, act and explain (45 minutes)

## Your mission in the story

Maya's Access request, a software-purchase request and a data-sharing request
must not all go to one all-powerful agent. Your triage agent should hand each
request to the relevant specialist. That specialist checks facts, retrieves
policy and either performs a permitted **mock** action, asks for missing
information, routes for approval or escalates for review.

**By the end:** `resolve` runs that bounded workflow and returns a validated
`Result` with actual evidence. You then run the ten final requests and demonstrate
what happened. No real access, purchase or transfer is performed.

**You change:** `resolve(request)` in `starter/route_resolve/agents.py`.
**You reuse:** triage, retrieval, supplied MCP tools and the same Foundry project.
**Timebox:** server/setup 5 min; workflow 20 min; practice/final 12 min; demo 8 min.
Prerequisite: the first three checkpoints passed. This guide is
`docs/mission-04.md` in your clone.

## Step 1 - See the whole flow before writing orchestration

**Where:** read here; keep `models.py` open in VS Code.
**Why:** orchestration decides what runs next; it is not asking every agent to
answer every request.

```text
Trusted fixture IDs + request text
       -> Triage -> one specialist: Access OR Procurement OR DataSharing
       -> retrieved policy + observed MCP facts
       -> clarification / permitted mock action / approval route / escalation
       -> Result + citations + redacted trace
```

| Outcome | What your evidence must mean |
|---|---|
| Resolve | An answer is sufficient; no action was needed |
| Execute | The permitted simulated operation actually completed |
| Route | More information or approval is needed; do not claim completion |
| Escalate | A relevant specialist/reviewer must assess the request |

The final runner passes `resolve` a JSON string containing trusted `id`, `user_id`
and `text`. Parse that envelope first. The business text cannot replace those
IDs, your team identity or the assigned service configuration.

Read [handoff orchestration](https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/handoff)
and [MCP tools](https://learn.microsoft.com/en-us/agent-framework/agents/tools/local-mcp-tools).
Use the pinned Python SDK, not an unrelated portal-hosted-agent deployment guide.

## Step 2 - Start one team-local MCP server and keep it running

**Where:** VS Code **Terminal A**, repository root.
**Why:** one retained mock store lets all specialists see the same action records.
The short-lived diagnostic from Mission 02 does not retain records after exit.

```powershell
$env:TEAM_ID = Read-Host "Assigned team ID"
.\.venv\Scripts\python -m route_resolve.mcp_server --transport streamable-http
```

**You should see:** a server listening on loopback port 8000.
Use `http://127.0.0.1:8000/mcp`; leave Terminal A running.
Do not open a public tunnel or start a different server for every specialist.
Restarting it erases its in-memory action records.

Open **Terminal B** for the workflow commands. Set the same team/model/project
and Search variables from Missions 01/03 there; environment variables do not
transfer between terminals. Reuse the correct cached CLI login.

Authenticated hosted team tools also exist for coordinator-led rehearsals, but
this customer starter's core runner uses local MCP. Do not paste a bearer-protected
hosted URL into an unauthenticated local example or silently switch transports.

## Step 3 - Build the smallest bounded multi-agent workflow

**Where:** `resolve` and your helpers in `agents.py`.
**Why:** specialists need only their own tools, and every model/tool loop must end.

1. Reuse your triage and retrieval work. Create a Triage agent and three specialist
   agents using the configured `FoundryChatClient` and existing deployment.
   Triage chooses a specialist; specialists gather evidence and decide next steps.
2. Register the agents in `HandoffBuilder`. Set Triage as the start and allow
   handoff edges only to Access, Procurement and DataSharing. Require a real
   handoff event, not a model-written sentence saying it handed off.
3. Set explicit turn/output/time limits and a termination condition for a valid
   specialist result. Start with a conservative cap, such as two Triage turns
   and three specialist turns; report unfinished work rather than silently
   raising limits or retrying forever.
4. Attach the policy adapter and only the relevant MCP tools to each specialist:

   | Specialist | Allowed MCP tools |
   |---|---|
   | Access | `check_user_access`, `get_project_owner`, `create_access_request`, `request_info` |
   | Procurement | `lookup_supplier`, `create_purchase_request`, `request_info` |
   | DataSharing | `check_partner`, `create_data_share_request`, `request_info` |

   Use `MCPStreamableHTTPTool` against the **same** loopback server with explicit
   `allowed_tools` and `load_prompts=False`. Triage does not need mock write tools.
5. Retrieve evidence and inspect facts before a write. If fields are missing,
   use `request_info` and keep the clarification result. If a tool reports
   `isError`, preserve the failure; do not convert it into Execute.
6. Construct the supplied `Result` dataclass. Preserve trusted ID, a valid category
   and outcome, a meaningful explanation, a nonempty tuple of actual retrieved
   citation strings, the observed action ID when applicable, and `simulation=True`.
   A queued approval can have an action ID while still being **Route**.

SDK orientation, not a solution:

```powershell
.\.venv\Scripts\python -c "import inspect; from agent_framework import MCPStreamableHTTPTool; from agent_framework.orchestrations import HandoffBuilder; print(inspect.signature(MCPStreamableHTTPTool)); print(inspect.signature(HandoffBuilder.with_autonomous_mode))"
```

The pinned handoff framework requires `require_per_service_call_history_persistence=True`
on its agents. Consume actual workflow events/`AgentResponse` objects instead of
assuming every event contains a list of messages. Close MCP and SDK clients
reliably; `FoundryChatClient` itself is not an async context manager in the pinned
version. If uncertain, inspect installed APIs with your team or coordinators.

You can revisit [Foundry](https://ai.azure.com/) to compare the project/deployment
details, but all orchestration runs from VS Code. You do not need a new project,
model, APIM instance or hosted-agent deployment.

## Step 4 - Observe one practice request end to end

**Where:** Terminal B, after the coordinators approve cloud calls.

```powershell
.\.venv\Scripts\python -m route_resolve.lab resolve --id P01 --allow-cloud
```

**You should see:** one Result with the original request ID and real evidence.
Before running a batch, inspect a redacted trace showing:

1. Which specialist actually received the handoff.
2. Which policy passages/references were retrieved.
3. Which MCP tool names, arguments and results were observed.
4. Why the Result follows from those observations.

Do not accept a plausible paragraph instead of that trace. Check a missing-field
case too. Test a same-ID/same-argument retry against the same server: no duplicate
action should appear. That is a same-process property, not durable storage.

## Step 5 - Run the final ten and keep your evidence

**Where:** Terminal B, once a practice flow and its trace work.
**Why:** the final runner checks record shape, not whether your business answer
is correct.

```powershell
.\.venv\Scripts\python -m route_resolve.lab final --allow-cloud
```

**You should see:** **Wrote 10 results** and `evidence/final-results.jsonl`.
JSONL means one JSON object per line. The runner preserves IDs, checks Result
shape, requires citation/simulation fields and refuses to overwrite existing
output before calling an agent. Keep previous evidence; for an explicitly
approved second run choose `--output evidence/final-results-02.jsonl`.

Do not repeatedly run the whole batch to get a passing screenshot. If something
fails, inspect one failing practice case first. No answer-key grader or private
reference implementation is included.

## Checkpoint - show the coordinators

- [ ] Demonstrate one permitted mock action, one approval/clarification route and one escalation.
- [ ] Point to actual handoff, retrieval and tool traces, not just model claims.
- [ ] Show the ten saved Results with `simulation: true`; keep credentials out.
- [ ] Explain one limitation and the fact that no real business system changed.

## Step 6 - Optional bonus missions are still inside Challenges

After the core demonstration, click **Optional bonus missions** in the Challenges
toolbar or open the [bonus mission guide](bonus.md). Choose failure-path testing,
evidence challenges or an offline evaluation report. Each is optional, takes
about 20-30 extra minutes and does not add a fifth required milestone.
The toolbar's Current/Last mission button returns to the core reader.

When finished, stop your local server in Terminal A with **Ctrl+C**. Do not delete
shared Azure resources; the coordinators manage event cleanup.

## Optional Copilot prompts

```text
Read docs/mission-04.md and my existing triage/retrieval functions. Propose a
bounded Triage-to-one-specialist workflow with least-privilege MCP tools. Use
the pinned SDK and verify signatures/events. Require actual retrieval and tool
evidence before constructing Result; keep trusted IDs and visible failures.
Explain each change before editing. Do not invent traces, provide final-fixture
answer labels, search private solutions or deploy more Azure resources.
```

## Troubleshooting

| What you see | What to do next |
|---|---|
| Loopback connection refused | Check Terminal A, port 8000 and the exact `/mcp` URL |
| Wrong identity/config in Terminal B | Reapply non-secret variables there; compare the cached CLI operator |
| Handoff never happens | Inspect actual events, allowed edges and Triage instructions; do not fake a specialist response |
| Client/context/history error | Check the pinned SDK signatures and lifecycle notes in Step 3 |
| Action ID but request still queued | Distinguish Route from Execute using the observed tool outcome |
| Final output already exists | Preserve it; request approval for another run and use a new output path |
