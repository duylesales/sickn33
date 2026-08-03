---
Title: "AI Software Engineering Principles Your Prototype Skipped"
Keywords: ai software engineering, ai coding, ai native, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI Software Engineering Principles Your Prototype Skipped

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Software Engineering Principles Your Prototype Skipped",
  "description": "A production-readiness checklist framed around classic software engineering principles that AI coding tools don't automatically apply, with a specific focus on input validation and price manipulation.",
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
    "@id": "https://launchstudio.eu/en/blog/ai-software-engineering-principles-your-prototype-skipped"
  }
}
</script>

Traditional software engineering has always rested on a handful of unglamorous principles: never trust client input, validate at every boundary, assume the network is unreliable. AI software engineering, as practiced through prompting and generation, tends to skip straight to functionality — because none of those principles are visible in a working demo, and nobody explicitly asked the tool to apply them.

## Principle One: Never Trust Data Coming From the Client

**Check:** does your server independently validate every value submitted from the frontend, or does it assume the frontend already enforced the rules (minimum order quantity, valid price range, required fields) before the request arrived? AI-generated forms frequently enforce these rules beautifully in the UI while never re-checking them once the data reaches the server — meaning anyone bypassing the UI entirely can submit whatever they want.

## Principle Two: Assume Every Numeric Input Can Be Manipulated

**Check:** can a quantity field, a price field, or a discount field accept a negative number, a zero, or an unreasonably large value without the server rejecting it? A negative quantity on an order, for instance, can sometimes be processed as a valid transaction by backend logic that was only ever tested with positive, reasonable values — occasionally resulting in a calculated total that works in the requester's favor rather than the business's. This isn't a hypothetical edge case dreamed up for the sake of a checklist — it's precisely the mechanism behind Niels's MakerLink incident, where a quantity field multiplied by a per-unit price produced a negative total, and that negative total, run through payment logic that only expected a value moving in one direction, was processed as a credit to the customer's account rather than a charge against it. The underlying arithmetic was completely correct; nobody had ever told it that a negative quantity shouldn't be allowed to reach that arithmetic in the first place.

## Principle Three: Validate at Every Boundary, Not Just the First One

**Check:** if your application has multiple entry points to the same underlying data — a web form, a public API, a bulk-import feature — is validation applied consistently across all of them, or only at the one entry point a founder happened to test most thoroughly? A validation rule enforced on the main form but forgotten on a secondary API endpoint offers no real protection at all, since the secondary endpoint becomes the obvious way around it.

## Principle Four: Design for the Malformed Request, Not Just the Expected One

**Check:** what does your application do when it receives a request that doesn't match any input a founder anticipated — a string where a number was expected, a missing required field, an extra unexpected parameter? Applications tested only against expected input often respond to malformed input in undefined, occasionally exploitable ways, rather than cleanly rejecting it with a clear error.

## Principle Five: Treat Server-Side Validation as Non-Negotiable, Not Redundant

**Check:** is there a temptation to skip server-side validation because "the frontend already checks it"? That temptation is understandable and extremely common in AI-generated code, since duplicating validation logic in two places feels redundant during development — but the frontend check and the backend check are answering two different questions, and only the backend one is actually enforceable against a determined user.

## A Quick Self-Test: Five Requests Worth Trying Against Your Own Application

Input validation gaps are unusually easy for a founder to test for directly, without reading a line of code, because the test is simply "try submitting something unreasonable and see what happens." None of these require technical skill — they require a specific, adversarial mindset most functional testing skips entirely.

**Five things worth trying on any form involving a number:**

1. **A negative number** where only positive values make sense — a quantity, a duration, a rating. A well-validated field rejects it outright; a poorly validated one may process it and produce a nonsensical or exploitable result.
2. **Zero**, where zero is a logically odd or meaningless value — a zero-quantity order, a zero-night booking. Some applications handle this gracefully; others produce a calculation error or an unintended free result.
3. **An enormous number** — nine digits instead of one or two — in a field expecting a normal, small value. This can occasionally trigger overflow behavior, or simply reveal that no upper bound was ever considered.
4. **A decimal where a whole number is expected**, or text where a number is expected. A field that silently accepts "3.7 units" of something that can only reasonably exist in whole units, or that errors in a confusing, unhelpful way rather than a clean rejection, is a sign validation wasn't specifically considered for that field.
5. **The same form submitted twice in quick succession** — double-clicking a "place order" or "submit payment" button. Without protection against duplicate submission, this can sometimes create two records, two charges, or two of whatever the form was meant to create exactly once.

