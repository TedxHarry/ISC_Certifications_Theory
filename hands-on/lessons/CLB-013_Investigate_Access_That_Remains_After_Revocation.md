# Investigate access that remains after revocation

A reviewer revokes an access profile. Export disappears from the account, but Read is still there.

Before calling that a failed removal, let's ask what was reviewed and why Read remains. Another assignment may still require it. We need to follow that connection to the exact account.

## Start with what the person has

An **identity** is ISC's record for a person. An **account** is that person's record in a managed system. A **source** holds ISC's configuration and collected account data for that system.

An **entitlement** represents an individual right, such as Read Reports. An **access profile** bundles entitlements from one source. A **role** groups access required for a business function.

For the CSV exercise, use source A, `certlab-reports-csv`, with these original holdings:

| Account | Identity | Existing permissions |
|---|---|---|
| certlab-account01 | certlab-employee01 | Read Reports and Export Reports |
| certlab-account02 | certlab-employee02 | Read Reports and Export Reports |
| certlab-account03 | certlab-employee03 | Read Reports |

That is three accounts and five holdings. One holding means one account having one permission.

Read uses `certlab-report-read`; Export uses `certlab-report-export`. They are individual entitlement values on A. Source B, `certlab-owner-reports-csv`, keeps its original four accounts and six holdings throughout.

Use an authorized training administrator who can manage the two temporary access objects, process selected identities and inspect campaigns/tasks. Reviewer `certlab-manager01` and source owner `certlab-manager02` need working sessions. Employee02's recorded manager must be manager01; A's recorded owner must be manager02.

Verify the original five test identities and their unique identification numbers. The people-source setup maps each person's employee number into the identity attribute `identificationNumber`. Employee02's value must be exactly `certlab-employee02`.

If A or B needs restoration, first resolve previous outstanding removal work. Use each source's complete private starting file, prepared against its actual downloaded template. A's values come from `lab-data/baselineA/report_accounts.csv`; B's come from `lab-data/baselineB/owner_review_accounts.csv`.

Begin with direct permissions and no earlier temporary profile, role, lifecycle grant or review redirect changing this case. A lifecycle grant is access assigned because a person is in a configured business state, such as Active. It is another possible requirement, so it would make our small test less clear.

CSV files represent simulated application accounts here. The ISC model and review actions are real when performed; a file edit remains a simulated external change.

## Give Read a separate reason to remain

We will make two connections to employee02's existing Read permission:

| Access object | What it contains | How employee02 obtains it |
|---|---|---|
| certlab-013-a-read-export | A Read and A Export | ISC detects the profile from rights already held. |
| certlab-013-a-read-required | Only A Read | A role membership condition matches this identity. |

An **assignment** connects an identity to access such as a role. Its **origin** tells us how that connection was established.

A detected profile means ISC recognized all its required permissions on the person. It does not prove that someone previously submitted and approved an access request.

A **membership criterion** is a condition used to decide who should receive a role. Our condition will match only employee02. The role will now require Read for that person.

Both paths refer to the same A account and Read entitlement. They do not create two copies of Read on that account.

The supplied work facts are simple: employee02 no longer needs bulk export, but still needs reading. The separate Read role represents that continuing requirement.

## Create the profile over rights already present

Open **Admin > Access Model > Access Profiles > Create New**.

Set the name to `certlab-013-a-read-export`, manager02 as Primary Owner, A as Entitlement Source and a description explaining the temporary Read-plus-Export test. Save.

Under **Manage Entitlements**, add exactly A Read and A Export. Inspect their source and actual IDs, then save. B's matching names are different entitlement objects.

Keep **Allow Access Requests** off. Do not put this profile inside a role, lifecycle state or application. After its contents are correct, use **Actions > Enable** on this exact Access Profiles entry.

The profile must remain independent of the role we create next. We are testing removal of that independent package while a role still requires one of its rights.

## Create the small role and check its condition

Open **Admin > Access Model > Roles > Create New**. Use a **Standard** role named `certlab-013-a-read-required`, with manager02 as Primary Owner and a clear test description. Save.

In **Manage Access > Add Access**, choose **Entitlements**. Select only A Read, use **Review**, inspect the selected source/value, then **Add Access**. The role must not contain Export or the two-right profile.

Under **Define Assignment**, choose **Standard Criteria**. Add one group with one condition:

