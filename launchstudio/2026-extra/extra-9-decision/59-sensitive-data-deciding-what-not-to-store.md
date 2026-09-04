---
Title: "Sensitive Data: Deciding What Not to Store in the First Place"
Keywords: data minimisation engineering, special category data GDPR, sensitive data storage decisions, avoid storing PII, database schema privacy, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Sensitive Data: Deciding What Not to Store in the First Place

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Sensitive Data: Deciding What Not to Store in the First Place",
  "description": "A technical decision framework for indie hackers on which data categories to avoid storing entirely, which to tokenize or strip before persistence, and how data minimisation choices made at the schema level eliminate whole categories of future compliance and breach risk.",
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
  "datePublished": "2027-01-23",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/sensitive-data-deciding-what-not-to-store"
  }
}
</script>

Everyone treats data security as a storage problem — encrypt the database, lock down access, rotate the keys. Nobody talks about the cheaper, more permanent fix sitting one step earlier: data you never stored in the first place can't leak, can't be subpoenaed, can't show up in a breach notification, and doesn't need a deletion process built for it at all. Encryption protects data at rest. Access control protects data from unauthorized reads. Neither one protects you from the data simply existing — and a meaningful share of what gets stored in early-stage SaaS databases exists only because an AI coding tool generated a field for it, or a "just in case" instinct added a column nobody's used since, not because the product genuinely needs it.

This is the myth worth dismantling directly: more data collected feels like more capability, more insight, more future flexibility. In practice, for a two-person startup, every field storing personal or sensitive data is a liability you're carrying whether or not it ever gets used — a bigger breach exposure, a bigger GDPR compliance surface, a bigger honest-answer problem on a future security questionnaire. The highest-leverage security decision available to a solo technical founder isn't a better encryption scheme. It's deciding, field by field, what not to store at all.

## What "Special Category Data" Means and Why It Changes the Calculus Entirely

GDPR draws a hard line around "special category" personal data — health information, biometric data, genetic data, racial or ethnic origin, political opinions, religious beliefs, sexual orientation, and trade union membership — requiring a much narrower set of lawful bases to process it at all, generally explicit consent or a specific narrow exception, compared to ordinary personal data's broader set of available bases. For a solo founder, the practical implication is blunt: if your product doesn't strictly need to process special category data to function, don't build features that collect it, even if collecting it seems like it would enable a nice-to-have feature later. A fitness app tracking workout history doesn't need to ask about specific medical conditions unless a core feature genuinely depends on it; a dating app doesn't need to store explicit sexual orientation data as a searchable database field if matching logic can be built around user-controlled preference tags instead, handled with materially lighter compliance weight than a field explicitly labeled and processed as special category data. The decision point is at the feature-design stage, before a database column exists — once "medical_conditions text[]" is a live column with real user data in it, removing that liability means a migration and a user communication, not a five-minute design change.

## The Field-by-Field Audit: A Concrete Exercise, Not a Philosophy

Rather than treating data minimisation as an abstract principle, run it as a literal exercise against your actual schema: open every table that stores user-related data, and for each column, ask "does a real, current feature break without this field?" Columns that survive this test — email for login, a hashed password, the core data your product's actual function depends on — stay. Columns that don't — a phone number field nobody's used since a "maybe we'll add SMS" idea six months ago, a "date of birth" field collected during signup because a template included it, a free-text "notes" field visible to admins that's accumulated unstructured personal commentary about users — are candidates for removal, not just of the UI field, but of the underlying column and any historical data already in it. This exercise is worth running as a standing quarterly habit for a fast-moving indie product, not a one-time cleanup, because AI coding tools generate generous default schemas continuously as new features ship, and each new feature is a fresh opportunity for an unnecessary field to sneak back in.

## Tokenization and Redaction: What to Do With Data You Genuinely Need

Some sensitive data can't simply be avoided — payment details, government ID numbers for KYC-regulated products, health data for a health-adjacent product where it's core to the function. For these cases, the decision isn't "store nothing," it's "store the minimum representation that still lets the product function." Payment card numbers should never touch your own database at all — Stripe, Mollie, and every reputable processor handle this via tokenization, where your system stores an opaque token referencing the card, not the card number itself, meaning a breach of your database exposes tokens useless outside your specific Stripe account, not usable card numbers. Government ID numbers, where genuinely required for compliance (KYC in fintech, age verification in specific verticals), should be processed through a specialized verification provider that returns a pass/fail or a minimal derived claim ("verified over 18") rather than storing the raw ID document and number in your own database indefinitely — the verification event, not the raw document, is usually what your product actually needs to retain. For any sensitive free-text field that can't be avoided (support ticket content, user-submitted descriptions that might incidentally contain sensitive information), consider whether the field needs to be searchable and indexed in plaintext, or whether it can be encrypted at the application layer with access restricted to a narrow, audited path — a meaningfully different risk profile than a plaintext column any developer with database access can query directly.

