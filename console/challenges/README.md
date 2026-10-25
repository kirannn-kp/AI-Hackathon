# AI Hackathon - Mission: Route & Resolve

Build an evidence-driven request assistant for fictional Contoso Manufacturing.
Start with one triage agent, add operational tools and policy evidence, then
connect specialists into a bounded workflow. All data and actions are synthetic.

**Read in HackboxConsole; edit and run in VS Code.** This repository contains
your exercise code, not the console platform. Keep the same clone for all four
missions. [Read the full story](docs/START_HERE.md).

## 1. Before you type commands

The coordinators supply your console login, approved workshop source, team ID,
Azure operator/tenant, direct Foundry project link, project endpoint, shared
chat deployment, Search endpoint and team knowledge-base name.
Do not use another team's values or a personal Azure project.

| You sign into | Why | Where |
|---|---|---|
| HackboxConsole with your team login | Read missions and see team progress | Browser |
| Your approved GitHub account | Clone the approved repository; optional Copilot | Git / VS Code |
| The assigned Azure operator identity | Call the lab's Foundry/Search services | Azure CLI and Foundry browser |

One nominated operator uses the Azure lab identity while the team collaborates.
Do not share passwords, TAPs or MFA. GitHub/Copilot access is not automatically
included with an Azure training identity. Copilot is optional.

Use a prepared workstation or install Git, VS Code, Python 3.12+ and Azure CLI
before the timed workshop. Docker is not required. Ask the coordinators if a
prerequisite is missing.

## 2. Clone once, open VS Code, then open a terminal

**Participant repository:** https://github.com/kirannn-kp/AI-Hackathon
This public repository contains the unsolved workshop starter and synthetic data,
not private coordinator implementations or Azure credentials.

If the folder is already prepared, skip cloning. Otherwise, in PowerShell:

```powershell
git clone https://github.com/kirannn-kp/AI-Hackathon.git
cd AI-Hackathon
code .
```

For an approved extracted folder, use VS Code **File > Open Folder** instead.
Do not clone a ZIP file. In VS Code use **Terminal > New Terminal** and select
PowerShell. Check that it is at the workshop root:

```powershell
Get-Location
Get-ChildItem README.md, pyproject.toml
```

**Expected:** the Explorer shows `README.md`, `pyproject.toml`, `starter`, `data`
and `tests`. Stay in this same folder through Mission 04 and optional bonus tasks.

## 3. Optional: sign in to Copilot for explanations and coding help

1. Use VS Code's **Accounts** menu to sign in to your approved GitHub account.
2. Open Chat and follow the Copilot sign-in/setup prompt if needed.
3. Ask it to explain this workspace before letting it edit:

```text
Read README.md and docs/START_HERE.md in this workspace only. Do not edit files,
run commands or search for private answers. Explain the story, what my first
triage agent does, and the first three setup actions in simple words.
```

**Expected:** an explanation, not a deployment proposal. If Copilot is unavailable,
continue with your team and the numbered mission steps. Never paste credentials,
real business data or customer documents into chat.

## 4. Prepare Python and check local imports

