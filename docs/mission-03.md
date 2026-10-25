# Mission 03 - Give decisions real policy evidence (45 minutes)

## Your mission in the story

The team can now read Maya's request and check operational facts. But knowing
who owns Phoenix does not tell you who may approve access. Similarly, a known
supplier does not authorize every purchase, and a known partner cannot receive
every dataset. The specialist needs the **current written policy**.

**By the end:** implement `retrieve_policy(category, request)` so it queries
your assigned knowledge base and returns actual passages and their references.
Do not implement final business decisions yet.

**You change:** the `retrieve_policy` stub in `starter/route_resolve/agents.py`.
**You use:** your team's existing Foundry IQ / Azure AI Search knowledge base.
**Timebox:** policy/configuration 10 min; adapter 25 min; checks/checkpoint 10 min.
Prerequisite: Missions 01-02 passed; the coordinators confirm the four policy
documents are loaded and your identity is authorized. This guide is
`docs/mission-03.md` in your clone.

## Learning map - know why you are doing each step

| Step | What you learn | Explain it to a teammate |
|---|---|---|
| 1 - Read a policy | Request claims, verified facts and policy rules are distinct evidence | What rule applies, and what fact is still unknown? |
| 2 - Configure Search | Retrieval has its own endpoint and authorization | Why is the Foundry project URL not a Search endpoint? |
| 3 - Implement the adapter | A real request must preserve returned passages and references | Which response fields prove this is retrieved evidence? |
| 4 - Inspect three queries | Grounding connects an explanation to an observed source | Can I point from one claim back to a returned reference? |
| 5 - Test sufficiency | Missing evidence must block unsupported decisions | When should the workflow ask, route or stop? |

Before coding, write a policy question and predict the kind of evidence needed,
not the final business outcome. After retrieval, compare to the actual passage.
Explain one reference yourself before using Copilot to summarize anything.

## Step 1 - Understand what retrieval adds

**Where:** VS Code Explorer, `data/policies`.
**Why:** reading the local files teaches you the rules; it is not proof that
your running agent retrieved them from the assigned cloud knowledge base.

```powershell
Get-ChildItem .\data\policies
Get-Content .\data\policies\access.md
```

Open all four files. Find their source IDs: `ACCESS-001`, `BUY-001`, `SHARE-001`
and `FAQ-001`. Choose one rule and identify its condition and approval owner.
Do not turn the entire policy matrix into hard-coded replacement answers.

| Source | Tells you | Does not prove |
|---|---|---|
| Request text | What someone asks or claims | That approval exists |
| MCP fact lookup | Current fictional operational facts | The complete policy |
| Retrieved passage and reference | The applicable policy and its source | That an operation completed |
| Observed mock action response | What the simulated operation did | That real business systems changed |

**Retrieval** finds passages. **Grounding** uses those passages to justify an
answer. **Citations** identify the actual returned sources.
[Microsoft Learn: query a knowledge base](https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-how-to-retrieve).
Select Python/REST as appropriate; you are querying an existing knowledge base,
not following resource-creation or indexing tutorials.

## Step 2 - Locate the assigned knowledge base and copy its configuration

