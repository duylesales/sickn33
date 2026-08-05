---
Title: "Performance Optimisation: When Your Software Is Too Slow for Users"
Keywords: software performance, web performance, page load speed, database optimisation, caching, Manifera
Buyer Stage: Awareness
Target Persona: C (Product Manager / Product Owner)
Content Format: Diagnostic Guide
---

# Performance Optimisation: When Your Software Is Too Slow for Users

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Performance Optimisation: When Your Software Is Too Slow for Users",
  "description": "A practical diagnostic guide for identifying and fixing the most common software performance problems — covering frontend load times, API response times, database query optimisation, and caching strategies.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "datePublished": "2026-08-05",
  "dateModified": "2026-08-05"
}
</script>

Google's "The Need for Mobile Speed" research found that 53% of mobile site visits are abandoned when a page takes longer than 3 seconds to load. The other benchmark every performance team cites — that Amazon's early 2000s A/B testing found every 100ms of added latency cost roughly 1% in sales — traces back to a conference talk and blog post by former Amazon engineer Greg Linden, not a formal published Amazon report. The underlying pattern holds up independently, though: at Velocity 2009, engineers from Google Search and Bing separately presented controlled latency experiments with strikingly similar results — Google found a 400ms delay reduced searches per user by 0.59%, and Bing found a 2-second slowdown reduced revenue per user by 4.3%. Applying that order of magnitude to a €10 million ARR SaaS product, a sustained 100ms regression could plausibly cost somewhere in the tens of thousands of euros per year in lost conversions — the exact multiplier varies by product, but the direction is consistent across every study on the subject. Performance is not a technical vanity metric — it is revenue.

Yet most startups only think about performance after users start complaining. By that point, the architecture has calcified around slow patterns that are expensive to undo. This guide helps you identify where your software is slow, why, and how to fix it systematically.

## The Performance Budget: Define "Fast" Before You Build

A performance budget is a set of quantitative targets that your application must meet. Without one, "fast" is subjective and unmeasurable.

**Recommended performance budgets for B2B SaaS in 2026:**

| Metric | Target | Measurement Tool |
|--------|--------|-----------------|
| First Contentful Paint (FCP) | < 1.2 seconds | Lighthouse, WebPageTest |
| Largest Contentful Paint (LCP) | < 2.5 seconds | Core Web Vitals |
| Time to Interactive (TTI) | < 3.0 seconds | Lighthouse |
| API response time (p95) | < 200ms | APM tools (Datadog, New Relic) |
| Database query time (p95) | < 50ms | Query analyser |
| Total page weight | < 500KB (compressed) | Browser DevTools |

Embed these targets in your CI/CD pipeline. If a pull request pushes any metric beyond the budget, the build fails. Performance degradation should be treated with the same urgency as a broken test.

## The RAIL Model: A Framework for Deciding Where to Look First

A performance budget tells you *whether* you have a problem. It does not tell you *where* to look. When a metric misses its target, teams often start optimising the wrong layer entirely — shrinking JavaScript bundles when the real bottleneck is a database query, or adding database indexes when users are actually complaining about animation jank on a button click. RAIL, a performance model developed by the Google Chrome team, gives a structured way to map a user complaint to the right diagnostic layer before you spend a sprint on the wrong fix.

RAIL breaks user-perceived performance into four stages, each with a latency budget grounded in human perception research:

| RAIL Stage | Budget | What It Measures | Where the Bottleneck Usually Lives |
|------------|--------|--------------------|---------------------------------------|
| **Response** | Under 100ms | Time from user input (click, tap) to visible acknowledgement | Frontend event handlers, main-thread-blocking JavaScript |
| **Animation** | Under 10ms per frame (16ms total budget; ~6ms is reserved for the browser itself) | Smoothness of scrolling, transitions, and animations | Frontend rendering — layout thrashing, unoptimised CSS, an oversized DOM |
| **Idle** | Use idle windows of roughly 50ms or less | Whether the browser has spare capacity to pre-fetch or pre-compute | Frontend background work scheduling |
| **Load** | Interactive in under 5 seconds on a mid-range mobile device over a typical mobile network | Whether the application is usable at all on first visit | Backend API response time, database queries, bundle size, network round-trips |

