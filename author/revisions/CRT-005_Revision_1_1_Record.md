# CRT-005 revision 1.1: making source access information understandable

November 11, 2026. Local revision; publication not performed.

Learner: [How application access becomes reviewable information](../../lessons/CRT-005_From_Application_Access_to_Reviewable_Information.md).
Editable diagram: [account data, entitlements and identity](../../assets/CRT-005_Account_Data_Entitlements_and_Identity_Link.txt).
Historical evidence: [original revision record](CRT-005_Revision_Record.md).

## Brief prepared before drafting

Continue the existing-lesson explanation pass with CRT-005 under teaching specification 1.1. Preserve its title/ID/filename and original teaching purposes. Keep local CRT-002/003 1.1 and all other learner/asset/revision files intact. No new topic or publication is part of this request. After this rewrite, CRT-006 and CRT-007 remain to revise; CRT-009 stays parked.

Build the explanation around the original reporting account rather than abstract data labels: report-014, login reports-user-14, staffNumber 1007 and two returned group values RPT.VIEW/RPT.EXPORT. Explain field/attribute, identifying values, schema interpretation, memberships as entitlement values, account aggregation, catalog details/type/linkage, unique correct identity match and actual generated review. The example names are illustrative connector data, not universal source fields or an API payload.

Preserve collection versus grant, read versus write, ordinary text versus entitlement data, operation success versus complete/correct data, catalog existence versus account holding, account matching versus need judgment and source observation versus generated review time. Preserve optimized skipped-record correlation and supported unoptimized reexamination without a destructive reset or universal processing order. Use locally explained terms before depending on their relationships.

Main conditions: identity already exists with staffNumber 1007; configured comparison uniquely finds the correct identity; account schema uses accountId/login and multi-valued entitlement attribute groups; groups type and RPT.EXPORT identifier match the catalog within the reporting source. The resulting direct entitlement is individually eligible, selected for review, outside retaining/containing packages or automatic requirements, with a suitable non-self reviewer. Supplied observation times 08:00/09:00/10:00 illustrate chronology, not runtime guarantees.

Preserve the independent payments case: pay-088 has permissions containing INV.APPROVE, but the supplied extraction/schema membership path expects groups. Catalog definition and correct identity are present, held value/review item are missing. Locate the account-data mismatch before catalog refresh; verify actual membership and generated inclusion after appropriate correction. A later accurately empty holding can coexist with the catalog definition.

No fictional biography, external learner sources, prerequisite statements or fixed content quotas. Tables and diagram should explain actual values/connections; they are not mandatory layout counts. No source schema mutation, new API syntax, live tenant result or exhaustive update audit is claimed.

## Primary-source checks before drafting, November 11, 2026

