---
Title: "Case Study: Migrating a Bolt Prototype to a Custom Domain Without Downtime"
Keywords: Bolt Prototype, Custom Domain Migration, Zero Downtime, DNS Cutover, LaunchStudio, Manifera, AI App Deployment, Herre Roelevink
Buyer Stage: Decision
---

# Case Study: Migrating a Bolt Prototype to a Custom Domain Without Downtime

Moving a Bolt prototype off its default subdomain and onto a real custom domain sounds like it should be a five-minute task — update a DNS record, point it at your new domain, done. For founders who've actually tried it with an app that has active users, a live database connection, and a payment integration, it's rarely that simple, and getting it wrong means real customers hitting a broken site, a failed login, or a payment that silently doesn't go through during the cutover window. This case study walks through exactly how LaunchStudio migrated a Bolt-built SaaS app from its default `.bolt.app`-style subdomain to a fully custom domain with zero downtime and zero lost sessions, and what typically goes wrong when founders attempt this migration themselves.

## Why a "Simple" Domain Migration Actually Isn't

On the surface, migrating to a custom domain is a DNS problem: point your new domain's A or CNAME records at your hosting provider, wait for propagation, and you're done. In reality, for an app with any real functionality beyond a static page, the domain is woven into far more of the system than founders expect:

- **Authentication callbacks.** If your app uses Supabase Auth, Auth0, Clerk, or a social login provider like Google or GitHub OAuth, the redirect URLs for login are typically registered against your original domain. Switch domains without updating every one of these callback URLs, and users trying to log in mid-migration hit a broken redirect or an outright authentication failure.

- **CORS and API configuration.** Backend APIs and Edge Functions frequently have Cross-Origin Resource Sharing rules that explicitly allow requests only from the original domain. The moment your frontend starts serving from the new domain without updating these rules, API calls silently fail with CORS errors that look like a broken app to a confused end user.

- **Payment webhook endpoints.** Stripe and other payment providers have webhook URLs configured against a specific domain. If that URL isn't updated in lockstep with the domain switch, payment confirmations stop arriving — meaning customers get charged, but your app never finds out and never grants access.

- **SSL certificate provisioning.** A new custom domain needs its own SSL certificate, and if this isn't provisioned and verified before traffic is cut over, visitors hit browser security warnings that will tank trust and conversion in the exact window you're trying to look professional.

- **DNS propagation timing.** DNS changes don't take effect instantly everywhere — propagation across the global DNS system can take anywhere from minutes to 48 hours, meaning some users may hit the old domain while others hit the new one during the transition, and if session state, cookies, or auth tokens aren't handled consistently across both, users can get logged out or land on inconsistent versions of the app.

Miss any one of these, and "simple domain migration" turns into an outage, a wave of failed logins, or — worse — silently lost payments that don't surface until a customer complains days later.

There's also a subtler failure mode that rarely gets caught until weeks later: transactional email deliverability. If your app sends password resets, invoice receipts, or notification emails through a service like Resend, Postmark, or SendGrid, those emails are typically sent "from" your domain and authenticated using SPF, DKIM, and DMARC DNS records specific to that domain. A new custom domain starts with none of these records configured, which means transactional emails sent from it are far more likely to land in spam or bounce entirely — and because email deliverability failures are silent from the app's perspective, a founder can go weeks believing password reset emails are working fine when a meaningful share of them are quietly never reaching the inbox.

## The Founder's Situation

The founder in this case had built a project management tool for creative agencies using Bolt, running successfully on Bolt's default hosting subdomain with around 400 active users and a functioning Stripe subscription flow. Ready to look more professional and improve trust with prospective agency clients, she purchased a custom domain and needed to move the live application over — without logging out her existing user base, without breaking active subscriptions, and without a visible outage during business hours in multiple timezones where her agency clients operated.

Her first attempt, done independently by updating the DNS record and calling it done, broke Google OAuth login within twenty minutes — the redirect URL registered with Google's OAuth console still pointed at the old domain, and every user trying to log in got bounced to an error page. She reverted the DNS change and reached out for help.

## The Zero-Downtime Migration Process

LaunchStudio's engineers approached the migration as a sequenced, staged process rather than a single DNS flip, specifically to avoid a repeat of the failed first attempt:

