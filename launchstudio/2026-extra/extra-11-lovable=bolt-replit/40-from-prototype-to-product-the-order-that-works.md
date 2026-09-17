---
Title: "Lovable, Bolt, Cursor and Replit: Prototype to Production, in Order"
Keywords: Lovable, Bolt, Cursor, Replit, vibe coding developer, prototype to production sequence, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable, Bolt, Cursor and Replit: Prototype to Production, in Order

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable, Bolt, Cursor and Replit: Prototype to Production, in Order",
  "description": "A sequenced plan for taking an AI-built prototype to production: what to fix first, what can wait, what never needed doing, and how to tell which stage your product is actually in.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-12",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/from-prototype-to-product-the-order-that-works" }
}
</script>

The hardest part of launching something built with AI tools is not any individual piece of work. It is that everything appears equally urgent at once — security, payments, hosting, email, performance, search engines, mobile, backups — and a founder with a working prototype and no engineering background has no basis for choosing what to do first.

So they do the visible things: polish the interface, add a feature, set up analytics. Those are pleasant and none of them are the reason the product cannot take a customer.

What follows is the order that works, derived from what actually blocks launches rather than from what feels productive.

## Stage Zero: Establish Where You Are

Before sequencing anything, answer three questions honestly.

**Can anyone other than you use it today?** If not, you are still building the product, and production work is premature. Finish the thing people would pay for first.

**Is anyone's money or personal data involved?** This determines whether the security work is urgent or merely important.

**Do you have a date, and who set it?** A self-imposed date can move. A customer's cannot, and that changes what you defer.

Most founders who feel overwhelmed are between stages: a product that works, a date approaching, and no map. The map is below.

## Stage One: Make It Safe to Have Customers

Nothing else matters until this is true, because every other problem is recoverable and this one is not.

**Access control.** Two accounts, each unable to reach the other's data, verified by trying. In multi-tenant products, the same between organisations. This is the single most common serious flaw in AI-built applications and the one that ends deals.

**Credentials.** Nothing privileged in the frontend bundle or the repository history, secrets in proper storage, spending caps on anything metered.

**The obvious input problems.** Server-side validation on the rules that matter commercially, uploads restricted by type and size, error messages that reveal nothing useful.

If you do only one stage before launching, do this one.

## Stage Two: Make the Money Work

If you charge, this is next, because a product that cannot reliably take payment is not a business regardless of how good it is.

Webhooks handled, verified and idempotent. Entitlement derived from payment state rather than a single flag set at checkout. Failed payments, refunds and cancellations handled. One real transaction completed and deliberately abandoned to prove the webhook path. Invoices that a Dutch accountant will accept.

## Stage Three: Make It Reachable and Reliable

Now the infrastructure around the product.

Your own domain with a valid certificate and one canonical address. Email that arrives, with authentication records published and delivery tested to real inboxes. Hosting with a deployment pipeline, a staging environment and a rollback you have used once. Backups that have been restored into a scratch environment and timed. Monitoring that alerts a human, plus error tracking you can read on a phone.

This stage is what turns a live prototype into something you can operate.

## Stage Four: Make It Survive Contact With Users

The work that matters once real people arrive in numbers.

Rate limiting on signup, login, password reset, contact forms and anything metered. Concurrency handled where two simultaneous actions would produce a wrong answer. The performance basics: indexes on the columns you filter by, repeated queries collapsed, images processed at upload. Sessions that expire and invalidate properly.

## Stage Five: Make It Defensible

Before or shortly after your first business customer.

Where data is stored, stated. Retention and deletion implemented rather than promised. A sub-processor list and the agreements behind it. Access logging on sensitive records. A privacy statement describing what the app actually does. A support capability that does not involve querying the production database by hand.

## Stage Six: Make It Findable and Usable

Last, deliberately.

Public pages rendered so search engines can read them, with per-page titles, a sitemap and canonical addresses. Mobile behaviour fixed properly. Search that finds what people type. A second language if your market needs one. Onboarding that explains itself.

Founders instinctively start here because it is the visible half. It is genuinely important and it is worthless if stage one is missing, because traffic arriving at an insecure product is a faster route to a bad outcome than no traffic at all.

## What Never Needed Doing

Some things founders worry about rarely matter at this size: a microservice architecture, a container orchestration platform, a comprehensive test suite chasing coverage, a custom design system, a native mobile app, multi-region deployment, or a full administrative interface built before anyone has asked for the features in it.

Each of these appears in advice written for companies with engineering teams. For a product with a founder and a few hundred users, they are cost without return.

## How Long the Whole Thing Takes

For a typical AI-built product with a working prototype, stages one to three are one to three weeks of focused engineering. Stages four and five add a week or two depending on how much data you handle. Stage six is continuous rather than a phase.

That is the shape behind LaunchStudio's fixed-price range of €800 to €7,500: the variable is how many stages your product needs and how much data it holds, not how many features it has, because the frontend is kept rather than rebuilt.

## The One Thing to Take Away

If you remember nothing else from this cluster of articles: **create two accounts in your own product right now, log in as one, and try to read the other's data by changing a number in the address bar.**

If it works, stop reading, stop building features, and fix that. It takes four minutes to test, it is the most common serious flaw in AI-generated applications, and it is the difference between a product that can have customers and one that merely looks like it can.

## Where to Get Help With the Sequence

LaunchStudio exists for exactly this gap: prototypes built in Lovable, Bolt, Cursor or Replit that work and cannot yet be launched. The frontend you built is kept — untouched — and the stages above are built underneath it, in the order above, with the code left documented and AI-readable so you can keep iterating in your own tool afterwards, and owned by you throughout.

