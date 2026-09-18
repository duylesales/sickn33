---
Title: "Lovable Payments: Subscriptions That Survive Failed Cards"
Keywords: lovable payments, subscription billing, failed payments, dunning, involuntary churn, SEPA mandate, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: SaaS Scale-Up
---

# Lovable Payments: Subscriptions That Survive Failed Cards

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Payments: Subscriptions That Survive Failed Cards",
  "description": "Between five and ten percent of subscription charges fail for reasons unrelated to willingness to pay. What a Lovable app must do with a failed payment: retries, grace periods, mandate expiry and the emails that recover revenue.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-payments-subscriptions-that-survive-failed-cards" }
}
</script>

Somewhere between five and ten percent of recurring charges fail every month, and almost none of those failures mean a customer decided to leave. Cards expire. Banks decline for reasons they do not explain. A direct debit bounces because a business current account was briefly empty on the wrong Tuesday.

The industry name for the customers you lose this way is involuntary churn, and for a subscription product it is routinely the largest single source of cancellation — larger than competitors, larger than dissatisfaction, and the only one you can fix with code rather than with a better product.

An AI-built subscription app almost never handles it. The generated integration creates a subscription, marks the user active, and has no concept of what happens on the day a charge does not go through.

## What Happens Today in Your App

Find out before you read further. Open your database and ask: if a renewal failed this morning, what would be different?

In most Lovable and Bolt applications the honest answer is *nothing*. The user row still says active. The webhook for the failed payment arrived at an endpoint that only listens for successes, or at no endpoint at all. The customer keeps their access indefinitely and you never learn that they stopped paying — until you reconcile the provider dashboard against your own revenue and find eleven accounts that have not paid since spring.

The mirror-image failure is just as common and worse: the app cuts access the instant a charge fails. A good customer whose card expired opens your product, finds themselves locked out with no explanation, and now has an excellent reason to evaluate an alternative. You have converted a five-day administrative problem into a cancellation.

## The Shape of a Correct Response

There is a standard pattern and it is not complicated.

**Retry, on a schedule, several times.** A charge that fails today frequently succeeds on Thursday, because salaries land and balances change. Stripe and Mollie both do this automatically if you let them — typically three to four attempts over two to three weeks. Your job is mostly not to interfere.

**Keep access during a grace period.** Give the customer the retry window with their account working. The revenue you protect by cutting them off on day one is roughly zero; the revenue you lose is everything they would have paid you afterwards.

**Tell them, in a way that is easy to act on.** The first email should be short, specific and contain a single link that goes straight to a page where they can update their payment method without logging in through three screens. Not a demand — a notification, because most recipients genuinely did not know.

**Escalate slowly and stop clearly.** A second message part-way through the window, a final one before access ends, and then a defined end state: subscription cancelled, access restricted, data retained for a stated period. A customer who returns two months later should be able to pay and resume, not discover their account was deleted.

**Record every step.** Which attempt failed, when, with what reason, what you sent and what the customer did. When somebody writes to say they were charged after cancelling — and someone will — this log is how you answer in two minutes instead of an afternoon.

## Three States, Not Two

The structural mistake in AI-generated billing code is that a subscription is treated as a boolean. Active, or not.

Real subscriptions need at least: **active** (paid and current), **past due** (a payment failed, retries running, access continues), **cancelled** (ended, access restricted, data retained), and usually **paused** as well, because seasonal businesses ask for it constantly and building it later means retrofitting every permission check.

Model those states explicitly in your own database rather than inferring them from the provider on each request. Your application must be able to answer "may this person use the product right now" without a network call, and it must give the same answer when the provider's API is having a bad morning.

## SEPA Direct Debit Fails Differently

If your Dutch customers pay by *automatische incasso*, the failure modes are not the card ones and the timing is unlike anything a card-based tutorial prepares you for.

