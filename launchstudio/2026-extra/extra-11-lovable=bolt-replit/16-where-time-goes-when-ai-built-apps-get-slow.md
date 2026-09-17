---
Title: "Lovable App Performance: Where the Time Goes in Production"
Keywords: Lovable, ai app performance, n+1 queries supabase, missing database index, image optimisation founder, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable App Performance: Where the Time Goes in Production

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable App Performance: Where the Time Goes in Production",
  "description": "Why AI-built applications feel instant with forty rows and sluggish with four thousand: repeated queries, missing indexes, unoptimised images and oversized bundles — with a measurement-first method for finding which one is yours.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-18",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/where-time-goes-when-ai-built-apps-get-slow" }
}
</script>

Nothing changed. That is what makes this particular problem so disorienting: you did not deploy anything, you did not touch the database, and yet the page that loaded instantly in March takes six seconds in June. Your code is identical. What changed is the amount of data it is running against, and AI-generated applications are unusually sensitive to that, for reasons that are entirely predictable once you know where to look.

Slowness is not one problem. It is three, they have different symptoms, and fixing the wrong one is how founders spend a fortnight optimising something that was never the bottleneck.

## The Three Kinds of Slow

**Slow to arrive.** The time between requesting a page and seeing anything at all. This is bundle size, server response time, cold starts and network round trips.

**Slow to fill.** The page appears but the content is missing, with a spinner. This is your data layer: queries, indexes, and how many separate requests are being made.

**Slow to respond.** The page is loaded and interaction is sluggish. This is usually rendering — too many elements, oversized images being scaled by the browser, work happening on every keystroke.

Before doing anything, establish which one you have. They feel similar to a frustrated user and they share almost no fixes.

## The Query Pattern That Multiplies Quietly

The most common data-layer problem in AI-generated apps has a name: the N+1 query. It happens when your app fetches a list, then makes an additional request for each item in that list.

Fetch twenty bookings, then for each booking fetch the customer, then for each customer fetch their company. That is one query plus twenty plus twenty — forty-one round trips where two would have done. With forty rows during development it is imperceptible. With four thousand rows it is a page that never finishes.

Generated code produces this pattern constantly, because it is the natural way to express the logic when you are thinking about one item at a time. Nothing is wrong with any individual query; the problem only exists in the aggregate, which is exactly the kind of thing a code review does not surface and a network tab does immediately.

The fix is to fetch related data in one query — a join, or the nested select your client library supports — rather than looping.

## Indexes: The Fix Nobody Thinks Of

A database index is a lookup structure that lets the database find matching rows without examining every row. Without one, a query filtering on a column reads the entire table.

With 500 rows, reading everything takes no measurable time. With 500,000, it takes seconds, and it gets worse every week you operate.

AI tools create tables from your description and rarely create indexes, because indexes are an optimisation decision rather than a structural one. The practical rule: any column you filter by, sort by or join on deserves an index. For a typical small app that is three to six indexes, added in one sitting, frequently turning multi-second pages into instant ones.

This is the single highest-return performance fix available to most AI-built products, and it is usually an afternoon.

## Images at Camera Resolution

Look at what your app serves when a user uploads a profile picture. In most generated applications, the answer is: exactly what they uploaded. A modern phone photograph is several megabytes and several thousand pixels wide, displayed in a 48-pixel circle.

The browser downloads the whole thing and scales it down. Twenty of them on a listing page is an enormous amount of transferred data for a page that shows tiny thumbnails.

The fix is processing at upload time: resize to the sizes you actually display, compress, serve modern formats, and keep the original only if you genuinely need it. This is usually the largest single improvement for perceived speed on mobile, and it also reduces your storage bill.

## Bundles and Cold Starts

Two smaller contributors worth knowing.

**Bundle size.** Generated apps accumulate dependencies — a date library, an icon set, a chart package, an animation library — and by default the browser downloads all of it before rendering anything. Splitting the bundle so each page loads only what it needs is a configuration change with a visible effect on first load.

**Cold starts.** Serverless functions that have not run recently take longer on the first request. If your app is quiet overnight, your first visitor each morning gets the slow version. This is rarely worth engineering around for a small product, and it is worth knowing so you do not chase a phantom.

## Why It Was Fast in Testing

Three reasons, all structural.

You tested with tens of rows, not thousands. You tested on a laptop over office wifi, not a mid-range phone on mobile data. And you tested alone, so nothing was competing for the same database connections.

Production reverses all three simultaneously, which is why the degradation feels sudden rather than gradual. It was gradual — you simply had no visibility into it.

## Measure Before You Optimise

Guessing is expensive and usually wrong. Four measurements give you an answer in twenty minutes.

**Open the network tab and reload a slow page.** Count the requests. If there are dozens of small identical-looking data requests, you have an N+1 problem. If one request takes four seconds, it is a query. If the largest items are images, it is the image pipeline.

**Look at query timings in your database dashboard.** Supabase and most managed providers show slow queries. The worst offender is usually obvious and usually the same one every time.

**Run a page through a public performance tool on a simulated mobile connection.** It will tell you what is large and what is blocking rendering.

**Check your database connection usage** during a busy period. Exhausted connections look like random slowness rather than consistent slowness, which is why they are so often misdiagnosed.

## The Fix Order That Works

In descending order of return for a typical AI-built product:

**Add the missing indexes.** Hours of work, frequently the biggest single win.

**Collapse the N+1 queries** on your two or three most-used pages.

**Process images at upload.** Biggest perceived improvement on mobile.

**Split the bundle** so pages load only what they need.

**Then, and only then, consider infrastructure** — a bigger database instance, caching, a content delivery network. Upgrading infrastructure before fixing queries is paying more to run the same inefficiency faster, and it is the most common way founders waste money on this problem.

