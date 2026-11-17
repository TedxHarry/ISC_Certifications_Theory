# CLS-003: Review a role's contents and verify the correction

A role called Report Reader sounds clear enough. But suppose its contents include both Read and Export.

The name tells us what someone intended. The contents tell us what access the role is designed to provide. If the job requires reading only, the design needs a correction before we rely on it.

You will review one test role, explain the correction it needs, and follow the work until an authorized administrator changes the role. The role will have no members. That lets us check its design without changing anyone's account permissions.

## What are we reviewing?

An **entitlement** is a permission ISC tracks, such as Read. An **access profile** groups permissions from one source. A **role** can group access profiles into the access needed for a job or function.

Our test role starts with this structure:

> Report Reader role
>
> → Read profile → Read permission
>
> → Export profile → Export permission

A role's **composition** means its design: the access it contains, the criteria for receiving it, and details such as its name and description.

A role-composition review asks, “Is this role designed correctly?”

**Approve** records that the reviewed design can be kept. **Revoke** requests a correction. Its comment tells the administrator what needs changing; the review decision does not edit the role by itself.

A person's access review asks a different question: “Should this person keep this role?” Removing a person's assignment would not correct the role for everyone else.

Here, the required correction is to remove the Export **profile reference**, the role's link to that profile. We will retain the Read link. The Export profile itself will remain a separate object with its Export permission intact.

## Prepare an isolated design

Use an approved training tenant and an administrator allowed to create the test source, profiles and role. The actual campaign creator must also be allowed to create and start the role-composition review.

Current documentation places role-composition campaigns in the **legacy** certification workflow, the older campaign workflow still used for this review type. Check the tenant's actual Role Composition choice and location before setup. If the route is unavailable or the test role is ineligible, resolve that requirement before running the lab. Do not assign the role to someone just to make it appear.

An **identity** is ISC's record for a person. Use the existing `certlab-manager02` identity as role owner and reviewer. The role owner is responsible for that role's design. Confirm this person can sign in through an approved reviewer session; an imported identity record alone does not provide a working login.

The prepared five-person dataset belongs to certlab-people-profile, fed by certlab-people-csv. Verify both manager identities are present. F will add no people; the correction administrator uses an existing authorized account.

Also identify an existing authorized **Org Admin or Role Admin** who will make the correction. Record this actual administrator privately. This person will be selected as the campaign's **remediation owner**: the person responsible for carrying out the requested correction.

The reviewer decides what needs changing. The remediation owner makes and verifies that change. Their permissions and responsibilities need separate checks even when one person could perform both.

On a repeat, reuse this lab's source, profiles and role only after verifying the original starting design and zero-member state below.

### Create the small permission catalogue

For the initial setup, open **Admin > Connections > Sources > Create New**, select **Generic** and use its supported manual-upload configuration. Create **certlab-role-design-csv**, called **F**, with `certlab-manager01` as source owner.

A **source** is ISC's configured representation of a system and its collected data. Its owner is responsible for that source in ISC. F will contain two permission definitions and no accounts. Keep it **non-authoritative**: it is not supplying trusted people records and must stay outside any human identity profile.

Use lab-data/baselineF/role_design_entitlements.csv. Its values describe:

| Permission value | Display name | Purpose in the exercise |
|---|---|---|
| certlab-design-read | Design Report Read | Required reading access. |
| certlab-design-export | Design Report Export | Access that does not belong in this reader role. |

These definitions represent training permissions. There is no reporting application or user account behind them.

Inspect the actual supported Generic upload mode and its dependencies. A **schema** defines the fields ISC collects. **String** means text; **scalar** means one value; **multi-valued** allows several values.

In **Account Management > Account Schema**, configure id and name as scalar String fields, with Account ID id and Account Name name. Configure groups as a multi-valued entitlement field with the source's supported entitlement association.

Download F's actual entitlement template through **Entitlement Management > Entitlement Aggregation > Download Entitlement Schema**. Put the supplied values into a private copy, retaining the template's required headings, order and additional fields.

**Aggregation** collects supplied data into ISC. Upload the catalogue through **Entitlement Aggregation**, follow successful completion and confirm both entitlement objects belong to F. Check that F still has zero accounts.

An entitlement definition describes a permission that could be granted. It does not mean anyone has that permission. There is no account CSV to upload in this exercise.

### Create two native access profiles

Create the following profiles under **Admin > Access Model > Access Profiles > Create New**:

| Profile name | Entitlement Source | Only entitlement | Primary Owner |
|---|---|---|---|
| certlab-cls003-read | F | certlab-design-read | manager02 |
| certlab-cls003-export | F | certlab-design-export | manager02 |

For each profile, save its basic configuration, add its one permission under **Manage Entitlements**, and save again. Give each a description that clearly states its training purpose.

Keep **Allow Access Requests** off. Enable the profile only after verifying its exact source and contents. Do not attach it to a lifecycle state, application or any other role.

The CSV has supplied the entitlement definitions. Creating these profiles is a separate action inside ISC. A **profile holder** is an identity recorded as having that profile. Check that both profiles exist, contain exactly one correct entitlement, and have no holders or other uses.

