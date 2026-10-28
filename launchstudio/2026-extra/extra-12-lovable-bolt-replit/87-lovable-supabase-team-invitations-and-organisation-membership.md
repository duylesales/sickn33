---
Title: "Lovable Supabase: Team Invitations and Organisation Membership"
Keywords: lovable supabase, team invitations, organisation membership, multi-user accounts, invite links, row level security, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Supabase: Team Invitations and Organisation Membership

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Team Invitations and Organisation Membership",
  "description": "The moment a customer wants to add a colleague, a single-user app needs organisations, memberships and invitations. The data model, secure invite tokens, the edge cases AI-generated flows miss, and what removing someone must actually do.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-05",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-supabase-team-invitations-and-organisation-membership" }
}
</script>

Most AI-built products start with one person per account. The founder signs up, the product works, the first customers sign up the same way. Then a customer asks the question every B2B product eventually hears: "Can my colleague use it too?"

What gets built in response is usually an "invite" button that sends a link, and an `organisation_id` column on the user's profile. It works for the demonstration. It also tends to produce invite links that never expire, links that work for whoever receives a forwarded email, people who cannot belong to two companies, and former employees who keep their access because "removing" them only hid them from a list.

Membership is the foundation that permissions, billing, audit and data separation all sit on. It is worth getting the model right before the second customer has five users, because changing it later means migrating every policy that depends on it.

## The Data Model: Three Tables, Not One Column

The shortcut is a single column: `profiles.organisation_id`. It answers "which company does this person belong to" - and nothing else.

It cannot represent a person who belongs to two organisations, which is common: accountants serving several clients, subcontractors working for several installers, consultants, and anyone who changes employer but keeps their email address. It cannot hold a role per organisation. And it cannot represent an invitation that has not yet been accepted.

The model that holds up uses three tables.

```sql
create table organisations (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  created_at timestamptz not null default now()
);

create table memberships (
  organisation_id uuid not null references organisations(id) on delete cascade,
  user_id uuid not null references auth.users(id) on delete cascade,
  role text not null check (role in ('owner', 'admin', 'member')),
  created_at timestamptz not null default now(),
  primary key (organisation_id, user_id)
);

create table invitations (
  id uuid primary key default gen_random_uuid(),
  organisation_id uuid not null references organisations(id) on delete cascade,
  email text not null,
  role text not null check (role in ('admin', 'member')),
  token_hash text not null unique,
  invited_by uuid not null references auth.users(id),
  expires_at timestamptz not null,
  accepted_at timestamptz,
  revoked_at timestamptz,
  created_at timestamptz not null default now()
);
```

A membership is the relationship between a person and an organisation, with the role belonging to that relationship rather than to the person. An invitation is a pending membership with an expiry. Neither replaces the other: the invitation records who was asked, by whom and when; the membership records who actually has access.

The composite primary key on `memberships` enforces that a person can be a member of an organisation once. The cascades mean that deleting an organisation removes its memberships and invitations, and deleting a user removes their memberships - which is what GDPR erasure requires, as the deletion article in extra-11 describes.

## Policies Follow Membership

Once membership is a table, row level security policies ask one question: is the current user a member of the organisation that owns this row?

```sql
create function is_member(org uuid) returns boolean
language sql security definer stable set search_path = public as $$
  select exists (
    select 1 from memberships
    where organisation_id = org and user_id = auth.uid()
  );
$$;

create policy "members read invoices" on invoices
  for select using (is_member(organisation_id));
```

The helper function matters for two reasons. It keeps policies short and identical across tables, which makes them reviewable. And because it is `security definer`, it reads `memberships` without that table's own policies recursing into themselves - the infinite recursion error that AI-generated policies produce with surprising regularity when a membership policy tries to check membership.

Index `memberships (user_id, organisation_id)`. Every policy evaluation on every table calls this function, and without the index each one is a scan.

Roles add a second helper - `has_role(org, 'admin')` - used for writes that not every member may perform: inviting people, changing billing, deleting records. The roles and permissions article in this series covers when three roles stop being enough.

