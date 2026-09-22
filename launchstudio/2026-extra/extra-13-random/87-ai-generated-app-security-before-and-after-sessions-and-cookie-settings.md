---
Title: "AI Generated App Security Before and After: Sessions and Cookie Settings"
Keywords: ai generated app security, session security, cookie flags httponly samesite, csrf protection, cursor auth, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI Generated App Security Before and After: Sessions and Cookie Settings

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Generated App Security Before and After: Sessions and Cookie Settings",
  "description": "Sessions decide who is logged in, and AI-generated code often stores and handles them loosely. A before-and-after look at session and cookie settings in AI generated app security: storage, cookie flags, CSRF, lifetimes, logout and session revocation.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-26",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-generated-app-security-before-and-after-sessions-and-cookie-settings" }
}
</script>

Logging in is a moment; a session is everything after it. Every request your app receives carries some proof that "this is still the user who logged in" — a token or a cookie. If that proof can be stolen, forged or reused, the strength of your login screen does not matter. Session handling is an area of AI generated app security that rarely gets attention in demos, because demos never test what happens to a session on a shared computer, in a malicious link or after a password change.

## Before: How AI-Generated Apps Often Handle Sessions

When AI tools implement custom authentication — or wrap a provider's auth in their own code — common patterns include:

- **Tokens in localStorage,** readable by any JavaScript on the page, including injected scripts.
- **Cookies without security flags** — missing `HttpOnly`, `Secure` or `SameSite`.
- **Very long lifetimes,** such as tokens valid for 30 days with no refresh or revocation.
- **Logout that only deletes the token in the browser,** while the token itself stays valid on the server.
- **No session revocation** after password changes or account removal.
- **No CSRF protection** on cookie-authenticated forms that change data.
- **Session identifiers in URLs,** which leak through browser history, logs and referrer headers.

## After: Cookie Settings That Matter for AI Generated App Security

For cookie-based sessions, three flags do most of the work:

- **`HttpOnly`**: JavaScript cannot read the cookie, so a script injection cannot simply steal the session.
- **`Secure`**: the cookie is sent only over HTTPS.
- **`SameSite=Lax` (or `Strict`)**: the browser does not send the cookie on most cross-site requests, which blocks a large class of cross-site request forgery.

Add a sensible `Path`, avoid overly broad `Domain` settings that share cookies across subdomains unnecessarily, and use the `__Host-` prefix where possible for cookies that should stay bound to one host.

## After: Where Tokens Live

If your app uses tokens (for example JWTs) rather than server sessions, storage matters. Tokens in `localStorage` are exposed to any script running on your page; an XSS flaw becomes an account takeover. Safer patterns keep refresh tokens in `HttpOnly` cookies, keep access tokens short-lived and in memory, and rotate refresh tokens on use. Mature auth providers implement these patterns; custom code often does not.

## After: CSRF Protection

If the browser sends session cookies automatically, another site can try to make a logged-in user's browser submit a request to your app. `SameSite` cookies mitigate most of this; for sensitive actions, add CSRF tokens or require a custom header that cross-site forms cannot set.

## After: Lifetimes, Logout and Revocation

- **Idle timeout** and **absolute lifetime** appropriate to the data: shorter for financial or health apps, longer for low-risk tools.
- **Logout invalidates the session on the server,** not just in the browser.
- **Password change and account removal revoke all sessions.**
- **"Log out everywhere"** for users who suspect a lost device.
- **Session listing** for higher-risk apps, so users can see active devices.

## After: Session Fixation and Rotation

Issue a new session identifier at login and at privilege changes (for example, after entering admin mode), so an identifier set before login cannot be reused by an attacker.

## Quick Self-Check

Open your browser's developer tools, log in, and look at Application → Cookies and Local Storage:

- Are there tokens in localStorage?
- Do your session cookies show HttpOnly, Secure and SameSite?
- After logging out, does replaying an old request still work?
- After changing your password on one device, is another device logged out?

The [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) covers the details.

## Setting Cookies Correctly, in Code

For AI generated app security, the difference between a weak and a strong session cookie is a handful of attributes. In a Next.js route handler, setting a session cookie properly looks like this:

```typescript
import { cookies } from "next/headers";

cookies().set("__Host-session", sessionId, {
  httpOnly: true,     // not readable by JavaScript
  secure: true,       // HTTPS only
  sameSite: "lax",    // not sent on most cross-site requests
  path: "/",          // required for the __Host- prefix
  maxAge: 60 * 60 * 8 // 8 hours
});
```

The `__Host-` prefix tells browsers to accept the cookie only if it is secure, has path `/` and no domain attribute — which prevents subdomains from overwriting it. Many AI-generated implementations set cookies with default attributes, which usually means no `HttpOnly` and sometimes no `Secure`.

## Choosing Session Lifetimes by Risk

