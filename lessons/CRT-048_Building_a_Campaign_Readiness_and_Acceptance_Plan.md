# How do we build a campaign readiness and acceptance plan?

A campaign preview contains three accounts. The requirement also names three accounts.

Before calling it ready, establish that they are the right three accounts, with the right access and suitable reviewers. You also need to know how rejected access will be removed and how its result will be checked.

A readiness and acceptance plan connects the requirement to evidence. It states what must be true, how that will be checked, who is responsible and what happens when the expected result is not established.

## Make the required result precise

In SailPoint Identity Security Cloud, or **ISC**, an **identity** represents a person or another managed subject. An **account** is the record through which that person or service uses an application.

A **campaign** organizes access reviews. A **certification** is an assigned review within it. A **review item** is an access entry on which a reviewer records a choice.

Suppose the approved requirement is to review Export Records for the current project team on **Project Records Production**.

Export Records allows downloading project records in bulk. Read Records allows viewing them. These permissions are represented as **entitlements** in ISC.

Unjustified export must be removed while justified reading remains.

An **acceptance criterion** states a result that must be established for the relevant requirement to be accepted.

For a rejected export permission, “the task completed” is too vague. A useful criterion is:

“Export Records is absent from the intended account, and required Read Records remains.”

That tells you which account result to verify. It also prevents disabling the entire account from being counted as a successful export-only removal.

Acceptance criteria belong to a particular stage. Before launch, you can check the intended contents and the ability to perform the planned work. After actual reviewer decisions and fulfillment, you can verify the real account outcomes.

You do not need to remove production access before the review has decided what should be removed.

## Build the expected set independently

A **source** is ISC's configured representation of the application or its account data.

For this example, the approved project roster, meaning the list of current project members, and the checked application inventory identify:

- proj-991, an employee's account.
- proj-992, a contractor's account.
- proj-admin-993, a privileged account used for work requiring higher authority.

Each related identity has one account on this source in the supplied example. Account ownership and current holdings have been checked. The review can examine Export Records as its own item.

Another account, proj-994, also has Export Records but belongs to someone outside this project. It must be excluded from this particular campaign.

That exclusion does not mean its access is unjustified or should be removed. This campaign's approved **scope**, the people, accounts and access intended for inclusion, does not include it.

Keep the expected account and item relationships with the requirement. Do not create the expected list by copying the campaign's own output. That would make the result its own proof.

## Compare membership, not just totals

A generated **preview** is review work available for inspection before **activation** starts reviewer work.

The first preview, P-860, contains:

| Required account | Present in P-860? | Finding |
|---|---|---|
| proj-991 | Yes | Required account included |
| proj-992 | No | Required contractor account missing |
| proj-admin-993 | Yes | Required privileged account included |

It also contains proj-994, which should have been excluded.

There are three accounts in the expected set and three in the preview. Every included account has an Export Records item. The totals match, but the membership does not.

Inspection establishes the cause: the saved people selection used the Engineering department as a substitute for current project membership. That misses the contractor and includes an employee from another project.

The source data is correct. The access selection is already restricted to Export Records. Refreshing data or changing the access choice would not repair the demonstrated people-selection problem.

Correct the selection through the supported process using the verified project roster. Then inspect the actual resulting work.

In the supplied corrected preview, P-861, proj-991, proj-992 and proj-admin-993 are present, and proj-994 is absent.

P-861 is a distinct generated instance. Retain the failed comparison and the correction rather than describing P-860 as though it had always been correct.

The population criterion now passes for the inspected instance and inputs. That does not automatically pass the reviewer or fulfillment checks.

## Write a check that another person can follow

A **test case** describes starting conditions, a check or action, and the expected result.

Include enough detail to identify the environment, source, account, review item, relevant configuration and actor. State what evidence will be examined and who will judge the result.

For the contractor case, the starting condition is a current project member with correctly collected Export Records. The expected result is inclusion of that account and item, assigned to a suitable independent reviewer.

For the outside-project case, the same entitlement exists, but the person is not in the approved roster. The expected result is exclusion from this campaign.

Those cases test different decisions. Repeating the employee case many times would not establish that contractor inclusion or outside-project exclusion works.

Choose cases for the conditions that can change the result. Depending on the requirement, those can include a privileged account, missing manager, package-held access, absent reviewer, failed write or manual task.

An **access profile** packages entitlements. A **role** groups access for a responsibility. If an entitlement is represented through one of those objects, an individual-entitlement expectation may be wrong.