## Log Files: The Sensitive Data Store Nobody Thinks to Minimise

This is the single most common gap LaunchStudio finds in AI-generated products, because it's genuinely invisible during normal development: application logs, error trackers, and debugging output routinely capture far more personal data than the database schema itself does, because logging frameworks by default log entire request payloads, form submissions, and API responses without anyone deciding that's appropriate. A password reset flow that logs the full request body for debugging purposes can end up logging plaintext passwords into a third-party error-tracking tool (Sentry, LogRocket) that nobody thinks of as "the database" but functions as one for compliance purposes. Session replay tools, popular for debugging user issues, can capture literally everything a user types, including data explicitly marked to be masked if that masking configuration wasn't set up correctly and verified. The decision here is specific and technical: audit what your logging and error-tracking tools actually capture, configure field-level scrubbing for anything sensitive (most tools support redaction rules, but they're opt-in configuration, not a default), and treat "does this new endpoint log anything sensitive by default" as a standing question when shipping new API routes, the same instinct as checking for a SQL injection vulnerability.

## Retention: The Data Minimisation Decision After the Data Already Exists

Even carefully minimised necessary data shouldn't live forever by default. GDPR's storage limitation principle requires retaining personal data no longer than necessary for the purpose it was collected for, which translates into a concrete engineering decision: define a retention period per data category and build the deletion job that enforces it, rather than accumulating data indefinitely because deleting it was never explicitly decided against. Account data for an active user needs to persist as long as the account is active — straightforward. But abandoned signup attempts that never converted, old support tickets from years-inactive accounts, verbose logs beyond what's useful for debugging recent issues, and soft-deleted records that were "deleted" from the user's perspective but never actually purged from the database all accumulate as pure liability with no offsetting product value. A practical default for a solo founder: 30-90 days for verbose logs, a defined retention window (commonly a few years, aligned to any applicable legal retention requirement like tax records) for closed accounts, and an actual scheduled job — not a manual someday task — that enforces these windows automatically.

## The AI API Data Minimisation Decision

For products routing user data through a third-party AI API — increasingly common across nearly every AI-native product — a specific minimisation decision matters more than founders initially realize: does the data sent to the model actually need to include personal identifiers, or can it be stripped or pseudonymized before the API call? A support-ticket summarization feature calling an LLM API frequently doesn't need the customer's actual name and email in the prompt to produce a useful summary — replacing them with a placeholder token before the call, and re-inserting the real values afterward in your own system, achieves the same product outcome while meaningfully reducing what leaves your infrastructure to a third party at all. This is a genuinely cheap engineering pattern — a find-and-replace pass before the API call and after the response — and it sidesteps a whole category of questions about the AI provider's data retention and training-use policies, because de-identified data flowing through a third party carries substantially less risk regardless of what that provider's own policies say.

## Why This Is the Cheapest Security Investment Available to a Solo Founder

Every other security control — encryption, access logging, intrusion detection, breach response planning — has an ongoing cost: it requires maintenance, monitoring, and expertise to run correctly over time. Data minimisation is nearly unique in being front-loaded: the decision to not collect a field, or to strip an identifier before an API call, costs a few minutes of design thought once and then costs nothing forever afterward, because there's simply less surface area to protect, audit, or eventually explain in a breach notification or a security questionnaire. For a solo technical founder without a security team, without dedicated ops capacity, and without much budget for tooling, this is the highest-leverage category of security decision available — not because it replaces encryption or access control, but because it shrinks what those other controls need to protect in the first place.

