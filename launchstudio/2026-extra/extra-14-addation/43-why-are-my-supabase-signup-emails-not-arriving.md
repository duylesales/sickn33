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
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/why-are-my-supabase-signup-emails-not-arriving" }
}
</script>

**Short answer:** most likely because your app still uses Supabase's built-in email service, which is intended for development and testing and has strict sending limits. Once real users sign up, confirmation, magic link and password reset emails get rate-limited, delayed or land in spam. The fix is to configure a custom SMTP provider, authenticate your sending domain with SPF, DKIM and DMARC, and send from an address on your own domain.

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
