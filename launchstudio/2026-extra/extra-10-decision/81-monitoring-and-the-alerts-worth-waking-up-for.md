---
Title: "Monitoring and the Alerts Worth Waking Up For"
Keywords: uptime monitoring small saas, alert fatigue solo founder, synthetic check critical flow, silent failure background jobs, error rate alerting, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Monitoring and the Alerts Worth Waking Up For

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Monitoring and the Alerts Worth Waking Up For",
  "description": "A homepage that returns 200 tells you almost nothing. What to monitor in a small product so that real failures reach you and nothing else does, why silent failures need their own checks, and how to set thresholds you will not learn to ignore.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-04-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/monitoring-and-the-alerts-worth-waking-up-for" }
}
</script>

Most small products have monitoring that checks whether the homepage loads, which is roughly equivalent to confirming a restaurant's front door opens. The door works. The kitchen has been closed since Thursday. A homepage returning a successful response says the web server is running; it says nothing about whether customers can log in, whether payments are being recorded, or whether the nightly job that sends every invoice has been failing since a deploy last week.

The right question is not "is the site up" but "which failures would matter, and would I find out?" For most products that list is short, and covering it properly takes an afternoon.

## Check the Journey, Not the Front Door

The single highest-value change to typical monitoring is to check a real flow rather than a page.

A synthetic check — a script running every few minutes from outside your infrastructure — that logs in as a test account, loads the main screen, and performs one meaningful read tells you what a customer would experience. If it can log in and see data, the application, the database, and authentication are all working, which is most of your product in one check.

Two or three of these cover a small product: the core read path, the core write path if it can be done safely with a test account, and the login itself. Run them from outside your own hosting, so that an infrastructure failure does not take the monitoring with it.

Underneath, add a health endpoint that reports whether the application can actually reach its dependencies — database, storage, queue — rather than merely responding. An application that returns a page while unable to reach its database is a specific and common state, and a naive check calls it healthy.

## The Failures That Never Return an Error

This is the category that catches founders, because nothing in ordinary monitoring notices it.

**Background jobs that stopped running.** The worker crashed on Tuesday. No page is broken, no error is served, and emails simply stop being sent. The check for this is a heartbeat: the job reports each successful run, and an alert fires when a run does not arrive on schedule. Without it, the discovery mechanism is a customer asking where their notification went.

**A queue that is growing.** Jobs are being accepted and processed too slowly, so everything works but arrives hours late. Alert on queue depth and on the age of the oldest waiting item.

**Payment webhooks not arriving.** Your provider tried, your endpoint failed, and subscriptions are quietly out of sync with reality. Check both that events are arriving at the expected rate and that your provider is not accumulating failed deliveries.

**Scheduled work that silently did nothing.** A nightly report that runs successfully but produces zero rows because a query changed. Alert on the absence of expected output, not only on errors.

**Certificates and credentials approaching expiry.** These fail completely, on a known date, and are entirely preventable — which makes them the most annoying category to be caught by.

Each is a small check. Together they cover the failures that otherwise get reported by customers days later, which is both the most expensive way to find out and the one that costs the most trust.

## Thresholds You Will Not Learn to Ignore

An alert that fires often and means nothing trains you to dismiss alerts, and then a real one arrives and is dismissed with the same reflex. Alert fatigue is not a minor inconvenience; it is the mechanism by which monitoring stops working.

Three principles keep it useful. **Alert on symptoms customers feel, not on internal metrics.** High CPU is interesting; requests failing is actionable. **Use rates and durations, not single events.** One error is noise; an error rate above a few percent sustained for five minutes is a problem. A single slow request is normal; sustained slowness is not. **Give every alert an action.** If your response to receiving it would be to look and do nothing, it should be a number on a dashboard rather than a notification.

Then split alerts into two tiers, because not everything deserves the same urgency. **Wake you up**: the product is down, payments are failing, data is being lost, or a security event has occurred. **Look at it in the morning**: elevated error rates, a slow queue, a job that failed once and succeeded on retry, expiring credentials with weeks remaining.

Keeping the first tier to a handful of genuine emergencies is what makes it work. If everything is urgent, nothing is.

## Errors, and Knowing Which Customer

Error tracking is separate from uptime monitoring and answers a different question: not "is it working" but "what is failing, for whom, and how often."

Two configuration details make the difference between a tool you use and one you ignore. **Attach the account and user to every error report**, so that an error becomes "this happened 14 times to this customer" rather than a count. That transforms error tracking into a support and retention tool, since it lets you contact the customer who has been hitting a failure without reporting it. **Group errors properly and alert on new ones and on spikes**, not on every occurrence, or the tool becomes a firehose within a week.

Then use it deliberately: read new errors after every deployment, since that is when they appear, and review the top few by frequency weekly. Most products have a small number of errors accounting for the majority of occurrences, and fixing three of them removes most of the noise.

