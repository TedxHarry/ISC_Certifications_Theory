# How does application access become information ISC can review?

A reviewer sees an item called Export reports. Behind that item, SailPoint Identity Security Cloud (**ISC**) needs to know which account has the permission, what the permission allows and which person the account belongs to.

Those details do not all come from one description. The account supplies its memberships. Information about the access item explains those memberships. The identity link connects the account to its person.

Let's follow those connections for one reporting account.

## Begin with what the application already knows

An **account** is a person's record in an application or system. Its **access** determines what someone using that account can do.

ISC keeps an **identity** representing the person. It connects information about them with their accounts and access. In this example, the identity already exists in ISC; we are collecting information about their reporting account.

The reporting application supplies these values:

| Field | Example value | What it tells us here |
|---|---|---|
| accountId | report-014 | Which account this is in the reporting system |
| login | reports-user-14 | The account's login name |
| staffNumber | 1007 | The personnel number available for matching the account to its person |
| groups | RPT.VIEW, RPT.EXPORT | Two separate group memberships held by this account |

A **group membership** means the account belongs to that group. Here, the groups field lists two memberships for one account. Each membership gives the account the access configured for that group.

The field names are examples for this source. Another application can use different names and data formats.

For the reporting application, its access configuration establishes that membership in RPT.VIEW allows viewing reports and membership in RPT.EXPORT allows exporting them. We know those meanings from the application configuration, rather than guessing from the group names.

The account already has both memberships. Collecting them in ISC will describe existing access; it will not give the account these permissions for the first time.

## Use a source and connector to collect the information

A **source** is the configuration in ISC for the system or collection of account data being managed. The reporting application holds the actual account. The reporting source in ISC provides the settings for working with that account information.

A **connector** supplies the integration: the way ISC communicates with that type of application or reads its account-data file.

For a directly connected source, ISC reads account information through the supported connection. For a file-based source, it imports a file representing the application accounts.

Both routes can provide information for a review. Neither route, by itself, proves that ISC can change the application's permissions. Reading the memberships and removing a membership are different operations. Their support and authorization depend on the actual source and configuration.

A source can therefore supply useful review information even when a later removal needs someone to make the change manually in the application.

## Explain what each returned field means

The connector can return accountId, login, staffNumber and groups. ISC needs configuration explaining how to use those fields.

A named piece of information like staffNumber is an **attribute**. Its value for this account is 1007. The attribute name tells us which piece of information we are discussing; the value tells us what was returned for this account.

The **account schema** defines the account attributes ISC uses and how it interprets them. It identifies which values refer to the account and which fields describe access.

In this example, the schema uses accountId for the **Account ID** and login for the **Account Name**. ISC can therefore reference account report-014 and show its readable name reports-user-14.

Keep the source with that account reference. A readable login can also exist in another system, so the login alone does not identify an account across all sources.

Now consider groups. The application uses these memberships to provide access. ISC represents an access right from a source as an **entitlement**. Here, the group memberships are the entitlement values held by the account.

The schema marks groups as an entitlement attribute. It also marks it as **multi-valued**, meaning that one account can have more than one value in that field. The connector returns two group values for report-014: RPT.VIEW and RPT.EXPORT.

These settings help ISC interpret the values as the account's access memberships. An ordinary field such as staffNumber has a different job. Storing that field as account information does not turn its value into a permission.

The settings must agree with the data the connector actually provides. Configuring a field called groups will not supply memberships from a differently named field unless the supported extraction or mapping connects that data correctly.

## Account aggregation tells ISC what this account holds

**Account aggregation** collects account information into ISC through the source's supported process.

For report-014, the collected data includes its login, personnel number and the two group values. ISC uses the configured schema to interpret that data and represent the account and its access.

We can now inspect the account record in ISC and establish whether it contains RPT.VIEW and RPT.EXPORT.

A completed aggregation tells you that the collection operation finished. To establish that the intended access arrived correctly, you still need to inspect the account and its values.

For example, an account filter could exclude report-014 from collection. A field configuration could miss its memberships. The operation could finish without establishing the particular account/access connection you expected.

For a file-based source, also check which file was imported and when its information was obtained. Importing an old file again does not turn its account data into a current observation.

## Entitlement details explain the access item, not who holds it

The account information tells us that report-014 has RPT.EXPORT. We also want to connect that value with a useful description of the access.

An **entitlement catalog** is the collection of entitlement records and their details. For this source, suppose it contains a record identified by RPT.EXPORT, displayed as Export reports, with a description explaining that it allows someone to export reports.