- Type: **Identity Attribute**.
- Attribute: the mapped Identification Number, `identificationNumber`.
- Operation: **Equals**.
- Value: `certlab-employee02`.

Save the criterion. Keep access requests off.

Read the condition as a sentence: give this role to the identity whose identification number equals this one test value. There is no department-wide rule and no second value.

Before enabling it, confirm that this key identifies only the intended test person. If it is missing or duplicated, correct the preparation first. Do not broaden the condition just to produce a match.

Use **Enable Role** on the exact role. Keep tenant-wide role settings unchanged.

**Identity processing** reevaluates an identity's information and applicable access configuration. Open **Admin > Identity Management > Identities**, select only employee01, employee02 and employee03, then use **Actions > Process Identities**.

Inspect the processing result and current access records:

- Employee01 and employee02 should have the detected two-right profile.
- Only employee02 should have the Read role.
- Employee03 should have neither temporary object.
- All three A accounts should still hold their original five permissions in total.

Check employee02's role assignment details and associated A account. Check that the role contains only Read and that the profile contains Read plus Export.

A saved role definition alone does not prove that this identity holds it. Equally, processing alone does not prove an account change succeeded. Inspect any resulting work and the account data.

If the assignments or holdings differ, check the criterion, profile contents, enabled states, processing and account association. Resolve any unexpected task before continuing. Do not add Export or make an unrelated account change to force the expected picture.

We created a current requirement for already-held Read. We have not proved that this new role originally granted the permission in the past.

## Review the package and the role separately

A **campaign** organizes reviews. A **certification** is an assigned review inside it. The **review item** is the particular access object needing a decision.

Open **Search > Certification Campaigns > New Campaign > Identities**. Under **Using a Search Query**, select **Create Campaign**, then **Specific Identities that I Select**.

Find the exact person:

```text
name.exact:"certlab-employee02"
```

Add only employee02 with **+ Add To Campaign**, inspect **Added to campaign**, then select **Certify Selected Identities**.

Choose **Refine Access Items**. Add only the temporary A profile and the temporary A role, using their respective access-type lists. Inspect the added objects before continuing.

Name the configuration `certlab-013-a-retained-run01`. Choose Manager as reviewer, a future deadline, the option to maintain undecided access and the available Revoke comment requirement. Follow an all-comments requirement if that is the actual setting.

Use approved training notifications, no extra filter or optional recommendations, an immediate preview and an unscheduled saved template.

Expect two review units for employee02: the independent profile and the automatically assigned role. These represent two access objects, not two separate copies of Read.

Check the actual items, account/source details and manager01 assignment. If a different unit appears, investigate its assignment and package relationships before starting. Do not substitute a similarly named entitlement or assume a matching count proves the right scope.

When the preview is correct, select **Start Campaign**.

In manager01's **Certifications > Active** work, inspect both access objects.

For the independent profile, record **Revoke**. Explain that bulk-export work ended and Read remains required through the named role.

For the automatically assigned role, use **Acknowledge**. This records that its access was reviewed. It does not remove the role or override the condition assigning it.

Roles assigned through criteria use this action because the membership condition still controls the assignment. Do not interpret the absence of a Revoke choice as a broken button.

Check the saved choices and reasons. Use **Finish** for each actual assigned certification and verify **sign-off**, the reviewer's final submission. A saved choice without that submission has not completed the required review.

## Predict the account result before making the file change

The revoked profile contains both Read and Export. Should account02 lose both?

The supported role-and-profile case gives a more specific result. The independent profile is revoked, but the role still requires A Read. Export has no remaining requirement in our prepared model.

We therefore expect employee02 to lose Export and retain Read. The profile should no longer be associated with employee02 after the account/model updates, while the Read role remains.

That remaining Read is justified by a current assignment. It is not enough to say that another role somewhere contains a similarly named right. We must show that this person holds the role and that its access applies to this account.

## Follow the actual removal work

In the actual recipient's **Task Manager**, open the generated removal work. The administrator can also inspect **Admin > Dashboard > Tasks > To Do**.

Match the signed profile decision, identity, source, account and requested changes. Record the actual task ID, recipient and scope.

The intended account change is employee02 Export removal. Read is still required by the verified role. If an actual task asks you to remove Read as well, keep that discrepancy visible and investigate the assignment and removal path. Do not delete required Read or mark a conflicting task complete merely to match the expected result.

