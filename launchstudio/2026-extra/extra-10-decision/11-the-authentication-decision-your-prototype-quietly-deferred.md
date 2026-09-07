---
Title: "The Authentication Decision Your Prototype Quietly Deferred"
Keywords: session vs token authentication, password reset token expiry, email enumeration login, role-based access control, JWT security, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# The Authentication Decision Your Prototype Quietly Deferred

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Authentication Decision Your Prototype Quietly Deferred",
  "description": "A technical breakdown of the authentication decisions an AI-generated prototype makes for you by default — session versus token storage, password reset token handling, email enumeration, and role design — and how to fix them before launch.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-02-02",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/the-authentication-decision-your-prototype-quietly-deferred" }
}
</script>

Ask a founder who bolted Supabase Auth or Firebase Auth onto their Lovable or Bolt prototype which authentication model they chose, and most will describe the login screen. Ask which token model it uses, where the token lives, how long it lasts, and what happens when it needs to be revoked, and the room goes quiet. Nobody chose. The AI tool picked a default, the default worked in the demo, and the decision that actually matters — the one with security and cost consequences — never got made by a human.

That's the pattern across every subsystem in this cluster: the prototype works, so the underlying decision looks settled. Authentication is the subsystem where that illusion is most dangerous, because the failure mode isn't a crash, it's a silent breach — someone else's account, someone else's data, discovered weeks later or never.

## Session Cookies or Bearer Tokens: The Question Your Prototype Answered by Accident

There are two fundamentally different ways to keep a user logged in, and most AI-generated backends pick one without telling you.

**Session-based auth** stores a session record server-side — in Postgres, Redis, or the auth provider's own store — and gives the browser an opaque, meaningless session ID in an httpOnly cookie. The browser can't read it, can't be tricked into leaking it via JavaScript, and the server can kill it instantly by deleting the record. Revocation is a single `DELETE` statement. The cost is state: every request needs a lookup, and if you ever run more than one server instance, that lookup needs to hit a shared store, not local memory.

**Token-based auth** (typically JWT) is the default in Supabase Auth, Firebase Auth, and most tool-generated backends because it's stateless and easy to wire into a serverless function. The access token itself carries the user's identity and claims, signed by the server, and the server can verify it without a database round trip. The tradeoff is the one founders don't learn until it bites them: a JWT can't be un-issued. Once signed, it's valid until it expires, no matter what you do in the database afterward — unless you build a separate revocation mechanism, which most prototypes don't have.

Neither model is wrong. The decision that got skipped is which one fits your product. A single web app with your own backend and no need for third-party API access is almost always simpler and safer on sessions — revocation, "log out everywhere," and account suspension all become trivial. A product with a web app, a mobile app, and a public API all authenticating against the same backend genuinely needs tokens, but needs them done properly: short-lived access tokens (15–60 minutes), a longer-lived refresh token that can be revoked, and a rotation scheme so a stolen refresh token gets detected on reuse.

## Where the Access Token Actually Lives — and Why That's Not a Detail

If your prototype uses token auth, the next decision is storage, and this is where AI-generated frontends consistently choose wrong by default: `localStorage`.

It's the easy path — `localStorage.setItem('token', ...)` works everywhere, survives refreshes, and needs no cookie configuration. It is also readable by any JavaScript running on your page, which means a single cross-site scripting vulnerability anywhere in your app — a comment field, a markdown renderer, a third-party widget — hands the attacker every logged-in user's token, not just one session. There is no browser-level defense against this; it's architectural.

The fix is to store the token in an httpOnly, Secure, SameSite cookie, which JavaScript cannot read at all, even if XSS exists elsewhere on the page. This requires your frontend and backend to cooperate on cookie-setting rather than the frontend managing the token directly, which is a real code change, not a config flag — and it's precisely the kind of change AI page-builders don't make because the demo doesn't need it to work.

If you're stuck with client-accessible token storage for architectural reasons (a fully static frontend hitting a third-party API directly, for instance), the mitigation is aggressive: short token lifetimes measured in minutes, strict Content Security Policy headers to constrain what scripts can run, and treating every third-party script you add as a potential exfiltration vector.

## The Password Reset Flow: Six Ways It Silently Fails

Password reset is the single most under-engineered flow in AI-generated auth, because it "works" in every version that never gets attacked. Six specific failures show up repeatedly:

**No expiry.** A reset token generated today is still valid in six months, sitting in an old email in someone's inbox or a shared support ticket.

**Not single-use.** The same link works twice. An attacker who gets a copy of the email — forwarded, cached, or intercepted — can reset the password even after the legitimate user already did.

**Predictable tokens.** Sequential IDs, timestamps, or a weak random function make the token guessable. This is more common than it sounds in code generated to "just work" rather than to resist an adversary.

**Stored in plaintext.** The token sits in the database as-is, so anyone with read access to that table — including a compromised dependency with database credentials — can reset any account.

