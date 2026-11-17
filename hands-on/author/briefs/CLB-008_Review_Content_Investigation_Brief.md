# CLB-008 brief: trace a missing and an extra review item

November14,2026. Saved before learner prose.
Learner filename: CLB-008_Investigate_Missing_and_Unexpected_Review_Items.md.

## Distinct practical task

Diagnose an intentionally misconfigured, unstarted Search preview against an explicit business requirement. The data is correct. Two independent selection mistakes produce a same-count wrong result: employee01's A Read and Export instead of employee01/02's A Export.

Trace each symptom to the earliest mismatching evidence. Repair the subject selection first, inspect its four-holding intermediate result, then repair access refinement and inspect the correct two-holding result. Count alone goes two/four/two and cannot determine correctness.

This adds a reproducible investigation and controlled repairs to005's selection teaching. It does not repeat007's source-change/scheduling experiment or a complete removal cycle.

## Baseline and authorization

Use an approved administrator allowed to inspect source accounts/identities and create previews. Prepared people and manager links, A original three accounts/five standalone holdings and B four accounts/six holdings must be verified. Employee01/02 are managed by manager01.006's temporary model and007's pending schedule are retired/restored before baseline-dependent execution.

No new CSV, collection, account association, manager mapping, profile, role, filter, source or access grant is intentionally changed. Both A definitions remain. Only three isolated immediate preview/template configurations are created during a future run; all stay unscheduled and unstarted.

## Requirement and fault

Correct requirement: employee01/account01/A Export and employee02/account02/A Export, manager01 reviewer, no Read/B/other subjects.

Use the exact two-name candidate query from005/007. In the faulty configuration add only employee01, despite both candidates being returned. Refine access to both Read and Export definitions on A. No campaign filter. Generate preview now and save template, never the start-now option.

Expected faulty result: employee01 A Read+Export, two holdings. Missing employee02 Export is an identity-added-list fault; extra employee01 Read is an access-added-list fault. Candidate query, collected rights, associations and managers are not changed.

Names: certlab-008-initial-run01; certlab-008-people-fixed-run01; certlab-008-corrected-run01.

## Investigation and correction

Compare complete actual tuples against the two required tuples, not just count/names. Inspect employee02's A account and identity link, Search candidate, Added to campaign subject list, selected access, no-filter state and actual first preview ID/time. Explain correlation only as the account-to-person link; do not re-correlate correct data to fix campaign selection.

Build a separate fresh configuration using documented creation steps rather than inventing an Edit/Duplicate/Regenerate control. Preserve first evidence. Change only added subjects from one to two; keep both A rights, Manager and other settings constant. Expected intermediate four holdings: both Read+Export for both people.

Build final configuration with both people and only A Export. Expected correct two tuples, no Read/B/extra people, manager01. Separate original preview evidence from new generation; no universal live-preview refresh behavior claimed.

Do not force fixture counts if actual input/model differs; record discrepancy and inspect the first actual mismatch.

## Changed reasoning and wider triage

Exercise predicts an alternative repair order: fix access first while employee02 remains unadded → one employee01 A Export holding; missing employee02 remains. Then add employee02 → two correct Export holdings. Avoid activating the extra alternative solely for the exercise.

Provide a compact evidence-based branching guide for genuinely absent source data, wrong account association, missing Search candidate, missing added subject, wrong access/source/filter and profile/role review units. These are first checks, not broad unverified repair procedures. Wrong reviewer is a separate manager/configuration investigation;009 owns transfer of actual review responsibility.

Do not test Role/account-filter edge semantics, change manager links or corrupt correlation to manufacture an issue. OQ-06/08 and other inherited behavior questions stay open.

## Evidence and reset

Keep intended versus actual tuples, account/identity facts, candidate/added lists, access selections, template/preview IDs, generation times, cause statements and each controlled correction. No fake screenshot or learner execution claim.

Confirm never started/no decisions/no delivery work. Delete only008's unused unscheduled saved configurations and unstarted preview instances after evidence preservation; reconcile accidental activation or dependencies before routine cleanup. Verify A five/B six and unchanged managers/associations. No CSV reset is needed when inputs stayed unchanged. Preserve prior work.

One complete learner file plus author record, no diagram/table quota. All tenant actions remain zero; no repository or publication.
