# CLB-011 author and source record

Revision1.0. November14,2026.
Learner file: [Verify automated removal and recover a write failure](../../lessons/CLB-011_Verify_Automated_Removal_and_Recover_a_Write_Failure.md).
Prepared from the saved [brief](../briefs/CLB-011_Automated_Removal_and_Recovery_Brief.md), teaching specification, environment record and planned [native C contract](../../lab-data/baselineC/README.md).

## New outcome and native setup

This is the first connected-target outcome. CSV reviews/task reconciliation cannot demonstrate it. Two ordinary AD users are linked to existing employee01/02, with four scoped direct memberships among three isolated test groups.

The C alias/specification [JSON](../../lab-data/baselineC/expected_memberships.json) is a planned set contract, not an upload, actual export or runtime report. Actual domain/DC, source/account/group DNs/IDs, effective write identity, service path and ACL evidence must be bound privately. No real endpoint, password, token or fabricated tenant GUID is supplied.

C is non-authoritative and matches AD employeeID to identity identificationNumber. A/B's seven canonical CSV files remain unchanged. The native pattern is intentionally four scoped memberships so a normal group and a separately permission-blocked group can be distinguished. It is separate from A's five-holding fixture.

The tested target fact is direct AD membership. Export/read-labelled group names do not prove a real reporting capability, token/session change or every effective authorization path. Primary/built-in/protected groups and nesting are excluded.

## Current primary checks

Checked November14,2026. This is a bounded documentation review, not an exhaustive release audit, inspected deployment or proven AD run.

