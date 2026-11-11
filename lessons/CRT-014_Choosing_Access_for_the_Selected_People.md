# Which access should we review for the selected people?

You have selected three people for an access review. The request is to review their permission to change stock quantities in the production warehouse system.

Each person can have other access too: viewing stock, reading support cases or using another application.

Should all of that access go to the reviewer?

That depends on the request. If you send every permission, you have created a broader review than the one requested. If you choose only the stock-adjustment permission, you need to check that the right people's existing permission reaches the review.

This choice is called **access refinement**: deciding which access to include for people already selected for the campaign.

Let's follow what that means in SailPoint Identity Security Cloud (ISC).

## Start with what the people actually have

An **identity** is ISC's record for a person. An **account** is that person's record in an application. The account can have permissions that determine what the person can do there.

ISC manages information from an application through a **source**, which contains the connection settings and collected account information. A permission can be recorded as an **entitlement**, such as membership of a group that allows stock adjustments.

A **certification campaign** organizes reviews of existing access. It brings access items to assigned **reviewers**, who judge whether people should keep that access.

Here is the access available in our example.

| Identity | Selected for this campaign? | Account and source | Access on the account |
|---|---|---|---|
| 810 | Yes | wh-810, Warehouse Production | STOCK.VIEW: view stock; STOCK.ADJUST: change recorded stock quantities |
| 810 | Yes | case-810, Case Management | CASE.READ: read support cases |
| 811 | Yes | wh-811, Warehouse Production | STOCK.VIEW and STOCK.ADJUST, with the same meanings as above |
| 812 | Yes | wh-812, Warehouse Production | STOCK.VIEW only |
| 813 | No | wh-813, Warehouse Production | STOCK.ADJUST |

Identity 810 appears twice because one person has two accounts in different systems.

The accounts are linked to the correct people, and the collected permissions agree with the current application records. Here, each listed permission is a separate item that can be reviewed on its own. No other campaign restriction removes one of these items.

For both access choices, assume a suitable reviewer has permission to perform the review and is not reviewing their own access.

The selected people are 810, 811 and 812. That selection is already established. Identity 813 is outside it.

Now we decide which access to review for those selected people.

## What happens if you choose all access?

In the Search campaign flow, **Certify All Access** includes the access associated with the selected identities, subject to the rules that determine what can appear in a certification.

For our supplied records, the resulting review work contains:

- Identity 810: Warehouse Production STOCK.VIEW and STOCK.ADJUST, plus Case Management CASE.READ.
- Identity 811: Warehouse Production STOCK.VIEW and STOCK.ADJUST.
- Identity 812: Warehouse Production STOCK.VIEW.

There are six permission holdings here. A holding means the named person has that permission through the named account.

Why did the case-reading permission appear? Because identity 810 was selected, and the access choice did not restrict the review to Warehouse Production.

Why did identity 813's adjustment permission stay outside? Because 813 was not one of the selected people.

“All access” is therefore about access for the selected identities. It does not mean every person's access across the organization.

This broad choice makes sense when the request really is to assess all reviewable access for those people. For the narrower stock-adjustment request, however, it introduces work beyond the requested permission.

## Now choose only the adjustment permission

**Refine Access Items** lets you choose the access items you want included instead.

Find the STOCK.ADJUST entitlement belonging to Warehouse Production. Confirm its source and object identifier, the reference that distinguishes that ISC object from others. Then add that item to the campaign's access selection.

You are choosing ISC's record describing the permission. You are not adding the permission to anyone's application account.

For the selected people in our table, the intended adjustment-only review contains:

- Identity 810's STOCK.ADJUST holding on wh-810.
- Identity 811's STOCK.ADJUST holding on wh-811.

Identity 812 has no STOCK.ADJUST holding in the supplied data. There is no adjustment item to judge for that person.

Identity 813 does hold STOCK.ADJUST, but remains outside the selected people. Refinement does not bring that person in merely because the entitlement matches.

Follow the two checks together. The holding must belong to someone selected for this campaign, and it must match the access chosen for review. A matching permission on an excluded person's account does not meet both conditions.

