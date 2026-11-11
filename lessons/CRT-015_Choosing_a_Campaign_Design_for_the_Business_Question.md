# Which campaign design answers this business question?

Someone asks you to review the Payment Approver role.

Before choosing a campaign, pause at the word review. What decision do they need?

They may want to know whether each person holding the role still needs it. They may want to check whether the role itself contains the right permissions. Or they may actually want every Finance person's access reviewed, including access outside that role.

Those requests can lead to different work even though the same role appears in the conversation.

A useful campaign design starts with the decision the review must support. Then you work out which records, access and reviewers can support that decision.

## Give the request a concrete meaning

In SailPoint Identity Security Cloud (ISC), a **certification campaign** organizes access-review work. A **reviewer** receives items to assess and records the supported decisions. For a person's reviewable access, Approve accepts continued access and Revoke calls for its removal. The available action depends on how the access was assigned.

An **identity** is ISC's record for a person. Their **accounts** hold access in applications. ISC manages information from each system through a **source**, which contains its connection settings and collected account data.

An **entitlement** is a recorded piece of access, such as permission to approve payments. An **access profile** groups entitlements from one source. A **role** can group profiles and direct entitlements, including access across sources.

For our comparison, the Payment Approver role contains two entitlements from Payments Production:

- PAY.VIEW allows viewing payment records.
- PAY.APPROVE allows approving payments.

These are supplied application capabilities. We know what the permissions do from the application, rather than guessing from their labels.

Here are the existing access records.

| Identity | Department | Source and account | Existing access |
|---|---|---|---|
| 1001 | Finance | Payments Production, pay-1001 | Payment Approver role |
| 1002 | Operations | Payments Production, pay-1002 | Payment Approver role |
| 1003 | Finance | Support, case-1003 | CASE.READ: permission to read support cases |

The role is assigned to each holder's identity in ISC. Its two permissions are held on that person's Payments account shown in the table.

The account links and collected access are correct. The two people received the role through access requests, meaning submitted requests for that access. The role and the separate case-reading entitlement can be reviewed in this example. No automatic access requirement or exclusion changes these supplied records.

Assume the chosen reviewers are suitable, permitted to perform their reviews and not reviewing their own access.

Now compare what each request needs.

## “Do Finance people still need their current access?”

The starting point is the people in Finance: identities 1001 and 1003.

Their access is not identical. One has a payment role; the other has case-reading access in another system.

A **manager review** is useful when a manager knows the people's current responsibilities and can assess which access their work requires. The manager still needs a clear explanation of what each permission or package allows.

A **query** is a search instruction that finds records matching conditions. In the Search identity route, you can select the Finance identities and choose the intended access to review for them. Where that campaign offers the Manager reviewer option, the recorded manager relationships determine the normal assignees.

That connects two different inputs. Department helps find the Finance people; each person's manager relationship tells ISC who their manager is. Selecting a Finance department value does not create or validate that manager link.

If the request includes all their reviewable access, identity 1003's Support permission matters. Choosing only Payment Approver holders would miss that person and that access.

The dedicated Manager Campaign route depends on recorded manager relationships. Identities without a defined manager are excluded from that route. In a Search campaign configured with the Manager reviewer choice, the documented missing-manager handling instead sends the work to the campaign creator. That fallback does not establish that the creator knows the person's current work.

Check the actual route, relationships and resulting assignment. A manager-focused intention does not repair missing data.

This request is about people's access needs. A successful role-only review would answer a narrower question.

## “Does everyone holding Payment Approver still need that role?”

The starting point now is the role and its holders: identities 1001 and 1002.

Identity 1002 matters even though the department is Operations. Identity 1003 is outside this role-holder request.

An **assignment** is the association through which a person holds an access object. Here, each person has an assignment of the same Payment Approver role.

An **assignment review** asks whether that person's holding remains appropriate. The role is the same object, but the answer can differ between holders because their work can differ.

The supported Access Items route can start from the role to identify its holders. You still need the later access choice to match a role-only request. Choosing all access for those people can bring unrelated access into the campaign; access refinement narrows what is reviewed.

