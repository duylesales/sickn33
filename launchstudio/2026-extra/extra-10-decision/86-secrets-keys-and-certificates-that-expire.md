---
Title: "Secrets, Keys, and Certificates That Expire"
Keywords: managing secrets small saas, api key rotation, secret in git history, certificate expiry outage, environment variables production, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Secrets, Keys, and Certificates That Expire

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Secrets, Keys, and Certificates That Expire",
  "description": "Every product accumulates credentials, and two things go wrong with them: they leak into places they should not be, and they expire on a date nobody recorded. What to keep where, how to rotate without downtime, and what to do when a key has been in a repository for a year.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-05-05",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/secrets-keys-and-certificates-that-expire" }
}
</script>

A product of any size accumulates credentials: database passwords, payment provider keys, email service tokens, storage access keys, OAuth client secrets, signing keys, and a certificate or two. Nothing about them is intellectually difficult, and they cause an outsized share of both outages and security incidents, through two failure modes that could not be more different.

One is leakage: a key ends up in a repository, a log file, a screenshot, or a frontend bundle, where it can be found and used. The other is expiry: something stops working at a moment nobody anticipated, because a certificate or credential had a date attached that was never written down.

## Where Secrets Belong, and Where They Keep Turning Up

The rule is simple: secrets live in the environment configuration of the system that needs them, and nowhere else. Not in your code, not in a file committed to the repository, not in a message to a colleague.

In practice they turn up in five places. **Committed to the repository**, usually in a configuration file that was meant to be excluded — and once committed, the secret is in the history permanently, even after being deleted in a later change. **In frontend code**, where anything shipped to the browser is public by definition; a key visible in a bundle is not secret regardless of how it is named. **In logs**, when a request or configuration object is logged wholesale during debugging and never removed. **In error reports**, where the same happens and the values travel to a third-party service. **In screenshots and support tickets**, when someone shares a terminal window showing their environment.

Two habits prevent most of this: excluding environment files from version control at the very start, and reviewing what your logging and error reporting actually include before launch rather than after an incident.

There is a specific trap in products built with AI tools. Public keys — the ones genuinely intended for the browser, such as a payment provider's publishable key or an analytics identifier — are safe to expose, and secret keys are not. A generated implementation sometimes places the wrong one in the frontend because both were available and the distinction was not made. Knowing which of your keys are which is a five-minute audit worth doing.

## Rotation Without Downtime

Credentials should be replaceable, and being able to replace one calmly is what makes a suspected leak a small event rather than a crisis.

The requirement that makes rotation possible is that your system can accept two valid credentials briefly. For an outgoing key — one you use to call a provider — this is straightforward: create a new key at the provider, deploy it, verify, then revoke the old one. For an incoming secret — one others use to authenticate to you, such as a webhook signing secret — you need to accept both the old and new value for an overlap period, which has to be built rather than assumed.

Some credentials warrant a schedule: annually for most, or whenever someone with access leaves. Others warrant rotation immediately: anything you suspect has been exposed, and anything that has ever appeared in a repository, a log, or a screenshot.

What matters more than the cadence is knowing where each credential is used. Rotating a database password used in four places and remembering only three produces a partial outage that is confusing to diagnose. A short inventory — what the credential is, where it is used, where it came from — makes rotation a routine operation rather than an investigation.

## The Dates Nobody Wrote Down

The second failure mode is entirely preventable and still catches people every year.

**TLS certificates** expire, typically after 90 days for automated ones. Automatic renewal usually works and occasionally does not — a changed DNS record, a renewal process that silently stopped — and the failure mode is a browser warning telling every visitor your site is unsafe.

**Domain registrations** expire, and a lapsed domain is a total outage plus a recovery process that is not always fast.

**Provider API versions** are deprecated with notice, and continuing to call an old version eventually fails.

**OAuth client secrets** at some providers expire, notably in the Microsoft ecosystem, where a two-year default catches people who set an integration up and forgot it.

**Signing keys, service accounts, and access tokens** issued with an expiry date do the same.

The remedy is one list, reviewed quarterly, containing everything with a date and where the renewal happens. Add calendar reminders several weeks ahead of each. Where automatic renewal exists, monitor that it worked rather than trusting that it will — a check that alerts when a certificate is within two weeks of expiry costs nothing and removes the entire category.

Setting up proper secret storage, an inventory with expiry dates, and rotation that does not require downtime is small, unglamorous production work that prevents both the leak and the outage. LaunchStudio, backed by Manifera's 11+ years of production engineering, audits credential handling — including what has ended up in repository history — as part of launch preparation. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## When a Secret Has Already Leaked

Assume it has, at least once. The response is a sequence, and the order matters.

