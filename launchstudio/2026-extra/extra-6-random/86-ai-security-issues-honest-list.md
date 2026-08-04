---
Title: "A Non-Exhaustive (But Honest) List of AI Security Issues We Keep Finding"
Keywords: ai security issues, ai generated code vulnerabilities, common ai app security gaps, ai coding security review
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# A Non-Exhaustive (But Honest) List of AI Security Issues We Keep Finding

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "A Non-Exhaustive (But Honest) List of AI Security Issues We Keep Finding",
  "description": "These are the AI security issues that show up most often in our reviews of AI-generated apps — not a hypothetical list, but the recurring ones we actually find week after week.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-security-issues-honest-list" }
}
</script>

We're not going to pretend this list is comprehensive, and we're not going to pretend every AI-generated app has every item on it. What we can say honestly is that these are the AI security issues that show up over and over, across different founders, different AI tools, and different product categories, often more than one at a time in the same codebase. This isn't a hypothetical worst-case list. It's closer to a field report.

## The recurring ones

**An exposed admin route.** Nearly every app with an admin panel or internal dashboard has, at some point, an admin URL that's reachable simply by knowing or guessing it exists — `/admin`, `/dashboard/internal`, something similarly guessable — with no check confirming the visitor is actually an administrator. AI tools build the admin panel because you asked for one. They don't automatically lock the door behind it unless the prompt specifically asked for that too.

**A public storage bucket.** File uploads — profile photos, documents, exported reports — usually get stored somewhere, and AI-assisted setups frequently default that storage to publicly readable, because a public bucket is the fastest configuration to get images loading in a demo. Nobody circles back to make it private once the demo works, because nothing flags it as a problem until someone finds a way to browse the bucket directly and sees every file that's ever been uploaded.

**A webhook with no signature verification.** Payment processors, email services, and most third-party integrations send webhooks — background notifications your server is supposed to trust and act on. Verifying that a webhook actually came from the service it claims to be from requires checking a cryptographic signature included in the request. AI-generated webhook handlers routinely process incoming requests without ever checking that signature, which means anyone who knows or guesses your webhook URL can send fake events your server will treat as real.

**Client-side-only validation.** A form that checks "is this email valid" or "is this discount code real" purely in the browser, with no matching check on the server, looks correct in every normal use case and is trivially bypassed by anyone who sends the request directly instead of through your form.

**Secrets committed into the repository itself.** API keys, database credentials, and similar secrets sometimes end up hardcoded directly into the AI-generated code rather than stored in environment variables, which means anyone with access to the codebase — including, eventually, anyone it gets shared with — has the keys too.

**Missing rate limiting on sensitive endpoints.** Login forms, password reset flows, and signup endpoints without any limit on how many attempts a single source can make in a short window are open invitations for automated guessing, and AI-generated auth flows rarely include this by default.

## Why these specific ones, and not others

These six aren't the only issues that exist, but they share a pattern worth naming: each one is invisible in normal use. A public storage bucket looks identical to a private one until someone tries to access it directly. An unverified webhook processes real events perfectly well right up until someone sends a fake one. That's precisely why they survive so long in AI-generated products — nothing about day-to-day operation reveals them, and AI coding tools optimize for "does this work as demoed," not "does this resist someone actively trying to misuse it."

