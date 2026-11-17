# CLB-006 beginner-readability revision

Revision 1.1. November 15, 2026.
Learner: [Compare campaign filters and review units](../../lessons/CLB-006_Compare_Campaign_Filters_and_Review_Units.md).
Original [revision1.0 record](CLB-006_Revision_Record.md) and [brief](../briefs/CLB-006_Filters_and_Review_Units_Brief.md) remain historical.

## Complete author reading

Read the full saved lesson before changes and again from opening through reasoning and cleanup after editing. Rechecked the final standalone/empty-result wording. This is a beginner-oriented author reading, not an independent learner test or tenant rehearsal.

## Useful corrections

The opening now explains review unit before relying on it. Holding and permission meanings precede the starting inventory. Inclusion/exclusion and the OR alternative are connected to the unchanged B set.

The two access selections were easy to confuse. The explanation now follows employee01: selecting an access item finds its holders, while refinement limits their reviewed access to B. It also explains why the Read-only holders still belong in the comparison.

The profile section preserves before-change observations and requires fresh work after processing. A profile association is explained as an ISC model change, distinct from a change to account permissions. The six-permission/four-unit comparison follows employee01's two permissions inside one profile and employee03's standalone Read. A later filter chooses a subset of those units.

Primary Owner is separated from the chosen Manager reviewer. Name-collision checks protect earlier objects. The two post-profile configurations now have distinct names: certlab-006-after-export-run01 and certlab-006-bundle-run01. Saved templates remain unscheduled. Cleanup accounts for both original comparisons, both later configurations and any empty generated record before removing the profile and filters.

No additional scenario, fixture, diagram or table quota was introduced. All three existing tables and the reasoning exercise remain. No campaign is started, no decision is made and no account permission is deliberately edited.

## Bounded current-source check

Checked November 15, 2026. Documentation support is distinct from runtime behavior.

| Primary source | Bounded use |
|---|---|
| [Using campaign filters](https://documentation.sailpoint.com/saas/help/certs/campaign_filters.html) | Inclusion/exclusion, OR criteria, display-name/source matching and profile versus standalone filtering. |
| [Managing access profiles](https://documentation.sailpoint.com/saas/help/access/access-profiles.html) | Detection during processing, ownership, enablement with requests off and deletion without entitlement removal; existing review references require separate handling. |
| [Starting a Search campaign](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html) | Access-based holder selection versus refined access, the separate filter-based route and standalone-access prerequisites. |

The original record retains support for selected-identity processing and unchanged administrative controls. Added names and comparison ordering are teaching choices. Actual capability, source templates, engine, operation, profile association, review grouping and cleanup remain untested. All inherited product questions remain open.

## Expected-data reconciliation

B remains four accounts and six holdings. Initial Export inclusion selects two; exclusion selects the four Reads. These sets are disjoint and their union is B's baseline. Adding Source B as an OR alternative would keep all six in the initial inclusion comparison.

Employee01 and employee02 each hold both profile rights; the other two holders have Read only. After actual verified detection, the expected model has two profile units and two standalone Read units. The post-profile standalone Export filter is expected to have no work, while the profile filter has two holdings. These are planned model/filter expectations, not observed processing or generated previews.

The complete B permission set and original A five are retained throughout. Cleanup removes only this attempt's unused generated/configuration records, temporary profile and three filters. Actual earlier activation or dependencies require separate resolution.

## Local verification

Saved-file validation passed across 114 reusable files: 92 Markdown files, 307 resolving project-local links, 116 consistent table groups and 902 table rows. Design/register reconcile all23 learner IDs. All14 CSVs and5 JSON assets/contracts pass; original baselineA input hashes remain unchanged.

The separate fixture check confirms the initial2/4 partition, the OR alternative retaining6, the two intended profile holders and four planned model units. Expanding those units recovers all six original B holdings. The planned later standalone Export/profile subsets are0/2. Manager responsibility remains two items with manager01 for inclusion, and three with manager01/one with manager02 for exclusion. All four configuration names are distinct and present; the reasoning exercise remains.

These are local planned-data checks. They do not execute ISC detection, filtering, generation, identity processing or cleanup. No executable code or canonical CSV/JSON asset was changed, so the collector's prior offline test suite was not rerun.

## Current state and next work

CLB-006 revision1.1 is authored and author/source/language reviewed. Tenant maintenance remains user-reported. Actual filters, profiles, processing, campaign generation, activation, cleanup, screenshots, repeated tenant runs and independent learner tests remain0.

Next local task is a complete fresh CLB-007 reading: saved configuration versus generated campaign, data collection versus scheduling, the expected next-cycle selection and retirement/reset. All 23 learner guides remain authored. No repository, push or Pages work.