## Invitation Tokens Done Properly

The invite link is a credential. Whoever holds it can join an organisation and see its data. It deserves the same care as a password reset link, and the password reset article in this series describes most of what goes wrong.

**Random, long and unguessable.** At least 32 bytes from a cryptographic random generator. Not the invitation's database ID, not the inviter's user ID, not an incrementing number - all of which appear in AI-generated invite flows.

**Stored as a hash.** The database holds `sha256(token)`, the email holds the token. Someone who reads the invitations table - through a backup, a leaked service key, an overly broad policy - cannot use what they find.

**Expiring.** Seven days is a sensible default for B2B products. Long enough for someone on holiday; short enough that an old email in a compromised mailbox is worthless.

**Single use.** Accepting sets `accepted_at`, and a token with `accepted_at` set is rejected.

**Revocable.** An admin who invited the wrong address can revoke the invitation before it is used, which sets `revoked_at`.

**Bound to an email address.** This is the property most often missing, and the one that matters most.

```ts
// Edge function: accept invitation
const tokenHash = await sha256(token);
const { data: inv } = await admin.from('invitations')
  .select('*').eq('token_hash', tokenHash)
  .is('accepted_at', null).is('revoked_at', null)
  .gt('expires_at', new Date().toISOString())
  .single();
if (!inv) return error(410, 'invitation_invalid');
if (inv.email.toLowerCase() !== user.email.toLowerCase())
  return error(403, 'invitation_email_mismatch');
// insert membership and mark accepted in one transaction
```

Without the email check, an invitation is a bearer link: forwarded once, it admits whoever clicks it. With it, a forwarded link is useless to anyone except the intended recipient.

Do the acceptance in one transaction - insert the membership, set `accepted_at` - so two simultaneous clicks cannot create a duplicate or accept a revoked invitation.

## The Flows AI-Generated Code Misses

The happy path - an admin invites a new address, the recipient signs up and joins - is what gets built and tested. Real usage hits several others within the first month.

**The recipient already has an account.** They should sign in and be added, not be asked to sign up again and told the email is taken.

**The recipient signs up with a different address.** Someone invited at `j.devries@company.nl` signs up with a personal Gmail address. The email binding rejects it, correctly, and the error message must say why and what to do - sign in with the invited address, or ask for a new invitation.

**The recipient is invited twice.** A second invitation to the same address for the same organisation should replace the first, not create a parallel one. A partial unique index on `(organisation_id, lower(email))` where the invitation is still pending enforces it.

**The recipient is already a member.** Inviting an existing member should say so, not send an email.

**The invitation expired.** The link should explain that it expired and that the admin can send a new one - not show a generic error, which produces a support ticket every time.

**The organisation has reached its seat limit.** Discussed below; the check belongs at invitation and again at acceptance.

Each of these is a few lines. Together they are the difference between a feature that generates support email and one that does not.

## Removing Someone Must Actually Remove Them

The most consequential gap in AI-built team features: removal that hides rather than revokes.

A "remove member" button that sets `active = false`, or removes the person from a list on screen while leaving their `organisation_id` intact, leaves them with full access through the API. As the session article in this series describes, an existing session also continues until it expires unless something ends it.

Removal must do four things:

1. **Delete the membership row.** Every policy that checks membership now denies access on the next request.
2. **End their session for that organisation**, or all sessions if they belong to nothing else. Supabase allows signing a user out server-side; use it.
3. **Revoke anything personal they held** - API keys they created, integrations they connected, calendar feeds with their token in the URL.
4. **Record it** - who removed whom, when - in the audit log.

And one thing removal must not do: delete the work they created. Invoices a former employee issued still belong to the organisation. Reference the user by ID, keep the row, and display "former member" where their name would appear. Deleting a person's contributions because they left is a data loss incident in waiting.

## Protect the Last Owner

An organisation with no owner cannot be administered, billed or deleted by anyone but you. It happens when the only owner leaves, removes themselves, or changes their own role to member to test something.

Enforce it in the database rather than the interface:

