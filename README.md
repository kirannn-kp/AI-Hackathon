# AI Hackathon - Mission: Route & Resolve

Help fictional Contoso Manufacturing handle access, procurement and data-sharing
requests more carefully. Start with a prompt, save your own agent, add policy
knowledge, then inspect operational tools and explain the evidence.
All requests, policies and actions are synthetic.

**The primary workshop happens in the Microsoft Foundry portal. No Python, Git,
VS Code or command-line setup is required before your first portal prompt.**
HackboxConsole remains your colourful guide and team checkpoint surface.
[Read the story and learning rhythm](docs/START_HERE.md).

## 1. Open the workshop, then your assigned project

The coordinators provide the console login, your individual workshop identity,
team assignment and direct Foundry project link. They must also confirm which
existing model, policy knowledge connection and authenticated MCP tools your
team should use. These are assignments to verify, not a promise that every
capability is ready.

| Surface | What you do there | Sign-in |
|---|---|---|
| HackboxConsole | Read guides and show team checkpoints | Coordinator-provided shared console login |
| [Microsoft Foundry](https://ai.azure.com/) | Prompt, create your own prompt agent and inspect evidence | Your own approved workshop identity |
| Private GitHub repository | Read/download reference material; optional coding extension | Your own approved GitHub account, if needed |

Everyone can prompt using their own identity in the **same assigned team
project**. A shared project does not mean a shared Azure login. Never borrow
passwords, temporary access passes, MFA approvals or tokens.
The console login does not grant Foundry access; GitHub access does not either.

Follow the identity/access portions of [Environment Setup](docs/environment-setup.md)
with your coordinator. Laptop coding preparation in that guide is for the
optional extension, not a gate to Mission 01. Use the direct project link and
check the assigned project name. Do not create a project or deploy a model.
Portal labels can vary; ask the coordinator when the guide and visible UI differ.

**Access is still being rehearsed.** A rehearsal encountered a 403 when reading
model metadata using the shared account. An account-level Reader addition was
approved for one rehearsal identity only, not for participants. That approval
does not establish participant readiness or authorize anyone to change roles.
If model selection or prompting is blocked, report it instead of working around
the boundary.

## 2. Follow the four portal-first missions

The core aims for approximately **150 minutes**, including checkpoints.
This is a planning target, not a certified beginner completion time.

| Mission | What you DO | What you LEARN | What you SEE at the checkpoint |
|---|---|---|---|
| [01 - First prompt](docs/mission-01.md) | Try a synthetic request in the chat/model playground; improve instructions and compare | Instructions change behaviour but do not prove correctness | Observed before/after prompts and responses |
| [02 - Your prompt agent](docs/mission-02.md) | Create a uniquely named prompt agent in the existing team project; test three synthetic requests | A saved agent keeps reusable instructions | Your saved agent name and three actual test responses |
| [03 - Policy grounding](docs/mission-03.md) | Attach the coordinator-prepared team policy knowledge connection; compare without/with grounding | Retrieval must supply evidence, not just plausible text | Actual returned citations and what they support |
| [04 - Operational tools and demo](docs/mission-04.md) | Attach coordinator-prepared authenticated team MCP tools; inspect approval/tool evidence and run a small final evaluation | An answer is not proof that a tool ran or an action completed | Actual approval/tool trace, a small comparison and an honest final demo |

Give your agent a unique name such as `team-XX-initials-triage`, replacing `XX`
and `initials` with your team and an agreed personal abbreviation. Add a short
suffix if needed. Record the exact name. Change **only your own agent**; do not
edit, rename or delete teammates' agents or shared connections.

Participants do not deploy hosted agents, create cloud resources, configure
shared authentication or administer permissions. Coordinators prepare the
connections and confirm the supported portal workflow.

## 3. Keep an evidence record

Use your workshop notes or another coordinator-approved place. Record only
synthetic inputs and redacted evidence:

- Mission 01: the same request before/after an instruction change, with the
  actual responses and one observation.
- Mission 02: your exact saved agent name, instructions and three test results.
- Mission 03: the real citations returned, the source passage inspected and the
  difference from the ungrounded answer. Mark missing citations explicitly.
- Mission 04: the actual approval state, tool name/arguments/result visible in
  the trace, and what the final response can honestly claim.
- Final demo: one improvement, one evidence-backed result and one limitation.

If a capability is blocked, record **blocked / missing evidence**, tell the
coordinator which mission and action failed, and share a redacted error.
Do not invent a citation, tool result or successful operation to complete a
checkpoint. A manual policy pasted into a prompt is a **prompt-context exercise**,
not live retrieval. A local test double is not a live MCP trace.

## 4. Reference/download and optional advanced coding

**Participant repository:** https://github.com/kirannn-kp/AI-Hackathon

This private repository contains workshop reference material, an unsolved coding
starter and synthetic data. Request access through the coordinator if needed;
do not use another person's GitHub credentials. Read in the console first.
Downloading or cloning is optional for the core portal workshop.

After the core, experienced learners can choose the separate coding track:

1. [Coding extension 01](docs/code-extension/mission-01.md)
2. [Coding extension 02](docs/code-extension/mission-02.md)
3. [Coding extension 03](docs/code-extension/mission-03.md)
4. [Coding extension 04](docs/code-extension/mission-04.md)

Use the existing pinned environment instructions linked from that track and
[Environment Setup](docs/environment-setup.md); do not improvise SDK upgrades.
Python stubs, a local MCP server and the final ten-case CLI batch belong to
that optional track, **not** the four core checkpoints.
Copilot is optional for explanations or coding help; never give it credentials,
real business data or requests to find private answers.

Choose additional [bonus exercises](docs/bonus.md) for offline failure testing,
evidence challenges and evaluation. There is no mandatory fifth milestone.

## Reading map and maintenance

- [Start here: story, teamwork and recovery](docs/START_HERE.md)
- [Architecture: what each component does](docs/architecture.md)
- [Optional bonus exercises](docs/bonus.md)

Maintainers can use the existing authoring environment and
`scripts/build_workshop.py` to regenerate the local reader and console import.
Generated `index.html` is a review reader, not authentication or proof of access.
Generated `console/challenges` is the console content import, not a deployment.
The hosted console keeps its original colourful Hackbox styling.

## Attribution and safe use

Adapted from Microsoft's MIT-licensed Fraud Intelligence MicroHack, revision
`3a3c15c9119b9b926c897a17332783c6dc055e3c`.
See the supplied `LICENSE`, the
[upstream licence](https://github.com/microsoft/MicroHack/blob/main/LICENSE) and
[upstream MicroHack](https://github.com/microsoft/MicroHack/tree/main/03-Azure/01-04-AI/07_Fraud_Intelligence).
Use fictional data only. Do not deploy resources, change roles, expose tool
endpoints publicly or delete shared services.