| Primary source | Bounded use |
|---|---|
| [AD connector integration/features](https://documentation.sailpoint.com/connectors/microsoft/active_directory/va/help/index.html) | Connected AD account/group entitlement support and VA architecture. The older supported-features URL redirects here; no tenant feature activation is inferred. |
| [Connecting AD](https://documentation.sailpoint.com/connectors/microsoft/active_directory/va/help/connecting.html) | Direct Connection versus Flat File, actual VA/domain/authentication/TLS and optional path components, source scopes and explicit provisioning enablement. Current instructions say provisioning starts disabled. |
| [Required AD permissions](https://documentation.sailpoint.com/connectors/microsoft/active_directory/va/help/required_permissions.html) | Read and write/member authorities differ. Actual effective principal and chosen deployment permissions must be checked; ISC admin is not directory write authority. |
| [Account correlation](https://documentation.sailpoint.com/saas/help/accounts/correlation.html) | Attribute-based linking to existing identities, inspected associations and no new authoritative people profile. |
| [Search campaign creation](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html) | Explicit one-person/refined-entitlement scopes, Manager, preview/template, independent activation and fresh corrective campaign. The new campaign is not an undocumented replay control. |
| [Provisioning/errors/retries](https://documentation.sailpoint.com/saas/help/provisioning/index.html) | Only recognized retryable errors receive platform retries. The documented timing for those errors is not a universal wait or permission-error guarantee. |
| [Monitoring provisioning](https://documentation.sailpoint.com/saas/help/provisioning/tracking.html) | Activities, exact account/source/attribute details and Provisioning Activity report evidence. No universal Retry button is documented here. |
| [Search/account-request states](https://documentation.sailpoint.com/saas/help/search/index.html) | Nested account-request Pending/Committed, Retry, Failed and Finished meanings; Finished can carry success or failure, and terminal Failed is not treated as pending Retry. |
| [Microsoft member schema](https://learn.microsoft.com/en-us/windows/win32/adschema/a-member) | A group's member property records membership. No backlink write or invented schema attribute is used as the fault. |
| [Microsoft property-specific permissions](https://learn.microsoft.com/en-us/windows/win32/ad/setting-permissions-to-a-specific-property) | Property-specific allow/deny ACE support. The proposed fault is exact member write on one group, not all directory writes. |
| [Microsoft AD user administration](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage-user-accounts-in-windows-server) | AD Users and Computers setup requires actual directory authority, not simply ISC administration. |
| [Microsoft delegation](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/delegation-control-wizard) | Directory permission scope and authorized delegation context. No domain-wide role or permission change is prescribed. |

Connection schema, actual group values, GUI security labels/effective permissions, processing results, errors, classification, AD observations and successful recovery remain deployment/run checks. No literal LDAP error, same-controller identity or fixed time is fabricated.

## Controlled fault and recovery decisions

First prove e01 ExpOK removal through the connector while Read remains. Save actual operations and direct AD observations, then reconcile ISC by collection.

The AD operator adds only an explicit object-only member-write Deny on ExpFail for the actual effective write principal. Baseline security/effective authority is recorded first. Reads, inheritance, other principals and other properties stay intact. No credential rotation, service shutdown, OU/domain ACL change or provisioning-disable simulation is used.

The actual fault must show a denied membership write with e02 still present. An unrelated connection error or a successful removal does not pass the planned failure. No connector log or screenshot is invented.

Remove only the added entry. Do not blindly replace a saved entire ACL if other changes occurred. Observe whether the exact original request is pending/Retry or terminal Failed before submitting another operation.

For Retry, follow existing work after repair. For terminal Failed with no pending attempt, the planned recovery is a new explicit one-holding certification/reaffirmed removal using the documented creation path. Preserve original error and signed history and reference them from the new operation. Do not call the old operation successful merely because a later action achieved the target. If a supported new scope or operation cannot be established, record recovery incomplete.

A manual AD membership deletion would be manual remediation; it cannot pass the automated recovery outcome. Target membership must change from the real connector operation. Permission restoration alone is not that operation.

## Saved beginner read-through

The saved learner file was read in full. Campaign/certification/sign-off, AD, source/connector, OU, sAMAccountName, DN, VA, provisioning, correlation, entitlement, holding, remediation and ACE receive useful meanings near the action that needs them.

The prose connects reviewer UI, ISC provisioning, connector identity, AD authority/result and later collection without inventing internal queues or tables. The normal success precedes fault injection so an unrelated unready integration is not mistaken for a deliberate failure.

Three tables serve concrete comparisons: starting memberships, nested request states and expected membership phases. No diagram/screenshot quota is imposed. The reasoning exercise separates successful reading, repaired authority and an actual recovered write.

The language pass added local meanings before the actions, clear candidate/add-list checks, a direct-versus-manual fulfillment check and conservative group/account aliases. The reset preserves completed/error evidence and accounts for pending removals before restoring memberships. No fictional company, continuing character, learner source/course links or invented target result was added.

## Local expected sets and readiness

All SAM aliases fit the conservative20-character limit used for these objects. Both AD employeeID values match the original two people and their manager01 links. All membership rows reference the two declared users and three declared groups.

Expected scoped counts are four initially; three after normal removal; three after the blocked write; two after connector recovery, both Read; and four after resolved reset. The normal and fault removals are distinct and neither targets Read.

These are native-fixture calculations. They do not validate real ACL effects, connector authority, retry classification, successful writes, directory replication or a generated recovery campaign. Source/VA/AD readiness and every actual execution outcome remain uninspected.

## Cleanup and inherited boundaries

Verify fault ACE removal, all review finalizations and absence of pending/retrying/queued removes before the directory operator restores only the two original test memberships. Preserve Read, both native accounts, the source and OU as the reusable connected baseline. Keep failed/signed histories and retire only unused unscheduled011 templates. No deletion-as-cancellation or rollback is taught.

A five/B six and all original people/manager mappings remain unchanged. The native C contract is separate from the first CSV setup. No new CSV is added.

All inherited behavior questions retain their prior states. This lab does not test unsigned administrator completion, signed-review editing, role/account-filter edge cases or independent-profile overlap. A supported membership-removal feature is not a tested source or a complete release audit.

## Actual status

Local validation passed58 course files,48 Markdown documents,125 project-local relative links and57 consistent table groups across459 rows. Design/register agree on23 planning IDs and eleven complete learner files. All seven CSVs retain structure/reference integrity and exact expected-result checks; original A hashes are unchanged. Both JSON files parse. Native C aliases fit the chosen SAM constraint, match existing people/manager references and contain exactly four unique valid memberships. Independent set checks reconcile four→three→three→two→four, preserving both Read memberships and exact reset; fault scope is one declared object/property/principal binding, not a tested ACL. Earlier003 diagram-source and005–010 fixture checks pass. Fences, answer wrappers, whitespace and absence of learner source/course links pass. No directory, permission, retry, write or target outcome is verified by these local checks.

Authored/source/language reviewed:011 revision1.0. Native fixture authored, not executed. Actual AD source/OU/user/group creation, credentials/configuration, aggregation/correlation, permission changes, campaigns, decisions, operations, error capture, retries, recovery, screenshots, reset and independent learner tests:0. No repository, push or Pages action. The course remains local.
