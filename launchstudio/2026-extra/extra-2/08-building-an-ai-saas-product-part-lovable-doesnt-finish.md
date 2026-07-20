---
Title: "Building an AI SaaS Product? Here's the Part Lovable Doesn't Finish"
Keywords: ai saas, ai coding, ai native, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Building an AI SaaS Product? Here's the Part Lovable Doesn't Finish

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Building an AI SaaS Product? Here's the Part Lovable Doesn't Finish",
  "description": "80% of AI-built projects never reach production. A cost-analysis look at the specific, bounded piece of work that typically closes that remaining 20% for a founder-built AI SaaS product.",
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
    "@id": "https://launchstudio.eu/en/blog/building-an-ai-saas-product-part-lovable-doesnt-finish"
  }
}
</script>

80% of AI-built projects never reach production. That statistic tends to alarm founders in exactly the wrong direction — toward assuming their own prototype must have some deep, unknown flaw — when the far more common reality is a specific, boring, and entirely fixable gap: nobody added protection against a form being submitted from somewhere it shouldn't have been.

## What CSRF Protection Actually Prevents

Cross-site request forgery protection exists to stop a malicious site from tricking a logged-in user's browser into submitting a request to your application without the user's knowledge or consent — for instance, a hidden form on an unrelated page that silently submits a request to change a logged-in user's account settings the moment they visit it. Without this protection, your application has no way of distinguishing a request the user genuinely intended from one their browser was tricked into sending.

## Why AI-Generated Forms Frequently Skip This

Building a form that successfully submits data — the part a demo directly tests — is straightforward for an AI coding tool to generate correctly. Adding a CSRF token that the form includes and the server independently verifies is a separate, additive step that has no visible effect on whether the form "works" during a founder's own testing, which is precisely the kind of invisible-until-relevant detail that gets skipped by default.

## Why This Specific Gap Rarely Shows Up in Casual Testing

A founder submitting their own account settings form, from their own application, on their own device, never generates the scenario CSRF protection defends against — there's no malicious external site involved in that test at all. The gap only becomes relevant the moment a logged-in user visits somewhere else on the internet that's specifically trying to exploit it, a scenario no amount of the founder's own careful testing would ever produce.

## Why "Only 20% Remaining" Undersells How Bounded the Fix Actually Is

Framing this as "the last 20%" makes it sound vague and open-ended, when in practice it's usually a short, specific list: CSRF tokens on state-changing forms, server-side verification of those tokens, and testing that a request without a valid token gets rejected. It's a defined scope of work, not an open-ended rebuild — which is exactly why LaunchStudio prices it as a fixed, bounded engagement rather than an hourly, unpredictable one.

## What Closing This Gap Costs and Takes

For a typical founder-built SaaS product, this category of fix — CSRF protection alongside the handful of related form-security gaps that usually travel with it — fits comfortably within LaunchStudio's Launch Ready range of €800–€3,500, delivered in one to three weeks at a fixed price agreed after a short intro call. [LaunchStudio](https://launchstudio.eu/en/) is backed by Manifera, a software development company with 11+ years of experience closing exactly this category of gap for production applications.

Manifera's engineering delivery runs through its development center on Pho Quang Street in Ho Chi Minh City, coordinated with the Amsterdam headquarters at Herengracht 420 that handles the initial client conversation.

[Get a cost estimate with our pricing calculator](https://launchstudio.eu/en/#calculator).

## Real example

### An AI-Native Founder in Action: The Settings Change Nobody Requested

Eva, a former events coordinator turned founder in Breda, built TicketFlow, an AI-assisted event ticketing tool built with Lovable, letting organizers manage their own account and payout settings through a straightforward settings form.

A user reported their payout bank details had changed without their knowledge, and support logs showed no login from an unfamiliar device — just a normal, authenticated session. LaunchStudio's review found the settings form had no CSRF protection, meaning any external page could have silently triggered the same change while the user was simply logged in elsewhere.

**Result:** LaunchStudio added CSRF tokens to every state-changing form in TicketFlow and verified rejection of any request missing a valid token, closing the exposure without altering the settings page's design or workflow.

> *"The idea that just being logged in somewhere else on the internet could let a totally unrelated page change my bank details is honestly terrifying, and I had no idea it was even possible until this happened."*
> — **Eva Willems, Founder, TicketFlow (Breda)**

**Cost & Timeline:** €1,800 (CSRF protection and form security audit) — completed in 6 business days.

---

## Frequently Asked Questions

### Would a frontend-focused engineer describe CSRF as a frontend issue or a backend issue?

Genuinely both — the token has to be generated and embedded by the frontend, but it's meaningless unless the backend independently verifies it, which is exactly why it's easy for either side, working alone, to assume the other has handled it.

### Is CSRF protection specific to forms, or does it apply to API calls too?

It applies to any state-changing request, not just traditional HTML forms — API endpoints that change data based on a logged-in session face the identical exposure and need the same protection, regardless of whether the request originated from a visible form.

### Does the 80% production-failure statistic overstate how serious any individual founder's specific gap tends to be?

Often, yes — the statistic describes an outcome (never reaching production), not necessarily a severity level; many of the specific gaps behind it, like Eva's, are narrowly scoped and fixable in days once actually identified, rather than indicating some fundamentally broken foundation.

### CEO Herre Roelevink has framed the founder-economy opportunity around exactly this kind of gap — does TicketFlow's case reflect that framing directly?

Very directly — Roelevink's stated view is that founders now build genuinely good products quickly with AI, but need dedicated architecture and security expertise to close the remaining, specific gaps, which is precisely the shape of what happened with Eva's settings form.

### Is this something a founder could reasonably catch by asking their AI coding tool directly whether CSRF protection is included?

Sometimes — explicitly prompting for CSRF protection can lead a tool to include it, but relying on remembering to ask for every relevant protection, across every form, in every session, is a fragile substitute for a dedicated review that checks systematically rather than depending on prompt completeness.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is CSRF protection a frontend issue or a backend issue?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Both — the frontend generates the token but it's meaningless unless the backend independently verifies it."
      }
    },
    {
      "@type": "Question",
      "name": "Does CSRF protection apply only to HTML forms?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, it applies to any state-changing request, including API endpoints acting on a logged-in session."
      }
    },
    {
      "@type": "Question",
      "name": "Does the 80% production-failure statistic mean most gaps are severe?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not necessarily — many underlying gaps are narrowly scoped and fixable in days once identified."
      }
    },
    {
      "@type": "Question",
      "name": "Does this case reflect the CEO's framing of the founder-economy opportunity?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Very directly — good products built quickly with AI still need dedicated expertise to close specific remaining gaps."
      }
    },
    {
      "@type": "Question",
      "name": "Can a founder catch this by explicitly asking their AI tool for CSRF protection?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sometimes, but relying on remembering to ask every time is a fragile substitute for a systematic review."
      }
    }
  ]
}
</script>
