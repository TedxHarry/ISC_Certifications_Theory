# Compare campaign filters and review units

A **certification** is an assigned access review. A **campaign** organizes those reviews.

An account can have Read Reports and Export Reports while its review shows only Read. Excluding Export from the review leaves it out of the reviewer's work; it does not remove Export from the account.

A **review unit** is the particular access object the reviewer is asked to decide on. It can be one permission or a package containing several permissions.

We'll first compare which individual permissions appear when a filter includes or excludes Export. Then we'll create a small access profile, a named package of permissions, and inspect the review units again. The account permissions will stay unchanged throughout.

## Use a known set and keep every campaign unstarted

Use an authorized training administrator who can manage campaign filters, generate previews, create the temporary access profile and process the selected test identities.

All campaigns in this lab stay unstarted. Starting a campaign makes its reviews available for action. Here, we only generate and inspect previews. Do not enter decisions, sign off, request access or edit the CSV permissions.

An **identity** is ISC's record for a person. An **account** is that person's record on a managed system. A **source** holds the configuration and collected account data for that system. An **entitlement** is a specific access value ISC can govern.

A **holding** means one account having one permission. Read Reports allows viewing reports; Export Reports represents downloading reports in bulk in our simulated application.

The application sources are:

- A: `certlab-reports-csv`, with the original three accounts and five holdings.
- B: `certlab-owner-reports-csv`, with the original four accounts and six holdings.

Check B's initial set:

| Account | Identity | Read Reports | Export Reports |
|---|---|---|---|
| `certlab-account01` | `certlab-employee01` | Present | Present |
| `certlab-account02` | `certlab-employee02` | Present | Present |
| `certlab-account03` | `certlab-employee03` | Present | Absent |
| `certlab-account04` | `certlab-manager02` | Present | Absent |

Employee01/02 and manager02 have manager01 as manager. Employee03 has manager02 as manager. The five people identities and their manager links must already be prepared and checked. Each B account must be linked to the identity shown above. No new source or person is needed.

Before restoring a baseline left by an earlier run, preserve its evidence and reconcile outstanding work. Use the original complete private source-template files, not their post-removal versions. The A starting data comes from `lab-data/baselineA/report_accounts.csv`; B comes from `lab-data/baselineB/owner_review_accounts.csv`, with its `owner_review_entitlements.csv` catalogue. These are the canonical data values. Keep the actual downloaded source columns in your private upload copies, collect any restored account file and verify the resulting ISC records before generating a preview.

At the beginning, B's six holdings must be individual entitlements, without an access profile, role or automatic requirement changing their review units. Inspect existing access models and the four identities before proceeding.

## Decide what the filter is supposed to change

A **campaign filter** selects review contents using conditions. An **inclusion** filter keeps matching items. An **exclusion** filter leaves matching items out.

We'll keep the initial possible review set fixed at B's six holdings. Only the filter mode will change.

With an Export inclusion filter, expect the two Export holdings belonging to employee01/02.

With the same Export criterion used for exclusion, expect four Read holdings, one for each B account. Employee01/02 remain in that second set because each still has Read to review.

Neither comparison changes any account permission.

## Create two filters with the same criterion

Open **Search > Certification Campaigns > View previewed/Active > Campaign Filters > Create Filter**.

Use unused names for this attempt and record the actual names and IDs. If a proposed name belongs to an earlier run, inspect that record rather than overwrite it. Choose a different run suffix for the new filters, campaigns and saved configurations.

Name the first filter `certlab-006-export-in-run01`. Enter a description and select **Continue**. In the builder, select **Inclusion**, then **+ Add Group**, and set this one condition:

- Criteria type: **Entitlement**
- Source: the actual B source, `certlab-owner-reports-csv`
- Operation: **Equals**
- Entitlement: **Export Reports** on B

The entitlement filter uses its display name. Confirm the source and actual entitlement reference; do not substitute the A permission or assume that typing its raw group value identifies the same object.

Select **Create Filter** to save it. Create a second named `certlab-006-export-out-run01`, with the identical criterion and **Exclusion** as its mode. Reopen both to compare their saved settings.

Use one criterion in each. Adding a Source condition beside Export would not mean “Source AND Export.” The filter criteria are joined with **OR**: a match to either condition is enough.

Every B holding matches Source B, including its four Read holdings. Adding that alternative can therefore make the inclusion filter keep all six B holdings instead of just the two Exports.

Keep the six-item starting set separate from the condition applied to it.

## Build the access-focused starting set

Open **Search > Certification Campaigns > New Campaign > Access Items**. Choose **Using a Search Query**, then **Specific Access Items that I Select**.

Use `*` to find candidate access items. It means all results; it is not permission to add them all to the campaign.

Inspect and add only B's Read Reports and Export Reports entitlements. Check **Added to campaign**, then select **Certify This Access**.

