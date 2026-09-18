---
Title: "AI App Security: Sessions, Cookies and Staying Logged In Safely"
Keywords: ai app security, session management, httpOnly cookies, token storage, session revocation, CSRF, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI App Security: Sessions, Cookies and Staying Logged In Safely

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Security: Sessions, Cookies and Staying Logged In Safely",
  "description": "Where an AI-built app keeps its session token decides how bad a cross-site scripting bug becomes. Storage choices, expiry that suits your product, revoking a stolen session, and the sign-out that does not.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-10",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-app-security-sessions-cookies-and-staying-logged-in-safely" }
}
</script>

A session is the answer to a question your application asks on every request: who is this. Get it wrong and every other control you have built is decoration, because an attacker holding a valid session is your customer as far as your code is concerned.

AI-built applications tend to get the happy path right — people log in, they stay logged in, they log out — and to leave three things unconsidered: where the token lives, how long it lasts, and what you can do when one is stolen.

The third is the one founders discover they need at the worst moment.

## Where the Token Lives Decides How Bad XSS Gets

Two options, and the difference is not subtle.

**Local storage** is readable by any JavaScript running on your page. That includes your code, every dependency you installed, anything injected through a cross-site scripting flaw, and any third-party script you added for analytics or support chat. One XSS bug anywhere in your application means every session token can be read and exfiltrated.

**An httpOnly cookie** cannot be read by JavaScript at all. The browser attaches it to requests automatically and your code never sees it. The same XSS bug is now much less valuable: the attacker can act within the page while the victim is there, but cannot take the session away and use it elsewhere at leisure.

Most AI-generated authentication code uses local storage, because it is the simplest thing that works and because many client libraries default to it. Moving to cookies is a configuration change in some stacks and a day's work in others, and it is the single highest-value change in this article.

The cookie needs three attributes to be worth having: httpOnly so script cannot read it, secure so it only travels over HTTPS, and sameSite set to lax or strict so it is not sent on cross-site requests. With sameSite lax, most CSRF risk disappears; for anything sensitive, add an explicit CSRF token as well.

## Expiry Should Match Your Product

There is no universally correct session length. There is a correct one for what your product does.

A tool people use all day from a fixed desk — a planning board, a workshop system — can keep people signed in for weeks, because forcing a login every morning produces shared accounts and written-down passwords. A product handling health, financial or personal data on shared devices needs hours.

Two mechanisms, used together. A short-lived access token, valid for minutes, which limits the window in which a stolen one is useful. And a longer-lived refresh token that quietly issues new access tokens, so the user is not interrupted. Most authentication providers, including Supabase, do this by default — the part founders must decide is the refresh token's lifetime, which is the real answer to "how long do people stay logged in".

Add an idle timeout where the data warrants it: sessions that end after a period of inactivity, separate from absolute expiry. And be deliberate about "remember me" — it should extend the refresh lifetime, not disable expiry entirely.

## You Must Be Able to End a Session

This is the capability most small products lack and the one that matters in an incident.

If a laptop is stolen, a phone is lost, an employee leaves, or a token is suspected stolen, someone must be able to end that session immediately. With stateless tokens that are valid until they expire, the honest answer is often that you cannot — the token works until it ages out, whatever you do.

Two things make revocation real. Keep a record of active sessions, so refresh tokens can be invalidated and a session genuinely ends. And provide the two actions people need: sign out everywhere, available to the user, and force sign-out for an account, available to you.

While you are building that, show the user their active sessions — device, approximate location, last used. It costs little, it is the feature that lets a customer notice a session they do not recognise, and it is increasingly expected by business buyers reading your security page.

## Sign-Out Must Actually Sign Out

Test this on your own product. Sign out, then use the browser's back button, then try an action.

In a surprising number of AI-built applications, signing out clears the interface and leaves the session valid. The token was removed from the client, or not, and nothing was invalidated on the server. Anyone with the device — or with a copy of the token — remains authenticated.

Signing out must invalidate the session server-side, clear the cookie, and discard any cached user data the client is holding. That last part is where generated code leaks: a data-fetching library keeps the previous user's responses in memory, and the next person to sign in on that device sees a flash of somebody else's dashboard before their own loads.

## Rotate on Privilege Change

Two moments require a new session identifier rather than a reused one.

**At login.** If a session identifier issued before authentication survives it, an attacker who planted that identifier in a victim's browser is now sharing their authenticated session. This is session fixation, and the defence is simply to issue a fresh session on successful login.

**On password change.** Changing a password should end every other session for that account. It is what users expect the action to mean, and it is the natural response to "I think someone has access" — which is why the person doing it usually needs it to work.

## Multi-Tenant Products Have a Second Question

For a product where one person can belong to several organisations — an accountant serving twelve clients, a consultant working across three customers — the session answers who, and something else must answer which.

The mistake is to keep the current organisation in the client and send it with each request. Whatever the browser sends, the browser can change, so an identifier posted from the page is a request rather than a fact. Products built this way are one edited value away from a customer reading another customer's data, and it is among the most common serious findings in multi-tenant applications built quickly.

The correct arrangement stores the active organisation server-side as part of the session, changed only through an explicit action that verifies membership. Every subsequent request then derives the organisation from the session, and the client cannot influence it at all.

Two details follow. Switching organisation should rotate or at least update the session record, so the change is auditable — knowing which context an action was taken in matters when somebody asks what happened. And every query must still filter by the organisation from the session rather than trusting a value passed into a function, because the boundary is only as good as its least careful call site.

Test it the way an attacker would: sign in as a user belonging to two organisations, act in one, then replay the same request with the other organisation's identifier substituted. The correct response is a refusal.

