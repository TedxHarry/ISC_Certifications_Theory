# Author terminology register

Version 3.18. November 11, 2026.
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
| Role | An ISC access package that can contain direct entitlements and access profiles from one or multiple sources; definition and an identity's assignment are separate. | CRT-006/007 |
| Assignment origin | How access was assigned or recognized; it affects what is independently reviewable or removable. | CRT-006/007 |
| Lifecycle state | A configured business stage that can drive access behavior. Its grants are not interchangeable with individually requested items. | CRT-004/007 |
| Birthright access | Access automatically assigned under defined business conditions. The Birthright Access flag points to automated grants such as lifecycle rules; inspect origin and actual action. Manual revocation does not establish that the assigning rule stops requiring it. | CRT-007/027/035 |
| Effective access | Access that remains through applicable assignment paths and target permissions; removing one path does not establish that every path is gone. | CRT-035/037 |

## Campaign objects, scope and responsibility

| Term | Working meaning and important connection | Primary planned teaching |
|---|---|---|
| Access certification | A review of whether represented access is appropriate; distinguish it from a professional certification exam. | CRT-001 |
| Certification campaign | The organized campaign containing assigned reviews; generated contents and settings need their own evidence. | CRT-002/003 |
| Certification / assigned review | A review assigned to a reviewer within the campaign. Do not use campaign and individual review as identical objects. | CRT-002 |
| Review subject | The identity/account or other subject whose access is under review, as used by the supported campaign type. | CRT-002/008 |
| Review item | An individual unit on which a decision is recorded; identify its access and subject/account context. | CRT-002/006 |
| Certifier / reviewer | The identity or supported group actually assigned review work through the campaign type/choice, relevant input and supported controls. Distinguish configured choice, generated assignee and recorded decision actor. | CRT-002/022/043 |
| Decision maker | The actor recorded as making a decision; distinguish them from the currently assigned reviewer. | CRT-022/043 |
| Campaign creator | The actor who created the campaign; do not infer every later responsibility or permission from that fact. | CRT-002/022 |
| Campaign owner | Responsibility for the campaign according to configuration; owner, creator and reviewer are not assumed identical. | CRT-002/022 |
| Source owner | The responsible source owner recorded in ISC; relevant to some review/routing/removal paths, not automatic permission for every action. | CRT-012/022/034 |
| Access owner | Recorded responsibility for the reviewed access object. The documented Access Owner choice uses its primary owner and supported fallback; additional entitlement owners do not by themselves establish separate assignees. | CRT-009/022 |
| Remediation owner | The person responsible for carrying out or coordinating the required removal/change in the applicable path. Verify actual task assignment. | CRT-002/034; X-01 |
| Cert Admin / Org Admin | Platform administration levels relevant to certification actions. Verify the current permission matrix and task scope. | CRT-002/021/022 |
| Governance group | Configured identities whose member can act for the group in supported review scope. Group owner, actual membership and individual decision actor differ; inactive/disabled identity status does not automatically update membership. | CRT-022 |
| Authorization | Permission to perform an action. Business acceptance, campaign ownership, assigned review responsibility and actual administrative platform permission are distinct; verify the actor's required scope/state. | CRT-002/021/025 |
| Query | Search instruction matching records through fields and conditions; returned category and actual saved selections determine what is selected. | CRT-016; supporting CRT-013 |
| Access refinement | Choosing which reviewable access to include for already selected identities; a saved choice does not grant missing access or establish an account-specific restriction. | CRT-014; supporting CRT-013 |
| Campaign filter | Saved criteria for review content to include or exclude; affected work depends on criterion type and supported combination, not an access grant/removal decision. | CRT-017/018 |
| Template | Reusable saved campaign instructions, including actual saved selection/reviewer/settings in the supported route. Distinguish this definition from each campaign generated from it; edits alone do not prove an existing instance changed. | CRT-020 |
| Schedule | Supported one-time/recurring timing instructions for preview generation, with configured time zone. Search scheduling does not replace administrator start, and an early preview does not cancel the documented planned occurrence. | CRT-020 |
| Generated review data / snapshot | Review work established from the scope/data used for generation. Source observation, generation and report times differ. Dedicated-route snapshot guidance does not prove every field immutable across all engines; inspect actual work and permitted workflow changes. | CRT-019 |
| Preview | Actual generated campaign work/settings inspected before launch. Compare intended people/account/access/assignment relationships and settings, explain gaps, correct and reinspect; distinguish this from identity-mapping Preview in other ISC features. | CRT-019/021 |
| Activation | Starting a particular generated campaign for reviewer work under supported state/permissions. An accepted activation-job request is distinct from a verified running result; UI/API state labels need their own documented scope. | CRT-020/021 |
| Fallback | Alternative routing used when required responsibility cannot be supplied under the applicable campaign rule. Distinguish a verified fallback, exclusion and an unestablished terminal outcome; the receiving person still needs suitability and permission. | CRT-023 |
| Reassignment | Changing responsibility for selected existing review work under supported state/actor/recipient rules. Whole certification, selected subject and selected item can be different scopes. Verify the resulting assignment, retained coverage, decision state/history and visibility; distinguish as-created work redirection. | CRT-025/026 |
| Work reassignment | Configured automatic redirection of a selected person's work type as work is created during a specified period. Distinguish this instruction from existing-work handover and actual assignment; replacement/end/delete/feature-disable do not return prior work. Check recipient, period/time zone, enabled feature and group/self-review/chain conditions. | CRT-026 |
| Self-certification | A person assessing their own access. Documented automatic handling separates own-access review work and routes it elsewhere; a manual certification reassignment containing any proposed new reviewer's own access is blocked. Verify subject, actual reviewer and actor, preserving coverage. | CRT-024 |

