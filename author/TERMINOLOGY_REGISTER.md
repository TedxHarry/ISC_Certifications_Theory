# Author terminology register

Version 1.4. October 30, 2026.
Purpose: consistent working meanings and primary teaching locations.
Status: authoring aid; no learner glossary or tooltip interaction is implemented.

These are author working meanings. Verify product-specific use in the applicable lesson/engine. Reintroduce necessary terms in prose where they become useful. The learner should not be sent here to understand a missing explanation.

## Access and represented information

| Term | Working meaning and important connection | Primary planned teaching |
|---|---|---|
| Access | What an account is permitted to do in a system; an access label needs its business meaning explained. | CRT-001/006 |
| Identity | ISC's representation of a person or other managed subject, connecting information and accounts/access. | CRT-002/005 |
| Account | A record in a particular system; distinguish the exact account from the owning identity. | CRT-005/008 |
| Source | ISC's configured representation of a system or collection of account data. | CRT-005 |
| Target system | The actual system whose account access must change or be verified; distinguish it from ISC's collected representation. | CRT-003/033/037 |
| Connector | The supported integration used to read or change data for a source. Reading support does not establish write capability. | CRT-005/033 |
| Account aggregation | Reading account information into ISC's represented source data. It is not itself an access-review decision. | CRT-005 |
| Account correlation | Matching/associating an account with its owning identity. A correct value on the wrong account is not the intended person's evidence. | CRT-005/008 |
| Uncorrelated account | A source account lacking the intended authoritative identity association; do not infer that it has no access. | CRT-008/045 |
| Machine/service account | A non-human account used by an application/process; ownership and supported review type need explicit treatment. | CRT-008/015; X-03 |
| Attribute | A named piece of information on a record. Identity and account attributes can belong to different objects. | CRT-005/009 |
| Entitlement | An access right represented from a source, such as a group membership; explain what that right allows. | CRT-006 |
| Access profile | A named bundle of entitlements from one source; review and removal depend on how it was assigned. | CRT-006/007 |
| Role | An access package associated with a business responsibility, with configured assignment behavior. Distinguish role access from campaign responsibility. | CRT-006/007 |
| Assignment origin | How access was assigned or recognized; it affects what is independently reviewable or removable. | CRT-006/007 |
| Lifecycle state | A configured business stage that can drive access behavior. Its grants are not interchangeable with individually requested items. | CRT-004/007 |
| Birthright access | Access automatically assigned under defined business conditions; verify the particular role/model behavior rather than assume manual revocation overrides it. | CRT-007/035 |
| Effective access | Access that remains through applicable assignment paths and target permissions; removing one path does not establish that every path is gone. | CRT-035/037 |

## Campaign objects, scope and responsibility

