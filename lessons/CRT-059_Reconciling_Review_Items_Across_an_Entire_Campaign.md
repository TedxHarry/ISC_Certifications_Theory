# How do you reconcile review items across an entire campaign?

You have read every item in one assigned review. The pages are complete, and the returned records match what you expected.

Can you now say that you collected every review item in the campaign?

Only if that assigned review was the whole required set. A campaign can contain several assigned reviews, each with its own items.

Let's follow both levels so that a complete first review does not hide a missing second or third review.

## Establish the campaign and the records it contains

In SailPoint Identity Security Cloud (ISC), a **certification campaign** organizes access reviews. A **certification** is an assigned review within it. A **review item** is an access entry presented for a decision.

The campaign, its certifications and their items have different **IDs**, identifiers for those particular records.

A readable campaign name is useful, but an earlier monthly campaign can have the same name. Use the actual campaign ID for the instance being investigated.

Our example reviews access associated with selected identities. It has three expected certifications, labelled R1, R2 and R3 for this comparison.

An **identity** represents a person in ISC. An **account** is their record in an application, and a **source** is ISC's configuration for that application or its account data.

The expected items include report-reading and report-export entitlements. An **entitlement** represents an access right: reading permits viewing reports; export permits downloading report contents.

The campaign administrator has checked which accounts and permissions should be reviewed, along with the generated assigned reviews. That independent check supplies the expected review and item lists we will compare with the returned records.

This **expected baseline** states which records should be accounted for. If it was simply copied from an incomplete first API page, it would not help detect what that page omitted.

## Check what the caller is allowed to retrieve

An **API**, application programming interface, lets software request data or operations. A **request** asks for information; a **response** is what ISC sends back. **GET** is the read operation used here.

An **endpoint** is the address for an API operation. The next-generation certification-list read uses this path:

`/certification-campaigns/v1/certifications`

A **query parameter** supplies a condition or control with the request. This endpoint supports a filter on **campaignRef.id**. Use it to select the actual campaign ID.

For example, the condition has the form `campaignRef.id eq "<actual campaign ID>"`. It means that the certification's campaign reference must match that campaign.

The filter selects among the certifications the caller can retrieve. It does not grant permission to read other people's reviews.

The endpoint returns certifications the caller is authorized to review. A non-admin caller must include **reviewer-identity=me**, asking for certifications in their own reviewer scope.

A complete personal result can therefore be smaller than the campaign's complete review set.

For the ordinary example, an authorized investigation administrator can retrieve all three expected certifications. That visibility is checked against the campaign baseline, rather than assumed from a successful response.

This API is Experimental and requires the **X-SailPoint-Experimental** header set to **true**. A **header** carries information alongside the request or response. Confirm the supported environment and operation before relying on its results.

## Collect the complete certification list first

**Pagination** returns a larger collection in portions. **limit** sets the maximum records requested per response. **offset** states how many matching records to skip from the beginning, starting at zero.

With limit set to 2, our first certification-list request uses offset=0 and returns R1 and R2. The next uses offset=2 and returns R3.

The caller, campaign condition and other request conditions stay the same. The example's collection is not changing while it is read.

Check the returned IDs against the expected R1, R2 and R3. Do this before declaring the campaign's item collection complete.

The supported **count=true** option can request **X-Total-Count**, a response header giving the matching total without the page restriction. In our example, that certification total is three.

Three here means three matching certifications. It does not mean three people or three review items.

Also inspect whether extra filters excluded expected certifications. Retrieving every match for a narrower request would not establish the campaign's full review set.

## Read all items inside each certification

The item-list operation is a separate read:

`/certification-campaigns/v1/certifications/{certificationId}/review-items`

Put each actual certification ID in its certificationId position. Do not substitute the campaign ID.

For identity-campaign certifications, this operation supports an organization administrator (**ORG_ADMIN**), a certification administrator (**CERT_ADMIN**), or a reviewer for the certification. Permission to list a certification does not establish every other API permission.

