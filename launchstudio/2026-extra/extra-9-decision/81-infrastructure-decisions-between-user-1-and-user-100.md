---
Title: "Infrastructure Decisions That Matter Between User 1 and User 100"
Keywords: saas infrastructure decisions, database schema scaling, background job processing, session handling architecture, file storage saas, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# Infrastructure Decisions That Matter Between User 1 and User 100

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Infrastructure Decisions That Matter Between User 1 and User 100",
  "description": "Some early infrastructure shortcuts are free to fix later and some become expensive, downtime-risking rewrites the moment real users show up. A concrete guide to which is which, covering database schema, background jobs, file storage, and session handling.",
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
  "datePublished": "2027-01-04",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/infrastructure-decisions-between-user-1-and-user-100"
  }
}
</script>

Which of the technical decisions you're making this month will still be fine when you have 10,000 users, and which ones will need to be ripped out and rebuilt under pressure during your busiest growth week? Almost no founder can answer that question with confidence, because nobody sorts early infrastructure choices into "cheap to fix later" and "expensive to fix later" before shipping — they build whatever gets the product live fastest, usually with an AI coding tool doing the heavy lifting, and find out which bucket each decision fell into only when it breaks. The frustrating part is that the split isn't random. Some choices genuinely don't matter until you're well past product-market fit, and a small number of others get exponentially harder to change for every additional week you wait, because by the time you notice the problem, real user data is sitting on top of the wrong structure.

## The Real Difference Between "Works" and "Scales"

A prototype and a scaling product are judged by different standards, and confusing the two is where most early technical debt gets created. "Works" means the demo runs, a handful of beta users can sign up and use the core feature, and nothing visibly breaks during a walkthrough. "Scales" means the same code behaves correctly under concurrent load, doesn't silently corrupt or lose data as volume grows, and doesn't require someone to be awake at 2 AM manually intervening every time traffic spikes. Between user 1 and user 100, almost every SaaS product looks identical from the outside regardless of which path it took internally — the difference only becomes visible between user 100 and user 1,000, which is exactly why founders systematically underprice the decisions made in this window. The rule of thumb that actually holds up across the products LaunchStudio has hardened: decisions that touch how data is *structured and stored* are expensive to reverse once real users depend on them; decisions that touch how work gets *processed* are moderately expensive to reverse; decisions about *where files live* and *how sessions are tracked* are the cheapest to defer, right up until a specific, predictable trigger event forces the issue.

## Database Schema and Indexing: The Decision You Can't Undo Without Downtime

Of every category of early infrastructure decision, database schema is the one that punishes procrastination hardest, because fixing it after the fact usually means a migration running against a live table with real customer rows in it — not a code change, a data operation, with all the risk that implies. Two specific mistakes show up constantly in AI-generated prototypes taken from Lovable, Bolt, or Cursor: missing indexes on foreign keys and frequently-filtered columns, and schema shapes that store structured data as unindexed JSON blobs because it was faster to prototype that way. Neither one causes a visible problem at 50 users, because a full table scan across 200 rows returns in milliseconds regardless of whether an index exists. The same query against 200,000 rows, without an index, can take seconds — and at that point, adding the index isn't free anymore, because building an index on a large, actively-written table can lock it or degrade write performance during the operation, which means it has to be scheduled, tested, and sometimes run with `CONCURRENTLY` in PostgreSQL to avoid taking the product down while it happens. The fix that costs nothing pre-launch — add an index on every foreign key and every column you'll filter or sort by in a `WHERE` or `ORDER BY` clause — costs a genuine engineering task with real risk once the table has grown. The related mistake, storing what should be structured relational data as a JSON column because an AI tool defaulted to it, compounds the same way: it's trivial to query flexibly at 50 rows and genuinely painful to query, index, or migrate out of at 50,000.

## Background Jobs: Why Code That Works at 10 Users Breaks at 200

