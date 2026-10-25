# Mission 04 - Hand off, act and explain (45 minutes)

**Working mode:** read here in HackboxConsole; edit the same cloned repository in VS Code. All exercise files are already present. Add `--allow-cloud` only after the facilitator confirms access and approves shared-service calls.

## What you will learn

Combine triage, policy evidence and tools into a bounded multi-agent workflow.
Run the ten final requests and explain actual outcomes, not just fluent text.

**Timebox:** concepts 5 min; handoff implementation 20 min; final run 10 min;
demo/checkpoint 7 min; stop local processes 3 min.
Prerequisite: triage, MCP and actual policy retrieval pass their checkpoints.

## Concepts in plain language

**Orchestration** coordinates which component runs next. A **handoff** transfers
control from Triage to one relevant specialist. It is not a loop that asks every
agent to answer every question.

**Least privilege** means each specialist gets only its required tools.
**Idempotency** means retrying the same unchanged request does not create a
second action. **Bounded turns** prevent endless model/tool calls and cost.

```text
Triage --handoff--> Access OR Procurement OR DataSharing
                  --retrieve policy--> inspect facts
                  --mock action / clarification--> Result
```

The orchestration runs on your laptop against approved shared Azure services.
The coach may host authenticated tools for the full event, but the timed core
below uses a local loopback tool server. Do not deploy a hosted agent, APIM,
Grafana or extra infrastructure during the exercise.

## Core path

### Step 1 - Add final requests and keep your implementations

The final request file is already in your clone. Do not overwrite your agent implementations.

```powershell
.\.venv\Scripts\python -c "import json; from pathlib import Path; rows=json.loads(Path('data/final-requests.json').read_text()); print('Final requests:',len(rows))"
```

Expected: **Final requests: 10**. There is no answer file in this workshop repository.
Do not ask Copilot to search the private coach repository for one.

### Step 2 - Keep one MCP server alive

A short-lived stdio diagnostic loses its records when it exits. To test retries
across calls, keep a **single team-local HTTP server** running.

In terminal A, from your working folder:

```powershell
$env:TEAM_ID = "team-01"
.\.venv\Scripts\python -m route_resolve.mcp_server --transport streamable-http
```

Expected: a server on loopback port 8000. Use
`http://127.0.0.1:8000/mcp`, not a public address. Leave terminal A running.
Do not run a separate server per specialist; they must see the same mock store.

In terminal B set the cloud/team variables from README.md again. This terminal
runs your agent workflow. Restarting terminal A intentionally erases mock state.

### Step 3 - Build a bounded handoff workflow

Implement `resolve(request: str) -> Result` in `starter/route_resolve/agents.py`.
For the supplied runner, `request` is a JSON string with the fixture's `id`,
`user_id` and `text`. Parse this envelope first. The runner supplies IDs; the
business text must not override identity, team settings or request IDs.

Build these pieces incrementally:

1. Reuse your triage and retrieval work. Create Triage and three specialist
   `Agent` instances using `FoundryChatClient` and the assigned deployment.
2. Register the specialists with `HandoffBuilder`. Set Triage as the start agent
   and add handoff edges only from Triage to the three specialists.
3. Add explicit turn limits and a termination condition for a valid specialist
   result. Use a conservative cap such as two Triage turns and three specialist
   turns; report an unfinished workflow instead of silently increasing the cap.
4. Connect each specialist to the **same loopback server** with
   `MCPStreamableHTTPTool(name=..., url="http://127.0.0.1:8000/mcp", ...)`.
   Set `load_prompts=False` and an explicit `allowed_tools` list:

| Specialist | Allowed MCP tools, plus your policy-retrieval adapter |
|---|---|
| Access | `check_user_access`, `get_project_owner`, `create_access_request`, `request_info` |
| Procurement | `lookup_supplier`, `create_purchase_request`, `request_info` |
| DataSharing | `check_partner`, `create_data_share_request`, `request_info` |

5. The specialist retrieves evidence and checks facts **before** its mock action.
   With missing fields, call `request_info` and preserve clarification instead
   of calling a write with guessed arguments.
6. Treat tool results as authoritative for simulated completion/approval state.
   Handle MCP `isError` explicitly. Do not turn exceptions into Execute.
7. Return the starter's `Result` dataclass, not a prose-only response. Preserve
   retrieved references separately from the mock tool's local policy references.
   A tool's local filename alone is not evidence of a cloud retrieval.
   Construct `citations` as a tuple of nonempty reference strings, as declared
   in `models.py`; JSON serialization will represent it as an array.

SDK names used here match the installed lab versions. If unsure, inspect them:

```powershell
.\.venv\Scripts\python -c "import inspect; from agent_framework import MCPStreamableHTTPTool; from agent_framework.orchestrations import HandoffBuilder; print(inspect.signature(MCPStreamableHTTPTool)); print(inspect.signature(HandoffBuilder.with_autonomous_mode))"
```

Use async context managers for clients/tools and close them reliably. If
`resolve` wraps async code with `asyncio.run`, call it from a normal CLI runner,
not from a notebook's running event loop. Keep the HTTP server separate.

