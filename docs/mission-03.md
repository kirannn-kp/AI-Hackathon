# Mission 03 - Give your agent a policy it can cite (45 minutes)

## What you are going to do

Compare policy answers in Foundry, then implement the Python retrieval adapter.
Spend 5 minutes on the baseline, 5 reading policy, 10 connecting/inspecting the
portal result, 20 implementing Python retrieval and 5 on the checkpoint.

**You finish with:** a real portal policy result and a working Python
`retrieve_policy` function with actual returned references.
**You learn:** grounding means using supplied evidence. A citation must point to
something actually retrieved, not a plausible filename the model invented.

**Where:** your saved agent in Foundry, then `agents.py` in VS Code.
**Why:** business decisions need current written rules, not the model's memory.

## Step 1 - See the problem before connecting knowledge

Open the agent from Mission 02. Start a new conversation and send:

**Paste into Foundry Chat — before knowledge is attached:**

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

**Paste into Copilot Chat — read only:**

```text
Open data/policies/access.md and starter/route_resolve/agents.py. Do not edit.
Explain the difference between a policy requirement, a requester's claim and
an operational fact. Show me the unfinished retrieve_policy function and the
policy branch in lab.py that checks its returned references.
Explain why reading a local policy file is not live cloud retrieval.
Do not provide final-case answers or implement resolve.
```

**You should see:** concrete rules, not a generic "be helpful" instruction.
**What you learn:** reading a policy yourself helps you evaluate an AI answer.
Reading the repository is preparation for the experiment, not its completion.

## Step 3 - Connect only the prepared team knowledge

**Workshop access update:** the coordinators have enabled read-only policy access
for all eight Foundry project identities. The policy connection has successfully
retrieved ACCESS-001 through the team-01 rehearsal agent. This verifies that path,
not every team's connection or individual sign-in. If your connection is missing,
ask for setup help rather than assuming your test has passed.

The fictional policy collection is shared for this workshop. Separate index names
are organizational labels, **not an enforced policy-read boundary between team
project identities**. Keep using your assigned connection so your evidence is
repeatable. Shared policy access does not authorize editing policies, reading
other teams' agents or changing real business systems.

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
4. Open **Setup > Instructions**. Append the following, keeping your intake
   instructions. Save/apply, then return to **Chat**.

**Paste into Foundry Instructions — add policy behaviour:**

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

Click **New chat**, then use the same question. It is repeated here so you do
not have to scroll back:

**Paste into Foundry Chat — after knowledge is attached:**

```text
Which Contoso policy and approval owner apply to Reader access to Project
Phoenix? Show the source that supports your answer. If you do not have a policy
source, say so rather than invent one.
```

1. Read the policy explanation.
2. Open the citation/source details shown with the response.
3. Identify the actual returned policy passage.
4. Compare one claim in the answer to that passage.
5. If available, expand the run/tool details and identify the retrieval call.

If you see an approval request for `knowledge_base_retrieve`, inspect its query
and choose **Approve > Approve once** for your intended policy question.
The tested path returned the actual ACCESS-001 document and its source
`policies/access.md`. It did not produce a clickable citation annotation in
every answer. Inspect the returned tool document/source URL with the coordinator
when needed; a filename written by the model alone still does not count.

If the portal does not show enough source detail, ask the coordinator to inspect
the actual retrieval trace with you. Do not infer success from a bracketed `[1]`
that cannot be tied to returned evidence.

**You should see:** a real returned source supporting the explanation, or a
visible retrieval failure that needs fixing.
**What you learn:** a grounded answer is checked against evidence, not trusted
because it sounds confident.

**Look for:** a real `knowledge_base_retrieve` activity and an actual policy
document such as ACCESS-001. Point to the passage that supports one sentence.
The policy may describe owner approval, but it does not verify that anyone
actually approved this request.

If ahead of time and approved for another call, use this second-domain test.
Otherwise keep it for bonus; the core priority is the Python adapter.

**Paste into Foundry Chat — optional second-domain test:**

```text
Which Contoso policy applies to a EUR 600 software purchase from Contoso
Software? Explain the approval requirement and cite the returned source.
```

Only run the additional domain query if you are ahead of the timebox and the
coordinators approve capacity. Prioritize the Python task below.

## Step 5 - Build the retrieval adapter in Python

Open `starter/route_resolve/agents.py` and implement **only**
`retrieve_policy(category, request)`. Keep `triage` and its tests working.
Leave `resolve` as a stretch exercise. Read `lab.py`'s `policy` branch without
editing it: it requires a dictionary containing actual `references`.

