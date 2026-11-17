---
Title: "Case Study: Achieving AI Decision Traceability for a Compliance-Heavy Fintech in 12 Days"
Keywords: AI decision traceability, explainability, fintech compliance, DORA, EU AI Act, audit trail, LaunchStudio, Manifera, Herre Roelevink, Cursor
Buyer Stage: Decision
---

# Case Study: Achieving AI Decision Traceability for a Compliance-Heavy Fintech in 12 Days

When an AI model helps decide whether someone gets approved for a loan, a credit line, or a payment plan, "the model said no" is not an answer any financial regulator will accept. Regulated fintechs are expected to explain, for any individual decision, exactly what factors drove it and be able to reconstruct that reasoning on demand - a requirement that most AI-builder-generated products were never designed to satisfy. This is the story of Elena Petrova, founder of a credit-risk scoring AI SaaS built with **Cursor**, and the 12-day sprint that turned an opaque model into a fully traceable one, just in time for a regulatory review.

## The Question That Stopped a Regulatory Conversation Cold

Elena's product, CreditLens AI, used a machine learning model to generate risk scores that fed into lending decisions for a network of partner credit providers. Her business was growing, and a national financial regulator scheduled a routine compliance review - standard practice for any fintech whose scoring model materially influences credit decisions. The reviewer's first substantive question was simple and devastating: for a specific denied application, could Elena's team reconstruct exactly which input factors drove the model's score, and demonstrate that the same factors would be evaluated consistently across similar applicants?

Elena's Cursor-built product could not answer that question. Her model produced a score, and the score fed into a decision, but there was no logging connecting a specific applicant's inputs to the specific reasoning that produced their score, no record of which model version had scored a given application, and no systematic way to demonstrate consistency across similar cases. The regulator gave her team a firm 12-business-day window to demonstrate traceability before the review would escalate to a formal compliance action.

## Why Traceability Is Different From "The Model Works"

**A working model and an explainable model are not the same thing.** Elena's model was genuinely accurate - its predictions correlated well with actual repayment outcomes. Accuracy is necessary but not sufficient for regulatory purposes; a regulator specifically needs to see the reasoning behind individual decisions, not just evidence that the model performs well in aggregate.

**Regulatory frameworks increasingly require this by name.** Frameworks like the EU AI Act's provisions for high-risk AI systems and financial regulation such as DORA increasingly require documented traceability and explainability for automated decisions that materially affect individuals - not as a best practice, but as a compliance requirement with real consequences for non-compliance. A model without decision-level traceability is not just a technical gap; it's a regulatory exposure.

**Model versioning matters as much as the decision logic itself.** Elena's model had been retrained and updated three times since launch, but her system had no record of which version scored which application. Without that, she couldn't even establish which model's reasoning to reconstruct for a given historical decision - the traceability problem started before the explainability problem could even be addressed.

**Consistency across similar cases is its own separate requirement.** Beyond explaining one decision, a regulator wants evidence that the model treats comparable applicants comparably - a fairness and consistency check that requires being able to query and compare decision reasoning across many cases at once, not just reconstruct one in isolation.

## The Distinction Elena's Team Learned the Hard Way: Explainability Is Not Optional Polish

Early in the sprint, one of Elena's own engineers suggested a shortcut: rather than building true feature-importance reporting per decision, could they simply write a generic disclaimer describing the model's overall methodology and present that to the regulator alongside the raw scores? The team tested this idea against what the regulator had actually asked for in the initial review meeting, and it fell apart immediately - the reviewer's specific question had been about one denied application, not the model in the abstract, and a generic methodology statement couldn't answer a question about a specific person's specific outcome. That distinction is easy to underestimate from the outside: it's tempting to treat explainability as a documentation exercise that can be satisfied with a well-written policy statement, when what regulators overseeing consequential automated decisions actually expect is the ability to answer "why did this specific person get this specific outcome" on demand, for any decision, at any time. Building the actual decision-level infrastructure rather than a description of it was the difference between a review that closed and one that would have escalated regardless of how polished the documentation looked.

## The Fix: A 12-Day Traceability Sprint