```sql
create function prevent_ownerless_org() returns trigger language plpgsql as $$
begin
  if (select count(*) from memberships
      where organisation_id = old.organisation_id and role = 'owner'
      and not (organisation_id = old.organisation_id and user_id = old.user_id)) = 0
     and (tg_op = 'DELETE' or new.role <> 'owner') then
    raise exception 'organisation_must_keep_an_owner';
  end if;
  return coalesce(new, old);
end $$;
```

Then give owners a deliberate way to hand over: promote someone else first, then step down. That is a two-step process customers understand, and it removes a category of support request that otherwise arrives as an urgent email from a company whose owner has left.

## Switching Between Organisations

As soon as one person can belong to two organisations, every screen needs to know which one they are working in.

The common mistake is to keep the active organisation only in the browser - in `localStorage` or a React context - and send it with each request as a parameter the server trusts. A user who edits that parameter is asking for another organisation's data, and the only thing standing between them and it is the policy. If the policies are right, they get nothing; but "the policies are right" is the assumption the IDOR article in this series is about.

The robust arrangement:

- The active organisation is chosen in the interface and sent with requests.
- The server, or the policy, verifies membership in that organisation on every request - never trusting the parameter alone.
- The organisation switcher shows only organisations the user is a member of, read from `memberships`, not a cached list.
- URLs include the organisation where it helps - `/app/org/{id}/invoices` - so a link shared between colleagues opens the right context, and a link opened by someone without membership shows a clear "no access" rather than an empty page.

## Seats, Billing and Domains

Membership is where pricing per user meets the database.

**Seat limits** are enforced on the server at two points: when an invitation is created, and when it is accepted. Checking only at invitation lets an organisation create twenty invitations while under the limit and have all twenty accepted. Count pending invitations towards the limit, or check again at acceptance.

**Billing changes** follow membership changes. If you charge per seat, adding or removing a member should update the subscription quantity - through the provider's API, with proration as described in the refunds and proration article in this series - rather than waiting for someone to notice at renewal.

**Domain-based joining** - anyone with an `@company.nl` address may join without an invitation - is convenient for larger customers and dangerous by default. Offer it only when the organisation has verified ownership of the domain, never for free email providers, and make joined users land as members rather than admins.

## Audit What Membership Changes

Who invited whom, who accepted, who changed a role, who removed someone. These events are what a customer's administrator asks about when something goes wrong, and what a security questionnaire asks whether you record.

A single `audit_events` table with the actor, the organisation, the action, the target and a timestamp covers it, as the audit trail article in extra-11 describes. Write the event in the same transaction as the change, so the log cannot disagree with the data.

Show the organisation's own events to its admins. "Members" with a history tab answers a large share of the questions that otherwise reach your support inbox.

## Migrating From a Single Column

For a product already in production with `profiles.organisation_id`, the migration is mechanical if done in order.

1. Create `organisations`, `memberships` and `invitations` alongside the existing column.
2. Backfill: one membership per existing profile, with the role it effectively had - usually owner for the person who signed up, member for anyone added later.
3. Rewrite every policy to use `is_member()` instead of comparing with the profile column. This is the largest step; list every table first.
4. Update the frontend to read the active organisation from memberships.
5. Run both for a period, then drop the column once nothing reads it.

Test the policy rewrite with two accounts in two organisations, attempting every read and write across the boundary - the cross-account test the IDOR article in this series recommends. It is the only reliable way to know the new policies hold.

## Setting This Up

For a Lovable product adding teams, this is typically two to four days: separate organisations, memberships and invitations tables with roles on the membership, row level security rewritten around a `security definer` membership helper with the supporting index, invitation tokens that are random, hashed, expiring, single-use, revocable and bound to the invited email, acceptance in a single transaction, the edge cases handled - existing accounts, mismatched addresses, duplicates, expiry - removal that deletes the membership, ends sessions and revokes personal credentials while keeping the person's work, a database guard against ownerless organisations, server-verified organisation switching, seat limits enforced at invitation and acceptance, billing quantity kept in step, and membership events written to an audit log.