Use a new copy of A's complete private account file. Remove only account02's Export holding; retain its Read row and every other account/permission. Compare the values with:

`lab-data/baselineA/report_accounts_after_employee02_export_removal.csv`.

Preserve the actual source template's extra columns and required values. The supplied file is an expected comparison, not a tenant result.

Use the task's supported file-upload step, or have the authorized administrator open A under **Admin > Connections > Sources > Account Management > Account Aggregation**.

**Aggregation** reads the changed account data into ISC. Follow it through completion and inspect the resulting records. An accepted upload is not enough. If collection fails, inspect its history/error and keep fulfillment unresolved.

Process only the three test employees again as needed to apply and inspect their current model associations.

The expected result is:

| Person | A account now | Temporary profile now | Read role now |
|---|---|---|---|
| Employee01 | Read and Export | Present | Absent |
| Employee02 | Read only | Absent | Present |
| Employee03 | Read only | Absent | Absent |

All three A accounts remain. A has four holdings, and B still has six. Both A entitlement definitions remain because employee01 still uses Export.

A historical review may still display the profile that was reviewed. That is a record of the decision; inspect the identity's current access to establish whether the profile is still held.

Close actual manual tasks only after all their requested work agrees with the established result. The recipient uses **Mark Complete** and checks the **Completed** tab; the administrator's equivalent is **Actions > Mark as Complete** in Tasks. Uploading a file and completing a task are separate actions.

## Explain why the remaining Read is correct

Open employee02 under **Admin > Identity Management > Identities** and inspect **Access**. Follow the role's assignment to the associated A account, then open the role's definition to confirm it requires Read.

Compare that with the revoked profile's contents and the account's current rights. The connections should explain both observations:

- Export was included in the revoked profile and has no remaining requirement in this test. It is absent.
- Read was also in that profile, but the still-assigned role requires the same A right. It remains.

Do not remove Read just because it was listed inside the revoked profile. That would work against the requirement you have just verified.

Now generate fresh campaign status/decision, sign-off and remediation reports through **Admin > Certifications > Campaigns > Actions > Download Reports**, using the reports available for the recorded campaign.

Keep the actual campaign/review/task IDs, decisions, assignment/account details, file versions, collection results and observation times together. Generate reports again after changes; an old download will not update itself.

The reports and tasks establish parts of the process. In this branch, the file and collected record establish the simulated account result. They do not prove a real application's current authorization.

## Try a different explanation for the same symptom

Suppose someone says:

“Employee02 still has Read because another source also has a Read Reports entitlement. We don't need to inspect the role.”

Is that enough to explain why **A account02** retained Read?

<details markdown="block">
<summary>Read the reasoning</summary>

No. B's Read label belongs to another source. It does not establish a requirement for A's account permission.

The evidence needed here is employee02's actual A Read role assignment, its associated account and the exact A entitlement included in the role.

A name match is a useful search clue. It is not proof of overlap on one account.

</details>

If Export remains too, the same retained-Read explanation does not resolve it. Trace the exact remaining Export holding:

First confirm that the profile Revoke was finalized and is due. Then inspect the matching manual task or automatic operation and its current result. Compare the latest account observation with the most recent successful collection.

If another assignment really requires Export, inspect that actual path and its business justification. If no such requirement exists and removal is unfinished or failed, treat Export as unresolved work. Do not label every remaining permission as harmless overlap.

An account can also stay in place after a permission is removed. Our task removes one right; it does not require deleting or disabling the account.

## Keep the rule within the case you proved

Our test has a role requiring Read and a separate profile containing Read plus Export.

Two independent profiles sharing a right are a different configuration. Do not apply this role-retention result to them without establishing the supported behavior for that exact removal process. Current guidance does not give us a consistent general answer for every such case.

Likewise, if the business no longer needs Read, acknowledging the role will not change the assigning condition. The appropriate response is an authorized policy or source-data correction, depending on which is wrong.

Do not falsify employee02's identification number or business status just to stop a role matching. Those values may affect other decisions. In this exercise, reading is still justified; we are not correcting the role's business policy.

## Check a live target when it is ready

The CSV branch can finish on its own. The live variant needs the prepared connected source `certlab-ad-lab`, called C here, with a verified automatic membership-write path.

