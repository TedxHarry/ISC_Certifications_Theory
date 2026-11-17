# Target people and access through Search

The request is narrow: review Export Reports for employee01 and employee02 on `certlab-reports-csv`.

That is different from reviewing everything those people have. Each also has reporting permissions on another source. If we find the correct people but include all their access, we have changed the request.

Let's make the two selections separately, then check that the generated review contains exactly what was requested.

A **certification campaign** organizes access-review work. Here, we will tell it which people and permissions to include, who should review them and when that review is due.

## Put the requirement into a checkable form

An **identity** is ISC's record for a person. An **account** is that person's record on a managed system. One identity can have accounts on different systems.

A **source** holds the configuration and collected accounts for a managed system. An **entitlement** is a particular access value that ISC can govern.

For this run, the subjects are `certlab-employee01` and `certlab-employee02`. A subject is the person whose access is being examined.

The selected source is `certlab-reports-csv`. The selected entitlement is its Export Reports value, `certlab-report-export`. Export Reports means downloading reports in bulk.

The expected review contains only:

| Subject | Source | Account | Permission | Reviewer |
|---|---|---|---|---|
| `certlab-employee01` | `certlab-reports-csv` | `certlab-account01` | Export Reports | `certlab-manager01` |
| `certlab-employee02` | `certlab-reports-csv` | `certlab-account02` | Export Reports | `certlab-manager01` |

A **reviewer** is the person deciding whether that access is appropriate. Both employees have manager01 as their recorded manager.

Keep this table in the run notes before opening the campaign builder. It lets us check more than a total of two.

Read Reports is outside this review. Employee03 and both managers are outside the subject set. All access on `certlab-owner-reports-csv` is outside the review, including its identically named Export Reports permission.

## Establish the starting records

Use an authorized training administrator who can prepare Search campaigns and collect the test source's data. Manager01 needs a working reviewer session.

The **source owner** is the identity recorded as responsible for a source. Open `certlab-reports-csv` under **Admin > Connections > Sources**. Check **Source Setup > Base Configuration** and verify that **Source Owner** points to manager02. Manager02 needs a working session to open any removal task assigned to them.

Use the prepared five test identities and these two application sources:

- A: `certlab-reports-csv`.
- B: `certlab-owner-reports-csv`.

A **holding** means one account having one permission. Check each person's accounts against this starting set:

| Person and account label | Permissions on A | Permissions on B |
|---|---|---|
| employee01 / account01 | Read Reports and Export Reports | Read Reports and Export Reports |
| employee02 / account02 | Read Reports and Export Reports | Read Reports and Export Reports |
| employee03 / account03 | Read Reports | Read Reports |
| manager02 / account04 | No account | Read Reports |

The full names use the `certlab-` prefix. A has three accounts and five holdings. B has four accounts and six holdings.

Account01 on A and account01 on B are separate source accounts, even though their names match. The sources use CSV files to represent simulated applications. There is no live reporting product behind either file.

Verify the original baselineA and baselineB data in ISC, not the result left by an earlier removal. Before restoring any file, preserve earlier evidence and resolve outstanding work that could change these same accounts.

Keep private working copies that match each source's complete downloaded template. The original values are supplied in `lab-data/baselineA/report_accounts.csv` and `lab-data/baselineB/owner_review_accounts.csv`. The expected-result files are comparisons for later; they are not the starting inputs.

The account associations and manager links must already be correct. Keep the rights as individual entitlements. An access profile packages rights and a role can require access for its assigned users; neither should replace these individual review units here.

There is no new source or people import in this lab.

## Notice what selecting people does not decide

Follow employee01 first. Their A account has Read and Export. Their separate B account also has Read and Export. That is four holdings for this person across the two sources.

Employee02 has the same four holdings. Together, these two people have eight. That count excludes employee03 and the owner's account.

We want only each selected person's A Export holding. Finding the two people identifies whose access we can consider; it does not choose those two permissions from the eight.

A **search query** is an instruction for finding records. Here it will identify the people. The separate access-selection step will identify their source-specific permission.

Keep those questions separate:

The people selection contains employee01 and employee02. The access selection contains only Export Reports on `certlab-reports-csv`.

The campaign is the combination of those choices, with an assigned reviewer and a deadline.

## Find and add the two identities

