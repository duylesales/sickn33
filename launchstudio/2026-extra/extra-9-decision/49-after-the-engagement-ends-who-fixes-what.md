---
Title: "After the Engagement Ends: Who Fixes What, and When"
Keywords: post-launch support window, warranty bug fix scope, software handover package, expiring SSL certificates, self-managed hosting after launch, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# After the Engagement Ends: Who Fixes What, and When

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "After the Engagement Ends: Who Fixes What, and When",
  "description": "The line between a covered bug fix and billable new work, what a real handover package contains, and the things that break on their own months later — expiring certificates, dependency updates, API deprecations — that a technical founder needs to plan for before the support window closes.",
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
  "datePublished": "2027-01-26",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/after-the-engagement-ends-who-fixes-what"
  }
}
</script>

"Is this covered under the 48-hour window, or is this a new ticket?"

That question, asked by a founder in a support thread eleven days after launch, is more revealing than it looks. It means nobody defined the boundary clearly enough at the start for the founder to answer it themselves. And it's not a rare question — it's close to the single most common source of friction between a technical founder and a development partner once the initial build is done, because "bug fix" and "new work" feel obviously different in the abstract and turn out to be genuinely ambiguous in the specific case sitting in front of you.

This matters more for a technical solo founder than most, because you're the one who's going to keep building on this codebase yourself once the engagement ends. Getting the boundary, the handover, and the maintenance timeline right isn't just about the first two weeks post-launch — it's about whether you can actually maintain and extend what was built, or whether you're quietly locked out of your own product by gaps nobody flagged at handover.

## The Line Between Warranty and New Work, Defined Before You Need It

The useful definition of a bug, for the purposes of a post-launch warranty window, is: the software doesn't do what was specified and agreed during the engagement. If the scoping document said users could reset their password and the reset email never arrives, that's a bug — the built thing doesn't match the agreed thing. If the scoping document said nothing about two-factor authentication and you now want it added, that's new work, however small it seems to add, because it's a capability that was never part of what was priced and delivered.

The ambiguity almost always lives in the space between those two clean examples, and a few patterns come up repeatedly. A feature that technically works but performs badly under conditions nobody tested for — a search function that returns correct results but takes eight seconds — sits closer to a bug than most founders initially assume, because "search works" implicitly meant "search works usably," not just "search returns the right answer eventually." A feature that works as specified but where the specification itself turns out to have been wrong or incomplete — "when we said 'send a confirmation email' we didn't realize we needed to also handle the case where the email bounces" — is the genuinely gray area, and the honest answer depends on how reasonably foreseeable the gap was at scoping time, which is exactly why it's worth resolving with a direct conversation rather than a unilateral call from either side. And a change requested because real users are behaving differently than expected — "nobody uses the feature the way we designed it, we need to change the flow" — is new work almost without exception, because it reflects a product decision made after launch, not a defect in what was built.

The practical fix isn't a perfect definition — none exists — it's agreeing, in writing, before the engagement starts, on the process for resolving an ambiguous case: usually a short conversation, in good faith, referencing the original scoping document, with the benefit of the doubt going to the founder for anything within roughly the first week and shifting toward a case-by-case judgment call after that, as the line between "this was always broken" and "this changed later" gets genuinely harder to establish with confidence.

## What a Real Handover Package Actually Contains

A handover package that's just "here's your GitHub repo link" is not a handover package — it's a repo link, and it leaves a technical founder able to read code without necessarily understanding the decisions embedded in it. A real handover, worth insisting on explicitly before an engagement is considered complete, includes several distinct things.

