---
Title: "Why Did My App Stop Working Overnight? The Silent Expiry Checklist"
Keywords: app stopped working overnight, website down suddenly, ssl certificate expired app, api key expired, supabase project paused, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# Why Did My App Stop Working Overnight? The Silent Expiry Checklist

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Why Did My App Stop Working Overnight? The Silent Expiry Checklist",
  "description": "An AI-built app that worked yesterday can fail today without anyone changing code. The usual causes are things that expire or run out: domains, SSL certificates, API keys and tokens, credit cards on service accounts, free-tier quotas, paused projects, deprecated APIs and model versions. This guide explains how to diagnose a sudden outage and how to track every expiry date before it hits.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-07-26",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/why-did-my-app-stop-working-overnight" },
  "citation": [
    { "@type": "CreativeWork", "name": "Let's Encrypt: Certificate lifetimes", "url": "https://letsencrypt.org/docs/faq/" },
    { "@type": "CreativeWork", "name": "Supabase: Billing and usage", "url": "https://supabase.com/docs/guides/platform/billing-on-supabase" },
    { "@type": "CreativeWork", "name": "Google SRE Book: Monitoring Distributed Systems", "url": "https://sre.google/sre-book/monitoring-distributed-systems/" },
    { "@type": "CreativeWork", "name": "SIDN: .nl domain names", "url": "https://www.sidn.nl/en" }
  ]
}
</script>

**Short answer:** when an app stops working overnight and nobody changed anything, something usually expired, ran out or was switched off by a provider. The common culprits are a domain registration that lapsed, an SSL certificate that did not renew, an API key, OAuth token or app password that expired, a credit card on a service account that failed so the service was suspended, a free-tier quota exhausted or a project paused for inactivity, and an API version or AI model that the provider retired. Check your status pages and provider emails first, then work through the checklist below. Afterwards, list every account, key and renewal date in one place, put it in monitoring and give yourself warnings weeks in advance.

## Key Takeaways

- **"Nothing changed" usually means "something expired".** Code does not break by itself; dependencies do.
- **Provider emails are the fastest clue:** failed payments, quota warnings and deprecation notices often arrived weeks earlier.
- **Expiries hide in many places:** domains, certificates, keys, tokens, cards, plans and API versions.
- **Founders' personal accounts** are a frequent single point of failure.
- **An expiry register plus monitoring** turns surprise outages into routine renewals.

## First: Is It You or Them?

Before anything else:

- **Check provider status pages:** Supabase, Vercel, Netlify, Cloudflare, Stripe, Mollie, your AI provider and email service. A regional outage needs patience, not fixes.
- **Search your email,** including spam, for messages from those providers in the past month: "payment failed", "action required", "deprecation", "quota", "expiring".
- **Note exactly what fails:** the whole site, login, payments, emails, AI features or one integration.
- **Read error messages** in the browser console and server logs. An expired certificate, a 401 from an API or a "project paused" message is usually explicit.

## Cause 1: The Domain Expired

Domains are registered for a year or more and must be renewed. If auto-renewal was off, or the card on the registrar account expired, the domain stops resolving or shows a parking page. Email on that domain stops too.

