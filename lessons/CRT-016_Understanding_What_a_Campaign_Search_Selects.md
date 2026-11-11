# What does this search actually select for the campaign?

You need to review access for Finance people in Chennai.

You enter a search, see a list of results and use it to build a certification campaign. The search runs without an error.

Does that establish that it found the intended people?

You still need to know what kind of records it searched, which fields it checked, how the conditions were combined and which results were actually added.

A query can be valid and still answer a different question from the one you meant to ask.

## Start with the record you want back

In SailPoint Identity Security Cloud (ISC), an **identity** is a record representing a person. Their **accounts** hold access in applications. ISC collects information about those accounts through **sources**, which contain the connection settings and collected data for the managed systems.

An identity can have **attributes**, named pieces of information such as department and location, along with links to accounts and access.

A **query** is a search instruction. It describes the conditions a record must satisfy to be returned.

The **search category** is the kind of record you are searching: identities, entitlements, access profiles or roles, for example.

An **entitlement** describes a piece of access, such as permission to export reports. An **access profile** groups entitlements from one source. A **role** can group access profiles and direct entitlements.

If you search identities, a matching result is an identity. A condition about that person's account or access does not turn the returned result into an account or permission record.

If you search entitlements, a result is a record describing a permission. One permission definition can have many holders.

This matters when creating a **certification campaign**, which organizes access-review work. An identity-based selection chooses people; an access-item-based selection chooses access objects and uses their holdings to determine the included people. The campaign's starting route and search category need to agree.

## Tell Search where to look

Searching for the word Chennai without naming a field can match that word in places other than someone's location.

A **search field** identifies the particular information you want checked. In an identity search, `attributes.location` means the location value inside that identity's attributes.

The colon separates the field from the value to find:

`attributes.location:"Chennai"`

Here, Search is checking the location field. It is not looking for Chennai anywhere in every available record.

Technical field names matter. `attributes.location` and a guessed field called `location` are not interchangeable instructions. Field names are case sensitive, so use the name supported by the relevant search data model.

A **data model** describes how information is organized on a type of record, including its fields and related records.

An attribute mapping defines how an identity attribute gets its value from source information.

For our example, department and location are available as searchable identity attributes using the technical names `department` and `location`. The mappings and stored values are supplied facts for this example; another environment may use different attributes or values.

## Follow one query through the records

Here is the identity data currently available in Search.

| Identity | department | location |
|---|---|---|
| 1201 | Finance | Chennai |
| 1202 | Finance | Pune |
| 1203 | Operations | Chennai |
| 1204 | Finance | No value |
| 1205 | Finance Support | Chennai |

In these tables, No value means that no value is available for that field in the query data.

Suppose the requirement uses the complete department value Finance and the complete location value Chennai.

For supported text fields, `.exact` requests the complete text value. With the plain values shown here, it checks the whole value, including case.

The department condition is:

`attributes.department.exact:"Finance"`

This matches Finance. It does not match Finance Support.

The full query is:

`attributes.department.exact:"Finance" AND attributes.location.exact:"Chennai"`

Read it in two parts: the department must be exactly Finance, and the location must be exactly Chennai.

`AND` is a **Boolean operator**, a word that combines conditions according to a logical rule. With AND, both conditions must be true for the returned identity.

Identity 1201 meets both.

Identity 1202 meets the department condition but has Pune as its location. Identity 1203 meets the location condition but has Operations as its department. Identity 1204 has no location value to match Chennai. Identity 1205 has a different complete department value.

Only 1201 matches these supplied conditions.

The result follows from the actual fields and values. The fact that some other identities look related to Finance or Chennai is not enough to satisfy both tests.

## Quotation marks and exact matching do different jobs

Double quotation marks keep a value containing spaces together as a phrase. For example, `"Finance Support"` is one phrase.

A quoted ordinary text search is not the same as a case-sensitive whole-value match. The ordinary Finance phrase can also occur inside a longer value such as Finance Support.

That is why the earlier query used `.exact` for the complete department value.

Exact matching also brings a condition you must consider: `"Finance"` and `"finance"` are different exact strings. If both values represent the same business department in your records, a query accepting only one spelling can omit a person you intended to include.

Resolve the accepted values or the data quality; do not infer that the person belongs outside Finance just because the stored case differs.

Use double quotes for multiword values. Single quotes do not perform the same grouping job in ISC Search.

Also check whether the field supports `.exact`. It applies to supported text fields. A field storing true or false, such as an account's disabled flag, does not use it.

## What changes if you use OR?

`OR` means that either condition is enough. An identity satisfying both conditions still matches.

If you replace AND with OR in our department/location query, every row in the supplied table matches.

Finance people in Pune match through department. The Operations person in Chennai matches through location. Identity 1204 matches through department even though location is missing. Finance Support in Chennai matches through location.

That is a much broader result than Finance people in Chennai.

Use the operator that expresses the request, not the one that produces a convenient number of results. ISC Search expects these operator words in capitals. When conditions are written without an operator between them, the documented default is OR.

Now change the request to Finance or Operations people who are in Chennai.

Group the acceptable departments, then apply the location condition:

`(attributes.department.exact:"Finance" OR attributes.department.exact:"Operations") AND attributes.location.exact:"Chennai"`

The parentheses make the two department choices one group. The Chennai condition applies to that whole group.

The supplied matches are 1201 and 1203. Finance in Pune still fails the location requirement, and Finance Support is not one of the two exact department values.

Grouping makes the intended relationship explicit instead of leaving the reader to guess how several operators should be read.

These are Search query rules. Do not assume that another filter builder, an API parameter or a different product uses the same combination rules.

