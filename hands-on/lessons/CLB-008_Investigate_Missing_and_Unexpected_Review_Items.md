# Investigate missing and unexpected review items

A preview contains two items. The request also calls for two items. That sounds encouraging, but one person may be missing while an unrelated permission takes their place.

Let's investigate that situation using unchanged account data. We'll find where the selected people and permissions stop matching the request, then correct those choices separately.

## Keep the request beside the preview

A **campaign** groups access reviews. A **preview** is the generated work an administrator checks before starting the campaign for reviewers.

A **subject** is the person whose access is being examined. The **reviewer** decides whether that access should remain.

The requirement is to review Export Reports for these two people on `certlab-reports-csv`:

| Person whose access is reviewed | Account | Permission | Reviewer |
|---|---|---|---|
| `certlab-employee01` | `certlab-account01` | Export Reports on `certlab-reports-csv` | `certlab-manager01` |
| `certlab-employee02` | `certlab-account02` | Export Reports on `certlab-reports-csv` | `certlab-manager01` |

These two rows define our **review scope**, the access we were asked to examine. We need both, with no extra rights. The reviewer column identifies who should make each decision.

Read Reports is outside the request. So are employee03, both managers as subjects and all permissions on `certlab-owner-reports-csv`.

Keep the full requirement in your run notes. “Two items” leaves out the person, source, account, permission and responsible reviewer.

## Check that the starting data is correct

Use an authorized training administrator who can inspect accounts and identities and generate campaign previews. All three campaign instances in this exercise stay unstarted. Their saved configurations stay unscheduled. Do not enter decisions, sign off or request access.

An **identity** is ISC's record for a person. An **account** is that person's record on a managed system. A **source** contains the configuration and collected account data for that system. An **entitlement** is an individual access value ISC can govern.

A holding means one account having one permission. Read Reports represents viewing reports; Export Reports represents bulk downloads. The CSV files model simulated applications.

Use the existing isolated sources:

- A: `certlab-reports-csv`. Account01/employee01 has Read and Export; account02/employee02 has Read and Export; account03/employee03 has Read. That is three accounts and five holdings.
- B: `certlab-owner-reports-csv`. The same three employees have those five holdings, and manager02/account04 has Read. That is four accounts and six holdings.

The shortened account and identity labels above use the `certlab-` prefix.

Employee01 and employee02 must both have manager01 as their recorded manager. Account01 and account02 must already be linked to their intended identities.

Check that the A rights are individual entitlements. An access profile packages permissions from one source, and a role can require access for its assigned people. Neither should change these A review items in this starting state.

Use the original values in `lab-data/baselineA/report_accounts.csv` and `lab-data/baselineB/owner_review_accounts.csv`, already prepared in private copies matching the actual source templates.

If an earlier run changed the data, preserve its evidence and resolve outstanding work before restoring it. Retire any earlier pending training schedule that could interfere with this run. Inspect the actual records after any necessary restoration.

Once this baseline is verified, leave the CSVs, account links and manager records unchanged. We are going to change campaign selections, not manufacture incorrect identity data.

## Prepare a preview with two selection mistakes

Use unused names for all three configurations. If the example names already exist, choose a fresh run suffix. Record each new object's ID as it is created. Keep earlier attempts' records and evidence separate.

Open **Search > Certification Campaigns > New Campaign > Identities**. Under **Using a Search Query**, choose **Create Campaign**, then **Specific Identities that I Select**.

A **search query** finds candidate records. Run:

```text
name.exact:"certlab-employee01" OR name.exact:"certlab-employee02"
```

`name.exact` matches the exact identity name. `OR` means either named identity can match.

Verify that both intended identities are returned. If either is absent, investigate that different starting problem before continuing.

For this deliberately incorrect configuration, select and add **only employee01** with **+ Add To Campaign**. Inspect **Added to campaign**. It must contain employee01 alone, even though the query found both people.

Choose **Certify Selected Identities**, then **Refine Access Items**.

Add **both Read Reports and Export Reports from A**. Check the actual source and entitlement objects. Their values are `certlab-report-read` and `certlab-report-export`. Do not add the matching names from B.

Inspect the added access list. Record the actual added identity and both source-specific access objects in your private run notes, then continue. This preserves the evidence you will compare with the generated work.

