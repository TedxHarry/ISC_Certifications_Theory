# How does application access become information ISC can review?

A reporting account belongs to two groups. One allows viewing reports; the other allows exporting them.

A reviewer needs to see whose account this is, which access it holds and what that access permits. The application already knows about its account and group memberships. ISC needs to collect and connect that information before it can present a useful review.

Let's follow those connections.

## Begin with the application's account record

An **account** is a record in a particular system. **Access** is what that account can do.

In SailPoint Identity Security Cloud (ISC), an **identity** represents the person and connects information about them with their accounts and access.

For this example, the person's identity already exists in ISC. We are adding information about their reporting account.

The reporting system supplies these account values:

| Field | Example value | Meaning here |
|---|---|---|
| accountId | report-014 | The identifier of this account in the reporting system |
| login | reports-user-14 | The account's login name |
| staffNumber | 1007 | The personnel number used to associate this account with its person |
| groups | RPT.VIEW, RPT.EXPORT | Two group memberships held by the account |

These are illustrative field names for this source. A different system can use different names and representations.

The application's access configuration establishes that RPT.VIEW allows viewing reports and RPT.EXPORT allows exporting them. We are not guessing the rights from the group names.

The account already has those memberships. Reading them into ISC will record existing access; it will not grant the permissions for the first time.

## The source tells ISC what it is managing

A **source** is ISC's configured representation of a system or collection of account data. The reporting application and the source configured in ISC are different things.

The application holds the actual account. The source configuration tells ISC how to work with information from that system.

A **connector** provides the integration: how ISC communicates with that type of system or reads its account-data file.

A directly connected source can read account information from the application through its supported connection. A file-based source imports a file representing the accounts.

The available operations depend on the connector and configuration. Being able to read an account does not establish permission or support for changing it.

That distinction matters even before a review. A source can provide useful access information while removal later requires separate manual work.

## The schema gives the fields their meaning

An **attribute** is a named piece of information, such as staffNumber or groups.

The **account schema** defines the account attributes ISC uses and how those attributes are interpreted. It identifies the account and describes details such as whether a field can contain multiple values or represents entitlements.

For this example, the schema uses accountId as the Account ID and login as the Account Name.

The Account ID is used to reference the account. A familiar login name alone is not enough to distinguish every account across every source. Keep the source and the account identifier together.

An **entitlement** is an access right represented from a source. In this example, each group membership is represented as an entitlement because that membership provides the corresponding application access.

The schema also marks groups as a **multi-valued** entitlement attribute. Multi-valued means one account can hold several values in that field. Here, those are RPT.VIEW and RPT.EXPORT.

Marking the membership field correctly matters. If a field is only treated as ordinary text, you cannot assume its values are also being interpreted as held access.

The schema must agree with the actual data the connector provides. A field named groups in one integration does not make groups the universal field name for every application.

## Account aggregation reads who holds what

**Account aggregation** brings account information into ISC through the source's supported collection process.

For our reporting account, the incoming values identify report-014, its login, staffNumber and both group memberships. ISC processes those values according to the configured schema.

The result is an account record in ISC that represents the reporting account and its collected access values.

This is the account-to-access connection: report-014 holds RPT.VIEW and RPT.EXPORT as represented by the collected data.

A completed aggregation status is useful evidence that a collection operation finished. It does not, by itself, prove that every intended account or attribute was included correctly.

For example, an account filter can limit which accounts are read. An incorrectly configured field can leave out a membership value. To establish that the right data arrived, inspect the relevant account and values rather than relying only on a successful operation label.

For a file-based source, the file itself also matters. Importing yesterday's file again does not turn yesterday's account information into a current observation.

## Entitlement information answers a different question

The account data tells us that report-014 holds RPT.EXPORT. We also need information explaining that access item.

An **entitlement catalog** is the collection of represented entitlement records and their details. A record can identify the entitlement, give it a display name and describe what it permits.

Where supported, **entitlement aggregation** collects information about the entitlement objects themselves. That is different from reading an account's memberships.

For the reporting source, suppose the catalog contains RPT.EXPORT with the display name Export reports and an established description of its capability. The record belongs to an entitlement type called groups.

The **entitlement type** identifies the category of access represented here. In this source, the type is groups. Other sources can have other types.

The account's group value must link to the correct entitlement record. In the supported schema-linking model, the account attribute is marked as an entitlement, its name matches the entitlement type and its value matches that entitlement's identifier.

For this example, groups and RPT.EXPORT match the catalog's type and identifier. The source also identifies which reporting system those values belong to.

Now ISC can connect “this account holds RPT.EXPORT” with “this is the reporting-source entitlement described as Export reports.”

Both connections are needed. A catalog entry for Export reports does not prove that report-014, or any particular account, holds it. Collecting more descriptions cannot substitute for missing account membership information.

Not every source supports a separate entitlement aggregation. Check what account and entitlement information the actual source can collect rather than assuming that every integration has identical jobs.

## Correlation connects the account with its person

We now have an account and its represented access. Who owns that account?

**Account correlation** matches and associates a source account with an identity in ISC.

The existing identity in our example has staffNumber 1007. The configured correlation criteria compare the account's staffNumber with the identity's staffNumber. The supplied values match the intended identity uniquely.

The account is therefore associated with that identity under the supplied configuration.

This adds the person-to-account connection. The identity matched through staffNumber 1007 is associated with report-014 on the reporting source, with login reports-user-14. That account's collected membership RPT.EXPORT links to the reporting-source entitlement.

