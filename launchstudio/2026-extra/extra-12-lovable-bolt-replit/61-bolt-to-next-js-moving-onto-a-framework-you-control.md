---
Title: "Bolt to Next.js: Moving Onto a Framework You Control"
Keywords: bolt to next.js, migration, server rendering, framework choice, prototype to production, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Bolt to Next.js: Moving Onto a Framework You Control

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bolt to Next.js: Moving Onto a Framework You Control",
  "description": "When a Bolt prototype should move to a full framework, what actually transfers, the order that keeps the product running, and the honest case for not doing it at all.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-13",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/bolt-to-next-js-moving-onto-a-framework-you-control" }
}
</script>

Bolt typically produces a single-page application: a React frontend built with Vite, talking to Supabase from the browser. For a prototype this is exactly right and for many products it remains right indefinitely.

There are specific reasons to move to a full framework, and there are more common reasons that people offer which do not survive examination. Knowing the difference saves a month.

## The Reasons That Are Real

**You need public pages to be found.** A marketing site, a blog, public listings, documentation. A single-page application makes these slower and more fragile for search engines, and server rendering is the durable fix. This is the most common genuine reason by a wide margin.

**You need substantial server-side logic.** Not one or two functions, which any platform provides, but a real backend: integrations, scheduled work, business rules that must not run in a browser. A framework with server routes gives you one codebase instead of two.

**You have outgrown client-only data fetching.** Every screen waiting on requests from the browser, with loading states everywhere, when the data could be fetched on the server and sent with the page.

**The first meaningful paint is too slow and cannot be fixed otherwise.** Genuine on content-heavy products, usually solvable by other means on an application behind a login.

## The Reasons That Are Not

**"It is more professional."** Nobody buys a framework. Customers experience speed, reliability and whether the product does what they need.

**"We might need it later."** Later is when the reason will be specific and the migration will be justified by it.

**"A developer told me to."** Sometimes correct. Ask what problem it solves and whether that problem is one you currently have.

**"Performance is bad."** Frequently missing indexes, N+1 queries, oversized images or no caching. All of those travel with you.

A product behind a login, used by people who are already customers, with no public pages that need to rank, has very little to gain.

## What Transfers and What Does Not

The reassuring part: most of the work comes across.

React components transfer almost unchanged. Your Supabase schema, policies and functions are untouched. Business logic moves with modest adjustment. Styling transfers.

What needs real work: routing conventions differ; data fetching moves from browser-side calls to server components or loaders, which is the largest single piece; environment variables are named and exposed differently, and getting this wrong is how a secret ends up in a bundle; authentication moves to a server-aware pattern with cookies rather than browser storage, which is an improvement and is work; and your build and deployment configuration is replaced.

For a typical Bolt application of twenty to forty components, this is one to three weeks depending on how much data fetching is spread through the interface.

## The Order That Keeps the Product Running

Do not stop feature work for a month. Migrate in stages.

Start with the public pages — marketing, blog, anything that needs to rank — as a new application on the same domain, with the existing application still serving everything behind the login. This delivers the main benefit immediately and touches nothing customers depend on.

Then move the application's screens one at a time, beginning with the simplest and the least used, verifying each before the next. Both applications share the same database throughout, so there is no data migration at all.

Then authentication, which is the step with user-visible effect because sessions end. Do it at a quiet hour with notice.

Then remove the old application, once nothing routes to it.

At every stage the product works. If the migration stalls — and they do, when something more urgent appears — you are left in a working state rather than half-way through a rewrite.

## The Middle Path Worth Considering

Before committing to a migration, consider whether you need two applications rather than one.

A statically generated marketing site and blog, entirely separate, on the same domain at the root, with the existing Bolt application served under `/app`. The public pages get server-rendered HTML, speed and indexability; the application stays exactly as it is.

This is a day of work rather than three weeks, it addresses the most common genuine reason for migrating, and it leaves the application migration as a decision you can make later on its own merits. For a large share of the founders who ask about this, it is the right answer.

## What Changes About Working With AI Tools

One consequence of migrating is rarely mentioned and matters for products built this way: the tools behave differently against a full framework than against the application they generated.

Bolt and its equivalents are at their best producing a self-contained application from scratch. Against an established framework codebase with server components, route conventions and its own patterns, a general assistant such as Cursor or Claude Code is the better fit — it reads the existing code, follows the conventions it finds, and makes contained changes.

So a migration is usually also a change in how you work: from describing features to a builder that generates them, to editing a codebase with an assistant that helps. That is a real shift, and founders who are not developers sometimes find it harder rather than easier, which is worth knowing before committing.

Two things make the transition comfortable. A conventions file describing your patterns, which matters more in a framework project because there are more decisions to be consistent about. And a working test suite, even a small one, because an assistant editing a larger codebase benefits enormously from being able to check whether it broke something.

If neither of those appeals, that is itself an argument for the middle path: keep the application as it is, and solve the specific problem you actually have.

## Choosing the Framework, Briefly

If a migration is genuinely warranted, the choice among the serious options matters less than founders expect, and the decision can be made in an afternoon.

**Next.js** is the default for React applications, which is what Bolt produces, and has the largest ecosystem and the most material for coding assistants to have learned from. That last point is not trivial in a product built this way — an assistant writes better Next.js than it writes almost anything else, simply because there is more of it in the world.

**Remix** has a cleaner data model in several respects and a smaller community.

**Astro** is excellent when most of your site is content with islands of interactivity, which describes a marketing-heavy product well and an application poorly.

