# When is a manager review the right choice?

A person still needs to read reports, but no longer approves invoices. Their manager knows that the invoice-approval responsibility moved to another team.

That knowledge is useful in an access review. It connects the person's current work with the permissions they should keep.

But sending a review to someone labelled Manager does not establish that the right person received it, that all intended access was included or that the permission descriptions are understandable.

Let's connect the business reason for a manager review with the information the system needs to make it work.

## Use a manager review for a question about current work

A **manager review** asks the manager to assess whether access remains appropriate for the people whose work they supervise.

It fits questions such as: does this person still need invoice approval, report access or case-management access for their present responsibilities?

The manager can know which duties changed, whether a project ended and which tasks the person is still expected to perform.

That does not mean the manager knows what every technical permission allows. Someone may recognize the person's work but not understand an item called FIN_GRP_42.

The person responsible for that access or application needs to provide a reliable explanation of the capability. The manager then connects that capability with the person's current need.

If the question is instead “What does this application group permit across all accounts?”, application or source expertise is central. A manager's knowledge of one employee does not establish the group's technical design.

Choose who can answer the actual review question, then check that the relevant information reaches them.

## Establish whose access is being reviewed

An **account** is a record used to access an application or system. Its **access** determines what someone using it can do.

SailPoint Identity Security Cloud (**ISC**) keeps an **identity** representing the person and links it with their accounts. A **source** is the configuration in ISC for the system or collection of account data being managed.

An **entitlement** represents an access right from a source.

For this example, worker-214 has a reporting account with reports-view, which permits viewing reports. Their payments account has invoice-approve, which permits approving invoices.

Both application accounts are correctly linked to worker-214's identity. The permissions are already held, and their meanings have been confirmed.

A **certification campaign** organizes access reviews. A **certification** is an assigned review within it. Its **reviewer** assesses the **review items**, the access presented for decisions.

The campaign includes worker-214 and these two individually reviewable entitlements. Neither permission is included through another package or required by an automatic assignment in this example.

Now we need to establish who should receive that review.

## A manager relationship links two identities

A **manager relationship** records which identity is the manager of another identity.

For worker-214, the intended manager is the person represented by manager-840. These are two distinct identities.

The relationship tells ISC who the employee's manager is. It does not describe who owns the reporting application or who created the campaign.

**Account correlation** links an application account to the identity that owns it. **Manager correlation** establishes the employee-to-manager relationship by matching the configured manager reference to information on the manager's identity.

These comparisons have different jobs. Correctly linking the payments account to worker-214 does not establish that worker-214 is linked to the right manager.

## Follow the manager reference from its source

An **attribute** is a named piece of information on a record. Here, the personnel source account for worker-214 has an attribute called manager with the value 840.

That value is a reference to the manager. It is not worker-214's own employee number.

An **identity profile** contains settings for establishing and maintaining identity information from source data. In this example, its Manager Name mapping uses the personnel account's manager attribute.

The source's manager-correlation configuration supplies the other part: compare that account value with the identificationNumber attribute on possible manager identities.

The manager-840 identity already exists in ISC and has identificationNumber 840. The configured comparison uniquely identifies that manager, so the resulting relationship links worker-214 to manager-840.

The field names are illustrative for this configuration. The Manager Name label does not require the source value to be a person's readable name. A number can identify the manager when that is what the matching configuration expects.

Both configurations matter: which source information supplies the reference, and which manager-identity attribute it should match.

**Account aggregation** collects source account information into ISC. **Identity processing** evaluates identity information and relevant configuration. After the appropriate processing, inspect the actual manager relationship on the employee's identity rather than assuming a nonblank source field proves the link.

## Let the campaign use the relationship

Selecting Manager as the reviewer tells the supported campaign to use the manager relationships for the selected identities.

It does not, by itself, select every person in the organization or every account in an application. People and access selection still determine what the campaign contains.

For worker-214, the campaign selects the intended person and the two permissions. The resolved manager relationship is manager-840, and the generated certification is actually assigned to manager-840.

