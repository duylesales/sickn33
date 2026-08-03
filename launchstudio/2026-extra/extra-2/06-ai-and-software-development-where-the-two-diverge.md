---
Title: "AI and Software Development: Where the Two Actually Diverge"
Keywords: ai and software development, ai coding, ai secure, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI and Software Development: Where the Two Actually Diverge

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI and Software Development: Where the Two Actually Diverge",
  "description": "AI and software development are often treated as interchangeable terms. A specific technical deep-dive into where they diverge, focused on unencrypted personal data as a concrete example.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-07-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/ai-and-software-development-where-the-two-diverge"
  }
}
</script>

Everyone says AI can code your entire app. Nobody mentions that "AI" and "software development" are not, in fact, synonyms — one is a code-generation capability, the other is a discipline that includes decisions about data handling, compliance, and long-term maintainability that a generation tool has no particular reason to make correctly on its own, because nobody specifically asked it to.

## The Part AI Handles Extremely Well

Translating a described feature into working, reasonably structured code — a form that submits data, a dashboard that displays it, a workflow that moves a record from one state to another — is squarely within what modern AI coding tools do well, often faster and with fewer typos than a human writing the same code from scratch. This genuinely is software development, in the narrow sense of producing functioning code.

## The Part That Requires a Separate, Deliberate Decision

Software development, in the fuller sense, also includes decisions like: how is sensitive personal data stored, and is it encrypted at rest? What happens to that data if a user requests deletion? Is data retention aligned with what your privacy policy actually promises? These aren't code-generation questions — they're policy and architecture decisions that have to be made deliberately, and an AI tool responding to "build me a user profile page" has no way of knowing your specific answers to any of them unless you specifically provide them.

## Why Personal Data Storage Is Where This Divergence Shows Up Starkly

Storing a user's name and email in a plain database column is a completely reasonable, common pattern for non-sensitive data. Storing more sensitive personal information — health details, financial information, government identifiers — in the same undifferentiated way, without additional encryption or access restriction, is a materially different and riskier decision that an AI tool has no basis for flagging unless the prompt specifically called out that distinction.

## Why This Isn't Simply a "More Careful Prompting" Problem

It's tempting to think the fix is just prompting more precisely — "build this securely, encrypt sensitive fields." In practice, founders building fast with AI tools are managing dozens of simultaneous feature requests, and reliably remembering to specify data-handling requirements for every single field, in every single prompt, across an entire application, is a genuinely difficult standard to hold yourself to consistently, which is exactly why a separate review pass exists as a category of work in the first place. Consider what a single feature prompt like "add a field for emergency contact information" actually requires the founder to also specify in the same breath: that the field should be encrypted, that access to it should be logged, that it should be excluded from any data export sent to a third-party analytics tool, and that it should be deleted on a specific retention schedule. Very few founders write prompts that dense on the first pass, and there's no realistic version of AI-assisted development where they reliably would, across every field, for the entire lifetime of the product.

## A Simple Framework for Classifying Which Fields in Your Schema Actually Need Extra Protection

Most founders don't need a legal background to get a reasonable first pass at this — they need a simple way to sort their own data model into a few clear tiers, then treat each tier differently rather than treating every field the same way.

**A workable four-tier classification:**

1. **Public or already-visible data** — a business name, a public product listing, a published blog post. This data carries essentially no additional risk from being stored plainly, since it's meant to be seen widely anyway.
2. **Standard personal data** — a name, an email address, a phone number. Worth reasonable protection (access control, not sharing it unnecessarily), but plain storage in a standard database column is a common, defensible pattern for this tier.
3. **Sensitive personal data** — health information, financial details, government identifiers, precise location history, information about children. This tier generally warrants encryption at rest, tighter access logging, and a deliberate answer to "who on our own team can actually query this field directly."
4. **Data your specific industry regulates explicitly** — medical records under health-data rules, payment card details under PCI requirements, biometric data under increasingly common biometric-privacy laws. This tier often has legally mandated handling requirements beyond what a founder would choose on their own, and getting it wrong carries consequences beyond a data breach's usual reputational cost.

**A practical exercise worth doing with your own schema:** open your database's table list and go column by column, marking each one with a tier number from one to four. Most schemas turn out to be overwhelmingly tier one and two, with only a small handful of genuinely tier-three-or-four fields — which is useful to know, because it means the actual scope of a hardening pass is usually much narrower than "encrypt the whole database" makes it sound. PawFile's entire fix, for instance, touched only the medical-history and owner-contact fields; the scheduling logic, the calendar, the reminder system, and dozens of other tables were left completely untouched, because they never needed to be.