### Create the role without giving it to anyone

Under **Admin > Access Model > Roles > Create New**, create:

- Name: **certlab-cls003-report-reader**
- Role Type: **Standard**
- Primary Owner: **certlab-manager02**
- Description: **Temporary test role for report reading; remove Export after review.**

Keep the role disabled while configuring it. Under **Manage Access > Access Profiles**, add the two profiles you just created. Save and verify their actual IDs. Add no direct entitlements.

The profile list tells ISC **what access** the role contains. **Define Assignment** tells it **who receives the role**. A **role assignment** means an identity has the role; an **assignment criterion** is a condition ISC uses to choose who receives it automatically.

Choose **Standard Criteria** and add one condition:

> Identity Attribute — uid — Equals — certlab-cls003-no-member

The uid attribute contains the identity's username. The value above is a synthetic training value that must match nobody. Verify the attribute is mapped and selectable, inspect the saved condition, and establish that no identity in the actual tenant has that value.

Keep this as the only condition. Keep role access requests off and add no identities through a membership list.

This condition deliberately gives the test role no audience. It is a way to isolate this exercise, rather than a membership rule for a real job. A production role needs criteria supported by the actual business requirement.

Before enabling the role, verify zero matching identities, no assignments and no requests for it. Enable only the prepared test role, then inspect **View Details > Identities** and confirm it still has no members.

If an unexpected member, request or operation appears, pause this run and reconcile what happened. Do not remove someone's access merely to restore our expected count.

You do not need the role list's **Apply Changes** action for this definition-only outcome. That action starts identity processing across the tenant. Our result will prove the saved role correction and its zero-member boundary; it will not claim a rollout to members. Keep global role-removal propagation settings unchanged.

## Inspect the design before creating the review

Record the actual F source, two entitlement, two profile and role IDs privately. Save the role's current configuration and verify:

- It is the one standard test role, enabled, with requests off.
- Its contents are exactly the Read and Export profiles, with no direct entitlements.
- Both profiles contain their original single F entitlement.
- The uid condition is unchanged and matches nobody.
- The role has zero assignments; the profiles have zero holders; F has zero accounts.

The expected_role_design.json file in baselineF records these planned relationships and the expected correction. It is a reference contract, not an import file or a record exported from your tenant.

The supplied work requirement is simple: this reader role should provide reading only. Export is outside that purpose. Its name, description and test-only no-member criterion can remain.

We have enough information to explain the required correction precisely. “Reduce access” would leave the administrator guessing which object to change.

## Create one role-composition campaign

A **certification campaign** organizes review work: what needs review, who reviews it and when it is due.

Open **Search > Certification Campaigns > New Campaign > Role Composition**. Choose **Specific Roles That I Select**.

Search for:

`name:"certlab-cls003-report-reader"`

Inspect the result and select the exact saved role by its ID and contents. A matching name alone is insufficient if there are similar records. Use **+ Add To Campaign**, then **Certify Selected Roles**.

Name the campaign **certlab-cls003-role-design-run01**.

If the name already exists, use an unused run suffix and record it; preserve earlier history. Keep the saved-template and generated-campaign references separate.

Choose **Role Owner** when offered and verify manager02 as the intended reviewer. If the supported route instead offers an explicit Individual choice, select manager02 and record that this was an explicit assignment.

Select the previously identified authorized administrator as **remediation owner**. Inspect the actual setting. Source ownership, role ownership and remediation responsibility are separate properties; do not substitute one for another.

Choose to maintain undecided items so a blank review does not become an unintended rejection. Require comments for Revoke decisions, turn this campaign's notification emails off and choose a future due date.

A **preview** lets you inspect the generated work before starting it. A **template** saves campaign settings for reuse. Generate a preview now and save an unscheduled template. Leave additional filters and recurring schedules out of this run.

Use **Legacy Saved/Scheduled** for the saved configuration and **Legacy Campaigns** for the generated instance in the administration interface. Verify the selected role, its two profiles, criterion and details, the reviewer and the remediation-owner setting.

We selected one role design. Its two profiles are contents to inspect; do not assume they are two separately assigned certifications or two independent profile decisions.

If the preview differs, correct the selection or setup before starting. Once it matches, use **Start Campaign** on the checked preview and retain the actual campaign ID.

## Review the role as its owner

Sign in as manager02 and open the assigned work through **Certifications > Active**. Select the role and inspect its contents, membership criteria and details.

Open the Read profile and trace it to F's Read entitlement. Then trace the Export profile to F's Export entitlement. Check the criterion still selects nobody.

The Read content fits the role's purpose. Export does not. The current design therefore needs correction.

Use the supported **Revoke** action for the role composition that needs changing. Explain the required correction in its comment. For example:

> This reader role should contain reading access only. Remove certlab-cls003-export from certlab-cls003-report-reader. Retain certlab-cls003-read, the role's owner, description and existing test-only uid criterion. Keep the Export profile and both entitlement definitions intact.

