# Complete and defend an independent certification project

You have received a small access-review request. Your job is to turn it into correctly scoped work, handle a change while the review is in progress, and explain the result using evidence.

Choose the supported actions yourself. Save your plan before making changes. If you need help, record what help you used so the result describes what you actually demonstrated.

## The work request

Review the existing **Export Reports** access of employee01 and employee02 on both of these sources:

- A: `certlab-reports-csv`.
- B: `certlab-owner-reports-csv`.

An **identity** is ISC's record for a person. A **source** holds ISC's configuration and collected account data for a managed system. An **account** is the person's record on that system.

An **entitlement** represents an individual right. Read Reports uses `certlab-report-read`; Export Reports uses `certlab-report-export`. The account's `groups` attribute is the field holding those permission values.

Matching names and values on A and B are separate source-specific access objects.

A **source owner** is the person responsible for the source in ISC. That responsibility is separate from deciding whether a particular employee needs access.

Only the named employees' existing Export rights belong in the review. All Read rights must remain. Employee03 and the source owner's account are outside the decision scope; their access must remain unchanged.

Use the existing recorded manager for the initial review responsibility.

## Establish the starting facts

A **holding** means one account having one permission. Use the three employee identities, two manager identities and these starting account records:

| Source | Account / identity | Starting holdings |
|---|---|---|
| A | certlab-account01 / certlab-employee01 | Read and Export |
| A | certlab-account02 / certlab-employee02 | Read and Export |
| A | certlab-account03 / certlab-employee03 | Read |
| B | certlab-account01 / certlab-employee01 | Read and Export |
| B | certlab-account02 / certlab-employee02 | Read and Export |
| B | certlab-account03 / certlab-employee03 | Read |
| B | certlab-account04 / certlab-manager02 | Read |

A has three accounts/five holdings; B has four accounts/six holdings. Verify the actual records rather than assume that a previous exercise restored them.

The original people records make manager01 the manager of employee01/02. Employee03 is managed by manager02. Both application sources should be owned by manager02.

Use the working `certlab-manager01` and `certlab-manager02` test sessions. Imported people records alone do not establish working sign-in.

The administrator needs the permitted campaign, existing unsigned-review transfer, report, task and source-upload actions. Verify that the intended replacement reviewer can receive the selected work without reviewing their own access.

The selected rights must remain direct individual entitlements. A profile or role can package or require access; a lifecycle grant can supply it based on the person's business state. None should change this case. Check for old review redirects, pending removals or temporary models before beginning.

Use complete private source-template copies for any permitted file preparation. Initial values are in `lab-data/baselineA/report_accounts.csv` and `lab-data/baselineB/owner_review_accounts.csv`.

Do not restore or alter data while earlier work could still apply. If the starting state is not ready, record what is missing, who must resolve it and what can safely continue.

## Read the initial work evidence

These are the supplied business facts:

| Person and source | Current work information |
|---|---|
| Employee01 on A | The bulk-export work has ended. No continuing Export need is authorized. |
| Employee01 on B | Current authorized work still requires bulk export. |
| Employee02 on A | Current Export need has not yet been confirmed. |
| Employee02 on B | The bulk-export work has ended. No continuing Export need is authorized. |

All Read access remains needed. Do not infer one source's need from the other source's similar permission label.

**Approve** records that access should be kept. **Revoke** records that it should be removed. An **undecided** item has no recorded choice. An unanswered business question is not confirmation of either choice; keep that uncertainty visible until the supplied update resolves it.

## Save your approach before acting

Choose private storage outside the reusable course folder and create a case folder such as `CLB-017/run01/`. Use `certlab-017-` names for objects you create; `certlab-017-csv-run01` is a suitable case name. Use an unused run suffix if needed and record the actual names and references.

A **campaign** organizes reviews. A **certification** is an assigned review inside it. A **preview** shows generated content before activation. A saved **template** stores settings for generating review work; it is separate from the generated campaign.

Write a short plan covering:

