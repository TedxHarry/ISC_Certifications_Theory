# BaselineB: source-owner review with the owner's own account

Version 1.0. November 14, 2026.
For [CLB-004](../../lessons/CLB-004_Review_a_Source_and_Separate_the_Owners_Access.md).
Local synthetic fixtures; no tenant import or observed routing.

## Environment and reason for isolation

Reuse the five people identities and manager sessions defined by [baselineA](../baselineA/README.md). Do not import another people file or create a profile for this application source.

Prepare one fresh Generic/manual-upload source: certlab-owner-reports-csv. This is an isolated copy of the simulated reporting data, with manager02's account added. It keeps the existing003 report source and account set unchanged and avoids account deletion as a reset requirement.

BaselineB is a third CSV source after the initial two-source setup; it is not another connected application or an AD prerequisite. Record actual Generic mode/dependencies and full templates before import.

## Files and contract

| File | Data rows | Meaning |
|---|---|---|
| owner_review_accounts.csv | 6 | Initial four accounts/six holdings, including the source owner's Read. |
| owner_review_entitlements.csv | 2 | Read/Export definitions on this new source. |
| owner_review_accounts_after_employee02_export_removal.csv | 5 | Expected004 result only; not initial data or a tenant export. |

UTF-8 CSV, one header, comma separators. Account ID id; Account Name name. Those fields and employeeNumber are scalar text; groups is a multi-valued entitlement attribute using the actual supported single entitlement association. Adjacent repeated rows model multiple values; their scalar fields agree.

The narrow canonical headers define values, not universal upload templates. Preserve the new source's complete downloaded account/catalogue templates, extra columns and required fields. Adapt private copies before upload. Do not upload these files to certlab-reports-csv or certlab-people-csv.

The new source is non-authoritative. Its account employeeNumber matches existing identity identificationNumber. Bind source ownership to the actual certlab-manager02 identity in Base Configuration; no CSV column assigns that ownership.

Catalogue IDs exactly match groups values. The same literal IDs on baselineA and B do not make one global entitlement. Match source plus account/entitlement value in every observation.

## Subjects, reviewers and need

| Account | Existing identity | Initial holdings | Expected review responsibility |
|---|---|---|---|
| certlab-account01 | certlab-employee01 | Read/Export | manager02, as source owner. |
| certlab-account02 | certlab-employee02 | Read/Export | manager02, as source owner. |
| certlab-account03 | certlab-employee03 | Read | manager02, as source owner. |
| certlab-account04 | certlab-manager02 | Read | manager01, through the documented self-certification separation and known manager link. |

The actual generated recipients and grouping must be inspected. Six holdings do not imply a universal number of certification objects. Manager01 has no account on this selected source; their absence as a review subject does not prevent independent review responsibility.

Business evidence supports employee01 Read/Export, employee02 Read only, employee03 Read and manager02 Read for a defined reporting-oversight task. Source-owner status by itself is not approval evidence.

Expected choices are five Approve/one Revoke. The rejected holding is employee02 Export. Expected collected result: four accounts/five holdings, with account01 Export and all four Read holdings retained. Both definitions remain.

## Reset and limits

Keep baselineB source/account04 as the intended004 fixture. After preserving campaign/task/file evidence and reconciling outstanding work, restore the full private original B account file and verify six holdings. Existing A files, people records, manager links and sources are unchanged.

Do not upload A into B to remove account04, reset an authoritative source, delete an identity or treat campaign deletion as rollback. Reuse the dedicated B source only after verifying its exact setup and separate campaign history.

No email/password data is needed in these account fixtures. Actual reviewer sessions still require the approved private registration setup. Files and local calculations do not prove authentication, independent assignment, task routing, external access removal or a successful tenant run.

## Staged manual-task use in CLB-012

[CLB-012](../../lessons/CLB-012_Complete_Manual_Removal_and_Verify_Each_Result.md) independently rejects employee02 Export on both A and B. After only A is fulfilled, B remains six holdings and its removal remains outstanding. Use B's own complete private template for the later five-holding result; preserve account04 owner Read. A's four-holding comparison has only three accounts and cannot stand in for B. Close actual tasks only when their full requested scope is fulfilled; resolve work before resetting B six/A five. No new CSV or tenant result is introduced.

## Capstone scope in CLB-017

[CLB-017](../../lessons/CLB-017_Complete_and_Defend_an_Independent_Certification_Project.md) reviews only employee01/02's existing Export holdings on A and B under its own supplied facts. B's Read holdings, employee03 and owner account04 stay outside decision scope and must remain. Manager02 owning this source does not make the selected employees' Export their own access; verify actual eligible handover from the original manager and record real actors.

The learner derives complete source-specific changes and evidence rather than treating this fixture's expected file as an observed result. Preserve histories and restore original B six only after all work is resolved. No new file or tenant result is supplied.