Read every required item page for R1. Then start R2's own item collection at offset=0, and do the same for R3.

The offset for R1 does not carry over to R2. They are different collections.

For our unchanged example, using a page limit of 2 produces this working comparison:

| Certification | Expected item IDs | Returned portions | Unique items collected |
|---|---|---|---|
| R1 | A, B | A/B at offset=0 | 2 |
| R2 | C, D, E | C/D at offset=0; E at offset=2 | 3 |
| R3 | F | F at offset=0 | 1 |

We now have all three expected certifications and six expected items.

Keep the certification ID with each item ID and the actual identity, source, account and access details. That association lets another person trace an item back to the review that supplied it.

Do not combine two items just because both say Report Reader. One may concern an ordinary account and another an administration account. They remain different review relationships.

## Reconcile the relationships as well as the totals

**Reconciliation** means comparing expected and returned records and explaining the differences.

For this task, check both:

- Did we retrieve every expected certification?
- Within those certifications, did we retrieve the intended permissions on the correct accounts?

The six-item total is useful, but it cannot answer the second question by itself.

Suppose the requirement includes report export on rep-03, but the collected set contains export on rep-30 in its place. Both sets can still contain six rows. That matching count would not correct the missing required account and unexpected account.

Compare the actual account and permission relationships. Explain missing and unexpected records instead of adjusting the expected list to make the total agree.

In our normal example, all expected review IDs and all six intended item relationships match. We can explain the result clearly: we retrieved the three assigned reviews and all six expected items for the campaign as checked at the time of collection.

It does not establish that reviewers made decisions, gave final confirmation of their reviews, or that rejected access was removed. Those questions need their own evidence.

The two levels connect like this:

```text
Identify the campaign and expected review set
                         |
                         v
Read every required certification-list page
                         |
                         v
Compare returned certification IDs with expected IDs
                         |
                         v
For each matching certification:
  Start its item collection at offset zero
  Read all required item pages
  Retain certification ID, item ID and account context
                         |
                         v
Compare required accounts and their permissions
                         |
             +-----------+-----------+
             |                       |
             v                       v
Reviews and items match        Missing review, item,
the checked requirement        or unexpected relationship
             |                       |
             v                       v
State the scope and time       Investigate before calling
of that complete collection    the campaign collection complete
```

## When a whole certification is missing

Suppose only R1 and R2 were collected. Their own item pages are complete, giving five items.

The missing sixth item belongs to R3. Repeatedly reading R1 and R2 will not retrieve it.

Check the certification-list pages, actual campaign ID, extra filters and caller visibility. Then establish why R3 was not in that parent list.

If the caller is limited to their own reviews, obtain the remaining information through an appropriately authorized investigation. Keep the personal result accurately scoped while that work continues.

Likewise, a failed R3 item request is not evidence that R3 has no items. Retain its error and describe the campaign collection as incomplete until the required records are retrieved or the difference is explained.

## Keep collection times with the comparison

A campaign's assignments and items can change while an investigation is running. A review can also be handed to another person.

Keep the request conditions and observation times for the certification list and each item collection. If the expected baseline describes an earlier campaign state, establish what changed before merging records from different times.

Using a consistent supported ordering can help paging, but it does not freeze the campaign. Each endpoint has its own permitted filters and ordering fields; do not copy one operation's choices into another.

Our example supplies an unchanged set. If that condition is not true, investigate the changed records and qualify the collection result. A second successful request alone does not establish one complete view of an unchanged campaign.

## Try a complete personal list

A reviewer retrieves all their certifications for a campaign and every item inside them. The parent response total is two, and two certifications were collected successfully.

Someone asks them to confirm that the entire campaign contains only those reviews.

What is still missing?

The total describes that request's authorized result. It does not establish that other reviewers have no certifications.

Compare the result with the independently checked campaign review set and establish who can retrieve the remaining scope. Only then can the investigation support a campaign-wide collection claim.

The important connection is the campaign you intended, the reviews you could retrieve, the items inside them and the permissions those items describe on the actual accounts.