1. Read `SEARCH_ENDPOINT` and `TEAM_KNOWLEDGE_BASE` from this terminal.
2. Obtain a Search-scoped token with your approved CLI identity, in memory.
   Portal project-identity access does not automatically grant this CLI user
   Search access; coordinators must verify the user's direct retrieval permission.
3. Use a bounded POST to the existing knowledge-base `retrieve` endpoint, API
   version `2026-08-01-preview`, with the question in `messages`.
4. Check status before parsing. Preserve the returned passages, `references`
   and `activity`. Missing evidence and HTTP failures remain explicit errors.
5. Separate HTTP transport from evidence validation so Mission 04 can test
   missing evidence without calling Search.

**The exact request contract — no extra recipe page is required:**

```text
POST {SEARCH_ENDPOINT}/knowledgebases/{TEAM_KNOWLEDGE_BASE}/retrieve?api-version=2026-08-01-preview
Content-Type: application/json
Authorization: Bearer <token obtained in memory, never copied into chat>
```

```json
{
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Access: Which policy covers Reader access to Phoenix?"}
      ]
    }
  ]
}
```

The application replaces the example question with its category/request inputs.
Use the configured Search endpoint, **not** the Foundry project endpoint.
Use your CLI credential with scope `https://search.azure.com/.default`.

**Paste into Copilot Chat — implement retrieval only:**

```text
Read my agents.py, the policy command in lab.py and this Mission 03.
Implement only retrieve_policy(category, request) and small helpers in agents.py.
Keep triage, resolve, the supplied runner, policies and examples unchanged.
Explain the plan before editing.

Validate category and nonempty question. Read SEARCH_ENDPOINT and
TEAM_KNOWLEDGE_BASE from this prepared terminal. Use AzureCliCredential to get
a token for https://search.azure.com/.default in memory. Never log the token,
Authorization header or credentials.
Make one bounded POST to the /knowledgebases/{name}/retrieve endpoint using
api-version=2026-08-01-preview and the messages JSON shape in this guide.
Use a transport available in the installed environment; do not add packages.
Check HTTP status first. Preserve the actual returned response passages,
references and activity in the returned dictionary. Do not guess an answer
property, synthesize citations or read local files as a replacement.
Reject missing/empty references explicitly; leave HTTP errors, timeouts and
authentication errors visible. Separate transport and evidence validation so
we can test empty evidence offline. Do not catch errors and return success.
Do not make cloud calls until I approve the command. Do not implement resolve.
```

Review the HTTP endpoint, `messages` body and evidence-validation helper before
accepting. Then run one approved query and point to its actual source:

```powershell
.\.venv\Scripts\python -m route_resolve.lab policy --category Access --text "Which policy covers Reader access to Phoenix?" --allow-cloud
```

**Check the result:** the command must print a nonempty `references` collection
and returned policy content. Find the Access source and explain one rule.
A Python traceback or missing references is a failure to investigate, not
permission to paste a filename into the result.

**Paste into Copilot Chat — inspect actual retrieval evidence:**

```text
Here is my real policy command output or redacted error: [paste below].
Show which returned fields contain the policy passage and source reference.
If it failed, compare the actual status/response with my adapter and propose
the smallest fix in my helpers. Do not fabricate citations, expose tokens,
change permissions or use local files to disguise a failed cloud request.
```

[Detailed retrieval reference](code-extension/mission-03.md) is optional extra
reading; the core instructions and request body are all above.

**You should see:** the Python command's real returned references and passages.
**What you learn:** a portal tool and a direct Python request can retrieve the
same knowledge through different identities and interfaces.

## Checkpoint - show the coordinators

- [ ] Compare one answer before and after connecting knowledge.
- [ ] Open an actual source and explain one supported claim.
- [ ] Show a second-domain query or clearly record why it was blocked.
- [ ] Explain why a policy requirement is not proof of approval or completion.
- [ ] Show your Python adapter and an actual returned reference; a portal-only run is insufficient.

If live knowledge is blocked, coordinators may demonstrate pasting one short
synthetic policy excerpt into a prompt. Label that **prompt-context practice,
not live retrieval**. It does not pass the live knowledge checkpoint.

Next: [Mission 04](mission-04.md). Let the agent check operational facts and inspect
what it actually called.

## Optional Copilot prompts

```text
Help me implement only retrieve_policy using the reviewed request contract in
docs/code-extension/mission-03.md. Inspect the actual response shape, preserve
references and surface errors. Explain each change; do not fabricate citations,
change permissions, implement resolve or substitute local files for retrieval.
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
