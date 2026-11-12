# When should a review be reassigned?

A review has reached the wrong person. That person can open it, but they do not have the business information needed to assess the access.

Moving the work to someone else may be the right correction. First, identify exactly what should move and why.

**Reassignment** changes responsibility for existing review work. It does not decide whether the access should be kept, change the account's permissions or establish that the new reviewer has finished the assessment.

## Start with the work that needs a different reviewer

An **access review** asks whether someone still needs particular access. A **campaign** organizes the reviews, and an assigned review is called a **certification**.

Within a certification, a **review item** identifies access awaiting a decision. The **reviewer** is responsible for assessing that work.

An **identity** is ISC's person record. An **account** is the record used to access an application. ISC can represent account permissions as **entitlements**.

Suppose campaign C-1 contains a reporting review called R-report. It is assigned to reviewer 3310 and contains:

- Identity 3301's View Reports on account rep-3301, allowing reports to be read.
- Identity 3301's Export Reports on that account, allowing report contents to be exported.
- Identity 3302's View Reports on account rep-3302.

The permissions are on Reporting Production. In ISC, a **source** represents a connected system or account-data collection.

These are individually reviewable entitlements here, without a containing role or access profile, which group access. Their account data is current in ISC and linked to the correct people.

The campaign also contains R-support, assigned to 3310. That review contains identity 3303's Read Cases permission on account case-3303 in Support Production. Read Cases allows reading support-case information.

The business requirement has changed. Reporting access should be assessed by reviewer 3320, who has the necessary reporting context. Reviewer 3310 should continue the support review.

The intended correction is therefore precise: move R-report's responsibility to 3320 and leave R-support with 3310.

“Move 3310's work” would be too broad for this requirement.

## Decide whether reassignment solves the actual problem

Reassignment is useful when an appropriate replacement should assess existing work. Reasons can include an incorrect assignment, a reviewer who cannot complete the work or a change in the responsibility for the business area.

The replacement needs to understand what the access permits and how to establish current need. Availability alone is insufficient.

Also check whether assignment is the real problem.

If an intended person's access is absent, moving the existing review does not establish that the missing item was added. If the wrong account is included, a new reviewer still receives the wrong account.

Likewise, changing a person's manager relationship or an access object's owner is a configuration or data correction. That is different from changing responsibility for a review that already exists.

Sometimes both changes are needed: repair the information used for future generation, then correct the existing work through a supported action.

## Check the complete contents before moving anything

The **scope** of a reassignment is the work the chosen action will move.

Start with the campaign and certification identifiers, then inspect the subjects, accounts and access within the selected work. A subject is the person or account whose access is under review.

A certification can contain more than the one item that first caught your attention. Do not assume that selecting a familiar row means only that permission will move.

For R-report, the requirement is to transfer all three reporting holdings. Moving the whole certification fits that requirement.

But if only 3301's Export Reports item needed a different reviewer, moving all of R-report would also transfer the two View Reports items. That would be a broader action.

An **API** is an interface software uses to request actions or read records. The documented next-generation APIs include an operation for specified whole certifications and separate operations for selected subjects or items within an identity campaign certification.

A subject-level choice and an item-level choice can also differ. A person can have several access items, so moving that person's review work can include more than one permission.

Establish which unit the actual supported action selects. Check the campaign type and interface before assuming it offers the same selection choices as another route.

## Match the action to the people allowed to perform it

**Authorization** means permission to perform an action.

Being responsible for the campaign does not, by itself, establish every platform permission. Being a reviewer does not give unrestricted authority over everyone else's certifications.

For example, the documented next-generation whole-certification operation requires an Org Admin or Cert Admin role. These are organization-administration and certification-administration user levels.

The documented subject/item operations for an identity campaign also allow reviewers of that certification to perform the action, as well as the specified administrators.

Those are different action scopes. Check the permission for the particular operation and the actual person using it.