This explains the change from six holdings to two. We narrowed the access included for the selected people. We did not change what their application accounts can do.

The people and access totals describe these supplied records. They do not promise a particular number of certifications or screen rows. A **certification** is assigned review work within the campaign; a **review item** is an access item presented for a decision. Check the actual work to see how it is organized.

## A search result and a saved choice are different things

Finding STOCK.ADJUST in a search tells you that a matching object was found. The campaign still needs your access selection saved.

In this flow, **Add to Campaign** records the chosen items. **Added to campaign** lets you inspect what you have added before continuing.

These controls concern campaign contents. They do not grant access in the source system.

Suppose you also want stock-viewing access reviewed. Add the intended STOCK.VIEW object as well. Then inspect the saved selection to confirm both permissions are present.

With the same people and supplied access, that choice includes view and adjustment for 810 and 811, and view for 812. It still does not create adjustment access for 812.

The choice can involve different access types. An **access profile** is a package of entitlements from one source. A **role** can group access profiles and direct entitlements, including access across sources.

Check the saved choices for each type you intended to include. Seeing the right entitlement in one list does not prove that a role or access profile you also needed has been added.

The relationship is:

```text
Selected people and their collected access
                    |
                    v
          Choose the review's access
                    |
          +---------+---------+
          |                   |
          v                   v
     All access          Refined access
          |                   |
          v                   v
  Reviewable access    Holdings of the chosen
  for those people     reviewable access items
          |                   |
          +---------+---------+
                    |
                    v
        Inspect the generated work:
        right people, sources, accounts,
        access items and reviewers
```

The left branch keeps the broader reviewable access. The right branch keeps holdings of the chosen access items. Both branches still need an inspection of the generated work.

The arrows connect the inputs, choice and evidence. They are not an exact sequence of internal ISC services.

## What if a selected person does not have the chosen access?

Return to identity 812. The person has stock-viewing access but no adjustment permission.

If the campaign is adjustment-only, there is no adjustment holding for 812 to approve or revoke. Do not invent a missing decision just to make every selected person have the same item count.

If someone says, “But 812 should be able to adjust stock,” that is a different requirement. You would investigate why the permission is missing and whether access should be requested or assigned through the appropriate process.

A certification reviews access that exists in the relevant records. Choosing an absent permission for review is not an instruction to grant it.

There is a data question too. If you have evidence that wh-812 really does hold STOCK.ADJUST in the application, compare that evidence with ISC's collected account data and ownership link. The apparent absence may be a collection or association problem.

Those two cases need different responses: genuinely missing access versus existing access missing from the review data. The campaign's short item list cannot tell you which case you have without that evidence.

## Be precise about the access object

Selecting all access from Warehouse Production would be broader than selecting STOCK.ADJUST alone. Stock-viewing permissions could still belong to that source-wide scope.

Likewise, an entitlement called Adjust in Warehouse Test is a different choice from the production entitlement. Similar names do not make them the same object.

Check the source, the object's reference and what the application says it permits. A display name helps you find an item, but the intended environment and actual permission determine whether it meets the request.

There is another detail when one person has multiple accounts. Selecting an entitlement definition is not automatically the same as selecting one particular account that holds it.

If the requirement names an account, inspect the supported account conditions and the generated account context. Do not infer an account restriction solely from an access object's name.

## Refinement works with the access model

The **access model** describes how access is grouped and assigned. So far, our entitlements were separately reviewable. A person can also receive access through the profiles and roles described above.

Consider a separate case in which a person holds a Warehouse Supervisor access profile containing both stock viewing and stock adjustment. The person received this profile through an **access request**, a submitted request for that package. The adjustment permission is part of the profile.

You cannot assume that choosing the component entitlement will pull it out of the package as a separate review item. The containing profile is the reviewable object in that arrangement. If the profile comes through a role, the role can be the relevant containing object instead.

A request to review adjustment access must therefore account for the actual package that gives it. If you include the profile, the reviewer needs to understand the profile's complete access scope, including viewing. Refinement does not redesign the package into an adjustment-only package.

The way access was assigned still matters:

