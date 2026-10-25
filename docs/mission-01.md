# Mission 01 - Send your first prompt in Foundry (30 minutes)

## What you are going to do

Open **Microsoft Foundry**, send a request, read the answer, then improve the
instructions and try again. **No Python or Copilot is needed for this mission.**
You are not just reading a repository. You will make real model calls in a
playground and keep a before/after example.

Imagine you work at the service desk of fictional Contoso Manufacturing.
Maya writes: "I join Project Phoenix next week. Please give me Reader access."
A helpful-sounding answer is easy. An answer that admits what it cannot verify
is more useful. You will see that difference for yourself.

**You finish with:** two observed responses and your explanation of what changed.
**You learn:** a prompt is what you ask now; instructions describe how the model
should behave. Neither gives it permission to change a business system.

## Before you click

Complete **Environment Setup**, including your own approved Azure sign-in.
Have your assigned project name/link and existing chat deployment name ready.
Team members share the team project, not Azure passwords. Use synthetic text only.
The coordinators must confirm playground access before starting the timer.

**Where:** [Microsoft Foundry](https://ai.azure.com/) in your browser.
**Why:** this is where you experience the model directly before building an agent.
Keep this console open in a second tab so you can follow one step at a time.

## Step 1 - Open your team's existing project

1. Sign in with your own approved workshop account.
2. Open the project link supplied by the coordinators.
3. Check the project selector at the top: it must show your assigned `team-XX`.
4. Stay inside that project. Do not use **Create project**, **Deploy model** or a
   personal subscription.

**You should see:** your team's project home. The home page can show **Build an
agent**, **Use a model**, and the project endpoint.
**What you learn:** a project is your team's workspace; it is not the agent itself.

If your project is missing, stop here and ask a coordinator. Signing into the
console or GitHub does not grant Foundry access.

## Step 2 - Open the model playground

1. On the project home, choose **Test in playground**. Another normal entry is
   **View deployments**, then click the existing chat deployment's **name** to
   open its playground. Use this if the home shortcut is unavailable but the
   deployment is visible and authorized; never force a disabled button.
2. Select the **existing chat deployment** from your team handout. The workshop
   deployment is supplied; do not choose an embedding model or deploy a new one.
3. Open **Setup** and inspect **Tools**. If Foundry automatically added
   **Web search**, use its actions menu > **Remove**. For this first comparison,
   keep tools empty. We are testing instructions, not searching the web.
4. Return to **Chat**. Find **Chat with the model...** and the **Send** button.
5. Leave advanced parameters at their supplied defaults.

In the classic interface, the equivalent entry is **Playgrounds > Chat**.
Follow the path matching the interface you actually see; do not switch projects
to make a button work.

**You should see:** a chat playground, the selected deployment and an input box.
**What you learn:** a playground lets you experiment with a model without writing
an application. A chat deployment runs language responses; embeddings do not.

**If blocked:** a disabled button, empty deployment list or 403 is an access/setup
problem, not an exercise to solve by granting yourself roles. Ask a coordinator.
Do not treat the empty screen as a reason to deploy your own model.

## Step 3 - Send a first request and inspect the answer

Paste this into the **message** box and press Send:

```text
I join Project Phoenix next week. Please give me Reader access.
What should happen next?
```

Before reading the response, predict: can this model actually grant access?
Now read it. Does it ask a question, suggest a process, or claim it did something?
There is no single guaranteed wording; record what **your run actually says**.

**You should see:** a real response in the playground.
**What you learn:** fluent text is not proof of a lookup, approval or action.
This first model has no workshop operational tools connected.

Save the prompt and response in a local note. Do not include passwords, tokens,
account screenshots or real customer requests.

## Step 4 - Give the model a clear job and try the same request

Open **Setup** and find the **system message / instructions** area, separate from
the user-message box. Replace its workshop instructions with the following,
then apply/save if the playground requires it:

```text
You are the intake assistant for the fictional Contoso service desk.
Read requests; do not claim to perform actions.
Choose one category: Access, Procurement, or DataSharing.
Keep your answer under 120 words. Reply with:
1. Category
2. Details supplied by the requester
3. Missing details or checks needed
4. Suggested next step
Do not invent facts, approval, policy or tool results.
If information is missing, say what you would ask.
All examples are simulations, not real business operations.
```

Return to **Chat** and choose **New chat / clear chat**, keeping those instructions, and send
the **same** Maya request again. Clearing the conversation avoids mixing the
first answer's history into the comparison.

**You should see:** an answer that follows the requested structure more closely.
It still has not granted access or checked a real policy.
**What you learn:** a clear role, output format and boundaries change behavior.
Instructions guide the model; they are not a guarantee of correct behavior.

If the response breaks a rule, underline the exact line and improve one
instruction. Do not keep pressing Send until you get a lucky screenshot.

## Step 5 - Test something incomplete, then something different

Start a fresh conversation for each test, retaining your instructions:

```text
Please give me access.
```

```text
We need a EUR 600 software licence from Contoso Software.
```

For the first, check whether missing project/role details remain missing.
For the second, check whether the category changes to Procurement.
Write one sentence describing a mistake or limitation you observed.

**You should see:** different inputs produce appropriately different intake
responses; missing information is not silently invented.
**What you learn:** one good answer is not a test suite. Try a normal case, an
incomplete case and a different domain.

**Call budget:** aim for these four messages (baseline, improved and two tests).
One reviewed correction is enough; stagger tests with your teammates.

## Checkpoint - show the coordinators

- [ ] Show your actual playground conversation, not a generated mock screenshot.
- [ ] Compare the first and improved responses to the same request.
- [ ] Explain the difference between instructions and a user message.
- [ ] Point out one missing field and one thing the model has not verified.
- [ ] Every member has sent at least one prompt with their own approved access.

Next: [Mission 02](mission-02.md). You will save this behavior as a named prompt
agent and test it in the agent playground.

## Optional Copilot prompts

```text
Read my before/after responses. Do not generate replacement evidence or edit
anything. Ask me which instruction changed the response and which claim still
needs a real tool or policy source.
```

## Troubleshooting

| What happens | What to do |
|---|---|
| Test in playground is disabled | Try the normal View deployments > existing chat name path; if unavailable, ask for help; never force a disabled control |
| No deployment is available | Compare the assigned project and handout; ask for help |
| The model says it granted access | No tools are attached; identify the unsupported claim and strengthen the instruction |
| Old answers influence the comparison | Start a new conversation while keeping the instructions |
| Rate limit / service error | Stop, retain the error, and ask when to retry; do not loop automatically |

**Read when useful:** [Microsoft Foundry playgrounds](https://learn.microsoft.com/en-us/azure/foundry/concepts/concept-playgrounds).
The portal changes over time; coordinators verify the workshop's exact path.
