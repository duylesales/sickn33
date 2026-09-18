---
Title: "AI App Security: Logging and Audit Trails You Will Need"
Keywords: ai app security, audit trail, logging, incident investigation, Lovable, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI App Security: Logging and Audit Trails You Will Need

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Security: Logging and Audit Trails You Will Need",
  "description": "The questions an incident asks — what happened, who did it, when, and to how many people — can only be answered by records written before it. What to log, what never to log, and how long to keep it.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-13",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-app-security-logging-and-audit-trails-you-will-need" }
}
</script>

Every incident asks the same four questions, and it asks them in a hurry. What happened. Who did it. When did it start. How many people were affected.

None of those can be answered afterwards. They are answered by records written before anybody knew they would be needed — or they are not answered at all, and you find yourself telling a customer, a colleague or a regulator that you do not know.

Logging is the least interesting thing to build and the only thing that makes the bad day survivable. It is also almost entirely absent from AI-generated applications, because nobody asks for it and it contributes nothing to a feature working.

## Three Different Records, Frequently Confused

They serve different purposes and you need all three.

**Application logs** record what the system did: a request arrived, a job ran, an external call failed. Useful for debugging, high in volume, short-lived.

**Error tracking** records what went wrong, grouped and deduplicated, with enough context to reproduce it. This is the one that tells you a feature has been broken for eleven days for a subset of users.

**An audit trail** records what people did to data: who changed this record, to what, when. This is the one that answers the questions above, and it is the one nobody builds.

A product with only the first is common. A product with all three can reconstruct almost any incident in an afternoon.

## What an Audit Trail Should Capture

For tables that matter — anything holding money, permissions, customer data or legal obligations — record for each change: who made it, when, what the values were before, what they became, and where the request came from.

That last field is more useful than it sounds. "The same account, from an address it has never used before, at four in the morning" is a different story from "the same account, from the office, during working hours", and the difference determines whether you are dealing with a mistake or a compromise.

Three implementation notes. Write the audit entry in the same transaction as the change, so a successful change always has a record. Make the audit table append-only — no updates, no deletes, and not writable by the account your application uses for ordinary work. And keep it separate from the data it describes, so a deletion cannot remove its own evidence.

## Log the Security Events, Not Only the Business Ones

A separate category, and the one that turns a suspicion into a timeline.

Successful logins, with time and origin. Failed logins, which reveal a password-guessing attempt long before it succeeds. Password changes and resets. Email address changes, which are how an account gets stolen quietly. Permission and role changes. Invitations and access grants. Bulk operations, especially exports — the most under-logged and most sensitive action in most products.

Record these even when nothing appears wrong. Their entire value is retrospective.

## What Must Never Appear in a Log

The failure mode where logging itself becomes the breach.

Never log passwords, in any form, including failed attempts — people type their password into the username field and a log capturing both has just stored a credential in plain text. Never log session tokens, API keys or authentication headers. Never log full payment card details. Never log request bodies wholesale on endpoints handling personal data, which is the lazy default that quietly copies your most sensitive records into a third-party service with a different retention policy and different access controls.

Log identifiers, not contents. `Updated patient record 4,182, field "notes"` tells you what you need. Logging the note's text does not, and it makes your logging system a second copy of the data you are trying to protect.

## Retention, and the Fact That Logs Are Personal Data

Logs containing identifiers and addresses are personal data, which has three consequences.

They need a defined retention period rather than growing forever. A common shape is short retention for high-volume application logs, longer for security events, and longest for the audit trail — where a legal or contractual obligation may set the floor.

They need access control. A log everyone on the team can read is a route around every permission you wrote.

And they need to be mentioned when you describe your data handling. A business customer asking what you store and for how long is asking about logs too, whether or not they say so. Specific obligations depend on your data and situation, so verify current requirements rather than relying on a summary.

## The Practical Minimum

If you build only one thing, build the audit trail on the tables that matter — and add an error tracker, which takes twenty minutes and is the highest-return configuration change available to a small product.

If you build a second thing, log security events.

If you build a third, add alerts: a notification when errors spike, when a scheduled job does not run, when failed logins cluster on one account. Records tell you what happened; alerts tell you it is happening.

## Why This Is Missing From Generated Applications

Worth understanding, because it explains why the gap is so consistent.

Nobody prompts for it. A request produces a feature; logging is not part of the feature working, so it is not part of what gets built. Generated code frequently swallows errors — a catch block that silently continues, which makes the application appear robust while destroying the evidence. And an agent asked to fix a noisy error will sometimes remove the logging rather than the cause.

The remedy is to ask explicitly, in the same way you would ask for access rules: state that changes to these tables must be recorded, that errors must be reported rather than suppressed, and that nothing sensitive may appear in a log.

## Reading What You Have Collected

Collecting is half of it. Once a week, spend ten minutes: look at the top errors by frequency, check that scheduled jobs ran, and glance at failed logins for clusters.

Almost every founder who starts this finds something in the first session — usually a feature that has been failing for a subset of users for weeks, silently, with nobody reporting it because people assume a broken thing is their own fault.

## When the History Becomes a Feature

Something unexpected happens once an audit trail exists: customers want to see it.

**Show the change history in the product.** "Changed by Anouk, Tuesday 14:32, from 3 to 5" beside a record answers the question at the moment it is asked, without anyone contacting you. In products where several colleagues share data — rosters, stock, quotations, patient records — this consistently becomes one of the features customers mention most, because it ends the category of argument that begins with "I never touched it".