Direct debit is slow. A collection can take several business days to confirm, and a reversal can arrive weeks after you believed the payment succeeded, because consumers in SEPA have a long unconditional refund right. Code that grants access on "payment initiated" is code that will eventually give away a year of product for free.

Mandates also expire and lapse. A mandate unused for a long period may no longer be valid, a customer can revoke it at their bank without ever telling you, and the first you hear is a bounce with a reason code. Your app needs to treat mandate status as a thing that changes, not as something established once at signup.

The practical rule: wait for settlement before granting anything valuable, and keep the reversal window in mind before you treat revenue as certain.

## The Emails Do Most of the Work

Recovery is overwhelmingly an email problem rather than an engineering one, and the difference between a mediocre sequence and a good one is large enough to matter to your revenue.

What works: sending from a real address a human replies to, naming the product and the amount, saying plainly which payment method failed, and giving one link that solves it. What does not: a generic "billing issue" subject line, a link to a login page rather than to the fix, and anything that reads like a collections notice.

And send them from a domain that is properly configured, or your carefully written recovery sequence will be filtered before anyone reads it — which is the quiet reason many founders conclude that dunning emails do not work.

## Watch the Number That Tells You It Is Working

Failed-payment handling is one of the few pieces of billing work with a metric attached, and the metric is easy to compute: of charges that failed in a month, what proportion eventually succeeded without the customer cancelling?

Below about forty percent, something is broken — usually the emails are not arriving, or the update-payment link requires a login the customer has forgotten. Between fifty and seventy-five percent is what a competent setup produces. Above that and you are either lucky in your customer base or you sell to businesses with reliable direct debits.

Two secondary numbers are worth a monthly glance. How many accounts are past due right now, which should be a small and stable number rather than a growing one. And how long the average past-due account stays past due — if that is climbing, your final step is not firing and accounts are sitting in limbo with working access.

None of this needs a dashboard. A saved query, run on the first Monday of the month and written in a note, is enough for a product of any size a solo founder is running. What matters is that the number exists at all, because involuntary churn is invisible by nature: nobody writes to tell you they stopped paying by accident, and the customers it removes are, on average, the ones who liked your product enough to still be subscribed.

## One Thing Not to Automate

There is a temptation, once the sequence works, to let it handle everything — including the customer who has failed four times across three months and whose account keeps recovering just long enough to fail again.

Look at those by hand. A repeatedly failing account is usually one of three things: a business whose finance process genuinely cannot accommodate your billing date, a customer who wants to leave and has chosen the passive route, or a card being used by someone who should not have it. Each deserves a different response, and none of them is a fifth automated email.

For the first, moving the billing date or switching them to annual invoicing solves it permanently. For the second, a short human message asking whether they still want the product is more respectful than a machine that keeps trying. For the third, you want to know.

Five minutes a month on the handful of accounts the automation could not resolve is the highest-value billing work a founder does, precisely because everything easier has already been handled by the system.

## Setting This Up

For a running subscription product this is two to four days: subscription states modelled properly in your own database, the provider's retry schedule configured deliberately rather than by default, a grace period with access maintained, a payment-update page reachable from an email without a full login, a three-message recovery sequence from a verified sending domain, webhook handling for the failure and recovery events your integration currently ignores, a clear end state with data retention, and a small internal view showing which accounts are past due right now.

LaunchStudio builds this as part of payment integration under the Launch & Grow package, hosted and monitored at €49 per month. Behind it is Manifera — 160+ delivered projects and eleven years of production systems, with engineering in Ho Chi Minh City and client contact from Amsterdam.