Include the actual object IDs in private evidence where needed. The comment should let another authorized administrator identify the exact relationship to change.

Submit the comment through the actual review control. If the interface presents separate design items, match each action to its actual item and the requested Export correction. Do not reject retained Read or the test criterion just to complete a row.

Check every item the generated review requires, then complete its actual final confirmation. **Sign-off** is that final submission of review work. Preserve the actual final state and reviewer/time rather than treating a saved choice or comment as proof of sign-off.

This decision asks for a correction to the role's design. It does not instruct the administrator to delete the role or remove a person's role assignment. Our test role has no assignments.

Preserve the submitted decision, comment and finalization evidence. The review decision and the completed correction are two separate stages.

## Follow the correction task

As the configured remediation owner, open **Task Manager** and inspect the actual work created from this campaign.

Match its campaign, role, comment, recipient and full scope. The correction work is also called **remediation**. Do not assume the role reviewer is also the task recipient. If the task is missing or assigned differently, check the campaign configuration and actual delivery before editing anything.

A task requesting a role change needs a role change. Uploading a modified account CSV would change a different kind of data.

Recheck that the role still has zero members and the profiles have no new dependencies. Then open the exact role through **Admin > Access Model > Roles > Edit**.

In **Manage Access > Access Profiles**, use **Remove** for certlab-cls003-export only. Save the change, reopen the role and inspect the saved contents.

The role should now contain certlab-cls003-read only.

Open certlab-cls003-export separately. It must still exist and still contain its Export entitlement. Removing a profile reference from one role does not require changing the profile's own definition.

Use these checks to verify the complete result:

| Object or relationship | Expected after correction |
|---|---|
| Test role's profile references | Read only; Export reference absent. |
| Role name, type, owner, description and criterion | Unchanged. |
| Role enabled/request settings | Enabled; requests remain off. |
| Read profile | Still contains only F Read. |
| Export profile | Still exists and contains only F Export. |
| F entitlement catalogue | Both definitions remain. |
| Role assignments, profile holders and F accounts | All remain zero. |

Keep the actual before/after role configuration and available change history with the task and review comment. Inspect any unexpected operation or work before declaring the correction complete.

When the full task scope has been fulfilled and checked, use its supported completion control, such as **Mark Complete**. Record the task's actual completed state. A completed task without the requested role change is incomplete evidence.

The CSV catalogue stays unchanged throughout. When performed in ISC, the role edit is the actual native outcome. This exercise does not demonstrate removal of an application's permission from a user.

## What changes when a role has members?

Before correcting a role with members, an administrator must understand who holds it, how they received it, what other access requires the same permissions, and how the tenant applies role changes.

A role-definition edit, identity processing and a successful target-system change are different events. Removing a profile from a role does not by itself prove that all existing members lost its permissions.

For a real rollout, inspect the configured **propagation** behavior: whether and how a role-content change is applied to existing members' access. Check their assignment origins, plan the authorized change, then verify both removed and retained access through actual operations and account observations.

Keep that rollout separate from this lab's result. Here, zero membership is part of the starting state and must remain true.

## Check that the editor changes the right object

The task says to remove the Export profile from the reader role. An administrator instead proposes opening the Export profile and deleting its entitlement.

Would that fulfill the request?

<details markdown="block">
<summary>Follow the objects involved</summary>

The requested change concerns one role's reference to a profile.

Changing the profile's contents changes the shared package itself. Other roles or workflows using that profile could be affected. It would also leave our single-entitlement profile empty, which is not a valid intended profile.

Compare the actual role reference, profile definition and task comment. Remove only the Export reference from the named role and verify that the profile retains its entitlement.

A task checkbox cannot correct the wrong edit. If an incorrect change was actually made, preserve its history, investigate its scope and arrange the authorized correction before closing the work.

</details>

Use this as a reasoning check; there is no need to save an intentionally incorrect edit.

## Restore the test design for another run

First preserve the signed review, correction task, before/after role evidence and zero-member checks. Confirm there is no outstanding task, scheduled campaign generation or pending change that could act on this role after restoration.

Before re-adding Export, check again that the role has zero assignments, both profiles have zero holders and no unexpected requests, dependencies or operations appeared. If that state has changed, resolve the actual scope before restoring this deliberate defect. Do not add Export to a role that has unexpectedly acquired members.

Reopen the test role. Under **Manage Access**, add the same original certlab-cls003-export profile, review the selection and save.

Verify the exact initial two-profile design. Check that the role's owner, description, criterion, enabled state and request setting remain unchanged. Confirm both profile contents and F's two entitlement definitions.

Recheck zero role assignments, profile holders and source accounts. Keep the prepared source, profiles and role for repetition. No deletion is needed to restore this design.

This reintroduces the deliberate training defect after its correction has been recorded. Preserve the restoration time separately from the earlier successful correction.

Retire only this run's unneeded unscheduled template in **Search > Certification Campaigns > Legacy Saved/Scheduled** after matching its saved reference and actual name and confirming no generation remains. Preserve the separate completed campaign, its reports and task history. Leave earlier course sources, files and people unchanged.