**A question worth asking yourself honestly:** if this specific field appeared in a news headline about a data breach, would it be a minor mention or the entire story? A leaked list of business names is a minor mention. A leaked list of pets' medical conditions tied to their owners' home addresses is closer to the entire story. That gut check, applied column by column, gets a founder most of the way to the same tier assignment a formal review would produce — the review's real value is catching the columns a founder wouldn't have thought to flag, and applying the technical protection correctly once the tier is decided.

## Closing the Gap Between Generated Code and Genuine Development

A proper review identifies which fields in your data model actually qualify as sensitive, applies appropriate encryption or access restriction to those specifically, and leaves the rest of your schema untouched. [LaunchStudio](https://launchstudio.eu/en/) performs exactly this kind of data-sensitivity review as part of its production-readiness process, backed by Manifera's 11+ years of software development experience across regulated and compliance-sensitive industries.

Manifera's data-handling reviews are led out of its Amsterdam headquarters at Herengracht 420, with implementation carried out by its engineering team at the Pho Quang Street development center in Ho Chi Minh City.

[Book a free 15-minute intro call](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: The Pet Records Nobody Encrypted

Anne, a former veterinary assistant turned founder in Haarlem, built PawFile, an AI-assisted scheduling and medical-history tool for small veterinary clinics, built with Cursor, storing pet owners' contact details alongside pets' medical treatment history.

While preparing a data processing agreement for a clinic client, Anne's accountant asked a simple question she couldn't answer: was medical history data encrypted at rest? LaunchStudio's review found it wasn't — treatment records sat in the same plain, unencrypted columns as a pet's name or breed.

**Result:** LaunchStudio applied field-level encryption specifically to medical history and owner contact data, leaving the rest of PawFile's scheduling logic and interface completely unchanged.

> *"I had genuinely never thought about medical records needing different treatment than a pet's name. Cursor built the database exactly as I described it, and I just never described that distinction."*
> — **Anne Verstappen, Founder, PawFile (Haarlem)**

**Cost & Timeline:** €2,500 (data sensitivity review and field-level encryption) — completed in 9 business days.

---

## Frequently Asked Questions

### A privacy lawyer might ask whether encryption alone satisfies GDPR obligations for health-adjacent data — does it?

Not entirely on its own — encryption is one specific technical safeguard among several GDPR expects (including lawful basis, retention limits, and access controls), so it addresses one real risk without functioning as complete compliance by itself.

### Is this specifically a veterinary-industry issue, or does it generalize to other founder verticals?

It generalizes broadly — any product handling health, financial, or identity-adjacent data faces the same underlying question, veterinary medical history is simply a clear, concrete example of a data category founders don't always intuitively recognize as sensitive.

### Manifera works with clients like CFLW Cyber Strategies on cybersecurity-adjacent work — does that inform how data sensitivity gets assessed for a founder project?

It does inform the underlying methodology — treating certain data categories as requiring distinct handling by default, rather than as an afterthought, is a habit carried over from more security-focused engagements into LaunchStudio's founder-facing reviews.

### Would a founder using a managed platform like Supabase's built-in auth still need this kind of review?

Yes — Supabase and similar platforms provide the infrastructure to implement encryption and access control, but they don't automatically decide which of your specific fields deserve that treatment; that judgment call still requires a deliberate review of your actual data model.

### How does a founder even know which fields in their own schema count as "sensitive" without a legal or security background?

That judgment call is exactly what a review is for — a founder describing what data their product collects, in plain language, is enough for LaunchStudio's engineers to identify which fields warrant additional protection, without the founder needing to make that determination themselves first.

### Once fields are tiered, does every tier-three or tier-four field need the exact same protection?

Not necessarily — the appropriate protection (encryption at rest, access logging, restricted query access) can vary by the specific regulatory requirement and how the data is actually used in the product, which is why the tiering exercise is a useful starting point for a review, not a substitute for one.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does encryption alone satisfy GDPR obligations for health-adjacent data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not entirely — encryption is one safeguard among several GDPR expects, including lawful basis and retention limits."
      }
    },
    {
      "@type": "Question",
      "name": "Is this issue specific to veterinary products?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, it generalizes to any product handling health, financial, or identity-adjacent data."
      }
    },
    {
      "@type": "Question",
      "name": "Does cybersecurity-adjacent client work inform how data sensitivity gets assessed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, treating certain data categories as requiring distinct handling by default carries over into founder-facing reviews."
      }
    },
    {
      "@type": "Question",
      "name": "Does a managed platform like Supabase remove the need for this review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, it provides the infrastructure but doesn't decide which specific fields need that protection."
      }
    },
    {
      "@type": "Question",
      "name": "How does a founder know which fields count as sensitive without a legal background?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Describing what data the product collects in plain language is enough for engineers to identify what needs protection."
      }
    },
    {
      "@type": "Question",
      "name": "Does every tier-three or tier-four field need the exact same protection?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not necessarily — protection varies by specific regulation and use, so tiering is a starting point for a review, not a substitute."
      }
    }
  ]
}
</script>