**How to use it diagnostically:** If users report the interface "feels laggy" when clicking a button, the problem sits in the Response budget — look at the frontend event-handling and main-thread-blocking causes covered in the next section, not the database. If users report the page "takes forever to show anything," the problem sits in the Load budget — that is where the backend, database, and caching sections later in this guide apply. This distinction matters in practice because the fixes are almost entirely non-overlapping: a team that spends a sprint optimising database queries in response to "the app feels laggy" complaints is very likely solving the wrong problem, because that specific complaint usually describes a Response or Animation issue living entirely in the browser, three sections away from any query the backend team could touch.

## Frontend Performance: The User's First Impression

Most performance problems that users notice are frontend problems — not because the server is slow, but because the browser is doing too much work before showing meaningful content.

**The three biggest frontend performance killers:**

**1. JavaScript bundle size.** If your React application ships 2MB of JavaScript, the user's browser must download, parse, and execute all of it before the page becomes interactive. Fix: code splitting (load only the JavaScript needed for the current page), tree shaking (remove unused library code), and lazy loading (defer non-critical components).

**2. Unoptimised images.** A single 5MB hero image on your landing page destroys load times on mobile connections. Fix: use modern formats (WebP, AVIF), implement responsive images with `srcset`, lazy-load images below the fold, and set explicit width/height attributes to prevent layout shift.

**3. Render-blocking resources.** CSS and JavaScript files in the `<head>` that block the browser from rendering any content until they are fully loaded. Fix: inline critical CSS, defer non-critical CSS, add `async` or `defer` attributes to non-essential scripts.

## Backend Performance: API Response Times

When your frontend is optimised but the application still feels sluggish, the bottleneck has moved to the backend. The most common backend performance problems:

**1. N+1 query problem.** The single most common database performance issue. Your code loads a list of 100 orders, then executes a separate database query for each order to load the customer details. That is 101 database queries instead of 2 (one for orders, one for all relevant customers). Fix: eager loading in your ORM, or write explicit JOIN queries.

**2. Missing database indexes.** A query scanning 10 million rows because the WHERE clause column has no index. Fix: analyse your slow query log, identify the most expensive queries, and add indexes on the columns used in WHERE, JOIN, and ORDER BY clauses. One index can turn a 5-second query into a 5-millisecond query.

**3. Synchronous external API calls.** Your endpoint calls three external APIs sequentially — each taking 200ms. Total response time: 600ms. Fix: make the calls concurrently (Promise.all in JavaScript, asyncio.gather in Python). Total response time: 200ms.

**4. No caching.** Your application recalculates the same expensive report every time a user views the dashboard. Fix: cache the result with an appropriate expiration time. Redis is the standard choice for application-level caching.

## Database Optimisation: The Foundation of Everything

The database is almost always the ultimate bottleneck. When your application is slow, the first place to investigate is the database.

**The diagnostic workflow:**

1. **Enable the slow query log.** Every major database (PostgreSQL, MySQL, MongoDB) can log queries that exceed a time threshold. Set the threshold to 100ms and let it run for a week.
2. **Analyse the top 10 slowest queries.** Use EXPLAIN ANALYZE to understand what the database is doing: is it scanning the entire table? Is it sorting a million rows in memory? Is it joining five tables without indexes?
3. **Fix in order of impact.** One query that runs 10,000 times per day and takes 500ms each time consumes 5,000 seconds of database time daily. That is where your optimisation effort should start.

**Common fixes:**

- **Add indexes** on frequently queried columns (but do not over-index — every index slows down writes).
- **Denormalise** when read performance matters more than write normalisation. Store the customer name directly on the order record instead of joining tables every time.
- **Use read replicas** to distribute read traffic across multiple database instances.
- **Implement connection pooling** (PgBouncer for PostgreSQL) to prevent running out of database connections under load.

