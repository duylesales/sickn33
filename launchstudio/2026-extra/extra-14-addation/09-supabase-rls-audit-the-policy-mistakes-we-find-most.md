---
Title: "Supabase RLS Audit: The Policy Mistakes We Find Most"
Keywords: supabase rls audit, row level security mistakes, supabase policies, supabase security review, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Supabase RLS Audit: The Policy Mistakes We Find Most

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Supabase RLS Audit: The Policy Mistakes We Find Most",
  "description": "A technical walkthrough of a Supabase RLS audit: the seven Row Level Security mistakes found most often in AI-built apps, with example policies, how to test them and how to fix them safely.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-17",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/supabase-rls-audit-the-policy-mistakes-we-find-most" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" },
    { "@type": "CreativeWork", "name": "PostgreSQL: Row Security Policies", "url": "https://www.postgresql.org/docs/current/ddl-rowsecurity.html" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A01 Broken Access Control", "url": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/" },
    { "@type": "CreativeWork", "name": "Veracode 2025 GenAI Code Security Report", "url": "https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/" },
    { "@type": "CreativeWork", "name": "OWASP Authorization Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html" }
  ]
}
</script>

Row Level Security is a short feature to describe and a long one to get right. In a Supabase app, the browser queries your database directly with a public key, and RLS policies are the only thing between one user and another user's data. When LaunchStudio runs a Supabase RLS audit on an app built with Lovable, Bolt or Cursor, we almost always find at least one of the seven mistakes below.

This is a technical article. If you write or review SQL, you can use it as a checklist on your own project.

## Key Takeaways

- **In Supabase, Row Level Security is the only barrier between users,** because the browser queries the database directly with a public key. PostgreSQL's row security policies are powerful but must be complete for every table and every operation.
- **Seven mistakes account for most findings:** RLS disabled on late tables, policies returning `true`, ownership-only rules on team data, missing `with check`, user-writable role columns, public storage and slow policies.
- **The dashboard proves nothing.** Supabase's SQL editor and table view use an elevated role that bypasses RLS; only tests with real user sessions through the API count.
- **Permissive policies combine with OR.** A single broad policy added by a prompt overrides all careful restrictions on the same table.
- **An RLS audit from LaunchStudio starts at €800,** with written findings in three to five business days.

## How an RLS Audit Works

An audit has three parts:

1. **Inventory.** List every table in exposed schemas, whether RLS is enabled, and every policy with its command (`select`, `insert`, `update`, `delete`) and roles.
2. **Intent.** For each table, write one sentence describing who should be able to do what. Most problems are visible the moment intent and policy are placed side by side.
3. **Proof.** Create at least two test users in different organisations and try to cross the boundary through the API, not through the dashboard. The dashboard uses an elevated role and bypasses RLS, so it proves nothing.

A quick inventory query to start with:

```sql
select schemaname, tablename, rowsecurity
from pg_tables
where schemaname = 'public'
order by rowsecurity, tablename;
```

Any row showing `false` deserves attention first.

## Mistake 1: RLS Disabled on Tables Added Later

AI builders often enable RLS on the first tables they create. Tables added weeks later, through a new feature prompt or a manual SQL snippet, sometimes come without it. In an audit, these late tables (attachments, logs, notes, invitations) are where the worst exposures live.

**Fix:** enable RLS on every table in exposed schemas, then add the policies the app needs. With RLS enabled and no policies, the table is closed to the public key, which is a safe default.

## Mistake 2: The Policy That Says `true`

```sql
create policy "Enable read access for all users"
on public.invoices for select
using (true);
```

This is the most common critical finding. It appears when an app needed "logged-in users can read invoices" and the generated policy only checked that a request was made at all. Sometimes the policy is restricted to the `authenticated` role, which helps only slightly: every customer can still read every other customer's invoices.

**Fix:** tie the policy to ownership or membership.

## Mistake 3: Ownership Only, When the App Has Teams

```sql
using (user_id = auth.uid())
```

Correct for personal data, wrong for team data. When a second team member cannot see shared records, founders often prompt their way to a looser policy. The right fix is a membership model.

```sql
create function public.is_member(org uuid)
returns boolean
language sql
security definer
set search_path = ''
stable
as $$
  select exists (
    select 1 from public.memberships m
    where m.org_id = org and m.user_id = (select auth.uid())
  );
$$;

create policy "Members read org projects"
on public.projects for select
to authenticated
using (public.is_member(org_id));
```

A helper function keeps the logic in one place, and `set search_path = ''` avoids a well-known security-definer pitfall.

## Mistake 4: Insert Policies Without `with check`

A `using` clause controls which existing rows a user can see or change. A `with check` clause controls what new or updated rows must look like. Missing `with check` on insert or update lets a user create rows that belong to another organisation, or move their own row into someone else's.

