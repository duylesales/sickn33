---
Title: "Prisma or Drizzle in an AI-Written Next.js App?"
Keywords: prisma vs drizzle, drizzle orm supabase, prisma supabase rls, orm for nextjs ai app, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Prisma or Drizzle in an AI-Written Next.js App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Prisma or Drizzle in an AI-Written Next.js App?",
  "description": "AI coding tools often add Prisma or Drizzle to Next.js apps built with v0, Cursor or Claude Code. This guide compares the two ORMs on developer experience, migrations, performance in serverless environments and type safety, and explains the most important security point: server-side ORMs usually bypass Supabase Row Level Security, so authorisation must be enforced deliberately.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-29",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/prisma-or-drizzle-in-an-ai-written-nextjs-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "Prisma ORM documentation", "url": "https://www.prisma.io/docs" },
    { "@type": "CreativeWork", "name": "Drizzle ORM documentation", "url": "https://orm.drizzle.team/docs/overview" },
    { "@type": "CreativeWork", "name": "Supabase: Connecting with Prisma and Drizzle", "url": "https://supabase.com/docs/guides/database/connecting-to-postgres" },
    { "@type": "CreativeWork", "name": "Supabase Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" }
  ]
}
</script>

Founders who build with v0, Cursor or Claude Code often discover a new layer in their project after a few weeks: an ORM. The agent decided that writing raw SQL was messy, installed Prisma or Drizzle, generated a schema and started using it in server actions and API routes. Sometimes it did this alongside the Supabase client already in the project, so the app now talks to the same database in two different ways.

Object-relational mappers, or ORMs, are valuable. They make database access type-safe, readable and easier to maintain. Prisma and Drizzle are the two most popular choices in the TypeScript world, and both work well with Next.js and Postgres databases such as Supabase. The choice between them matters less than one detail that AI-generated code frequently gets wrong: how authorisation works when the ORM connects to your database.

This guide compares the two and explains how to use either safely.

## Key Takeaways

- **Prisma emphasises a schema-first workflow** with its own schema language, a generated client and mature migration tooling.
- **Drizzle emphasises being close to SQL,** with schemas defined in TypeScript, a lightweight runtime and good fit for serverless and edge environments.
- **Both are solid choices.** Pick one, use it consistently and avoid mixing ORMs and raw clients without a clear reason.
- **Server-side ORMs typically connect with a database role that bypasses Row Level Security.** Authorisation must then be enforced in your server code, or the connection must be configured to respect RLS.
- **Migrations must be the single source of truth** for schema changes, whichever ORM you choose.

## What an ORM Does

An ORM lets your code work with database tables as typed objects. Instead of writing SQL strings, you write something like `db.select().from(projects).where(eq(projects.ownerId, userId))` in Drizzle or `prisma.project.findMany({ where: { ownerId: userId } })` in Prisma. Benefits:

- **Type safety:** your editor knows the columns and their types, catching mistakes before runtime.
- **Readability:** queries are expressed in the same language as the rest of the code.
- **Migrations:** schema changes are tracked as files and applied consistently.
- **Productivity:** AI tools write correct ORM queries more reliably when types guide them.

## Prisma at a Glance

Prisma uses a dedicated schema file, `schema.prisma`, where you define models and relations. From it, Prisma generates a typed client and migration files.

**Strengths:**

- Very approachable schema language and documentation
- Mature migration workflow with `prisma migrate`
- Rich relation queries, such as including related records in one call
- Large community, many examples and broad AI familiarity
- Additional products for connection pooling and caching

**Points to consider:**

- Historically, Prisma relied on a separate query engine binary, which added size and cold-start overhead in serverless environments. Recent versions have worked to reduce this, so check current documentation for your deployment target.
- The schema language is Prisma-specific, adding a layer between you and SQL.
- Complex SQL features sometimes require raw queries.

## Drizzle at a Glance

Drizzle defines schemas in TypeScript and offers a query builder that closely mirrors SQL, plus a relational query API. Its migration tool, Drizzle Kit, generates SQL migration files from schema changes.

**Strengths:**

- Lightweight runtime with no separate engine, suiting serverless and edge functions
- SQL-like API, easy to reason about for anyone who knows SQL
- Schema in TypeScript, so no extra language
- Good support for Postgres features
- Generated migrations are plain SQL, easy to review

**Points to consider:**

- Younger ecosystem than Prisma, though growing fast
- The SQL-like style may feel less abstracted to developers who prefer object-style queries
- Relation queries and migrations require some understanding of SQL concepts

## Comparison

| Factor | Prisma | Drizzle |
| --- | --- | --- |
| Schema definition | Prisma schema language | TypeScript |
| Query style | Object-style API | SQL-like builder plus relational API |
| Migrations | Prisma Migrate | Drizzle Kit, plain SQL files |
| Runtime weight | Heavier historically, improving | Lightweight |
| Serverless and edge | Supported, check configuration | Well suited |
| Learning curve | Gentle for beginners | Gentle for those who know SQL |
| Ecosystem and examples | Very large | Large and growing |
| AI tool familiarity | Very high | High |

