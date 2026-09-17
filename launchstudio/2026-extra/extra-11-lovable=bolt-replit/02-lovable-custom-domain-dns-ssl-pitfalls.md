---
Title: "Lovable Custom Domain: The DNS, SSL and Email Details That Bite"
Keywords: lovable custom domain, Lovable, DNS records SSL certificate, domain ownership founder, transactional email SPF DKIM, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable Custom Domain: The DNS, SSL and Email Details That Bite

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Custom Domain: The DNS, SSL and Email Details That Bite",
  "description": "What actually happens when you point a custom domain at a Lovable app: apex versus www, SSL issuance, the email records nobody connects to the domain, and who holds the keys. A practical guide for non-technical founders about to go live.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-04",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-custom-domain-dns-ssl-pitfalls" }
}
</script>

Everyone says connecting a domain takes five minutes. That is true, and it is also why so many founders end up with a live app, a working domain, and password reset emails landing in spam for three weeks before anyone tells them.

Pointing a custom domain at a Lovable app really is a short task. The problem is that a domain is not one thing. It is a name with several jobs attached — serving your website, proving your identity, sending your email, and belonging to somebody — and the five-minute version only handles the first one. This article covers the rest, in the order they tend to hurt.

## What Connecting a Domain Actually Does

A domain name is a pointer. When someone types your address, their browser asks the domain name system where to go, and the DNS records you configure supply the answer. Connecting your domain to a Lovable app means adding one or two records that point your name at the place your app is served from.

That is genuinely all the first step is. What matters is that DNS has several different kinds of record doing several different jobs, and the ones controlling your website are not the ones controlling your email. Change the first and your site moves. Change the second carelessly and your email stops arriving, silently, with no error anywhere.

## Apex or www: Choose One, Redirect the Other

Your domain exists in two forms: the apex (`yourapp.nl`) and the subdomain (`www.yourapp.nl`). Search engines treat them as distinct addresses. So do browsers, and so do the systems that issue security certificates.

Pick one as the real address, and make the other permanently redirect to it. Which one you pick matters far less than picking. What goes wrong when you skip this is not dramatic — both versions work — but you end up with two addresses serving identical content, which splits your search visibility, confuses analytics, and produces the peculiar situation where a customer's bookmark works and a colleague's does not because one of them has a certificate and the other does not.

There is also a technical wrinkle worth knowing in advance: apex domains cannot use the same kind of DNS record that subdomains use for this purpose, so hosting providers offer workarounds with different names. This is why your provider's documentation asks for one record type and your registrar offers a differently-named option. It is normal, and it is the step where most founders stall.

## SSL: Automatic Until It Isn't

The padlock in the browser comes from a certificate proving your domain is yours. Modern hosting issues these automatically and renews them automatically, which is why most founders never think about it.

Three things still go wrong. Issuance fails silently if your DNS records are not yet correct, leaving the site loading with a browser warning that destroys trust instantly. Renewal fails if the domain's DNS is later moved somewhere else and nobody updates the verification. And mixed content — a page served securely that loads an image or script over an insecure connection — produces a broken padlock even when the certificate itself is perfect.

The practical check: after connecting, open your site in a private browser window on a phone, on mobile data rather than your own wifi. It is remarkable how many certificate problems are invisible from the laptop that set them up.

## The Email Records Nobody Connects to the Domain

This is where the three-week delay comes in.

Your app sends email: signup confirmations, password resets, booking receipts, invoices. Those emails claim to come from your domain. Receiving mail servers decide whether to believe that claim by checking three kinds of DNS record — one listing which servers may send on your behalf, one carrying a cryptographic signature, and one stating what should happen to messages that fail those checks.

If your app sends through a provider and those records were never added, your messages are unauthenticated. Some will arrive. Many will land in spam. Nobody will tell you, because the people not receiving your password reset emails are, by definition, not able to log in and complain.

Two rules keep this simple. Send transactional email through a proper provider rather than from the app server directly, and add the authentication records that provider gives you at the same time you connect the domain — not later, because later means after your first customer could not reset their password.

## Who Actually Owns the Domain

Ask yourself: if you and your co-founder fell out tomorrow, or your first freelancer stopped answering messages, could you still move your domain?

