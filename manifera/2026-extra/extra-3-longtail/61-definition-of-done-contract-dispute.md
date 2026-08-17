---
title: "The Two Words Missing From Most Software Contracts That Cause Every Later Dispute"
keywords: "custom software development, software development company, custom software development services, software product"
buyer_stage: "Consideration"
target_persona: "A"
---

# The Two Words Missing From Most Software Contracts That Cause Every Later Dispute

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Two Words Missing From Most Software Contracts That Cause Every Later Dispute",
  "description": "Why 'definition of done' is the single most consequential phrase missing from most custom software development contracts, and what including it actually requires.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/definition-of-done-contract-dispute" }
}
</script>

A CTO reviewing a vendor contract checks the price, the timeline, the IP assignment clause, and the termination terms. What most contracts never actually define is the two words that determine whether any of those other terms can be enforced at all: "done" and, more specifically, what evidence proves it.

## Why "Complete" Is Doing an Enormous Amount of Undefined Work

Almost every software contract promises delivery of a "complete" or "fully functional" product without specifying what complete actually means in checkable terms — does it mean the code compiles, that it passes an agreed test suite, that a specific list of acceptance criteria is verifiably met, or simply that the vendor believes the work is finished? Each of these is a legitimate standard. The problem isn't that any one of them is wrong — it's that a contract silent on which one applies leaves both parties free to assume the interpretation that favors them, and that gap surfaces at exactly the worst moment: the final milestone payment, when a client believes work is incomplete and a vendor believes it has delivered exactly what was promised.

## Why This Gap Is Structural, Not Accidental

Economist Oliver Hart, whose work on incomplete contract theory earned him a share of the 2016 Nobel Memorial Prize in Economic Sciences, formalized a finding that's directly relevant here: real-world contracts are necessarily incomplete, because it's prohibitively costly, and often genuinely impossible, to specify contractual obligations for every state of the world that might arise. Hart's theory doesn't treat this incompleteness as a drafting failure to be shamed away — it treats it as an economic fact about contracting under uncertainty, and asks instead who should hold decision rights over the gaps a contract inevitably leaves open.

Applied to software development, "definition of done" is precisely the kind of gap Hart's framework describes: no contract, however carefully drafted, can enumerate every possible interpretation of "complete" for a system that doesn't exist yet at signing time. What Hart's theory does offer is a practical prescription — since some incompleteness is unavoidable, the contract should explicitly assign who has the residual right to decide the ambiguous cases, rather than leaving that right implicitly contested. A software contract that names a specific, checkable acceptance process (a defined test suite, a formal client sign-off step, a named arbiter for disputed cases) has assigned that residual right deliberately. A contract that simply says "complete" has left it to be fought over later, precisely when both sides have the least incentive to compromise.

## What a Working "Definition of Done" Actually Specifies

- **A concrete, testable acceptance criteria list** tied to each major deliverable, written in language specific enough that a third party could verify it without asking either side what they meant.
- **An explicit test suite or QA checklist** the deliverable must pass, agreed before development begins rather than negotiated after a dispute has already started.
- **A formal sign-off mechanism**, naming who on the client side has authority to accept a milestone and how long they have to raise objections before acceptance is assumed.
- **A process for handling disputed interpretations**, whether that's a named technical arbiter, an escalation path, or a pre-agreed standard both sides can point back to.

## Why Vague Contracts Favor Whoever Has More Leverage Later, Not Whoever Is Right

An ambiguous "definition of done" doesn't stay neutral once a dispute actually starts — it tends to resolve in favor of whichever party has more leverage at that specific moment, which is rarely the party with the stronger underlying case. A vendor holding source code and institutional knowledge of an undocumented system has real leverage over a client who needs the product live regardless of the dispute's merits. A client withholding a final payment has real leverage over a vendor who has already staffed and delivered most of the work. Neither leverage position reflects who was actually right about what "complete" meant — it reflects who blinks first, which is exactly the outcome a clear, pre-agreed definition of done is designed to prevent.

## What "Residual Control Rights" Look Like in Practice

Hart's broader theory identifies a second, related mechanism worth understanding directly: when a contract can't specify every contingency, whoever holds the residual control rights over an asset effectively gets to decide the unspecified cases as they arise, and that party's incentives shape how the relationship actually plays out under ambiguity. In software development, the "asset" in question is the interpretation of what counts as finished — and by default, without an explicit assignment, both parties implicitly believe they hold that residual right, which is precisely why disputes escalate rather than resolve quickly when ambiguity surfaces.

A specific, testable definition of done doesn't eliminate incompleteness — Hart's theory says that's not actually achievable — but it does something almost as valuable: it assigns the residual right to an agreed, checkable standard rather than to whichever party can argue more persuasively or hold out longer once a disagreement starts. This is the practical translation of a fairly abstract piece of contract theory into something a CTO can act on directly during vendor scoping, and it's exactly why the specific mechanics matter more than simply agreeing, in principle, that the software should be "good" or "complete" before work begins.

## Manifera's Approach: Naming the Residual Rights Before the Work Begins

- **Amsterdam (Governance/Contract Clarity):** Dutch project leads write specific, testable acceptance criteria and a named sign-off process into every statement of work before development starts, treating this as core scoping work rather than legal boilerplate to be finalized later.
- **Vietnam (Execution/Verifiable Delivery):** The engineering pod builds against the same acceptance criteria the client agreed to, with QA validation tied directly to those criteria rather than an internal, unverifiable standard of "looks finished to us."

