# BaselineA: a small manager review

Specification1.3. November14,2026. The [three canonical CSV fixtures](baselineA/README.md) are authored and locally reconciled. Actual source-template alignment, private email binding and tenant import are not run.

## Purpose

Prepare enough data to complete one manager review and reconcile its CSV outcome. A later connected variant verifies a real external account change. The small inventory makes it possible to account for every person, account and reviewed right without relying on a percentage.

The first dataset uses five identities: three employees and two managers. Only the employees have accounts in the simulated application data. The managers can perform their assigned reviews through separate permitted sessions.

## People and ownership

These labels are course aliases. Bind them to actual source values and immutable IDs during CLB-002 after defining the two fresh manual CSV-upload sources and their schemas. Use separate people-account, review-account and entitlement-catalogue files. Manager reviewer logins are arranged separately; importing their records does not create authenticated sessions.

| Identity alias | Purpose | Manager identity alias | Test application account |
|---|---|---|---|
| certlab-employee01 | Still needs report viewing and exporting | certlab-manager01 | certlab-account01 |
| certlab-employee02 | Still needs viewing; the export task has ended | certlab-manager01 | certlab-account02 |
| certlab-employee03 | Needs viewing only | certlab-manager02 | certlab-account03 |
| certlab-manager01 | Reviews employees01/02 | No manager required for this initial target population | No account on this test application |
| certlab-manager02 | Reviews employee03; recorded source owner for this fixture | certlab-manager01 | No account on this test application |

Do not map an employee's manager field to their own identity or substitute an arbitrary available reviewer. The stored source values, identity attributes and actual manager identity link must agree.

Managers' lack of target-application accounts is part of this initial fixture. It keeps their own access outside this first manager case. A later source-owner lab explicitly adds and verifies an own-access case; do not silently assume that extension already exists.

## Permission meanings and initial holdings

Read Reports means viewing reports; Export Reports means downloading them in bulk. In the first CSV phase these are permissions in a simulated application, represented by entitlement values. No real reporting product or account capability is implied.

Bind two individually reviewable entitlement values and metadata to the actual review-source schema. Define required columns, keys, manager matching, account correlation and multivalue syntax before issuing import files. Verify those values and five collected holdings in ISC.

In a later connected variant, use actual independently reviewable permissions and record their real names, identifiers and meanings. A direct extension of this manager case can preserve its five-holding pattern and one-remove/four-retain outcome. CLB-011 instead uses the separate [native C contract](baselineC/README.md): four scoped memberships across two accounts, with distinct normal-removal and permission-failure groups. Its task does not copy A's item count. Do not label an unrelated group Export Reports to pretend it controls exporting.

If the target is a directory and the demonstrated right is group membership, state and verify that membership outcome. Do not claim that a downstream application ability was removed unless its relationship and result are established.

| Application account alias | Read Reports | Export Reports | Business decision to establish |
|---|---|---|---|
| certlab-account01 | Present | Present | Retain both for current authorized work. |
| certlab-account02 | Present | Present | Retain reading; remove export because that task ended. |
| certlab-account03 | Present | Absent | Retain reading; do not invent a missing export review item. |

This is three accounts and five direct entitlement holdings. Expected decisions are four Approve and one Revoke, provided this exact baseline and business context are confirmed.

The intended managers must assess these facts. A successful exercise does not mean clicking every choice because this blueprint supplies an answer. In the actual learner lab, present the current-work evidence and ask for reasons before showing worked decisions.

## Conditions needed for this five-item exercise

Every application account belongs to its intended employee identity. The relevant current account data has been collected, and both employee-manager relationships resolve to the correct manager identities.

The five rights are individually reviewable direct entitlements for these identities. No existing profile detection, role, lifecycle state or other automatic requirement changes their review unit or restores the rejected export. Inspect those relationships before accepting the fixture. Choose isolated test rights or the correct later package variant if the condition is not true; do not alter unrelated access models.

The CSV baseline, collection result and expected review set must agree. A connected variant additionally requires actual external account observations. A matching display name or successful aggregation job is not sufficient.

Managers are eligible, can use their own approved sessions and do not own the employee accounts. The campaign creator has the actual permission needed to create and start this supported campaign.

The configured scope must select precisely the intended population and these rights. If the available dedicated route cannot isolate the fixtures with a verified criterion, arrange a supported scoped setup before running it. Never launch a broad campaign merely to get the three intended employees into it.

## Expected responsibility and generated work

certlab-manager01 is responsible for employee01/02 and certlab-manager02 for employee03. Inspect the actual preview, its grouping and recipient assignments. Do not infer a universal certification-object count from the number of people or managers.

Compare all five person-account-right holdings, correct target source and actual reviewers. Keep examples of excluded unrelated accounts as part of the scope check where they exist.

## Outcomes to prove

CSV phase: after justified choices and final confirmation, inspect any actual manual task and recipient. Remove only Export Reports from certlab-account02 in a new review-account file version, explicitly as a simulated external change. Follow the tested task workflow; do not assume uploading a file closes a task. Collect the revised account data and verify four remaining holdings in ISC.

Read Reports remains on all three accounts. Export Reports remains on certlab-account01. certlab-account03 does not acquire export. Preserve both file versions and reconcile the account/right records, review history and actual task state. These are real ISC/file observations over a simulated application.

Connected phase: the supported actual change must remove the rejected right from the real account, preserve approved rights and agree with fresh ISC data. A signed review, closed task or uploaded CSV alone does not prove that external outcome. Keep the CSV and connected results separate.

## Reset and repeated use

Before resetting, preserve the completed review and its evidence through the training process. Inspect outstanding requests/tasks so the reset is not racing earlier work.

For CSV runs, restore only the approved baseline file version, collect it and verify the five holdings and relationships. Preserve completed campaign/task history and do not reset while earlier manual work could apply again.

For connected runs, restore only this approved test baseline using the target's supported authorized grant/change process. Regranting employee02's export here resets a training fixture; it is not a business recommendation to restore access removed from a real employee.

Verify the exact five baseline holdings, ownership/manager links and absence of outstanding prior work before the next lab that declares baselineA. Use a distinct campaign instance for a new run. Do not treat an old signed review as editable.

Keep a private run ledger mapping course aliases to actual objects and times. A failed reset leaves that baseline not ready.

## Later datasets

A profile/role, owner-own-access, multi-account or failure case needs an explicitly defined extension in its owning lab. Do not carry a changed fixture into another lab without identifying its starting state. The baselineA package defines the normal case only; its narrow fixture headers are not a substitute for actual source templates.