## Decisions, delivery and evidence

| Term | Working meaning and important connection | Primary planned teaching |
|---|---|---|
| Approve | Accept continued access to the actual reviewed item under assessed conditions. Does not grant missing access, approve unrelated permissions or freeze future access requirements. | CRT-028 |
| Revoke | Record removal/change for the actual reviewed item. Package scope, origin and review type matter; decision, finalization, required removal work and verified account result differ. Not an account-delete instruction. | CRT-028/032 |
| Acknowledge | Record examination of a role assigned through automated membership criteria. Does not remove access, override criteria, fix a mismatch or provide a general uncertainty response; investigate governing data/rule/contents separately. | CRT-006/007/028 |
| Consultation | Asking someone with relevant knowledge for facts supporting the review decision. Does not itself change the assigned reviewer, finalize choices, extend a deadline or change account access. | CRT-031 |
| Decision criteria | Organization-approved conditions used to judge access against current authorized work and actual account/capability facts. Distinct from campaign filters that select review content; not asserted as a built-in ISC field or universal policy. | CRT-029 |
| Decision comment | Explanation retained with an item decision, connecting current facts, actual item and usable evidence to the choice. Mandatory entry does not establish truth; report Decision Comments differs from status Comments. | CRT-029 |
| Bulk decision | A supported operation applying a decision to multiple selected items. Each item still needs valid reasoning; inspect exact selection, saved choice/comment and operation result without assuming all-pages scope or shared-comment propagation. | CRT-029 |
| Sign-off / finalization | Separate confirmation of the assigned review's decisions, distinct from saved item choices, campaign completion and source result. Normal next-generation sign-off makes review decisions read-only and initiates needed remediation; unsigned administrator-completion and broader editing scope remain bounded questions. | CRT-030 |
| Undecided | A review item has no decision; distinguish it from a review with saved decisions but no finalization. | CRT-030/039 |
| Unsigned review | Assigned review not finalized, which can contain some or all saved item decisions. Does not mean every item is undecided. Treatment at administrator completion remains OQ-01, not a universal preserve/discard rule. | CRT-030/039 |
| Reauthentication | Confirming the acting person's identity again through the configured sign-in service when required for completion. A prompt alone is not successful review sign-off or business justification. | CRT-030 |
| Overdue | The relevant deadline has passed; determine the applicable object and handling rather than assume access changed. | CRT-039 |
| Campaign completion | The campaign's completed state/action under the relevant engine; not a universal synonym for verified target removal. | CRT-040 |
| Revocation date | A specified removal date where the review action supports it. Does not prove completed removal; the described reviewer path for individual entitlements does not offer this setting. | CRT-028/032 |
| Remediation | Work required to carry out a removal/change decided in the review. The applicable trigger, path and outcome need evidence. | CRT-032–037 |
| Provisioning | Supported work that changes external accounts/access; inspect the actual operation and result. | CRT-033 |
| Manual fulfillment task | Assigned human work to make an external change. Task closure and actual target state are separate observations. | CRT-034 |
| Retry | Another supported attempt at failed work; conditions and limits are operation-specific. | CRT-036 |
| Status | A recorded state of a particular object or operation. Always identify what the status describes. | CRT-042 |
| Audit evidence | Records supporting what was scoped, reviewed, decided and done, with actor/time/context. It does not automatically establish every claim. | CRT-043/044 |
| Report freshness | When a report was generated and which campaign state it represents; later campaign changes require a fresh report. A new report does not itself generate new review items or prove current source coverage. | CRT-019/044 |
| Asynchronous processing | Work proceeds separately from the submitted request, with task/result evidence needed before claiming the business outcome. A tracking task or accepted request alone does not establish the intended review assignment. | CRT-025; supporting CRT-044/045 |
| API | An application programming interface through which software requests operations or data. Core includes interpreting action/data requests and their results without requiring code execution. | CRT-025/044 |
| Object ID | An identifier for the relevant platform record; a matching display name alone is not an exact record reference. | CRT-042/044 |
| Request/response | An operation/data request and the returned result. An accepted request is not automatically completion of downstream work. | CRT-044 |
| Pagination | Returning a collection in portions; seeing one page does not establish the whole population. | CRT-010/044; X-05 |
| Recommendation / access flag | A certification recommendation suggests decision support using available peer/identity analysis; an access flag identifies a specific fact to inspect. Interpret actual reason, type, source and freshness. Neither supplies a missing current business justification. | CRT-027/031; X-04 |
| Peer group | A comparison group based on similar access patterns; common access can support investigation without establishing this person's current authorized need. | CRT-027; X-04 |
| Source activity | Events gathered from a supported configured application source. Certification active-days context can cover 90 days; source use is not proof of each permission's use or authorization, and absent data is not zero. | CRT-027; X-04 |
| New Access flag | The access has not previously been certified; this does not establish its grant date. | CRT-027 |
| High Privilege (Overridden) flag | An entitlement's privilege classification was manually changed to indicate high privilege; inspect actual sensitive capabilities and need. | CRT-027 |
| Contains Privileged Access flag | A role or profile includes privileged entitlement access; inspect which component and the actual package under decision. | CRT-027 |
| Timebound Access flag | Access has a set end date; the time limit does not itself justify the access until that date. | CRT-027 |
| Comments flag | Comments are associated with access; read author/date/relevance rather than assume a current approval. | CRT-027 |
| Cloud Enabled flag | Access relates to cloud infrastructure; deeper resource/privilege/path and activity context is conditional on support/configuration/licensing. | CRT-027; X-04 |
| Critical Data Access flag | Access includes critical data; investigate actual data/scope and authorized need, using licensed context where available. | CRT-027; X-04 |

