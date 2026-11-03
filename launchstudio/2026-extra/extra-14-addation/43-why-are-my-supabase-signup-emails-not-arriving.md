---
Title: "Why Are My Supabase Sign-Up Emails Not Arriving?"
Keywords: supabase emails not arriving, supabase smtp, lovable confirmation email, supabase auth email limit, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: Technical Solo Founder / Indie Hacker
---

# Why Are My Supabase Sign-Up Emails Not Arriving?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Why Are My Supabase Sign-Up Emails Not Arriving?",
  "description": "Supabase's built-in email service is meant for development, with tight sending limits. This article explains why confirmation and reset emails stop arriving after launch and how to fix it with custom SMTP, domain authentication and better templates.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-20",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/why-are-my-supabase-signup-emails-not-arriving" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Custom SMTP", "url": "https://supabase.com/docs/guides/auth/auth-smtp" },
    { "@type": "CreativeWork", "name": "Supabase: Redirect URLs", "url": "https://supabase.com/docs/guides/auth/redirect-urls" },
    { "@type": "CreativeWork", "name": "Google: Email sender guidelines", "url": "https://support.google.com/a/answer/81126" },
    { "@type": "CreativeWork", "name": "GDPR Article 28: Processor", "url": "https://gdpr-info.eu/art-28-gdpr/" }
  ]
}
</script>

**Short answer:** most likely because your app still uses Supabase's built-in email service, which is intended for development and testing and has strict sending limits. Once real users sign up, confirmation, magic link and password reset emails get rate-limited, delayed or land in spam. The fix is to configure a custom SMTP provider, authenticate your sending domain with SPF, DKIM and DMARC, and send from an address on your own domain.

## Key Takeaways

- **Supabase's built-in email service is meant for development** and has strict sending limits; production apps should configure custom SMTP.
- **Authenticate your sending domain with SPF, DKIM and DMARC.** Major mailbox providers, including Google and Yahoo, have tightened requirements for bulk senders, and unauthenticated mail increasingly lands in spam.
- **Wrong redirect URLs make valid emails useless,** sending users to preview domains or broken pages.
- **Corporate link scanners can consume magic links** before users click them; one-time codes avoid this.
- **Branded, clear templates improve both deliverability and trust,** and Dutch users should receive Dutch templates.

## The Four Usual Causes

| Cause | Symptom | Fix |
| --- | --- | --- |
| Built-in email limits | First few sign-ups work, then emails stop | Custom SMTP provider |
| Unauthenticated domain | Emails arrive in spam or not at all | SPF, DKIM and DMARC records |
| Wrong redirect URLs | Email arrives but link opens the preview or errors | Site URL and redirect list in Supabase |
| Link scanners | Links "already used" when users click | Use OTP codes or confirmation pages that require a click |

## Step 1: Configure Custom SMTP

In Supabase's Auth settings, enable custom SMTP and enter the host, port, username and password from a transactional email provider such as Postmark, Resend, Mailgun or Amazon SES. Choose a provider with EU data processing options if your users are in Europe, and add it to your list of processors.

## Step 2: Authenticate Your Domain

Your provider will ask you to add DNS records:

- **SPF** lists which services may send email for your domain
- **DKIM** signs messages so receivers can verify them
- **DMARC** tells receivers what to do with messages that fail checks

Without these, Gmail, Outlook and corporate filters increasingly reject or spam-folder your emails. Use a sending address such as `hello@yourdomain.nl`, never a free email address.

## Step 3: Fix Redirects

Confirmation and reset links point to your Supabase site URL and allowed redirect URLs. If those still reference the Lovable or Bolt preview, users click a valid email and land on the wrong app. Update them for production.

## Step 4: Handle Link Scanners

Some corporate email systems open every link to scan it, which can consume single-use magic links before the user clicks. Options: send a one-time code instead of a link, or point the email to a page in your app where the user presses a button to confirm.

## Step 5: Improve the Templates

Supabase lets you edit auth email templates. Use your product name, a clear subject line, plain language and your branding. Generic templates look like phishing, which hurts both deliverability and trust. For Dutch users, offer Dutch templates.

## Quick Diagnosis

1. Check Supabase Auth logs: was the email sent or rate-limited?
2. Check your SMTP provider's activity log: delivered, bounced or blocked?
3. Check a test inbox at Gmail and Outlook: inbox, spam or missing?
4. Click the link: does it open the right domain?

## Why Email Deliverability Has Become Stricter

Mailbox providers fight spam by checking whether a sender is who it claims to be. Three DNS-based standards do this work: SPF lists the servers allowed to send mail for your domain, DKIM adds a cryptographic signature to each message, and DMARC tells receiving servers how to treat messages that fail those checks and where to send reports. In recent years, Google and Yahoo announced stricter requirements for senders, including authentication and easy unsubscribe for bulk mail. Transactional emails such as confirmations and password resets benefit from the same authentication, because providers judge your domain's reputation as a whole.

