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

A founder submitting their own account settings form, from their own application, on their own device, never generates the scenario CSRF protection defends against — there's no malicious external site involved in that test at all. The gap only becomes relevant the moment a logged-in user visits somewhere else on the internet that's specifically trying to exploit it, a scenario no amount of the founder's own careful testing would ever produce. Even QA processes that involve a second person testing the product tend not to catch it, because that second tester is still using the application as intended, from a normal browser tab, with no attacker-controlled page anywhere in the loop — the entire vulnerability only exists in the specific gap between "a request the user meant to send" and "a request their browser was tricked into sending," which no amount of conventional functional testing, however thorough, is designed to probe.

## The Other Form-Security Gaps That Usually Travel With Missing CSRF Protection

CSRF protection rarely turns up alone. In practice, when a review finds a form missing CSRF tokens, it's common to find a small cluster of related, similarly invisible-in-testing gaps sitting right alongside it, because they all share the same root cause: a category of protection that adds no visible functionality during a founder's own straightforward testing.

**Missing or misconfigured cookie attributes.** Session cookies should typically be set with a `SameSite` attribute restricting when a browser will send them along with a cross-site request in the first place — a setting that, correctly configured, blocks a meaningful share of CSRF-style attacks before a token check is even needed. AI-generated authentication code frequently leaves cookies at their permissive default rather than setting this attribute explicitly.

**Clickjacking exposure.** Without an explicit header telling browsers your pages can't be loaded inside an invisible iframe on someone else's site, a malicious page can layer transparent buttons over your application's real interface, tricking a logged-in user into clicking something they can see (on the attacker's page) while actually clicking your application's hidden button underneath. A single response header (`X-Frame-Options` or an equivalent Content-Security-Policy directive) closes this, and it's another example of a one-line fix that has zero visible effect during normal testing.

**Open redirects.** A "redirect after login" or "return to this page" feature that accepts any URL without validating it against an allowed list can be exploited to send a user through your legitimate, trusted domain on the way to a convincing phishing page — technically leaving your application working exactly as designed, while being used as a stepping stone for something else entirely.

**Unescaped output reaching the page.** Anywhere user-submitted content (a comment, a display name, a support message) gets rendered back into the page without proper escaping opens the door to stored cross-site scripting, where one user's malicious input executes in another user's browser session simply by that second user viewing the page.

**Why these travel together:** all four share the exact profile described throughout this piece — a form or a page that visibly works correctly in every test a founder runs, because none of these gaps affect the happy path at all. A CSRF audit that stops at CSRF tokens alone, without checking cookie configuration, framing headers, redirect validation, and output escaping, tends to leave the rest of this cluster untouched — which is why LaunchStudio's form-security pass checks all of them together rather than treating CSRF as an isolated finding.

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

### If a review is scoped narrowly to "add CSRF protection," would these other related gaps get missed?

Possibly, if the review is interpreted that literally — this is why LaunchStudio's form-security pass checks the related cluster (cookie configuration, framing headers, redirect validation, output escaping) together by default, rather than treating a narrowly worded request as the full scope of what needs checking.

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
    },
    {
      "@type": "Question",
      "name": "Would a narrowly scoped CSRF review miss related form-security gaps?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Possibly — LaunchStudio's form-security pass checks the related cluster together by default rather than just CSRF alone."
      }
    }
  ]
}
</script>