Record the actual reviewable object and permitted decision. Do not make a failing test pass by assuming the package behaves like a separately held permission.

A useful planning record connects the check with evidence:

| Requirement | Expected result | Evidence and responsible check |
|---|---|---|
| Correct project coverage | Include the three required accounts and Export Records; exclude proj-994 | ISC engineer compares the complete generated set with the approved roster and account inventory |
| Independent review | Each actual assignment reaches a knowledgeable, authorized reviewer who is not reviewing their own access | Campaign owner checks generated assignments and relevant self-review handling |
| Usable decision context | Reviewer can identify the account, permission meaning and current need | Business and application owners confirm descriptions and supporting context |
| Required manual removal | Authorized operator can remove export while retaining justified reading | Fulfillment owner checks a controlled exercise and the production-specific prerequisites |
| Verifiable outcome | Actual rejected access can be traced to source evidence and retained access | Evidence owner defines the account/result/time records to retain |

The record is useful only when its expected results are compared with actual evidence.

## Check the data and assignment prerequisites

A **connector** is the integration used to read source data or make changes. **Account aggregation** reads account information into ISC.

For a data-readiness check, inspect the actual relevant accounts and holdings, their collection time and the result of the collection. A successful job that did not include the required account is insufficient.

**Account correlation** associates the account with its owning identity. Verify that association when the review depends on the person's identity.

If managers drive assignment, inspect the resolved manager relationship as well. **Manager correlation** establishes that link from configured matching information.

Then check the actual recipient in the generated review. A populated manager field or a saved reviewer option does not replace the assignment result.

Include the relevant missing-input case. For example, dedicated manager campaigns exclude identities without managers, while the Search-based Manager choice documents transfer to the campaign creator when a manager is undefined.

Use the expected result for the actual route. Do not combine those behaviors into a universal missing-manager test.

For self-review, verify that a person does not end up approving their own access. Automatic routing and manual reassignment have different conditions. The documented reassignment path also restricts signed certifications.

Keep a candidate who has the right name separate from a reviewer who has the required knowledge, independence and permitted visibility.

## Check the decision flow at the right stage

**Approve** accepts continued access to the reviewed item. **Revoke** records that the reviewed access should be removed. **Sign-off** is final confirmation of the assigned review's choices.

ISC's newer, next-generation flow separates saving choices from that final confirmation.

A controlled check can therefore distinguish a saved choice from a successfully finalized review. Do not use an item-completed indicator as proof of every required confirmation.

Plan how comments, unclear decisions and unfinished work will be handled. The expected result should follow the approved business criteria and the actual supported campaign behavior.

If an administrative completion case has an unresolved outcome for the relevant engine and state, resolve that exact case before relying on it. A plan entry saying “test passed” cannot supply a missing product contract.

Name the owner who must establish the supported behavior and hold the dependent use until the answer is supported. Another passing case does not resolve that uncertainty.

For notifications, check the intended event, recipient and actual delivery through the permitted test arrangement. A visible review and a delivered email are different results.

Also verify the deadline and whether it leaves time for reviewer work, fulfillment and the required evidence. A date field being saved does not establish that the workload is feasible.

## Prove the fulfillment path without confusing environments

**Remediation** is the work needed to carry out a removal decision. **Provisioning** changes external accounts or access.

In this example, the production connection can read account data but cannot change permissions. The applicable removal path is manual.

Before launch, establish the actual work recipient, available authorized operators, usable instructions and a way to verify the account result.

A preview comparison cannot prove that a future human task will be performed correctly.

If the plan requires exercising Revoke, use approved isolated test accounts and an appropriate test environment. Finalizing review decisions can initiate removal work; it is not a universal harmless simulation.

The following are supplied example results from such a controlled exercise.

An operator marks the removal task complete. The current test account still has Export Records.

The task step completed, but the account-result criterion failed. Calling the test successful would hide the work it was intended to check.

The responsible owner corrects the actual external change. Rechecking the failed account-result criterion with current test-source evidence now shows export absent and required reading retained.

That checks the correction. If the plan also requires a fresh exercise of the entire decision-to-removal path, arrange a separate permitted test case; do not assume the earlier signed review can simply be reopened.

That supports the result of the controlled exercise. It does not establish that the production environment has identical permissions, routing or operators.

Check those production-specific prerequisites separately. After real production reviewers make and finalize decisions, verify the actual required outcomes for the real accounts.

Before launch, the question is whether the planned process is ready to perform and verify the work. Later, the question is whether that work actually achieved each required result.