## Actual introductory teaching

[CRT-001](../lessons/CRT-001_Why_Review_Previously_Approved_Access.md) now explains access, account, identity, entitlement, source, account aggregation/correlation, review item, access certification, reviewer/certifier, campaign, Approve, Revoke, sign-off/finalization and remediation in context. Its evidence comparison distinguishes an earlier approval, current need, decision and actual account result.

These are supporting introductions for this purpose lesson. CRT-002's authored foundations are recorded next; other primary detailed teaching locations remain planned. Source checking and simulated author review are recorded in [its author record](revisions/CRT-001_Revision_Record.md); no observed beginner test is claimed.

The local [CRT-001 revision 1.1 record](revisions/CRT-001_Revision_1_1_Record.md) preserves the earlier meanings and explains them through separate person/account/right and source/collection/association steps. No distinct working meaning is added or removed. The existing 94-term register remains an author consistency aid, not a prerequisite vocabulary list. Later lessons in the active revision queue must provide their own needed explanations.

[CRT-002](../lessons/CRT-002_Campaigns_Certifications_and_Review_Items.md) now explains certification campaign, certification/assigned review, review item, subject, reviewer/certifier, campaign scope, generation/start, creator/owner, Cert Admin/Org Admin, source/access owner, remediation, decision maker, undecided and sign-off in connected prose. It reintroduces account/access/identity/entitlement and Approve/Revoke as needed. It distinguishes saved item decisions, confirmed review completion, campaign state and target-account outcome.

[The CRT-002 record](revisions/CRT-002_Revision_Record.md) locates each actual teaching purpose. No exact permission matrix, algorithm for grouping reviews, report counter formula or engine finality policy is claimed.

The local [CRT-002 revision 1.1 record](revisions/CRT-002_Revision_1_1_Record.md) preserves these meanings with a clearer one-item-to-review-to-campaign explanation. Scope, generation and starting are existing campaign concepts, explained where used; no distinct working term is added or removed. The current register remains at 94 working meanings. An author review is not evidence that an independent learner has mastered the vocabulary.

[CRT-003](../lessons/CRT-003_From_Access_Data_to_a_Verified_Outcome.md) explains source, connector/integration, account aggregation, correlation, entitlement, generated review item, assigned certification, reviewer, scope/start, Approve/Revoke, sign-off, remediation, provisioning and target system as parts of one trace. It distinguishes collection from granting access, reading from writing, accepted work from account change, and historical review data from refreshed account evidence.

Its local [revision 1.1 record](revisions/CRT-003_Revision_1_1_Record.md) records the clearer contextual explanations and preserved process. No distinct working term is added or removed; the register remains at 94 meanings. A term is connected with its input/action/result where used rather than treated as sufficient explanation by itself.

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

