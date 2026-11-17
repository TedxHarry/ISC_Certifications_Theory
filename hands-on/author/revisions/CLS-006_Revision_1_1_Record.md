# CLS-006 beginner-readability revision

Revision 1.1. November 16, 2026.
Learner: [Automate a bounded read-only evidence collection](../../lessons/CLS-006_Automate_a_Bounded_Read_Only_Evidence_Collection.md).
The original [revision1.0 record](CLS-006_Revision_Record.md) and [brief](../briefs/CLS-006_Bounded_Read_Automation_Brief.md) retain their original stage.
Support: unchanged [collector](../../tools/collect_certification_evidence.py), [configuration example](../contracts/CLS-006_Config_Example.json), [offline tests](../tests/test_collect_certification_evidence.py) and [five-GET plan](../contracts/CLS-005_Read_Only_Request_Plan.json).

## Complete author reading

Read the entire original learner, saved revision, brief, original record and blank configuration. Read the collector's configuration/output checks, connection/retry/GET boundaries, paging, record/summary comparisons, reporting and command flow to reconcile the instructions with its actual local behavior.

The review follows the practical sequence from known manual case through private setup, configuration-only check, bounded live reads, saved result, manual comparison, incomplete recovery and repeat. This is author review, not an independent beginner test or live capture.

## Useful teaching changes

Collector, capture, bounded, script, token, caller, scope, sign-off, engine/contract, redirect/proxy and fulfillment are explained near use. Source A/B and the expected retained access are stated locally.

The learner creates the private folder, copies the blank example, edits the private copy and preserves earlier configurations. JSON object/list punctuation and each command option have a practical meaning. The existing single current-reviewer restriction and complete pinned certification set are explicit; a configuration label grants no authority.

The configuration-only command prints a short limit summary, not a full request plan. The heading and explanation now describe what it actually does. The blank example cannot establish actual IDs or tenant readiness.

Paging includes the empty final page in the ten-page limit and requires numeric totals on every page. Retry means another attempt at the failed GET; two retries allow at most three attempts within the total budget. MiB and the collector-specific nature of all limits are clearer.

The result has separate outcome and mode fields. Numbered responses contain parsed JSON when available; raw unsuccessful response bodies are not retained. NOT_RUN covers setup/output failure and may have no report; INCOMPLETE preserves partial capture and its reason code. These labels do not establish a permission decision.

Subject-summary versus target identity, capture checks versus manual evidence, and the unchanged verification flags are explained. CSV fulfillment remains simulated application work. Later source restoration does not erase the historical review or prove missing earlier removal.

Three learner tables, the relationship sketch and the changed-reviewer reasoning exercise remain. No extra scenario, endpoint, credential-generation flow, code change, new fixture, live response, screenshot or tenant action was added.

## Current documentation and local behavior checks

Checked November 16, 2026.

| Evidence source | Scope and limit |
|---|---|
| [Certification list](https://developer.sailpoint.com/docs/api/list-certifications-v-1/) | Current experimental list/header and caller-limited view. |
| [Review items](https://developer.sailpoint.com/docs/api/list-review-items-v-1/) | Current experimental identity-review list and authorized actor conditions. |
| [Certification model](https://developer.sailpoint.com/docs/tools/sdk/typescript/gov_certification/models/certification/) | Entered decisions differ from final sign-off and its date. |
| [Rate limiting](https://developer.sailpoint.com/docs/api/rate-limit/) | Respect Retry-After rather than retrying earlier; no universal throughput promise is added. |
| [Collector source](../../tools/collect_certification_evidence.py) | Private output, fixed requests/budgets, configuration-only summary, shared reviewer, required totals, result flags and saved response behavior. |
| [Offline tests](../tests/test_collect_certification_evidence.py) | Synthetic local behavior only, with fake connection and clocks; no token or tenant. |

Same-day CLS-005 primary checks support the unchanged five-operation request/schema plan. This is a bounded affected-passage recheck, not a complete release audit. Actual engine, allowed experimental use, host/IDs, authority, response compatibility, grouping and UI/fulfillment correspondence remain unobserved. Inherited product questions remain open.

## Local verification

All25 offline test methods passed in a fresh run using the existing synthetic tests. CLI help was checked. The unfilled example stopped with NOT_RUN: CONFIG_ORIGIN as expected, without a token prompt or network. No real --live command was issued.

The full-project check passed across129 reusable files,107 Markdown files,410 project-local links,130 table groups and1001 rows. All23 learner IDs,14 CSV fixtures and five JSON assets/contracts reconcile. Original baselineA hashes are unchanged; prior case/contract checks remain consistent.

Collector code, tests, request/configuration JSON and canonical CSVs are unchanged. Local program checks do not establish a complete live capture, actual permissions, business decision quality, removal, tenant repeatability or independent learner performance.

## Actual state and next work

Maintenance remains the last user-reported tenant status. Actual authenticated requests, UI comparison, historical fulfillment verification, live repeat, screenshots and independent learner tests remain0. No actual private binding or live evidence file was created.

All23 learner guides now have complete fresh author beginner-readability readings recorded:17 main units and6 specialists, plus the supporting017 assessor guide. Next is a final cross-file consistency/packaging check of this revised set. Actual setup, lab execution and repeat/learner testing remain separate. Local only; no repository, push or Pages action.
