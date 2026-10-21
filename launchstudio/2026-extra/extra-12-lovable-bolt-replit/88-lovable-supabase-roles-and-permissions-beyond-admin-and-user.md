---
Title: "Lovable Supabase: Roles and Permissions Beyond Admin and User"
Keywords: lovable supabase, roles and permissions, RBAC, access control, row level security, custom roles, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Scale-Up
---

# Lovable Supabase: Roles and Permissions Beyond Admin and User

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Roles and Permissions Beyond Admin and User",
  "description": "Admin and user stop being enough the first time a larger customer asks for a read-only accountant or managers limited to one location. How to model permissions, scope them, enforce them in the database and server, and test them without a combinatorial nightmare.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-07",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-supabase-roles-and-permissions-beyond-admin-and-user" }
}
</script>

Every AI-built product starts with two kinds of user: the person who set it up and everyone else. Sometimes three — owner, admin, member. That is enough for a customer with four employees.

It stops being enough at a recognisable moment. A larger customer asks for an external accountant who can see invoices but change nothing. Or for location managers who run their own branch and must not see the others. Or for planners who schedule staff but must not see what anyone earns. The founder adds a role, then another, and within a year the code contains `if (role === 'admin' || role === 'manager' && location === user.location)` in forty places, each slightly different.

Permissions are where security, product and sales meet. Getting the model right lets you say yes to larger customers; getting it wrong produces the incidents the IDOR and admin panel articles in this series describe. This article covers the model, the scoping, the enforcement, and how to test it.

## Why Three Roles Break

Owner, admin and member describe one dimension: how much someone may do. Real organisations need at least three.

**What someone may do** — read invoices, approve hours, change prices, invite people.

**Where they may do it** — all locations, their own location, one project, one client.

**What they may see** — every field, or every field except salaries, margins or medical notes.

A single role field can represent only the first, and only coarsely. Every request from a customer that touches the second or third is answered by creating a new role that bundles a scope into its name — "manager-amsterdam" — or by a special case in code. Both scale badly, and both are where AI-generated permission logic drifts, because each new session adds its own check in its own style.

## Permissions as Codes, Roles as Bundles

The model that holds up separates three things.

**Permissions** are the atomic actions your product supports, named as codes: `invoices.read`, `invoices.approve`, `hours.approve`, `wages.read`, `members.invite`, `billing.manage`. They are defined by you, in code, and change only when the product changes.

**Roles** are named bundles of permissions: an "Accountant" role holds `invoices.read` and `reports.read`. Roles are what customers see and assign.

**Assignments** connect a member to a role, optionally within a scope.

```sql
create table roles (
  id uuid primary key default gen_random_uuid(),
  organisation_id uuid references organisations(id) on delete cascade, -- null = system role
  name text not null,
  is_system boolean not null default false
);

create table role_permissions (
  role_id uuid not null references roles(id) on delete cascade,
  permission text not null,
  primary key (role_id, permission)
);

create table role_assignments (
  organisation_id uuid not null,
  user_id uuid not null,
  role_id uuid not null references roles(id) on delete cascade,
  location_id uuid references locations(id) on delete cascade, -- null = whole organisation
  foreign key (organisation_id, user_id) references memberships(organisation_id, user_id) on delete cascade
);
```

Three properties make this practical. System roles — Owner, Administrator, Manager, Member, Read-only — ship with the product and cover most customers without configuration. Custom roles per organisation are possible later without a schema change. And the foreign key to `memberships` means removing someone from an organisation removes every role they held, which is the guarantee the team invitations article in this series argues for.

Keep the list of permission codes in one file in the codebase, with a one-line description each. It is the reference for developers, the source for the customer-facing permission matrix, and the list an AI assistant reads before adding a new check.

## Scope: Where a Permission Applies

Most multi-location and multi-project customers need permissions that apply to part of the organisation. The `location_id` on the assignment expresses it: a Manager role assigned with a location applies only there; without one it applies everywhere.

