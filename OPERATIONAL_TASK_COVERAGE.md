# ISC certifications: operational task coverage

Planning revision 1.2. October 29, 2026.
Companion to [course design 2.1](COURSE_DESIGN.md).
Status: coverage committed for authoring. CRT-001 revision 1.0 develops the purpose/current-need foundation for task 1 and introduces supporting access/decision/outcome meanings. Other task mechanics remain planned. Actual learner performance has not been validated.
Authoring must follow the [teaching specification](TEACHING_SPECIFICATION.md) and reconcile each completed task against its saved lesson record.

This map gives routine work an explicit place. It is not a statistical ranking of customer task frequency. Planning labels remain provisional. Change lesson boundaries if a task needs a clearer independent explanation.

Every mapped task must teach the purpose, actor/permission, required input, applicable rule or operation, outcome, meaningful changed condition and evidence. Responsible owner and authorized operator are not assumed interchangeable.

## Before launch

| Task | What the learner must reason through | Planned location |
|---|---|---|
| 1. Clarify the review request | Business question, people/access/accounts in scope, accountable owners and required outcome. | CRT-001/011–015/047 |
| 2. Check source data and ownership readiness | Collected versus live access, correlation, manager/source owner, missing data and account identity. | CRT-005/008–010/023 |
| 3. Choose a campaign approach | Manager/source-owner/targeted review and the scope each actually addresses. | CRT-011–015 |
| 4. Build and validate selection | Query meaning, identity versus access results, inclusion and exclusion examples. | CRT-013/014/016 |
| 5. Apply filters without losing the intended population | Supported criteria/combination, encapsulated access and inclusion/exclusion evidence. | CRT-007/017/018 |
| 6. Reuse or schedule a review correctly | Template versus generated campaign, preview timing, recurring work and activation responsibility. | CRT-019/020 |
| 7. Validate generated contents and reviewers | Compare intended baseline to actual identities/items/assignees, samples, omissions and settings. | CRT-010/019/021–024 |
| 8. Establish launch readiness and authority | Data/exception readiness, due-date/comment/notification choices, permissions and approved activation responsibility. | CRT-002/021/048 |

## During an active review

| Task | What the learner must reason through | Planned location |
|---|---|---|
| 9. Check campaign and reviewer progress | Correct unit, status, pending work, generated data and current observation time. | CRT-038/042/044 |
| 10. Investigate a missing or incorrect reviewer | Manager/owner inputs, selected campaign rules, fallback and generated assignee. | CRT-022–024/045 |
| 11. Handle reviewer absence or departure | Campaign reassignment versus work reassignment, eligible replacement, state and self-review restrictions. | CRT-024–026 |
| 12. Investigate why the reviewer cannot see or open work | Correct identity/environment, actual assignment, campaign state, sign-off and permitted access; no assumed universal cause. | CRT-021/025/042/045 |
| 13. Investigate missing, unexpected or repeated-looking items | Scope, filter, grant origin, account identifier, uncorrelated data and snapshot timing. | CRT-005–010/016–019/045 |
| 14. Help the reviewer understand and record a decision | Access meaning, business need, Approve/Revoke/Acknowledge, comments and limits of bulk decisions. | CRT-027–031 |
| 15. Distinguish undecided work from an unsigned review | Item decisions, review finality, deadline/completion policy and engine-verified behavior. | CRT-030/039/040 |
| 16. Investigate notifications and follow up | Notification configuration versus assignment/visibility, reminder work and evidence of the actual delivery issue. | CRT-021/038/045 |

## After decisions and through closure

| Task | What the learner must reason through | Planned location |
|---|---|---|
| 17. Establish whether removal work should have started | Decision finality, supported trigger, revocation timing and exact item/account. | CRT-028/030/032 |
| 18. Track automated or manual fulfillment | Applicable write path, authorized integration or assigned human task, action versus completion. | CRT-033/034/044 |
| 19. Diagnose failed, pending or partial remediation | Actual operation, permissions, target rejection, supported retries and partial results. | CRT-036/046 |
| 20. Explain retained access after revocation | Assignment origin, shared entitlements, other paths and applicable access-model changes. | CRT-006/007/035/046 |
| 21. Verify the required removal | Correct target account/right, actual target observation, task/operation result and refreshed ISC representation. | CRT-034/037/046 |
| 22. Produce and explain review evidence | Composition/status/sign-off/remediation/provisioning records, decision maker, timestamps and report freshness. | CRT-042–044 |
| 23. Complete the campaign and hand over unresolved work | Administrative completion versus delivery, approved undecided handling, exceptions, ownership and closure criteria. | CRT-039–041/050 |
| 24. Prepare the next cycle or a changed review requirement | Revisit population, assignments, template, business criteria, prior exceptions and acceptance evidence. | CRT-020/047–050 |

## Specialist depth and its core foundation

| Area | Required core understanding | Deeper route and trigger |
|---|---|---|
| Role composition | A person's role assignment and a role's contents are different review subjects. | X-01 when responsible for role governance or role-composition campaigns. |
| Uncorrelated accounts | Recognize absent authoritative ownership and its effect on ordinary scope, reviewer selection and investigation. | X-02 for dedicated uncorrelated-account reviews and their fulfillment cases. |
| Machine/service accounts | Recognize non-human account purposes and avoid assuming an employee manager or personal owner. | X-03 when responsible for supported machine-account reviews; verify tenant capabilities. |
| Flags, recommendations and activity | Understand any available context as evidence, with source/freshness/availability limits. | X-04 for detailed licensed insight configuration and unusual interpretation cases. |
| APIs and automation | Explain IDs, request/response records, status and permissions; choose read-only evidence appropriate to the engine. | X-05 for bulk/paginated investigation and automation design. Coding remains in a later hands-on course. |

A deeper route may be essential for a particular job. Its separate placement keeps unrelated implementation depth out of the general learner's route; it does not mark that subject as rare or unimportant.

## Current authored coverage

[CRT-001 author record](author/revisions/CRT-001_Revision_Record.md) maps the purpose foundation and supporting introductions to actual saved sections. This does not complete task 1's campaign-design depth or mark delivery/reporting tasks fully taught. The detailed planned locations above remain responsible for those mechanisms.

## Evidence of learning

For the task being assessed, give an unfamiliar situation and supplied evidence. The learner should explain what is happening, identify missing evidence, choose a useful next check and justify the expected outcome under stated conditions.

For example:
- A reviewer is named in a report but cannot find an active review.
- A person is absent from a generated manager campaign.
- A manual removal task is closed but the collected entitlement still appears.
- An access profile is revoked while another assignment contains a shared entitlement.
- A report is complete but was generated before the latest review changes.

Do not treat reading completion, matching totals or a memorized button sequence as an assessment pass. Tenant execution remains separate later practice.
