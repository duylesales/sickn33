---
Title: "What to Do When the Model Returns Nonsense"
Keywords: LLM output validation, structured output json schema, handling hallucinations product, ai fallback when model fails, retry model call, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# What to Do When the Model Returns Nonsense

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What to Do When the Model Returns Nonsense",
  "description": "A model that is right 95% of the time fails once in twenty, and a product that assumes success handles that failure by showing it to a customer. How to validate outputs, design the failure state, and decide which tasks are safe to automate at all.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-05-19",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/what-to-do-when-the-model-returns-nonsense" }
}
</script>

Every other component in your product either works or raises an error. A database query returns rows or fails. A payment succeeds or is declined. A language model has a third state that no other part of your system has: it returns something confident, well-formed, and wrong, with no indication that anything went awry.

That state is not an edge case to be engineered away. It is a property of the technology, and the practical question is not how to eliminate it but what your product does when it happens — which, in most prototypes, is to display it to the customer as though it were correct.

## Validate Everything the Model Returns

The single highest-return practice is to treat model output as untrusted input, exactly as you would treat something typed by a stranger.

**Ask for structured output and enforce the structure.** Most providers now support constrained or schema-based responses, which dramatically reduces malformed results — but the response must still be validated on your side, because "usually valid" is not a guarantee.

**Check values against reality.** If the model returns a category, confirm it is one of your categories. If it returns a customer identifier, confirm that customer exists and belongs to this account. If it returns a date, confirm it is plausible. If it returns a number, confirm it is in range. Each of these is a few lines and each catches a class of confident wrongness.

**Verify claims against the source where you can.** For extraction tasks — pulling a total from an invoice, a date from a contract — checking that the extracted value appears in the source text catches a large share of fabrications cheaply.

**Never let output flow directly into an action.** Model output that becomes a database write, an email, or a payment without validation is the arrangement that turns a wrong answer into a business consequence.

## Design the Failure State Deliberately

Validation tells you something is wrong. What happens next is a product decision, and the options are not equal.

**Retry once**, which is worth doing because model output varies between calls and a second attempt frequently succeeds. Retry once, not repeatedly: three attempts producing invalid output means the task is failing rather than the response.

**Fall back to a simpler approach.** A rule-based extraction, a smaller model, a default value, or the previous version of the answer — often less good and reliably available.

**Ask the customer.** "We could not read this document automatically — please enter the total" is an honest and perfectly acceptable outcome, and customers accept it readily when the alternative is a wrong number.

**Show nothing rather than something wrong.** For anything a customer will act on, an empty state saying the summary is unavailable is far better than a plausible fabrication.

What should not happen is silent degradation: displaying an empty summary, a zero, or a default that looks like a real answer. Customers cannot distinguish those from correct results, which is precisely the harm.

## Decide Which Tasks Tolerate Being Wrong

Before building, the useful question is what happens when this specific output is wrong one time in twenty.

**Tolerant tasks** — suggesting tags, drafting text a person will edit, proposing a category, summarising for orientation — have a natural human check, and a wrong answer costs a moment. These are good candidates for automation.

**Intolerant tasks** — extracting an amount that will be charged, deciding eligibility, classifying something with legal or medical weight, generating content published without review — have consequences that outlast the error. These need either verification against a source, a human confirmation step, or a decision not to automate at all.

The distinction is not about model capability; it is about consequence. A useful heuristic: if being wrong once in twenty would produce a support ticket, automate freely. If it would produce a refund, a complaint, or a legal question, put a person in the loop.

Confidence deserves a mention here, because it is frequently misunderstood. Asking a model how confident it is produces a number that does not correspond reliably to whether it is right; models express high confidence in fabrications. Checking output against a source is evidence. A self-reported score is not.

Building AI features that validate output, degrade honestly, and keep humans in the loop where consequences warrant it is a specific and well-understood discipline, and it is the most common gap in AI-generated products, where the model's response is typically displayed directly. LaunchStudio, backed by Manifera's 11+ years of production engineering, builds these paths properly before customers rely on them. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Make It Correctable, and Learn From the Corrections

Whatever the model produces, the customer should be able to change it — and that edit is the most valuable data your product generates.

