---
Title: "How Do I Hand My AI-Built App to a Developer?"
Keywords: hand over ai-built app, onboard developer lovable app, developer handover document, ai codebase onboarding, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# How Do I Hand My AI-Built App to a Developer?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How Do I Hand My AI-Built App to a Developer?",
  "description": "Bringing a developer into an AI-built codebase goes faster with the right preparation. This guide lists what to share, how to grant access safely, what to write down and how to structure the first week so the developer becomes productive quickly.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-10",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-hand-my-ai-built-app-to-a-developer" }
}
</script>

**Short answer:** before the developer starts, make sure the code is in a GitHub repository you own, collect a list of every service the app uses, write a one-page description of how the product works and what must not break, and prepare a staging environment they can safely experiment in. Grant access through their own accounts with the least privileges needed, never by sharing your passwords. Then plan the first week around understanding, not new features.

## Why Handovers of AI-Built Apps Go Wrong

Developers joining an AI-built codebase face specific problems: code that nobody wrote deliberately, logic spread across components and database policies, few comments, no tests and a founder who knows the product deeply but not the code. Without preparation, the first weeks are spent reverse-engineering, and many developers then propose a rewrite.

## What to Prepare

**1. The repository.** Code synced to GitHub under a company organisation. See our [GitHub export guide](https://launchstudio.eu/en/blog/how-to-export-lovable-code-to-github-and-keep-building).

**2. A systems list.**

| Service | Purpose | Account owner | Developer access needed? |
| --- | --- | --- | --- |
| GitHub | Code | Company | Yes, write |
| Supabase | Database, auth, storage | Company | Staging: yes; production: read-only at first |
| Vercel/Netlify | Hosting | Company | Yes |
| Stripe/Mollie | Payments | Company | Test mode only at first |
| Email provider | Transactional email | Company | Usually no |
| Domain registrar | DNS | Company | No |

**3. A product page.** One page in plain language: who the users are, the main flows, what earns money, and the three things that must never break.

**4. Known issues.** What you already know is wrong or fragile. Developers appreciate honesty more than a polished pitch.

**5. Staging.** A safe environment with test data where they can break things. See our [staging guide](https://launchstudio.eu/en/blog/how-do-i-set-up-a-staging-environment-for-a-lovable-app).

## Granting Access Safely

- Invite the developer with their own account to each service
- Give production access only when needed, and read-only first
- Never share your personal login or secret keys in chat
- Remove access promptly when the engagement ends, and rotate any secrets they saw

## The First Week

| Day | Focus |
| --- | --- |
| 1 | Walkthrough call: product, users, flows; developer explores code and staging |
| 2 | Developer maps the architecture and lists questions |
| 3 | Short Q&A; developer writes or updates a README with setup steps |
| 4 | A small, low-risk fix through the full process (branch, review, staging, production) |
| 5 | Developer proposes priorities: risks, quick wins, things to leave alone |

Starting with a small fix proves the whole pipeline before anything important changes.

## Agree on How You Will Keep Using AI Tools

Decide whether you will keep prompting in Lovable or Bolt, on which branch, and which areas are off limits. Most conflicts between founders and developers in AI-built projects come from both changing the same files without coordination.

## Getting the Handover Ready

LaunchStudio's production work produces exactly this foundation: code in your repository, documented services, staging, migrations and an operating document. LaunchStudio is backed by Manifera, which writes handover documentation as standard practice in its 11+ years of client delivery, with teams in Ho Chi Minh City and client contact in Amsterdam; see [Manifera's offshore development teams](https://www.manifera.com/services/offshore-software-development/). GitHub's guide on [writing a good README](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) is a helpful reference.

## Real example

### An AI-Native Founder in Action: The Developer Who Wanted to Start Over

Inge Brinkhuis built Opvangplan in Lovable: a scheduling and parent communication tool for small childcare centres. After a year with eight centres, she hired a freelance developer for two days a week. After his first week, he recommended rewriting everything in a different framework, estimating three months.

Inge asked LaunchStudio for a second opinion. The code was workable; the developer had struggled because nothing was documented: the repository was on Inge's personal account, the database had policies created both by prompts and by hand, there was no staging, and he had been given Inge's own Supabase login.

LaunchStudio moved the repository to a company organisation, reconciled the database into migrations, set up staging with test data, wrote a README and an operating document with a systems list and known issues, and set up individual access for the developer. Inge and the developer agreed that Lovable would only be used for interface changes on `main`.

**Result:** The developer withdrew the rewrite proposal. Within a month he had shipped a long-requested attendance export and fixed two known issues, all through staging.

> *"He didn't need a new framework. He needed a map of what I'd built and somewhere safe to try things."*
> - **Inge Brinkhuis, Founder, Opvangplan (Amersfoort)**

**Cost & Timeline:** €2,250 (repository transfer, migration reconciliation, staging, README, operating document and access setup) - completed in 6 business days.

## Frequently Asked Questions

### What should I give a developer who joins my Lovable project?

Access to a GitHub repository you own, a list of services and accounts, a plain-language product description, known issues and a staging environment. Grant access through their own accounts with limited privileges.

### Why do developers often want to rewrite AI-built apps?

Because undocumented AI-generated code is hard to understand quickly, and rewriting feels safer than learning it. Good preparation and a staging environment usually show that targeted improvements are faster than a rewrite.

### Should I share my passwords with a developer?

No. Invite them with their own accounts to each service. Shared logins make it impossible to see who did what and difficult to remove access later.

### How does Manifera onboard engineers onto existing codebases?

With a standard package: repository access, systems map, operating document, staging and a small first task through the full process. Manifera's 11+ years of taking over client projects made this routine.

### Does documentation affect my product's online presence?

Public documentation, such as help pages and API docs, can be indexed and cited by AI assistants. Internal handover documents should stay private, but they make it easier to keep public information accurate.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What should I give a developer who joins my Lovable project?",
      "acceptedAnswer": { "@type": "Answer", "text": "Repository access, a services list, a product description, known issues and staging, with their own limited accounts." }
    },
    {
      "@type": "Question",
      "name": "Why do developers often want to rewrite AI-built apps?",
      "acceptedAnswer": { "@type": "Answer", "text": "Undocumented code is hard to learn quickly; preparation and staging usually make targeted improvements faster." }
    },
    {
      "@type": "Question",
      "name": "Should I share my passwords with a developer?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. Use individual accounts to keep accountability and easy removal." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera onboard engineers onto existing codebases?",
      "acceptedAnswer": { "@type": "Answer", "text": "Repository access, systems map, operating document, staging and a small first task." }
    },
    {
      "@type": "Question",
      "name": "Does documentation affect my product's online presence?",
      "acceptedAnswer": { "@type": "Answer", "text": "Public docs can be cited by AI assistants; internal handover docs help keep public information accurate." }
    }
  ]
}
</script>
