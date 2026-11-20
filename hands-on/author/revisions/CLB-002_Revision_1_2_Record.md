# CLB-002 revision1.2: see the two matching relationships

November20,2026. The user approved continuing the recommended single illustration pilot. Scope: one diagram beside Follow one employee through the complete setup, a short connected explanation and the necessary portable assets/download. Existing source setup, mappings, manager prerequisites, fixtures, operating instructions and reset remain intact. This revises a lesson; it does not add a topic.

## Before drafting

The concrete teaching gap is recorded in the [targeted visual review](../../../author/VISUAL_TEACHING_OPPORTUNITIES_2026-11-20.md): the learner must remember multiple records across the setup procedure. Use the existing reporting account02 and employee02/manager01, not another scenario. Show two independent matches, with their actual attribute names, source roles and equal values. Do not draw a chronological link between the two panels or attach the reporting account directly to the manager.

The account criterion is report_accounts.csv employeeNumber certlab-employee02 to identity identificationNumber certlab-employee02. The manager criterion starts on employee02's people.csv record, where manager is certlab-manager01, and finds manager01's identity identificationNumber. Both configured mappings and the existing unique baseline identities remain required.

## Primary-source checks

Opened and read November20,2026:

- [Account correlation](https://documentation.sailpoint.com/saas/help/accounts/correlation.html): source account and identity attributes are paired and compared. This supports the first matching relationship, not proof of a live association.
- [Manager correlation](https://documentation.sailpoint.com/saas/help/sources/manager_correlation.html): the employee account's manager value is compared with the manager identity attribute. The guide explicitly uses manager and identificationNumber as an example and requires both identity-profile Manager Name mapping and source Manager Correlation configuration. This supports the second relationship and preserves the lesson's prerequisites.

The supplied people/account files were inspected before drawing. No tenant was accessed. Documentation checks establish the bounded mechanism; they do not establish that the user's current environment has been configured successfully. Source links stay in this author record.

## Saved revision and review

The diagram is placed after the five employee02 checks and before the explanation of the future manager review. Both account correlation and manager correlation, their settings and their source records are explained earlier in the lesson. The new paragraphs read each pair using its existing configured values. They make the different results explicit: employee02 holds the reporting account, while manager01 is employee02's manager. The separate source-owner setting remains unchanged later in the lesson.

The modified section and its surrounding explanation/table were reread from the saved file. Earlier mappings, the two correlation sections, the baseline inventory and later reviewer/reset instructions were checked for consistency. This is a bounded author review, not a new independent beginner test or a new complete course audit.

The [editable definition](../../assets/CLB-002_two_matches.canonical.json) has four records and two separately labelled edges. Its schema validates against canonical-v2.schema.json; static lint and a portable Mermaid source export succeed. The website picture is a locally built, script-free SVG, not output from a native Mermaid renderer. A [PNG preview](../../../author/previews/2026-11-20/CLB-002_two_matches.png) was rendered with PyMuPDF and visually inspected: all four names, fields, values, captions and arrowheads are readable and unclipped. No arrow connects the two matching pairs.

All22 site tests pass. The image test now verifies all three diagrams' node text, edge endpoints, labels, static markup and alternative text. Fixture checks verify that the new employee and manager keys still match the supplied people/account rows; they reject an account-to-manager shortcut. Local content verification passes24 lessons/3714 units/62 tables/27 answers/29 code blocks/three diagram assets. The two existing SVGs remain unchanged.

The rebuilt59-file kit includes the revised lesson and two new picture/definition files. CRC, exact packaged content and all26 relative Markdown/image references pass. Its SHA-256 is7bd27108553a082ee89439c8fe2c21380eb549c0b5032356f3ff20994082771b. The14 CSVs, 24 lesson IDs and existing URLs remain unchanged. No new topic, fixture, application connection or tenant execution is added.

## Observed publication

Content9864416c2d4855d1a3e42558358bcc91a02b6f0a was pushed to main. [Pages run44741935680](https://github.com/TedxHarry/ISC_Certifications_Theory/actions/runs/44741935680) completed build, report and deployment successfully on November20.

Complete live verification passes24 hands-on learners/3714 units/62 tables/27 closed answers/29 code blocks/three served diagrams/26 fetched reading pages. The new picture is an img element with the exact alternative text and resolved destination; all three served SVG contents match after Git's CRLF/LF normalization. The online59-file kit matches the exact local SHA-256. Author/control/assessor pages remain excluded. Separate theory verification passes61 learners/6819 units/61 diagrams and assets/63 tables/4020 link visits.

These observations establish publication and preserved content. They do not establish actual tenant matches or an independent beginner's understanding. The original authoring folder remains unchanged; this revision belongs to the published repository's learner copy.
