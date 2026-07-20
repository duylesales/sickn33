---
Title: "Your AI Database Isn't as Persistent as It Looks in the Demo"
Keywords: ai database, ai native, ai coding, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# Your AI Database Isn't as Persistent as It Looks in the Demo

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Your AI Database Isn't as Persistent as It Looks in the Demo",
  "description": "A working AI database in a demo and a production-ready one are not the same claim. A before/after look at what changes between the two, and why rate limiting is often the first thing missing.",
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
  "datePublished": "2026-07-21",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/your-ai-database-isnt-as-persistent-as-it-looks-in-demo"
  }
}
</script>

It's a reasonable assumption: if your AI database is saving and retrieving data correctly in every test you run, it's working. The trouble is that "working" during a founder's own careful, low-volume testing and "working" under real, unpredictable user traffic are two very different claims, and the gap between them tends to show up first at exactly the endpoints nobody demos on purpose — the ones that only get exercised when something goes wrong, or when someone deliberately tries to make something go wrong.

## Before: What the Demo Actually Proves

**Before production hardening,** a typical AI-generated backend correctly reads and writes records, handles the expected happy-path requests, and returns sensible data when tested exactly as designed, exactly as many times as a founder patiently clicks through it themselves. What it usually hasn't been tested against: repeated rapid requests to the same sensitive endpoint, malformed or deliberately malicious input, concurrent writes to the same record from two different sessions, or a genuine attacker deliberately probing a specific weak point rather than using the product as intended. None of these scenarios naturally arise from a founder testing their own product carefully and cooperatively.

## After: What a Production-Ready Database Layer Adds

**After hardening,** the same database layer includes rate limiting on sensitive endpoints — password resets, login attempts, any action that could be scripted and abused at volume — input validation rejecting malformed or malicious data before it ever reaches a query, and monitoring that flags unusual request patterns rather than silently absorbing them into the logs unnoticed. It also typically includes safeguards against concurrent write conflicts, so two near-simultaneous updates to the same record don't silently overwrite one another without either party knowing.

## Why Rate Limiting Specifically Gets Missed

Rate limiting has no visible effect during normal use — a founder testing their own password reset flow once or twice never notices its absence, because nothing about a single legitimate request looks any different with or without a limit in place. It only matters the moment someone, or some automated script, sends that same request hundreds or thousands of times in a short window, which a demo, by definition, never does, and which most AI coding assistants have no particular reason to add unless specifically asked.

## The Quiet Cost of Discovering This After the Fact

Unlike a visible bug, a missing rate limit or validation check doesn't announce itself with an error message. It tends to surface instead as an unexplained spike in a hosting bill, a flood of junk records in a database table, or a customer support inquiry about an account that was never actually created by its supposed owner — each one a downstream symptom of the same missing, upstream safeguard.

## What Closing This Gap Actually Involves

Adding rate limiting and abuse protection to sensitive endpoints is a targeted, additive change — it doesn't touch your product's core logic or its frontend, it wraps the entry points that matter with the constraints a real, adversarial internet actually requires. [LaunchStudio](https://launchstudio.eu/en/) includes exactly this kind of database and endpoint hardening in its standard production-readiness review, backed by Manifera's 11+ years of experience with PostgreSQL, Supabase, and Firebase-backed production systems.

Manifera's engineering team, based primarily out of its development center on Pho Quang Street in Ho Chi Minh City, has applied this same hardening pattern across 160+ delivered projects for clients ranging from Vodafone to smaller AI-native founders working with LaunchStudio directly.

[Calculate what your project costs with our calculator](https://launchstudio.eu/en/#calculator).

## Real example

### An AI-Native Founder in Action: The Password Reset That Never Slept

Bram, a former HR coordinator turned founder in Eindhoven, built OnboardIQ, an AI-assisted employee onboarding platform, using Cursor, launched to a handful of small businesses managing new-hire paperwork through the platform.

A month in, Bram noticed his email-sending costs had spiked overnight. His logs showed tens of thousands of password reset emails triggered against a single account within hours — not a targeted attack, but an automated bot scanning for exactly this kind of unprotected endpoint. LaunchStudio's review confirmed the endpoint had no rate limiting whatsoever.

**Result:** LaunchStudio added rate limiting to the password reset endpoint and every other sensitive, unauthenticated route, alongside basic abuse-pattern monitoring, closing the gap without touching OnboardIQ's onboarding logic.

> *"I didn't even know 'rate limiting' was a thing I needed until it cost me money overnight."*
> — **Bram Willemsen, Founder, OnboardIQ (Eindhoven)**

**Cost & Timeline:** €1,150 (endpoint hardening and rate limiting) — completed in 4 business days.

---

## Frequently Asked Questions

### An infrastructure engineer might say this is a "hosting problem," not a "code problem" — which is it, really?

It's neither cleanly — hosting providers can offer network-level protections, but the specific logic of what counts as reasonable versus abusive use of a password reset endpoint has to be defined in the application itself, which is a code and product decision, not something a hosting plan handles automatically.

### Does this same exposure risk apply to apps with very few users, or only ones with meaningful traffic?

It applies from day one, regardless of traffic — as Bram's case shows, the bots that find unprotected endpoints aren't targeting popular apps specifically, they're scanning broadly for the pattern itself, so a brand-new app with ten users is exactly as exposed as one with ten thousand.

### Manifera has built systems handling far larger data volumes than a typical founder's prototype — does that experience actually transfer to smaller-scale fixes like Bram's?

Yes, in the sense that matters most — the specific technique (rate limiting, input validation, concurrency-safe writes) doesn't change with scale, only the volume it's tested against; applying enterprise-grade patterns at founder scale is a large part of what LaunchStudio was built to do.

### Herre Roelevink has spoken about founders needing architecture more than raw code output at this stage — is a missing rate limit really an "architecture" issue?

Yes — it's a decision about how the system as a whole handles a category of request, not a single line of broken logic, which is precisely the kind of structural, easy-to-overlook decision Roelevink's framing of "architecture over code" is describing.

### If a founder fixes this themselves after reading an article like this, is there still value in a professional review?

Possibly not, if the founder has the technical background to implement and correctly test rate limiting themselves — LaunchStudio exists specifically for the founders who don't have that background or the time to acquire it safely before launch.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is a missing rate limit a hosting problem or a code problem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Neither cleanly — the application itself has to define what counts as abusive use, which hosting alone doesn't handle."
      }
    },
    {
      "@type": "Question",
      "name": "Does this exposure risk apply to low-traffic apps too?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, from day one — automated bots scan broadly for the pattern rather than targeting popular apps specifically."
      }
    },
    {
      "@type": "Question",
      "name": "Does experience with larger data volumes transfer to smaller-scale fixes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, the specific technique doesn't change with scale, only the volume it's tested against."
      }
    },
    {
      "@type": "Question",
      "name": "Is a missing rate limit really an architecture issue?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, it's a decision about how the whole system handles a category of request, not a single broken line of logic."
      }
    },
    {
      "@type": "Question",
      "name": "Is a professional review still worth it if a founder can fix this themselves?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Possibly not with the right technical background — the service exists for founders who lack that background or the time."
      }
    }
  ]
}
</script>
