---
Title: "How to Add Authentication Roles and an Admin Panel to a Lovable App"
Keywords: lovable admin panel, lovable user roles, lovable authentication roles, supabase roles lovable, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# How to Add Authentication Roles and an Admin Panel to a Lovable App

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Add Authentication Roles and an Admin Panel to a Lovable App",
  "description": "Adding roles and an admin panel to a Lovable app takes more than a hidden menu. This guide shows a secure pattern: a roles table users cannot edit, RLS policies that check roles, admin actions in edge functions and testing.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-06",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-to-add-roles-and-an-admin-panel-to-a-lovable-app" }
}
</script>

**Short answer:** store roles in a separate table that users cannot write to, check those roles in Supabase Row Level Security policies, and perform admin actions through edge functions that verify the caller's role on the server. The admin panel itself can be a normal Lovable page, but hiding it from non-admins is only cosmetic. Real protection happens in the database and on the server.

Here is the pattern step by step.

## The Insecure Pattern Lovable Often Generates

Ask Lovable for "an admin panel for admins only" and you may get:

- An `is_admin` or `role` column on the `profiles` table
- A check in React: if the user is an admin, show the admin menu
- Admin pages that query tables directly with the anon key

Three problems: users can often update their own profile row, including the `role` column; anyone can open the admin URL and call the same queries; and RLS policies may not distinguish admins at all. The admin panel is protected only by the fact that normal users do not see the button.

## Step 1: A Roles Table Users Cannot Edit

```sql
create type public.app_role as enum ('admin', 'staff', 'member');

create table public.user_roles (
  user_id uuid references auth.users on delete cascade,
  role public.app_role not null,
  primary key (user_id, role)
);

alter table public.user_roles enable row level security;

create policy "Users read own roles"
on public.user_roles for select
to authenticated
using (user_id = (select auth.uid()));
```

There are deliberately no insert, update or delete policies. Users can read their own roles; nobody can change roles through the public API. Role changes happen only through server-side code.

## Step 2: A Helper Function for Policies

```sql
create function public.has_role(_role public.app_role)
returns boolean
language sql
stable
security definer
set search_path = ''
as $$
  select exists (
    select 1 from public.user_roles
    where user_id = (select auth.uid()) and role = _role
  );
$$;
```

## Step 3: Use Roles in Row Level Security

```sql
create policy "Admins read all orders"
on public.orders for select
to authenticated
using (public.has_role('admin') or customer_id = (select auth.uid()));
```

Now the database enforces what the interface displays. A non-admin calling the API directly still only sees their own orders.

## Step 4: Admin Actions in Edge Functions

Actions such as refunding a payment, changing someone's role or deleting an account should not be done with the anon key from the browser. Create an edge function that:

1. Reads the caller's JWT and verifies it
2. Checks `user_roles` for the admin role
3. Performs the action with server-side credentials
4. Writes an audit log entry: who did what, to whom, when

## Step 5: The Admin Panel in Lovable

Now Lovable can build the admin interface freely. It reads data the policies allow and calls the edge functions for privileged actions. Prompting tip: tell Lovable explicitly that admin actions must call specific edge functions and that it must not change RLS policies or the `user_roles` table.

## Step 6: Test Like an Attacker

- Log in as a member, open the admin URL, and try every action
- Call admin edge functions with a member's token
- Try to insert a row into `user_roles` through the API
- Try to update your own `profiles` row with a role field, if one still exists

Every attempt should fail.

## Roles Beyond Admin and Member

| Pattern | When to use |
| --- | --- |
| Global roles (admin, staff, member) | One organisation, internal staff and customers |
| Organisation roles (owner, admin, member per org) | B2B SaaS where customers manage their own teams |
| Resource permissions (editor, viewer per project) | Collaboration tools with shared items |

B2B products usually need organisation roles: a `memberships` table with `org_id`, `user_id` and `role`, and policies checking membership. The same principles apply: users cannot change their own role, policies enforce access, privileged actions go through the server.

## Getting It Built

