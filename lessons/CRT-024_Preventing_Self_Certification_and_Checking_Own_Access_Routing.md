# How does ISC prevent someone reviewing their own access?

A reviewer can understand an application well and still need someone else to assess their own access.

Suppose the reviewer has permission to export reports. Asking that person to decide whether they should keep it would make the person holding the access responsible for approving it too.

**Self-certification** means reviewing one's own access. ISC's documented controls separate that work from the person's ordinary review responsibilities and assign it elsewhere.

To follow the control, identify two things: whose access is being reviewed and who would perform the review.

## Start with two people and one proposed reviewer

An **identity** is ISC's person record. An **account** is the record used to access an application.

In Reporting Production:

- Identity 3101 has Export Reports on account rep-3101. It allows exporting report contents.
- Identity 3102 has View Reports on account rep-3102. It allows reading reports.

ISC represents these permissions as **entitlements**. Both are individually reviewable in this example. They are not contained in an access profile or role, which group access into larger review objects.

The account data has been collected into ISC and connected to the correct people. That connection matters: the review must identify the actual person whose account holds each permission.

An **access review** assesses whether that person still needs the access. A **campaign** organizes the work. An assigned review is called a **certification**, and each **review item** identifies access awaiting a decision.

**Generation** creates the campaign's actual review items and assignments from its settings and available information. The resulting **preview** allows an administrator to inspect that work before starting the campaign for reviewers.

The administrator, who prepares and manages the campaign, chooses the supported Individual reviewer option in a Search identity campaign and selects identity 3101.

That person can be an appropriate reviewer for 3102's access. But the selected campaign also includes 3101's own Export Reports holding.

Choosing one name in the reviewer setting does not make both assignments appropriate.

## Follow the own-access comparison

The person whose access is under review is the **review subject**. The person responsible for assessing it is the **reviewer**.

For 3102's View Reports holding, subject 3102 and proposed reviewer 3101 are different people.

For 3101's Export Reports holding, subject 3101 and proposed reviewer 3101 are the same person. That is the own-access case.

The documented automatic control separates the person's own access into another certification and assigns responsibility to another identity.

In our example, 3101 has a valid manager relationship to identity 3110. Manager 3110 is distinct from the subject, available and permitted to perform the review. No other reassignment changes this ordinary result.

When the campaign is generated, the administrator inspects these supplied results:

- R-other contains 3102's View Reports holding and is assigned to 3101.
- R-own contains 3101's Export Reports holding and is assigned to manager 3110.

The labels R-other and R-own distinguish the example records. The useful result is that both intended holdings remain covered and the own-access holding has another reviewer.

```text
SELECTED ACCESS
3101: Export Reports on rep-3101
3102: View Reports on rep-3102

PROPOSED INDIVIDUAL REVIEWER: 3101
        |
        | compare the access subject with the reviewer
        |
        +-- Subject 3102: someone else's access
        |       |
        |       v
        |   R-other: assigned to 3101
        |   3102 / rep-3102 / View Reports
        |
        +-- Subject 3101: the reviewer's own access
                |
                | separate own-access review work
                | valid distinct manager is 3110
                v
            R-own: assigned to 3110
            3101 / rep-3101 / Export Reports

CHECK THE GENERATED RESULT
Both intended holdings remain in review.
Neither holding has received a decision merely by routing.
3101's own access has a different assigned reviewer.
```

Follow the upper branch for someone else's access and the lower branch for the proposed reviewer's own access.

The diagram shows the actual supplied assignments after generation. It does not imply a universal rule that every campaign creates exactly one certification per person or exactly two certifications.

The separation changes review responsibility. It has not granted, removed or approved either permission.

## Why keeping both holdings matters

An own-access control should leave the access available for assessment by someone else.

If 3101's Export Reports item simply disappeared from the intended review, that would leave a coverage question. The fact that 3101 could not review it would not establish that anyone else had reviewed it.

Inspect the separated work and its assignee. Confirm the person, source account and entitlement, rather than finding only a similarly named permission.

