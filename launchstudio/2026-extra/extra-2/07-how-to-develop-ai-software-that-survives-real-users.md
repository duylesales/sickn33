---
Title: "How to Develop AI Software That Survives Contact With Real Users"
Keywords: develop ai software, ai saas, ai deployment, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# How to Develop AI Software That Survives Contact With Real Users

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Develop AI Software That Survives Contact With Real Users",
  "description": "A how-to guide for founders scaling past MVP, focused on the specific webhook and payment-event handling gap that tends to surface once real customers, not test cards, start using the product.",
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
    "@id": "https://launchstudio.eu/en/blog/how-to-develop-ai-software-that-survives-real-users"
  }
}
</script>

It's 2 AM. You just finished scaling your SaaS prototype past its first hundred paying customers. The demo looked perfect at ten users. Then a payment provider's webhook starts firing events your code was never actually tested against, and the gap between "works for the founder" and "develop AI software that holds up under real usage" becomes very concrete, very quickly.

## Step One: Recognize That Scale Changes What Breaks

At low volume, almost every workflow completes exactly as designed, because there's rarely more than one thing happening at once. As real customers arrive, concurrent events become the norm rather than the exception — multiple webhooks firing close together, retried requests, and edge cases that simply never occurred often enough at small scale to be noticed. A founder testing their own product might trigger one webhook every few minutes, if that — an SaaS product with even a modest few hundred paying customers can see dozens of events arrive within the same second during a billing cycle's renewal window, a load pattern that simply doesn't exist anywhere in a founder's own manual testing history.

## Step Two: Understand Why Webhook Verification Specifically Gets Skipped

A webhook handler that processes an incoming "payment succeeded" event correctly, using test data during development, has proven the happy path works. It hasn't proven the handler correctly verifies that the event genuinely originated from the payment provider itself, rather than a forged request crafted to look like one — a distinction that matters enormously once the endpoint is publicly reachable and processing real financial events.

## Step Three: Identify Where Signature Verification Actually Belongs

Every reputable payment provider signs its webhook payloads cryptographically, specifically so the receiving server can verify authenticity before acting on the event. AI-generated webhook handlers frequently parse and act on the payload's contents without first checking that signature, because the signature-check step adds no visible functionality during a founder's own straightforward testing — it only matters against an event that was never legitimate in the first place.

## Step Four: Recognize the Compounding Risk of Scaling Before Fixing This

An unverified webhook endpoint is a manageable, theoretical risk at ten trusted early users. At meaningful scale, with a public, discoverable endpoint processing real financial events, it becomes a concrete avenue for someone to submit forged "payment succeeded" events and receive product access without ever actually paying — a risk that grows directly with how many people know your endpoint exists.

## Beyond Webhooks: Other Concurrency Failure Modes That Surface Only at Scale

Signature verification closes one specific gap, but it's part of a broader category of problems that share the same root cause: code tested against one request at a time, deployed into an environment where many requests now arrive close together. Recognizing the pattern helps a founder spot the next instance before it turns into a support ticket.

**Idempotency — handling the same event twice safely.** Payment providers, by design, sometimes send the same webhook event more than once, particularly during network retries or provider-side hiccups. Code that processes "payment succeeded" by simply granting access or incrementing a counter, without first checking whether that specific event was already processed, can end up granting double access or double-counting a single payment if the event arrives twice. The fix is straightforward once identified — record each processed event's unique ID and skip anything already seen — but it never surfaces during single-request testing, because a founder testing manually never triggers the same webhook twice by accident.

**Race conditions on limited resources.** Anything with a fixed, countable quantity — the last seat in a class, the last unit of inventory, a limited-time discount code capped at a specific number of uses — can be claimed by more than one concurrent request if the "check remaining count, then decrement it" logic isn't handled as a single atomic operation. Tested one request at a time, this always works correctly. Tested by two customers clicking "buy" within the same second, it can let both succeed against a resource that only had one unit left.

**Retry storms.** When an external service the application depends on goes down briefly, a naive retry implementation — one that immediately retries a failed request in a tight loop — can turn a short outage into a much longer one, by hammering the recovering service with a burst of retries the moment it comes back online, sometimes taking it back down again. A more resilient pattern spaces retries out with increasing delays between attempts, rather than retrying as fast as possible.

**Ordering assumptions that don't hold under load.** Code that assumes event A always arrives before event B — a user signup event before their first payment event, for instance — can behave unpredictably once traffic is high enough that the two arrive out of order or nearly simultaneously, a scenario that essentially never happens during low-volume founder testing.

