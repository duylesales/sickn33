---
Title: "Telling Customers When Something Is Broken"
Keywords: status page small saas, incident communication template, outage email to customers, when to tell customers about downtime, transparency after bug, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Telling Customers When Something Is Broken

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Telling Customers When Something Is Broken",
  "description": "How a founder communicates during an outage matters more to customer retention than how long the outage lasted. What to say in the first fifteen minutes, when a status page is worth having, and why the instinct to stay quiet until it is fixed is the expensive one.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-04-23",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/telling-customers-when-something-is-broken" }
}
</script>

Something will break. Not as a possibility to be minimised but as a certainty to be planned for — a provider outage, a bad deploy, an expired certificate, a database that stops accepting connections at the worst possible hour. What determines whether customers leave over it is rarely the duration. It is whether they found out from you or from their own failed attempt to use your product, and whether what you told them was accurate.

The instinct almost every founder has is to stay quiet and fix it, because announcing a problem feels like advertising incompetence. That instinct is backwards, and it is worth understanding why before you are in the middle of one making the decision under pressure.

## Silence Is Read as Not Knowing

From a customer's side, an unexplained failure has two possible interpretations: the vendor is aware and working on it, or the vendor has no idea. Silence is indistinguishable from the second, and the second is far more alarming — it suggests that when something goes wrong nobody notices, which raises questions about everything else they cannot see.

There is also a practical cost. Every customer who cannot use your product will try to find out why, and if you have not said anything, they contact you. A single sentence posted where they can find it prevents twenty support emails, each of which requires a reply during the exact period you most need to be working on the problem.

The threshold for saying something is lower than founders assume. If a customer would notice, say something. Partial failures deserve it as much as complete ones — "invoices are not sending, everything else works" is more useful than silence and prevents customers assuming the whole product is unreliable.

## What to Say in the First Fifteen Minutes

The first message should go out before you know the cause, and this is the part that feels wrong and is correct. Three elements, no more.

**What is affected, in their terms.** Not "the API is returning 500s" but "creating and sending invoices is currently failing. Viewing existing invoices works normally."

**That you are working on it.** One line.

**When you will next update**, and then meet it. "Next update within 30 minutes" is a commitment, and keeping it — even to say there is no news — is what builds the confidence that carries you through the incident.

Deliberately absent: a cause you do not yet know, an estimated resolution time you cannot support, and any assignment of blame. Guessing at either produces a correction later, and corrections during an incident cost more credibility than the original uncertainty.

Then update on the schedule you promised, even when nothing has changed. "Still investigating, next update in 30 minutes" reads as control. An hour of silence after promising 30 minutes does not.

## Where to Post It

Two channels, chosen for different reasons.

**A status page**, which is the thing customers check when your product is not working, and which — critically — must be hosted somewhere independent of your infrastructure. A status page on the same server as the product is unavailable exactly when it is needed. Hosted services exist for this at low cost; a simple page on separate hosting works too.

**Email to affected customers**, for anything significant or prolonged. This is the one customers remember. Send it while the problem is ongoing, not after.

An in-product banner is useful for partial failures, when customers can still log in. And for a small product, a personal message to your handful of largest customers is worth more than any broadcast — that is the relationship that survives incidents.

Whether to build a status page before launch depends on who your customers are. Selling to businesses whose own operations depend on your product, yes; it also appears in security questionnaires. Selling to individual users who will simply try again later, it can wait — but knowing where you will post, before you need to, takes ten minutes and removes one decision from a bad moment.

## The Message After: What Actually Rebuilds Confidence

When it is resolved, one more message closes the loop, and this is where trust is either restored or quietly lost.

Four elements: what happened, in plain language; what the impact was, specifically — including whether any data was lost or any action needs to be taken by the customer; what you did to fix it; and what you are changing so it does not recur. The last one is what distinguishes a vendor customers keep from one they start evaluating alternatives to.

Be specific and be honest about cause. "A configuration change we deployed caused the database to reject connections" is better received than "an unexpected technical issue", because vagueness reads as evasion. Owning a mistake plainly is, in practice, the single most trust-restoring thing available — customers know software breaks, and what they are assessing is whether you understand your own system.

Two things to avoid. Do not blame a provider as though it absolves you: choosing and configuring providers is your responsibility, and customers know it. And do not promise it will never happen again, which nobody believes. Say what specific change you have made.

If data was lost or affected, say so immediately and precisely. The temptation to soften this is strong and the consequence of a customer discovering it later, independently, is severe.