Environment documentation: every environment variable, what it does, where its value lives (and how to rotate it if it's a secret), and which services — Stripe, a hosting provider, an email service like Resend or Postmark, an auth provider — each one connects to. Architecture notes: not a full technical spec, but a readable summary of the major decisions — why this database structure, why this auth approach, what the deployment pipeline does at each step — written so that you, picking the codebase back up in four months, can reconstruct the reasoning without reverse-engineering it from the code alone. Access transfer: full ownership of every account the engagement touched — hosting, domain, payment processor, email service, error monitoring — confirmed in your name, with old collaborator or service-account access removed, not left dangling. A dependency and service inventory: every third-party library, API, and paid service the product relies on, ideally with version numbers and renewal or billing dates attached, because this is the single most common thing a founder discovers is missing three months later, at the worst possible moment.

And critically for anyone planning to keep building with AI tools: documentation written in a way that's genuinely useful to feed back into Lovable, Cursor, or Bolt for your next round of changes — clear naming, comments on non-obvious logic, a structure an AI coding assistant can actually parse and extend, rather than technically-correct-but-opaque code that only the original engineer could safely modify.

## The Things That Break on Their Own, Quietly, Months Later

This is the category founders underestimate most, because nothing about it feels like "the software has a bug" — it's the software continuing to work exactly as built while the world around it changes, and the gap between those two things eventually becomes an outage that looks, from the inside, exactly like something broke.

SSL/TLS certificates, if not on auto-renewal through a service like Let's Encrypt integrated into the hosting setup, expire on a fixed schedule — typically 90 days for Let's Encrypt, up to a year for others — and an expired certificate doesn't degrade gracefully, it presents visitors with a security warning that stops most of them cold. Confirming auto-renewal is actually configured, not just assumed, is a five-minute check worth doing at handover rather than a surprise browser warning worth discovering from a customer's screenshot. Dependency updates — the libraries and packages your product is built on — carry their own decay curve: a library version that's current and secure at launch accumulates known vulnerabilities over time as security researchers find and publish them, and a product that's never had its dependencies updated since launch is, eighteen months later, running on components with publicly documented weaknesses that didn't exist as risks on day one. Third-party API deprecations are the third quiet failure mode: the payment provider, the mapping API, the email service — any of them can change their API version, deprecate an endpoint, or update authentication requirements on their own schedule, with advance notice that goes to whichever email address is on the account, which is a real problem if that email address was the original developer's rather than yours.

None of these show up in a QA pass at launch, because none of them are wrong yet at launch — they're time bombs with different fuse lengths, and the founders who avoid being surprised by them are the ones who know the fuse lengths in advance rather than discovering them by outage.

## Building Your Own Post-Handover Maintenance Calendar

Given the previous section, a concrete artifact worth having before the engagement officially closes: a simple calendar, even just a handful of recurring entries in whatever tool you already use, covering the predictable maintenance a self-managed product needs. A quarterly check that SSL auto-renewal actually fired (checking the certificate's expiry date takes thirty seconds in any browser). A quarterly or monthly dependency audit — running your package manager's built-in vulnerability check (`npm audit` or the equivalent for your stack) and updating anything flagged as high-severity, rather than letting updates accumulate into a large, risky batch. An annual review of every third-party service's status page and changelog for anything you rely on directly, since deprecation notices are easy to miss in a busy inbox but usually appear on a status or developer blog well in advance too.

This calendar is the single highest-leverage five minutes a founder spends at handover, because it converts "things that break on their own eventually" from an unknown, anxiety-inducing category into a short, known, schedulable list — which is exactly the difference between a founder who gets blindsided by an expired certificate at 11 PM and one who fixed it during a routine Tuesday check three weeks before it would have expired.

## Keep Building Yourself: What Makes a Codebase Actually AI-Readable

For a technical solo founder, the real promise of a good handover isn't just "the code works" — it's "you can keep extending this yourself, including with the same AI tools you started with." That promise depends on specific, checkable qualities in the code and documentation, not just a general sense of code quality.

Consistent naming conventions matter more for AI-assisted extension than for human-only maintenance, because an AI coding assistant infers a lot of context from naming patterns, and inconsistent naming — a `user_id` here, a `userId` there, a `uid` somewhere else, all referring to the same concept — meaningfully degrades how well a tool like Cursor can reason about the codebase when you ask it to add a feature. Comments on non-obvious business logic — not comments on every line, which add noise, but comments explaining *why* a particular decision was made where the reasoning isn't visible from the code alone — give both you and an AI tool the context that prevents a well-intentioned future change from breaking something for a reason nobody wrote down. And a clear separation between the frontend you built and the backend infrastructure added during the engagement, documented explicitly rather than left to be inferred from file structure, is what actually lets you keep working in Lovable or Bolt on the parts you're comfortable with while understanding where the boundary is with the parts that need more care.

Asking directly, before an engagement is called complete: "if I open this repo in Cursor in six months and ask it to add a feature, will it have what it needs to do that safely?" is a fair, specific question, and a partner confident in their own handover should be able to answer it without hedging.

[Manifera has shipped 160+ projects for enterprise clients](https://www.manifera.com/services/web-app-develop/) before turning that same documentation discipline toward founder-scale handovers through LaunchStudio, on the principle that the code — and the understanding of it — belongs to the founder, always.

Describe what's still open on your current build and what you're hoping to keep doing yourself — we'll reply within one business day with what a proper handover package would include for your specific stack.

## Real example

### An Indie Hacker in Action: The Handover That Actually Held Up

Tobias Reinders, a backend-leaning solo founder in Leiden, built Werkrooster, a shift-scheduling tool for small retail teams, mostly in Cursor with an AI-generated Node.js backend. After a two-week LaunchStudio hardening engagement covering auth and payment integration, Tobias specifically asked for the extended handover package rather than just repo access, planning to keep building the product himself.

Four months later, an SSL renewal check he'd added to his own calendar — copied directly from the handover documentation's maintenance checklist — caught a certificate that had silently failed to auto-renew due to a DNS configuration change he'd made himself the previous month, breaking the automated renewal's verification step. He fixed it in twenty minutes, three weeks before it would have expired and taken the site down with a security warning in front of live customers.

**Result:** The same handover package's dependency inventory let Tobias run a security audit himself six months post-launch, updating two packages flagged with newly disclosed vulnerabilities — work he was able to do independently because the original documentation had named every dependency and its role clearly enough for him, and his AI coding tools, to act on it without needing to re-engage anyone.

> *"The code was never the hard part for me. Knowing what would quietly break in month five if I didn't check — that's what the handover doc actually gave me."*
> — **Tobias Reinders, Founder, Werkrooster (Leiden)**

**Cost & Timeline:** €2,900 (Launch Ready package, auth and Mollie integration, extended handover documentation) — live in 10 business days.

---

## Frequently Asked Questions

### How long does a typical post-launch bug-fix warranty window actually last?

LaunchStudio's Launch Ready package includes a 48-hour post-launch support window as standard, covering anything that doesn't match what was scoped and agreed. Longer or ongoing coverage is available through a managed plan for founders who want continued support beyond the initial window.

### What's a fair way to resolve a disagreement about whether something is a bug or new work?

Go back to the original scoping document and ask whether the behavior in question was explicitly agreed to. If it was and the software doesn't match it, that's a bug. If it wasn't discussed, or reflects a decision made after seeing the product in use, it's new work — and agreeing on this process before the engagement starts avoids the disagreement turning personal later.

### What's the single most important item in a handover package for a technical founder?

The dependency and third-party service inventory, because it's the thing most likely to cause a real problem months later if missing — a certificate, a deprecated API, an outdated library with a known vulnerability — and the thing least likely to be top of mind during the excitement of a fresh launch.

### Can I really keep building with Cursor or Lovable on a codebase someone else hardened?

Yes, provided the handover specifically addresses AI-readability: consistent naming, comments on non-obvious logic, and a clear boundary between your original frontend and the added backend infrastructure. Ask about this explicitly before the engagement closes rather than assuming it was handled by default.

### How often should I check for dependency vulnerabilities once I'm maintaining the product myself?

A monthly or quarterly automated check using your stack's built-in tool (`npm audit` or equivalent) catches most issues before they accumulate into a risky backlog. Pairing this with a simple maintenance calendar, set up at handover, turns an easy-to-forget task into a routine one.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long does a typical post-launch bug-fix warranty window actually last?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LaunchStudio's Launch Ready package includes a 48-hour post-launch support window as standard, covering anything that doesn't match what was scoped and agreed, with longer coverage available through a managed plan."
      }
    },
    {
      "@type": "Question",
      "name": "What's a fair way to resolve a disagreement about whether something is a bug or new work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Return to the original scoping document and check whether the behavior was explicitly agreed. If it was and the software doesn't match it, that's a bug; if it wasn't discussed or reflects a post-launch decision, it's new work. Agreeing on this process before the engagement starts prevents it from becoming personal later."
      }
    },
    {
      "@type": "Question",
      "name": "What's the single most important item in a handover package for a technical founder?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The dependency and third-party service inventory, because it's the item most likely to cause a real problem months later, such as an expired certificate or a deprecated API, and the least likely to be top of mind right after launch."
      }
    },
    {
      "@type": "Question",
      "name": "Can I really keep building with Cursor or Lovable on a codebase someone else hardened?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, provided the handover specifically addresses AI-readability: consistent naming, comments on non-obvious logic, and a clear boundary between the original frontend and the added backend infrastructure."
      }
    },
    {
      "@type": "Question",
      "name": "How often should I check for dependency vulnerabilities once I'm maintaining the product myself?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A monthly or quarterly automated check using your stack's built-in tool catches most issues before they accumulate, and pairing it with a simple maintenance calendar set up at handover turns an easy-to-forget task into a routine one."
      }
    }
  ]
}
</script>