For most AI-built Next.js apps, either works well. If the project already uses one consistently, keep it. If starting fresh and deploying heavily on serverless or edge functions, Drizzle's lightweight runtime is appealing. If the team values Prisma's schema readability and migration tooling, Prisma is a sound choice.

## The Security Point That Matters Most

Supabase's security model relies heavily on Row Level Security. When the browser queries Supabase with the public key and a user's session, Postgres applies RLS policies that decide which rows that user can access. That is why a Lovable app can safely query the database directly from the browser, provided the policies are right.

ORMs work differently. Prisma and Drizzle run on the server and connect to Postgres with a database connection string. In many setups, that connection uses a privileged role, such as the `postgres` role or another role that bypasses RLS. Every query through the ORM then ignores your policies entirely.

This is fine if your server code enforces authorisation properly: every query filters by the current user's ID or organisation, and every mutation checks ownership. It is dangerous if developers, or AI tools, assume that RLS still protects them.

Typical failure: a server action written by an AI agent uses `db.select().from(invoices).where(eq(invoices.id, invoiceId))` to load an invoice by ID from a URL parameter. In the browser-client version of the app, RLS would have blocked access to other users' invoices. Through the ORM with a privileged connection, any logged-in user can load any invoice by changing the ID.

## Two Safe Patterns

**Pattern 1: Enforce authorisation in server code.**

- Every query includes the current user's or organisation's scope, for example `where ownerId = currentUser.id`.
- Use helper functions that require a scope, such as `getInvoiceForUser(userId, invoiceId)`, so a query without a scope is hard to write.
- Write negative authorisation tests for every route and server action.
- Keep RLS enabled on tables as a second line of defence for any browser access.

**Pattern 2: Make the ORM connection respect RLS.**

- Connect with a role that does not bypass RLS.
- Set the user context for each request, for example by setting the request's JWT claims in a transaction before running queries, so policies can evaluate `auth.uid()`.
- This approach requires care with connection pooling, because session settings must not leak between requests.

Pattern 1 is simpler and more common. Pattern 2 provides defence in depth but requires a correct implementation. In either case, document which approach the project uses, so future AI sessions follow it.

## Writing Scoped Helpers That AI Tools Will Reuse

The most effective defence against unscoped queries is to make the safe way the easy way. Instead of letting each server action query tables directly, create a small data access module with functions that always take the current user's context:

- `listInvoices(ctx)` returns only invoices for `ctx.organisationId`.
- `getInvoice(ctx, invoiceId)` returns the invoice only if it belongs to `ctx.organisationId`, otherwise nothing.
- `updateInvoiceStatus(ctx, invoiceId, status)` checks ownership and the user's role before updating.

The context object is created once per request from the authenticated session, never from parameters supplied by the client. Server actions then call these helpers instead of the ORM directly.

This structure has a useful side effect with AI coding tools. When an agent adds a new feature, it tends to reuse existing helpers it finds in the codebase. A clear data access module with scoped functions and a short comment explaining the rule nudges the agent towards safe patterns, while a codebase full of direct ORM calls nudges it towards more of the same. Add a line to your project instructions, such as "all database access goes through the data access module; never query tables directly from server actions", and review new code against it.

## Avoid Mixing Access Paths Without a Plan

AI-built apps sometimes use the Supabase JavaScript client in the browser for some features, the Supabase client on the server for others and an ORM for the rest. Each path has different authorisation behaviour:

| Access path | RLS applied? |
| --- | --- |
| Supabase client in browser with user session | Yes |
| Supabase client on server with user session | Yes |
| Supabase client on server with service role key | No |
| ORM with privileged connection string | No, typically |
| ORM with restricted role and user claims set | Yes, if configured correctly |

Choose deliberately, document it and review new code against the chosen pattern.

## Migrations: One Source of Truth

Whichever ORM you use, schema changes must flow through migrations:

- **Never edit production schemas manually** in the Supabase dashboard while also using ORM migrations; the two drift apart.
- **Review generated migrations** before applying them, especially for destructive changes such as dropping or renaming columns.
- **Apply migrations through your deployment pipeline,** not from laptops.
- **Keep RLS policies, functions and triggers in migrations too,** since ORMs focus on tables and may not manage these by default. Supabase migrations can hold the SQL for policies alongside ORM-generated table changes.

