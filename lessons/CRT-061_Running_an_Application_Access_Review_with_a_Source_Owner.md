# Run an application access review with a source owner

The request is: “Review access to Reporting Production. Confirm which permissions each account still needs, and remove access that no longer has an approved purpose.”

The accounts belong to people in different departments. One person has both an ordinary account and a separate administration account. The person responsible for the application also has access.

Sending this work to one department's manager would not establish coverage of the whole application.

Let's follow a source-owner review that accounts for those differences, from selecting the right system to checking the final account results.

## Identify the application boundary first

In SailPoint Identity Security Cloud, or **ISC**, a **source** is the configuration representing a system or collection of account data. An **account** is a record used to access that system.

The application itself holds the accounts and enforces their permissions. ISC collects information about them so access can be managed and reviewed.

Our reporting application has two source configurations: Reporting Production and Reporting Test. Their account names and permission labels can look similar.

The business requirement concerns Production only. Check which source actually represents that environment, including its identifying reference and connection details. Selecting a source because its name contains Reporting would leave that boundary unverified.

A **source-owner campaign** organizes review work around selected sources and their recorded owners. It fits this application-focused requirement when those owners understand the permissions and can obtain evidence of current business need.

Here, the agreed inventory point defines which existing accounts and access the review must cover. A current application inventory supplies this complete set:

| Account | Who uses it | Existing permissions |
|---|---|---|
| app-181 | worker-181, ordinary reporting work | Read Reports; Export Reports |
| app-182 | contractor-182, approved support work | Read Reports; Administer Reports |
| app-admin-181 | worker-181, separately authorized administration | Read Reports; Administer Reports |
| app-owner-610 | owner-610, application operations | Read Reports; Administer Reports |

Read Reports allows viewing reports. Export Reports allows downloading copies. Administer Reports allows changing report definitions and application settings. Those capabilities have been checked in the application.

An **entitlement** is ISC's representation of an access right from a source. Each permission in this example can be reviewed individually. None is contained in a larger access package or required through an automatic assignment.

We therefore expect four accounts and eight reviewable items.

There are three people, because worker-181 has two accounts. Combining their accounts into one row would lose the distinction between ordinary reporting and separately approved administration.

These are the supplied facts for this review. In actual work, establish the full inventory and the meaning of each permission rather than assume that this small set represents every application.

## Confirm that ISC has the same accounts and access

An **identity** is ISC's record representing a person or another managed subject. The three people here have established identities, and each application account is linked to the correct one.

**Account correlation** creates the account-to-identity association. Check that app-181 and app-admin-181 both belong to worker-181, while keeping them identifiable as different application accounts.

**Account aggregation** collects source account information into ISC. Compare that collected information with the application inventory and its observation time.

For this review, all four production accounts and eight permissions are correctly represented. There is no unaccounted machine or unmatched account in the supplied starting inventory.

If the application has an account that ISC has not collected, generating a campaign will not supply the missing application observation. Locate the collection or association problem before relying on the generated work.

Likewise, do not select only employees from one department. The contractor and the separately authorized administrator can be part of the application population even though they do not belong to the same employee team.

The question is which accounts and permissions the approved application review must account for.

## Check who is actually recorded as source owner

A **source owner** is the responsible person recorded for a source in ISC.

That setting is different from a business document calling someone the application owner. A person can understand the application without being the configured source owner used by this campaign.

An authorized administrator opens **Admin > Connections > Sources**, selects Reporting Production, then opens **Source Setup > Base Configuration** and checks **Source Owner**.

The recorded owner is owner-610. This person understands the reporting permissions and is permitted to perform the review.

If the field needs correction, establish the actual responsible person, update the supported owner setting and save it. Do not enter an available person's name merely to make campaign generation possible.

Every source selected for this dedicated route needs an assigned owner. If the prerequisite is missing, resolve it before generating the work.

Also distinguish **access ownership** from source ownership. An access owner is responsible for an individual access object, such as an entitlement or a package of permissions. That person's name does not automatically replace the Source Owner reviewer rule.

## Prepare a campaign for this production source

A **certification campaign** organizes access reviews. A **certification** is an assigned review within it. A **review item** is the access entry presented for a decision.

The administrator opens **Admin > Certifications > Campaigns > Create New** and selects **Source Owner Campaign**.

Confirm that this route and the required administrative permissions are available in the environment being used.

Give the campaign a name identifying the reporting production review and its cycle. Describe its purpose, inventory point and intended account population.

Select **Reporting Production** in the source selection. Leave Reporting Test outside this requirement. Selecting **All Sources** would broaden the exercise beyond the agreed application boundary.

