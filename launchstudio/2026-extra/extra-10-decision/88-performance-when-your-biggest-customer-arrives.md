---
Title: "Performance When Your Biggest Customer Arrives"
Keywords: saas performance large account, n plus one query, pagination missing, slow dashboard large dataset, database index for scale, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# Performance When Your Biggest Customer Arrives

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Performance When Your Biggest Customer Arrives",
  "description": "Products built and tested on small accounts break in predictable ways when one customer arrives with fifty times the data. The specific patterns that fail, how to find them before the customer does, and why the largest account is also usually the most valuable.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-05-09",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/performance-when-your-biggest-customer-arrives" }
}
</script>

The customer you most want is the one most likely to break your product. They arrive with four years of history to import, twelve people who will use it simultaneously, and expectations set by software that handles their volume without noticing. Everything you built and tested against accounts holding thirty records meets an account holding sixty thousand, and the failure is rarely a crash — it is a product that becomes slow enough to be unusable, for them specifically, while working perfectly for everyone else.

This is worth anticipating for a commercial reason as much as a technical one: the largest account is usually the largest invoice, and it is the one whose experience determines whether you can sell to similar businesses. Performance problems here are not an engineering inconvenience; they are the thing standing between you and the customers you most want.

## The Patterns That Break, in Order of Frequency

Products degrade at scale in a small number of well-known ways, and AI-generated code exhibits them reliably because a generator optimises for producing something that works, not something that works at volume.

**The query in a loop.** The page fetches 200 projects, then for each project fetches its owner — 201 queries where two would do. At ten projects this is imperceptible. At a thousand it is several seconds. This single pattern accounts for more slow pages in generated code than everything else combined, because it is the natural way to write the logic if you are not thinking about the database.

**No pagination.** A list page that loads every record. Fine at fifty, catastrophic at fifty thousand, and it fails on three axes at once: the database work, the transfer, and the browser rendering.

**Missing indexes.** A query filtering on a column with no index scans the entire table. Imperceptible on small tables, and the dominant cost on large ones.

**Aggregations computed on every view.** Dashboard totals summing every record each time the page loads, rather than being maintained or cached.

**Everything loaded at once.** A page fetching six datasets before rendering anything, so its speed is the slowest of the six plus overhead.

**Work done in the browser.** Sorting and filtering ten thousand records client-side, which requires transferring them first and then freezes the interface while it runs.

Each has a standard remedy. What matters is knowing they are there, which requires testing at a volume you have not yet encountered.

## Finding Out Before the Customer Does

The test is straightforward and rarely performed: create an account containing considerably more data than your largest real customer, and use the product.

Generate a realistic volume — if the biggest account has 5,000 records, make one with 100,000 — and then click through every page yourself, timing them. The problems announce themselves immediately, and you will typically find that three or four pages account for all of the slowness.

Then look from the database's side. Every managed database exposes a slow query log, and reading the top ten queries by total time tells you where the work is going. Almost always a small number of queries dominate, and fixing the top three transforms the product.

Two habits keep this from regressing. Measure the response time of your main pages routinely, at a high percentile rather than an average — the average is dominated by small accounts and hides exactly the customer you care about. And when a customer says the product is slow, ask which page and check that page for that account, since slowness is usually specific rather than general.

## Fix the Cause, Not the Symptom

When something is slow, the tempting remedies — a bigger database, a cache in front of it — treat the symptom and postpone the diagnosis.

The order that works: **find the actual slow query**, using the database's own tools rather than guessing; **understand why it is slow**, which for most cases means a missing index or a query pattern that fetches far more than needed; **fix it directly**, with an index, a restructured query, or pagination. Only then consider caching, and only for genuinely expensive computations that cannot be made cheap.

Caching deserves that caution because it introduces its own class of problem — stale data, invalidation, and bugs that appear only for some customers — and applied over an unfixed query it hides the issue until the cache misses at the worst moment.

Scaling hardware has a similar shape. Increasing database capacity to compensate for a missing index works, costs money every month indefinitely, and stops working at the next threshold. The index is cheaper and permanent.

Finding and fixing the queries that make a product slow for its largest customers is well-understood engineering, and it is the most common category of work needed when an AI-built product meets its first serious account. LaunchStudio, backed by Manifera's 11+ years of production engineering, performs exactly this review, including testing against generated data at the volume you expect rather than the volume you have. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Designing for Volume Without Over-Building