Pick one scoping dimension and model it explicitly — locations, projects, departments, clients — rather than building a generic hierarchy. A generic "resource" scope with nested parents is tempting and almost always more than a product of this size needs. If a second dimension becomes necessary later, it is an additional nullable column, not a redesign.

The rule for combining assignments is union: a person with Manager at Amsterdam and Read-only for the whole organisation can manage Amsterdam and read everything. Never implement "deny" assignments at this stage; they make every question about access require reasoning about precedence, and they are the source of most confusion in larger permission systems.

## Enforce in Three Places, Trust One

Permissions are checked in three layers, and each has a different job.

**The database decides what data is visible.** Row level security policies use a helper that answers whether the current user holds a permission, in this organisation, for this location:

```sql
create function has_permission(org uuid, perm text, loc uuid default null)
returns boolean language sql security definer stable set search_path = public as $$
  select exists (
    select 1
    from role_assignments ra
    join role_permissions rp on rp.role_id = ra.role_id
    where ra.organisation_id = org
      and ra.user_id = auth.uid()
      and rp.permission = perm
      and (ra.location_id is null or ra.location_id = loc)
  );
$$;

create policy "read shifts" on shifts for select
  using (has_permission(organisation_id, 'shifts.read', location_id));
```

**The server decides what actions are allowed.** Edge functions and RPCs that approve, send, pay or delete check the specific permission before acting — `hours.approve`, not merely membership. Policies protect rows; actions often span rows, call external services or have side effects a row policy cannot see.

**The interface decides what to show.** Buttons a user cannot use are hidden or disabled. This is for usability only. A hidden button is not a permission check, and AI-generated code frequently treats it as one — the admin panel article in this series describes the result.

The database is the layer to trust, because it is the one every path goes through: the interface, the API, an integration, a script someone runs next year.

## Field-Level Permissions

Some permissions concern columns rather than rows: a planner may see a shift, but not the hourly wage attached to it. Row level security cannot hide a column.

Two arrangements work in Supabase.

**Move sensitive fields into their own table**, with its own policy. `staff_compensation` keyed by staff member, readable only with `wages.read`. The main table stays readable by planners; the sensitive one is invisible to them. This is the cleanest option and the one to prefer for anything genuinely sensitive.

**Expose a view without the column** to roles that may not see it, and revoke direct access to the underlying table, as the views article in this series describes. Workable, but easier to get wrong when someone later adds a column to the table and forgets the view.

What does not work is fetching the full row and omitting the field in the interface. The field is in the response, visible to anyone who opens the browser's network tab.

## Privilege Escalation Rules

A permission system must also govern itself, and this is where AI-generated implementations are weakest.

**People cannot grant permissions they do not hold.** An administrator without `billing.manage` cannot create a role containing it, or assign one. Enforce this in the function that creates roles and assignments, not in the interface.

**People cannot raise their own access.** Assigning a role to yourself requires a permission that is reserved to owners, or is forbidden entirely.

**Some actions need separation.** The person who submits hours should not be the person who approves them; the person who creates a payment should not be the person who releases it. A simple check — `approved_by <> submitted_by` — enforced in the database, closes the most common fraud pattern in small products.

**Owners are protected.** Nobody below owner may remove an owner or change an owner's role, and the last owner cannot be removed at all, as described in the team invitations article.

## Performance and Freshness

`has_permission` runs on every row of every query. Without care, it becomes the slowest part of the product.

Index `role_assignments (user_id, organisation_id)` and `role_permissions (role_id, permission)`. Mark the function `stable` so Postgres can evaluate it once per statement for constant arguments. And keep the number of joins small — the model above needs two.

The alternative often suggested is putting permissions into the JWT through Supabase's custom access token hook, so policies read claims rather than tables. It is faster and it is stale: a permission removed at ten o'clock stays in the token until it is refreshed. For most B2B products the database lookup is fast enough with indexes and has the property that matters — removal takes effect on the next request. Use claims for coarse, rarely-changing facts, if at all, and keep revocable permissions in the database.

## Testing a Permission Matrix

Permissions multiply. Six roles, twenty-four permissions and two scopes make hundreds of combinations, and nobody tests them by clicking.

