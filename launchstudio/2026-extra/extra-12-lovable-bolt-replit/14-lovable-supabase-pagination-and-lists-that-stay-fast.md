---
Title: "Lovable Supabase: Pagination and Lists That Stay Fast"
Keywords: lovable supabase, pagination, cursor pagination, offset performance, list pages, infinite scroll, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Supabase: Pagination and Lists That Stay Fast

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Pagination and Lists That Stay Fast",
  "description": "Every AI-built app has a list page, and most of them load the whole table. Offset versus cursor pagination, why page 400 is slow, and how to keep lists fast as data grows.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-11",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-supabase-pagination-and-lists-that-stay-fast" }
}
</script>

Open the main list page of an AI-built product and watch the network tab. In a large proportion of them you will see a single request returning every row the account owns — four hundred, nine thousand, whatever exists — which the browser then filters, sorts and displays twenty of.

It works. It is fast at first. And it degrades along three axes at once: the database reads more, the network transfers more, and the browser holds more in memory, until a phone on a train cannot open the page at all.

The fix is pagination, and the reason it is worth an article is that the obvious way to do it is the one that breaks later.

## Why Page 400 Is Slower Than Page 1

The default approach is offset: skip 20, take 20; skip 40, take 20. It is what every tutorial shows and what an AI tool will write.

The problem is what skipping means. To return rows 8,001 to 8,020 sorted by date, the database must produce the first 8,020 rows in order and then discard 8,000 of them. The work grows with how deep you go, which is why the last pages of a long list are dramatically slower than the first.

For most products this never matters, because nobody visits page 400 and because their tables are small. It matters for three specific cases: an export or sync that walks every page in a loop, a list ordered in a way that puts interesting rows at the end, and a table that has grown past a few hundred thousand rows.

There is a second, subtler problem. Offsets are unstable. If a row is inserted while someone is paging, everything shifts by one — so an item can appear on two consecutive pages, or be skipped entirely. For a human clicking through it is a curiosity. For a job importing every page into another system, it is silent data loss.

## Cursor Pagination, Explained Once

The alternative asks a different question. Instead of "skip 8,000 rows", it says "give me the next 20 rows after this specific one".

The cursor is the sort key of the last row you saw — typically a timestamp and an identifier to break ties. The next page is a straightforward filter, which an index answers instantly regardless of how deep you are. Page 400 costs the same as page 1, and rows cannot be duplicated or skipped by inserts happening elsewhere.

The cost is that you cannot jump to an arbitrary page number, because the cursor only knows about the row you just saw. In practice this suits most product interfaces, which are load-more buttons or infinite scroll rather than numbered pages.

The rule of thumb: numbered pages with offsets for administrative screens over modest tables; cursors for anything long, anything infinite-scrolling, and every programmatic consumer such as an export, a sync or an API your customers call.

## The Sort Must Be Total

Both approaches break in the same way if the sort order is ambiguous.

Sorting by a creation date alone is not enough, because two rows can share a timestamp — and when they do, the database is free to return them in a different order each time. With offsets that produces rows appearing twice across pages. With cursors it produces a page boundary that either loses a row or repeats one.

Always sort by something unique as a tiebreaker: the date, then the identifier. The index should match that ordering exactly, and the cursor must carry both values.

This is a two-minute change that eliminates an entire class of "sometimes a record is missing from the list" report, which otherwise gets categorised as intermittent and is never fixed.

## Do Not Count Unless You Must

The pagination question always drags a second one behind it: showing the total.

A count over a large filtered table is frequently more expensive than fetching the page, and it runs on every page load. For most interfaces the total is decoration — users want the first twenty results and a way to continue, not the knowledge that there are 8,412.

Three sensible options. Omit it, and use a next control that appears when more rows exist — which you can determine by asking for one row more than you display. Estimate it, using the database's own statistics, and label it as approximate. Or maintain a counter deliberately for the one place it genuinely matters.

The cheap trick is worth naming: request 21 rows, display 20, and the existence of the 21st tells you there is a next page. No count, no extra query.

## Filtering and Sorting Are Part of the Problem

A list page that lets users filter and sort is really many queries, and each combination needs to be served by an index or it will fall back to reading everything.

Be deliberate about what you offer. Three useful filters and two sort orders, each backed by an appropriate index, makes a fast page. Twelve filters in arbitrary combinations makes a page that is fast in the combinations you tested and slow in the ones customers use.

For search across text, do not use a pattern match with a leading wildcard — it cannot use an ordinary index and will read the table. Postgres has proper full-text search, and adopting it for the one field people search is usually an hour of work.

## Infinite Scroll Has Its Own Costs

If the interface keeps appending rows as the user scrolls, the browser accumulates every row fetched. Four hundred rows of rich list items is a page that stutters on a mid-range phone, and the user did not choose it — they just kept scrolling.

Two mitigations, in order of effort. Keep the rows light: avoid heavy components per row and load images lazily at the size actually displayed. And if lists genuinely get long, render only what is visible, which is well-supported by libraries and is the point at which infinite scroll stops being free.

Also give people a way out. A filter or a search box is a better answer than scrolling to row 600, and it is cheaper for everyone.

## Exports Are Pagination Too

The place where offsets do the most damage is the export that nobody thinks of as a list page.

A CSV of everything, built by fetching all rows at once, works until a customer has enough data to exhaust memory or exceed a timeout — and it fails for your largest customer, who is the one you least want to disappoint.

