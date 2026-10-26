# Mission 01 - From a Foundry prompt to Python triage (40 minutes)

## What you are going to do

Try a request in Foundry, read how an agent is constructed, then implement the
first small part of your Python application with GitHub Copilot.

**You finish with:** a real model-backed `triage` result, a before/after prompt
comparison and an explanation of the agent construction code.
**You learn:** instructions, identity, a model client and output validation have
different jobs. Classification is not business authorization.

**Where:** Foundry and VS Code, in your single workshop clone.
**Why:** the playground helps you discover behaviour; code makes it repeatable.
Complete [workstation setup](code-extension/setup.md) before the three-hour timer.

## Step 1 - Predict, then send a first prompt (5 minutes)

Open your assigned project in [Microsoft Foundry](https://ai.azure.com/).
Choose **Test in playground**, or **View deployments > route-resolve-chat**.
If a shortcut is disabled, use the normal deployment route; never force a control.
Remove automatically attached Web search for this exercise.

Open `data/practice-requests.json` in VS Code and find P01. Predict its category
and missing fields. Send its exact `text` to the model. Press **Send** and keep
the actual response. Add a system message / instructions asking for the category,
supplied facts and missing facts, then repeat the same input.

**You should see:** an actual before/after comparison, not necessarily an improvement.
**What you learn:** a helpful paragraph is not yet a structured application result.

## Step 2 - Read the creation code; do not edit it (5 minutes)

Open [examples/agent_blueprint.py](../examples/agent_blueprint.py) in VS Code.
Use **Ctrl+F** to locate `FoundryChatClient`, then `client.as_agent`.
Read it only: do not run it as a deployment script or change the example.

| Code to point at | Explain to your teammate |
|---|---|
| `AzureCliCredential()` | Which signed-in identity obtains the token? |
| `project_endpoint` | Which existing team workspace does this address? |
| `model` | Which deployment answers the request? |
| `client.as_agent(...)` | Where do name and reusable instructions become a local agent object? |
| `return agent, client` | Why has construction alone neither sent a prompt nor created a portal agent? |

This is local Agent Framework construction, **not** the implementation behind
Foundry's Save as agent button. The two configurations do not synchronize.
The example deliberately omits execution, tools and the triage solution.

**You should see:** the construction call and no invocation in this example.
**What you learn:** creating an object, invoking a model and saving a remote agent
are separate operations.

## Step 3 - Implement only triage (20 minutes)

Open `starter/route_resolve/agents.py`. Edit only `triage(request)` and helpers
you need for it. Leave `retrieve_policy` and `resolve` alone for now.
Read `models.py` and `lab.py` without editing them; the supplied runner retains
trusted request/user IDs. It does not implement your agent.

1. Define the instruction and a structured schema: `category` must be `Access`,
   `Procurement` or `DataSharing`; `urgency` is a documented enum;
   `missing_fields` is a list; `arguments` holds extracted business fields.
2. Use the existing Foundry deployment and your CLI identity. Inspect the
   installed SDK signatures; do not ask Copilot to upgrade dependencies.
3. Make one bounded model call and parse/validate its real response.
4. Missing values stay missing. Invalid JSON, refusal, authentication errors and
   timeouts must remain explicit errors, not hard-coded successful answers.

Use [the detailed triage recipe](code-extension/mission-01.md)
only for extra help. Do not complete its other missions now.

**You should see:** a small implementation replacing the deliberate triage stub.
**What you learn:** Copilot helps implement code; you own its contract and errors.

## Step 4 - Run the application (5 minutes)

After coordinator approval for cloud calls, run in the configured terminal:

```powershell
.\.venv\Scripts\python -m route_resolve.lab triage --id P01 --allow-cloud
```

Compare its fields with P01, not with an answer key. Point to the client call
in your own function. Ask which output came from the model and which IDs came
from the runner. A `NotImplementedError` means the exercise is unfinished.

**You should see:** real JSON from your implementation; not an access grant.
**What you learn:** a Python invocation uses the service outside the playground.

## Step 5 - Explain and hand over (5 minutes)

Rotate driver and reviewer. Explain one changed instruction and one validation
check without Copilot. Record a redacted error if blocked; ask the coordinator
at the end of the timebox instead of making repeated calls.

**You should see:** code, a run and a human explanation.
**What you learn:** understanding an AI-generated change is part of engineering.

## Checkpoint - show the coordinators

- [ ] Locate `client.as_agent` in the read-only example and your actual model call.
- [ ] Show the prompt before/after and one live Python P01 result.
- [ ] Explain why category and urgency do not authorize an action.

## Optional Copilot prompts

```text
Read examples/agent_blueprint.py without editing it. Explain client.as_agent.
Then help me implement only triage in starter/route_resolve/agents.py using the
installed SDK. Propose the schema first, explain changes, preserve visible
errors and do not implement retrieval/resolve or invent evidence.
```

## Troubleshooting

| Problem | Next step |
|---|---|
| Missing clone, interpreter or identity | Return to setup with a coordinator; do not borrow credentials |
| Playground or Python 401/403 | Check the exact identity/project, not broader roles |
| `Please give me access.` produces invented details | Test missing fields; do not fill them silently |
| Unexpected SDK parameter | Inspect the installed signature; no speculative upgrades |
| Timebox expires | Preserve work and ask for help; do not mark the code checkpoint passed |

Next: [Mission 02](mission-02.md).

Reference: [Agent Framework structured outputs](https://learn.microsoft.com/en-us/agent-framework/agents/structured-outputs).
