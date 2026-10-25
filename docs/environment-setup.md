# Environment Setup - start here before the challenges

Keep this page open beside VS Code. Follow these steps at your own pace, even
when the presentation moves on. Setup is preparation, not a scored challenge;
opening this page does not start your team's challenge timer.

**Your route:** sign in to the console -> find your team -> confirm individual
access -> join GitHub -> clone on your laptop -> prepare Python -> verify your
own Azure sign-in -> configure your team's resources -> Mission 01.

## First: open the console and find your team

1. Open the [workshop setup page](https://bosch-rnr-console-czfb3nscn5otc.azurewebsites.net/environment-setup).
2. Sign in using the **shared team console username/password** delivered privately
   by the coordinators. This is not your Bosch or GitHub password.
3. Check the team roster on this console page and confirm your assigned team.
   If the roster is missing or your assignment differs, ask a coordinator.
4. Everyone follows the preparation below on **their own laptop**. The Foundry
   buddy helps teammates; they are not the only person allowed to run code.

**Expected:** you know your team and can keep this guide open while working.
**What you learn:** the console tracks team milestones, while individual sign-ins
authorize code and service access. A console login does not grant Azure access.

The team allocation is proposed until the coordinators confirm it. Roles are
starting responsibilities, not restrictions: rotate coding, design, testing and
demo work. Foundry access reported in registration is not a certification of
expertise or proof of access to the workshop tenant.

## 1. Know which account to use

| Account | What it is for | What to use |
|---|---|---|
| Console team login | This setup page, challenges and team progress | Team username/password delivered privately by coordinators |
| GitHub | Join the workshop organization, access the starter and optional Copilot | Your personal GitHub account, as directed on the joining image below |
| Azure / Foundry | Run model and policy-retrieval calls | Your own approved Bosch work account after workshop access is confirmed, or an individually assigned approved training account |

These are separate sign-ins. Joining GitHub does not grant Azure permissions.
Never share passwords, MFA codes, temporary sign-in passes or tokens in the form,
chat, source code or screenshots.

**What you learn:** GitHub repository access, optional Copilot entitlement and
Azure permissions are independent; success in one does not prove the others.

## 2. Confirm your individual Azure access

Coordinators already collected registration emails. Confirm that your team and
Bosch work email are correct; follow their instructions for the updated form.
Use it to supply requested individual confirmation, corrections or access issues.
Do not submit repeated responses when your details are already confirmed.

[Open the individual Azure access confirmation form](https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR83ImEQa061Powk_w90_QApUMkM4TVROQVA2Vlk2OFFEQVpBNDNYWTYxTC4u)

Use your own Bosch work email used for Microsoft 365, not a shared mailbox or
distribution list. You do not need your own paid subscription or subscription
Owner. Required workshop resource permissions must be assigned separately.

**Expected:** your email/team and access status are confirmed with coordinators.
Form submission is **not** proof that Azure permission is ready. Individual
onboarding is subject to tenant policy and coordinator confirmation.
**What you learn:** authentication identifies you; authorization determines
which workshop services you can call. Continue local preparation while waiting.

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

**What you learn:** organization membership and Copilot entitlement are distinct
from access to a particular private repository.

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

Everyone uses their **own local clone**. Before running `git push`, agree which
branch or contribution method your coordinators allow; do not overwrite another
person's work or assume repository read access includes write access.
**What you learn:** Git downloads editable code; the console is the guide, not
the code execution environment.

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

**What you learn:** a virtual environment isolates dependencies. Python and Azure
CLI installation do not grant Azure permissions; `az version` is only an
installation check. This offline check can run before your Azure access is ready.
If `python` or `az` is not recognized, stop and ask for an approved installation;
do not skip the failed step and assume the later commands will work.

## 6. Optional: open GitHub Copilot in VS Code

Use the VS Code Accounts menu to sign into the approved GitHub account, then
open Chat. Follow any entitlement/sign-in prompt. Your approved Azure sign-in
may differ from your GitHub account.

You may ask:

```text
Read README.md and docs/START_HERE.md in this workspace. Do not edit files or run
commands. Explain the business problem and what the first triage agent will do.
```

**Expected:** an explanation, not a resource deployment. Copilot is optional;
the written missions and your teammates are sufficient to continue.

**What you learn:** Copilot proposes changes; you remain responsible for
understanding, reviewing and testing them. Before accepting a change, name the
function being edited, predict its output and explain one failure it must reject.

## 7. Everyone: verify your own Azure sign-in

Only continue once coordinators confirm **your individual workshop access**.
Accept any workshop directory invitation using your approved account.
Do not use a coordinator's or teammate's credentials.

Check the existing CLI sign-in first:

```powershell
az account show --query "{account:user.name,tenant:tenantId}" --output json
```

If it is already your approved account and workshop tenant, reuse it. Otherwise:

```powershell
$tenantId = Read-Host "Workshop tenant ID supplied by the coordinators"
az login --tenant $tenantId --allow-no-subscriptions --use-device-code
az account show --query "{account:user.name,tenant:tenantId}" --output json
```

Follow the CLI's displayed sign-in URL/code using your own approved account.
Do not send that device code to another person. Use the tenant-specific sign-in;
do not repeatedly log in once the correct cached identity works.

Open [Microsoft Foundry](https://ai.azure.com/) as the same approved identity and open
the team's assigned project using the coordinator's direct project link.
Switch to the workshop directory if prompted. Do not create a new resource,
subscription, project or model. Portal labels vary; a missing management screen
does not imply permission to broaden access.

**Expected:** your correct account/tenant and access to the assigned team project.
The real model and retrieval calls in the challenges verify service access;
successful sign-in alone is not proof of it.

**What you learn:** the portal helps locate resources; your Python code uses the
CLI identity. Browser sign-in alone does not sign the CLI in. Members share the
assigned team project, not credentials. If access is pending, pair for local
work and request help; do not change identities to bypass the failure.

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

**What you learn:** configuration selects the project/model/knowledge base;
credentials authorize the request. A project endpoint is not a portal URL, and
a deployment name is not necessarily the model family name.
All team members use the same assigned values on their own laptops.
Stagger cloud experiments, run one small example before a batch, and ask for help
on rate-limit errors rather than adding automatic retries or increasing limits.

## 9. Ready checklist - then start Mission 01

- [ ] My own approved email, team and individual access status are confirmed.
- [ ] GitHub joining completed and the private repository opens.
- [ ] One clone is open in VS Code with the correct `.venv`.
- [ ] The offline check prints **Contracts ready**.
- [ ] My own Azure access and assigned resource details are confirmed.
- [ ] You understand that GitHub, console and Azure are separate sign-ins.

When ready, open **Challenges** and build your first triage agent in Mission 01.
If you already completed setup here, skip repeating the clone/install/sign-in
steps there and begin its first-agent implementation step.

If blocked, tell the coordinators your team number, the step above and a redacted
error. Never include passwords, MFA codes or tokens.

## How to learn rather than blindly accept generated code

For each mission, use **read -> predict -> implement -> run -> explain**:

1. Read the story and learning map before opening Copilot.
2. Predict one input's output in your own words.
3. Implement only the current small step, with or without Copilot.
4. Review the changed function and run the specified check yourself.
5. Explain the observed evidence to a teammate; if you cannot, pause and ask why.

Every participant builds and tests Mission 01 locally. Then pair on specialist
work, compare approaches and rotate roles. Agree one **team demo driver** for the
final ten-case cloud run, so the team does not launch duplicate final batches.
Each laptop's loopback MCP server has separate synthetic state; shared `TEAM_ID`
does not synchronize local servers.
