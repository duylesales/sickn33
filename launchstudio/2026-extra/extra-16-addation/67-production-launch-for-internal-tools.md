---
Title: "Production Launch for Internal Tools"
Keywords: internal tool production launch, ai built internal tool security, employee app access control, internal dashboard company sso, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Production Launch for Internal Tools

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Production Launch for Internal Tools",
  "description": "A guide to taking an internal tool built with Lovable, Bolt, v0, Cursor or Claude Code into everyday production use inside a company: access through company accounts, roles by department, protecting business data, connections to existing systems, approval of the tool by IT, backups, ownership when the builder leaves, documentation and what LaunchStudio does to make internal tools safe and maintainable.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-10-01",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/production-launch-for-internal-tools" },
  "citation": [
    { "@type": "CreativeWork", "name": "Microsoft Entra ID: Single sign-on", "url": "https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/what-is-single-sign-on" },
    { "@type": "CreativeWork", "name": "Supabase: Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" },
    { "@type": "CreativeWork", "name": "NCSC Netherlands", "url": "https://www.ncsc.nl/" },
    { "@type": "CreativeWork", "name": "OWASP Top 10", "url": "https://owasp.org/www-project-top-ten/" }
  ]
}
</script>

Some of the most useful AI-built apps never reach the public. An operations manager builds a planning board for the warehouse. A finance controller builds a tool to approve supplier invoices. A sales lead builds a dashboard that combines CRM data with stock levels. A facility manager builds an app to log building issues. These internal tools often start as weekend experiments and become part of how a company works within weeks.

That success creates a new kind of risk. The tool now holds business data, sometimes personal data about colleagues or customers. It may connect to the CRM, the ERP or the accounting system with powerful credentials. It runs in the personal account of the person who built it. IT may not know it exists. And when the builder goes on holiday, changes role or leaves the company, nobody knows how to keep it running.

This page explains what it takes to turn an AI-built internal tool into a properly managed part of the company, and what LaunchStudio does to get it there.

## Key Takeaways

- **Internal does not mean low risk;** internal tools often hold the most sensitive business data.
- **Login through company accounts** gives IT control and removes access automatically when people leave.
- **Ownership must move to the company,** not stay with the builder's personal accounts.
- **Connections to business systems** need scoped, server-side credentials.
- **Typical price: €1,500-€3,500 within Launch Ready,** or Launch & Grow for tools with several integrations.

## Why Internal Tools Need Production Work

| Risk | Typical situation |
| --- | --- |
| Personal ownership | Tool, database and hosting in the builder's private accounts |
| Shared passwords | One login used by the whole team |
| Former employees keep access | No link to the company's account management |
| Broad credentials | A CRM or ERP admin key used by the tool |
| Public exposure | Tool reachable on the internet without strong login |
| No backups | Data lost if the database is deleted or corrupted |
| No documentation | Nobody else understands how it works |
| Shadow IT | IT and privacy officers unaware of the tool and its data |
| Unclear data processing | Personal data stored without the company's privacy documentation |

## Company Accounts and Single Sign-On

The single most effective step for an internal tool is login through the company's existing accounts, typically Microsoft Entra ID or Google Workspace. Employees use the account they already have, MFA policies apply automatically and access disappears when IT disables the account of someone who leaves. Access can be restricted to specific groups, such as the finance department, managed by IT rather than by the tool's builder.

We implement single sign-on with the company's identity provider and, where useful, map groups to roles in the tool. For small companies without a central identity provider, we use secure logins with MFA and an admin who can remove users.

## Roles by Department

Internal tools often start with everyone seeing everything. As usage grows, that stops being acceptable: salary-related data, supplier terms, customer complaints and performance figures should be visible only to the people who need them. We define roles with you, such as viewer, editor, approver and admin, scoped by department or team where needed, and enforce them through database policies so that a direct request to the backend cannot bypass them.

## Moving Ownership to the Company

When an employee builds a tool in their own Lovable, Supabase, Vercel or GitHub account, the company does not own it. If that person leaves, access, billing and data may leave with them. We move every component into accounts owned by the company, with the builder invited as a collaborator, document the inventory and make sure billing runs through the company. This step often matters most to managers and IT.

## Connecting to Business Systems Safely

