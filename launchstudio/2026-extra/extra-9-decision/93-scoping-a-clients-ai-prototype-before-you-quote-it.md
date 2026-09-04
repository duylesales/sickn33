---
Title: "Scoping a Client's AI Prototype Before You Quote It"
Keywords: scoping AI prototype, Lovable prototype audit, Bolt app scope checklist, technical due diligence agency, quoting client dev work, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Agency / Freelancer (White-Label Partner)
---

# Scoping a Client's AI Prototype Before You Quote It

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Scoping a Client's AI Prototype Before You Quote It",
  "description": "Quoting a client's Lovable or Bolt prototype without a structured scoping pass is how agencies end up underwater on fixed-price engagements. A concrete checklist to run before you commit to a number.",
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
  "datePublished": "2027-01-08",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/scoping-a-clients-ai-prototype-before-you-quote-it"
  }
}
</script>

The client's Lovable link arrives in your inbox at 4:50pm on a Thursday, with a message that reads "can you have a number for me by Monday?" You open it. The demo looks genuinely good — clean UI, a working signup flow, a dashboard that populates with real-looking data. Forty minutes later you close the tab having quoted nothing, because forty minutes was enough to notice that the "working" signup flow doesn't actually verify email ownership, the dashboard data is hardcoded rather than pulled from a real query in three of five places, and there's no visible database schema behind any of it that you can find without repo access. The demo told you what the client sees. It told you almost nothing about what you'd actually be quoting.

This is the gap that catches agencies on fixed-price white-label work more than any other single factor: quoting off the demo instead of off a structured scoping pass, because the demo is what's in front of you and a proper scope takes an hour you don't feel like you have on a Thursday afternoon. The agencies that stop losing money on these engagements are the ones that build the hour into every quote request as a non-negotiable step, not an optional nicety.

## Why the Demo Lies to You, Specifically

An AI-generated prototype is built to demo well, because demoing well is what the founder was optimizing for while building it — that's not a criticism, it's simply the incentive structure of building fast with tools like Lovable, Bolt, or v0. The visible layer, what a client clicks through in a five-minute walkthrough, is frequently the most finished part of the whole build, while the parts that don't show up in a demo — server-side permission checks, data validation, error handling for the cases users don't hit on a clean first try, whether the database schema can actually support real concurrent usage — are often thin or entirely absent. This is the specific pattern behind the widely cited finding that a large share of AI-generated code carries real security vulnerabilities: the gaps aren't visible in a walkthrough because they're gaps in exactly the layer a walkthrough doesn't test.

Quoting off the demo means quoting off the 20% of the build that's actually finished, then discovering the other 80% mid-engagement, at a fixed price you already committed to. This is the single most common way a "fixed-price" white-label engagement stops being fixed-price in practice, absorbed as unbilled overtime that erodes exactly the margin your pricing model was supposed to protect.

## The Scoping Checklist: What to Actually Check Before Quoting

Run this in order, and treat any "no" or "unclear" answer as a scope-widening signal, not a minor detail to resolve later.

**Authentication, actually tested.** Does signup verify email ownership, or does it just accept any string as an email? Is there a working password reset flow, or a placeholder button that goes nowhere? Try creating two accounts and confirm they're actually isolated from each other's data — a shockingly common gap is a dashboard that shows the same seed data to every logged-in user regardless of account.

**Server-side permission checks, not just UI hiding.** A prototype that hides an admin panel from regular users in the interface is not the same as a prototype that blocks regular users from reaching that panel's underlying API endpoints directly. Check this by trying to access an obviously-restricted URL directly, logged in as a non-admin account — if it loads, the permission model exists only in the frontend, which means it doesn't exist at all from a security standpoint.

**Database schema and data integrity.** Ask for read access to the database (Supabase, Firebase, or whatever backend the tool generated) and look for actual relational structure versus a flat, denormalized dump of whatever the AI tool defaulted to. Confirm whether data persists correctly across sessions and whether concurrent writes — two users editing related data at once — would produce sensible results or silently corrupt something.

**Payment readiness, if applicable.** Is there a real Stripe or Mollie integration processing test transactions, or a UI mockup of a checkout flow with no backend behind it? This distinction alone can shift a quote by thousands of euros, since building real payment logic from nothing is a materially different scope than hardening an existing integration.

**What's hardcoded versus what's real.** Click through every screen that shows data and ask, for each one, "if I refreshed this after changing the underlying data, would it update?" AI tools frequently leave placeholder or seed data wired into components that look dynamic but aren't, and a client demoing their own product often doesn't know the difference because it's never occurred to them to check.

