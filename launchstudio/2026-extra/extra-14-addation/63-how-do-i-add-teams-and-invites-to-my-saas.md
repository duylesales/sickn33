---
Title: "How Do I Add Teams and Invitations to My AI-Built SaaS?"
Keywords: add teams to saas, team invitations supabase, organisations lovable app, b2b saas accounts, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: SaaS Founder Scale-Up
---

# How Do I Add Teams and Invitations to My AI-Built SaaS?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How Do I Add Teams and Invitations to My AI-Built SaaS?",
  "description": "Moving from single users to teams is the step that turns a tool into a B2B SaaS. This guide covers the data model, invitation flow, roles, billing per organisation and the migration of existing single-user accounts in a Supabase-backed app.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-11",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-add-teams-and-invites-to-my-saas" },
  "citation": [
    { "@type": "CreativeWork", "name": "OWASP Authorization Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html" },
    { "@type": "CreativeWork", "name": "Supabase: Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A01 Broken Access Control", "url": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/" },
    { "@type": "CreativeWork", "name": "GDPR Article 28: Processor", "url": "https://gdpr-info.eu/art-28-gdpr/" }
  ]
}
</script>

**Short answer:** introduce three tables (organisations, memberships with a role, and invitations), move ownership of business data from users to organisations, rewrite Row Level Security to check membership instead of `user_id`, build an invitation flow with expiring tokens handled by a server function, and attach billing to the organisation rather than the user. Then migrate every existing user into a personal organisation so nothing breaks.

## Key Takeaways

- **Adding teams turns a single-user tool into a B2B SaaS:** data moves from belonging to users to belonging to organisations.
- **Three tables do most of the work:** organisations, memberships with roles and invitations with expiring tokens.
- **Every Row Level Security policy changes** from `user_id = auth.uid()` to membership checks through a helper function.
- **Billing attaches to the organisation,** with seat limits enforced in the invitation flow.
- **Existing users migrate into personal organisations,** so nothing breaks for current customers.

## Why This Is a Bigger Change Than It Looks

Most AI-built apps start with "each user owns their data" (`user_id = auth.uid()`). Teams change the question to "which organisation owns this data, and is this user a member with the right role?" That touches the data model, every policy, billing and the interface. It is very doable; it should just be planned as one change, not prompted feature by feature.

## The Data Model

| Table | Key columns |
| --- | --- |
| `organisations` | id, name, plan, billing customer ID |
| `memberships` | organisation_id, user_id, role (owner, admin, member) |
| `invitations` | organisation_id, email, role, token hash, expires_at, accepted_at |
| Business tables | add `organisation_id`, keep `created_by` for history |

## Policies