LaunchStudio is powered by Manifera, a software development company with 11+ years of experience, and our engineers, including the team based in Singapore, run this same recurring checklist against every AI-generated codebase that comes through review — not because we expect to find all six every time, but because we've learned not to be surprised when we do. If you'd like a straightforward pass against this exact list on your own product, you can [send us your prototype link for free advice](https://launchstudio.eu/en/#contact) on which of these, if any, apply to you. Manifera's broader security and engineering standards are described on its [custom software development page](https://www.manifera.com/services/custom-software-development/).

## How to Triage This List When You Can't Fix Everything at Once

Finding two or three items from this list in the same review, which happens more often than not, raises an immediate practical question: which one gets fixed first when you can't fix all of them today? Three criteria, applied in order, produce a reasonable answer without needing to treat every item as equally urgent.

**First: is it reachable without any credentials at all?** An exposed admin route, a public storage bucket, and an unverified webhook all share this property — anyone on the internet can hit them without ever logging in. Missing rate limiting and client-side-only validation, by contrast, usually require the attacker to already be interacting with your app in a normal way, which is a real risk but a narrower one. Unauthenticated exposure moves to the front of the line first, because the pool of people who could stumble onto it or find it deliberately is effectively unlimited.

**Second: what does it actually expose or allow?** Within the unauthenticated group, rank by consequence. A public storage bucket exposing customer-uploaded documents or photos is worse than one holding only generic marketing assets. An unverified webhook that can trigger a state change — marking an order paid, granting access — is worse than one that only logs an event nobody acts on. This step requires actually knowing what each gap touches in your specific product, not applying a generic severity label from a list like this one.

**Third: how long does the fix actually take?** Among items of similar severity, the quicker fix goes first, purely because it removes risk sooner. Committed secrets typically require rotating the exposed credential and confirming nothing was accessed with it in the meantime — usually a same-day fix. A public storage bucket usually takes about as long. An exposed admin route needs an actual authorization check added and tested, which can take longer depending on how your permission system is structured elsewhere. Sequencing the fast, high-severity fixes first buys time to do the slower ones properly rather than rushing all of them at once.

A rough default ordering, when nothing about your specific product argues otherwise: committed secrets and public buckets first, since they're both fast to close and both unauthenticated; unverified webhooks and exposed admin routes next, since they take a bit more care to fix correctly; rate limiting and client-side validation gaps last, not because they don't matter, but because they generally require an attacker already engaging with your product rather than simply finding an open door. This ordering is a starting point, not a substitute for knowing what each specific gap touches in your own app — but it beats fixing whichever one you noticed first.

## Real example

### An AI-Native Founder in Action: three issues in one review

Iris Voorschoten, a founder in Voorschoten, built "MeldGrip" — a facilities-issue reporting tool for property managers — using Lovable. The app worked well for its pilot users: staff could report a broken light or a leaking pipe, and managers could track resolution. Iris hadn't had any security review done, mostly because nothing about the app's day-to-day use suggested a problem.

A LaunchStudio review of MeldGrip, done ahead of a larger rollout Iris was planning, turned up three of the recurring issues on this exact list, all at once. The admin route that let property managers see all reported issues across buildings was reachable without any check confirming the visitor was actually a manager. The storage bucket holding photos of reported facility issues — some showing building interiors and unit numbers — was configured to be publicly readable. And the webhook that received notifications from Iris's SMS provider had no signature verification, meaning anyone who found the webhook URL could send fake "issue reported" events into the system.

None of the three had caused a visible problem yet. All three were the kind of gap that stays invisible until someone actively looks for it, or actively exploits it. LaunchStudio's engineers locked down the admin route with a proper role check, switched the storage bucket to private with signed, time-limited access links, and added signature verification to the SMS webhook handler.

**Result:** MeldGrip passed its pre-rollout review with all three issues closed before the wider release Iris had planned.

> *"None of these would have shown up in normal use. That's exactly what scared me once I understood it."*
> — **Iris Voorschoten, Founder, MeldGrip (Voorschoten)**

**Cost & Timeline:** €900 (three-issue remediation across admin access, storage, and webhook security) — completed in 3 business days.

---

## Frequently Asked Questions

### How common are these AI security issues, realistically?

Very common — in our experience reviewing AI-generated codebases, it's unusual to find none of the items on this list, and finding two or three together, as with MeldGrip, isn't rare either.

### Can I check for an exposed admin route myself without technical skills?

You can try navigating directly to common admin paths while logged out, but a proper check requires reviewing the server-side code to confirm access control exists, which is best done by an engineer.

### Why would an AI tool build a public storage bucket by default?

Because a public bucket is the fastest configuration to get uploaded files loading and visible in a demo, and switching it to private with proper access controls is an extra step nothing prompts the tool to take automatically.

### What does "webhook signature verification" actually protect against?

It confirms an incoming request genuinely came from the service it claims to be from — without it, anyone who knows your webhook URL can send fabricated events your server will treat as real.

### Does Manifera's Singapore team review for all of these issues in a standard pass?

Yes — this recurring list reflects exactly the checks our engineers, including the Singapore-based team, run as a standard part of any AI-generated codebase review.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "How common are these AI security issues, realistically?", "acceptedAnswer": { "@type": "Answer", "text": "Very common — it's unusual for a review of an AI-generated codebase to find none of these, and finding two or three together isn't rare." } },
    { "@type": "Question", "name": "Can I check for an exposed admin route myself without technical skills?", "acceptedAnswer": { "@type": "Answer", "text": "You can try navigating to common admin paths while logged out, but a proper check requires reviewing server-side access control code, best done by an engineer." } },
    { "@type": "Question", "name": "Why would an AI tool build a public storage bucket by default?", "acceptedAnswer": { "@type": "Answer", "text": "A public bucket is the fastest configuration to get uploaded files displaying in a demo, and switching it to private is an extra step nothing prompts automatically." } },
    { "@type": "Question", "name": "What does webhook signature verification actually protect against?", "acceptedAnswer": { "@type": "Answer", "text": "It confirms an incoming request genuinely came from the claimed service; without it, anyone who knows the webhook URL can send fabricated events treated as real." } },
    { "@type": "Question", "name": "Does Manifera's Singapore team review for all of these issues in a standard pass?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, this recurring list reflects the checks Manifera's engineers, including the Singapore-based team, run as standard on AI-generated codebases." } }
  ]
}
</script>
