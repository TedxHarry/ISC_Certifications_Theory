# Can you defend the outcome when conditions change?

Someone asks you, “The review is signed off. Why are you still saying there is work to do?”

You check the account. The permission that should have been removed is still there.

You can explain both facts without contradicting yourself. The reviewer has finished the decision. The application has not yet made the required change.

But a useful answer needs more than that distinction. Which account still has access? Why did removal fail? Who will act next? What evidence will let you say the work is finished?

Let's follow those questions through a review that needs correction along the way.

## First, be clear about what the review must achieve

The requirement is to review everyone who currently holds **Export Invoices** in Invoice Production, the application used for live invoice work.

Export Invoices allows an account to download invoices in bulk. **Read Invoices** allows the person to view invoices.

The business wants unnecessary export access removed while keeping justified viewing access.

The application inventory has three accounts with export access: **inv-201**, **inv-202** and **inv-203**. Each belongs to a different employee, and each employee has only one account in this example. All three still need viewing access.

ISC stores information about these employees as **identities**. Their application accounts are linked to those identities. That link tells ISC whose access it is showing.

A **source** is ISC's configured representation of an application and its account data. Here, the Invoice Production source contains the collected account records. Those records have been checked against the current application inventory.

Export Invoices is an **entitlement**, a specific permission on each account. In this example it can be reviewed individually, rather than through a bundle of permissions.

These three export holdings are the review's **scope**, the access this exercise must account for. All three must receive an appropriate review. Any required export removal must be verified, and justified reading must remain.

## The preview contains only two people

The administrator prepares a **manager campaign**, where employees' managers review their access.

A **campaign** is the overall review exercise. Its **preview** shows the generated review work before the administrator starts it for reviewers.

The first preview, **C-960**, contains inv-202 and inv-203. It does not contain inv-201, so the administrator leaves this campaign unstarted.

The configured filter includes only Export Invoices from Invoice Production. A filter narrows which access appears. Checking that filter is useful, but the actual cause here is elsewhere: inv-201's identity has no manager.

For the dedicated manager-campaign route used here, identities without managers are excluded.

Notice what that means. The account exists in the application. Its export permission exists in ISC's collected data. Yet the review does not contain it.

“ISC has the account” and “this campaign covers the account” are different claims.

The expected set has three accounts. The preview has two. Even if both generated items later received decisions, that would leave one required account unreviewed.

A percentage calculated from the generated items cannot reveal a person who never entered that set.

### Correct the cause, then inspect the result

The responsible data owner confirms that the employee behind inv-201 reports to reviewer **R-60**. The authoritative employee data, meaning the trusted source of employment information, needs that correct manager information.

**Manager correlation** links an employee's identity to the manager's identity. The employee's source record supplies information identifying their manager. ISC uses the configured matching attributes to find that manager's identity and establish the relationship.

The authorized team corrects the genuine employee data and uses the supported processing path. The supplied result now shows the employee linked to R-60. R-60 is also the correct manager for the other two employees.

Don't change the manager to an arbitrary available person just to make the account enter a campaign. That would make the review depend on a false relationship.

The administrator generates a distinct new preview, **C-961**, from the corrected inputs.

In this preview, all three intended export items appear. The account identifiers, owners and permission values match the expected set. R-60 is assigned the review, can see the work and does not own any of the access being reviewed.

The earlier C-960 preview remains evidence of its earlier contents. Updating manager data does not establish that an already generated preview has repaired itself.

Here, the new preview is the evidence that the correction reached the review work.

After the other readiness checks pass, an authorized administrator starts C-961. The result is checked: the campaign is active and R-60 can open the assigned work.

## Now the reviewer becomes unavailable

R-60 records **Revoke** for inv-202 because its earlier bulk-export task has ended.

Revoke is the decision that the reviewed access should be removed. **Approve** means it should be retained.

R-60 has not finished reviewing the other two items and has not signed off.

**Sign-off**, or finalization, confirms the review's decisions. Saving an item choice and confirming the finished review are separate actions.

R-60 then becomes unavailable before the deadline.

What should happen next?

A reminder to R-60 would not solve the known absence. Marking the review complete would not supply the missing business judgments.

The campaign administrator identifies **R-61**, an eligible replacement who understands the employees' current work and has authority to decide their access. R-61 owns none of the access in this review.

The assigned collection of review work is a **certification**. In this supplied campaign, the affected certification contains these three employees' export items.

Because it is still unsigned, an authorized administrator uses the supported reassignment operation to transfer that work. A certification that has already been signed off cannot be transferred through this operation. The actual assignment and R-61's ability to open all three items are then checked.

That final check matters. Requesting a transfer is not the same observation as seeing the correct work with the replacement reviewer.

Manual reassignment also has a self-review restriction: you cannot transfer a certification containing the proposed reviewer's own access to that reviewer. Being knowledgeable does not remove that restriction.

### What happens to the earlier Revoke choice?

Inspect it.

In the supplied transferred review, inv-202 still shows R-60's recorded Revoke choice and reason. R-61 checks that reason against the current facts rather than assuming an earlier choice must still be correct.