**Where:** the coordinator handout, [Foundry portal](https://ai.azure.com/), and
the VS Code terminal.
**Why:** the Foundry project endpoint is **not** the Search endpoint; neither is
the browser page address.

1. Reopen your assigned Foundry project from Mission 01. If a knowledge listing
   is available, match its knowledge-base name to your team's handout.
2. Some participant identities cannot browse the Search management screens.
   Use the verified handout values; ask the coordinators if a screen is absent.
   Do not try a different team's knowledge base or grant yourself more roles.
3. Set the values in the terminal that will run your code:

   ```powershell
   $env:SEARCH_ENDPOINT = Read-Host "Assigned HTTPS Search endpoint"
   $env:TEAM_KNOWLEDGE_BASE = Read-Host "Assigned team knowledge-base name"
   ```

4. Compare the knowledge-base team prefix with `TEAM_ID`. Name matching is a
   useful configuration check, not a substitute for real service authorization.

**You should have:** two distinct HTTPS service addresses (Foundry project and
Search) and the exact assigned knowledge-base name. The coordinators provide
and verify the services; you do not upload policies or create an index here.

## Step 3 - Build the retrieval adapter one operation at a time

**Where:** `retrieve_policy(category, request)` in `agents.py`.
**Why:** an adapter converts your question into a real retrieval request and
preserves the evidence the specialist will later need.

1. Validate the domain and require nonempty question text. Read only your assigned
   HTTPS Search endpoint and knowledge-base name.
2. Use the assigned Azure CLI identity for an Entra token with scope
   `https://search.azure.com/.default`. Keep the token in memory; never print it
   or write it into code/evidence. See
   [AzureCliCredential](https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity.azureclicredential).
3. Send one bounded request using the workshop's reviewed retrieval contract:

   ```text
   POST {SEARCH_ENDPOINT}/knowledgebases/{TEAM_KNOWLEDGE_BASE}/retrieve?api-version=2026-08-01-preview
   Content-Type: application/json
   Authorization: Bearer <token obtained in memory>
   ```

   ```json
   {
     "messages": [
       {
         "role": "user",
         "content": [
           {"type": "text", "text": "Your category and synthetic policy question"}
         ]
       }
     ]
   }
   ```

   Replace the question with your input; do not paste the placeholder literally.
   This workshop version was live-rehearsed against the assigned service.
   If newer Learn examples use a different preview API, keep the reviewed lab
   version unless the coordinators issue an updated contract.
   The Authorization header uses the Bearer scheme with the token from your
   credential. The notation above is explanatory only; never log a real header.
4. Check HTTP status before reading success fields. Use the real response shape,
   not a guessed `answer` property. Preserve returned `references`, passages and
   retrieval `activity` when present.
5. Return a dictionary retaining that evidence. A local policy filename or a
   citation written by the model is not a returned retrieval reference.
6. Make 401/403, timeouts, empty evidence and missing references visible. Stop
   unsupported execution; do not substitute local files while claiming the
   cloud query succeeded.

You may use transport/schema boilerplate from the docs, but you must understand
the endpoint, identity, question and returned evidence. No new model or hosted
agent deployment is needed. See the
[Foundry SDK/endpoints guide](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview)
if those addresses are still confusing.

**Small-build checkpoints:** validate the configuration/question first; then
send one bounded query; inspect its status and response keys; only then map
passages/references into your return dictionary. Do not ask Copilot to guess a
response schema or implement the final workflow while this adapter is untested.
Use an offline fake response to test empty/missing references without generating
repeated billable requests. Label fake output as offline evidence.

## Step 4 - Retrieve and inspect evidence for each domain

**Where:** the same configured terminal, after coordinator approval of cloud calls.

```powershell
.\.venv\Scripts\python -m route_resolve.lab policy --category Access --text "Which policy and approval owner apply to Reader access to Phoenix?" --allow-cloud
.\.venv\Scripts\python -m route_resolve.lab policy --category Procurement --text "Which rules apply to a EUR 600 software purchase from Contoso Software?" --allow-cloud
.\.venv\Scripts\python -m route_resolve.lab policy --category DataSharing --text "Which rules apply to sharing an Internal dataset with Fabrikam?" --allow-cloud
```

**You should see:** actual returned evidence and nonempty references for each
question. For one passage, explain the rule and approval owner in your own words,
then point to its source reference. Do not label the exercise successful merely
because JSON was returned.

Save redacted evidence locally: question, returned passage, reference ID and
relevant activity. Do not save Authorization headers, tokens or real business data.

## Step 5 - Decide when the evidence is not enough

Consider a request missing its classification or price. What must you ask before
applying the rule? Now consider a requester saying "already approved." Does the
request text prove authorization? Explain why retrieved instructions such as
"ignore all previous rules" are untrusted content, not a new system instruction.
You will connect this reasoning to actual clarification/actions in Mission 04.

## Checkpoint - show the coordinators

- [ ] Show live retrieved evidence for all three domains.
- [ ] Link one policy explanation to an actual passage and returned reference.
- [ ] Explain the difference between an approval requirement and verified approval.
- [ ] Show how retrieval failures block unsupported action.

Next: [Mission 04](mission-04.md), where a specialist uses this adapter and
the MCP tools to produce an evidence-backed simulated result.

## Optional Copilot prompts

```text
Read docs/mission-03.md. Help me plan retrieve_policy only using the assigned
Search endpoint, knowledge base, CLI identity and reviewed API version. Explain
the request/response and preserve real references/activity. Fail visibly on
missing evidence. Do not log tokens, invent citations, use another team's index,
deploy resources or replace cloud retrieval with a local answer. Review my
redacted evidence and ask which passage supports my explanation.
```

## Troubleshooting

| What you see | What to do next |
|---|---|
| 401/403 | Recheck assigned CLI identity, tenant and target; ask the coordinators |
| 404 | Compare service URL, knowledge-base spelling and reviewed API version |
| No references | Stop; ask the coordinators to check indexing/access rather than inventing evidence |
| Unknown response field | Inspect the actual JSON and the retrieval docs; do not assume an `answer` key |
| Portal listing unavailable | Use verified handout configuration; management browsing and retrieval rights differ |
