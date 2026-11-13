# How do you use sensitive-data details in an access review?

An entitlement in a certification has a High Impact Score and a Health Information category.

Should the reviewer remove it?

Those details tell us to examine the data the permission reaches. They do not yet tell us whether the person's work requires that access.

Let's connect the classification information with the actual permission and the person's current duty.

## Establish what is being reviewed

SailPoint Identity Security Cloud (ISC) keeps an **identity** representing a person and associates their application **accounts** with it. A **source** is ISC's configuration for the system or account data being managed.

Our account is benefits-09 on Benefits Production. It holds Case-Document-Reader, an **entitlement** representing an access right.

The application owner confirms that this permission allows reading and downloading documents from the production benefits-case library. Those documents include health information. It does not allow changing or deleting the documents in this example.

A **certification campaign** organizes access reviews. A **certification** is an assigned review within it.

Here, Case-Document-Reader is individually reviewable, outside a larger package or another automatic assignment. The assigned reviewer is authorized to assess somebody else's access, and the review is open.

We know which held permission needs a decision. Now we need to understand the extra data information beside it.

## Read the data details together

**SailPoint Data Access Security**, or **DAS**, identifies and provides information about access to organizational data.

One part of this is **data classification**: examining information and applying categories according to configured rules.

With the supported DAS capability available, ISC can show **Impact Score**, **Policies** and **Data Categories** for entitlements. These fields describe the data reached through the access.

A **data category** is a label applied through classification, such as Health Information. It identifies a type of data found; it does not establish who is authorized to read it.

The **Impact Score** combines the sensitivity of the data with how many occurrences of that type of data are involved. It can be High, Medium or Low.

Think about why both factors matter. A permission reaching many sensitive records can expose more information than a permission reaching a small amount of less-sensitive data. The score helps draw attention to that exposure. It is not a rating of the employee or an instruction to select Revoke.

The **Policies** field identifies policies associated with the data. A **data classification policy** organizes the rules used to identify and categorize data. It helps explain why the data was classified; it does not establish this person's business need to read it.

For our example, the review shows a supplied High score, the Health Information category and a health-document classification policy. Read them as connected facts to investigate: what was classified, where it was found, and whether this permission actually reaches it.

## Understand where the category came from

For example, a rule can identify a type of sensitive information in a document and apply the relevant category when its conditions match. Policies organize those rules. Their configuration and the resources examined affect the results.

Classification describes what was identified in the data. Account permissions describe who can access it and what actions are possible.

Those are different kinds of evidence. A document classified as Health Information does not establish that benefits-09 can read it. Conversely, a confirmed broad document-reading permission does not prove that every document has been classified recently.

The connection needs checking.

## Check the evidence for the correct resource

The reviewer opens **Certifications > Active**, selects the assigned review and inspects its entitlement information. Where the DAS context is available, examine the score, policies and categories attached to the actual entitlement.

If the detail needs clarification, ask the person responsible for DAS classification to investigate the matching resource. That person needs their own authorized DAS access; being an ISC reviewer does not establish it.

In DAS, **Forensics > Data Classification** provides classification results. The authorized investigator can filter by application/resource and the relevant policy or category.

Ask for the production library's relevant classification result, including the resource, category, rule or policy, and **Last Updated** information.

Here, Last Updated describes when the file was classified into that category. It is not the date the person last read it or the date the account's permission was checked.

Then ask the application or data owner to confirm that Case-Document-Reader really reaches that production library, with the reading and download capabilities described earlier.

For our case, those checks agree: the classification concerns the intended production documents, and the account's held permission reaches them. The dates are appropriate for this review.

Do not assume that correcting a classification result automatically refreshes an existing ISC review. After a correction, check what the actual review presents and agree on supported handling with the campaign administrator.

## Decide whether this person needs the capability

The responsible business owner confirms that this person's current duty includes handling individual employee benefits requests and reviewing the supporting health documents.

The approved duty requires reading and downloading those documents on benefits-09. The scope of that authorization has been checked.

Here, we can explain why the person should keep the access even though the score is High. Their approved work requires this sensitive information.

The reviewer can record **Approve**, accepting continued access to the reviewed entitlement, with a reason connecting the case-handling duty to the confirmed production-library capability.

A useful reason identifies that current duty and the evidence used. “High score reviewed” would not explain why this person should keep the access.

The information connects like this:

```text
Classification evidence
  What data was identified?
  Which resource and classification date?
                  |
                  v
Confirm the reviewed permission reaches that data
  Correct source, account, resource and capability
                  |
                  v
Compare with the person's current approved work
                  |
          +-------+--------+
          |                |
          v                v
Approved work needs   Permission allows more
this permission       than approved work needs
          |                |
          v                v
Explain why access    Plan the right access
should stay           and review decision
```

The category and score explain the data exposure. The permission check establishes what the account can do. Current authorized work supplies the reason for the decision.

## When the person's duty becomes narrower

Now change the duty. The person no longer handles individual cases and is authorized only to read summary totals.

The Health Information category remains accurate. The production documents have not become less sensitive merely because this person's responsibilities changed.

Their new duty no longer justifies reading and downloading individual case documents.

Establish whether an available, separately authorized permission can provide the required summaries. Coordinate that arrangement with the responsible access owner and permitted operators.

The reviewer must decide on the actual Case-Document-Reader entitlement. **Revoke** records that it should be removed. It does not automatically grant a replacement permission or prove that the application has already changed.

Preserve the approved summary work in the plan, follow the required removal, and verify the account's resulting access. Changing a description or removing a category would not reduce the permission's real capability.

## When the score is Low or missing

A Low score still needs interpretation. It does not establish that the permission is harmless or appropriate for this person.

If the score or category is absent, ask the responsible administrator to check whether the feature is available, whether the information concerns the correct library, and which documents were classified. An empty field has not established that no sensitive information exists.

Likewise, a classification result for a test library does not explain production data, even when the library names look alike.

Suppose someone proposes approval because a test folder has no Health Information category and the production review's score is blank.

First identify the exact production library and the entitlement reaching it. Establish what information is currently classified there and whether the available result covers the relevant documents.

Then connect the actual permission to the person's approved work. Until those facts are established, neither the test result nor the blank score supplies a reason to keep broad production access.
