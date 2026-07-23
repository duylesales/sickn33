---
Title: "Authentication Looks Done in the Demo. Is It Done at the API Level?"
Keywords: from vibe coding to production, ai secure, ai security vulnerabilities, ai native, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Authentication Looks Done in the Demo. Is It Done at the API Level?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Authentication Looks Done in the Demo. Is It Done at the API Level?",
  "description": "A working login screen tells you nothing about whether your underlying API actually enforces access control. A deeper look at the specific vulnerability classes involved, how they're exploited, and how to verify the difference properly.",
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
  "datePublished": "2026-12-31",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/authentication-looks-done-demo-api-level"
  }
}
</script>

Your login screen rejects wrong passwords. It redirects unauthenticated users away from protected pages. By every visible measure, authentication works. None of that tells you whether the API underneath — the part a browser's address bar never shows you, the part that actually stores and serves your data — enforces the same rules, or whether it simply trusts whatever the frontend tells it about who's asking and what they're allowed to see.

## The Gap Between Frontend Gatekeeping and Real Access Control

Frontend authentication controls what a user sees rendered on their screen. It does nothing, structurally, to control what a user — or anyone bypassing the interface entirely and calling your API directly — can actually retrieve or modify at the data layer. If your API doesn't independently verify identity and permissions on every single request, your login screen is a polite suggestion enforced by convention, not a security boundary enforced by the system. This distinction matters because the two produce identical-looking demos and completely different real-world risk profiles.

## How This Gap Actually Gets Exploited

It doesn't require sophisticated hacking or specialized tools. Browser developer tools, freely available API testing clients like Postman or curl, or simply reading the network requests your own frontend already makes in the browser's network tab reveal the exact API endpoints your app calls, along with their expected request format. If those endpoints don't independently check who's asking on the server side, anyone moderately technical — not necessarily a sophisticated attacker, sometimes just a curious user or a competitor doing reconnaissance — can request data that the frontend was supposed to keep hidden, simply by constructing the same request the frontend would have sent, minus whatever restriction only existed in the interface.

## Three Specific Things to Verify

**Role-based access control.** Does a regular user's account, tested directly against the API rather than through the interface, actually get blocked from admin-only endpoints — or does the block exist only in which buttons and menu items the frontend chooses to render for that user's role?

**Session expiration.** Does an old or expired session token actually get rejected by the API when presented, or does it keep working indefinitely because expiration is only enforced by the frontend clearing local storage and redirecting to a login page, while the underlying token itself remains valid if someone captured and reused it?

**Direct object references.** Can a logged-in user request another user's data simply by changing an ID number in the request URL or payload, or does the API verify — on every single request, not just the first one — that the requesting user actually owns or has explicit permission for that specific record being requested?

## Why This Category of Bug Is So Persistent Across AI-Generated Backends

The reason this specific gap recurs so consistently isn't carelessness on the part of the AI tool — it's a direct consequence of how these systems are trained and how demos get built. A prompt describing "let users view their own data" gets satisfied the moment the frontend correctly requests and displays the logged-in user's own data under normal, cooperative use. Nothing in that instruction, or in the natural way a demo gets tested, forces the generated backend to also verify that assumption independently — the check that stops a *different* user from requesting someone else's ID simply never gets exercised until someone deliberately goes looking for it.

## The Verification That Actually Proves It

The real test: use a valid but insufficiently-privileged account, and try to access a restricted resource directly through the API, bypassing the frontend entirely. A properly secured API returns a 403 (forbidden) response, explicitly rejecting the request based on the requester's actual permissions. If it returns the data instead, your authentication exists in the wrong place — enforced by the interface's cooperation rather than the system's actual verification.

