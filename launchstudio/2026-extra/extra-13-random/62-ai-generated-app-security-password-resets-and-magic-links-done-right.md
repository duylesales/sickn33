---
Title: "AI Generated App Security: Password Resets and Magic Links Done Right"
Keywords: ai generated app security, password reset security, magic link login, account takeover, cursor auth, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI Generated App Security: Password Resets and Magic Links Done Right

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Generated App Security: Password Resets and Magic Links Done Right",
  "description": "Password reset and magic-link flows are the quiet back door of AI generated app security. This article covers token entropy, expiry, single use, host header poisoning, enumeration, session invalidation and email delivery — with a checklist for technical founders.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-01",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-generated-app-security-password-resets-and-magic-links-done-right" }
}
</script>

Attackers rarely break your login form. They go around it. The password reset flow — and its cousin, the magic link — is a second way into every account, and in AI generated app security it is one of the least examined parts of the codebase. The login screen gets attention because everyone uses it. The reset flow is used rarely, tested once and then forgotten, which is exactly what makes it attractive.

If your auth runs fully on a mature provider such as Supabase Auth, Auth0 or Firebase Auth, most of this is handled for you — as long as you have not wrapped it in custom code. The trouble starts when an AI tool generates its own reset logic, or its own "passwordless" login, on top.

## What a Reset Link Really Is

A reset link is a temporary password. Whoever holds it can take over the account. Every property that matters for a password matters for the token in that link: how hard it is to guess, how long it lasts, where it travels and whether it can be reused.

## AI Generated App Security: Seven Mistakes in Reset Flows

**1. Guessable tokens.** Tokens built from `Math.random()`, timestamps, user IDs or short numeric codes can be predicted or brute-forced. Tokens must come from a cryptographically secure random generator and be long enough — 128 bits or more.

**2. No expiry, or a long one.** Links that work for days or forever turn every old email in someone's inbox into a key. Fifteen to sixty minutes is typical for resets; magic links are often shorter.

**3. Reusable tokens.** After a successful reset, the token should be invalidated. Many generated flows leave it valid, so anyone who later sees the link — in a forwarded email, a shared screen, browser history — can use it again.

**4. Tokens stored in plain text.** If the database stores reset tokens as-is, anyone with read access to that table, or a leaked backup, can take over accounts with pending resets. Store a hash, as you would a password.

**5. Host header poisoning.** Generated code often builds the reset URL from the incoming request's host header. An attacker who requests a reset for your account while sending a forged host header can make the email you receive point to their domain; when you click it, they receive your token. Build URLs from a fixed, configured base URL.

**6. Enumeration.** "No account found with that email" tells an attacker which addresses are customers. Always respond with the same message.

**7. Sessions survive the reset.** When someone resets a password — often because they suspect compromise — existing sessions elsewhere should end. AI-generated flows usually just update the password hash.

## Magic Links Have the Same Rules, and One More

Magic links are password resets used as login. Everything above applies, plus a consideration about where the link is opened. Some corporate email systems and security scanners "click" links automatically to check them, which can consume single-use tokens before the user does. Common solutions include a confirmation page that requires a button press to complete login, or short one-time codes as an alternative.

## Rate Limits and Monitoring

Reset and magic-link endpoints need rate limits per email and per IP, both to prevent enumeration at scale and to stop your email provider from being used to spam people. Log reset requests and completions, and alert on unusual spikes.

## Email Delivery Is Part of Security

A reset email that lands in spam is a support ticket; a reset email sent from an unauthenticated domain teaches users to trust phishing lookalikes. Use a transactional email provider, publish SPF, DKIM and DMARC records, and keep reset emails plain, branded and consistent.

## A Checklist for Your Codebase

- Tokens from a secure random generator, 128+ bits
- Stored hashed, with expiry and single use
- Reset URL built from configured base URL, never the request host
- Identical response for known and unknown emails
- Rate limited per email and IP
- All sessions revoked after reset; user notified by email
- Magic links protected against scanner pre-clicks
- Transactional email with authenticated domain

The [OWASP Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html) goes into more depth and is short enough to read in one sitting.

## Generating and Storing Reset Tokens Correctly

A correct implementation of reset tokens for AI generated app security is short, and worth seeing:

```typescript
import { randomBytes, createHash } from "crypto";

export function createResetToken() {
  const token = randomBytes(32).toString("base64url");       // sent to the user
  const tokenHash = createHash("sha256").update(token).digest("hex"); // stored
  const expiresAt = new Date(Date.now() + 30 * 60 * 1000);   // 30 minutes
  return { token, tokenHash, expiresAt };
}
```