Name this configuration `certlab-008-initial-run01`. Select **Manager** as reviewer, a future due date and the option to maintain undecided access. An undecided item has no review decision.

Leave the campaign filter empty. A filter would add another selection condition and make this first investigation harder to isolate. Keep optional recommendations off and notifications within the approved training settings.

A **template** saves the campaign selections and settings used to produce a preview. The saved template and generated campaign are separate records. Record both IDs for each preparation.

Choose **Generate a preview now and save as a template**. Use **Review Campaign**, check the summary and generate the preview. Keep the saved template unscheduled.

Before opening the result, predict which holdings those added lists can produce. The query found two people, but which person did we actually add? Which permissions did we add?

## Describe the mismatch precisely

Open the generated preview through **View** and record its actual ID and generation time.

Record when you checked the source accounts too. If someone changed the data after the preview was generated, today's account view cannot by itself tell you what that earlier preview used.

The expected faulty result is employee01's A Read and A Export: two holdings for the same person, assigned to manager01.

Compare the actual result with the requirement. If it differs from this expected faulty case, retain the difference and check the saved inputs before proceeding. Do not force the example by editing account data.

For the intended faulty case, write down both symptoms:

- Missing: employee02's A account02 Export.
- Unexpected: employee01's A account01 Read.

Employee01's A Export belongs in both the requirement and this preview.

The total is two, but only one of the two required holdings is present. There is one missing holding and one extra holding. Approving the sensible-looking items would not correct the campaign's scope.

A **certification** is an assigned review within a campaign and can contain several items. Keep item counts separate from the number of certification objects you actually observe.

## Follow the missing item through the inputs

Start with employee02's missing Export. We need to find where a correct record stops being included.

Open the A source account and verify account02 still has Export. Then inspect employee02 under **Admin > Identity Management > Identities**, including the linked account.

**Account correlation** means linking a source account to an identity. Here, account02 should belong to employee02. If that link is already correct, moving the account to another identity would create a new problem.

Check employee02's current access and Search record. The same candidate query should find that person.

Open the faulty configuration from Search's **Saved/Scheduled** tab and inspect the fields shown in its saved summary. Compare them with the added-list evidence you retained before generation. Use that evidence to verify the selection if the summary does not show the full list.

The retained list shows only employee01. Finding employee02 in today's Search results does not prove they were added to this instance.

That is the first selection that disagrees with the two-person requirement. The account exists, Export exists, the account belongs to the right person and the query finds the person. But employee02 was never added.

Write the cause in a complete sentence:

“Employee02's A Export is missing because employee02 was not in the added identity list.”

This explanation identifies a specific input we can correct. “Search is broken” does not.

## Trace the extra Read item separately

Now examine employee01's unexpected Read.

The account really has Read. Employee01 is an intended subject. The source and account are correct. So the extra item does not prove that collected account data is wrong.

Inspect the added access list: it contains both A Read and A Export. The requirement contains only Export.

Write the second cause:

“Employee01's A Read is included because Read was added to the access selection.”

The two symptoms have different causes. Adding employee02 will not remove Read. Removing Read will not add employee02.

Do not delete the Read entitlement, remove it from the CSV or revoke it in a review to make the preview look right. Read is legitimate account access; it simply falls outside this request.

## Correct the people selection and inspect the intermediate result

Keep the first preview and its configuration evidence. Create a separate configuration so the comparison has a distinct generated result.

Repeat **Search > Certification Campaigns > New Campaign > Identities > Using a Search Query > Specific Identities that I Select**.

Use the same query, but this time add **both employee01 and employee02**. Confirm both actual identity IDs in **Added to campaign**, then choose **Certify Selected Identities**.

Keep the access choice unchanged for this intermediate check: **Refine Access Items**, with both Read and Export from A added.

Name it `certlab-008-people-fixed-run01`. Keep Manager, due date, undecided-access handling, no filter and the other training settings the same.

Generate an immediate preview and save its template, without starting or scheduling it.

Expect four holdings: Read and Export for employee01, and Read and Export for employee02, all on A with manager01 responsible. Inspect each row.

The missing employee02 Export is now present. However, Read remains outside the requirement for both people.

The count increased from two to four because we corrected the people list while preserving the overly broad access list. That increase is explainable; it is not evidence that the repair failed.

If employee02 remains absent, compare the actual added identity, selected source-specific entitlements, current account association and new preview ID. Check that you opened the new instance.

