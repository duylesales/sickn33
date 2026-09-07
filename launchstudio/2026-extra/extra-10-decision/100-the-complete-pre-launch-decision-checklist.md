---
Title: "The Complete Pre-Launch Decision Checklist"
Keywords: pre launch checklist ai built product, production readiness checklist saas, what to fix before launch, prototype to production decisions, founder launch checklist, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# The Complete Pre-Launch Decision Checklist

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Complete Pre-Launch Decision Checklist",
  "description": "The decisions that determine whether an AI-generated prototype survives contact with real customers, gathered into one sequence: what must be settled before launch, what can wait, and how to tell which is which for your particular product.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-02",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/the-complete-pre-launch-decision-checklist" }
}
</script>

The hardest thing about taking an AI-generated product to production is not any individual technical problem. It is that the problems are invisible from where the founder is standing: the product works, the demo goes well, and the failures are all in paths nobody has walked — an empty account, a large customer, a second user, a declined card, a document in the wrong encoding, a Sunday when the certificate expires.

This is the last article in a hundred, and it exists to be the thing you actually work through. It is organised by consequence rather than by topic: what has to be settled before anyone pays you, what should be settled before the first serious customer, and what can wait until demand proves it necessary.

## The Test That Sorts Everything Else

Before the list, the question that resolves most disagreements about priority: **if this is wrong, does it cost an apology, money, or a customer's trust?**

An apology means it can wait. A confusing empty state, a missing digest email, an integration nobody has asked for twice — real problems, and none of them irreversible.

Money means it needs a limit before launch. Anything metered, anything reachable without authentication, anything a script could call in a loop.

Trust means it needs to be right on day one, because it is not recoverable. One customer seeing another's data. A payment taken and no record kept. Work that disappears. A wrong number on an invoice. These are the ones where the customer does not complain — they leave, and tell someone.

That ordering matters because pre-launch time is finite and the temptation is to spend it on what is visible. Almost everything in the first list below falls into the third category.

## Before Anyone Pays You

**Access control enforced on the server.** Every rule that decides who can see what must hold at the database or endpoint level, not in the interface. Test it with two accounts and confirm that neither can reach the other's data by changing an identifier. This is the single most common serious defect in AI-generated products, and it is the one with no recovery.

**The empty account works.** Sign up with a genuinely new address, in a private window, and look at what a first customer sees. Then do the same on a phone. Fix anything that reads as broken rather than empty.

**The first save actually saves.** Complete the core action as a new customer and verify the record exists in the database. A success message over a silently failed write is the worst possible first impression.

**Payments are correct end to end.** Amounts stored as integers, one rounding rule applied everywhere, a real card charged and refunded in test mode, a declined card handled with a retry and a notification, and trial expiry exercised deliberately rather than assumed.

**Backups exist and have been restored once.** Not configured — restored, into a separate environment, with the timing written down and file storage included.

**Cancellation is self-service**, with data retained for a stated period and deletion as a separate action that reaches storage, indexes, and connected tools.

**Cost has a ceiling.** Per-account and global daily limits on anything metered, enforced in your own code, with nothing expensive reachable without a verified account.

**Monitoring tells you before customers do.** A synthetic check that logs in and loads real data, error tracking with the account attached, and a heartbeat on every scheduled job.

**Secrets are out of the repository and off the frontend**, with expiry dates recorded for certificates, domains, and provider credentials.

**Email arrives.** Authentication records configured, transactional and marketing streams separated, and a test to Gmail, Outlook, and a corporate address confirming inbox rather than spam.

## Before Your First Serious Customer

These are the decisions that decide whether the account you most want becomes a reference or a warning.

**Volume.** Create an account with far more data than your largest real customer and use the product. Paginate every list, index what you filter and sort by, and remove the query-in-a-loop patterns. Slowness is always specific to an account before it is general.

**A second person logging in.** Even if you have no team features, create an organisation per customer and attach data and billing to it. Retrofitting this is a rewrite; doing it now is invisible.

**Import that does not lose anything.** Validate the whole file before writing, handle European encodings and separators, show a preview, state what happens to duplicates, and never leave a half-populated account.

**Export that is complete.** Including attachments, in machine-readable formats, delivered by an expiring authenticated link — and tested by importing it into a fresh account.

**An audit trail with before-and-after values**, append-only, on anything involving money, permissions, or deletion.

**Dates and timezones.** Store moments in UTC, keep calendar dates as dates, compute reporting boundaries in the customer's timezone, and test around month ends and midnight.

**Bulk actions that state their scope**, prefer soft deletion, run in the background, and report partial failures honestly.

**A written answer to the security questionnaire.** Where data is processed, who your subprocessors are, whether there is an audit trail, whether AI features can be switched off. Having this written turns a multi-day exchange into a link.

## Before You Have the Problem It Prevents

Judgement calls, each worth doing when a specific trigger appears rather than on a schedule.

**A minimal admin panel** — find a customer, extend a trial, reset access, change a plan, resend an email, view account state — when you find yourself writing database queries to answer support requests.

**A staging environment with anonymised data** when you are about to make a change you cannot easily reverse.

**Feature flags** before the first change large enough that you would want a way to switch it off without deploying.

**Webhooks, an API, or a platform connector** when integration requests are diverse rather than concentrated — and only after the endpoints they depend on are consistent.

**Notification preferences with scoped unsubscribes** before your product sends enough that someone reaches for the unsubscribe link and silences their billing emails with it.

**Two-way sync** only when both systems are genuinely edited by different people. Most requests for it are satisfied by one-way sync and a link back.