**Third-party service configuration.** Check whether API keys, environment variables, and service connections (email sending, file storage, external APIs) are properly configured for a production environment or are development/sandbox credentials that would need to be rebuilt entirely for a real launch — this is invisible in a demo and can represent a full day of otherwise-unscoped work.

**What the client actually has access to.** Confirm the client owns the accounts — the Lovable or Bolt project, the hosting, any connected services — rather than having built on a shared or trial account that would need migrating before any real work could start. Migration work is real scope that's easy to miss entirely if you don't ask the question directly.

## Translating What You Find Into a Number

Each gap on the checklist above maps to a rough scope category, and running the checklist gives you the inputs to place the engagement correctly rather than guessing. A prototype with real authentication, real data persistence, and just missing payments and hosting hardening sits comfortably in the €800–€3,500 Launch Ready range. A prototype with UI-only permission checks, hardcoded data throughout, and no real backend logic behind several core flows is a materially larger build, likely landing in the €2,500–€7,500 Launch & Grow range or beyond — and knowing that distinction before you quote, rather than discovering it in week two, is the entire value of the scoping pass.

It's worth communicating this back to the client honestly rather than absorbing the surprise silently: "the signup and dashboard look finished, and they are — but the payment flow and the admin permissions need to be built essentially from scratch, which is a bigger piece of work than the demo suggests" is a sentence that costs you nothing to say and saves you from a fixed-price commitment built on incomplete information.

## Red Flags That Multiply the Scope, Not Just Add to It

Some findings on the checklist add a known, boundable chunk of work to the quote — a missing Stripe integration is a defined piece of scope with a fairly predictable cost. Others are worse than they first look, because they signal that the entire underlying build needs re-examining rather than just the specific feature you happened to test. Treat these as multipliers, not line items, when you find them.

The first is inconsistent patterns across similar features — if the signup flow has real server-side validation but the password reset flow doesn't, that's not one gap, it's a signal that the AI tool (or the founder prompting it) wasn't applying a consistent standard, which means every other similar feature needs the same scrutiny rather than being assumed fine by association. The second is a founder who can't answer basic questions about their own data model — not because they're unintelligent, but because they generated the schema through prompts without reviewing it, which means the schema itself may contain structural decisions nobody actually chose deliberately, and untangling accidental structure is slower than building intended structure from a clear spec. The third is any sign the prototype was built across multiple tools or in disconnected sessions — a Lovable frontend bolted onto a Bolt-originated backend, or evidence of the founder switching tools mid-build — because integration seams between tools generated independently are exactly where the checklist's individual items stop predicting total effort accurately; the sum of the parts undercounts the cost of gluing them together correctly.

When you spot a multiplier rather than a line item, say so plainly in your scoping notes and build contingency into the quote rather than treating it as one more item on an additive list — a client who understands why the number moved from "roughly what I expected" to "notably higher" because of a structural issue is far easier to keep than one blindsided by a mid-project scope conversation they were never prepared for.

## Documenting Findings So the Quote Explains Itself

The scoping pass has a second purpose beyond sizing the engagement correctly: it produces the specific language you'll use to justify the number to the client, which matters because "it's more complicated than it looked" is a weak sentence and "the payment flow you saw in the demo isn't connected to a real processor yet, and the admin data-export feature has no access control at all" is a strong one. Write down what you actually found, in plain non-technical language, as you go through the checklist rather than trying to reconstruct it from memory when the client asks why the number is what it is. This documentation becomes the backbone of the proposal's scope section and, just as usefully, becomes the reference point if the client later suggests the engagement is taking longer than it should — you have a specific, dated record of what was actually there at the start, rather than a fading memory of a Thursday-afternoon demo call.

## Who Actually Runs the Scoping Pass

For agencies without in-house technical capability, this checklist is exactly the kind of pass worth handing to a technical partner before committing to a client number rather than attempting it with limited technical fluency and hoping nothing important gets missed — the difference between a founder-level walkthrough and an engineer actually opening the repo and testing the permission model directly is the difference between a guess and a scope. A short paid scoping call with a partner like LaunchStudio, run before you quote rather than after you've committed, costs a fraction of what an underscoped fixed-price engagement costs in absorbed overtime, and it gives you a defensible, specific number to bring back to the client instead of a gut-feel figure padded for uncertainty you can't actually name.

