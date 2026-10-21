---
Title: "Lovable Hosting: Load Testing Before a Large Customer Onboards"
Keywords: lovable load testing, performance testing, k6, Supabase performance, capacity planning, enterprise onboarding, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Scale-Up
---

# Lovable Hosting: Load Testing Before a Large Customer Onboards

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting: Load Testing Before a Large Customer Onboards",
  "description": "A customer twice the size of all the others will find every limit your product has, on its first Monday morning. How to model their load, seed data at their scale, run realistic tests, read the results, find the bottleneck, and go live with measured headroom instead of hope.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-23",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-hosting-load-testing-before-a-large-customer-onboards" }
}
</script>

The contract is signed. The new customer has more users than all your existing customers together, and they will all start on the same Monday. Your product has never served this many people, held this much data, or seen this many requests in a single hour — and you will find out how it copes in front of the most important customer you have.

Load testing replaces that discovery with a rehearsal. It is not an enterprise ritual reserved for large engineering teams. For a product built with Lovable and Supabase, a useful load test is a few days of work: model what the customer will do, create data at their scale, simulate their busiest hour, and measure where the product slows down. Almost every product that does this finds two or three problems that would have been visible to the customer within the first hour — and fixes them before anyone notices.

This article covers what to test, how to model a customer's load, why data volume matters more than concurrent users, how to run tests safely, how to read the results, where bottlenecks usually are in AI-built products, and how to go live with measured headroom.

## Start From the Customer, Not the Tool

The most common mistake is to begin with a tool and an arbitrary number — "let's see what happens with a thousand users" — rather than with the customer's actual behaviour.

Ask the customer, and write down:

- **How many users, and how many active at the same time.** A care organisation with 2,600 carers may have 900 of them opening the app between 6:45 and 7:15 when shifts start. That half-hour is the test, not the daily average.
- **What they do in that window.** Open the roster, check today's clients, register the start of a visit. Three or four actions, each a handful of requests.
- **How much data they bring.** Clients, records, history, documents — and how much they will add per month.
- **What runs in the background for them.** Nightly calculations, reminders, integrations with their systems, month-end invoicing.
- **What they integrate.** An API or import that sends thousands of records at once is a load pattern of its own.

From this, define the scenario: the user journeys, their mix, the peak arrival rate, and the data volume — usually tested at two to three times the customer's expected size, so the result includes headroom.

## Data Volume Matters More Than Concurrency

In AI-built products, most performance problems are not caused by many people at once. They are caused by one query that is fast with your test data and slow with a real customer's.

A roster screen that loads in 200 milliseconds with fifty carers can take ten seconds with three thousand, because it fetches every shift for every carer, or because a row level security function runs once for each of a hundred thousand rows, or because an index that seemed unnecessary at small scale is missing. None of these show up with ten concurrent users on a small database; all of them show up with one user on a large one.

So the first step of a load test is not traffic but data. Create a test environment with data at the customer's scale — and at two or three times it — using generated data that resembles reality: the same distributions, the same number of related records per parent, the same proportion of large accounts. The seed data article in this series describes how; the important thing is that the largest organisation in the test is as large as the largest organisation you will have.

Then run the slowest screens and endpoints as a single user and look at the timings and query plans before simulating any concurrency at all. This alone usually finds the first problem.

## Where to Run the Test

Not against production. A load test that saturates the database slows down every existing customer, and test data written into production is the kind of mistake that is discussed for months.

Use a separate environment with the same configuration as production: the same Supabase plan and compute size, the same pooling settings, the same edge function configuration, the same region. A Supabase branch or a separate project works; what matters is that it resembles production closely enough that its limits are production's limits. The environment variables article in this series describes how to keep its credentials separate.

Disable or redirect everything outbound in the test environment: emails, SMS, push notifications, payments, accounting sync, webhooks to customers. A load test that sends three thousand real text messages is a load test you will remember for the wrong reasons.

