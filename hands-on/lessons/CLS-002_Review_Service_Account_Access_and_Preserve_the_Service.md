# CLS-002: Review service-account access and preserve the service

A program can use an account to do its work. For example, a nightly job may sign in with an account, read reports and prepare a summary. People call this a **service account** because a service or program uses it.

Someone still needs to answer: “Does this account need all the access it has?”

In this lab, the report-reading job still needs Read. It also has Export, which was used for a migration that has now ended. You will prepare its machine-account record in ISC, ask its human owner to review the access, and follow the Export removal through a manual CSV task. A manual task is an instruction for an authorized person to carry out the change and confirm its completion.

The job and its work requirements are supplied training facts. The CSV represents its account data; there is no running report program behind this exercise. You will check the actual ISC work and the simulated file result.

## Start with the three things we need to connect

The **account** is the record the program uses in the source system. An **application identity** is a type of **machine identity** in ISC: it represents a program or service and groups its related accounts. Here, one application identity will hold our one service account. A **native record** means the actual ISC record produced by processing, rather than a label written in a CSV.

The **account owner** is a human who is responsible for that account. Assigning an owner gives someone responsibility for its use. It does not make the service account that person's personal login.

Here is the relationship we want to establish:

> Service account → native machine identity → access available for review
>
> Human account owner → responsibility for reviewing that account's access

We will use one service account so you can follow every permission back to the exact account. ISC can also organize several machine accounts under an application identity. Combining several accounts is a separate setup decision; we do not need it for this review.

A name such as svc-report01 helps a person recognize an account. ISC still needs a classification rule and the resulting machine-account record. **Classification** means identifying which accounts on a source should be treated as machine accounts.

## Prepare the people, source and files

Use your approved training tenant and an administrator allowed to configure the fresh source and its machine accounts. Verify that the tenant offers both native Machine Accounts configuration and the Machine Accounts certification type. If either is unavailable, record the lab as not run and resolve that requirement before creating a campaign.

Two existing people have different responsibilities:

- certlab-manager02 will own the service account and review its access. Verify this person has a working, approved reviewer session.
- certlab-manager01 will own the CSV source. Verify this person can receive or arrange the manual removal work.

A **source** is ISC's configured connection and collection of account data for a system. The source owner is responsible for that source. The service-account owner is responsible for the individual account. Keeping these two people different will help us notice an owner-mapping mistake.

Use the five prepared people in certlab-people-profile, fed by certlab-people-csv. Check that employee01 and both managers are present with the expected names and manager relationships.

Two identity attributes matter here: **uid** holds the person's username, and **identificationNumber** holds the employee-matching key. Their uid values come from people.name; their identificationNumber values come from employeeNumber.

Private approved email values and reviewer registration must already be complete. A row imported from CSV does not itself create a working login.

For the initial setup, open **Admin > Connections > Sources > Create New**, select **Generic** and use its supported manual-upload configuration. Create **certlab-machine-reports-csv**, called **E** here. Set its source owner to `certlab-manager01` in **Base Configuration**. On a repeat, reuse this isolated source only after checking its baseline. Keep E **non-authoritative**: it supplies application accounts, and must not be attached to a new human identity profile.

An **entitlement** is a permission ISC can track. Read is `certlab-report-read`; Export is `certlab-report-export`. A definition describes the available permission, while the account's `groups` values say which permissions it holds.

Use the three files in lab-data/baselineE:

- machine_report_accounts.csv supplies the starting accounts and their permissions.
- machine_report_entitlements.csv describes the two permissions.
- machine_report_accounts_after_export_removal.csv shows the expected values after removal. Keep it for comparison; do not upload it as the starting file.

Make private working copies outside the reusable course folder. Download E's account template through **Account Management > Account Aggregation > Download Account Schema** and its catalogue template through **Entitlement Management > Entitlement Aggregation**. Match the supplied values to those templates, retaining additional required columns. Inspect the supported Generic upload mode and its dependencies before importing.

The starting account values are:

| Account | Used by | Initial permissions | Purpose |
|---|---|---|---|
| certlab-svc-report01 | Report-reading job | Read and Export | Read reports each night; Export migration has ended. |
| certlab-human-control01 | Existing employee01 | Read | A human account we will check stays unchanged. |