R-61 establishes that inv-201 and inv-203 still need bulk export. The earlier task behind inv-202 has ended, so that employee needs reading but no longer needs export.

The finished choices are therefore:

| Account | Final choice for Export Invoices | Current reason |
|---|---|---|
| inv-201 | Approve | Ongoing invoice-export work requires it. |
| inv-202 | Revoke | The export task ended; viewing is still needed. |
| inv-203 | Approve | Ongoing invoice-export work requires it. |

R-61 checks the complete set and signs off before the deadline.

Keep the actors clear when explaining the evidence. R-60 recorded the earlier inv-202 choice. R-61 received the work and finalized the completed review. A current assignment field alone cannot tell that whole story.

If someone instead asks an administrator to complete an overdue campaign with unfinished reviews, establish how that exact campaign handles the remaining work before promising a result. An item nobody decided and a saved choice in an unsigned review are different starting situations. The saved choice alone does not establish what administrator completion will do to it. Check the applicable behavior and settings. A policy applied by an administrator also does not supply the missing reviewer's business judgment.

In our case, the supported unsigned handover and R-61's final confirmation avoid relying on an assumed bulk-completion outcome.

### Would an absence setting have done the same thing?

ISC also has **work reassignment**, a configuration that redirects newly created work during a specified period.

That can help prepare for a known absence. It does not establish who owns work that already existed before the configuration began.

When you need an existing certification moved, inspect that existing assignment and the supported transfer result.

When a work-reassignment period ends, previously redirected work remains with its new owner. The end time does not automatically return those items to the original person.

So the useful question is not just “Was absence configured?” It is “Who owns this exact work now, and can that person finish it?”

## The decision is final, but the application rejects removal

After R-61 signs off, the actual removal work for inv-202 is present and due for processing.

**Remediation** is the work needed to carry out the review's required access changes. **Provisioning** is the process that makes changes to accounts and permissions.

The Invoice Production source has a supported automated removal path. Its **connector** is the integration ISC uses to communicate with the application.

The connector uses **INT-6**, an integration account authorized to communicate with Invoice Production. That is different from inv-202, the employee account whose export permission must change.

The removal attempt is rejected by the application.

The example records times in UTC, a shared time reference, so the team can compare events without mixing local time zones. At 11:10 UTC, the operation record shows the failed attempt against inv-202's Export Invoices permission. At 11:20 UTC, a current application check shows that export is still present.

The application administrator checks the exact rejection and INT-6's current permissions. In these supplied facts, INT-6 lacks the permission needed to remove that export membership.

Now the evidence tells you why removal failed.

It is not enough to say “the connector failed.” The integration account can still read account data, but it cannot perform this particular removal.

A working aggregation would not disprove the failure. **Aggregation** reads account information into ISC. Read permission does not establish permission to change an account.

Changing inv-202's review choice would address the wrong problem. The business decision is supported and finalized. The failure is in carrying that decision out.

## Hand over what is still open

Suppose your work period ends at noon. The removal has not yet been corrected.

A message saying “certification issue, please check” leaves the next person to reconstruct the situation.

A useful handover explains the exact remaining work. For this example, it could say:

> C-961 contains all three required Invoice Production export items. R-61 finalized two Approve choices and one Revoke. The removal for inv-202 is still open.
>
> The 11:10 UTC operation was rejected. At 11:20 UTC, inv-202 still had Export Invoices and Read Invoices. The application administrator confirmed that integration account INT-6 lacks the required removal permission.
>
> The application administrator owns arranging and applying the authorized permission correction. The ISC operations owner will check for outstanding attempts, then use the supported recovery action. The campaign owner will check progress at 15:00 UTC today. Closure requires evidence that inv-202 no longer has export, still has justified reading, and the other two approved export holdings remain accounted for.

Attach or identify the matching records through the approved evidence location: campaign, affected review/item, source, account, operation, error and current account observation. The recipient needs access to that evidence.

The named owners and 15:00 check are agreed working arrangements in this example. They are not ISC states or platform time guarantees.

A handover is complete when the receiving owner understands and accepts the responsibility. In the supplied handover, the application administrator and ISC operations owner confirm that they can access the evidence and accept their actions. The campaign owner accepts the 15:00 progress check. That agreement does not mean the access removal is complete.

If the issue will miss the agreed business date, the campaign owner needs the actual remaining risk and a decision from the appropriate accountable person. Record any approved temporary exception with its scope, owner, expiry or review time and required follow-up.

An exception records an accepted departure from the requirement. It does not turn existing export access into evidence of removal.

## What would let you close this issue?

The application administrator obtains approval and corrects INT-6's specific removal authority.

The ISC operations owner checks the outstanding work before choosing the supported recovery action. This avoids blindly creating another attempt while an earlier one may still be running.

An error does not by itself tell you whether ISC will retry it automatically. Follow the actual error, connector behavior and operation state.

The authorized operator uses the supported path to attempt the same required removal again. In the supplied result, this retry succeeds. A current application check at 14:00 UTC shows that inv-202 no longer has Export Invoices and still has Read Invoices.

