# Review a source and separate the owner's access

A manager can review access because they know an employee's work. The person responsible for an application can review access because they know what its permissions allow.

In ISC, a **source** holds the configuration and collected account information for a managed system. Its **source owner** is the person recorded as responsible for that source.

A **source-owner campaign** asks those owners to review access on the sources you select. Each assigned review inside the campaign is called a **certification**.

There is one extra situation we need to handle: the source owner may have an account on the same source. Being responsible for the application does not make someone the right person to approve their own access.

We'll prepare that situation with a separate CSV source and inspect both parts of the review.

## Identify the people and responsibilities

An **identity** is ISC's record for a person. The source-owner setting points to one of these identity records.

Use the five prepared test identities: `certlab-employee01`, `certlab-employee02`, `certlab-employee03`, `certlab-manager01` and `certlab-manager02`.

The names manager01 and manager02 are test labels. For this task, manager02 is also the source owner. That responsibility is separate from being an employee's manager.

Check these existing manager relationships:

- Employee01 and employee02 report to manager01.
- Employee03 reports to manager02.
- Manager02 reports to manager01.

Both managers need working reviewer sign-ins. Use their separate browser sessions and an authorized training administrator who can create the source and campaign. Keep actual credentials and registration messages private.

The people must already exist with the correct relationships. This setup adds application accounts, not new people.

## Prepare an isolated source for this review

Use a fresh source named `certlab-owner-reports-csv`. It is a separate training copy of the reporting data. This lets us add an account for the owner without changing the earlier manager-review source.

If that source already exists from your own earlier run, verify its exact setup before reusing it. Preserve its history and resolve any outstanding work that could change these same accounts before restoring data or starting this run. An earlier removal task can still ask for a change even after you upload a starting file again.

Do not overwrite an unrelated source with a similar name.

A **CSV file** stores rows of values under column headings. Our file represents a simulated application; there is no live reporting product behind it.

The baselineB package contains:

- `owner_review_accounts.csv`: the initial accounts and their permission holdings.
- `owner_review_entitlements.csv`: the permission names and descriptions.
- `owner_review_accounts_after_employee02_export_removal.csv`: the expected result to compare with after the review.

An **entitlement** is a specific access value ISC can govern. Here, Read Reports means viewing reports and Export Reports means downloading reports in bulk. The account file records who holds each permission. The entitlement file supplies its name and meaning; it does not assign it to an account.

Keep the expected result file separate from the initial input. We need the reviewers' justified choices and the actual resulting work before applying a change.

As the administrator, open **Admin > Connections > Sources > Create New**. Select **Generic** and its manual flat-file upload setup. Enter the new source name and a description, and select the actual manager02 identity as source owner.

Save the source and record its ID privately. Keep it non-authoritative, meaning it supplies accounts for existing identities. The existing people identity profile already maps trusted people data to identities. We do not want this application source to create another set of people, so do not create an identity profile for it.

Confirm the actual file-upload mode and any required connection dependencies. If the setup requests a remote file server or a different integration, resolve the selected source type before importing.

## Make the file describe four accounts correctly

A source's **account schema** defines the fields ISC stores for each account. Open **Account Management > Account Schema** and check these four fields:

- `id`: select this as **Account ID**, the stable key for an account on this source.
- `name`: select this as **Account Name**.
- `employeeNumber`: the person key we will use to find the existing identity.
- `groups`: the permission values held by the account.

The first three fields are single text values. For `groups`, **Multi-Valued** lets one account hold both Read and Export. **Entitlement** tells ISC to treat those values as access it can govern.

Also check that `groups` uses the source's existing entitlement type. This connects the account's permission values to the entitlement records we will load. Use the type actually configured on this source rather than copy a different connector's type name.

Set the account keys before collecting data. Download the actual account template through **Account Aggregation > Download Account Schema**. Copy the supplied values into its complete heading order, retaining extra columns and filling any other required fields.