Elena brought her existing Cursor-built product to LaunchStudio with the regulatory deadline fixed and non-negotiable. Working under an expedited **Enterprise Hardening** engagement, the team built the traceability infrastructure CreditLens AI needed:

1. **Decision-level input and output logging.** Engineers implemented logging that captured every input factor considered for a given scoring decision, the model version that processed it, and the resulting score and decision outcome - creating a permanent, queryable record for every decision going forward, and reconstructed what was recoverable for historical decisions from existing data.

2. **Model versioning and lineage tracking.** The team built a versioning system tying every model deployment to a specific date range and set of training parameters, so any historical decision could be definitively linked to the exact model version that produced it.

3. **Feature-importance reporting per decision.** For each scoring decision, the system now generates a report showing which input factors most influenced that specific score, in a format a compliance officer or regulator could review without needing to interpret raw model internals.

4. **A consistency audit dashboard.** Engineers built an internal tool letting Elena's compliance team query decisions by applicant profile similarity, surfacing whether comparable applicants received comparable treatment - the specific fairness evidence the regulator's review was designed to test for.

5. **Documentation matching the regulator's expected format.** The team packaged the technical implementation into documentation structured the way financial regulators typically expect to receive it, so Elena's compliance team could present it directly rather than translating technical output into regulatory language under deadline pressure.

## What Elena's Compliance Team Learned About Presenting Technical Evidence

Building the traceability infrastructure turned out to be only half the challenge; presenting it in a way the regulator's reviewer could actually use was the other half. Elena's compliance team initially planned to hand over raw system exports - JSON logs and database dumps - assuming the technical accuracy would speak for itself. LaunchStudio's team pushed back on that plan, pointing out that a reviewer evaluating dozens of vendors doesn't have time to parse raw exports, and a document that requires the regulator to do their own data engineering to understand it reads as evasive rather than transparent, regardless of intent. The final package instead paired the underlying data with plain-language summaries and visual decision trails for each reviewed case - the same underlying evidence, but packaged for how a compliance reviewer actually works through a submission.

## The Result: A Review That Closed Instead of Escalating

Elena's team presented the completed traceability system on day 11, a day ahead of the regulator's 12-day deadline. The reviewer was able to select several historical and hypothetical decisions and receive a clear, documented account of the reasoning behind each one, along with consistency evidence across a sample of similar applicant profiles. The review closed without escalation to formal compliance action, and the regulator specifically noted the traceability infrastructure as a positive factor going into CreditLens AI's next scheduled review cycle.

## Why This Matters Beyond One Regulatory Deadline

Decision traceability isn't a one-time compliance checkbox - it's infrastructure that has to exist continuously, because the next regulatory question, customer dispute, or internal audit could focus on any decision made at any point going forward. Fintech founders building on AI-generated scoring or decisioning models should treat traceability as a foundational requirement from the start, not a scramble triggered by a regulator's first hard question - because by the time that question arrives, the clock on demonstrating an answer is already running.

## A Question Worth Asking Before a Regulator Does

Fintech founders building on AI-driven scoring can get an early read on their own exposure with one direct exercise: pick any single decision from the past month, at random, and try to reconstruct exactly why the model produced that specific outcome, using only what's currently logged. If that reconstruction takes more than a few minutes, or isn't possible at all, that's the same gap Elena's regulator found, discovered on the founder's own timeline instead of a compliance deadline's. Running that exercise quarterly, on a randomly selected decision each time, is a low-effort way to catch traceability gaps well before a regulator's first hard question forces the issue.

## What Is AI Decision Traceability?

AI decision traceability is the ability to reconstruct, for any single automated decision, which inputs were used, which model version processed them, what the model returned, which factors drove that result, and what final decision followed. It is narrower and more practical than general "explainability": a traceable system can answer "why did this specific applicant receive this specific outcome?" from stored records, without guessing.

For fintechs, the legal pressure comes from several directions at once. The EU AI Act lists AI systems used to evaluate the creditworthiness of natural persons or establish their credit score among its high-risk use cases, and high-risk systems must support automatic record-keeping of events through logging. GDPR Article 22 limits decisions based solely on automated processing that significantly affect people, and the Court of Justice of the EU's 2023 SCHUFA ruling confirmed that generating a credit score can itself fall under Article 22 when lenders rely on it heavily. Both point to the same technical need: a complete, queryable record of each decision.

