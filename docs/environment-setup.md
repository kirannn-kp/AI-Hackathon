# Environment Setup - get ready for Foundry and Python

**Your first goal is simple: open your team's Foundry project and send a prompt.**
You can try that before installing Python, but the three-hour core includes
Python implementation and tests. Complete workstation preparation before the
challenge timer starts; do not leave it until Mission 03.

Keep this console open in one browser tab and Foundry in another.
Follow one step, check what you see, then continue. Reading setup does not start
your team's challenge timer.

## 1. Sign in to the console and find your team

Open the [workshop setup page](https://bosch-rnr-console-czfb3nscn5otc.azurewebsites.net/environment-setup).
Use the **shared team console username/password** supplied privately by the
coordinators, for example your assigned `team-01`.
Expand **Show team members and roles** above this guide and find your name.
If your name or team is wrong, ask a coordinator before using resource details.

Everyone uses **their own laptop**. Foundry buddies help teammates; they are not
the only people who can send prompts. Roles rotate.

**You should see:** your team roster and this setup guide.
**What you learn:** the console organizes team learning; it does not sign you
into Azure or run an agent.

## 2. Confirm your own workshop Azure access

Coordinators already collected work emails. Confirm your team and the **Bosch
work account you will actually use to sign in**. Follow their instructions for
the updated individual access form; do not submit duplicates unnecessarily.

[Open the individual Azure access confirmation form](https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR83ImEQa061Powk_w90_QApUMkM4TVROQVA2Vlk2OFFEQVpBNDNYWTYxTC4u)

Wait for coordinator confirmation, and accept any workshop invitation using your
own approved identity. An individually assigned training account is an alternative
only when coordinators explicitly provide one. Never use a teammate's credentials.

**You should see:** your email/team and access status are confirmed.
**What you learn:** form submission does not automatically grant permissions.
Existing Foundry access elsewhere does not authorize this workshop project.
You do not need a personal paid subscription or subscription Owner.

## 3. Know which account belongs where

| Place | Account | What it lets you do |
|---|---|---|
| This console | Shared assigned team login | Read challenges and track team milestones |
| Foundry | Your own approved work/training identity | Use the assigned project, model and agents after authorization |
| GitHub | Public repository; your own account for Copilot | Clone the workshop and work on Python exercises |
| Copilot | Your own entitled GitHub account | Explain read-only code, implement focused changes and write tests |

Never share passwords, MFA, temporary passes, tokens or device codes.
Do not paste credentials or real business data into prompts.

**You should see:** you can explain which sign-in you will use next.
**What you learn:** GitHub joining does not automatically grant Azure permissions;
console login does not automatically sign you into Foundry.

## 4. Open your team's Foundry project

1. Open [Microsoft Foundry](https://ai.azure.com/) in a second tab.
2. Sign in with your own approved identity.
3. Click your **team name in the roster above**, or use the direct project link
   supplied by coordinators if you are reading the repository copy.
4. Check the project selector: it must show your assigned `team-XX`.

If prompted, switch to the workshop directory. Do not create a resource,
subscription, project or model deployment. If the screen differs, ask a
coordinator to show you the correct workspace rather than guess.

**You should see:** your project's home and its project name.
**What you learn:** the project is your team's workspace. Your browser page
address and the project's API endpoint serve different purposes.

## 5. Check that the playground is available

On the project home, look for **Test in playground**, or choose **View deployments**
and click the existing chat deployment's name to open its playground. In the
classic experience, use **Playgrounds > Chat**. Select the **existing chat deployment** supplied by
the coordinators; do not select an embedding deployment or deploy a new model.

Open **Setup > Tools** and remove any automatically added **Web search** for the
first lab. Return to **Chat** and look for the message box and Send control.
Mission 01 gives you the exact request to paste, compare and improve.

**You should see:** a playground with a selected model deployment and input box.
**What you learn:** you can experiment with a model without Python. Opening the
portal alone does not prove that you can call a model or create an agent.

If both playground entry paths are unavailable, deployments are missing or a 403
blocks the actual model call:
**stop and tell a coordinator**. This is an access/readiness issue. Do not try to
fix it by changing roles, creating resources or borrowing another login.
Coordinators must verify the participant experience before starting the mission.

## 6. Know what you will build and test

| Mission | Your hands-on task | What you keep |
|---|---|---|
| 01 / 40 min | Compare Foundry prompts, read construction code, implement Python triage | Real model call and code explanation |
| 02 / 40 min | Save a portal agent, inspect local MCP tools, write two tests | Agent, tool result and tests |
| 03 / 45 min | Inspect portal policy evidence and implement Python retrieval | Actual references in both surfaces |
| 04 / 40 min | Combine portal knowledge/tools, add a third test and demo code | Evidence table and working components |

Core work uses **both Foundry and VS Code**. Reserve the last 15 minutes for
recovery/checkpoints: 40 + 40 + 45 + 40 + 15 = **180 minutes**.
Bonus is outside the three-hour core, after the required work is complete.

**You should see:** a concrete goal beyond "read these files."
**What you learn:** prompt design, agent configuration, grounding, tools and
evaluation are separate skills. Do not claim retrieval or execution without evidence.

## 7. Join GitHub and open the workshop materials

Complete this before the timed core. If repository access is unavailable, ask for
an approved source folder; do not borrow credentials. Confirm Copilot entitlement
beforehand. If it is unavailable, pair-review the same code tasks manually.

For workshop Copilot onboarding, open the authenticated console's
[Environment Setup page](https://bosch-rnr-console-czfb3nscn5otc.azurewebsites.net/environment-setup).
Follow the joining instructions shown there using your own GitHub account.
The joining image and code are deliberately not included in the public repository.

<!-- console-only-github-join -->

Open the [public AI-Hackathon repository](https://github.com/kirannn-kp/AI-Hackathon).
Reading and cloning it does not require an invitation. Joining the workshop
organization **does not automatically** grant Azure permissions or prove that
Copilot entitlement is active.

**You should see:** the README, documentation, synthetic data and optional starter.
**What you learn:** organization membership, repository permission and Copilot
entitlement are different. Do not buy a subscription to finish the workshop.
Keep the joining image within the workshop audience.

## 8. Prepare VS Code, Python and your CLI identity before the timer

Follow the [workstation checklist](code-extension/setup.md) in your one clone:
Git, VS Code, Python 3.12+, Azure CLI, the pinned `.venv` and configured terminal.
Select that `.venv` in VS Code. Run `route_resolve.lab check` and the supplied
offline contract tests. **Contracts ready** does not prove Azure access.

Verify your own CLI identity separately from browser sign-in. Obtain the assigned
project endpoint, deployment, Search endpoint and knowledge-base name from the
coordinator. The coordinator must verify individual model **and direct Search
retrieval** access before starting; the approved project-MI role does not grant
your CLI user that permission. No participant should create role assignments.

**You should see:** a prepared coding environment and an individually verified
identity, not just a portal tab.
**What you learn:** browser, CLI, application runtime and Copilot are distinct
contexts. Review suggestions and predict results before running them.

## 9. Ready checklist - then open Mission 01

- [ ] I know my team and can read the console guide.
- [ ] My own Azure access is confirmed.
- [ ] I can open the assigned Foundry project, not a personal project.
- [ ] I can open the playground with the assigned chat deployment.
- [ ] I know where to type a message and read the response.
- [ ] I understand that synthetic prompts cannot authorize real operations.
- [ ] My clone, selected Python environment and offline tests are ready.
- [ ] My own CLI model/retrieval access and terminal configuration are verified.
- [ ] I know which functions to edit and which reference code is read-only.

Open **Challenges > Mission 01** when coordinators start the workshop.
Use **read -> predict -> do -> observe -> explain**: before each test, say what
you expect; afterwards, point to what actually happened.

**You should see:** a first task you can perform, not a command you must trust.
**What you learn:** a response, citation or tool result is evidence to inspect,
not a reason to stop thinking.

If a required live capability is blocked, label it **blocked** and ask for help.
Pasting policy into a prompt is not live retrieval; saying "tool ran" is not a tool
trace. Do not mark those checkpoints complete without the actual evidence.

**Policy access update:** read-only access is enabled for all eight workshop
project identities, and team-01 policy-tool retrieval has been rehearsed
successfully. Your team's connection must still be attached and tested in
[Mission 03](mission-03.md). Fictional policies are shared across team project
identities; do not treat separate index names as a security boundary.
