# BaselineC: isolated connected AD membership lab

Version1.1. November16,2026.
For [CLB-011](../../lessons/CLB-011_Verify_Automated_Removal_and_Recover_a_Write_Failure.md), with possible later connected013/017 reuse.

## Actual status

This is a planned native directory setup contract. No AD domain, VA, IQService connection, source, account, group, credential, ACL change or operation has been created or inspected here.

[expected_memberships.json](expected_memberships.json) describes logical aliases and expected scoped sets. It is not an AD import, ISC upload template, actual export or tenant execution result. Bind actual directory/source references privately before execution. Keep passwords, tokens, real endpoints and raw ACL evidence outside the reusable package.

The original seven A/B CSV files are unchanged. Their CSV-backed account outcomes are separate from this native membership outcome.

## Objects and correlation

Use one authorized isolated training domain/OU, labelled ISC-CertLab. Prepare two ordinary user accounts and three ordinary non-nested security groups, avoiding primary/built-in/protected groups. All supplied SAM names fit20 characters.

| AD account alias | AD employeeID | Existing ISC identity | Initial direct memberships among the three test groups |
|---|---|---|---|
| certlab-ad-e01 | certlab-employee01 | certlab-employee01 | certlab-ad-read; certlab-ad-exp-ok |
| certlab-ad-e02 | certlab-employee02 | certlab-employee02 | certlab-ad-read; certlab-ad-exp-fail |

Source certlab-ad-lab is non-authoritative. Correlate AD employeeID to identity identificationNumber; the people CSV remains authoritative. Do not create a new people profile, overwrite uid/email/manager mappings or assume the AD account name equals the existing identity name.

Group labels describe test membership purposes. They do not establish a real reporting application's effective permission. Four means four scoped direct test memberships, not every directory group or permission held by these users. Existing built-in memberships remain out of scope.

## Connection and authority contract

Use the actual Microsoft Active Directory Direct Connection, with an authorized VA cluster and actual forest/domain/DC/authentication/TLS settings. Current connector documentation requires IQService for provisioning: prepare and verify that service, its connection settings and permissions before this write lab. Flat File cannot provide the write outcome. Provisioning is disabled by default; verify enabled state explicitly for this isolated source.

Restrict account and group collection to the test subtree and record group-membership search scope. Bind source owner, user/account/group IDs, DNs and objectGUID/SIDs privately. Inspect service accounts/effective group-write identity, required read/write privileges and the actual path used. Full ISC admin does not supply domain authority.

Complete aggregation/correlation checks, inspect both employee-manager01 links and verify all four direct memberships before campaign generation. No alternative role/profile/lifecycle/nested grant or other writer should restore removed test memberships.

## Fault boundary and expected phases

Record both export groups' baseline access-control entries and the exact effective write principal. Deny only member-property write on certlab-ad-exp-fail for that principal, on that object only. Preserve reads, inheritance, other principals and other object permissions. Remove only that added entry during recovery.

No domain/OU-wide Deny, service outage, shared credential change, global provisioning switch or arbitrary retry-configuration patch is part of the fault.

| Phase | Scoped membership count | Required evidence during an actual run |
|---|---|---|
| Initial | Four | Both users in their two specified groups. |
| Normal removal | Three | e01 absent from ExpOK, Read retained, e02 unchanged; matching successful connector work. |
| Permission-blocked removal | Three | Exact write failure and e02 still in ExpFail, with Read retained. |
| Recovery | Two | Both exports absent and Read retained; actual successful retry or explicit new connector operation. |
| Reset | Four | Original two memberships restored only after no pending/retrying removal can apply. |

A request in Retry is not treated as terminal Failed. Fix authority and follow existing retry when pending. A terminal failure can require a new explicit authorized removal instruction;011 uses a fresh narrowly targeted certification with linked evidence. Old failure history remains failed history.

## Restore and retain

Resolve active campaigns and outstanding writes before resetting. Remove only the injected ACL entry, preserve signed/error/recovery evidence, restore only the two removed native memberships and aggregate the connected source. Verify four test memberships plus unchanged A five/B six and original identity links.

Retain the isolated objects/source as the reusable native baseline. Routine deletion of accounts, source or OU is not required. A manually removed membership cannot count as successful automated recovery. A membership observation does not prove all downstream application authorization or existing sessions have changed.

## Separate role/profile variant in CLB-013

[CLB-013](../../lessons/CLB-013_Investigate_Access_That_Remains_After_Revocation.md) starts from these same four memberships only after faults/pending work are resolved and the supported automatic write path is verified. Any manual setup from012 needs its own approved readiness/restoration; do not assume it is automatic.

The intentional temporary model delta is an independent detected C Read+ExpFail profile and a direct-C-Read Standard role with only employee02 matching. No other model/grant is added. After checked profile Revoke/automatic-role Acknowledge, remove only e02 ExpFail through the connector; retain e02 Read and both e01 memberships. Expected four→three→four differs from011's normal/fault/recovery sequence. No additional native data/CSV is created.

Resolve work, disable/retire only013 temporary model, inspect any cleanup operations, then restore e02 ExpFail through the authorized directory operator and collect. Prove the exact original four memberships and unchanged A/B. No configuration, model, operation or runtime retention is established by this reuse.

## Existing-case evidence in CLB-015

[CLB-015](../../lessons/CLB-015_Build_an_Evidence_Trail_Someone_Else_Can_Verify.md) can index an actual ordinary e01 ExpOK removal only when real C operation/target evidence exists. Planned aliases/sets here are not evidence. Expected normal observation C4→3 retains e01 Read and e02 Read+ExpFail; eventual reset returns four. If the actual run also contains011's later fault/recovery/removal events, retain them in the timeline rather than implying an uninterrupted three-to-four reset. No new native operation, manual removal, source configuration or target observation is introduced by this evidence-only use.

## Separate connected capstone in CLB-017

[CLB-017](../../lessons/CLB-017_Complete_and_Defend_an_Independent_Certification_Project.md) uses these original four memberships only after actual automatic-write readiness, existing account correlation, clear prior work and absence of old ACL/manual/model changes. It adds no onboarding, group, identity or forced fault. The learner request reviews the two non-Read test memberships and supplies an unsigned-work handover/update; the author assessor guide holds its expected outcome.

CSV proof cannot pass the connected assessment. Actual connector work and direct directory observations, retained memberships, collection and resolved reset to the exact four are required. No learner attempt, native operation or passed assessment has occurred.