The reviewer needs to understand both the role's capabilities and each person's current need. The **role owner** is the person recorded as responsible for the role. That person can explain its intended purpose, but the ownership label alone does not prove knowledge of every holder's current work.

For example, where the campaign offers an Individual reviewer choice, a suitable authorized person could assess the selected role holdings with the necessary business evidence. The choice is not automatically fixed merely because you started with a role.

Inspect the actual included holders, access objects and assigned reviewers. The work here concerns people's holdings. The shared role's design is a different review target.

## “Is Payment Approver itself designed correctly?”

Now the subject changes.

The **role definition** is the shared configuration describing the role: its access, description and any conditions used to determine membership. Each person's holding is separate from that shared definition.

A **role-composition review** assesses the role's design. It can examine whether the permissions and membership conditions fit the role's intended purpose.

Follow the difference in the diagram.

```text
Shared role definition: Payment Approver
        PAY.VIEW + PAY.APPROVE
                    |
        +-----------+-----------+
        |                       |
        v                       v
 Holding for 1001         Holding for 1002
 Finance                 Operations

 Assignment question:
 Should this person keep this role?

 Composition question:
 Is this role designed appropriately?
```

The lines connect the shared definition to two people's holdings. They show a relationship, not a sequence of background jobs.

If you ask whether identity 1001 still needs the role, you assess the left-hand holding. If you ask whether PAY.APPROVE belongs in the role at all, you assess the shared design.

Approving 1001's role does not establish that every permission in the role was correctly designed for its purpose. Rejecting 1001's holding does not rewrite the definition for 1002.

In the documented Search flow, role-composition campaigns appear under **Legacy Campaigns**. Legacy means the older campaign-processing path. These reviews can remain on that path even where newer campaign features are available.

Check that the role is eligible for this review type. The presence of a role in ISC does not establish that every review route can assess it.

The role owner needs the business and technical evidence to assess the design. Ownership and permission remain different things: a person responsible for a role is not automatically allowed to perform every administrative change.

Rejected contents in this role-composition path lead to manual change work for the campaign's selected **remediation owner**, the person responsible for carrying out the required correction. The supported setup requires an administrator permitted to update roles.

The review outcome creates work to correct the role. Check who received that work and what the permitted administrator changed. Confirm the saved role contents and, where account permissions need to change, the actual account results. Closing a task alone does not prove that those permissions are correct.

You need this route when the question concerns the shared package. A holder review answers whether a particular person should keep it.

## “Is access inside Payments Production appropriate?”

This request is focused on the system.

A **source-owner review** asks the recorded source owners to assess access within the selected systems. The **source owner** is the person recorded as responsible for that source in ISC.

Source expertise helps interpret what the permissions allow and what the application requires. Current business need may still require information from managers or other responsible people.

In our records, Payments Production includes accounts for identities 1001 and 1002. A Finance-only people selection would miss the Operations account.

Conversely, a Payments-only review does not establish that identity 1003's Support permission was assessed. That permission belongs to another source.

The dedicated Source Owner Campaign route can select one or more sources, and every included source needs a recorded source owner for generation. Verify the owner is appropriate as well as present.

Also inspect the actual reviewable objects. A permission inside a role or profile may be assessed through that containing object. Selecting a source does not make every underlying permission independently reviewable.

Manager knowledge, source expertise and precise selection can support the same review requirement. They are not mutually exclusive categories that force you to choose only one kind of reasoning.

## What if the request concerns an account without a matched person?

An **uncorrelated account** is a source account without the intended link to an identity established from authoritative person data. Authoritative person data means the trusted records used to establish who the people are, such as employee records.

The account may still have access. A missing identity link is not evidence that the account is unused or that its permissions should all be removed.

A normal people selection cannot establish coverage of accounts that it never reaches through a person. Where supported, an Uncorrelated Accounts campaign starts from accounts on selected sources.

The immediate questions include what the account does, who is responsible for it, what access it holds and why that access remains needed. Check whether a missing or incorrect person link needs correction, or whether the account belongs to a different kind of use.

Do not attach an account to an arbitrary employee just to make it appear in an employee review. That would change the apparent ownership without establishing the truth.