1. **Pre-migration audit.** The team mapped every place the original domain was referenced: OAuth provider callback URLs, CORS allowlists in the backend, Stripe webhook endpoint configuration, hardcoded domain references in the frontend code, and email templates that linked back to the app.

2. **Parallel domain configuration.** The new custom domain was fully configured — SSL certificate provisioned and verified, DNS records set — while the app continued running normally on the original domain, so nothing was live or user-facing yet on the new domain until it was fully verified.

3. **Dual-domain support window.** Rather than an instant cutover, the backend was temporarily configured to accept requests from both the old and new domains simultaneously — CORS rules allowing both, OAuth callbacks registered for both — so that as DNS propagated at different speeds across different users' networks, neither version of the domain would produce a broken experience.

4. **Staged webhook cutover.** The Stripe webhook endpoint was updated to the new domain only after the team confirmed test events were being received correctly and after monitoring showed the new endpoint responding properly, avoiding any window where a real payment event could be sent to a stale endpoint.

5. **Monitoring during propagation.** The team actively monitored error rates, login success rates, and payment webhook delivery throughout the 48-hour propagation window, ready to roll back instantly if anything showed signs of breaking.

6. **Email authentication records.** SPF, DKIM, and DMARC records were configured and verified for the new domain before any transactional email traffic (password resets, invoice receipts, notifications) was switched over, confirmed with test sends checked against major inbox providers rather than assumed to be correct.

7. **Old domain redirect, not removal.** Once propagation was confirmed complete and traffic had fully shifted to the new domain, the old domain was configured to redirect to the new one rather than simply deactivated, so any lingering bookmarks, old marketing links, or slow-to-propagate DNS resolvers wouldn't hit a dead end.

## The Result

The entire migration ran without a single reported login failure, a single missed payment webhook, or any customer-visible downtime. Users who happened to hit the app during the propagation window experienced no difference in functionality regardless of which domain version they landed on, because both were fully functional in parallel throughout the transition.

## What This Case Study Reveals About AI-Builder Deployments

Bolt, Lovable, and similar tools make getting a working app onto a default subdomain nearly instant, which is exactly why founders underestimate how many system components are quietly wired to that specific domain by the time real users, real payments, and real integrations are in play. A domain migration on a brand-new, empty app with zero users is genuinely a five-minute task. The same migration on a live app with active sessions, OAuth logins, and a payment integration is an infrastructure project with real failure modes — and the gap between those two realities is exactly where founders get burned attempting it themselves under the assumption that "it's just DNS."

## Key Takeaways

- A custom domain migration on a live AI-built app touches authentication callbacks, CORS configuration, payment webhooks, and SSL provisioning — not just a single DNS record, and missing any one causes a real customer-facing failure.

- DNS propagation isn't instant; it can take up to 48 hours globally, meaning both the old and new domain need to function correctly in parallel during the transition, not just the new one.

- A single-step DNS cutover without updating OAuth callback URLs is one of the most common causes of a broken migration — login failures appear almost immediately because the identity provider still points at the old domain.

- Updating a Stripe webhook endpoint before confirming the new endpoint works correctly risks silently losing payment confirmations during the exact window customers are paying.

- Keeping the old domain as a redirect rather than deactivating it protects against lingering bookmarks, marketing links, and slow-to-propagate DNS resolvers sending users to a dead end after the migration is otherwise complete.

## Ready to Move to Your Custom Domain Without the Risk?

Get a zero-downtime domain migration that keeps your logins, payments, and active sessions intact throughout the transition.