Record and verify the actual source, account and group identifiers. Check that each account is linked to the intended existing identity and that the connector's technical account can make the required group-member change. ISC administrator access alone does not establish that directory permission. The starting scoped memberships are:

- `certlab-ad-e01`, linked to employee01: `certlab-ad-read` and `certlab-ad-exp-ok`.
- `certlab-ad-e02`, linked to employee02: `certlab-ad-read` and `certlab-ad-exp-fail`.

Use ordinary, non-nested test groups. These four direct memberships do not describe every AD permission or prove access to an actual reporting application.

Resolve earlier tasks/operations and remove any earlier test Deny before starting. C must not still be in an unverified manual-fulfillment configuration. Use the supported prepared automatic setup; do not guess a configuration reversal or change a shared source.

Finish and reset the CSV branch first. Then use the same steps above with these substitutions:

| CSV exercise object | Live variant |
|---|---|
| A source | C, certlab-ad-lab |
| Two-right profile | certlab-013-c-read-export, containing only C Read and ExpFail |
| Read role | certlab-013-c-read-required, containing only direct C Read |
| Role condition | identificationNumber Equals certlab-employee02 |
| Campaign | certlab-013-c-retained-run01 |
| Reviewed account | certlab-ad-e02, linked to employee02 |

Keep both temporary C objects independent, access requests off and the role condition restricted to employee02. Process only the selected test identities, inspect the assignments and verify C's original four memberships before generating the two-item preview.

The profile should be detected only for employee02: employee01 has ExpOK, not ExpFail. Do not change employee01's memberships to make the profile appear.

Have manager01 finalize profile Revoke and automatic-role Acknowledge after checking the correct preview and current need.

Track the actual connector operation for e02 ExpFail. An error or pending write is unresolved removal, not proof of expected retention. Do not remove the membership manually to manufacture an automatic pass.

Have the authorized directory operator inspect actual membership on the recorded directory controller. E02 must no longer be in ExpFail and must remain in Read. E01 must still be in Read and ExpOK.

The scoped result is three memberships. Account for directory replication if observations use different controllers. Collect C's account data afterward and reconcile the current profile/role/account records and fresh reports.

No CSV edit passes this outcome. Record the actual operation and independent AD observations before calling it a successful connected result.

## Remove the temporary model before restoring the baseline

Preserve signed history, assignment details, reports and account observations. Reconcile every outstanding removal before reset so old work cannot run after you restore a right.

Retire only this lab's unused unscheduled configurations after checking their actual state. Keep the signed campaign history; deletion is not rollback.

For each branch you actually ran:

1. Locate the exact temporary Read role. Turn **Enable Role** off in its edit screen so it cannot keep assigning this test requirement.
2. Process the selected test employees and inspect removal of the temporary role association and any resulting work. Saving a model change is not proof of its account effect; inspect the actual assignments, work and retained rights before proceeding.
3. Check that the temporary profile has no role, lifecycle, application, request or unfinished-work dependency. Delete only that profile through its **Actions > Delete** flow, reading the confirmation. Delete only the unused, disabled test role through the Roles action.
4. Process the selected test employees again. Confirm both temporary objects are absent from current access, then inspect and resolve any resulting tasks/operations before restoring permissions.

Disabling the role removes its association with the identity and stops future automatic assignment. It does not, by itself, remove the account permissions the role provided. Read can therefore remain on the account after the temporary role disappears. Check the role association and account permissions separately before restoring the baseline.

Keep tenant-wide role settings and unrelated roles unchanged during cleanup.

For the CSV branch, restore A's complete private original account file and collect it. Verify three accounts/five direct holdings, the original identity links and unchanged B four accounts/six holdings. The original people data remains unchanged.

For the live branch, after model/work cleanup, have the authorized directory operator restore only e02's ExpFail membership. Verify the original four scoped memberships, collect C and reconcile ISC. Keep e01's memberships and both Read memberships unchanged. If cleanup unexpectedly affected Read, establish and resolve that work before restoring and checking the complete original set.

Restoring the training baseline does not change the final historical review decision.

Before ending, explain which access object was revoked, which exact account right remained, the assignment that still required it, and the evidence showing whether the other right was removed. That is the difference between recognizing a familiar symptom and understanding this account's result.
