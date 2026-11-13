# How do you check all review items across API pages?

An investigation returns two review items. The item you expected to find is absent.

Is it missing from the certification, or have you only read the first page?

An API can return a larger set of records in portions. Before reporting a missing item, let's establish which records were requested and whether every required portion was read.

## Start with the record being investigated

In SailPoint Identity Security Cloud (ISC), a **certification campaign** organizes access reviews. A **certification** is an assigned review within it. A **review item** is an access entry on which a decision is recorded.

One campaign can contain several certifications. Reading the items of one assigned certification does not establish everything in the campaign.

Our task is to check the five expected items in one identity-campaign certification. An **identity** represents a person in ISC, and an **account** is their record in an application.

The expected set includes report-reading and report-export permissions on production reporting accounts. Reading permits viewing reports. Export permits downloading report contents.

We want to establish whether the export item for account rep-03 is present.

The review item has its own **ID**, an identifier distinguishing that record from others. Keep it with the identity, account, source and permission information. A **source** is ISC's configuration for the application or account data.

Two items with the same readable permission name can concern different accounts. Do not merge them merely because their labels match.

## Use the read operation for this certification

An **API**, application programming interface, lets software request information or operations. The **request** states what is wanted; the **response** is what the service returns.

**GET** is the read operation used here. The next-generation List Review Items endpoint uses this path:

`/certification-campaigns/v1/certifications/{certificationId}/review-items`

An **endpoint** is the address for an API operation. The certificationId position needs the actual assigned certification's ID, not the campaign ID.

Confirm that the certification belongs to the intended campaign and review. Similar names from an earlier cycle are not enough.

This endpoint is currently Experimental and requires the **X-SailPoint-Experimental** request header set to **true**. A **header** carries request or response information separately from the returned item records.

Its documented callers are **ORG_ADMIN**, **CERT_ADMIN**, or a reviewer for this certification. Being able to review one certification does not establish authority to read every review in the organization.

Use the supported operation and authorized scope for the actual environment. This read does not record decisions, reassign work or sign off a review.

## Understand the two paging controls

**Pagination** returns a collection in portions, called pages.

The **limit** is the maximum number of records requested in one response. The **offset** is the number of records skipped from the beginning of the matching collection.

Offset starts at zero. It is not a page number.

With limit set to 2:

- offset=0 starts at the first record.
- offset=2 skips the first two and starts at the third.
- offset=4 skips the first four and starts at the fifth.

These are **query parameters**, values supplied with the read request to control the returned portion. Filters can also limit which records match.

For our supplied example, the account data and generated review have already been checked. The collection is not changing while we read it. The caller and query conditions stay the same, and no filter excludes any expected item.

Call the five expected item IDs A through E for the comparison. A/B concern rep-01, C concerns rep-02, and D/E concern rep-03. E is the export item we are investigating.

The pages are:

| Request | limit | offset | Returned item IDs | Records returned |
|---|---|---|---|---|
| First portion | 2 | 0 | A, B | 2 |
| Second portion | 2 | 2 | C, D | 2 |
| Third portion | 2 | 4 | E | 1 |

The first two records did not contain E because it was in the third portion.

A successful first read established that A and B were returned. It did not establish that E was absent from the certification.

## Compare the complete set, not just the row total

The five expected IDs are A, B, C, D and E. Across the three pages, we have those same five unique IDs and their matching account/access details.

**Reconciliation** means comparing the intended records with the actual records and explaining differences.

Here, that comparison supports a precise result: all five expected items were retrieved for this assigned certification, including the export item on rep-03.

The endpoint also supports **count=true**, which requests **X-Total-Count** in the response headers. That value is the number of matching results without the limit and offset restriction.

For our checked, unfiltered example, the returned total is five. It helps confirm that we expected more than the first two rows. Request it when the total is needed for the investigation.

The total still belongs to the request's collection and conditions. It is not the number of people in the organization or proof that every campaign item was selected correctly.

A matching total also does not replace checking IDs. Five collected rows could contain a repeated item and omit another.

The useful flow is:

```text
Confirm the assigned certification and read scope
                         |
                         v
Request the first page with consistent conditions
                         |
                         v
Retain item IDs and their account/access context
                         |
                         v
Read each remaining portion with the correct offset
                         |
                         v
Compare all unique returned IDs with expected IDs
                         |
              +----------+-----------+
              |                      |
              v                      v
Set matches the requirement    Missing, repeated or
for this certification         unexpected records
              |                      |
              v                      v
State that bounded result      Investigate scope, paging
                               and changes during collection
```

In our normal example, the returned set matches the expected set. We can stop the missing-item investigation at that bounded result. We have not established which decisions were finalized or whether any application access was removed.

## Notice how an incorrect offset creates overlap

Suppose someone treats offset=1 as the second page while keeping limit set to 2.

It skips only one record. In our unchanged example, it returns B and C, not C and D.

B now appears in both requests. Counting all returned rows without checking IDs would overstate how many different items were collected.

Use the documented record-based offset and keep the item IDs from each successful response. If records repeat, investigate the paging conditions and whether the collection changed. Do not silently delete repeated rows and declare the investigation complete; an expected item may still be missing.

## Keep filters, ordering and time consistent

A **filter** limits which records match a request. This endpoint supports filtering on specified fields, including completed.

If one request retains the filter condition `completed eq false`, it concerns only items matching that condition. Its total is not the total of all expected items. The item's completed field also does not establish final certification sign-off.

Check the actual conditions on every request. A total that looks too small may accurately describe a narrower query.

A **sorter** specifies a supported ordering of returned records. Use a consistent supported ordering across pages.

Ordering does not freeze the collection. Several items can also share an ordering value, such as the same account name. Do not assume that sorting by a unique ID is supported, or that all pages describe one frozen set of records.

If reviewers are changing items while the pages are collected, records can move within a filtered or ordered set. Keep the request conditions and collection times. Investigate differences before claiming a complete comparison of one unchanged set.

Our five-item example supplies an unchanged collection. That condition is why its page arithmetic and set comparison can be followed directly.

## Separate an empty result from an unsuccessful request

A successful read returning an empty list is different from a request that failed.

A **403** response means the caller does not have access to that operation. It does not mean the certification contains zero items.

A **404** means the requested resource was not found through that request. Check the endpoint and actual ID before describing the review as absent from ISC.

If a later page fails, retain the successful earlier pages and mark the collection incomplete. Resolve the error through the permitted process before using the partial set as the whole result.

Keep the certification ID, request conditions, relevant response headers, collection times and matching item/account details with the investigation evidence.

## Try a question about the whole campaign

You have retrieved every item in one certification. Someone asks whether this proves that the entire campaign's intended access was reviewed.

It does not.

First establish which certifications belong to the campaign and which records the caller can read. Then establish the required item set across that wider scope.

Even a complete collection of review items would still need the relevant decision and final-confirmation evidence to establish that the work was reviewed.

The first question was whether rep-03's export item existed in one assigned review. The larger question concerns a different population and a different result. Keep the evidence matched to the question.
