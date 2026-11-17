# CLS-006: Automate a bounded read-only evidence collection

You have checked a campaign manually and matched its assigned reviews, access items and decisions. Now you need to collect the same evidence again.

Doing every request by hand can become repetitive. Automation can repeat those reads, but it must also repeat the checks. Otherwise, it can save an incomplete first page faster than a person would.

A **collector** is a program that gathers and saves the responses for you. A **capture** is the saved set from one run. **Bounded** means we set limits on what it may read, how many requests it may send and how long it may continue.

You will configure the collector for one known campaign, check the setup, run the permitted reads and compare the capture with your manual evidence. The **script**, the supplied Python program, collects information. It does not approve access, sign off, change a campaign or remove a permission.

## Understand what we are repeating

An API is a supported way for a program to request information from ISC. A GET request reads information.

A campaign organizes review work. Its certifications are the assigned reviews. Each certification contains review items, such as a person's Export permission. **Approve** means keep that access; **Revoke** requests its removal. **Sign-off** is the reviewer's final submission of the assigned review.

The collector follows this relationship:

> One verified campaign
>
> → Its expected assigned certifications
>
> → Every page of review items and decision summaries
>
> → A private capture for a person to check

A successful request is only one part of the task. The collector must establish that it read the expected records, completed the pages and found the expected relationships.

That is why we will give it the actual campaign and certification IDs already verified manually. An ID identifies an exact record. A name or a familiar-looking identifier is insufficient.

## Start with a working manual case

Use an actual next-generation identity campaign whose API reads have already worked through the supported contract. Its signed review must contain these two A Export holdings:

| Person and account | Source | Entitlement value | Signed decision |
|---|---|---|---|
| certlab-employee01 / certlab-account01 | certlab-reports-csv | certlab-report-export | APPROVED |
| certlab-employee02 / certlab-account02 | certlab-reports-csv | certlab-report-export | REVOKED |

An identity represents a person. An account is their record in the managed system. An entitlement is a tracked permission. A holding means one account has one permission.

The real certlab-cls004-context-run01 is suitable only if it was actually run, signed and manually inspected. A planned campaign or expected-result file cannot supply the history.

Have the actual campaign, certification, reviewer, source, entitlement, identity and account IDs available privately. Keep the matching ISC interface observations, the saved rejection reason and any removal/reset evidence with them.

Here, **A** means certlab-reports-csv, the source holding the simulated reporting accounts. **B** means certlab-owner-reports-csv, the separate source whose six holdings must remain unchanged. Export allows bulk report downloads; Read allows viewing reports.

The source can already be back at its five-holding training baseline. That later reset does not erase the earlier review. Historical removal and current account access still need separate evidence.

An **access token** is a credential sent with the API requests. Use an existing approved token with the required read scopes and permission to inspect this case. The **caller** is the identity ISC sees when the token sends a request. A **scope** limits the operations the token can perform; it does not establish that the caller can read every assigned review.

Check the caller's actual authority before running. Writing admin in a configuration file grants no access. Keep any reviewer-limited view recorded as limited. The returned certifications must still match the complete set you verified manually for this case; a view missing required work cannot pass that check.

## Check the environment before using the collector

Use Python 3.11 or later on your training computer. From a terminal opened in this course folder, check:

~~~text
python --version
~~~

Python runs the supplied script. Its **standard library** provides the functions this collector needs, so there is no additional package installation. If Python is missing or older than 3.11, prepare the approved Python installation before continuing.

The supplied files are:

- tools/collect_certification_evidence.py, the collector.
- author/contracts/CLS-006_Config_Example.json, the configuration example.
- author/tests/test_collect_certification_evidence.py, the offline checks.

Use the same campaign engine and API contract that worked in your manual investigation. The **engine** is the implementation managing the campaign; the **contract** describes its supported requests and returned fields.

This collector uses /certification-campaigns/v1 for next-generation identity campaigns. Its selected operations are currently **experimental**, meaning their contracts can change. The collector sends the required experimental header. Confirm the current contracts and permitted experimental use before connecting.

The supplied connection supports a standard HTTPS address in the form tenant.api.identitynow.com, with no added path, port or embedded credentials. Use the actual verified tenant API address. A different domain or custom connection needs a reviewed adaptation; do not change certificate validation to make it connect.