Use a private working copy rather than replacing the source template with the short sample. The same rule applies to the entitlement template.

**Account correlation** matches a source account to the identity that holds it. Before collecting accounts, open **Account Management > Account Correlation**. Configure account `employeeNumber` to match identity **Identification Number** (`identificationNumber`). Identification Number must already contain each person's unique key from the people setup.

Inspect any preset criteria on this fresh source so a different criterion cannot silently attach an account to another person.

**Aggregation** reads the file into ISC. Download the template under **Entitlement Management > Entitlement Aggregation** and prepare the supplied Read/Export definitions in that structure. Their IDs must match the account `groups` values. Upload the catalogue, then collect the initial account file through **Account Aggregation**. Keep account deletion disabled for this initial load.

Follow collection through completion and inspect the actual account associations.

## Check the owner's account as carefully as the employees' accounts

The new source should contain this set:

| Account | Existing identity | Initial permissions |
|---|---|---|
| `certlab-account01` | `certlab-employee01` | Read Reports and Export Reports |
| `certlab-account02` | `certlab-employee02` | Read Reports and Export Reports |
| `certlab-account03` | `certlab-employee03` | Read Reports |
| `certlab-account04` | `certlab-manager02` | Read Reports |

There are four accounts and six holdings. A holding means one account having one permission. There are still only two permission definitions.

The repeated rows for account01 and account02 represent their two permissions. Keep rows for one account together and repeat their other field values consistently.

Follow account04 through the same matching rule. Its `employeeNumber` is `certlab-manager02`. The existing manager02 identity must have that value in `identificationNumber`. The match associates account04 with manager02.

Open manager02's identity and verify that this exact source account is attached to it. Then compare that identity with the source's recorded owner. Both must point to manager02. That is how we establish that account04 is the source owner's own account; a similar display name is not enough.

All four accounts in this fixture belong to known people. An **uncorrelated account** has not been matched to an identity. A **service account** is used by a program rather than a person. If unexpected accounts appear, establish their purpose and ownership before reviewing them; do not attach them to the source owner just to complete the expected set.

Manager01 has no account on this selected source. The people identity count remains five; creating this non-authoritative source should not create a sixth person.

The literal account and permission names can also appear on another training source. Match the source ID as well as the account or entitlement value when inspecting them.

Keep these rights as direct entitlements. An access profile packages rights and a role can require access for assigned users. Neither should change the individual review units in this fixture.

Under **Source Setup > Base Configuration**, verify **Source Owner** is the actual manager02 identity. Save and reopen the configuration if you changed it. Source ownership is a stored reference, not a label in the account file.

## Predict who should review each part

A **subject** is the person whose access is being reviewed. A **reviewer** is the person making the decision.

Take employee02 first. Their recorded manager is manager01. A manager campaign would use that relationship. We are creating a source-owner campaign instead, so the source-owner setting points this review to manager02.

Now look at account04. Its holder is manager02, who is also the source owner. Sending that item to manager02 would ask the same person to judge their own access.

ISC's **self-certification prevention** separates that own-access item into another certification. In this fixture, the review goes to manager02's recorded manager, manager01. We will check that assignment in the preview.

Account04 and its Read permission stay in scope. What changes is who reviews them.

Before generating work, write down the expected reviewer for each account. Keep manager02's source responsibility and personal permission as separate questions.

<details markdown="block">
<summary>Compare your expected responsibilities</summary>

| Access being reviewed | Expected reviewer | Reason |
|---|---|---|
| Employee01's two holdings | manager02 | Recorded owner of the selected source. |
| Employee02's two holdings | manager02 | Recorded owner, even though employee02 reports to manager01. |
| Employee03's one holding | manager02 | Recorded owner of the selected source. |
| Manager02's one holding | manager01 | Independent review through manager02's known manager relationship. |

The five employee holdings belong in the source owner's work. The owner's own holding remains in scope and needs a different reviewer.