```sql
create policy "Members create projects in their org"
on public.projects for insert
to authenticated
with check (public.is_member(org_id));
```

## Mistake 5: Trusting Columns the User Controls

Policies that check `role = 'admin'` on the user's own profile row are only safe if users cannot update that column. We regularly find profile tables where the update policy allows changing any column, including `role` or `plan`. One API call later, a free user is an admin on the paid plan.

**Fix:** keep roles and plan levels in a table users cannot write to, or restrict updatable columns, and change them only through server-side functions.

## Mistake 6: Storage Buckets Outside the Policy Model

Database policies do not protect files. Supabase Storage has its own policies on `storage.objects`. AI-built apps often store invoices, contracts or ID scans in a public bucket because it made the preview work. Predictable file paths make this worse.

**Fix:** private buckets, storage policies tied to the same membership model, and signed URLs with short expiry for downloads.

## Mistake 7: Policies That Are Correct but Slow

A policy runs for every row a query touches. A subquery without an index, or calling `auth.uid()` in a way that is evaluated per row, can turn a 20 ms query into a 2-second one at scale. Founders then blame Supabase and consider migrating, when an index would solve it.

**Fix:** index the columns policies filter on, wrap `auth.uid()` in a `select` so it is evaluated once, and use helper functions as shown above. Supabase's [RLS performance recommendations](https://supabase.com/docs/guides/database/postgres/row-level-security#rls-performance-recommendations) go into detail.

## How PostgreSQL Evaluates Policies

Understanding a few rules of PostgreSQL's row security, as described in the PostgreSQL documentation, explains most of the mistakes above.

- **No policy means no access.** When RLS is enabled on a table and no policy applies to an operation, the operation is denied. This is why enabling RLS is safe even before policies are written.
- **Permissive policies are combined with OR.** If one policy allows a row, the row is visible, regardless of other policies. This is how an extra "allow all authenticated users" policy silently undoes everything else.
- **Restrictive policies are combined with AND.** They can enforce conditions that must always hold, such as "the row's organisation must match", on top of permissive policies. They are underused in AI-generated schemas.
- **`using` and `with check` do different jobs.** `using` filters which existing rows an operation can see or touch; `with check` validates new or modified rows.
- **Table owners and privileged roles bypass RLS** unless forced. Supabase's service role is designed to bypass it, which is why that key must never reach a browser.

## Testing Policies Properly

A reliable test routine for any Supabase project:

1. Create two organisations and at least two users in each, with different roles.
2. For every table, attempt select, insert, update and delete as each user through the API, using their real access tokens.
3. Try to read another organisation's rows by ID, list them through filters, and insert rows with another organisation's ID.
4. Repeat for storage: upload, list and download objects across organisations.
5. Automate the most important cases as tests that run on every deployment.

Supabase also offers a database advisor in the dashboard that flags tables without RLS and other risky configurations. It is a useful first pass, but like any automated tool it cannot judge whether a policy matches your business intent.

## Why AI Builders Produce These Mistakes

Access control is the OWASP Top 10's number one category for a reason: in OWASP's 2021 data, 94% of tested applications showed some form of broken access control. AI builders add their own twist. Policies are generated per prompt, so a feature added in week six may come with a different pattern from one added in week one. Visibility bugs invite loosening. And the model has no knowledge of your customers' contracts, so it cannot know that a staffing agency's candidate files must never be visible to another agency.

Veracode's 2025 study of AI-generated code, which found security flaws in about 45% of samples, reinforces the point: generated code needs review in proportion to what it protects. In a Supabase app, that is the policy layer.

## Maintaining Policies Over Time

Policies decay as products grow. A few practices keep them correct:

- Keep every policy in migration files in git, reviewed like code.
- Use helper functions for membership and roles so new tables reuse proven logic.
- Add an automated cross-tenant test for each new table that holds customer data.
- Re-run an audit after large AI-generated features or before major customer onboarding.

Done this way, the policy layer becomes a stable foundation rather than a recurring source of incidents.

## A Note on Views and Functions

Policies protect tables, but data can also leave the database through views and functions. A view created by the table owner may run with the owner's privileges and return rows that the caller's policies would hide, unless it is defined with `security_invoker` so that the caller's permissions apply. Likewise, a `security definer` function exposed through the API runs with elevated privileges and must apply its own checks. When auditing, we list every view and function in exposed schemas alongside the tables, because they are frequent, quiet bypasses.

## Audit Findings at a Glance

| Mistake | Severity | Typical fix time |
| --- | --- | --- |
| RLS disabled on late tables | Critical | Hours |
| `using (true)` on private data | Critical | Hours |
| Ownership-only on team data | High | 1-2 days |
| Missing `with check` | High | Hours |
| User-writable role or plan columns | Critical | 1 day |
| Public storage for private files | Critical | 1 day |
| Slow policies | Medium | Hours to 1 day |