Its local [revision 1.1 record](revisions/CRT-004_Revision_1_1_Record.md) records the expanded contextual explanation of these existing terms, the supporting assignment meaning and locally explained sign-off. The revision adds no distinct working term. Existing primary owners remain unchanged.

## Account-data context authored in CRT-005

| Term | Working meaning and connection | Teaching location |
|---|---|---|
| Account schema | Account fields and their interpretation, including identifying attributes, multiple values and entitlement data. | CRT-005 |
| Account ID | The configured identifier used to reference an account in its source context. | CRT-005/008 |
| Account Name | The configured account-name attribute; a readable login alone is not a global account identifier. | CRT-005/008 |
| Multi-valued | A field can contain several values for one account, such as separate group memberships. | CRT-005 |
| Entitlement catalog | Represented entitlement objects and details; an object definition does not prove a particular account holds it. | CRT-005/009 |
| Entitlement aggregation | Supported collection of entitlement-object information, distinct from collecting a specific account's held values. | CRT-005 |
| Entitlement type | The category of entitlement, linked to account-held values under the supported schema model. | CRT-005/006 |
| Optimized aggregation | Account change checking that can skip unchanged records without reevaluating their correlation. | CRT-005 |
| Unoptimized aggregation | Supported reexamination that includes unchanged account records and correlation evaluation. | CRT-005 |

[CRT-005](../lessons/CRT-005_From_Application_Access_to_Reviewable_Information.md) also explains existing identity/account, source/connector, attributes, account aggregation, correlation/uncorrelated accounts, review objects, reviewer, access model and certifiable-access eligibility. Its supporting meanings are located in [the author record](revisions/CRT-005_Revision_Record.md). It supplies correct unique ownership and actual field values rather than assuming all catalog entries are held by all accounts.

## Review-object context authored in CRT-006

| Term | Working meaning and connection | Teaching location |
|---|---|---|
| Assignment | The association through which an identity holds an access object; distinguish it from the object's shared definition. | CRT-006/007; supporting explanation in CRT-004 1.1 |
| Role assignment | One identity's holding of a role, with the access scope it provides; it is not the role definition for everyone. | CRT-006 |
| Role definition | The role's configured contents and related requirements, separate from each identity's assignment. | CRT-006; X-01 |
| Membership criteria | Configured conditions used to determine automatic role membership. | CRT-006/007 |
| Access profile detection | Recognition of an already-held entitlement set as a profile where supported; not proof of a newly issued grant. | CRT-006/007 |
| Role-composition review | Review of a shared role's definition, contents and membership requirements; distinguish the documented legacy review and manual correction from removing one person's holding. | CRT-006/015; X-01 |
| Role owner | Responsibility for the role; this label alone does not establish platform permission to change the definition. | CRT-006/022 |

[CRT-006](../lessons/CRT-006_Entitlements_Access_Profiles_and_Roles_in_a_Review.md) reintroduces entitlement/profile/role meanings and connects them with actual item scope and assignment origin. Requested roles, criteria roles, requested/detected profiles and contained components receive the locally needed action/eligibility explanation. [Its author record](revisions/CRT-006_Revision_Record.md) locates the teaching and partial-need transfer. Detailed overlap, role configuration and composition remediation remain with their primary owners.

## Appearance and absence context authored in CRT-007

| Term | Working meaning and connection | Teaching location |
|---|---|---|
| Encapsulation | A component is contained in the access object through which it is reviewed; separate component absence does not prove absent access. | CRT-007/017/035 |
| Platform permissions | Authorization to perform actions in ISC, distinct from the application's access being reviewed. | CRT-002/007/021 |

[CRT-007](../lessons/CRT-007_Why_Access_Appears_Differently_or_Is_Missing.md) connects held access, represented values, eligible review units and available actions. It reintroduces objects/origins, campaign filter, certifiable access/model, collection/catalog/correlation and review context where required. [Its author record](revisions/CRT-007_Revision_Record.md) maps the four-right main example and three-absence transfer. A missing item or button alone does not establish its cause.

## Multiple-account and ownership context authored in CRT-008

| Term | Working meaning and connection | Teaching location |
|---|---|---|
| Privileged account | An account with rights for sensitive actions; verify actual purpose/permissions rather than a readable account label. Application privileges do not establish ISC administrative authority. | CRT-008 |
| Authoritative source | A source configured to establish ISC identities from its accounts, such as a personnel source for employees. | CRT-008; supporting CRT-005 context |
| Authoritative identity | An identity established from authoritative-source information; distinguish it from a placeholder representing an unmatched account. | CRT-008; X-02 |
| Account owner | The person recorded as responsible for an account; responsibility for a service account does not make it a personal employee login or establish every platform permission. | CRT-008/022; X-03 |
| Application identity | Representation of a program or process with associated machine accounts; the reviewer experience also uses machine identity terminology. Capability and actual subject need verification. | CRT-008/015; X-03 |