Walk the data with a cursor, stream it to the client or to a file as you go, and for anything genuinely large, generate it in the background and send a link when it is ready. The middle option — streaming — is usually enough and is a small change from what already exists.

## Pagination Belongs to the API, Not the Page

One design decision saves a great deal of rework later: make the bounded page the shape of your data access everywhere, not a thing you added to one screen.

If fetching records is always "give me a page, here is the cursor", then every consumer inherits it — the list screen, the mobile view you build next year, the export, the customer-facing API, the internal admin tool, the sync to somebody's accounting package. If instead the default is "fetch everything" with pagination bolted onto the one page that got slow, each new consumer starts from the unbounded version and the problem is rediscovered every time.

Practically this means the function your application calls to read records takes a limit and a cursor, and has no mode that returns everything. Code that genuinely needs all rows — a nightly job, a migration — loops over pages explicitly, which is both honest about what it is doing and safe as the data grows.

The same applies to anything you expose to customers. An endpoint without a maximum page size is an endpoint one customer will request a hundred thousand rows from, in a loop, from a script they wrote at half past four on a Friday. Set a ceiling, document it, and return the cursor in the response so the correct usage is the easy one.

## Setting This Up

For an existing product this is typically one day: list endpoints changed to fetch a bounded page rather than everything, cursor pagination for long lists, exports and any programmatic consumer, a total sort order with a unique tiebreaker matching an index, counts removed or estimated with the fetch-one-extra trick for next-page detection, filters and sorts constrained to combinations that indexes cover, text search moved off pattern matching, exports converted to cursor walks with streaming, and the whole thing verified against a seeded table large enough to show the difference.

LaunchStudio does this as part of performance work, usually alongside indexing, and the two together are what keep a product feeling the same at 200 customers as it did at 20. The engineers are Manifera's: eleven years, 160+ projects, from Herengracht 420 in Amsterdam and development in Ho Chi Minh City.

[Send us the page that got slow](https://launchstudio.eu/en/#contact) and we will tell you which of the two problems it is.

## Real example

### The Export That Failed for the Best Customer

Rutger Doedens built Urenstaat with Lovable: timesheet and project-hours tracking for engineering consultancies, 34 firms, the largest with 90 consultants.

Two complaints arrived in the same fortnight. The hours overview took eleven seconds to load for that largest firm and was instant for everyone else. And the monthly export — the thing every firm does on the first working day to invoice clients — failed for that same firm with a timeout, every month, which they had been working around by exporting week by week.

Both had the same cause. The overview fetched every hour entry for the firm and paginated in the browser: 240,000 rows for the large firm, 3,000 for a typical one. The export did the same thing and then built a CSV in memory.

One business day: the overview converted to cursor pagination on timestamp and identifier, with a matching composite index and a total sort order; the row count replaced with a next control using the fetch-one-extra technique; filters reduced from nine arbitrary fields to four backed by indexes, with the consultant-name filter moved to full-text search; the export rewritten to walk the data with a cursor and stream rows to the response as it goes, with a background job and an email link for exports above a threshold; and the whole thing tested against a seeded database of 400,000 entries rather than the 900 in development.

**Result:** the overview went from 11 seconds to 240 milliseconds for the largest firm, and the monthly export completed in 9 seconds rather than failing. Rutger's largest customer stopped exporting week by week, and mentioned it at renewal.

> *"My worst performance problems were all in my best customer's account. They were the only ones with enough data to find them, and the last people I wanted finding them."*
> — **Rutger Doedens, Founder, Urenstaat (Enschede)**

**Cost & Timeline:** €1,900 (cursor pagination with composite index, total ordering, count removal, filter and search rework, streaming export with background generation, load verification against seeded volume) — completed in 1 business day.

## Frequently Asked Questions

### When is offset pagination good enough?

For administrative screens over modest tables where users want numbered pages and nobody goes deep. Anything long, infinite-scrolling or read by a program should use cursors.

### Why does a record sometimes appear on two pages?

Because the sort order is not unique, or rows were inserted while someone paged through. Sort by a timestamp plus a unique identifier, and prefer cursors for anything a program consumes.

### How do I show a next-page button without counting?

Request one row more than you display. If it comes back, there is another page. No count query needed.

### Should I use infinite scroll?

Only with light rows and, once lists get genuinely long, virtualised rendering. And always provide filtering or search, because scrolling is a poor way to find anything past the first hundred rows.

### Why does my export fail only for large customers?

Because it fetches everything into memory before writing. Walk the data with a cursor and stream it out, or generate it in the background and send a link.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "When is offset pagination good enough?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Administrative screens over modest tables with numbered pages. Long lists, infinite scroll and programmatic consumers should use cursors."
      }
    },
    {
      "@type": "Question",
      "name": "Why does a record appear on two pages?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The sort order is not unique, or rows shifted while paging. Sort by timestamp plus a unique identifier and use cursors for programmatic reads."
      }
    },
    {
      "@type": "Question",
      "name": "How do I show a next-page control without counting rows?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Fetch one row more than you display; if it returns, a next page exists. No count query required."
      }
    },
    {
      "@type": "Question",
      "name": "Is infinite scroll a good choice?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Only with light rows and virtualised rendering once lists get long, and always alongside filtering or search."
      }
    },
    {
      "@type": "Question",
      "name": "Why does my CSV export fail only for large customers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It loads everything into memory first. Walk with a cursor and stream output, or generate in the background and email a link."
      }
    }
  ]
}
</script>
