---
Title: "Row Level Security Performance in Supabase"
Keywords: supabase rls performance, slow rls policies, auth.uid select wrapper, supabase custom claims rls, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Row Level Security Performance in Supabase

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Row Level Security Performance in Supabase",
  "description": "Row Level Security is the foundation of data protection in Supabase apps, but badly written policies can make queries dramatically slower as data grows. This guide explains how policies are evaluated, why function calls and joins inside policies are expensive, and the techniques that keep RLS fast: wrapping auth functions in subselects, indexing policy columns, specifying roles, security definer helpers, custom claims and matching filters in queries.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-21",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/row-level-security-performance-in-supabase" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" },
    { "@type": "CreativeWork", "name": "Supabase: RLS performance recommendations", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security#rls-performance-recommendations" },
    { "@type": "CreativeWork", "name": "Supabase: Custom access token hook", "url": "https://supabase.com/docs/guides/auth/auth-hooks/custom-access-token-hook" },
    { "@type": "CreativeWork", "name": "PostgreSQL: Row security policies", "url": "https://www.postgresql.org/docs/current/ddl-rowsecurity.html" }
  ]
}
</script>

Row Level Security is what makes Supabase apps safe. Because the browser talks to the database directly, policies on each table decide which rows each user can read, insert, update and delete. Founders who have read about Supabase security rightly put a lot of effort into writing good policies.

Then the app grows, and something unexpected happens: pages that were instant become slow. Lists of a few hundred items take seconds. Dashboard queries time out. Investigation often points to the policies themselves. A policy that checks team membership with a subquery, calls a function for every row or joins several tables can turn a simple query into thousands of hidden operations.

The good news is that secure policies do not have to be slow. A handful of well-documented techniques keep RLS fast without weakening protection. This guide explains them.

## Key Takeaways

- **Policies are evaluated as part of every query,** often for every row considered. Expensive conditions multiply with table size.
- **Wrap functions such as `auth.uid()` and `auth.jwt()` in a subselect,** so Postgres can evaluate them once per query instead of per row.
- **Index every column used in policies,** especially `user_id`, `organisation_id` and membership foreign keys.
- **Avoid joins and complex subqueries inside policies;** use security definer helper functions or custom JWT claims for membership and roles.
- **Add filters to client queries that match the policy,** and specify the roles a policy applies to.

## How Policies Are Evaluated

When a query runs on a table with RLS enabled, Postgres adds the policy conditions to it, roughly as if they were extra `WHERE` clauses. For a select policy like:

```sql
create policy "members can read projects"
on projects for select
using (
  exists (
    select 1 from memberships
    where memberships.organisation_id = projects.organisation_id
      and memberships.user_id = auth.uid()
  )
);
```

a query such as `select * from projects` effectively becomes "select projects where a matching membership exists for the current user". If Postgres cannot use indexes efficiently, it may check that condition for every project in the table. With a thousand rows, nobody notices. With a million, it hurts.

## Technique 1: Wrap Auth Functions in a Subselect

Supabase's own performance recommendations highlight this simple change. Functions such as `auth.uid()` may be evaluated for each row. Wrapping them in a subselect allows Postgres to evaluate them once and reuse the result:

```sql
-- Slower
using (user_id = auth.uid())

-- Faster
using (user_id = (select auth.uid()))
```

The same applies to `auth.jwt()` and to your own stable functions. It is a small edit with often dramatic results on large tables.

## Technique 2: Index Policy Columns

Every column referenced in a policy should usually be indexed:

- `user_id` on tables where users own rows
- `organisation_id` on almost every table in a multi-tenant app
- Foreign keys used in membership checks, such as `memberships(user_id, organisation_id)`

Postgres does not index foreign keys automatically. AI-generated schemas rarely add these indexes, and missing ones are the most common cause of slow policies.

## Technique 3: Specify Roles

Policies can be limited to specific roles with `to authenticated` or `to anon`. Without it, a policy may be evaluated for requests where it can never pass, for example anonymous requests on a table only authenticated users should see. Specifying the role avoids unnecessary work and makes intent explicit:

```sql
create policy "users read own profile"
on profiles for select
to authenticated
using (id = (select auth.uid()));
```

## Technique 4: Avoid Joins Inside Policies

Policies that join several tables to determine access, such as project to team to organisation to membership, are expensive and hard to reason about. Alternatives:

**Denormalise the tenant key.** Store `organisation_id` directly on every tenant-owned table, even if it can be derived through relations. Policies then check one indexed column instead of following a chain.

**Use a security definer helper function.** A function that returns the organisations or teams the current user belongs to, marked `security definer` and `stable`, with a fixed `search_path`, can be used in policies:

```sql
using (organisation_id in (select private.user_organisations()))
```