Run the load generator from outside the platform — a separate machine or a cloud load testing service — so that the test includes the network path real users take.

## Writing Realistic Scenarios

A realistic test simulates what users do, not a single endpoint called as fast as possible.

```js
// k6 scenario: carers starting their shift
import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  scenarios: {
    shift_start: {
      executor: 'ramping-arrival-rate',
      startRate: 2, timeUnit: '1s', preAllocatedVUs: 300,
      stages: [
        { target: 30, duration: '10m' },   // ramp to peak
        { target: 30, duration: '20m' },   // hold the peak
        { target: 2,  duration: '5m' },
      ],
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],
    'http_req_duration{name:roster}': ['p(95)<800'],
    'http_req_duration{name:visit_start}': ['p(95)<500'],
  },
};

export default function () {
  const token = tokens[__VU % tokens.length];      // pre-created test users
  const headers = { Authorization: `Bearer ${token}` };
  const r = http.get(`${BASE}/rest/v1/rpc/my_roster_today`, { headers, tags: { name: 'roster' } });
  check(r, { 'roster ok': (res) => res.status === 200 });
  sleep(5 + Math.random() * 10);                   // reading the screen
  http.post(`${BASE}/functions/v1/visit-start`, JSON.stringify({ visit_id: pick(r) }),
            { headers, tags: { name: 'visit_start' } });
}
```

Four details make the difference between a meaningful test and a misleading one.

**Use many real test users**, each signed in with their own token and belonging to the right organisation, so row level security behaves as it will in production. A test with one user and one token tests caching, not the product.

**Include think time** — the seconds a person spends reading a screen. Without it, a hundred simulated users behave like several thousand real ones.

**Model arrival rate, not just user count.** People arrive over the peak window, not all at the same millisecond — unless the real behaviour is a notification that everyone taps at once, in which case test exactly that spike.

**Define pass and fail in advance.** Thresholds — 95% of roster requests under 800 milliseconds, fewer than 1% errors — turn the test into a yes or no rather than a graph to interpret.

k6 is a good default for products of this kind; Artillery and Locust are reasonable alternatives. The tool matters less than the scenario.

## Four Kinds of Test

**Load test** — the expected peak, at the expected data volume, held for long enough to be meaningful. This answers "will Monday morning work?"

**Stress test** — increase the load until something breaks, to know where the limit is and what fails first. This answers "how much headroom do we have?"

**Spike test** — a sudden jump from quiet to peak, as after a push notification or an email to every user. This tests autoscaling, cold starts and connection pools.

**Soak test** — a normal load for several hours. This finds memory leaks, slowly filling queues, and connection pools that degrade over time.

For a single large customer onboarding, a load test at two to three times their expected peak and a spike test are the minimum. A stress test tells you when to plan the next upgrade.

## What to Measure

Collect three groups of measurements during each run.

**From the load generator:** latency percentiles per scenario step — median, p95, p99 — error rate, and throughput. Percentiles matter more than averages: an average of 400 milliseconds can hide that one request in twenty takes eight seconds, and those are the requests users remember.

**From the database:** CPU, memory, active connections against the limit, and above all the slowest queries. Enable `pg_stat_statements` and look at the queries with the highest total time during the test — not only the slowest single query, but the one that runs thousands of times at moderate cost. The indexes article in this series describes how to read query plans.

**From the platform:** edge function duration and cold starts, error rates, and any rate limiting from third parties. Also watch queue lengths for background jobs, which can grow silently while the foreground looks healthy.

Record the configuration of each run — data volume, compute size, code version — so results can be compared after each fix.

## Where AI-Built Products Usually Break

The same handful of bottlenecks appear in almost every test.

**Missing indexes and unbounded queries.** Lists that fetch everything, filters on unindexed columns, sorting large tables. The pagination and indexes articles in this series cover the fixes; they are usually the largest single improvement.

