---
Title: "The SSL Certificate Is the Easy Part — What Comes After Is the Real Security Work"
Keywords: web security beyond SSL, security headers SaaS, CORS policy AI prototype, CSRF protection Next.js, production security checklist, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# The SSL Certificate Is the Easy Part — What Comes After Is the Real Security Work

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The SSL Certificate Is the Easy Part — What Comes After Is the Real Security Work",
  "description": "A green padlock in the browser address bar only means your connection is encrypted. It does not mean your application is secure. Here is what real production hardening looks like behind the padlock — CSP, CORS, security headers, rate limiting, RLS, and a pre-launch security checklist.",
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
    "@id": "https://launchstudio.eu/en/blog/ssl-certificate-easy-part-real-security-work"
  }
}
</script>

When you deploy a Next.js or Lovable prototype to Vercel, Netlify, or Railway, an automated Let's Encrypt SSL/TLS certificate generates in under ten seconds. The browser displays a comforting green padlock. To non-technical observers and many first-time founders, that padlock is synonymous with "our app is secure." In reality, an SSL certificate only ensures that data in transit cannot be read by someone sniffing Wi-Fi traffic at a coffee shop. It does nothing to protect your database, your API keys, your user permissions, or your application headers from being systematically exploited. A penetration tester does not care whether your padlock is green — they care whether your `/api/admin` route checks a session token, whether your storage bucket permissions default to private, and whether your login form can survive 10,000 automated password guesses in a minute.

## The Security Layers AI Tools Routinely Omit

AI-generated code prioritizes getting features on screen quickly. In doing so, it almost always leaves out the standard HTTP security headers and defensive architectural patterns that enterprise penetration testers look for:

**1. Content Security Policy (CSP):** Without a strict CSP header, your application is vulnerable to Cross-Site Scripting (XSS). If a malicious actor injects an inline script into a comment or profile field, the browser will execute it, exposing user session cookies and authentication tokens. AI scaffolds almost never generate a CSP because it requires manually enumerating every legitimate script, style, font, and image source your app loads — a tedious, easy-to-skip step when the priority is shipping a demo.

**2. Cross-Origin Resource Sharing (CORS):** Prototype backends often default to `Access-Control-Allow-Origin: *` to avoid pesky local development browser errors. In production, this wildcard allows any malicious website visited by your logged-in user to send authenticated requests directly to your API, silently exfiltrating data using the victim's own session cookies.

**3. HTTP Security Headers:** Essential headers like `X-Frame-Options: DENY` (preventing clickjacking), `X-Content-Type-Options: nosniff`, and `Strict-Transport-Security` (HSTS, which forces browsers to refuse plain-HTTP connections even if a link is mistyped) are rarely included in default AI project scaffolds. Each one closes a specific, well-documented attack vector that automated scanners check for on the first pass.

**4. Rate Limiting & Brute Force Defenses:** A login endpoint without IP and account-level rate limiting allows automated credential-stuffing bots to test thousands of stolen password combinations every minute, often sourced from unrelated data breaches and replayed against your app hoping for password reuse.

**5. Database Row-Level Security (RLS):** Encrypting the connection to PostgreSQL is pointless if any authenticated user can query `SELECT * FROM invoices` without table-level permission filters. Supabase ships RLS disabled by default on new tables specifically so developers can move fast during prototyping — which means it is almost always still disabled the day the app goes live.

**6. Secrets Exposed to the Client Bundle:** AI copilots frequently place API keys directly in `.env` variables prefixed `NEXT_PUBLIC_` or import server-only credentials into client components, which bundlers then ship in plaintext inside the JavaScript any visitor can view via browser dev tools.

## Real Security Is Multi-Layered Defense

True application security is not a single plugin or certificate — it is a layered defense model where every tier (network, server headers, API gateway, database) assumes the other tiers might be breached and enforces its own boundaries. A penetration tester working through the OWASP Top 10 checklist does not stop looking once they confirm HTTPS is active; they treat the certificate as table stakes and spend the remaining hours probing authorization logic, input validation, and access control — the layers that actually determine whether an attacker who gets past the front door can reach anything valuable. This is why enterprise procurement teams increasingly require a signed vulnerability scan report, not just a screenshot of a padlock icon, before approving a vendor contract.

## A Pre-Launch Security Checklist

Before any AI-built prototype takes real customer data or processes payments, run through this baseline:

1. CSP header configured and tested against every legitimate asset source.
2. CORS restricted to your exact production domain(s), not a wildcard.
3. HSTS, `X-Frame-Options`, and `X-Content-Type-Options` headers set at the CDN or reverse-proxy level.
4. Rate limiting active on authentication, password reset, and billing endpoints.
5. Row-Level Security enabled and tested on every Supabase or Postgres table holding user data.
6. Storage buckets audited for accidental public read/write access.
7. Environment variables audited so no server-side secret is reachable from client bundles.
8. Dependency scan run for known CVEs in third-party packages.

[LaunchStudio](https://launchstudio.eu/en/) hardens AI prototypes using the enterprise security standards developed over 11+ years at Manifera — trusted by security-sensitive organizations including TNO and CFLW Cyber Strategies.

[Schedule a comprehensive security audit for your application](https://launchstudio.eu/en/#contact) — go live knowing your users' data is truly protected.

## Real example

### An Indie Hacker in Action: From Green Padlock to Enterprise Security Approval

Lennart de Boer, a developer in Delft, built OfferteGenie — an AI tool generating construction project quotes for commercial building contractors. He deployed on Vercel with automatic SSL and assumed his security was complete.

When his first enterprise prospect — a commercial developer with 200 staff — requested an independent security scan before signing an enterprise license, the automated report came back with 6 High and 4 Medium vulnerabilities:
- Missing CSP allowed unsafe inline script execution.
- Permissive CORS wildcard allowed cross-origin API invocation.
- The `/api/generate` endpoint had zero rate limiting, allowing unlimited OpenAI quota consumption.
- Supabase storage buckets for PDF blueprints were set to public read.

Lennart reached out to LaunchStudio. The Manifera team implemented strict security headers, configured locked-down CORS policies matching production domains, added Redis-backed distributed rate limiting on all API routes, and restructured Supabase storage with time-limited signed URLs.

**Result:** OfferteGenie re-ran the enterprise vulnerability scan, achieving a clean A+ rating and closing a €14,400 annual enterprise contract.

> *"I thought Vercel's SSL certificate meant I was secure. When the corporate security scan came back red across the board, I realized how much invisible security work goes beyond encryption in transit. LaunchStudio fixed every vulnerability in four days."*
> — **Lennart de Boer, Founder, OfferteGenie (Delft)**

**Cost & Timeline:** €1,600 (Launch Ready Package, full security header hardening + rate limiting + storage access control) — completed in 4 business days.

---

## Frequently Asked Questions

### What does an SSL certificate actually protect against?
An SSL certificate encrypts communication between the user's browser and your server, protecting passwords and data from being intercepted over untrusted networks (like public Wi-Fi).

### Why do AI tools default to permissive CORS policies?
AI tools frequently use wildcard `*` CORS headers to prevent cross-origin errors during rapid local development, but leaving them in production opens your API to unauthorized cross-site requests.

### What is Content Security Policy (CSP) and why does it matter?
CSP is an HTTP header telling the browser which domains are allowed to load scripts, styles, and images on your site, acting as the primary defense against Cross-Site Scripting (XSS) attacks.

### How does LaunchStudio prevent automated bot attacks on login endpoints?
We implement rate limiting (using token buckets or Redis) on sensitive authentication and billing endpoints, throttling suspicious request spikes before they impact performance or breach user accounts.

### Can security hardening slow down my web application?
When implemented properly at the CDN and reverse-proxy level, security headers and rate limit checks add less than 2 milliseconds of latency, keeping your app fast and responsive.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What does an SSL certificate actually protect against?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It encrypts data in transit between the client browser and your server, preventing eavesdropping on public networks, but does not protect application code or database access."
      }
    },
    {
      "@type": "Question",
      "name": "Why do AI tools default to permissive CORS policies?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "AI code generators often use wildcard CORS rules to bypass local development errors, which leaves production APIs vulnerable to unauthorized third-party site requests."
      }
    },
    {
      "@type": "Question",
      "name": "What is Content Security Policy (CSP) and why does it matter?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "CSP is an HTTP response header that restricts script execution sources, serving as the strongest protection against Cross-Site Scripting (XSS) and data injection."
      }
    },
    {
      "@type": "Question",
      "name": "How does LaunchStudio prevent automated bot attacks on login endpoints?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We deploy server-side and edge rate limiting that throttles excessive login attempts and blocks malicious brute-force patterns automatically."
      }
    },
    {
      "@type": "Question",
      "name": "Can security hardening slow down my web application?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Modern security headers and optimized rate limit middleware introduce virtually zero measurable latency (<2ms) while dramatically reducing attack surface."
      }
    }
  ]
}
</script>