A **source** is ISC's representation of a connected system or account-data collection. Reporting Production and a similarly named test source can contain different accounts and permissions.

Also distinguish multiple accounts belonging to one person. Moving a decision between two of that person's accounts does not introduce a different human reviewer.

If the review concerns an access profile or role, identify the complete review object and whose assignment it represents. Do not treat a component entitlement as a separate review merely to change how the control appears to apply.

## Where does the separated work go?

For the documented automatic own-access process, ISC uses the person's manager first. If the person has no manager, it uses the campaign owner. In the no-manager case where the person also owns the campaign, the guidance describes assignment to an administrator chosen at random.

The **campaign owner** is responsible for the campaign. The **campaign creator** identifies who created it. These are different roles, even when one person fills both.

Consider these cases for subject 3101, with valid, available and permitted recipients wherever a particular person is named:

| Relevant facts | Own-access responsibility to check |
|---|---|
| A valid distinct manager 3110 is recorded | The separated review is routed to 3110 |
| No manager is recorded; campaign owner is distinct identity 3140 | The separated review is routed to 3140 |
| No manager is recorded; subject 3101 also owns the campaign | ISC selects an administrator; inspect the actual recipient |

The last row does not let you predict a particular administrator from a list or a name. Check who was actually assigned and whether the resulting work is ready to be assessed.

Keep this process tied to the own-access situation. A campaign can have other fallback rules, meaning alternative recipients when required information is missing.

For example, the Search Manager reviewer option documents a creator fallback for an ordinary missing-manager case. That does not turn creator and campaign owner into interchangeable words or replace the own-access process.

Inspect the campaign route, the subject, the relevant manager and owner records, and the actual resulting assignment.

## A manual reassignment has a different outcome

**Reassignment** changes who is responsible for an existing certification.

An administrator might try to move work to a knowledgeable person. Before doing so, inspect everything in that certification.

For the documented manual action, reassignment is blocked if the certification contains any of the proposed new reviewer's own access.

The word **any** matters. Consider a proposed new reviewer of 3101:

| Contents of the certification being moved | Own-access condition |
|---|---|
| Only 3102's View Reports holding | This own-access condition does not block the move; other requirements still apply |
| Only 3101's Export Reports holding | The move to 3101 is blocked |
| Both 3102's View Reports and 3101's Export Reports | The move to 3101 is blocked because their own access is included |

In the mixed case, most of the work could concern other people and the restriction would still apply.

Do not expect this manual action to move the other person's item and automatically create another review for the conflicting item. Its documented response to that condition is to block the reassignment.

Select a supported independent reviewer or use an appropriate supported correction to the review work. Preserve the intended access coverage and verify the resulting assignments.

Here, the new owner of a certification means the person receiving that review responsibility. It does not mean that person becomes the campaign owner.

## Automatic work reassignment still checks own access

A **work reassignment** is a configured arrangement for supported work to be directed from one person to another as it is created.

Suppose work originally intended for reviewer 3120 contains the two Reporting Production holdings. A configured work reassignment directs the new work to 3101.

That introduces the same own-access problem: the work includes 3101's Export Reports permission.

The documented automatic work-reassignment process applies self-certification prevention. In the ordinary conditions already established, 3101's own access is separated and routed to manager 3110, while the other person's work can remain with 3101.

The reason for the difference from the manual case is the process being used. Automatic routing follows the documented separation path; an attempted manual move containing the new reviewer's own access is blocked.

Do not assume a setting for future work moved every already pending certification. Inspect the particular work and its actual responsibility.

## A group name is not the person making a decision

A **governance group** is a configured group whose members can perform supported governance work.

When review responsibility belongs to a group, identify the human subject of the access and the person who can actually act. Comparing a person's identity number with a group identifier is insufficient.

If the group contains a person whose own access is in the intended population, inspect how that own-access work was generated and who is permitted to assess it.

Do not infer the member-specific separation or permitted actions just from the group name or membership list. Check the actual campaign's own-access work and supported reviewer behavior.

