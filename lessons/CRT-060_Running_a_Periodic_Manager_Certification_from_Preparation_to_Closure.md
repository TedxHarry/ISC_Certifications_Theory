# Run a periodic manager certification from preparation to closure

The request is: “Run this quarter's Finance access review. Ask managers whether their employees still need their access, remove what is no longer justified, and keep the access needed for their work.”

Where would you begin?

Before opening the campaign screen, make that request specific enough to check. Which people are included? Which accounts and permissions must be reviewed? Who will explain unfamiliar access? Who can carry out a removal?

Those answers let you follow the work from a business request to a result you can defend.

## Turn the request into a reviewable requirement

A **periodic review** repeats at an agreed interval. Quarterly is the interval for this request. It does not mean that starting one campaign automatically schedules every later quarter.

In SailPoint Identity Security Cloud, or **ISC**, an **identity** is a record representing a person or another managed subject. Here, we are reviewing employee identities. An **account** is their record in an application, and its permissions determine what they can do there.

A **source** is ISC's configuration for a system or its account information. The application itself holds the actual account and enforces its permissions.

For this review, the business owner, the person accountable for the work requirement, confirms:

- Include the employees in Finance at the agreed review cutoff.
- Review their certifiable access, meaning the access ISC can present for certification decisions, including the relevant production accounts.
- Keep access supported by current work and remove access whose approved purpose has ended.
- Verify any removal on the correct account while preserving access still needed.

The cutoff is the agreed point for deciding who belongs in this cycle. Keep it with the requirement. Otherwise, two people can compare lists from different days and disagree about who is missing.

A **certification campaign** organizes the review work. A **certification** is an assigned review within that campaign. A **review item** is the access entry presented for a decision.

Our checked example has two Finance employees, staff-71 and staff-72. They have the same current manager, M-61. These labels identify the records we will follow.

The complete account inventory for this example is:

| Employee | Source and account | Existing access to review |
|---|---|---|
| staff-71 | Reporting Production, rep-71 | Read Reports and Export Reports |
| staff-71 | Archive Production, arc-71 | Read Archive and Export Archive |
| staff-72 | Reporting Production, rep-72 | Read Reports and Export Reports |

Reading allows viewing the relevant records. Export allows downloading copies. The application owners have confirmed those meanings.

Each permission is represented as an **entitlement** in ISC. All six are individually reviewable here. None is included through a larger access package or required by an automatic assignment.

We therefore expect two people, three accounts and six access decisions. Those are different things to count.

This inventory covers the agreed scope in our example. In a real review, obtain that list from the responsible people and application evidence. Do not use the campaign's first results as the only proof of what it should have included.

## Check the information the campaign will use

The manager can judge current work, but ISC first needs to connect the right person, account and manager.

**Account aggregation** collects account information from a source into ISC. Compare the collected accounts and permissions with the application inventory. Keep their collection dates so you know which observations you are comparing.

**Account correlation** associates an application account with its owning identity. Confirm that rep-71 and arc-71 belong to staff-71, and rep-72 belongs to staff-72.

Then inspect each employee's manager relationship. **Manager correlation** establishes the connection between an employee identity and the manager identity using the configured information.

These are separate checks. The reporting account can belong to the correct employee while that employee still points to a previous manager.

For our normal review, both employee identities show M-61 as the verified current manager. Their department values correctly show Finance. Their account information is current enough for this review.

The administrator also checks **Admin > Global > Reports**, using the **Identities Without Managers** report to investigate any intended employee missing a manager relationship.

This matters for the dedicated manager-campaign route: identities without a manager are excluded. A clean-looking preview could therefore omit a required person.

Resolve a genuine missing relationship through the responsible data process and inspect the resulting identity link. Do not assign an arbitrary manager to make a count agree. If the business needs a different reviewer arrangement, choose a supported review design deliberately.

The manager M-61 is permitted to review this work and understands the employees' duties. Their own access is outside this example's selected population. We are not asking them to approve their own permissions.

## Decide how the people will be selected

Selecting Manager Campaign determines the review approach. It does not, on its own, express “Finance only.”

We use a **campaign filter**, a configured condition controlling which review content is included.

For this example, the employee identity's department attribute is available for filtering. An **attribute** is a named piece of information; department is the field and Finance is its value.

An authorized administrator opens **Search > Certification Campaigns**, selects **View previewed/Active**, then **Campaign Filters > Create Filter**.

Give the filter a name and description explaining the intended Finance population. In **Builder**, choose **Inclusion** and add an **Identity Attribute** condition: the configured department attribute, **Equals**, Finance. Select **Create Filter** to save it.

The condition selects people according to their identity information. It does not ask whether an entitlement's name contains Finance.

Our filter has one condition. Adding unrelated conditions could change who enters the review, so we leave them out. We will still compare the generated work with the two-person, three-account inventory.

