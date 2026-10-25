# Mission: Route & Resolve - start here

## The story

It is Monday morning at fictional **Contoso Manufacturing**. The service desk
receives three kinds of requests:

> "I join Project Phoenix next week. Please give me Reader access."
>
> "We need a EUR 600 software licence from Contoso Software."
>
> "Can we share an Internal dataset with Fabrikam?"

A person normally reads each message, identifies the right team, checks policy
and operational facts, and asks for missing information or approval. A fluent
chatbot might sound helpful while skipping those checks.

**Your goal is to explore a more evidence-driven assistant.** It should explain
what it knows, what it checked and what is still missing. Asking a question or
routing to a reviewer can be a better result than an unsupported "yes".
All organizations, requests, policies and operational actions in this lab are
fictional. Mock actions do not grant real access, spend money or transfer data.

## What you will do, learn and see

You begin in the **Foundry portal**, not a terminal. Use your own approved
identity and the coordinator's direct link to your existing assigned team
project. Everyone gets hands-on prompting; you do not need Python or Git first.

| Mission | You DO | You LEARN | You SEE |
|---|---|---|---|
| [01](mission-01.md) | Try a request in the chat/model playground, improve instructions, repeat the request | Prompting is an experiment: change something and compare | Actual before/after responses |
| [02](mission-02.md) | Save your own uniquely named prompt agent and test three synthetic requests | An agent is reusable instructions plus configured capabilities | Your agent name and three test results |
| [03](mission-03.md) | Attach the prepared team policy knowledge connection and compare without/with grounding | Grounding means retrieving evidence, not claiming to have read policy | Actual citations you can inspect |
| [04](mission-04.md) | Attach the prepared authenticated team MCP tools; inspect approvals and tool results; evaluate and demo | Tool execution and permission need observable evidence | Actual approval/tool trace and an honest small final demonstration |

The core targets about **150 minutes**. Access, portal capabilities and beginner
timings still need rehearsal; this is not a readiness certification.
You are not asked to deploy a hosted agent or create cloud resources.

## Three surfaces, three different jobs

1. **HackboxConsole:** read the story and current mission, move between guides
   and show team progress to the coordinator. Use the shared console login
   supplied for the workshop. Its styling and navigation remain unchanged.
2. **Microsoft Foundry:** use your individual identity to prompt and save your
   agent in the same assigned team project. Use the existing assigned model and
   coordinator-prepared knowledge/tool connections.
3. **Private GitHub repository:** optional reference/download and advanced coding,
   at https://github.com/kirannn-kp/AI-Hackathon. Repository access is separate
   from Foundry authorization. VS Code and Copilot are optional, not core gates.

Read the identity/access sections of [Environment Setup](environment-setup.md)
with your coordinator. Coding setup can wait. Portal labels and available
features vary: the coordinator confirms the live route; do not guess connection
names, permissions or resource-creation steps from a generic tutorial.

## Work safely alongside your team

- Everyone signs into Foundry individually. Share observations, never Azure
  passwords, temporary access passes, tokens or MFA approvals.
- Create your own agent, for example `team-XX-initials-triage`. Replace the
  placeholders and add an agreed suffix if another learner already uses it.
  Write down the saved name so you can return to the right agent.
- Edit only your own agent. Do not alter teammates' instructions or shared
  connections. Ask before changing a shared team setting.
- Rotate the person explaining results. A buddy can help you navigate, but
  should not replace your opportunity to send prompts.
- Use only synthetic workshop data. Never upload customer documents, real
  employee information or credentials.

## Learn by comparing, not by collecting green ticks

Use **read -> predict -> try -> inspect -> explain**:

1. Read the next action and say what you expect to happen.
2. Send the synthetic prompt or make the instructed change to your own agent.
3. Inspect the actual response, returned citations or tool evidence.
4. Compare against your prediction and previous run.
5. Explain the result and one limitation to a teammate, then show the checkpoint.

A convincing answer is not proof of a correct answer. A statement such as
"I checked the policy" is not a citation. A tool name appearing in a response is
not proof of a tool call. An approval request is not an approval, and a queued
mock action is not a completed one. The [architecture guide](architecture.md)
explains these boundaries.

## If something does not work

Stop the affected step and tell the coordinator the mission, attempted action,
assigned project and a **redacted** error. Keep tokens, passwords and sensitive
account details out of screenshots and shared notes.

| What you see | What to do | What to record |
|---|---|---|
| Wrong account/project or an empty project list | Check your assigned identity and direct project link with the coordinator | Access not confirmed |
| 403, unavailable model or a failed prompt | Ask the coordinator to check that exact identity and capability | Prompt blocked; no successful model evidence |
| Missing knowledge connection or no returned citations | Ask which prepared connection is supported; do not create a replacement | Retrieval/citation evidence missing |
| MCP authentication error, unavailable tool or unclear approval | Stop; ask the coordinator before proceeding | Tool execution unverified or approval pending |
| Unexpected response | Repeat a small controlled comparison with the coordinator's guidance | Actual observed result, not the hoped-for result |

A model-metadata 403 has occurred during rehearsal. An account-level Reader
addition was approved for **one rehearsal identity only**. It is not a general
participant permission or evidence that everyone's portal access works.
Participants must not self-grant roles or borrow that identity.

If the coordinator offers a manual policy-in-prompt exercise while retrieval is
blocked, label it **prompt-context exercise, not live retrieval**. Record the
missing live evidence. Never replace a failed retrieval or tool call with an
invented successful output.

## Finish with an honest demonstration

Show the observed prompt improvement, your saved agent and three tests, actual
knowledge citations, and actual MCP approval/tool evidence. Finish with a small
evaluation of what worked and what did not.

If a capability remains blocked, demonstrate the parts you actually observed and
identify the missing evidence. Do not claim a blocked checkpoint passed.
The core does not require Python stubs or a ten-case CLI batch.

## Optional next steps

After the four missions, choose [Bonus 1, 2 or 3](bonus.md): safe failure handling,
evidence challenges or repeatable offline evaluation. These are not a fifth
mandatory milestone.

Experienced learners can separately follow the coding extension linked from
the [README](../README.md), using its existing pinned environment instructions.
Offline tests and simulated outputs are useful, but must be labelled honestly.
Extra live calls require coordinator approval; optional work does not authorize
new deployments or broader permissions.

[Open Challenges and begin Mission 01](/challenges)
