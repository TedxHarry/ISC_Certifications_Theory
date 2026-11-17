# CLB-011 brief: prove a connected removal and recover a write failure

November14,2026. Saved before learner prose.
Learner filename: CLB-011_Verify_Automated_Removal_and_Recover_a_Write_Failure.md.

## Distinct task

Move from CSV reconciliation to observed AD group-member changes. Compare a normal automatic removal with one blocked group write; restore only the injected permission fault and establish a real connector-mediated recovery. An accepted/signed review, successful read or CSV edit cannot pass this outcome.

Use baselineC: two ordinary AD users linked to existing employee01/02, one retained test group and two separate removable test groups. Four scoped direct memberships, not the users' entire AD permission inventory. A/B remain unchanged.

## Required setup and native fixture

Source certlab-ad-lab is an isolated Microsoft Active Directory Direct Connection using the actual prepared VA/domain/authentication/TLS/IQService path as needed by the chosen deployment. Provisioning is disabled by default in current connector documentation and must be enabled for the test source. Full ISC admin does not establish AD write authority.

Dedicated OU ISC-CertLab; ordinary accounts certlab-ad-e01/e02, employeeID equals the existing certlab-employee01/02 identity identificationNumber. Non-authoritative AD source; no duplicate identity profile or people CSV.

Three non-privileged, non-nested security groups: certlab-ad-read, certlab-ad-exp-ok, certlab-ad-exp-fail. e01 in Read+ExpOK; e02 in Read+ExpFail. Names fit conservative 20-character SAM limits. No primary/protected/built-in group is used for removal.

BaselineC README/JSON are a planned native setup contract, not an import or tenant export. Actual source/account/group IDs, DNs/SIDs/GUIDs, domain/DC endpoints, effective write identity and ACL snapshot are bound privately.

## Normal write

First campaign certlab-011-normal-run01: employee01 only, Refine C Read+ExpOK, Manager reviewer manager01. Current need retains the read-named group membership and ends the ExpOK test membership. Approve Read, Revoke ExpOK, Finish. Track exact per-source account/attribute operation and verify direct AD membership absent, Read present, e02 unchanged. Refresh collection and reconcile three remaining scoped memberships.

Group names are labels for test memberships. There is no claim that they grant real report-reading/export capability in an application.

## Controlled fault

Use an authorized directory administrator and the actual effective membership-write principal, not an assumed bind account. Inspect baseline permissions on both export groups.

On only ExpFail, add one explicit object-only Deny for that principal's Write Members/member-property write. Preserve read, inheritance, other principals and all other permissions. Snapshot/record before and exact added entry. Do not stop VA/IQService/DC, rotate credentials, disable provisioning or edit domain/OU-wide ACLs.

Verify effective denial on this object and continued reads. No protected group or other writer/assignment should interfere. If the GUI cannot identify the exact principal/property/scope, do not improvise a broader fault.

Second campaign certlab-011-fault-run01: employee02 only, C Read+ExpFail. Approve Read, Revoke ExpFail, Finish. Capture actual write error and status, observe ExpFail remains and Read remains. Expected scoped membership count stays three. A success or unrelated error does not pass the permission-failure exercise.

## Recovery without inventing a retry

Remove only the added Deny entry; compare effective authority/ACL with the saved baseline. Fixing authority is not the same as submitting another operation.

Inspect nested account request state, not only overall activity/campaign. Retry means another attempt is scheduled; follow that existing work without a duplicate. Current platform guidance retries recognized retryable errors, not every permission failure; no guaranteed hour clock, Retry button or custom retryableErrors patch is taught.

If the exact request is terminal Failed and will not retry, ensure no pending removal remains, collect current still-held membership and prepare one fresh targeted certification certlab-011-recovery-run01 for employee02 ExpFail only. Include original campaign/activity/error references in the new reason, reaffirm Revoke with the actual reviewer, Finish and observe a new successful connector operation. Preserve the old failed operation as failed history, not relabelled success. If no supported new preview/operation can be established, recovery stays incomplete.

Manual AD deletion of the membership would be manual remediation, not automated recovery. Do not use it to manufacture a pass.

## Completion and reset

Expect both removable memberships absent and both Read memberships retained: four→three→three after fault→two after recovery. Verify on the actual connector/DC path and account for replication if a different controller is read. A refreshed ISC record is the later reconciliation, not the independent AD observation.

Finish all actual reviews, preserve original failure and recovery evidence, resolve pending/retrying/queued writes before reset. Restore only the two test memberships via the AD operator after no old removal can fire; collect and prove four scoped holdings. Remove the added ACL fault, restore any source settings actually changed through scoped procedure, retain native objects for later013/017, preserve signed histories and retire only unused011 unscheduled templates.

OQ-01/02 and other inherited cases remain untested. No actual AD source, account, group, write, ACL, campaign, retry, error or recovery has been executed. No CSV added/changed; no repo/publication.