That record describes the permission. It does not, by itself, establish that report-014 has it. Another account could have the permission, or the access item could exist without this account being a member.

Where supported, **entitlement aggregation** collects information about the entitlement objects themselves. Account aggregation and entitlement aggregation therefore answer different questions: what the account holds, and what the access objects are.

Some sources do not support a separate entitlement aggregation. Check the actual source's supported collection paths instead of expecting every integration to have identical jobs.

## Link the account value to the correct entitlement record

The reporting-source entitlement record has a type called groups. An **entitlement type** identifies the category of access being represented. Here, the category is group membership.

For the account value to connect with this source's entitlement record, these details must agree:

- The account's groups attribute is marked as entitlement information in the schema.
- The attribute name groups matches the entitlement type groups.
- The collected value RPT.EXPORT matches the entitlement's identifier RPT.EXPORT.

The source keeps this match in the reporting system's context. A similar value on another source would need its own source context.

Those details connect two useful facts: report-014 has the RPT.EXPORT membership, and the reporting-source entitlement with that identifier is described as Export reports.

A good description cannot replace the account's missing membership value. If the catalog contains Export reports but the account record does not show that membership, collecting the description again has not established that this account holds it.

Likewise, a returned group value needs the correct interpretation and access meaning. The name alone is not a reason to assume it matches whichever catalog description looks familiar.

## Match the account to the person's identity

The next connection concerns whose account report-014 is. **Account correlation** matches and associates the account with an identity in ISC.

The existing identity in this example has staffNumber 1007. The configured comparison uses the account's staffNumber and the identity's staffNumber. Here, both records contain 1007, and no other identity matches that number. The comparison therefore identifies the intended person.

Under those conditions, the account is linked to the correct person's identity. We can connect that person with report-014 on the reporting source, and that account with its collected RPT.EXPORT membership.

The number 1007 identifies the person for this configured match. It does not identify the export permission or establish that the person needs to keep it.

If the link is wrong, accurate account permissions can appear in the wrong person's context. If ISC cannot match the account to its established identity, the account is **uncorrelated**, meaning that it has no identity link. The application account can still exist and hold access even though the person link is missing.

Investigate the ownership information or use the appropriate supported account-review process. Do not treat an unmatched account as evidence that nobody has its permissions.

## Changing a matching rule does not prove existing accounts were rechecked

Suppose a matching configuration needs correction. Saving the corrected setting changes the instruction ISC should use. You also need to establish whether the relevant existing account was examined under that instruction.

An **optimized aggregation** checks account records for changes and can skip further processing of unchanged records. Correlation is not reevaluated for those skipped records.

That means an account can remain associated as before if its returned data has not changed and it is skipped, even though the correlation settings were changed.

Where supported, an **unoptimized aggregation** reexamines unchanged records for correlation as well. Use the appropriate supported reprocessing for the source and situation, then inspect the account's actual identity association.

The evidence you need is the resulting correct link. A saved configuration and a completed optimized run do not, on their own, establish that the old association was corrected.

### What if someone linked the account manually?

An account can also be linked to an identity through **manual correlation**. This means someone explicitly assigned that account to the identity, rather than relying only on the configured attribute match.

ISC preserves that manual link even when the account's matching information changes. An unoptimized aggregation does not remove the manual correlation. Rereading the account is therefore not enough to assume that it will move to a different person.

Suppose report-014 was manually linked to the wrong identity. Its staffNumber is 1007, and the correct matching configuration identifies the intended person. After an unoptimized run, the account is still linked to the wrong identity.

In this changed situation, the retained manual link explains why a correct comparison has not moved the account. Establish how the link was created and confirm the actual owner. An authorized person then needs to use the supported correction for that manual association and inspect the resulting identity link.

Correcting the account's association in ISC is different from deleting the account in the reporting application. The ownership correction must put report-014 under the right person; it does not, by itself, decide whether its export permission should remain.

## Check what the campaign actually presents for review

We now have account membership information, matching entitlement details and the correct identity association. These connections tell us what access ISC can represent for the person.

A **certification campaign** organizes access reviews. An administrator selects which people or access should be included.

When ISC prepares the campaign, it creates the review work. A **certification** is an assigned access review within that campaign. The person responsible for that review is its **reviewer**.

Inside the assigned review, each **review item** presents access for a decision. For example, an item can show this person's export permission on report-014. The reviewer assesses whether the person still needs that access for their work.

Having a permission represented in ISC does not automatically mean it will appear as its own review item.

The **access model** describes how access is organized and assigned in ISC. A permission can be included in a larger package of access. A configured rule can also require the person to have certain access automatically.