Security definer functions run with the privileges of their owner, so they bypass RLS on the membership table, which avoids recursive policy evaluation. Place them in a schema not exposed through the API, set `search_path` explicitly and keep them simple, because they are security-sensitive.

## Technique 5: Custom Claims in the JWT

For data that rarely changes during a session, such as the user's organisation and role, you can add custom claims to the user's access token with a custom access token hook in Supabase Auth. Policies then read claims from the token instead of querying membership tables:

```sql
using (organisation_id = ((select auth.jwt()) ->> 'org_id')::uuid)
```

This is very fast. The trade-off is staleness: claims update only when the token is refreshed. If a user is removed from an organisation, their token may remain valid until it expires. For sensitive changes, combine claims with checks against the database, or force token refresh when memberships change.

## Technique 6: Add Matching Filters to Queries

Even with good policies, queries from the client should include filters that match the policy, such as filtering by `organisation_id`. This helps Postgres use indexes before evaluating policies, rather than scanning everything and letting the policy discard most rows.

```typescript
const { data } = await supabase
  .from("projects")
  .select("id, name, status")
  .eq("organisation_id", currentOrgId)
  .order("updated_at", { ascending: false })
  .limit(50);
```

The filter does not replace the policy. Security still comes from RLS; the filter only helps performance.

## Technique 7: Keep Policies Simple and Separate

- **Write separate policies per operation:** select, insert, update and delete often need different rules.
- **Avoid `for all` policies** that mix concerns and are hard to optimise.
- **Use `with check` for inserts and updates** to ensure users cannot write rows for other organisations.
- **Prefer simple equality checks** on indexed columns over complex expressions.

## Views and Security

Views can simplify queries, but by default in Postgres, views run with the privileges of their owner, which can bypass RLS on underlying tables. In recent Postgres versions, you can create views with `security_invoker = true`, so the querying user's permissions and policies apply. When using views in Supabase for performance or convenience, make sure they do not accidentally expose data.

## Common Multi-Tenant Policy Patterns

Most B2B SaaS apps on Supabase end up with a few recurring patterns. Using consistent, efficient versions of them across all tables makes policies easier to review and keeps performance predictable:

| Pattern | Efficient form | Notes |
| --- | --- | --- |
| User owns row | `user_id = (select auth.uid())` | Index `user_id` |
| Member of organisation | `organisation_id in (select private.user_organisations())` | Helper returns user's organisations; index `organisation_id` |
| Role within organisation | `private.has_role(organisation_id, 'admin')` | Security definer helper, used only where needed |
| Organisation from claim | `organisation_id = ((select auth.jwt()) ->> 'org_id')::uuid` | Fastest; mind token staleness |
| Shared with specific users | `exists (select 1 from shares where shares.item_id = items.id and shares.user_id = (select auth.uid()))` | Index `shares(item_id, user_id)` |
| Public rows | `is_public = true` | Combine with role restrictions for writes |

Document the chosen patterns in the repository and in project instructions for AI tools. When every table follows the same few patterns, reviewing a new policy takes seconds, and AI-generated policies are far more likely to be both correct and fast.

## Measuring Policy Performance

To see the real cost of policies:

1. **Run queries as an authenticated user** in a staging environment, with realistic data volumes, by setting the role and JWT claims in the SQL editor or testing through the API.
2. **Use `EXPLAIN ANALYZE`** to see how the policy conditions are executed and whether indexes are used.
3. **Compare before and after** each change.
4. **Check query statistics** in Supabase's performance reports for the slowest and most frequent queries.

