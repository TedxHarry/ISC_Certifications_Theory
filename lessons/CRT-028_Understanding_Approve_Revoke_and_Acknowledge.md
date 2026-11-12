# What do Approve, Revoke and Acknowledge actually mean?

A person still needs to read reports but no longer needs to download them. Their review shows View Reports and Export Reports as two separate items.

Approve View Reports and Revoke Export Reports sounds straightforward. But what have you changed when those decisions are saved? Has export already disappeared from the application? And why might another review offer Acknowledge instead of Revoke?

To answer those questions, start with the access being reviewed and the instruction each action records.

## Establish what the decision is about

SailPoint Identity Security Cloud, or **ISC**, keeps an **identity** representing a person and associates their application accounts with it. An **account** is the record through which someone accesses a particular system. Its permissions determine what they can do there.

For this example, identity 3901 owns account `rep-3901` in Reporting Production. ISC manages the collected account information through a **source**, its configuration representing that application or account-data collection.

The account has two **entitlements**, access rights represented from the source:

- **View Reports** permits reading reports in the application.
- **Export Reports** permits downloading reports from the application.

A **certification campaign** organizes access reviews. A **certification** is an assigned review within the campaign. Each **review item** is a unit on which the reviewer records a decision.

Here, each entitlement is an individual review item. The account information is current and correctly linked to identity 3901. Neither permission is included through a larger access package, required by an automatic assignment or supplied by another assignment in this example. The certification is active and unsigned, meaning it has not been finalized. A knowledgeable reviewer has the required permission to act and is reviewing somebody else's access.

The responsible business owner confirms that the person's current duty needs View Reports. Their earlier report-download duty has ended, and there is no continuing authorization for Export Reports.

We now have two access questions with different answers on the same account.

## Approve means accepting continued access to the reviewed item

The reviewer selects **Approve** for View Reports because the person still needs that permission for their authorized work.

The decision says that keeping this reviewed access is appropriate under the facts assessed. It concerns View Reports on `rep-3901`. It does not approve every other permission the person holds, or every permission another reporting account might have.

ISC records the choice against the review item. The business meaning is continued access to that item. The person already holds View Reports; this is a review of that existing access.

An access-request approval answers a different question: whether a requested access assignment should be granted through its request process. Approve in this certification is not a general instruction to add missing access.

Suppose the review lists View Reports, but current application evidence shows that `rep-3901` no longer has it. Selecting Approve does not establish that ISC has restored the permission. First resolve the difference between the review information and the account's current state. If access needs to be granted again, that requires the appropriate separately authorized access process.

Approval also does not freeze the account permanently. A later change of duties or another authorized control can change whether the access remains appropriate. The recorded decision describes this review, not every future business situation.

## Revoke records that the reviewed access should be removed

The reviewer selects **Revoke** for Export Reports because the person no longer needs to download reports.

That records a removal decision for this item. In our example, the intended result is specific: `rep-3901` should keep View Reports and lose Export Reports.

Notice the difference between the review record and the application account. The review record can show Revoke while the account still holds the permission. Selecting the action and changing the external system are separate work.

**Sign-off**, also called finalization, confirms the assigned review's decisions through the supported review process. A saved item decision is different from a finalized certification. **Remediation** is the work required to carry out a removal decision.

For removal to occur, the decision needs the applicable finalization and removal processing. The exact trigger and any supported removal date depend on the campaign experience and operation. Do not infer a completed application change from a saved choice or a signed-off review alone.

If the review offers a **revocation date**, that is a date specified for removal. Choosing a future date does not mean access has already been removed. You cannot set a revocation date for an individual entitlement through this review action, so check which choices the actual item supports.

Where ISC has the supported connection and permission to write the change, **provisioning** can carry the removal to the external account. Where a human must make the change, a manual task can be used. In either case, inspect the operation and the resulting access before reporting that the permission is gone.

For `rep-3901`, a useful final check would establish that report viewing remains available and report export has been removed from the correct account. Checking only that Export Reports disappeared from one screen would not establish that View Reports was preserved.

Revoke of an access item also does not mean “delete this person's account.” Removing a permission, disabling an account and deleting an account are different changes. Choose and verify the action that matches the actual requirement.

For these two items, the intended outcome is to keep viewing while removing export. Follow the decisions through the required review and removal work, then check the account.

