---
Title: "What to Write Down Before You Hand Your Product to Anyone"
Keywords: founder handover document, knowledge transfer before launch, business rules documentation, edge cases founder, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# What to Write Down Before You Hand Your Product to Anyone

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What to Write Down Before You Hand Your Product to Anyone",
  "description": "A template and worked example for the handover document a founder should write before an engineer, employee, or partner touches the product — covering intended behaviour, edge cases, business rules and known compromises. Helps founders decide what knowledge in their head actually needs to be on paper first.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-02-08",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/what-to-write-down-before-you-hand-your-product-to-anyone" }
}
</script>

Marit Hendriks sat at her kitchen table the night before her first engineering call, laptop open, cursor blinking in an empty document titled "notes for the call." She'd built her subscription box product, Groenteboxen, entirely in Lovable over four months of evenings. She knew, without being able to say exactly how she knew, that a paused subscription shouldn't be charged but should still count toward a loyalty discount threshold. She knew a handful of customers had been manually given a discount code that didn't exist anywhere in the system. She knew the "delivery day" field on some early accounts meant something slightly different than it did on newer ones, because she'd changed the onboarding flow in month two without migrating the old data. None of it was written down anywhere. All of it lived in her head, and only her head.

This is the most common and most avoidable cause of a slow, expensive first week on any engagement: not a technical problem, but an absent one. The founder is the only person who knows how the product is actually supposed to behave, and that knowledge has never been asked to leave their head before. Writing it down before you hand the product to anyone — an engineer, a hire, a co-founder — isn't paperwork. It's the fastest thing you can do to make everything after it faster.

## Why This Document Doesn't Already Exist

It's worth naming why almost no founder has this written, because understanding the gap makes it easier to close. When you're building solo in Lovable or Bolt, the product's rules live implicitly in a sequence of prompts and manual fixes, not in a document anyone was ever going to read. You made a hundred small decisions — what happens when a form field is left blank, what a cancelled order actually does to inventory — as you went, and each one felt too small to write down at the time. Individually, they were. Collectively, they're the actual specification of your product, and nobody but you has ever seen it in one place.

The document below isn't a technical spec — you're not describing how anything is built. It's a knowledge-transfer document: everything a competent engineer would otherwise have to discover by asking you one question at a time, spread across the first week of a build, each one a small delay.

## Section One: Intended Behaviour, in Plain Language

For each core feature, write one paragraph describing what should happen, end to end, from a user's perspective — not what currently happens in your prototype if the two differ. "When a customer places an order, they receive a confirmation email within a minute, their card is charged immediately, and the order appears in their account history with status 'processing' until it ships, at which point status changes to 'shipped' and a tracking email goes out." This sounds obvious once written. It is not obvious to someone who has never used your product and is looking at a codebase instead of your mental model.

Do this for every feature a customer directly interacts with: signup, checkout, cancellation, password reset, any core action specific to your product. Ten to fifteen short paragraphs is normal for a small SaaS or e-commerce product. This section alone typically removes half the clarifying questions an engineer would otherwise ask in week one.

## Section Two: Edge Cases You've Already Discovered

Every founder who's had even a handful of real users has already discovered edge cases the prototype doesn't handle well — a customer who tried to cancel twice, an order placed with a discount code after it expired, someone who signed up with an email they later needed to change. Write these down as they occurred, not as you wish they'd been handled: "A customer's payment failed after the confirmation email had already gone out — right now nothing catches this, and it should probably cancel the order and notify them."

This section is where founders provide the most value nobody else can, because these situations only surface through real use, and an engineer building against a clean specification will not think to ask about failure modes they don't know exist. If you have any support inbox, refund requests, or angry customer messages, they are the raw material for this section — read back through the last three months of them specifically looking for "this shouldn't have happened" moments.

## Section Three: Business Rules That Aren't Written Anywhere Else

This is the section Marit was missing, and it's usually the most consequential. Business rules are the decisions about money, access, and eligibility that a prototype implements as a side effect of how it was built, rather than as a deliberate choice — refund windows, discount stacking, what counts as an active subscriber, who can see whose data.