A **redirect** asks the client to connect to another address. A **proxy** is an intermediary through which a computer sends requests. This collector follows no redirects and does not automatically use the computer's proxy settings. If your approved network needs different connection handling, resolve that preparation before the live run.

## Configure one exact expected case

In the course folder, create a folder named `private` if it does not already exist. Copy `author/contracts/CLS-006_Config_Example.json` into it and name the copy `cls006-config.json`. Open that copy in a text editor. Keep the supplied example unchanged.

If that private filename already exists, choose a new name and use it in the commands below. Preserve the old configuration so you can explain what changed between runs.

The example has blank actual identifiers deliberately. It cannot run until you fill them from your manually verified case.

A configuration file tells the collector where it may read and what result it should expect. It does not grant permission or change the campaign.

The file uses **JSON**, a text format that groups named fields and their values. An object uses `{` and `}`. An array uses `[` and `]` to hold a list. Keep quotation marks around text and separate entries with commas, preserving the example's structure.

Fill these fields:

| Field | What to enter |
|---|---|
| api_base_url | The verified HTTPS API base address for the training tenant. |
| campaign_id | The actual generated campaign ID, not its saved-template ID. |
| campaign_name | The exact name of that campaign. |
| caller_view | admin or reviewer, matching the actual authorized caller. |
| certification_ids | The complete manually verified array of assigned certification IDs for the case. |
| reviewer_id | The actual current reviewer ID; certlab-manager01 in the normal case. All selected certifications must have this same current reviewer for this collector. |
| source_id | A's actual source ID. |
| entitlement_id | A Export's actual entitlement object ID. |
| attribute_name | groups for this prepared source. |
| entitlement_value | certlab-report-export. |
| expected_items | The two actual identity/account pairs and their expected signed decisions. |

Inside `expected_items`, the APPROVED pair belongs to employee01/account01. The REVOKED pair belongs to employee02/account02. Replace their blank `identity_id` and `account_id` values with actual IDs. The first identifies the person in ISC; the second identifies that person's account on A.

Keep the entitlement value separate from its object ID. The text certlab-report-export is a source value, not the identifier to paste into entitlement_id.

If your campaign has one certification containing both items, certification_ids contains one actual ID. If it has two assigned certifications, include both. Do not add another campaign's review to make the count match.

The collector compares the returned certification IDs with this **pinned set**, the exact IDs you named in advance. It rejects both missing and unexpected certifications. A successful first response cannot substitute for the complete expected set.

If legitimate work has different current reviewers or another access model, keep this collector pending for that case. Verify a suitable case or arrange a reviewed adaptation; do not change real reviewers or expected IDs merely to make the script pass.

Keep the access token out of this file. The script asks for it through a hidden prompt only when you request a live capture.

## Check the configuration without connecting

Run:

~~~text
python -B tools/collect_certification_evidence.py --config private/cls006-config.json
~~~

Read the command in parts: `python` starts Python; `-B` avoids creating local bytecode-cache files; the script path selects the collector; `--config` names the private configuration it must read. Run it from the course folder so those paths point to the supplied files.

Without `--live`, this command checks the configuration and prints `CONFIG_CHECKED_NO_NETWORK` with a short summary of the fixed limits. It does not display a full request-by-request plan, ask for a token or send requests.

Read that result carefully. It proves the configuration passed the local checks. It does not prove the IDs exist, the token is authorized or the tenant supports the expected contract.

If a blank example field, wrong address or invalid ID is rejected, correct it from the verified manual evidence. Do not replace a missing value with an invented one.

Before a live run, compare the private configuration and the read sequence described below with the actual case. Confirm the complete certification set, the expected two source-account-permission relationships, signed state and the caller's authority.

## Know where the collector will stop

The collector has fixed limits for this small exercise:

