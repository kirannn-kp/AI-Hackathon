# Bonus missions - engineering beyond the happy path

**Optional, after the four core missions.** Choose one task that interests your
team; these are not extra mandatory milestones and do not change the 150-minute
core. Ask the facilitator before continuing if your core demonstration is not
complete. There are no bonus answer keys in this repository.

Work in the same clone. Start with offline tests and test doubles. No additional
Azure deployment, broader permissions, public MCP tunnel or real business data.
Any extra live model/retrieval calls require separate facilitator approval.

## Bonus 1 - Make failure safe (20-30 minutes)

### The situation

Your prototype works when every dependency behaves. What happens when retrieval
times out, a tool returns an error, or a retry carries different arguments?
Your task is to prove that the workflow does not turn failure into a plausible
success.

### Your task

1. Create `tests/test_workflow_resilience.py` using `unittest` and local test
   doubles. Read the existing public tests for test structure, not an agent
   implementation.
2. Add at least **five** cases from this table:

| Injected condition | Required observation |
|---|---|
| Retrieval timeout | Error is visible; no mock write is called |
| Retrieval returns no references | Unsupported execution is blocked |
| MCP response has `isError: true` | It cannot become a successful Execute result |
| Model output is malformed or has an unknown category | Validation rejects it |
| Same request ID and unchanged arguments on the same server | Same action record, no duplicate |
| Same request ID but changed action arguments | Explicit conflict, no overwrite |
| Workflow exceeds its turn limit | It stops rather than silently increasing the limit |

3. Make each test fail for the right reason before fixing your implementation.
   Use your existing adapters; do not weaken `MockOperations` rules to pass.
4. Record which dependency is fake and which behavior is actually under test.

```powershell
.\.venv\Scripts\python -m unittest discover -s tests -p test_workflow_resilience.py -v
```

**Success:** five or more meaningful tests pass, and you can show one failing
test from before the fix. Offline doubles do not prove live service reliability.
Idempotency here applies to one retained local server process, not across restarts.

### Optional Copilot prompt

```text
Help me test my existing workflow without solving the workshop. Read
docs/bonus.md and my implementation. Propose five failure-path tests using
unittest and local doubles, with no network calls. For each, state the dependency
being replaced and the assertion that prevents a false success. Do not weaken
tool rules, fabricate live traces or change the expected behavior to match a bug.
Ask me to approve the test plan before editing.
```

## Bonus 2 - Challenge the evidence (20-30 minutes)

### The situation

A requester insists that an operation is already approved, and a retrieved
passage contains text that looks like an instruction. Can your workflow keep
business evidence separate from instructions?

### Your task

1. Write **six new synthetic cases**, two per specialist. Do not reuse final
   request IDs or search for facilitator answer labels.
2. Include a missing field, a claimed approval and an instruction-like sentence
   in either request text or a fake retrieved passage. Keep them fictional.
3. Run your own cases against controlled local model/retrieval doubles first.
   Mark those traces **offline test evidence**, not real model or Search output.
4. For each case, preserve the trusted input ID and compare the request claim,
   retrieved evidence, observed tool result and final explanation.
5. If the facilitator approves a live check, agree a small limit first: no more
   than **three end-to-end requests**, bounded turns and no automatic retries.
   Use only assigned shared resources.

**Success:** all six offline cases retain trusted IDs; none claims a completed
action without an observed permitted mock result; missing evidence remains
visible. Explain one case where a fluent response would have been misleading.
The facilitator reviews business correctness; your tests are not a new answer key.

### Optional Copilot prompt

```text
Act as a test designer for my fictional workflow. Suggest six new synthetic
cases across Access, Procurement and DataSharing, including missing information
and unverified approval claims. Do not give final-fixture answers. Help me define
evidence-based assertions and distinguish a controlled test from a live trace.
Do not run cloud calls or alter permissions.
```

## Bonus 3 - Build a repeatable evaluation report (20-25 minutes)

### The situation

Another engineering team needs to understand whether your changes improved
reliability. A screenshot of one good answer is not enough.

### Your task

1. Create `scripts/evaluate.py` to read a **saved** JSONL run and redacted trace
   records. It must not call a model, retrieval endpoint or action tool.
2. Report:
   - Record count and distinct request IDs.
   - Missing/invalid Result fields and missing simulation flags.
   - Which records have retrieval and tool evidence, and which do not.
   - Unfinished/error records, not just successful cases.
   - Elapsed time and token usage **only when measured and present**.
3. Write a machine-readable report under `evidence`. Refuse to overwrite an
   existing report unless the user explicitly selects a new output path.
4. Test with a valid record, a duplicate ID, missing citations and missing trace
   evidence. Include at least **four** offline test cases.
5. Explain why matching a tool name in model-written text does not prove that
   the tool ran. Correlate actual trace records with trusted request IDs.

**Success:** repeatable offline results, four tests and no invented timing,
token counts or monetary costs. Label evidence availability separately from
business-policy correctness.

### Optional Copilot prompt

```text
Help me design an offline evaluation script for saved JSONL and actual redacted
trace records. No network calls, model-based grading or business answer keys.
Start with the input schema and four failing tests. Do not invent missing
telemetry or count a model's claim as proof of tool execution. Preserve previous
reports and explain every metric's limitation.
```

## Bonus demonstration

Show the facilitator the problem, your change, reproducible evidence and one
remaining limitation. A bonus is successful when the team understands and can
defend the improvement, not when it adds the most services.

Stop your local servers when finished. Do not delete shared cloud resources.
