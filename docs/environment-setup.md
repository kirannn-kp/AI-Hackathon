# Environment Setup - start here before the challenges

Keep this page open beside VS Code. Follow these steps at your own pace, even
when the presentation moves on. Setup is preparation, not a scored challenge;
opening this page does not start your team's challenge timer.

**Your route:** nominate an operator -> submit the access form -> join GitHub ->
open the private starter -> prepare Python -> verify Azure access -> Mission 01.

## 1. Know which account to use

| Account | What it is for | What to use |
|---|---|---|
| Console team login | This setup page, challenges and team progress | Team username/password delivered privately by coordinators |
| GitHub | Join the workshop organization, access the starter and optional Copilot | Your personal GitHub account, as directed on the joining image below |
| Azure / Foundry | Run model and policy-retrieval calls | Your nominated operator's approved Bosch work account after its workshop invitation is accepted, or an explicitly assigned training account |

These are separate sign-ins. Joining GitHub does not grant Azure permissions.
Never share passwords, MFA codes, temporary sign-in passes or tokens in the form,
chat, source code or screenshots.

## 2. Nominate one Azure operator and submit the team form

Choose one operator per team to run the Azure-connected code while teammates
pair on the work. Submit **one response per team**:

[Open the Team Azure Access form](https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR83ImEQa061Powk_w90_QApUMkM4TVROQVA2Vlk2OFFEQVpBNDNYWTYxTC4u)

Use the operator's Bosch work email used for Microsoft 365. Do not enter a shared
mailbox or distribution list. If already submitted correctly, do not submit again.

**Expected:** the form confirms submission. This is a request for access, **not**
proof that Azure permission is ready. Coordinators must confirm onboarding.
You can continue with local preparation while waiting.

## 3. Join the workshop GitHub organization

Use the coordinator-supplied joining image below. Scan its QR code with your
phone, sign in with your personal GitHub account, enter the displayed joining
code and follow the join instructions.

![GitHub workshop joining instructions, QR code and joining code supplied by the coordinators](assets/github-join.png)

If the QR code is hard to scan on the same device, keep this page on your laptop
and scan with your phone, or ask the coordinators for the joining URL.
Do not guess the URL or share the joining image outside the workshop.

**Expected:** the joining flow confirms your organization membership.
Copilot availability depends on the assigned entitlement; if it is not active,
ask the coordinators and continue without it. Do not enter card/payment details
or buy a subscription to finish this workshop.

## 4. Open the private participant repository

[Open AI-Hackathon on GitHub](https://github.com/kirannn-kp/AI-Hackathon)

Sign in with the GitHub account granted repository access. The repository is
private and currently hosted under `kirannn-kp`, separately from the organization
shown in the joining image. **Joining that organization does not automatically
grant access to this repository.** If you see 404, ask the coordinators to confirm
your repository invitation/access; do not clone the console platform instead.

**Expected:** the GitHub page shows `README.md`, `starter`, `data` and `docs`.
Once the page is accessible, open PowerShell:

```powershell
git --version
git clone https://github.com/kirannn-kp/AI-Hackathon.git
cd AI-Hackathon
code .
```

If Git prompts for authentication, use its browser sign-in with the approved
GitHub account. Do not put your password or a token into the clone URL.
If a coordinator has already prepared the folder, open it in VS Code instead
of cloning again. All four challenges use this same working folder.

## 5. Prepare your Python environment

**Where:** VS Code > Terminal > New Terminal > PowerShell, in the folder containing
`pyproject.toml`. If any tool is missing, ask the coordinators or install only
through an approved workstation procedure.

```powershell
Get-Location
Get-ChildItem README.md, pyproject.toml
python --version
az version
```

**Expected:** the workshop root, Python 3.12 or newer and an installed Azure CLI.
Git, VS Code, Python and Azure CLI are required; Docker is not.

If this folder's `.venv` is not already prepared:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -e ".[mcp,cloud]"
```

Then run:

```powershell
.\.venv\Scripts\python -m route_resolve.lab check
```

**Expected:** **Contracts ready**. This checks local imports only, not model access.
Use Ctrl+Shift+P > **Python: Select Interpreter** and choose this folder's `.venv`.
No execution-policy or activation change is necessary with explicit Python paths.
The unfinished functions in `agents.py` are intentional exercises.

## 6. Optional: open GitHub Copilot in VS Code

Use the VS Code Accounts menu to sign into the approved GitHub account, then
open Chat. Follow any entitlement/sign-in prompt. Do not assume your Azure
operator identity is your GitHub account.

You may ask:

```text
Read README.md and docs/START_HERE.md in this workspace. Do not edit files or run
commands. Explain the business problem and what the first triage agent will do.
```

**Expected:** an explanation, not a resource deployment. Copilot is optional;
the written missions and your teammates are sufficient to continue.

## 7. Verify the operator's Azure sign-in

Only continue once the coordinators confirm the nominated operator's Azure
access. Accept any workshop directory invitation using that approved account.
Do not use the coordinator's account or another team's identity.

Check the existing CLI sign-in first:

```powershell
az account show --query "{operator:user.name,tenant:tenantId}" --output json
```

If it is already the assigned operator and workshop tenant, reuse it. Otherwise:

```powershell
$tenantId = Read-Host "Workshop tenant ID supplied by the coordinators"
az login --tenant $tenantId --allow-no-subscriptions --use-device-code
az account show --query "{operator:user.name,tenant:tenantId}" --output json
```

Follow the CLI's displayed sign-in URL/code using the approved operator account.
Do not send that device code to another person. Use the tenant-specific sign-in;
do not repeatedly log in once the correct cached identity works.

Open [Microsoft Foundry](https://ai.azure.com/) as the same operator and open
the team's assigned project using the coordinator's direct project link.
Switch to the workshop directory if prompted. Do not create a new resource,
subscription, project or model. Portal labels vary; a missing management screen
does not imply permission to broaden access.

**Expected:** the correct operator/tenant and access to the assigned project.
The real model and retrieval calls in the challenges verify service access;
successful sign-in alone is not proof of it.

[Microsoft Learn: Foundry projects, SDKs and endpoints](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview)

## 8. Set your team's configuration

The coordinators supply these non-secret addresses/names privately per team.
Do not guess a project endpoint from the browser's URL or select another team:

```powershell
$env:TEAM_ID = Read-Host "Assigned team ID"
$env:FOUNDRY_PROJECT_ENDPOINT = Read-Host "Assigned Foundry project endpoint"
$env:FOUNDRY_MODEL = Read-Host "Assigned chat deployment name"
$env:SEARCH_ENDPOINT = Read-Host "Assigned HTTPS Search endpoint"
$env:TEAM_KNOWLEDGE_BASE = Read-Host "Assigned team knowledge-base name"
```

These assignments apply to this terminal only. `.env.example` documents names
but is not automatically loaded. Shared service calls need coordinator approval
and the runner's `--allow-cloud` flag; setup does not authorize unlimited calls.

## 9. Ready checklist - then start Mission 01

- [ ] One operator nominated and the team's form submitted.
- [ ] GitHub joining completed and the private repository opens.
- [ ] One clone is open in VS Code with the correct `.venv`.
- [ ] The offline check prints **Contracts ready**.
- [ ] Operator's Azure access and assigned resource details are confirmed.
- [ ] You understand that GitHub, console and Azure are separate sign-ins.

When ready, open **Challenges** and build your first triage agent in Mission 01.
If you already completed setup here, skip repeating the clone/install/sign-in
steps there and begin its first-agent implementation step.

If blocked, tell the coordinators your team number, the step above and a redacted
error. Never include passwords, MFA codes or tokens.