Preparing for scale you do not have is a genuine waste, and there is a small set of decisions that costs almost nothing now and prevents the expensive version later.

**Paginate every list from the start.** Retrofitting pagination means changing the interface, the API, and anything consuming it. Building it in from the beginning is trivial and it removes the most common failure entirely.

**Index the columns you filter and sort by**, particularly the account identifier that scopes every query in a multi-tenant product.

**Fetch related data in one query rather than in a loop**, which is a habit rather than an architecture.

**Set a limit on everything that returns a list**, including internal endpoints. A default cap of a few hundred means an unexpected volume produces a truncated result rather than a timeout.

**Do heavy work in the background.** Reports, exports, and imports belong in a job with progress, not in a request.

That list is a day of attention during the build. What it does not require is caching layers, read replicas, sharding, or a queue-based architecture — all of which are legitimate at a scale most products never reach, and all of which cost more to maintain than they return at a hundred customers.

## Real example

### Forty Seconds for the Customer Paying the Most

Elif Demir ran Verzuimlijn, an absence-tracking tool for HR departments, built in Bolt. Most customers were companies of 20 to 60 employees, and the product was comfortably fast for all of them.

Her first enterprise account had 1,400 employees and six years of history. Their main overview page took 38 seconds to load and frequently timed out. Three problems compounded: the page fetched all employees and then queried each one's absence records individually — 1,401 queries; there was no pagination, so every employee was returned regardless; and the absence table had no index on the employee reference, so each of those 1,400 queries scanned the whole table.

The account was also degrading the product for everyone else, since each page load consumed most of the database's capacity for the better part of a minute.

**Result:** the query pattern replaced with two queries fetching employees and their aggregated absence data together, pagination added at 50 per page with search, indexes added on the employee reference and date columns, and dashboard totals precomputed nightly. Load time went from 38 seconds to 400 milliseconds, and general slowness reported by three smaller customers disappeared at the same time.

> "The customer paying me the most had the worst experience of anyone, and every one of the causes had been in the product since the first week."
> — **Elif Demir, Founder, Verzuimlijn**

**Cost & Timeline:** performance review and optimisation delivered in 3 business days.

## Frequently Asked Questions

### Why is my product slow for one customer and fast for everyone else?

Because performance problems scale with data volume. A query pattern or missing index that is imperceptible on a small account becomes dominant on a large one, so slowness appears account by account rather than globally.

### What is the most common performance problem in AI-generated code?

Fetching a list and then querying the database once per item in it, producing hundreds of queries where two would suffice. Missing pagination and missing indexes follow closely.

### How do I test performance before I have a large customer?

Generate an account with substantially more data than your largest real one, use the product, and time each page. Then read the database's slow query log, where a small number of queries usually account for most of the load.

### Should I add caching to fix a slow page?

Only after the underlying query has been made efficient. Caching over an unfixed query hides the problem and introduces staleness and invalidation bugs of its own.

### What should I build for scale before I need it?

Pagination on every list, indexes on the columns you filter and sort by, fetching related data in one query rather than in a loop, limits on every list endpoint, and heavy work moved to background jobs. Caching layers and replicas can wait.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Why is my product slow for one customer and fast for everyone else?", "acceptedAnswer": { "@type": "Answer", "text": "Performance problems scale with data volume, so a query pattern or missing index that is imperceptible on a small account becomes dominant on a large one." } },
    { "@type": "Question", "name": "What is the most common performance problem in AI-generated code?", "acceptedAnswer": { "@type": "Answer", "text": "Fetching a list then querying the database once per item, producing hundreds of queries where two would do. Missing pagination and missing indexes follow closely." } },
    { "@type": "Question", "name": "How do I test performance before I have a large customer?", "acceptedAnswer": { "@type": "Answer", "text": "Generate an account with far more data than your largest real one and time each page, then read the database's slow query log where a few queries usually dominate." } },
    { "@type": "Question", "name": "Should I add caching to fix a slow page?", "acceptedAnswer": { "@type": "Answer", "text": "Only after the underlying query is efficient. Caching over an unfixed query hides the problem and adds staleness and invalidation bugs." } },
    { "@type": "Question", "name": "What should I build for scale before I need it?", "acceptedAnswer": { "@type": "Answer", "text": "Pagination on every list, indexes on filtered and sorted columns, fetching related data in one query, limits on list endpoints, and heavy work in background jobs." } }
  ]
}
</script>
