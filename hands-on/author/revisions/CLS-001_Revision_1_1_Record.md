# CLS-001 beginner-readability revision

Revision 1.1. November 16, 2026.
Learner: [Review uncorrelated account access and track ownership](../../lessons/CLS-001_Review_Uncorrelated_Account_Access_and_Track_Ownership.md).
The original [revision1.0 record](CLS-001_Revision_Record.md) and [brief](../briefs/CLS-001_Uncorrelated_Account_Review_Brief.md) remain historical. The current [D setup contract](../../lab-data/baselineD/README.md) is revision1.1; its three CSVs are unchanged.

## Complete author reading

Read the full original learner, D contract and relevant data, then the complete saved revision through setup, correlation, review, fulfillment, ownership follow-up, reasoning exercise and reset. This is author review, not an independent beginner test or tenant execution.

## Useful teaching changes

Source/entitlement meanings precede the account table. Control means a comparison account with a known expected match. A/B aliases, account-versus-holding counts, source owner and working reviewer sign-in are explicit.

Schema fields now explain their roles. The Multi-Valued and Entitlement flags have practical purposes, and the catalogue describes rights while the account file assigns those values. Aggregation is explained before loading. The Generic Review and Import Accounts step is distinguished from actual account aggregation.

The matching example follows the control's employeeNumber to employee01's Identification Number and keeps Read/Export outside that pairing. A missing matching key alone was insufficient readiness guidance: built-in Account Name-to-identity-name fallback must also be checked. The learner and current D contract now require that pre-collection check, alongside configured criteria and manual-link inspection. No supplied account value or real correlation was changed.

Custodian is introduced before the supplied facts. The limited Read purpose uses simpler wording; permission approval, source ownership, custody and verified personal ownership remain separate. Follow-up is a work obligation, not automatic expiry. Deadline, maintained undecided access, template/preview, remediation and manual-task meanings support later actions.

Unused run naming, saved/generated references, the return to the administrator's session, CSV simulation before editing and successful reset collection are explicit. The normal reset applies only while original associations remain valid; a legitimate later ownership/key correction must be preserved and a new approved training starting state agreed.

The two existing tables and ownership reasoning exercise remain. No new scenario, diagram, catalogue right, matching value or canonical fixture was added.

## Bounded current-source check

Checked November 16, 2026.

| Primary source | Scope of this pass |
|---|---|
| [Dedicated campaign creation](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html) | Uncorrelated Accounts source/account selection and type-dependent reviewer options; actual route and recipient remain inspected prerequisites. |
| [Account correlation](https://documentation.sailpoint.com/saas/help/accounts/correlation.html) | Attribute matching, configured criteria and the built-in name fallback. The explicit pairing does not disable fallback. |
| [Sources and accounts](https://documentation.sailpoint.com/saas/help/sources/index.html) | Account filters, shadow representation and source-owner responsibility. |
| [Generic configuration](https://documentation.sailpoint.com/connectors/flat_file/va/help/connecting.html) and [introduction](https://documentation.sailpoint.com/connectors/flat_file/va/help/index.html) | Setup/import distinction, disabled authentication/password features and stated VA prerequisite. |
| [Reviewer guidance](https://documentation.sailpoint.com/saas/user-help/certs/reviewing/index.html) | Uncorrelated Identities/Access Items, possible grouping, Finish and no entitlement revocation-date control. |

The Generic configuration link now resolves to the VA connecting page that was inaccessible at the original review. That does not establish the actual manual-upload dependency in this tenant: the introduction lists a VA prerequisite while creation exposes no cluster choice. Runtime mode/dependency checks remain required. Same-day task/loading/report checks from the main-route review support unchanged fulfillment instructions.

This pass does not resolve actual grouping, automatic owner routing, missing-feature fallback, ownership, signed editing or any inherited product question. No actual tenant association or import is inferred from source documentation.

## Planned cases remain unchanged

D has two accounts and three holdings. Only the unmatched target's Read/Export belongs in the review; the employee01-linked control keeps Read outside the decision scope. Supplied facts support one Approve/one Revoke. Exact Export removal leaves both accounts and both Reads, the target key unchanged and control linked. Resolved normal reset restores three holdings; A5/B6 and people mappings remain unchanged.

Actual permission decisions and ownership resolution are separate outcomes. The limited Read authorization is not evidence that manager02 personally owns the account. A verified later ownership correction changes reset readiness and is not undone merely to reproduce the planned unmatched count.

## Local verification

Saved-file validation passed across 124 reusable files: 102 Markdown files, 369 resolving project-local links, 125 consistent table groups and 960 table rows. Design/register reconcile all23 learner IDs. All14 CSVs and5 JSON assets/contracts pass; original baselineA input hashes remain unchanged.

The existing D checks reconcile two accounts, target-only two-right review, one Approve/one Revoke and holdings3→2→3. Both Read holdings, original scalar keys, the linked-control value and the other source baselines are preserved.

A separate read-only comparison of the supplied files finds zero target employeeNumber matches, zero case-insensitive target Account Name matches among the five people.name values mapped to identity uid, and exactly one control key match to employee01. This confirms the planned fixture only. Actual tenant identities, prior manual links, fallback effects and shadow grouping remain uninspected.

No executable collector or canonical CSV/JSON asset changed, so the collector's earlier25-test offline suite was not rerun. Local checks do not establish source imports, real association, reviewer routing, task completion, owner resolution or a live application result.

## Actual state and next work

CLS-001 revision1.1 and current D instructions are authored and author/source/language reviewed. Maintenance remains the last user-reported tenant status. Actual source/schema/correlation setup, imports, shadow grouping, reviewer assignment, decisions/sign-off, tasks, collection, ownership resolution, screenshots, resets, repeated runs and independent learner tests remain 0.

Eighteen of 23 complete fresh learner readings are covered: all17 main-route units and CLS-001. Next is CLS-002, followed by003–006: five specialist readings remain. All23 learner guides remain authored locally. No repository, push or Pages action.