**Decide who may see it.** History is not automatically public within an organisation. A manager seeing who changed a shift is reasonable; every colleague seeing who viewed a personnel record may not be. Apply the same access rules to the history that apply to the data, and remember that the history of a deleted record still describes a real person.

**Make it exportable for disputes.** A customer in a disagreement with their own client, an employer in a discussion with a works council, an inspection body asking for evidence — each wants a defensible extract with timestamps and actors. An export that produces exactly that turns your logging from an internal cost into something customers value.

**Distinguish history from evidence.** A change log your own account can edit is a feature. A record nobody can alter, including you, is evidence. If your customers operate under professional obligations — inspection, care, finance, certification — the second is what they need, and it means the audit table must be append-only and outside your application's ordinary write permissions.

There is a commercial argument here as well as a security one. Among the products that reach a procurement conversation, the ones with an intact, attributable history reliably do better, because it is the shortest possible answer to "how would we know if something went wrong". Building it for your own incident response and discovering it sells the product is the most pleasant kind of surprise available in this work.

## Putting the Records in Place

For an existing application this is a few days rather than a project: an error tracker configured with alerts, security events logged, audit trails added to the tables holding money, permissions and personal data, written append-only in the same transaction as the change, sensitive values excluded by design, retention periods set per category with access restricted, and a short weekly review routine handed over.

LaunchStudio does this as part of production readiness, because it is what makes every later incident answerable. The engineers are Manifera's: eleven years of running production systems for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City.

[Tell us what your product records today](https://launchstudio.eu/en/#contact) and you will get an honest answer about what you could reconstruct, usually within one business day, or see the [packages](https://launchstudio.eu/en/#packages).

## Real example

### Nine Weeks of Changed Shifts and No Way to Say Who

Lotte Wijnands built Dienstrooster with Lovable: shift scheduling used by three residential care organisations around Assen, covering about 280 care workers across eleven locations.

A complaint arrived from a team leader: shifts were being changed without notice, staff were arriving for shifts that no longer existed, and one weekend a location had been left with one qualified person instead of three. The organisation wanted to know who had made the changes.

There was no answer available. The application stored the current state of the roster and nothing else. No history, no record of who changed what, no login log. The only evidence was in people's memories and a WhatsApp group.

It had been happening for at least nine weeks.

Seven business days of work: an append-only audit table added, capturing actor, timestamp, origin, and before and after values for every roster change, written in the same transaction as the change and not writable by the application's ordinary account; security events logged, including logins, failed logins, role changes and bulk operations; an error tracker configured, which immediately revealed a shift-notification job that had been failing for six weeks and explained a large part of the "no notice" complaint; alerts added for error spikes and for the notification job not running; retention set per category with access to the audit trail restricted to organisation administrators; a change history shown in the interface so a team leader can see who altered a shift without asking anyone; and a written note of what is logged and for how long, for the organisations' own records.

The original nine weeks could not be reconstructed. That was stated plainly to the three organisations rather than estimated.

**Result:** two subsequent disputes were resolved in minutes from the history, the broken notification job explained most of the original complaint, and the change history became the feature team leaders mention most often.

> *"They asked who changed the roster and the honest answer was that my application had no idea. Not that it was hard to find out — it had never recorded it."*
> — **Lotte Wijnands, Founder, Dienstrooster (Assen)**

**Cost & Timeline:** €3,600 (audit trail, security event logging, error tracking with alerts, retention policy, change history in the interface) — completed in 7 business days.

## Frequently Asked Questions

### What is the difference between logs and an audit trail?

Application logs record what the system did and are short-lived; an audit trail records what people did to data — who changed what, from what, to what, when. Only the second answers the questions an incident actually asks.

### What should an audit entry contain?

Actor, timestamp, the values before and after, and the origin of the request. Write it in the same transaction as the change, keep the table append-only, and do not let your application's ordinary account modify it.

### What must never go into a log?

Passwords in any form including failed attempts, session tokens, API keys, full card details, and whole request bodies on endpoints handling personal data. Log identifiers and field names rather than contents.

### How long should I keep logs?

Set a period per category — short for high-volume application logs, longer for security events, longest for the audit trail where an obligation may apply. Logs with identifiers are personal data, so they need retention limits and access control.

### Why do AI-built apps have no logging?

Because nobody prompts for it and it contributes nothing to a feature working. Generated code also tends to swallow errors silently, which makes the application look robust while removing the evidence. Ask for it explicitly, as you would for access rules.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the difference between logs and an audit trail?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Application logs record what the system did; an audit trail records what people did to data — actor, time, before and after. Only the latter answers incident questions."
      }
    },
    {
      "@type": "Question",
      "name": "What should an audit entry contain?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Actor, timestamp, before and after values, and request origin — written in the same transaction, in an append-only table the app cannot modify."
      }
    },
    {
      "@type": "Question",
      "name": "What must never go into a log?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Passwords including failed attempts, session tokens, API keys, full card details, and whole request bodies on personal-data endpoints. Log identifiers, not contents."
      }
    },
    {
      "@type": "Question",
      "name": "How long should I keep logs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Set retention per category — short for application logs, longer for security events, longest for audit trails — with access control, since logs with identifiers are personal data."
      }
    },
    {
      "@type": "Question",
      "name": "Why do AI-built apps have no logging?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nobody prompts for it and it does not make a feature work. Generated code also swallows errors silently, destroying evidence. Ask for it explicitly."
      }
    }
  ]
}
</script>
