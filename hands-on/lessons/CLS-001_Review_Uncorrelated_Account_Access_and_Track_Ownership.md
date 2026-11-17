# Review uncorrelated account access and track ownership

ISC can collect an account and its permissions without knowing which authoritative person record the account belongs to.

You can still have useful questions to answer: why does this account exist, which permissions does it need, and who will resolve the missing ownership link?

Let's review the permissions without pretending that the review itself identifies the person.

## Understand what is missing

An **identity** is ISC's record for a person. An **authoritative source** supplies the trusted people data used to establish those records.

An **account** is a record on a managed system. **Account correlation** matches that account to an identity using configured attributes.

An **uncorrelated account** has not been associated with an authoritative identity. It can still have collected permissions.

That label does not prove the account is unused, malicious or a service account. It tells us something specific about its association in ISC.

A **campaign** groups access reviews. A **certification** is an assigned review inside it. Reviewing an uncorrelated account's access is different from proving who personally owns that account.

## Use one unmatched account and one linked control

A **source** holds ISC's configuration and collected account data for a managed system. An **entitlement** represents a specific access value. Read uses `certlab-report-read`; Export uses `certlab-report-export`.

Use a fresh Generic manual-upload source:

`certlab-uncorrelated-reports-csv`, called **D** here.

Keep the existing people source/profile and original three employee/two manager identities. The administrator needs source/schema/correlation setup, campaign/report inspection and permitted upload/task actions. The `certlab-manager02` reviewer session must already work; importing a people record does not by itself provide a working sign-in.

The second account is a **control**: a comparison account whose expected match is known. It should link to employee01 while the target stays unmatched.

Use these supplied values:

| D account | employeeNumber value | Intended association | Initial access |
|---|---|---|---|
| certlab-uc-account01 | certlab-unmatched01 | No authoritative identity match | Read and Export |
| certlab-uc-control01 | certlab-employee01 | Existing employee01 | Read |

The control helps us check the setup. If both accounts unexpectedly remain unmatched, we should investigate the mapping instead of assuming we created the intended test.

The Read and Export values may look familiar, but on D they are separate source-specific objects.

D starts with two accounts and three holdings. A **holding** means one account having one permission: the target has two, and the control has one. Keep A, `certlab-reports-csv`, at its original five holdings and B, `certlab-owner-reports-csv`, at six. No connected directory is needed.

The new files are:

- `lab-data/baselineD/uncorrelated_report_accounts.csv`.
- `lab-data/baselineD/uncorrelated_report_entitlements.csv`.
- `lab-data/baselineD/uncorrelated_report_accounts_after_export_removal.csv`, an expected comparison for later.

Keep the comparison separate until the actual review and required removal work have been established.

## Prepare only this fresh source

First check that the training tenant offers the documented **Uncorrelated Accounts** campaign type and an appropriate reviewer option. If the route or required permission is missing, record the execution prerequisite rather than create a different campaign and label it equivalent.

Open **Admin > Connections > Sources > Create New**, find **Generic** and use its supported Configure or Standard Setup flow for manual CSV upload.

The **source owner** is the person responsible for the source in ISC. Name the new source `certlab-uncorrelated-reports-csv`, add a clear test description and set its actual source owner to `certlab-manager02`. Verify the owner in **Source Setup > Base Configuration**.

Source ownership makes manager02 responsible for this source's work. It does not establish that the unmatched account is manager02's personal account.

Keep D **non-authoritative**. Do not select it as the account source for a new identity profile. We want to inspect an unmatched application account, not manufacture another trusted person.

Check the actual connection mode and dependencies. If the selected setup requires a virtual appliance, a component used by some connections, establish that requirement. Do not mix manual upload with a remote file-fetch connection or assume Generic provides working authentication passwords.

## Match the files and correlation rule before loading

A **schema** defines the fields stored for an account. String means text; scalar means one value, while multi-valued allows several values. Under D's **Account Management > Account Schema**, establish:

| Field | Required meaning |
|---|---|
| id | Scalar String; Account ID, identifying this source account. |
| name | Scalar String; Account Name, the name stored for this account. |
| employeeNumber | Scalar String; the value to compare with the person's Identification Number. |
| groups | Multi-valued entitlement field using the source's supported entitlement association. |

For groups, verify **Multi-Valued** so one account can hold both Read and Export. Verify **Entitlement** so those values are treated as access that can be governed, rather than ordinary account text.

Download D's actual account template through **Account Aggregation > Download Account Schema**. Prepare a complete private copy with the supplied values in the correct columns, preserving additional required fields and column order.

In the supplied format, the target has adjacent Read and Export rows. They describe one account with two values, not two separate accounts. Keep repeated scalar values identical and accounts grouped/sorted by account name.

Before first collection, open D's **Account Management > Account Correlation**. Configure account **employeeNumber** to match identity **Identification Number**, `identificationNumber`.

Inspect preset criteria and keep only the explicit pairing needed on this fresh test source. Do not change another source's correlation configuration.