**No invalidation of prior tokens.** A user requests three reset links across a week; all three stay valid, tripling the attack surface.

**No session invalidation on change.** The password changes, but sessions opened before the change stay logged in — meaning an attacker who already had access before the victim noticed keeps it after the "fix."

The correct version: generate a cryptographically random token (32 bytes from a CSPRNG), hash it before storing it exactly like a password, set a 15–60 minute expiry, mark it consumed the moment it's used inside the same database transaction that changes the password, invalidate every other outstanding token for that user, and terminate existing sessions on successful reset. It's maybe forty extra lines of code. It's also the forty lines that separate "reset flow" from "attack surface."

## Email Enumeration: The Leak Hiding in Plain Sight

Try signing up with an email that's already registered on most AI-generated prototypes and you'll get a specific, helpful error: "This email is already registered." Helpful to the user, and equally helpful to an attacker running a list of ten thousand emails against your signup form to find out which ones have accounts on your product — useful intelligence for phishing, credential-stuffing, or simply confirming someone uses your service at all.

The same leak hides in login ("no account found" versus "wrong password") and in password reset ("no user with that email" versus a generic confirmation). Response timing can leak it too — if checking a nonexistent email short-circuits faster than hashing a real password comparison, an attacker can distinguish the two from latency alone even when the messages match.

The fix is a discipline, not a library: every one of these flows returns the same message and takes roughly the same time regardless of whether the account exists. Login says "invalid email or password" for both a wrong password and a nonexistent account. Password reset always replies "if that email is registered, we've sent a link" — full stop, no branching. Signup is the one legitimate exception where you often do need to tell a real user their email is taken, so mitigate there instead with rate limiting per IP and per email, which turns a scriptable enumeration attack into a slow, expensive one.

## Why "We'll Add Roles Later" Turns Into a Rewrite

Almost every AI-generated prototype starts with exactly one implicit role: authenticated user. Every logged-in account can do everything an account can do, which is fine for a demo and fine for the first admin — until you need a second admin, a support-only role, or a `read-only` invited teammate, and "we'll add roles later" turns out to mean rewriting the authorization layer, not extending it.

The reason it's a rewrite rather than an addition: authorization checks that were never designed to branch on role are usually implemented as "is this user logged in" rather than "is this user allowed to do this specific thing." Retrofitting roles means finding every endpoint and every Supabase row-level security policy that assumed a single undifferentiated user, and rewriting each one's condition — not adding one condition somewhere central. In a codebase with forty API routes and RLS policies on a dozen tables, that's forty-plus places to touch, each one a chance to miss something and leave a gap where the old "any logged-in user" logic still applies.

The inexpensive alternative is deciding the shape early even with a single role. Add a `role` column to your users table on day one, default it to `member`, and write every authorization check — API middleware and database policy alike — to reference that column, even when there's only one value it can hold. Adding `admin` or `viewer` later becomes adding a value and a handful of new conditions, not restructuring a system that was never asked the question.

## Logout, Revocation, and What "Signed Out" Should Actually Mean

Clicking "log out" on most prototypes deletes a token from the browser's local storage or clears a cookie. On the server, nothing happens — the token or session the user just "logged out" of is still perfectly valid until it naturally expires. If it was ever copied (a shared computer, a leaked log line, a compromised browser extension), logging out does nothing to stop it.

Real logout needs a server-side action: for sessions, delete the record; for JWTs, either keep access tokens short enough that this barely matters (5–15 minutes) and revoke the refresh token server-side, or maintain a denylist of revoked tokens checked on each request — the tradeoff being that a denylist reintroduces the state you adopted JWTs to avoid. Products that need "log out of all devices," which any product handling billing or sensitive data eventually needs, require this server-side revocation to exist at all; it cannot be retrofitted onto a token scheme that assumed tokens live until expiry with no way to check.

## A Decision Framework: Which Auth Model Fits Your Product

Three questions settle most of this without a lengthy architecture debate.

**Do you have more than one client type?** Web-only with your own backend: sessions. Web plus mobile plus a public API: tokens, done properly with short expiry and refresh rotation.

**Does a compromised account need to be shut down instantly and completely?** If yes — anything handling payments, health data, or B2B accounts where one compromised login can touch a whole organization's data — you need real-time revocation, which sessions give you for free and tokens require you to build deliberately.

**Will you need more than one role within twelve months?** If the honest answer is yes, design the role column and the authorization checks around it now, at near-zero marginal cost, rather than as a structural change under time pressure later.

None of these decisions require exotic technology. Supabase Auth, Firebase Auth, and Auth0 all support both models correctly — the gap isn't the tool, it's that nobody told the tool which one your product actually needs.