| App type | Idle timeout | Absolute lifetime | Re-authentication for |
| --- | --- | --- | --- |
| Low-risk tool (notes, planning) | Days to weeks with refresh | 30–90 days | Changing email or password |
| Typical SaaS with business data | Hours | 7–30 days | Billing, exports, role changes |
| Financial, health or HR data | 15–60 minutes | 12–24 hours | Any sensitive view or change |
| Shared devices (reception, classrooms) | Minutes | Same working day | Every session |

Choose lifetimes deliberately and explain them to users where they cause friction ("for your security, please log in again to download documents").

## Token-Based Sessions Done Safely

Apps using JWTs or similar tokens should follow a few rules: short-lived access tokens (minutes); refresh tokens stored in HttpOnly cookies, rotated on every use, with reuse detection that revokes the whole session if an old refresh token appears again; server-side records of active sessions so they can be revoked; and verification of token signature, expiry and audience on every request. Mature auth providers implement these patterns; custom implementations generated by AI tools often skip rotation and revocation entirely.

## CSRF Protection in Modern Frameworks

With SameSite cookies, most cross-site request forgery is blocked by the browser. For additional protection on sensitive actions, use one of: synchroniser tokens (a random token in the form, verified on the server), double-submit cookies, or requiring a custom header that simple cross-site forms cannot set. Some frameworks provide CSRF protection for form actions by default — for example by checking the Origin header — but verify it is active in your configuration rather than assuming.

## Logout That Actually Ends Sessions

A correct logout: deletes the session record or revokes the refresh token on the server, clears the cookie with the same attributes used to set it, and invalidates any cached user data in the client. "Log out everywhere" revokes all sessions for the user. Test it: log out, then replay a previously captured request with the old cookie or token. It must fail.

## Session Security and Content Security Policy

Session protections and XSS protections reinforce each other. HttpOnly cookies stop injected scripts from reading session cookies, but scripts can still act on behalf of the user within the page. A Content Security Policy that restricts script sources and disallows inline scripts reduces the chance that injected code runs at all. Together, they turn an XSS bug from a potential account takeover into a much smaller problem.

## Monitoring Session Anomalies

Log session events — login, refresh, logout, revocation, failed refresh — with IP ranges and user agents. Alert on patterns such as many sessions for one account from different countries within minutes, refresh-token reuse detection triggering, or spikes in failed logins. Users can also be shown their active sessions and recent logins, giving them a chance to spot suspicious activity themselves.

## Testing Session Behaviour

Add automated tests for: cookie attributes on login responses; access denied after logout with the old cookie; sessions revoked after password change; refresh token rotation and reuse detection; CSRF protection on state-changing endpoints; and idle timeout enforcement. These tests protect against regressions when authentication code is regenerated or refactored.

## Sessions on Shared and Public Devices

Apps used on shared devices — reception desks, classrooms, workshops, kiosks — need special handling. Offer a "shared device" mode with short idle timeouts, no "remember me," automatic logout at the end of the working day and quick user switching via PIN on top of a device-level session. Clear sensitive data from the page when the session ends, so the back button does not reveal previous screens; set cache headers on authenticated pages to prevent browsers from storing them.

## Mobile App Sessions

Mobile apps typically keep users logged in longer, which is reasonable because the device itself is usually protected. Store tokens in the platform's secure storage (Keychain or Keystore), not in plain local storage; use refresh token rotation; allow remote revocation from the web app ("log out of all devices"); and require biometric or PIN confirmation for sensitive actions if the app handles financial or health data.

## Third-Party Cookies and Embedded Apps

If your app is embedded in other sites (for example as a booking widget) or uses authentication across domains, browser restrictions on third-party cookies affect sessions. Plan for this: prefer first-party domains for authentication, use redirect-based login flows rather than cookies in iframes, and test in browsers with strict privacy settings. Embedded widgets that rely on third-party cookies often break silently for a growing share of users.

## A Session Security Checklist

Before launch, confirm: session cookies are HttpOnly, Secure and SameSite with the `__Host-` prefix where possible; no tokens in localStorage; access tokens short-lived, refresh tokens rotated with reuse detection; logout and password change revoke sessions on the server; idle and absolute timeouts match the data's sensitivity; CSRF protection active on state-changing requests; a Content Security Policy in place; authenticated pages not cached by browsers; session anomalies logged; and automated tests covering these behaviours.

## Why Founders Should Care

Session flaws rarely show up in demos, yet they decide whether a single stolen token or a shared computer turns into an account takeover. They are usually cheap to fix — mostly configuration and the use of a mature auth provider — and expensive to explain after an incident. Put session security on the same list as access control and payments before launch.

## Before and After, Summarised

Before: tokens in localStorage, cookies without flags, sessions that last a month, logout that only hides the token, no CSRF protection and no revocation after a password change. After: HttpOnly, Secure, SameSite cookies with host binding; short-lived access tokens with rotated refresh tokens; server-side revocation on logout and password change; timeouts matched to risk; CSRF protection on sensitive actions; a Content Security Policy; anomalies logged; and tests that keep all of it in place. The interface looks identical in both cases — the difference is whether a stolen token, a shared computer or a malicious link can turn into someone else's account.

