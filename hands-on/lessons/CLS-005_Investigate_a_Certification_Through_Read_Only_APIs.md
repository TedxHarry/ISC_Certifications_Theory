# CLS-005: Investigate a certification through read-only APIs

The campaign screen says the review is complete. You need to explain which access was reviewed, who made the decisions and whether the removal was actually carried out.

The API can help you examine the underlying records. But a successful response can still contain only the first page, only work visible to your account, or only the review decision.

We will trace one small campaign carefully and compare its records with the interface and removal evidence. Every request in this investigation reads data. You will leave the campaign, decisions, tasks and accounts unchanged.

## First, understand the records we are connecting

An **API** is a supported way for another program to request information or actions from ISC. An **API client** is the tool you use to send that request and read ISC's response. You choose what to ask for; ISC checks your access and returns the information it allows you to read.

The interface and API provide views of supported product records. We are not reading ISC's database or relying on an undocumented browser request.

A **campaign** organizes the whole review. A **certification** is an assigned review within that campaign. A **review item** is an individual piece of access within the assigned work.

The relationship is:

> Campaign
>
> → Assigned certifications
>
> → Individual review items and their decisions

Two permissions can be inside one assigned certification. Counting certifications does not tell us how many permissions were reviewed.

Each record has an **ID**, an identifier used to refer to that exact object. A campaign ID, certification ID, review-item ID and entitlement ID identify different objects. Keep them separate even if their values look similar.

## Choose an actual case we can inspect

Use an existing, actually executed next-generation **identity** campaign with this exact small scope:

| Person | Source | Account | Reviewed access | Recorded final choice to verify |
|---|---|---|---|---|
| certlab-employee01 | certlab-reports-csv | certlab-account01 | certlab-report-export | Approve |
| certlab-employee02 | certlab-reports-csv | certlab-account02 | certlab-report-export | Revoke |

An identity is ISC's record for a person. A source is its configured representation of a system and collected accounts. An entitlement is a tracked permission; Export here represents downloading reports in bulk.

The existing certlab-cls004-context-run01 is suitable only if someone has actually run it and its records match this scope. A course filename or expected-result file is not a real campaign.

`certlab-manager01` is the intended reviewer. `certlab-manager02` is the source owner, the person responsible for this source in ISC. Verify who actually received and completed the review, including any transfer to another reviewer.

If you do not yet have a compatible actual campaign, prepare and complete that authorized review separately before this investigation. Do not create history through API writes merely to fill the example.

First inspect the existing campaign and its assigned reviews in ISC. Record their actual IDs, reviewers, item counts and final submission state, with your observation time. Keep the signed decisions and any removal evidence available. These observations give us something to compare with the API responses.

The accounts model a CSV application. We call certlab-reports-csv source A and certlab-owner-reports-csv source B. Historical removal should show A changing from five holdings to four, with all Read access and employee01 Export retained; B keeps its six holdings. A **holding** means one account has one permission.

The source may already have been restored to five holdings for another training run. Record whether that reset occurred and when. We will compare history with current state rather than change the accounts again.

## Verify the API family and your access

The **campaign engine** means the implementation that created and manages the review. ISC has different API families for different campaign implementations. These requests use the next-generation service path:

`/certification-campaigns/v1`

The older campaign and certification API families have different paths and contracts. An API contract describes the supported request paths, parameters and response fields. An ID from a legacy role-composition campaign must not be inserted into these requests just because both products use the word campaign.

Confirm the actual campaign engine and current operation contracts before sending. The selected next-generation operations are currently **experimental**: their contracts can change and they require the experimental header shown below. The v1 in the path does not itself mean an operation is stable.

Use an approved API client with an already prepared, valid **access token**. The token lets ISC identify the caller and check what they may read.

Identify the **caller**, the identity ISC sees when this token makes a request. Check its **user level**, such as Org Admin or Cert Admin, and its **scopes**, which limit the operations the token can perform. The caller also needs permission to read the selected review records. A token that works for one operation is not proof that it can read every record we need.

Check each operation's current Authorization details. Choose its listed read scope where available; the certification-list contract currently lists `idn:campaign:read` as a read option. That scope name belongs to the token's permissions, not the request's filters. Check the other operations individually.

