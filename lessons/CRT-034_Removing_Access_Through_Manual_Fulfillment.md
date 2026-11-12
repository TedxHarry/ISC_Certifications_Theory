# What happens when access must be removed manually?

ISC can record that access should be removed even when it cannot make the change directly in the application.

In that situation, a person must make the change. ISC assigns the work so somebody can receive it, understand it and record its completion.

The important connection is between the work record and the application account. Closing the record tells ISC that somebody has reported the work complete. We still need to establish what actually changed.

## Follow one permission that is no longer needed

SailPoint Identity Security Cloud, or **ISC**, keeps an **identity** representing a person. An **account** is that person's record in an application. The account's permissions determine what the person can do there.

Identity 5301 owns account `arc-5301` in Document Archive Production. The account has two **entitlements**, rights represented in ISC from the application:

- **Read Archive** permits reading archived records.
- **Export Archive**, identified by `ARCH_EXPORT`, permits exporting archived records in bulk.

The current job still needs reading, but bulk export is no longer authorized. The intended change is to remove Export Archive while keeping Read Archive and the account.

A **certification campaign** organizes access reviews. Within it, a **certification** is an assigned review. Here, the permissions appear as separate review items. The reviewer understands the access, has permission to review it and is reviewing somebody else's account. Approve for Read Archive accepts continued reading. Revoke for Export Archive records the decision to remove bulk export.

The account information is current and associated with the correct person. Neither permission comes through a bundle or an automatic assignment, and no other assignment requires Export Archive to remain.

The review has been signed off, meaning its decisions are finalized. The required removal is due, and we have checked that its manual work was generated. We are following that actual work, rather than assuming that a saved Revoke has already changed the account.

## Why does ISC create a task?

A **source** is ISC's configuration for a system or collection of account information. The Document Archive Production source receives account information through a file.

This is a **flat-file source**: ISC imports account data from a supplied file instead of reading it through a direct application connection. A **CSV**, or comma-separated values file, is a text file containing rows and named columns of data.

Reading that file tells ISC which accounts and permissions were reported. It does not give ISC a way to change the archive application's account.

**Provisioning** means carrying out changes to accounts or access in another system. **Remediation**, in this review, means carrying out the required removal. Where ISC cannot write that removal directly, the work can be assigned as a **manual fulfillment task**.

A task is an instruction to a person. It identifies work that must happen outside ISC. Creating the task does not itself remove `ARCH_EXPORT` from `arc-5301`.

A direct-connected source can also be configured to use manual work when its ability to provision changes is disabled. However, a failed automatic attempt is not enough to prove that a manual task now exists. Find the actual work and its assignment before relying on it.

## Check who has received the work

The reviewer decides whether the access should remain. The person carrying out the removal needs to make the application change. Those responsibilities can belong to different people.

In ISC, the **source owner** is the recorded person responsible for the source. An **entitlement owner** is responsible for a particular access right. These ownership records can matter to task routing, but an ownership title alone does not show who received this particular task.

Open the task and inspect its actual assignment. If a group is involved, establish who is taking responsibility for completing it. A group name alone does not show that somebody has made the change.

For our example, task `T-34` is assigned to the recorded source owner. We have checked that assignment. We also know that this person has permission in the archive application to remove Export Archive from `arc-5301`.

Those are two separate facts. Receiving a task in ISC does not grant administrative permission inside the application.

The assigned user can open **Task Manager**, the area for work they need to perform in external systems. A notification can point them toward the task, but the task details are what they should inspect.

An authorized administrator can also inspect manual provisioning work in the Tasks view under Admin > Dashboard > Tasks. This gives the administrator a way to track responsibility and progress; it does not replace the application change.

## Read the instruction before making the change

For `T-34`, establish the source, account and permission:

Document Archive Production, `arc-5301`, Export Archive with value `ARCH_EXPORT`.

Then establish the requested action: remove that permission from that account.

The identity tells us whose access is involved. The account tells us where the change must happen. The entitlement identifies what must be removed. Similar account names in another environment, or another account owned by the same person, are different targets.

A removal task can contain more than one listed entitlement. Read the complete instruction before treating the task as finished.

The task is not a new request to decide whether export is useful. That decision has already been finalized. If the instruction conflicts with current facts or cannot be carried out, raise the specific issue through the responsible process instead of silently replacing the decision or claiming completion.

Now the assigned, authorized person opens the archive application's account-management interface, locates `arc-5301` and removes its Export Archive permission. The exact application screen depends on that application.

Suppose a current account check then shows that `ARCH_EXPORT` is absent and Read Archive remains. That result fits the requirement: bulk export was removed while justified reading was preserved.

Removing one permission does not call for deleting the account, disabling all access or deleting the permission's definition for every user.

## Bring the changed account information back into ISC

The application has changed. ISC's previously imported account information may still show the earlier permissions.

**Account aggregation** brings account information into ISC. For a flat-file source, this happens through a file import.

The file should truthfully describe the account after the application change. In our example, the updated information for `arc-5301` should show its retained reading permission and the absence of `ARCH_EXPORT`.

This is where the direction of the data matters. Removing export inside the archive application changes access. Importing the account file tells ISC what access the file reports.

Editing a CSV to omit export while leaving it in the application does not remove that access. It gives ISC an inaccurate account record.

Use the file format and account identifiers expected by that source. Its **account schema** describes the fields and how they are interpreted. Check the required file scope as well; do not assume that a file containing only one edited row is safe for every source.

When account-deletion processing is enabled, an account missing from the imported data can have its record removed from ISC. The actual application account could still exist. Deleting a row is not a substitute for recording the permission change on an account that should remain.