| Term | Working meaning and important connection | Primary planned teaching |
|---|---|---|
| Access certification | A review of whether represented access is appropriate; distinguish it from a professional certification exam. | CRT-001 |
| Certification campaign | The organized campaign containing assigned reviews; generated contents and settings need their own evidence. | CRT-002/003 |
| Certification / assigned review | A review assigned to a reviewer within the campaign. Do not use campaign and individual review as identical objects. | CRT-002 |
| Review subject | The identity/account or other subject whose access is under review, as used by the supported campaign type. | CRT-002/008 |
| Review item | An individual unit on which a decision is recorded; identify its access and subject/account context. | CRT-002/006 |
| Certifier / reviewer | The person or supported review group assigned to review; the actual decision actor can differ in recorded history. | CRT-002/022/043 |
| Decision maker | The actor recorded as making a decision; distinguish them from the currently assigned reviewer. | CRT-022/043 |
| Campaign creator | The actor who created the campaign; do not infer every later responsibility or permission from that fact. | CRT-002/022 |
| Campaign owner | Responsibility for the campaign according to configuration; owner, creator and reviewer are not assumed identical. | CRT-002/022 |
| Source owner | The responsible source owner recorded in ISC; relevant to some review/routing/removal paths, not automatic permission for every action. | CRT-012/022/034 |
| Access owner | The responsible owner of the access object, with object/type-specific supported routing. | CRT-009/022 |
| Remediation owner | The person responsible for carrying out or coordinating the required removal/change in the applicable path. Verify actual task assignment. | CRT-002/034; X-01 |
| Cert Admin / Org Admin | Platform administration levels relevant to certification actions. Verify the current permission matrix and task scope. | CRT-002/021/022 |
| Governance group | A configured group that may be used for review responsibility where supported. Verify how members can act. | CRT-022 |
| Authorization | Permission to perform an action; being responsible for a campaign does not itself establish that permission. | CRT-002/021/025 |
| Query | A request selecting records under defined search conditions; identify which kind of records the query returns. | CRT-013/016 |
| Access refinement | Selecting which access to include for selected identities; people selection alone does not express every access restriction. | CRT-014 |
| Campaign filter | Configured campaign inclusion/exclusion criteria applied under supported combination rules. | CRT-017/018 |
| Template | A reusable campaign definition; it is not the same as a generated active campaign. | CRT-020 |
| Schedule | Timing instructions for a supported generation process; do not assume it also activates the campaign. | CRT-020 |
| Generated review data / snapshot | Review information captured/generated at a particular point; verify exact engine behavior for later changes. | CRT-019 |
| Preview | Generated campaign content/settings available for validation before starting; distinguish this from proposed identity-mapping Preview in other ISC features. | CRT-019/021 |
| Activation | Starting the campaign for reviewer work under its supported state/permissions. | CRT-020/021 |
| Reassignment | Changing review responsibility within supported scope/state; distinguish campaign reassignment from general work reassignment. | CRT-025/026 |
| Self-certification | Reviewing one's own access; teach the supported prevention/routing controls rather than assume any reassignment is permitted. | CRT-024 |

## Decisions, delivery and evidence

| Term | Working meaning and important connection | Primary planned teaching |
|---|---|---|
| Approve | Accept continued reviewed access under the applicable conditions; not an instruction to grant unrelated missing access. | CRT-028 |
| Revoke | A decision requiring removal/change of the reviewed access; it is not proof that the target change is complete. | CRT-028/032 |
| Acknowledge | A supported review action for access controlled through applicable automated assignment; do not present it as a freely revocable manual grant. | CRT-007/028 |
| Sign-off / finalization | Confirmation/finalization of the assigned review's decisions. Exact consequences and unsigned cases require engine-specific verification. | CRT-030 |
| Undecided | A review item has no decision; distinguish it from a review with saved decisions but no finalization. | CRT-030/039 |
| Unsigned review | A review not signed off/finalized; documented completion behavior has an unresolved scope question in the capability register. | CRT-030/039 |
| Overdue | The relevant deadline has passed; determine the applicable object and handling rather than assume access changed. | CRT-039 |
| Campaign completion | The campaign's completed state/action under the relevant engine; not a universal synonym for verified target removal. | CRT-040 |
| Remediation | Work required to carry out a removal/change decided in the review. The applicable trigger, path and outcome need evidence. | CRT-032–037 |
| Provisioning | Supported work that changes external accounts/access; inspect the actual operation and result. | CRT-033 |
| Manual fulfillment task | Assigned human work to make an external change. Task closure and actual target state are separate observations. | CRT-034 |
| Retry | Another supported attempt at failed work; conditions and limits are operation-specific. | CRT-036 |
| Status | A recorded state of a particular object or operation. Always identify what the status describes. | CRT-042 |
| Audit evidence | Records supporting what was scoped, reviewed, decided and done, with actor/time/context. It does not automatically establish every claim. | CRT-043/044 |
| Report freshness | When a report was generated and which state it represents; an old report may not show later work. | CRT-044 |
| API | An application programming interface through which software requests operations or data. Core coverage includes interpreting read-only evidence. | CRT-044 |
| Object ID | An identifier for the relevant platform record; a matching display name alone is not an exact record reference. | CRT-042/044 |
| Request/response | An operation/data request and the returned result. An accepted request is not automatically completion of downstream work. | CRT-044 |
| Pagination | Returning a collection in portions; seeing one page does not establish the whole population. | CRT-010/044; X-05 |
| Recommendation / access flag | Available decision-support context. Interpret source/meaning/freshness; it is not a replacement for the reviewer understanding the access. | CRT-027/031; X-04 |