Our guide on [finding and fixing slow Supabase queries](https://launchstudio.eu/en/blog/slow-supabase-queries-how-to-find-and-fix-them) covers the general measurement process.

## Insert and Update Policies Deserve Attention Too

Most performance discussions focus on select policies, but `with check` conditions on inserts and updates run for every written row as well. Bulk imports, such as uploading a CSV of 20,000 contacts, can become slow if each row triggers an expensive membership lookup. The same techniques apply: subselects for auth functions, indexed columns and simple helper functions. For very large imports, consider a dedicated server-side import function that validates the user's access once, then inserts rows in batches within the verified organisation, rather than evaluating complex checks per row from the client.

## Performance Without Weakening Security

Under performance pressure, it is tempting to "fix" slow policies by loosening them, using the service role key in more places or moving checks to the frontend. Each of these trades performance for risk. The techniques above keep the same rules and make them fast. When rewriting policies, write tests first: for each table and role, confirm which rows users can and cannot access. Then optimise, and run the tests again.

Our article on the [Supabase RLS audit and the policy mistakes we find most](https://launchstudio.eu/en/blog/supabase-rls-audit-the-policy-mistakes-we-find-most) covers the security side.

## Common Mistakes in AI-Built Apps

**`auth.uid()` called per row** without a subselect.

**Missing indexes** on `organisation_id`, `user_id` and membership tables.

**Multi-table joins in policies.**

**Policies on membership tables that query themselves,** causing recursion or very slow evaluation.

**Loosening policies to fix performance.**

**Views that bypass RLS** unintentionally.

## How LaunchStudio Helps

LaunchStudio optimises Row Level Security in AI-built Supabase apps: measuring policy cost with realistic data, rewriting policies with subselects and role specifications, adding indexes, denormalising tenant keys, introducing safe security definer helpers or custom claims where appropriate, securing views and adding access tests that guarantee security stays intact.

The **Launch Ready** package (€800-€3,500) covers RLS review and optimisation along with security hardening and deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, with deep PostgreSQL experience on enterprise systems. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Secure Ticketing Tool That Became Too Slow to Use

Lars Willemsen built Servicedesk Lite with Lovable and Supabase: a helpdesk for small IT service providers, where engineers handle tickets for many client organisations. Lars had followed security advice carefully, with policies on every table. As one customer grew to around 400,000 tickets, the ticket list took over six seconds to load and sometimes timed out.

Analysis showed that the select policy on tickets joined tickets to client organisations, to teams and to team memberships to decide whether the current engineer could see a ticket, calling `auth.uid()` inside the join without a subselect. There were no indexes on the columns used in the join. The memberships table had its own policy that queried memberships again, causing heavy recursive evaluation. The frontend queried tickets without filters and sorted them on an unindexed column. Under pressure from the customer, a freelancer had suggested switching the list to the service role key, which would have removed tenant isolation entirely.

LaunchStudio first wrote access tests for every role and table. Then `organisation_id` and `team_id` were added directly to tickets and backfilled, policies were rewritten to check team membership through a small security definer function in a private schema with a fixed search path, `auth.uid()` was wrapped in subselects and policies were limited to the authenticated role. Composite indexes were added for team, status and update time, the frontend added matching filters and keyset pagination, and the memberships policy was simplified to avoid recursion. Access tests ran before and after each change.

**Result:** The ticket list now loads in about 200 milliseconds for the largest customer, with identical access rules verified by tests. The service role shortcut was never needed, and database CPU during office hours dropped by around 60%.

> *"I thought I had to choose between secure and fast. It turned out my policies were secure and badly written, and they could be both."*
> - **Lars Willemsen, Founder, Servicedesk Lite (Amersfoort)**

**Cost & Timeline:** €3,000 (Launch Ready package: access tests, policy rewrite, denormalised tenant keys, helper function, indexes and query changes) - completed in 8 business days.

## Frequently Asked Questions

### Does Row Level Security make Supabase slow?

Well-written policies add little overhead. Slowness usually comes from specific patterns: auth functions evaluated per row, missing indexes, joins inside policies and recursive policies on membership tables. Fixing those patterns typically restores fast queries without weakening security.

### Why should I wrap auth.uid() in a select?

Wrapping `auth.uid()` as `(select auth.uid())` allows Postgres to evaluate it once per query and reuse the value, instead of potentially calling it for every row. Supabase recommends this pattern in its RLS performance guidance.

### Are custom JWT claims safe for RLS?

They are fast and convenient for values such as organisation and role, but they only update when the token refreshes. For sensitive changes, such as removing a user from an organisation, combine claims with database checks or force token refresh so access changes take effect promptly.

### How does Manifera's experience help with RLS performance?

Manifera has optimised PostgreSQL access control and performance on enterprise systems for 11+ years. LaunchStudio applies that experience to make policies fast while proving, with tests, that the same access rules still hold.

### Does RLS performance affect SEO or AI visibility?

For public pages served from your database, yes, because slow queries slow down pages that search engines and AI crawlers access. For logged-in features, performance affects user satisfaction and retention, which influence reviews and recommendations.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does Row Level Security make Supabase slow?",
      "acceptedAnswer": { "@type": "Answer", "text": "Well-written policies add little overhead; slowness comes from per-row auth calls, missing indexes, joins and recursion." }
    },
    {
      "@type": "Question",
      "name": "Why should I wrap auth.uid() in a select?",
      "acceptedAnswer": { "@type": "Answer", "text": "So Postgres evaluates it once per query instead of per row, as Supabase recommends." }
    },
    {
      "@type": "Question",
      "name": "Are custom JWT claims safe for RLS?",
      "acceptedAnswer": { "@type": "Answer", "text": "Fast but stale until token refresh; combine with database checks or forced refresh for sensitive changes." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with RLS performance?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has optimised enterprise PostgreSQL access control for 11+ years, making policies fast with tests proving rules hold." }
    },
    {
      "@type": "Question",
      "name": "Does RLS performance affect SEO or AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "For public pages yes; for logged-in features it affects satisfaction and reviews." }
    }
  ]
}
</script>
