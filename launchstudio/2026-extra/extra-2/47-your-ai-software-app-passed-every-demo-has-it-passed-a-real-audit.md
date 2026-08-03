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

Passing every demo you've personally run and passing a genuine, adversarial audit are different achievements, and the gap between them shows up in exactly the kind of place a demo never checks: what actually happens to a session after a user clicks "log out," versus what a founder assumes happens based on the fact that the interface itself changes and looks logged out. A demo is fundamentally a cooperative exercise between a founder and an audience that wants the product to succeed; an audit is adversarial by design, specifically trying to find the one thing a cooperative walkthrough would never think to attempt.

## What "Logged Out" Looks Like From the Interface

Clicking logout in a typical AI software app correctly changes what the interface displays — the dashboard disappears, a login form reappears, everything visually confirms the logout worked. This is exactly what a founder checks when testing a logout feature, and it's a genuinely correct, necessary part of the feature working. It's also the only part most founders have a natural reason to check, since the interface is the entire surface a normal user interaction actually touches — nothing about clicking a logout button naturally prompts anyone to also verify what happened on the server behind the scenes.

## What "Logged Out" Needs to Mean on the Server

Beyond the visible interface change, a proper logout needs to actually invalidate the underlying session or token server-side, so that even if a copy of that same session token were somehow reused — through a saved browser tab, a shared device, or a captured request — it would no longer grant access. A logout that only clears the frontend's reference to the token, without invalidating the token itself server-side, leaves that token still fully functional if presented again. The two failure modes look identical from the interface — both show a login screen — but only one of them actually revokes access, which is precisely the distinction a founder has no natural way to observe just by watching their own screen.

## Why This Gap Is Nearly Invisible During Ordinary Testing

Testing your own logout feature means clicking logout and confirming the interface changes correctly — which it does, regardless of whether the underlying token was actually invalidated or merely forgotten by the frontend. There's no natural point during this test where a founder would think to manually resend the old, supposedly logged-out token directly to the server to check whether it still works. Doing so requires deliberately working against the interface rather than through it — capturing a token before it's discarded and replaying it directly against the server — which is precisely the kind of adversarial step a cooperative, feature-focused test has no built-in reason to take.

## Why This Matters More on Shared or Institutional Devices

An e-learning platform used across shared school computers or institutional devices faces this risk more concretely than a typical single-user consumer product — a student logging out on a shared classroom computer reasonably expects that action to fully end their session, and a token that remains valid afterward creates a real, practical risk of the next person on that device retaining unintended access. In a classroom specifically, that next person is often another student with an obvious incentive to look at someone else's quiz answers, grades, or account — turning an abstract technical gap into a very concrete, very human problem within days of anyone actually finding it.

## What Properly Fixing This Requires

A proper fix ensures the logout action actively invalidates the session or token on the server, not merely clears its reference on the client, verified by confirming a captured pre-logout token genuinely stops working immediately afterward. [LaunchStudio](https://launchstudio.eu/en/) tests exactly this scenario as part of its authentication security review, backed by Manifera's 11+ years of experience with session and token management across production systems.

Manifera's session security audits are conducted by the engineering team at the Ho Chi Minh City development center on Pho Quang Street, coordinated with the Amsterdam headquarters at Herengracht 420.

[Talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact).

## Session Management Beyond Logout: What Else to Check

Logout invalidation is one specific, concrete example of a broader category worth understanding fully: session and token behavior across the entire lifecycle of a user's access, not just the moment they explicitly click "sign out."

**Other session behaviors worth verifying alongside logout:**

- **Token expiration** — does a session token eventually expire on its own even if the user never logs out, or does it remain valid indefinitely once issued? A token with no expiration at all means a single captured token grants access forever, regardless of whether logout is later fixed.
- **Password change invalidation** — when a user changes their password, does that action invalidate their other existing sessions, or does an old, already-issued token remain valid even after the password it was originally issued under has changed?
- **Concurrent session limits** — for products where it matters (shared-device or security-sensitive contexts especially), can a founder see or limit how many active sessions a single account has open simultaneously, or does the system have no visibility into this at all?
- **Token refresh behavior** — if the system uses short-lived tokens with a separate refresh mechanism, does refreshing correctly extend only what it should, without accidentally granting broader access than the original token had?
- **"Remember me" persistence** — a long-lived "stay signed in" token often has different, looser security properties than a normal session token, and deserves its own explicit review rather than being assumed to inherit the same protections.

**Why these all matter together, not just individually:** a product can fix logout invalidation perfectly and still leave a meaningful gap if tokens never expire on their own, or if a password change doesn't revoke sessions issued before it. Session security is a lifecycle, not a single checkbox — and a thorough audit walks through the entire lifecycle deliberately, rather than stopping at the first, most obvious checkpoint a founder happened to think of.

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
