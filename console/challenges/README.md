# Mission: Route & Resolve

## Your team is the engineering team

An employee asks for access. A buyer requests software. A colleague wants to
share a dataset. The requests look simple, but the right response depends on
policy, existing facts and approval authority.

Your mission is to build an evidence-driven AI workflow that understands the
request, selects a specialist and reports what can happen next. This is a
professional hands-on workshop using a **fictional manufacturing case study**.
No real customer data or business systems are connected.

**Where to read:** open your facilitator's HackboxConsole link, sign in, and
start on its workshop home page. Read each mission there while editing this
repository in VS Code. The same guides are under [docs/](docs/START_HERE.md)
for reference. This repository is the working codebase, not a replacement for
the guided console experience.

## 1. Read the mission before coding

- [Mission briefing and definition of success](docs/START_HERE.md)
- [Architecture and component responsibilities](docs/architecture.md)
- [Optional bonus missions for early finishers](docs/bonus.md)
- Four missions, one working folder, approximately **150 minutes**.
- All exercise materials are available from the initial clone. Console
  milestones pace the workshop; they do not make repository files secret.
- Agent implementations are deliberately unfinished. You will build them.
  Facilitator answers and the answer-key grader are not included.

## 2. Clone once and open VS Code

Before the workshop, install Git, VS Code, Python 3.12+ and Azure CLI, or use the
facilitator's prepared workstation. Docker is not required.

The repository URL will be supplied after the customer review/publishing step.
There is no published remote configured in this local review copy.

For the organizer's local review, this is also a standalone Git repository
named `route-resolve-workshop`, with a `main` branch and no remote. You can clone
its local path into a different working directory; no GitHub publication is needed:

```powershell
git clone "C:\Github Repo\route-resolve-workshop" "$env:TEMP\route-resolve-team-review"
```

Use a fresh target folder and open that clone in VS Code. This organizer-only
path is not the address customers will receive after publishing.

```powershell
$repositoryUrl = Read-Host "Paste the workshop Git repository URL supplied by your facilitator"
git clone $repositoryUrl route-resolve-workshop
cd route-resolve-workshop
code .
```

Expected: VS Code opens the folder containing this README and `pyproject.toml`.
Keep this same folder for all four missions. Do not download replacement source
folders, overwrite your work, or clone the private facilitator repository.

## 3. Sign in to GitHub Copilot

1. In VS Code open the **Accounts** menu and sign in to your approved GitHub
   account. If prompted, complete the browser authorization and return to VS Code.
2. Open **Chat** and choose GitHub Copilot. Follow the setup/sign-in prompt if
   it appears; interface labels can vary by VS Code version.
3. Confirm this account has Copilot access. An Azure training identity or TAP
   does **not** automatically provide a GitHub account or Copilot license.
4. Try the following in explanation/read-only mode:

```text
I am joining this workshop. Read README.md and docs/START_HERE.md in this
workspace only. Do not edit files or run commands. Explain the business problem,
the architecture and my first task in simple terms. Ask me one question to
check understanding. Do not look for facilitator solutions.
```

Expected: an explanation of this case study, not a deployment proposal.
Copilot is optional. If it is unavailable, pair with your team or ask the
facilitator; the guides contain the steps without requiring Copilot.

For coding prompts, ask for a plan first and review edits/terminal commands.
Never paste passwords, TAPs, keys, tokens or real customer information into chat.

## 4. Prepare the local Python environment