The team also checks the approved outcomes: inv-201 and inv-203 retain their justified export access, and all three accounts retain justified reading. There is no other open removal in this review's required set.

The source data is collected again through the supported path and checked against those application results. Freshly generated campaign evidence is then matched to C-961.

Keep those observations separate:

The operation record shows what was attempted and its result. The application check shows the actual account permission at that time. The later collection shows what ISC obtained. The new report shows the campaign information available when that report was generated.

Downloading the old report again would not give it new contents. A report must be generated again to include later campaign changes.

You can now explain the scoped outcome: all three intended export holdings received finalized decisions, the one required export removal is verified, and the access that should remain has been checked.

The earlier failed attempt remains part of the explanation. There is no need to hide it to show that the eventual result is correct.

## Keep the reasoning connected

The problems we followed needed different corrections.

The missing employee needed truthful manager data and a checked new preview. The absent reviewer needed eligible responsibility for the existing unsigned work. The failed removal needed correction of the demonstrated application permission problem.

The following map shows those investigation choices. Its arrows describe how you reason and verify; they do not describe private ISC services running in this order.

```text
The result no longer matches the requirement
                       |
      Name the exact person, account and access
                       |
       Find where the evidence first differs
                       |
      +----------------+------------------+
      |                |                  |
 Wrong scope     Unfinished review    Failed removal
      |                |                  |
 Correct inputs  Assign an eligible   Correct the
 and check fresh reviewer and         failed operation's
 generated work  confirm decisions    cause
      |                |                  |
      +----------------+------------------+
                       |
        Recheck the affected requirements
                       |
           Is the required result proved?
                       |
             +---------+---------+
             |                   |
            Yes                  No
             |                   |
 Explain the scoped       Hand over the open work:
 result and evidence      owner, next check, due time
                          and evidence needed to close

These arrows describe investigation and verification.
They are not ISC's internal processing sequence.
```

After each correction, return to the affected requirement. A repaired manager relationship is not proof of account removal. A successful removal is not proof that the original review included everyone.

## Try the reasoning when the access comes in a bundle

A different application has an account, **wh-301**, used for warehouse work.

**Read Stock** lets the person view stock records. **Adjust Stock** lets them change stock quantities.

The account received a separately requested **Stock Adjustment access profile**, a bundle containing both permissions.

It also receives Read Stock through the **Warehouse Reader role**. A role groups access for a business function. Its **membership criteria** are the conditions ISC checks to decide who belongs to it. This role is assigned automatically because the person's employment information matches those conditions.

The person has finished the temporary stock-adjustment task but still needs to view stock. The review requirement is to remove adjustment ability and keep justified reading.

The supported review presents the separately requested Stock Adjustment profile. The reviewer revokes that profile and finalizes the decision.

In the supplied completed result, Adjust Stock is absent. Read Stock remains, and the Warehouse Reader role still requires it on this same account.

Has removal failed because one permission from the profile remains? Explain how the account result and the remaining role assignment support your answer.

<details class="practice-answer" markdown="block">
<summary>Compare your reasoning</summary>

No. The required result was to end stock adjustment while preserving legitimate reading. The observed account matches that requirement.

The access model explains the retained permission: revoking the separate profile does not remove access still required through the role.

This case uses a role and a separate requested profile. It does not establish how every possible overlap between independent profiles will behave.

</details>

### Now change the requirement

The business then confirms that the person has left warehouse duties and should have no Warehouse access.

The requested profile is already revoked, but Warehouse Reader is still assigned automatically and still requires Read Stock on wh-301.

The automatically assigned role can be **acknowledged** in a certification. Acknowledge records review of that rule-driven assignment; it does not manually revoke the assignment or switch off the rule.

Would repeating the profile revocation or choosing Acknowledge meet this new requirement? Explain what the responsible owners should investigate, and what evidence would let you say Warehouse access has ended.

<details class="practice-answer" markdown="block">
<summary>Compare your reasoning</summary>

Neither action establishes that the remaining reading access has ended. The profile is already gone; the automatic role is the remaining reason Read Stock is required.

Check why ISC is still assigning Warehouse Reader. Compare the person's current employment values with the role's membership criteria, the conditions that caused ISC to assign it.

The responsible owners must establish why the person still matches. If employment data is wrong, correct it truthfully. If the role criteria no longer express the approved business rule, assess and authorize the criteria change, including its effect on other members.

Don't alter accurate employee data simply to force a desired membership result.

Follow the supported change through actual role assignment and account outcomes. Until those results are established, hand over the new no-access requirement as open.

The evidence needs to show that the person no longer has the Warehouse Reader assignment and that wh-301 no longer has Read Stock or Adjust Stock. Removing the role assignment on screen alone would not prove the application account changed. If the investigation finds another source of Warehouse access, account for that too.

The first completed review proved that adjustment ability ended while reading remained justified. It did not prove the later, broader requirement.

When you explain the outcome, name which requirement you are answering, show the evidence that answers it, and identify who owns anything still unproved.

</details>
