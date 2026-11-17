# ISC Certifications Hands-On

Practise access reviews and certification campaigns in SailPoint ISC: prepare the data, make justified decisions, follow the resulting work and check what actually changed.

## Start here

1. Open [CLB-001: Check the training setup](lessons/CLB-001_Check_the_Training_Setup_Before_Creating_a_Campaign.md). Record the campaign choices and permitted training scope without changing the tenant.
2. Follow [CLB-002: Prepare fresh CSV sources](lessons/CLB-002_Prepare_Fresh_CSV_Sources_and_Prove_the_Review_Data.md). Prepare the five people, manager relationships, three application accounts, five permission holdings and two working reviewer sign-ins.
3. Complete [CLB-003: Run a manager review](lessons/CLB-003_Complete_a_Manager_Review_and_Check_the_CSV_Result.md). Check the review, final submissions, manual removal work and changed CSV data, then restore the training baseline.

Use the approved training tenant and fresh synthetic data. Keep actual identifiers, reachable test emails, credentials and tenant evidence private. The supplied CSV values must be fitted to the actual source's downloaded template before import.

## Continue with the task you need

The CSV route uses real ISC review operations when you perform them. The reporting application is simulated: editing and collecting its CSV represents an external change. It does not prove removal of a permission from a real application.

After the first review, work through CLB-004–010, then CLB-012–017 using each lab's checked starting state. CLB-011 needs a separately prepared AD connection and can wait while you continue the CSV work. The connected variants in CLB-012, CLB-013 and CLB-017 have their own readiness requirements; they do not block those labs' CSV exercises.

A lab may need its own feature or timing check. For example, absence cover needs the supported reassignment setup, and the overdue part of CLB-014 needs an actual deadline to pass. Keep that part pending while completing work whose prerequisites are ready.

| ID | Practical task |
|---|---|
| [CLB-001](lessons/CLB-001_Check_the_Training_Setup_Before_Creating_a_Campaign.md) | Check the training setup |
| [CLB-002](lessons/CLB-002_Prepare_Fresh_CSV_Sources_and_Prove_the_Review_Data.md) | Prepare the people, CSV source and reviewer sign-ins |
| [CLB-003](lessons/CLB-003_Complete_a_Manager_Review_and_Check_the_CSV_Result.md) | Complete the first manager review |
| [CLB-004](lessons/CLB-004_Review_a_Source_and_Separate_the_Owners_Access.md) | Review a source and handle the owner's own access |
| [CLB-005](lessons/CLB-005_Target_People_and_Access_Through_Search.md) | Select particular people and permissions through Search |
| [CLB-006](lessons/CLB-006_Compare_Campaign_Filters_and_Review_Units.md) | Compare filters and the access objects being reviewed |
| [CLB-007](lessons/CLB-007_Reuse_a_Template_and_Prepare_the_Next_Review_Cycle.md) | Reuse a template and schedule the next cycle |
| [CLB-008](lessons/CLB-008_Investigate_Missing_and_Unexpected_Review_Items.md) | Investigate missing or unexpected review items |
| [CLB-009](lessons/CLB-009_Transfer_Review_Work_and_Handle_Reviewer_Absence.md) | Transfer reviews and arrange cover for an absence |
| [CLB-010](lessons/CLB-010_Make_Clear_Decisions_and_Finalize_the_Review.md) | Record, revise and finalize justified decisions |
| [CLB-011](lessons/CLB-011_Verify_Automated_Removal_and_Recover_a_Write_Failure.md) | Verify automatic removal and recover a write failure — AD required |
| [CLB-012](lessons/CLB-012_Complete_Manual_Removal_and_Verify_Each_Result.md) | Complete manual removals and check partial work |
| [CLB-013](lessons/CLB-013_Investigate_Access_That_Remains_After_Revocation.md) | Explain access that remains after a removal decision |
| [CLB-014](lessons/CLB-014_Monitor_Campaign_Progress_and_Handle_Unfinished_Work.md) | Monitor progress and handle unfinished reviews |
| [CLB-015](lessons/CLB-015_Build_an_Evidence_Trail_Someone_Else_Can_Verify.md) | Build a traceable evidence package |
| [CLB-016](lessons/CLB-016_Correct_or_Retire_a_Campaign_Without_Losing_the_Truth.md) | Correct or retire review work while preserving its history |
| [CLB-017](lessons/CLB-017_Complete_and_Defend_an_Independent_Certification_Project.md) | Complete the independent project |