An Org Admin or Cert Admin may be appropriate for a complete campaign investigation. A reviewer can read authorized assigned work through the documented routes, but that view may be narrower. A browser session and a token do not necessarily act as the same person.

Keep the token in your client's protected authentication settings. Keep secrets out of the URL, response evidence and course files. Credential preparation is a prerequisite; this lesson does not create or broaden credentials.

## Prepare a request you can explain

Use your approved training tenant's **API base URL**, recorded privately as apiBase. This is the API address for that tenant, rather than its browser address or the example host in documentation.

A request has a method, an address and optional parameters or headers:

- **GET** asks for information.
- The **path** identifies the resource beneath the API base URL.
- **Query parameters** narrow or page the returned results.
- **Headers** carry settings such as authentication and the requested response format.
- The **response** contains a status and the returned data.

For this lesson, use these headers:

```text
Accept: application/json
Authorization: Bearer {accessToken}
X-SailPoint-Experimental: true
```

The Authorization line shows what the client must send; configure it through the client's protected token setting. Replace symbolic names with verified actual values privately. Do not send the braces literally.

There is no request body for these GET operations. Start with an empty request, rather than an imported collection containing unrelated actions.

ISC returns **JSON**, a structured text format. An **object** groups named fields between `{` and `}`. A field can hold a value or another object. An **array** groups a list of records between `[` and `]`; an empty array is `[]`.

The campaign detail request returns one campaign object. The certification list returns an array of assigned-review objects. Open each object in your client's response viewer to inspect its fields.

For example, `campaignRef.id` means: open the `campaignRef` object, then read its `id` field. The dot describes where to look in the response. It is not part of a new ID you invent.

Save response bodies privately. Record the status separately, along with needed response headers such as X-Total-Count and Retry-After. Exclude authentication secrets.

## Read the parent campaign first

Send:

```text
GET {apiBase}/certification-campaigns/v1/campaigns/{campaignId}
```

Use the actual ID of the generated campaign, not its saved template ID.

Check the returned campaign against the interface: its identity, name, type and available state information must match the selected case. Record the request and observation time.

The **status** is the response's result code. A 200 response means this read succeeded. It does not prove that this is the campaign you intended. If the read fails, use the error checks below before following any IDs; an error message is not a campaign record.

If the result belongs to a different engine, tenant or object, stop and correct the binding. Do not try alternate versions until something returns a familiar name.

## Retrieve every assigned certification

Send:

```text
GET {apiBase}/certification-campaigns/v1/certifications
```

Enter the following in your client's query-parameter table:

| Parameter | Value |
|---|---|
| filters | campaignRef.id eq "{campaignId}" |
| limit | 1 |
| offset | 0 |
| count | true |
| sorters | name |

Read the filter as: return certifications whose `campaignRef.id` **equals** this campaign's ID. `eq` means equals. This keeps another campaign's assigned work out of our list.

Replace campaignId inside the filter with the actual campaign ID. Keep the quotation marks around that value. Let the client **encode** the parameters, converting characters such as spaces into a form the URL can carry. Enter the readable value in the parameter table; do not encode it first and then ask the client to encode it again.

`count=true` asks for the total in the `X-Total-Count` response header. `sorters=name` requests name order. These settings help us inspect and compare the pages; they do not select a different campaign.

This API filter syntax differs from the identity Search query used to create a campaign.

For a non-admin reviewer, also set **reviewer-identity=me**, as required by the list contract. Record that you are examining that caller's authorized view. Do not claim campaign-wide completeness unless the authority and visible scope establish it.

Check every returned record's campaignRef.id. It must match the selected parent.

### Keep reading until there are no more records

The **limit** is the maximum number of records in a response page. The **offset** is how many records to skip from the beginning.

With limit=1, offset=0 reads the first record. Offset=1 reads the next record. Offset=2 reads the third, if one exists.

Our small page size makes the completeness check visible:

1. Save the page, its record IDs and X-Total-Count when provided.
2. Increase offset by the number of records returned.
3. Send the same filtered request for the next page.
4. Continue until a successful response contains an empty array, `[]`. A failed request or blank response body does not confirm the end.
5. Compare the number of unique IDs collected with the reported total, when available.

