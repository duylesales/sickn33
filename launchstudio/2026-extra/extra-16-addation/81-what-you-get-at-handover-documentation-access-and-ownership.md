---
Title: "What You Get at Handover: Documentation, Access and Ownership"
Keywords: project handover documentation, software handover checklist, what to receive from developer, code ownership after project, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# What You Get at Handover: Documentation, Access and Ownership

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What You Get at Handover: Documentation, Access and Ownership",
  "description": "An explanation of what founders receive at the end of a LaunchStudio project for an app built with Lovable, Bolt, v0, Cursor or Claude Code: ownership of code and accounts, an account inventory, a written summary, architecture and data documentation, procedures for releases, rollback and restore, project instructions for AI tools, tests, monitoring, access removal and how to use the handover pack with future developers, customers and investors.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-10-15",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/what-you-get-at-handover-documentation-access-and-ownership" },
  "citation": [
    { "@type": "CreativeWork", "name": "GitHub: Transferring a repository", "url": "https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository" },
    { "@type": "CreativeWork", "name": "Anthropic: Claude Code memory and project instructions", "url": "https://docs.anthropic.com/en/docs/claude-code/memory" },
    { "@type": "CreativeWork", "name": "Cursor: Rules", "url": "https://docs.cursor.com/context/rules" },
    { "@type": "CreativeWork", "name": "Diátaxis: A systematic approach to technical documentation", "url": "https://diataxis.fr/" }
  ]
}
</script>

The end of a software project is where many founders discover what they actually bought. Some receive a working app and a well-organised set of documents that let them, or anyone else, continue confidently. Others receive a link, a few passwords in an email and a supplier who is the only person who understands how things work. The difference shows up months later: when something breaks, when a new developer joins, when an investor asks for due diligence or when a customer sends a security questionnaire.

At LaunchStudio, the handover is a defined deliverable in every Launch Ready and Launch & Grow project. This page explains exactly what you receive, why each part matters and how to use it after we finish.

## Key Takeaways

- **You own everything:** code, accounts, data and domain are in your company's name.
- **An account inventory** lists every service, who owns it and who has access.
- **A written summary** explains what was reviewed, fixed and left open.
- **Procedures** for releases, rollback and restore let you act without us.
- **Project instructions for your AI tool** keep future changes consistent with the work done.

## Ownership: Nothing to Transfer at the End

We work in your accounts from the start: your repository, your hosting, your database, your payment and email providers, your domain. When accounts were in someone else's name, such as a former freelancer, a co-founder's personal account or an agency, we move them into your company's ownership during the project. At handover, there is nothing left to transfer, because everything was already yours. That is the most important property of a good handover, and the one founders most often overlook until it is too late.

## The Account Inventory

The account inventory is a single document listing every service the app depends on:

| Column | Example |
| --- | --- |
| Service | Supabase, Vercel, Stripe, Postmark, GitHub, domain registrar |
| Purpose | Database and auth, hosting, payments, email, code, domain |
| Owner account | Company account name and email |
| Plan and billing | Plan name, billed to company card |
| Region | Data location where relevant |
| Who has access | Named users and roles |
| Critical settings | For example backups enabled, DMARC policy |
| Notes | Renewal dates, limits, contacts |

This inventory is valuable well beyond the project. It answers due diligence questions, helps your accountant understand recurring costs, makes onboarding a new developer faster and forms the basis of your subprocessor list for data protection documents.

## The Written Summary

The summary explains, in plain language, what we found, what we changed and what remains. It typically covers the scope of the review, findings grouped by area with severity, fixes applied, accepted risks with recommended dates, measures now in place, such as database policies, private storage, backups and monitoring, and recommended next steps. It is written so you can share it, or a version of it, with customers, investors or a future technical lead. Sensitive details that could help an attacker are kept in an internal annex.

## Architecture and Data Documentation

A short architecture description explains how the pieces fit together: frontend, backend functions, database, storage, external services, background jobs and how data flows between them. A data overview lists the main tables, what they contain, which personal data they hold, how access is controlled and how long data is kept. This documentation does not need to be long; it needs to be accurate and current, so a developer or auditor can understand the system in an hour rather than a week.

## Procedures You Can Follow Without Us