This is Dutch Management × Vietnamese Mastery applied to contractual clarity itself: governance that resolves ambiguity before it can become a dispute, paired with execution that's verifiably measured against what was actually agreed. Explore Manifera's [custom software development](https://www.manifera.com/services/custom-software-development/) engagement process.

## Case Study: An Oslo Manufacturer's Costly Ambiguity

Fjordvekst Industrial, an Oslo-based manufacturing software buyer, had signed a fixed-price contract with a previous vendor that promised a "fully functional inventory management system" with no further specification. At the final milestone, the vendor considered the system complete; Fjordvekst's operations team considered several workflows non-functional in practice, though technically present. Neither side had a shared, pre-agreed standard to point to, and the resulting dispute delayed final payment and system rollout by nine weeks while both sides argued past each other.

For the replacement engagement, Manifera's Amsterdam team wrote a specific, line-item acceptance criteria list into the statement of work, tied to a defined test suite the client's operations team helped shape during discovery. The final milestone sign-off took one afternoon, not nine weeks, because both sides had already agreed, in writing, what "done" would look like.

> *"We'd argued for two months about whether the software was finished. The actual argument should have been a fifteen-minute conversation before we signed anything, about what 'finished' meant in the first place."*
> — **Head of Operations, Fjordvekst Industrial**

Fjordvekst's procurement team now requires a specific, testable definition-of-done section in every vendor contract above a defined value, treating its absence as a red flag worth raising before signing rather than a detail to sort out later.

## Reading a Vendor's Reaction to This Request as Its Own Signal

A useful secondary benefit of asking a prospective vendor to help define testable acceptance criteria during discovery: how they respond is itself informative, independent of the criteria eventually agreed. A vendor genuinely confident in their delivery process typically welcomes the exercise, since it protects them as much as the client — a specific, agreed standard is also a vendor's best defense against a client moving the goalposts after signing. A vendor who resists specificity, preferring to keep "complete" vague, is revealing something about how they intend to handle disputes later, well before any dispute has actually happened.

## What a Vague vs. Specific Definition of Done Produces

| Element | Vague Contract | Specific Contract |
|---|---|---|
| "Complete" defined as | Left to interpretation | Testable, line-item criteria |
| Acceptance process | Implicit, informal | Named sign-off authority and timeline |
| Dispute resolution | Ad hoc, leverage-driven | Pre-agreed arbiter or standard |
| Final milestone risk | High, favors whoever has leverage | Low, resolved against agreed criteria |

## Writing a Real Definition of Done Into Your Next Contract

Before signing a custom software development contract, insist on a specific, testable definition of done for every major milestone, not just a general promise of "complete" or "fully functional." [Talk to one of our senior architects](https://www.manifera.com/contact-us/) about scoping acceptance criteria before your next project starts.

## Frequently Asked Questions

### (Scenario: CTO reviewing a vendor contract before signing) What should a proper "definition of done" clause actually include?

Specific, testable acceptance criteria for each major deliverable, an agreed test suite or QA checklist, a named sign-off authority with a clear timeline, and a defined process for resolving disputed interpretations.

### (Scenario: founder in an active dispute over whether work is complete) What should I do if my vendor and I disagree about whether a milestone is actually done?

Check whether your contract defines specific acceptance criteria — if it doesn't, that ambiguity is the actual root problem, and future contracts should close it explicitly rather than relying on general language.

### (Scenario: CTO worried acceptance criteria will slow down contracting) Does writing detailed acceptance criteria into a contract add significant time to the scoping process?

Some, but meaningfully less time than a later dispute costs — defining testable criteria during discovery is a front-loaded cost that avoids a much larger, less predictable cost during a final-milestone disagreement.

### (Scenario: founder unsure who should have authority over disputed interpretations) Who should have the final say when a definition-of-done dispute can't be resolved by discussion alone?

Naming this explicitly in the contract, whether a specific client stakeholder, a named third-party technical arbiter, or a pre-agreed standard, matters more than which specific option is chosen — the absence of a named authority is the real risk.

### (Scenario: CTO trying to apply this to an ongoing dedicated-team engagement) Does definition of done matter for an ongoing dedicated team relationship, not just a fixed-scope project?

Yes — even ongoing engagements benefit from sprint-level or feature-level acceptance criteria, since the same ambiguity that causes disputes at a final milestone can recur at every sprint boundary without a shared standard.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO reviewing a vendor contract before signing) What should a proper 'definition of done' clause actually include?", "acceptedAnswer": { "@type": "Answer", "text": "Specific, testable acceptance criteria, an agreed test suite, a named sign-off authority with a timeline, and a defined dispute resolution process." } },
    { "@type": "Question", "name": "(Scenario: founder in an active dispute over whether work is complete) What should I do if my vendor and I disagree about whether a milestone is actually done?", "acceptedAnswer": { "@type": "Answer", "text": "Check whether your contract defines specific acceptance criteria — if not, that ambiguity is the root problem for future contracts to close." } },
    { "@type": "Question", "name": "(Scenario: CTO worried acceptance criteria will slow down contracting) Does writing detailed acceptance criteria into a contract add significant time to the scoping process?", "acceptedAnswer": { "@type": "Answer", "text": "Some, but meaningfully less than a later dispute costs — it's a front-loaded cost avoiding a larger, less predictable one." } },
    { "@type": "Question", "name": "(Scenario: founder unsure who should have authority over disputed interpretations) Who should have the final say when a definition-of-done dispute can't be resolved by discussion alone?", "acceptedAnswer": { "@type": "Answer", "text": "Naming this explicitly matters more than which specific option is chosen — the absence of a named authority is the real risk." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to apply this to an ongoing dedicated-team engagement) Does definition of done matter for an ongoing dedicated team relationship, not just a fixed-scope project?", "acceptedAnswer": { "@type": "Answer", "text": "Yes — sprint-level or feature-level acceptance criteria prevent the same ambiguity from recurring at every sprint boundary." } }
  ]
}
</script>