Write these as explicit if-then statements: "If a subscription is paused for more than 60 days, it should count as cancelled for loyalty-discount purposes, not paused." "If a customer has used a manual discount code outside the system, note it here so it isn't lost during any rebuild: [list them]." "A 'delivery day' set before March counted from order date; one set after March counts from the following Monday — these mean different things in the database even though they look the same field." That last one is exactly the kind of quiet inconsistency that causes a real, hard-to-diagnose bug three weeks after launch if it isn't flagged in advance.

## Section Four: Known Compromises and Things You Already Know Are Wrong

Every founder who's shipped something with AI tools has at least a few things they know are broken, half-built, or wrong, and have been quietly living with because fixing them wasn't urgent enough to interrupt everything else. Write these down explicitly rather than hoping nobody notices, because an engineer who discovers an undocumented compromise on their own has to stop and ask whether it's intentional — exactly the kind of blocking question covered in article 31 of this series.

"The inventory count doesn't actually decrement when an order is placed — I've been adjusting it manually every few days." "There's no real password reset flow; I've been emailing new passwords manually to the four people who've asked." "The admin dashboard shows revenue including tax, which is wrong, but I haven't had time to fix the calculation." Naming these isn't embarrassing — it's the single fastest way to convert a founder's private workaround list into a scoped, priced fix instead of a surprise discovered mid-build.

## Section Five: Who Owns What Outside the Code