| Official source | Checked teaching scope and limit |
|---|---|
| [Source configuration](https://documentation.sailpoint.com/saas/help/sources/config_sources.html) | Source/connector, direct versus file collection and read/write separation. No connector-specific setup or permission guarantee. |
| [Account schemas](https://documentation.sailpoint.com/saas/help/accounts/schema.html) | Attributes, identifying values, multi-valued/entitlement interpretation and matching attribute/type/entitlement identifier in the documented linking model. No universal field names or advice to change identifiers. |
| [Account loading](https://documentation.sailpoint.com/saas/help/accounts/loading_data.html) | Actual collection, filters/freshness, optimized skipping and unoptimized correlation reexamination. No fixed duration or source-wide reset. |
| [Entitlement aggregation](https://documentation.sailpoint.com/saas/help/loading_entitlements/aggregating_entitlements.html) | Supported access-object collection and account-only exceptions; separate aggregation is not universal. |
| [Account correlation](https://documentation.sailpoint.com/saas/help/accounts/correlation.html) | Configured account/identity comparison and unmatched accounts; correct unique match is supplied, not a universal ambiguity/fallback algorithm. |
| [Managing entitlements](https://documentation.sailpoint.com/saas/help/access/entitlements.html) | Entitlement records, source context and descriptions distinct from a particular account's membership. Actual business meaning is supplied from the application's configuration. |
| [Understanding certifications](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html) | Individual item eligibility depends on access-model origin/containment. The example supplies a narrow reviewable entitlement; no universal action/timing claim. |
| [Manager/source-owner campaigns](https://documentation.sailpoint.com/saas/help/certs/starting_campaign.html) | Captured review information and later observations can differ; no automatic rewriting of generated review contents promised. |

The four data/eligibility/snapshot references reused from today's CRT-003 checks remain current for these claims; source configuration, schema, entitlement aggregation and entitlement management were reopened for this revision. All seven product questions remain open. No tenant test or release-completeness claim is added.

## Coverage preserved in the saved revision

All 26 teaching purposes in the historical revision 1.0 record remain. This is semantic reconciliation against the saved sections, not a keyword-only check.

| Original purpose | Saved explanation in revision 1.1 |
|---|---|
| 1. Existing account and identity | Begin with what the application already knows: identity already exists; reporting account already holds access. |
| 2. Concrete values and business meanings | Same section: original four-row table, report-014, reports-user-14, staffNumber 1007, both RPT memberships and application-established meanings. Group membership is explained locally. |
| 3. Collection versus grant | Same section: collecting the memberships describes access already present. |
| 4. Source versus application | Use a source and connector: source settings in ISC versus the actual external account. |
| 5. Connector and collection paths | Same section: direct/file collection, reading versus authorized supported change and possible manual removal. |
| 6. Attribute and schema | Explain what each returned field means: staffNumber name/value, schema interpretation. |
| 7. Account ID, Account Name and source | Same section: accountId/login uses, exact account and source context; no identifier-change procedure. |
| 8. Entitlement and multiple memberships | Same section: group values as entitlements, multi-valued meaning and two values on one account. |
| 9. Ordinary fields versus held access | Same section: staffNumber has a different job; actual returned field and supported interpretation must agree. |
| 10. Account aggregation | Account aggregation tells ISC what this account holds: collection through the source and interpreted account record. |
| 11. Completed operation versus included data | Same section: inspect report-014/values; account filter and field configuration can miss expected data. |
| 12. File freshness | Same section: reimporting an old file does not make the observation current. |
| 13. Entitlement catalog and aggregation | Entitlement details explain the access item: object definition, readable description and supported object collection separate from account holdings. |
| 14. Entitlement linkage | Link the account value: marked entitlement attribute, groups attribute/type match, RPT.EXPORT value/identifier match and source context. |
| 15. Catalog existence versus holding | Same two sections: description cannot supply missing membership; separate entitlement aggregation is not universal. |
| 16. Correlation | Match the account: configured account/identity staffNumber comparison uniquely matches the correct existing person. |
| 17. Ownership versus need/grant | Same section and campaign explanation: personnel number identifies the person; it does not establish current export need or grant access. |
| 18. Wrong or absent association | Same section: accurate permissions under wrong person; uncorrelated account can still hold actual access. |
| 19. Configuration versus reexamination | Changing a matching rule: optimized skipping, supported unoptimized correlation reexamination and actual resulting-link verification. |
| 20. Review meanings and eligibility | Check what the campaign actually presents: campaign, assigned certification, reviewer, review item, access model and certifiable access explained before relying on them. |
| 21. Main review conditions | Same section: individually reviewable export, no containing package or automatically required access, selected person/access and suitable non-self reviewer. |
| 22. Dependency visual | Put the connections together: editable inline/text-asset diagram, explained as information dependencies rather than fixed internal batch phases. |
| 23. Observation chronology | Compare the time: original 08:00 collection, 09:00 generation, 10:00 target removal, later updated account information; no runtime promise. |
| 24. Historical versus current evidence | Same section: old review information need not disappear; old absence cannot disprove a newer grant. |
| 25. Connection-specific investigation | Find the connection: extraction/schema, wrong association, catalog without holding and correct data without selected eligible review item. |
| 26. Independent transfer and changed fact | Different source: pay-088, permissions INV.APPROVE versus groups expectation, catalog present, actual holding missing; supported correction and account/review verification, then accurate absent membership with definition retained. |

Routine task foundations remain task 2 (source data/ownership readiness), 7 (generated relationship), 13 (missing or mismatched access), 21 (newer account information versus older observations) and 22 (records/times needed for evidence). COV-04 and basic COV-05 remain the primary coverage; supporting review/eligibility/timing introductions do not complete later implementation units.

## Saved-file author review

The saved lesson was read in contiguous portions and checked against the original purposes. The normal account-data path precedes mismatch diagnosis. Account membership and entitlement-object details have separate explanations before their linking conditions. Attribute names and values are connected to the original table. Correlation explains the two compared values and unique intended identity rather than relying on a definition alone.

During the final language pass, ISC was expanded at first use, group membership received a direct explanation, and the certification/reviewer/item meanings were split into concrete steps. Access-model wording now explains a larger package and automatic requirement before their review consequences. Compressed generation-context wording was replaced with the actual question about information captured when the review was generated. All original cases, conditions, timings and the different-field transfer remain.

The diagram and prose distinguish dependencies from a universal internal job sequence. The final payments explanation identifies the account-data mismatch before recommending inspection; it separately asks for actual account membership, identity and generated review evidence after correction. The later empty-membership branch prevents treating a retained catalog record as a renewed grant.

This is an author reading from a beginner's perspective, not an independent learner observation. The user's positive CRT-004 readability feedback does not establish mastery of this revision. Independent learner assessment and hands-on tenant execution remain pending.

## Saved-package verification

Final local checks completed November 11, 2026:

- All four existing navigation tests passed.
- The local site verifier passed for all eight learners: 876 normalized content units, eight diagrams, eight tables and eight editable assets. This was a local consistency check, not a live-site comparison or graphical browser inspection.
- The saved inventory contains 64 authored/site files and 39 Markdown documents. All 220 relative Markdown links resolve. All 67 table groups have consistent columns across 921 rows; code fences are closed.
- The CRT-005 inline diagram exactly matches its editable text asset. All 23 originally emphasized meanings remain explicitly emphasized; the 26-row semantic reconciliation above separately checks substantive coverage.
- The design and candidate register retain the same 50 ordered topic IDs. Eight learner files exist; no CRT-009 stub was created. The working terminology remains 94 distinct meanings, and all seven product questions remain open.
- The pre-turn SHA-256 inventory confirms 54 existing files are byte-identical, including earlier learners/assets, local CRT-002/003 rewrite records, historical records, publication evidence, manifest and reader/verification implementation. Only the target learner/asset and seven current metadata files changed; this new revision record is the only added file.
- Whitespace checks passed. Learner prose contains no external source links, fictional character names, TODO/TBD placeholders or revision footer.
- Course metadata consistently sets CRT-006 next, then CRT-007: two revisions remain, separately from 42 unwritten topics.

The local course now has CRT-001/002/003/004/005 at revision 1.1 and CRT-006/007/008 at 1.0. CRT-002/003/005 1.1 remain unpublished. No commit, push or deployment was performed; the November 2 published snapshot remains unchanged. Source/author/local checks do not establish independent learner mastery or a tenant result.