**Fix:** renew immediately at the registrar; most have a grace period. Then enable auto-renewal, register for several years and make sure renewal notices go to an address someone reads. Our guide on [DNS setup for launch](https://launchstudio.eu/en/blog/dns-setup-for-launch-domain-email-and-ssl) covers domain setup.

## Cause 2: The SSL Certificate Did Not Renew

Most hosts renew certificates automatically, typically every few months. Renewal fails when DNS records change, a CDN blocks the validation request, a custom server's renewal job stopped or a domain was moved. Browsers then show a full-page security warning, which most users will not click past.

**Fix:** find out why renewal failed in the host's dashboard, correct DNS or proxy settings and trigger renewal. Add certificate expiry monitoring, which most uptime tools offer.

## Cause 3: Keys and Tokens Expired

Many integrations use credentials with a limited lifetime:

- **OAuth tokens** for Google, Microsoft, accounting systems or social platforms, which need refresh and sometimes re-authorisation.
- **API keys** with an expiry date set at creation.
- **App passwords and SMTP credentials** revoked after a password change.
- **Apple sign-in and push certificates** that expire yearly.
- **Webhook signing secrets** rotated by a team member.

**Fix:** renew the credential, store the new one in server secrets and redeploy. Record expiry dates and implement token refresh properly. Make sure integrations fail visibly, with an alert, rather than silently.

## Cause 4: A Payment Failed and the Service Was Suspended

Hosting, database, email, SMS and AI providers charge monthly. If the card expired or was blocked, the provider retries a few times, sends emails and then suspends or downgrades the account. AI APIs with prepaid credit simply stop when the balance reaches zero.

**Fix:** update the payment method and contact support for reactivation. Then move all service billing to a company card with a known expiry date, use invoices where available and set up low-balance alerts for prepaid services. See [what it costs to run an AI-built app per month](https://launchstudio.eu/en/blog/how-much-does-it-cost-to-run-an-ai-built-app-per-month).

## Cause 5: Quotas, Limits and Paused Projects

Free and entry plans have limits: database size, bandwidth, function invocations, emails per day, AI tokens per minute. Exceeding them can block requests or switch features off. On Supabase's free plan, inactive projects are paused after a period without activity, which surprises founders with apps that are used only occasionally.

**Fix:** check usage dashboards, upgrade where needed and set usage alerts below the limits. For production with paying customers, move off free plans; our guide on [whether you need a paid Supabase plan](https://launchstudio.eu/en/blog/do-i-need-a-paid-supabase-plan-for-production) explains why. If AI costs spike, see [stopping AI API costs from exploding](https://launchstudio.eu/en/blog/how-do-i-stop-ai-api-costs-from-exploding).

## Cause 6: Deprecated APIs and Models

Providers retire old API versions, SDK features and AI models on announced dates. On that day, requests to the old version start failing. Deprecation emails often go to whoever created the account, possibly years ago.

**Fix:** move to the supported version, test and deploy. Then keep a list of external APIs and model versions you depend on, with their deprecation dates, and subscribe to provider changelogs. Our guide on [AI feature fallbacks](https://launchstudio.eu/en/blog/ai-feature-fallbacks-when-the-model-api-is-down) covers handling model changes gracefully.

## Cause 7: Time-Based Bugs

Some failures are triggered by the calendar: a trial period ending for all users created in a campaign, a hard-coded year, daylight saving time changes, a scheduled job that runs on the first of the month or a date filter that excludes everything after a certain point. Our guide on [timezone and date bugs](https://launchstudio.eu/en/blog/timezone-and-date-bugs-in-ai-built-apps) covers these.

## The Overnight Outage Checklist

| Check | Where to look | Sign it is the cause |
| --- | --- | --- |
| Provider status | Status pages | Reported incident |
| Domain | Registrar dashboard, WHOIS | Expired or parking page |
| SSL certificate | Browser warning, host dashboard | Certificate expired |
| Billing | Provider emails and accounts | Failed payment, suspension |
| Quotas and pauses | Usage dashboards | Limit reached, project paused |
| Keys and tokens | Integration logs | 401 or 403 errors |
| API and model versions | Provider changelogs | Deprecated or not found errors |
| Calendar logic | Recent date boundaries | Failures started at midnight or month start |

## Prevention: The Expiry Register

Create one document, owned by the company, that lists:

- **Every account:** registrar, DNS, host, database, email, SMS, payments, AI providers, app stores, analytics, monitoring.
- **Who owns it and the login email:** a company address, not a personal one, with two-factor authentication and at least two people with access.
- **Billing method and card expiry date.**
- **Renewal and expiry dates:** domains, certificates where manual, keys, tokens, Apple certificates, contracts.
- **Plan limits** and the alert thresholds you set.
- **API and model versions** in use and known deprecation dates.

Add calendar reminders for every date, 30 and 7 days ahead. Combine it with uptime monitoring and alerts; our guide on [knowing when your app goes down](https://launchstudio.eu/en/blog/how-do-i-know-when-my-ai-built-app-goes-down) explains the setup.

## How LaunchStudio Helps

LaunchStudio restores and protects AI-built apps after sudden outages: fast diagnosis, recovery of domains, certificates, credentials and suspended services, migration of accounts to company ownership, upgrade of plans where needed, an expiry register, and monitoring for uptime, certificates, quotas, failed integrations and deprecations.

The **Launch Ready** package (€800-€3,500) covers recovery, account consolidation and monitoring setup with security hardening; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting where renewals and monitoring are handled for you, with priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Monday Morning Everything Broke at Once

Roos van Dam built Oppaskompas with Bolt and Supabase: a platform where parents find and book babysitters, with in-app messaging, payments through Mollie and AI-assisted profile checks. About 2,800 families and 600 babysitters used it in and around Breda.

One Monday morning, nothing worked. The app showed a certificate warning, emails were not arriving and, once the warning was bypassed in testing, the AI profile checks and SMS reminders failed. Roos had changed nothing in weeks. The investigation found four separate expiries converging. The personal credit card she had used for most services had expired at the end of the previous month; the SMS provider had suspended the account after failed payments, and the AI provider's prepaid credit had run out because auto-recharge failed. The SSL certificate had not renewed because, two months earlier, a Cloudflare setting had been changed that blocked the validation request; renewal reminders went to the email address of a freelancer who had set up DNS. And the email service had revoked an SMTP credential after a password reset, which Roos had not connected to the app.

LaunchStudio restored service the same morning: certificate validation was fixed and renewed, billing was moved to a company card on every service, the SMS account was reactivated, AI credit was topped up with alerts and the SMTP connection was replaced with an API key stored in server secrets. In the following days, all accounts were moved to company email addresses with two-factor authentication and a second admin, DNS ownership was transferred from the freelancer, and an expiry register was created with calendar reminders. Monitoring now covers uptime, certificate expiry, failed email and SMS sends, AI errors and low credit balances.

**Result:** The app was fully available again within four hours. In the following year, the register and alerts flagged eleven renewals and two quota warnings ahead of time, and Oppaskompas has not had an unplanned outage since.

> *"Nothing in my code broke. My app died of a dead credit card, an old email address and a certificate nobody was watching."*
> - **Roos van Dam, Founder, Oppaskompas (Breda)**

**Cost & Timeline:** €1,500 (Launch Ready package: emergency recovery, account consolidation, DNS ownership transfer, expiry register and monitoring) - completed in 4 business days, with service restored on day one.

## Frequently Asked Questions

### Why did my app stop working when nobody changed anything?

Usually because something expired or ran out: a domain, SSL certificate, API key or token, payment method on a service account, a quota, or an API version that was retired. Provider emails and status pages are the fastest way to find which.

### How do I prevent my SSL certificate from expiring?

Use your host's automatic renewal, make sure DNS and CDN settings allow validation, and add certificate expiry monitoring that alerts you weeks before the expiry date.

### Why was my Supabase project paused?

Free-plan projects can be paused after a period of inactivity. Paid plans are not paused this way. For an app with real users, a paid plan avoids this and adds backups and support.

### How does Manifera's experience help with outages?

Manifera has operated production systems for clients for 11+ years, where renewals, credentials and monitoring are managed routinely. LaunchStudio brings that operational discipline to AI-built apps.

### Does downtime affect SEO or AI visibility?

Yes. Extended downtime or certificate warnings stop crawlers from accessing pages and can harm rankings if repeated. Reliable uptime and valid certificates are basic requirements for being found and cited.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why did my app stop working when nobody changed anything?",
      "acceptedAnswer": { "@type": "Answer", "text": "Something expired or ran out: domain, certificate, key, payment method, quota or a retired API version." }
    },
    {
      "@type": "Question",
      "name": "How do I prevent my SSL certificate from expiring?",
      "acceptedAnswer": { "@type": "Answer", "text": "Use automatic renewal, allow validation through DNS and CDN, and monitor certificate expiry." }
    },
    {
      "@type": "Question",
      "name": "Why was my Supabase project paused?",
      "acceptedAnswer": { "@type": "Answer", "text": "Free-plan projects can be paused after inactivity; paid plans avoid this." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with outages?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has operated production systems for 11+ years with managed renewals and monitoring." }
    },
    {
      "@type": "Question",
      "name": "Does downtime affect SEO or AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; downtime and certificate warnings block crawlers and can harm rankings." }
    }
  ]
}
</script>