There is a specific work-reassignment distinction worth knowing. For certification work assigned to a governance group with multiple identities, the documented member work-reassignment configurations are not applied.

So if a group has two members and one member has configured a redirect to someone else, that setting alone does not establish that the group's certification moved to that other person.

Access-request review reassignment has different group handling. Do not import its per-member behavior into certification work.

Group responsibility, actual membership, permitted human reviewer and recorded decision maker are separate pieces of evidence.

## Ownership and administration do not settle the own-access question

A person can own the campaign, own an access object or have administrative duties and still be the subject of access under review.

Those responsibilities do not make someone a different person from themselves.

For the documented manual reassignment action, the relevant check is whether the certification contains the proposed new reviewer's own access. Do not infer an exemption merely from a campaign-owner or administrator title.

**Sign-off** means the reviewer's confirmation or finalization of the assigned review's decisions. The documented reassignment action also requires appropriate preview or active work that has not been signed off.

Check permissions and campaign state alongside the own-access condition. Passing one check does not establish that every other requirement is satisfied.

If someone asks to bypass the control to meet a deadline, first identify an appropriate independent recipient and the supported way to assign the work. Removing the own-access item from the intended population would leave a review gap, rather than establish independent assessment.

## Check the result and the person who acted

After generation or an allowed correction, inspect the actual assigned certification.

Confirm that the intended person's access remains present, that the correct source account and review object are identified, and that the assignee is suitable and permitted.

Then distinguish assignment from action.

An **Approve** decision records that the reviewer decided the access should be retained. Assignment of R-own to 3110 does not mean that 3110 has already made that decision.

The **decision maker** is the identity recorded as performing a particular decision. A current reviewer and an earlier decision maker can differ after a permitted reassignment.

Use current campaign work and fresh report evidence where available to establish each fact. A changed manager field or a chosen reviewer setting does not prove what happened to an existing certification.

An independent reviewer also needs to understand the access and current business need. Avoiding self-review is one requirement for a sound assessment; it does not supply that understanding automatically.

## Work through a mixed review

An active, unsigned Warehouse Production certification contains:

- Identity 3201's View Stock on account wh-3201, allowing stock information to be read.
- Identity 3202's Adjust Stock on elevated account wh-3202-admin, allowing stock quantities to be changed.

An **elevated account** has additional permissions for more powerful tasks. Both holdings here are standalone reviewable entitlements, current in ISC and correctly linked to their subjects.

The administrator proposes manually reassigning the whole certification to 3202. Identity 3202 owns the campaign and has Cert Admin duties, meaning certification-administration responsibilities.

Someone argues that the move should be allowed because one item belongs to 3201 and 3202 understands warehouse access.

What should happen under the documented manual rule? How should the intended review remain covered?

### Compare every included subject with the proposed reviewer

The certification includes 3202's own Adjust Stock holding. The manual reassignment to 3202 is therefore blocked by the own-access condition.

The other person's item does not cancel that conflict. Campaign ownership, knowledge and the administrator title do not establish an exception for this documented action.

Choose an appropriate permitted independent recipient or a supported correction that leaves both intended holdings assigned for assessment. Check the actual resulting records. Do not assume that a rejected manual action partially moved the non-conflicting item.

Preserve the correct source accounts and access objects. A successful assignment of only 3201's View Stock would not establish coverage of 3202's elevated access.

Now change the proposal. A supported group has two active members, one of whom is 3202. That member has a work-reassignment setting directing their work to 3210.

Can you conclude that all group review work, including 3202's own access, will move to 3210?

No. The documented multi-member group exception means that member setting is not applied to the group's certification work. It cannot prove that 3210 received anything.

Inspect the actual group-assigned and own-access review work and the permitted human actors. Establish an appropriate independent assessment for 3202 rather than treating a different group name or a redirect setting as proof.

For each own-access case, trace the subject, the proposed or actual reviewer, the automatic or manual action and the resulting assignment. Then verify that the access is still covered and identify who actually assessed it.
