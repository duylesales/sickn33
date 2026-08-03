---
Title: "Using AI for Development? Here's Where Founders Get Stuck Next"
Keywords: ai for development, ai in development, ai coding, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Using AI for Development? Here's Where Founders Get Stuck Next

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Using AI for Development? Here's Where Founders Get Stuck Next",
  "description": "A direct look at the specific point founders using AI for development tend to get stuck at next, using a mass-assignment vulnerability letting a user escalate their own role as the concrete case.",
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
  "datePublished": "2026-07-27",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/using-ai-for-development-heres-where-founders-get-stuck-next"
  }
}
</script>

Using AI for development gets a founder remarkably far before they hit their first genuine wall. That wall rarely looks like "the AI couldn't build this feature." It usually looks more like: the feature works, a user reported something strange about their own account, and nobody can quite explain why a simple profile update let them change something they were never supposed to be able to touch.

## Where the Wall Typically Appears

The specific wall many founders hit involves an update endpoint — a profile edit form, an account settings page — that accepts a broader set of fields from the request than the visible form actually presents. If a user's request can include fields beyond what the UI displays, and the backend saves whatever fields are present without filtering them, a request crafted (deliberately or accidentally) to include an extra field can modify data the UI never intended to expose for editing at all.

## Why This Is Called a Mass Assignment Vulnerability

The pattern has a specific, established name in software engineering because it's specific and recurring enough to be well documented: a backend that "mass assigns" whatever fields a request contains directly onto a database record, without an explicit list of which fields are actually allowed to be updated through that particular endpoint, trusts the request to only ever contain reasonable fields — an assumption that holds during normal UI-driven use and breaks the moment a request is crafted directly.

## Why a Working Profile Form Provides No Reassurance Here

Testing a profile edit form by actually using it — changing a name, updating a phone number — only ever sends the fields that specific form includes, so it never reveals what the backend would do with additional fields the form doesn't happen to submit. The gap is entirely about what's possible outside the form's own constraints, not about anything visibly wrong with the form itself. A founder can click through every single field on the form, confirm each one saves correctly, and still learn nothing about this risk — the vulnerability lives specifically in the space between what the form shows and what the backend will actually accept, a space ordinary use of the form never touches at all.

## Why an Account Role Field Is the Worst Possible Field to Leave Unprotected

If a user record includes a role or permission field — "member," "admin," "moderator" — and that field isn't explicitly excluded from what a profile update can modify, a specifically crafted request can potentially set that field directly, granting elevated privileges without any legitimate authorization process ever being involved. Once that happens, the consequences aren't limited to whatever the newly elevated account does next — an admin-level account typically has visibility into every other user's data, every other user's records, and often the platform's own configuration, meaning a single mass-assignment gap on a single field can function as a master key to the entire product rather than a narrow, contained issue.

## What Fixing This Requires