The second expensive-to-defer decision is whether slow or bursty operations — sending emails, generating PDFs, processing an uploaded file, calling a third-party API, running a webhook handler — happen synchronously inside the request that triggered them, or get handed off to a background job queue. At 10 users, synchronous processing is invisible: a signup that sends a welcome email adds perhaps 400 milliseconds to the response, nobody notices, and the code is simpler to write and reason about. At 200 concurrent signups — a launch day spike, a mention on a newsletter, a Product Hunt feature — that same synchronous email call means 200 requests all holding a server thread open waiting on an external mail API, and if that API is even briefly slow, the entire application can queue up and appear down to every user, not just the ones triggering emails. The fix is a job queue — Redis-backed tools like BullMQ for Node.js stacks or equivalent queueing built into Laravel and Django are standard, well-documented, and not expensive to add early. The reason this belongs in the "fix it before it hurts" category rather than the "defer freely" category is that retrofitting a queue after synchronous code has spread across a dozen endpoints means finding and rewriting every one of those call sites under time pressure, usually right when growth makes the rewrite riskiest to attempt.

## File Storage: The Local Disk Trap

By contrast, file storage is one of the cheaper decisions to get wrong early and fix later, provided you catch it before it becomes a data-loss event rather than a performance one. AI-generated prototypes frequently save uploaded files — user avatars, generated documents, imported CSVs — directly to local disk on the server, because it's the simplest thing to make work in a demo. This is genuinely fine for a single-server deployment with light usage. It becomes a real problem the moment the app runs on more than one server instance, because a file uploaded to server A is invisible to a request that lands on server B — and it becomes a data-loss problem the moment a hosting provider redeploys or restarts the instance and the local disk gets wiped, taking every uploaded file with it. The fix — moving storage to S3, Cloudflare R2, or Supabase Storage — is a well-scoped, contained piece of work: swap the file-write calls for an SDK call to object storage, migrate existing files once, done. Unlike schema changes, this rarely touches production data structure or requires a risky live migration under load, which is exactly why it's safe to defer until you're actually adding a second server instance or notice files disappearing after a deploy — just don't defer it past that specific trigger.

## Session Handling: The Multi-Instance Problem Hiding in Plain Sight

Session handling follows a similar shape to file storage — safe to leave as-is for longer than founders assume, but with one specific trigger that turns it urgent. Many AI-scaffolded auth setups store session state in server memory or in a way that implicitly assumes one server instance is answering every request. That's fine, and arguably simpler, right up until you scale horizontally — adding a second application instance for reliability or load — at which point a user can get logged out mid-session simply because their next request happened to land on the instance that doesn't have their session in memory. The fix is to move session state somewhere every instance can read: a shared Redis store, a database-backed session table, or a switch to stateless JWT-based sessions that don't require server-side storage at all. This is a moderate, well-understood change, not a data migration — existing users simply get issued a fresh session on their next login, with no historical data to preserve. The decision point is concrete and easy to watch for: the moment you add a second server, load balancer, or auto-scaling group, session handling needs to already be fixed, not scheduled for "sometime soon."

## A Threshold Table: What to Fix at 100, 1,000, and 10,000 Users

Mapping these decisions to rough user-count thresholds makes the abstract concrete, even though the exact numbers shift by product type. Below roughly 100 users, almost nothing here needs attention yet except getting indexes right on the handful of tables you already know will grow fastest — user records, transactional data, anything queried on every page load. Between 100 and 1,000 users, background jobs for anything touching an external API or taking more than a second becomes worth doing before it's forced on you, and file storage should move off local disk the moment you're planning any kind of redundancy or multi-instance deployment. Past 1,000 users, database query performance under real, messy production data patterns — not the clean data from a demo — starts to matter, N+1 query patterns that AI tools frequently generate become genuinely slow rather than theoretically inefficient, and session handling needs to already be solved if it isn't. By 10,000 users, all four of these should be long settled, and the new work shifts to caching layers, read replicas, and connection pooling — a different, later conversation.

## The Cost of Getting the Order Wrong

The founders who get burned aren't the ones who deferred these decisions — deferring the right ones is smart, not negligent. They're the ones who deferred the expensive ones because they looked, from the outside, exactly as harmless as the cheap ones. A missing database index and a local file-upload folder both work fine in a demo; only one of them turns into a locked production table during a migration attempted at 2 AM while paying customers are trying to use the product. This is precisely the kind of judgment call that's hard to make alone if you can't read the codebase yourself, and it's a large part of why [LaunchStudio](https://launchstudio.eu/en/#process) exists as a "last mile" service rather than a full rebuild shop — the team, backed by Manifera's 11+ years of production engineering experience, reviews what an AI tool actually generated, tells you specifically which of your current shortcuts are fine to leave alone and which are quietly compounding, and fixes only the ones that matter before they become a 2 AM incident instead of a planned two-day task.

