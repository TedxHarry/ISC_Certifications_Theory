# Build an evidence trail someone else can verify

A task says Completed. A report says Revoke. A file no longer contains Export.

Do these records prove that the right person's access was removed?

Let's connect them before answering. We need the same person, source, account and permission all the way through. We also need to know when each record was true.

## Choose one removal to explain

A **campaign** organizes access reviews. A **certification** is an assigned review inside it.

**Approve** records that reviewed access should be kept. **Revoke** records that it should be removed. **Sign-off** is the reviewer's final submission of those choices.

ISC's **identity** is its record for a person. That person can have an **account** in a managed system. A **source** holds ISC's configuration and collected account information for that system. The particular right we are reviewing, such as Export, is an **entitlement**.

An **attribute** is a field in a record. In this case, the account's `groups` field holds permission values. We need both the field name and the particular value being removed.

Our case is employee02's Export removal:

- Identity: `certlab-employee02`.
- Source A: `certlab-reports-csv`.
- Account: `certlab-account02`.
- Entitlement attribute: `groups`.
- Entitlement value: `certlab-report-export`.

Employee02 still needs Read, represented by `certlab-report-read`, on the same A account.

A starts with three accounts and five holdings. One holding means one account having one permission:

| A account | Identity | Before removal | Required result |
|---|---|---|---|
| certlab-account01 | certlab-employee01 | Read + Export | Read + Export |
| certlab-account02 | certlab-employee02 | Read + Export | Read only |
| certlab-account03 | certlab-employee03 | Read only | Read only |

Source B, `certlab-owner-reports-csv`, stays at four accounts and six holdings. Its matching account names and permission values are different source records.

The business requirement is to remove only employee02 A Export, retain A Read and leave the other holdings unchanged.

This source uses CSV uploads. A **manual task** asks an operator to carry out the required change. Editing the file simulates the external change; it does not change a real reporting application. **Aggregation** reads the supplied account data into ISC. We need evidence of the review, the actual file used, successful collection and the resulting account data.

## Reuse a real record before creating another review

Start by looking for an actual completed review of individual entitlements. It must have this one A removal, a verified reviewer sign-off and removal work whose result is known. Keep the actual campaign name, record IDs, full review scope and decisions.

A wider review can be used if its full scope is known and its other changes agree with the unchanged A/B holdings above. The only A removal must be the one named here. Do not describe a five-item review as a two-item review just because two items interest us now.

If the training data has already been reset, record that fact. Do not change the current account merely to recreate an old screenshot. We will distinguish the historical removal result from the later restored state.

The administrator needs access to the actual campaign, reports, task/account details and existing private run records. Access to an expected-result file is not evidence that a run occurred.

If there is no usable completed record, capture one through the small path below. Otherwise, continue directly to the evidence index.

## Capture one small case only if you need it

Use the three employee identities and two manager identities from the training setup, with correct manager relationships and working manager01/02 sign-ins. Importing their people records does not by itself give them working reviewer sessions. Employee02's manager must be manager01.

A's **source owner**, the person responsible for the source in ISC, should be `certlab-manager02`. The authorized administrator also needs permission to create this campaign and upload the source file.

Verify A's original five holdings and B's original six. Use complete private files prepared against the actual source templates if restoration is needed. First preserve and resolve earlier work.

A's original values are in `lab-data/baselineA/report_accounts.csv`; B's are in `lab-data/baselineB/owner_review_accounts.csv`.

Keep the rights as individual entitlements. Check that earlier test profiles, roles or lifecycle settings do not restore the rejected right or change the review items. Check that no reassignment setting redirects this review.

Open **Search > Certification Campaigns > New Campaign > Identities**. Under **Using a Search Query**, choose **Create Campaign**, then **Specific Identities that I Select**. Find `name.exact:"certlab-employee02"`, inspect the person, use **+ Add To Campaign**, check the added list and choose **Certify Selected Identities**.

Use **Refine Access Items** to add only A Read and A Export. Name the configuration `certlab-015-evidence-run01`. If that name already exists, use an unused run suffix and record it; keep earlier history.

