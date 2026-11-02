# One person has two accounts. Which account's access is under review?

Suppose a person uses a reporting application in two ways. They have one account for everyday reporting work and another account for administration work.

Both accounts can export reports. The person still needs to export reports during their everyday work, but their administration duties do not require exporting them.

A review that asks only “Does this person need to export reports?” can miss that difference. We need to connect the need with the account where the permission exists.

## Start with the person and each account

An **account** is a record in an application or system. Its permissions determine what someone using that account can do. In this example, the everyday account and the administration account are separate application records, even though the same person uses both.

SailPoint Identity Security Cloud, or **ISC**, has an **identity** representing the person. That identity connects information about the person with their accounts and access. One identity can be linked to more than one account on the same system.

The everyday account is used for normal reporting tasks. The administration account is used for separately authorized tasks such as managing application users. An account with permissions for sensitive actions is called a **privileged account**. Its purpose and actual permissions matter when deciding what access it should keep.

Having an administration account does not explain a need for every permission on it. For our example, the person's administration work needs user-management permissions but does not need report export. Their everyday reporting work does need report export.

This also differs from being an administrator of ISC itself. Permission to manage users in a reporting application does not, by itself, authorize someone to configure certification campaigns in ISC.

## Identify the account before judging its access

ISC uses a **source** to represent a system or a collection of account data. Here, the Reporting source contains information collected from the reporting application.

Within that source, each account has identifying information. The source's **Account Name** is the configured name used to represent the account. Here, the names help us recognize the everyday account and the administration account.

The **Account ID** is the configured value used to reference that source account. The source's settings determine which application fields supply the Account Name and Account ID.

In our example, the readable names help us recognize the two accounts. The identifiers let us follow the exact records:

| Source | Account Name | Account ID | Purpose |
|---|---|---|---|
| Reporting | reports-daily | acct-104 | Everyday reporting work |
| Reporting | reports-admin | acct-908 | Authorized application administration |

Both accounts currently hold reports-export, meaning permission to export reports. ISC represents an access right like this as an **entitlement**.

The permission name tells us what access we are discussing. It does not tell us which account holds it. To follow the intended change here, we need the Reporting source, the account identifier and reports-export together.

Keep the source with the account reference. A test system and a production system can both contain an account named reports-admin. A matching account name does not establish that they are the same account. Confirm the exact source record and its account details before comparing them.

You may also encounter an ID for ISC's own account record in an operation or report. Establish which record that ID identifies and how it relates to the application's account. Do not assume every field called ID is interchangeable with the configured source Account ID.

The readable name reports-admin is a useful clue, but it is still a name. Check the account's recorded purpose and actual rights rather than using the word admin as proof of its ownership or privilege.

## Follow how the two accounts become review information

ISC first needs information about the accounts. It reads account data and held access from the application through the configured source. This collection is called **account aggregation**.

Reading reports-export from an account tells ISC that the account holds that permission. The collection itself does not give the account that permission or decide whether the person should keep it.

Collection gives ISC information about each account. ISC also needs to associate an account with the correct identity. Making that association is called **account correlation**. Configured correlation settings compare account information with identity information to establish the link.

Suppose this source's matching rule uses an employee-number field. Both accounts carry employee number 7312, and that number identifies exactly one identity: the correct person. The configured match can therefore link both accounts to that identity.

The employee number helps establish who the accounts belong to. The Account IDs still distinguish which account is which. Matching both accounts to one person does not combine their permissions into one application account.

For this example, both accounts are correctly linked to the same person's identity. ISC has current information showing reports-export on acct-104 and on acct-908.

These two account records are legitimate. They serve different purposes. Seeing the same identity against two accounts is not enough reason to delete an account or remove one of the links.

An administrator then includes the relevant access in a **certification campaign**, an organized set of access reviews.

A **certification** is an assigned review within the campaign. The **reviewer** is the person responsible for deciding about the access presented in that review.

The particular access presented for a decision is a **review item**. When you open an item, establish which person, source, access and account or accounts it concerns. Start with its details and use the supporting account information when needed.

The review screen can organize information around a person or an access item. That organization does not make the underlying accounts one account. If both entries say reports-export, compare the account references before calling them duplicates.

