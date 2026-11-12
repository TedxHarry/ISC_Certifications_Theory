# What makes a decision explainable later?

A review item shows Approve. Its comment says “Required.”

Someone checking the decision later can see the choice, but they still cannot tell what work required the access, what the reviewer checked or whether the explanation applies to this account.

A useful reason connects the access to the facts that justified the decision. It lets another person follow that connection without having to guess what the reviewer meant.

## Begin with the access and the person's current work

SailPoint Identity Security Cloud, or **ISC**, keeps an **identity** representing a person and associates their application accounts with it. An **account** is a record in a particular system. Its permissions determine what someone using it can do.

For this example, identity 4101 owns account `case-4101` in Support Production. ISC manages its collected account information through a **source**, the configuration representing the application or account-data collection.

The account holds two **entitlements**, access rights represented from that source:

- **Read Cases** allows reading the customer cases assigned to the person.
- **Case Bulk Export** allows downloading all customer case records, including contact details.

These capabilities have been confirmed in the application. The current account information and its association with identity 4101 have also been checked.

A **certification campaign** organizes access reviews. A **certification** is an assigned review within it, and a **review item** is the unit presented for a decision. Here, the two entitlements are separate, individually reviewable items. Neither is included through a package, required by an automatic assignment or supplied through another assignment in this example.

The certification is active and unsigned, meaning its decisions have not been finalized. An authorized reviewer who understands the access is reviewing somebody else's access.

The person's current duty is to answer assigned customer cases. The responsible business owner has confirmed this duty and its access needs in evidence record C-71. Reading assigned cases is authorized; downloading every customer's case records is not needed or authorized for that duty.

Under these facts, the reviewer can explain keeping Read Cases and removing Case Bulk Export. **Approve** accepts continued access to the reviewed item. **Revoke** records that the reviewed access should be removed. The reason for each choice comes from the difference between the two capabilities and the current work.

## Use a decision rule that the organization has actually agreed

**Decision criteria** are the conditions used to judge whether the access is appropriate.

For this example, the organization has agreed this rule: keep access when the person's current authorized task requires its capabilities on the reviewed account. A confirmed absence of that need requires a removal decision unless the organization's process establishes another authorized reason to retain it.

That is an example business rule for the review. It is not a built-in ISC field or an automatic campaign filter. A **campaign filter** selects which review content is included or excluded. Decision criteria help a human judge access that is already under review.

Follow your organization's actual criteria. A reviewer should not invent a new rule such as “Approve everyone in Support” simply because the department name is easy to check. The same department can contain people who need very different permissions.

The rule also needs facts. If you do not know whether an access item is still needed, that is a gap to clarify. It is different from having confirmed that the need has ended. Writing a confident reason cannot supply missing evidence.

## Turn the facts into a useful comment

A **decision comment** is the explanation recorded with an access-review decision. It should help someone understand why the choice fits the actual item.

Compare these comments for our two items:

| Item and choice | Comment that leaves a gap | Comment that explains the decision |
|---|---|---|
| Read Cases: Approve | Required. | Current duty is answering assigned customer cases. Business-owner confirmation C-71 establishes the need for Read Cases on case-4101; the permission's assigned-case scope matches that work. |
| Case Bulk Export: Revoke | No longer required. | C-71 confirms the current duty needs assigned-case reading, with no authorized need to export all customer cases and contact details. Remove Case Bulk Export from case-4101; retain the separately reviewed Read Cases permission. |

The stronger comments name the relevant work, connect it to the permission and identify the evidence used. The removal comment also makes the intended boundary clear: remove export while preserving the separately justified reading permission.

You do not need to repeat every field already attached to the item. The person, account, source and access record supply important context. Add the reasoning that those identifiers cannot supply on their own.

An evidence reference such as C-71 should lead an authorized person to the actual confirmation through the organization's record-keeping process. An unexplained ticket number that nobody can retrieve is a weak substitute for the facts. Keep the reference precise enough to find the relevant confirmation and establish that it was current when the decision was made.

Keep unnecessary sensitive contents out of the comment. For example, refer to the confirmation of access need rather than copying customer records or credentials into the explanation.

There is no useful minimum essay length. A short, accurate explanation with a usable evidence reference is better than a long paragraph that says only “approved after review.”

## A mandatory comment still needs a real reason

Campaign settings can determine when reviewers must leave comments. The review may therefore require an explanation for a particular choice before it can be submitted.

That setting helps collect reasons. It does not establish that the text is correct. “Approved,” “OK” or a copied statement about the wrong task can fill a comment field without explaining the decision.

Read the campaign's requirement and record the reason at the appropriate decision. If comments are optional, the question remains whether the retained review evidence is sufficient to explain this choice. Optional text does not make the underlying reasoning optional.

Some review types need instructions for a change as well as a reason. A **role** is an access package that can include entitlements and access profiles. An **access profile** bundles entitlements from one source. A role-composition review examines the role's shared contents and membership requirements, rather than one person's assignment alone.

For that kind of review, a removal decision needs an explanation of why and how the role should change. “Remove access” gives the person doing the manual work little help. State the confirmed problem, the intended change to the relevant part of the role and the access that should remain. Check the actual task assignment to establish who will make the change.

A comment describing a proposed correction is still an instruction or explanation. It does not establish that the role or an application account has already changed.

## Bulk decisions need a reason that holds for every selected item

A **bulk decision** applies a decision to multiple selected review items in one operation. Where the supported interface or approved tool offers this, it can reduce repeated submission work. It does not reduce the need to establish whether each item belongs in that decision.

Consider these four items. Their current data, correct person/account associations, individual review eligibility and authorized non-self reviewer have been checked. Their assigned certification is active and unsigned, with no package, automatic or alternative assignment affecting the example.

