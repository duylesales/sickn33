---
Title: "AI App Security Starts With Where You Keep Your Secrets"
Keywords: ai app security, environment variables frontend exposure, api key rotation, git history secrets, Cursor, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI App Security Starts With Where You Keep Your Secrets

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Security Starts With Where You Keep Your Secrets",
  "description": "A practical guide to credential handling in AI-generated applications: which keys are actually secret, why build tools publish some variables on purpose, how git history keeps copies, and a ten-minute audit you can run today.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/where-secrets-belong-in-an-ai-built-app" }
}
</script>

A founder in Tilburg discovered his mapping provider had billed him for 1.4 million requests in eleven days. He had roughly 200 users. The key that authorised those requests had been sitting in his published JavaScript since launch, and somebody — or more likely something — had found it and started using his account as free infrastructure.

Nothing was hacked. No system was breached. He had simply published a credential, which is what most AI-built applications do by default, and the bill arrived before anyone noticed.

This article is about which credentials matter, where they end up, and how to find yours in about ten minutes.

## Not Everything Is a Secret

A useful first distinction, because treating everything as sensitive produces paralysis and treating nothing as sensitive produces the story above.

**Public identifiers are meant to travel.** A Supabase public key, a Stripe publishable key, a Google Analytics ID, a public map style identifier. These say which project you are, not what you may do, and they are designed to sit in a browser.

**Secrets authorise action.** A Supabase service role key, a Stripe secret key, an email provider's API key, a model provider's API key, database connection strings with credentials, webhook signing secrets. Anyone holding one can act as your application.

**The category that catches people out: keys that spend money.** Mapping, SMS, translation, and AI model APIs bill per request. A leaked key of this kind is not a data breach; it is a direct debit with no upper bound, and automated scanners find exposed keys within hours of publication.

If you are unsure which category something falls into, the provider's documentation states it explicitly, and the answer is worth reading before rather than after.

## The Four Places Secrets End Up

**In the frontend bundle.** The most common. It happens because the fastest way to make an API call work is to make it from the code you are already editing, and in an AI-assisted workflow that is the code the model is looking at.

**In the repository.** A `.env` file committed early, before anyone added it to the ignore list. Everything downstream — every clone, every fork, every collaborator — carries a copy.

**In a platform dashboard nobody can leave.** Variables configured in a hosting or builder interface, known only to whoever set them up. This is safer than the first two and becomes a problem when you migrate, when a contractor leaves, or when you need to rotate and cannot find every location.

**In conversation.** Pasted into a chat with a developer, emailed to a contractor, dropped into a shared document. These copies persist far longer than the working relationship and are invisible to any technical audit.

## Why Some Variables Are Published on Purpose

This is the mechanic that produces the most surprised founders.

Frontend build tools need a way to pass configuration into browser code, so they expose environment variables that carry a specific prefix — the exact prefix depends on the framework. Anything with that prefix is inlined into the JavaScript your users download. That is not a leak; it is the documented behaviour.

The trap is that a variable in a `.env` file *feels* private regardless of its name. Put a secret key into a prefixed variable and it looks exactly like configuration while being published to the world. This is precisely how the mapping key in the opening story travelled, and it is invisible in the source code because the source only shows the variable name.

Rule of thumb: if a variable is read by code that runs in a browser, treat its value as public, whatever the file it lives in suggests.

## Git History Keeps What You Deleted

Removing a key from a file removes it from the current state, not from the repository's memory. Every previous commit still contains it, and anyone with access to the history can read it.

If a repository was ever public, even briefly, assume any credential it contained is compromised. Automated scanners monitor public repositories continuously and the window between publication and discovery is frequently minutes.

The correct response is rotation rather than history rewriting. Rewriting history is possible and awkward, and it does not retrieve copies already taken. Changing the key makes every copy worthless, which is the outcome you actually want.

## Where Secrets Should Live Instead

**In server-side environments only.** Serverless function configuration, your hosting platform's secret storage, or a dedicated secrets manager. Never in code that reaches a browser.

**Behind your own endpoint.** When a frontend needs something a secret unlocks — a map render, a model completion, an SMS — it calls your own server-side function, which checks who the user is, applies your own rate limit, then calls the third party with the secret. Your key never leaves your infrastructure and you gain the ability to cut off abuse.

**Scoped as narrowly as the provider allows.** Many services issue restricted keys: read-only, domain-restricted, limited to specific endpoints, capped in spend. If a key must be exposed by design, a scoped one limits the damage.

**With spending limits configured.** For any metered service, set a hard cap in the provider's dashboard. It will not prevent a leak and it turns an unbounded bill into a bounded one.

**Rotatable in one place.** If changing a key means editing six files and redeploying three services, rotation becomes something you avoid — and avoided rotation is how a contractor from last year still has working access.

## A Ten-Minute Audit

- Open your live site, view the page source, and search the loaded JavaScript for `key`, `secret`, `token` and `api`.
- List every third-party service your app calls. For each, check the provider's documentation for which of their keys are publishable and which are not.
- Search your repository for `.env`, and check whether it is in the ignore file. Then search the history, not just the current files.
- Open your hosting platform's environment settings and read every variable. Ask, for each one, whether it is prefixed for browser exposure.
- Check the billing dashboard of every metered service for usage that does not match your traffic.
- Ask yourself who else has ever held these values — contractors, former co-founders, a chat thread.

Anything ambiguous should be rotated. Rotation is cheap; discovery is not.

## What Good Looks Like Afterwards

A short list of secrets, each existing in exactly one authoritative place. Frontend code containing only public identifiers. Every third-party call that uses a secret routed through your own endpoint with authentication and a rate limit in front of it. Spending caps on anything metered. A documented rotation procedure that takes minutes. And ideally a check in your deployment pipeline that fails the build if a credential pattern appears in a client bundle — because the original mistake is always made late in the evening under deadline pressure, and a pipeline does not get tired.