Replace ownership checks with membership checks through a helper function, for example `is_member(organisation_id)` for reading and `has_org_role(organisation_id, 'admin')` for managing members or billing. Our article on [roles and admin panels](https://launchstudio.eu/en/blog/how-to-add-roles-and-an-admin-panel-to-a-lovable-app) shows the helper function pattern.

## The Invitation Flow

1. An admin enters an email and role
2. A server function checks the admin's role, creates an invitation with a random token (stored hashed) and an expiry date, and sends an email
3. The invitee clicks the link, signs up or logs in
4. A server function verifies the token, checks the email matches, creates the membership and marks the invitation as accepted

Rules worth enforcing: invitations expire, can be revoked, can only be accepted once, and limits apply to prevent abuse.

## Roles That Cover Most B2B Needs

| Role | Can |
| --- | --- |
| Owner | Everything, including billing and deleting the organisation |
| Admin | Manage members and settings |
| Member | Use the product |

Start with these; add custom roles only when customers ask.

## Billing Per Organisation

Attach the Stripe or Mollie customer to the organisation. Decide whether you charge per seat, per organisation or by usage, and enforce seat limits in the invitation function.

## Migrating Existing Users

Create a personal organisation for every existing user, make them owner, and set `organisation_id` on their records in a migration. Test on staging with a copy of realistic data before running in production.

## Why Teams Increase Revenue

B2B customers buy for teams, not individuals. Team accounts raise average revenue per customer through seats or tiered plans, improve retention because switching tools affects many people, and open doors to larger companies. They also introduce expectations: roles, invitations, shared data, admin controls and billing that matches how companies buy. Planning these together avoids a patchwork of features that never quite fit.

## Designing the Membership Model

A membership model answers three questions: who belongs to which organisation, with which role, and what each role may do. Keep it simple at first:

| Role | Typical permissions |
| --- | --- |
| Owner | Billing, deleting the organisation, everything an admin can do |
| Admin | Inviting and removing members, changing roles (except owner), settings |
| Member | Using the product within the organisation |

Store roles in the memberships table, never on the user's profile where they could be edited. Enforce permissions in Row Level Security policies and server functions, using helper functions such as `is_member(org_id)` and `has_role(org_id, 'admin')`. OWASP's Authorization Cheat Sheet recommends exactly this pattern: centralised, server-side, deny-by-default checks.

## Users in Multiple Organisations

Consultants, agencies and freelancers often belong to several customer organisations. Support this from the start: let users switch between organisations, show the current organisation clearly in the interface and include the organisation ID in every query. Policies based on membership naturally handle multi-organisation users, as long as every table that holds organisation data has an `organisation_id` column.

## Invitation Edge Cases

Real-world invitations raise questions worth answering before launch:

- **Invitee already has an account:** link the invitation to the existing account on acceptance
- **Invitee uses a different email:** decide whether to allow acceptance with a different address; safer to require the invited email
- **Invitation expires:** show a clear message and let admins resend
- **Seat limit reached:** block the invitation with a message suggesting an upgrade
- **Member removed:** revoke access immediately and decide what happens to content they created

Handling these cases explicitly prevents both security holes and frustrated customers.

## Data Ownership When Members Leave

When someone leaves a company, their account should lose access to the organisation's data, but the data itself usually belongs to the organisation and must remain. Keep `created_by` for history, transfer ownership of items where needed and never delete organisation content because one member left. For GDPR purposes, the individual's personal data, such as their profile, can be deleted or anonymised, while organisation records remain under the customer's control as controller.

## Organisation-Level Settings and Security

Business customers often want controls: requiring two-factor authentication for all members, restricting sign-in to their email domain, viewing an audit log of member changes and exporting their data. These features are often the difference between a pilot and a signed contract with a larger customer. Build them on the same membership model, enforced server-side.

## Migration Without Disruption

Migrating existing single-user accounts is usually the riskiest part. Write the migration as a script that creates one organisation per user, makes the user owner and sets `organisation_id` on all their records. Rehearse it on a staging copy with realistic data, verify that each user sees exactly their previous data and nothing else, then run it in production during a quiet period. Update policies in the same release so there is no window where data is unprotected.

## Billing Models for Teams

| Model | How it works | Best for |
| --- | --- | --- |
| Per seat | Price per active member, quantity updated on invite or removal | Collaboration tools where every user gets value |
| Tiered plans | Fixed price for up to N members | Simpler pricing, predictable invoices |
| Per organisation | One price regardless of members | Products where only a few users per company are active |
| Usage-based | Price per transaction, document or action | Products whose value scales with volume |

Attach the subscription to the organisation, let only owners or billing admins change it, and enforce limits on the server: an invitation that would exceed the seat limit should fail with a clear upgrade message.

## Testing a Team Setup

Before launching team features, test with at least two organisations and three roles. Verify that members of one organisation cannot see the other's data through the interface or the API, that members cannot invite others or change roles, that admins cannot remove the owner, that expired or revoked invitations cannot be accepted and that removing a member revokes their access immediately. Automate the cross-organisation test so future changes cannot silently break it.

## Communicating the Change to Existing Users

When existing single users gain team features, explain what changed: their data now lives in a personal workspace they own, they can invite colleagues, and billing may move to the workspace. Most users welcome the change, especially when it unlocks collaboration they wanted. Clear in-app messages and a short email reduce confusion.

## Common Mistakes

- Adding a teams table without changing existing policies
- Storing roles on profiles that users can edit
- Attaching subscriptions to individual users in a team product
- Forgetting `organisation_id` on newly added tables
- Allowing invitations to be accepted by a different email without checks

## Enterprise Features That Follow

Once teams work, larger customers ask for more: single sign-on with their identity provider, SCIM user provisioning, custom roles, data export and audit logs covering all member activity. You do not need these on day one, but designing the membership model cleanly makes them much easier to add. Keep membership changes in one place, log them consistently and avoid hard-coding role names throughout the interface.

## Performance Considerations

Membership checks run on almost every query. Index `memberships` on `(user_id, organisation_id)` and `organisation_id` columns on every data table. Use helper functions with a fixed `search_path` and wrap `auth.uid()` so it is evaluated once per query. Without these, team features can make an app noticeably slower as organisations grow.

## Related Reading

Our guides on roles and admin panels, single-tenant versus multi-tenant SaaS and Stripe subscriptions cover the closely related decisions in more depth.

## Summary

Model organisations and memberships first, move data ownership to organisations, rewrite policies around membership, build a secure invitation flow, attach billing to the organisation and migrate existing users carefully. Done as one planned change, teams become the foundation for B2B growth rather than a source of bugs.

## A Rollout Plan

Week one: design the data model and policies, write the migration and test it on staging with realistic data. Week two: build invitations, roles in the interface and organisation billing, test cross-organisation access thoroughly. Release with existing users migrated into personal organisations, announce the new team features and monitor closely for a week. Two weeks of focused work is typical for a small SaaS.

## Questions to Answer First

Who can invite members? Can a user belong to several organisations? What happens to content when a member leaves? How is billing calculated? Answer these before building, and the implementation follows naturally.

## Getting It Built

Adding organisations, invitations and organisation billing is a typical LaunchStudio engagement of €2,500-€5,500, depending on the number of tables and billing model. Behind LaunchStudio is Manifera's team of 120+ engineers, who have built multi-tenant B2B systems for 11+ years from Ho Chi Minh City, Singapore and Amsterdam; see [Manifera's web app development](https://www.manifera.com/services/web-app-develop/). Supabase's [RLS guide](https://supabase.com/docs/guides/database/postgres/row-level-security) covers membership-based policies.

## Real example

### An AI-Native Founder in Action: The Freelancer Tool That Agencies Wanted to Share

Rianne Mulders built Uurwerk in Lovable: a time tracking and invoicing tool for freelance designers. It grew to 600 users. Then small design agencies started asking for team accounts: shared clients, shared projects and one invoice. Rianne tried prompting "add teams", which created a teams table but left every policy based on `user_id`, so team members still could not see shared projects, and one attempt made all projects visible to everyone.

LaunchStudio designed organisations, memberships and invitations, added `organisation_id` to clients, projects, time entries and invoices, rewrote all policies around membership, built the invitation flow with expiring tokens and seat limits, moved Stripe customers to organisations with per-seat pricing, and migrated the 600 existing users into personal organisations over a weekend.

**Result:** Existing freelancers noticed nothing except a new "Invite team" button. Within three months, 34 agencies were on team plans, and average revenue per account roughly doubled.

> *"Teams sounded like one feature. It turned out to be a new foundation under every feature I already had."*
> - **Rianne Mulders, Founder, Uurwerk (Tilburg)**

**Cost & Timeline:** €4,700 (Launch Ready package extended: organisations, memberships, invitations, policy rewrite, per-seat billing and user migration) - completed in 13 business days.

## Frequently Asked Questions

### Can I add teams to my Lovable app with prompts?

You can generate parts of it, but teams change the data model, every access policy and billing at once. Prompting it piece by piece often leaves policies inconsistent. Planning it as one change, ideally with an engineer, is safer.

### Should data belong to users or organisations in B2B SaaS?

To organisations, with users as members. Keep a `created_by` column for history, but grant access based on membership. This makes it possible for people to leave a company without taking its data with them.

### How do I make invitation links secure?

Use random tokens stored hashed, expiry dates, single use, a check that the accepting user's email matches, and server-side verification. Allow admins to revoke pending invitations.

### How does Manifera approach multi-tenant SaaS design?

With membership-based access enforced in the database, organisation-level billing and a migration plan for existing users. Manifera's 11+ years of B2B systems make this a familiar design rather than an experiment.

### Do team features affect how AI assistants recommend my SaaS?

They can. Business buyers often ask assistants for tools "for teams" or "with user roles". Documenting team features, roles and per-seat pricing on public pages gives assistants the facts to match you.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I add teams to my Lovable app with prompts?",
      "acceptedAnswer": { "@type": "Answer", "text": "Partly, but teams change the data model, policies and billing together; plan it as one change." }
    },
    {
      "@type": "Question",
      "name": "Should data belong to users or organisations in B2B SaaS?",
      "acceptedAnswer": { "@type": "Answer", "text": "To organisations, with membership-based access and created_by for history." }
    },
    {
      "@type": "Question",
      "name": "How do I make invitation links secure?",
      "acceptedAnswer": { "@type": "Answer", "text": "Hashed random tokens, expiry, single use, email match and server-side verification, with revocation." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera approach multi-tenant SaaS design?",
      "acceptedAnswer": { "@type": "Answer", "text": "Membership-based database access, organisation billing and planned user migration." }
    },
    {
      "@type": "Question",
      "name": "Do team features affect how AI assistants recommend my SaaS?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Documented team features and per-seat pricing help assistants match business queries." }
    }
  ]
}
</script>
