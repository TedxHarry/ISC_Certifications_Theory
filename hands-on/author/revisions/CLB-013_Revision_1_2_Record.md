# CLB-013 revision1.2: one shared holding, two relationships

November20,2026. The user requested continuation after the002 illustration. The next concrete gap is the retained-access relationship identified in the [visual review](../../../author/VISUAL_TEACHING_OPPORTUNITIES_2026-11-20.md). Scope: one picture and its explanation in the existing013 lesson. Keep its independent-profile/separate-role conditions, CSV and connected branches, task checks and reset.

## Before drafting and source check

The lesson's model is already explicit: the detected independent profile contains A Read+Export; the separately assigned employee02-only role requires direct A Read. The two objects refer to one Read holding on the same account. The profile is not inside the role; another source's matching Read name is not this holding. Do not imply that the newly configured role historically provisioned Read.

Reopened the official [access-profile guide](https://documentation.sailpoint.com/saas/help/access/access-profiles.html) on November20. Its Deprovisioning with Access Profiles section retains the bounded statement that role-required access remains when an overlapping independent profile is revoked. Its detection explanation supports the existing profile origin. This supports a conditional expected result for this configured case, not actual tenant execution.

The current [certification overview](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html) was also opened; it did not independently supply the detailed Acknowledge wording. No new claim about that action is introduced. Existing reviewer/criteria instructions retain their earlier sources and runtime checks. OQ-07 about two independent overlapping profiles remains unresolved and outside this diagram.

Show four nodes: profile, separate role, one Read holding and one Export holding. Three edges connect profile to both rights and role to Read only. Label the two relationships Contains and Requires. Put the actual source/account scope above the picture and make the result explicitly expected after review and completed removal work while the role still applies. Adjacent prose must explain the arrows rather than leave the drawing to carry the reasoning alone.

## Saved change and bounded review

The picture follows the existing definitions, two-object table, detection explanation, membership criterion and same-holding explanation. Its introduction explicitly identifies a relationship being prepared. The new paragraphs trace the two arrows into one Read holding, connect retention to the role's continuing requirement and leave actual assignment/task/account verification in the procedure.

The saved changed section, model definitions, scoped role condition, review instructions, predicted-result section and later same-account investigation were reread for consistency. Connected-source substitutions and reset remain unchanged. This is an author review of the changed explanation and its dependencies, not an independent learner test or an observed native result. No new general rule about independent overlapping profiles is introduced.

The [editable definition](../../assets/CLB-013_retained_read.canonical.json) validates against the canonical v2 schema. Static lint and portable Mermaid source export pass; a native Mermaid renderer was not used. The diagram builder creates the script-free SVG with three explicit arrowheads, one Read node and the expected-result condition. The [PNG preview](../../../author/previews/2026-11-20/CLB-013_retained_read.png) was rasterized with PyMuPDF and visually inspected for readable labels, unclipped text, distinct incoming arrows and the explicit expected/conditional footer. Existing three SVGs remain unchanged.

All22 site tests pass in a fresh run. They check one shared Read node with profile/role incoming edges, profile-only Export, detected origin, initial account02 Read+Export and the supplied Read-only result. They also preserve the footer's completion/role conditions. These are fixture and asset checks, not evidence that ISC processed this setup.

The rebuilt61-file kit contains the24 existing guides,14 unchanged CSVs and the new image/definition pair. CRC, every packaged byte and all27 relative Markdown/image references pass. SHA-256:dad8efb2ba752dd50272d70e69d5199f457d0eff1b8ac0e8db9c1c5049edd755. Local content verification passes24 learners/3717 units/62 tables/27 answers/29 code blocks/four SVGs. Publication remains a separate observed step.