Authentication is one of the recurring gaps [Manifera's engineers](https://www.manifera.com/services/custom-software-development/) find first when reviewing an AI-generated backend, because it's invisible until it fails. Getting it right before your first real user account exists is far cheaper than migrating live users through a token scheme change after the fact. If you want a second pair of eyes on what your prototype actually implemented versus what it should have, [send LaunchStudio your prototype link for free feedback](https://launchstudio.eu/en/#contact) before you scale past the first few accounts.

## Real example

### A Two-Person SaaS Team Finds Out What "Logged Out" Actually Meant

Tomasz Nowak and his co-founder built Rotaflow, a shift-scheduling tool for small hospitality businesses, in Bolt over six weekends. It used Supabase Auth out of the box, storing the JWT in `localStorage`, with a thirty-day expiry and no refresh rotation. It worked fine through their first eight pilot customers.

The problem surfaced when one pilot customer's manager left the company on bad terms and the owner asked Tomasz to "remove his access immediately." Tomasz deleted the user from the Supabase dashboard, confident that was the end of it — until testing showed the former manager's browser session kept working for the rest of its thirty-day token lifetime, because deleting the user record didn't invalidate a JWT that had already been signed and handed out. There was no revocation mechanism at all.

A short engagement moved the token into an httpOnly cookie, cut the access token lifetime to twenty minutes backed by a revocable refresh token, and added a `role` column that, for now, only ever holds `owner` or `staff` — but exists, and is checked, everywhere an authorization decision gets made.

**Result:** Rotaflow can now kill any account's access within twenty minutes worst case instead of thirty days, and adding a `read-only` accountant role next quarter is a one-line addition instead of an audit of every route.

> "I genuinely thought deleting the user was the fix. Finding out the old token just kept working was the moment I understood we'd never actually chosen an auth model — Bolt had chosen it for us."
> — **Tomasz Nowak, Co-Founder, Rotaflow (Kraków)**

**Cost & Timeline:** Launch Ready engagement, auth hardening scope — live in 6 business days.

## Frequently Asked Questions

### Is JWT-based auth inherently less secure than sessions?

No — it's a different tradeoff, not a weaker one. JWTs are stateless and harder to revoke instantly; sessions require server-side storage but revoke instantly. The risk isn't the token format, it's that most AI-generated prototypes implement JWTs without short expiry, refresh rotation, or any revocation path at all.

### How do I know if my prototype is storing tokens insecurely?

Open your browser's dev tools, go to Application → Local Storage, and check whether your auth token appears there in plain text. If it does, any script running on your page — including a compromised third-party widget — can read it. That's the single fastest check you can run today.

### Do I need to fix the roles issue if I only have one admin right now?

You don't need multiple roles today, but you should structure the authorization checks around a role field now rather than "is logged in." The fix costs almost nothing at one role and becomes a genuine rewrite once you have real endpoints and RLS policies built around the assumption that every account is equal.

### What's the minimum viable password reset flow that's actually safe?

A random token hashed before storage, a 15–60 minute expiry, single-use enforcement inside the same transaction as the password change, invalidation of other outstanding tokens, and a generic "if that email exists" response regardless of outcome. All of it is standard library functionality in Supabase, Firebase, and most frameworks — it just has to be turned on deliberately.

### Can LaunchStudio fix authentication without touching the rest of my app?

Yes — authentication hardening is typically an isolated backend and middleware change that doesn't require touching your frontend UI at all, which is the core of how LaunchStudio works: your interface stays exactly as your AI tool built it while the auth logic underneath gets rebuilt to hold up under real use.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Is JWT-based auth inherently less secure than sessions?", "acceptedAnswer": { "@type": "Answer", "text": "No, it's a different tradeoff. JWTs are stateless and harder to revoke instantly, while sessions require server-side storage but revoke instantly. The real risk is that most AI-generated prototypes implement JWTs without short expiry, refresh rotation, or any revocation path." } },
    { "@type": "Question", "name": "How do I know if my prototype is storing tokens insecurely?", "acceptedAnswer": { "@type": "Answer", "text": "Open browser dev tools, go to Application → Local Storage, and check whether your auth token appears in plain text. If it does, any script running on the page, including a compromised third-party widget, can read it." } },
    { "@type": "Question", "name": "Do I need to fix the roles issue if I only have one admin right now?", "acceptedAnswer": { "@type": "Answer", "text": "You don't need multiple roles today, but authorization checks should be structured around a role field now rather than 'is logged in.' The fix is nearly free at one role and becomes a genuine rewrite once endpoints and database policies assume every account is equal." } },
    { "@type": "Question", "name": "What's the minimum viable password reset flow that's actually safe?", "acceptedAnswer": { "@type": "Answer", "text": "A random token hashed before storage, a 15 to 60 minute expiry, single-use enforcement in the same transaction as the password change, invalidation of other outstanding tokens, and a generic response regardless of whether the email exists." } },
    { "@type": "Question", "name": "Can LaunchStudio fix authentication without touching the rest of my app?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. Authentication hardening is typically an isolated backend and middleware change that doesn't require touching frontend UI, consistent with LaunchStudio's approach of keeping the interface your AI tool built while rebuilding the logic underneath it." } }
  ]
}
</script>
