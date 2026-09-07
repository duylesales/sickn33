---
Title: "Spam, Bots, and Abuse on Anything Public-Facing"
Keywords: signup spam prevention SaaS, bot signups free tier abuse, contact form spam, credential stuffing protection, rate limit login attempts, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Spam, Bots, and Abuse on Anything Public-Facing

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Spam, Bots, and Abuse on Anything Public-Facing",
  "description": "Every form reachable without logging in will be found by automated traffic within days of launch. What actually gets attacked, why signup spam damages more than your metrics, and the layered defences that stop it without punishing real customers.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-04-09",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/spam-bots-and-abuse-on-anything-public-facing" }
}
</script>

Nothing about launching a product announces it to the internet's automated traffic, and yet within days of a domain becoming publicly reachable, scanners will have found your signup form, your contact form, your password reset, and any endpoint that accepts a request without a login. They are not looking for you specifically. They are enumerating everything, constantly, and your product is now part of everything.

Founders are usually surprised by this because during development nothing happened — the prototype lived at a preview URL nobody knew about. The first week of real hosting is a different environment entirely, and the forms that worked perfectly for four months of testing meet a category of traffic they were never designed for.

## What Actually Gets Attacked, and Why It Costs You

Five things, in roughly the order they arrive.

**Signup forms.** Automated account creation, sometimes to abuse a free tier, sometimes to use your product's emails to deliver content elsewhere, often for no discernible reason beyond that the form existed. The cost is not only noise in your numbers: every fake signup that triggers a welcome email sends mail to an address that does not want it, and enough of those damage your sending reputation, which affects delivery of the emails your real customers need.

**Contact and enquiry forms.** The oldest target. If the form sends you an email, it will be used to send you a great many emails.

**Login endpoints.** Credential stuffing — trying username and password pairs from other services' breaches — is entirely automated and continuous. Your customers reuse passwords, so some of those attempts will succeed unless something stops them.

**Password reset.** Abused both to enumerate which email addresses have accounts and to bombard a specific person with reset emails.

**Anything expensive that runs without authentication.** A public search, a report generator, a preview, and above all anything calling a paid third-party service. Free tiers of AI features are the current favourite, because the attacker's cost is zero and yours is not.

That last category deserves emphasis: an unauthenticated endpoint that costs you money per call is not a spam problem, it is a billing problem, and it can produce a four-figure invoice over a weekend.

## Layers, Not a Single Wall

There is no single control that stops abuse without also stopping customers. What works is several cheap measures stacked, each removing a category.

**Rate limiting by IP and by target.** The first and most effective layer. Five signup attempts per IP per hour, five reset requests per email address per hour, ten login attempts before a delay. Most automated traffic is defeated by this alone, and legitimate customers never encounter it.

**Honeypot fields.** A form field hidden from human view; if it is filled in, the submission came from a script. Costs nothing, catches a surprising share of simple bots, and is invisible to real people — unlike a CAPTCHA.

**Email verification before anything valuable.** Requiring a confirmed address before the account can use paid features, send anything, or appear publicly removes most of the incentive to create accounts in bulk.

**Blocking disposable email domains.** A maintained list handles the low-effort cases. Not comprehensive, cheap to apply.

**A CAPTCHA, last.** Modern invisible challenges are far less intrusive than the old image grids, but they still add friction and fail for some legitimate users. Reach for it when the cheaper layers prove insufficient, not first.

**Progressive delays on repeated failures.** For login specifically, an increasing delay after each failed attempt makes credential stuffing impractical without ever locking a real customer out — which is better than a hard lockout, since lockouts can themselves be used to deny service to a specific account.

## Protecting Login Without Punishing Customers

Login deserves its own treatment because the trade-off is sharpest: too little and accounts get taken over, too much and you lock out the person paying you.

Rate limit by both source address and target account, because the two attack shapes are different — many passwords against one account, or one common password against many accounts. Apply increasing delays rather than lockouts. And never let error messages distinguish between "no such account" and "wrong password", which is how attackers build a list of valid addresses to focus on.

Two higher-value measures worth having. **Notify on new-device sign-in**: an email saying an account was accessed from an unfamiliar device is often how a takeover is discovered, and it costs a template. **Offer two-factor authentication**, at minimum for account owners on team plans. It need not be mandatory to be valuable; it also answers a question that appears in nearly every business customer's security review.

If a customer's password appears in a known breach — services exist that check this without receiving the password itself — requiring a change at next login is a legitimate and appreciated intervention.

Adding rate limiting, honeypots, verification gates, and login protection is a small, well-understood piece of work, and it is consistently absent from AI-generated products because nothing in a prototype's development ever exercises hostile traffic. LaunchStudio, backed by Manifera's 11+ years of production engineering, hardens public-facing endpoints before launch, including the unauthenticated paths that cost money per request. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Cost Controls Are Part of Abuse Prevention

Any feature that spends money per use needs a ceiling that is enforced by your own code, not only by your provider's dashboard.