These next-generation reassignment APIs are marked Experimental, meaning what they support and how you call them can change.

Their existence does not establish that every tenant, campaign type, screen or review state supports every form of reassignment. Use the current supported path for the work involved.

There is no need to give someone broad administration merely because a permitted narrower review action is needed.

## Check the review's state and the proposed recipient

For the documented administrative individual-certification reassignment path, the campaign must be in preview or started, and the review must not have been signed off.

A **preview** is generated review work available for inspection before launch. A started or active campaign is available for its permitted reviewer work.

**Sign-off** is the reviewer's confirmation or finalization of the assigned decisions. A review can contain saved decisions and still not be signed off.

That distinction matters in R-report. Suppose 3310 has saved an Approve decision for 3301's View Reports item. **Approve** records that the reviewer decided the access should be retained.

The other two items have no decision, and R-report has not been signed off. These are separate facts to verify before the move.

The documented administrative action does not allow an already signed-off certification to be reassigned. A different API appearing in the documentation is not permission to bypass a state restriction; verify its actual contract.

Then inspect the proposed recipient. In our example, 3320 is available, knowledgeable and permitted, and none of the selected certification concerns 3320's own access.

**Self-certification** means reviewing one's own access. For the documented manual action, a certification containing any of the proposed new reviewer's own access cannot be reassigned to that person.

Passing the own-access check does not remove the other state, scope or permission requirements.

## Record why this work is moving

A reason helps the new reviewer understand the handover and helps others investigate it later.

For this example, a useful reason would say:

“Reporting Production review responsibility has moved to reviewer 3320. Transfer R-report's three reporting holdings. R-support remains with 3310. Contact the campaign administrator for the handover details.”

The reason identifies the business change and the intended boundary. “Reassigned” alone would not explain either.

Include the relevant contact or administrator identity in the supported reasoning field where appropriate. Keep the information sufficient for the handover without adding unrelated personal details.

The reason records an instruction and its justification. It does not prove the action succeeded.

## Follow the request to the actual assignment

The authorized administrator selects the supported action for R-report and submits the move to 3320.

Depending on the operation, the response can describe updated certification work or return a task that tracks processing.

For example, the documented whole-certification API returns a task for asynchronous reassignment. **Asynchronous** means the work is processed separately from the request being submitted.

The identity-campaign subject/item documentation includes an operation returning a certification object and an asynchronous variant returning a tracking task.

These responses must be interpreted according to the operation used. A request accepted for processing is not, by itself, proof that the intended assignment has already changed.

Inspect the relevant result or task, then the actual campaign work. If an outcome is uncertain, establish what happened before repeating the request. A timeout or missing confirmation does not prove that no change occurred.

There is no universal number of seconds after which a submitted reassignment can safely be treated as complete.

## Compare the result with the intended handover

Suppose inspection after the permitted action confirms:

| Work inspected | Current reviewer before | Current reviewer after | Decision information found after the move |
|---|---|---|---|
| 3301 / rep-3301 / View Reports | 3310 | 3320 | Earlier Approve remains recorded as made by 3310 |
| 3301 / rep-3301 / Export Reports | 3310 | 3320 | No decision yet |
| 3302 / rep-3302 / View Reports | 3310 | 3320 | No decision yet |
| 3303 / case-3303 / Read Cases | 3310 | 3310 | Outside the requested move |

These are the inspected results supplied for this example. Do not turn them into a promise that every action copies or resets every decision and status in exactly the same way.

Check the actual decision state and history for the chosen action. Also identify the resulting records rather than assuming every operation preserves the same certification identifier.

The main handover can be followed like this:

```text
CAMPAIGN C-1 BEFORE THE MOVE
R-report -> reviewer 3310
  3301 / rep-3301 / View Reports
  3301 / rep-3301 / Export Reports
  3302 / rep-3302 / View Reports

R-support -> reviewer 3310
  3303 / case-3303 / Read Cases
        |
        | permitted action selects whole R-report only
        | new reviewer: 3320
        v
INSPECTED RESULT
Reporting work -> reviewer 3320
  Same three intended reporting holdings verified
  Earlier decision still records its actual maker, 3310

Support work -> reviewer 3310
  Read Cases remains with the original reviewer

Then confirm remaining work and recipient visibility.
A submitted request alone does not establish this result.
```

The reporting branch changes responsibility. Its three intended holdings remain present in the inspected work.

The support branch stays with 3310 because it was outside the requested move.

The earlier approval still names its actual maker. A **decision maker** is the person recorded as performing a particular decision. Changing the current reviewer does not make 3320 the person who performed 3310's earlier action.

A fresh campaign status report can help distinguish current responsibility from that history. An old downloaded report will not update itself after reassignment.

## Finish the handover with the new reviewer

The assignment record is necessary, but it is not the whole operational result.

Confirm that 3320 can find and open the intended work through the permitted reviewer path. Establish which decisions remain and what information is needed to assess them.

Do not assume a saved earlier approval is either automatically lost or newly made by the replacement. Read its actual state and history, then follow the applicable review procedure.

An email alone cannot establish the correct handover. Check the campaign, the assignment and the work available to the recipient. If a notification is missing, investigate that separately instead of assuming the reassignment failed.

Likewise, a successful reassignment is not a completed review or verified access removal. The reviewer still needs to assess and finalize the relevant work, and any resulting access change needs its own evidence.

## Keep future redirection separate from existing work

A **work reassignment** configuration directs supported work to a designated person as it is created, during the configured period.

That differs from selecting R-report and changing its existing responsibility.

Do not assume that setting a future redirect moved all previously generated reviews. Inspect existing work separately.

If an incorrect manager or owner caused the original assignment, decide whether that underlying data also needs repair. A successful move of this campaign's work does not establish that the next campaign will be routed correctly.

The useful boundary is between the existing work being handed over and the instructions or data used to prepare later work.

## Try a request to move only one item

A Warehouse Production identity campaign has an active, unsigned certification assigned to 3410. It contains:

- Identity 3401's View Stock on wh-3401, allowing stock information to be read.
- Identity 3402's View Stock on elevated account wh-3402-admin, allowing stock information to be read.
- Identity 3402's Adjust Stock on that elevated account, allowing stock quantities to be changed.

An **elevated account** has additional permissions for more powerful tasks. All three holdings are standalone reviewable entitlements, current in ISC and correctly linked to their subjects.

The requirement is to move only 3402's Adjust Stock assessment to knowledgeable, permitted, independent reviewer 3420. Both View Stock holdings must remain with 3410.

Someone proposes selecting the whole certification because it contains the required item.

Is that the correct scope? What should the result show?

### Follow the item that was requested

The whole-certification choice is broader than the requirement: it includes all three holdings. A choice that moves all of subject 3402's work is also too broad, because that person has View Stock as well as Adjust Stock.

Establish whether the actual supported identity-campaign interface and operation allow selecting only the intended Adjust Stock item. Check what the selection includes, who may perform it and whether the current state permits it.

If the available screen cannot express the intended scope, do not invent a selector or remove the other person's work. Use a verified supported route or obtain the appropriate authoritative guidance.

After an allowed correction, inspect the resulting work. The intended result is both people's View Stock holdings still assigned to 3410, with only 3402's Adjust Stock assigned to 3420.

Check all three holdings and their account references, current decision states, history and recipient visibility. A total of three items somewhere in the campaign would not prove that the assignments are correct.

Now change one fact. Before the documented administrative move is performed, the original reviewer signs off the certification.

An earlier observation that the review was unsigned is now stale. Refresh the state and reassess the permitted action. Do not keep submitting the same move as though sign-off had not happened.

Before reporting the handover as complete, point to the changed assignment for Adjust Stock and the retained assignments for both View Stock holdings. Those records establish which work moved and who is responsible next.
