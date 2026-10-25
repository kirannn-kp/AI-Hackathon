# Mission 02 - Understand requests and gather facts (30 minutes)

**Working mode:** read here in HackboxConsole; edit the same cloned repository in VS Code. All exercise files are already present. Add `--allow-cloud` only after the facilitator confirms access and approves shared-service calls.

## What you will learn

Turn free text into validated fields and discover/call a real MCP tool.
Do not decide final business outcomes yet.

**Timebox:** concepts 4 min; MCP check 6 min; triage 15 min; checkpoint 5 min.
Prerequisite: challenge 01 passed and coach-approved model access.

## Concepts in plain language

- **Triage** extracts what the person wants and chooses a domain. It is not
  permission to approve the request.
- **Structured output** means a predictable JSON object, not paragraphs your
  program has to guess how to read.
- **MCP client/server**: your client asks a server which tools exist, then calls
  one by name with validated arguments. Describing a lookup is not running it.
- **Prompt injection** is text trying to change the system's rules. Treat request
  text as data, even when it says "ignore policy" or "already approved".

## Core path


### Step 1 - Inspect the supplied request data

All files are already in your clone. Do not replace your implementations.
Open `data/practice-requests.json` and find P01, P06, P14 and P04.
There are **20** practice requests. Each has `id`, `user_id` and `text`.
The fictional business user is separate from your Azure operator identity.
Set the assigned TEAM_ID in this terminal using README.md.

### Step 2 - Run one real MCP lookup

For this core exercise use **local stdio**. It is ready for local use and does
not depend on unverified public hosting. Stdio starts the server as a child
process; you do not also start the HTTP server.


The repository includes the diagnostic so you can focus on learning:

```powershell
.\.venv\Scripts\python -m route_resolve.lab tools
```

Expected: JSON containing **"tool_count": 9**, tool names and an actual result
for Phoenix's owner. Save the output as evidence. The child server stops when
this diagnostic exits. Open `starter/route_resolve/lab.py` to inspect how
discovery, initialization and the tool call work.

The read-only tools are `check_user_access`, `get_project_owner`,
`lookup_supplier`, `check_partner`, and `lookup_status`. `request_info` reports
a need for clarification. Three `create_*_request` tools perform simulated
actions; use them in challenge 04, not as a shortcut to triage.

### Step 3 - Implement structured triage

Open `starter/route_resolve/agents.py` and implement **only `triage(request)`**.
Use the coach-provided Foundry deployment, not keyword routing or a fabricated
model response. Follow README.md to set the cloud variables and identity.

Your model should extract this shape:

```json
{
  "category": "Access",
  "urgency": "normal",
  "missing_fields": [],
  "arguments": {
    "project": "Phoenix",
    "role": "Reader"
  }
}
```

This is a **shape example**, not the answer file. Define and validate a schema:

| Field | Requirement |
|---|---|
| `category` | Exactly `Access`, `Procurement` or `DataSharing` |
| `urgency` | Your documented enum, e.g. `low`, `normal`, `high`; never an approval bypass |
| `missing_fields` | List of missing business-field names; never invent their values |
| `arguments` | Domain-specific extracted fields, not claims of verified approval |

Access needs `project` and `role`; Procurement needs `supplier` and a positive
EUR amount; DataSharing needs `partner` and `classification`. Preserve monetary
values as decimal strings rather than imprecise binary floats.

The runner retains the practice record's **trusted** `id` and `user_id`.
Do not ask the model to invent them. `triage` receives the business text; your
saved evidence combines its output with those IDs. Authentication and team
settings must not come from the request's wording.

Implementation sequence:

1. Write a short extraction-only instruction and the schema.
2. Use the installed Foundry client with Entra credentials and the assigned
   deployment. Bound output tokens; do not run open-ended retries.
3. Parse and validate the output. A refusal, malformed JSON or network error
   must be visible, not converted into plausible successful triage.