There are two accounts and three permission holdings. A **holding** here means one account has one permission. The service account has two holdings; the human account has one.

## Tell ISC what the file fields mean

Open E's **Account Management > Account Schema**. A **schema** tells ISC how to interpret the values it collects. **String** means text; **Scalar** means one value; **Multi-valued** allows several values. Configure:

| Field | Meaning and setting |
|---|---|
| id | Stable account identifier. Scalar String; use as Account ID. |
| name | Account name. Scalar String; use as Account Name. |
| employeeNumber | Person-matching key for the human account. Scalar String. |
| accountKind | Supplied label: service or human. Scalar String. |
| ownerKey | Key used to find the human service-account owner. Scalar String. |
| environment | Training environment label. Scalar String. |
| purpose | Explanation of the account's work. Scalar String. |
| groups | Permissions held by the account. Multi-valued entitlement with E's supported entitlement association. |

Verify the **Multi-Valued** and **Entitlement** flags for groups. The service account appears on adjacent CSV rows, once for Read and once for Export. These are two permissions on one account, not two service accounts. Its other values stay identical on both rows.

Before collecting accounts, configure only E's account correlation pairing: account employeeNumber matches identity identificationNumber. **Correlation** is the association between an account and an identity.

The human control carries certlab-employee01, so it should associate with the existing employee01 identity. The service account carries certlab-machine01. Verify that no authoritative human identity in the tenant has that key. We will classify this account as a machine account rather than add a made-up person to the people feed.

Also check the built-in name fallback before first collection: no existing identity should be named `certlab-svc-report01`, including different capitalization. A missing employeeNumber match alone does not guarantee an unmatched account. Check for any existing manual human association as well.

**Aggregation** collects supplied data into ISC. Load E's permission definitions through **Entitlement Management > Entitlement Aggregation**, then its complete starting account file through **Account Management > Account Aggregation**. Wait for successful completion, then inspect the accounts and permissions.

Before machine classification, check the human control is linked to employee01, the service account is not linked to a human, and E contains exactly the three intended holdings. If a key, association or permission differs, correct E's preparation first. Keep the other course sources and their data unchanged.

## Establish the native machine record

Open E under **Admin > Connections > Sources**. Under **Machine Accounts > Classification**, enable classification and choose **Customize classification**. Set the condition to accountKind equals service, then save.

The service account has `accountKind=service`, so it meets this condition. The human control has `accountKind=human`, so it does not. We want the classification rule to select only the service account.

A **mapping** tells ISC where to obtain a value or relationship. Open **Machine Accounts > Mappings**. In **Machine Account Owner**, choose **Account to Identity**, using ownerKey to match the human identity's uid. A searchable attribute lets ISC look up identities by that value. First verify uid is an offered searchable target and certlab-manager02 identifies exactly one person. If that requirement is missing, resolve it before proceeding.

Follow the service account's two keys separately. Its `employeeNumber=certlab-machine01` does not identify a human in the prepared people data. Its `ownerKey=certlab-manager02` matches manager02's uid and identifies who is responsible for it. The owner mapping assigns responsibility; it does not turn the service account into manager02's personal account.

Leave **Machine Identity** unmapped. We are not supplying a separate application record to match this service account to. Under this supported setup, classification creates an **uncorrelated application identity** containing this one machine account.

Here, “uncorrelated” concerns the application grouping. ISC creates a one-account application identity instead of matching the account to an existing application identity. The account can still have a known human owner. Inspect both relationships in ISC.

Leave **Account Subtype** unmapped. Map Environment from environment and Description from purpose, then save. A subtype adds a further category of machine account; it is unnecessary for this permission review.

Return to Classification and select **Process Classification** for the initial setup. Wait for its completed status. Then open **Admin > Identity Management > Accounts > Machine Accounts** and inspect certlab-svc-report01.

Check the result before creating review work:

- It is classified as a machine account on E.
- Its account owner is the actual manager02 identity.
- The machine account's environment and description reflect training and the report-reading purpose.
- Its associated application identity contains this one service account and exposes its Read and Export access.
- The human control remains associated with employee01 and is excluded from the machine-account set.