## What to Put in a Token, and What to Look Up

Tokens can carry claims — the user's role, their organisation, their permissions — and doing so avoids a database lookup on every request. It also freezes those values for the token's lifetime, which is the trade nobody explains.

A role embedded in an access token valid for an hour means a user demoted from administrator keeps administrative access for up to an hour. For most products that is acceptable for a short-lived token and unacceptable for a long-lived one, which is another argument for short access tokens with frequent refresh.

The practical division: put identity in the token — who this is, which session — and look up authority. Roles, permissions, subscription state and organisation membership are read from your database as part of the entitlement check that every meaningful endpoint runs anyway. The lookup is one indexed query, it is cached briefly if it matters, and it means a permission change takes effect on the next request rather than at the next login.

Two related habits. Never trust a claim the client could have influenced — if a value arrived in a request body rather than in a signed token, it is input. And verify the token's signature and expiry on every request, on the server, rather than decoding it and reading the fields, which is a mistake that appears in generated code more often than it should.

## Setting This Up

For an existing product this is typically one day: session tokens moved from local storage into httpOnly, secure, sameSite cookies with CSRF protection where needed, access and refresh lifetimes chosen to suit the product with an idle timeout where the data warrants it, a server-side record of active sessions enabling genuine revocation, sign-out-everywhere for users and force sign-out for support, a visible active session list, sign-out verified to invalidate server-side and clear client caches, and session rotation at login and on password change.

LaunchStudio covers this in security review, and the local storage finding appears in the clear majority of AI-built applications we look at. The engineers are Manifera's — eleven years, 120+ engineers, for clients including Vodafone, TNO and CFLW.

[Ask us to check where your app keeps its token](https://launchstudio.eu/en/#contact). It takes two minutes and decides how much a future bug costs you.

## Real example

### A Session That Outlived the Employee

Roos Verhagen built Zorgplanning in Lovable: shift planning and client scheduling for home care organisations, 18 organisations covering around 900 carers.

A planner at one organisation left after a disagreement. The organisation's manager removed her account on her last day and considered the matter closed.

Three weeks later, changes appeared in the schedule that nobody could account for: shifts reassigned overnight, two client visits removed. The former planner's tablet still had the application open, and the session was still valid, because the refresh token issued at her last login had a 90-day lifetime and deleting the account row had not invalidated it. Her browser continued refreshing access tokens against a user record that no longer existed, and the application — which checked the token rather than the account — kept accepting them.

Two business days: session tokens moved from local storage to httpOnly secure sameSite cookies, with CSRF tokens on state-changing requests; a sessions table recording every active session with device, last-used time and approximate location; account deactivation extended to invalidate all sessions immediately, as was password change; sign-out-everywhere added for users and force sign-out for organisation administrators, who can now end a departing employee's access themselves; the access token lifetime shortened to 30 minutes with a 14-day refresh lifetime, chosen with the organisations rather than by default, plus a 12-hour idle timeout appropriate to shared tablets in care locations; sign-out corrected to invalidate server-side and clear the client data cache, which had been showing the previous user's client list for a second after switching; session rotation at login; and a visible active-sessions screen.

**Result:** the unauthorised changes were reconstructed from the audit trail and corrected, and the organisation reported the incident internally as required. The active-sessions screen has since been used by three organisations to find tablets left signed in at client locations — a problem none of them knew they had.

> *"We deleted her account. Everyone in the room believed that meant she was out. Her tablet kept working for three weeks."*
> — **Roos Verhagen, Founder, Zorgplanning (Apeldoorn)**

**Cost & Timeline:** €2,700 (cookie-based session storage with CSRF protection, session records and revocation, deactivation and password-change invalidation, sign-out-everywhere and administrator force sign-out, lifetime and idle policy, sign-out and cache correction, session rotation, active session screen) — completed in 2 business days.

## Frequently Asked Questions

### Is local storage safe for session tokens?

No. Any JavaScript on your page can read it, including injected script and third-party libraries. An httpOnly cookie cannot be read by script, which greatly reduces what an XSS bug is worth.

### How long should users stay logged in?

Match the product. All-day internal tools can run for weeks; anything handling health, financial or personal data on shared devices should be hours, with an idle timeout.

### Can I end a session before it expires?

Only if you keep a server-side record of sessions and invalidate refresh tokens. Without that, a stateless token remains valid until it ages out regardless of what you do.

### Does deleting a user account end their sessions?

Not automatically. Account deactivation, password change and administrator removal must all explicitly invalidate sessions, or a signed-in device keeps working.

### What does correct sign-out involve?

Invalidating the session server-side, clearing the cookie, and discarding cached data on the client. Clearing the interface alone leaves the session valid and can show the previous user's data.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is local storage safe for session tokens?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — any script on the page can read it. httpOnly cookies are unreadable by JavaScript, which greatly limits the damage of an XSS bug."
      }
    },
    {
      "@type": "Question",
      "name": "How long should a session last?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Match the product: weeks for all-day internal tools, hours with an idle timeout for sensitive data on shared devices."
      }
    },
    {
      "@type": "Question",
      "name": "Can a session be revoked before it expires?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Only with a server-side record of sessions and refresh token invalidation. Otherwise a stateless token stays valid until it ages out."
      }
    },
    {
      "@type": "Question",
      "name": "Does deleting a user end their active sessions?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not by default. Deactivation, password change and administrator removal must each explicitly invalidate sessions."
      }
    },
    {
      "@type": "Question",
      "name": "What must sign-out actually do?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Invalidate server-side, clear the cookie and discard client-side cached data — clearing only the interface leaves the session usable."
      }
    }
  ]
}
</script>