| Item | Person, account and permission | Current confirmed facts | Choice justified by the example criteria |
|---|---|---|---|
| I1 | 4101, case-4101, Read Cases | C-71 confirms current assigned-case work needs this permission. | Approve |
| I2 | 4102, case-4102, Read Cases | C-72 confirms current assigned-case work needs this permission. | Approve |
| I3 | 4103, case-4103, Read Cases | C-73 confirms the person's case-handling duty has ended, with no continuing authorized need. | Revoke |
| I4 | 4101, case-4101, Case Bulk Export | C-71 establishes no authorized need for all-case export in the current duty. | Revoke |

Someone selects all four and proposes Approve with the comment “Required for current case-handling duties.”

That statement fits the checked facts for I1 and I2. It does not fit I3 or I4. I3 has lost the relevant duty. I4 provides a broader export capability that the duty does not justify.

The selection put four items together on a screen or in an operation. It did not make their business facts equal.

After checking every item, the reviewer can consider an Approve action for I1 and I2 through the supported mechanism. Each still needs its own correct account context and evidence. I3 and I4 need removal decisions with reasons reflecting their different facts. Two items needing the same action do not necessarily need identical comment text.

This is the decision grouping supported by the supplied facts:

```text
Proposed selection: I1 + I2 + I3 + I4
Proposed common reason: current case-handling need
                       |
                       v
Check the reason against each item

I1: Read Cases, current duty confirmed C-71
I2: Read Cases, current duty confirmed C-72
  -> Approve can be justified for these items

I3: Read Cases, duty ended C-73
  -> Revoke; continuing-duty reason does not apply

I4: Case Bulk Export, no authorized need C-71
  -> Revoke; assigned-case reading does not justify export

Inspect the saved choice and explanation for each item.
Grouping items does not establish equivalent need.
```

The branches show the reviewer's judgment using the supplied criteria and facts. They are not an instruction for ISC to decide automatically from those labels.

## Check the selection before submission and the records afterward

Before a multi-item action, establish exactly which items it will affect. Inspect the people, source accounts, access types and permissions included. A matching display name or a shared department does not establish that the same decision is appropriate.

If the interface uses filters, pages or a select-all control, check its actual selection behavior. Do not infer whether it selected visible rows, all matching results or another set. Use the selection evidence provided by that supported interface or tool.

Make sure the chosen action and any shared explanation apply to every selected item. Separate exceptions before submission. If the scope is unclear, establish it before acting rather than rely on the displayed total alone.

After submission, inspect the resulting records. For this example, the intended decisions are I1 and I2 approved, I3 and I4 revoked, with the relevant explanations retained on the correct items. Check the actual saved comments rather than assume a shared comment was copied in the way you expected.

An accepted request or one successful item does not establish that the whole selected set reached the intended result. If any outcome is uncertain, inspect the affected records and operation result before repeating the action.

Likewise, the decision records do not prove that revoked permissions have been removed from the applications. When the reviewer signs off, they confirm the assigned review's decisions. That **finalization** is a separate step from saving an item choice. Removal work carries out the required access change. The review state and eventual account result need their own evidence.

## Read the right explanation and the right actor

The Campaign Status Report distinguishes **Decision Comments**, the explanation left with the decision, from **Comments**, which can describe issues with report status. A status message saying an account changed is not the reviewer's business justification.

The report also distinguishes **Reviewer**, the person currently assigned the certification, from **Decision Maker**, the person recorded as making the decision. After a handover, those people can differ. An administrator acting on an item can also be recorded as its decision maker even when someone else is assigned the review.

Use the recorded decision date and actor with the correct item and explanation. Do not infer that the current reviewer made every earlier decision, or that the decision-maker field alone proves who wrote every piece of associated text.

Generate a fresh campaign report after changes when you need the updated state. An earlier downloaded report can accurately describe an earlier point in the campaign while missing later corrections.

Keeping the item, decision, actor, relevant time, reason and supporting evidence connected creates a record someone else can follow. It still does not turn an unsupported reason into a justified decision or a removal instruction into a completed account change.

## Test a copied explanation against the access

Identity 4201 owns account `inv-4201` in Invoice Production. The reviewed item is a requested access profile called Invoice Review. It contains **Read Invoices**, permission to read invoice records, and **Release Payments**, permission to release payments for processing.

The package contents, current account information and person/account association have been confirmed. No other assignment or automatic requirement supplies these rights. The assigned non-self reviewer is authorized, and the certification is active and unsigned.

Business confirmation C-81 establishes that the person's current work is checking invoice records. Reading is required; releasing payments is not authorized. A bulk approval left Approve on this profile with the comment “Read-only access required for invoice checks; C-81.”

Is the retained comment a sufficient explanation of the approval?

The evidence reference is useful, but its content does not justify the whole item. The profile includes payment release, so calling it read-only misdescribes its capabilities. The approval covers the profile under review, not only the reading component mentioned in the comment.

Verify the actual selected item and saved choice, correct the explanation through the permitted review process, and establish the appropriate decision and separately authorized narrower arrangement. Correcting the wording alone would leave the excessive permission unchanged. Do not claim that a profile decision automatically creates a replacement or that a component was removed because its details were opened.

Now suppose the certification is handed from reviewer 4301 to reviewer 4302. The resulting report identifies 4302 as Reviewer and 4301 as Decision Maker for that earlier approval. Someone says that the new assignment proves 4302 checked and approved the profile.

The report supports a different explanation: 4302 holds the review now, while 4301 made the earlier decision. It does not establish that 4302 reassessed it. Inspect the current review state and relevant history before claiming any correction or new decision occurred.

To explain this item later, you need the actual package and account, the current authorized need, the recorded decision and actor, and a reason that fits those facts. Neither a filled comment box nor a bulk action can make that connection for the reviewer.