In the documented file-based Task Manager flow, uploading the updated CSV starts aggregation. Starting the import and successfully updating the intended account are different results. Check the import outcome and the account information that ISC now holds.

For this example, suppose the updated application data is imported successfully. ISC now shows Read Archive on `arc-5301` and no longer lists `ARCH_EXPORT`. We can connect that information to the actual application change, rather than infer the change from a file alone.

## Record what has actually been completed

**Mark Complete** records completion of the manual task. It should reflect work that has actually been carried out.

In the normal example, the correct permission was removed in the application, the account check confirmed the intended result and updated account information was brought into ISC. The task can now be recorded as complete through its supported action.

The review decision, task completion and account information answer different questions:

| Record or observation | What you learn |
|---|---|
| Finalized Revoke decision | Which reviewed access should be removed. |
| Completed manual task | The assigned work has been recorded as complete. |
| Current application account | Which permissions the account now holds. |
| Later imported account information | What the supplied data has told ISC about that account. |

Keep the times as well as the account and permission. A task closed today and a file exported before the change describe different moments.

The documented file-based Task Manager procedure also describes an early-completion condition: if the task is marked complete before aggregation runs, the source owner has 24 hours to update the CSV and trigger aggregation. Otherwise, a second manual work item is created.

That is a condition of the described task/file process, not a universal campaign deadline or a guarantee for every manual integration. Follow the completion requirements of the actual source and task.

If another task appears, check its account, permissions and the previous change/import evidence before repeating application work. The application might already be correct while ISC still has older data.

Here is the normal path we followed. The arrows connect the required work, human action and later evidence; they do not mean that closing a task performs the application change.

```text
Finalized, due removal
  Document Archive Production / arc-5301 / ARCH_EXPORT
                          |
                          v
ISC creates and assigns manual work
  Inspect actual task, recipient and required change
                          |
                          v
Authorized person changes the application account
  Export Archive removed; Read Archive retained
                          |
                          v
Bring back truthful, updated account information
  File-based path: upload and check aggregation result
                          |
                          v
Record completion of the required work
  Check task, current account and later report together
```

## What if the assigned person cannot finish?

First establish why. Is the account unclear, does the task name the wrong permission, is the person unavailable, or do they lack permission to make the change?

A manual task can be reassigned through its supported **Reassign** action. Explain the handover, select an appropriate recipient and verify who now holds the work. The new recipient still needs the knowledge and application permission to perform it.

This is **manual task reassignment**. It transfers responsibility for the removal work. Reassigning a certification transfers review work instead. Changing one does not, by itself, establish that the other was transferred.

If only part of the task was carried out, record that situation accurately and arrange authorized follow-up. Suppose a task lists two removals and only one succeeds. The account is only partly changed; closing the whole task would hide the remaining work.

If a task was already closed incorrectly, establish the discrepancy and use the supported correction or follow-up process. Do not assume that every source has a Reopen button, that another task will always appear automatically or that the original removal decision must be made again.

## Check completion reports in the context of the delivery path

The Campaign Remediation Status Report helps track revoked access. In its Status field, Finished can follow closure of a manual task or a service-desk ticket, as well as removal through a connected source.

A **service-desk ticket** is a work record in a service-management system. If an integration uses one, inspect the actual ticket and its completion evidence. A closed ticket is not, on its own, a current observation of the application account.

The report's completion time can therefore tell you when work was marked complete. It does not always mean that ISC directly observed the application's permission at that moment.

Generate the report again when you need updated campaign information. Then connect the row to the right account, permission and work record. If the task says complete but the application still has export, investigate that disagreement rather than explain it away with the Finished label.

Likewise, removing an account record from ISC is not evidence that the real account lost its permission. An account removed only from ISC can return at the next collection while it still exists in the application.

## Try a task that was only partly completed

Account `fin-5401` in Finance Production has three individually reviewed permissions:

- **Read Invoices** permits reading invoice records.
- **Export Invoices**, identified by `INV_EXPORT`, permits exporting invoice records.
- **Release Payments**, identified by `PAY_RELEASE`, permits authorizing payment release.

Current work justifies reading only. A permitted reviewer who is not reviewing their own account finalizes Revoke for both export and payment release. Current data and the person/account association are correct, and no bundle, automatic assignment or other requirement supplies those two rights.

One actual manual task lists both removals. The assigned operator removes `INV_EXPORT` but receives a permission-denied response when trying to remove `PAY_RELEASE`. A current application check confirms that reading and payment release remain.

The operator nevertheless marks the task complete. A later remediation report says Finished.

Has the required removal been completed?

Only the export part has been completed. The payment-release permission still exists on the correct account. The task and report do not turn that partial result into success.

Arrange the remaining change through a person and process authorized to carry it out, keep the work records accurate and verify the resulting account. Preserve Read Invoices and the account. Do not delete them to make the task look complete or infer that the operator automatically gained the missing permission.

Now suppose somebody edits the account CSV to omit `PAY_RELEASE`, imports it and points to ISC's updated account view. The application still holds payment release.

The file has reported a state that does not match the account. Importing it has not carried out the missing removal. Correct the application access through the authorized process and bring back truthful data.

Finally, suppose payment release is later removed correctly, but somebody imports a file exported before that removal. Payment release appears again in ISC.

That older file does not establish that the application granted payment release again. Check the current account and the file's time and contents. The remaining issue may be the account information supplied to ISC rather than another application change.

For manual removal, follow both the person doing the work and the evidence coming back. The task assigns and records the work; the application account is where the required permission must change.