## Getting There Without Rebuilding

Credential handling is one of the most common findings when an AI-built application comes in for review, and it is also one of the fastest to resolve. LaunchStudio audits every credential in the codebase, the build configuration and the git history, rotates what is exposed, moves privileged calls behind server-side functions with authentication and rate limiting, configures scoped keys and spending caps, and adds a build-time check so it does not recur.

The interface you built in Lovable, Bolt or Cursor stays exactly as it is, and the codebase is left conventional and AI-readable so you can keep working in your own tool. That is part of the [Launch Ready package](https://launchstudio.eu/en/#packages), delivered by Manifera's engineers — eleven years of production systems for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City.

If your ten-minute audit turned up something you cannot explain, [talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact).

## Credentials That Outlive the Relationship

The technical audit above finds keys in code. It does not find keys in people, and that is the category that produces the most awkward conversations.

**Contractors.** A freelancer who worked on your app for three weeks in the spring may still hold database credentials, a hosting login and a payment provider invitation. The engagement ended; the access did not, because nobody made a list.

**Former co-founders.** The most uncomfortable version, and the most common in small startups. Access granted informally at a point when trust was total, never revoked because revoking it would have been a statement.

**Shared tooling.** Password managers with a shared vault, a team account that everyone signs into, a document listing credentials for convenience. These leak by copying rather than by breach.

**Your past self.** Values pasted into chats with AI assistants, support tickets, or emails to yourself. They persist in places no audit script reaches.

The remedy is a short offboarding routine applied every time someone stops working on the product: remove their account access from each service, rotate any shared credential they could have copied, and check whether anything was in their name rather than yours. It takes twenty minutes and it is the difference between access that ends and access that merely stops being used.

Make the list of who has ever held what, and keep it. Not out of suspicion — out of the same instinct that makes you keep a list of who has keys to an office.

## Real example

### A Route Planner That Funded Somebody Else's Project

Stefan Rombouts built Bezorgroute in Cursor: a delivery route optimiser sold to small catering companies around Tilburg. It called a commercial mapping API for distances and turn-by-turn directions, and the key sat in a prefixed environment variable that was published into the frontend bundle at build time.

The first month's invoice was ordinary. The second was forty times larger. Usage analytics showed requests originating from addresses across three continents, at a rate no catering company in Brabant could produce.

The remediation took four business days. The mapping key was revoked and reissued with domain restrictions and a hard monthly spending cap. All mapping calls moved behind a server-side function that authenticates the caller, checks they are an active subscriber, and rate-limits per account. The git history was audited, which surfaced two further credentials committed eight months earlier — an email provider key and a database connection string — both rotated. A build-time check was added that fails deployment if a credential pattern appears in the client bundle.

The provider credited part of the fraudulent usage after Stefan demonstrated the key had been restricted and the architecture changed, which would not have been possible without evidence of the fix.

**Result:** mapping costs returned to normal and have stayed proportional to subscriber count for fourteen months, and the build check has since blocked one further attempt to expose a key during a rushed feature release.

> *"I was paying for someone else's product. The key was in my own website, visible to anyone who pressed the right button in their browser."*
> — **Stefan Rombouts, Founder, Bezorgroute (Tilburg)**

**Cost & Timeline:** €1,650 (credential audit, key rotation, server-side proxy with rate limiting, pipeline check) — completed in 4 business days.

## Frequently Asked Questions

### How do I tell whether a key is safe to put in my frontend?

Check the provider's documentation, which states it explicitly. Public or publishable keys identify your project and are designed for browsers; secret keys authorise actions and must stay server-side. When the documentation is ambiguous, treat it as secret.

### I removed the key from my code. Is that enough?

No. Every previous commit still contains it, and if the repository was ever public it may already have been collected. Rotate the key, which makes every existing copy worthless, rather than relying on deletion.

### What if my app genuinely needs to call a paid API from the browser?

Route the call through your own server-side endpoint instead. Your function authenticates the user, applies your rate limit, then calls the third party with the secret. The key stays on your infrastructure and you retain the ability to stop abuse.

### Why did my key get found so quickly?

Automated scanners continuously scrape public repositories and published JavaScript for credential patterns. There is rarely a human looking for your specific key — it is found by a script, often within hours of exposure.

### Do spending limits protect me from a leaked key?

They do not prevent misuse, and they convert an unbounded bill into a bounded one, which is worth configuring on every metered service regardless of how confident you are about your key handling.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I tell whether a key is safe to put in my frontend?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The provider's documentation states it. Public or publishable keys identify your project and are designed for browsers; secret keys authorise actions and must stay server-side. When ambiguous, treat it as secret."
      }
    },
    {
      "@type": "Question",
      "name": "I removed the key from my code. Is that enough?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Previous commits still contain it, and a briefly public repository may already have been scraped. Rotate the key so every existing copy becomes worthless."
      }
    },
    {
      "@type": "Question",
      "name": "What if my app genuinely needs to call a paid API from the browser?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Route it through your own server-side endpoint that authenticates the user and applies a rate limit before calling the third party, so the secret never leaves your infrastructure."
      }
    },
    {
      "@type": "Question",
      "name": "Why did my key get found so quickly?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Automated scanners continuously scrape public repositories and published JavaScript for credential patterns, often finding exposed keys within hours."
      }
    },
    {
      "@type": "Question",
      "name": "Do spending limits protect me from a leaked key?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They do not prevent misuse but they bound the damage, which makes them worth configuring on every metered service."
      }
    }
  ]
}
</script>