| Procedure | What it explains |
| --- | --- |
| Releasing a change | From branch to staging to production, including migrations |
| Rolling back | Returning to the previous version quickly |
| Restoring data | Restoring from backup, including partial recovery |
| Rotating a secret | Where secrets live and how to replace them |
| Adding a user or collaborator | Giving access with the right role |
| Removing access | Steps when someone leaves |
| Responding to an incident | First steps, who to inform, where to look |

Each procedure is written step by step for a non-specialist, with screenshots or commands where helpful. We walk through the most important ones with you during the handover call, and usually practise a rollback together.

## Project Instructions for Your AI Tool

Most founders keep building with Lovable, Bolt, v0, Cursor or Claude Code after the project. Without guidance, these tools can undo the work: loosening a database policy to fix an error, placing a key in the browser or bypassing the payment webhook. We leave project instructions in your repository, in the formats the tools read, such as Cursor rules or a CLAUDE.md file for Claude Code, describing the architecture, conventions, security rules, how to write migrations and what never to do. Founders consistently tell us their AI tool behaves more predictably afterwards.

## Tests That Protect the Work

Automated tests are part of the handover. They typically cover access control between users and organisations, payment events including duplicates and failures and the key journeys of your app. The tests run in the pipeline on every change, so if you or your AI tool break an important rule, the build fails before customers are affected. Tests are documentation too: they show precisely what the app is supposed to do.

## Monitoring and Alerts

Monitoring and alerting are configured in your accounts and send alerts to you, and to us if you choose Launch & Grow. The handover includes an overview of what is monitored, where to look and what each alert means, so an alert at night is understandable rather than alarming.

## Access Removal

At the end of the project, we remove or reduce our access at your request and confirm it in writing. If you continue with Launch & Grow, we keep the access needed for ongoing care, documented in the inventory. Either way, you can see exactly who has access to what.

## The Handover Call

The handover ends with a call of about an hour, in which we walk through the summary, the inventory, the main procedures and the AI tool instructions, answer questions and agree on any open points. Founders often invite a co-founder, a freelancer or the person who will maintain the app. The call is recorded if you wish, so others can watch it later.

## How Founders Use the Handover Pack

- **Due diligence:** investors receive the summary, inventory and architecture overview.
- **Security questionnaires:** answers draw on the summary and data overview.
- **Hiring:** a new developer reads the documentation and tests before their first change.
- **Customer conversations:** a public security page is based on the summary.
- **Your own peace of mind:** when something breaks, you know where to look.

## What a Weak Handover Looks Like

If you have worked with other suppliers, compare: a weak handover is a set of passwords in an email, accounts in the supplier's name, no written explanation of what was done, no procedures, no tests and an implicit expectation that you will call them for every change. That is not necessarily dishonest, but it creates dependency. Ask any supplier, before you sign, what you will receive at the end.

## Keeping Documentation Current

Documentation loses value when it drifts from reality. A simple habit helps: update the inventory when you add or remove a service, update the architecture notes when you add a major feature and review the summary's open points every few months. Under Launch & Grow, we keep documentation current as part of ongoing care and include changes in the monthly health note.

## Where Everything Lives

The handover pack is stored where you can always find it: usually a folder in your repository for technical documentation and AI instructions, plus a shared document space of your choice for the summary and inventory. Nothing important sits only in our systems or in email threads. If you ever stop working with us, you lose nothing.

## Handover for Teams

When a founder has a co-founder, a freelancer or an in-house developer, the handover is shared with them as well. Developers usually want the architecture overview, test instructions and AI project rules first; co-founders and managers want the summary, inventory and costs. We tailor the walkthrough to the people attending and can hold a separate technical session for developers who will take over day-to-day work.

## What We Need From You

- Time for the handover call, ideally with anyone who will work on the app later
- A place where you want documents stored
- Confirmation of which access we should keep or remove

## Price

The handover is included in every project:

| Package | Price |
| --- | --- |
| Launch Ready | €800-€3,500 fixed, including handover and 48 hours of post-launch support |
| Launch & Grow | €2,500-€7,500 fixed, plus €49 per month, including handover and ongoing documentation updates |