The manager is authorized to review that work, the review is open and there is no self-review conflict in this example.

Here is the connection:

```text
Employee's source manager value
              |
              v
Mapped manager reference
              |
              v
Match existing manager identity
              |
              v
Resolved manager relationship
              |
              v
Campaign reviewer rule
              |
              v
Actual assigned certification
```

The arrows show the information needed for this assignment. They do not promise a fixed schedule of internal jobs or that every later data change immediately changes an existing review.

Check the source reference, resolved relationship and actual assignment as separate facts.

## Give the manager enough information to decide

Here, manager-840 knows that worker-214 still prepares reports but no longer approves invoices. The access descriptions establish what reports-view and invoice-approve actually permit.

Those facts support different judgments for the two items.

**Approve** accepts keeping the reviewed access. **Revoke** records that the reviewed access should be removed.

The current reporting responsibility can justify keeping reports-view. The confirmed end of invoice-approval responsibility can justify removing invoice-approve.

The decision must still follow the required review confirmation and change process. Selecting Revoke is not evidence that the payments account has already lost invoice approval.

Being the manager also does not give manager-840 permission to edit source integrations or administer every campaign in ISC. Review responsibility and platform administration authority are separate.

If the manager cannot understand an item, obtain the missing capability information. A department label or a previous approval cannot substitute for that understanding.

## Keep package and automatic-access rules in view

An **access profile** is a bundle of entitlements from one source. A **role** can group profiles, direct entitlements or both, across sources.

A manager can receive a package as the review item. The decision then concerns that package, not only the permission that first attracted attention.

If the person still needs part of it, establish how the required access will be preserved before treating removal of the whole package as the intended outcome.

Some roles are assigned automatically through **membership criteria**, the configured conditions determining who should hold them. Their certification action is **Acknowledge**. This records examination of automatically controlled access without overriding the criteria or requesting removal.

A **lifecycle state** is a configured stage in the person's relationship with the organization and can require profiles. Profiles required by the current state do not appear individually in certifications.

A manager can identify an inappropriate requirement, but their judgment does not turn these automatically controlled items into ordinary individual Revoke decisions. Investigate the governing data or access requirement with the authorized people.

## Distinguish the two routes when a manager is missing

There is a difference between the dedicated Manager Campaign and a campaign created through Search with Manager selected as reviewer.

The documented dedicated Manager Campaign excludes identities without a manager relationship. That means a missing manager can become a missing person in the review.

The Search route supports selecting Manager as reviewer for the chosen population. The **campaign creator** is the person who created the campaign. Its documented missing-manager handling assigns that certification to the creator.

A **reviewer fallback** is an alternative assignment used when the normal reviewer cannot be determined. It is not evidence that the alternative person knows the employee's work.

For a missing-manager employee who is included through Search, suppose the creator is administrator-900, a different person from the employee, and no self-review conflict applies. The documented handling sends that work to the creator. Inspect the actual certification to confirm its assignment.

Compare the two routes:

| Chosen route | Documented missing-manager handling | What needs checking |
|---|---|---|
| Dedicated Manager Campaign | Identity is excluded | Whether the intended population now has a gap |
| Search campaign with Manager as reviewer | Certification is assigned to the creator | Actual assignee, suitability and any other applicable assignment controls |

Do not replace creator with campaign owner when explaining this particular missing-manager rule; those responsibilities are not interchangeable.

An assignment to administrator-900 can keep work from disappearing, but the administrator may still lack the business knowledge needed to decide. Establish an appropriate supported review arrangement.

Do not remove the employee from the expected population merely because a manager field is blank.

## A nonblank manager can still be wrong

Suppose the personnel account names an old manager, or contains a new reference that does not match an available identity.

Inspect the actual resolved relationship. A nonblank input can identify the wrong person or fail to establish the intended new link.

The documented field-matching behavior can retain an existing manager relationship when a changed manager value cannot be matched to a new manager. Therefore, “a manager is present” is weaker evidence than “the correct current manager is linked.”

