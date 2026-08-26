---
Title: "The Real Cost of a Botched DNS Migration When Connecting a Custom Domain"
Keywords: DNS Migration, Custom Domain Setup, DNS Propagation, MX Records, SSL Certificate, LaunchStudio, Manifera
Buyer Stage: Decision
---

# The Real Cost of a Botched DNS Migration When Connecting a Custom Domain

Connecting a custom domain looks, on paper, like the easiest step in launching an AI-built product: point some DNS records at the hosting provider, wait a little while, and the app is live on a real domain instead of a `.vercel.app` or `.lovable.app` subdomain. Most tutorials make it look like a five-minute task. What those tutorials rarely mention is everything that can break silently in the process — email deliverability, SEO signals, SSL certificate validation, and every existing service that depended on the old DNS configuration — and how expensive it gets to untangle once a founder has already told their waitlist the new domain is live. This is the story of what happened when Renate Voss, founder of a customer-feedback analytics tool called SignalBoard, moved her Bolt-built app from its default subdomain to a custom domain the week before launch, and how a rushed DNS migration turned a routine task into four days of lost signups and undelivered emails.

## What a DNS Migration Actually Touches

A domain's DNS records aren't a single setting — they're a small collection of independent records, each responsible for a different function, and a migration that changes one without accounting for the others is where things go wrong. The A or CNAME record points the domain to the hosting provider's servers. The MX records route incoming email to whatever mail service the domain uses. TXT records handle domain verification for services like Google Workspace, SPF and DKIM authentication for outbound email deliverability, and ownership verification for third-party tools. When a founder migrates a domain by simply following their new host's "point your domain here" instructions and wholesale replacing the DNS records at the registrar, it's alarmingly easy to overwrite MX and TXT records that had nothing to do with the new hosting provider but everything to do with email actually working.

## What Went Wrong for SignalBoard

Renate had been using her domain, signalboard.io, for a Google Workspace email address and a waitlist landing page hosted separately from her Bolt app, which lived on a `.bolt.app` subdomain during development. The week before launch, she followed Bolt's domain-connection guide, which walked her through adding an A record and a CNAME at her registrar. What the guide didn't flag — because it was written for the general case, not for someone with an existing email setup on the same domain — was that her registrar's "quick connect" option replaced the entire DNS record set rather than adding to it, silently deleting the MX records that routed mail to Google Workspace and the SPF/DKIM TXT records that authenticated it.

The app itself came up fine on the new domain within a few hours. What Renate didn't notice until the next morning was that every email sent to her `@signalboard.io` address had started bouncing, and — because SPF and DKIM were gone — the transactional emails her app sent through its email provider (password resets, welcome emails, trial-ending notices) were landing in spam folders or being rejected outright by major providers like Gmail and Outlook, since there was no longer any DNS-level proof the email provider was authorized to send on the domain's behalf. She launched to her waitlist that morning, unaware that a meaningful share of her welcome emails and password reset links were silently failing to arrive.

## The Four-Day Cost

By the time Renate noticed the pattern — a wave of "I never got my confirmation email" messages on social media — 60 of her first 400 signups had never received a working welcome email, and an unknown number more had simply never come back after a login or password-reset email failed to arrive. Rebuilding the DNS records correctly was, mechanically, not difficult: restoring the MX records, re-adding SPF and DKIM TXT records with the correct values for both Google Workspace and her transactional email provider, and verifying SSL certificate issuance on the new custom domain hadn't been broken by the same overwrite. What made it costly wasn't the fix itself — it was DNS propagation time. DNS changes don't take effect instantly everywhere; depending on the record's TTL (time-to-live) setting and how aggressively different internet service providers and email servers cache DNS results, changes can take anywhere from a few minutes to 48-72 hours to fully propagate globally. Renate's original record set had a 24-hour TTL, meaning even after the correct records were restored, some portion of the internet was still resolving the broken configuration for a full day afterward.

## Why This Specific Failure Is So Common With AI-Builder Launches

This isn't a rare edge case — it's close to the default outcome when a founder with an existing email setup follows a generic "connect your domain" tutorial written by a hosting provider that has no visibility into what else is running on that domain. AI builders like Bolt, Lovable, and Vercel-hosted Cursor projects all provide domain-connection instructions optimized for the common case of a brand-new domain with nothing else configured on it — which describes a large share of first-time founders, but not founders migrating an existing business domain that already has email, a previous landing page, or other verified services attached. The instructions aren't wrong, they're just incomplete for anyone outside that common case, and nothing in the flow warns a founder before they overwrite a working configuration.