Internal tools are valuable because they combine data from systems such as the CRM, ERP, accounting, HR or warehouse software. Builders often connect them with whatever credentials work, sometimes an administrator API key pasted into the code. We move connections server-side, create dedicated integration accounts with the minimum permissions needed, rotate exposed keys, add logging and handle errors and retries so that a temporary outage does not corrupt data. Where the tool writes back to business systems, writes are made idempotent and, for important actions, require confirmation.

## Getting IT and Privacy on Board

In many companies, a useful internal tool eventually meets the IT department or privacy officer. That meeting goes better when the tool is already in company accounts, uses company login, stores data in an EU region, has documented data flows and keeps backups. We provide a short overview that answers typical questions: what data the tool holds, where it is hosted, who has access, which systems it connects to and how it is maintained. That turns a potential "shut it down" into "let's support it".

## Internal Doesn't Mean Private

Many internal tools are reachable on the public internet, protected only by a login page. That is normal for modern web apps, but it means the tool faces the same threats as any public app: password guessing, exploited vulnerabilities and misconfigured access rules. Company SSO, rate limiting, security headers and updated dependencies matter just as much as for customer-facing apps. Where required, access can be further restricted, for example to company networks, though that can limit mobile and remote use.

## What LaunchStudio Does for Internal Tools

| Area | Typical work |
| --- | --- |
| Ownership | All accounts and billing moved to the company, documented inventory |
| Login | SSO with Microsoft or Google, group-based access, or MFA logins |
| Roles | Department and function roles enforced in the database |
| Integrations | Server-side, scoped credentials, logging and idempotent writes |
| Data protection | EU hosting, data minimisation, documentation for the privacy officer |
| Reliability | Staging, pipeline, backups with restore test, monitoring |
| Documentation | How the tool works, how to maintain it and who owns what |
| Continuity | Project instructions for AI tools so others can continue development |

## The Builder's Role After Launch

The colleague who built the tool usually remains its champion and often keeps improving it with AI tools. That is a good thing, as long as changes go through staging, follow the project rules and do not undo access controls. We set up the workflow so the builder can keep contributing safely, and so a second colleague, or an external partner, can take over when needed. Under Launch & Grow, we provide monitoring, updates and reviews of larger changes for €49 per month.

## What We Need From You

- A 15-minute intro call with the tool's builder and, ideally, someone from IT or management
- Access to the tool's accounts, repository and connected systems' sandbox or test environments
- Information about the company's identity provider and IT policies
- Decisions on roles and data access

## Price and Timeline

| Scope | Typical tool | Indicative price | Duration |
| --- | --- | --- | --- |
| Single-team tool | One department, simple roles, no integrations | €1,500-€2,200 | 4-5 business days |
| Department tool with integration | SSO, roles, one business system connection | €2,200-€3,500 | 6-10 business days |
| Cross-department platform | Several integrations, approvals, audit trail | Within Launch & Grow (€2,500-€7,500 plus €49 per month) | 2-4 weeks |

The quote is fixed after an assessment. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an indication.

## Not Included

We do not change your identity provider's configuration beyond what is needed for the tool, manage your company's IT policies or provide legal advice on employee data. Licence costs for business systems and identity providers are paid by your company. Large-scale replacement of existing business systems is outside the scope.

## Audit Trails for Approvals

Internal tools often handle approvals: supplier invoices, expense claims, purchase orders, leave requests, price changes. When money or commitments are involved, the company needs to know who approved what and when, both for internal control and for the accountant. AI-built tools usually record only the current status. We add an append-only history of approvals and important changes, showing the user, time, previous value and new value, with an export for audits. Where rules exist, such as a second approval above a certain amount, they are enforced on the server rather than only in the interface.

## Backups and Recovery for Business Data

Because internal tools quickly become the place where work happens, losing their data can stop a department. Default backups on free plans may be limited or absent. We make sure the database runs on a plan with appropriate backups, test a restore to a separate environment and document how to recover from common mistakes, such as a colleague deleting the wrong records. For tools that write to business systems, we also check that the source systems remain the authority, so the internal tool can be rebuilt from them if necessary.

## Keeping Internal Tools Out of Search

Internal tools should never appear in search results or AI answers. We block indexing, require login on every route and make sure no internal data is exposed through public pages, previews or shared links.

## Costs Over Time

Internal tools are cheap to run compared with commercial software, but costs still exist: hosting and database plans, AI tool subscriptions for the people improving it and occasional maintenance. Moving billing to the company makes these visible and predictable. Under Launch & Grow, ongoing care costs €49 per month, which is often less than a single seat of commercial software the tool replaces.

