# CLB-011 beginner-readability revision

Revision 1.1. November 16, 2026.
Learner: [Verify automated removal and recover a write failure](../../lessons/CLB-011_Verify_Automated_Removal_and_Recover_a_Write_Failure.md).
The original [revision1.0 record](CLB-011_Revision_Record.md) and [brief](../briefs/CLB-011_Automated_Removal_and_Recovery_Brief.md) remain historical.

## Complete author reading

Read the full original learner and the full saved revision, from the opening through the request-state comparison, reasoning exercise and reset. Reconciled its procedure with the planned native [C contract](../../lab-data/baselineC/README.md). This is an author reading, not an independent beginner test or tenant execution.

## Useful changes

Source aliases A/B/C and the full names behind Read/ExpOK/ExpFail now precede their use. Direct membership means an account explicitly listed in the group; short group labels do not imply application authorization. The authoritative people source and non-authoritative AD account source have separate purposes.

Provisioning, account correlation, entitlement and aggregation meanings support the connection checks. The example follows the actual planned employeeID match. The source owner, technical account, employee account and effective write principal are distinguished. A supplied review instruction covers both users before decisions begin.

The fault explanation starts with Members versus Security: belonging to a group is different from being allowed to change its member list. Only then does it introduce member-property writes, ACL and ACE. The read-preserving, object-only fault remains unchanged. Successful reads, repaired write authority and an actual recovered operation remain separate checks.

Recovery uses plain descriptions of Failed with no further attempt. Existing Retry work is followed without issuing duplicate removal; a failed request with no pending attempt uses a separately linked corrective review only if supported fresh work can actually be established. No universal Retry button, permission-error classification, retry duration or successful result is promised.

Template and preview meanings, separate references, Manager/Maintain choices and unused run naming are explicit. The reset heading uses direct language while retaining outstanding-write checks and preservation of signed/error history. The original three useful tables and reasoning exercise remain; no diagram, extra scenario or lab was added.

## Bounded current-source check

Checked November 16, 2026.

| Primary source | Scope of this pass |
|---|---|
| [Connect SailPoint and AD](https://documentation.sailpoint.com/connectors/microsoft/active_directory/va/help/connecting.html) | Direct Connection, prepared VA, source scopes, provisioning disabled by default and IQService required for provisioning. |
| [AD required permissions](https://documentation.sailpoint.com/connectors/microsoft/active_directory/va/help/required_permissions.html) | Technical service account and separate member read/write authority; actual permissions depend on the use case. |
| [AD member attribute](https://learn.microsoft.com/en-us/windows/win32/adschema/a-member) | Group membership list changes when a user is added or removed. |
| [Microsoft ACL explanation](https://learn.microsoft.com/en-us/windows/win32/secauthz/access-control-lists) and [property-specific permission entries](https://learn.microsoft.com/en-us/windows/win32/ad/setting-permissions-to-a-specific-property) | Allow/deny entries for a principal and a property-scoped permission, supporting the narrow fault explanation. |
| [Account activity and nested request states](https://documentation.sailpoint.com/saas/help/search/index.html) | Pending/Committed, Retry, Failed and Finished meanings; overall activity and individual request results are different levels. |
| [Provisioning overview](https://documentation.sailpoint.com/saas/help/provisioning/index.html) | Provisioning changes access; only recognized retryable errors receive the documented retry handling. |

The earlier conditional IQService wording was too loose for a provisioning lab. The current learner and baselineC README now make the documented prerequisite explicit. This is a current contract clarification, not proof that IQService or AD has been installed, configured or tested. The JSON fixture remains unchanged.

Unchanged campaign creation, reviewer controls and retirement retain their earlier bounded source review. Actual connection components, effective principal, narrow Deny effect, exact error classification, fresh corrective review eligibility, operation state and target results require tenant/AD evidence. All inherited product questions remain open.

## Planned outcome and evidence

C starts with e01 Read+ExpOK and e02 Read+ExpFail: four direct test memberships. Normal e01 ExpOK removal leaves three. Blocking e02 ExpFail member write leaves the same three. Connector recovery removes only e02 ExpFail, leaving both Reads. After all outstanding removals are resolved, the authorized training reset restores exactly four.

Each actual run must preserve normal-operation evidence, the isolated fault entry, original error, actual target observations with controller/time, permission restoration and either the existing retry or the separately linked new operation. A manual group deletion, changed CSV, successful collection or restored permission alone cannot pass automated recovery. A remains five holdings and B six throughout.

## Local verification

Saved-file validation passed across 119 reusable files: 97 Markdown files, 338 resolving project-local links, 120 consistent table groups and 927 table rows. Design/register reconcile all 23 learner IDs. All 14 CSVs and 5 JSON assets/contracts pass; original baselineA input hashes remain unchanged.

The existing native-fixture checks reconcile two users, three groups and the four→three→three→two→four membership sequence. Both retained Read memberships and the exact planned reset remain; source/group aliases, employeeID links and the object-only read-preserving fault contract are consistent. These are planned-data checks, not tests of an actual ACL, error, recovery campaign or connector operation.

No executable collector or canonical CSV/JSON asset was changed. The collector's earlier 25-test offline suite was not rerun for these prose changes. Tenant execution and independent learner testing remain separate, pending work.

## Actual state and next work

CLB-011 revision1.1 is authored and author/source/language reviewed. The last user-reported tenant status is maintenance. Actual directory setup, ACL changes, connection/correlation checks, campaigns, decisions, sign-offs, errors, retries, corrective operations, target observations, screenshots, resets, repeated runs and independent learner tests remain 0.

Thirteen of the 23 complete fresh author readings are now covered: CLB-001 through013. Next is CLB-014, followed by015–017 and the six specialist units: ten readings remain. CLB-012 and013 were already covered earlier in this pass. No repository, push or Pages action; all 23 guides remain authored locally.