## Getting a DNS Migration Right the First Time

The difference between a clean migration and a four-day recovery comes down to a handful of specific steps that generic tutorials routinely skip: exporting and documenting the domain's full existing DNS record set before making any changes, adding new records for the hosting provider rather than replacing the entire set, explicitly preserving MX, SPF, and DKIM records if email is in use on the domain, lowering TTL values 24-48 hours before a planned migration so any needed rollback propagates quickly instead of taking a full day, and verifying the new configuration — SSL issuance, email deliverability, and app resolution — from an external testing tool before pointing real traffic and real email at the domain. None of these steps are individually difficult; the risk is entirely in not knowing they're needed until after something has already broken in front of real users.

## The Compounding Cost Beyond the Migration Itself

It's worth quantifying why this matters more than a typical bug. A broken checkout button gets noticed and fixed within minutes because the founder is watching the funnel closely on launch day. A broken email deliverability chain is different — it fails silently, doesn't throw an error anywhere the founder is looking, and only becomes visible once users start complaining on social media or support tickets pile up, by which point the damage has already compounded across every signup during the broken window. For Renate, the 60 affected signups weren't just 60 missed welcome emails; several of them had also triggered a password-reset request that silently failed, meaning those users concluded the product was simply broken and never returned to try again, even after the underlying issue was fixed. A launch-day cohort is disproportionately valuable — these are the most enthusiastic, highest-intent users a product will ever see, arriving in the same 48-hour window that determines a large share of early word-of-mouth. Losing a portion of that specific cohort to a fixable DNS oversight is a worse trade than the same number of losses spread out over a normal month, because that early momentum is difficult to manufacture a second time.

## Key Takeaways

- A DNS migration touches more than just the hosting record — MX records for email routing and SPF/DKIM TXT records for email authentication are commonly and silently overwritten by "quick connect" domain tools that replace the full record set instead of adding to it.

- The specific failure mode is dangerous because it's invisible at first: the app itself loads fine on the new domain while transactional emails — welcome messages, password resets — quietly bounce or land in spam in the background.

- DNS propagation delay compounds the cost of any mistake: depending on TTL settings, a broken record can remain live for a portion of the internet for up to 48-72 hours even after the correct fix is deployed.

- Generic domain-connection tutorials from AI builders and hosting providers are written for the common case of a brand-new domain with nothing else configured — they don't warn founders with an existing email setup about the risk before it happens.

- Lowering TTL values 24-48 hours before a planned migration, documenting the existing DNS record set first, and verifying deliverability from an external tool before going live are the specific steps that prevent this failure rather than just recovering from it.

## Don't Let a DNS Mistake Break Your Launch Week

If you're about to connect a custom domain to your AI-built app — especially one with existing email — get the migration checked before you point real traffic at it.

