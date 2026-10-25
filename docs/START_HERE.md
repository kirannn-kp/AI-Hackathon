# Mission: Route & Resolve

## The story: Monday morning at Contoso Manufacturing

At 08:15, the service desk at fictional **Contoso Manufacturing** opens its queue.
Maya joins Project Phoenix next week and needs Reader access. Arun needs a
software licence from Contoso Software. Leah wants to send a dataset to partner
Fabrikam. Each message looks like a simple request:

> "I join Project Phoenix next week. Please give me Reader access."
>
> "We need a EUR 600 software licence from Contoso Software."
>
> "Can we share an Internal dataset with Fabrikam?"

Today a person reads the message, finds the right team, checks the system,
searches the policy and asks for approvals or missing information. Requests bounce
between teams. A fast but unsupported answer can grant too much access, spend
money without authority or expose data. A fluent chatbot alone does not fix that.

**You are the engineering team building a safer request assistant.** Its job is
not to say "yes" to everything. It should investigate, select the right specialist
and explain the next action with evidence. Sometimes the correct next step is
to ask a question, route for approval or stop and escalate.

Everything here is synthetic: people, business requests, policies and operations.
No real access grant, purchase or data transfer is possible through the mock tools.

## What problem are we solving?

| Today | What your workflow should do |
|---|---|
| Someone manually reads every request | A triage agent extracts the domain and missing fields |
| Staff guess which team owns it | Triage hands off to the relevant specialist |
| A requester claims something is approved | The specialist checks actual facts and policy |
| An answer gives no supporting evidence | The result includes retrieved references and observed tool results |
| A failed dependency becomes a plausible reply | Errors remain visible and unsupported actions stop |

You will build three unfinished functions in `starter/route_resolve/agents.py`:
`triage`, `retrieve_policy` and `resolve`. The repository supplies runners,
contracts, synthetic data and MCP tools, but not completed agent implementations.

## Follow the story through four missions

| Mission | What you build | What you should be able to show | Time |
|---|---|---|---:|
| 01 - Your first triage agent | Connect the existing Foundry project/model and extract a request into fields | A real model-backed triage result | 30 min |
| 02 - Operational facts | Discover and call MCP tools; improve triage across three domains | Actual fact lookups and missing-information handling | 30 min |
| 03 - Policy evidence | Query the assigned Foundry IQ / Search knowledge base | Retrieved passages with genuine references | 45 min |
| 04 - Specialist workflow | Hand off, use evidence and perform permitted simulated operations | Ten Results and an explainable demonstration | 45 min |

The 150-minute core assumes tools, identities and shared resources are prepared.
Newcomers may need more time; the first-time learner timing is not yet certified.
Coordinators can help rather than having you guess at configuration.

```text
Trusted request ID + fictional user + request text
                    |
              Your triage agent
                    |
           one specialist handoff
          /         |          \
       Access   Procurement   Data Sharing
          \         |          /
       MCP operational facts + retrieved policy evidence
                    |
       mock action / clarification / review
                    |
       Result + citations + actual trace
```

## What the four outcomes mean

| Outcome | In everyday language | What it does not mean |
|---|---|---|
| Resolve | An evidence-backed answer is enough; no action is needed | A business operation was secretly performed |
| Execute | A permitted **mock** operation completed | Real access, money or data moved |
| Route | More information or approval is needed | Approval already exists |
| Escalate | A specialist/reviewer must assess the request | A review was bypassed |

A model-written "I checked the policy" is not evidence. You must show the actual
retrieval and tool trace. Read the [architecture](architecture.md) if the
responsibilities are unclear.

## Start here: browser, VS Code and Foundry have different jobs

1. **Stay in this console** to read the current challenge and use Prev/Next.
   Coordinators approve team milestones here.
   Before Challenges, complete **Environment Setup** using its tab, or read
   the [setup guide](environment-setup.md) alongside the presentation.
2. **Clone the [AI Hackathon participant repository](https://github.com/kirannn-kp/AI-Hackathon)**
   once, or open an approved source folder supplied by the coordinators.
   The console platform repository is not the participant starter.
3. **Open that folder in VS Code.** Keep its PowerShell terminal and files open.
   Mission 01 gives the clone, Python setup and first-agent steps in full.
4. **Use the assigned Azure identity in Foundry when a step asks.** The portal
   helps you locate the existing project, model and configuration. Your code runs
   locally; you do not deploy more resources or create agents manually in a portal.
5. **At every numbered step:** read the purpose, do the action, compare the expected
   result, and stop for help if it differs. Tell the coordinators the mission/step
   number and a redacted error. Do not paste passwords or tokens.
6. **At each checkpoint:** show the coordinators your result and explain it.
   Only then proceed to the next core mission.

**One clone per participant, one working folder per laptop:** all exercise materials are already supplied.
Do not replace your code between missions. The console paces learning; it is
not a secrecy mechanism for files already present in the repository.

## Finished the four core missions? Bonus is inside Challenges too

Click **Optional bonus missions** in the Challenges toolbar, or open the
[bonus guide](bonus.md). Choose one:

- Make failure safe with offline resilience tests.
- Challenge the evidence with synthetic approval/prompt-injection cases.
- Build an offline, repeatable evaluation report.

Allow 20-30 extra minutes per bonus. These are optional extensions, not a fifth
required milestone, and do not grant permission for extra cloud calls.

## Help and reading

- [Repository and sign-in guide](../README.md)
- [Microsoft Learn: your first agent](https://learn.microsoft.com/en-us/agent-framework/get-started/your-first-agent)
- [Microsoft Learn: Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/overview)
- [Microsoft Learn: Foundry SDKs and project endpoints](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview)

Each challenge links the specific Learn topic needed at that step. Use the Python
examples with the installed SDK versions. Skip resource-creation sections in
generic tutorials; the coordinators have already prepared the lab services.

Copilot is optional. Ask it to explain or plan one component, review its edits,
run the code yourself and explain the result. Do not ask it to find private
answers or change permissions. The workshop can be completed with your team
and the written steps if Copilot is unavailable.

**Access note:** private GitHub repository access does not grant Azure lab permissions.
Coordinators must separately confirm each participant's access to their team's
assigned resources. Everyone uses their own approved identity, never a teammate's
credentials. Foundry buddies provide support, not shared sign-ins.
Never commit credentials or real business data.

## Learning rhythm and teamwork

Use **read -> predict -> implement -> run -> explain** at each step. Before accepting
Copilot edits, identify the changed function and describe why the observed output
is correct. Passing a command without understanding its evidence is not the goal.
Each mission's learning map links actions to concepts and an explanation to give
your teammate.

Everyone builds the first agent on their own laptop; pair and rotate later.
Choose one team demo driver for the final cloud batch and stagger smaller checks
to respect shared capacity. Each laptop's local MCP state is independent.
An access problem is a reason to ask for help, not borrow credentials.

[Open Challenges and begin Mission 01](/challenges)