- The exact people, accounts, sources and rights you will include and exclude.
- The supported review route, actual initial reviewer and permissions you need.
- How you will establish the starting data and validate the preview.
- What evidence will distinguish saved choices, final submission and removal.
- How you will protect retained access, handle incomplete work and restore the training baseline.

Choose your configuration and generate the preview. Inspect its complete actual items and recipients. Save that observation before starting reviewer work.

Keep this attempt unscheduled and campaign notification emails off. Record any saved-template reference separately from the generated campaign reference. Do not change tenant-wide settings or unrelated sources to make the project work.

You may consult official product references for supported controls. Record coaching, a supplied query or other help beyond the stated request. Do not open worked assessment material before recording your attempt if you want the result assessed as uncoached.

## Reach the first checkpoint before reading the update

A saved **draft** can still be checked before final submission. That final submission is called **sign-off**, performed through **Finish**. The review remains **unsigned** until then.

Start the verified scoped review. Have the initial reviewer save at least one choice that the available facts justify, then reopen it to check what was actually saved.

Keep **every assigned certification unsigned** at this point. Do not finalize while a required business answer is still missing.

Save the actual campaign/certification references, current reviewer, chosen item, saved choice and unsigned state. Do not assume a tab named Completed means the whole review was signed off.

Once that checkpoint is recorded, continue to the update.

## Apply the new work information

<details markdown="block">
<summary>Read the update after recording the checkpoint</summary>

The following update now applies:

- Manager01 is unavailable for the rest of this review.
- Manager02 has been expressly authorized to cover these selected employees' review work.
- Employee02's A bulk-export work is now confirmed as current and authorized.
- All other supplied access needs remain unchanged.

</details>

The change is who handles these existing reviews. Keep the people's recorded manager relationships unchanged. Limit the handover to this attempt's work; inspect the complete contents of each certification before transferring it.

Adapt the existing work through the supported route. Verify recipient eligibility and the actual effects on saved choices and history. Do not assume a saved choice or decision-maker field will survive transfer in a particular form.

Do not delete work to hide a handover, bypass final submission or claim an administrative action was the reviewer's own decision.

The authorized reviewer must assess the complete scope using the updated facts, record clear reasons and finalize the actual assigned work. Preserve the relationship between initial responsibility, saved work, the handover and final submission.

If the actual environment cannot perform the supported transfer, record that execution limit and a safe handover. Do not invent an API or substitute a global reassignment rule.

## Complete the resulting work and prove what remained

A finalized removal decision may still need **remediation**, the work that carries it out. A **manual task** asks an operator to make a change that the file-based integration cannot write automatically.

Inspect the actual tasks and their complete requested changes. Distinguish review responsibility from source ownership, file-upload permission and the actual person performing the work.

Choose the correct complete private file for each source. Derive its required changed values from this request and the final decisions. Do not reuse an earlier exercise's result merely because its row count looks plausible.

Follow actual collection and work states. **Aggregation** reads account data into ISC; an accepted upload alone does not establish the collected result.

Verify each account and permission that should change, each right that must remain and the untouched people/accounts. If one change is complete while another is outstanding, keep that distinction in your progress record. Do not close a task containing unfinished requested work.

The CSV result is actual ISC review/task/data work over simulated external account files. It is not proof of a live reporting application's authorization.

If the result differs, investigate the precise source/account/right and its actual decision, submission, task, file and collection evidence. Explain the cause you established or the specific gap you could not resolve.

## Submit a case someone else can follow

Keep the original records and prepare:

1. Your readiness findings, initial plan and preview evidence.
2. The saved unsigned checkpoint, released update and actual reviewer-transfer observations.
3. Final choices, reasons, decision makers and sign-off evidence.
4. Actual work records, source-bound file versions, collection results and account observations, including retained rights.
5. Fresh available reports and a short index linking the records by actual objects and times.
6. A closure note, or an accurate handover naming unresolved work, the responsible person and the next safe action.

Record the actual human operating each test session. If one person operates several training roles, say so; separate accounts do not establish independent human review.

