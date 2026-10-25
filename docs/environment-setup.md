# Environment Setup - get ready to use Foundry

**Your first goal is simple: open your team's Foundry project and send a prompt.**
You do not need to install Python, write code or ask Copilot to build anything
before your first playground conversation.

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
| GitHub | Your own account with repository access | Read/download workshop references; optional coding |
| Copilot | Your own entitled GitHub account | Optional help explaining code; not required for portal labs |

Never share passwords, MFA, temporary passes, tokens or device codes.
Do not paste credentials or real business data into prompts.

**You should see:** you can explain which sign-in you will use next.
**What you learn:** GitHub joining does not automatically grant Azure permissions;
console login does not automatically sign you into Foundry.

## 4. Open your team's Foundry project

1. Open [Microsoft Foundry](https://ai.azure.com/) in a second tab.
2. Sign in with your own approved identity.
3. Use the **direct project link supplied by coordinators**.
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
| 01 | Send a prompt in Foundry, improve instructions, compare responses | Before/after observations |
| 02 | Create a uniquely named prompt agent and test service-desk messages | Agent name and actual conversations |
| 03 | Connect prepared team policy knowledge and inspect a citation | Retrieved source supporting an answer |
| 04 | Connect prepared operational tools, inspect a real lookup and demonstrate behavior | Tool evidence and a small test table |

Core work happens in **Foundry**, not in a Python terminal. Use the console to
follow each step and show checkpoint evidence. The repository is reference
material plus an optional advanced coding track, not the main exercise.

**You should see:** a concrete goal beyond "read these files."
**What you learn:** prompt design, agent configuration, grounding, tools and
evaluation are separate skills. Do not claim retrieval or execution without evidence.

## 7. Join GitHub when you need the workshop materials

You may do this now or after your first Foundry prompt. GitHub/Copilot must not
block the browser-based introduction if coordinators can supply the synthetic
reference documents another approved way.

Scan the supplied QR code, sign in using the personal GitHub account directed by
the screenshot, and follow its joining instructions:

![GitHub workshop joining instructions, QR code and joining code supplied by the coordinators](assets/github-join.png)

Then open the [private AI-Hackathon repository](https://github.com/kirannn-kp/AI-Hackathon)
with the GitHub account granted repository access. Joining the organization in
the screenshot **does not automatically** grant access to this separately owned
repository. A 404 usually needs coordinator invitation/access verification.

**You should see:** the README, documentation, synthetic data and optional starter.
**What you learn:** organization membership, repository permission and Copilot
entitlement are different. Do not buy a subscription to finish the workshop.
Keep the joining image within the workshop audience.

## 8. Use the optional code track only when ready

You do **not** need Git clone, Python, Azure CLI or environment variables for
the four browser-based core missions. They are needed if you choose to implement
the advanced Python workflow later.

Start the [optional coding setup](code-extension/setup.md) only when the
coordinators confirm time and cloud-call approval. It preserves the earlier
triage, MCP, retrieval and handoff exercises without making them a beginner's
first task.

**You should see:** a clear separation between the portal lab and optional code.
**What you learn:** the playground demonstrates behavior; an application later
reproduces it using APIs, authentication, configuration and tested code.
Copilot is optional: review its suggestions and predict results before running them.

## 9. Ready checklist - then open Mission 01

- [ ] I know my team and can read the console guide.
- [ ] My own Azure access is confirmed.
- [ ] I can open the assigned Foundry project, not a personal project.
- [ ] I can open the playground with the assigned chat deployment.
- [ ] I know where to type a message and read the response.
- [ ] I understand that synthetic prompts cannot authorize real operations.

Open **Challenges > Mission 01** when coordinators start the workshop.
Use **read -> predict -> do -> observe -> explain**: before each test, say what
you expect; afterwards, point to what actually happened.

**You should see:** a first task you can perform, not a command you must trust.
**What you learn:** a response, citation or tool result is evidence to inspect,
not a reason to stop thinking.

If a required live capability is blocked, label it **blocked** and ask for help.
Pasting policy into a prompt is not live retrieval; saying "tool ran" is not a tool
trace. Do not mark those checkpoints complete without the actual evidence.
