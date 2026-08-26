---
Title: "Case Study: Migrating From a Single Postgres Instance to Read Replicas Without Downtime"
Keywords: Postgres Read Replicas, Zero-Downtime Migration, Database Scaling, Connection Pooling, Supabase Postgres, LaunchStudio, Manifera
Buyer Stage: Decision
---

# Case Study: Migrating From a Single Postgres Instance to Read Replicas Without Downtime

Every AI SaaS product built on a single Postgres instance eventually hits the same wall: read traffic — dashboard loads, RAG context lookups, analytics queries — grows faster than the primary database can comfortably serve alongside the writes that actually change data, and CPU or connection saturation starts showing up as slow page loads across the entire product, not just the heaviest queries. Migrating to read replicas fixes this, but the migration itself carries real risk: done carelessly, it can take the product offline for the exact users the migration was meant to help. This is the story of Ingrid, a founder whose single-instance Postgres database was buckling under read load, and the specific six-day, zero-downtime migration LaunchStudio ran to split her traffic across a primary and two read replicas.

## The Product and the Problem

Ingrid used **Cursor** to build a market-research platform that let brand strategists query a database of consumer survey data using natural language, with an AI layer translating questions into SQL and summarizing the results. The product had grown to 60 paying teams, and usage patterns showed a predictable but increasingly severe problem: query-heavy hours (weekday mornings, when strategists ran their weekly reports) pushed her single Supabase Postgres instance to 85-95% CPU utilization, and both read and write queries — including the writes updating each team's saved query history — slowed down together, because they were all competing for the same database's resources with no separation between read and write load.

Ingrid's monitoring showed average query latency during peak hours climbing to 2.1 seconds, up from a baseline of 180 milliseconds during quieter periods — and the product's own AI-generated SQL queries, some of them genuinely complex aggregations across large survey datasets, were disproportionately responsible for the load, competing directly with the simpler writes that kept the product's core save and update functions responsive. The pattern was frustrating precisely because it was predictable and self-inflicted by success: the same weekly-report habit that made the product genuinely useful to strategists was also the exact traffic spike degrading the experience for everyone using it at the same time, including teams who weren't running a report at all and were simply trying to save a query.

## Why This Migration Is Genuinely Risky to Do Carelessly

A read-replica migration sounds simple in outline — stand up a replica, point read traffic at it — but three specific failure modes make it easy to get wrong, and each one produces a different kind of damage if missed.

**Replication lag causing stale reads on freshly written data.** A read replica is, by definition, slightly behind the primary. If a user saves a query and is immediately redirected to a page that reads from a replica that hasn't caught up yet, they can see their own just-created data appear to be missing — a specific, jarring bug pattern that erodes trust fast if the application doesn't account for it.

**An in-flight cutover that drops or duplicates requests.** Switching an application's read traffic from the primary to replicas isn't instantaneous at the infrastructure level; a naive cutover that flips a connection string without a coordinated rollout can leave some in-flight requests pointed at a database connection that's being torn down mid-query.

**Connection pool exhaustion during the transition.** Adding replicas means the application needs pooling logic aware of multiple database endpoints, not just one. A migration that doesn't correctly reconfigure connection pooling for the new topology can inadvertently create more total connections than the database tier supports, causing exactly the kind of saturation the migration was meant to fix — just distributed across more instances instead of solved.

## The Migration Plan

LaunchStudio's engineers designed the migration around a core principle: nothing about Ingrid's 60 active customer teams should notice anything happened, during the migration or after. That meant the work had to be sequenced carefully rather than executed as a single cutover event.