## Caching Strategy: The 80/20 of Performance

Caching delivers the highest performance improvement per engineering hour invested. The key is caching at the right layer:

**Layer 1: Browser caching.** Set appropriate `Cache-Control` headers on static assets (JavaScript, CSS, images). Immutable assets with content hashes (`app.a1b2c3.js`) should be cached for 1 year.

**Layer 2: CDN caching.** Serve static assets and cacheable API responses from edge locations close to your users. Cloudflare, AWS CloudFront, or Fastly reduce latency from 200ms (origin server in Europe) to 20ms (edge server in the user's country).

**Layer 3: Application caching (Redis).** Cache frequently accessed data that is expensive to compute: dashboard aggregations, user session data, permission checks, and search results.

**Layer 4: Database query caching.** Most databases have built-in query caches. PostgreSQL's shared_buffers and work_mem settings significantly impact performance when properly tuned.

**The cache invalidation problem:** The two hardest problems in computer science are cache invalidation, naming things, and off-by-one errors. Use time-based expiration (TTL) for data that can tolerate slight staleness. Use event-based invalidation (purge the cache when the underlying data changes) for data that must be current.

## Performance Monitoring: Measure Everything, Always

Performance optimisation without measurement is guesswork. Set up continuous monitoring from day one:

- **Real User Monitoring (RUM):** Track actual page load times from real users on real devices and real networks. Vercel Analytics, Google Analytics Web Vitals, or Datadog RUM.
- **Application Performance Monitoring (APM):** Trace every request from the user's browser to the database and back. Identify bottlenecks in specific services, functions, or queries. Datadog, New Relic, or Sentry Performance.
- **Synthetic monitoring:** Run automated performance tests from multiple geographic locations every 5 minutes. Alert when response times degrade. Pingdom, Uptime Robot, or AWS CloudWatch Synthetics.

At Manifera, performance is a first-class engineering concern across our distributed teams. Our [custom software development](https://www.manifera.com/services/custom-software-development/) includes performance budgets, database optimisation, and monitoring setup as standard deliverables — not optional add-ons.

Discuss your application's performance challenges — [manifera.com/contact-us](https://www.manifera.com/contact-us/).

---

## Frequently Asked Questions

### Our application is fast in development but slow in production. What is going wrong? (Scenario: Full-stack developer whose app loads in 500ms locally but 4 seconds in production)

Three likely causes: (1) Data volume — your development database has 1,000 rows, production has 1 million. Queries that scan the entire table are fast with small data and catastrophic with large data. Add indexes. (2) Network latency — your development environment has zero network latency between services. Production services communicate over the network, adding milliseconds per call. (3) Concurrent users — your local environment has one user. Production has hundreds of simultaneous requests competing for database connections and server memory. Load test your staging environment with realistic traffic patterns.

### How do we balance new feature development with performance work? (Scenario: Product Manager whose backlog has 50 feature requests and 20 performance issues)

Treat performance like technical debt — allocate 15-20% of sprint capacity to performance improvements. Prioritise by user impact: a 2-second page load affecting 10,000 daily users is more important than a 5-second report load affecting 50 admin users. Include performance acceptance criteria in feature specifications: "The dashboard must load in under 2 seconds with 1,000 data points." This prevents new features from creating new performance problems.

### What database should we choose for optimal performance? (Scenario: CTO starting a new project and choosing between PostgreSQL, MySQL, and MongoDB)

For 90% of B2B SaaS applications, PostgreSQL is the correct choice. It handles relational data excellently, supports JSON for semi-structured data, has excellent indexing capabilities, and scales to billions of rows with proper tuning. Use MongoDB only if your data is genuinely document-oriented and schema-less. Use MySQL if your team has deep MySQL expertise. The database choice matters less than how you use it — proper indexing and query optimisation matter more than which engine you pick.

### When should we add a caching layer? (Scenario: Engineering lead noticing database CPU at 80% during peak hours)

Add caching when you see the same expensive query executed repeatedly with the same parameters. Start with Redis for application-level caching — cache dashboard data, user sessions, and permission checks. For most applications, adding Redis caching reduces database load by 50-70% and costs €50-€200/month for a managed instance. The implementation typically takes 2-3 days per cached endpoint.

### How do we set performance targets that are realistic? (Scenario: Product Owner defining non-functional requirements for a new feature)

Base targets on industry benchmarks and user expectations: p95 page load under 3 seconds, p95 API response under 500ms, and p99 under 2 seconds. Then validate against your specific user base — if 60% of your users are on mobile in Southeast Asia, your targets must account for slower network connections. Monitor real user data for 2 weeks to establish a baseline, then set improvement targets of 20-30% per quarter.

### A user says "the app feels laggy" — how do we know if that's a frontend or backend problem before we start debugging? (Scenario: Engineering lead triaging a vague performance complaint with no clear reproduction steps)

Use the RAIL model to classify the complaint before assigning it. "Laggy when I click things" almost always describes a Response-budget problem (target: under 100ms) — that lives in frontend event handlers and main-thread-blocking JavaScript, not the database. "Choppy when I scroll" describes an Animation-budget problem (target: under 10ms per frame) — also frontend, usually layout thrashing or an oversized DOM. "Takes forever to show anything" describes a Load-budget problem (target: interactive under 5 seconds) — that is where backend API response time, database queries, and bundle size come in. Classifying the complaint first prevents a common failure mode: a team spending a sprint on database optimisation to fix a complaint that was actually about animation jank in the browser.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Our application is fast in development but slow in production. What is going wrong?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Three likely causes: (1) Data volume — development has 1,000 rows, production has 1 million. (2) Network latency — development has zero latency between services. (3) Concurrent users — local has one user, production has hundreds competing for resources. Load test staging with realistic traffic."
      }
    },
    {
      "@type": "Question",
      "name": "How do we balance new feature development with performance work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Allocate 15-20% of sprint capacity to performance. Prioritise by user impact. Include performance acceptance criteria in feature specs: 'The dashboard must load in under 2 seconds with 1,000 data points.' This prevents new features from creating new performance problems."
      }
    },
    {
      "@type": "Question",
      "name": "What database should we choose for optimal performance?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For 90% of B2B SaaS applications, PostgreSQL. It handles relational data, supports JSON, has excellent indexing, and scales to billions of rows. The database choice matters less than how you use it — proper indexing matters more than which engine you pick."
      }
    },
    {
      "@type": "Question",
      "name": "When should we add a caching layer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "When you see the same expensive query executed repeatedly. Start with Redis — cache dashboards, sessions, and permissions. Adding Redis typically reduces database load by 50-70% and costs €50-€200/month. Implementation takes 2-3 days per endpoint."
      }
    },
    {
      "@type": "Question",
      "name": "How do we set performance targets that are realistic?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Base on benchmarks: p95 page load under 3 seconds, p95 API under 500ms. Validate against your user base — account for mobile users on slower networks. Monitor real data for 2 weeks to establish a baseline, then target 20-30% improvement per quarter."
      }
    },
    {
      "@type": "Question",
      "name": "A user says 'the app feels laggy' — how do we know if that's a frontend or backend problem before we start debugging?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use the RAIL model to classify the complaint first. 'Laggy when I click things' is usually a Response-budget problem (under 100ms), which lives in frontend event handlers, not the database. 'Choppy when I scroll' is an Animation-budget problem (under 10ms per frame), also frontend. 'Takes forever to show anything' is a Load-budget problem (interactive under 5 seconds), which is where backend and database work applies. Classifying first prevents teams from spending a sprint on database optimisation to fix what was actually browser-side animation jank."
      }
    }
  ]
}
</script>
