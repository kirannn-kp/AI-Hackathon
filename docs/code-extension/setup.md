# Python workstation checklist - complete before the three-hour core

This is setup for the mixed Foundry/Python core, not a fifth challenge. The
unfinished functions are deliberate exercises. During the core implement
`triage` and `retrieve_policy`; leave `resolve` for the after-core stretch.

## Clone and install

In PowerShell, with your own approved GitHub account:

```powershell
git clone https://github.com/kirannn-kp/AI-Hackathon.git
cd AI-Hackathon
code .
```

If the clone already exists, open that folder instead. In VS Code, open a
PowerShell terminal at the folder containing `pyproject.toml`.
Git, VS Code, Python 3.12+ and Azure CLI must be installed through an approved
workstation procedure. Docker is not required.

```powershell
python --version
az version
python -m venv .venv
.\.venv\Scripts\python -m pip install -e ".[mcp,cloud]"
.\.venv\Scripts\python -m route_resolve.lab check
```

Expected: **Contracts ready**. This checks local imports, not agent behavior or
Azure access. Select this folder's `.venv` in VS Code's Python interpreter picker.
Explicit executable paths avoid activation/execution-policy changes.

## Verify your own CLI identity

Your portal sign-in does not automatically sign in the CLI. Reuse the cached
account if it is your approved workshop identity and tenant:

```powershell
az account show --query "{account:user.name,tenant:tenantId}" --output json
```

Otherwise use the coordinator-supplied tenant:

For this workshop, the tenant ID is
`c6670b79-8a8a-472a-8d88-728245ab89e1`. Enter this value below; use your
assigned Azure account when the device-code page asks you to sign in.

```powershell
$tenantId = Read-Host "Workshop tenant ID"
az login --tenant $tenantId --allow-no-subscriptions --use-device-code
```

Never borrow a teammate's login or print/share tokens.

## Configure this terminal

Use your assigned team ID and these prepared event values, not the browser
address or another team's project. The remaining names are derived from your
team; you do not need to ask a coordinator to find them.

```powershell
$env:TEAM_ID = Read-Host "Assigned team ID (team-01 to team-08)"
if ($env:TEAM_ID -notmatch '^team-0[1-8]$') { throw "Enter your assigned team-01 to team-08." }
$env:FOUNDRY_PROJECT_ENDPOINT = "https://bosch-rnr-tcek5ldad64oc.services.ai.azure.com/api/projects/$($env:TEAM_ID)"
$env:FOUNDRY_MODEL = "route-resolve-chat"
$env:SEARCH_ENDPOINT = "https://bosch-rnr-search-tcek5ldad64oc.search.windows.net"
$env:TEAM_KNOWLEDGE_BASE = "$($env:TEAM_ID)-policy-kb"
```

These values apply only to this terminal. `.env.example` is documentation, not an
automatically loaded file. A new terminal needs configuration again.
Cloud calls require coordinator approval and the runner's `--allow-cloud` flag.

## Verify before starting the timer

Run the supplied offline tests:

```powershell
.\.venv\Scripts\python -m unittest discover -s tests -v
```

Ask the coordinator to verify your individual model and Search retrieval access.
The project managed identity's policy role does not apply to your CLI user.
Do not discover missing permissions halfway through the timed core.

## Core versus detailed recipes

Return to [Mission 01](../mission-01.md) once ready. The main four missions define
the 180-minute scope. The detailed recipes below supply implementation help;
do not complete the full advanced workflow inside the core.

1. [Code extension 01](mission-01.md): implement model-backed `triage`.
2. [Code extension 02](mission-02.md): inspect MCP facts and improve triage.
3. [Code extension 03](mission-03.md): implement real policy retrieval.
4. [Code extension 04](mission-04.md): implement bounded specialist handoff.

The local MCP server binds to your own laptop. It is not the remote tool
connection used by a Foundry-hosted agent, and its state is not shared between
teammates. Do not expose it publicly. Keep all evidence synthetic and redacted.