A full page of one record requires another request. It does not mean there is only one record overall.

Keep the parent filter unchanged on every page. X-Total-Count describes the filtered collection visible to the caller. It is not the number of entitlement decisions or a guarantee of unrestricted visibility.

For this tiny case, allow at most ten page requests per collection, including the empty final page. If you cannot finish within that bound, stop and investigate the scope. This is a bound for this exercise, not an API limit.

If a record ID repeats, the total changes, or the campaign is changing while you read it, keep the capture marked incomplete. Sorting helps order records. It does not freeze the data while you read later pages. Arrange a stable read window and repeat the bounded capture, preserving the earlier observations.

## Follow each certification to its items

For every certification returned, save its actual ID and send:

```text
GET {apiBase}/certification-campaigns/v1/certifications/{certificationId}
```

Copy certificationId from the `id` of that returned certification, not from the campaign record. Verify its `campaignRef.id`, reviewer and available review-state fields. Do not assume the first returned certification contains all campaign work.

Then retrieve its items:

```text
GET {apiBase}/certification-campaigns/v1/certifications/{certificationId}/review-items
```

Set the query parameters limit=1, offset=0, count=true and sorters=certificationSubjectSummary.subjectName. Leave additional item, decision and completed filters unset so they do not hide the rejected or unfinished items.

Here the certificationId in the path selects whose assigned review you are reading. The sorter orders those items by the reviewed subject's name. Keep this certificationId fixed while you move through its item pages.

Use the same paging process through a successful empty final page. Start offset at 0 again for each certification's item collection. If one certification contains both Export items, its item requests use offsets 0, 1 and 2: two one-item pages followed by `[]`. This is an illustration of the paging rule; inspect how your actual review work is grouped.

Keep the item object's own id separately from the entitlement id. Check the current **response schema**, the documented arrangement and meanings of the returned fields, as you inspect:

| Field or group | What to match |
|---|---|
| type, decision, comments | The kind of reviewed access and its recorded decision/reason. |
| certificationSubjectSummary.subjectTargetId | The actual person targeted by this identity review. |
| certificationSubjectSummary.id | The subject-summary record; preserve separately from the person's ID. |
| reviewData.entitlement.id and reviewData.entitlement.sourceId | The exact entitlement object and source. |
| reviewData.entitlement.attributeName and reviewData.entitlement.attributeValue | The source field and permission value. |
| reviewData.entitlement.account | The account reference, including its actual ID and nativeIdentity, the account identifier used in the source system, when supplied. |

To follow a longer field path such as `reviewData.entitlement.account`, open `reviewData`, then `entitlement`, then `account`. Keep the item object's own `id` beside these nested details so you can trace which review item they describe.

For this fixture, expect ENTITLEMENT items and the two exact person-source-account-Export relationships from the starting table. The recorded decision values should be APPROVED for employee01 and REVOKED for employee02. Approve means keep the access; Revoke means request its removal.

Names and the literal value certlab-report-export help you read the response. The source, account and entitlement IDs establish which objects those values refer to.

Do not accept an identically named B permission, a different account, or a role/profile item as a match. If a required account association is missing or unclear, keep that mapping unresolved and inspect the supported detail evidence. Never fill the gap with a guessed ID.

Combine items only after retrieving every certification's complete collection. Retain certificationId plus reviewItemId so separate assigned work cannot be confused.

## Check decisions, sign-off and totals separately

A certification's **completed** field means all decisions have been entered. It does not by itself establish sign-off or account removal.

**Sign-off** is the reviewer's final submission. A saved choice can exist before that submission.

Read `phase` as the certification's stage, `reviewProgress` as its decision/submission progress and `dateSigned` as the recorded sign-off date when present. Compare them with the signed review in ISC. DECISIONS_COMPLETE indicates decisions are entered with sign-off still pending. SIGNED and dateSigned concern the final review submission; they do not establish whether the permission was removed.

Record the current reviewer and available item actor or reassignment evidence. When work moved between people, the current reviewer alone cannot establish who made every decision.

Use modified only for its documented modification meaning. It is not automatically the decision time, sign-off time or account-collection time.