**SvelteKit** and others are fine and mean discarding your React components, which is most of what transfers.

For a Bolt application with a real reason to move, Next.js is the sensible default and the burden of argument is on any alternative. The one genuine fork is Astro for a product that is mostly content — and in that case, the day-long option of a separate static marketing site achieves the same thing without touching the application at all.

## Set a Budget and a Stopping Rule

Migrations of this kind have a characteristic failure: they take twice as long as planned, feature work stops, and three months later the product has not changed for customers while the founder has been busy every day.

Two protections, agreed with yourself before starting.

**A time budget with a review point.** Three weeks, with an honest assessment at the end of week two. If the public pages are done and the application screens are going slowly, stopping there is a legitimate outcome — you have the benefit that justified the work, and the rest can wait indefinitely.

**A rule that the product keeps shipping.** At least one customer-visible improvement a week during the migration, however small. It keeps you in contact with the people paying you and it prevents the quiet slide into a quarter spent on infrastructure.

The staged approach described above makes both possible, because there is no point at which the migration must be completed to have been worthwhile. That is the property to insist on in any plan somebody proposes to you: if the answer to "what happens if we stop half-way" is anything other than "we keep the part we finished", the plan is a rewrite wearing a migration's clothes, and rewrites are where small products go to lose a year.

## Setting This Up

For a product with a real reason to migrate this is typically one to three weeks: the reason stated specifically and tested against the alternatives, public pages moved first as a separate application on the same domain, screens migrated one at a time from least to most used with both applications sharing the database, data fetching moved to the server, environment variables renamed with the bundle checked for secrets, authentication migrated to a cookie-based server-aware pattern at a quiet hour with notice, the old application retired once nothing routes to it, and the whole thing kept working at every stage.

LaunchStudio does this migration, and also tells founders when the day-long alternative is sufficient — which it often is. The engineers are Manifera's — eleven years, 160+ projects, from Amsterdam and Ho Chi Minh City.

[Tell us what you are trying to fix](https://launchstudio.eu/en/#contact) and we will tell you whether a migration is the way to fix it.

## Real example

### Three Weeks, Then One Day

Ties Grootveld built Aanbestedingsradar with Bolt: a service that monitors Dutch public tender publications and alerts 90 subscribing companies to relevant opportunities, €79 a month.

He had been told repeatedly that he should move to Next.js. His stated reasons were that his marketing pages did not rank and that the product felt slow.

The assessment separated the two. The marketing pages genuinely needed server rendering — they were a single-page application serving an empty document, which is why none of his eleven articles were indexed. The application's slowness was something else entirely: the tender list fetched every row a company had ever been matched with and paginated in the browser, which for his largest subscriber was 41,000 rows.

One business day, not three weeks: the marketing site and blog rebuilt as a statically generated application serving real HTML, deployed at the domain root, with the existing Bolt application moved to `/app` and excluded from indexing; canonical URLs and a sitemap added; the tender list converted to cursor pagination with an index on the matching table, taking the largest subscriber's list from 9 seconds to 210 milliseconds; and a note written recording that a full framework migration remains available if server-side logic ever justifies it.

**Result:** nine of eleven articles indexed within a month and organic enquiries began arriving for the first time. The application's speed problem, which the migration would not have fixed, was resolved by an index and a query change. Ties has not migrated the application and, two years on, has not needed to.

> *"Everyone told me the framework was the problem. The marketing pages did need fixing. The slow screen was a query that fetched forty-one thousand rows, and it would have been just as slow in Next.js."*
> — **Ties Grootveld, Founder, Aanbestedingsradar (Den Haag)**

**Cost & Timeline:** €2,400 (static marketing application with server-rendered HTML, application relocation and index exclusion, canonical URLs and sitemap, cursor pagination with indexing, documented migration option) — completed in 1 business day.

## Frequently Asked Questions

### When should a Bolt app move to Next.js?

When you need public pages to rank, substantial server-side logic, or server-side data fetching. Not because a framework sounds more professional or because something is slow for reasons that would follow you.

### What transfers in the migration?

Components, business logic, styling and your entire Supabase schema and policies. Routing, data fetching, environment variables, authentication and deployment configuration all need work.

### How long does it take?

One to three weeks for a typical twenty-to-forty component application, most of it moving data fetching from the browser to the server.

### Can I migrate without stopping the product?

Yes, and you should. Move public pages first, then screens one at a time from least used to most, sharing the same database throughout, with authentication last.

### Is there a cheaper alternative?

Often. A separate statically generated marketing site at the domain root with the existing application under `/app` is a day of work and addresses the most common genuine reason for migrating.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "When should a Bolt app move to a full framework?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "When public pages must rank, substantial server-side logic is needed, or data should be fetched on the server — not for professionalism or unexplained slowness."
      }
    },
    {
      "@type": "Question",
      "name": "What transfers when migrating from Bolt to Next.js?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Components, business logic, styling and the whole Supabase schema. Routing, data fetching, environment variables, auth and deployment need rework."
      }
    },
    {
      "@type": "Question",
      "name": "How long does a Bolt to Next.js migration take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "One to three weeks for twenty to forty components, dominated by moving data fetching from browser to server."
      }
    },
    {
      "@type": "Question",
      "name": "Can the migration happen without downtime?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — public pages first, then screens one at a time sharing the same database, with authentication migrated last."
      }
    },
    {
      "@type": "Question",
      "name": "Is there a cheaper alternative to migrating?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Often: a separate static marketing site at the domain root with the existing app under /app, which is a day of work."
      }
    }
  ]
}
</script>