The database stores only `tokenHash`, `user_id`, `expires_at` and `used_at`. When the user clicks the link, the app hashes the received token, looks up a matching unexpired, unused record, marks it used in the same transaction as the password change and revokes other sessions. If the database leaks, the stored hashes are useless to an attacker; if the email leaks after use, the token is already spent.

## Building URLs Safely

The reset link must be built from configuration, never from the incoming request:

```typescript
const base = process.env.APP_BASE_URL; // e.g. https://app.example.nl
const link = `${base}/reset-password?token=${encodeURIComponent(token)}`;
```

Validate at startup that `APP_BASE_URL` is set and uses HTTPS in production. This single rule eliminates host header poisoning, one of the more elegant ways attackers steal reset tokens.

## Rate Limiting Reset and Login Endpoints

Sensible limits for small apps:

| Endpoint | Per email | Per IP | Response when exceeded |
| --- | --- | --- | --- |
| Request reset / magic link | 3–5 per hour | 20 per hour | Same generic message; no email sent |
| Submit reset token | 5 attempts per token | 30 per hour | Invalidate token after limit |
| Login | 5–10 failures per 15 min | 50 per 15 min | Temporary lock, generic message |
| One-time code verification | 5 attempts per code | 30 per hour | Invalidate code |

Limits should be enforced on the server, ideally in a shared store so they hold across serverless instances. Log limit hits; a spike is often the first sign of credential stuffing or enumeration.

## Choosing Between Links and Codes

Magic links are convenient on the same device; one-time codes work better when users read email on a phone and log in on a laptop. Many apps offer both. For codes, use at least six digits with strict attempt limits and short expiry, or longer alphanumeric codes; for links, use long random tokens. In both cases, bind the token to the email address and, if possible, to the browser session that requested it, so a code intercepted elsewhere is less useful.

## Account Recovery Beyond Email

If a user loses access to their email, recovery becomes a support process — and a social-engineering target. Define in advance what evidence you accept (for example access to a verified phone number, recent payment details or identity verification for high-value accounts), log recovery actions, notify the old email address of the change and apply a cooling-off period before sensitive actions. For apps holding sensitive data, offer two-factor authentication with recovery codes, so users can recover without support.

## Notifications That Help Users Spot Attacks

Send an email when a password is changed, a new device logs in, the email address is changed or two-factor authentication is disabled. Include "this wasn't me" guidance with a link to secure the account. These notifications cost almost nothing and turn users into an early-warning system for account takeover.

## Testing Authentication Flows

Authentication deserves dedicated tests: tokens expire, cannot be reused, and do not work for other accounts; reset links use the configured base URL; sessions are revoked after a password change; rate limits trigger at the right thresholds; and responses are identical for known and unknown emails. Add them to CI so AI-assisted changes to auth code cannot quietly weaken these properties.

## When to Use Your Provider's Flows

Mature auth providers implement most of the above by default. The most reliable approach for AI-built apps is usually to use the provider's reset and magic-link flows directly, configure expiry, redirect URLs and rate limits in the provider's settings, and avoid wrapping them in custom code unless there is a clear need. Most vulnerabilities in this area come from custom wrappers, not from the providers themselves.

## Two-Factor Authentication as the Next Step

For apps holding sensitive data or admin powers, offer two-factor authentication. Authenticator apps (TOTP) and passkeys are stronger than SMS codes, which are vulnerable to SIM swapping. Provide recovery codes at setup, allow users to manage devices, and require re-authentication before disabling two-factor authentication. For staff and admin accounts, make it mandatory. Most auth providers support these features; enabling them is often a configuration task rather than a development project.

## Passkeys: Where Authentication Is Heading

Passkeys replace passwords with cryptographic credentials stored on users' devices and synced by their platform. They are resistant to phishing and credential stuffing and remove the need for password resets in many cases. Support is growing across browsers, operating systems and auth providers. For new AI-built apps, offering passkeys alongside email-based login is an increasingly practical option — and it reduces the attack surface this article describes.

## Common Questions From Users

Users sometimes ask why reset links expire quickly or why they did not receive an email. Answer both in your help pages: links expire to protect accounts; emails may take a minute or land in spam; for security reasons the app does not say whether an email address has an account. Clear explanations reduce support requests and help users understand that friction is protection.

## A Final Check Before Launch

Request a reset for a real account and inspect everything: the email's sender domain, the link's host, how long it works, whether it works twice, whether other sessions end after use and whether you receive a notification. Then request a reset for an address that does not exist and compare the response. Ten minutes of testing verifies the whole flow end to end.

## Why This Deserves Founder Attention