| Limit | Purpose |
|---|---|
| One campaign and at most four pinned certifications | Keep the investigation tied to the checked case. |
| One record per page; ten pages per collection, including the empty final page | Exercise complete paging and catch an unexpectedly broad result. |
| Forty request attempts, including retries | Limit the total attempts sent to ISC in one run. |
| Fifteen-second network timeout | Bound individual network operations. |
| 180-second read budget, checked between reads and waits | Stop the collection from continuing indefinitely; socket timing can affect the exact stopping time. |
| Two retries for a temporary, retryable failed GET | Allow at most three attempts for that read: the first attempt and two retries, within the overall limits. |
| Thirty-second maximum retry wait | Stop with an incomplete result if the server requires a longer wait. |
| Two MiB, about two million bytes, maximum per response | Reject a response that is unexpectedly large for this case. |

These are limits chosen for this training collector, not general ISC limits.

A **page** is a portion of a returned list. The collector asks for the total using `count=true`, then checks the `X-Total-Count` response header. It requires that total on every list page, reads through a successful empty final page and rejects repeated IDs. Missing totals leave the capture incomplete.

It resets the offset, meaning the number of skipped records, for each new item collection. Finishing one certification's pages does not finish the others.

A **retry** sends the failed read again. For a retryable response, the collector respects `Retry-After`, the server's instruction about how long to wait. If that wait exceeds its limit, it stops rather than retrying earlier than permitted.

Authentication errors, wrong paths and denied access do not trigger automatic privilege changes or version switching.

## Run the explicit live capture

Create a new output name inside the course's private folder. For the first capture, use:

~~~text
python -B tools/collect_certification_evidence.py --config private/cls006-config.json --live --out private/cls006-run01
~~~

`--live` permits the GET requests. `--out` names the new folder where this run will save its results. Paste the approved access token at the hidden prompt; its characters will not be displayed. Keep it out of the command line and configuration file.

The output folder must be new. The collector refuses to reuse a previous capture or write outside this course's private area.

It then performs the checked reads:

First, it verifies the parent campaign. It retrieves all campaign-filtered certifications and compares their IDs with the pinned set.

For each certification, it checks the parent and reviewer, signed state and decision counts. It retrieves every item page, matches the exact person-source-account-entitlement relationships and compares the decision summary.

Finally, it rereads the relevant certification records, the parent collection and the campaign to check for observed changes during capture.

The script uses the same fixed GET routes throughout. It does not follow a URL supplied inside a response or execute an instruction found in a review comment.

## Read the result before relying on it

Open `run.json` in the new output folder with a text editor. Its `outcome` field starts as `INCOMPLETE`. It changes to `CAPTURE_CHECKS_PASSED` only after the collector's checks succeed.

The `mode` field should be `LIVE_GET` for a run that used the real HTTP connection. That label identifies the connection used; `outcome` tells you whether the capture checks passed.

CAPTURE_CHECKS_PASSED means the retrieved records passed these capture checks. It does not mean:

- A person independently verified the caller's authority.
- The review decisions were the correct business decisions.
- The rejected permission was removed from an application.
- The whole course or tenant passed validation.

Those conclusions need their own evidence.

The folder also contains numbered response files, such as `response-001.json`. Open them to follow the reads in order. Each records the request path and parameters, response status, selected headers, observation time and parsed JSON when available. An unsuccessful read can have a null body because raw error bodies are not retained.

The collector excludes the authentication header and redacts the token's literal value from its output. The responses still contain private tenant records, so keep the whole capture in the private case folder.

A mode of `OFFLINE_TEST` identifies synthetic test records. Those cannot establish tenant behavior.

## Compare the capture with the actual work

Trace the two items from the campaign through their assigned certifications. Check the actual person, account, source, entitlement, signed decision and reviewer against the interface and your manual record.

A **subject** is the person being reviewed in this identity campaign. In a returned item, open `certificationSubjectSummary`: its `id` identifies the review's subject-summary record; `subjectTargetId` identifies the person in ISC. Keep both. The dot notation in `certificationSubjectSummary.subjectTargetId` tells you which nested field to read.

The collector requires signed state and a dateSigned value. A completed field alone only means decisions were entered; it does not establish sign-off.

Record any actual item actor or reassignment history needed to explain who made a decision. The current reviewer is not automatically the person who made every earlier choice.

**Fulfillment** means carrying out the requested change. Inspect its separate evidence: the actual matching task, changed full private account file, successful account collection into ISC and historical account observations.

