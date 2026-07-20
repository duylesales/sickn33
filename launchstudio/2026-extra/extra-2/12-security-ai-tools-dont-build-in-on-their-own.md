---
Title: "Security AI Tools Don't Build In on Their Own"
Keywords: security ai, ai secure, ai coding, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Security AI Tools Don't Build In on Their Own

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Security AI Tools Don't Build In on Their Own",
  "description": "There's a specific irony in a security-monitoring product built with AI tools that itself stores passwords in plaintext. A technical deep-dive into why security-mindedness in a product's mission doesn't extend to its own codebase.",
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
  "datePublished": "2026-07-23",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/security-ai-tools-dont-build-in-on-their-own"
  }
}
</script>

There's a specific, almost uncomfortable irony that comes up more often than founders expect: a product whose entire premise is helping other businesses monitor their own security can itself be built with a glaring security gap, because the AI coding tool that built it has no particular awareness of the product's mission — it just builds what's described, the same way it would for any other kind of app.

## Why Domain Doesn't Transfer to Implementation

Building a security-focused product requires a founder to think carefully about security as a feature — what threats to detect, what alerts to send, what dashboards to show. It doesn't automatically require, or produce, careful thinking about security as a property of the codebase itself — how passwords are stored, how sessions are managed, how the underlying infrastructure is protected. These are two entirely separate concerns that happen to share the word "security," and an AI coding tool addresses the first because it was asked to, without addressing the second because it wasn't.

## The Specific, Textbook Failure: Plaintext Password Fallback

One of the oldest, most well-known security anti-patterns is storing user passwords in plaintext, or falling back to plaintext storage when a hashing library isn't properly configured. AI-generated authentication code sometimes includes a working hashing implementation for the main signup path, while a secondary path — an admin-created account, a bulk import, a password-reset completion — falls back to storing the new password directly, unhashed, because that secondary path wasn't as thoroughly specified in the original prompt.

## Why a Working Login Doesn't Rule This Out

Logging in successfully proves only that whatever's stored matches what's compared during login — it says nothing about the format in which that value is stored. A plaintext password and a properly hashed one can both authenticate a user correctly during normal use; the difference only becomes catastrophic in the event of a database breach, which a founder's day-to-day testing will never simulate.

## Why This Specific Gap Tends to Hide in Secondary Paths

Founders and AI tools alike tend to focus attention on the primary, most-used flow — the signup form a new user sees first. Secondary account-creation paths, added later or less carefully specified, are exactly where inconsistent handling creeps in, because each new path is effectively a fresh implementation decision rather than an extension of an already-reviewed one.

## What a Genuine Fix Requires

Closing this gap means auditing every single path that creates or updates a stored password — not just the main one — and confirming each applies the same proper hashing consistently, then migrating any existing plaintext-stored values safely. [LaunchStudio](https://launchstudio.eu/en/) performs exactly this kind of full-path authentication audit, backed by Manifera's 11+ years of security-focused engineering experience, including work adjacent to cybersecurity research through CEO Herre Roelevink's prior background with CFLW Cyber Strategies.

Manifera's authentication audits are carried out by the engineering team at the Ho Chi Minh City development center on Pho Quang Street, with client relationships managed from the Amsterdam headquarters at Herengracht 420.

[Talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: The Monitoring Tool That Didn't Monitor Itself

Iris, a former IT compliance officer turned founder in Apeldoorn, built WachtPost, an AI-assisted security-alert monitoring dashboard for small businesses, built with Cursor, offering both self-service signup and an admin-assisted onboarding path for less technical clients.

While preparing for a client's own security audit of WachtPost as a vendor, Iris's technical advisor asked to see how passwords were hashed. The self-service signup path was hashed correctly — but accounts created through admin-assisted onboarding, added later in development, stored the client's chosen password directly in plaintext.

**Result:** LaunchStudio audited every account-creation path in WachtPost, applied consistent hashing across all of them, and safely migrated the affected plaintext-stored passwords, closing the inconsistency before it reached the client's own audit.

> *"The whole point of WachtPost is telling other businesses about exactly this kind of gap. Finding it in my own product before a client did was a genuinely humbling moment."*
> — **Iris van Dongen, Founder, WachtPost (Apeldoorn)**

**Cost & Timeline:** €2,600 (full authentication path audit and password migration) — completed in 9 business days.

---

## Frequently Asked Questions

### Would an experienced security auditor be surprised that a security-focused product had this specific gap?

Not especially — auditors specifically expect to check every account-creation path independently precisely because secondary paths are so commonly inconsistent with the primary one, regardless of what the product itself claims to specialize in.

### Is plaintext password storage still a common issue in 2026, given how well-documented the risk is?

It remains common specifically in secondary or later-added paths, even in otherwise well-built products, because the risk being well-documented doesn't mean every new code path automatically inherits the lesson — each new implementation is a fresh decision unless explicitly reviewed against the same standard.

### Does Herre Roelevink's cybersecurity background through CFLW give LaunchStudio a specific edge in catching this type of issue versus a general dev shop?

It shapes the review methodology directly — treating every account-creation path as independently suspect until verified, rather than assuming consistency, is a habit drawn from dedicated cybersecurity practice rather than general software development.

### Does this kind of audit require access to a founder's live user database, or can it be done without touching real customer data?

It can typically be assessed by reviewing the code paths themselves without needing direct access to live customer data, though remediating any already-affected accounts does require careful, direct handling of the existing data under appropriate safeguards.

### Should a founder assume their AI tool used the same authentication pattern everywhere just because the main flow looks correct?

No — as WachtPost's case shows directly, a correctly implemented primary flow provides no guarantee about secondary or later-added flows, which is exactly the assumption a dedicated audit exists to test rather than take on faith.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Would experienced auditors be surprised a security product had this gap?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not especially — auditors expect to check every account-creation path independently regardless of the product's focus."
      }
    },
    {
      "@type": "Question",
      "name": "Is plaintext password storage still common despite being well-documented?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, especially in secondary paths, since being well-documented doesn't mean every new code path inherits the lesson."
      }
    },
    {
      "@type": "Question",
      "name": "Does a cybersecurity background give an edge in catching this issue?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, treating every account-creation path as independently suspect is a habit from dedicated cybersecurity practice."
      }
    },
    {
      "@type": "Question",
      "name": "Does this kind of audit require access to live customer data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Assessment can be done from the code paths alone, though remediation requires careful handling of affected data."
      }
    },
    {
      "@type": "Question",
      "name": "Should a founder assume all authentication paths follow the same pattern if the main one is correct?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, a correct primary flow provides no guarantee about secondary or later-added flows."
      }
    }
  ]
}
</script>