Our guide on [zero-downtime database migrations in Supabase](https://launchstudio.eu/en/blog/zero-downtime-database-migrations-in-supabase) explains safe migration patterns.

## Connection Pooling in Serverless

Serverless functions can open many database connections at once, which can exhaust Postgres connection limits. When using an ORM with Supabase in serverless environments, connect through Supabase's connection pooler using the appropriate connection string and settings recommended for your ORM. Our article on [Supabase connection pooling and limits](https://launchstudio.eu/en/blog/supabase-connection-pooling-and-limits-explained) covers this in detail.

## Common Mistakes

**Assuming RLS protects ORM queries.** It usually does not with privileged connections.

**Two ORMs, or ORM plus raw client everywhere.** Inconsistent behaviour and duplicated logic.

**Schema edited in the dashboard and in migrations.** Production and code disagree.

**Direct connections from serverless without pooling.** Connection errors under load.

**Selecting full rows by default.** Leaking columns, such as internal notes or tokens, into API responses. Select only the fields you need.

## How LaunchStudio Helps

LaunchStudio reviews database access in AI-written Next.js apps: identifying every access path, choosing and documenting an authorisation pattern, adding scoped query helpers and negative authorisation tests, aligning migrations with Supabase policies, configuring connection pooling and cleaning up mixed ORM and client usage.

The **Launch Ready** package (€800-€3,500) covers the security review and fixes along with deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, with deep experience in PostgreSQL and data access layers for enterprise systems. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Invoice Portal Where Prisma Ignored Every Policy

Ahmed Benali built Factuurportaal with v0, Next.js and Supabase: a portal where freelancers and small agencies send invoices to clients, and clients view and pay them online. He had carefully written Row Level Security policies after reading about Supabase security. Later, while adding reporting features with Cursor, the agent installed Prisma and moved most data access into server actions.

A client discovered by accident that changing the invoice number in a URL showed another freelancer's invoice to a different client. Investigation showed that Prisma connected using the `postgres` role from the default connection string, which bypassed every RLS policy Ahmed had written. Of 23 server actions and API routes using Prisma, 14 loaded or updated records by ID without checking ownership. The app also used the Supabase client in the browser for some screens, schema changes had been made both in the Supabase dashboard and through Prisma migrations, and serverless functions opened direct connections that failed under month-end invoice peaks.

LaunchStudio documented every data access path and chose a clear pattern: Prisma for server-side access with authorisation enforced in code through scoped helper functions, and the Supabase client in the browser only for read access protected by RLS. All 23 server actions were rewritten to use helpers that required the user's organisation scope, and negative authorisation tests covered each one. The schema drift was resolved into a single migration history, RLS policies were kept in SQL migrations as a second layer, Prisma connected through the Supabase pooler with appropriate settings, and project instructions told Cursor which pattern to follow.

**Result:** The exposure was closed within a day, and the full cleanup took nine business days. Month-end connection errors disappeared, and the new authorisation tests caught two later AI-generated changes that would have reintroduced unscoped queries.

> *"I had written all the right policies. I just didn't know that the code doing most of the work wasn't using them."*
> - **Ahmed Benali, Founder, Factuurportaal (Den Haag)**

**Cost & Timeline:** €3,500 (Launch Ready package: access path review, scoped query helpers, authorisation tests, migration cleanup and connection pooling) - completed in 9 business days.

## Frequently Asked Questions

### Should I use Prisma or Drizzle for my Next.js app?

Both are good choices. Drizzle is lightweight and SQL-like, which suits serverless and edge deployments. Prisma offers a readable schema language and mature migrations. If your project already uses one consistently, keep it. Consistency matters more than the choice.

### Does Supabase Row Level Security apply to Prisma or Drizzle queries?

Usually not when they connect with a privileged role, such as the default `postgres` role. In that case, your server code must enforce authorisation. RLS can apply if you connect with a restricted role and set user claims per request, but that requires careful implementation.

### Can I use the Supabase client and an ORM in the same app?

Yes, but deliberately. A common pattern is the Supabase client in the browser for reads protected by RLS, and an ORM on the server with authorisation enforced in code. Document the pattern and review new code against it.

### How does Manifera's experience help with ORM and database design?

Manifera has designed PostgreSQL data layers for enterprise systems for 11+ years. LaunchStudio applies that experience to choose consistent access patterns, enforce authorisation correctly and keep migrations reliable in AI-written codebases.

### Does my ORM choice affect performance and visibility?

Indirectly. Efficient queries, proper pooling and selecting only needed fields keep pages fast, which supports user experience, search rankings and reliable access for AI crawlers to your public content.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should I use Prisma or Drizzle for my Next.js app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Both are good. Drizzle is lightweight and SQL-like; Prisma has a readable schema and mature migrations. Consistency matters most." }
    },
    {
      "@type": "Question",
      "name": "Does Supabase Row Level Security apply to Prisma or Drizzle queries?",
      "acceptedAnswer": { "@type": "Answer", "text": "Usually not with a privileged role, so server code must enforce authorisation, unless a restricted role with per-request claims is configured." }
    },
    {
      "@type": "Question",
      "name": "Can I use the Supabase client and an ORM in the same app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, deliberately: browser client for RLS-protected reads and server ORM with code-enforced authorisation, documented and reviewed." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with ORM and database design?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has designed PostgreSQL data layers for 11+ years, and LaunchStudio enforces consistent access patterns and authorisation." }
    },
    {
      "@type": "Question",
      "name": "Does my ORM choice affect performance and visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirectly; efficient queries and pooling keep pages fast for users, search engines and AI crawlers." }
    }
  ]
}
</script>
