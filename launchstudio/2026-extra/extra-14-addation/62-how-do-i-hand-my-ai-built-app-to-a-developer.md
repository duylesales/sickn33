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
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-hand-my-ai-built-app-to-a-developer" },
  "citation": [
    { "@type": "CreativeWork", "name": "GitHub: About READMEs", "url": "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes" },
    { "@type": "CreativeWork", "name": "OWASP Secrets Management Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html" },
    { "@type": "CreativeWork", "name": "GDPR Article 28: Processor", "url": "https://gdpr-info.eu/art-28-gdpr/" },
    { "@type": "CreativeWork", "name": "GitHub: About protected branches", "url": "https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches" }
  ]
}
</script>

**Short answer:** before the developer starts, make sure the code is in a GitHub repository you own, collect a list of every service the app uses, write a one-page description of how the product works and what must not break, and prepare a staging environment they can safely experiment in. Grant access through their own accounts with the least privileges needed, never by sharing your passwords. Then plan the first week around understanding, not new features.

## Key Takeaways

- **Prepare before the developer starts:** repository in your company's GitHub, a systems list, a one-page product description, known issues and a staging environment.
- **Grant access through individual accounts with least privilege;** never share your own logins or secret keys in chat.
- **Plan the first week around understanding,** ending with a small fix shipped through the full process.
- **Agree how AI tools and the developer will share the codebase,** to avoid overwriting each other's work.
- **Good preparation prevents rewrite proposals,** which often come from undocumented code rather than bad code.

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

## Why Onboarding Time Matters

Every hour a developer spends reverse-engineering your app is an hour you pay for without new value. In AI-built codebases, that time can be substantial: logic spread across components, policies and functions, few comments and no tests. Good preparation shortens it dramatically. It also changes the developer's first impression of the codebase, which influences whether they propose targeted improvements or a full rewrite.

## The Systems List in Detail

For each service your app uses, record:

| Field | Example |
| --- | --- |
| Service | Supabase |
| Purpose | Database, authentication, storage, edge functions |
| Environments | Staging project, production project |
| Account owner | Company organisation, admin email |
| Region | Frankfurt (EU) |
| Who has access | Founder (owner), developer (staging write, production read) |
| Secrets | Stored in edge function secrets and host settings |
| Notes | Daily backups, PITR enabled |

Repeat for hosting, domain, payments, email, analytics, error tracking and AI providers. This table answers half of a new developer's questions on day one, and doubles as your sub-processor list for GDPR purposes.

## Least-Privilege Access

Give developers what they need, not everything. Typical starting access: write access to the repository, full access to staging, read-only or no access to production data, test-mode access to payment providers and no access to the domain registrar. Expand access when a specific task requires it, and remove it when the engagement ends. OWASP's guidance on secrets management recommends rotating credentials when people with access leave; include that in your offboarding routine.

## Contracts and Confidentiality

Before granting access, have a written agreement covering intellectual property (code belongs to your company), confidentiality, data protection and handover obligations. If the developer will see personal data, a data processing agreement under Article 28 of the GDPR may be required, depending on the arrangement. Freelancers and agencies usually have standard templates; read them for IP clauses, which sometimes default to the developer retaining rights.

## Explaining the Product Well

Developers build better when they understand why. In your product page, describe the customer and their problem, the main user journeys in plain steps, how the business makes money and which three things must never break. Include screenshots or a short screen recording of the main flows. Ten minutes of explanation saves hours of misinterpretation.

## Defining Done

Agree what "done" means for each task: code merged through review, tested on staging, documentation updated, no new errors in monitoring after release. Clear definitions prevent misunderstandings about whether work is finished, which are a common source of friction between founders and developers.

## Communication Rhythm

A simple rhythm works for most collaborations: a short written update from the developer at the end of each working day or session, a weekly call to review progress and priorities, and a shared task list visible to both. Agree response times for urgent issues. For developers in other time zones, written updates matter even more and allow work to continue across the day.

## Ending an Engagement Cleanly

When the engagement ends, ensure all work is merged and documented, remove the developer's access to every service, rotate any secrets they handled and update the systems list. A clean exit makes it easy to bring the same person back later, or to onboard someone new without starting from zero.

## What Developers Wish Founders Knew

Developers joining AI-built projects consistently mention the same wishes. They want to know which parts are fragile before touching them, which decisions were deliberate and which were accidental, which areas the founder will keep changing in Lovable and how quickly they can get answers to questions. They also want permission to say "this part needs restructuring" without it being read as criticism of the founder. A short conversation covering these points on day one builds trust quickly.

## Documentation Worth Writing Before Day One

| Document | Contents | Time to write |
| --- | --- | --- |
| README | How to run, configure and deploy the app | 1-2 hours |
| Systems list | Every service, owner, region, access | 1 hour |
| Product page | Users, flows, money, must-not-break items | 1 hour |
| Known issues | Bugs, fragile areas, postponed work | 30 minutes |
| Decisions log | Why key choices were made | 30 minutes, then ongoing |

Five short documents, written in a single afternoon, often save a week of developer time.

## Common Handover Mistakes

- Sharing the founder's own login instead of individual accounts
- Leaving the repository on a personal account
- Giving production database access on day one without need
- Expecting new features in week one before the developer understands the system
- Continuing to prompt in the same files the developer is changing, without coordination

## Measuring Whether the Handover Worked

After two weeks, check: can the developer deploy a change through staging without help? Have they fixed at least one known issue? Can they explain the architecture in their own words? Have they added to the documentation? If the answers are yes, the handover succeeded and you can start planning features with confidence.

## Using AI Tools Together With the Developer

Many founders keep using Lovable after a developer joins, which works well with clear boundaries. Agree that Lovable changes interface files on `main`, while the developer owns policies, functions and integrations through branches and pull requests. Add those boundaries to Lovable's project knowledge so prompts respect them. Review Lovable's commits together for the first few weeks; it quickly shows both of you where the boundaries need adjusting.

## Related Reading

Our guides on exporting Lovable code to GitHub, staging environments and preventing prompts from breaking security cover the setup that makes developer handovers smooth.

## Summary

Own the repository and accounts, write five short documents, prepare staging, grant least-privilege access, start with understanding and a small fix, and agree how AI tools and the developer share the codebase. A handover prepared this way turns a new developer into a productive contributor within days instead of weeks.

## The Payoff

A prepared handover shows developers that you take the product seriously, earns their respect and gets them building value in days rather than spending weeks deciphering what exists.

## One More Tip

Record a ten-minute screen video walking through the app and its admin areas. Developers revisit it more often than any document.

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