This predicts responsibility, not a fixed number of certification objects. Inspect how ISC actually groups and assigns the work.

</details>

## Create the source-owner campaign

Open **Admin > Certifications > Campaigns > Create New** and choose **Source Owner Campaign**.

Use a distinct name, such as `certlab-source-owner-review-run01`, and describe the four-account training review. Select a future deadline.

Select only `certlab-owner-reports-csv` in the source selection. Leave **All Sources** unselected. For this initial case, do not add a campaign filter: we want all six direct holdings on this one inspected source.

Keep the setting that maintains access to undecided items, and choose a comment requirement that captures why access is rejected. An **undecided item** has no choice yet. Our normal result requires every assigned item to be reviewed and finalized.

Check notification settings against the approved test recipients and record any visible campaign engine or Legacy label. If the matching source-owner creation route is unavailable, resolve that before generating work; do not substitute another engine's controls.

A **preview** is generated review work that the administrator inspects before activation. Select **Preview Campaign**, wait for generation to finish and open its details.

## Inspect both the ordinary work and the separated own-access work

Compare the actual preview with all six holdings and the predicted responsibilities.

Manager02 should receive the five employee holdings. Manager01 should receive the owner's Read Reports holding on account04. Check that account04 is included exactly once, that it is linked to manager02 as the subject and that manager02 cannot review their own holding.

For account04, manager02 is the subject and manager01 is the reviewer. Manager01 does not need an account on this source to make that review decision.

Inspect actual certification groupings and the full subject-account-permission set. Use available composition details or reports to reconcile the set. Count the right holdings, not just six arbitrary rows.

If account04 is missing, that is not proof that its access was independently reviewed. Check its collected group, its identity association and the generated scope.

If the own-access holding is assigned back to manager02, leave the campaign unstarted. Check the source owner reference, account04's actual identity, manager02's actual manager and the selected campaign route. Record the mismatch if the expected separation is still absent.

Do not remove the owner's account from scope just to obtain an easy preview. Do not manually reassign work to conceal an unresolved own-access problem.

When the entire set and its recipients match, select **Start Campaign**. Start from a fresh checked preview; changed input data requires fresh generation and inspection.

## Judge access from current need

The supplied work evidence is:

Employee01 still views and exports reports. Employee02 still views reports, but the bulk-export work has ended. Employee03 only needs viewing.

Manager02 has a defined reporting-oversight task that requires opening reports. That task needs Read Reports. Being named source owner, by itself, would not prove this permission is needed.

Decide each holding from those facts before recording choices.

In manager02's reviewer session, open **Certifications** and inspect the active assigned work. For each employee holding, choose **Approve** if the current need supports it or **Revoke** if the permission should be removed.

The employee decisions should total four approvals and one Revoke: retain employee01 Read/Export, employee02 Read and employee03 Read; reject only employee02 Export. Add a useful reason for the rejected holding, such as “Bulk-export work has ended; report viewing remains required.”

Inspect all choices and finalize every actual assigned certification. **Sign-off** is the final submission of the review. On the documented completion screen, use **Finish**; saving or exiting is not sign-off. If the interface differs, establish its matching supported final-confirmation flow.

In manager01's session, open the separately assigned review for manager02's account04. Verify the subject, source, account, permission and oversight need. Approve Read Reports and finalize that review.

The whole result is five approvals and one Revoke. Keep actual reviewer identities and final states in the run notes. Do not finish missing reviewer work through an administrator bulk action.

## Carry out the one simulated removal

The review decision and its delivery are separate. **Remediation** is the work that carries out the required change.

Inspect the actual manual task for employee02's rejected Export Reports holding. The expected recipient is the source owner, manager02, but verify the actual task and recipient.

Manager02's review of the employees, manager01's independent review of manager02 and manager02's later removal task are different responsibilities. Check which work you are opening.

As the task recipient, open **Task Manager** or **My Tasks**. Open the task's full details and match the new owner-review source, account02 and the export value before acting.