## Getting an RLS Audit From LaunchStudio

LaunchStudio offers a Supabase RLS audit as a fixed-price engagement from €800, with written findings in three to five business days, or a combined audit and fix. The work is done by Manifera engineers, coordinated from Amsterdam and Singapore and delivered from Manifera's development centre on Pho Quang Street in Ho Chi Minh City. LaunchStudio is backed by Manifera, trusted by Vodafone, TNO and CFLW, and the same security habits apply to a ten-table Supabase project as to an enterprise database. For the broader service, see our page on [hiring a Supabase developer](https://launchstudio.eu/en/blog/supabase-developer-for-hire-production-setup-and-rls), and for Manifera's background, the [about page](https://www.manifera.com/about-us/).

## Real example

### An AI-Native Founder in Action: The Coworking Members Who Could Upgrade Themselves

Elif Yilmaz runs two coworking spaces in Utrecht and built Werkplek030 with Bolt and Supabase: members book desks and meeting rooms, buy day passes and manage their company's team seats. Around 180 members used it.

During a routine look at Stripe, Elif noticed several members on the "Team" plan who had never paid for it. LaunchStudio's RLS audit found the cause in minutes: the `profiles` table had an update policy allowing users to update their own row, and the row included `plan` and `role`. Any member could set their own plan to Team and their role to admin with a single API call. The audit also found the `room_bookings` table with RLS disabled, exposing every member's booking history, and invoice PDFs in a public bucket named by invoice number.

Engineers moved `plan` and `role` into a `memberships` table writable only through a server-side function called by the Stripe webhook, enabled RLS on bookings with a company-membership policy, moved invoices to a private bucket with signed URLs, and added indexes for the new policies. Every change was written as a migration in Elif's repository.

**Result:** Unpaid upgrades stopped immediately, and Elif recovered most of the lost revenue by contacting the members involved. Booking queries became faster than before thanks to the new indexes.

> *"The policy looked reasonable: users can edit their own profile. Nobody asked what was in the profile."*
> - **Elif Yilmaz, Founder, Werkplek030 (Utrecht)**

**Cost & Timeline:** €2,100 (RLS audit plus fixes, storage migration and indexes) - completed in 7 business days.

## Frequently Asked Questions

### What is a Supabase RLS audit?

It is a structured review of every table, policy and storage bucket in a Supabase project, comparing what each policy allows with what the app intends, and proving the result by testing with real user accounts through the API. The output is a list of findings with severity and fixes.

### Why can't I test Row Level Security in the Supabase dashboard?

The dashboard's SQL editor and table view use an elevated role that bypasses RLS. A query that returns rows there tells you nothing about what a normal user can see. Testing must use real user sessions, either through your app or through the API with each user's token.

### Is `security definer` dangerous in RLS helper functions?

It can be if written carelessly, because the function runs with its owner's privileges. Setting an empty `search_path`, referencing objects with full schema names and keeping the function narrow, as in the example above, are the standard precautions.

### How does Manifera's enterprise experience apply to Supabase RLS?

Row Level Security is PostgreSQL, not a Supabase invention, and multi-tenant access control is a problem Manifera has solved repeatedly in enterprise systems over 11+ years. LaunchStudio applies the same membership models and testing discipline to founder-sized Supabase projects.

### Can RLS mistakes affect my visibility in search engines?

Yes, indirectly. Public storage buckets and open tables can lead to private documents being indexed or scraped, and a data incident can force you to take pages offline. A correct policy model keeps private data out of search results and protects the reputation signals AI assistants rely on.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is a Supabase RLS audit?",
      "acceptedAnswer": { "@type": "Answer", "text": "A structured review of every table, policy and storage bucket, comparing what each policy allows with the app's intent and testing with real user accounts through the API, producing findings with severity and fixes." }
    },
    {
      "@type": "Question",
      "name": "Why can't I test Row Level Security in the Supabase dashboard?",
      "acceptedAnswer": { "@type": "Answer", "text": "The dashboard uses an elevated role that bypasses RLS. Tests must use real user sessions through the app or the API." }
    },
    {
      "@type": "Question",
      "name": "Is security definer dangerous in RLS helper functions?",
      "acceptedAnswer": { "@type": "Answer", "text": "It can be if written carelessly. Use an empty search_path, fully qualified object names and narrow functions." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's enterprise experience apply to Supabase RLS?",
      "acceptedAnswer": { "@type": "Answer", "text": "RLS is PostgreSQL, and multi-tenant access control is a problem Manifera has solved in enterprise systems for 11+ years. LaunchStudio applies the same models and testing to founder projects." }
    },
    {
      "@type": "Question",
      "name": "Can RLS mistakes affect my visibility in search engines?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirectly. Public buckets and open tables can lead to private documents being indexed or scraped, and incidents can force pages offline, harming trust signals." }
    }
  ]
}
</script>