## Narrow the access and verify the complete result

Create the final separate configuration, named `certlab-008-corrected-run01`.

Use the same query and add both identities. Under **Refine Access Items**, add **only A Export Reports**. Inspect the final added list before continuing.

Keep the other settings unchanged. Generate the immediate preview and saved unscheduled template.

Compare its entire contents with the requirement table. Expect employee01/account01/A Export and employee02/account02/A Export, each with manager01 responsible.

There must be no Read, B entitlement or additional subject.

The three preparations should now tell a connected story:

| Preparation | Added people | Added A permissions | Expected review holdings |
|---|---|---|---|
| Initial | employee01 | Read and Export | Two: employee01 Read/Export |
| People corrected | employee01 and employee02 | Read and Export | Four: both rights for both people |
| Access also corrected | employee01 and employee02 | Export only | Two: Export for each person |

The first and final counts match, but their contents do not.

Record the actual new IDs, times, rows and reviewer assignments. Check that A still has five account-permission holdings and B still has six. Changing review scope must not be mistaken for changing account access.

Leave even the correct preview unstarted. The investigation is complete when the cause, correction and verified result agree.

## If your evidence points somewhere else

Start with the first check whose result does not match the requirement or verified starting data. Use that specific difference to decide what to inspect next.

If the source account itself lacks the permission, inspect the source file and last completed aggregation. **Aggregation** reads account data into ISC. A campaign selection cannot supply a right that the collected account does not have.

If the account exists but is unlinked or linked to the wrong identity, investigate that account association and its correlation configuration. Do not widen the campaign to everyone to conceal the missing person.

If the correct identity is missing from the query results, compare the exact stored name with the query and the current Search data. Completed collection and updated Search results are separate checks; do not promise a fixed wait will resolve a particular mismatch.

If the identity is returned but absent from **Added to campaign**, correct the added selection. That is the fault we demonstrated.

If the people are correct but the items differ, inspect the added access objects, their sources and any campaign filter. A permission packaged into an access profile or represented through a role can require a different review item; do not assume the individual entitlement must appear too.

If the items are correct but the reviewer is wrong, inspect the configured reviewer choice and the person's recorded manager. That is an assignment problem. Changing an entitlement will not correct it.

Keep the investigation tied to an observed record. Do not change correlation, manager data, filters and permissions together just because one preview is wrong.

## What if you correct access first?

Return to the original faulty case in your notes: only employee01 was added, with A Read and Export selected.

Suppose you remove Read from the access selection first, while still leaving employee02 out. Predict the next preview's contents. Would the smaller result satisfy the request?

<details markdown="block">
<summary>Compare your reasoning</summary>

The expected result is one holding: employee01's A Export.

The extra Read is gone, but employee02 is still missing because the added people list has not changed. That is a partial correction.

Adding employee02 as well, while keeping only A Export, produces the two required holdings.

A smaller total is not automatically better, just as the four-item intermediate result was not automatically worse. Compare which mismatch each change fixes.

</details>

## Preserve the explanation and retire only this test work

Keep the requirement, actual rows, account/identity checks, candidate results, added lists and settings. For each of the three preparations, retain the preview's campaign ID and generation time alongside the separate saved-configuration ID.

Your investigation notes should explain each symptom, its cause, the one changed input and the checked result. Someone else should be able to follow that explanation without guessing what you changed.

Confirm every 008 instance was never started and has no decisions or removal work. Confirm its saved configurations have no schedule. If a campaign was activated or another dependency exists, reconcile that actual work before routine cleanup.

After preserving evidence, remove only these unused 008 saved configurations from Search's **Saved/Scheduled** tab. Use the applicable legacy tab only for a legacy record; check each exact object before confirming deletion.

Delete only the unused, unstarted 008 campaign instances through **Admin > Certifications > Campaigns**, selecting the exact records, then **Delete > Delete Campaign**. Their preview pages also provide deletion.

Check that none of this run's unused configurations or previews remains as future work. Keep earlier labs' saved work and history.

Verify A's three accounts/five holdings, B's four accounts/six holdings and the original identity and manager links. No CSV reset is needed when those inputs stayed unchanged.

The result to retain is the explanation backed by those checks: the data was correct, one person was not added, and an extra permission was selected. Correcting the campaign inputs produced the requested review without altering anyone's access.
