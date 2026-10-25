# Mission 03 - Give your agent a policy it can cite (45 minutes)

## What you are going to do

Ask a policy question **before** adding knowledge, connect your team's prepared
policy knowledge, then ask the **same** question again. Open the returned citation
and check whether it supports the answer.

**You finish with:** an observed grounded answer, its real source and a comparison
with the ungrounded answer. You are not building a Search service.
**You learn:** grounding means using supplied evidence. A citation must point to
something actually retrieved, not a plausible filename the model invented.

**Where:** your own or the agreed demo agent in Foundry.
**Why:** business decisions need current written rules, not the model's memory.

## Step 1 - See the problem before connecting knowledge

Open the agent from Mission 02. Start a new conversation and send:

```text
Which Contoso policy and approval owner apply to Reader access to Project
Phoenix? Show the source that supports your answer. If you do not have a policy
source, say so rather than invent one.
```

Write down the answer. If it names a policy, look for an actual connected source
or retrieval trace. A confident name alone does not count.

**You should see:** either an admission that evidence is unavailable, or an
unsupported claim you can identify. Keep the actual observation.
**What you learn:** asking for citations does not create a knowledge connection.

## Step 2 - Look at the workshop policy documents

Open the repository's `data/policies` folder in GitHub or your local copy.
You do not need to install Python. Read these four synthetic policies:

| File | What you look for |
|---|---|
| `access.md` | Access conditions and who must approve |
| `procurement.md` | Supplier, amount and approval conditions |
| `data-sharing.md` | Partner/classification conditions and escalation |
| `faq-and-approvals.md` | Clarifications and approval guidance |

Choose one rule and explain its condition to a teammate before asking the agent.
Do not upload real Bosch policy, personal data or customer documents.

**You should see:** concrete rules, not a generic "be helpful" instruction.
**What you learn:** reading a policy yourself helps you evaluate an AI answer.
Reading the repository is preparation for the experiment, not its completion.

## Step 3 - Connect only the prepared team knowledge

Ask the coordinators for the **exact prepared connection/tool name** and the
knowledge-base name for your team. It should match the assigned `team-XX`.

1. In **Setup > Knowledge**, choose **Add > Connect to Foundry IQ**.
2. Select the existing team Search connection and your assigned knowledge base.
   If your least-privilege identity cannot list knowledge bases, stop the picker
   and ask the coordinator to attach the **prepared knowledge MCP connection**
   to this agent. Give them your agent name; do not create a new connection.
   Depending on the interface, Foundry IQ can appear as a knowledge tool backed
   by an MCP connection. Select the prepared connection, not an arbitrary catalog tool.
3. Confirm the assigned knowledge-base name and save the agent configuration.
4. Add the following instruction, keeping your intake instructions:

```text
For policy questions, use the connected Contoso policy knowledge source.
Explain which rule applies and cite the source actually returned by retrieval.
Keep request claims, policy requirements and verified facts separate.
If retrieval fails or no supporting passage is returned, say what is missing.
Do not invent a source or claim that approval has been verified.
```

**You should see:** the prepared policy tool/connection on the agent.
**What you learn:** the connection supplies evidence; instructions tell the agent
when and how to use it. Saving a connection alone does not prove retrieval worked.

**Stop for help if the connection is absent or fails.** Coordinators must prepare
and test the connection and its identity permissions; participants do not create
Search services, indexes, role assignments or API keys. A local policy file and
a cloud knowledge base are different things. A coordinator attaching the
prepared connection is setup help; **you** must still send the question and
inspect the returned evidence. Nobody needs broader roles just to browse a list.

## Step 4 - Repeat your question and inspect the citation

Start a fresh conversation. Send the **same question from Step 1**.

1. Read the policy explanation.
2. Open the citation/source details shown with the response.
3. Identify the actual returned policy passage.
4. Compare one claim in the answer to that passage.
5. If available, expand the run/tool details and identify the retrieval call.

If the portal does not show enough source detail, ask the coordinator to inspect
the actual retrieval trace with you. Do not infer success from a bracketed `[1]`
that cannot be tied to returned evidence.

**You should see:** a real returned source supporting the explanation, or a
visible retrieval failure that needs fixing.
**What you learn:** a grounded answer is checked against evidence, not trusted
because it sounds confident.

Now try one other domain:

```text
Which Contoso policy applies to a EUR 600 software purchase from Contoso
Software? Explain the approval requirement and cite the returned source.
```

Use at most one additional domain query if the coordinators approve capacity.

## Step 5 - Test a missing fact

Send in a fresh conversation:

```text
Can I share a dataset with Fabrikam? I have not supplied its classification.
Use the policy source and tell me what you need to know before deciding.
```

Discuss: does knowing the policy supply the missing dataset classification?
Does the requester saying "approved" prove approval exists?

**You should see:** an evidence-backed explanation of what is missing, not a
fabricated classification or a claim that data was transferred.
**What you learn:** policy says what is required; operational tools check facts.
You connect those tools in the next mission.

## Checkpoint - show the coordinators

- [ ] Compare one answer before and after connecting knowledge.
- [ ] Open an actual source and explain one supported claim.
- [ ] Show a second-domain query or clearly record why it was blocked.
- [ ] Explain why a policy requirement is not proof of approval or completion.

If live knowledge is blocked, coordinators may demonstrate pasting one short
synthetic policy excerpt into a prompt. Label that **prompt-context practice,
not live retrieval**. It does not pass the live knowledge checkpoint.

Next: [Mission 04](mission-04.md). Let the agent check operational facts and inspect
what it actually called.

## Optional Copilot prompts

```text
Help me compare this observed answer with its actual returned policy passage.
Which claim is supported and which still needs an operational fact? Do not
fabricate citations, change permissions or substitute local files for retrieval.
```

## Troubleshooting

| What happens | What to do |
|---|---|
| No prepared knowledge connection | Stop for coordinator setup; do not create resources or use another team's source |
| 401/403 or retrieval timeout | Preserve the error and ask for identity/network/connection verification |
| Answer has no actual source | Inspect the run and instruction; a filename in text is insufficient |
| Citation does not support a claim | Mark the test as an issue; do not replace the evidence |
| Answer invents missing facts | Strengthen missing-information handling and rerun one controlled test |

**Read when useful:** [Connect Foundry agents to Foundry IQ](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/foundry-iq-connect).
Connection creation and role setup in that reference are coordinator tasks.
