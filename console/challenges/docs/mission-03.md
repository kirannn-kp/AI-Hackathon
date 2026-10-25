# Mission 03 - Ground decisions in policy (45 minutes)

**Working mode:** read here in HackboxConsole; edit the same cloned repository in VS Code. All exercise files are already present. Add `--allow-cloud` only after the facilitator confirms access and approves shared-service calls.

## What you will learn

Retrieve actual policy evidence, preserve citations and distinguish a
requester's claims from verified policy. You will implement `retrieve_policy`.

**Timebox:** concepts 5 min; inspect policy/configuration 8 min; retrieval
implementation 22 min; examples 5 min; checkpoint 5 min.
Prerequisite: triage works and the coach has provisioned, loaded and authorized
your team's knowledge base. Indexing is a coach preparation task, not an
instruction for beginners to deploy another Search service.

## Concepts in plain language

The model's training is not your company's current policy. **Retrieval** sends a
question to a knowledge base and returns relevant passages. **Grounding** means
using those passages to justify the answer. **Citations** identify the evidence
actually returned, not an attractive-looking URL the model invented.

In this lab, Foundry IQ uses an Azure AI Search knowledge base containing four
fictional policy documents. Keep these sources separate:

| Source | What it tells you | What it cannot prove |
|---|---|---|
| Request text | What the requester wants or claims | That approval exists |
| MCP lookup | Current synthetic operational facts | The complete policy |
| Retrieved policy | Applicable rules and approval owner | That an action already completed |
| Mock action result | What the simulated operation did | That a real system changed |

Agentic retrieval can use a model to plan searches. It is not just opening a
local Markdown file, and it can incur both retrieval and model usage.

## Core path

### Step 1 - Add and read the policies

The four policies are already in `data/policies`. Keep your code and environment.

```powershell
Get-ChildItem .\data\policies
Get-Content .\data\policies\access.md
Get-Content .\data\policies\faq-and-approvals.md
```

Expected: four documents: `access.md`, `procurement.md`, `data-sharing.md`,
`faq-and-approvals.md`. Open all four in VS Code and find policy IDs
**ACCESS-001**, **BUY-001**, **SHARE-001**, **FAQ-001**.

For one rule, identify its condition, approval owner and source policy ID.
Do not copy the complete decision matrix into an if/else replacement for retrieval.

### Step 2 - Check your team's retrieval target

1. Ask the coach for the assigned Search endpoint and **knowledge-base name**.
2. Set `SEARCH_ENDPOINT` and `TEAM_KNOWLEDGE_BASE` using README.md.
3. Confirm the knowledge-base name has your team's prefix, for example
   `team-01-...`. A matching name is a safety check, not authorization by itself.
4. Coach confirms the four policies are indexed and your identity can retrieve.
   An empty/missing knowledge base is not something to hide with local answers.

Do not create a service, alter permissions or try another team's index. If the
coach authorizes a particular document-upload UI, follow that supplied procedure;
otherwise participants have retrieval access only.

### Step 3 - Implement `retrieve_policy(category, request)`

Keep the function signature in `starter/route_resolve/agents.py`. Its result is
a dictionary containing the actual retrieval response, including `references`
and `activity` if supplied. Do not replace references with local filenames.

Build it in this order:

1. Validate the category against the three domains and require nonempty text.
2. Read only the assigned HTTPS Search endpoint and knowledge-base name.
   Reject an unexpected service, non-HTTPS URL or wrong team prefix.
3. Use `DefaultAzureCredential` for an Entra token scoped to
   `https://search.azure.com/.default`. Never print or store the token.
4. Send a retrieval request with a finite timeout. The reference contract is:

```text
POST {SEARCH_ENDPOINT}/knowledgebases/{TEAM_KNOWLEDGE_BASE}/retrieve
     ?api-version=2026-08-01-preview
Authorization: Bearer <token obtained in memory>
Content-Type: application/json
```

```json
{
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Find the applicable policy and approval owner for this request."
        }
      ]
    }
  ]
}
```