If a suitable filter already exists, inspect its actual saved condition before reusing it. Its name is not proof that it still implements this quarter's requirement.

## Prepare the campaign and its working rules

The administrator needs the appropriate certification-management permission. Being someone's manager does not automatically give them authority to configure the campaign or its source connections.

Open **Admin > Certifications > Campaigns > Create New** and select **Manager Campaign**.

Confirm that this route is supported in the environment being used. Other creation routes can have different controls and missing-manager handling.

Enter a name identifying Finance and this quarter. Use the description to state the cutoff, intended population and purpose. Someone reading the campaign later should be able to distinguish it from the previous quarter's instance.

Set a deadline that allows the managers to investigate access and finish their reviews. Also agree who will follow removal work and how unresolved questions will be handed over.

Attach the checked Finance inclusion filter.

Leave the configured reviewer emails enabled for this example. Notifications help people find and finish work; they do not establish that the correct person received the actual review. Disabling those emails would not be a way to correct an assignment.

Set the required decision comments. Here, a removal decision must explain why the access is no longer needed. The manager will also record useful reasons for retained sensitive access.

Choose the agreed treatment of undecided access. Our policy maintains never-decided access at administrative completion and keeps the unresolved business question visible for follow-up.

That setting is an unfinished-work policy. It is not a reason to skip the review or claim that an unexamined permission was justified. In our normal path, all six decisions will be finalized before the deadline, so this policy does not supply any of them.

## Inspect the preview before starting

Select **Preview Campaign**. **Generation** creates the review work using the campaign settings and the information available to it.

The **preview** is that prepared work before the administrator starts it for reviewers.

Open the generated campaign and compare the actual contents with the inventory:

Are staff-71 and staff-72 both present? Are rep-71, arc-71 and rep-72 the correct production accounts? Are all six intended items included? Is the work assigned to M-61?

Check the access relationships, not just the total. Six items could still contain a test account in place of arc-71.

In our supplied preview, M-61 has an assigned certification containing both employees and the six intended items. This is the inspected result for the example, rather than a rule that every campaign groups reviews in exactly that way.

Check the deadline, filter, comment and notification settings as well. A **Campaign Composition Report** can help retain the campaign's configuration evidence. It does not replace the account-by-account coverage comparison.

A generated preview describes information at generation time. Adding a manager or changing department data later does not establish that this existing work was rebuilt.

For this dedicated route, plan to start within a day of generating the preview. If it has become stale, establish the current requirement and supported replacement process before relying on it.

Once the checks pass, the administrator selects **Start Campaign**. Confirm that the campaign has started and that M-61 can open the intended work. A generated preview alone did not start it.

## Help the manager make explainable decisions

M-61 opens **Certifications > Active** and selects the assigned review. In **Identities**, choose the employee, then open an access item's details. Check its source and actual account before assessing what the employee should keep.

Begin with the account and capability. Then connect that capability to the person's current authorized work.

For staff-71, the manager confirms that the ongoing reporting duty requires both reading reports and downloading copies through rep-71. That supports keeping both reporting permissions.

The same employee still needs to view archive records through arc-71. However, exporting archive copies supported a temporary project that has ended. The responsible business contact confirms there is no continuing approved need for that export.

For staff-72, viewing reports remains part of the current job. Export Reports supported a former duty, and that duty has ended without another approved export requirement.

The choices now have reasons:

- Approve both permissions on rep-71.
- Approve Read Archive and revoke Export Archive on arc-71.
- Approve Read Reports and revoke Export Reports on rep-72.

**Approve** accepts keeping the reviewed access. **Revoke** records that it should be removed.

There are four approvals and two revokes. Every choice concerns an identified account and permission. A Finance department label alone would not justify all six.

For arc-71, a useful removal comment explains that archive export was needed for the completed project, has no continuing approved purpose, and archive viewing must remain.

If the manager cannot explain a permission, the application or access owner should establish what it actually allows. The administrator helps obtain that information; completing rows on the manager's behalf would not supply the missing business judgment.

## Follow the review while it is open

During the review, the administrator checks the actual assigned work and remaining items.

A **Campaign Status Report** can show item choices and the recorded decision maker. Generate it again when later changes need to be reflected; opening an older downloaded file does not update its contents.

In our example, the manager first saves the six choices but has not yet finished the review.

At that checkpoint, six recorded choices do not establish **sign-off**, the manager's final confirmation.

Ask the manager to check their choices and complete the review through **Finish**, including any required confirmation. Then inspect the finalization evidence. A **Certification Sign Off Report** supplies sign-off information; the item-choice count answers a different question.

When all reviewers finish and sign off by the deadline, the documented normal path moves the campaign to **Completed**. All required review work is finalized in time here; inspect the resulting campaign state. Do not use an administrator's bulk unfinished-work action merely to make a dashboard look complete.

