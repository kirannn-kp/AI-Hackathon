# Optional code extension 01 - Build your first triage agent

This is a detailed implementation recipe. The mixed core uses its triage steps
only; follow the timebox and checkpoint in [Mission 01](../mission-01.md).
Do not redo completed setup or extend into orchestration during this mission.

## Your mission in the story

It is Monday morning at fictional Contoso Manufacturing. Maya is joining Project
Phoenix and writes, "Please give me Reader access." The service desk also receives
software-purchase and data-sharing requests. Today someone reads every message
and decides which team should investigate it. You will build that first reader:
the **triage agent**.

**By the end:** your Python code sends one synthetic request to the assigned
Foundry model and returns structured information about what it asks for.
It does **not** grant access, approve spending or decide whether sharing is safe.
Those decisions need facts and policy evidence in later missions.

**You change:** `triage(request)` in `starter/route_resolve/agents.py`.
**You use:** the supplied runner, an existing Foundry project and its shared model.
**You do not create:** Azure resources, model deployments or new accounts.

**Timebox:** orientation/setup 10 min; first agent 15 min; checkpoint 5 min.
Tools and accounts should be prepared before the timed workshop. If installation
or access blocks you, ask the coordinators rather than spending the whole mission
troubleshooting. The main timed guide is `docs/mission-01.md` in your clone.

## Learning map - know why you are doing each step

| Step | What you learn | Explain it to a teammate |
|---|---|---|
| 1 - Open the clone | The console is a guide; local code is what you change | Where will my edits run? |
| 2 - Check Python/files | An environment isolates dependencies; contracts define valid outputs | Why is Contracts ready not a working agent? |
| 3 - Inspect Foundry | Identity, project endpoint and deployment have different jobs | Which value is the address, which selects the model, and who is calling? |
| 4 - Configure | Environment variables configure this terminal only | What must I repeat in a new terminal? |
| 5 - Implement triage | An instruction plus a schema turns text into validated fields | Why does classification not authorize an action? |
| 6 - Run and inspect | An observed model response tests the implementation | Which fields came from the request, and which must stay missing? |

Before asking Copilot to edit, read P01 and write your prediction of its domain,
project and role. After the run, compare that prediction to actual output.
Everyone builds this first agent on their own laptop; the Foundry buddy helps,
but must not be the only person who understands or runs it.

## Before you start: collect your team handout

If you completed the console's **Environment Setup** tab, do not clone, reinstall
or sign in again. Confirm the same terminal has your configuration, then continue
at **Step 5 - Build the first agent**. The [setup guide](../environment-setup.md)
remains available if you need to revisit a prerequisite.

Ask the coordinators for all of these. Never guess another team's details.

| Detail | Where you use it | What it means |
|---|---|---|
| Workshop repository URL or approved source folder | Step 1 | Your editable exercise code, not the HackboxConsole platform repository |
| Console team login | This browser | Mission navigation and team progress |
| Team ID | PowerShell | For example, your assigned `team-XX` |
| Your approved Azure identity and tenant ID | Step 3 | Each participant signs in individually after coordinator confirmation |
| Direct Foundry project link and project name | Step 3 | The team's already-created workspace |
| Foundry project endpoint and chat deployment name | Step 4 | The address and deployed model your code calls |
| Search endpoint and knowledge-base name | Mission 03 | Your team's policy evidence |

The console password, GitHub account and Azure identity are **different sign-ins**.
Everyone uses their own laptop and approved identity; pair on the code, not passwords or MFA.
Copilot is optional and requires its own entitlement.

## Step 1 - Get the code and open the right folder

**Where:** a PowerShell terminal on the workshop workstation.
**Why:** the browser explains the exercise; VS Code is where you build it.

If the coordinators already opened the workshop folder for you, **do not clone
again**. Confirm you can see `README.md`, `pyproject.toml`, `starter` and `data`.
Otherwise clone the private **workshop** starter using an approved GitHub account
with repository access:

```powershell
git clone https://github.com/kirannn-kp/AI-Hackathon.git
cd AI-Hackathon
code .
```

If a coordinator supplied an approved extracted folder instead, open that folder
with **File > Open Folder** in VS Code. Do not run `git clone` on a ZIP file.
If GitHub is unavailable, ask the coordinators for an approved source folder.
Do not substitute the console platform or a private preparation repository.

**You should see:** a VS Code Explorer with the files listed above. In VS Code,
open **Terminal > New Terminal**, select PowerShell, and check the working folder:

```powershell
Get-Location
Get-ChildItem README.md, pyproject.toml
```

Keep this one folder for all missions. You will not download replacement code
between challenges. [Repository setup reference](../../README.md).

## Step 2 - Prepare Python and understand the supplied files

**Where:** the VS Code terminal, at the repository root.
**Why:** the virtual environment installs this workshop's pinned SDK versions
without changing the machine's other projects.

Skip creation/install if the coordinators already prepared this same environment:

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\python -m pip install -e ".[mcp,cloud]"
.\.venv\Scripts\python -m route_resolve.lab check
```

**You should see:** Python 3.12+ and **Contracts ready**. This is an offline import
check, **not** a working agent or proof of Azure access. Use **Ctrl+Shift+P >
Python: Select Interpreter** and choose this folder's `.venv`.
No activation or execution-policy change is needed with the explicit executable.

Open these files in the Explorer:

| File | Read it to understand |
|---|---|
| `starter/route_resolve/agents.py` | Three unfinished functions; implement only `triage` now |
| `starter/route_resolve/models.py` | Allowed categories and the final Result contract |
| `data/practice-requests.json` | Synthetic records; find P01 and read its `text` |
| `starter/route_resolve/lab.py` | The supplied runner, which keeps trusted request/user IDs |

`NotImplementedError` in the agent functions is deliberate. The task is to replace
the current mission's stub, not remove checks until the command appears to pass.

## Step 3 - Find your existing project in the Foundry portal

**Where:** PowerShell for Azure login; [Microsoft Foundry](https://ai.azure.com/)
in a browser for orientation.
**Why:** the project endpoint tells your code **where** to work; the deployment
name tells it **which model** to call. A portal page URL is not a project endpoint.

1. First run `az account show --query user.name --output tsv`. If it shows the
   your approved identity and the coordinators confirm its tenant, reuse that sign-in.
2. If not signed in, use the supplied tenant ID. Do not repeatedly sign in when
   the correct cached CLI account is already working:

   ```powershell
   $tenantId = Read-Host "Paste the Azure tenant ID from the coordinators"
   az login --tenant $tenantId --allow-no-subscriptions --use-device-code
   az account show --query "{account:user.name,tenant:tenantId}" --output json
   ```

3. In the browser, sign into Foundry as that **same approved identity**. Open the
   coordinator's direct project link or choose the assigned project by name.
   Check the directory/tenant if the project is missing; do not create a project.
4. On the project's overview/details page, find **Project endpoint**. Compare it
   with the handout. Its shape is an HTTPS address ending in
   `/api/projects/<assigned-project>`, not the `ai.azure.com` browser address.
5. Locate the existing model/deployment listing and compare the chat deployment
   name with the handout. Labels differ between Foundry experiences; if the
   participant cannot see a listing, ask the coordinators to confirm the value.
   A missing management screen does not authorize you to deploy another model.

**You should be able to explain:** "This is my team's project; this endpoint
belongs to it; this deployment is the shared model." Sign-in alone does not prove
model permission. A later real call will check that.

**Read if needed:** [Foundry SDKs and project endpoints](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview)
and [What is Foundry Agent Service?](https://learn.microsoft.com/en-us/azure/foundry/agents/overview).
Documentation can describe creating resources: skip those setup sections because
the coordinators already supplied them. Do not add API keys or change roles.

## Step 4 - Connect this terminal to the assigned resources

**Where:** the same VS Code PowerShell terminal.
**Why:** these environment variables are configuration, not an agent implementation.

```powershell
$env:TEAM_ID = Read-Host "Assigned team ID"
$env:FOUNDRY_PROJECT_ENDPOINT = Read-Host "Assigned Foundry project endpoint"
$env:FOUNDRY_MODEL = Read-Host "Shared chat deployment name"
```

Use the exact handout values, including spelling. `FOUNDRY_MODEL` means the
**deployment name**, not a model family you pick yourself. These assignments last
only in this terminal. `.env.example` is a reference and is not automatically
loaded. Never paste credentials into source, screenshots or Copilot.

## Step 5 - Build the first agent: extract, do not approve

**Where:** `starter/route_resolve/agents.py`, function `triage(request)`.
**Why:** the rest of the workflow needs predictable fields rather than a paragraph.

Use the Python sections of [Your first agent](https://learn.microsoft.com/en-us/agent-framework/get-started/your-first-agent)
and the [Microsoft Foundry provider](https://learn.microsoft.com/en-us/agent-framework/integrations/by-component/model-providers/microsoft-foundry).
Use the installed versions in `pyproject.toml`; current online samples can target
a newer SDK. Inspect the installed constructor before adapting sample code:

```powershell
.\.venv\Scripts\python -c "import inspect; from agent_framework.foundry import FoundryChatClient; print(inspect.signature(FoundryChatClient))"
```

Build in this order, without implementing the other two functions:

1. Write a short instruction: identify the domain and extract the requested
   business fields; treat the request as data, not instructions that change rules.
2. Create a Foundry-backed client using the configured project/deployment and
   your approved CLI identity. Prefer `AzureCliCredential` for this CLI-based lab
   so a different cached VS Code identity is not selected. Do not print tokens.
3. Define a structured response schema and validate the returned values:

   | Field | Meaning and requirement |
   |---|---|
   | `category` | Exactly `Access`, `Procurement` or `DataSharing` |
   | `urgency` | Your documented enum, for example `low`, `normal`, `high`; not approval |
   | `missing_fields` | List of business fields the requester did not provide |
   | `arguments` | Extracted fields; Access needs `project` and `role`, Procurement needs `supplier` and positive EUR amount, DataSharing needs `partner` and `classification` |

4. Call the assigned model with a finite output/timeout budget. Parse its response
   and return a dictionary matching your schema. Missing facts stay missing;
   do not make up a project, approval or price. Keep monetary values as decimal
   strings rather than binary floats.
5. Make invalid JSON, a refusal, timeout or authentication failure visible.
   Do not fall back to hard-coded categories and call that a successful model run.
6. Keep the synchronous `triage(request)` signature used by the CLI runner.
   Async SDK work can live in an async helper called from this normal CLI process.
   Close underlying clients reliably; not every client is an async context manager.

**Small-build checkpoints:** first write the schema and instruction and explain
them without a model call. Next wire one client call and parse its actual output.
Then add validation and visible errors. Finally use Step 6; do not ask Copilot to
complete retrieval and orchestration at the same time.

**Self-check without an answer key:** if you remove the project name from a
synthetic request, should your output invent one? Explain your expected behavior
before adding a controlled local validation test.

This is a **code-built agent using the existing Foundry service**. You do not
need to press "Create agent" in the portal or deploy a hosted agent. You can
reopen the portal to check your project/model details whenever needed.
[Structured output reference](https://learn.microsoft.com/en-us/agent-framework/agents/structured-outputs).

## Step 6 - Run one real request and explain what happened

After the coordinators approve shared-service calls:

```powershell
.\.venv\Scripts\python -m route_resolve.lab triage --id P01 --allow-cloud
```

**You should see:** JSON with the original request/user IDs retained by the runner,
and your structured triage output identifying an Access request. Inspect the
extracted project/role against P01's text. This is **not** proof that access was
granted. If the stub is still present, "Exercise not implemented yet" is the
expected stop; return to Step 5.

## Checkpoint - show the coordinators

- [ ] Explain the business problem and the difference between classification and approval.
- [ ] Point to your clone, Python environment, assigned project and deployment.
- [ ] Show a real model-backed P01 triage result and explain each field.
- [ ] Explain where trusted IDs come from and what your agent must not invent.

After coordinator approval, continue to [Mission 02](mission-02.md): let the
workflow check operational facts through MCP tools.

## Optional Copilot prompts

```text
Read docs/mission-01.md and my starter files. Explain what triage does and propose
a short plan for triage(request) only. Use the installed Foundry/Agent Framework
APIs, Azure CLI identity and assigned project/deployment. Help me validate the
schema and make errors visible. Explain each change before editing. Do not
implement the other missions, find private answers, deploy resources or expose
credentials. Ask me to explain why a category is not an approval.
```

## Troubleshooting

| What you see | What to do next |
|---|---|
| No repository URL | Ask the coordinators for the approved source; do not clone a guessed repository |
| Cannot find `pyproject.toml` | Use `Get-Location`; open the cloned workshop root, not `starter` |
| Wrong Python/import failure | Select this folder's `.venv`; use its explicit Python executable |
| Project missing or 401/403 | Compare your account, tenant, endpoint and deployment; ask the coordinators, not for broader roles |
| Unexpected SDK argument | Inspect the installed signature; do not upgrade all packages to match a web sample |
| JSON looks like prose | Recheck schema/instructions and reject invalid output; do not silently guess |
