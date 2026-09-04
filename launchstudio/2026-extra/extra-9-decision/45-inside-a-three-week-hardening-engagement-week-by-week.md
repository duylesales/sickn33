---
Title: "Inside a Three-Week Hardening Engagement, Week by Week"
Keywords: hardening engagement timeline, MVP to production three weeks, software project week by week, production readiness sprint, SaaS launch plan, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# Inside a Three-Week Hardening Engagement, Week by Week

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Inside a Three-Week Hardening Engagement, Week by Week",
  "description": "Founders committing to a fixed-price hardening engagement rarely know what the three weeks actually contain until they are inside them. This is a day-by-day account of how the time is spent, where scope gets renegotiated, and what causes three weeks to become four.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2027-01-14",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/inside-a-three-week-hardening-engagement-week-by-week"
  }
}
</script>

It is a Tuesday in February and a founder in Amsterdam has just signed a fixed-price quote for three weeks of hardening work on a SaaS product that already has forty paying customers and a growing sense of unease. She knows what she is buying in outcome terms — security, proper payments, an environment that will not fall over at 300 users. What she does not know is what the next fifteen working days will actually look like, when she will hear from anyone, when she is meant to do something, and at what point it will start to feel like it is working.

That gap is worth closing, because a founder who understands the shape of the engagement makes better decisions inside it — particularly at the midpoint, where the most consequential conversation happens and where an uninformed founder tends to say "whatever you think." Here is the real shape.

## Day Zero: Scoping, and the Quote That Fixes the Shape

Before day one there is a scoping conversation, typically thirty to forty-five minutes, and one to two hours of asynchronous investigation on the engineering side. The output is a fixed price and a scoped list — and for a scale-up product it is worth insisting the list is ordered by risk, not by convenience.

What gets examined at this stage: the shape of your database schema, how authentication is wired, whether payment flows are real or simulated, where secrets currently live, what your hosting setup is, and how much real customer data is in play. On a product with existing paying customers, that last question dominates everything downstream — it means migrations must be reversible, staging must use scrubbed data, and there will be a cutover rather than a launch.

Two things you should get in writing at day zero and can reasonably insist on: an ordered scope list where the top items are the ones that would hurt you most if they broke, and an explicit statement of what is *out* of scope. On a three-week engagement in the €2,500–€7,500 band, the out-of-scope list is as informative as the in-scope one.

## Week One, Days 1–2: Reading Before Writing

The first two days produce very little visible output, and this is the single most misread part of the engagement. An engineer spends them reading: your schema and its relationships, every route into your data, what your AI tooling generated automatically versus what was hand-written, and where the assumptions in your prototype diverge from the assumptions your growing customer base has started to rely on.

They will typically run automated passes too — dependency and vulnerability scanning, a secrets scan across git history, and a review of what is exposed to the client versus enforced on the server. On AI-generated codebases these consistently surface the same categories: keys in the frontend, missing or incomplete row-level security, endpoints trusting client-supplied identifiers, and webhooks accepting unsigned requests.

By end of day two you should receive a findings note: what exists, what is missing, what is worse than expected and what is better. This is when the honest picture arrives, and it is normal for it to contain at least one thing nobody scoped. Roughly 45% of AI-generated code carries security vulnerabilities as written, so the interesting question is never whether something turns up, but whether it changes the plan.

## Week One, Days 3–5: The Foundation Layer

Days three to five go into the layer everything else sits on, in a deliberate order.

Environments come first: a staging project separate from production, with its own database seeded from a scrubbed copy of real data, and a deployment pipeline — usually GitHub Actions into Vercel or your existing host — so that shipping stops being a manual act performed by whoever remembers the command. Without this, everything later in the engagement is verified in the wrong place.

Then authentication and authorisation, which are separate problems and get treated separately. Authentication is who you are; authorisation is what you may touch. In products built with AI tooling, authentication is usually present and adequate, and authorisation is usually the hole. This is where row-level security policies get written table by table, where endpoints stop trusting an account ID sent by the browser, and where the multi-tenant boundary gets enforced in the database rather than hoped for in the interface.

Then secrets: keys moved out of client-side code and into server environment variables, anything with exposure history rotated, and a single source of truth established for configuration. By Friday of week one you should have a staging URL, a deployment pipeline, and a first pass of access rules — and you should personally test the "can Customer A reach Customer B's data" case before the weekend.

## Week Two: The Parts That Touch Money

Week two is usually payments, email, and the integrations that carry real-world consequences when they go wrong.

