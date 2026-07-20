---
Title: "Your AI Prototype Looks Done. Here's How to Check If It Actually Is"
Keywords: ai prototype, prototype ai, ai native, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# Your AI Prototype Looks Done. Here's How to Check If It Actually Is

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Your AI Prototype Looks Done. Here's How to Check If It Actually Is",
  "description": "A how-to guide for founders wondering whether their AI prototype is genuinely ready, centered on a real example involving a Stripe secret key exposed in client-side code.",
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
  "datePublished": "2026-07-25",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/your-ai-prototype-looks-done-how-to-check-if-it-actually-is"
  }
}
</script>

"Looks done" is a genuinely misleading signal, and it's worth being honest about why: an AI prototype that renders cleanly, responds instantly, and handles every click you personally make is optimized specifically to produce that impression, regardless of what's actually happening underneath. Here's a concrete way to start checking whether "looks done" and "is done" actually match, using your own browser's developer tools as the first, free diagnostic.

## Step One: Open Your Browser's Developer Tools and Look at the Network Tab

Every modern browser includes a "Network" or "Sources" tab in its developer tools, showing every request your app makes and, often, the raw JavaScript bundle sent to the browser. This is publicly visible to literally anyone who opens the same tab on your live site — it's not a hidden or advanced hacking technique, it's a standard, built-in browser feature.

## Step Two: Search That Bundle for Anything Resembling a Secret Key

Searching the visible JavaScript bundle for strings like "sk_" (a common Stripe secret key prefix), "secret," "private," or your own known API key patterns is a simple, direct way to check whether a key that should only ever exist on your server has instead ended up bundled into code sent to every visitor's browser.

## Step Three: Understand Why This Specific Mistake Is So Common

Payment providers like Stripe issue two distinct kinds of keys — a "publishable" key, safe to use in frontend code, and a "secret" key, meant only for server-side use. AI coding tools generating a quick payment integration sometimes use whichever key was provided in the prompt without distinguishing between the two, and if a founder pastes the secret key where the publishable key belongs, the tool has no independent way of knowing that's the wrong one.

## Step Four: Recognize Why a Working Payment Flow Doesn't Rule This Out

A payment integration using the secret key directly in frontend code will, in many cases, still process test payments successfully — the mistake doesn't necessarily produce an error, which is exactly why "it works" isn't reassuring evidence here. The risk isn't that it fails to function; it's that a fully privileged key sits somewhere any visitor can read it.

## Step Five: Get a Systematic Review, Not Just a Manual Search

A manual search catches obvious cases but isn't exhaustive — a proper audit checks every integration systematically, confirms the correct key type is used in each context, and verifies no other secrets followed the same pattern. [LaunchStudio](https://launchstudio.eu/en/) performs exactly this kind of systematic key-and-secrets audit as a standard first step in its production-readiness review, backed by Manifera's 11+ years integrating Stripe and Mollie into secure production systems.

Manifera's payment security audits are carried out by the engineering team at the Ho Chi Minh City development center on Pho Quang Street, with client scoping conversations handled through the Amsterdam headquarters at Herengracht 420.

[Describe what you're building — we reply within one business day](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: The Donation Platform's Fully Privileged Key

Wouter, a former nonprofit program coordinator turned founder in Dordrecht, built SchenkPunt, an AI-assisted donation platform helping small nonprofits collect and track recurring donations, built with v0, integrated with Stripe for payment processing.

A volunteer developer helping another nonprofit evaluate SchenkPunt as a potential vendor opened the browser's developer tools out of habit and found Stripe's secret key sitting directly in the bundled frontend JavaScript, fully readable by anyone who did the same. LaunchStudio's review confirmed the secret key had been used in place of the publishable key throughout the entire checkout integration.

**Result:** LaunchStudio rotated the exposed Stripe key immediately, correctly separated publishable and secret key usage across frontend and backend code, and audited the rest of the integration for similar mistakes, closing the exposure without disrupting the donation flow nonprofits were already using.

> *"Donations were processing successfully the entire time, so nothing about using the app ever suggested anything was wrong. It took a volunteer with a developer background poking around out of habit to find it."*
> — **Wouter Smeets, Founder, SchenkPunt (Dordrecht)**

**Cost & Timeline:** €1,400 (Stripe key audit and secure integration remediation) — completed in 5 business days.

---

## Frequently Asked Questions

### Would a payments engineer consider mixing up publishable and secret keys a beginner mistake, or one experienced developers make too?

Both — it's a well-known enough pitfall that experienced developers are taught to watch for it specifically, but it remains common precisely because the two key types look superficially similar and both "work" during testing, regardless of experience level.

### Does checking the browser's Network tab yourself catch every possible key-exposure scenario?

No — it catches keys embedded directly in visible frontend code, which covers a meaningful portion of real cases, but a full audit also checks server-side configuration, third-party integrations, and any place a key might be logged or exposed indirectly rather than just the visible bundle.

### Is this specifically a Stripe issue, or do other payment providers have the same publishable-versus-secret key distinction?

The specific naming differs, but the underlying two-tier key structure — one safe for frontend use, one restricted to server-side use — is standard across virtually all major payment providers, including Mollie and PayPal, so the same category of mistake is possible with any of them.

### Does Manifera's broader B2B client base give it more experience specifically with nonprofit-sector tools like SchenkPunt?

Not specifically nonprofit-focused, but the underlying payment security review is identical regardless of sector — the same rotate-and-correctly-reintegrate process applies whether the client is a nonprofit donation platform or a commercial SaaS product, since the technical risk doesn't change based on who the end customer is.

### CEO Herre Roelevink has emphasized that closing gaps like this doesn't require rebuilding a product — does that apply to a payment integration fix like Wouter's?

Yes, directly — SchenkPunt's checkout flow, donation form, and nonprofit dashboard were completely untouched; the fix lived entirely in how keys were used and where, consistent with Roelevink's stated philosophy of fixing only what's structurally necessary.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is mixing up publishable and secret keys a beginner-only mistake?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, it's common at any experience level since both key types look similar and both work during testing."
      }
    },
    {
      "@type": "Question",
      "name": "Does checking the browser Network tab catch every key-exposure scenario?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, a full audit also checks server-side configuration and indirect exposure, not just the visible bundle."
      }
    },
    {
      "@type": "Question",
      "name": "Is the publishable-versus-secret key distinction unique to Stripe?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, the same two-tier key structure is standard across most major payment providers, including Mollie and PayPal."
      }
    },
    {
      "@type": "Question",
      "name": "Does broader B2B experience give a specific advantage for nonprofit-sector tools?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not sector-specific — the same payment security review applies regardless of the end customer's industry."
      }
    },
    {
      "@type": "Question",
      "name": "Does fixing an exposed payment key require touching the product's frontend?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, the fix lives entirely in how and where keys are used, leaving the frontend completely untouched."
      }
    }
  ]
}
</script>