The review design needs the account's actual source and identifier, appropriate responsibility and evidence for its use.

## What if software uses the account?

A reporting job can use an account to run exports automatically. The access supports a program's work, even though a human is responsible for that program.

A **machine or service account** supports this kind of non-human use. ISC can represent the program or process through an **application identity**, with machine accounts associated with it.

Human responsibility and the identity used to represent the program have different purposes. Recording an engineer as the responsible owner does not turn the account into that engineer's personal application access.

Where the machine-account functionality is available and configured, use the supported machine-account review route for the relevant account population. Check classification, application identity, source coverage and actual reviewer assignment.

Classification means the configuration and account information used to identify machine accounts on a source. An account name beginning with svc does not prove, by itself, that ISC has classified it or included it in that route.

Also distinguish the two questions: is the account linked to the right identity, and is it used by a person or by a program? A missing person link alone does not tell you the account's use.

The required outcome is justified access for the program's actual work. A manager's approval of the responsible engineer's personal access does not establish that the program's account was reviewed.

## Turn the decision into a review plan

For an ordinary request, write a short statement that connects the required facts. For example:

“Review Payment Approver holdings for everyone who has that role, regardless of department. Include only that role. Assign a supported reviewer who can assess the holders' current need. Check the generated holders, role items and assignments before starting.”

This makes the review target clearer than a campaign name such as Payment Review.

For a role-design request, the statement changes:

“Assess whether Payment Approver's definition fits its approved purpose. Use the supported role-composition path and suitable role expertise. Identify who can perform any required definition changes and how the correction will be checked.”

For an account request, replace person assumptions with the actual account population and responsible ownership.

Then validate the work generated from the plan. A **preview** is generated review work available for inspection before the campaign starts.

Check the actual subjects, sources, accounts where relevant, review objects and reviewers. Look for a deliberate inclusion and exclusion: which record must be there, which similar-looking record should be absent, and why?

If those facts do not match the request, investigate the selection, data, access model or assignment before treating the design as ready.

The available campaign functionality, role or account type, permissions and configured data determine which route you can use. A useful business question remains valid even when a particular route is unavailable; you need an authorized process that can actually assess the intended object.

## Try a request that contains two different problems

An Inventory Reader role on Warehouse Production contains:

- STOCK.VIEW: view recorded stock quantities.
- STOCK.ADJUST: change those quantities.

The approved purpose of this role is viewing only. Two people hold it through access requests. The supplied current-work evidence confirms that both still need viewing access.

The request says: “Check this role. Its members should not receive adjustment access.”

Would approving each person's existing role assignment solve the problem?

No. The current role includes adjustment access. Approving the whole holding accepts continued access to that package; it does not turn the package into view-only access.

Would revoking every holder's role be a complete correction?

That would also affect the viewing access the people still need. It would not, by itself, correct the shared definition for future holders.

The unresolved design question is whether STOCK.ADJUST belongs in the role. The supplied approved purpose gives evidence that it does not. A supported role-composition assessment and authorized role-maintenance work address that definition.

If the review type cannot assess this role, an authorized role-maintenance process still needs to resolve the definition problem. Do not claim that a holder campaign has performed that assessment merely because its decisions finished.

The existing unwanted adjustment access also needs a verified outcome. Record which accounts must lose STOCK.ADJUST and which must keep STOCK.VIEW, then check the actual permissions after the authorized changes. A planned definition correction does not show that account access has already changed.

Now a third holder is found whose current need has not been checked. The request is extended: “Also establish whether every holder still needs the role.”

You have added an assignment question. Assessing the definition alone does not settle each holder's current need. Both questions need evidence, even if the same people help with them.

Finally, change how the role is assigned. Suppose it is granted automatically because people meet configured **membership criteria**, meaning conditions used to determine who receives it.

Those automatically assigned roles can only be acknowledged in an assignment review. **Acknowledge** records that the reviewer has seen the access; it does not remove the role or change the membership conditions.

Inspect the controlling definition and criteria when addressing that requirement. Choosing a different reviewer or a narrower access list does not create a Revoke action for a criteria-controlled role.