Payments are more work than founders expect, because a payment integration is not a checkout button. It is: a checkout or subscription flow; webhook handling with signature verification; idempotency so a retried webhook does not double-charge or double-provision; a subscription state machine covering trial, active, past due, cancelled, and reactivated; a customer portal or cancellation path; VAT handling, which for EU B2C sales means charging the customer's local rate; and failed-payment retry logic. On Stripe, subscription lifecycle testing uses test clocks so a full year of renewals and failures can be simulated in an afternoon rather than waited out. On Mollie — often the right choice if your customers are Dutch and expect iDEAL — the equivalent testing is done against their test mode with the mandate and recurring-payment flows exercised explicitly.

Email comes next because it is time-sensitive rather than difficult. The sending domain gets configured with SPF, DKIM, and DMARC, ideally on a subdomain, and then it needs days rather than hours to settle before launch. Transactional templates — confirmation, password reset, receipt, failed payment — get wired to real events, and each is tested to a real inbox at Gmail, Outlook, and at least one corporate domain, since deliverability differs sharply between them.

Somewhere in week two the database work also lands: indexes on the columns your product actually filters by, connection pooling if you are on Supabase and heading past a few hundred concurrent users, and a backup and restore process where the restore has actually been performed once rather than assumed.

## The Midpoint Review: Where Scope Gets Renegotiated Honestly

Around day seven or eight there is a conversation that determines how the engagement ends. By then everything unknown is known, and the question is whether the original list still fits the remaining time.

Three outcomes are normal. The plan holds and week three proceeds as scoped. Something significant was found — a data model that cannot support the multi-tenant boundary without a migration, say — and something else gets dropped or deferred to make room. Or the work turned out cleaner than expected and there is room to pull something forward from the "after launch" list.

Your job in this conversation is to make the trade-off decision rather than delegate it, because it is a business decision wearing technical clothing. "Do we spend two days on the migration or two days on the admin dashboard" is not an engineering question; it depends on whether your next ten customers are enterprise buyers who will ask about data isolation. Unlike freelancers, LaunchStudio is backed by Manifera — trusted by Vodafone, TNO, and CFLW — and the habit that carries over from that kind of client is putting the trade-off in front of the person who owns the consequences, in writing, at the midpoint rather than in a summary at the end.

## Week Three, Days 11–13: Monitoring and the Dress Rehearsal

Week three shifts from building to proving. Monitoring goes in: error tracking with something like Sentry so failures reach a channel rather than a user's imagination, uptime checks against a real endpoint rather than the homepage, and alerting rules with thresholds set deliberately — a page for "payments failing," an email digest for "error rate slightly elevated." Alerting that fires on everything gets muted within a week, which is worse than no alerting.

Then the dress rehearsal: a full pass through the acceptance checklist on staging, including every failure case. Declined cards. Duplicate signups. Expired password reset links. A user who cancels mid-period. A webhook that arrives twice. For a scale-up with existing customers, this is also where the cutover plan gets written — what happens to sessions in flight, whether there is downtime, what the rollback path is, and who runs it.

Load behaviour gets a look here too. Not a formal load test in most cases, but a smoke test with a tool like k6 at a few multiples of your current peak, enough to find the obvious cliff: an unindexed query, a connection pool ceiling, a third-party rate limit. Finding it here costs an afternoon; finding it during a launch spike costs customers.

## Week Three, Days 14–15: Cutover and Handover

The final two days are cutover and handover, and they are separate things.

Cutover on a product with live customers is a scheduled, reversible operation: DNS TTLs lowered a day or two in advance so changes propagate quickly, a maintenance window chosen for your lowest-traffic hour, the migration run with a tested rollback, and someone watching error rates and payment success for the following few hours rather than closing the laptop.

Handover is the document. It should contain what changed and why, in plain language; where everything now lives and which accounts hold it; what was deliberately not done and what it would cost later; how to run, deploy, and roll back; what the monitoring alerts mean when they fire; and the credential rotation list for closing out access. On any engagement worth its price the code stays yours throughout, in your repositories and on your accounts, and the handover is what makes that ownership practically usable rather than nominally true.

The support window starts the moment cutover completes. Use it deliberately — it is a resource with an expiry date, not an insurance policy.

## What Turns Three Weeks Into Four

Four causes account for most overruns, and three of them sit on the founder's side.

Access delays in week one, which push everything and never fully recover. Payment provider verification started too late, where Stripe or Mollie identity checks run for several business days and block live-mode testing entirely. Slow decisions at the midpoint, where a two-day trade-off question waits four days for an answer. And genuine discovery — a data model problem that cannot be worked around — which is the only one that is nobody's fault and the one a well-run midpoint review exists to surface early.

