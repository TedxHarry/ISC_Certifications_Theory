# What if the reviewer cannot confidently decide?

A review item is called Stock Support. The person works in a warehouse, and the application shows recent activity.

Should the reviewer approve it?

We still need to know what Stock Support permits and whether this person's current work requires those capabilities. A familiar name and a recent login do not answer those questions.

Being unsure is a reason to identify the missing facts. It is different from confirming that access is unnecessary.

## Make the unanswered question specific

SailPoint Identity Security Cloud, or **ISC**, keeps an **identity** representing a person and associates their application accounts with it. An **account** is a record in a particular system. Its permissions determine what someone using it can do.

Here, identity 4601 owns account `wh-4601` in Warehouse Production. ISC manages collected account information through a **source**, its configuration representing that application or account-data collection.

The account holds entitlement `STK_HELPER`, displayed as Stock Support. An **entitlement** represents an access right from the source. Its readable label identifies the item for people, but it does not explain which application actions the permission allows.

A **certification campaign** organizes access reviews. A **certification** is an assigned review within it, and a **review item** is a unit on which the reviewer records a decision.

For this example, `STK_HELPER` is an individually reviewable entitlement outside a larger package or automatic assignment, with no other assignment supplying it. Current account information and the person/account association have been checked. The assigned review is active and unsigned, meaning its decisions have not been finalized. Its reviewer is permitted to act and is reviewing somebody else's access.

The description only says “Warehouse support.” The reviewer also knows that identity 4601 works with stock counts, but has not confirmed which actions that duty authorizes.

There are two separate gaps:

- What can someone using `STK_HELPER` actually do on `wh-4601`?
- Which of those actions does identity 4601's current authorized duty require?

“I don't understand this access” becomes much easier to resolve when it names the missing information.

## Ask the person who can establish that fact

Different people can help with different questions. An **access owner** is responsible for an access object. A **source owner** is responsible for the source recorded in ISC. A manager or responsible business owner can help establish the person's current duties and authorization. A campaign administrator can investigate the generated review, its assignment and permitted actions.

Those responsibilities are useful starting points. Check that the person you consult actually understands the question and can support the answer.

| What is unclear? | Useful question | Who can help establish it? |
|---|---|---|
| Permission capability | Does STK_HELPER only read stock, or can it change quantities? Which warehouse does it reach? | Someone responsible for the access who understands the current application configuration. |
| Current business need | Does this person's stock-count duty include correcting recorded quantities on this account? | The manager or responsible business owner who can confirm the current task and authorization. |
| Person or account association | Does this exact warehouse account belong to this identity, and is it the intended account under review? | The people responsible for source data and identity/account association. |
| Conflicting information | Which description or account observation is current, and what changed? | The relevant data or application owner, with the campaign administrator if the review content needs correction. |
| Review responsibility or action | Is the right reviewer assigned, and can the required handover or correction be performed in this state? | The campaign administrator or other actor authorized for that action. |

Include the exact source, identity, account and item when asking. State what the review currently shows and the fact you need confirmed. “Please confirm access” is less useful than “Does STK_HELPER permit quantity corrections in the assigned warehouse, and does this account's current duty authorize them?”

Keep the answer and its evidence connected to the review. A current application configuration, an accountable duty confirmation or a specific business record can support the answer. A vague assurance such as “everybody has it” still leaves the capability and individual need unclear.

## Consultation supplies facts; it does not transfer the review

**Consultation** means asking someone for information to help establish the decision. The reviewer can consult an application owner about capability and a business owner about need while remaining responsible for the assigned review.

Sending the question or adding a comment does not establish that either person has become the assigned reviewer. Inspect the assignment if responsibility is intended to change.

For `STK_HELPER`, the application owner now confirms that the permission allows reading stock records and correcting recorded quantities for the warehouse assigned to `wh-4601`. That warehouse restriction has been checked in the application; it is not inferred from the account name.

The business owner confirms that identity 4601's current stock-count duty includes comparing physical stock with recorded quantities and correcting authorized differences. Both capabilities are required on this account. The relevant confirmation is retained in business record C-91.

The reviewer can now connect the facts: the account can read and correct quantities in the relevant warehouse, and the current authorized duty requires those actions there. Under those supplied facts, keeping the reviewed entitlement has a reason the reviewer can explain.

**Approve** accepts continued access to the reviewed item. **Revoke** records that the reviewed access should be removed. Either choice needs a reason grounded in the actual access and current circumstances. The clarification has supplied the facts for judgment; it has not automatically made the choice or changed the account.

## Check the answer against the whole capability

Now change the business confirmation. The person only counts stock and reports differences. Someone else is authorized to correct the application's quantities.

The same entitlement still permits both reading and correcting quantities. A statement that “stock access is required” would justify too little of what the permission provides.

Establish whether a narrower authorized access arrangement can provide the needed reading without quantity correction. Involve the responsible access owner and the authorized people making the change. Correcting the display name to Stock Reader would not remove the ability to change quantities.

If the new information conflicts with an old description, establish what each record describes and when it was confirmed. The newest message is not automatically the most reliable explanation; the person answering needs knowledge and evidence for that particular fact.

Also check whether the answer covers the actual review item. An **access profile** bundles entitlements from one source. A **role** can include profiles and direct entitlements across sources. A justification for one component does not establish that an entire reviewed package is appropriate.

## When another person should take over

Sometimes the missing information can be supplied to the existing reviewer. Sometimes another person is better suited to assess the review itself.

**Reassignment** changes recorded responsibility for selected review work through a supported action. It is different from consultation. Before arranging it, establish why the proposed recipient can assess the actual access, whether they are available and whether they have the necessary permission.