Choose **Refine Access Items** and explicitly add those same two B entitlement objects as the access to be reviewed. Continue only after checking that final added set.

The first selection finds the holders of those B permissions. The second selection limits which of their access we ask them to review.

For employee01, finding the person through B Read or Export does not by itself rule out their A access. **Refine Access Items** keeps the reviewed access on B. Employee03 and manager02 have B Read only, so their Read holdings still belong in our starting set.

**Certify All Access** would allow a broader review of the selected holders' access. It would not give us the controlled B-only comparison we need.

The starting set should therefore be all six B holdings, with no A access. This is the same set for both filter modes.

## Generate the two comparison previews

For the first configuration, use a name such as `certlab-006-in-run01`, the inclusion filter and **Manager** as reviewer.

Set a future due date, select the option to maintain undecided access and use the approved training notification settings. Leave optional recommendations off so this comparison stays focused on the selected access. An undecided item has no review choice; this lab will not produce reviewer decisions.

A **preview** is generated review work that an administrator inspects before activation. Choose **Generate a preview now and save as a template**, select **Review Campaign**, check the summary and generate it. Use **View** to inspect the result. A template is a saved configuration; keep it unscheduled and record its ID.

Inspect the preview without selecting Start Campaign.

Build a second configuration with the same B selections, reviewer and settings, named `certlab-006-out-run01`. Use the exclusion filter. Generate a separate preview so you can compare both results without assuming an old preview refreshes.

Check the actual subject, source, account, item type and permission for every included row. Record what was left out as well.

| Preview | Expected review holdings | Expected reviewer responsibility |
|---|---|---|
| Inclusion: B Export | Two Export holdings, employee01 and employee02 | manager01 |
| Exclusion: B Export | Four Read holdings, employee01/02/03 and manager02 | manager01 for employee01/02/manager02; manager02 for employee03 |

A total alone is insufficient. Confirm that the inclusion result contains no Read and that the exclusion result contains no Export or A access.

Four review holdings do not necessarily mean four certification objects. A **certification** is an assigned review and can contain several items.

Now inspect the current B accounts again. They must still have all six starting holdings across the four accounts. The two previews changed the review question, not the access.

If a result differs, check the saved access selections, filter mode, source, criterion and existing access-model associations before continuing.

## Change how the two rights are represented

Save the two original preview results before changing the model. They are the before-change comparison. We will generate fresh work to check the model after processing.

An **access profile** packages entitlements from one source into a named set. If ISC detects that a person already has all the entitlements in the profile, it can associate the profile with that identity.

For employee01/02, the review item can then be the profile rather than separate Read and Export items.

Create only this temporary profile:

`certlab-filter-reports-bundle`, containing B's Read Reports and Export Reports.

Create a new profile for this attempt. If that name is already in use, choose an unused name and use it consistently in the later filter and cleanup notes. Do not edit or delete an existing profile just to obtain this name.

Open **Admin > Access Model > Access Profiles > Create New**. Set the name, manager02 as **Primary Owner**, a clear test description and B as **Entitlement Source**. Save.

Primary Owner records responsibility for this profile. Our campaigns still use the Manager reviewer setting; selecting manager02 here does not replace that choice.

Under **Manage Entitlements**, add exactly the two B entitlements and save. Check the source on both; A's identical display names are not substitutes.

Leave **Allow Access Requests** off under **Access Requests**. Enable the profile after its entitlements are configured, using **Actions > Enable** on its Access Profiles entry. Do not attach it to a role, lifecycle state or application, or submit a request for it.

We are examining detection of rights that already exist. We are not assigning the package to make missing permissions appear.

## Process only the four test identities and inspect detection

**Identity processing** rechecks a person's data and the access packages associated with that person. In this case, ISC compares the collected permissions with the profile's two required entitlements. A successful profile save does not prove that identities have been updated.

Open **Admin > Identity Management > Identities**. Select only employee01, employee02, employee03 and manager02, then use **Actions > Process Identities**. Check the actual operation and resulting records before continuing.

Inspect their access-profile associations and current B account permissions.

An association means ISC now records the identity as holding the profile. This is a change to ISC's access model, while the account's Read and Export values can remain exactly as they were.

Employee01 and employee02 already have both required rights, so the expected result is a detected profile for each. Employee03 and manager02 have Read only; they should not gain the two-right profile or Export.

If detection is absent or differs, check the profile's contents, source, enabled state, the current account data and processing result. Do not issue grants or alter the CSV to force the expected association.

In the table below, **standalone** means a permission reviewed on its own, outside the profile. The expected representation is:

| Person | Account permissions still present on B | Review unit after verified detection |
|---|---|---|
| employee01 | Read and Export | One detected access profile |
| employee02 | Read and Export | One detected access profile |
| employee03 | Read | One standalone Read entitlement |
| manager02 | Read | One standalone Read entitlement |

There are still six account-permission holdings. The corresponding review view can have four units: two profile holdings and two standalone Read holdings.