**Rotate first, investigate second.** Create a new credential, deploy it, revoke the old one. The instinct to first determine whether anyone used it wastes the window in which it remains valid.

**Then look for use.** Provider dashboards show recent API activity; unusual patterns, unfamiliar addresses, or requests at hours you were not working are what you are looking for.

**Remove it from where it leaked**, understanding that deleting a secret from a repository does not remove it from the history. Rewriting history is possible and disruptive; the reliable answer is that the credential is now invalid, which is why rotation comes first.

**Consider the obligations.** If a leaked credential could have given access to personal data, that is potentially a reportable incident under GDPR, with a 72-hour notification window in some circumstances. This is worth understanding before it happens rather than during.

A prevention worth adopting: automated secret scanning on your repository, which most code hosting platforms offer at no cost. It catches the accidental commit within minutes rather than a year later, and providers themselves increasingly scan public repositories and revoke keys they find — which is helpful and also means a leak can become an unexplained outage.

## Real example

### The Certificate That Expired on a Saturday

Youssef Hamdi ran Wachtkamer, a check-in system for medical practices, built in Cursor. Certificate renewal was automated and had worked reliably for over a year.

A DNS change made while adding a subdomain removed a record the renewal process relied on. The renewal failed silently at 60 days and again at 75. On a Saturday morning the certificate expired, and every browser reaching the product displayed a full-page security warning. Practices opening on Saturday could not check patients in; the first message reached him two hours later, and the fix took a further hour once identified.

The subsequent audit found more. The payment provider's secret key was present in the repository history, committed 14 months earlier in a configuration file that had been deleted three days later — and the key had never been rotated. A storage access key with full read and write permissions was included in the frontend bundle, having been used for uploads. And an OAuth client secret for the practice-management integration was 22 months old with a two-year expiry, due to fail within eight weeks.

**Result:** all credentials rotated, an inventory created with usage locations and expiry dates, calendar reminders and monitoring for certificate expiry at 14 days, uploads reworked to use short-lived server-issued credentials rather than an embedded key, and secret scanning enabled on the repository.

> "The certificate was the visible problem. The audit it triggered found a payment key that had been sitting in my repository for over a year, which was the actual one."
> — **Youssef Hamdi, Founder, Wachtkamer**

**Cost & Timeline:** credential audit, rotation, and expiry monitoring delivered in 2 business days.

## Frequently Asked Questions

### Where should secrets be stored?

In the environment configuration of the system that needs them, never in code, committed files, or frontend bundles. Anything shipped to the browser is public regardless of how it is named.

### What do I do if a key was committed to my repository?

Rotate it immediately, then investigate whether it was used. Deleting the file does not remove the value from history, so the only reliable remedy is invalidating the credential.

### How often should credentials be rotated?

Annually as a baseline, whenever someone with access leaves, and immediately for anything that may have been exposed. Knowing where each credential is used matters more than the cadence.

### Why do certificates still expire when renewal is automated?

Because automatic renewal can stop working silently, often after a DNS change, and nothing reports the failure. Monitoring that alerts when expiry is within two weeks removes the problem.

### Which expiry dates should I be tracking?

TLS certificates, domain registrations, OAuth client secrets, provider API version deprecations, and any token or service account issued with an expiry. One list, reviewed quarterly, with reminders set weeks ahead.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Where should secrets be stored?", "acceptedAnswer": { "@type": "Answer", "text": "In the environment configuration of the system that needs them, never in code, committed files, or frontend bundles. Anything shipped to the browser is public." } },
    { "@type": "Question", "name": "What do I do if a key was committed to my repository?", "acceptedAnswer": { "@type": "Answer", "text": "Rotate it immediately, then investigate use. Deleting the file does not remove the value from history, so invalidating the credential is the only reliable remedy." } },
    { "@type": "Question", "name": "How often should credentials be rotated?", "acceptedAnswer": { "@type": "Answer", "text": "Annually as a baseline, whenever someone with access leaves, and immediately for anything possibly exposed. Knowing where each credential is used matters more than cadence." } },
    { "@type": "Question", "name": "Why do certificates still expire when renewal is automated?", "acceptedAnswer": { "@type": "Answer", "text": "Automatic renewal can stop working silently, often after a DNS change, with nothing reporting the failure. An alert at two weeks before expiry removes the problem." } },
    { "@type": "Question", "name": "Which expiry dates should I be tracking?", "acceptedAnswer": { "@type": "Answer", "text": "TLS certificates, domain registrations, OAuth client secrets, provider API deprecations, and any token or service account with an expiry, on one quarterly-reviewed list." } }
  ]
}
</script>