Domains are frequently registered by whoever happened to be doing the setup — an agency, a developer, a technical friend — in that person's account, with that person's payment card and recovery email. The app is yours; the name people type to reach it is not.

Before launch, confirm three things: the domain is registered in an account you control, the contact email on the registration is one you can access, and you know where the DNS is managed, which is sometimes a different provider from the registrar. If any of those sits with someone else, transfer it now, while everyone is on good terms. The cost of fixing this later ranges from a tedious support process to a genuine loss of your brand address.

## Staging, Preview and the Links You Forget to Change

Once a custom domain exists, you effectively have two addresses for the same app: the original preview URL and the real one. Both usually keep working.

That is convenient and it creates a trail of problems. Payment providers, authentication services and email templates all store redirect and callback addresses, and if those still point at the preview URL, users get bounced to an address that is not your brand — or a flow silently fails. Analytics ends up split across two hostnames. And the preview link, still shared in old messages and pitch decks, keeps serving a version of your app that may drift out of date.

The fix is a boring sweep: update every callback URL, every email template link, every integration setting, and every "share this" link you have sent, then decide whether the preview address should redirect to the real one.

## Changing a Domain After Launch Is Expensive

Founders frequently pick a working name, launch, then rebrand two months later. Technically, moving is straightforward — new domain, new records, redirect the old one. The cost is elsewhere.

Search engines need time to transfer accumulated reputation, and that only happens correctly with permanent redirects on every old address. Customers' bookmarks and password managers are tied to the old name. Payment and authentication integrations need their settings changed again. Email authentication records must be rebuilt for the new domain.

None of this is catastrophic. All of it is avoidable by deciding on the real name before you launch rather than after, which is a product decision, not a technical one.

## A Pre-Flight Checklist for Going Live on Your Own Domain

- Domain registered in your account, with your email and your payment method.
- Apex and www decided, with one redirecting to the other.
- Certificate issued and verified on a phone over mobile data.
- Email authentication records added for your transactional email provider.
- A test signup, password reset and receipt sent to a Gmail address and an Outlook address, and both checked in the inbox rather than the spam folder.
- Every callback and redirect URL updated away from the preview address.
- Analytics recording one hostname, not two.

Seven checks, most of them quick. The reason they matter is that each failure is silent: nothing errors, nothing crashes, and you simply lose some percentage of the users you worked hard to get.

## Where This Sits in a Launch

Domain configuration is small work that sits on top of larger questions — whether secrets are exposed, whether your database has backups, whether payments actually settle. LaunchStudio handles it as part of getting an AI-built prototype production-ready: the domain, the certificate, the email authentication, the callback sweep and the redirects, alongside the security and infrastructure work underneath. The frontend you built in Lovable stays untouched, and the code stays yours.