[Get a free scope review of your prototype](https://launchstudio.eu/en/#contact) — most scale-up founders are surprised to learn that two or three specific fixes account for nearly all of their real scaling risk, not the dozen things they were worried about.

## Real example

### A Rotterdam SaaS Hits Its First Real Traffic Spike

Tijs Bakker built Ledgerly, a small-business invoicing tool, in Bolt over six weeks and grew it to 340 paying users mostly through word of mouth, without touching the backend beyond what the AI tool generated by default. When a Dutch fintech newsletter featured Ledgerly and drove a single-day spike of 1,200 signups, the app didn't crash outright — it simply became unusably slow for twenty minutes, with signup confirmation emails arriving up to an hour late and several users abandoning the flow entirely.

A LaunchStudio scoping call the following week traced the slowdown to exactly two of the decisions covered above: welcome and invoice-notification emails were being sent synchronously inside the request cycle, and the `invoices` table had no index on the `user_id` foreign key it was filtered by on every dashboard load. Neither issue was visible at Tijs's normal traffic level; both became the entire bottleneck under a burst.

**Result:** A Redis-backed job queue for all outbound email and a single added index resolved both issues in a four-day fixed-price engagement. Ledgerly's next traffic spike, a similarly-sized feature in a different newsletter three months later, produced no slowdown at all.

> *"I thought I needed to rebuild the backend. It turned out to be one queue and one index — I just had no way to know which two things out of everything actually mattered."*
> — **Tijs Bakker, Founder, Ledgerly (Rotterdam)**

## Frequently Asked Questions

### How do I know if my database is missing indexes without being able to read the code myself?

Ask a technical partner to run an `EXPLAIN ANALYZE` on your slowest-feeling queries, or simply describe which pages of your app feel sluggish as your data grows — a scoping call can usually spot missing indexes on foreign keys and frequently-filtered columns within an hour of looking at the schema.

### Is it ever safe to just keep using local file storage?

Yes, as long as you're running a single server instance and haven't lost files after a deploy — the moment you add a second instance for reliability or plan to, object storage like S3 or Supabase Storage should already be in place, since the failure mode is silent data loss, not just slowness.

### Do I need a background job system from day one, or can it really wait?

It can wait until you're regularly seeing more than a handful of concurrent signups or requests that trigger slow external calls — the risk isn't the concept, it's how many endpoints have grown to depend on synchronous processing by the time you finally add a queue.

### What's the single most expensive infrastructure mistake you see in AI-generated prototypes?

Unindexed foreign keys on tables that later hold real transactional data, because fixing it after the fact means running a schema change against live production data instead of a clean, low-risk code deploy.

### How does LaunchStudio decide what to fix versus what to leave alone?

A scoping call reviews the actual codebase and current usage pattern against known scaling thresholds, then fixes only the specific gaps that are cheap now and expensive later — never a full rebuild, and never touching the frontend you've already built.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I know if my database is missing indexes without being able to read the code myself?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ask a technical partner to run an EXPLAIN ANALYZE on your slowest-feeling queries, or describe which pages feel sluggish as your data grows — a scoping call can usually spot missing indexes on foreign keys and filtered columns within an hour."
      }
    },
    {
      "@type": "Question",
      "name": "Is it ever safe to just keep using local file storage?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, as long as you run a single server instance and haven't lost files after a deploy. The moment you add a second instance for reliability, object storage like S3 or Supabase Storage should already be in place, since the failure mode is silent data loss."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need a background job system from day one, or can it really wait?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It can wait until you regularly see concurrent signups or slow external calls — the risk isn't the concept, it's how many endpoints have grown to depend on synchronous processing by the time you finally add a queue."
      }
    },
    {
      "@type": "Question",
      "name": "What's the single most expensive infrastructure mistake you see in AI-generated prototypes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Unindexed foreign keys on tables that later hold real transactional data, because fixing it after the fact means running a schema change against live production data instead of a clean code deploy."
      }
    },
    {
      "@type": "Question",
      "name": "How does LaunchStudio decide what to fix versus what to leave alone?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A scoping call reviews the actual codebase and usage pattern against known scaling thresholds, then fixes only the specific gaps that are cheap now and expensive later — never a full rebuild, and never touching the existing frontend."
      }
    }
  ]
}
</script>
