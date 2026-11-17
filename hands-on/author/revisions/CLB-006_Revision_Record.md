# CLB-006 author and source record

Revision1.0. November14,2026.
Learner file: [Compare campaign filters and review units](../../lessons/CLB-006_Compare_Campaign_Filters_and_Review_Units.md).
Prepared from the saved [brief](../briefs/CLB-006_Filters_and_Review_Units_Brief.md), practical teaching specification, environment record and unchanged A/B data.

## Teaching task and boundaries

The distinct task is a preview-only comparison: hold the B starting set constant, change inclusion to exclusion, inspect what is included/omitted and explain why filtering is not revocation. Then create one temporary native access profile to examine detection and the review unit it produces. This is not another complete decision/removal lab.

The administrator works only with the existing synthetic identities/sources and temporary006 objects. No campaign is activated, no decisions or sign-off are entered and no account-file permission is edited. Three filters, unstarted previews, their unscheduled saved configurations and one native profile are planned temporary writes during a future run. Identity processing is limited to employee01/02/03 and manager02. None of those operations has been performed here.

The original [A package](../../lab-data/baselineA/README.md) and [B package](../../lab-data/baselineB/README.md) supply all inputs. No new CSV or connected source is added. The existing two same-name source catalogues make source identification useful without creating unnecessary new fixtures.

## Primary documentation checked

Checked November14,2026. These are current documentation checks for the taught path, not a complete release audit or inspection of the user's tenant.

| Primary source | Bounded use in this lesson |
|---|---|
| [Using campaign filters](https://documentation.sailpoint.com/saas/help/certs/campaign_filters.html) | Filter builder, inclusion/exclusion, OR conditions, source-specific entitlement display-name matching, access-profile criteria and deletion. Its entitlement example expressly distinguishes a holder's profile association from a standalone entitlement. Role/account examples are not generalized into unverified multi-account outcomes. |
| [Starting campaigns from Search](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html) | Access Items entry; Specific Access Items selection; Refine Access Items; a separate Using a Campaign Filter entry; Manager assignment; preview/template choices and separate activation. Entitlement-selected holders can differ once the profile represents their access. |
| [Understanding certifications](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html) | Standalone entitlements, detected/requested profiles, role-origin representation, automatically assigned versus requested roles and lifecycle-required access boundaries. |
| [Managing access profiles](https://documentation.sailpoint.com/saas/help/access/access-profiles.html) | One-source package, creation/contents, detection during identity processing, enablement with requests off, deletion and retained account entitlements. Existing certifications can still reference a deleted profile, so the lesson retires its unstarted previews before deleting it. |
| [Processing identity data](https://documentation.sailpoint.com/saas/help/setup/identity_processing.html) | Selected identities' Process Identities action, actual operation/result checks and the distinction from a broader Apply Changes action. No guaranteed processing time or immediate indexing result is claimed. |
| [Configuring access requests](https://documentation.sailpoint.com/saas/help/requests/config_ap_roles.html) | Allow Access Requests remains off. Enabling the model is distinct from making it requestable; no request or grant is used to force detection. |
| [Completing campaigns](https://documentation.sailpoint.com/saas/help/certs/completing_campaigns.html) | Scoped deletion of unused campaign instances and saved configurations; preserve evidence and reconcile actual work before cleanup. Deletion is not taught as access restoration or delivery cancellation. |
| [Building search queries](https://documentation.sailpoint.com/saas/help/search/building-query.html) | The candidate lookup uses * and explicit manual additions; it is not a command to certify all tenant results. |

The profile owner's manager02 alias identifies an already prepared person; it does not imply the owner is the reviewer. Manager is explicitly selected for the previews. Reviewer routing and certification-object grouping remain actual-run checks.

## Saved beginner read-through

The saved learner file was read in full after writing. It introduces certification/campaign, identity, source, entitlement and holding before the first comparison. Inclusion/exclusion meanings precede their builder settings. Preview, template, profile and identity processing have local explanations before relying on their effects.

The language pass replaced compressed filter wording with one condition, named the builder actions and explained processing as rechecking a person's data/packages. It supplies the starting account table, manager relationships and exact baseline file names rather than assuming an earlier run ended correctly. Technical terms support the action instead of becoming a glossary list.

The causal chain is explicit: fixed B rights → direct review set → one filter mode → inspected preview; then unchanged rights → profile definition → selected processing → observed association → fresh filter-based review. Reusing an explicit entitlement selection after detection would confound the profile test, so the lesson explains why a fresh entry is necessary.

Three tables are used because they compare different facts: initial account permissions, two filter results and changed review representation. No extra screenshot or diagram was added to meet a quota. The reasoning exercise asks the learner to investigate an empty direct-entitlement review without duplicating account data.

## Expected set reconciliation

B contains six account-permission holdings across four accounts. Export inclusion has two holdings; Export exclusion leaves the four Read holdings. The sets are disjoint and together recover B's original six. Source B OR Export B would include the whole B set, so it is not substituted for a conjunction.

Employee01/02 each hold both profile entitlements; employee03 and manager02 each hold Read only. After actual verified detection, the expected review model is two profile holdings plus two standalone Read holdings. That is four review units covering six account rights, not four certification objects. The corresponding standalone Export inclusion is expected to have no work; the profile inclusion has two holdings. An empty generated record is not called a completed business review.

These are local fixture calculations and source-supported expectations. They do not establish runtime filter behavior, profile detection, successful processing, indexing or a generated campaign result.

## Restoration and unresolved checks

Retain comparison evidence and object IDs. Confirm every006 campaign was never activated and has no decisions/removal work, including any empty generated record. Delete only these unused instances and their unscheduled configurations before removing the profile. If actual activation or another dependency exists, reconcile that work rather than using routine cleanup as rollback.

Delete only the unused006 profile, reprocess the same four identities and inspect absence of the profile plus B's six direct holdings. Preserve A's five rights. Remove the three temporary filters after their configurations are retired. No people, accounts, sources or catalogues are deleted.

OQ-06/08 Role/account-filter edge cases and OQ-07 independent-profile overlap remain open. The ordinary role/lifecycle explanation is recognition, not an executed assignment experiment. Actual availability, permissions, source templates, reviewers, processing, preview output and restoration remain tenant checks.

## Actual status

Local validation passed41 files,32 Markdown documents,76 project-local relative links and39 consistent table groups across341 rows. The design/register agree on23 planning IDs and six complete learner files. All seven CSVs retain their checked structure, reference consistency and exact expected-removal results; the original A hashes are unchanged. The006 set checks produce two inclusion holdings, four complementary exclusion holdings, two qualifying profile holders, two remaining standalone Read holdings and four expected model units over six unchanged B rights. The expected post-model standalone Export set is empty. Existing005 scope/query and003 diagram-source checks still pass. Fences, answer wrappers, whitespace and absence of learner source/course links pass. These are local document/data checks, not runtime ISC evidence.

Authored/source/language reviewed:006 revision1.0. New CSV files:0. Tenant imports, queries, filters, profiles, processing operations, templates, previews, activated campaigns, decisions, tasks, screenshots, cleanup operations, repeated runs and independent learner tests:0. This course remains local; no repository, push or Pages action occurred.
