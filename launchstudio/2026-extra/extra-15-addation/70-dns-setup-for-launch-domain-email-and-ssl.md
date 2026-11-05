---
Title: "DNS Setup for Launch: Domain, Email and SSL"
Keywords: dns setup for launch, custom domain lovable app, spf dkim dmarc setup, dnssec nl domain, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# DNS Setup for Launch: Domain, Email and SSL

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "DNS Setup for Launch: Domain, Email and SSL",
  "description": "Moving an AI-built app from a preview URL to its own domain involves DNS records, email authentication and SSL certificates, and mistakes can break the site, email or both. This guide explains domain ownership, the records you need, apex and www setup, subdomains, SPF, DKIM and DMARC, SSL and HSTS, DNSSEC, CAA records and how to avoid dangling records that enable subdomain takeover.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-26",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/dns-setup-for-launch-domain-email-and-ssl" },
  "citation": [
    { "@type": "CreativeWork", "name": "SIDN: DNSSEC", "url": "https://www.sidn.nl/en/modern-internet-standards/dnssec" },
    { "@type": "CreativeWork", "name": "Internet.nl test for modern internet standards", "url": "https://internet.nl/" },
    { "@type": "CreativeWork", "name": "RFC 7489: DMARC", "url": "https://www.rfc-editor.org/rfc/rfc7489" },
    { "@type": "CreativeWork", "name": "MDN: Strict-Transport-Security", "url": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security" }
  ]
}
</script>

Launching on your own domain is one of the most satisfying moments in building a product. The preview URL with random characters becomes `yourproduct.nl`. It also involves DNS, the internet's address book, which most founders touch only a few times and which is unforgiving of mistakes. A wrong record can take your site offline. A deleted record can stop your company email. A missing record can send your password reset emails to spam. A forgotten record can let someone else serve content on your subdomain.

DNS is not complicated once you understand the handful of record types involved. This guide walks through what an AI-built product needs at launch, in plain language.

## Key Takeaways

- **Register the domain in your company's name,** with auto-renewal, registrar lock and MFA on the registrar account.
- **Point the root domain and `www` to your host** with the records your host specifies, and redirect one to the other.
- **Authenticate email with SPF, DKIM and DMARC** before sending production email from the domain.
- **Let your host manage SSL certificates** automatically, and enable HTTPS everywhere, with HSTS once stable.
- **Enable DNSSEC and remove unused records** to prevent spoofing and subdomain takeover.

## Domain Ownership Basics

Before records, check ownership:

- **Register the domain to your company,** not a freelancer, agency or personal account. Domains held by others are a common due diligence finding and a real risk if relationships end.
- **Enable auto-renewal** with a valid payment method. Expired domains can be lost to others.
- **Enable registrar lock** to prevent unauthorised transfers.
- **Use MFA** on the registrar account and keep recovery details current.
- **Document who has access** to the registrar and DNS provider.

For `.nl` domains, registration goes through registrars accredited by SIDN, the registry for the Netherlands. Many founders also register common variants, such as `.com` or `.eu`, and redirect them.

## Where DNS Is Managed

DNS records may be managed at your registrar, at a DNS provider such as Cloudflare, or at your hosting platform. Choose one place, document it and avoid splitting records across providers. If you move DNS, copy every existing record first, especially email records.

## The Records You Will Use

| Record | What it does | Example use |
| --- | --- | --- |
| A / AAAA | Points a name to an IPv4 / IPv6 address | Root domain to a host's IP |
| CNAME | Points a name to another name | `app` to your hosting platform's address |
| ALIAS / ANAME / flattened CNAME | CNAME-like behaviour at the root, where supported | Root domain to a platform hostname |
| MX | Says which servers receive email | Company email provider |
| TXT | Text records for verification and policies | SPF, DMARC, domain verification |
| CAA | Says which certificate authorities may issue certificates | Restrict SSL issuance |

## Root Domain and www

Visitors type both `yourproduct.nl` and `www.yourproduct.nl`. Choose one as canonical and redirect the other:

- **Follow your host's instructions** for the root domain. Some hosts provide IP addresses for A records; others require ALIAS or flattened CNAME records, which only some DNS providers support.
- **Point `www`** with a CNAME to the host.
- **Configure the redirect** at the host, so all traffic ends up on the canonical version over HTTPS.

Search engines prefer a single canonical domain, and consistent URLs help analytics and authentication redirect settings.

## Subdomains

Plan subdomains deliberately:

| Subdomain | Typical use |
| --- | --- |
| `app.` | The logged-in application |
| `www.` or root | Marketing site |
| `docs.` or `help.` | Documentation or help centre |
| `api.` | Public API, if offered |
| `status.` | Status page |
| `mail.` or similar | Transactional email sending domain |
| `news.` or similar | Marketing email sending domain |