If someone is absent or a material question remains unanswered, identify that actual problem and follow the permitted reassignment or unresolved-work process. A reminder cannot supply an absent person's judgment.

## Carry the two removals into their applications

The final review decisions establish what should change. **Remediation** is the work to carry out the required removal.

A **connector** is the integration used to read or change source information. **Provisioning** is work that changes application accounts or access through a supported connection.

Reporting Production has a configured, enabled removal operation. Its integration credentials are permitted to remove Export Reports from rep-72.

Follow the actual account-change activity under **Admin > Identity Management > Activities**. Inspect the source, account, permission, operation and result. A successful read connection would not establish permission for this change.

Archive Production uses an account-data file. Importing that file tells ISC about access; it cannot remove Export Archive from the application.

The supported manual-removal path creates a work item telling the responsible person what needs changing outside ISC. In our example, the removal is due and the actual task is available in **Task Manager**, assigned to an authorized archive operator. Check that task's target and instructions rather than assume that the manager must perform it.

The operator removes Export Archive from arc-71 in the archive application and records the work. Read Archive must remain.

These two paths connect to the same required outcome:

```text
Agreed Finance review requirement
  People, accounts, permissions and cutoff
                   |
                   v
Checked data, manager links and filter
                   |
                   v
Generated preview checked against the requirement
                   |
                   v
Administrator starts the campaign
                   |
                   v
Manager records and finalizes six decisions
                   |
          +--------+---------+
          |                  |
          v                  v
Reporting removal      Archive removal
Supported connector    Assigned human operator
rep-72: remove export  arc-71: remove export
          |                  |
          +--------+---------+
                   |
                   v
Check actual accounts and fresh ISC information
  Both exports absent; needed reading remains
```

The arrows connect responsibilities and evidence. They do not promise one universal delay between sign-off and delivery.

## Verify the result before reporting closure

Suppose the reporting operation reports success and the archive task is closed. We still need to establish the actual account results.

A current Reporting Production check confirms that rep-72 lacks Export Reports and retains Read Reports.

A current Archive Production check confirms that arc-71 lacks Export Archive and retains Read Archive.

Also confirm that rep-71 keeps its two justified reporting permissions. A removal process should not silently take away access the manager approved.

Next obtain fresh account information in ISC. Aggregate the changed reporting account through the supported source process. For Archive Production, obtain an accurate new account-data file reflecting the application changes and import it.

Check the resulting account records. A file prepared before the archive change could still show export. Editing a file to hide export without changing the application would establish only a misleading ISC record.

In this successful example, the updated ISC data agrees with both applications.

You can now explain the closure:

The intended people and six items were included. The manager justified and finalized all six choices. Both required exports were removed from the correct accounts. The required reading remains, and the collected data agrees.

Keep the requirement and inventory, campaign reference, coverage checks, decision reasons, finalization evidence and account results together. Campaign reports can support that history; they cannot supply an application observation they never made.

The campaign's completed status and the business outcome need their own checks. Report the review as completed in the platform only when that state is established. Report the removal requirement as met only when its evidence is established.

If either export remains, record which account still holds it, who owns the follow-up and what check will establish completion. Do not describe the whole business task as finished merely because the review is signed.

## Prepare the next quarter from current facts

The next review needs a new check of the people, accounts, managers and permissions. Reuse sound configuration after checking it; do not copy this quarter's six-item result as next quarter's expected population. Prepare a new campaign from the rechecked instructions. The old campaign remains evidence of its own review cycle.

Carry unresolved issues forward explicitly. If the archive removal had remained open, the next campaign would not erase that earlier obligation.

The useful repeat is the process of establishing current need and verifying the result. The old approvals are evidence of an earlier decision, not permanent authorization.

## What changes when the requirement changes before launch?

A third employee joins Finance after this preview was generated. Before launch, the business owner extends the approved scope to include that employee.

Their reporting access is held through a requested **access profile**, a bundle of entitlements from one source. It contains reading and export. Reading is needed; export is not justified.

Would you start the old six-item campaign and ask the manager to remove only the export entitlement?

First account for the changed population. The original preview has not established coverage of the added employee. Check their data, accounts and manager, then use the supported campaign-preparation process and inspect the resulting work. Updating a department value alone does not prove the old preview now includes them.

Then inspect the actual decision unit. Where reading and export are contained in the person's profile, the independently presented item can be the profile rather than separate entitlement rows.

The manager must understand both capabilities. Establish an authorized arrangement that preserves needed reading, and how the broader profile should be handled. Do not promise that Revoke on a package removes only its unwanted component or automatically grants a narrower replacement.

The changed case needs both a coverage correction and an access-arrangement decision. Correcting one would leave the other unanswered.
