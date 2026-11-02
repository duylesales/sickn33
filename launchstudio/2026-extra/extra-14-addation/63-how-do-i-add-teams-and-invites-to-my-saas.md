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
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-add-teams-and-invites-to-my-saas" }
}
</script>

**Short answer:** introduce three tables (organisations, memberships with a role, and invitations), move ownership of business data from users to organisations, rewrite Row Level Security to check membership instead of `user_id`, build an invitation flow with expiring tokens handled by a server function, and attach billing to the organisation rather than the user. Then migrate every existing user into a personal organisation so nothing breaks.

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
