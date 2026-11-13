# How does a role-composition decision become a corrected role?

A role is intended for viewing reports. When you inspect it, you find that it also gives people permission to export those reports.

The reviewer rejects the export access. Later, a task for correcting the role is marked complete.

Has the problem been fixed?

We need to check what changed in the role and what happened to the accounts that already received its access. Those are connected results, but they need different evidence.

## Start with what the role gives people

In SailPoint Identity Security Cloud, or **ISC**, a **role** groups access for a business purpose. Its **definition** describes the access it includes and the related configuration.

Our role is called Report Reader. Its approved purpose is viewing reports inside Reporting Production. Downloading copies is outside that purpose.

The role contains two **access profiles**. A profile is a bundle of access rights from one source:

- Report Reading contains REPORT.VIEW, permission to view reports.
- Report Export contains REPORT.EXPORT, permission to export them.

ISC represents each of those rights as an **entitlement**. The **source** is ISC's configuration for the reporting application and its account information.

Look at the connection: Report Reader includes the profiles, and the profiles supply the permissions. The name Reader sounds narrow, but its current contents include export.

Two people hold this role. Their production accounts are rep-6101 and rep-6102. Each account currently has both permissions. ISC has current account information, and the accounts are correctly linked to their **identities**, ISC's records for those people.

Both people still need viewing. No other assignment requires export in this example.

## Choose the question you want the review to answer

A person's **role assignment** is the association through which they hold the role.

An assignment review asks whether that person should keep it. A **role-composition review** asks whether the shared role itself is appropriate: does its access fit its intended purpose?

Here, the approved purpose is viewing only, so export does not belong in the shared definition. Reviewing just one holder would leave that definition unchanged for the other holder and for future assignments.

An authorized administrator prepares a **certification campaign**, which organizes review work. They use the supported Role Composition route and select Report Reader as the role to assess.

This route uses the **legacy campaign experience**, the older certification path. Use the controls and work records for that path when following its result.

Report Reader is eligible for this composition route. Check eligibility before planning the review; finding a role somewhere in ISC does not establish that every campaign type can review it.

## Give the judgment and the correction clear owners

The **role owner** is the person recorded as responsible for the role. The **reviewer** assesses its contents. The **remediation owner** is responsible for carrying out the required correction.

These responsibilities need different knowledge and authority. Understanding why a role exists does not automatically give someone permission to edit it.

For this campaign, the role owner understands Report Reader's approved purpose and is permitted to review it. That person is also a role administrator, authorized to change this role, and is explicitly selected as the remediation owner.

One person fills both responsibilities here. We will still check the actual task assignment before relying on who must act. Do not infer the recipient merely from an ownership label.

The campaign requires a comment explaining rejected contents, so the person making the correction can understand the intended change.

## Check the work that was actually generated

Campaign settings describe what should be prepared. **Generation** creates the review work from those settings and the available information.

Before starting the campaign, inspect its **preview**, the generated work available for checking. Confirm that it contains Report Reader, the expected profiles and the intended reviewer.

Selecting the role's name is not enough. A similarly named role might contain different access, or the generated work might not match the intended selection.

The reviewer can inspect the role's details and associated profiles. A role can also have **membership criteria**, conditions used to determine who receives it. Those details can matter when assessing its design. In this example, the problem is the export profile in its contents.

Once the generated work and responsibilities match the requirement, the administrator starts the campaign. The reviewer can now assess the prepared work.

## Make the correction understandable

The reviewer confirms that Report Reading fits the role's purpose. Report Export does not.

In this composition review, **Revoke** on the export profile records that it should be removed from the role's contents. It is a request for a role correction, not evidence that either account has already lost export.

A useful comment is precise:

> Remove Report Export from Report Reader because this role is approved for viewing reports inside the application only. Retain Report Reading. Check the removal of export from existing holders without removing their viewing permission.

The comment identifies what must change, why and what must remain. “Too much access” would leave the administrator to work out those details.

The reviewer finishes and confirms the required review decisions. This confirmation is **sign-off**. It is separate from merely saving a choice.

Now suppose the review is confirmed and the required correction task is available. Inspect that task, its role, its instructions and its actual recipient. In our case, it is assigned to the role administrator selected earlier.

The work being followed is a role-definition correction. It is not an instruction to remove the entire role from both people.

## Change the role's contents

The administrator opens the correct role and removes its association with Report Export. Report Reading remains included.

The association being removed is:

Report Reader → Report Export.

It does not require deleting Report Export from ISC or emptying that profile's contents. Another role could legitimately use the same profile. Changing a shared profile would affect more than this role's inclusion of it.

After saving, inspect Report Reader's actual contents. Confirm that Report Reading remains and Report Export is absent.

The two people's assignments to Report Reader still make sense. Their continuing viewing need has not ended. We have corrected what their shared role contains rather than removed their whole role assignment.

At this point, the role definition has been corrected. We still need to establish what happened to the export permission already held by each account.

## Follow the change into the accounts

An application account is separate from the role configuration in ISC. Saving a smaller role definition does not, by itself, prove that existing application permissions changed.