In this CSV case, the file edit simulates the application's permission change. Even a correct file and ISC result do not prove that a real reporting application removed Export.

The historical result should show employee02's Export removed, all three Read holdings retained, employee01 Export retained, A at four holdings and B unchanged at six.

If a later documented reset restored A to five holdings, record that later event and the current observation separately. Do not let the script's matching REVOKED decision stand in for removal proof.

The report leaves `manual_comparison_required=true` and `fulfillment_verified=false`. It also leaves `authority_verified_by_script=false` and `target_permission_verified=false`. These fields state what the collector has not established. Describe your separate checks in the case note; do not rewrite the saved report to turn them into automated verification.

## Preserve an incomplete capture and recover carefully

If the command reports `NOT_RUN`, it could not finish setup or save required output. There may be no `run.json` yet. Check the printed reason and any partial folder before another attempt.

If it reports `INCOMPLETE`, open `run.json`, read `reason_code` and keep the partial response files. That code names the check that stopped the run, not a new decision about anyone's access.

For example, a missing total, repeated page ID, unexpected reviewer, wrong source or unsigned certification means the capture did not meet this lab's contract. Some successful pages may still be useful evidence of what was observed.

A reported authorization or API-contract problem needs its cause checked. Do not broaden the token, edit expected IDs or disable a check merely to obtain a successful result.

If a manually verified correction changes the legitimate expected case, update the private configuration with that evidence. Preserve the old configuration and capture so the change remains explainable.

After resolving the cause, choose a new output folder:

~~~text
python -B tools/collect_certification_evidence.py --config private/cls006-config.json --live --out private/cls006-run02
~~~

Do not resume by overwriting run01 or deleting failed pages. The new capture starts its own complete read.

If interrupted, preserve any partial folder and treat it as incomplete. Resolve any startup or output-write failure before a new attempt.

## Repeat it without confusing change with failure

Perform another capture only after the first actual capture has been checked and there is a reason to repeat it. Use another new folder name.

Compare the expected campaign, certifications, person-account-entitlement bindings, decisions and sign-off. The observation times and response-file numbers can differ.

The script checks for changes it can observe. It cannot freeze the tenant into a single transaction while it reads.

If someone legitimately reassigns or changes work between captures, investigate that change. Do not hide it by comparing only the total number of items.

Repeating this collector sends reads again. It cannot submit another sign-off, duplicate a removal request or grant access, because those operations are outside its routes.

## Test a tempting shortcut

The collector stops because an unexpected reviewer ID was returned. Someone suggests replacing reviewer_id with whatever the latest response contains and running again.

Would that establish a correct result?

<details markdown="block">
<summary>Follow the missing check</summary>

It would remove the mismatch without explaining it.

First inspect the actual review and reassignment history. Establish whether the new reviewer is authorized and whether the current case still matches the investigation.

If the reassignment is legitimate, record its evidence, preserve the earlier configuration and update the expected binding deliberately. Start a new capture.

If the change is unexplained, keep the investigation incomplete. The collector's role is to expose a disagreement, not redefine the expected case automatically.

</details>

Use this as a reasoning exercise. You do not need to reassign live work to practise it.

## Use the offline checks for what they prove

You can run the supplied checks without a tenant or token:

~~~text
python -B -m unittest discover -s author/tests -p test_collect_certification_evidence.py
~~~

They use synthetic local records and a fake connection. No token or real request is needed. They check paging, scope mismatches, signed state, retry limits, protected output and repeat handling. The command should finish with `OK`; a failure needs investigation before relying on the collector.

Passing them proves those local behaviors under the tested conditions. It does not prove a live endpoint, real authority or a successful tenant capture.

The usable sequence is local checks, verified manual case, checked live capture and a separately recorded repeat. Each stage needs its own result.

## Finish without resetting tenant data

Keep the successful and incomplete captures, their matching configurations, the manual comparison and any unresolved gaps in the private case record.

Exiting the process ends this local run. The script does not save the token as a credential file.

There is no account, source, campaign or task reset because the collector changed none of them. Leave signed review and fulfillment history intact.

The result is a repeatable evidence-collection task with limits you can explain. Automated review decisions or permission changes would need a separately designed and verified workflow.
