# Core audit batch06: uncertainty, removal and failure investigation

November 13, 2026. Author review.
Previous: [batch05](CORE_AUDIT_05_Reassignment_Decisions_and_Sign_Off.md).

## Outcome and inspection depth

CRT-031–036 were each read completely from their saved learner files. All six individual reads were returned without truncation. The review included the middle and ending, all six diagrams, tables and worked changed cases. Twenty-two distinct primary documentation bodies were checked for selected technical claims.

No learner correction was established. These lessons explain the ordinary flow before using changed inputs to test it. Necessary terms are introduced locally and attached to the exact person, account, access right, operation or evidence involved. This remains a simulated beginner author review, not an observed participant assessment or a tenant test.

Cumulative fresh full audit rereads cover001–036:36 of50. Fourteen remain,037–050. Indexing still covers all50 and is separate from rereading. All learner text and assets are preserved this batch, including local CRT-005 revision1.2. That earlier correction remains unpublished.

## Saved explanations and changed cases followed

| Lesson | Actual flow and changed case inspected | Audit conclusion |
|---|---|---|
| [CRT-031](../lessons/CRT-031_Resolving_Uncertainty_Before_an_Access_Decision.md) | STK_HELPER on wh-4601 has unclear capability and need. Application confirmation establishes warehouse-scoped reading/correction; C-91 confirms the authorized task. Changed duty allows reading but not correction. Case Review on case-4701 has justified reading but initially unknown all-case export; peer recommendation and logins cannot answer that gap. Later no-export confirmation changes what is known. Proposed manual handover to someone whose own access is included is blocked. | Unknown need differs from confirmed lack of need. Consultation supplies facts without changing assignment. Description edits, questions and recommendations do not change permissions or finalize work. The normal path and unresolved path both identify a useful next actor and evidence. |
| [CRT-032](../lessons/CRT-032_Following_a_Revoke_Decision_into_Required_Removal_Work.md) | Finalized Revoke concerns ORD_APPROVE on pur-4801, preserving View Orders. It is an individual entitlement, so no deferred reviewer revocation date applies. The separate Invoice Approval profile supports a saved future removal time: access before that time is not failure; access afterward requires actual work/result checks. A closed manual task alone does not prove the target result. | Reviewed item, finality, due time, supported path, operation and target observation remain distinct. Automatic and manual diagram branches are alternatives, not an invented failure-to-task switch. |
| [CRT-033](../lessons/CRT-033_How_Automated_Removal_Reaches_the_Application.md) | Warehouse sign-in wh-5101 and actual operation reference acct-8842 identify different useful values. STOCK_ADJUST removal uses a configured Web Services SaaS operation, enabled write capability and authorized integration credentials. The Reporting changed case has Finished with a denied REC_EXPORT removal; a later variant succeeds on adm-5201 instead of required rep-5201. | Identity ID, account ID, source environment and entitlement value are kept separate. Reading does not prove write authority. HTTP success is not sufficient if the body reports an error. Finished requires its detailed result, and success on the wrong account is not the requested removal. |
| [CRT-034](../lessons/CRT-034_Removing_Access_Through_Manual_Fulfillment.md) | T-34 is actually assigned to a source owner authorized in the archive application. ARCH_EXPORT is removed from arc-5301, reading retained, and truthful later CSV data is imported. Finance task removes INV_EXPORT but PAY_RELEASE is denied; closing the task/Finished report cannot erase that partial result. A false CSV omitting release does not remove it; a later old file does not prove a regrant. | Task recipient, application permission, actual change, import outcome and task completion answer different questions. The24-hour second-work-item condition is tied to the documented Task Manager file process. No universal recipient, safe one-row import or reopening contract is invented. |
| [CRT-035](../lessons/CRT-035_Overlapping_Access_and_Assignment_Origins.md) | Document Staff requires DOC_READ through Document Reading while independently requested Document Export supplies read/export. The supported role/profile case retains required reading after removing the requested assignment/export. Case Base still requires CASE_EXPORT after the separate requested Case Export assignment is removed; the inspected outcome does not prove all export requirements are gone. Later stale file differs from current application state. | Exact same-account/source/right overlap and actual assignment are required. The narrower role/profile rule is supported; independent-profile overlap remains bounded. Automatic role criteria, lifecycle enforcement and enabled-role content propagation are separate mechanisms. |
| [CRT-036](../lessons/CRT-036_Investigating_Pending_Failed_and_Partial_Removal.md) | Ledger removal succeeds for LEDGER_EXPORT but is denied for LEDGER_POST, preserving reading. Overall Incomplete does not negate the successful part. Service retry and Web Services429/503 policy have different conditions. Invoice removal times out with no supplied final observation or retry plan; later INV_RELEASE absence confirms the account state without rewriting the uncertain response history. | Each required change needs its own result. Authentication, authorization, connection failure, uncertain response and continued assignment need different evidence. Retry is intended work, not successful delivery; no blind repeat, automatic manual fallback or universal retry count is promised. |