**Row level security that is expensive per row.** A policy that calls a function performing its own query, evaluated for every row of a large table. Rewrite helpers as `stable security definer` functions that the planner can evaluate once, index the membership tables they read, and filter by organisation explicitly in queries so the policy is not the only filter.

**N+1 request patterns.** A screen that loads a list and then makes a separate request per item — fifty items, fifty-one requests. Harmless for one user, crushing for nine hundred. Replace with one query or one RPC that returns what the screen needs.

**Connection exhaustion.** Edge functions or a backend opening direct database connections instead of using the pooler, until the connection limit is reached and requests start failing. The connection pooling article in this series describes the configuration.

**Synchronous calls to third parties.** Sending a push notification, an email or an accounting booking inside the user's request. At scale, the provider's rate limit becomes your latency. Move it to a queue.

**Background jobs that do not scale linearly.** A nightly calculation that takes twenty minutes for current customers and six hours for the new one, overlapping with the morning peak. Batch it, parallelise it with care for the database, and test it at the customer's volume as part of the load test.

## The Fix-and-Retest Cycle

Load testing is iterative. Run the test, find the largest bottleneck, fix it, run the same test again, compare. Change one thing at a time where possible, so each improvement is attributable.

Fix the code before scaling the infrastructure. Upgrading the database compute size makes a missing index slightly less slow; adding the index makes it fast and keeps the smaller instance. Once queries and patterns are sound, a compute upgrade is often still needed — but then it buys real headroom rather than hiding a defect.

Keep the scenario scripts in the repository and rerun them before each significant release and before each new large customer. A load test that runs once is a snapshot; one that runs regularly catches regressions an AI-assisted refactor may introduce.

## Capacity Planning and Cost

The final test run should give you three numbers: the load you expect, the load at which the product stays within its thresholds, and the load at which it breaks. Aim for two to three times headroom between expected peak and the point where thresholds are exceeded.

Translate that into infrastructure and cost: which compute size, which plan, what that costs per month, and what the next step up costs when the following customer arrives. The hosting cost articles in this series describe how; the point here is that the customer's contract value and the infrastructure cost to serve them are now both known numbers rather than estimates.

Share a short summary with the customer if they ask — and larger customers increasingly do. "We tested at three times your expected peak, with these results" is a strong answer in a procurement process and a reassuring one for their project manager.

## Onboarding in Steps

Even with a successful test, avoid moving every user of a large customer on the same morning if you can.

Agree a staged onboarding: one department or region first, then the rest a week later. Watch the real metrics during the first stage and compare them with the test. Real users always do something the scenario did not anticipate — a report run at the busiest moment, an export of everything, a browser tab left polling — and a first stage of a few hundred users reveals it while the stakes are low.

Prepare the response in advance: who watches the dashboards during the first peak, what the thresholds for intervention are, which kill switches exist for expensive features, as the feature flags article in this series describes, and how the customer is informed if something slows down.

## Setting This Up

For a Lovable or Supabase product preparing for a large customer, this is typically four to six days: the customer's peak behaviour, data volume and background work modelled from conversations with them, a production-like test environment with outbound messages disabled, generated data at two to three times the customer's scale, single-user profiling of the slowest screens first, realistic scenarios with many test users, think time, arrival rates and pass-fail thresholds, load and spike tests at a minimum, database, platform and queue metrics collected per run, the common bottlenecks addressed — indexes, unbounded lists, row level security cost, N+1 patterns, pooling, synchronous third-party calls, background job scaling — a fix-and-retest cycle with code fixed before infrastructure is scaled, a capacity and cost summary with explicit headroom, scenario scripts kept for future runs, and a staged onboarding with monitoring and a prepared response.

LaunchStudio runs this before the onboarding that matters most. Behind it is Manifera — eleven years, 120+ engineers, 160+ projects, with infrastructure experience from clients including Vodafone, TNO and CFLW.

