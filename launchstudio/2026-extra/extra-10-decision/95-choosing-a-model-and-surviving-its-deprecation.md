---
Title: "Choosing a Model and Surviving Its Deprecation"
Keywords: llm model deprecation, pinning model version production, switching ai provider, abstraction layer llm, model migration testing, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Choosing a Model and Surviving Its Deprecation

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Choosing a Model and Surviving Its Deprecation",
  "description": "Models are retired on the provider's schedule, not yours, and the replacement behaves differently even when it is better. How to choose one, why pinning a version matters, and how to migrate without discovering the differences through customer complaints.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-05-23",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/choosing-a-model-and-surviving-its-deprecation" }
}
</script>

A dependency you cannot control on a schedule you do not set is an unusual thing to build a feature on, and that is what a hosted language model is. The version you developed against will be retired, with a notice period measured in months, and the replacement — even when it is genuinely better — will not produce the same output for the same input. Instructions tuned to one model's habits behave differently on the next.

This is manageable and it is not automatic. The founders who handle it well made three decisions early: which model, pinned how, and behind what boundary.

## Choosing: Capability Is Rarely the Constraint

The reflex is to pick the most capable model available. For most product features that is the wrong optimisation, because capability is rarely what limits the feature's usefulness.

Four criteria matter more in practice.

**Is it good enough for this specific task?** Classification, extraction, short rewrites, and routing are handled well by smaller, faster, cheaper models. Test the small one first; if it succeeds, the difference in cost and latency is substantial and permanent.

**Latency.** A model taking eight seconds for something a customer waits on is a worse product than one taking two, regardless of a marginal quality difference.

**Where it runs, and under what terms.** For European products handling customer data this can be decisive: whether processing occurs in the EU, whether the provider offers a data processing agreement, and whether inputs are used for training. These are procurement questions your business customers will ask.

**Whether more than one provider can do it.** A capability unique to one provider is a lock-in decision; a task any competent model performs leaves you options.

A pattern worth adopting: different models for different tasks. A small model for extraction and classification, a larger one for the tasks that genuinely need it. This is usually cheaper and faster overall than routing everything to the biggest available option.

## Pin the Version, Always

Providers offer aliases that point at the current version of a model. Using one means your product's behaviour changes when they update it — silently, without a deployment on your side, potentially on a Tuesday afternoon.

Always specify an explicit, dated version. Then you upgrade deliberately, after testing, rather than discovering the change through a customer noticing that summaries have become longer or a classifier has started using a category it never used before.

The corollary is that you must watch deprecation notices, because a pinned version will eventually be retired. Providers announce these by email and in changelogs, and the notice period is typically several months. Put the retirement dates for every model you use on the same list as your certificate expiries, and treat them the same way.

Two related habits. **Record which model version produced each output**, so that after a migration you can compare. And **know your fallback**: if your primary model is unavailable for an afternoon, does the feature fail cleanly, degrade to a smaller model, or take the product down with it?

## An Abstraction Thin Enough to Be Useful

Between calling a provider's library directly throughout your code and building an elaborate multi-provider framework, there is a modest middle that is worth the hour it takes.

One place in your code that calls models, taking a task, an input, and returning a validated result. Inside it: which model to use per task, the retry policy, the validation, the logging, the cost accounting. Everything else in your product calls that.

The benefit is not theoretical portability. It is that changing a model means changing one line, that you can run two models in parallel to compare, that cost tracking exists in one place rather than nowhere, and that a provider outage is handled once.

What to avoid is over-engineering it into a framework that supports every provider's every feature. Provider capabilities differ enough that a fully general abstraction ends up exposing the lowest common denominator, and structured output, caching, and tool use are exactly the features you would lose.

Establishing this boundary, pinning versions, and building the comparison capability that makes migration safe is a small piece of production engineering that repays itself at the first deprecation notice. LaunchStudio, backed by Manifera's 11+ years of production engineering, structures AI features so that changing models is a planned change rather than an emergency. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Migrating Without Discovering Differences From Customers

When the deprecation notice arrives, or when a better model appears, the migration has a sequence.

**Assemble a comparison set** — 30 to 50 real inputs covering the ordinary cases and the awkward ones. If you have been storing inputs and outputs with provenance, this already exists.

**Run both models over it** and compare. You are looking less for "better" than for *different*: outputs that changed category, became substantially longer or shorter, stopped following the format, or lost a detail the old one caught.