A proper fix explicitly defines which fields each specific endpoint is allowed to update — an allow-list rather than accepting whatever a request happens to contain — applied consistently across every update path in an application, not just the ones a founder remembers to check. [LaunchStudio](https://launchstudio.eu/en/) audits exactly this pattern across an entire codebase, backed by Manifera's 11+ years of backend engineering discipline applied to founder-scale products.

Manifera's backend security audits are carried out by the engineering team at the Ho Chi Minh City development center on Pho Quang Street, with client conversations handled through the Amsterdam headquarters at Herengracht 420.

[Talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact).

## Where Else This Same Pattern Hides Beyond Profile Forms

An account role field is the most damaging version of this vulnerability, but the underlying pattern — an update endpoint accepting more fields than the visible form presents — shows up anywhere a record has fields a user shouldn't be able to touch directly.

**Other places worth specifically checking for the same pattern:**

- **Order or subscription status fields** — if an "update my shipping address" endpoint also happens to accept an order-status field, a crafted request could potentially mark an unpaid order as paid, or a canceled subscription as active, without ever going through the actual payment or cancellation flow.
- **Pricing or discount fields on a cart or checkout object** — an endpoint that updates cart contents might also, unintentionally, accept a price-override or discount-percentage field never meant to be user-editable at all.
- **Ownership or ID reference fields** — an endpoint updating a resource's details might also accept a field reassigning which user account owns that resource, letting one user potentially claim another's data.
- **Verification or approval status fields** — a profile update on a marketplace or services platform might inadvertently allow setting an "is verified" or "is approved" flag directly, bypassing whatever manual or automated verification process was supposed to gate that status.

The common thread across every one of these is the same: a backend that trusts a request to only contain reasonable fields, rather than explicitly defining what each endpoint is allowed to accept. A review that finds and fixes one instance of this pattern in a codebase has good reason to specifically check for the same shape of problem everywhere else a record has a field more sensitive than the ones its own form intentionally exposes.

## Real example

### An AI-Native Founder in Action: The Profile Update That Granted Admin Access

Lars, a former staffing agency recruiter turned founder in Roosendaal, built WerfMakelaar, an AI-assisted recruitment and staffing platform built with Cursor, distinguishing between standard recruiter accounts and administrator accounts with broader platform access.

A partner testing the platform on Lars's behalf, while inspecting requests out of technical curiosity, discovered that the profile update endpoint accepted a role field alongside name and contact details, and that submitting a request with the role set to "admin" actually changed the account's permission level, with no server-side check preventing it. LaunchStudio's review confirmed the update endpoint saved every field present in the request without any allow-list restriction.

**Result:** LaunchStudio implemented an explicit allow-list on every update endpoint in WerfMakelaar, ensuring only intended fields can ever be modified through each specific form regardless of what else a request might contain, closing the privilege-escalation risk platform-wide.

> *"He showed me what he'd done and I genuinely didn't understand at first why it was even possible. It hadn't occurred to me that the same endpoint handling a phone number update could theoretically also hand out admin access."*
> — **Lars Verbeek, Founder, WerfMakelaar (Roosendaal)**

**Cost & Timeline:** €2,100 (mass assignment audit and allow-list implementation across update endpoints) — completed in 7 business days.

---

## Frequently Asked Questions

### Would a backend security specialist consider mass assignment a common vulnerability class in modern web frameworks?

Yes, common enough that many established web frameworks include built-in mechanisms specifically to prevent it, though those mechanisms have to be actively configured and used correctly — simply having access to the protective feature doesn't automatically mean every endpoint in a project correctly applies it.

### Does this risk only apply to fields like account roles, or is it broader?

It's broader — any field a user shouldn't be able to directly modify, including things like account balances, subscription status, or ownership references, carries the same underlying risk if an endpoint saves whatever a request contains rather than explicitly restricting which fields are allowed.

### Manifera has decades of combined backend engineering experience — does that specifically help catch mass assignment issues in an unfamiliar codebase quickly?

Yes, because the pattern to look for is well-defined and consistent regardless of the specific application — engineers experienced in backend security review know to specifically check every update endpoint's field-handling logic as a matter of routine, rather than needing to rediscover the risk from scratch each time.

### Is this the kind of issue CEO Herre Roelevink refers to when describing architecture gaps that aren't visible in a working demo?

Yes, precisely — a profile update that works correctly for its intended fields gives no visible indication of what else it might silently accept, which is exactly the invisible-until-tested-adversarially category Roelevink has repeatedly pointed to in discussing AI-generated software risk.

### If a founder used a well-known backend framework with built-in mass-assignment protection, could this still happen?

Yes, if the protective feature isn't correctly enabled or configured for every specific endpoint — having access to a safety mechanism and consistently applying it correctly across an entire codebase are two different things, and AI-generated code doesn't automatically guarantee the latter just because the framework supports the former.

### Would a founder normally have any way of knowing this risk exists without a technical background?

Not easily on their own — the term "mass assignment" itself isn't something a non-technical founder would encounter unless they specifically researched backend security concepts, and the vulnerability leaves no visible trace in normal product use. This is precisely the category of risk that benefits most from a founder simply knowing to ask "has someone checked our update endpoints for this specific pattern" during a pre-launch review, rather than needing to understand the underlying mechanics in detail themselves.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is mass assignment a common vulnerability in modern web frameworks?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, common enough that many frameworks include built-in prevention mechanisms, though they must be actively configured."
      }
    },
    {
      "@type": "Question",
      "name": "Does this risk only apply to account role fields?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, it's broader, applying to any field a user shouldn't directly modify, like balances or subscription status."
      }
    },
    {
      "@type": "Question",
      "name": "Does broad backend engineering experience help catch this quickly in unfamiliar codebases?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, the pattern to check for is well-defined and consistent regardless of the specific application."
      }
    },
    {
      "@type": "Question",
      "name": "Does this fit the invisible architecture-gap framing the CEO has described?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, a working update form gives no visible indication of what else it silently accepts."
      }
    },
    {
      "@type": "Question",
      "name": "Can mass assignment still happen with a framework offering built-in protection?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, if the protection isn't correctly enabled and consistently applied across every specific endpoint."
      }
    },
    {
      "@type": "Question",
      "name": "Would a non-technical founder normally know this risk exists on their own?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not easily — the vulnerability leaves no visible trace in normal use, which is why a pre-launch review needs to check for it."
      }
    }
  ]
}
</script>