These relationships affect the review. ISC may present the larger package for a decision rather than each permission inside it. Access required by an automatic rule may not be available for individual removal through a certification.

**Certifiable access** means access eligible for review under the applicable rules. The campaign's selection also needs to include the intended access.

For this example, RPT.EXPORT is individually reviewable. It is not part of a larger package that must be reviewed together, and no configured automatic rule requires the person to keep it. The campaign includes the intended person and access, and a suitable reviewer is assigned without reviewing their own access.

When ISC generates the review work, it produces an item connecting the correct identity, report-014 and the export entitlement. The reviewer can inspect those details and investigate the person's current reporting need.

Collecting and connecting the information makes that question possible. The current business reason for keeping or removing export still needs to be established by the review.

## Put the connections together

```text
Reporting account values
            |
            v
Connector reads the data
Schema interprets the fields
            |
            v
Collected account record
  + matching access details
  + correct identity link
            |
            v
Person / account /
held access
            |
            v
Campaign selection and
eligible review unit
            |
            v
Generated export review item
```

The arrows show information and dependencies. They do not prescribe a fixed order of internal batch jobs or promise that every screen updates immediately.

Entitlement details and the identity link can come through their supported processing paths. Both need to fit the collected account information before you rely on the resulting review.

The account record, entitlement record, identity link and generated item remain different records. Finding one of them does not establish that all the other connections are correct.

## Compare the time of each observation

Suppose an account aggregation reads RPT.EXPORT at 08:00. A campaign generated at 09:00 includes that access for review.

At 10:00, an authorized application administrator removes the membership from report-014 in the reporting system.

The 08:00 account data describes the account before that removal. The generated review also records the access it was created to assess. Seeing the membership in those earlier records does not establish that it is still present after 10:00.

A later supported collection and processing run confirms that report-014 no longer holds RPT.EXPORT. That supplies newer account information in ISC.

Inspect the generated review and the current account information according to the time each represents. Do not assume that a historical review item must disappear when the account changes.

The reverse matters too. If the application granted export after the 08:00 collection, that older record could not establish that the account lacks the permission now.

These times show the order of events in this example; they do not predict how long a real collection or campaign takes. A freshly opened page or a readable display name does not tell you when the underlying account data was collected.

## Find the connection that needs investigation

If the application account has export but ISC's account record lacks RPT.EXPORT, compare what the source returned with how the schema interprets it. Establish whether the intended account was read, whether its membership field contained the value and whether that field was treated as entitlement information.

If the correct value is on the ISC account but appears under the wrong person, inspect correlation. Changing the entitlement's description would not correct the account's identity link.

If the entitlement is in the catalog but no membership is shown on this account, check the account-data path. Another entitlement aggregation can collect access-object information without supplying the missing account membership.

If the correct person/account/access connection exists but the generated review lacks the item, inspect campaign selection, whether the access can be reviewed separately, and what information was captured when the review was generated. A missing review item does not, by itself, establish that collection failed.

The next check follows the missing connection. First identify which record or relationship is absent or wrong, then choose the appropriate correction.

## Work through a different source and membership field

A payments account named pay-088 is correctly linked to its identity. A current account extract has a field called permissions containing INV.APPROVE, meaning permission to approve supplier invoices.

The source configuration still expects entitlement memberships in groups. In the ISC account record, INV.APPROVE is not shown as access held by pay-088.

The catalog does contain INV.APPROVE with an Invoice approval description. The campaign has no invoice-approval item for this account.

Explain why the catalog is not enough to establish that the account's access reached the review. What would you inspect first, and what would you need to verify after a correction?

The catalog describes the access object. The account extract supplies a membership in permissions, while the configured account-data path expects groups. The missing connection is the account's membership being interpreted and represented correctly.

Compare the returned field with the source's extraction, mapping and schema interpretation. Establish the supported configuration needed to treat the actual membership field as entitlement information. Do not assume that collecting the entitlement description again will repair the account-data mismatch.

After the appropriate correction and supported processing, inspect pay-088's actual held-access value and correct identity link. Then check whether the campaign includes that access under its selection and review rules. Saving a source setting does not prove that an already generated campaign was repaired.

Now change one fact. A later accurate collection shows that pay-088's permissions no longer include INV.APPROVE. The catalog still contains the entitlement definition.

Those records can agree. The catalog says the access object exists; the newer account information says pay-088 no longer holds it. Keeping the definition does not assign the permission back to that account.

Use the current account membership, its correct identity and the review's own contents and timing to explain what has actually been established.