In a VS Code PowerShell terminal, from this repository root:

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\python -m pip install -e ".[mcp,cloud]"
.\.venv\Scripts\python -m route_resolve.lab check
```

Expected: Python 3.12+ and **Contracts ready**. The check does not call a model.
Select **Python: Select Interpreter** in the command palette and select this
folder's `.venv`. Using the explicit executable avoids activation-policy changes.
The functions in `starter/route_resolve/agents.py` remain unfinished on purpose.

On a facilitator-supported macOS/Linux machine, create the environment with
`python3` and replace `.\.venv\Scripts\python` with `.venv/bin/python`.

## 5. Cloud configuration: a separate identity

You have three separate sign-ins:

| Sign-in | Purpose |
|---|---|
| HackboxConsole team login | Read missions, see credentials and obtain milestone approval |
| Your approved GitHub account | Access this code repository and optional Copilot |
| Facilitator-provided Entra identity | Access the assigned Azure/Foundry lab |

Do not reuse or share passwords between them. One nominated operator uses the
team's Azure identity while teammates collaborate.

Only continue when the facilitator confirms resources and permissions are ready:

```powershell
$tenantId = Read-Host "Paste the facilitator-provided tenant ID"
az login --tenant $tenantId --allow-no-subscriptions
az account show --query user.name --output tsv
$env:TEAM_ID = Read-Host "Enter the assigned team ID, for example team-01"
$env:FOUNDRY_PROJECT_ENDPOINT = Read-Host "Paste the assigned Foundry project endpoint"
$env:FOUNDRY_MODEL = Read-Host "Paste the shared chat deployment name"
$env:SEARCH_ENDPOINT = Read-Host "Paste the assigned HTTPS Search endpoint"
$env:TEAM_KNOWLEDGE_BASE = Read-Host "Paste the assigned knowledge-base name"
```

Expected: your assigned operator identity, not a personal account. A successful
sign-in alone does not prove resource access; the facilitator verifies it.
Variables apply to this terminal. A new terminal needs its own assignments.

The root `.env.example` documents the variable names. It does **not** load
automatically. If you use a local `.env`, keep it out of Git and load it
explicitly in your code. Never print tokens to prove authentication.

All runner commands that could invoke shared cloud services require an explicit
`--allow-cloud` flag. Add it only after facilitator approval. A budget alert or
rate limit is not a spending cap.

## 6. Follow the missions in the console

| Mission | You build | Time | Local guide |
|---|---|---:|---|
| 01 - Establish the base | Explain the flow and verify your setup | 30 min | [Mission 01](docs/mission-01.md) |
| 02 - Investigate the request | Structured triage and operational fact lookup | 30 min | [Mission 02](docs/mission-02.md) |
| 03 - Find the evidence | Policy retrieval and faithful citations | 45 min | [Mission 03](docs/mission-03.md) |
| 04 - Route and resolve | Bounded specialist handoff and simulated actions | 45 min | [Mission 04](docs/mission-04.md) |

For each mission: read the story, understand the concept, follow the numbered
steps, run the check, explain the evidence and ask for facilitator approval.
Optional Copilot prompts and stretch tasks are in each guide. You do not need
to complete stretch tasks to finish the core workshop.

Finished early? Choose one [bonus mission](docs/bonus.md): failure-path testing,
evidence challenges or an offline evaluation report. Each takes approximately
20-30 extra minutes. They do not add a fifth required console milestone.

## Definition of done

- Ten final request results with the required shape and `simulation: true`.
- Actual traces for handoff, retrieval and required mock tool calls.
- No fabricated approvals, citations or successful actions.
- A three-minute team demonstration of a completed mock action, an approval
  route, a sensitive escalation and one limitation.
- No real access grant, purchase or data transfer.

The runner checks structure, not business correctness. Facilitator review is
still needed. Keep evidence local and free of credentials.

## Local customer review

Open `index.html` for a self-contained preview of the story and mission content.
It is a **review preview**, not another deployed workshop platform or an
authentication/approval system. Production guidance is intended for HackboxConsole.
No GitHub remote, live console address or customer resource configuration is
included in this local review copy.

The reader uses a **MOAW-style learning flow**: a section outline, topic links,
timeboxes and Previous/Next reading navigation. It is not the MOAW framework.
Reading position is not a completion score; HackboxConsole owns coach approvals.

## Repository checks and contribution workflow

Use a feature branch for your implementation, keep credentials out of commits,
and review changes before merging. Do not edit the supplied operational rules
to manufacture a successful result.

```powershell
git switch -c team/my-implementation
.\.venv\Scripts\python -m unittest discover -s tests -v
git status --short
```

The public tests check fixtures, contracts and local tool registration, not
hidden answer labels or live Azure access. They do not require completed agents.
Add tests for your implementation as you progress.

The included GitHub Actions workflow runs offline checks only if this repository
is later hosted on GitHub. It does not deploy infrastructure or use Azure secrets.
It has not been run on GitHub during this local review.

Maintainers can rebuild the review page and console import files:

```powershell
.\.venv\Scripts\python -m pip install -e ".[authoring]"
.\.venv\Scripts\python scripts\build_workshop.py
```

`console/challenges` contains the workshop home, four console mission files and
supporting documents. Use the console's source-directory import; this repository
does not provision Azure resources or contain coach solutions.

## Attribution and safe use

Adapted from Microsoft's MIT-licensed Fraud Intelligence MicroHack, revision
`3a3c15c9119b9b926c897a17332783c6dc055e3c`.
See [LICENSE](LICENSE) and the
[upstream MicroHack](https://github.com/microsoft/MicroHack/tree/main/03-Azure/01-04-AI/07_Fraud_Intelligence).
All organizations, requests, policies and operational actions in the case study
are fictional. Do not run deployment commands or change subscription roles.