A role obtained through an access request can be approved or revoked in a certification. A role can also be assigned automatically because configured conditions match the person. Those conditions are its **membership criteria**. In that case, the role can only be acknowledged in the review. Acknowledge records that the reviewer has seen it; the criteria continue to control membership.

A **lifecycle state** represents an identity's status, such as active or terminated, and can have access profiles assigned through its configuration. Profiles granted through that state do not appear as individual certification items.

Selecting all access does not bypass those rules. Refining access does not bypass them either.

If the chosen object does not appear, identify how the person received the access before changing selections. Choosing more objects cannot fix an incorrect assumption about which object can actually be reviewed.

## Leaving access out is not a decision about keeping it

In our adjustment-only example, identity 810's CASE.READ permission is outside this campaign.

That omission does not say that reading cases is appropriate. Nobody has assessed that permission through this campaign's item decisions. It also does not remove the permission from case-810.

There are separate records here:

The campaign selection says which access will be reviewed. A reviewer decision says whether the reviewed access should be kept or removed. Any required removal then needs its own supported processing and account evidence.

Narrowing the campaign performs the first job. It does not perform the other jobs.

This distinction also applies to access that is present in the campaign but still undecided. An undecided item is present but has no review decision yet. The campaign's completion rules determine how remaining undecided work is handled. An omitted permission has no review item in this campaign to decide in the first place.

If another required permission is outside the review, arrange appropriate coverage for it. Do not describe the whole person's access as approved because the adjustment-only review finished.

## Check the work that was actually generated

A **preview** is generated campaign work you can inspect before starting the review.

For our adjustment-only request, confirm the two expected holdings: 810 on wh-810 and 811 on wh-811, both for the exact Warehouse Production STOCK.ADJUST entitlement.

Then inspect the boundaries. Stock viewing and case reading should not be included in this supplied adjustment-only result. Identity 813 should not be imported. Identity 812 should not acquire a fictional adjustment holding.

Check the assigned reviewer too. A correct access selection does not by itself establish who received the work, whether that person can judge the permission or whether they are reviewing their own access.

A saved selection is evidence of the chosen instruction. The preview is evidence of the work generated from the instructions and available data.

If the preview is wrong, identify the differing record before acting: selected person, collected holding, containing package, saved access choice or reviewer assignment.

Also check whether a **campaign filter** applies. This is a separate configured set of inclusion or exclusion criteria that can affect campaign content. Do not assume that a manually chosen access list describes every restriction when a filter is also applied.

Also distinguish a changed saved definition from an already generated campaign. A newly saved access choice is not proof that existing review work changed. Use the supported correction or generation process for the campaign's engine and state, then inspect the resulting work.

These Search choices depend on the functionality available in the tenant. When working with a large result set, check the applicable selection and display limits rather than assuming that every result fits in the refinement screen.

## Test the same reasoning with another system

The request is:

“Review payment-approval access in Payments Production for selected identities 901 and 902.”

The supplied records show that 901 has two production accounts, pay-main and pay-backup. Both hold the separately reviewable PAY.APPROVE entitlement, meaning permission to approve payments. The account links and access data are correct.

Identity 902 holds a permission with the same label only in Payments Test. Identity 903 has production approval access but is outside the selected people.

What should you establish before calling the scope correct?

Start with the selected people: 901 and 902. Then choose the exact production approval object.

Both production account holdings for 901 need to be accounted for in the generated review scope. Checking only pay-main would leave the pay-backup holding unverified.

Do not substitute 902's test permission for missing production access. Do not bring in 903 simply because 903 holds the production entitlement.

This does not tell you how many rows the interface must show or whether it offers a separate decision for each account. It tells you which actual holdings the review requirement covers and which evidence you must inspect.

Now change the request: review only pay-main, and leave pay-backup outside this campaign.

Does selecting the same production entitlement prove that narrower account scope?

No. The entitlement definition is shared by both holdings. It identifies the permission, but does not by itself express “pay-main only.”

You need to establish a supported way to restrict the account scope in that campaign type, and verify the resulting account context. Until then, the account-specific requirement has not been shown to be met.