Behind that is Manifera, a software company with eleven years of engineering behind it and clients including Vodafone and TNO — which mostly matters here because the boring checklist above is exactly the kind of thing experienced teams do by habit and first-time founders discover by accident. If you are about to go live, [describe your project](https://launchstudio.eu/en/#contact) and you will hear back within one business day.

## If It Is Already Live and Something Is Wrong

Most founders read this after connecting the domain, not before. Work through the symptoms in this order, because each step rules out the layer beneath it.

**The site does not load at all.** Almost always a record pointing at the wrong place, or two competing records for the same name. Check what your domain resolves to from a device that has never visited the site — a phone on mobile data is the easiest clean test — rather than from the laptop that may be holding a cached answer.

**The site loads with a certificate warning.** The certificate was requested before the records were correct, or the domain has since moved. Trigger reissuance from your hosting provider once the records are verified, and check again from a device that has never seen the old certificate.

**The site loads securely but the padlock is broken on some pages.** Something on those pages is loading over an insecure connection — usually an image URL, an embedded font or a script that was hardcoded during the build. Fix the references rather than the certificate.

**Everything looks right but users complain about emails.** This is the authentication layer, not the website layer. Send a test signup to a Gmail address and an Outlook address, and check the spam folder rather than trusting that no error appeared.

**Logins or payments redirect somewhere unexpected.** A callback URL somewhere still points at the preview address. Work through each integration's settings rather than searching your code, because these values usually live in a dashboard rather than in the repository.

The pattern behind all five: nothing in a domain misconfiguration produces a loud error. Each failure is silent and partial, which is why a short deliberate test pass after going live is worth far more than the five minutes it takes.

## Real example

### A Recruitment Tool Whose Password Resets Never Arrived

Sanne Bakker launched Shiftly, a shift-matching tool for hospitality staff built in Lovable, on her own domain in a single afternoon. The site loaded, the padlock was green, and she posted the link to two Amsterdam hospitality groups on a Thursday.

Signups came in. Logins did not. Over the following fortnight, about a third of new users never completed registration, and Sanne assumed the onboarding flow was confusing. It was not: her app sent confirmation emails through a transactional provider whose authentication records had never been added to the domain, so a large share of them were being filed as spam. Meanwhile her payment provider's callback URL still pointed at the original preview address, so the handful of users who did subscribe were redirected to a URL that was not her brand and, in two cases, abandoned the flow.

The fix took three business days: authentication records added and verified, the sending domain configured properly, every callback and email template link swept and repointed, apex-to-www redirect standardised, and a test matrix run across Gmail, Outlook and two mobile clients before it was called done.

**Result:** completed registrations rose from roughly two-thirds to over ninety percent of signups in the following three weeks, with no change to the product itself.

> *"Nothing was broken. That was the worst part — the app worked perfectly and a third of my users just quietly disappeared into a spam folder."*
> — **Sanne Bakker, Founder, Shiftly (Amsterdam)**

**Cost & Timeline:** €1,150 (domain, email authentication, callback sweep and verification) — completed in 3 business days.

## Frequently Asked Questions

### How long does a custom domain take to work after I change the records?

Usually minutes to a few hours, occasionally longer, because DNS changes propagate gradually. If it has been more than a day, the cause is almost always a record with the wrong type or a stray leftover record pointing somewhere else, not slow propagation.

### Do I need both yourapp.nl and www.yourapp.nl?

You need to control both and serve one. Pick whichever you prefer as the canonical address and permanently redirect the other to it, so you do not split search visibility and analytics across two addresses.

### Why are my app's emails going to spam even with a working domain?

Because website records and email authentication records are different things. Your site can be perfectly configured while your sending domain remains unauthenticated. Add the records your transactional email provider specifies, then test to real Gmail and Outlook inboxes.

### Can I keep using the preview URL after connecting my own domain?

It generally keeps working, which is precisely the risk: integrations, callbacks and old shared links quietly stay on it. Sweep every setting and template to the real domain, then treat the preview address as a leftover rather than a second entrance.

### What happens to my search ranking if I change domain later?

It transfers, slowly and only if every old address permanently redirects to its new equivalent. Expect a dip and a recovery period, plus reconfiguration of payment callbacks, authentication settings and email records. Choosing the final name before launch avoids all of it.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long does a custom domain take to work after I change the records?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually minutes to a few hours, because DNS changes propagate gradually. If it takes more than a day, the cause is almost always a record with the wrong type or a leftover record pointing elsewhere, rather than slow propagation."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need both the apex domain and the www version?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You need to control both and serve one. Choose a canonical address and permanently redirect the other to it, so search visibility and analytics are not split across two hostnames."
      }
    },
    {
      "@type": "Question",
      "name": "Why are my app's emails going to spam even with a working domain?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Website records and email authentication records are different. A correctly configured site can still have an unauthenticated sending domain. Add the records your transactional email provider specifies and test against real Gmail and Outlook inboxes."
      }
    },
    {
      "@type": "Question",
      "name": "Can I keep using the preview URL after connecting my own domain?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It usually keeps working, which is the risk: integrations, callbacks and old shared links quietly remain on it. Sweep every setting and template to the real domain and treat the preview address as a leftover."
      }
    },
    {
      "@type": "Question",
      "name": "What happens to my search ranking if I change domain later?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It transfers slowly, and only if every old address permanently redirects to its new equivalent. Expect a dip and a recovery period, plus reconfiguration of payment callbacks, authentication settings and email records."
      }
    }
  ]
}
</script>