## Choosing a Transactional Email Provider

Look for these properties when choosing a provider for auth and product emails:

| Property | Why it matters |
| --- | --- |
| Separate streams for transactional and marketing mail | Marketing complaints do not hurt password reset delivery |
| EU processing options | Simpler GDPR documentation for European users |
| Clear delivery logs | You can answer "did my email arrive?" in seconds |
| Bounce and complaint handling | Protects your sender reputation automatically |
| SMTP and API access | SMTP for Supabase Auth, API for your own emails |

Sign the provider's processing agreement and list it in your privacy documentation; it processes names and email addresses.

## Setting Up DNS Records Without Breaking Anything

Your email provider gives you exact records to add. Practical tips:

- **One SPF record per domain.** Multiple SPF records invalidate each other; merge them into one.
- **Use a subdomain for sending,** such as `mail.yourdomain.nl`, if your main domain already sends mail from other services.
- **Start DMARC in monitoring mode** (`p=none`) to collect reports, then tighten to quarantine or reject once everything passes.
- **Allow time for DNS propagation** before testing, typically minutes to a few hours.

## Templates That Work

Good auth emails share a pattern: a clear subject such as "Confirm your account at YourApp", the product name and logo, one prominent button or code, a short explanation of why the user received the email and what to do if they did not request it, and a plain-text version. Avoid link shorteners, large images and spam-trigger phrasing. For multilingual apps, send each user the template in their preferred language.

## Monitoring Delivery

Do not wait for users to report missing emails. Watch your provider's dashboard for bounce rates, spam complaints and blocked messages. Set an alert if confirmation emails stop being sent for an hour during normal usage. A sudden drop in sign-up completions is often the first visible sign of an email problem.

## Beyond Auth: Product Emails

Once SMTP is set up for auth, you will want other emails: receipts, notifications, reminders. Send these from server-side functions using your provider's API, never from the browser with an exposed key. Keep transactional and marketing emails separate, and give marketing emails an unsubscribe link and consent basis under the GDPR and e-privacy rules.

## Common Mistakes

- Sending from a free email address instead of your own domain
- Adding a second SPF record instead of merging
- Forgetting to update redirect URLs after moving to a custom domain
- Using the same provider stream for newsletters and password resets
- Never checking the delivery logs until a customer complains

## A Step-by-Step Fix in Under an Hour

For a typical Lovable or Bolt app with unreliable auth emails, the fix follows a fixed sequence:

1. **Create an account** with a transactional email provider and add your sending domain.
2. **Add the DNS records** the provider gives you for SPF, DKIM and, if not yet present, a DMARC record in monitoring mode.
3. **Wait for verification,** then copy the SMTP host, port, username and password.
4. **Enable custom SMTP in Supabase Auth,** set the sender address on your own domain and a recognisable sender name.
5. **Update the site URL and redirect allow list** to your production domain.
6. **Edit the templates** for confirmation, magic link, password reset and email change.
7. **Send test emails** to Gmail, Outlook and a corporate address, and check inbox placement.
8. **Check Supabase Auth logs and the provider's logs** to confirm both sides recorded the sends.

Most founders complete these steps in under an hour, with a short wait for DNS.

## Rate Limits and Abuse

Custom SMTP removes Supabase's development limits, but it also removes a safety net. Bots that hammer your sign-up form can now send thousands of confirmation emails from your domain, damaging its reputation. Protect sign-up and password reset with CAPTCHA and rate limits, and watch for unusual spikes in sends. Supabase Auth supports CAPTCHA providers such as Cloudflare Turnstile and hCaptcha.

## What Users See When It Goes Wrong

From a user's perspective, a missing confirmation email looks like a broken product. Many will try again, creating duplicate accounts, and some will leave for good. Add a clear "didn't receive the email?" option with a resend button that respects rate limits, and show which address the email was sent to so typos are easy to spot. Small touches like these recover users who would otherwise be lost silently.

## Testing Deliverability Properly

Sending a test email to your own Gmail account proves little, because providers treat familiar senders differently. Test with fresh addresses at several providers - Gmail, Outlook, a Dutch provider such as KPN or Ziggo mail if relevant to your audience, and a corporate Microsoft 365 account - and check whether messages land in the inbox, the promotions tab or spam. Many providers' tools show authentication results in the message headers; look for "pass" on SPF, DKIM and DMARC. Repeat these tests after any change to your domain, DNS or provider.

## Planning for Growth

As your user base grows, email volume grows with it: confirmations, resets, notifications and receipts. Review your provider plan's limits, keep an eye on bounce and complaint rates, and remove addresses that hard-bounce. Healthy lists and authenticated sending keep delivery reliable at scale.