```text
Account rep-3901 currently has:
  View Reports + Export Reports

Current authorized work needs:
  View Reports only
               |
               v
Review decisions
  View Reports   -> Approve: keep reviewed access
  Export Reports -> Revoke: remove reviewed access
               |
               v
Check required finalization and removal processing
  A saved choice is not a verified account change
               |
               v
Verify the intended account result
  View Reports remains
  Export Reports is removed

The decision concerns these items on rep-3901.
It is not an instruction to delete the account.
```

## The item can be a whole package

An **access profile** is a bundle of entitlements from one source. A **role** can group access profiles and direct entitlements from one or multiple sources.

If View Reports and Export Reports are instead included in one requested profile called Reporting Package, the profile can be the item presented for review. Its decision concerns that package. Opening it to inspect the two entitlements does not automatically create two independent entitlement decisions.

Approving Reporting Package therefore requires a justification for the reviewed package, including its export capability. Revoking the package is broader than a decision aimed only at Export Reports. Check the contents and the continuing need before choosing that broader action.

If only part of a package remains justified, work with the responsible access owner to establish a supported correction or a separately authorized narrower arrangement. An **access owner** is the person responsible for the access object. That responsibility and permission to change its configuration are separate, so involve an authorized operator where needed.

A role decision in a review of a person's access concerns that person's role assignment. It does not, by itself, rewrite the role for every other person who holds it. A requested role may also provide access across several applications, so understand the whole assignment before deciding to remove it.

Other assignments can affect the access that ultimately remains. Before predicting every permission that will disappear, inspect those assignments and the supported removal behavior. A decision on one package is not proof that all ways of obtaining the same permission have been removed.

## Why an automatically assigned role uses Acknowledge

Now consider a role called Warehouse Handler. It contains a Warehouse View access profile with two entitlements: View Stock permits reading stock quantities, and Record Receipt permits recording stock received into the warehouse.

The role is assigned by a configured membership condition:

`workFunction equals WarehouseHandling`

Here, **workFunction** is an identity attribute, a named piece of information about the person. **WarehouseHandling** is the value the condition checks. These are example organization-defined data, not mandatory built-in ISC fields.

During **identity processing**, ISC evaluates identity information and the relevant access requirements. If the identity meets this role's condition, the rule governs that role assignment and its access. The person's role membership is controlled by that requirement.

For a role assigned through automated membership criteria, the certification action is **Acknowledge**. It records that the reviewer has examined this automatically controlled access. It does not request removal of the role or override the condition that assigns it.

The reason is the continuing assignment rule. A review action that merely removed a permission would not correct the rule saying the person should receive that access. You need to establish whether the person should still meet the condition and whether the role provides the right access to everyone who meets it.

Acknowledge is therefore not another name for approving a request, and it is not a removal instruction. It also does not make an inappropriate rule or inaccurate identity value correct.

If Warehouse Handler is wrong for a person, investigate what is wrong:

- The person no longer performs warehouse handling, but their workFunction still says WarehouseHandling. The identity information needs an authorized correction.
- The identity information is accurate, but the rule includes people who should not receive the role. The membership requirement needs investigation.
- The right people receive the role, but one of its permissions is too broad. The role's access contents need investigation.

These are different problems. Changing accurate person information to avoid an overbroad role would hide the actual configuration problem. Changing a shared role to solve one person's incorrect data could affect other people whose access is appropriate.

The **role owner** is responsible for the role. Work with that owner and the authorized people maintaining identity data or role configuration to establish the right correction. Record and raise a known mismatch rather than treat Acknowledge as evidence that the mismatch has been resolved.

After a correction, the applicable identity processing and access-change work still need to occur. Inspect the resulting role assignment and the relevant account permissions. Acknowledge itself does not perform that correction.

## The origin matters as much as the role's name

**Assignment origin** means how the person received the access. A role called Warehouse Handler could be assigned to one person through a request and to another through membership criteria.

The requested role assignment can be approved or revoked in certification. The criteria-assigned role can only be acknowledged. The readable role name alone cannot tell you which action should be available for the reviewed assignment.

Access profiles also have different origins. Requested profiles and profiles detected from the person's existing entitlements can be certified. A profile supplied through a role is included within that role's review rather than offered as a separate profile decision. An entitlement included in the person's profiles or roles is likewise not an independent entitlement decision that bypasses the package.