For employee01, two account permissions are now covered by one profile review item. Employee03 has no profile and still has one Read item. We are counting the objects being reviewed, not copies of the underlying permissions.

A filter can then select a subset of those four review units.

This difference is why comparing a review-item total directly with the number of account permissions can mislead you.

## Filter the object that now exists

Do not reuse the earlier explicitly selected entitlement configuration to prove a profile-filter result. That selection can leave out profile holders before the new filter is applied.

Instead, create a fresh **Access Items** campaign using **Using a Campaign Filter**. Name it `certlab-006-after-export-run01`. Select the existing B Export inclusion filter and use the same reviewer/settings. Generate a preview now and leave its saved template unscheduled. Record the saved configuration and any generated campaign record separately from the earlier inclusion comparison.

After verified detection for both Export holders, the expected standalone Export result is empty. An empty campaign may have no ordinary preview and may appear as an empty completed record. Inspect the actual state and contents; do not treat that label as a completed business review.

Do not activate any review work from this comparison. If there is no ordinary preview, record that outcome rather than try to produce a reviewer task. The absence of a direct entitlement item is not evidence that Export was removed from the account.

Create a third filter, `certlab-006-bundle-in-run01`: **Inclusion**, one **Access Profile** criterion, **Equals**, the exact temporary profile.

Generate a new **Access Items > Using a Campaign Filter** campaign named `certlab-006-bundle-run01` using that profile filter. Keep the same Manager reviewer/settings, generate only a preview and leave its saved template unscheduled.

Check that its actual review contents include the profile holdings for employee01 and employee02, with manager01 responsible for both.

Inspect the profile details to see its two entitlements. Two profile review holdings represent two people each holding that package; they are not four independently selectable entitlement review items.

If the result differs, retain the mismatch as an unresolved check. Do not start either campaign to get past it.

## Recognize the other common review units

The origin of access matters as well as its name.

A profile detected from existing rights or obtained as a standalone request can be reviewed as a profile. If a **role** grants that profile, its access is represented through the role instead. A role groups access requirements for assigned identities.

An automatically assigned role can be acknowledged in a review because the access model controls its assignment. A requested role can have Approve/Revoke actions. A profile required by a **lifecycle state**, such as an employment state, does not appear as an individually reviewable profile.

Before choosing a filter, inspect which object the identity actually holds and why it is there.

Do not guess Role-filter behavior from an Entitlement example. Similarly, matching one account attribute does not prove what happens to that person's other accounts. Those variations need their own inspected input and full retained/omitted set.

## Did the filter remove access, or did the review unit change?

Both employees still have Read and Export on B. The temporary profile is detected for them. A fresh standalone Export inclusion campaign has no review work, while the profile inclusion campaign has two profile holdings.

Someone suggests adding Export back to the CSV because the entitlement review is empty.

Would that address the problem? What facts would you compare first?

<details markdown="block">
<summary>Compare your reasoning</summary>

Export is already present on both accounts. Adding it again would not restore a missing permission.

The change is in the review representation: the two entitlements are covered by each person's detected profile. Compare current account values, the actual profile association and the selected filter type.

Choose the filter for the review unit that matches the requirement. Do not widen scope or change account data just to make an expected number of entitlement rows appear.

</details>

## Remove the temporary work and prove the original state

First save the comparison results, source/account observations, profile associations and IDs of this lab's filters, previews and templates.

Confirm each test campaign was never activated, has no reviewer decisions and has no removal work. Account for the two original comparisons and both post-profile configurations. Include any empty generated record from the after-export test, even if it has no ordinary preview. If a campaign was activated or another dependency exists, reconcile that actual work before using the routine cleanup below.

Remove only these unused campaign instances. From **Admin > Certifications > Campaigns**, select their checked records, use **Delete**, and confirm **Delete Campaign**. Their preview pages also provide deletion. Locate their unused saved configurations in Search's **Saved/Scheduled** tab and remove only those unscheduled test configurations.

Retire the previews before deleting the temporary profile. Deleting a profile does not erase it from existing certifications or make those old records safe to activate.

Check the profile is not used by any request, role, lifecycle state or other active work. In **Admin > Access Model > Access Profiles**, use **Actions > Delete** on the exact test profile and confirm **Continue** after reviewing the message.

Deleting this profile removes the package's association with its holders; it does not remove their account entitlements. Verify that actual result rather than treat deletion as an access-removal method.

Process the same four test identities again. Confirm that the temporary profile is absent and B's six holdings remain directly represented. A must still have its original five holdings.

Finally, remove only the three temporary filters through **Campaign Filters**, selecting their exact records and **Delete > Delete Campaign Filter**. Do not remove earlier labs' saved work.

No account, person, source or entitlement catalogue needs deletion. Keep the original CSV files unchanged. The completed result is a checked comparison and a restored access model, not a reviewer approval or a permission removal.