## When It Genuinely Is Infrastructure

Sometimes the code is fine. Sustained traffic beyond what a small instance can serve, a database at its connection limit, or a workload that genuinely needs caching are real situations — they are simply less common than a missing index at this stage. The way to tell is that the fixes above produce no improvement, and that your measurements show resource saturation rather than slow individual operations.

## Getting It Diagnosed Properly

Performance work rewards measurement over instinct, which is why it is worth having someone do it who has seen the same four causes in a hundred applications. LaunchStudio's engineers profile the app, add the indexes, collapse the repeated queries, build the image pipeline, split the bundle and set up monitoring so you can see the effect rather than assume it — without touching the interface you built.

That is part of the [Launch Ready and Launch & Grow scopes](https://launchstudio.eu/en/#packages), and the team behind it is Manifera's, whose eleven years of production engineering for clients including Vodafone and TNO involves a great deal of exactly this unglamorous work.

If your app is slower than it was and you do not know why, [describe your project](https://launchstudio.eu/en/#contact) and you will get a diagnosis rather than a quote for a rebuild.

## Caching Is the Fix to Reach For Last

Caching gets suggested early in every performance conversation and belongs near the end, because it hides problems rather than removing them and it introduces a new category of bug.

**What it does well.** Data that is expensive to compute and rarely changes — a homepage listing, a public catalogue, an aggregate count — served from memory instead of recalculated per request. For read-heavy public pages this is genuinely transformative.

**What it does badly.** Anything personalised or transactional. Cache a page that includes the logged-in user's name and you will eventually serve one user's view to another, which is a data exposure rather than a performance issue.

**The bug it introduces.** Stale data. A price updated in the database and not in the cache is a customer seeing one number and being charged another. Every cache needs an invalidation rule, and getting invalidation right is famously the harder half.

**Why it comes last.** Caching an inefficient query makes the inefficiency intermittent rather than absent — fast until the cache misses, and then just as slow as before, usually under load, which is exactly when you least want it.

The order that works: fix the queries, add the indexes, optimise the images, split the bundle. Then, if public pages are still heavy under real traffic, cache them deliberately with explicit invalidation and never cache anything that varies per user.

## Real example

### A Recipe Platform That Got Slower Every Week

Fenna Hoekman's app, Kookstudio, hosted recipes and meal plans for a community of home cooks around Zwolle. It launched fast and grew steadily. By month five, the recipe browse page took between five and nine seconds to show anything, and her most active users had started complaining.

The measurement took an hour. The browse page issued one query for recipes, then one query per recipe for its author, then one per recipe for its tags — 121 requests for a page of forty recipes. The `recipes` table had no index on the category column used for filtering, so every filtered view read all 4,300 rows. Recipe photographs were served at full upload resolution, averaging 3.8 megabytes each, forty per page.

Five business days of work: the three queries collapsed into one nested select, four indexes added on the columns actually used for filtering and sorting, an upload pipeline added that generates thumbnail, card and full sizes in a modern format, and the bundle split so the browse page no longer downloads the recipe editor's dependencies.

**Result:** the browse page went from between five and nine seconds to under one second on a mid-range phone over mobile data, and the monthly storage and bandwidth bill fell by roughly two-thirds as a side effect.

> *"I had been reading about upgrading my database plan. The actual problem was four missing indexes and photographs the size of posters."*
> — **Fenna Hoekman, Founder, Kookstudio (Zwolle)**

**Cost & Timeline:** €2,200 (query optimisation, indexes, image pipeline, bundle splitting) — completed in 5 business days.

## Frequently Asked Questions

### Why did my app slow down without any code changes?

Because the code did not change but the data did. Queries that scan an entire table and pages that issue one request per item scale linearly with your content, so the same code takes longer every week you operate.

### What is an N+1 query and how do I spot it?

It is fetching a list and then making a separate request for each item in it. Open your browser's network tab and reload a slow page: dozens of near-identical small data requests is the signature, and the fix is fetching related data in a single query.

### Will upgrading my database plan fix the problem?

Usually not at this stage. A larger instance runs the same inefficient query faster, which buys time rather than solving anything. Add indexes and collapse repeated queries first, then reassess.

### How many indexes does a small app need?

Typically three to six: one for each column you filter, sort or join on frequently. It is one of the highest-return changes available and normally an afternoon of work.

### My app is only slow on mobile. Why?

Almost always images and bundle size. A desktop connection hides both. Process uploads into display-appropriate sizes and split your bundle before investigating anything more complex.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why did my app slow down without any code changes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The code did not change but the data did. Queries that scan whole tables and pages issuing one request per item scale with your content, so the same code takes longer as you grow."
      }
    },
    {
      "@type": "Question",
      "name": "What is an N+1 query and how do I spot it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Fetching a list and then making a separate request per item. In the browser network tab it appears as dozens of near-identical small requests; the fix is fetching related data in one query."
      }
    },
    {
      "@type": "Question",
      "name": "Will upgrading my database plan fix the problem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually not at this stage. A larger instance runs the same inefficient query faster. Add indexes and collapse repeated queries first, then reassess."
      }
    },
    {
      "@type": "Question",
      "name": "How many indexes does a small app need?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Typically three to six — one for each column frequently filtered, sorted or joined on. It is among the highest-return changes and usually an afternoon of work."
      }
    },
    {
      "@type": "Question",
      "name": "My app is only slow on mobile. Why?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Almost always images and bundle size, both of which a desktop connection hides. Process uploads into display sizes and split the bundle before investigating further."
      }
    }
  ]
}
</script>