Choose **Manager** so employee02's recorded manager receives the review. Set a permitted future deadline. Choose to maintain undecided access when completing the campaign: an item left without a decision keeps its access under that setting. Require Revoke comments, or all comments if that is the offered rule. Turn campaign emails off and use no extra filter or recommendations.

A **template** stores campaign settings. A **preview** is the generated work you inspect before releasing it to reviewers. Choose to generate the preview now and save it as a template, without a future schedule. Record the template and generated campaign references separately.

Verify the two employee02 A holdings, manager01's responsibility and actual certification IDs before **Start Campaign**. In manager01's session, Approve the still-required Read and Revoke Export because bulk-export work ended. Inspect the saved reasons and use **Finish** on all actual assigned work. Verify final submission.

Now return to the administrator's session and inspect the resulting removal work. Open the task through the recipient's **Task Manager**, or administrator **Admin > Dashboard > Tasks**. Match the finalized decision and read the full requested work before changing anything. Do not infer a fixed number of tasks or assume the recipient from a role name alone.

Make a new copy of A's complete private account file and remove only employee02 Export. Compare values with `lab-data/baselineA/report_accounts_after_employee02_export_removal.csv`, preserving the actual template's required columns. Editing this file simulates an external account change; it does not change a real reporting application.

Upload through the supported task step, or open A under **Admin > Connections > Sources > Account Management > Account Aggregation**. Follow successful collection and inspect A's three accounts/four holdings and unchanged B six.

Verify employee02 Read and all other A rights remain. Complete only wholly fulfilled tasks using the recipient's **Mark Complete**, or the permitted administrator equivalent **Actions > Mark as Complete**. Capture the actual file, account, collection and task records before reset.

This fresh review has one Approve and one Revoke. The other A holdings are retained account data, not additional reviewer approvals. A reused wider review keeps its own actual counts.

If collection or fulfillment fails, retain the error and leave that part unresolved. Do not build a successful evidence story around an expected file.

## Make an index that explains the records

During the actual run, choose private storage outside the reusable course folder. Create a case folder such as `CLB-015/run01/`, using a new run name if needed. Keep original downloads and observations in an `originals` folder and your analysis in a separate `working` folder.

Create `evidence-index.md` in that private case folder. This is a short map to the evidence, not a replacement for the original records.

For example, an entry supporting retained A Read can use this blank format. Fill it from the actual records; leave a missing fact identified as missing.

```text
Claim: [the statement this entry supports]
Source, account and permission: [actual references, with IDs where available]
Original record: [filename or system record reference]
Person or system involved: [who performed the action or took the observation]
Event or observation time: [date, time and time zone]
Download time: [if different from the event or observation]
What the record shows: [the relevant details]
Limit or missing link: [what this record cannot establish]
```

For retained A Read, the supporting observation must concern A account02 after removal. An expected-result file or a current observation of another source cannot fill that role.

Use a small set of purposeful entries:

| Evidence entry | What it should establish |
|---|---|
| Requirement and actual campaign scope | Which access needed review and what removal was authorized. |
| Identity/source/account/right details | Exactly which person's account and permission the case concerns. |
| Final decision and sign-off | Who made the choice and who finalized the assigned review. |
| Removal work | What task or operation was created and what its recorded result was. |
| Account/file observation and collection | What was absent, what remained and when that was observed. |
| Later reset, if performed | Why the current training state may differ from the earlier removal result. |

Keep raw exports unchanged. Put annotations in the index or a marked working copy. When sharing training material, use a redacted copy and keep enough consistent references to follow the case.

Do not put passwords, tokens or unrelated identities into this package.

## Match the objects before interpreting the status

Open the actual campaign and source records. Record the real campaign, certification, identity, source, account and entitlement identifiers where the interface provides them.

ISC can give a stored account record its own internal ID. The source also has a key identifying the account there. Record which kind of reference you have. The supplied name `certlab-account02` alone cannot distinguish A's account from B's account with the same name; keep the source with it.

Check the entire connection:

employee02 → A account02 → groups → certlab-report-export.

