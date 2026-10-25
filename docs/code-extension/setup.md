# Optional Python track - prepare your own workstation

Finish the [Foundry portal introduction](../mission-01.md) first. This advanced
track is for participants who want to implement the workflow in code after the
core lab. The three unfinished functions are deliberate exercises, not a working
agent you can run without implementing them.

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

```powershell
$tenantId = Read-Host "Workshop tenant ID"
az login --tenant $tenantId --allow-no-subscriptions --use-device-code
```

Never borrow a teammate's login or print/share tokens.

## Configure this terminal

Use coordinator-supplied values, not the browser address or another team's project:

```powershell
$env:TEAM_ID = Read-Host "Assigned team ID"
$env:FOUNDRY_PROJECT_ENDPOINT = Read-Host "Assigned project endpoint"
$env:FOUNDRY_MODEL = Read-Host "Assigned chat deployment name"
$env:SEARCH_ENDPOINT = Read-Host "Assigned HTTPS Search endpoint"
$env:TEAM_KNOWLEDGE_BASE = Read-Host "Assigned team knowledge-base name"
```

These values apply only to this terminal. `.env.example` is documentation, not an
automatically loaded file. A new terminal needs configuration again.
Cloud calls require coordinator approval and the runner's `--allow-cloud` flag.

## Build in order

1. [Code extension 01](mission-01.md): implement model-backed `triage`.
2. [Code extension 02](mission-02.md): inspect MCP facts and improve triage.
3. [Code extension 03](mission-03.md): implement real policy retrieval.
4. [Code extension 04](mission-04.md): implement bounded specialist handoff.

The local MCP server binds to your own laptop. It is not the remote tool
connection used by a Foundry-hosted agent, and its state is not shared between
teammates. Do not expose it publicly. Keep all evidence synthetic and redacted.
