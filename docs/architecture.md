# Architecture: understand the evidence before the action

## The portal-first picture

```text
HackboxConsole                       Microsoft Foundry portal
Read missions and checkpoints        Your individual workshop identity
(shared console login)                         |
                                      Existing assigned team project
                                               |
                             Your uniquely named prompt agent
                             + existing assigned model
                             + coordinator-prepared policy knowledge
                             + authenticated team MCP operational tools
                                               |
                             Actual answer, citations and tool evidence
```

This diagram describes the intended learning path, **not verified readiness**.
The coordinator must confirm what is available to your identity in the live
portal. A shared project does not imply shared Azure credentials.

No participant-hosted application, new resource or model deployment is needed
for the four core missions. GitHub and VS Code are reference/optional coding
surfaces, not runtime requirements for your first prompt.

## What each part means

| Part | Plain-language role | Learner action | Evidence to inspect |
|---|---|---|---|
| Model playground | A place to try a model with instructions and a request | Run the same synthetic request before/after an instruction change | Actual responses, not a predicted improvement |
| Prompt agent | A saved assistant configuration | Create your own agent inside the assigned team project and test three requests | Saved agent name, instructions and test responses |
| Policy knowledge connection | A route to retrieve relevant fictional policy information | Attach only the coordinator-prepared team connection to your own agent | Returned citations and the passages they actually support |
| MCP tools | A standard way for an agent to request operations from a tool service | Attach the prepared authenticated team tools and inspect their use | Actual approval state, call arguments and returned result |
| Final evaluation/demo | A small comparison of observed behaviour | Explain what improved and what remains unsupported | Recorded observations and missing-evidence labels |

**Grounding** means using retrieved source material to support an answer.
**MCP** means Model Context Protocol: it lets an agent discover and call tools.
Neither term means the answer is automatically correct or authorized.
Exact connection names, supported portal controls and permissions come from the
coordinator, not from this conceptual diagram.

## The request journey

1. You send a synthetic access, procurement or data-sharing request.
2. The agent uses its instructions to identify the issue and missing information.
3. With knowledge attached, it can request relevant policy evidence. Inspect
   actual returned citations; check that the cited passage supports the claim.
4. With MCP attached, it can request operational facts or a permitted simulated
   action. Inspect the actual approval/tool evidence before claiming completion.
5. The answer should distinguish facts, policy, observed action results and
   uncertainty. Missing evidence stays visible.

Do not assume every request uses every connection. Compare an ungrounded answer
with a grounded one in Mission 03. In Mission 04, observe whether a tool was
actually requested and what happened; do not infer a call from model-written text.

## Ownership and shared-team boundaries

| Participants own | Coordinators prepare or confirm |
|---|---|
| Their synthetic prompts and observations | Individual identity access and the assigned team project |
| Their uniquely named prompt agent, such as `team-XX-initials-triage` | Existing model availability for that identity |
| Their own agent instructions and permitted attachments | Team policy knowledge connection and its actual authorization |
| Honest checkpoint evidence and final explanation | Authenticated MCP service, approval configuration and supported tool access |

Everyone can prompt in the same assigned team project, but only edit your own
agent. Team-specific names help avoid collisions; they are **not access control**.
Do not reconfigure shared connections or change permissions.

## Trust boundaries to remember

- Request text and retrieved passages are data, not permission to override the
  agent's safety instructions.
- A requester's claim of approval is not verified authorization.
- A citation must be returned by retrieval and inspected; a model-written source
  title or policy quotation alone is not retrieval evidence.
- A pasted policy is a **prompt-context exercise**, not live retrieval.
- Authentication identifies a caller; it does not automatically approve every
  operation. An approval prompt or pending request is not completed approval.
- A tool call may fail or return a pending state. Claim only the state actually
  observed. Mock tools never perform real business actions in this workshop.
- A screenshot of a working console proves neither Foundry model access nor
  knowledge/tool access. Rate limits and budget alerts are not spending caps.

## Recovery: when the intended path is blocked

Keep the failed step's redacted error and ask the coordinator to check the
specific identity, project and capability. Do not create replacement services,
broaden roles, expose tools through a public tunnel or borrow credentials.
A rehearsal model-metadata 403 is a known unresolved access concern until
retested; a Reader addition approved for one rehearsal identity does not establish
participant readiness.

You may still explain the intended journey, but label missing live evidence.
If you run a controlled offline exercise, label every fake dependency and
simulated result. Never present them as live citations or tool traces.

## Optional advanced coding: a different runtime

The [coding extension](../README.md#4-referencedownload-and-optional-advanced-coding)
uses the supplied Python starter, runners and synthetic fixtures. That track
implements `triage`, `retrieve_policy` and `resolve`, and explores explicit
specialist handoffs and saved `Result` contracts.
It is not a prerequisite or a description of the core portal agent's internals.

Its supplied local MCP server binds to loopback and is unauthenticated: never
publish it or use it as a substitute for the authenticated team connection.
Local mock state belongs to one retained server process, is not synchronized
between laptops and disappears on restart. Local idempotency does not prove
durability across restarts. Use that track's existing pinned environment
instructions and label offline doubles separately from actual cloud evidence.