### Step 4 - Observe one practice request before the final batch

Run P01 or another practice request through `resolve` with the trusted envelope:

```powershell
.\.venv\Scripts\python -m route_resolve.lab resolve --id P01 --allow-cloud
```

Expected: one `Result` with the original request ID, valid category/outcome,
meaningful explanation, citations and `simulation: true`. An action ID is
present when the mock operation supplies one. A queued approval may have an
action ID and still be **Route**, not Execute.

Record a trace showing:

1. Triage's handoff destination.
2. The actual policy retrieval references.
3. Actual MCP tool name, arguments and result, or clarification result.
4. How the final outcome follows from that evidence.

Do not log credentials or Authorization headers. Keep mock fixtures local.
An error must remain visible; it is not a successful result.

### Step 5 - Run ten final requests


Use the supplied runner after your practice flow works:

```powershell
.\.venv\Scripts\python -m route_resolve.lab final --allow-cloud
```

Expected: **Wrote 10 results** and `evidence/final-results.jsonl`.
JSONL means one JSON object per line. The runner preserves trusted IDs, requires
the Result contract, checks simulation/citation shape and refuses to overwrite
existing output before calling an agent. To preserve a previous run, pass a
new path such as `--output evidence/final-results-02.jsonl`.

Inspect `starter/route_resolve/lab.py` to understand the checks. This is **not**
an answer-key grader: it does not prove policy correctness, actual handoff,
genuine retrieval or tool execution. The facilitator reviews those traces.

Do not repeatedly run the batch to hide an error. Keep the first failure,
diagnose it, and rerun only the affected request while developing. Preserve
prior results and remember that restarted tool servers lose idempotency records.

### Step 6 - Check one retry and explain a result

With terminal A still running, repeat the same unchanged request ID and action
arguments. Inspect the actual mock response/action ID: no duplicate action
should be created. Reusing an ID with different arguments must be an error,
not an overwrite. This server-level check is distinct from whether the model
happens to produce the same wording twice.

## Optional Copilot prompts

**Guided orchestration support**:

```text
Help me complete challenge 04 in this workshop workspace. Read docs/mission-04.md,
README.md, agents.py, models.py and my existing triage/retrieval code.
First show the control flow, then help implement resolve(request: str) -> Result
incrementally. Parse the trusted JSON envelope {id,user_id,text}; never let its
text override IDs or TEAM_ID. Verify installed Agent Framework signatures.
Use HandoffBuilder, Triage plus three specialists, explicit turn limits and a
termination condition. Use the shared local MCP HTTP server and the exact
specialist allowed_tools from the guide. Preserve actual retrieval evidence,
check MCP errors, and only claim completion from an observed mock result.
Keep credentials in memory, errors visible and every result a simulation.
Do not read coach answers, hardcode final labels, deploy resources, change roles
or create a public tunnel. Explain each change and help me run one practice
request before the final batch. Keep real business systems disconnected.
```

**Coach-style review, without answers**:

```text
Review this redacted trace and my Result. Do not provide an answer key.
Check whether a real handoff, policy retrieval and required MCP call occurred,
whether the citation supports the claim, and whether Route was confused with
Execute. Point to missing evidence rather than inventing it. Ask me to explain
one safety check and one limitation of my implementation.
```

## Checkpoint and three-minute demo

- [ ] All three specialists can be chosen from unstructured requests.
- [ ] A trace proves a real handoff, retrieval and mock call/clarification.
- [ ] Ten final JSONL records pass shape checks and are submitted for coach review.
- [ ] You can distinguish a completed mock action, pending approval and escalation.
- [ ] An unchanged retry does not duplicate the simulated operation.
- [ ] No real grant, order or data transfer occurred.

Show a permitted simulated action, an approval route and a sensitive escalation
from your run. Explain the evidence and one limitation. These are demo categories,
not the expected labels for particular final request IDs.

Then stop terminal A with `Ctrl+C` and stop any running workflow. Do not delete
shared Azure resources. The coach exports console timings and handles cleanup.

## Troubleshooting

| Symptom | What to do |
|---|---|
| Connection refused on port 8000 | Start terminal A with the same `.venv` and assigned team ID |
| Address already in use | Check your own terminal for the existing server; ask coach before stopping anything |
| Workflow repeats handoffs | Check permitted edges, termination and turn bounds; do not increase limits blindly |
| Result is prose or wrong type | Validate the structured output and construct `Result` explicitly |
| Status disappeared after restart | Expected for the in-memory store; keep one process for the retry check |
| Result says Execute without a tool trace | It is not acceptable evidence; fix observation/validation |
| Final run exceeds the timebox | Show the failing step to coach; do not skip safety checks or claim completion |

## Stretch - after the checkpoint

Compare the same request with and without its policy-override sentence. Add an
automated check that a fabricated citation or unobserved action is rejected.
Do not optimize for answer labels at the expense of actual evidence.

## Finished early?

After your core demonstration, choose an [optional bonus mission](docs/bonus.md). This does not add a required console milestone or authorize extra cloud calls.
