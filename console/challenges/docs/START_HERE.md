# Mission: Route & Resolve

## The story: a request arrives

It is the start of a busy working day at fictional **Contoso Manufacturing**.
Three requests arrive:

> "I join Project Phoenix next week. Please give me Reader access."

> "We need a EUR 600 software license from Contoso Software."

> "Can we share an Internal dataset with Fabrikam?"

Today, people manually read these requests, check facts, look up policy and find
the right approver. A plausible reply is not enough: an incorrect approval can
grant excessive access, spend money or expose information.

**You are the engineering team.** Build a small AI-powered workflow that does
the investigation, chooses the right specialist and explains the next action
using real evidence from this fictional lab.

## Your problem statement

Given an unstructured request and a trusted request/user ID:

1. Understand the domain and identify missing information.
2. Gather operational facts through MCP tools.
3. Retrieve the relevant policy and preserve its citations.
4. Hand off to Access, Procurement or Data Sharing.
5. Perform only a permitted **simulated** operation, or route/escalate it.
6. Explain the outcome with evidence.

The four outcomes are **Resolve**, **Execute**, **Route**, and **Escalate**.
You will learn their differences as you build. This is not a general support
chatbot, and fluent text is not proof that an operation happened.

## The architecture you will build

```text
Trusted request ID + synthetic user + request text
                         |
                      Triage
                         |
            one specialist handoff
           /             |             \
       Access       Procurement      Data Sharing
           \             |             /
            policy retrieval + MCP facts
                         |
          mock action or clarification
                         |
       Result + citations + actual trace
```

The facilitator supplies the shared Foundry models and Search knowledge base.
Your code runs in VS Code. The local MCP server has fictional operational data;
it cannot change real business systems. Read the detailed
[architecture](docs/architecture.md) in the repository.

## How this workshop works

**One console link. One repository clone. One working folder.**

1. Sign in to this console using the credentials supplied by the facilitator.
2. Read this briefing, then open **Challenges** to start Mission 01.
3. Follow the repository onboarding in **README.md**: clone, open VS Code,
   sign in to optional Copilot and prepare Python.
4. Follow the current console mission alongside your code.
5. Use its commands and expected results to check each step. If stuck for
   three minutes, ask the facilitator with the step number and a redacted error.
6. Show your evidence and obtain approval before moving on.

The console controls the guided pace, not secrecy of files in your repository.
All exercise materials are included in the initial clone; facilitator solutions
and the answer-key grader are kept separately.

## The four missions

| Mission | Question you will answer | Time |
|---|---|---:|
| 01 - Establish the base | What are we building, and can my environment run it? | 30 min |
| 02 - Investigate | What is being requested, and which facts can I verify? | 30 min |
| 03 - Find evidence | Which policy supports the next step? | 45 min |
| 04 - Route and resolve | Which specialist should act, and what actually happened? | 45 min |

**Early finishers:** choose one [optional bonus mission](docs/bonus.md):
make failure safe, challenge the evidence or build a repeatable evaluation
report. Allow 20-30 extra minutes. These are not required console milestones.

The 150-minute core assumes tools, identities and shared resources are ready.
Stretch tasks are optional. First-time learner timing still needs a rehearsal.

## Use Copilot as a partner, not an authority

Each mission includes prompts to explain a concept, help implement one component
or review your evidence. Ask for a plan first and review edits before accepting.
You must still run the code and explain why the result is justified.

Never send passwords, TAPs, tokens, real business data or customer documents to
chat. Do not authorize Copilot to deploy resources or broaden permissions.
No Copilot entitlement? Continue with the guide, your team and the facilitator.

## Your final demonstration

Show one permitted mock action, one approval route and one escalation. Point to
the retrieved policy and actual tool trace. Explain one limitation. Every result
must say `simulation: true`.

**Local review status:** this content and the working code skeleton are prepared
for customer review. Publishing, live Foundry integration, participant resource
permissions and automated cleanup are separate readiness gates.

[Open Challenges and begin Mission 01](/challenges)