Our guide on [connecting a Webflow or Framer site to an AI-built app](https://launchstudio.eu/en/blog/webflow-or-framer-site-with-an-ai-built-app-domains-auth-and-seo) explains the marketing site and app split.

## Email: MX and Authentication

**MX records** route incoming email for your domain to your email provider, such as Microsoft 365 or Google Workspace. Never delete or change MX records while working on website records unless you mean to change email providers.

For **outgoing** email, both from your company mailboxes and from your app, authenticate the domain:

**SPF** is a TXT record listing services allowed to send email for the domain. Only one SPF record is allowed per name; combine all senders into it, and keep it within the lookup limits the standard imposes.

**DKIM** uses cryptographic keys published as DNS records, usually provided by each sending service. Add the records for your company email provider and your transactional email provider.

**DMARC** is a TXT record at `_dmarc.yourdomain` that tells receivers what to do when SPF or DKIM checks fail, and where to send reports. Start with a monitoring policy (`p=none`) and reports, review them, then move to `quarantine` or `reject` once all legitimate senders pass.

Using a subdomain for app email, such as `mail.yourproduct.nl`, keeps its reputation separate from company mail. Our article on [transactional email providers](https://launchstudio.eu/en/blog/transactional-email-providers-resend-vs-postmark-vs-brevo) covers the sending side.

## SSL Certificates and HTTPS

Modern hosting platforms issue and renew SSL certificates automatically, usually through Let's Encrypt or similar authorities, once DNS points to them. Your tasks:

- **Wait for certificate issuance** after adding records, and verify HTTPS on every hostname.
- **Redirect HTTP to HTTPS** everywhere.
- **Enable HSTS** with the `Strict-Transport-Security` header once HTTPS works reliably, so browsers always use HTTPS. Start with a modest duration and increase it.
- **Add CAA records** if you want to restrict which certificate authorities may issue certificates for your domain, including those your hosts use.

## DNSSEC

DNSSEC adds cryptographic signatures to DNS responses, protecting against certain spoofing attacks. SIDN actively promotes DNSSEC for `.nl` domains, and many Dutch registrars support it. Enable it if your DNS provider and registrar support it, following their instructions carefully, especially when moving DNS between providers, where misconfiguration can make the domain unreachable.

## Dangling Records and Subdomain Takeover

A subtle risk: you create `demo.yourproduct.nl` pointing to a hosting service for a test, later delete the project on the hosting service, but leave the DNS record. Someone else can sometimes claim the same hosting name and serve content on your subdomain, a subdomain takeover. Attackers use this for phishing or to steal cookies scoped to your domain.

Prevention:

- **Remove DNS records when you remove services.**
- **Review DNS records periodically** and delete anything you do not recognise.
- **Avoid wildcard records** unless necessary.
- **Scope cookies narrowly,** so a compromised subdomain cannot read session cookies.

## Verification Records

Many services ask you to add TXT records to prove domain ownership: search consoles, email providers, SSO configurations, app stores. Keep them, document what each is for and remove those for services you no longer use.

## Understanding TTL and Propagation

Every DNS record has a time to live, or TTL, which tells resolvers how long to cache it. With a TTL of one day, a change may take up to a day to reach everyone, because some resolvers keep using the cached old value. That is why DNS changes seem to "propagate" slowly, and why a mistake can linger.

Practical rules:

- **Lower TTLs before planned changes,** for example to five minutes, a day ahead, then raise them again afterwards.
- **Expect mixed results during transitions:** some users see the new site while others still see the old one. Keep the old host running until traffic has moved.
- **Test from several networks,** such as office Wi-Fi, a phone on mobile data and an online DNS lookup tool, rather than relying on your own browser, which may have cached old results.
- **Do not keep changing records while waiting.** Each change resets caches and makes problems harder to diagnose.

## Documenting Your DNS

Keep a simple document, ideally in your repository or operations notes, listing every DNS record, what it is for, which service it belongs to and who added it. Include the registrar, DNS provider, account owners and renewal dates. When someone asks why a TXT record exists, or a new team member needs to add a subdomain, the answer is there. This document also speeds up security questionnaires and due diligence, which often ask about domain ownership and email authentication.

## Launch Day Sequence

1. **A day before:** lower TTLs on records you will change, so changes propagate quickly and mistakes can be corrected.
2. **Export or screenshot all existing records.**
3. **Add new records** for the app and site, without touching email records.
4. **Verify HTTPS** on each hostname, from a phone network and another network.
5. **Update authentication settings** in Supabase or your auth provider: site URL, redirect URLs and OAuth origins.
6. **Test critical flows:** sign-up, email confirmation, password reset, payment and webhook delivery.
7. **Check email:** send and receive company email, and send app emails to test inboxes.
8. **Raise TTLs again** once stable.

## Checking Your Setup

The Dutch platform Internet.nl offers free tests for modern internet standards, including HTTPS, DNSSEC and email authentication. Running your domain through it gives a quick overview of what is configured correctly and what is missing.

## Common Mistakes

**Breaking email while changing website records.**

**Two SPF records,** which makes SPF fail.

**DMARC set to reject immediately,** blocking legitimate email from services not yet authenticated.

**Domain registered to a freelancer.**

**Dangling CNAMEs** to deleted services.

**Authentication redirect URLs still pointing to the preview domain.**

## How LaunchStudio Helps

LaunchStudio handles domain and DNS setup as part of every production launch: verifying ownership and registrar security, configuring root, `www` and subdomains for your hosts, preserving and authenticating email with SPF, DKIM and DMARC, enabling HTTPS, HSTS, CAA and DNSSEC where appropriate, removing dangling records and updating authentication settings for the new domain.

The **Launch Ready** package (€800-€3,500) includes deployment to your own domain with DNS, SSL and email configuration, security hardening and 48 hours of support; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Launch That Took Company Email Offline

Anouk van Dijk built Huurcontractcheck with Bolt and Supabase: a tool that helps tenants and small landlords check rental contracts against Dutch rules. On launch day, she followed a tutorial to point her `.nl` domain to her hosting platform, deleting what looked like old records to "clean up". Her website went live within an hour. Her company email stopped working, and nobody noticed until a journalist mentioned she had not replied to an interview request.

The deleted records included the MX records for her Microsoft 365 mailbox and the SPF record. Password reset emails from the app, sent through an unauthenticated provider, landed in spam. Supabase Auth still redirected users to the Bolt preview URL after confirming their email, and a leftover CNAME pointed `beta.` to a hosting project she had deleted months earlier. The domain itself was registered under the account of a freelancer who had helped with an earlier website.

LaunchStudio restored the MX and SPF records from her email provider's documentation, then added DKIM for Microsoft 365 and for a transactional email provider on a `mail.` subdomain, with a single combined SPF record and a DMARC policy in monitoring mode. Supabase Auth's site URL and redirect URLs were updated to the production domain, the dangling `beta.` record was removed, and DNSSEC was enabled at the registrar. HTTPS redirects and HSTS were configured, and the domain was transferred to Anouk's company account with registrar lock and MFA.

**Result:** Company email was restored the same day, app emails began reaching inboxes, and the Internet.nl test showed full marks for HTTPS and email authentication. Anouk now keeps a DNS document listing every record and its purpose.

> *"I thought I was tidying up old records. I was actually unplugging my own email."*
> - **Anouk van Dijk, Founder, Huurcontractcheck (Nijmegen)**

**Cost & Timeline:** €1,450 (Launch Ready package: DNS recovery, email authentication, auth redirect fixes, DNSSEC, HTTPS hardening and domain transfer) - completed in 4 business days.

## Frequently Asked Questions

### What DNS records do I need to launch my app?

Typically: records pointing the root domain and `www` to your marketing site or app host, a CNAME for the `app` subdomain if used, MX records for company email, TXT records for SPF and DMARC, DKIM records for each email sender and any verification records services require.

### Why did my email stop working after changing DNS?

Most often because MX records were deleted or changed, or because DNS was moved to a new provider without copying all existing records. Restore MX and email authentication records from your email provider's documentation and verify delivery.

### Do I need DNSSEC for my domain?

It is recommended. DNSSEC protects against certain DNS spoofing attacks, and SIDN encourages it for `.nl` domains. Enable it if your registrar and DNS provider support it, and follow their instructions carefully when changing providers.

### How does Manifera's experience help with launch configuration?

Manifera has configured domains, DNS and email infrastructure for enterprise systems for 11+ years. LaunchStudio applies that experience so launches move to production domains without breaking email, authentication or security.

### Does DNS setup affect SEO and AI visibility?

Yes. A single canonical domain with HTTPS, correct redirects and reliable uptime helps search engines and AI answer engines index and cite your pages consistently. Misconfigured DNS can cause duplicate content, certificate warnings or downtime that harm visibility.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What DNS records do I need to launch my app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Root and www records to your host, app subdomain CNAME, MX for email, SPF and DMARC TXT, DKIM per sender and verification records." }
    },
    {
      "@type": "Question",
      "name": "Why did my email stop working after changing DNS?",
      "acceptedAnswer": { "@type": "Answer", "text": "Usually deleted or changed MX records or incomplete DNS migration; restore records from your email provider's documentation." }
    },
    {
      "@type": "Question",
      "name": "Do I need DNSSEC for my domain?",
      "acceptedAnswer": { "@type": "Answer", "text": "Recommended; SIDN encourages it for .nl domains. Follow provider instructions carefully." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with launch configuration?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has configured enterprise DNS and email for 11+ years, so launches do not break email or authentication." }
    },
    {
      "@type": "Question",
      "name": "Does DNS setup affect SEO and AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; a canonical HTTPS domain with correct redirects and uptime helps indexing and citation." }
    }
  ]
}
</script>