The approach that works is to write the expected matrix down as data and generate tests from it:

```ts
const matrix = {
  'Manager (Amsterdam)': { 'shifts.read@amsterdam': true, 'shifts.read@utrecht': false, 'wages.read': false },
  'Accountant':          { 'invoices.read': true, 'invoices.approve': false, 'wages.read': false },
};
// For each entry: sign in as a seeded user with that role and assert the query succeeds or returns nothing.
```

The matrix doubles as documentation: it is what you show a customer's IT department when they ask what each role can do, and the customer-facing permission page can be generated from the same file. When a permission changes, the matrix changes in the same commit, and the tests say whether the database agrees.

Add the cross-organisation test from the IDOR article on top: a user with every permission in organisation A must still see nothing in organisation B.

## API Keys, Integrations and Support Access

People are not the only actors. Three others need permissions too, and AI-built products usually give them everything.

**API keys created by customers** should carry a role, exactly as a person does. A key used by an accounting integration needs `invoices.read`, not the full rights of the administrator who created it. Store the role on the key, check it the same way, and show it on the key's settings page so the customer can see what each integration may do. The integrations article in extra-11 describes what happens when one key with full access leaks.

**Your own background jobs** run with the service role and bypass row level security entirely. That is necessary, and it means every job must filter by organisation explicitly and be reviewed as carefully as a policy — the service role is the one actor no permission check will stop.

**Support access** — you or a colleague looking at a customer's account to help them — should be a deliberate, time-limited and logged action, ideally granted by the customer: "allow support access for 48 hours". Impersonating users silently, through the service role or by signing in as them, is convenient and is exactly what a careful customer's security questionnaire asks about. A short `support_grants` table with an expiry, checked by the same helper, turns it into a capability you can describe honestly.

## What to Show Customers

Larger customers judge a product partly by how understandable its permissions are. Three things help.

**A permission matrix in the product** — roles down the side, capabilities across the top — generated from the same definitions the code uses, so it cannot drift.

**Sensible default roles**, named in the customer's language: Eigenaar, Beheerder, Locatiemanager, Medewerker, Alleen lezen. Most customers never create a custom role; good defaults are what they actually use.

**An audit of role changes**, visible to administrators: who gave whom which role, when. It answers the questions that otherwise become support tickets, and it is what a security questionnaire asks about.

## When Not to Build Custom Roles Yet

Custom roles per organisation are a feature larger customers ask about and smaller ones never use. Building the editor, the validation and the escalation rules is a week of work.

The sequence that works: permission codes and system roles first, which costs little more than three hard-coded roles and makes everything else possible. Scoping when the first multi-location customer needs it. A custom role editor when three customers have asked for it — and, until then, configure custom roles for the customers who need them by hand, which the model supports without any interface.

## Migrating From Owner, Admin and Member

For a product in production with a single role column, the migration is safe if done in order:

1. Define the permission codes by listing every check currently in the code. The list is usually longer than expected, and making it is the most useful part of the exercise.
2. Create system roles that reproduce today's behaviour exactly — the existing admin role becomes a bundle of the permissions admins effectively have now.
3. Backfill assignments from the role column.
4. Replace checks one area at a time — policies first, then server functions, then the interface — running the matrix tests after each.
5. Remove the old column when nothing reads it.

Only after the migration reproduces existing behaviour should new roles and scopes be added. Changing the model and the behaviour in the same step makes every difference ambiguous.

## Setting This Up

For a Lovable product with its first larger customers, this is typically three to five days: permission codes defined in one file with descriptions, system roles as bundles of permissions, assignments linked to memberships with an optional location or project scope, row level security built on an indexed `has_permission` helper, action-level checks in server functions, sensitive fields moved to separately protected tables, escalation rules preventing self-promotion and grants beyond one's own permissions, separation of duties for approvals, a permission matrix maintained as data with generated tests, a customer-facing matrix and role-change audit, and a migration path that reproduces existing behaviour before anything new is added.