Do not invent missing identifiers, screenshots or historical observations. Current evidence supports its observation time; a later reset must be recorded separately.

A safe handover is a useful result. It does not mean an unfinished removal has passed its execution outcome.

## Restore the setup after preserving the result

Keep signed review and task histories. Resolve outstanding removals and generation before restoring permissions for another training attempt.

Use the complete private original source files to restore the starting A and B inventories shown above. Follow aggregation through successful completion, then verify the exact accounts, holdings and identity links. Do not change the people data or manager relationships as a shortcut.

Retire only this attempt's now-unneeded unscheduled templates, matching their saved references and names after accounting for actual work and generation. Preserve the signed campaigns and their reports. Campaign deletion is not an assumed cancellation or access-restoration method.

Record the controlled reset as training preparation, separate from the completed review's business decision.

## Attempt the connected project only when its setup is ready

The CSV project can be assessed without a connected directory. **Active Directory**, or AD, stores user accounts and groups. A **direct membership** means the account is explicitly listed as a member of a group. A separate connected outcome needs actual membership changes and observations in AD.

For the connected project, use source `certlab-ad-lab`, called C here, with the approved automatic membership-write setup. Verify the real source/account/group identifiers, actual read/write authority and account links to the existing identities.

Start from these four direct test memberships:

- `certlab-ad-e01`, linked to employee01: **Read** (`certlab-ad-read`) and **ExpOK** (`certlab-ad-exp-ok`).
- `certlab-ad-e02`, linked to employee02: **Read** (`certlab-ad-read`) and **ExpFail** (`certlab-ad-exp-fail`).

Use ordinary non-nested groups. These names describe test memberships; they do not prove that a real reporting application uses them.

No earlier test permission block, manual-fulfillment configuration, pending write or automatic assignment should interfere. Do not onboard or reconfigure a shared target merely to make the assessment available. If readiness is missing, record this outcome as Not run.

Use `certlab-017-ad-run01`, or an unused run name, and a separate private evidence folder after the CSV project has been resolved and reset.

The connected request is to review only e01's ExpOK and e02's ExpFail memberships. Both Read memberships must remain. The initial facts are:

- Employee01's need for ExpOK has ended.
- Employee02's continuing need for ExpFail awaits confirmation.
- Initial review responsibility follows the recorded manager.

Plan and validate the exact connected review. Record the same active-but-entirely-unsigned checkpoint after at least one justified draft choice.

<details markdown="block">
<summary>Read the connected update after recording its checkpoint</summary>

Manager01 is unavailable, manager02 is authorized to cover the selected work, and employee02's ExpFail need is confirmed as continuing.

</details>

Apply that update to this connected review's existing unsigned work. Preserve actual transfer/history and final submission evidence separately from the CSV attempt. Keep the people's manager relationships unchanged.

Carry out and investigate the resulting supported automatic work. Obtain directory observations from the authorized operator and reconcile later ISC collection. The target check must inspect AD itself, independently of ISC's status. Record which directory server was checked and when; account for differences between directory copies before interpreting a mismatch. Verify retained memberships as carefully as removed ones.

A CSV edit, closed manual task or manual membership removal cannot pass this automatic connected outcome. A failed or pending write remains unresolved until actual recovery is established; otherwise submit a precise handover.

Preserve evidence and resolve pending work before the authorized directory operator restores the original test memberships. Verify all four starting memberships and collect C again. Keep the original A/B setup unchanged.

## Record what you demonstrated

Report the CSV outcome, connected outcome, reset readiness and assistance used separately.

A self-checked run is not an observed third-party assessment. A run completed with coaching is not an uncoached pass. Looking up a supported control is normal engineering work; record the help that affected your decisions.

Be ready to explain why your scope was correct, how the update changed responsibility and knowledge, what each completion status proved, and which record supports the final account state.

Your explanation should still make sense if someone asks about a different source, an unsigned review or an unfinished removal. Use the relationships and evidence you inspected, rather than a remembered sequence of clicks.