**Role access removal propagation** is the configuration that lets supported role-content removals lead to removal of previously granted access.

For the profile-removal case here, that feature is enabled before the change, and Report Reader remains enabled. These conditions matter to the effect on its existing holders.

The relevant **identity processing** evaluates identity and access configuration. The resulting **provisioning** work makes the required account-access changes in the application.

Our reporting connection supports the required removal and is authorized to perform it. Once the relevant processing runs, follow the account-change work for REPORT.EXPORT on rep-6101 and rep-6102.

The administrator's manual role edit can therefore be followed by automated changes to application accounts. “Manual correction” describes who updates the role definition; it does not mean that every later account change must also be made by hand.

Follow the actual processing and operation results. A saved role edit or a request to start processing is not proof that the account changes have finished. Where processing must be initiated, use the authorized process for the intended scope; do not assume an action applies only to this one role.

Here is the connection we are following:

```text
Role contents being reviewed
  Report Reading -> REPORT.VIEW
  Report Export  -> REPORT.EXPORT
                 |
                 | reviewer records the correction
                 v
Required role correction
  Assigned administrator removes Report Export
  from Report Reader; Report Reading stays
                 |
                 | propagation and processing
                 v
Account-change work
  Remove REPORT.EXPORT from the affected accounts
                 |
                 | verify current permissions
                 v
Verified result
  Viewing remains; export is absent
```

The upper part concerns a decision and a human change to shared configuration. The lower part follows the resulting account work under the conditions described above. The arrows do not promise an immediate change.

## Check both the removed and retained access

Suppose the account-change work completes successfully. A current check in Reporting Production then shows:

| Account | REPORT.VIEW | REPORT.EXPORT |
|---|---|---|
| rep-6101 | Present | Absent |
| rep-6102 | Present | Absent |

These results match the requirement: both people can still view reports, and neither account retains export.

If viewing had also disappeared, removing export would not be the whole explanation. The correction would have taken away access that was still needed.

Check ISC's account information as well. **Account aggregation** reads account data into ISC. An account view based on information collected before the change can still show the old export permission.

Obtain and process updated information through the source's supported collection process. In our successful example, the refreshed ISC account data agrees with the application.

You can now explain the result using connected evidence: the review required a particular correction, the saved role has the intended contents, the account work succeeded, and the correct accounts have the required permissions.

A task marked complete supplies part of that history. It cannot replace the checks of the role and its account results.

## What changes if propagation is disabled?

Keep the same starting access and required role correction, but now suppose role access removal propagation is disabled.

Removing Report Export can still correct the role definition. That content edit does not remove the old permissions from existing holders through role-content propagation.

The role can therefore show the intended smaller contents while an existing account still has export. That observation needs follow-up; it is not proof that the role edit failed to save.

Identify the remaining access-removal requirement and arrange a supported, authorized way to meet it while preserving viewing. Do not casually enable an organization-wide feature as a shortcut for one correction.

Likewise, do not delete the role and assume that its former members' permissions have disappeared. A role-definition change, an assignment change and an application change have different effects.

Record which result is complete and who will handle the remaining work. If the task records only the completed role edit, keep the outstanding account requirement visible through the appropriate process.

## Work through a different remaining permission

A Warehouse Viewer role is approved for viewing stock quantities. It includes Stock Reading and Stock Adjustment profiles.

Stock Reading supplies STOCK.VIEW, permission to view quantities. Stock Adjustment supplies STOCK.ADJUST, permission to change them.

A composition reviewer rejects Stock Adjustment because changing quantities is outside Warehouse Viewer's purpose. The role administrator removes that profile from the role. The role remains enabled, the supported propagation feature is enabled, and the relevant processing finishes.

Two people hold Warehouse Viewer and use warehouse accounts wh-7101 and wh-7102. A current application check shows:

- wh-7101 has viewing and no adjustment permission.
- wh-7102 has viewing and still has adjustment permission.

An investigation confirms that the second person also holds an independently approved Inventory Controller role. Its current assignment supplies STOCK.ADJUST to wh-7102 for an authorized duty. The first person has no such additional assignment.

Someone suggests repeating the removal because “all adjustment access should have gone.”

Does the supplied evidence support that conclusion?

The composition requirement concerns what Warehouse Viewer should contain. Its saved definition now excludes Stock Adjustment. The first account has the expected viewing-only result.

The second account has another verified reason to retain adjustment. Its remaining permission does not, by itself, show that Warehouse Viewer still contains the rejected profile or that its correction failed.

Check the other role's actual assignment, the correct account and its current authorization. Under the supplied facts, retaining adjustment through Inventory Controller is consistent with the separate approved duty.

Now change the business question. Consider a different role, Warehouse Operator, whose approved purpose legitimately includes both viewing and adjustment. Only one holder has moved to viewing-only work; the other holders still need both.

That person's changed duty calls for assessing their assignment and the access they should retain. It does not establish that adjustment should be removed from the shared role for everyone.

Start with the object the review is meant to correct. Then follow that correction to its actual scope and account results.