Skip creating/installing again if this same environment is already prepared:

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\python -m pip install -e ".[mcp,cloud]"
.\.venv\Scripts\python -m route_resolve.lab check
```

**Expected:** Python 3.12+ and **Contracts ready**. Use **Ctrl+Shift+P > Python:
Select Interpreter** to select this folder's `.venv`. Explicit executable paths
avoid activation-policy changes. This check does not call a model or prove Azure
access; the three agent functions are deliberately unfinished.

On a coordinator-supported macOS/Linux workstation use `python3` and replace
`.\.venv\Scripts\python` with `.venv/bin/python`.

## 5. Sign in to Azure and identify your existing Foundry project

First check the cached account:

```powershell
az account show --query "{operator:user.name,tenant:tenantId}" --output json
```

If it is already the assigned operator/tenant, reuse it. Otherwise:

```powershell
$tenantId = Read-Host "Azure tenant ID from the coordinators"
az login --tenant $tenantId --allow-no-subscriptions --use-device-code
az account show --query "{operator:user.name,tenant:tenantId}" --output json
```

Open the coordinator's direct project link or [Microsoft Foundry](https://ai.azure.com/)
as that same operator. Match the assigned project name, then locate its
**Project endpoint** and the existing chat deployment. A browser page URL is
not an SDK endpoint; a model family name is not necessarily a deployment name.

Portal labels and visibility vary. If a listing is absent, use verified handout
values and ask the coordinators; do not create resources or broaden permissions.
[Learn about project endpoints](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview).

## 6. Set configuration in the terminal that runs your code

```powershell
$env:TEAM_ID = Read-Host "Assigned team ID"
$env:FOUNDRY_PROJECT_ENDPOINT = Read-Host "Assigned Foundry project endpoint"
$env:FOUNDRY_MODEL = Read-Host "Shared chat deployment name"
$env:SEARCH_ENDPOINT = Read-Host "Assigned HTTPS Search endpoint"
$env:TEAM_KNOWLEDGE_BASE = Read-Host "Assigned team knowledge-base name"
```

These values apply to this terminal only. A second terminal needs its own
assignments. `.env.example` documents the names but is **not automatically loaded**.
Keep any local `.env` out of Git. Use the assigned CLI identity in your adapters
and never print access tokens. A successful login is not proof of model/retrieval
authorization; the real mission calls test those permissions.

Commands that can invoke shared services require `--allow-cloud`. Add it only
with coordinator approval. Budget alerts/rate limits are not spending caps.

## 7. Build in order - do not implement everything at once

| Mission | Edit/build | Check | Guide |
|---|---|---|---|
| 01 / 30 min | Your first model-backed `triage` agent | One real P01 triage result | [Mission 01](docs/mission-01.md) |
| 02 / 30 min | MCP fact lookup; improve triage | Nine tools, three domains, missing fields | [Mission 02](docs/mission-02.md) |
| 03 / 45 min | `retrieve_policy` adapter | Real passages and references | [Mission 03](docs/mission-03.md) |
| 04 / 45 min | `resolve` specialist workflow | Ten Results and an evidence-based demo | [Mission 04](docs/mission-04.md) |
| Optional / 20-30 min each | Resilience, evidence challenges or evaluation | Offline bonus evidence | [Bonus missions](docs/bonus.md) |

Read the purpose, perform the numbered action, compare its expected result, then
show the coordinators at the checkpoint. The console's **Optional bonus missions**
button stays available after Challenge 4. Bonus is not a fifth required milestone.

### Files you will work with

| Path | Responsibility |
|---|---|
| `starter/route_resolve/agents.py` | Your three unfinished agent functions |
| `starter/route_resolve/models.py` | Supplied Result/category/outcome contract |
| `starter/route_resolve/tools.py` | Supplied synthetic operational rules; do not bypass |
| `starter/route_resolve/mcp_server.py` | Supplied nine-tool MCP server |
| `starter/route_resolve/lab.py` | Diagnostics and CLI runners, not agent solutions |
| `data/practice-requests.json` | Twenty development requests with trusted IDs |
| `data/policies` | Four fictional policies, also loaded into the assigned knowledge base |
| `data/final-requests.json` | Ten final requests, without answer labels |

## Definition of done

Ten saved Results with required fields and `simulation: true`, genuine retrieval
references, actual handoff/tool traces and a three-minute team demonstration.
Show a mock action, an approval route, an escalation and one limitation.
The runner checks shape, not business correctness; coordinators review evidence.

## Local checks and rebuilding documentation

```powershell
git switch -c team/my-implementation
.\.venv\Scripts\python -m unittest discover -s tests -v
git status --short
```

The supplied offline tests do not require solved agents or Azure. Add your own
tests as you implement. No answer-key grader or private implementations are
included. The GitHub Actions workflow is offline-only and has not run on GitHub
until a GitHub run is independently verified.

Maintainers can rebuild the local review and console content without deployment:

```powershell
.\.venv\Scripts\python -m pip install -e ".[authoring]"
.\.venv\Scripts\python scripts\build_workshop.py
```

`index.html` is a local review reader, not an authentication/progress system.
`console/challenges` is the import for the hosted console: four core missions
plus supporting documents including the optional bonus guide.
The hosted console retains its original colourful Hackbox styling.

## Attribution and safe use

Adapted from Microsoft's MIT-licensed Fraud Intelligence MicroHack, revision
`3a3c15c9119b9b926c897a17332783c6dc055e3c`.
See the supplied `LICENSE`, the [upstream licence](https://github.com/microsoft/MicroHack/blob/main/LICENSE), and the
[upstream MicroHack](https://github.com/microsoft/MicroHack/tree/main/03-Azure/01-04-AI/07_Fraud_Intelligence).
All organizations, requests, policies and operational actions are fictional.
Do not deploy resources, change roles or delete shared services.
