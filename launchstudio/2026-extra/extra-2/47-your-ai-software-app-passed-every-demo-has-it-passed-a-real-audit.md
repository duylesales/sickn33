---
Title: "Your AI Software App Passed Every Demo. Has It Passed a Real Audit?"
Keywords: ai software app, ai generated tool, ai coding, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Your AI Software App Passed Every Demo. Has It Passed a Real Audit?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Your AI Software App Passed Every Demo. Has It Passed a Real Audit?",
  "description": "A direct look at the difference between passing a demo and passing a real audit, using a session that stayed valid after logout in an e-learning quiz platform as the concrete case.",
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
  "datePublished": "2026-08-01",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/your-ai-software-app-passed-every-demo-has-it-passed-a-real-audit"
  }
}
</script>

Passing every demo you've personally run and passing a genuine, adversarial audit are different achievements, and the gap between them shows up in exactly the kind of place a demo never checks: what actually happens to a session after a user clicks "log out," versus what a founder assumes happens based on the fact that the interface itself changes and looks logged out.

## What "Logged Out" Looks Like From the Interface

Clicking logout in a typical AI software app correctly changes what the interface displays — the dashboard disappears, a login form reappears, everything visually confirms the logout worked. This is exactly what a founder checks when testing a logout feature, and it's a genuinely correct, necessary part of the feature working.

## What "Logged Out" Needs to Mean on the Server

Beyond the visible interface change, a proper logout needs to actually invalidate the underlying session or token server-side, so that even if a copy of that same session token were somehow reused — through a saved browser tab, a shared device, or a captured request — it would no longer grant access. A logout that only clears the frontend's reference to the token, without invalidating the token itself server-side, leaves that token still fully functional if presented again.

## Why This Gap Is Nearly Invisible During Ordinary Testing

Testing your own logout feature means clicking logout and confirming the interface changes correctly — which it does, regardless of whether the underlying token was actually invalidated or merely forgotten by the frontend. There's no natural point during this test where a founder would think to manually resend the old, supposedly logged-out token directly to the server to check whether it still works.

## Why This Matters More on Shared or Institutional Devices

An e-learning platform used across shared school computers or institutional devices faces this risk more concretely than a typical single-user consumer product — a student logging out on a shared classroom computer reasonably expects that action to fully end their session, and a token that remains valid afterward creates a real, practical risk of the next person on that device retaining unintended access.

## What Properly Fixing This Requires

A proper fix ensures the logout action actively invalidates the session or token on the server, not merely clears its reference on the client, verified by confirming a captured pre-logout token genuinely stops working immediately afterward. [LaunchStudio](https://launchstudio.eu/en/) tests exactly this scenario as part of its authentication security review, backed by Manifera's 11+ years of experience with session and token management across production systems.

Manifera's session security audits are conducted by the engineering team at the Ho Chi Minh City development center on Pho Quang Street, coordinated with the Amsterdam headquarters at Herengracht 420.

[Talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: The Logout That Didn't Actually Log Anyone Out

Anna, a former secondary school teacher turned founder in Kampen, built ToetsTijd, an AI-assisted e-learning quiz platform built with Cursor, used across several schools on shared classroom computers where students frequently logged in and out throughout the day.

An IT-savvy teacher, testing the platform's behavior out of professional caution given its use on shared devices, saved a session token before logging out and manually resent it afterward, finding it still granted full access despite the interface showing a logged-out state. LaunchStudio's review confirmed the logout feature only cleared the token from the frontend's local storage, without invalidating it on the server at all.

**Result:** LaunchStudio implemented proper server-side session invalidation triggered by logout, confirming a captured pre-logout token genuinely stops working immediately afterward, closing the gap specifically important for ToetsTijd's shared-device classroom use.

> *"The interface looked completely logged out every single time I tested it myself, which is exactly why I never suspected anything was actually still active underneath. It took a teacher specifically testing for this shared-device scenario to catch it."*
> — **Anna Visser, Founder, ToetsTijd (Kampen)**

**Cost & Timeline:** €1,600 (server-side session invalidation implementation) — completed in 5 business days.

---

## Frequently Asked Questions

### Would a session management specialist consider incomplete logout invalidation a common gap in quickly built applications?

Yes, fairly common — building a logout feature that correctly updates the visible interface is the more obvious, directly testable requirement, while the separate step of server-side token invalidation requires understanding that the two aren't automatically the same thing, a distinction that's easy to miss without dedicated session-management experience.

### Does this risk only matter for shared-device contexts like classrooms, or does it matter for individual users too?

It matters for individual users too, though the practical risk is more concrete and immediate on shared devices — an individual user's own device being compromised or a token being intercepted some other way still benefits from the same server-side invalidation, just with a less obvious, everyday trigger than a shared classroom computer.

### Manifera's experience spans consumer and institutional-use products alike — does that variety help catch a shared-device-specific risk like ToetsTijd's?

Yes, since understanding the specific usage context (shared classroom devices versus individual personal devices) shapes which risks matter most urgently, and having reviewed products across both contexts helps a review correctly prioritize and specifically test for the scenario that's actually most relevant to a given product's real-world use.

### Herre Roelevink has described the gap between "looks correct" and "is correct" as central to why AI-native founders need dedicated review — does this logout case capture that distinction well?

About as well as any single example could — the interface looked entirely correct through every test Anna herself ran, while the actual underlying behavior was meaningfully different, precisely the looks-correct-versus-is-correct gap Roelevink's broader commentary on AI-generated software consistently returns to.

### Is there a way for a founder to test their own logout feature for this specific gap without deep technical knowledge?

It requires at least some technical comfort with tools that let you resend a previously captured request, which isn't something every founder will have readily available — this is a reasonable example of a check that specifically benefits from a technical reviewer's tooling and experience rather than being easily self-verified by a non-technical founder alone.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is incomplete logout invalidation a common gap in quickly built applications?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, fairly common, since the visible interface update is more obviously testable than server-side token invalidation."
      }
    },
    {
      "@type": "Question",
      "name": "Does this risk only matter for shared devices like classrooms?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, it matters for individual users too, though the practical risk is more immediate on shared devices."
      }
    },
    {
      "@type": "Question",
      "name": "Does experience across consumer and institutional products help catch shared-device-specific risks?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, understanding the usage context shapes which risks matter most and how to prioritize testing for them."
      }
    },
    {
      "@type": "Question",
      "name": "Does this logout case capture the looks-correct-versus-is-correct gap the CEO describes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "About as well as any example could — the interface looked entirely correct while the actual behavior differed."
      }
    },
    {
      "@type": "Question",
      "name": "Can a founder test their own logout feature for this gap without deep technical knowledge?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It requires some technical tooling to resend a captured request, which most non-technical founders won't readily have."
      }
    }
  ]
}
</script>