The selected work matters. Handing over a whole certification can move more people's access than the one item that raised the question. Use a supported action with the intended scope and inspect the result, including any remaining work with the original reviewer.

For the documented administrative certification handover, the campaign must be in preview or started and the selected certification must still be unsigned. Preview means review work has been generated for checking before launch. That handover does not provide a general way to reopen a signed-off review.

Own-access protection matters too. A manual certification reassignment is blocked if the selected certification contains access belonging to the proposed new reviewer. Knowledge of the application does not authorize someone to review their own access. Do not assume the manual action will automatically split out that work.

After a permitted handover, inspect who holds the intended work now and confirm that the recipient can open and continue it. Keep the reason, relevant questions and evidence available. A request being submitted or a message being sent is not the same observation as changed responsibility.

The flow below connects the question to the next useful action. The decision still rests on verified facts and the organization's criteria.

```text
Review item is unclear
  Identify exact account, access and missing fact
                       |
                       v
Ask someone with the relevant knowledge
  Capability, current need, data or review-state question
                       |
                       v
Compare the answer with the actual reviewed item

Facts now establish the justified decision
  -> record the choice, reason and useful evidence

Another person should assess the review
  -> check recipient, scope, state and permission
  -> use a supported handover and verify responsibility

Material facts are still missing or conflicting
  -> raise the gap with the person running the campaign
  -> agree the next action and follow up before the deadline

Clarification is not sign-off or verified access removal.
```

## Use recommendations and activity to ask better questions

A **certification recommendation**, where available, supplies decision-support information. Its reasons can include comparison with **peer groups**, identities grouped for analysis of similar access patterns. A suggestion to retain access because peers hold it can help locate a possible explanation.

It does not establish what this person is currently authorized to do. Open the reasons and compare them with the actual task and capabilities. Uncommon access can also have a justified specialist purpose.

An **access flag** draws attention to a particular fact. New Access, for example, means the access has not been certified before. It does not prove the access was recently granted or that it should be removed. A privilege indicator points to access requiring closer inspection; it does not supply the business justification.

Available **source activity** describes events gathered from the application. A login establishes application use within the measured context. It does not establish use of every entitlement, or authorization to keep using those permissions.

Check the activity's source, coverage and time period. With the relevant Activity Insights service and source configuration, certification context can show active days over a 90-day period. An unavailable panel is different from a measured zero. Even a measured zero needs to be considered alongside duties such as an authorized annual recovery task.

These forms of context depend on supported services, configuration and review type. A missing recommendation or activity panel is not a reason to invent a default access decision. Ask what fact the available information actually establishes and what remains unknown.

## If the question is still unresolved

State the gap precisely to the person responsible for the campaign. Include the exact item and account, what has been checked, whose confirmation is still needed and when the review is due. Agree who will obtain the information or arrange an appropriate permitted handover, then follow up.

Check the actual deadline and work state. Asking a question does not establish that the deadline was extended or the campaign paused. A comment such as “waiting for owner” records an issue; it does not establish a future access outcome.

An item with no recorded choice is **undecided**. An assigned review with saved choices but no final confirmation is **unsigned**. **Sign-off**, also called finalization, confirms the assigned review's decisions through its supported process. Saving a question or getting an answer does not establish sign-off.

**Acknowledge** is the review action for a role assigned through automated membership criteria, the conditions controlling who receives that role. It is not a general “unsure” response and does not remove access or override those conditions.

Follow the organization's established process for unresolved work. If a specific access concern needs urgent attention, raise it through the appropriate operational process as well; do not assume the certification question has already restricted the account.

When clarification establishes the decision, record the reason and useful evidence on the correct item. A saved Revoke is still a removal decision. The applicable finalization, removal work and actual account outcome remain separate checks.

## Work through a recommendation that does not answer the question

Identity 4701 owns account `case-4701` in Support Production. Its requested Case Review access profile contains two entitlements:

- **Read Cases** allows reading the cases assigned to the person.
- **Case Bulk Export** allows downloading all customer case records and contact details.

The contents, current account information and identity association have been confirmed. No other or automatic assignment supplies these rights. The certification is active and unsigned, and its independent reviewer is authorized to act.

The responsible business owner has confirmed that the person must handle assigned cases, so reading is required. The owner has not confirmed whether all-case export is authorized or needed. A recommendation suggests retaining the profile, and source activity shows recent application logins.

Can those two signals complete the justification for approving the profile?

They do not answer the missing export question. Application use does not establish use of all-case export, and the recommendation is guidance rather than authorization. The reviewer has a justified reading requirement and a material gap about the broader package. The gap is not itself proof that export is needed or proof that it is unnecessary.

Ask the responsible business owner to confirm the export requirement and authorized data scope, with the access owner clarifying any capability question. Then assess the whole selected profile. Do not describe it as read-only or approve it solely because one component is justified.

Now the business owner confirms that this person's duty does not authorize all-case export. The missing evidence has been supplied: export authorization is absent. Establish the appropriate decision and a separately authorized narrower arrangement preserving assigned-case reading. A description edit or a comment alone will not remove export, and the certification will not automatically grant a replacement profile.

Finally, suppose the proposed replacement reviewer is knowledgeable but their own access is also included in the selected certification. Can the manual handover simply put the problem with that person?

The documented manual own-access restriction prevents that move. Check the selected work and find a supported independent recipient and action, preserving the access that still needs review. Do not drop an item to make the work appear complete or assume the manual handover will separate the person's own access automatically.

The useful outcome is an explainable decision or a verified handover based on the correct facts. It starts by naming what is missing and ends by checking what the clarification or action actually established.