Auditing a schema and its logging pipeline for exactly this kind of unnecessary sensitive-data exposure — the fields, logs, and third-party payloads nobody deliberately decided to include — is core to the security hardening [LaunchStudio](https://launchstudio.eu/en/) does on AI-generated products before launch, backed by Manifera's 11+ years of production security experience across regulated and unregulated clients alike.

[Send us your prototype link for free feedback](https://launchstudio.eu/en/#contact) on what your schema and logs are quietly storing that they don't need to.

## Real example

### A Technical Solo Founder in Action: The Field Nobody Remembered Adding

Joris Dekker built Spreekuur, a scheduling tool for independent therapists to manage client appointments, using Cursor over several intense weekends, and moved fast enough that the schema accumulated fields organically as features got added — including a free-text "session_notes" column added early on as a placeholder for a "maybe someday" feature that never actually shipped, but that a handful of early users had started using anyway, typing genuine clinical notes into a field with no encryption, no access restriction beyond standard row-level security, and full visibility to Joris's own debugging queries.

A LaunchStudio review, done ahead of Joris pursuing a partnership with a therapy practice network, flagged the field immediately as effectively unmanaged special category health data sitting in a plaintext column that had never been part of a deliberate product decision — it existed because Cursor had generated it early on and nobody had revisited whether it should. The team helped Joris either remove the field entirely for users not actively using it, or migrate active users' notes to an application-layer-encrypted column with access logged and restricted to the individual therapist's own session.

**Result:** Spreekuur launched its practice-network partnership with a schema Joris could confidently describe field by field, and the resolved field became the centerpiece of an honest, specific answer in the network's own security review rather than a liability he'd have had to disclose reactively.

> *"I didn't consciously decide to store clinical notes insecurely. I just never consciously decided anything about that field at all — it was just there, from a feature I forgot I'd half-built."*
> — **Joris Dekker, Founder, Spreekuur (Delft)**

## Frequently Asked Questions

### How do I know if a data field counts as "special category" under GDPR?

Special category data is a specific, enumerated list: health, biometric, genetic, racial or ethnic origin, political opinion, religious belief, sexual orientation, and trade union membership. If a field doesn't clearly fall into one of these categories, it's ordinary personal data with a broader set of available lawful bases, though still worth minimising for general security reasons.

### Is it safe to log request payloads for debugging as long as I don't look at the logs often?

No — the risk isn't how often you look, it's that the data exists in a third-party tool (Sentry, LogRocket, a cloud logging service) with its own access controls, retention policies, and potential exposure, regardless of your own usage habits. Configure field-level redaction for sensitive data before it ever reaches the logging tool, rather than relying on discipline about not reading the logs.

### Does tokenizing payment data through Stripe mean I don't need to think about PCI compliance at all?

Using Stripe's or a similar processor's tokenization and hosted checkout correctly removes the large majority of PCI-DSS scope from your own systems, since raw card data never touches your servers. You still need to follow the specific integration pattern the processor recommends (their hosted fields or checkout, not building your own card input form) to actually achieve that reduced scope.

### How long should I actually retain data before deleting it?

There's no single universal answer — it depends on the data category and any legal retention requirements (tax records commonly need multi-year retention in most EU jurisdictions), but as a working default, verbose logs in the 30-90 day range and closed-account data aligned to your legal minimum retention requirement is a reasonable starting point for most SaaS products.

### Is stripping personal data before sending it to an AI API actually effective, or just security theater?

It's genuinely effective risk reduction, not theater — data that never leaves your infrastructure with identifiable information attached can't be exposed by a third-party provider's own breach, retention policy, or misuse, regardless of what that provider's terms say. It doesn't eliminate every risk (the underlying content might still be sensitive even de-identified), but it meaningfully narrows what's exposed.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "How do I know if a data field counts as special category under GDPR?", "acceptedAnswer": { "@type": "Answer", "text": "Special category data is a specific, enumerated list: health, biometric, genetic, racial or ethnic origin, political opinion, religious belief, sexual orientation, and trade union membership. Fields outside this list are ordinary personal data with broader available lawful bases." } },
    { "@type": "Question", "name": "Is it safe to log request payloads for debugging as long as I don't look at the logs often?", "acceptedAnswer": { "@type": "Answer", "text": "No. The risk is that the data exists in a third-party tool with its own access controls and retention policies, regardless of your own usage habits. Configure field-level redaction before sensitive data reaches the logging tool." } },
    { "@type": "Question", "name": "Does tokenizing payment data through Stripe mean I don't need to think about PCI compliance at all?", "acceptedAnswer": { "@type": "Answer", "text": "Using a processor's tokenization and hosted checkout correctly removes most PCI-DSS scope from your own systems since raw card data never touches your servers, but you need to follow their recommended integration pattern to actually achieve that reduced scope." } },
    { "@type": "Question", "name": "How long should I actually retain data before deleting it?", "acceptedAnswer": { "@type": "Answer", "text": "It depends on the data category and legal retention requirements, but as a working default, verbose logs in the 30-90 day range and closed-account data aligned to your legal minimum retention requirement is reasonable for most SaaS products." } },
    { "@type": "Question", "name": "Is stripping personal data before sending it to an AI API actually effective, or just security theater?", "acceptedAnswer": { "@type": "Answer", "text": "It's genuinely effective risk reduction. Data that never leaves your infrastructure with identifiable information attached can't be exposed by a third-party provider's breach or retention policy, though it doesn't eliminate every risk if the underlying content is still sensitive." } }
  ]
}
</script>
