---
Title: "What an AI Generated Application Still Needs Before Real Users Arrive"
Keywords: ai generated application, ai generated tool, ai coding, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: SaaS Founder Scale-Up
---

# What an AI Generated Application Still Needs Before Real Users Arrive

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What an AI Generated Application Still Needs Before Real Users Arrive",
  "description": "A technical deep-dive on session token handling, using improperly validated JWTs in a newsletter subscription platform as the concrete case of what an AI generated application often gets wrong.",
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
  "datePublished": "2026-07-28",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/what-an-ai-generated-application-still-needs-before-real-users"
  }
}
</script>

An AI generated application handling paid subscriber logins typically gets the visible part of authentication right on the first try — a login form that accepts correct credentials and rejects incorrect ones. What frequently doesn't get the same scrutiny is the token that login actually issues afterward, and specifically whether that token is properly validated, correctly scoped, and set to actually expire.

## What a JWT Token Is Supposed to Guarantee

A JSON Web Token, commonly used to represent a logged-in session, is cryptographically signed so a server can verify it hasn't been tampered with and genuinely originated from a legitimate login. That guarantee only holds if the server actually verifies the signature on every request — a token that's merely decoded and read, without its signature being checked, provides no real security guarantee at all, regardless of how official it looks.

## Why Skipping Signature Verification Is an Easy Mistake to Make Invisibly

Decoding a JWT to read its contents (which user, which permissions) is a simple, common operation, and code that decodes a token correctly can appear to work perfectly during testing — a legitimately issued token decodes to the correct, expected information every time. The separate step of actually verifying that the token's signature is valid, rather than simply readable, produces no different visible outcome during normal, honest use.

## Why This Gap Becomes Serious the Moment Someone Crafts Their Own Token

If signature verification is skipped, a token doesn't need to be legitimately issued at all — anyone who understands the token's basic structure can construct their own, claiming to be any user or any permission level, and a server that only decodes without verifying will accept it as genuine, having no actual way to distinguish a forged token from a real one.

## Why Expiration Is a Separate, Equally Important Piece

Beyond signature verification, a token needs a reasonable expiration time, after which it's no longer accepted regardless of validity — without this, a token captured once (through a lost device, a compromised network, or any other means) remains usable indefinitely, extending what should be a bounded exposure window into an unbounded one.

## What a Complete Fix Looks Like

A proper implementation verifies every token's signature on every request, enforces reasonable expiration with a working refresh mechanism for legitimate ongoing sessions, and rejects anything that fails either check without leaking details about why. [LaunchStudio](https://launchstudio.eu/en/) audits exactly this pattern as part of its authentication review process, backed by Manifera's 11+ years of experience with Auth0, Supabase Auth, and custom JWT-based systems.

Manifera's session and token security audits are performed by the engineering team at the Ho Chi Minh City development center on Pho Quang Street, coordinated with the Amsterdam headquarters at Herengracht 420.

[Talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: The Subscriber Token That Never Expired

Britt, a former magazine editor turned founder in Hoorn, built LeesKring, an AI-assisted newsletter and long-form journalism subscription platform built with Lovable, gating premium articles behind a paid subscriber login.

A departed team member's old session, used months earlier during development, was still granting full premium access on a device nobody remembered was ever logged in, discovered only when Britt happened to notice unfamiliar activity while reviewing analytics. LaunchStudio's review found the platform's tokens had no expiration set at all, and worse, the server only decoded tokens to read their contents without ever verifying the cryptographic signature.

**Result:** LaunchStudio implemented proper signature verification on every request and added reasonable token expiration with a working refresh flow, closing both the forgery risk and the indefinite-session risk without disrupting how current subscribers logged in and stayed logged in.

> *"I found out almost by accident, just noticing something in analytics that didn't quite make sense. There was no alert, no error, nothing that would have told me on its own that this was even a possibility."*
> — **Britt Hendriks, Founder, LeesKring (Hoorn)**

**Cost & Timeline:** €2,300 (JWT verification and session expiration hardening) — completed in 7 business days.

---

## Frequently Asked Questions

### Would an identity-and-access engineer consider skipped signature verification a subtle mistake or an obvious one?

Subtle specifically because of how it presents during testing — a legitimately issued token decodes correctly whether or not its signature is actually checked, so the mistake produces zero visible symptoms until someone deliberately constructs a token that was never legitimately issued in the first place.

### Does using a well-known authentication provider like Auth0 or Supabase Auth eliminate this risk entirely?

It substantially reduces the risk when the provider's own libraries and recommended verification flow are used correctly, but a custom implementation layered on top — for instance, additional token handling logic written separately from the provider's own middleware — can still reintroduce the same underlying gap if it isn't reviewed specifically.

### Manifera's engineering has built authentication systems across multiple industries — does that variety matter for a subscription media platform specifically?

The underlying token security principles are identical regardless of industry, so the variety matters less for the core fix and more for understanding the surrounding context — subscription and paywall-specific nuances, like how Britt's platform needed to handle a legitimate reader's long-lived session convenience against the same security requirement.

### Herre Roelevink has described security gaps as often being invisible rather than obviously broken — does this case fit that description well?

About as well as any example could — Britt discovered the issue by pure chance during unrelated analytics review, with no error, alert, or visible symptom pointing to it, precisely the invisible-until-specifically-checked pattern Roelevink has repeatedly emphasized in discussing AI-native founders' security blind spots.

### Should a founder specifically ask their AI coding tool whether it verifies JWT signatures, or is that too technical a question to expect an answer from?

It's a reasonable, specific question to ask, and getting a clear answer is a good habit — but relying solely on that answer without an independent technical review to actually confirm it in the resulting code isn't a substitute for verification, since a described intention and the actual implemented behavior aren't always guaranteed to match.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is skipped JWT signature verification a subtle or obvious mistake?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Subtle — a legitimate token decodes correctly whether or not its signature is actually checked, producing no visible symptoms."
      }
    },
    {
      "@type": "Question",
      "name": "Does using Auth0 or Supabase Auth eliminate this risk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It substantially reduces risk when used correctly, but custom token handling layered on top can reintroduce the gap."
      }
    },
    {
      "@type": "Question",
      "name": "Does cross-industry authentication experience matter for a subscription media platform?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Token security principles are identical across industries; the variety helps more with surrounding context and nuance."
      }
    },
    {
      "@type": "Question",
      "name": "Does this case fit the invisible-security-gap description the CEO has given?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Very well — it was discovered by pure chance with no error or alert pointing to it at all."
      }
    },
    {
      "@type": "Question",
      "name": "Is asking an AI tool if it verifies JWT signatures enough on its own?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It's a reasonable question, but an independent technical review is still needed to confirm the actual implemented behavior."
      }
    }
  ]
}
</script>