[LaunchStudio](https://launchstudio.eu/en/) verifies authentication at exactly this level as a core part of every Launch Ready engagement — testing against the API directly, not just confirming the login screen works — backed by Manifera's cybersecurity-informed engineering practices.

[Get your API-level access control actually tested](https://launchstudio.eu/en/#contact) — a login screen that works is not the same claim as an API that's secured.

## Real example

### An AI-Native Founder in Action: Discovering Every User Could See Every Other User's Data

Milan, a personal finance enthusiast turned founder in Zoetermeer, built BudgetMaatje, an AI tool analyzing bank statement uploads to generate personalized budgeting insights, using v0 for the interface with backend logic added through Cursor. Milan's login screen worked correctly, and each user only ever saw their own data in every test he personally ran, because the frontend always requested data using the currently logged-in user's own ID, and Milan had never had a reason — or a second test account handy in the right context — to check what happened if that assumption were deliberately violated.

During a LaunchStudio security review, the team tested the API directly, using one test account's valid session token to request another test account's financial data by simply changing the ID number in the request — a change entirely invisible to and unreachable through the actual frontend interface under normal use, but trivially available to anyone inspecting network requests with tools freely available in any browser.

The API returned the second account's full financial data without any verification that the requesting user had permission to see it. BudgetMaatje's frontend had been quietly relying on users only ever behaving as the interface intended, with nothing at the API layer preventing a user from requesting anyone else's sensitive financial information directly, given only a guessable or sequential ID number.

**Result:** LaunchStudio implemented proper server-side ownership verification on every data request before BudgetMaatje's beta launch, closing a gap that — given the sensitivity of financial data involved — represented the highest-consequence finding of the entire review, and one that would have been effectively invisible in any amount of Milan's own normal-use testing.

> *"My login screen worked perfectly. I had no idea that meant almost nothing about whether the actual data underneath was protected. Finding out before launch instead of after is the difference between a fix and a disaster."*
> — **Milan de Vries, Founder, BudgetMaatje (Zoetermeer)**

**Cost & Timeline:** €2,400 (Launch Ready Package, priority security scope) — live in 9 business days.

---

## Frequently Asked Questions

### How is this different from just making sure my login page is secure?

A secure login page controls who gets in. It says nothing about whether the API behind it independently verifies permissions on every subsequent request — Milan's login page was entirely secure, well-built, and functioning exactly as intended, and his data access was not, which is precisely the distinction this guidance addresses and why the two need to be evaluated completely separately.

### Can I test for this gap myself without technical security expertise?

Basic testing (trying to access another test account's data by changing an ID in a request, using browser developer tools) can surface obvious cases with minimal technical setup, though a thorough review — like the one that found Milan's gap — typically requires the kind of systematic, adversarial testing across every endpoint that a dedicated security-focused review provides, rather than a handful of manual spot-checks.

### Does this vulnerability type have a name I should know, for researching it further?

This category is commonly referred to as an insecure direct object reference (IDOR) vulnerability, alongside broader role-based access control gaps — both are well-documented, extremely common categories in web application security, appearing consistently on industry vulnerability classification lists across both traditionally-coded and AI-generated applications.

### Is this gap more likely in apps built with certain AI coding tools than others?

It's a broadly common gap across AI-generated backends generally, since AI tools tend to implement the access pattern that makes the demo work correctly under cooperative, intended use, without independently verifying every request server-side unless a founder or developer explicitly and specifically instructs the tool to add that verification — which requires knowing to ask for it in the first place.

### If my app doesn't handle sensitive data, is this still worth checking urgently?

It's worth checking regardless, though urgency scales directly with data sensitivity — an app handling financial or health data, like Milan's, warrants materially higher priority than a low-stakes internal tool, though the underlying architectural gap is worth closing in any production app before real users depend on it, since the fix is the same regardless of urgency and only gets more disruptive to retrofit later.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How is this different from just making sure my login page is secure?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A secure login page controls who gets in but says nothing about whether the API independently verifies permissions on every subsequent request."
      }
    },
    {
      "@type": "Question",
      "name": "Can I test for this gap myself without technical security expertise?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Basic testing using browser developer tools can surface obvious cases, though a thorough review typically requires systematic, adversarial security-focused testing across every endpoint."
      }
    },
    {
      "@type": "Question",
      "name": "Does this vulnerability type have a name I should know?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "This category is commonly called an insecure direct object reference (IDOR) vulnerability, alongside broader role-based access control gaps."
      }
    },
    {
      "@type": "Question",
      "name": "Is this gap more likely in apps built with certain AI coding tools than others?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It's a broadly common gap across AI-generated backends, since tools implement the pattern that makes the demo work without necessarily verifying every request server-side by default."
      }
    },
    {
      "@type": "Question",
      "name": "If my app doesn't handle sensitive data, is this still worth checking urgently?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Worth checking regardless, though urgency scales with data sensitivity — financial or health data warrants higher priority than low-stakes internal tools."
      }
    }
  ]
}
</script>