Check the campaign-filter field. A **campaign filter** includes or excludes supported review content according to configured conditions.

For this example, no filter narrows the intended human-account access. The generated preview will still need to establish that all eight items are present. Selecting the source is an instruction; the generated accounts and items are evidence of what was prepared.

Set the deadline, notification and decision-comment choices. Require a useful explanation for removal, including the account, capability and ended business need.

Our unfinished-work policy maintains never-decided access at administrative completion and records the unresolved question for follow-up. It does not turn an unexamined permission into a justified business decision. All reviews will finish before the deadline in this normal example.

The administrator also confirms the removal path before launch. Reporting Production has a supported, enabled connection that can remove the two kinds of membership involved here. Its integration credentials have the authority needed for those changes.

Integration credentials identify the software connection, such as its configured account or token. They are separate from the reviewer's ISC login and review permission.

Being able to collect accounts does not prove that the connection can change them.

## Inspect both the coverage and the independent assignments

Select **Preview Campaign** and open the generated preview.

A **preview** is prepared review work available for inspection before the campaign starts. It uses the information and settings available when that work was generated.

Compare the actual production accounts and permissions against the four-account inventory. Check the account references, not only the number eight.

Now check the reviewers.

owner-610 holds application access on app-owner-610. **Self-certification** would mean reviewing their own access. ISC prevents that by separating such work and assigning it to another identity.

In this example, owner-610's verified manager, R-711, is a suitable independent reviewer with the required business and application context.

The inspected preview contains:

- Six items for owner-610: the access on app-181, app-182 and app-admin-181.
- Two items for R-711: the access on app-owner-610.

This is the actual grouping supplied for our example. Do not calculate a universal certification count from the number of sources or owners.

Confirm that each reviewer can perform their assigned work and that neither is assessing their own access.

A current owner field cannot substitute for this check. If the owner setting changes after generation, inspect the existing assignment; changing the source does not establish that the prepared review moved.

Once the content, assignments and settings agree with the requirement, the administrator selects **Start Campaign**. Verify that the campaign is active and both reviewers can open their intended work.

## Combine application knowledge with current-work evidence

owner-610 opens **Certifications > Active** and selects the assigned review. In the identity and access-item details, keep each permission attached to its source account.

The source owner can explain what Administer Reports permits. To decide whether contractor-182 should keep it, the reviewer also needs to know what the contractor is currently authorized to do.

The responsible business sponsor confirms the continuing support assignment. A **sponsor** here is the business contact accountable for that contractor's work.

Reading reports is still needed. The temporary repair that required administrative access has ended, and no continuing approved duty requires administration on app-182.

Those facts support keeping Read Reports and removing Administer Reports from that account. The contractor label alone would not supply either decision.

For worker-181, the current ordinary reporting duty needs reading but no longer needs export from app-181. The earlier export task ended.

The same person still has a separately approved administration duty through app-admin-181. The business owner and application evidence confirm why both reading and administration remain appropriate on that account.

This is why we kept the two accounts separate. Removing export from the ordinary account does not mean that every permission on the person's admin account should disappear.

owner-610 records:

- **Approve** Read Reports and **Revoke** Export Reports on app-181.
- Approve Read Reports and revoke Administer Reports on app-182.
- Approve both permissions on app-admin-181.

Approve accepts keeping the reviewed access. Revoke records that it should be removed.

The removal reasons identify the ended duties and the exact accounts. “I own this application” would not explain either choice.

## Let the independent reviewer assess the owner's access

R-711 opens the separately assigned review for app-owner-610.

Source ownership is a responsibility in ISC. It does not automatically justify every application permission the owner holds.

R-711 checks the current application-operations duty, its approved authority and the actual capabilities. For this example, that work requires both reading and administration through app-owner-610.

Those verified facts support two approvals. The source owner's own assertion is not the sole basis for the independent judgment.

Across both assigned reviews, there are now six approvals and two revokes.

Suppose owner-610 finishes their six items first. Has the whole campaign's review work finished?

Not while R-711's two items remain unfinished. The source owner's assigned review and the campaign's complete set are different scopes.

Track the actual review items and each reviewer's final confirmation. A **Campaign Status Report** helps inspect item choices and decision actors. A **Certification Sign Off Report** supplies final-confirmation information.

Generate reports again when later changes need to be reflected. An earlier downloaded file cannot establish a later sign-off.

Each reviewer checks the decisions and uses the supported **Finish** step to give final confirmation, or **sign-off**. Saving the choices alone does not establish that confirmation.