A short inventory, separate from the technical handover: which email address sends customer communications and who has the login, which payment processor account is connected and under whose name, which domain registrar holds your domain, whether any manual processes (like Marit's discount codes) exist that a new system needs to account for. Article 35 in this series goes deeper into which of these should always stay in your own name specifically — this section is simply making sure nothing is missed.

## A Worked Example, Condensed

Here is roughly what one section of Marit's actual document looked like once she wrote it, the night after that blank kitchen-table document:

*Intended behaviour — pause: A customer can pause their box for up to three months. While paused, no charges occur and no boxes ship. Business rule: a pause under 60 days still counts toward the loyalty discount (5 consecutive months = 10% off); a pause over 60 days resets the counter to zero. Known compromise: currently the system doesn't distinguish these two cases — every pause resets the counter, which is wrong and has already annoyed at least two customers who complained. Edge case: one customer paused, then tried to cancel entirely while paused — the current flow doesn't allow this and silently does nothing, which looks like a bug to the user.*

Four sentences. That single paragraph would have prevented the exact clarifying-question delay Marit's actual engagement started with — because instead of the engineer discovering the counter-reset bug by testing it themselves on day three, it was already flagged, prioritised, and scoped into the quote on day one.

## What Belongs in Each Section vs. What Doesn't

A common mistake once founders understand the value of this document is trying to make it comprehensive in every direction, which turns a two-hour exercise into a two-week one that never gets finished. A few boundaries keep it useful:

Don't describe UI layout or visual design here — screenshots and a walkthrough video cover that far more efficiently than paragraphs of text, and an engineer working with your prototype's actual code can see the interface directly. Do describe what happens when a user interacts with it, especially anything that isn't visible from looking at the screen alone.

Don't try to document every possible input combination — that's what testing is for, not this document. Do document the specific edge cases real users have already hit, because those are proven to matter and won't be found by generic testing.

Don't write implementation preferences ("I think this should use a queue system") unless you have a specific reason tied to a business constraint. Do write business constraints themselves ("orders need to survive a brief payment provider outage without being lost") and let your engineering partner choose how to satisfy them.

Don't worry about organising this document beautifully. A messy list under the five headings above, written honestly, beats a polished document that took three extra evenings and left out the embarrassing parts because they felt unpolished.

## How Long This Actually Takes and What It Saves

Most founders can produce a first draft of this document in two to four hours, spread across an evening or two — noticeably less time than a single day of back-and-forth clarifying questions during an active, billable engagement. It doesn't need to be polished. Bullet points and half-sentences are fine; the goal is capturing what's in your head, not writing well.

The document also has a life beyond this one engagement: it's the same knowledge your next hire, your future co-founder, or a different engineering partner would eventually need to extract from you one conversation at a time if it isn't written down once, properly, now.

LaunchStudio asks new clients for exactly this kind of input before scoping a fixed-price quote — not because the engineers can't figure things out through questions, but because Manifera's 11+ years of client handoffs have shown that a founder's own knowledge, captured before work starts, consistently shortens the build more than any technical shortcut does. If you're preparing for your first call, [describe your project](https://launchstudio.eu/en/#contact) alongside whatever notes you've already got — even a rough version moves things faster than starting from a blank page on the call itself.

## Real example

### The Night-Before Document That Changed Marit's First Week

Marit Hendriks spent two evenings after that blank-page moment writing down everything about Groenteboxen she'd never told anyone: the loyalty-counter bug, the four customers with manual discount codes, the delivery-day field inconsistency from her March onboarding change, and a dozen smaller things she'd been quietly working around for months.

Her LaunchStudio engineer read the document before the kickoff call rather than during it. The call itself, planned for an hour, took twenty-five minutes — mostly confirming priorities rather than extracting facts, because the facts were already on paper. The loyalty-counter bug and the delivery-day inconsistency both turned out to affect the database migration already planned for payments hardening, so they were folded into the same piece of work rather than discovered separately later and requiring a second pass.

**Result:** what Marit had budgeted as a two-and-a-half-week engagement, expecting the usual back-and-forth, finished in nine business days — largely because the first three days, typically spent on discovery questions, had already been answered on paper before the engineer started.

> *"I thought I was writing notes for myself. I was actually writing the thing that made the whole engagement fast. I wish I'd known that four months earlier."*
> — **Marit Hendriks, Founder, Groenteboxen**

**Cost & Timeline:** €2,200 (Launch & Grow Package) — live in 9 business days.

## Frequently Asked Questions

### Do I need to write this before getting a quote, or can it wait until after I've signed on?

Before, if possible — even a rough draft. A scoping conversation grounded in a real document produces a more accurate quote than one built on questions alone, because compromises and edge cases you'd otherwise mention halfway through the build get priced in from the start instead of arriving as scope surprises.

### What if I genuinely don't remember all the small decisions I made while building?

Write what you remember now, and add to it as things occur to you over the following days — this document is never really finished. Your support inbox, old customer emails, and any manual workaround spreadsheet you keep are good prompts for the things you've forgotten you know.

### Should this document be technical, or is plain language actually fine?

Plain language is not just fine, it's preferred. You're describing what should happen and why, not how to build it. Translating your plain-language rules into technical implementation is exactly the part your engineering partner is equipped to do.

### Isn't this basically the same as a product requirements document?

It overlaps, but it's narrower and more personal — a PRD usually describes what to build going forward, while this document captures what's already true (or already broken) about what exists, including compromises you'd never put in a forward-looking spec because they're embarrassing rather than aspirational.

### Who should have access to this document after the handover is complete?

Keep it as a living reference for yourself and anyone who joins your team with product responsibility — a new hire, a co-founder, a future engineering partner. It's one of the few artefacts that keeps paying off well past the engagement it was written for.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Do I need to write this before getting a quote, or can it wait until after I've signed on?", "acceptedAnswer": { "@type": "Answer", "text": "Before, if possible, even a rough draft. A scoping conversation grounded in a real document produces a more accurate quote, because compromises and edge cases get priced in from the start instead of arriving as scope surprises." } },
    { "@type": "Question", "name": "What if I genuinely don't remember all the small decisions I made while building?", "acceptedAnswer": { "@type": "Answer", "text": "Write what you remember now and add to it as things occur to you. Your support inbox, old customer emails, and any manual workaround spreadsheet are good prompts for things you've forgotten you know." } },
    { "@type": "Question", "name": "Should this document be technical, or is plain language actually fine?", "acceptedAnswer": { "@type": "Answer", "text": "Plain language is preferred. You're describing what should happen and why, not how to build it — translating your rules into implementation is exactly the part your engineering partner is equipped to do." } },
    { "@type": "Question", "name": "Isn't this basically the same as a product requirements document?", "acceptedAnswer": { "@type": "Answer", "text": "It overlaps but is narrower and more personal. A PRD usually describes what to build going forward, while this document captures what's already true or already broken about what exists, including compromises you wouldn't put in a forward-looking spec." } },
    { "@type": "Question", "name": "Who should have access to this document after the handover is complete?", "acceptedAnswer": { "@type": "Answer", "text": "Keep it as a living reference for yourself and anyone who joins with product responsibility — a new hire, a co-founder, or a future engineering partner. It keeps paying off well past the engagement it was written for." } }
  ]
}
</script>