**Adjust the instructions** to the new model, because prompts are tuned to a model's habits and rarely transfer perfectly. This is usually the bulk of the work.

**Roll out behind a flag**, to yourself, then a small share, watching the correction rate — which is why tracking customer edits pays off here specifically.

**Keep the old version available** until the provider actually retires it, so a problem discovered late has a way back.

The mistake to avoid is treating a newer, more capable model as a drop-in improvement. Better on benchmarks does not mean identical on your task, and the differences show up in the specifics: a summariser that becomes more verbose, a classifier that starts distinguishing cases you wanted grouped, an extractor that now returns nulls where it used to guess.

## Real example

### The Retirement Notice That Arrived Three Weeks Late

Mert Yıldız ran Aanvraagfilter, a tool triaging incoming grant applications for regional funds, built in Cursor. It classified applications into six categories using a model referenced by an alias rather than a pinned version.

Two things happened in the same month. The provider updated the alias to a newer version, and Mert did not know, because nothing on his side changed. Classification behaviour shifted: applications previously assigned to a general category began being split across two others, and one fund's triage workflow — built around the old distribution — started routing applications to the wrong reviewers.

It was noticed eleven days later by a reviewer receiving applications outside their remit. Because model versions had not been recorded with outputs, establishing when the behaviour changed required correlating classification patterns against the provider's release notes.

The deprecation notice for the original version had also arrived, to an email address he no longer monitored, three weeks earlier.

**Result:** the model pinned to an explicit version, a single call layer introduced with per-task model selection, model and prompt version recorded with every classification, a comparison set of 50 historical applications built for testing future migrations, deprecation dates added to the quarterly review list, and provider notices routed to a monitored address. The migration to the newer version was then done deliberately, with instruction adjustments, over four days.

> "The provider improved the model and my product started sending applications to the wrong people. I had not changed anything, which is exactly why it took eleven days to work out."
> — **Mert Yıldız, Founder, Aanvraagfilter**

**Cost & Timeline:** model abstraction, version pinning, and migration process delivered in 3 business days.

## Frequently Asked Questions

### Should I use the most capable model available?

Usually not for every task. Smaller models handle classification, extraction, and short rewrites well at much lower cost and latency. Test the small one first and reserve the large model for tasks that genuinely need it.

### Why pin a model version instead of using the provider's alias?

Because an alias points at whatever is current, so your product's behaviour can change without any deployment on your side. Pinning makes upgrades deliberate and testable.

### How much notice do providers give before retiring a model?

Typically several months, announced by email and in changelogs. Retirement dates belong on the same review list as certificate and domain expiries, and notices should go to a monitored address.

### Do I need an abstraction layer over the provider's library?

A thin one is worth it: a single place that selects the model, retries, validates, logs, and tracks cost. A fully general multi-provider framework usually costs more than it returns and hides the features you want.

### How do I migrate to a new model safely?

Build a comparison set of real inputs, run both models over it and look for differences rather than improvements, adjust the instructions, roll out behind a flag while watching correction rates, and keep the old version available until it is retired.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Should I use the most capable model available?", "acceptedAnswer": { "@type": "Answer", "text": "Usually not for every task. Smaller models handle classification, extraction, and short rewrites at much lower cost and latency; reserve the large model for tasks that need it." } },
    { "@type": "Question", "name": "Why pin a model version instead of using the provider's alias?", "acceptedAnswer": { "@type": "Answer", "text": "An alias points at whatever is current, so behaviour can change with no deployment on your side. Pinning makes upgrades deliberate and testable." } },
    { "@type": "Question", "name": "How much notice do providers give before retiring a model?", "acceptedAnswer": { "@type": "Answer", "text": "Typically several months by email and changelog. Retirement dates belong on the same review list as certificate expiries, with notices going to a monitored address." } },
    { "@type": "Question", "name": "Do I need an abstraction layer over the provider's library?", "acceptedAnswer": { "@type": "Answer", "text": "A thin one: a single place selecting the model, retrying, validating, logging, and tracking cost. A fully general framework usually hides the features you want." } },
    { "@type": "Question", "name": "How do I migrate to a new model safely?", "acceptedAnswer": { "@type": "Answer", "text": "Build a comparison set of real inputs, look for differences rather than improvements, adjust instructions, roll out behind a flag watching correction rates, and keep the old version until retirement." } }
  ]
}
</script>