[Tell us about the customer you are about to onboard](https://launchstudio.eu/en/#contact) and we will tell you what to test.

## Real example

### Nine Hundred Carers at Seven O'Clock

Thomas van Leeuwen built Zorgrooster in Lovable: rostering and visit registration for home care organisations, used by 23 small organisations with around 1,400 carers in total.

He signed a regional care group with 2,600 carers — almost double his entire user base — due to go live on a Monday. The care group's shifts start at 7:00, and most carers open the app between 6:45 and 7:15 to see their clients for the day.

A load test in a production-like environment, with generated data at three times the care group's size and a scenario of 900 carers arriving over thirty minutes, failed badly. The roster screen's p95 was 9.8 seconds. At around 400 concurrent users, requests began failing with connection errors. Starting a visit sent a push notification to the coordinator inside the request, and the provider's rate limit added seconds to every visit start. And the nightly calculation of worked hours, which took twenty minutes for existing customers, took six hours at the new scale — ending after the morning peak had begun.

Five business days: the roster query rewritten to fetch one week for one carer through a single RPC, with two composite indexes added; the row level security helper rewritten as a `stable security definer` function with an indexed membership lookup, removing a per-row subquery; edge functions moved to the transaction pooler; push notifications moved to a queue processed by a worker; the hours calculation batched by organisation and week and run in parallel with a concurrency limit; the database compute upgraded one size after the code fixes; and the load and spike tests rerun after each change.

**Result:** the final test at three times the care group's expected peak gave a roster p95 of 420 milliseconds, no errors and a nightly calculation of 35 minutes. The care group was onboarded in two stages; on the second Monday, 2,600 carers started their shifts without a single support call about speed. Infrastructure costs rose by about €110 a month.

> *"The first test told me that on our biggest customer's first morning, the roster would take ten seconds to load and then stop loading at all. I would much rather have heard it from k6 than from nine hundred carers."*
> — **Thomas van Leeuwen, Founder, Zorgrooster (Assen)**

**Cost & Timeline:** €5,400 (customer load modelling, production-like test environment with generated data at 3x scale, k6 load and spike scenarios, query and index fixes, row level security helper rewrite, pooler configuration, queued notifications, batched nightly calculation, compute sizing, staged onboarding plan) — completed in 5 business days.

## Frequently Asked Questions

### When should I load test my product?

Before onboarding a customer substantially larger than your current ones, before a launch or campaign that will bring a sudden peak, and as a regular check before significant releases.

### Should I load test against production?

No. Use a separate environment with the same plan, compute size, pooling and region, with outbound messages disabled, so the test does not affect existing customers or send real messages.

### Is the number of concurrent users the most important factor?

Usually not. In AI-built products, data volume causes most slowdowns — queries and policies that are fast on small data and slow on large data. Seed data at the customer's scale first.

### What should I measure during a load test?

Latency percentiles and error rates per user action, database CPU, connections and slowest queries, edge function duration and cold starts, third-party rate limits, and background queue lengths.

### Should I upgrade the database or fix the code first?

Fix the code first — indexes, unbounded queries, expensive policies, N+1 patterns. Then size the infrastructure for two to three times the expected peak.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "When should a SaaS product be load tested?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Before onboarding a much larger customer, before a launch or campaign peak, and regularly before significant releases."
      }
    },
    {
      "@type": "Question",
      "name": "Is it safe to load test production?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — use a production-like environment with the same plan, compute, pooling and region, with outbound messages disabled."
      }
    },
    {
      "@type": "Question",
      "name": "What usually causes slowdowns in AI-built apps?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Data volume more than concurrency — missing indexes, unbounded lists and expensive row level security on large datasets."
      }
    },
    {
      "@type": "Question",
      "name": "What metrics matter in a load test?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Latency percentiles and errors per action, database CPU, connections and slow queries, function cold starts, third-party limits and queue lengths."
      }
    },
    {
      "@type": "Question",
      "name": "Should I scale infrastructure or fix code first?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Fix code first, then size infrastructure for two to three times the expected peak."
      }
    }
  ]
}
</script>