A source B record with the same account name and Export value cannot establish what happened on A.

Use the actual entitlement details to confirm the value. In a campaign report, **Entitlement Name** can mean the attribute name, such as groups. **Display Name** describes the right. Neither label alone guarantees a unique permission across sources.

If a report exposes only names, open the corresponding source/account/access details and document how you matched it. Do not invent an ID or claim a field was present when it was not.

If those screens cannot supply a necessary record reference, record the specific gap for an authorized read-only API investigation. An API is a programmatic way to inspect supported records, but the applicable certification API and permissions depend on the actual campaign implementation. Do not guess an endpoint or change account data just to produce a missing link.

## Follow the people who actually acted

From **Admin > Certifications > Campaigns**, find the actual case and use **Actions > Download Reports**. Generate the available composition, status and sign-off reports.

In the status report, **Reviewer** is the person currently assigned the review. **Decision Maker** identifies who recorded the choice. They can differ if a review moved after the choice was entered. The sign-off report identifies final submission and can also reflect an administrator's action. Check each report's field meaning when matching the people.

Record the people shown by the actual records. Do not infer every actor from today's assigned reviewer.

For a manual case, distinguish the person assigned the removal task from the person who performed the permitted file upload. For a live system, record the actual external operator as well.

There is no need to reassign a review or administratively complete a campaign to create more interesting evidence. Use the events that actually occurred.

If a report is unavailable in the current state, record that limit and inspect the relevant actual review/task records. Check preserved original exports when an older record is no longer visible. An empty current view does not prove that no event occurred. Do not force another completion action merely to make a report appear.

## Connect the decision to the work and the result

Inspect the matching task in **Admin > Dashboard > Tasks**, including its completed details. Match its source, account, permission, action and actual recipient to the case.

Use a direct campaign/request/task reference when the actual record supplies one. If it does not, record the available references and explain the matching evidence. Do not assume every export contains one shared ID.

A nearby timestamp alone is not proof that this review caused a particular task or account change. A complete explanation also needs the matching objects, action and actual relationship evidence. If a necessary link cannot be established, record it as a gap.

For the CSV case, keep the actual uploaded file version and successful aggregation record alongside the account observations. Check that only employee02 Export disappeared and all retained rights remain.

The course's four-holding comparison file tells you the intended values. It does not show who uploaded a file, whether aggregation succeeded or what ISC contained afterward.

**Remediation** is the work that carries out the required removal. Regenerate its available report after the relevant changes. **Finished** can mean a manual task was marked complete. That supports the task's recorded completion; it does not independently establish a real application's permission.

Keep that limit in the conclusion instead of hiding it behind a green status.

## Keep the times attached to the facts

A decision time, sign-off time, account observation time and report download time describe different events.

If you download a report today, that does not mean the access changed today. A file's local modified time also does not, by itself, establish the time an application permission changed.

Preserve each original time and its time zone. For comparison, convert a copy of the times to one shared reference, such as **UTC**, Coordinated Universal Time. Keep the original values alongside the converted ones. Use the offset that applied on the event's date: places that change their clocks during the year do not always have the same offset. If a time zone is missing, record the gap rather than guess.

Use your timeline to explain the actual sequence: final submission, matching work, observed result, collection/task updates and any later reset. Do not invent a universal order between every internal platform event.

If a record does not supply an observation time, say so. A new observation can establish the present state; it cannot manufacture a missing historical observation.

## Find the broken reference in a working copy

Keep the original index unchanged, including any recorded gaps. Make a clearly marked working copy for this check.

In that copy only, replace the reference supporting “employee02 retained A Read” with an observation of employee02's **B** Read. If no B observation was retained, inspect B account02 now and record its source and actual observation time. That new check supports B's present state, not A's earlier result.

The account label and Read value may match, but the source does not.

Leave all source data, original reports, screenshots, timestamps and task states unchanged.

Now inspect the case as if someone else had handed it to you. Can the working copy still support its retained-Read claim? Which exact observation is missing?

<details markdown="block">
<summary>Read the reasoning</summary>