LaunchStudio is operated by **Manifera**, an international software engineering company founded in 2014 and led by Founder & Managing Director **Herre Roelevink**. As Roelevink puts it: *"We see a shift in software needs. The challenge is no longer turning good ideas into software. It's now about the architecture and security needed to bring those products to maturity. We have eleven years of experience in exactly that."* Combining "Dutch management with Vietnamese mastery," Manifera maintains headquarters in **Amsterdam, the Netherlands** (Herengracht 420), an Asia hub in **Singapore** (100 Tras Street), and a primary development center in **Ho Chi Minh City, Vietnam** (Pho Quang Street), with enterprise clients including Vodafone and TNO. Through LaunchStudio, senior engineering teams plan and execute your custom domain and DNS migration correctly the first time — preserving email deliverability, SSL validity, and SEO signals — as part of turning your AI-built prototype into a production-ready MVP in 1 to 3 weeks. [Get a free quote today](https://launchstudio.eu/en/#contact) or see how Manifera's [custom software development team](https://www.manifera.com/services/custom-software-development/) approaches production hardening for AI-generated codebases.

## Real example

### An AI-Native Founder in Action: An SSL Gap That Locked Out a Legal-Tech Launch

Callum Ferreira, founder of a contract-review tool called ClauseWatch built with **Cursor** and deployed on Vercel, migrated his domain from a staging subdomain to his purchased custom domain two days before a scheduled LinkedIn launch post. The A record pointed correctly to Vercel, but he hadn't waited for SSL certificate issuance to complete before sharing the new URL — Vercel's automatic SSL provisioning depends on DNS propagating first, and issuing a certificate before propagation is confirmed can leave a domain serving an invalid or mismatched certificate for hours. Every visitor who clicked his launch post hit a browser security warning instead of his landing page, and a meaningful share never clicked past it.

Callum brought in LaunchStudio to properly sequence a second migration attempt. Engineers documented his full existing DNS record set, staged the new A and CNAME records with a reduced TTL to control propagation timing, confirmed SSL certificate issuance and validity from multiple external locations before any traffic was pointed at the new domain, and verified transactional email deliverability end-to-end before the relaunch post went out.

**Result:** Callum's relaunch post drove 1,100 clicks with zero SSL warnings and a fully verified checkout and email flow, converting at a rate 3x higher than his first attempt.

**Cost & Timeline:** €900 (Launch Ready Package) — migration verified and relaunched in 3 business days.

---

---

---
## Frequently Asked Questions

### What's the most common mistake in a DNS migration for a custom domain?

The most common mistake is using a "quick connect" tool that replaces a domain's entire DNS record set instead of adding new records to it — silently deleting MX records (email routing) and SPF/DKIM TXT records (email authentication) that had nothing to do with the new hosting provider but were essential to existing email service on the domain.

### Why did email stop working even though the website loaded fine?

The A or CNAME record that makes a website load and the MX/TXT records that route and authenticate email are independent settings. A migration tool can correctly update the website-facing record while overwriting the email-facing ones in the same "quick connect" action, so the app appears to work perfectly while email quietly breaks in the background.

### How long does it take to fix a botched DNS migration?

The technical fix — restoring the correct records — can take under an hour. The real delay is DNS propagation: depending on the TTL (time-to-live) setting on the original records, it can take anywhere from a few minutes up to 48-72 hours for the corrected configuration to be visible everywhere on the internet.

### How can I prevent a DNS migration from breaking my email or SSL?

Document your domain's full existing DNS record set before making changes, add new records for your hosting provider rather than replacing the entire set, explicitly preserve any existing MX and SPF/DKIM records, lower TTL values 24-48 hours before a planned migration so any needed rollback propagates faster, and verify SSL issuance and email deliverability from an external testing tool before pointing real traffic at the domain.

### Does a botched DNS migration affect SEO?

It can. A domain migration handled incorrectly can produce redirect chains, broken canonical signals, or temporary downtime that search engines interpret as instability, potentially affecting how quickly rankings transfer to the new domain configuration. Verifying the migration end-to-end before relying on it publicly reduces this risk alongside the email and SSL issues.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What's the most common mistake in a DNS migration for a custom domain?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The most common mistake is using a \"quick connect\" tool that replaces a domain's entire DNS record set instead of adding new records to it — silently deleting MX records (email routing) and SPF/DKIM TXT records (email authentication) that had nothing to do with the new hosting provider but were essential to existing email service on the domain."
      }
    },
    {
      "@type": "Question",
      "name": "Why did email stop working even though the website loaded fine?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The A or CNAME record that makes a website load and the MX/TXT records that route and authenticate email are independent settings. A migration tool can correctly update the website-facing record while overwriting the email-facing ones in the same \"quick connect\" action, so the app appears to work perfectly while email quietly breaks in the background."
      }
    },
    {
      "@type": "Question",
      "name": "How long does it take to fix a botched DNS migration?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The technical fix — restoring the correct records — can take under an hour. The real delay is DNS propagation: depending on the TTL (time-to-live) setting on the original records, it can take anywhere from a few minutes up to 48-72 hours for the corrected configuration to be visible everywhere on the internet."
      }
    },
    {
      "@type": "Question",
      "name": "How can I prevent a DNS migration from breaking my email or SSL?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Document your domain's full existing DNS record set before making changes, add new records for your hosting provider rather than replacing the entire set, explicitly preserve any existing MX and SPF/DKIM records, lower TTL values 24-48 hours before a planned migration so any needed rollback propagates faster, and verify SSL issuance and email deliverability from an external testing tool before pointing real traffic at the domain."
      }
    },
    {
      "@type": "Question",
      "name": "Does a botched DNS migration affect SEO?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It can. A domain migration handled incorrectly can produce redirect chains, broken canonical signals, or temporary downtime that search engines interpret as instability, potentially affecting how quickly rankings transfer to the new domain configuration. Verifying the migration end-to-end before relying on it publicly reduces this risk alongside the email and SSL issues."
      }
    }
  ]
}
</script>