## Actual introductory teaching

[CRT-001](../lessons/CRT-001_Why_Review_Previously_Approved_Access.md) now explains access, account, identity, entitlement, source, account aggregation/correlation, review item, access certification, reviewer/certifier, campaign, Approve, Revoke, sign-off/finalization and remediation in context. Its evidence comparison distinguishes an earlier approval, current need, decision and actual account result.

These are supporting introductions for this purpose lesson. CRT-002's authored foundations are recorded next; other primary detailed teaching locations remain planned. Source checking and simulated author review are recorded in [its author record](revisions/CRT-001_Revision_Record.md); no observed beginner test is claimed.

[CRT-002](../lessons/CRT-002_Campaigns_Certifications_and_Review_Items.md) now explains certification campaign, certification/assigned review, review item, subject, reviewer/certifier, campaign scope, generation/start, creator/owner, Cert Admin/Org Admin, source/access owner, remediation, decision maker, undecided and sign-off in connected prose. It reintroduces account/access/identity/entitlement and Approve/Revoke as needed. It distinguishes saved item decisions, confirmed review completion, campaign state and target-account outcome.

[The CRT-002 record](revisions/CRT-002_Revision_Record.md) locates each actual teaching purpose. No exact permission matrix, algorithm for grouping reviews, report counter formula or engine finality policy is claimed.

[CRT-003](../lessons/CRT-003_From_Access_Data_to_a_Verified_Outcome.md) explains source, connector/integration, account aggregation, correlation, entitlement, generated review item, assigned certification, reviewer, scope/start, Approve/Revoke, sign-off, remediation, provisioning and target system as parts of one trace. It distinguishes collection from granting access, reading from writing, accepted work from account change, and historical review data from refreshed account evidence.

[The CRT-003 record](revisions/CRT-003_Revision_Record.md) locates this supporting teaching and its evidence cases. Detailed term owners remain responsible for configuration and engine-specific behavior. A new target-system working row records the exact-account meaning used here.

## Requests and lifecycle context authored in CRT-004

| Term | Working meaning and connection | Teaching location |
|---|---|---|
| Access request | A submitted request for a supported access change; grant and removal intentions differ. | CRT-004 |
| Requester | The person submitting the request, who may differ from the recipient where supported. | CRT-004 |
| Recipient | The person for whom access is requested; keep the target account distinct. | CRT-004 |
| Approver | The actor evaluating the requested change under its configured process. | CRT-004 |
| Mapping | Configuration specifying how incoming information sets an identity value. | CRT-004/005 |
| Identity processing | Evaluation of identity information and applicable access configuration, including required access work. | CRT-004/005 |
| Access model | Configured access packages and assignment requirements; distinguish a review decision from changing a requirement. | CRT-004/006/007 |
| Certifiable access | Access eligible for the supported certification review under the applicable model; not all held access is an individual decision item. | CRT-004/006/007 |

[CRT-004](../lessons/CRT-004_Certifications_Access_Requests_and_Lifecycle_Rules.md) also explains LCS, birthright, assignment origin, the profile as a review unit and the different meanings of request approval and certification Approve. Its state name, configured requirement, data calculation, removal work and account evidence remain distinct. [The author record](revisions/CRT-004_Revision_Record.md) locates the actual teaching; no full lifecycle implementation or universal campaign timing is claimed.

## Maintenance

When a lesson is authored, add the actual teaching location to its author record and reconcile any term whose meaning changes by engine/context. Do not mark a term taught simply because it is listed here.

Introduce abbreviations with their plain meaning in each lesson that depends on them. Important examples include ISC, API and lifecycle state (LCS); do not create an acronym solely to shorten a one-time mention.

New terms may be added when a real explanation needs them. Avoid growing a glossary with unrelated IAM material or exposing these author tables as a preliminary vocabulary test.