None of these are exotic problems; they're the standard list any engineer scaling a payments-adjacent system checks for as a matter of course. What they have in common with the webhook-signature gap is the same underlying reason they get missed: they're invisible at low volume, by definition, and only become visible at exactly the point where a founder is busiest with growth rather than looking backward at infrastructure. [LaunchStudio](https://launchstudio.eu/en/#process) reviews for this specific category of failure as part of scaling founders' production-readiness work, alongside the webhook fix itself.

## Step Five: Apply the Fix Without Disrupting What Already Works

Adding signature verification is a narrowly scoped, additive change to the webhook handler itself — it doesn't touch your subscription logic, your product's core features, or the customer-facing payment flow that already works correctly. [LaunchStudio](https://launchstudio.eu/en/) implements this specifically as part of its Launch & Grow package for scaling SaaS founders, backed by Manifera's 11+ years integrating Stripe, Mollie, and other payment infrastructure into production systems.

Manifera's payment-integration engineering is delivered through its Vietnam development center on Pho Quang Street in Ho Chi Minh City, with client scoping handled through the Amsterdam office at Herengracht 420.

[Get started — from prototype to production in weeks, not months](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: The Course Access Nobody Actually Paid For

Joris, a former high-school teacher turned founder in Leiden, built LeerPad, an AI-assisted online course platform built with Bolt, integrated with Mollie for subscription payments, scaling from a small pilot to several hundred paying students within two months.

A support ticket flagged a student with full course access and no matching successful payment record in Mollie's dashboard. LaunchStudio's review found LeerPad's webhook handler processed "payment succeeded" events without verifying the request's signature, meaning any correctly formatted payload — forged or genuine — granted access.

**Result:** LaunchStudio added proper signature verification to the webhook endpoint, ensuring only genuinely signed events from Mollie can grant access, closing the gap before it could be exploited at any larger scale.

> *"We caught one account this way through pure luck — a mismatched support ticket. There could easily have been others we never noticed at all."*
> — **Joris Bakker, Founder, LeerPad (Leiden)**

**Cost & Timeline:** €3,200 (webhook security and payment reconciliation hardening) — completed in 10 business days.

---

## Frequently Asked Questions

### Would a payments engineer consider signature verification a "basic" requirement, or an advanced one?

Basic, in the sense that it's considered a foundational requirement in professional payment integration work — it's easy to overlook precisely because it's not visually obvious in a demo, not because it's an advanced or obscure technique.

### Does this issue scale in severity with a product's growth, or stay roughly constant?

It scales directly with growth — a wider, better-known, more publicly discoverable endpoint gives more potential bad actors the opportunity to find and exploit it, so the risk compounds rather than staying flat as a product gains users.

### Manifera's payment integration work spans multiple providers — does the specific provider (Mollie vs. Stripe) change how this gap gets found or fixed?

The specific implementation details differ slightly by provider, but the underlying principle — verify the signature before trusting the payload — applies identically across Stripe, Mollie, PayPal, and others, so provider choice doesn't change the fundamental fix.

### Herre Roelevink has emphasized architecture over raw code output — is webhook verification really an "architecture" decision rather than a bug?

Yes — it's a decision about how the system verifies trust at a specific external boundary, which is squarely the kind of structural, easy-to-defer decision his commentary on AI-generated software consistently returns to.

### If a founder catches an issue like Joris's through a support ticket, is that a reliable enough detection method going forward?

No — a mismatched support ticket catching this once was fortunate rather than a repeatable safeguard, which is exactly why a proactive review, rather than waiting for a customer to stumble onto evidence, is the more reliable path once a product is scaling.

### Do these same concurrency issues apply to a product that isn't handling payments at all?

Yes — any feature involving a limited resource (booking slots, coupon codes, seat availability) or any process triggered by an external event, like an email service webhook or a third-party integration callback, can hit the same idempotency and race-condition patterns, regardless of whether payments are involved.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is webhook signature verification a basic or advanced requirement?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Basic and foundational — it's overlooked because it's not visually obvious in a demo, not because it's advanced."
      }
    },
    {
      "@type": "Question",
      "name": "Does this risk scale with a product's growth?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, a wider, more discoverable endpoint gives more potential bad actors the chance to find and exploit it."
      }
    },
    {
      "@type": "Question",
      "name": "Does the specific payment provider change how this gap is fixed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Implementation details differ slightly, but verifying the signature before trusting the payload applies across all providers."
      }
    },
    {
      "@type": "Question",
      "name": "Is webhook verification an architecture decision rather than a simple bug?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, it's a decision about how the system verifies trust at an external boundary, a structural rather than cosmetic issue."
      }
    },
    {
      "@type": "Question",
      "name": "Is catching this via a support ticket a reliable detection method?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, it was fortunate rather than repeatable, which is why a proactive review is more reliable than waiting for evidence."
      }
    },
    {
      "@type": "Question",
      "name": "Do these concurrency issues apply to products that don't handle payments?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — any limited resource or externally triggered process can hit the same idempotency and race-condition patterns."
      }
    }
  ]
}
</script>