Likewise, finding the person in a campaign does not prove that every account and permission belonging to them is included. Compare the intended accounts with the actual campaign contents.

## Decide why the permission is needed on each account

For acct-104, the person still performs reporting work that requires exporting reports. The reviewer has confirmed that need.

For acct-908, the person still performs administration work, but those duties do not require exporting reports. The reviewer has confirmed that difference too.

The intended outcome is to keep reports-export on acct-104 and remove it from acct-908. The person's other authorized administration permissions should remain.

```text
One person's ISC identity
    |
    +-- Reporting / acct-104
    |       reports-export: keep
    |
    +-- Reporting / acct-908
            reports-export: remove
```

The branches show two accounts linked to one identity. The keep and remove labels show the intended outcomes after checking current need. They do not mean either account has already changed.

An **Approve** decision accepts keeping the access being reviewed. A **Revoke** decision says that the reviewed access should be removed. Before applying either decision, confirm the scope of the item: exactly which access and accounts the decision covers.

Suppose the supplied review item concerns only reports-export on acct-908. With that target confirmed, Revoke fits the established lack of need. The continuing need on acct-104 does not justify keeping export on acct-908.

Now suppose the displayed item covers both accounts, or its account scope is unclear. You cannot assume that its Revoke action will remove export only from the administration account. Establish the supported decision scope with the campaign administrator before finalizing it. Explain that the person needs export on one account and not the other, so a broad removal would not meet the requirement.

The number of visible rows is not a reliable rule for the number of affected accounts. This is especially important when the item is an **access profile**, a package of related entitlements from one source, or a **role**, which groups access for a business purpose. Inspect the package's contents and the accounts affected by its assignment before treating its decision as a change to one permission on one account.

For the account-specific removal we follow below, the target has been confirmed as reports-export on Reporting account acct-908. The permission is reviewed directly, and no other package or automatic access requirement is keeping it on that account.

## Carry the same account reference through removal

Once Revoke is recorded, the reviewer still needs to finish and confirm the review. This confirmation is called **sign-off**. The campaign's process determines when the required removal work is initiated.

**Remediation** is the work needed to act on the review decision. Making an access change in an application is called **provisioning**. Here, the required change is to remove reports-export from acct-908.

Follow the operation or assigned removal task using the same source, account and permission that were established in the review. A successful change to acct-104 would concern the wrong account, even if it removed an entitlement with the correct name.

The requirement concerns a permission. It does not ask for deletion or disabling of the administration account, because the person still needs that account for other authorized work. Removing an entitlement, disabling an account and deleting an account are different actions with different effects.

Suppose the removal from acct-908 succeeds. Check the resulting account access in the reporting application. The evidence should show that acct-908 no longer has reports-export. Also check that acct-104 still has the approved export access that should remain.

If the person can still export reports while using acct-104, that does not prove the removal failed. Export on that account was meant to remain. A test of the outcome must identify which account was used.

Conversely, if export stops working on acct-104 while acct-908 still has it, the intended outcome has not been achieved. Investigate the operation's account target and the source account results. Do not close the issue simply because some export access was removed.

ISC's collected account data may still show the earlier permissions until the relevant collection and processing update it. Check when each observation was made. Current application evidence, an earlier ISC account view and the generated review can describe different moments. A completed operation alone does not make every displayed record current.

## If the account is shown under the wrong person

Correlation tells ISC which identity an account belongs to. That association influences whose access appears in an identity review. If the association is wrong, the reviewer can be judging account access using the wrong person's job and responsibilities.

Suppose acct-908 is linked to a different person's identity. First verify who actually uses or is responsible for that account, using reliable account and employment information. Compare that evidence with the correlation recorded in ISC.

Once a wrong association is established, an authorized administrator needs to correct it through the appropriate account-correlation process. Approving or revoking an item does not repair the ownership information behind it.

After the correction, check both the account's current identity link and the affected campaign's actual contents. Do not assume that correcting source or identity data automatically rewrites a review that was already generated.

Keep the responsibilities separate. The person associated with an account is not necessarily the reviewer. The reviewer is also not necessarily authorized to change correlation or carry out provisioning. Those actions depend on the assigned responsibility and permissions.

## If ISC cannot associate the account with an authoritative identity