## When an Internal Tool Should Become a Product

Sometimes an internal tool turns out to be valuable for other companies too. If you are thinking about selling it, the production work for internal use, such as roles, SSO, integrations and documentation, is a good start, but a commercial product also needs multi-tenancy, billing and customer onboarding. We can plan that transition, so the internal version keeps running while the product version is prepared.

## Why Companies Choose LaunchStudio

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, building internal systems and integrations for clients such as Vodafone and TNO. Teams meet us at Herengracht 420 in Amsterdam; engineering happens at Manifera's development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore. We move your tool into company ownership, connect it to your systems safely and keep the builder's momentum going.

## Real example

### An AI-Native Founder in Action: The Planning Board That Lived in a Personal Account

Johan Vermeer is operations manager at a mid-sized transport company in Tiel. Frustrated with spreadsheets, he built Ritbord with Bolt and Supabase, a planning board that showed trucks, drivers and deliveries, pulled orders from the company's transport management system and let planners drag deliveries between routes. Within two months, twelve planners used it daily and the managing director called it indispensable.

When Johan went on a three-week holiday, the IT manager discovered the tool. It ran in Johan's personal Supabase and Bolt accounts, paid with his own credit card. Planners shared a single login. The connection to the transport management system used an administrator API key stored in a client-side function, and drivers' phone numbers and home addresses were visible to anyone with the login. There were no backups beyond the default and no documentation.

LaunchStudio quoted €3,100 within Launch Ready. All components moved into company accounts with company billing and Johan as collaborator. Login switched to the company's Microsoft accounts, with access limited to the planning and management groups. Roles separated planners, managers and drivers, with drivers seeing only their own routes on their phones. The transport system connection moved to a scheduled server function with a dedicated, read-and-limited-write account, and the admin key was rotated. Drivers' home addresses were removed from the board, backups were tested, staging was set up and documentation explained how the tool worked.

**Result:** The IT manager approved Ritbord as an official company tool. Johan continued improving it with Bolt through the staging workflow, and when he was on leave again, a colleague made a small change confidently using the documentation.

> *"I built the tool in an evening. It took a holiday to realise the company depended on my personal credit card and one shared password."*
> - **Johan Vermeer, Operations Manager, Ritbord (Tiel)**

**Cost & Timeline:** €3,100 (Launch Ready package: ownership transfer, Microsoft SSO, roles, secured TMS integration, data minimisation, backups, staging and documentation) - completed in 8 business days.

## Frequently Asked Questions

### Do internal tools really need production work?

Yes, once colleagues depend on them or they hold business or personal data. Internal tools often have broad access to business systems and sensitive information, and they frequently run in personal accounts without backups or proper login. A focused production project fixes these risks.

### Can employees log in with their company Microsoft or Google accounts?

Yes. We implement single sign-on with the company's identity provider, map groups to roles where useful and make sure access disappears when IT disables an account.

### What happens to the tool if the person who built it leaves?

After the project, the tool belongs to the company: accounts, billing, code and data are in company ownership, documented and maintainable by others. The builder can keep contributing as a collaborator while employed.

### How does Manifera's experience help with internal tools?

Manifera has built internal systems and integrations for 11+ years across 160+ projects with 120+ engineers, for clients such as Vodafone and TNO. LaunchStudio applies that experience to make AI-built internal tools secure, owned and maintainable.

### Do internal tools affect SEO and AI visibility?

They should not be indexed at all. We make sure internal tools are excluded from search engines and AI crawlers, so internal pages and data never appear in search results or AI answers.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do internal tools really need production work?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes once colleagues depend on them or they hold sensitive data." }
    },
    {
      "@type": "Question",
      "name": "Can employees log in with their company Microsoft or Google accounts?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, through SSO with group-based roles." }
    },
    {
      "@type": "Question",
      "name": "What happens to the tool if the person who built it leaves?",
      "acceptedAnswer": { "@type": "Answer", "text": "It belongs to the company, documented and maintainable by others." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with internal tools?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has 11+ years building internal systems and integrations." }
    },
    {
      "@type": "Question",
      "name": "Do internal tools affect SEO and AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "They should be excluded from indexing so internal data never appears." }
    }
  ]
}
</script>