## Quick Reference: Symptoms and Fixes

| Symptom | Fix |
| --- | --- |
| First sign-ups work, later ones get no email | Configure custom SMTP |
| Emails in spam | Add SPF, DKIM and DMARC; send from your own domain |
| Link opens wrong domain | Update Supabase site URL and redirect list |
| "Link expired" immediately | Use one-time codes or a click-to-confirm page |
| Users cannot tell your email from phishing | Branded templates with clear sender name |

## Keep Your Configuration Documented

Record your SMTP provider, sender domain, DNS records and template owners in your repository's README, so changes to domains or providers never silently break sign-ups.

## Getting Help

Email setup is a standard part of LaunchStudio launches, often combined with branded templates and transactional emails such as receipts and notifications. LaunchStudio is backed by Manifera, which has set up email delivery for client systems for 11+ years from Amsterdam and Ho Chi Minh City; see [Manifera's about page](https://www.manifera.com/about-us/). Supabase documents [custom SMTP setup](https://supabase.com/docs/guides/auth/auth-smtp) in detail. If you are checking the rest of your launch, our [25-point audit checklist](https://launchstudio.eu/en/blog/vibe-code-audit-checklist-25-checks-before-launch) covers email alongside security.

## Real example

### An AI-Native Founder in Action: The Volunteer Sign-Up That Went Silent at 30

Mirjam Dekkers coordinates a food bank in Helmond and built Voedselhulp in Lovable: volunteers sign up for distribution shifts and receive reminders. During the launch evening, the first 30 or so volunteers received confirmation emails. After that, nothing. Volunteers tried again, created duplicate accounts and gave up.

The app used Supabase's built-in email, which had hit its sending limit. Emails that did go out came from a generic address and several landed in spam. Password reset links pointed to the Lovable preview domain.

LaunchStudio configured custom SMTP through an EU-region transactional provider, added SPF, DKIM and DMARC records to the food bank's domain, set production redirect URLs, rewrote templates in Dutch with the food bank's name, switched magic links to one-time codes for volunteers using work email, and merged duplicate accounts.

**Result:** All pending volunteers were confirmed the next morning. Within a month, 210 volunteers were registered, and reminder emails reached inboxes rather than spam.

> *"Thirty people got in and then the door quietly closed. Nobody saw an error, including me."*
> - **Mirjam Dekkers, Founder, Voedselhulp (Helmond)**

**Cost & Timeline:** €850 (Launch Ready package: SMTP, DNS authentication, redirects, Dutch templates, OTP and account clean-up) - completed in 3 business days.

## Frequently Asked Questions

### Does Supabase limit how many auth emails I can send?

Yes. The built-in email service is meant for development and testing and has strict rate limits. For production, Supabase recommends configuring your own SMTP provider, which removes those limits and improves deliverability.

### Which SMTP provider should I use with Supabase?

Any reputable transactional provider works, such as Postmark, Resend, Mailgun or Amazon SES. For European users, prefer one with EU data processing, sign its processing agreement and authenticate your domain.

### Why do my magic links say they have expired or were already used?

Often because an email security scanner opened the link before the user did, consuming it. Using one-time codes, or a confirmation page that requires a click, avoids this.

### How does Manifera approach email deliverability?

As infrastructure, not an afterthought. Manifera's 11+ years of client systems include transactional email at scale, so LaunchStudio configures authentication records, monitoring and templates as part of every launch that sends email.

### Can poor email deliverability affect my domain's reputation online?

Yes. If your domain sends unauthenticated or spammy email, mailbox providers lower its reputation, which can affect all email from that domain, including sales emails. Proper SPF, DKIM and DMARC protect it.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does Supabase limit how many auth emails I can send?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. The built-in service is for development with strict limits; production apps should use custom SMTP." }
    },
    {
      "@type": "Question",
      "name": "Which SMTP provider should I use with Supabase?",
      "acceptedAnswer": { "@type": "Answer", "text": "A reputable transactional provider such as Postmark, Resend, Mailgun or Amazon SES, ideally with EU processing and an authenticated domain." }
    },
    {
      "@type": "Question",
      "name": "Why do my magic links say they have expired or were already used?",
      "acceptedAnswer": { "@type": "Answer", "text": "Email scanners can open links first. Use one-time codes or a confirmation page that requires a click." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera approach email deliverability?",
      "acceptedAnswer": { "@type": "Answer", "text": "As infrastructure, configuring authentication records, monitoring and templates based on 11+ years of client systems." }
    },
    {
      "@type": "Question",
      "name": "Can poor email deliverability affect my domain's reputation online?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Unauthenticated or spammy mail lowers domain reputation for all email; SPF, DKIM and DMARC protect it." }
    }
  ]
}
</script>