**Step one: provision replicas and validate replication health before touching application traffic.** Two read replicas were provisioned in the same region as the primary, and replication lag was monitored under real production write load for 48 hours before any application code changed — confirming replicas were staying within a consistently low lag window (under 50 milliseconds in Ingrid's case) rather than assuming a healthy replication link based on a brief initial test.

**Step two: classify every query in the application by read/write sensitivity.** Rather than routing all reads to replicas uniformly, the team categorized queries into three groups: writes and read-after-write operations (a user's own just-saved query history) that needed to stay on the primary to guarantee consistency, analytics and cross-team dashboard queries that could safely tolerate the replicas' small lag window, and a middle category — a user viewing another user's shared report — that got routed to replicas but with a short client-side cache-busting delay after any write touching that specific resource.

**Step three: implement read-after-write consistency logic for the sensitive path.** For the specific case of a user immediately viewing data they just created, the application was updated to route that request to the primary for a short window (a few seconds) after any write from that same session, rather than routing all reads to replicas uniformly and risking the stale-read bug entirely.

**Step four: roll out traffic gradually with a kill switch.** Rather than flipping all read traffic to replicas at once, the migration used a feature-flag-controlled rollout — 10% of eligible read traffic, then 50%, then 100% — over the course of two days, with real-time monitoring at each stage and an immediate rollback path if replica latency or error rates showed any regression.

## What Almost Went Wrong at the 50% Rollout Stage

The gradual rollout wasn't just a formality — it caught a real problem before it reached Ingrid's full customer base. During the 50% traffic stage, monitoring flagged a subset of dashboard queries whose latency on the replicas was actually *higher* than on the primary, the opposite of what the migration was supposed to achieve. The cause turned out to be a missing index: one of the more complex cross-team aggregation queries relied on an index that existed on the primary but hadn't been included in the replica provisioning script, which had been built from a slightly older schema snapshot. Because the rollout was staged rather than immediate, this surfaced as a contained, visible regression affecting roughly 30% of traffic for about twenty minutes rather than the entire customer base at once — the team paused the rollout at the feature-flag level, added the missing index to both replicas, confirmed replica query plans matched the primary's, and resumed the rollout from 50% rather than starting over. This is a specific, concrete argument for staged rollouts over a single cutover: not just as a theoretical safety net, but as a mechanism that catches migration-specific bugs — like a schema drift between primary and replica — while they're still small and reversible, instead of after they've reached every user.

## The Results

The migration completed with zero customer-visible downtime and zero reported data-freshness complaints. Peak-hour average query latency dropped from 2.1 seconds to 310 milliseconds, because write-sensitive queries no longer competed with the heavy analytics workload for the same database resources — the primary's CPU utilization during peak hours dropped from 85-95% to 35-45%, with the two replicas absorbing the analytics and dashboard read load that had previously saturated it. None of this required changes to Ingrid's Cursor-built frontend beyond the read-after-write consistency logic, which lived entirely in the backend's query-routing layer. Ingrid also kept the monitoring dashboard built for the migration in place afterward, giving her ongoing visibility into replica lag and per-query latency by category — visibility her original single-instance setup never had, and one she now checks before each new feature ships, specifically to catch the next query that might need reclassifying as her product's usage patterns keep evolving.

## Key Takeaways

- A single Postgres instance serving both heavy read and write traffic degrades both simultaneously once load grows, because reads and writes compete for the same database resources with no separation.

- The three real risks in a read-replica migration are replication lag causing stale reads, an uncoordinated cutover dropping in-flight requests, and connection pool misconfiguration recreating the exact saturation the migration was meant to fix.

- Classifying queries by read/write sensitivity — rather than routing all reads to replicas uniformly — is what prevents the specific bug where a user can't immediately see data they just created.

- A gradual, feature-flag-controlled traffic rollout with real-time monitoring and an immediate rollback path is what makes a zero-downtime migration actually zero-downtime, rather than just low-downtime.

- Splitting read and write load across a primary and replicas can produce large latency improvements — this migration cut peak-hour query latency by roughly 85% — without requiring changes to the existing frontend beyond query-routing logic in the backend.

## Get Your Database Scaled Without the Downtime Risk

If your Postgres instance is buckling under read load, a read-replica migration done carelessly can hurt more than the problem it fixes.

LaunchStudio is operated by **Manifera**, an international software engineering company founded in 2014 and led by Founder & Managing Director **Herre Roelevink**. Manifera brings 11+ years of production engineering experience and enterprise clients including Vodafone and TNO to every database engagement it runs for AI SaaS founders. Combining "Dutch management with Vietnamese mastery," Manifera maintains headquarters in **Amsterdam, the Netherlands** (Herengracht 420), an Asia hub in **Singapore** (100 Tras Street), and a primary development center in **Ho Chi Minh City, Vietnam** (Pho Quang Street). Through LaunchStudio, senior engineering teams design and execute zero-downtime read-replica migrations, with tested consistency logic and gradual, monitored rollouts — transforming your prototype into a scalable, production-ready MVP in 1 to 3 weeks, without a rebuild. [Get a free quote today](https://launchstudio.eu/en/#contact) or see how Manifera's [custom software development team](https://www.manifera.com/services/custom-software-development/) approaches database scaling for AI-generated codebases.

## Real example

### An AI-Native Founder in Action: Restaurant Inventory Forecasting Tool

Owen, a former restaurant operations manager, used **Lovable** to build a tool that used AI to forecast ingredient demand for small restaurant groups based on historical sales data. As his customer base grew to 35 restaurant groups, weekly forecast-generation runs — heavy read queries scanning months of historical data — began slowing down the entire application during the exact hours restaurant managers were also trying to log daily sales, since both workloads hit his single Postgres instance simultaneously.

Owen brought in LaunchStudio to migrate to a read-replica architecture without risking downtime during business hours his customers actively depended on. The team classified his queries — sales logging as write-sensitive, forecast generation as replica-safe — provisioned a single read replica, and rolled out the traffic split gradually over two days with monitoring at each stage.

**Result:** Forecast-generation queries no longer slowed down daily sales logging, and peak-hour query latency dropped from 1.8 seconds to 290 milliseconds, with zero downtime during the migration.

**Cost & Timeline:** €2,900 (Relaunch & Scale Package) — migration completed in 7 business days.

---

---

---
## Frequently Asked Questions

### How do you migrate to Postgres read replicas without downtime?

By provisioning and validating replica health before touching application traffic, classifying queries by read/write sensitivity so consistency-critical reads stay on the primary, implementing read-after-write consistency logic for the specific cases where a user needs to see their own just-created data, and rolling out traffic gradually with monitoring and a rollback path at each stage rather than a single cutover event.

### What is replication lag, and why does it matter for a migration like this?

Replication lag is the delay between a write happening on the primary database and that write becoming visible on a read replica. If application traffic is routed to a replica without accounting for this lag, a user can experience the jarring bug of not seeing data they just created, because the read hit a replica that hasn't caught up yet.

### Why not just route all read traffic to replicas immediately?

Because not all reads have the same consistency requirements. A user viewing data they just personally created needs guaranteed up-to-date results, typically served from the primary or with short-lived consistency logic, while analytics and cross-team dashboard queries can safely tolerate a replica's small lag window. Routing everything uniformly risks stale-read bugs on the sensitive cases.

### How much can read replicas actually improve query latency?

In this case study, splitting read and write load across a primary and two replicas cut peak-hour average query latency from 2.1 seconds to 310 milliseconds — roughly an 85% reduction — because write-sensitive queries stopped competing with heavy analytics workloads for the same database resources.

### How long does a zero-downtime read-replica migration typically take?

Most engagements take 1 to 2 weeks depending on query complexity and how many distinct read/write sensitivity categories the application has, typically falling under the Relaunch & Scale package (roughly €2,500-4,500) for a standard Postgres-based AI SaaS product.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do you migrate to Postgres read replicas without downtime?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "By provisioning and validating replica health before touching application traffic, classifying queries by read/write sensitivity so consistency-critical reads stay on the primary, implementing read-after-write consistency logic for the specific cases where a user needs to see their own just-created data, and rolling out traffic gradually with monitoring and a rollback path at each stage rather than a single cutover event."
      }
    },
    {
      "@type": "Question",
      "name": "What is replication lag, and why does it matter for a migration like this?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Replication lag is the delay between a write happening on the primary database and that write becoming visible on a read replica. If application traffic is routed to a replica without accounting for this lag, a user can experience the jarring bug of not seeing data they just created, because the read hit a replica that hasn't caught up yet."
      }
    },
    {
      "@type": "Question",
      "name": "Why not just route all read traffic to replicas immediately?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because not all reads have the same consistency requirements. A user viewing data they just personally created needs guaranteed up-to-date results, typically served from the primary or with short-lived consistency logic, while analytics and cross-team dashboard queries can safely tolerate a replica's small lag window. Routing everything uniformly risks stale-read bugs on the sensitive cases."
      }
    },
    {
      "@type": "Question",
      "name": "How much can read replicas actually improve query latency?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In this case study, splitting read and write load across a primary and two replicas cut peak-hour average query latency from 2.1 seconds to 310 milliseconds — roughly an 85% reduction — because write-sensitive queries stopped competing with heavy analytics workloads for the same database resources."
      }
    },
    {
      "@type": "Question",
      "name": "How long does a zero-downtime read-replica migration typically take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most engagements take 1 to 2 weeks depending on query complexity and how many distinct read/write sensitivity categories the application has, typically falling under the Relaunch & Scale package (roughly €2,500-4,500) for a standard Postgres-based AI SaaS product."
      }
    }
  ]
}
</script>