Roles and an admin panel are among the most common LaunchStudio additions to Lovable apps, typically within a Launch Ready engagement of €1,200-€3,500. Behind LaunchStudio is Manifera's team of 120+ seasoned engineers, who have built role-based systems for enterprise clients across 11+ years, coordinated from Amsterdam and delivered from Ho Chi Minh City. See [Manifera's web app development](https://www.manifera.com/services/web-app-develop/) for the enterprise side, and Supabase's [custom claims and RBAC guide](https://supabase.com/docs/guides/database/postgres/custom-claims-and-role-based-access-control-rbac) for an alternative approach using JWT claims. If you also want to check the rest of your app, try our [Lovable security self-test](https://launchstudio.eu/en/blog/is-my-lovable-app-secure).

## Real example

### An AI-Native Founder in Action: The Volunteer Platform Where Anyone Could Become Coordinator

Roos van Dam coordinates a neighbourhood help network in Zaandam and built Buurthulp in Lovable: residents post requests such as groceries or a lift to the doctor, volunteers accept them, and coordinators manage volunteers and check sensitive requests. About 140 volunteers and 300 residents joined.

Lovable had implemented coordinators with a `role` column on `profiles`, and a profile edit page that saved the whole row. A volunteer discovered, without meaning to, that editing their profile through the browser's developer tools could set `role` to `coordinator`, which revealed residents' addresses and medical notes on sensitive requests. The admin page itself checked the role only in the React component.

LaunchStudio created a `user_roles` table with no write policies, migrated existing coordinators into it, removed the `role` column from `profiles`, added a `has_role` helper and rewrote RLS so medical notes and addresses were visible only to coordinators and the assigned volunteer. Approving volunteers and assigning coordinators moved into edge functions with an audit log.

**Result:** The privilege escalation was closed within four business days. Roos informed the network's board, documented the incident and now reviews the audit log monthly. Buurthulp has since handled around 2,000 requests.

> *"The admin page was hidden. That's all it was: hidden. Anyone who knew how to look could promote themselves."*
> - **Roos van Dam, Founder, Buurthulp (Zaandam)**

**Cost & Timeline:** €1,750 (Launch Ready package: roles table, migration, RLS rewrite, admin edge functions and audit log) - completed in 6 business days.

## Frequently Asked Questions

### Can I just hide the admin page from non-admin users?

Hiding it improves the interface but provides no security. Anyone can type the URL or call the same database queries directly. Protection must come from Row Level Security and server-side checks in edge functions.

### Should roles be stored in the profiles table?

Preferably not, unless users cannot update that column. A separate roles table without write policies is simpler and safer, because it removes the risk of a profile edit becoming a privilege escalation.

### How do I add organisation-level roles for a B2B Lovable app?

Use a memberships table linking users to organisations with a role per membership. Policies check membership through a helper function, and only organisation owners or admins, through server-side functions, can invite users or change roles.

### Why do Manifera's engineers prefer database-enforced roles?

Because interfaces change constantly, especially with AI tools regenerating components, while database policies stay put. Manifera's 11+ years of enterprise access control work show that rules enforced at the database level survive redesigns and new features.

### Do admin panels affect SEO?

They should not be indexed at all. Make sure admin routes require authentication on the server and are excluded from sitemaps. An exposed admin page appearing in search results is both a security and a reputation problem.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I just hide the admin page from non-admin users?",
      "acceptedAnswer": { "@type": "Answer", "text": "Hiding provides no security. Protection must come from Row Level Security and server-side checks in edge functions." }
    },
    {
      "@type": "Question",
      "name": "Should roles be stored in the profiles table?",
      "acceptedAnswer": { "@type": "Answer", "text": "Preferably not. A separate roles table without write policies prevents profile edits from becoming privilege escalations." }
    },
    {
      "@type": "Question",
      "name": "How do I add organisation-level roles for a B2B Lovable app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Use a memberships table with a role per organisation, helper functions in policies, and server-side functions for invitations and role changes." }
    },
    {
      "@type": "Question",
      "name": "Why do Manifera's engineers prefer database-enforced roles?",
      "acceptedAnswer": { "@type": "Answer", "text": "Interfaces change, especially with AI tools, while database policies persist. Manifera's 11+ years of access control work favour database-level rules." }
    },
    {
      "@type": "Question",
      "name": "Do admin panels affect SEO?",
      "acceptedAnswer": { "@type": "Answer", "text": "They should not be indexed. Require server-side authentication and exclude admin routes from sitemaps." }
    }
  ]
}
</script>