All records and results above are supplied teaching cases. No operation, account change, task closure, CSV upload, configuration edit or actual consultation was performed.

## Beginner language, reasoning and independence

The lessons start with a recognizable question and explain its first useful relationship before adding exceptions.031 turns uncertainty into two answerable questions.032 walks from a specific required change to the work carrying it out.033 follows identifiers and integration permissions into the actual request.034 connects human action with truthful return data.035 follows two visible assignment paths.036 preserves successful and outstanding parts separately.

Terms such as source, entitlement, sign-off, provisioning, remediation, connector, schema, integration credentials, authentication, authorization, grant path, retry and timeout are explained where they matter. The prose then returns to the named permission and account instead of making the reader reason from labels alone.

The field/status table in036 has real diagnostic value: overall Pending, account-request Pending and Stage Executing do not mean the same thing. The examples explain why that matters. Similarly,033's account-name/account-ID comparison and034's application/file distinction connect front-end records to supported processing without inventing private backend services.

The six lessons repeat enough setup to stand alone. They do not depend on a continuing fictional company or a glossary link. No new source citations, teaching-method announcements, fixed visual quotas or revision metadata enter learner text. No demonstrated explanation gap justified rewriting the learner files in this batch. Actual non-native-English beginner performance remains unmeasured; future participant feedback can still reveal difficulty.

## Fresh primary checks

Each row is one distinct documentation body. Reopens and finds do not add to the count. The checks support the named claims, not every sentence or exhaustive feature currency.