LaunchStudio is operated by **Manifera**, an international software engineering company founded in 2014 and led by Founder & Managing Director **Herre Roelevink**. As Roelevink puts it: *"We see a shift in software needs. The challenge is no longer turning good ideas into software. It's now about the architecture and security needed to bring those products to maturity. We have eleven years of experience in exactly that."* Combining "Dutch management with Vietnamese mastery," Manifera maintains headquarters in **Amsterdam, the Netherlands** (Herengracht 420), an Asia hub in **Singapore** (100 Tras Street), and a primary development center in **Ho Chi Minh City, Vietnam** (Pho Quang Street). Through LaunchStudio, senior engineering teams take your existing AI-built frontend and implement production-ready security controls, live payment gateways, secure hosting, and monitoring — transforming your prototype into a secure, compliant MVP in 1 to 3 weeks, without a rebuild. [Get a free quote today](https://launchstudio.eu/en/#contact) or see how Manifera's [custom software development team](https://www.manifera.com/services/custom-software-development/) approaches production-hardening for AI-generated codebases.

## Real example

### An AI-Native Founder in Action: Creative Agency Project Management Tool

Ines, the founder behind this case, had grown her Bolt-built project management tool for creative agencies to roughly 400 active users on Bolt's default subdomain, with Stripe subscriptions live and working. A do-it-herself DNS switch to her newly purchased custom domain broke Google OAuth login within twenty minutes, locking out active users mid-workday across multiple timezones.

Ines brought in **LaunchStudio (by Manifera)** to execute the migration properly. The team ran a full pre-migration audit, configured dual-domain support for the propagation window, staged the OAuth callback and Stripe webhook updates only after each was verified, and monitored the transition in real time.

**Result:** Ines's migration completed with zero reported login failures, zero missed payment webhooks, and no customer-visible downtime throughout the 48-hour DNS propagation window.

**Cost & Timeline:** €1,400 (Launch Ready Package) — audited, migrated, and verified in 5 business days.

---

---

---
## Frequently Asked Questions

### Why did my DNS-only domain switch break login?

OAuth providers like Google and GitHub register a specific redirect URL tied to your domain. If you switch your DNS to a new domain without also updating the callback URL registered in the OAuth provider's console, every login attempt gets redirected to a broken or mismatched URL, producing an immediate authentication failure.

### How long does DNS propagation actually take?

It varies by DNS provider and by each user's network, but it can take anywhere from a few minutes to as long as 48 hours to fully propagate globally. During that window, different users may be routed to either the old or new domain, so both need to function correctly in parallel.

### What happens to Stripe payments during a domain migration?

If your Stripe webhook endpoint URL isn't updated correctly, or if it's updated before you've confirmed the new endpoint is receiving and processing events properly, payment confirmation events can fail to reach your app. Customers get charged, but your app never grants access, because it never received the webhook confirming the payment.

### Should I deactivate my old domain after migrating?

No — configure it to redirect to your new domain instead. Bookmarks, old marketing links, and slow-to-propagate DNS resolvers will continue directing some traffic to the old domain for a period after migration, and a redirect ensures those visitors still land somewhere functional rather than a dead page.

### How long does a zero-downtime domain migration typically take?

For a live app with authentication, payments, and active users, a properly staged migration — including the pre-migration audit, dual-domain support window, and monitored cutover — typically takes about a week from start to full verification, though the DNS propagation window itself can add up to 48 additional hours of monitoring.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why did my DNS-only domain switch break login?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "OAuth providers like Google and GitHub register a specific redirect URL tied to your domain. If you switch your DNS to a new domain without also updating the callback URL registered in the OAuth provider's console, every login attempt gets redirected to a broken or mismatched URL, producing an immediate authentication failure."
      }
    },
    {
      "@type": "Question",
      "name": "How long does DNS propagation actually take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It varies by DNS provider and by each user's network, but it can take anywhere from a few minutes to as long as 48 hours to fully propagate globally. During that window, different users may be routed to either the old or new domain, so both need to function correctly in parallel."
      }
    },
    {
      "@type": "Question",
      "name": "What happens to Stripe payments during a domain migration?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "If your Stripe webhook endpoint URL isn't updated correctly, or if it's updated before you've confirmed the new endpoint is receiving and processing events properly, payment confirmation events can fail to reach your app. Customers get charged, but your app never grants access, because it never received the webhook confirming the payment."
      }
    },
    {
      "@type": "Question",
      "name": "Should I deactivate my old domain after migrating?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — configure it to redirect to your new domain instead. Bookmarks, old marketing links, and slow-to-propagate DNS resolvers will continue directing some traffic to the old domain for a period after migration, and a redirect ensures those visitors still land somewhere functional rather than a dead page."
      }
    },
    {
      "@type": "Question",
      "name": "How long does a zero-downtime domain migration typically take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For a live app with authentication, payments, and active users, a properly staged migration — including the pre-migration audit, dual-domain support window, and monitored cutover — typically takes about a week from start to full verification, though the DNS propagation window itself can add up to 48 additional hours of monitoring."
      }
    }
  ]
}
</script>