**What to do with what you find:** none of these tests, on their own, tell you how to fix the underlying issue safely — that still requires someone who can implement server-side validation correctly, test it against every entry point (not just the form you tried it on), and confirm the fix doesn't break legitimate edge cases like a genuinely large but valid order. But running through this five-item list yourself, on your own product, before a conversation with an engineer, turns a vague "can you check if my validation is okay" into a specific "here's what I found when I tried X, Y, and Z" — which tends to make the resulting review faster and more precisely scoped from the very first call.

## What Closing These Gaps Looks Like in Practice

A thorough validation pass applies consistent, server-side rules across every entry point a system exposes, catching malformed and adversarial input before it reaches business logic. [LaunchStudio](https://launchstudio.eu/en/) runs exactly this kind of validation audit as part of its standard review, backed by Manifera's 11+ years of enterprise software engineering discipline applied to founder-scale products.

Manifera's validation and hardening work is carried out primarily through its Ho Chi Minh City development center on Pho Quang Street, with client scoping conversations run through the Amsterdam office at Herengracht 420.

[Talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: The Order That Paid the Customer Instead

Niels, a former print-shop manager turned founder in Nijmegen, built MakerLink, an AI-assisted freelance marketplace connecting small manufacturers with custom-order clients, built with v0, calculating order totals from a quantity field and a per-unit price.

A client testing edge cases out of curiosity submitted a negative quantity on a custom order and received a calculated total that credited the account instead of charging it. LaunchStudio's review confirmed the order endpoint validated quantity as a required field but never checked that it was a positive number, either on the form or on the server.

**Result:** LaunchStudio added consistent server-side validation across every order-related endpoint, rejecting negative, zero, or unreasonable quantity and price values regardless of which entry point submitted them.

> *"A client found this by accident while testing something unrelated and mentioned it almost as a joke. It genuinely could have gone unnoticed a lot longer than it did."*
> — **Niels Kramer, Founder, MakerLink (Nijmegen)**

**Cost & Timeline:** €2,000 (input validation audit across order and pricing endpoints) — completed in 7 business days.

---

## Frequently Asked Questions

### Would a QA engineer typically test for negative-quantity inputs as part of standard functional testing?

Not always — standard functional QA is often built around "does this work with expected input," and testing deliberately unreasonable input (negative numbers, extreme values) requires a specific adversarial mindset that isn't automatically part of every QA process.

### Does this kind of gap only affect marketplace or e-commerce products, or does it generalize further?

It generalizes to essentially any product with numeric inputs feeding into a calculation — quantities, prices, durations, discounts — meaning booking platforms, subscription tools, and billing systems all face structurally the same risk, not just marketplaces specifically.

### Manifera has decades of combined engineering experience across enterprise systems — does that translate directly to catching an edge case like MakerLink's?

Yes, directly — enterprise software engineering has always treated boundary and edge-case validation as a first-class concern rather than an afterthought, and that discipline transfers cleanly to founder-scale products regardless of how the initial code was generated.

### Is there a reason AI tools don't just validate numeric ranges by default without being asked?

Generally because a tool responds to what's described, and "quantity field" doesn't inherently imply "must reject negative values" unless the constraint is explicitly stated — the tool isn't failing at its job, it's simply completing a narrower job than the founder assumed.

### How does LaunchStudio decide the fixed price for a validation-focused engagement like this one?

The 15-minute intro call scopes the actual number of entry points and endpoints requiring review, and the fixed quote reflects that specific scope — a narrowly bounded issue like Niels's, once diagnosed, typically prices toward the lower end of the Launch Ready range rather than the higher end.

### If I try these five tests myself and nothing breaks, does that mean my validation is fully covered?

No — it means the specific paths you tested held up, not that every entry point did. A form might validate correctly while a secondary API endpoint reaching the same underlying data doesn't, which is exactly the kind of gap a full review checks for systematically rather than one form at a time.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do standard QA processes test for negative-quantity edge cases?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not always — this requires a specific adversarial mindset not automatically part of every QA process."
      }
    },
    {
      "@type": "Question",
      "name": "Does this validation gap only affect marketplace products?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, it generalizes to any product with numeric inputs feeding into a calculation, like bookings or subscriptions."
      }
    },
    {
      "@type": "Question",
      "name": "Does enterprise engineering experience translate to catching founder-scale edge cases?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, boundary and edge-case validation has always been treated as first-class in enterprise engineering discipline."
      }
    },
    {
      "@type": "Question",
      "name": "Why don't AI tools validate numeric ranges by default?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The tool completes the narrower job it was described, not the broader job a founder may have assumed."
      }
    },
    {
      "@type": "Question",
      "name": "How is the fixed price decided for a validation-focused engagement?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The intro call scopes the actual number of entry points needing review, and pricing reflects that specific scope."
      }
    },
    {
      "@type": "Question",
      "name": "If these five self-tests pass, does that mean validation is fully covered?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, it means the tested paths held up, not that every entry point did, including untested secondary API routes."
      }
    }
  ]
}
</script>