Use the [price calculator](https://launchstudio.eu/en/#calculator) for an indication.

## Costs and Renewals in One Place

Founders are often surprised by how many small subscriptions and renewals an app depends on: a database plan, hosting, an email provider, monitoring, a domain renewing every year, perhaps an AI provider and a video host. The inventory lists each with its plan, billing method and renewal date, so nothing expires unexpectedly and your accountant can see the full picture of recurring costs. Under Launch & Grow, renewals and plan limits are part of the platform watch in the monthly service.

## Questions to Ask Any Supplier About Handover

Before you sign with any supplier, ask: in whose name will the accounts be? What documents will I receive? Will there be procedures for releases, rollback and restore? Will tests stay in my repository? Will my AI tool receive instructions? How is access removed at the end? A supplier who answers clearly and specifically is planning for your independence. A supplier who is vague may be planning for your dependency, intentionally or not.

## A Living Document

Treat the handover pack as a living document rather than a final report. Each time the app changes meaningfully, a few lines of updated documentation keep it trustworthy for the next person who needs it.

## Why Founders Choose LaunchStudio

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, handing over and maintaining systems for clients such as Vodafone and TNO. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at Manifera's development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore. Our handovers are designed so you never depend on us, which is exactly why many founders choose to keep working with us.

## Real example

### An AI-Native Founder in Action: Due Diligence in an Afternoon

Wouter van Beek runs a maintenance planning SaaS for housing cooperatives from Zwolle, built with Bolt and Supabase. A year after a Launch & Grow project with LaunchStudio, a larger property software company offered to acquire his business. Its technical team sent a due diligence request: who owns the code and accounts, which services are used and where data is stored, how the app is secured, what tests exist, how releases and backups work and what technical risks remain.

Wouter opened the handover pack. The account inventory, kept current under the ongoing service, listed every service with owner, region and access. The written summary and its annex described the security measures, findings and accepted risks with their status. The architecture and data overview explained the system and personal data flows. Procedures showed how releases, rollbacks and restores worked, and the pipeline history showed tests running on every change. The monthly health notes provided a year of evidence of uptime, updates and incidents.

Wouter answered the questionnaire in an afternoon. The acquirer's engineers asked for one additional walkthrough of the database policies, which LaunchStudio provided in a one-hour call.

**Result:** The technical due diligence closed in less than two weeks, with no findings that affected the price. The acquirer's CTO said the documentation was more complete than that of most companies of a similar size they had reviewed.

> *"I thought due diligence would take a month and cost me sleep. It took an afternoon, because everything I needed was already written down and in my name."*
> - **Wouter van Beek, Founder, Onderhoudsplanner (Zwolle)**

**Cost & Timeline:** Handover included in the original €4,200 Launch & Grow project, plus €49 per month for ongoing care with documentation updates - due diligence completed within two weeks.

## Frequently Asked Questions

### What do I receive at the end of a LaunchStudio project?

Ownership of code and accounts in your company's name, an account inventory, a written summary, architecture and data documentation, procedures for releases, rollback, restore and access, project instructions for your AI tool, automated tests, monitoring and a recorded handover call if you wish.

### Who owns the code after the project?

You do. We work in your repository and accounts from the start, so there is nothing to transfer at the end. Access for our team is removed or reduced at your request.

### Can another developer continue after you?

Yes. The documentation, tests and AI instructions are written so any competent developer, or you with your AI tool, can continue. Many founders hand the pack to a freelancer or first hire.

### How does Manifera's experience shape the handover?

Manifera has handed over and maintained systems for 11+ years across 160+ projects with 120+ engineers, for clients such as Vodafone and TNO. LaunchStudio's handover follows the same principle: the client must be able to continue without the supplier.

### Does the handover help with SEO and AI visibility?

Indirectly. The inventory and procedures make sure domain, redirects, sitemaps and monitoring stay correctly configured as the app evolves, and the summary can feed a public security page that helps search engines and AI answer engines describe your product accurately.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What do I receive at the end of a LaunchStudio project?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ownership, inventory, summary, documentation, procedures, AI instructions, tests, monitoring and a handover call." }
    },
    {
      "@type": "Question",
      "name": "Who owns the code after the project?",
      "acceptedAnswer": { "@type": "Answer", "text": "You do; we work in your accounts from the start." }
    },
    {
      "@type": "Question",
      "name": "Can another developer continue after you?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; documentation, tests and AI instructions make it possible." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience shape the handover?",
      "acceptedAnswer": { "@type": "Answer", "text": "It follows the principle that clients must be able to continue without the supplier." }
    },
    {
      "@type": "Question",
      "name": "Does the handover help with SEO and AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirectly, by keeping technical SEO settings documented and supporting a security page." }
    }
  ]
}
</script>