## An identity can contain several accounts

So far, each condition checked one value on an identity.

Account conditions need another step because one identity can have several accounts. Search needs to know which related account is being tested.

Consider identity 1301:

- Its Directory Production account is recorded with `disabled:true`.
- Its Directory Test account is recorded with `disabled:false`.

The disabled flag is a Boolean value: true records that the account is disabled; false records that it is not marked disabled.

A false disabled flag does not establish that a login will succeed. Other controls and account conditions can still matter.

A **nested query** checks information inside related records, such as the accounts belonging to an identity. In `@accounts(...)`, the part inside the parentheses supplies conditions about those account records.

Look at this query in the Identities category:

`@accounts(source.name.exact:"Directory Production") AND @accounts(disabled:false)`

The first part asks whether the identity has a Directory Production account. The second asks whether it has an account whose disabled flag is false.

Identity 1301 meets both separate tests. The production account satisfies the first; the test account satisfies the second.

But the request “has a production account that is not disabled” needs both conditions on the same account.

Put those conditions inside one account query:

`@accounts(source.name.exact:"Directory Production" AND disabled:false)`

Now an account must have the exact production source name and a false disabled flag to satisfy the nested query. Neither of 1301's accounts meets both, so this identity does not match.

```text
Identity 1301
    |
    +-- Directory Production account
    |      disabled: true
    |
    +-- Directory Test account
           disabled: false

Separate tests:
    Has a Production account?       Yes
    Has an account not disabled?    Yes

One-account test:
    Has a Production account
    whose disabled flag is false?   No
```

Follow each account separately. The production account has the required source but the wrong flag. The test account has the required flag but the wrong source.

The diagram explains why two separate successful account tests do not prove that a single account has both properties. It shows record relationships, not an ISC job sequence.

## The same field label can describe a different relationship

Inside `@accounts(...)`, `source.name` describes the source of that account.

On the identity record itself, `source.name` describes its **authoritative source**, the source used to establish that identity, such as a personnel source.

An identity established from a personnel source can also have accounts on Directory Production, Payments and other sources.

If your question concerns one of those linked accounts, checking only the identity's authoritative-source field asks a different question.

Read the full field path and its category. The word source alone does not identify which relationship you are testing.

The source names in our examples are supplied distinct labels. In actual selection, confirm the source's identifier as well when names could be repeated or changed.

## Found results still need to become campaign selections

Return to the grouped department query, which found identities 1201 and 1203.

In the applicable Search campaign flow, you can include all returned identities or choose specific identities. If you choose only 1201, the presence of 1203 in the search results does not prove that it was added.

Check the actual saved selection as well as the query.

The same distinction applies when searching access objects: finding three matching entitlements and adding one is a selection of that one object, not all three.

There is another boundary when the query uses account conditions. An identity returned because it has a qualifying production account is still a person record. That match does not, by itself, restrict the campaign to that account or its permissions.

**Access refinement** determines which access to include for the selected people. A **campaign filter** is a configured set of inclusion or exclusion criteria that can also affect the contents. Both need their own checks. Rules about which permissions or packages can be reviewed still apply to the generated work.

Then inspect the **preview**, the generated review work available before the campaign starts. Verify the actual people, access items, account context where needed and assigned **reviewers**, the people or groups responsible for assessing the access. Search success alone does not prove that the intended access reached the intended reviewer.

These campaign choices depend on the functionality available in your ISC environment. Check applicable selection and display limits before treating the complete-looking screen as a complete population.

## What if the query is right but the data is wrong?

Search checks the information available to it.

If identity 1204 really works in Chennai but its searchable location is empty, the exact query still has no Chennai value to match.

That result is consistent with the search data. It does not establish that excluding 1204 meets the business request.

First inspect the person's source record for the location value. Then check the mapping and the location actually recorded on the ISC identity. Finally inspect the value available in Search. Updates to records and their appearance in Search need not happen at the same instant.

Likewise, an application account's current state may differ from older collected information. Compare the correct source account and the relevant observation times before changing a query to hide the disagreement.

Do not replace AND with OR merely to make a missing person appear. That would change the selection rule for everyone else too.

Use expected inclusions and deliberate exclusions to test the rule. In our first query, 1201 should match; 1202 and 1203 should not. Review the missing-location case separately as a data question.

Counts help detect changes, but the actual identity references and matching values explain whether the result is right.

## Try a different combination

The request is:

“Select Finance people who have at least one Warehouse Production account that is not marked disabled.”

Here is the supplied Search data.

| Identity | department | Accounts and disabled flags |
|---|---|---|
| 1401 | Finance | Warehouse Production: false |
| 1402 | Finance | Warehouse Production: true; Warehouse Test: false |
| 1403 | Operations | Warehouse Production: false |
| 1404 | No value | Warehouse Production: false |

The fields, values and account associations are correct as shown. How would you express the requirement, and which identity should match?

The department condition concerns the identity. The production-source and disabled conditions must concern one of that identity's accounts.

Combine the identity condition with one account query:

`attributes.department.exact:"Finance" AND @accounts(source.name.exact:"Warehouse Production" AND disabled:false)`

Only 1401 meets both parts under the supplied data.

Identity 1402's test account cannot compensate for the disabled production account. Identity 1403 fails the department condition. Identity 1404 has no Finance value to match; investigate the missing department if this person is expected to belong to Finance.

Now suppose 1402's production account is changed, and Search subsequently contains `disabled:false` for that account.

The same query now matches 1402 as well as 1401. A relevant input changed, so the result changed without altering the query.

That new search result does not establish that an already generated campaign was updated. Inspect the actual generated work before claiming that either person's required account access is under review.