**Retention and deletion jobs** once you hold data from customers who have left.

## If Your Product Has AI Features

The additional decisions, none of which are optional once a feature reaches customers.

Estimate the cost per use for the heaviest plausible customer before building. Pin the model version rather than using an alias. Validate every output against a schema and against your own data, and design the failure state so a customer sees an honest message rather than a plausible fabrication. Keep the model's access bounded by the permissions of the person it is acting for, prefer read-only, and require confirmation for anything consequential. Record provenance — model, prompt version, timestamp, source — with every generated result, and label generated content where the customer sees it. Send the minimum data to the provider, on a tier with a data processing agreement, with a switch to disable AI processing per account. And keep thirty real examples as a test set, so that changing a prompt is a measurement rather than a guess.

## What This Costs, and the Honest Alternative

Working through the first list takes an experienced engineer somewhere between one and three weeks for a typical AI-generated product, depending on how much of it exists already. The second list is comparable. Neither produces a feature, which is exactly why it is postponed, and why the products that skip it fail in the same small number of ways.

The alternative — doing it yourself, over months, learning each item at the moment it goes wrong — is legitimate and it is a real trade. It costs time rather than money, it costs some customers, and it works for founders whose market is forgiving and whose data is not sensitive.

Where it does not work is when the first serious customer arrives before the learning does, because that customer is not a test. They are the reference that determines whether the next five buy.

LaunchStudio exists for the founders who would rather not find out which items on this list they got wrong. Backed by Manifera's 11+ years of production engineering, it takes an AI-generated prototype through exactly these decisions at a fixed price agreed before anyone touches your code, with your frontend left as you built it. If you have a product that works and you are not certain what it does on the paths nobody has walked, [describe your project](https://launchstudio.eu/en/#contact) and you will have an assessment within one business day.

## Real example

### The List That Took Nine Days

Bram Kooij had built Wachtrij, a queue-management tool for municipal service desks, in Lovable. It worked, three municipalities had piloted it, and a fourth — considerably larger — had asked for a security assessment before signing.

The review worked through the first two lists. Access rules were enforced only in the interface: any authenticated user could retrieve any municipality's visitor records by changing an identifier. Backups covered the database but not the uploaded identity documents. There was no audit trail, which the assessment required. Reporting boundaries were computed in UTC, so daily visitor counts were wrong by the visitors between 23:00 and midnight. And a single unindexed query made the largest pilot's dashboard take nineteen seconds.

None of it had produced a complaint, because no pilot had been large enough or curious enough to find any of it.

**Result:** nine business days of work covering access control at the database level, backup scope, an append-only audit trail, timezone-correct reporting, indexes and pagination, self-service export, and a written data-flow document. The assessment passed at the second submission and the contract signed six weeks later, at roughly nine times the value of the three pilots combined.

> "Nothing on that list was something a customer had complained about. Every single item was something that would have ended the contract if the assessment had found it and I had not."
> — **Bram Kooij, Founder, Wachtrij**

**Cost & Timeline:** production-readiness engagement completed in 9 business days, fixed price agreed in advance.

## Frequently Asked Questions

### What is the single most important item to check before launch?

Access control enforced on the server rather than in the interface. Test whether one account can reach another's data by changing an identifier. It is the most common serious defect in AI-generated products and the one from which there is no recovery.

### How do I decide what to fix before launch and what can wait?

Ask whether being wrong costs an apology, money, or trust. Apologies can wait, anything costing money needs a limit before launch, and anything costing trust — data exposure, lost work, wrong charges — has to be right on day one.

### How long does production readiness take for a typical AI-built prototype?

Between one and three weeks of experienced engineering for the essential items, depending on how much already exists. The work produces no new features, which is why it is postponed and why the same failures recur.

### Can I do this myself over time instead?

Yes, and it is a real trade: time and some customers instead of money. It works when your market is forgiving and your data is not sensitive. It fails when a serious customer arrives before the learning does.

### What changes if my product includes AI features?

Cost estimation and hard limits, pinned model versions, output validation with an honest failure state, model access bounded by the user's own permissions, provenance recorded with every result, minimised data sent to the provider under a proper agreement, and a small test set so prompt changes are measured rather than guessed.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "What is the single most important item to check before launch?", "acceptedAnswer": { "@type": "Answer", "text": "Access control enforced on the server rather than in the interface. Test whether one account can reach another's data by changing an identifier; it is the most common serious defect and has no recovery." } },
    { "@type": "Question", "name": "How do I decide what to fix before launch and what can wait?", "acceptedAnswer": { "@type": "Answer", "text": "Ask whether being wrong costs an apology, money, or trust. Apologies can wait, money needs a limit before launch, and trust must be right on day one." } },
    { "@type": "Question", "name": "How long does production readiness take for a typical AI-built prototype?", "acceptedAnswer": { "@type": "Answer", "text": "One to three weeks of experienced engineering for the essential items, depending on what exists. It produces no new features, which is why it is postponed." } },
    { "@type": "Question", "name": "Can I do this myself over time instead?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, trading time and some customers for money. It works when the market is forgiving and the data is not sensitive, and fails when a serious customer arrives before the learning does." } },
    { "@type": "Question", "name": "What changes if my product includes AI features?", "acceptedAnswer": { "@type": "Answer", "text": "Cost estimation and hard limits, pinned model versions, output validation with an honest failure state, access bounded by the user's permissions, recorded provenance, minimised data sent under a proper agreement, and a test set for prompt changes." } }
  ]
}
</script>