Read every removal listed in the task. Our campaign calls for one rejected holding, but a task is complete only when all the work it lists is done. If the actual task includes other unfinished changes, keep it open and account for those changes before closing it.

Create a new version of the complete private B account file. Remove only the account02 row whose `groups` value is `certlab-report-export`. Keep account02's Read row and every other account.

Compare with the supplied expected B result. Do not use the similarly named baselineA result, which lacks account04.

Keep both catalogue definitions. Export is still justified on account01; removing employee02's holding does not delete the permission itself.

This file edit simulates an application-side change. It does not demonstrate ISC changing a live application's account.

Upload the revised complete file through the supported task upload control. If that control is unavailable, have the authorized training administrator upload it through this source's **Account Aggregation**. Source ownership does not grant every administrative permission.

Follow the collection to successful completion and verify the current accounts. If collection fails, inspect its error and leave the result unresolved. After verifying the complete requested work, the actual task recipient can select **Mark Complete** and inspect the resulting state.

If no matching task exists, or its subject/source/right differs, keep that part unresolved. A completed review is not a reason to invent a task or close unrelated work.

## Check what stayed as well as what changed

The resulting set should be:

| Account on the owner-review source | Read Reports | Export Reports |
|---|---|---|
| `certlab-account01` | Present | Present |
| `certlab-account02` | Present | Absent |
| `certlab-account03` | Present | Absent |
| `certlab-account04` | Present | Absent |

Verify four accounts and five holdings, with both permission definitions retained. Account04 must still belong to manager02, and its Read permission must have an independent finalized review by manager01.

As administrator, inspect the campaign's actual completion state and preserve the decisions, sign-off records, task details and before/after file versions. The fully signed normal path can move the campaign to Completed; removal evidence must still be checked separately.

Generate the available sign-off and remediation reports through the campaign's **Actions > Download Reports**. Match source, account, subject, actual decision maker and result. Regenerate after collection if the earlier download predates the change.

Do not expect a historical rejected-item row to vanish merely because the current holding is absent. Read the actual report status and comments. An unresolved task or conflicting report remains something to investigate.

You can record the run as complete when all six holdings have the right finalized reviews, the sole rejected holding is absent from the revised CSV and collected account, approved holdings remain and the actual removal work is reconciled. This is the CSV outcome; real external account removal is a different result.

## Should you exclude the owner's account to avoid self-review?

Imagine the preview has all six holdings, but all are assigned to manager02, including account04's Read Reports.

Someone suggests filtering out account04. The remaining five items would all be employee access and could be started immediately.

Would that finish the original source-owner review requirement? What needs attention before activation?

<details markdown="block">
<summary>Compare your reasoning</summary>

Filtering out account04 removes required coverage. It does not prove an independent review of the owner's access.

Keep the campaign unstarted. Check whether account04 is actually attached to manager02's identity, whether the recorded source owner is that same identity and whether manager02 is linked to manager01 as manager. Check the supported campaign route and inspect a fresh preview after any necessary correction.

The original requirement includes all six holdings, with a suitable independent reviewer for the owner's own holding. If that result cannot be established, record the unresolved assignment rather than publish a five-item result as complete.

</details>

## Restore this lab's starting data

Preserve completed review, task and report evidence first. Resolve outstanding work that could act on the same accounts before restoring the starting permissions.

Upload the full private original `owner_review_accounts.csv` data only to `certlab-owner-reports-csv` through **Account Management > Account Aggregation**. Wait for successful collection, then inspect four accounts and six holdings again, including employee02's Export and manager02's Read. Recheck source ownership, account04's identity and the manager link used for independent review.

Keep account04 and the dedicated source. They are part of this fixture's starting state, so reset does not require account or source deletion.

The people data and the original `certlab-reports-csv` source are unchanged. A later run must use a new campaign instance with its own checked preview. Restoring the file does not reopen or erase a signed review.