LaunchStudio builds this when a single-user product gets its first team customer. The engineers are Manifera's - eleven years, 120+ engineers, 160+ projects, from Amsterdam and Ho Chi Minh City.

[Ask us what removing a user in your product actually does](https://launchstudio.eu/en/#contact).

## Real example

### Thirty-Seven People Who Had Left

Joost Verhagen built Werkbonapp in Lovable: digital work orders for installation companies, used by 48 companies with around 600 technicians.

Team support had been added with an invite button and an `organisation_id` column on each profile. The invite link contained the organisation's ID and never expired; anyone who opened it and signed up joined that company. Removing a technician hid them from the team list and set a flag, but left the column - and their access through the API - untouched.

Two things surfaced the problem in the same month. A subcontractor who worked for two installers could not be added to the second, because a profile could hold only one organisation, and had been given a second email address as a workaround. And an installer noticed work orders being viewed by an account they had removed four months earlier.

Three business days: memberships and invitations tables created, with all 600 profiles backfilled into memberships; row level security rewritten across 17 tables around a membership helper, verified with a cross-organisation test suite; invitation tokens replaced with random, hashed tokens expiring after seven days, single-use and bound to the invited email; every outstanding old-style invite link invalidated; removal rebuilt to delete the membership, sign out the user's sessions and revoke their calendar feed tokens, while keeping their work orders attributed as "former member"; a last-owner guard in the database; seat counts checked at invitation and acceptance; and membership events written to an audit log visible to each company's admins.

**Result:** the backfill identified 37 removed technicians across 11 companies who still had working access, all revoked on the first day; logs showed four of them had used it after removal. Subcontractors can now belong to several installers with one login, and two installers upgraded to larger plans within the month because adding subcontractors had become possible.

> *"Removing someone took them off the screen and nothing else. Thirty-seven people who had left still had access, and four of them had used it."*
> - **Joost Verhagen, Founder, Werkbonapp (Hengelo)**

**Cost & Timeline:** €3,400 (membership and invitation model with backfill, policy rewrite across 17 tables with cross-organisation tests, secure invitation tokens, removal with session revocation, last-owner guard, seat enforcement, membership audit log) - completed in 3 business days.

## Frequently Asked Questions

### Why not just put an organisation ID on the user profile?

Because people belong to more than one organisation, roles belong to the relationship rather than the person, and pending invitations need somewhere to live. A memberships table handles all three; a column handles none.

### What makes an invitation link secure?

A long random token stored only as a hash, an expiry of around seven days, single use, revocation, and a check that the person accepting signs in with the email address that was invited.

### What should removing a team member do?

Delete the membership, end their sessions, revoke personal credentials such as API keys and calendar tokens, and log the change - while keeping the work they created attributed to them.

### How do I avoid the infinite recursion error in membership policies?

Put the membership check in a `security definer` function and call it from your policies, rather than having a policy on `memberships` query `memberships` directly.

### How should seat limits be enforced?

On the server, both when an invitation is created and when it is accepted, counting pending invitations - and with the billing quantity updated whenever membership changes.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why use a memberships table instead of an organisation column on profiles?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "People belong to several organisations, roles belong to the relationship, and pending invitations need their own record - a column supports none of these."
      }
    },
    {
      "@type": "Question",
      "name": "How do I make team invitation links secure?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use long random tokens stored as hashes, a seven-day expiry, single use, revocation, and require acceptance from the invited email address."
      }
    },
    {
      "@type": "Question",
      "name": "What should removing a team member do?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Delete the membership, end sessions, revoke personal credentials and log it, while keeping their past work attributed."
      }
    },
    {
      "@type": "Question",
      "name": "How do I avoid infinite recursion in Supabase membership policies?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Move the membership check into a security definer function and call that from policies instead of querying memberships inside its own policy."
      }
    },
    {
      "@type": "Question",
      "name": "Where should seat limits be enforced?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "On the server at both invitation and acceptance, counting pending invitations, with billing quantity updated on every membership change."
      }
    }
  ]
}
</script>