For the control, `employeeNumber=certlab-employee01` matches employee01's Identification Number, so it should link to that existing identity. The target's `certlab-unmatched01` has no intended person match. Read and Export values do not participate in this pairing.

Verify that employee01 is the only intended identity with that identification number. Also establish that no authoritative identity has `certlab-unmatched01`, and no manual association already links the new target account.

ISC also has fallback matching: when configured criteria do not match, it can compare Account Name with an identity's `name`. Before first collection, check that no existing identity is named `certlab-uc-account01`, including different capitalization. An unmatched employeeNumber alone is not enough.

The unmatched value is a synthetic external key. Do not add it to the people file or change it to somebody else's key just to produce a match.

**Aggregation** reads supplied data into ISC. The **entitlement catalogue** describes D's Read and Export values; the account file says which account holds each value. They are different inputs for the same source.

Open **Entitlement Management > Entitlement Aggregation**. Download the actual catalogue template, prepare it with D's Read/Export definitions and upload it. The catalogue IDs must match the account groups values exactly.

Then upload the complete private initial account file through D's **Account Management > Account Aggregation**. Follow successful completion before inspecting the result.

The Generic setup's **Review and Import Accounts** option can accept a file for correlation recommendations without aggregating those accounts. Use the account aggregation result to establish that the account data was actually collected.

## Inspect the two different account results

Open D's **Account Management > Accounts** and inspect both records.

The control should be linked to employee01 and retain Read. The target should have Read+Export without an authoritative person association.

Use the **Correlated** and **Uncorrelated** filters to inspect the difference. The target may appear with an Uncorrelated label and a **shadow identity**, the record ISC uses to represent unmatched account data.

That representation is not proof that a new trusted human identity has been established. Record its actual identifier and source-account relationship.

Do not assume one shadow record always equals one account. Inspect the actual accounts represented in the review; uncorrelated accounts can sometimes be grouped.

If the target is linked unexpectedly, inspect the configured criteria, key values, fallback name match and manual associations. If the control is unmatched, inspect its key, the existing person's mapped attribute and the source's collection/correlation result.

Do not continue by manually assigning the target to a convenient person. That would change the problem before we have reviewed it.

## Establish a reason for each permission

Before deciding, record the business evidence for the exact account.

A **custodian** is the named person overseeing this account's use and follow-up. That responsibility does not establish who personally owns the account or prove a person-account link in ISC.

For this controlled exercise, use the following supplied confirmation:

- Manager02 agrees to oversee the temporary work that needs this account to read reports.
- Read is still authorized for that limited work. Record a near-term follow-up date and responsible custodian in the run notes.
- Bulk-export work has ended; no continuing Export need is authorized.
- The individual account owner is still unverified and needs separate investigation.

**Approve** records that access should be kept. **Revoke** records that it should be removed. These facts support keeping the limited Read access and removing Export, with a separate ownership investigation still open.

If a real case lacks purpose, authority or custody evidence, seek that information and keep the outcome unresolved or handed over. Do not copy this exercise's approval into an unknown account case.

The follow-up date tells the responsible person when to investigate again. Typing it in a comment does not schedule automatic expiry. This entitlement review does not offer a future revocation date, so do not assume Read will stop on the date you record.

## Create the dedicated account review

Open **Search > Certification Campaigns > New Campaign > Uncorrelated Accounts**.

Select only D as the source. Inspect the displayed accounts before choosing **Certify These Accounts**.

The candidate set must contain the unmatched target and exclude the correlated control. Do not select A, B, the people source or all tenant sources to make the target appear.

Name the configuration `certlab-cls001-uncorrelated-run01`. If that name already exists, use an unused run suffix and record it; preserve earlier history.

Use **Source Owner** as reviewer when offered, then verify manager02's actual assignment. If this supported campaign implementation instead offers an explicit **Individual** selection, choose the verified source owner and record that explicit route; do not describe it as tested automatic source-owner routing.

If no suitable supported option exists, keep execution not ready. An invented manager association is not a substitute.

Use a permitted future deadline, the date by which the reviewer should finish. Choose to maintain undecided access when completing the campaign: access left without a decision is kept under that setting, without implying a completed review. Require Revoke comments, or all comments if that is the offered rule. Turn campaign emails off.

A saved **template** stores campaign settings. A **preview** is the generated review work you inspect before releasing it to the reviewer. Choose to generate the preview now and save it as a template, without a future schedule. Record the saved and generated references separately. Do not add a filter that defeats inclusion of the unmatched account; inspect any preset filter and the actual scope.

The preview should contain only the target's D Read and Export holdings, with the correct actual reviewer. Check the source/account/entitlement values and any grouped uncorrelated representation. No control account or unrelated person's access belongs here.

If it is empty, check that the target is still uncorrelated, D is selected and the saved filter/selection permits it. Do not correlate the account or broaden the campaign as a shortcut.

When the actual preview matches, select **Start Campaign**.

## Review the account's access, not an invented person

In manager02's **Certifications > Active** session, open the assigned work.