B Read does not prove A Read remained. The missing link is an observation of Read on the actual A account at the relevant time.

Restore the genuine A reference in the index and verify its source/account context. Do not fix the problem by relabelling B's screenshot or changing source data.

If no historical A observation was captured, preserve the gap. A fresh A check can support a statement about now, while the historical retention claim remains unverified.

</details>

Record what was wrong and how you corrected the working copy. Restore the genuine A reference, or mark the historical claim unverified if that evidence is missing, before using the index as the final case.

This exercise changes the evidence reference, not the person's access.

## Explain a later training reset honestly

Suppose the retained records show A Export absent after fulfillment, but the current account has Export again because the authorized training reset restored it.

The earlier sign-off did not disappear. The current-state claim changed after a later action.

Keep both observations and the actual reset record. Your conclusion should distinguish “absent at the captured post-removal observation” from “absent now.”

Do not overwrite the earlier evidence with a fresh report, or use an old report as proof of the present account state. Keep both versions with their purposes and generation times.

If the reason for the later access is unknown, leave it as an investigation. Do not assume every reappearing permission was a training reset.

## Extend the claim to a live target only with live evidence

The CSV package can establish actual ISC review/task events and the simulated file/account-data result. It cannot establish a live reporting system's authorization.

**Active Directory**, or AD, stores user accounts and groups. Direct group membership means the account is listed as a member of that group. If an actual connected AD run already exists, you can assemble its evidence separately.

For the ordinary removal case, source `certlab-ad-lab` is called **C**. The account is `certlab-ad-e01`, linked to employee01; the group to remove is `certlab-ad-exp-ok`, called **ExpOK**. The other test groups are `certlab-ad-read`, called **Read**, and `certlab-ad-exp-fail`, called **ExpFail**. These are test-group names, not proof of a reporting application's permissions.

Use the real source/account/group identifiers from that run. Do not substitute A's account02 aliases or the planned fixture specification.

Inspect **Admin > Identity Management > Activities** for the actual account operation. **Search > Reports > Provisioning Activity** also provides event details and a downloadable report.

The **connector** is the integration that communicates with AD. Match the finalized decision to its exact membership-removal operation and actual result. Keep the authorized operator's separate observation in AD, including the account, group, domain controller (the directory server checked) and observation time.

The starting set has four direct memberships: e01 Read+ExpOK, and employee02's AD account `certlab-ad-e02` in Read+ExpFail. The ordinary removal leaves e01 out of ExpOK and retains the other three memberships. A later recorded training reset restores the original four.

If the same run also contains later fault, recovery or additional removal work, keep those events in the timeline. The three-membership observation describes the ordinary removal checkpoint, not every later stage of that run.

A successful connector operation, independent target observation and later collection support different parts of that explanation. Do not substitute one for every other part.

If the actual AD run or target observation is missing, record the live outcome as Not run or unverified, according to what was actually performed. Do not create a new fault, manually remove a membership or claim a passed live outcome just to complete the evidence package.

## Finish with a conclusion someone can check

Write a short conclusion naming the actual scope, final decision/sign-off, matching work, observed account result and relevant times. State retained rights and the limits of the evidence.

If there is a gap, identify the missing record, who can obtain it and what claim remains unproved. That is more useful than declaring the whole case successful without support.

If you reused an existing case, this evidence work needs no tenant reset. Keep the original records, restore the correct working index and leave the current tenant state unchanged.

If you created the fresh capture case, preserve the closure evidence first. Resolve all outstanding work, restore A's complete private original file and run aggregation through successful completion. Verify the original rights in the starting table, A three accounts/five holdings and unchanged B four accounts/six holdings. Record this reset separately from the earlier removal result.

Keep signed campaign history. Remove only the now-unneeded, unscheduled `certlab-015-evidence-run01` template, or its recorded replacement name, from **Search > Certification Campaigns > Saved/Scheduled**. Match its saved reference and check no generation or work remains. Keep the completed campaign and its reports.

The finished package should let another person follow the same source account from the authorized decision to the supported result, without needing you beside them to explain away a missing connection.