Behind it is Manifera, a software company with eleven years of production engineering for clients including Vodafone, TNO and CFLW, from offices in Amsterdam, Singapore and Ho Chi Minh City. LaunchStudio is that capability at founder scale: fixed price, fixed scope, one to three weeks rather than one to three quarters.

[Describe your product](https://launchstudio.eu/en/#contact) and you will get a concrete assessment of which stages you need within one business day, or read what the [packages](https://launchstudio.eu/en/#packages) include first.

## What Changes After the First Hundred Customers

The stages above take a prototype to a product. A product with real usage develops a different set of needs, and it is worth knowing what is coming so you neither build it early nor are surprised by it.

**Operational rhythm replaces heroics.** At ten customers you can fix anything personally. At a hundred you need the weekly checks — jobs ran, queues are clear, reconciliation matches, errors are not recurring — because the failures you now have are slow rather than dramatic.

**Support becomes a product input.** Message volume tells you what the product explains badly, and the fix is usually in the interface rather than in a faster reply.

**Data grows past its design.** Queries written against forty rows meet forty thousand, retention becomes a real question, and the storage bill starts reflecting decisions made a year earlier.

**Someone else touches the code.** Which turns conventions, access separation and handover documentation from good practice into daily necessities.

**Customers start asking questions about you,** not just about the product: where data lives, who can see it, what happens if you stop. Stage five stops being preparation and becomes part of selling.

None of this requires anticipating it now. It requires only that the foundations from stages one to three exist, because every item above is far cheaper on a product that is already safe, observable and recoverable.

## If You Are Doing This Yourself

Plenty of technical founders work through these stages alone, and the sequence holds. Three adjustments make it survivable.

**Do one stage at a time, completely.** The failure pattern for self-directed production work is starting five things and finishing none, leaving a product that is partly hardened everywhere and safe nowhere.

**Verify each fix the way an adversary would.** Fixing an access rule and moving on is not the same as fixing it and then trying to break it again. The attempt is the evidence, and it takes minutes.

**Get one external opinion at the end of stage one.** Access control is the area where your own testing is least reliable, because you test the paths you built. A second pair of eyes on that stage specifically is worth more than a full review of everything else.

And keep a written list of what you decided not to do. Deferred work that exists only in memory becomes work that was never considered, which is what founders discover during a customer's security questionnaire a year later.

## Real example

### A Founder Who Did the Stages in Reverse, Then Did Them Again

Bo Klaassen built Groeiplan in Lovable: a goal-tracking tool for small business coaches, used by around ninety coaches with their own clients across Utrecht and Amersfoort. She spent three months before launch on the visible half — a redesigned interface, analytics, a content strategy, a mobile-friendly layout and a second language.

Launch went well for six weeks. Then a coach reported that she could see another coach's client notes by editing the address bar, which had been true since the first day and had simply gone unnoticed while user numbers were small.

The remediation was stage one and two, done in nine business days under considerable pressure: access rules written and tested across every table, a privileged key removed from the frontend bundle and rotated, payment webhooks implemented so abandoned checkouts stopped losing access, and a support lookup built so Bo stopped querying the database to answer questions.

The work she had done first was not wasted. It was simply done in an order that left the product exposed for six weeks with real client data in it.

**Result:** no evidence of misuse was found, the affected coaches were informed with a clear written account, and Groeiplan has since passed two client security questionnaires — with the stage-five documentation produced afterwards rather than in a panic.

> *"I built the shop window beautifully and left the back door open for six weeks. Everything I did was worth doing. I just did it in exactly the wrong order."*
> — **Bo Klaassen, Founder, Groeiplan (Utrecht)**

**Cost & Timeline:** €4,600 (access control remediation, credential rotation, payment webhooks, support tooling, documentation) — completed in 9 business days.

## Frequently Asked Questions

### What should I fix first in an AI-built prototype?

Access control: whether one customer can reach another's data. Test it by creating two accounts and trying. Everything else — payments, hosting, search visibility — is recoverable, and this one is not.

### Can I launch before doing all of this?

Frequently yes, with a reduced audience. Launch to a handful of customers you can contact directly, keep the unverified paths manual, and complete the remaining stages on a dated plan rather than an intention.

### Why is search engine visibility last?

Because it multiplies whatever you already have. Traffic arriving at a product that leaks data or cannot take payment reliably produces a worse outcome than no traffic, and the work itself is unaffected by doing it a month later.

### How long does the whole sequence take?

For a typical prototype, one to three weeks of focused engineering for the first three stages, plus a week or two for the next two depending on how much data you handle. The frontend is kept, which is what keeps the scope bounded.

### Will I still be able to edit my app in Lovable afterwards?

You should be, and it is worth stating as a requirement of any engagement. The codebase should be left conventional, documented and AI-readable, and you should verify it by making one small change yourself before the work is signed off.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What should I fix first in an AI-built prototype?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Access control — whether one customer can reach another's data. Test with two accounts; everything else is recoverable and this is not."
      }
    },
    {
      "@type": "Question",
      "name": "Can I launch before doing all of this?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Often yes with a reduced audience: a handful of contactable customers, unverified paths handled manually, and the rest on a dated plan."
      }
    },
    {
      "@type": "Question",
      "name": "Why is search engine visibility last?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because it multiplies what you already have. Traffic arriving at an insecure or unreliable product is worse than no traffic."
      }
    },
    {
      "@type": "Question",
      "name": "How long does the whole sequence take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "One to three weeks for the first three stages, plus a week or two for the next two depending on data volume, because the frontend is kept rather than rebuilt."
      }
    },
    {
      "@type": "Question",
      "name": "Will I still be able to edit my app in Lovable afterwards?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You should be — require a conventional, documented, AI-readable codebase and verify it with a small change before sign-off."
      }
    }
  ]
}
</script>