Open **Search > Certification Campaigns > New Campaign > Identities**. Choose **Create Campaign** under **Using a Search Query**, then **Specific Identities that I Select**.

Run this query against the prepared identity names:

```text
name.exact:"certlab-employee01" OR name.exact:"certlab-employee02"
```

`name` is the identity's name field. `.exact` asks for the exact string. `OR` means either of the two named identities can match.

This query finds people. It does not select Export Reports or a source.

Inspect the returned identities and their actual IDs. For this fixture, the names must match the prepared people; a familiar display name alone is not enough.

If a person is missing, compare the query with the actual identity name and current record. Resolve missing or different data before proceeding. Do not broaden the query to everyone merely to make a result appear.

Check only the two intended identities, select **+ Add To Campaign**, inspect **Added to campaign**, then choose **Certify Selected Identities**.

A search result is a candidate, meaning a record you can choose. Finding employee02 does not itself add them to the campaign; the checkbox and **+ Add To Campaign** make that selection.

Check the added list for exactly employee01 and employee02. A changed query is not proof that the already added list now contains only its new results.

## Refine their access to the requested entitlement

Choose **Refine Access Items**.

Select the Export Reports entitlement belonging to `certlab-reports-csv`, add it with **+ Add to Campaign**, inspect **Added to campaign**, then continue.

Take time over the source. Both sources use the display name Export Reports and the permission value `certlab-report-export`. ISC still stores them as separate entitlement records because they belong to different sources.

An **entitlement object ID** identifies the particular record in ISC. The text `certlab-report-export` is the source's permission value; it is not that object ID.

Check the source and entitlement record against the actual IDs in your baseline notes. Select A's record only. If the selection view lacks enough detail, establish the record's source before adding it.

One entitlement definition is being selected, but two people hold it. The expected review therefore has two account-permission holdings.

**Certify All Access** would answer a broader question. It can include other access belonging to the selected people. In this fixture, the eight A/B holdings alone already exceed the two requested holdings.

Refining access is not a removal action. We are choosing what the reviewers will examine; no permission has been revoked yet.

## Set the reviewer and prepare a preview

Name the campaign `certlab-targeted-export-run01` and describe the two-person, one-source export review. Choose **Manager** as reviewer because the two identities' manager links point to manager01. Set a future due date and keep notifications within the approved test users.

An **undecided item** has no review choice yet. Keep the setting that maintains access to those items. Our intended result still requires both items to be reviewed and finalized. Choose a comment requirement that records why access is rejected.

Do not add a campaign filter for this first explicit-selection run. We need to inspect the choices we just made without another restriction hiding them.

A **preview** is generated review work for inspection. A **template** keeps the campaign configuration for reuse. Neither means a reviewer has completed anything.

Choose **Generate a preview now and save as a template**. Leave the saved template unscheduled and record it as a separate object.

Use **Review Campaign** to check the summary, then generate and open **View**. Keep the preview unstarted until its contents match the requirement. Saving a template does not, by itself, create a recurring schedule.

Record the actual campaign route and any engine label. If the documented selection or preview-first flow is unavailable, establish the matching supported route before activation.

## Compare the full generated set

Check every row against the two-row requirement table.

Both subjects must be correct. The source must be `certlab-reports-csv`. The accounts must be account01 and account02. The permission must be Export Reports, with manager01 responsible for each holding.

There should be no Read Reports, no holding from the other source and no additional subjects.

Inspect the generated grouping without assuming that two holdings mean two certification objects. A **certification** is an assigned review within the campaign; it can contain more than one item.

If the preview has the right people but too much access, revisit the selected access. If it has the right permission name from the wrong source, inspect the selected entitlement object.

Do not start and hope the reviewer will ignore extra work. Correct the saved configuration through its supported path, generate a fresh preview and inspect it again. A changed Search result or current source record does not establish that an existing preview has changed.

When it matches, select **Start Campaign** on the checked preview. There is no need to generate another instance from the saved template.

## Make the two business decisions

Employee01's current work still includes bulk export. Employee02's bulk-export work has ended, although report viewing is still needed.

Before choosing, explain which export holding should remain and which should be removed.

In manager01's session, open **Certifications**, select the active assigned work and inspect the subject, source, account and permission.

**Approve** records that the access is appropriate. **Revoke** records that it should be removed. Choose Approve for employee01's Export Reports and Revoke for employee02's Export Reports, based on the supplied work evidence.