LaunchStudio builds this when a product starts selling to organisations with more than one location or department. The engineers are Manifera's — eleven years, 120+ engineers, 160+ projects, clients including Vodafone, TNO and CFLW.

[Ask us to map who can see what in your product](https://launchstudio.eu/en/#contact). The map is usually the surprise.

## Real example

### Managers Who Approved Their Own Overtime

Marloes Teunissen built Horecarooster in Lovable: staff scheduling and hour registration for hospitality groups, used by 27 groups with 140 locations and around 3,800 staff.

The product had three roles: owner, admin and member. Location managers needed to edit their own schedules and approve hours, which only admins could do, so every location manager was made an admin. Admins could see every location in the group, including the hourly wages of all staff, and could approve any hours — including their own.

A group's finance director noticed overtime at one location rising while the restaurant's revenue did not, and found that the manager had been approving his own extra hours. The same week, a larger group with 34 locations declined to sign because managers would be able to see wages across the whole group.

Four business days: 24 permission codes defined from the checks already scattered through the code; six system roles — Owner, Administrator, Location manager, Planner, Staff, Read-only — reproducing existing behaviour first; role assignments with an optional location scope, backfilled from the old role column; row level security rewritten around an indexed `has_permission` helper across 19 tables; wages moved to a separate compensation table readable only with `wages.read`; approval functions checking `hours.approve` for the location and refusing approvals by the person who submitted the hours; escalation rules preventing anyone from granting permissions they did not hold; a permission matrix of 24 permissions by 6 roles maintained as data, generating 288 tests run in CI; and a role-change audit visible to each group's administrators.

**Result:** the review of historical approvals found three managers in two groups who had approved their own overtime, totalling €4,100, which the groups recovered. The 34-location group signed within the month, and a second group of similar size followed, together adding 61 locations.

> *"We made every location manager an admin because it was the only role that could approve hours. That also let them see everyone's wages and approve their own overtime."*
> — **Marloes Teunissen, Founder, Horecarooster (Haarlem)**

**Cost & Timeline:** €4,800 (permission model and system roles, location-scoped assignments with backfill, policy rewrite across 19 tables, separated compensation data, approval separation, escalation rules, 288 generated matrix tests, role-change audit) — completed in 4 business days.

## Frequently Asked Questions

### When are owner, admin and member no longer enough?

When customers need read-only users, people limited to one location or project, or people who may act without seeing sensitive fields such as wages. A single role field cannot express scope or field visibility.

### What is the difference between a role and a permission?

A permission is one action your product supports, such as `invoices.approve`. A role is a named bundle of permissions that customers assign. Code checks permissions; customers manage roles.

### Where should permissions be enforced?

In the database for data visibility, in server functions for actions, and in the interface only for usability. The database is the layer to trust, because every access path goes through it.

### How do I hide a field such as salary from some roles?

Move it into a separate table with its own policy, or expose a view without the column and revoke access to the base table. Never fetch it and hide it in the interface.

### Should permissions be stored in the JWT?

Rarely. Claims are fast but stale until the token refreshes, so removed permissions linger. An indexed database lookup is fast enough for most products and takes effect immediately.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "When do owner, admin and member roles stop being enough?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "When customers need read-only users, location- or project-scoped access, or access without seeing sensitive fields such as wages."
      }
    },
    {
      "@type": "Question",
      "name": "What is the difference between roles and permissions?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A permission is a single action code; a role is a named bundle of permissions customers assign. Code checks permissions, customers manage roles."
      }
    },
    {
      "@type": "Question",
      "name": "Where should permissions be enforced in a Supabase app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In row level security for data, in server functions for actions, and in the interface only for usability — the database is the trusted layer."
      }
    },
    {
      "@type": "Question",
      "name": "How can I hide salary data from some roles?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Store it in a separate table with its own policy, or use a view without the column — never fetch it and hide it in the UI."
      }
    },
    {
      "@type": "Question",
      "name": "Should permissions live in JWT claims?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Rarely, because claims stay valid until refresh. An indexed database lookup is fast enough and revokes access immediately."
      }
    }
  ]
}
</script>
