# Mission 01 - Prepare the mission (30 minutes)

**Working mode:** read here in HackboxConsole; edit the same cloned repository in VS Code. All exercise files are already present. Add `--allow-cloud` only after the facilitator confirms access and approves shared-service calls.

## What you will learn

By the end you can explain what an agent does, open the workshop starter, run its
first check and identify your team's approved cloud resources. You do not need to
understand the agent code yet.

**Timebox:** concepts 5 min; local setup 15 min; access check 5 min; checkpoint 5 min.
Read README.md first. All four missions use the same cloned working folder.

## The story

Contoso Manufacturing receives informal requests such as:

> "I join Project Phoenix next week. Please give me Reader access."

A chatbot might write a nice reply. Our system must instead understand the
request, check existing facts, find policy evidence, choose a specialist and
explain what happened. All users, projects, suppliers and actions are fictional.

```text
Employee request -> Triage -> Policy evidence + operational facts
                 -> Access / Procurement / Data Sharing specialist
                 -> Mock tool -> Explained outcome
```

**Agent** = model + instructions + selected tools. **Tool** = a function that
actually runs. **Grounding** = retrieving evidence rather than trusting memory.
You will meet MCP, policy retrieval and handoffs in later challenges.

| Outcome | Meaning | What it must not claim |
|---|---|---|
| Resolve | No new operation is needed | That a new grant or order occurred |
| Execute | A permitted simulated operation completed | That a real system changed |
| Route | More information or approval is needed | That queued means approved |
| Escalate | Security, finance or another specialist must review | That review was bypassed |

## Before you start

The coach supplies your team ID, operator sign-in and resource details. Nominate
one operator to use the lab identity while the team works together. Never share
passwords, change MFA or use another team's identity. VS Code/Python/Azure CLI
must already be installed; tell the coach if they are not.

## Core path


### Step 1 - Clone once, sign in and prepare Python

Follow README.md sections 2-4: clone the facilitator-approved repository, open
it in VS Code, sign in to your approved GitHub/Copilot account and install the
local environment. If setup is already complete, do not recreate it.
Keep the console open for guidance and VS Code open for code.

### Step 2 - Check the local contract

```powershell
.\.venv\Scripts\python -m route_resolve.lab check
```

Expected: **Contracts ready**. Select this folder's `.venv` interpreter.
This checks local imports only, not Azure permissions or model access.

### Step 3 - Explore without implementing

1. Open `starter/route_resolve/models.py`. Find `Result` and its fields.
2. Find `Category` and `Outcome`. Compare them with the story above.
3. Open `starter/route_resolve/agents.py`. Find `triage`, `retrieve_policy`
   and `resolve`. Their `NotImplementedError` messages are deliberate exercises.
4. Do not implement them yet. The MCP server is supplied; you will investigate it in Mission 02.

Expected: you can point to where each of the next three challenges will fit.
`simulation=True` means a fictional result, not permission to touch real systems.

### Step 4 - Verify the operator and assigned project

Only do this after the coach confirms the cloud lab is ready.

1. Follow **Cloud configuration** in README.md using the supplied tenant ID.
2. Confirm the Azure CLI account is your nominated operator.
3. Open `https://ai.azure.com` in a browser signed in as the same operator.
4. Follow the coach's direct project link, or select the assigned Foundry
   resource/project. Portal labels can change; compare identifiers, not icons.
5. Identify the shared chat deployment and your team's Search knowledge-base
   name from the coach's handout. Do not create or deploy anything.

Expected: access to the assigned project. A successful Microsoft sign-in alone
does not prove model or Search permissions. Tell the coach if the project is
missing; do not grant yourself roles or reuse another project.

If cloud resources are not ready, complete steps 1-3 and label step 4 **blocked**.
Do not report this as cloud-ready or continue cloud exercises without approval.

## Optional Copilot prompts

You may work without Copilot. These are helpers, not extra mandatory work.

**Understand before editing** - use explanation/read-only mode:

```text
I am new to AI agents and this is a synthetic beginner lab. Read only README.md,
docs/mission-01.md and starter/route_resolve/models.py in this workshop workspace.
Do not edit files or run commands. Explain an agent, a tool, grounding and
handoff using our request-processing story. Compare Resolve, Execute, Route
and Escalate. Then ask me two short questions to check understanding.
Do not read coach solutions or other workspaces.
```

**Fix a setup error** - attach only a redacted error:

```text
Help me diagnose the setup error below, one step at a time. First verify my
working folder and selected Python environment. Do not change execution policy,
install global packages, deploy Azure resources, or request passwords/tokens.
Explain any proposed command before asking me to run it. Stay within this
workshop workspace and the installed dependency versions.
[Paste the non-secret error and the command that failed.]
```

## Checkpoint - show the coach

- [ ] `Contracts ready` appears in your terminal.
- [ ] Your team can explain the four outcomes in its own words.
- [ ] You found the three deliberately unfinished functions.
- [ ] Project access is confirmed, or explicitly recorded as blocked.
- [ ] No real grants, purchases, sharing actions or new Azure resources occurred.

Save a short note with your team ID and completed checks. No passwords, TAPs,
tokens or credentials in screenshots. Ask the facilitator to approve this checkpoint, then open Mission 02 in the console.

## Troubleshooting

| Symptom | What to do |
|---|---|
| `python` missing/older than 3.12 | Ask the coach to select the prepared interpreter |
| `No module named route_resolve` | Install from the folder containing `pyproject.toml`; use `.venv` Python |
| `NotImplementedError` when calling an agent | Expected now; only import contracts at this checkpoint |
| Project missing or 401/403 | Check account/tenant, then coach checks permissions; never add Owner |
| Copilot unavailable | Continue manually or pair with a teammate; it is optional |

## Stretch - only after the checkpoint

Draw the request flow. Mark which facts come from the requester, which from a
tool and which from policy. Explain why "the model said approved" is not evidence.