Inspect the associated application identity through **Admin > Identity Management > Identities > Machine Identities > Applications**. Save the actual source, account and application-identity IDs privately so you can compare them later. Also record any application-identity owner shown; account ownership and application-identity ownership are separate properties.

If the owner is missing, inspect the collected ownerKey, the selected mapping and the unique matching uid. A repeated or missing match cannot establish the intended owner. Fix the input or mapping and verify the result; do not manually assign an owner merely to hide a failed mapping.

## Check the work requirement before deciding

Use these supplied exercise confirmations from manager02:

The nightly report-reading job is still needed. It must retain Read. Export was used for a completed migration, and the owner has confirmed that the job no longer depends on Export.

That gives us a reason for each choice. We will retain the permission needed for continuing work and remove the one whose purpose has ended.

**Approve** records that a permission should be kept. **Revoke** records that it should be removed. Neither choice means that the whole service account should be disabled or deleted.

In a real review, obtain equivalent confirmation from someone who understands the service and its dependencies. Missing activity data does not establish that an unattended account is unused. Ask what job uses it, what work remains, and whether removing this particular permission would interrupt that work.

Our intended change concerns Export only. The account and Read remain in place. Disabling the whole account would also prevent the continuing read job from using it.

## Build and inspect the machine-account campaign

A **certification campaign** organizes access reviews. A **certification** is an assigned review inside it. We will include the service account's two permissions and have its human owner decide whether each should remain.

As the campaign administrator, open **Search > Certification Campaigns > New Campaign > Machine Accounts**.

Select E only. Inspect the account list beneath the source selection. It should contain certlab-svc-report01 and exclude the human control. Select **Certify These Accounts**.

Name the campaign **certlab-cls002-machine-run01**. If that name already exists, use an unused run suffix and record it; preserve earlier history. Its description should state that the service's Read continues and Export migration access is being reviewed for removal.

Choose **Account Owner** if the actual campaign type offers it. The intended recipient is manager02. If the tenant instead offers a suitable documented Individual option, explicitly select manager02 and record that choice. That run tests an explicitly assigned reviewer, rather than automatic account-owner routing.

ISC documents source-owner fallback when an Account Owner review has no configured account owner. In this lab that would lead to manager01. Work reaching manager01 therefore needs investigation; receiving a review somewhere does not prove our owner mapping succeeded.

Keep undecided access maintained, require comments on Revoke decisions, turn this campaign's notification emails off, and choose a future due date with enough time to complete the work. Maintaining undecided access prevents a blank decision from becoming an unintended removal at campaign end. If the comments setting requires comments on every decision, record both reasons.

A **preview** lets you check generated review contents before releasing them to the reviewer. A **template** saves the campaign settings for reuse. Choose to generate a preview now and save a template, leaving the template unscheduled. Record the saved-template and generated-campaign references separately. Review the summary and generate the preview without starting the campaign. Keep scheduling and additional campaign filters out of this run.

Open the generated preview and verify the actual recipient and scope. Trace both Read and Export to E, certlab-svc-report01 and its recorded machine identity. No human control or other source should be included.

Two permission holdings are expected. Inspect the actual certification grouping rather than assuming that two holdings mean two separate certifications. If the scope or recipient is wrong, correct the preparation before starting.

Once the preview is correct, use **Start Campaign**. Save the actual campaign ID and activation details in your private evidence.

## Review as the human account owner

Sign in through manager02's verified reviewer session. Open **Certifications > Active**, then the assigned work.

In **Machine Identities**, select the recorded identity and inspect **Entitlements**. The Access Items view offers another way to examine the same entitlement and the machine identity holding it.

Open the details and confirm the underlying account and E source. A machine identity can organize several accounts; always establish which account will be affected. Our prepared case contains one.

Approve Read with a reason such as:

> The nightly report-reading job continues and requires Read on this account.

Revoke Export with a reason such as:

> The Export migration has ended. The account owner confirmed no continuing Export dependency. Retain Read and the service account.

Use the actual account/source details in private notes where needed. Review the saved choices, then use **Finish** and complete any final authorization required for all assigned work in this campaign.