## What Has to Exist Before You Can Communicate

Communication depends on knowing. If you learn about outages from customer emails, you cannot post within fifteen minutes, because your fifteen minutes started when someone else noticed.

The minimum is uptime monitoring that checks your product from outside and alerts you, error tracking that notifies you when failures spike, and a check on the things that fail silently — background jobs, scheduled work, payment webhooks. This is a small amount of setup that turns "the customer told me" into "I knew before they did", which is the difference between managing an incident and reacting to one.

It also helps to have written down, in advance, what you will do: where to post, what the first message says, who you contact. Composing that under pressure while also diagnosing a database problem is how people send messages they regret.

Setting up monitoring that detects failures before customers do, and the silent-failure checks most prototypes lack entirely, is a small and well-defined piece of production work. LaunchStudio, backed by Manifera's 11+ years of production engineering, includes it in launch preparation. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Real example

### Four Hours of Silence and Two Cancellations

Sanne Bosman ran Planbord, a shift-planning tool for logistics firms, built in Cursor. A database connection limit was reached on a Monday morning — the busiest hour of her customers' week — and the product returned errors for four hours.

She spent the four hours fixing it, which she considered the responsible priority. She had no status page and sent nothing. Customers emailed, then phoned, then emailed again; by the time the product recovered there were 31 support messages, several from operations managers who had been unable to publish that week's shifts.

She sent one message afterwards, saying the issue had been resolved and apologising for the inconvenience. It did not describe what happened, whether anything had been lost, or what would change. Two customers cancelled within a fortnight, both citing not the outage but not being told anything during it, and one noting that they had spent the morning unsure whether the company still existed.

**Result:** external uptime monitoring with alerts, error-rate alerting, and silent-failure checks on background jobs; an independently hosted status page; and a written incident procedure with a first-message template. Two months later a provider outage caused 90 minutes of degraded service — a status post went up within eight minutes, three updates followed, and a full explanation was emailed the same day. Support messages during that incident: two, both saying thank you for the updates.

> "The second outage lasted a quarter as long and cost me nothing, and the only difference was that I told people what was happening while it was happening."
> — **Sanne Bosman, Founder, Planbord**

**Cost & Timeline:** monitoring, alerting, and status infrastructure set up in 2 business days.

## Frequently Asked Questions

### Should I tell customers about an outage before I know the cause?

Yes. The first message should go out within about fifteen minutes and say what is affected, that you are working on it, and when you will next update. Waiting for the cause means customers learn from a broken product instead.

### Does a small product need a status page?

If your customers are businesses whose work depends on your product, yes, and it also appears in security questionnaires. It must be hosted independently of your product, or it will be unavailable exactly when it is needed.

### How often should I post updates during an incident?

On whatever schedule you promised, and keep it even when there is no news. Saying "still investigating, next update in 30 minutes" reads as control; missing a promised update does the opposite.

### What should the message after an incident contain?

What happened in plain language, the specific impact including any data loss, what you did, and what you are changing to prevent recurrence. The last element is what determines whether customers stay.

### What has to be in place before I can communicate quickly?

External uptime monitoring, error-rate alerting, and checks on things that fail silently such as background jobs and payment webhooks. Without them your response starts when a customer notices rather than when the failure begins.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Should I tell customers about an outage before I know the cause?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. Within about fifteen minutes, say what is affected, that you are working on it, and when you will next update. Waiting for the cause means customers learn from a broken product." } },
    { "@type": "Question", "name": "Does a small product need a status page?", "acceptedAnswer": { "@type": "Answer", "text": "If customers are businesses depending on your product, yes, and it appears in security questionnaires. It must be hosted independently or it will be unavailable when needed." } },
    { "@type": "Question", "name": "How often should I post updates during an incident?", "acceptedAnswer": { "@type": "Answer", "text": "On the schedule you promised, even when there is no news. Keeping the cadence reads as control; missing a promised update does the opposite." } },
    { "@type": "Question", "name": "What should the message after an incident contain?", "acceptedAnswer": { "@type": "Answer", "text": "What happened in plain language, the specific impact including any data loss, what you did, and what you are changing to prevent recurrence." } },
    { "@type": "Question", "name": "What has to be in place before I can communicate quickly?", "acceptedAnswer": { "@type": "Answer", "text": "External uptime monitoring, error-rate alerting, and checks on silent failures such as background jobs and payment webhooks, so your response starts when the failure begins." } }
  ]
}
</script>