An **authoritative source** is a source configured to establish identities in ISC. A personnel system can serve this purpose for employees. ISC uses its account information to create the employee identities, then links their accounts from other sources to those identities. An **authoritative identity** is an identity established from that authoritative information.

An **uncorrelated account** has not been linked to an authoritative identity. For example, the account information needed for the configured match may be missing or incorrect. The account can still exist and hold permissions in the application.

ISC can represent such an account through an uncorrelated or placeholder identity. Seeing a name against that record does not establish that ISC has matched the account to a known employee.

If your review is intended to cover employee access, an account with no authoritative employee link needs explicit investigation. Do not assume that selecting an employee identity also includes an uncorrelated account that someone believes belongs to them.

ISC also supports dedicated uncorrelated-account certification campaigns. Where that capability is available, a reviewer can examine the account's permissions while the missing identity link is investigated. The campaign still needs deliberate scope, an appropriate reviewer and evidence of the account's purpose.

An uncorrelated account is not automatically an unnecessary account. Establish whether it belongs to a person, supports a process or is genuinely unused before deciding the required action. Correct a verified missing association where appropriate; do not choose an employee simply to make the account disappear from an uncorrelated list.

## A service account needs a different ownership question

Suppose an account exports reports every night for an automated job. A program uses the account to perform the work. This is a **service account**, one kind of **machine account**: an account used for a program or service rather than an individual's everyday work.

Its continuing need depends on the job it supports. Check what the job does, whether it still runs for an approved business purpose, and which permissions it needs. A human employee's job title alone does not answer those questions.

An **account owner** is the person recorded as responsible for that account. They help explain its purpose and access. A support team can also be involved in its operation. These responsibilities do not make the service account anyone's personal login. Recording an owner and correlating a personal employee account are different relationships.

Where the relevant machine-identity features are available, ISC can group machine accounts under an **application identity**, representing the program or process they support. Machine-account certification campaigns review access for those application identities. You may also see the term machine identity in the review experience.

Check the organization's available features, account classification and actual campaign type before choosing this route. An account name alone does not establish its classification or which review features are available.

Do not automatically apply an employee-manager review assumption to the service account. Establish the configured reviewer and someone with enough knowledge of the process to judge its access. If the responsible owner is missing, identify that gap rather than invent an owner or assume a universal fallback.

Two accounts held by one person and accounts grouped under a program identity can look similar as a branching diagram. Their business meanings differ. One describes a person's separate ways of working; the other describes a program or process and the accounts supporting it.

## Work through a removal that reached the wrong account

A person has two accounts on the Payments source. Both hold invoice-approve, meaning permission to approve supplier invoices.

Account pay-210 is used for invoice-processing work. The person still needs invoice approval on this account. Account pay-880 is used for separately authorized administration work, which no longer needs invoice approval.

Both accounts are correctly linked to the person. The review evidence confirms the current need on pay-210 and the lack of need on pay-880. The confirmed removal target is invoice-approve on pay-880. No other package or automatic requirement keeps that permission on pay-880.

A completed removal operation identifies pay-210. Current application evidence shows that pay-210 has lost invoice-approve, while pay-880 still holds it. Someone concludes, “The operation completed, so the review removal is finished.”

What does the evidence establish? Which account needs further removal work, and which approved access now needs attention?

The operation completed for the wrong account. It does not establish the required removal from pay-880. The current application evidence confirms that pay-880 still has the permission that should have been removed.

It also shows a second problem: pay-210 lost access that the person still needs. Report both differences. An authorized operator needs to investigate the incorrect target, carry out the approved correction for pay-210 and address the required removal from pay-880. Follow the organization's process rather than silently adding access just to make the symptoms disappear.

Verify both account results after the corrections. The intended outcome is invoice approval available on pay-210 and absent from pay-880. Then check that ISC's collected account information reflects the resulting access when it is updated. A success message for one operation cannot replace those account-specific checks.

Now change the situation: pay-880 is used by a scheduled invoice-processing job rather than by the employee. We can no longer use the employee's administration duties as the reason for removing its invoice permission. Establish what the job needs, who is responsible for it, how ISC represents the account and which review applies. The access decision needs evidence about the process using that account.