Check the employee's source reference, the configured comparison, the intended manager's identity and the resulting relationship. A readable manager name on a screen does not explain all of those steps.

If a project lead knows the current work better than the recorded line manager, establish the appropriate reviewer arrangement through the supported campaign process. Do not falsify accurate personnel-manager data merely to route one review.

The same applies when a manager is unavailable or lacks the knowledge to complete the work. Identify a suitable authorized reviewer and follow the applicable assignment and campaign-state rules.

## A manager change and a review reassignment are different changes

Suppose a preview was generated at 09:00 using manager-840. The employee changes manager later, and subsequent processing correctly links their identity to manager-855.

The newer identity relationship does not prove that the already generated certification has moved to manager-855.

A **preview** is generated campaign information available for validation before starting the campaign. It captures review context; it is not simply a live view of today's personnel record.

Inspect the actual assigned certification and its timing. Decide with the responsible administrator how the existing review should be handled under the supported process.

Correcting manager data addresses the employee's relationship used for relevant future processing. **Reassignment** changes responsibility for supported existing review work. One change is not proof the other happened.

Reassignment also has state and self-review restrictions. For example, a reviewer may have already signed off, confirming their completed review. That certification cannot be reassigned through the documented reassignment action.

Do not report that the new manager reviewed the access merely because their name now appears on the identity. The recorded decision actor and the current assigned reviewer are different evidence.

## Check readiness against the business question

Before relying on a manager review, establish that the selected people and access match the requirement, that the manager relationships are correct and that the generated work reached suitable reviewers.

Inspect a **review population**, the people, accounts and access intended for the campaign, against its actual generated contents. Correct routing for one employee does not establish that every intended employee was included.

Check the descriptions and account context the manager needs. An account used by an application or scheduled process needs responsible ownership and an appropriate supported review approach; an employee-manager relationship alone does not establish who should assess that account.

ISC prevents self-certification, meaning someone reviewing their own access, by separating that access and assigning review responsibility elsewhere under its supported controls. Do not assume that a manager receives a decision about their own access because they supervise other selected people.

Finally, confirm that the reviewer has the required permission and can perform the work. A correct reporting relationship, an email notification and a completed generation operation answer different questions.

The useful evidence is the intended population, reliable manager data, actual generated assignment and an understandable basis for the review.

## Try a new manager whose identity is not yet available

The person identified as operator-305 now reports to manager-920. Their warehouse account holds STOCK.ADJUST, which permits changing inventory quantities.

The account is correctly associated with operator-305. The review includes that individually reviewable entitlement, and no package or automatic requirement keeps it.

The personnel source manager value has changed to 920. But the identity that should represent manager-920 is not yet available to the configured matching process.

The employee's resolved manager relationship still points to manager-910. The generated certification is assigned to manager-910. There is no self-review issue in this example.

Someone says, “The manager field is filled in, so the manager review is ready.”

Which facts support or contradict that conclusion?

The new source reference supports the intended relationship with manager-920. It does not establish that the manager identity exists, that correlation found it or that the existing review is assigned to that person.

The actual link and generated assignment still identify manager-910. Under the documented field-matching behavior, an unmatched changed value can leave the old relationship in place.

Investigate the legitimate manager identity and configured match through the authorized data process. Do not create an inaccurate person record or overwrite correct personnel information just to make a review assignment appear complete.

After the appropriate correction and processing, inspect the resulting manager relationship. Then establish separately how the already generated review should reach a suitable authorized reviewer.

Suppose the current manager confirms that operator-305 still needs inventory adjustment. That supplies useful business evidence. It does not grant the manager permission to act on a certification still assigned to someone else.

The manager review fits the question of whether the operator needs adjustment for their work, but its data and assignment are not yet ready.

Now change the question: the task is to establish what STOCK.ADJUST technically permits across warehouse accounts and whether its configuration is too broad.

That needs application or source expertise. A corrected employee-manager link alone cannot answer it. Keep the business question, the knowledgeable reviewer and the actual assignment connected.