Correlation does not decide whether the person should keep export access. It establishes whose represented account is involved.

If the association is wrong, accurate account permissions can be presented in the wrong person's context. If an account cannot be matched to an identity, it is **uncorrelated**.

An uncorrelated account can still exist and hold access in the application. Missing a person association is not evidence of zero access. It needs the appropriate ownership investigation or supported account-review handling.

Also distinguish changing correlation configuration from changing existing account associations.

An **optimized aggregation** checks account records for changes and can skip those whose data is unchanged. Correlation is not reevaluated for those skipped records. Where supported, an **unoptimized aggregation** reexamines unchanged records for correlation too.

That difference explains why saving a matching rule and running an optimized aggregation does not prove that old associations were corrected. Use the appropriate supported reprocessing for that source, and inspect the actual association afterward.

## Now check what reaches the review

A **certification campaign** organizes assigned access reviews. A **certification** is one assigned review, and a **review item** is the particular access presented for a decision.

The **reviewer** is the person assigned to assess whether that access remains appropriate.

The **access model** includes the configured access packages and assignment requirements. **Certifiable access** is access eligible for review under that model. Having an entitlement represented in ISC does not make every component a separate review item.

Some access is managed through a containing package or an automatic requirement. The campaign's selection also determines which people or access it is intended to review.

For our example, RPT.EXPORT is individually reviewable, has no containing package or automatic requirement retaining it, and is included by the campaign's selection. An appropriate reviewer is assigned and is not reviewing their own access.

Generation produces an item connecting the intended identity, report-014 and its export entitlement.

The reviewer can inspect the person/account context and the entitlement's meaning, then investigate whether exporting reports remains appropriate for the person's current work.

Collection, interpretation and association have made the question possible to ask. They have not supplied the business answer.

## See the connections together

The arrows below follow information and dependencies. They do not describe a fixed sequence of internal batch jobs or promise that every screen updates immediately.

Entitlement information and the identity association can come from their supported processing paths. Both must fit the account information before you rely on the resulting person/account/access context.

```text
Application account values
            |
            v
Connector + account schema
            |
            v
Collected account in ISC
  + entitlement information
  + identity association
            |
            v
Person / account /
held access
            |
            v
Campaign selection and
certifiable-access rules
            |
            v
Generated review item
```

The source account record, the entitlement record, the identity association and the generated review are different records. Finding one of them is not proof that every connection is correct.

## Check when each piece of information was observed

Suppose account aggregation reads RPT.EXPORT at 08:00. A campaign generated at 09:00 includes it for review.

At 10:00, an authorized application administrator removes that membership directly in the reporting system.

The account data collected at 08:00 still describes the earlier state. The generated review also has a history of the access it was created to assess.

Seeing RPT.EXPORT in either of those earlier records does not, by itself, establish that the membership remains in the application after 10:00.

Now suppose a supported collection and processing run after the removal confirms that report-014 no longer holds RPT.EXPORT. That supplies newer represented account information.

Do not assume the historical review item must disappear simply because current account data changed. Inspect the account observation and review context separately.

The reverse timing problem matters too. If export access was added after the account data was read, the older collected record cannot establish that the account lacks it now.

A display name that looks current and a freshly opened page do not tell you when the underlying account information was collected.

## Find the first missing connection

If the application account has export access but ISC's account record lacks that value, start with what the source actually returned and how the schema interpreted it.

Was the intended account read? Did the membership field contain RPT.EXPORT? Was that field interpreted as entitlement data?

If the value is present on the correct ISC account but appears under the wrong person, investigate the identity association. Rewriting the entitlement's description would not correct account ownership.

If the entitlement exists in the catalog but no membership is represented on this account, distinguish the definition from the holding. Another entitlement aggregation is not proof that it will supply the missing account value.

If the correct identity/account/access relationship exists but the generated review lacks the item, inspect the campaign's actual scope, generation context and certifiable-access rules. A missing review item is not automatically a collection failure.

Each observation points to a different record. Establish where the expected information stops before choosing a correction.

## Try a different source and field name

A payment-system account pay-088 is correctly associated with its identity. A current account extract contains a permissions field with the value INV.APPROVE, meaning permission to approve supplier invoices.

The source's account configuration still expects a groups field for entitlement memberships. In the supplied ISC account record, INV.APPROVE is not represented as held access.

The entitlement catalog does contain INV.APPROVE with a useful Invoice approval description. The current campaign has no invoice-approval item for this account.

Does the catalog prove that this account's access has reached the review correctly? Should you start by collecting the entitlement descriptions again?

No. The catalog establishes information about the access object. The missing connection is the account's membership value being represented through the configured account-data path.

Compare the actual permissions field returned for pay-088 with the source's extraction, mapping and schema interpretation. Verify the supported configuration needed to represent that field as entitlement information.

After the appropriate correction and supported processing, inspect the exact account's held-access value and identity association. Then validate whether the applicable campaign includes that access under its selection and review rules. Do not assume an existing campaign's contents were repaired merely because a source setting was saved.

Now change one fact. A later, accurate collection shows that pay-088's permissions no longer include INV.APPROVE, while the entitlement catalog still contains its definition.

The catalog can retain that entitlement because the access object still exists. Its presence does not make pay-088 a holder again.

The useful evidence remains the connection between the current account, its collected membership values and the correct identity, followed by the review's own contents and timing.