[LaunchStudio](https://launchstudio.eu/en/) runs exactly this kind of scoping pass as the first step of every engagement, backed by [Manifera's 11+ years turning AI-generated prototypes into production systems](https://www.manifera.com/about-us/manifera-technologies/) — which means the checklist above isn't theoretical, it's the actual pass a Manifera engineer runs before any fixed-price quote goes out.

Send us the prototype link before you quote your client — [free scoping feedback within one business day](https://launchstudio.eu/en/#contact), so your number is built on what's actually there instead of what the demo made it look like.

## Real example

### An Agency Partner in Action: The Quote That Nearly Went Out Wrong

Sanne Bakker, who runs a small digital studio in Groningen, was about to quote a client's Bolt-built subscription box platform at €1,800 — a number based on a fifteen-minute demo walkthrough that looked essentially finished — before deciding to send the link to LaunchStudio for a scoping pass first, mostly to double-check her own instinct.

The scoping call surfaced that the subscription billing shown in the demo was a UI mockup with no real Stripe integration behind it, and that the admin dashboard's data-export feature, which the client had specifically called out as important for launch, had no server-side permission check at all — any logged-in user could hit the export endpoint directly and pull every customer's data.

**Result:** Sanne requoted at €4,200, explaining the specific gaps to her client in plain terms rather than absorbing the difference or walking away from the deal, and the client — relieved to understand what was actually being fixed — approved the revised number without pushback, since a security gap that serious was self-evidently worth addressing properly.

> *"If I'd quoted off the demo, I'd have eaten €2,400 in unplanned work or told my client mid-project that the price was going up. Neither of those conversations is one I want to have."*
> — **Sanne Bakker, Founder, Studio Bakker (Groningen)**

## Frequently Asked Questions

### How long should a proper scoping pass actually take?

A focused scoping pass, checking authentication, permissions, data integrity, and payment readiness, typically takes thirty to ninety minutes for someone with the technical access and fluency to test it directly — considerably longer for someone without repo access or backend familiarity, which is exactly why many agencies hand this step to a technical partner.

### What if the client won't grant repo or backend access before I quote?

Treat this as a genuine warning sign rather than a minor inconvenience — a client unwilling to share the access needed to scope the work accurately either doesn't trust the relationship yet or doesn't fully understand what a real quote requires, and either way you're being asked to commit to a fixed price on incomplete information.

### Can I run this checklist myself without technical background?

Some items, like clicking through screens to spot hardcoded data or asking direct questions about payment integration status, are accessible without deep technical skill. Others, like checking server-side permission enforcement or reviewing database schema, genuinely require someone who can read the backend directly.

### How much should a scoping pass cost, and who pays for it?

Many technical partners, including LaunchStudio, offer an initial scoping review at no cost as part of the quoting process, since it's also how the partner determines their own fixed-price number. For larger or more ambiguous prototypes, a paid scoping engagement is reasonable and should be treated as a small, separate line item from the main build.

### What's the single biggest scoping mistake agencies make?

Quoting off a client demo walkthrough instead of an actual technical review — the demo shows the 20% of a prototype built to look finished, and the fixed price gets committed before anyone has checked the 80% that doesn't show up in a five-minute click-through.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long should a proper scoping pass actually take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A focused scoping pass checking authentication, permissions, data integrity, and payment readiness typically takes thirty to ninety minutes for someone with technical access and fluency to test it directly."
      }
    },
    {
      "@type": "Question",
      "name": "What if the client won't grant repo or backend access before I quote?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Treat this as a genuine warning sign. A client unwilling to share the access needed to scope the work accurately is asking you to commit to a fixed price on incomplete information."
      }
    },
    {
      "@type": "Question",
      "name": "Can I run this checklist myself without technical background?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Some items like spotting hardcoded data are accessible without deep technical skill. Others, like checking server-side permission enforcement or database schema, genuinely require someone who can read the backend directly."
      }
    },
    {
      "@type": "Question",
      "name": "How much should a scoping pass cost, and who pays for it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Many technical partners offer an initial scoping review at no cost as part of quoting. For larger or ambiguous prototypes, a paid scoping engagement is reasonable and should be a small, separate line item."
      }
    },
    {
      "@type": "Question",
      "name": "What's the single biggest scoping mistake agencies make?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Quoting off a client demo walkthrough instead of an actual technical review. The demo shows the finished-looking layer while the fixed price gets committed before anyone checks what's underneath."
      }
    }
  ]
}
</script>
