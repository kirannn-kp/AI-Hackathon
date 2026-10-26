# Mission: Route & Resolve - start here

Contoso Manufacturing receives fictional access, software-purchase and
data-sharing requests. A fluent chatbot might promise help without checking
anything. Your task is to build and test a more evidence-driven prototype.

## Three hours: Foundry + code + explanation

Prepare accounts, VS Code, Python, CLI and the clone **before** the timed core.
Use [Environment Setup](environment-setup.md); keep the console beside VS Code
and Foundry. One folder and the same assigned project serve all missions.

| Time | Mission | Evidence |
|---|---|---|
| 0-40 minutes | [01 - Prompt to Python](mission-01.md) | Playground comparison, read-only agent construction tour, working `triage` |
| 40-80 minutes | [02 - Agents, tools and tests](mission-02.md) | Named portal agent, real local tool call, two offline tests |
| 80-125 minutes | [03 - Policy evidence](mission-03.md) | Real source in Foundry and Python `retrieve_policy` |
| 125-165 minutes | [04 - Evidence and demo](mission-04.md) | Combined portal tools/knowledge, three tests, code walkthrough and demo |
| 165-180 minutes | Recovery and checkpoints | Finish and explain; no new feature work |

**Bonus starts after core completion, outside the 180-minute schedule.**
These are timeboxes, not measured beginner completion guarantees. Ask for help
at a blocked step rather than spending the whole mission retrying.

## Read-only code tours and hands-on edits

First read [examples/agent_blueprint.py](../examples/agent_blueprint.py).
Point to `client.as_agent`: this constructs a local agent, not a remote portal
agent or a completed model request. Do not edit the example.

Read the supplied runner, contracts and MCP implementation without changing
them. Implement only `triage`, `retrieve_policy`, their small helpers and your
own tests. Leave `resolve` and the final ten-case batch for after-core work.
Detailed coding recipes remain available, but do not complete every extension
inside the core. [Repository and scope map](../README.md).

## Work as a team without sharing credentials

- Each learner has their own Azure and GitHub sign-ins and working clone.
- Rotate driver, reviewer, Foundry tester and presenter every mission; smaller
  teams combine roles. Everyone explains code and inspects a real result.
- Copilot helps explain APIs, implement a focused change and propose tests.
  Predict output, review its diff and explain it before execution.
- Edit only your own uniquely named portal agent, not teammates' or shared
  connections. Synthetic data only; never disclose passwords or tokens.

## What counts as evidence

Use **read -> predict -> do -> observe -> explain**.
Separate live model/retrieval/tool outputs from offline test doubles.
The portal agent and local Python program are different runtimes; demonstrate
both rather than claiming changes synchronize.

A missing source is not grounding. A tool name written by the model is not a
tool call. Approval requested is not approval granted. Local mocked tests do
not prove cloud reliability. Keep failures and explain what is unverified.

## Recovery and finish

For wrong identity, 401/403, absent connections or timeouts, preserve a redacted
error and ask the coordinator. Do not self-grant roles, deploy replacement
resources or borrow identities. The policy permission issue was resolved for
project identities; individual CLI access and all-team connections still need
their own checks. Shared synthetic-policy reads are intentional.

Finish with a real Python triage result, a Python policy reference, three
offline tests, your portal knowledge/tool evidence and a three-minute team demo.
The core does not require production hosting, automatic multi-agent handoff or
mock writes. Unfinished checkpoints stay unfinished, not silently waived.

Then choose [bonus missions](bonus.md) or the
[advanced handoff build](code-extension/mission-04.md).

[Open Challenges and begin Mission 01](/challenges)