## Record what happened when a check could not pass

A result record should keep the expected result, actual observation, evidence, relevant time, environment and responsible person together.

You can use simple labels in that record:

- **Pass**: the inspected result meets the criterion within the stated scope.
- **Fail**: the check ran and the observed result did not meet it.
- **Blocked**: a required prerequisite prevented the check from being completed.
- **Not run**: the check has not yet been performed.

These labels describe your verification record. They are not interchangeable with ISC's campaign or task statuses.

If the intended manual operator has no permitted access to the test application, the removal check may be blocked. That is not proof that the connector failed or that the removal succeeded.

For P-860, the population check failed. For P-861, the population check passed. If recipient visibility has not yet been checked, leave that separate result unverified.

Do not turn a whole plan green because one important check passed.

Agree in advance which unmet requirements prevent starting and who can authorize any bounded exception. Record its scope, reason, owner and follow-up under the organization's process.

A missing required account should not disappear from the requirement merely to make the preview pass.

## Retest the repair and check what depends on it

A **retest** repeats the relevant check after a correction.

For P-861, repeat the membership comparison against the independent expected set. Check both the previously missing contractor and the account that should have been excluded.

Then inspect results that depend on the changed selection, including the resulting items and reviewer assignments.

A **regression check** verifies that a change has not broken another required behavior that previously worked.

For example, correcting contractor inclusion must not remove the privileged account or send its review to the person who owns that account.

You do not need to repeat every unrelated check automatically. Identify which requirements depend on the changed data, rule, actor or configuration, and keep the reason for reusing earlier evidence.

If the earlier evidence no longer matches the actual conditions, it cannot establish current readiness.

Preserve failed results and their corrections. Record the relevant new campaign instance or configuration, instead of overwriting history with an unexplained pass.

A new report download is not a retest of selection logic or external removal. It is only new evidence when its actual generation and underlying records answer the required question.

## Make the decision to start explicit

Bring the relevant evidence together: current input coverage, correct preview contents, suitable assignments, usable context, permitted decisions, delivery arrangements, realistic timing and the planned evidence.

Record unresolved work honestly. The accountable business owner and the authorized platform operator have different responsibilities; business acceptance does not itself perform activation.

A generated-preview indicator establishes that work is available for inspection. It does not establish that the campaign meets your project roster.

For a recurring campaign, check the actual new instance and inputs. A previously accepted template does not prove that this cycle's accounts, managers and operators are still correct.

The diagram separates these checkpoints:

```text
Approved requirement and expected results
                    |
        Check inputs and required capabilities
                    |
        Inspect the actual generated preview
                    |
       Correct contents, assignments and settings?
                    |
       Verify the planned fulfillment path safely
                    |
       Resolve blocking gaps and record authority
                    |
             Ready to start the campaign
                    |
       Real reviewer decisions and final confirmation
                    |
       Actual removal work and current account evidence
                    |
       Accept the achieved results or retain open work

A changed input can invalidate dependent evidence.
Recheck what relies on that input before proceeding.
```

Use the checkpoints to distinguish readiness to start from acceptance of the achieved results. The actual production removals can only be verified after the relevant decisions and work occur.

After launch, track the actual decisions, final confirmation, required changes and account evidence. A successful representative test does not replace reconciliation of every required production result.

## Try a change after the earlier test passed

A separate Training Records source uses the Web Services SaaS connector, which integrates ISC with an application's web interfaces.

A controlled removal exercise passed using technical integration account **T-17**. The current review scope and assignments are correct.

Before activation, the configured integration account changes to **T-22**. A connection check succeeds and account data can be read.

Someone says the old removal test still proves readiness because the connection works.

Which condition changed?

The account that will perform the write changed. T-17's successful removal does not establish T-22's authority to remove the same permission.

The passing read check establishes only what it actually exercised. Do not mark the new write requirement passed while its authorization and result remain unverified.

Identify the exact configured identity, required operation, permitted source authority and appropriate controlled check. If a prerequisite is missing, record the fulfillment check as blocked; if it simply has not been exercised, record it as not run.

If inspection finds a missing prerequisite, correct it through the approved process. Then perform the appropriate check for the new configuration. Do not assume that giving broad administrator access or creating a manual fallback is the required fix.

The earlier population evidence can still be useful if its own inputs and instance remain unchanged. Reassess the evidence that depended on the replaced integration account.

Even a new successful controlled removal would establish that test's result, not every future production outcome. Keep that distinction in the plan and in the decision to proceed.