Setting up external synthetic checks, heartbeat monitoring for background work, error tracking with account context, and a small tiered alert policy is a bounded piece of production work that changes how you find out about problems. LaunchStudio, backed by Manifera's 11+ years of production engineering, sets this up as part of launch preparation, including the silent-failure checks prototypes almost never have. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## A Sensible Setup for a Small Product

What this looks like in practice, for a product with a few hundred customers and one person responsible.

An external uptime service running two or three synthetic journey checks every few minutes, alerting after two consecutive failures to avoid noise from momentary blips. Error tracking with account context, alerting on new error types and on rate spikes. Heartbeats on every scheduled job and background worker. Queue depth and age alerts. A weekly review of the top errors and slowest endpoints. Expiry alerts for certificates, domains, and API credentials, set weeks ahead.

Cost is modest — the free and entry tiers of common services cover most of this at this scale — and the setup is an afternoon. The thing that makes it work is not the tooling but the discipline of keeping the urgent tier small and acting on what it tells you.

## Real example

### Eleven Days of Invoices That Were Never Sent

Timo van Loon ran Abonnee, a subscription-billing helper for small publishers, built in Cursor. Monitoring consisted of an uptime service checking the homepage every five minutes, which had reported 100% availability for four months.

Invoices were generated and emailed by a nightly job. After a deploy, that job began failing on start-up due to a missing configuration value. The website was unaffected and continued reporting healthy. For eleven days no invoices were generated, no emails were sent, and no alert fired.

It surfaced when a publisher asked why they had not been invoiced. By then 340 invoices were outstanding across 60 accounts, several customers had assumed their subscriptions had lapsed, and reconciling which had been sent manually in the interim took two days.

The review found two more silent failures in progress: payment webhooks had been failing for three accounts since a routing change, and a weekly usage-report job had been producing empty reports for a month because a query returned nothing after a schema change.

**Result:** heartbeat monitoring on all scheduled jobs alerting when a run is missed, synthetic checks covering login and the core read path, error tracking with account context, webhook delivery monitoring, and alerts on expected output being absent. The nightly job failure would now be detected within an hour.

> "My uptime monitor was green the entire time. It was telling me the truth about the only thing it was watching, which happened not to be the part that mattered."
> — **Timo van Loon, Founder, Abonnee**

**Cost & Timeline:** monitoring and alerting setup delivered in 2 business days.

## Frequently Asked Questions

### Is checking that the homepage loads enough monitoring?

No. It confirms the web server responds while telling you nothing about login, the database, payments, or background work. A synthetic check that logs in and loads real data covers far more in one test.

### How do I detect failures that produce no error?

With heartbeats and expectations: scheduled jobs report each successful run and an alert fires when one is missed, queue depth and age are watched, and the absence of expected output is treated as a failure condition.

### How do I avoid ignoring my own alerts?

Alert on symptoms customers feel, use sustained rates rather than single events, and ensure every alert has an action. Keep the wake-you-up tier to genuine emergencies and route everything else to a morning review.

### What makes error tracking actually useful?

Attaching the account and user to every report, so errors become identifiable customer problems rather than counts, and alerting on new error types and spikes rather than on every occurrence.

### How much does adequate monitoring cost for a small product?

Usually very little. Free and entry tiers of common uptime and error-tracking services cover a few hundred customers, and the setup is an afternoon. The cost is discipline rather than money.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Is checking that the homepage loads enough monitoring?", "acceptedAnswer": { "@type": "Answer", "text": "No. It confirms the web server responds but says nothing about login, the database, payments, or background work. A synthetic check that logs in and loads real data covers far more." } },
    { "@type": "Question", "name": "How do I detect failures that produce no error?", "acceptedAnswer": { "@type": "Answer", "text": "Heartbeats and expectations: jobs report each successful run and alert when one is missed, queue depth and age are watched, and absent expected output is treated as a failure." } },
    { "@type": "Question", "name": "How do I avoid ignoring my own alerts?", "acceptedAnswer": { "@type": "Answer", "text": "Alert on customer-visible symptoms, use sustained rates rather than single events, give every alert an action, and keep the urgent tier to genuine emergencies." } },
    { "@type": "Question", "name": "What makes error tracking actually useful?", "acceptedAnswer": { "@type": "Answer", "text": "Attaching account and user context to every report so errors become identifiable customer problems, and alerting on new error types and spikes rather than every occurrence." } },
    { "@type": "Question", "name": "How much does adequate monitoring cost for a small product?", "acceptedAnswer": { "@type": "Answer", "text": "Usually very little. Free and entry tiers of common services cover a few hundred customers and setup takes an afternoon; the real cost is discipline." } }
  ]
}
</script>