Password reset and magic-link flows rarely appear in demos, and founders rarely click them after launch. Yet they decide whether an attacker can take over an account without ever knowing its password. A few hours spent on token strength, expiry, single use, safe URLs, rate limits and session revocation protects every account in your app — including your own admin account, which is often the most valuable target of all. Put the checks on your launch list next to payments and access control, where they belong.

## Where LaunchStudio Fits

LaunchStudio reviews authentication flows as part of every security pass, and reset and magic-link logic is where custom AI-generated code most often needs replacing with a provider's built-in flow or a hardened implementation. LaunchStudio is powered by Manifera, whose CEO Herre Roelevink started his career in cybersecurity — he co-founded CyberDevOps, now CFLW Cyber Strategies — and whose engineers in Ho Chi Minh City have built authentication for enterprise systems for more than 11 years. See [Manifera's about page](https://www.manifera.com/about-us/).

If you are not sure who wrote your reset flow, [talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: A Cleaning Company Scheduler With a Six-Digit Back Door

Tijmen Boersma, who runs a commercial cleaning company in Almelo, built Poetsplan with Cursor: a scheduling SaaS for cleaning companies, where planners assign cleaners to office buildings and clients see completed rounds and building access notes — including alarm codes. Twenty-two cleaning companies in Twente used it.

Tijmen had asked Cursor for "passwordless login with a code by email." The result sent a six-digit numeric code, valid for 24 hours, with no limit on attempts. A security-minded client tested it and guessed his way into a test account within an afternoon using a simple script. The review found more: the separate password reset flow built its link from the request's host header, tokens were stored in plain text, reset did not end other sessions, and the login form said "unknown email" for non-customers.

LaunchStudio's engineers replaced the custom login and reset code with Supabase Auth's built-in flows, configured ten-minute expiry, single-use hashed tokens and a confirmation step to survive email scanners, added rate limits per email and IP with attempt lockouts, fixed reset URLs to a configured base URL, revoked all sessions on password change with a notification email, unified error messages and moved sending to an authenticated domain. Alarm codes were additionally restricted to the planner role.

**Result:** The client's follow-up test found no way in, and Poetsplan passed that client's supplier security check. It has since grown to 35 cleaning companies.

> *"I asked for convenience and got a lock with six digits and unlimited guesses. The fix was mostly using what my auth provider already did properly."*
> — **Tijmen Boersma, Founder, Poetsplan (Almelo)**

**Cost & Timeline:** €1,150 (authentication flow replacement, rate limiting, session handling and email setup) — completed in 4 business days.

## Frequently Asked Questions

### How long should a password reset link stay valid?

Typically 15 to 60 minutes, used only once. Magic-login links are often shorter. Longer lifetimes turn old emails into standing keys to accounts.

### Are six-digit email codes safe for login?

Only with strict rate limits, short expiry and lockouts. Without them, a six-digit code can be brute-forced quickly. Long random links or provider-managed flows are safer defaults.

### Should I build my own reset flow or use my auth provider's?

Use the provider's built-in flow wherever possible. Custom flows are where AI-generated code most often introduces guessable tokens, missing expiry and host header issues.

### Why does Manifera emphasise authentication in every review?

Account takeover is one of the most damaging and common attacks on small apps. Manifera's cybersecurity roots, through Herre Roelevink's earlier work, make auth flows a standard first check rather than an optional extra.

### Does secure login affect trust signals online?

Indirectly. Account takeovers lead to public complaints and reviews that search engines and AI answer engines surface. Clean, authenticated emails also protect your domain's reputation with inbox providers.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "How long should a password reset link stay valid?", "acceptedAnswer": { "@type": "Answer", "text": "Typically 15 to 60 minutes and single use; magic links often shorter." } },
    { "@type": "Question", "name": "Are six-digit email codes safe for login?", "acceptedAnswer": { "@type": "Answer", "text": "Only with strict rate limits, short expiry and lockouts; otherwise they can be brute-forced." } },
    { "@type": "Question", "name": "Should I build my own reset flow or use my auth provider's?", "acceptedAnswer": { "@type": "Answer", "text": "Use the provider's built-in flow; custom flows are where AI code introduces weak tokens and host header issues." } },
    { "@type": "Question", "name": "Why does Manifera emphasise authentication in every review?", "acceptedAnswer": { "@type": "Answer", "text": "Account takeover is common and damaging; Manifera's cybersecurity roots make auth a standard first check." } },
    { "@type": "Question", "name": "Does secure login affect trust signals online?", "acceptedAnswer": { "@type": "Answer", "text": "Indirectly, by preventing takeover complaints and protecting email domain reputation." } }
  ]
}
</script>