The job-dependent routes below are optional. Choose one when its task applies. Reported feature access alone does not establish the source data, permissions or API behavior it needs.

| ID | Route | When to use it |
|---|---|---|
| [CLS-001](lessons/CLS-001_Review_Uncorrelated_Account_Access_and_Track_Ownership.md) | Uncorrelated accounts | You need to review an account without a confirmed link to a person. |
| [CLS-002](lessons/CLS-002_Review_Service_Account_Access_and_Preserve_the_Service.md) | Service accounts | You need to establish native machine classification and review the program's access. |
| [CLS-003](lessons/CLS-003_Review_a_Roles_Contents_and_Verify_the_Correction.md) | Role composition | You need to review and correct a role's design. |
| [CLS-004](lessons/CLS-004_Use_Activity_and_Recommendations_to_Support_a_Review.md) | Activity and recommendations | You need to interpret decision-support information and its limits. |
| [CLS-005](lessons/CLS-005_Investigate_a_Certification_Through_Read_Only_APIs.md) | Read-only API investigation | You need to reconcile an actual next-generation campaign through supported API reads. |
| [CLS-006](lessons/CLS-006_Automate_a_Bounded_Read_Only_Evidence_Collection.md) | Bounded read-only automation | You have verified the manual API case and need to collect it again. |

## Current status

All 23 planned learner guides are authored and individually author-reviewed: 17 main and 6 specialist. A [course-wide author audit](author/COURSE_WIDE_AUTHOR_AUDIT_2026-11-15.md) checked the route, repeated material, entry/reset instructions and local consistency, and records its reading coverage and corrections.

The fresh beginner-readability pass covers all23 complete learner guides and the supporting capstone assessor guide. The [revised-course review](author/REVISED_COURSE_AUDIT_2026-11-16.md) reconciles shared data, reset instructions, repeated material and local package contents. All23 units are retained. Actual learner testing remains separate.

Tenant execution, repeated tenant runs and independent learner tests remain 0. The read-only collector has 25 passing offline test methods; those do not establish a working tenant connection.

The tenant is temporarily unavailable during maintenance, as reported by the user on November 15. Local lesson review can continue. The setup and first review above will be tested when access returns.

This course is local. An author-review archive includes the worked assessor guide and author history; it is not a learner assessment release. Private tenant data and captures are excluded. No hands-on repository or Pages site has been created. The published theory course is separate and unchanged.

## Preparation and author records

- [Design and practical coverage](COURSE_DESIGN.md)
- [Teaching standards](TEACHING_SPECIFICATION.md)
- [Current status and next work](COURSE_REGISTER.md)
- [Environment readiness](LAB_ENVIRONMENT.md)
- [CSV and connected-system boundaries](CSV_LAB_STRATEGY.md)
- [Initial baseline specification](lab-data/BASELINE_SPECIFICATION.md)
- Fixtures: [A, people and manager review](lab-data/baselineA/README.md); [B, source-owner review](lab-data/baselineB/README.md); [C, planned AD](lab-data/baselineC/README.md); [D, unmatched account](lab-data/baselineD/README.md); [E, service account](lab-data/baselineE/README.md); [F, role design](lab-data/baselineF/README.md).
- [Sources and unresolved behavior](author/SOURCE_AND_BEHAVIOR_REGISTER.md)
- [Authoring history](author/AUTHORING_PLAN.md)

Writing, author review, ISC execution, repetition, learner testing and publication are separate recorded states.