Knowing the shape of the three weeks is what lets you be useful inside them: fast on access, present at the midpoint, rigorous on the checklist, and available at cutover. That is perhaps six hours of your time across fifteen working days, spent at the four moments where it changes the outcome. If you want the version of this mapped to your own product before you commit, the [package structure and what each covers](https://launchstudio.eu/en/#packages) is public, and the delivery method behind it comes from [Manifera's web application practice](https://www.manifera.com/services/web-app-develop/).

Ask for the week-by-week plan attached to your fixed-price quote — if a partner cannot tell you what days three and eleven look like, that is the more useful signal.

## Real example

### A Scale-Up in Action: The Migration That Was Found on Day Eight

Iris de Wit, a former fleet operations lead in Amsterdam, built Vlootzicht — a maintenance-scheduling and inspection-logging tool for small commercial vehicle fleets — starting in Bolt and extending it in Cursor. It had forty-one paying customers on €89/month and an enterprise prospect asking uncomfortable questions about data separation.

The day-two findings note was worse than the scoping call had suggested: fleet data was separated by a company ID filter applied in application code, not in the database, and three query paths bypassed it entirely. At the day-eight midpoint review, the choice was put to Iris plainly — two and a half days to move tenancy enforcement into row-level security with a migration, or keep the scoped admin reporting view. She dropped the reporting view.

**Result:** Vlootzicht cut over in week three with database-enforced tenant isolation, verified by an acceptance test Iris ran herself against two accounts, and the enterprise prospect's security questionnaire was answered with a written description of the model rather than a promise. The reporting view shipped six weeks later as a separate, smaller piece of work.

> *"The midpoint call was the whole engagement. If they'd just quietly made that choice for me and told me afterwards, I'd have accepted it — and it would have been the wrong one for the deal I was chasing."*
> — **Iris de Wit, Founder, Vlootzicht (Amsterdam)**

**Cost & Timeline:** €5,400 (Launch & Grow package, tenant isolation, Stripe subscriptions, monitoring and managed hosting) — cutover in 15 business days.

---

## Frequently Asked Questions

### Why do the first two days produce no visible output?

Because they are spent reading your schema, mapping every route into your data, and running vulnerability and secret scans. Writing code before that map exists produces changes that have to be redone once the real structure becomes clear, which is far more expensive than two days of reading.

### What happens to my existing paying customers during a cutover?

They are planned around rather than interrupted. DNS TTLs are lowered in advance, a low-traffic maintenance window is chosen, migrations are written with a tested rollback path, and error rates and payment success are watched for several hours afterwards. On most products of this size, actual downtime is minutes or none.

### Can a three-week engagement handle a database migration on live data?

Yes, provided it is identified early — which is what the day-eight midpoint review is for. A migration found on day eight is a planned trade-off against something else in scope; the same migration found on day thirteen is what turns three weeks into four.

### How much of my own time does a three-week engagement require?

Roughly six hours in total, but concentrated: access setup before day one, a weekly call, personal testing against the acceptance checklist, a real decision at the midpoint, and availability at cutover. The value is in being fast at those specific moments rather than generally available throughout.

### Is a smoke test the same as a proper load test?

No. A smoke test at a few multiples of your current peak finds the obvious cliff — an unindexed query, a connection pool limit, a third-party rate cap — in an afternoon. A formal load test models sustained traffic patterns and capacity planning, which is a separate exercise usually worth doing later, once you have real growth data rather than assumptions.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why do the first two days produce no visible output?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They are spent reading the schema, mapping every route into your data, and running vulnerability and secret scans. Writing code before that map exists produces changes that must be redone once the real structure is understood."
      }
    },
    {
      "@type": "Question",
      "name": "What happens to my existing paying customers during a cutover?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They are planned around: DNS TTLs lowered in advance, a low-traffic window chosen, migrations written with a tested rollback, and error and payment rates watched afterwards. On products of this size, downtime is typically minutes or none."
      }
    },
    {
      "@type": "Question",
      "name": "Can a three-week engagement handle a database migration on live data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, provided it is identified early, which is the purpose of the midpoint review around day eight. A migration found on day eight is a planned trade-off; the same one found on day thirteen is what turns three weeks into four."
      }
    },
    {
      "@type": "Question",
      "name": "How much of my own time does a three-week engagement require?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "About six hours, concentrated at four moments: access setup before day one, the weekly call, personal testing against the acceptance checklist, and the midpoint trade-off decision, plus availability at cutover."
      }
    },
    {
      "@type": "Question",
      "name": "Is a smoke test the same as a proper load test?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. A smoke test at a few multiples of current peak finds obvious cliffs such as unindexed queries or connection pool limits in an afternoon. A formal load test models sustained traffic and capacity, and is usually better done later with real growth data."
      }
    }
  ]
}
</script>