| Primary source | Selected claim and limit |
|---|---|
| [Provisioning overview](https://documentation.sailpoint.com/saas/help/provisioning/index.html) | Recognized retryable connector errors, hourly retries up to three with queue delay; also general entitlement-owner/source-owner manual routing. This does not establish every certification task's recipient. |
| [Monitoring provisioning](https://documentation.sailpoint.com/saas/help/provisioning/tracking.html) | Administrative Tasks view, reassignment/completion and activity Status/Stage context. Work closure is not target observation. |
| [Web Services configuration](https://documentation.sailpoint.com/connectors/web_services/saas/help/configuration_parameters.html) | HTTP200 with error payload;429/503 up to three retries, positive retryDelay before numeric Retry-After, otherwise30 seconds. No multiplication into a universal service-plus-connector call count. |
| [Task Manager](https://documentation.sailpoint.com/saas/user-help/task_manager.html) | Perform external work, upload changed CSV, aggregation starts, Mark Complete; early closure allows24 hours for updated file/aggregation before a second work item. Scoped file process. |
| [Search/account activity fields](https://documentation.sailpoint.com/saas/help/search/index.html) | Overall Pending/Incomplete, Executing stage and account-request Pending/Committed/Finished/Retry/Failed. Values are field-specific, not one mandatory sequence. |
| [Access profiles](https://documentation.sailpoint.com/saas/help/access/access-profiles.html) | Role-required access is retained on separate-profile revocation; independent-profile overlap wording differs from reviewer guidance. Actual origin and account applicability matter. |
| [Roles](https://documentation.sailpoint.com/saas/help/access/roles.html) | Supported content changes require role-change propagation and enabled role state for deprovisioning; disabled propagation does not remove the previously granted entitlement. No universal deleted/disabled-role or profile-edit theorem. |
| [Understanding certifications](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html) | Certifiable origin/unit, automatic role Acknowledge, own-access manual restriction, sign-off initiation and certification source-owner manual description. Unsigned completion wording is not harmonized with Completing. |
| [Campaign reports](https://documentation.sailpoint.com/saas/help/certs/campaign_status_reports.html) | Remediation Finished/Completed can follow connected-source verification or manual-task/service-desk closure; fresh report required after changes. |
| [Reviewer guidance](https://documentation.sailpoint.com/saas/user-help/certs/reviewing/index.html) | No entitlement revocation date, criteria-role acknowledgment and independent-profile common-right retention statement. The latter does not settle the administration conflict. |
| [Lifecycle states](https://documentation.sailpoint.com/saas/help/provisioning/lifecycle.html) | State-required profile assignments are enforced while the state applies; removing the profile while still in that state leads to provision again. Not every manual permission edit is this operation. |
| [Web Services connection](https://documentation.sailpoint.com/connectors/web_services/saas/help/connecting.html) | Provisioning disabled by default/read-only, requiring enablement; enabled setting does not supply missing target authority. |
| [HTTP operations](https://documentation.sailpoint.com/connectors/web_services/saas/help/http_operations.html) | Configured Remove Entitlement operation, operation-specific destination/method and account-reference context. No universal payload or target request invented. |
| [Timeout guidance](https://documentation.sailpoint.com/connectors/web_services/saas/help/troubleshooting/timeout_errors.html) | Waiting/communication and scoped configurable timeouts; increasing a wait does not establish the original account outcome. No numerical timeout setting added to learner text. |
| [Account loading](https://documentation.sailpoint.com/saas/help/accounts/loading_data.html) | Aggregation reads source data; enabled missing-account deletion affects ISC records. Collection is not the removal action. |
| [Account schemas](https://documentation.sailpoint.com/saas/help/accounts/schema.html) | Account Name and Account ID are configured source fields; Account ID references accounts across systems. Do not substitute the ISC person ID. |
| [Virtual appliances](https://documentation.sailpoint.com/saas/help/va/index.html) | VA-based architecture uses outbound polling for requested aggregation/provisioning. Not every connector requires a VA. |
| [Finalize operation](https://developer.sailpoint.com/docs/api/process-sign-off-certification-v-1/) | Experimental scoped operation finalizes decisions and initiates required remediation. Initiation is not completed source change. |
| [Next-generation overview](https://developer.sailpoint.com/docs/api/next-generation-certification-campaigns/) | Read-only normal sign-off and campaign-level remediation narrative; not a universal all-engine timing contract. |
| [Campaign completion](https://documentation.sailpoint.com/saas/help/certs/completing_campaigns.html) | Activities/remediation verification and saved-manager-decision preservation example; no automatic task on every failed write inferred. |
| [Access Recommendations](https://documentation.sailpoint.com/saas/help/ai/access_recs/recommendations.html) | Certification-specific peer/attribute guidance, conditional visibility and retained human responsibility. Not current business authorization. |
| [Activity Insights](https://documentation.sailpoint.com/saas/help/ai/activity_insights/index.html) | Supported source events and active days over90 days; source login does not prove use/authorization of each entitlement. |

## Unresolved boundaries

OQ-05 remains open after directly comparing current general provisioning and certification-specific manual-routing passages.031–036 establish actual task assignment where it matters;034 supplies a verified source-owner example without promoting it to a universal hierarchy.

OQ-07 remains open after directly comparing reviewer common-entitlement retention with independent-profile administration removal wording.035 uses the supported narrower role-required/access-profile case and explicitly avoids a universal independent-profile guarantee.

OQ-02 remains open for universal phase/timing claims: direct Finalize and Understanding describe initiation at sign-off, while the overview also describes campaign-level remediation.032–036 establish due/started work as supplied conditions instead of guessing a private sequence. OQ-01's saved-unsigned completion conflict is still visible in current Understanding/Completing bodies. None of these wider uncertainties is silently resolved.

All17 capabilities and11 open questions remain. No new question, invented tenant outcome, source-specific safe retry or blanket fallback was introduced.

## Coverage, tasks and continuation

Primary coverage inspected: COV-08/20's uncertainty portion in031,22 in032,23 in033/034,24 in035 and25 in036. Supporting03/04/05/06/07/13/17/18/19/21/26/29/30/31 connects authorization, exact source/account, origin, timing, evidence and diagnosis. Later owners such as037/044/046 still need their own fresh full rereads.

Routine-task foundations mainly14/17/18/19/20/21/22, with supporting11/12/13/15/23. Existing200 working meanings suffice. No new term row or glossary dependency is needed.

Next: CRT-037–042, verifying required removal, reminders/progress, overdue/undecided/unsigned work, campaign completion, correction/retirement and count/status interpretation. Complete the remaining14 core rereads before sequencing the five planned specialist routes. No051 stub or fixed specialist lesson quota.

Baseline205 files includes all earlier local work. This batch changes nine current metadata files and adds this complete report. Preserve all50 learner files/assets, local0051.2, prior audit/revision/publication records, course manifest/reader/styles/tests and corrected verifier. No commit, push, new deployment, tenant/API execution, graphical observation or independent participant assessment.

## Executed local checks

Local checks passed November 13, 2026: 206 files,139 Markdown files,856 resolving relative links,219 table groups and2,483 table rows. Comparison with the205-file baseline preserves196 files byte-identically. Only nine current metadata files change; this complete batch06 report is the sole addition. All50 learner files/assets, local CRT-005 revision1.2, earlier audit/revision/publication records, manifest, reader, styles, tests and verifier remain unchanged this batch. Ordered IDs, titles/URLs, ten modules,32 coverage rows,24 routine-task rows,200 unique working meanings,17 capabilities and11 questions reconcile; mapped primary references resolve. Fences/table widths, file endings and absence of trailing whitespace pass. The local site verifier passes with50 lessons,5,935 content units,50 diagrams/assets and59 learner tables. Tracked whitespace checks pass; nothing is staged and HEAD remains e5f47e6e9a1884117ee77080beeeaba053a1b51b. No commit, push, live publication check, graphical observation or tenant execution.