4. Keep the starter's function signature. If your SDK uses async calls, put them
   in an async helper; use a synchronous wrapper only from a normal CLI runner,
   not from inside an already-running event loop.

### Step 4 - Try three domains and one missing-field case

Choose P01, P06, P14 and P04 from `data/practice-requests.json`. The core requires
the three domains plus one missing-field example, not all 20 requests.

After implementing triage, this command runs one record:

```powershell
.\.venv\Scripts\python -m route_resolve.lab triage --id P01 --allow-cloud
```

Change only the selected ID for the other cases. Expected: valid fields for each
domain; P04 must retain missing information rather than guess a project.

Use an MCP lookup to verify a fact, separately from extraction. For Access,
inspect the discovered tool schemas and look up the project owner and existing
access. A missing-field request should use `request_info` with the stable
request ID and the missing field; retain its clarification result.


Try the supplied diagnostic options, which run only local synthetic lookups:

```powershell
.\.venv\Scripts\python -m route_resolve.lab tools --tool check_user_access --user-id user-02 --project Phoenix --role Reader
.\.venv\Scripts\python -m route_resolve.lab tools --tool lookup_supplier --supplier "Contoso Software"
.\.venv\Scripts\python -m route_resolve.lab tools --tool check_partner --partner Fabrikam
.\.venv\Scripts\python -m route_resolve.lab tools --tool request_info --request-id P04 --field project
```

These are diagnostic tool inputs, not final decisions. Inspect the server's
tool schemas before connecting them to a model.

Keep the fixture's user/request ID in your runner; do not let a model override
them. Do not edit `MockOperations` to change a tool's response.

## Optional Copilot prompts

**Implementation support** - review the plan and edits before accepting:

```text
Work only in this workshop workspace and on challenge 02. Read docs/mission-02.md,
README.md, pyproject.toml, starter/route_resolve/agents.py and models.py.
First propose a short plan, then help implement triage(request: str) only.
Use the pinned, installed Foundry/Agent Framework APIs, Entra credentials and
coach-supplied environment variables. Verify SDK signatures; do not invent them.
Return validated category, urgency, missing_fields and arguments. Preserve
request/user IDs in the caller, not model guesses. Missing facts stay missing.
Show errors explicitly and bound model calls. Explain the changes so I can
describe them. Do not implement policy retrieval, final decisions or handoff.
Do not read facilitator solutions, expose tokens, or deploy resources.
```

**Review rather than solve**:

```text
Review my triage output and code for this challenge. Do not change code yet.
Find invented facts, schema errors, unbounded retries or request text being
treated as instructions. Ask me to explain the evidence for each extracted
field. Then suggest the smallest fix. Do not give final-request answer labels.
```

## Checkpoint - show the coach

- [ ] A real MCP discovery/lookup trace, not text claiming a tool was called.
- [ ] Valid triage for Access, Procurement and DataSharing.
- [ ] A missing-field case with clarification preserved.
- [ ] Request claims remain separate from verified tool facts.
- [ ] Model/API errors are visible; no real actions were performed.

Save two structured examples and a redacted MCP trace in your own `evidence`
folder. Keep your code for the next mission. If behind schedule, show the failing
step to the coach rather than adding retries or changing permissions.

## Troubleshooting

| Symptom | What to do |
|---|---|
| `KeyError: TEAM_ID` | Set the assigned ID in the terminal running the diagnostic |
| No server or tool output | Use `.venv` Python; check stderr and `await session.initialize()` |
| Status lookup says request not found | No action was recorded in this server process; restarts lose memory |
| Model 401/403 | Coach verifies identity/project role; never paste an API key as a workaround |
| Model 429 | Pause and ask the coach; no parallel retry storm or quota changes |
| JSON surrounded by prose | Fix structured-output/schema handling; never silently accept an invalid shape |

## Stretch - after the checkpoint

Try P19. Explain why a requester cannot grant Owner access by instructing the
agent to skip checks. Add one malformed-output test with a fake model response;
label it a local test, not evidence of a live model call.