[CRT-008](../lessons/CRT-008_One_Person_Two_Accounts_and_the_Correct_Review_Target.md) reintroduces account/identity/source, Account Name/ID, entitlement, aggregation/correlation, campaign/certification/review item, decision, sign-off, remediation/provisioning and package scope at the points needed. Uncorrelated and machine/service-account meanings are now developed in core prose. [Its author record](revisions/CRT-008_Revision_Record.md) maps those relationships and the exact-account transfer. Five new distinct working terms are added; source account identifiers, display names and platform record IDs remain separate concepts.

## Maintenance

When a lesson is authored, add the actual teaching location to its author record and reconcile any term whose meaning changes by engine/context. Do not mark a term taught simply because it is listed here.

Introduce abbreviations with their plain meaning in each lesson that depends on them. Important examples include ISC, API and lifecycle state (LCS); do not create an acronym solely to shorten a one-time mention.

New terms may be added when a real explanation needs them. Avoid growing a glossary with unrelated IAM material or exposing these author tables as a preliminary vocabulary test.

## CRT-005 explanation revision, November 11, 2026

[Its new revision 1.1 record](revisions/CRT-005_Revision_1_1_Record.md) records the clearer explanations of attributes/schema, identifiers, multi-valued memberships, aggregation, entitlement details/type, correlation and review objects. Each meaning connects to the example's record or operation before being used in the flow. All existing meanings and owners remain; no distinct working term was added or removed. The register remains at 94 meanings. Author reading is not an observed learner vocabulary assessment.

## CRT-006 explanation revision, November 11, 2026

[Its revision 1.1 record](revisions/CRT-006_Revision_1_1_Record.md) locates the clearer entitlement/profile/role, definition/assignment/origin, membership criteria, detection, Acknowledge, lifecycle, composition/owner and removal-work meanings. Existing identity processing and attribute meanings are connected to the concrete workFunction comparison where needed. No distinct term or primary owner changed; the register remains at 94 working meanings. Author reading is not an independent learner vocabulary assessment.

## CRT-007 explanation revision, November 11, 2026

[Its new revision 1.1 record](revisions/CRT-007_Revision_1_1_Record.md) locates the clearer encapsulation, assignment-origin, certifiable-access, campaign-filter, collected-account/correlation and platform-permission meanings. Held permission, package, actual item and allowed action are connected in prose before the diagnosis relies on them. Campaign scope receives its local existing meaning; no distinct term or primary owner changed. The register remains at 94 working meanings. Completion of the rewrite pass does not establish an observed learner vocabulary pass.

## Access meaning and descriptions authored in CRT-009

| Term | Working meaning and connection | Teaching location |
|---|---|---|
| Display name | A readable entitlement label; source and identifying value remain necessary for exact access context. | CRT-009 |
| Entitlement description | Text explaining the actual access capability, relevant scope/data and verified boundaries; editing it in ISC does not change source permissions. | CRT-009 |
| Business purpose | The work access is intended to support, distinct from this person's current need; not a guaranteed ISC field. | CRT-009 |
| Metadata | Information describing an access object; configured access fields differ from identity attributes and are not automatically all visible to reviewers. | CRT-009/027 |
| Privileged access | Access to sensitive actions or information; inspect actual capability and context, not only an account name or flag. | CRT-009/027; supporting account context in CRT-008 |
| Privilege classification | Categorization of entitlement privilege through configured methods or manual handling; not proof of this person's need or absence of risk when unset. | CRT-009/027; X-04 |