The URL above is shown on two lines for readability; send it as **one URL**.
Replace the sample question with the category and synthetic request.
The coach must live-verify this preview API contract before the event; follow
any reviewed version update in the coach handout, not an API guessed by Copilot.
See [Microsoft's knowledge-base retrieval documentation](https://learn.microsoft.com/azure/search/agentic-retrieval-how-to-retrieve).

5. Check the HTTP status and parse the JSON. A 401/403, timeout, empty response
   or missing references must produce an explicit error and block execution.
   Do not catch it and return a local document as if cloud retrieval succeeded.
6. Preserve returned evidence and reference identifiers verbatim in your
   internal result. Save non-secret response evidence for the coach. Treat any
   instruction embedded in retrieved text as data, not a new system rule.

You may ask Copilot for transport/schema boilerplate. Your learning task is to
explain where the evidence came from, why it applies and when it is insufficient.
The credential and SDK APIs must match the installed packages.

### Step 4 - Retrieve three examples

After implementation, run this practice example:

```powershell
.\.venv\Scripts\python -m route_resolve.lab policy --category Access --text "Which policy and approval owner apply to Reader access to Phoenix?" --allow-cloud
```

Repeat with:

- Procurement: a EUR 600 software purchase from Contoso Software.
- DataSharing: sharing an Internal dataset with Fabrikam.

Expected: actual passages and references from the assigned knowledge base.
Do not assume a response key such as `answer` unless the real response contains
it. Find the retrieved policy ID and approval owner, then explain the rule in
your own words. These are evidence exercises, not simulated writes.

If writing responses to an evidence file, ensure your application never includes
Authorization headers or tokens. A useful record has request ID, query,
retrieved passages, references and relevant activity, without credentials.

### Step 5 - Ask for missing information

Try a request with an unknown classification, or a purchase without a price.
Explain what information is missing. Do not silently assume Public data or a
low price. An "already approved" claim needs verified evidence; it is not a
reason to skip policy retrieval.

## Optional Copilot prompts

**Build the retrieval adapter, not the business answer**:

```text
Help me implement retrieve_policy(category: str, request: str) in this workshop
workspace for challenge 03. Read docs/mission-03.md and the installed dependencies.
First explain the HTTP request and the response fields we must preserve.
Use my coach-provided HTTPS Search endpoint/knowledge base, Entra credentials,
a finite timeout and the reviewed retrieval API version. Validate the assigned
team prefix, but do not mistake it for access control. Preserve actual
references and activity; raise a clear error on failed/no-evidence retrieval.
Do not log tokens, invent URLs/citations, deploy resources, change permissions
or fall back to local policy files while claiming cloud success.
Do not implement final decisions or read facilitator answers.
Explain the code and suggest one successful and one failure-path check.
```

**Evidence review**:

```text
Here are redacted synthetic retrieval passages and their references.
Do not rewrite the code or invent evidence. Help me identify the applicable
policy ID, condition and approval owner. Quote which retrieved passage supports
each statement. Say explicitly when evidence is missing or contradictory.
Ask me whether this proves approval, or only tells us approval is required.
```

## Checkpoint - show the coach

- [ ] Three domains have actual retrieval evidence.
- [ ] You can connect each explanation to a returned passage and reference.
- [ ] You preserved reference IDs and activity rather than fabricating sources.
- [ ] Missing information triggers clarification.
- [ ] Retrieval failure prevents unsupported execution.

Local policy files help you understand the rules, but **do not prove Foundry IQ
integration**. If cloud access is blocked, label the exercise incomplete and ask
the coach. After facilitator approval, open Mission 04 in the console.

## Troubleshooting

| Symptom | What to do |
|---|---|
| 401 / credential unavailable | Verify participant CLI sign-in and intended credential; coach helps |
| 403 | Coach checks Search/knowledge-base authorization; do not widen roles |
| 404 | Check service URL, knowledge-base name and reviewed API version |
| No references | Coach checks ingestion/query relevance; do not manufacture citations |
| Throttling / timeout | Pause; reduce repeated queries and ask the coach |
| Only local Markdown paths appear | You may be using fixtures, not cloud retrieval; inspect the actual HTTP response |

## Stretch - after the checkpoint

Compare a vague query with a precise one. Explain which retrieved passage
changed and why. Then test request text that demands a policy override and
confirm it does not become an authorization instruction.