Two requirements. **Every AI output is editable**, and editing it is easy rather than a matter of deleting and starting again. **Corrections are recorded**, so you can see which outputs get changed and how often.

The correction rate per feature is the closest thing to a quality measurement available without building an evaluation system: a summariser whose output is edited 8% of the time is working, one edited 60% of the time is producing drafts customers find easier to rewrite than to fix. And reading the corrections themselves shows you the failure pattern — consistently missing one section, always getting a particular field wrong — which is usually addressable with a change to the instructions rather than a different model.

It also matters for trust. A customer who can fix a wrong output moves on. A customer facing a wrong output they cannot change stops using the feature, and often stops trusting the rest of the product with it.

## Real example

### The Invoice Totals That Were Sometimes Invented

Kasper Lund ran Bonnetjesbox, an expense-processing tool for small businesses, built in Lovable. Photographed receipts were sent to a model that extracted the vendor, date, total, and VAT amount, which were then written straight into the customer's expense records.

Accuracy was good on clear photographs and unreliable on poor ones — creased receipts, faded thermal paper, or awkward angles. The model returned a plausible total regardless, and there was no validation and no indication of uncertainty. A customer's bookkeeper found a €340 expense for a receipt whose actual total was €34, and a review of three months of data found 47 entries where the extracted total did not appear anywhere in the receipt image.

Some had already been submitted in VAT returns.

**Result:** structured output with schema validation, the extracted total checked against the text found in the image and flagged when absent, one retry on invalid output followed by a fallback to manual entry with the image shown, a visible indication on any entry requiring review, and correction tracking. The correction rate — 14% initially — became the measure used to assess subsequent changes, and the 47 historical entries were flagged for the affected customers to re-check.

> "It never said 'I could not read this'. It always returned a number, and thirty of those numbers went into someone's tax return."
> — **Kasper Lund, Founder, Bonnetjesbox**

**Cost & Timeline:** output validation and fallback handling delivered in 3 business days.

## Frequently Asked Questions

### How do I know when a model's output is wrong?

By validating rather than trusting: enforce a schema, check values against your own data, and where the task is extraction, confirm the extracted value appears in the source. Self-reported confidence scores are not reliable evidence.

### Should a failed model call be retried?

Once. Output varies between calls, so a second attempt often succeeds, but three invalid responses indicate the task is failing rather than the response, and repeated retries multiply cost.

### What should a customer see when the model fails?

An honest statement that automatic processing did not work, with a manual path. Showing an empty result, a zero, or a plausible default is worse, because customers cannot tell it from a correct answer.

### Which tasks are unsafe to automate with a model?

Those where being wrong has consequences that outlast the error: amounts that will be charged, eligibility decisions, classifications with legal or medical weight, and content published without review. These need source verification or a human confirmation step.

### How do I measure whether an AI feature is good enough?

Track how often customers edit its output. The correction rate per feature is the most accessible quality signal, and reading the corrections shows the specific failure pattern.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "How do I know when a model's output is wrong?", "acceptedAnswer": { "@type": "Answer", "text": "By validating rather than trusting: enforce a schema, check values against your own data, and for extraction confirm the value appears in the source. Self-reported confidence is not reliable." } },
    { "@type": "Question", "name": "Should a failed model call be retried?", "acceptedAnswer": { "@type": "Answer", "text": "Once. Output varies between calls so a second attempt often succeeds, but three invalid responses indicate the task is failing, and repeated retries multiply cost." } },
    { "@type": "Question", "name": "What should a customer see when the model fails?", "acceptedAnswer": { "@type": "Answer", "text": "An honest statement that automatic processing did not work, with a manual path. An empty result or plausible default is worse because it is indistinguishable from a correct answer." } },
    { "@type": "Question", "name": "Which tasks are unsafe to automate with a model?", "acceptedAnswer": { "@type": "Answer", "text": "Those where being wrong outlasts the error: charged amounts, eligibility decisions, legally or medically weighted classifications, and unreviewed published content." } },
    { "@type": "Question", "name": "How do I measure whether an AI feature is good enough?", "acceptedAnswer": { "@type": "Answer", "text": "Track how often customers edit its output. The correction rate is the most accessible quality signal, and the corrections themselves reveal the failure pattern." } }
  ]
}
</script>
