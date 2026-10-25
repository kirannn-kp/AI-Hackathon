# FAQ-001 - FAQ and approval matrix (fictional Contoso Manufacturing)

| Request | Approval owner | Before approval |
|---|---|---|
| Project Contributor / non-member Reader | Project owner | Route |
| Privileged Owner | Security | Escalate |
| Approved software above EUR 100 up to EUR 1,000 | Manager | Route |
| Unapproved software / over EUR 1,000 | Finance | Escalate |
| Internal data to approved partner | Data owner | Route |
| Confidential data / unapproved partner | Security/Legal | Escalate |

Resolve means no new action is needed, for example access already exists.
Execute means a pre-authorized **mock** operation was completed.
Route means clarification or approval is still needed.
Escalate means a privileged or policy-sensitive review is needed.

Every result must include request ID, category, outcome, explanation, citations
and `simulation: true`. No sensitive company data may be entered.
Mock status records are isolated per server process and disappear on restart.