For the uncorrelated review, use **Uncorrelated Identities** to open the representation and inspect its source account/access. The **Access Items** view can also show the uncorrelated accounts holding a selected permission.

Match the actual D account and rights, not only the displayed shadow name.

Record **Approve** for the limited, authorized Read need. Include the exact account/source, temporary purpose, named custodian and follow-up obligation in the available comment or private case record.

Record **Revoke** for Export, explaining that bulk-export work ended while the authorized Read work remains.

Check both choices and their reasons. Use **Finish** on every actual assigned certification and verify **sign-off**, the reviewer's final submission. Saved choices alone do not finish this work.

Record the actual review, representation, account and final actor/time. Do not assume the number of certification objects from the two permission holdings.

Approval of Read does not correlate the account. A successful review also does not close the ownership investigation.

## Fulfill only the rejected holding

Return to the administrator's session and inspect the actual generated removal work, also called **remediation**. A **manual task** asks an operator to carry out the required change. The recipient can use **Task Manager**; the administrator can inspect **Admin > Dashboard > Tasks**.

Match D, `certlab-uc-account01`, `groups` and `certlab-report-export`, along with the actual task recipient and complete requested scope. If no matching work appears, check final submission and the actual removal path before editing data or claiming fulfillment.

Do not interpret Revoke on this permission as Delete Account, Disable Account or Remove Account. Those are different actions and are outside this task.

The file edit simulates an external application change. Make a new copy of D's complete private account file. Remove only the target's Export row, preserving its Read and the control's Read.

Compare values with `lab-data/baselineD/uncorrelated_report_accounts_after_export_removal.csv`. That file is an intended result, not a captured task outcome.

Upload through the supported task file step, or have the authorized administrator use D's **Account Management > Account Aggregation**. Follow successful collection and inspect the actual records.

The result must have:

- Both D accounts still present.
- Target Read present and Export absent.
- Control Read present, still linked to employee01.
- Target still uncorrelated with its original matching key.
- Both entitlement definitions retained.
- Original A/B holdings and people/manager records unchanged.

If correlation unexpectedly changed, investigate the actual event before declaring this result or restoring data. Do not undo a verified ownership correction merely to recreate a training count. Approval or revocation itself is not proof of personal ownership.

Close only wholly fulfilled actual tasks through **Mark Complete**, or the permitted administrator's **Actions > Mark as Complete**, and inspect their completed state.

These are real ISC observations when performed, but the external application change is simulated by the file edit. No live application authorization has been proved.

## Leave an explicit ownership follow-up

Keep the account-level review result and ownership gap together without confusing them.

Your follow-up should identify the actual source/account, known temporary purpose and custodian, the missing verified individual owner, evidence needed, responsible investigator and follow-up date.

For example, confirming the business purpose helps decide permissions. Establishing the personal owner requires trustworthy account/person evidence and the approved correlation process. A source-owner title or a guessed name is not that evidence.

From **Admin > Certifications > Campaigns**, use the actual campaign's **Actions > Download Reports** for fresh available status/sign-off/remediation reports. Keep them with the actual task, file versions, collection and account observations. Record unavailable evidence as a gap rather than forcing administrative completion to obtain a report.

The access decision may be complete while ownership work remains open. Report those two states honestly.

## Think through the proposed quick fix

Someone says:

“Read was approved. Replace the unmatched key with manager02's employee key. The account will leave the uncorrelated list, so the ownership issue is solved.”

Would that establish the right owner?

<details markdown="block">
<summary>Read the reasoning</summary>

No. Approval establishes that the reviewed Read need was justified by the recorded facts. It does not prove that manager02 personally owns the account.

Changing the matching key without reliable ownership evidence would misattribute the account. A smaller uncorrelated list is not proof of accurate identity data.

Keep the verified custodian and unresolved owner separate. Investigate the actual owner, then use an authorized correlation correction if the evidence supports it. Do not carry out the proposed key change in this exercise.

</details>

## Restore the training data without erasing the issue

Preserve signed decisions, actual task/data evidence and the ownership follow-up first. Resolve all outstanding removal before restoring the test Export value.

If a legitimate ownership investigation has since changed the account's key or association, keep that correction and agree a new training starting state. Do not restore older matching data just for this exercise. The normal reset below applies while the original associations remain valid.

Restore D's complete private original file and run aggregation through successful completion. Verify two accounts/three holdings: target Read+Export, control Read, the same unmatched target key and the same employee01 control association.

Keep D, its definitions and the existing people/profile configuration. No source reset, identity deletion, account deletion or guessed manual correlation is needed.

Record the training restoration separately from the business decision. Keep the ownership follow-up explicit; a reset is not proof it was solved.

After accounting for all work and generation, remove only this attempt's unneeded unscheduled template from **Search > Certification Campaigns > Saved/Scheduled**. Match its saved reference and actual run name, preserving the separate signed campaign and its reports.

Before ending, explain what the certification established, which right changed, why Read remained and what evidence is still needed before the account can be linked to a person.