[CRT-009's record](revisions/CRT-009_Revision_Record.md) maps these six added meanings to connected explanations and examples. Existing access-owner, source-owner, attribute, package, catalog, action and recommendation/flag meanings are locally reintroduced. The register now has 100 distinct working meanings; no earlier term is removed. Actual learner vocabulary assessment remains pending.

## Population comparison authored in CRT-010

| Term | Working meaning and connection | Teaching location |
|---|---|---|
| Review population | The people, accounts and access intended for a review, under an explicit scope and observation time. | CRT-010/013/014 |
| Expected baseline | Evidence-supported list of relationships that should be accounted for, independently checked against the business requirement. | CRT-010/021 |
| Reconciliation | Comparing intended and actual records and explaining missing/unexpected person-account-access relationships. Equal totals or a clean selected case cannot erase another known gap. | CRT-010/021 |
| Coverage gap | Intended review content not adequately accounted for; a label or progress percentage does not establish resolution. | CRT-010/021/045 |

[CRT-010 record](revisions/CRT-010_Revision_Record.md) locates these four new meanings and the locally reintroduced pagination, preview, query/refinement/filter, collection/correlation and review-unit meanings. The register now has 104 distinct working meanings. No earlier meaning is removed, and no observed learner vocabulary result is claimed.

## Manager-review foundations authored in CRT-011

| Term | Working meaning and connection | Teaching location |
|---|---|---|
| Manager review | Manager assessment of current access need for supervised people's work; reliable technical meaning and actual assignment are still needed. | CRT-011 |
| Manager relationship | The link identifying one identity as another identity's manager; distinguish source reference and generated reviewer assignment. | CRT-011/022/023 |
| Manager correlation | Configured establishment of an employee's manager link. In the documented attribute-based case, null can clear the link while an unmatched changed reference can retain the existing manager; source text, current link and generated assignee are distinct. | CRT-011/023 |
| Identity profile | Settings for establishing/maintaining identities from source data, including identity attribute mappings; distinct from an access package. | CRT-011; source-data support |
| Reviewer fallback | Alternative review responsibility when the normal reviewer cannot be determined; actual handling is campaign-route specific and does not establish expertise. | CRT-023; supporting CRT-011 |

[CRT-011 record](revisions/CRT-011_Revision_Record.md) maps these five new meanings to the source value, unique identity match, actual assignment and worked transfer. Existing account correlation/aggregation, attribute, identity processing, campaign objects, creator, package/rule, preview, sign-off and reassignment meanings remain locally understandable. The register now has 109 distinct working meanings. No earlier meaning is removed or independent learner result claimed.

## Source-owner review authored in CRT-012

| Term | Working meaning and connection | Teaching location |
|---|---|---|
| Source-owner review | Review of access within selected sources using appropriate source-owner responsibility and expertise, with actual assignment and current need verified. | CRT-012 |

[CRT-012 record](revisions/CRT-012_Revision_Record.md) locates the new meaning and primary explanation of the existing source-owner term. Existing access-owner, reviewer, campaign object, source/connector/account, collection/correlation, package/rule, population, preview and reassignment meanings are explained locally. The register now has 110 distinct working meanings; none is removed and no observed learner vocabulary pass is claimed.

## Selection orientation authored in CRT-013

| Term | Working meaning and connection | Teaching location |
|---|---|---|
| Identity-oriented selection | Choose person identity records first, then determine which of their access belongs in the campaign. | CRT-013 |
| Access-item-oriented selection | Choose access definitions first to identify included holders; a later access choice determines what is reviewed for those people. | CRT-013 |

[CRT-013 record](revisions/CRT-013_Revision_Record.md) maps these two meanings and locally explained query/result type, all versus specific selection, object definition versus holding, entitlement/profile/role, standalone/container, refinement, preview and reviewer. There are now 112 distinct working meanings. No earlier meaning is removed or observed learner vocabulary pass claimed.

## Access refinement authored in CRT-014

[CRT-014 record](revisions/CRT-014_Revision_Record.md) locates the primary access-refinement explanation and locally reintroduced identity/account/source/entitlement, object reference, profile/role/model, access request, membership criteria, lifecycle state, campaign/review/item, reviewer, preview and campaign-filter meanings. Saved scope, current holding, review decision and actual account change remain distinct. No new meaning is added solely to increase glossary size: 112 distinct working meanings remain. No earlier term is removed or learner vocabulary pass claimed.

## Review targets authored in CRT-015

| Term | Working meaning and connection | Teaching location |
|---|---|---|
| Assignment review | Review purpose assessing whether a particular person's holding of an access object remains appropriate; this is not a separate invented campaign tile. | CRT-015; supporting CRT-006/013 |

[CRT-015 record](revisions/CRT-015_Revision_Record.md) locates the new assignment-review entry and the expanded existing role-composition meaning, along with local identity/account/source/object, manager/source/role ownership, actual reviewer, remediation owner, preview, uncorrelated and application/machine identity explanations. The register now has 113 distinct working meanings. Earlier meanings are preserved; no observed learner vocabulary result is claimed.

## Search meanings authored in CRT-016

| Term | Working meaning and connection | Teaching location |
|---|---|---|
| Search category | The kind of record being searched and returned; account/access conditions inside identity data still return identities. | CRT-016 |
| Search field | The specific named information checked on the selected record model; exact path, case, type and related-record context matter. | CRT-016 |
| Data model | Organization of fields and related records for an object type; source on an identity differs from source inside an account. | CRT-016 |
| Boolean operator | Logical combination such as AND or OR; the scoped Search rules do not establish another filter builder's behavior. | CRT-016 |
| Nested query | Query conditions applied inside related records, such as accounts; one grouped account query differs from separately satisfied account tests. | CRT-016 |

[CRT-016 record](revisions/CRT-016_Revision_Record.md) locates the five new meanings and local attribute/mapping, query, person/account/source, authoritative source, access object, refinement, filter, preview and reviewer explanations. There are now 118 distinct working meanings. Earlier meanings are preserved, and no observed learner vocabulary pass is claimed.

## Filter meanings authored in CRT-017

| Term | Working meaning and connection | Teaching location |
|---|---|---|
| Filter criterion | A test identifying the kind of information, source/field where relevant, operation and value used to find matches. | CRT-017/018 |
| Inclusion filter | Filter mode retaining matching review content under the supported criterion's scope; entitlement matching can narrow both people and items. | CRT-017 |
| Exclusion filter | Filter mode omitting matching review content; an entitlement exclusion and a person exclusion do not remove the same work. | CRT-017 |
| Comparison operation | How a criterion checks a value, such as Equals, Contains or supported Starts With; separate from the filter's inclusion/exclusion mode. | CRT-017 |

[CRT-017 record](revisions/CRT-017_Revision_Record.md) locates these four new meanings and local person/account/source, attribute/display label/source value, entitlement/profile/role/lifecycle, preview and reviewer explanations. There are now 122 distinct working meanings; none is removed and no observed learner vocabulary pass is claimed.

## Combined meanings developed in CRT-018

[CRT-018 record](revisions/CRT-018_Revision_Record.md) locates the connected use of identity/account/source/attribute/mapping, query and grouping, actual people selection, holdings, access refinement, filter/criterion/mode, entitlement versus identity scope, requested profile/role containment, preview and reviewer. Meaning is supplied locally instead of relying on a glossary or prior lesson. This unit consolidates existing meanings; 122 distinct working meanings remain, with no artificial entry added and no learner vocabulary pass claimed.

## Time and record meanings developed in CRT-019

[CRT-019 record](revisions/CRT-019_Revision_Record.md) locates observation/collection, identity/account correlation, generation/snapshot, current source/ISC data, Search availability, current reviewer versus decision maker, saved decision/sign-off, reassignment, preview/start and report freshness in connected prose. The three time labels organize these existing meanings without adding glossary filler. Generated snapshot is scoped to certification review work rather than another product's similarly named feature. Existing 122 working meanings remain; no standalone learner glossary or tooltip implementation is claimed.

## Reusable instructions and campaign-cycle meanings in CRT-020

[CRT-020 record](revisions/CRT-020_Revision_Record.md) locates template, schedule/recurrence/time zone, generation, preview, activation, deadline, campaign/assigned certification/item, owner/administrator/authorization, identity/account/source/entitlement and API/request/result meanings in the saved explanation. Staged and Experimental are explained only within the checked activation reference, not declared universal UI labels. Source/account and software-interface meanings were expanded during beginner author reading. Existing 122 working meanings remain; no standalone glossary or tooltip implementation is claimed.

## Preview acceptance meanings developed in CRT-021

[CRT-021 record](revisions/CRT-021_Revision_Record.md) locates scope/identity/account/holding, entitlement/source/collection, campaign/certification/item/generation/preview, actual reviewer/Individual choice, authority, role/profile/filter, deadline/comments, undecided versus saved/unsigned/sign-off, template/email redirection, operational exception and API/job/start evidence. Exception is explained as a business-process departure, not a native campaign status. Existing 122 working meanings remain; no ordinary-language label is added just to increase the glossary. No learner tooltip implementation is claimed.

## Reviewer responsibility meanings developed in CRT-022

[CRT-022 record](revisions/CRT-022_Revision_Record.md) locates campaign/certification/item, identity/account/source/entitlement, manager relationship/correlation, creator/campaign owner, primary/additional access ownership, source/account/role owner, named Individual, governance group/member/owner/actor, fallback/self-review/work reassignment, current reviewer versus decision maker, sign-off and platform authorization. Ordinary Manager routing and independent Access Owner mismatch are distinguished from missing-input effects. Existing 122 working meanings remain; group voting/sign-off contracts and every owner hierarchy are not invented.

## Missing-responsibility meanings developed in CRT-023

[CRT-023 record](revisions/CRT-023_Revision_Record.md) introduces Fallback as a primary operational routing meaning, raising the register to 123. Exclusion, null/absent reference, retained manager link, missing versus unusable identity, primary/additional ownership, source prerequisite, empty versus inactive-member group, current assignment, reassignment/sign-off and actual review outcome are explained where used. The owner sequence is not a universal access-request approval hierarchy. No standalone learner glossary or tooltip behavior is implemented.

## Own-access meanings developed in CRT-024

[CRT-024 record](revisions/CRT-024_Revision_Record.md) locates self-certification, human subject versus reviewer, identity/account/source/entitlement, complete access object, campaign/certification/item/generation/preview, manager/owner/creator/admin, automatic work redirection versus manual reassignment, mixed review, group/member/actor, sign-off and decision maker in connected prose. New owner of an assigned certification means recipient responsibility, not campaign ownership. Existing 123 working meanings remain. A group identifier or administrator title is not used to invent an own-access exception, voting rule or hidden permission algorithm.

## Handover and task/result meanings developed in CRT-025

[CRT-025 record](revisions/CRT-025_Revision_Record.md) locates whole certification, subject versus item, exact account/access, actor/recipient/knowledge/state, reason, saved versus signed off, current assignee versus actual decision maker, recipient visibility and future-work configuration in connected prose. Asynchronous processing is a new explicitly explained technical meaning, raising the register to 124. Experimental APIs and object/task responses are interpreted within their checked scopes rather than used as a universal completion, identity-preservation or retry guarantee.

## Absence and configured work meanings developed in CRT-026

[CRT-026 record](revisions/CRT-026_Revision_Record.md) connects existing reassignment with the new Work reassignment meaning: configuration instruction versus current certification, separate work types, recipient/period/time zone, one-per-person/type replacement, no end date and retained prior work. The register becomes 125 working meanings. Campaign/certification/item, source/identity/account/entitlement, preview/sign-off, actor/authority, permanent manager/owner/group responsibility, API, own-access routing, history, audit, current reviewer and earlier decision maker are reintroduced locally. First configured recipient is not assumed to be the last assignee. No glossary dependency or tooltip implementation is claimed.

## Review-context meanings developed in CRT-027

[CRT-027 record](revisions/CRT-027_Revision_Record.md) connects exact identity/account/source/entitlement, Additional Attributes and person attributes, capability/current need/authorization, package/origin, capture versus business-confirmation times and decision/outcome. Peer group, Source activity and seven newly registered flag labels add nine meanings, bringing the register to 134. Existing Birthright access and recommendation/flag meanings are extended without duplicate rows. Cloud/data/AI product context remains conditional, and all necessary reasoning is inline. No glossary prerequisite, universal activity coverage or tooltip implementation is claimed.

## Action meanings developed in CRT-028

[CRT-028 record](revisions/CRT-028_Revision_Record.md) extends Approve/Revoke/Acknowledge through exact person/account/item, unit/origin/type, continued need, automatic conditions and the selected package's contents. Revocation date adds one meaning, bringing the register to 135. Existing sign-off, remediation/provisioning, role/profile/lifecycle, membership/identity processing, owner/authority and undecided/unsigned meanings are locally connected without duplication. A component view is not an independent decision, and a person's role assignment is not the shared definition. No tooltip implementation, universal date control or target-result guarantee is claimed.

## Decision-quality meanings developed in CRT-029

[CRT-029 record](revisions/CRT-029_Revision_Record.md) introduces Decision criteria, Decision comment and Bulk decision in connected prose, raising the register from 135 to 138 working meanings. Existing identity/account/source/entitlement, review objects, Approve/Revoke, package/role, filters, authority, finalization, current Reviewer/Decision Maker, report freshness and evidence meanings are locally reintroduced. Business criteria are not selection filters; valid shared action is not necessarily identical reason text. Comments-field names do not establish all text authorship. No glossary prerequisite, tooltip, universal UI control or completed-removal inference.

## Finalization meanings developed in CRT-030

[CRT-030 record](revisions/CRT-030_Revision_Record.md) connects item choices, undecided versus unsigned, sign-off, distinct object state/count, permitted edits, campaign completion, signer/owner/decision maker, report dates/freshness and actual account outcome. Reauthentication adds one working meaning, raising the register to 139. Three choices out of three do not establish one signed review; first decision time does not establish sign-off. OQ-01 and new OQ-10 retain unresolved broader outcomes rather than manufacturing a rule. No glossary dependence, exact API status enum or universal progress-widget claim.

## Uncertainty meanings developed in CRT-031

[CRT-031 record](revisions/CRT-031_Revision_Record.md) adds Consultation, bringing the register to 140 working meanings. Existing source/person/account/access/review, owners/authority, package/origin, reassignment/preview/self-review, recommendation/peer/flag/activity, undecided/unsigned/sign-off/Acknowledge and evidence meanings are locally reintroduced. Missing capability/need evidence is not confirmed no need; knowledge and permission are separate; answers, actual transfer and account result establish different facts. No glossary prerequisite, tooltip or automatic escalation/pause feature is claimed.