[Ask us what your app does on a failed renewal](https://launchstudio.eu/en/#contact). It is usually a short and uncomfortable answer.

## Real example

### Eleven Accounts That Had Not Paid Since March

Fleur Alkemade runs Praktijkvoorraad, built in Lovable: stock and ordering software for independent physiotherapy and podiatry practices, €39 per month, 180 subscribers across the eastern Netherlands.

Her integration handled the happy path correctly. A subscription created a row, set `is_active` to true, and that was the entire model. There was no webhook handler for failed payments — the endpoint existed but ignored every event type except the one that confirmed a first charge.

She discovered the problem while preparing figures for her accountant in October. The provider dashboard showed 180 active subscriptions; her bank statements showed consistently fewer payments than that. Eleven practices had a failed card or a lapsed SEPA mandate — the oldest since March — and had been using the product free for up to seven months. None of them knew. Two had assumed the charges were simply on a different statement.

Five business days: the subscription model rewritten with active, past due, paused and cancelled states held in her own database and checked by a single access function; failure, recovery and mandate-revoked webhook events handled with idempotency; the provider's retry schedule set to four attempts across 21 days; a fourteen-day grace period during which the practice keeps working access; a payment-update page reachable from a signed email link with no login; a three-message recovery sequence sent from a domain with SPF, DKIM and DMARC configured; settlement-based access for direct debit rather than initiation-based; and an internal past-due list Fleur checks on Mondays.

**Result:** nine of the eleven lapsed practices reinstated within two weeks of being told, worth €4,212 in recovered annual revenue. Over the following six months the sequence recovered 71 percent of failed charges automatically, and Fleur's reconciliation went from an afternoon to a glance.

> *"I was not chasing anyone, because I did not know there was anyone to chase. Nine of the eleven paid the day I emailed them — they just thought it was going out."*
> — **Fleur Alkemade, Founder, Praktijkvoorraad (Deventer)**

**Cost & Timeline:** €2,900 (subscription state model, failure and mandate webhooks, retry and grace configuration, recovery sequence with email authentication, settlement-based access, past-due reporting) — completed in 5 business days.

## Frequently Asked Questions

### How long should a grace period be?

Two to three weeks, matching your provider's retry schedule, so access ends only after every automatic attempt has failed. Shorter windows cancel customers whose card simply expired; longer ones give away too much product before you find out.

### Will my provider retry failed payments automatically?

Both Stripe and Mollie can, and you should let them rather than building your own scheduler. What you must build is the reaction: keeping access during the window, notifying the customer and defining what happens when the retries run out.

### Why does SEPA direct debit need different handling from cards?

It settles slowly and can be reversed weeks later under the customer's refund right, and mandates can lapse or be revoked at the bank without notifying you. Grant access on settlement rather than initiation, and treat mandate status as something that changes.

### Should I delete the account when a subscription ends?

No. Restrict access, keep the data for a stated retention period, and say so in the final email. Returning customers are among the cheapest revenue a small product has, and they will not return to a product that erased their work.

### How much revenue does this actually recover?

A well-built sequence typically recovers between half and three quarters of failed charges, which for most subscription products is a larger number than any conversion experiment they are likely to run this year.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long should a grace period be?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Two to three weeks, matching the provider's retry schedule, so access ends only after every automatic attempt has failed."
      }
    },
    {
      "@type": "Question",
      "name": "Will my payment provider retry failed payments automatically?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Stripe and Mollie both can, and you should use their scheduler. What you build is the reaction: grace access, notification, and a defined end state."
      }
    },
    {
      "@type": "Question",
      "name": "Why does SEPA direct debit need different handling from cards?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It settles slowly, can be reversed weeks later under the customer's refund right, and mandates can lapse or be revoked without notice. Grant access on settlement, not initiation."
      }
    },
    {
      "@type": "Question",
      "name": "Should I delete the account when a subscription ends?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Restrict access and retain data for a stated period. Returning customers are cheap revenue, and they will not return to a product that deleted their work."
      }
    },
    {
      "@type": "Question",
      "name": "How much revenue does failed-payment recovery actually return?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A well-built sequence typically recovers half to three quarters of failed charges — usually more than any conversion experiment a small product runs in a year."
      }
    }
  ]
}
</script>