## First Step

Log in to your app, open the browser's developer tools and look at Application → Cookies and Local Storage. If you see a token in Local Storage or a session cookie without HttpOnly, start there.

## Where LaunchStudio Fits

LaunchStudio reviews session handling as part of every authentication check and usually replaces custom session code with the auth provider's secure defaults, adds correct cookie flags, CSRF protection, server-side logout and revocation, and appropriate lifetimes. LaunchStudio is powered by Manifera, whose CEO Herre Roelevink's cybersecurity background — including co-founding CyberDevOps, now CFLW Cyber Strategies — shapes a security-first review culture. Manifera's engineers work in Ho Chi Minh City, with client contact through Herengracht 420, Amsterdam. See [Manifera's about page](https://www.manifera.com/about-us/).

[Get a fixed-price quote](https://launchstudio.eu/en/#contact) for an authentication and session review.

## Real example

### An AI-Native Founder in Action: A Meeting Room App Where Logout Didn't Log Out

Sem Evers, a facility coordinator turned founder in IJsselstein, built Zaalvrij with Cursor: companies in shared office buildings book meeting rooms, manage visitors and get monthly usage invoices. Twenty-six companies across four buildings used it, often from shared reception computers.

A receptionist reported that after logging out on the shared computer, pressing the browser's back button showed another company's bookings — and that clicking around still worked. The review explained why: Cursor had implemented JWT authentication with tokens stored in localStorage, valid for 30 days, and logout simply removed the token from the browser without invalidating it. A copied token kept working. Cookies used for a "remember me" feature lacked HttpOnly and SameSite flags, forms that cancelled bookings had no CSRF protection, and changing a password did not end other sessions. A reflected XSS in the visitor name field meant a crafted link could have read the token from localStorage.

Over four business days, LaunchStudio's engineers replaced the custom JWT handling with Supabase Auth sessions, stored refresh tokens in HttpOnly, Secure, SameSite=Lax cookies, shortened access token lifetimes, invalidated sessions server-side on logout and on password change, added an eight-hour idle timeout for accounts flagged as shared-computer use, protected state-changing forms with CSRF tokens, fixed the XSS with output escaping and a Content Security Policy, and added "log out everywhere."

**Result:** The shared-computer issue disappeared, and a later security questionnaire from a larger tenant was answered without follow-up questions. Zaalvrij has since been adopted in two more office buildings.

> *"Our logout button was a polite suggestion. Now it actually ends the session."*
> — **Sem Evers, Founder, Zaalvrij (IJsselstein)**

**Cost & Timeline:** €1,100 (session and cookie hardening, CSRF protection, XSS fix and auth provider migration) — completed in 4 business days.

## Frequently Asked Questions

### Is storing tokens in localStorage insecure?

It exposes them to any JavaScript on the page, so an XSS flaw becomes an account takeover. HttpOnly cookies for refresh tokens and short-lived in-memory access tokens are safer.

### Which cookie flags should session cookies have?

HttpOnly, Secure and SameSite (Lax or Strict), with a narrow path and domain.

### Does logging out invalidate a token?

Only if the server revokes it. Many AI-generated apps just delete it from the browser, leaving it valid.

### Why does Manifera review sessions in every security check?

Because session flaws turn small bugs into account takeovers. Manifera's cybersecurity roots make sessions, tokens and cookies standard review items.

### Do secure cookie settings affect SEO or analytics?

Session cookies do not affect SEO. Proper security headers and HTTPS contribute to browser and search trust signals, and correctly scoped cookies avoid conflicts with analytics tools.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Is storing tokens in localStorage insecure?", "acceptedAnswer": { "@type": "Answer", "text": "It exposes tokens to page scripts; use HttpOnly cookies for refresh tokens and short-lived in-memory access tokens." } },
    { "@type": "Question", "name": "Which cookie flags should session cookies have?", "acceptedAnswer": { "@type": "Answer", "text": "HttpOnly, Secure and SameSite, with narrow path and domain." } },
    { "@type": "Question", "name": "Does logging out invalidate a token?", "acceptedAnswer": { "@type": "Answer", "text": "Only if revoked server-side; many AI apps just delete it in the browser." } },
    { "@type": "Question", "name": "Why does Manifera review sessions in every security check?", "acceptedAnswer": { "@type": "Answer", "text": "Session flaws turn small bugs into takeovers; cybersecurity roots make them standard checks." } },
    { "@type": "Question", "name": "Do secure cookie settings affect SEO or analytics?", "acceptedAnswer": { "@type": "Answer", "text": "Not SEO directly; HTTPS and headers support trust, and scoped cookies avoid analytics conflicts." } }
  ]
}
</script>