## What Should an AI Decision Record Contain?

An AI decision record should contain enough information for someone outside the engineering team to replay and understand the decision months later. The fields CreditLens AI ended up storing are a useful baseline for any AI decision traceability project:

| Field | Why it matters | Example |
|---|---|---|
| Decision ID and timestamp | Links the record to the customer case | Unique ID, UTC time |
| Input snapshot | Shows exactly what the model saw at that moment | Applicant features as submitted, not as they are today |
| Model version | Identifies which model logic applies | Version tag tied to a training run and deployment date |
| Raw model output | Separates the model's result from business rules | Risk score before thresholds |
| Top contributing factors | Explains the individual result | Feature-importance values, for example SHAP values |
| Business rules applied | Shows how the score became a decision | Threshold, overrides, policy rules |
| Final outcome | Records what happened | Approved, declined, referred |
| Human involvement | Shows whether a person reviewed it | Reviewer ID and action, if any |

Storing the input snapshot is the field teams most often skip, and it is the one that makes reconstruction possible. Customer data changes over time, so reading today's values back from the main database does not tell you what the model saw at decision time.

## How to Build AI Decision Traceability, Step by Step

The fastest way to build AI decision traceability is to start logging complete records for new decisions first, then recover what you can for older ones. A practical order:

1. **Version every model deployment** and record the version with each prediction.
2. **Write an append-only decision log** with the fields above, protected against later edits.
3. **Generate per-decision factor reports** at scoring time, not on request months later.
4. **Set a retention period** that matches your regulatory and contractual obligations, and document it.
5. **Build a simple review view** so compliance staff can open any decision without engineering help.
6. **Test it with a random decision** each quarter, as described below.

## Common Traceability Mistakes in Fintech AI

The most common mistake is logging the score but not the inputs, which leaves a number with no story behind it. Other frequent gaps include overwriting model files on retraining instead of keeping old versions, mixing model output and business-rule overrides into one field, and storing traceability logs in a system with weaker access control than the main database, even though they contain the same personal data.

## Key Takeaways

- A financial regulator evaluating an AI-driven credit or risk decision expects individual-decision traceability, not just aggregate model accuracy - these are genuinely different requirements.

- Frameworks like the EU AI Act and DORA increasingly require documented explainability for automated decisions that materially affect individuals, with real compliance consequences for gaps.

- Model versioning is a prerequisite for traceability; without knowing which model version produced a given decision, reconstructing the reasoning behind it isn't possible.

- Consistency across similar applicant profiles is a distinct requirement from explaining any single decision, and it requires infrastructure that can query and compare decisions at scale.

- LaunchStudio built Elena's complete decision-level logging, model versioning, feature-importance reporting, and consistency audit tooling in 12 business days, closing a regulatory review that had been on track to escalate.

## Don't Wait for a Regulator's First Hard Question to Build Traceability

If your AI model influences credit, lending, or other decisions that materially affect real people, decision-level traceability isn't optional infrastructure - it's the evidence a compliance review will ask for first.