When all reviewers finish and sign off by the deadline, the documented normal path moves the campaign to **Completed**. All required reviews are signed in time here; inspect the resulting campaign state. That status still does not prove that both application changes have finished.

## Follow each required removal to its account

**Remediation** is the work to carry out the review's required changes. **Provisioning** changes accounts or access through the supported integration.

Our two requirements are specific:

Remove Export Reports from app-181, and remove Administer Reports from app-182. Keep their Read Reports permissions.

A **connector** is the integration used to read or change source information. For this continuation, the final decisions have reached the supported removal work, and the configured connector performs the required membership changes.

The instructions concern those account memberships. They do not mean deleting Export Reports or Administer Reports from the entire application.

Deleting the shared administration permission would affect app-admin-181 and app-owner-610, whose administration access remains justified.

Follow the actual operations under **Admin > Identity Management > Activities**. Check the source, account, permission, action and result for each one.

One successful operation does not establish that the other succeeded. A connection can also be authorized for one change but denied another; investigate the actual result instead of assuming that a passing connection test settles both.

The relationships we are following are:

```text
Production application requirement
  Four accounts, eight permission holdings
                   |
                   v
Correct source data and configured source owner
                   |
                   v
Inspect generated work and self-review separation
                   |
          +--------+---------+
          |                  |
          v                  v
Source owner reviews   Independent reviewer
six items for other    reviews two items for
people's accounts      the owner's account
          |                  |
          +--------+---------+
                   |
                   v
All eight decisions finalized
  Six approvals; two revokes
                   |
                   v
Follow the two specific account changes
  app-181: remove export
  app-182: remove administration
                   |
                   v
Verify target results and retained access
then check fresh ISC account information
```

The branches separate review responsibility. The later arrows connect final decisions with delivery and verification; they do not specify a private queue or a universal processing delay.

## Verify the removals and the access that must remain

Suppose both operation records report success.

A current application check confirms that app-181 lacks Export Reports and still has Read Reports. A separate check confirms that app-182 lacks Administer Reports and still has Read Reports.

Check the retained administration on app-admin-181 and app-owner-610 as well. A correction should not take away the separately justified access.

These observations establish the required account-level result. They do not establish that worker-181 has lost every possible capability across all of their accounts. That was not the stated requirement.

Obtain new account information through the supported aggregation process and inspect the resulting ISC account records.

The application observation and ISC's collected information have their own times. Opening an old account view does not make its data current. In this successful example, the updated ISC information agrees with the application results.

If one removed permission still appears in the application, keep that requirement open even if a task, operation or campaign shows a completed state.

Identify the exact account and remaining permission, the responsible operator and the evidence needed to establish completion. Repeating a review decision without finding the failed change would not explain the problem.

## Close the stated production review with evidence

Bring the original requirement, complete inventory, source selection, generated assignments, decision reasons, both sign-offs and current account results together.

You should be able to explain:

All four intended production accounts and eight items were reviewed. The owner's two items received independent review. Both required memberships were removed from the correct accounts. Reading remains where needed, and the two separately approved admin accounts retain their justified rights.

The **Campaign Composition Report** can help retain configuration evidence. Item and sign-off reports explain the review work. Operation records and application checks explain the actual changes.

None of those records can replace a different missing part of the result.

Keep the closure within its agreed boundary. Reporting Test was not included. This campaign does not establish that test access, another source for the application or every possible account type has been reviewed.

## What if another production account is discovered before launch?

Return to the preparation stage. A new application inventory check finds a fifth production account that exports reports every night. It was absent from the four-account list.

The account is used by an automated job.

An **application identity** can represent a program or service in ISC. A **machine account** is the system account that software uses. The human responsible for that account is not necessarily its personal user.

Does selecting Reporting Production prove that this account is already covered by the prepared eight-item review?

No. Check whether ISC collected the account, whether it is recognized as a machine account, which application identity it belongs to, and who is responsible for the program. Then establish which supported review route can assess its access.

Where available and configured, a machine-account certification can review access in the program's context. Inspect the actual supported work and assignment rather than assume the human-account campaign silently includes it.

Do not link the account to an arbitrary employee just to make it appear in that person's review.

The nightly export tells you something about use. Establish whether the job still has an approved purpose and which permissions it needs before deciding what should remain.

Account for that additional production relationship through the appropriate authorized review and follow-up. The original eight-item result can still describe the four human accounts, but it no longer establishes that the complete production inventory was covered.

The useful correction is a complete and justified account-to-review connection, followed by evidence of the required result.