Three layers: a per-account limit, so one customer cannot consume everything; a global daily cap, so total spend has an upper bound regardless of where it comes from; and an alert when either is approached, so you learn about unusual consumption on the day rather than in the invoice.

The provider's own budget alerts are useful but insufficient — they typically notify after spending has occurred, and often hours later. The control that actually protects you is your product refusing to make the call, which requires counting usage yourself.

And treat any expensive operation available without authentication as a mistake to be corrected rather than a limit to be tuned. A demo or trial of an AI feature should require at least a verified email address, or it will be found and used at your expense.

## Watching Without Building a Security Programme

You do not need monitoring infrastructure to notice most abuse. Four numbers, checked weekly, cover it: signups per day, the proportion of signups that verify their email, failed login attempts, and daily spend on anything metered.

Sudden changes in any of these are the signal. A tripling of signups with a collapse in the verification rate is bot registration in progress. Failed logins jumping by an order of magnitude is credential stuffing. Metered spend rising without a corresponding rise in customers is abuse of a paid feature.

Two alerts are worth setting up beyond that: one for daily spend exceeding a threshold, and one for a sudden spike in signups. Both take minutes to configure and both catch problems while they are still small.

## Real example

### Four Thousand Accounts and a €1,900 Bill

Ahmed Bensaid launched Sameninkopen, a group-purchasing tool for hospitality businesses, built in Bolt. It included a free AI feature that summarised supplier quotes, available immediately after signup with no email verification, calling a paid model on each use.

Nine days after launch, signups jumped from a handful a day to several hundred. The AI summariser was being called continuously by automated traffic. Over a weekend, roughly 4,000 accounts were created and the model bill reached about €1,900 — discovered on Monday, because the provider's budget alert had been set at a monthly threshold that took until then to cross.

The secondary damage was worse in the longer term. Welcome emails to 4,000 non-existent addresses produced a hard-bounce rate that got his sending domain flagged, and for the following three weeks legitimate customers' verification emails were landing in spam.

**Result:** email verification required before any metered feature, rate limiting on signup by address and by IP, a honeypot field on the signup form, per-account and global daily caps on model calls enforced in the product, disposable domains blocked, and alerts on signup rate and daily spend. The fake accounts were removed and the sending domain's reputation recovered over about a month.

> "The AI feature was the reason people signed up. It was also a way for anyone in the world to spend my money, and it took nine days for someone to find it."
> — **Ahmed Bensaid, Founder, Sameninkopen**

**Cost & Timeline:** abuse prevention and cost controls delivered in 2 business days.

## Frequently Asked Questions

### How quickly will bots find a newly launched product?

Within days. Automated scanners enumerate publicly reachable addresses continuously, so a form that has never been attacked during development will meet hostile traffic almost immediately after launch.

### Is a CAPTCHA the right first defence?

No. Rate limiting by IP and by target, a honeypot field, and email verification before valuable actions stop most automated traffic with no friction for real customers. A CAPTCHA is a later layer, not a first one.

### Why does signup spam damage email delivery?

Welcome emails sent to fabricated addresses bounce heavily, and a high bounce rate causes mail providers to treat your domain as suspect, which affects delivery of the messages real customers need.

### How do I protect login without locking out real customers?

Rate limit by both source and target account, apply increasing delays rather than hard lockouts, keep error messages identical for unknown accounts and wrong passwords, and notify customers of sign-ins from new devices.

### What stops an AI feature from being used to run up a bill?

Requiring a verified account before use, per-account and global daily caps enforced in your own code, and alerts on daily spend. Provider budget alerts notify after the money is spent and are not a control.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "How quickly will bots find a newly launched product?", "acceptedAnswer": { "@type": "Answer", "text": "Within days. Automated scanners enumerate publicly reachable addresses continuously, so forms never attacked during development meet hostile traffic almost immediately after launch." } },
    { "@type": "Question", "name": "Is a CAPTCHA the right first defence?", "acceptedAnswer": { "@type": "Answer", "text": "No. Rate limiting by IP and target, a honeypot field, and email verification before valuable actions stop most automated traffic with no friction for real customers." } },
    { "@type": "Question", "name": "Why does signup spam damage email delivery?", "acceptedAnswer": { "@type": "Answer", "text": "Welcome emails to fabricated addresses bounce heavily, and a high bounce rate causes mail providers to treat the domain as suspect, affecting delivery to real customers." } },
    { "@type": "Question", "name": "How do I protect login without locking out real customers?", "acceptedAnswer": { "@type": "Answer", "text": "Rate limit by source and by target account, use increasing delays rather than lockouts, keep error messages identical for unknown accounts and wrong passwords, and notify on new-device sign-ins." } },
    { "@type": "Question", "name": "What stops an AI feature from being used to run up a bill?", "acceptedAnswer": { "@type": "Answer", "text": "A verified account before use, per-account and global daily caps enforced in your own code, and spend alerts. Provider budget alerts notify after the money is spent." } }
  ]
}
</script>