LaunchStudio is operated by **Manifera**, an international software engineering company founded in 2014 and led by Founder & Managing Director **Herre Roelevink**. As Roelevink puts it: *"We see a shift in software needs. The challenge is no longer turning good ideas into software. It's now about the architecture and security needed to bring those products to maturity. We have eleven years of experience in exactly that."* Combining "Dutch management with Vietnamese mastery," Manifera maintains headquarters in **Amsterdam, the Netherlands** (Herengracht 420), an Asia hub in **Singapore** (100 Tras Street), and a primary development center in **Ho Chi Minh City, Vietnam** (Pho Quang Street). Through LaunchStudio, senior engineering teams take your existing AI-built frontend and implement production-ready audit logging, compliance documentation, and monitoring - transforming your prototype into a defensible, compliant MVP in 1 to 3 weeks, without a rebuild. [Get a free quote today](https://launchstudio.eu/en/#contact) or see how Manifera's [custom software development team](https://www.manifera.com/services/custom-software-development/) approaches production-hardening for AI-generated codebases.

## Real example

### An AI-Native Founder in Action: An Insurance-Pricing Tool Facing an Audit Deadline

Matteo Ferrara used **Lovable** to build an AI-driven insurance-pricing SaaS, and a scheduled internal audit at a partner insurer asked for decision-level traceability on premium-pricing recommendations his platform generated - documentation his product had never been built to produce, with a two-week deadline before the audit's findings would be finalized.

Matteo partnered with **LaunchStudio (by Manifera)** to close the gap. The engineering team implemented decision-level input and output logging, model version tracking, and feature-importance reporting formatted for the insurer's audit requirements.

**Result:** Matteo's platform passed the partner insurer's audit with full traceability evidence for every reviewed pricing decision, preserving the partnership relationship without a formal remediation requirement.

**Cost & Timeline:** €5,200 (Enterprise Hardening Package) - 13 business days.

---

---

---
## Frequently Asked Questions

### What exactly does "AI decision traceability" mean in a compliance context?

It means being able to reconstruct, for any individual automated decision, which input factors were considered, which model version processed it, and what reasoning led to the outcome - documented in a form a regulator, auditor, or compliance officer can review without needing to interpret raw model internals themselves.

### Does having an accurate model satisfy regulatory requirements on its own?

No. Model accuracy and decision explainability are separate requirements. A regulator evaluating an AI-driven financial decision generally wants both evidence the model performs well in aggregate and the ability to explain and reconstruct the reasoning behind specific individual decisions.

### What frameworks specifically require this kind of traceability?

The EU AI Act's provisions for high-risk AI systems and financial regulations like DORA increasingly require documented explainability and traceability for automated decisions that materially affect individuals, particularly in credit, lending, and insurance contexts. Requirements vary by jurisdiction and use case, so specific applicability should be confirmed with compliance counsel.

### Can traceability be added retroactively, or does it only work going forward?

Both, to different degrees. Logging and versioning implemented going forward capture full detail for all new decisions immediately. For historical decisions, the amount of reconstructable detail depends on what data already existed - which is why building this infrastructure proactively, rather than after a regulator asks, produces much stronger evidence.

### How long does it typically take to implement decision traceability infrastructure?

For a typical AI-driven fintech scoring or decisioning system, implementing decision-level logging, model versioning, feature-importance reporting, and consistency audit tooling generally takes 1.5 to 3 weeks under an Enterprise Hardening engagement, depending on the complexity of the existing model and data pipeline.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What exactly does \"AI decision traceability\" mean in a compliance context?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It means being able to reconstruct, for any individual automated decision, which input factors were considered, which model version processed it, and what reasoning led to the outcome - documented in a form a regulator, auditor, or compliance officer can review without needing to interpret raw model internals themselves."
      }
    },
    {
      "@type": "Question",
      "name": "Does having an accurate model satisfy regulatory requirements on its own?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Model accuracy and decision explainability are separate requirements. A regulator evaluating an AI-driven financial decision generally wants both evidence the model performs well in aggregate and the ability to explain and reconstruct the reasoning behind specific individual decisions."
      }
    },
    {
      "@type": "Question",
      "name": "What frameworks specifically require this kind of traceability?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The EU AI Act's provisions for high-risk AI systems and financial regulations like DORA increasingly require documented explainability and traceability for automated decisions that materially affect individuals, particularly in credit, lending, and insurance contexts. Requirements vary by jurisdiction and use case, so specific applicability should be confirmed with compliance counsel."
      }
    },
    {
      "@type": "Question",
      "name": "Can traceability be added retroactively, or does it only work going forward?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Both, to different degrees. Logging and versioning implemented going forward capture full detail for all new decisions immediately. For historical decisions, the amount of reconstructable detail depends on what data already existed - which is why building this infrastructure proactively, rather than after a regulator asks, produces much stronger evidence."
      }
    },
    {
      "@type": "Question",
      "name": "How long does it typically take to implement decision traceability infrastructure?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For a typical AI-driven fintech scoring or decisioning system, implementing decision-level logging, model versioning, feature-importance reporting, and consistency audit tooling generally takes 1.5 to 3 weeks under an Enterprise Hardening engagement, depending on the complexity of the existing model and data pipeline."
      }
    }
  ]
}
</script>