For the rejected holding, add a reason such as “Bulk-export work has ended; report viewing is still required.”

**Sign-off** is the reviewer's final submission. Check both choices, then finalize every actual assigned certification using **Finish** on the supported completion screen. Saving or exiting is not final confirmation.

Record the actual decision maker and final confirmation. Do not approve or revoke Read Reports here; it was not included in this campaign.

## Apply the one simulated change to the correct source

**Remediation** is the work that carries out a review's required change.

Inspect the actual manual task for employee02's rejected Export on `certlab-reports-csv`. The expected source-owner recipient is manager02; verify the actual recipient and task contents rather than infer them from the reviewer.

Manager01 made the business decision. The actual task recipient carries out the change. Those are separate responsibilities.

In **Task Manager** or **My Tasks**, open the full details and match source A, account02 and `certlab-report-export`. Read every change listed in the task. If no matching task exists, first check final sign-off and the recipient session; keep the missing work unresolved if it remains absent.

Make a new version of the complete private A account file. Remove only account02's Export row. Keep its Read row, both account01 rows and account03's Read.

The supplied A file `report_accounts_after_employee02_export_removal.csv` shows the expected four-holding result. Preserve the actual full source-template structure in your working copy.

Do not edit B's account file or either entitlement catalogue. Identical permission names do not make their holdings interchangeable.

Upload the revised A file using the supported task upload control, or have the authorized administrator use A's **Account Management > Account Aggregation**. **Aggregation** reads the file into ISC and updates its collected account data.

Follow the aggregation through successful completion and inspect the actual result. If collection fails, inspect its error and leave the removal unresolved. This is a simulated external change represented by a CSV edit, not an automatic change to a live application.

Check that all the work listed in the task has been carried out and verified. If it includes another unfinished change, keep the task open. When the whole task is ready, its recipient can select **Mark Complete** and inspect its completed state.

## Verify the narrow change against the wider account data

Check more than the rejected holding.

On A, employee02's Export must be absent while its Read remains. Employee01 must retain Read/Export and employee03 must retain Read. That is four holdings across three accounts.

On B, all six original holdings must remain, including employee02's Export and manager02's Read. This campaign did not ask to remove them.

Employee02 still holding an identically named Export on B is not, by itself, evidence that the A removal failed. Match the source and account being checked.

Check the actual sign-off and campaign states, task completion and current account associations. Generate fresh available sign-off/remediation reports through the campaign's **Actions > Download Reports** and reconcile their source-specific fields and comments.

A completed campaign is evidence about review work. The changed account data and reconciled task establish the CSV removal outcome. Record a mismatch if those pieces disagree.

Keep the requirement table, query, added identities, selected access object, checked preview, final decisions, actual task and before/after files in the private run notes. Record the saved template too, with no schedule configured.

## Are two correct people and two matching permission names enough?

Imagine the preview contains employee01 and employee02, with Export Reports for each. Manager01 is the reviewer.

The total is two holdings. However, both rows show `certlab-owner-reports-csv`.

Does the preview meet the request? Would approving employee01 and revoking employee02 make it correct?

<details markdown="block">
<summary>Compare your reasoning</summary>

The people, reviewer and count match, but the source does not. It is a different entitlement object and a different pair of holdings.

Leave the preview unstarted. Inspect the access selection, replace the B entitlement with the A entitlement through the supported builder and inspect a fresh preview.

Making sensible decisions on the wrong source would still perform the wrong task. The full requirement is people plus source plus account plus permission, with a suitable reviewer.

</details>

## Leave the setup ready for another run

Preserve the campaign, task, reports, template reference and before/after files. Resolve outstanding work that could apply the same removal again before restoring the starting permissions.

Upload A's complete original private account file to A through **Account Management > Account Aggregation**. Follow successful collection, then inspect its three accounts and five holdings in ISC. Both employee01 and employee02 must again have Read and Export; employee03 must still have Read.

Check that B still has four accounts and six holdings. Keep its original data unchanged. Do not re-import unchanged people data just to reset an access review.

Keep the saved template unscheduled. A future run needs a new campaign instance and a fresh scope check; do not assume a saved configuration proves current review contents.

Restoring A is a training reset. It does not erase the signed review or reverse its business decision.