Save evidence of the final decisions and **sign-off**, the reviewer's final submission. A saved choice and a final submission are different stages. Completing the review establishes the decision; the removal still needs its own result check.

## Follow the manual work and verify the account

Return to the administrator's session and inspect the actual removal work in **Admin > Dashboard > Tasks**. Record its recipient, account, source, entitlement and full scope. The reviewer and task performer may be different people. The actual recipient can open the work in **Task Manager** and must follow its complete instructions.

If the matching work is missing, check sign-off, campaign state and the configured removal path before changing files. If it points to a different account or source, investigate that mismatch first.

For E's manual CSV path, edit the complete private starting account file after finalization and matching-work inspection. Remove only the row for:

> certlab-svc-report01 on E — certlab-report-export

Preserve the service account's Read row and every scalar value on it. Preserve the human control's Read row. The comparison file shows these expected values; your private full template may contain additional required columns.

This file edit **simulates the external application's permission change**. It does not demonstrate that a real program can still run or that a real application's Export permission has changed.

Upload the full changed file through the supported task/source path. Wait for successful aggregation and inspect the collected result:

| Check | Expected result |
|---|---|
| Service account | Present, classified as machine, owner still manager02. |
| Its access | Read present; Export absent. |
| Machine identity | Correct one-account association retained; compare actual IDs. |
| Human control | Still human, linked to employee01, Read retained. |
| E totals | Two accounts and two holdings. |
| Entitlement definitions | Both Read and Export definitions remain. |

The entitlement definition describes an available permission. Removing one account's Export membership does not require deleting that definition.

Changed accounts collected through aggregation also undergo native machine classification and mapping processing. Preserve accountKind and ownerKey so the permission change does not accidentally change the account's classification or owner. Inspect those results rather than assuming the unchanged CSV values prove native success.

In **Task Manager**, use **Mark Complete** only when the full listed scope has been fulfilled and checked. An authorized administrator can use **Actions > Mark as Complete**. Inspect the completed state; do not close a larger task after handling only this one item.

Keep the signed decision, actual task, changed private file, collection result and account observations together. Record the outcome as a CSV simulation with actual ISC review and collection evidence. Actual service continuity would require observing the real job and target system in a connected exercise.

## Investigate a review arriving with the wrong person

Suppose the campaign uses Account Owner, but manager01 receives the review. You discover that the service account has no owner. Its collected ownerKey has a typing mistake.

What explains the assignment, and what should you check before a new campaign?

<details markdown="block">
<summary>Work through the reason</summary>

The owner mapping could not find the intended person. The Account Owner route therefore fell back to the source owner, manager01.

Check the exact collected ownerKey against manager02's unique searchable uid and inspect the mapping. Correct the source value or configuration, process the change through the supported path, and inspect the native account owner.

Only then prepare a fresh checked campaign if another review is required. Preserve the existing assignment and decision history. Correcting account metadata does not establish that already assigned review work has been reassigned.

The account still needs a responsible human. An assignment produced by fallback cannot prove that the intended account owner was configured.

</details>

This is a reasoning exercise. You do not need to upload a deliberate mistake.

## Restore the starting access for another run

Preserve the completed review and removal evidence first. Confirm there is no outstanding task, scheduled generation or pending operation that could act on E after restoration.

If a legitimate owner correction changed the approved data, keep that correction and agree the new training baseline before uploading a restoration file. Do not overwrite a verified owner merely to reproduce the original value.

Restore the complete private file for the approved training baseline and collect it through the supported upload path. For unchanged ownership, use the original E values. Check two accounts and three holdings: service Read+Export, human control Read.

Follow collection through successful completion. Also inspect the service account's machine classification, approved human owner (manager02 in the original setup) and native identity association. Check that the human control still belongs to employee01. Preserve the classification rule and mappings used for this verified training baseline.

Do not declassify the source or delete the account/application identity to restore one permission. If an actual identity ID changed, retain both observations and investigate before recording continuity.

Retire only this attempt's unused unscheduled template after matching its saved reference and actual name and checking its generation state. Retain the separate signed campaign, its reports and task evidence. Leave the people source and other course sources unchanged.

The restored Export is test preparation after the recorded removal. Keep its later restoration time separate from the earlier result so someone reading the evidence can follow what happened.