A **lifecycle state** is a configured stage in the person's relationship with the organization, such as active employment. Access profiles included in the person's assigned lifecycle state do not appear as individual certification items. Their absence from a list does not establish that the account has no such access.

Use the actual item, assignment and campaign type to interpret the action. The comparison below concerns reviews of a person's access; it is not a promise that every screen presents the same controls.

| Reviewed access | Action and meaning | What it does not establish |
|---|---|---|
| Individually reviewable entitlement | Approve accepts continued access; Revoke records a removal decision. | That unrelated account permissions were reviewed or that removal is complete. |
| Requested or detected access profile | Approve or Revoke concerns the reviewed profile. | A decision on only the component whose details you opened. |
| Requested role assignment | Approve or Revoke concerns that person's reviewed role assignment. | A shared role-definition change for everyone. |
| Role assigned through membership criteria | Acknowledge records the review of automatically controlled access. | Removal of the role, an override of its criteria or resolution of a known mismatch. |

There is a separate kind of review called **role composition**, which examines the role itself: its membership criteria, description and included access. It currently uses the legacy certification experience. “Legacy” identifies that older experience; check the actual campaign type rather than assuming it behaves like a person's role-assignment review.

In a role-composition review, a removal decision requires an explanation of why and how the role should change. The change is carried out through a manual task; inspect its assignment to establish who must do that work. That is different from automatically removing one person's assignment. The reviewed object changes what the decision is asking someone to do.

## Separate the choice, the review state and the account result

When inspecting a decision, identify three things in order: which item was decided, whether the assigned review was finalized, and what change actually reached the application if removal was required.

A report showing Revoke answers a decision question. A finalization record answers a review-state question. An operation result and current account evidence help answer the removal question. One record may be useful evidence without proving all three.

For example, keeping View Reports and removing Export Reports matches the supplied reporting task. If export removal later fails, the recorded Revoke remains a removal decision; it is not proof of successful delivery. Investigate the failed change and the current account state.

An item is **undecided** when no decision has been recorded for it. A reviewer may have opened it and still need information before deciding. An unsigned review may contain saved decisions but has not been finalized. Neither state is the same as Acknowledge.

Acknowledge is not a general “I don't know” option for an entitlement. If you cannot establish whether access is justified, seek the necessary clarification through the campaign's process. Leaving an item alone does not record a deliberate review decision.

## Try the decision on supplier access

Identity 4001 owns account `sup-4001` in Supplier Production. The current review item is a requested access profile called Supplier Review. It includes:

- **View Suppliers**, permission to read supplier records.
- **Change Supplier Bank Details**, permission to edit the bank information used for supplier payments.

The application's capabilities and current account information have been confirmed. The profile is eligible for review, the identity/account association is correct, and no other assignment or automatic requirement supplies these rights. An authorized non-self reviewer has confirmed that the person's current work needs supplier viewing but does not authorize bank-detail changes. The certification is active and unsigned.

Someone proposes: “Revoke Supplier Review. That will remove only the bank-edit permission and delete the account immediately.”

Which parts of that explanation need correction?

The selected item is the whole profile. Its scope includes View Suppliers as well as Change Supplier Bank Details. The profile decision cannot be described as a bank-edit-only decision. Removing the whole package also puts the required viewing capability in scope, so establish the supported narrower access arrangement before treating the proposed change as the intended solution.

Revoke records the removal decision. It does not establish immediate account deletion or completed permission removal. Check finalization and the applicable removal work, then verify that the correct account can still view suppliers and cannot change their bank details. A separate replacement profile would need its own authorization and assignment; the certification does not automatically create it.

Now change the origin. Supplier Review is included in a role assigned through membership criteria, and that automatically assigned role is the item presented for review. Someone chooses Acknowledge and reports that bank editing has been removed.

Acknowledge does not support that report. The criteria still govern the role assignment, and the action did not request removal of the bank-edit permission. Establish whether the person's information, the membership condition or the shared role's access needs correction. Coordinate the authorized change without losing required supplier viewing, then inspect the actual resulting assignment and account permissions.

The action label tells you what the review recorded. The item and its origin tell you what that action applies to. The account evidence tells you whether the required access outcome was achieved.