For each certification, send:

```text
GET {apiBase}/certification-campaigns/v1/certifications/{certificationId}/decision-summary
```

Use no subject filter. Compare its entitlementDecisions counts with that certification's fully retrieved items. Then combine the summaries for the complete selected campaign scope.

Inside `entitlementDecisions`, `approved`, `revoked` and `acknowledged` count the recorded choices. `decisionsMade` counts choices already made; `decisionsTotal` includes both decided and undecided items. These are counts for this certification, not the whole campaign unless it contains all the campaign's work.

After combining every certification, our compatible completed case should total `approved=1`, `revoked=1`, `acknowledged=0`, `decisionsMade=2` and `decisionsTotal=2`. Those are expected totals for the supplied case, not an observed response.

If the totals disagree, first check the selected parent, caller visibility, missing pages, filters and observation times. Two captures of the same item are two observations, not two separate decisions.

## Compare the review with fulfillment and current access

The API tells us what was reviewed and decided. **Fulfillment** is carrying out the requested access change. To establish whether the rejection was fulfilled, inspect the existing matching manual task and source-result evidence.

Use the actual Task Manager record, full scope and recipient, the changed private file, successful collection and the account observations recorded for this case. Do not assume an API resource named certification-tasks is the same manual entitlement-removal task without verifying that contract.

The historical CSV result should show:

- Employee02's A Export absent.
- Read retained on all three A accounts.
- Employee01's A Export retained.
- A at four holdings and B unchanged at six.

This proves the simulated file result when backed by actual execution evidence. It does not prove a real reporting application's capability changed.

Now inspect the current accounts without changing them. If a later documented training reset restored A's five holdings, the current Export on employee02 can coexist with the earlier signed REVOKED decision.

Keep the sequence clear: review decision, historical removal, later reset, current observation.

If the old removal evidence is missing, today's account state cannot reconstruct it. Record that gap. Do not re-upload the file or submit another rejection just to make today's state resemble the old decision.

## Diagnose an unsuccessful read

Use the response to decide the next check:

| Status | First useful check |
|---|---|
| 400 | Parameter names, filter syntax, encoding and current request contract. |
| 401 | Missing, expired or invalid authentication. |
| 403 | Caller user level, token scope and authority for the selected object. |
| 404 | Tenant, engine, path/version and actual object ID; this alone does not prove deletion. |
| 429 | Read Retry-After, the response header telling you how long to wait, before another permitted attempt. |
| 5xx | A code from 500 to 599 indicates a server-side failure. Preserve the failed read and use a bounded retry or support investigation. |

An empty successful list also needs explanation: the filter, caller visibility and campaign binding may explain it.

For this small investigation, make at most two later retries of a failed read after addressing the cause or waiting as directed. If it still fails, preserve the gap and stop that read. Do not widen access, probe other tenants or change the campaign to make an unsuccessful read return data.

## Test the first-page conclusion

An investigator uses limit=1. The first review-item page contains an approval. They conclude there were no rejected items.

What is missing from that conclusion?

<details markdown="block">
<summary>Follow the collection</summary>

They have read one page rather than proved the complete scope.

Retrieve the remaining pages for that certification and all other certifications under the selected campaign. Preserve the campaign filter, correct caller view and actual item IDs.

Only then compare the complete set with the summary and interface. A successful request establishes that page, not the absence of records on later pages.

Even a complete list of decisions would still need separate sign-off and fulfillment checks.

</details>

This is a reasoning case, not a sample response from your tenant.

## Finish with a conclusion someone can verify

Create a private case note identifying the tenant alias, API family, actor/view, campaign ID, request parameters, capture times and each saved response.

State whether the parent/child links, all pages, item scope, decisions and sign-off reconcile with the interface. Record missing authority, unstable captures or unresolved mappings as gaps.

Keep historical removal, later reset and current access conclusions separate. Reference the actual existing evidence for each.

End the temporary local client session and remove its temporary token value according to your training process. Preserve evidence without authentication secrets.

There is no tenant-data reset in this investigation because it changed no tenant objects. Once the required checks agree, your explanation of the existing work can support a later bounded automation. Keep any incomplete part clearly recorded before relying on the capture.
