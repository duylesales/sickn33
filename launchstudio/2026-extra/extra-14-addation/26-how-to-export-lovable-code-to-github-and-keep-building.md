---
Title: "How to Export Lovable Code to GitHub and Keep Building"
Keywords: export lovable code to github, lovable github sync, lovable code ownership, continue lovable project, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: Technical Solo Founder / Indie Hacker
---

# How to Export Lovable Code to GitHub and Keep Building

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Export Lovable Code to GitHub and Keep Building",
  "description": "Connecting Lovable to GitHub gives you ownership of your code and lets you keep building in Lovable, Cursor or with a developer. This guide covers the sync, branching, secrets, conflicts and a workflow that keeps Lovable and hand-written changes from overwriting each other.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-03",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-to-export-lovable-code-to-github-and-keep-building" },
  "citation": [
    { "@type": "CreativeWork", "name": "GitHub: About protected branches", "url": "https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches" },
    { "@type": "CreativeWork", "name": "OWASP Secrets Management Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html" },
    { "@type": "CreativeWork", "name": "GitHub Actions documentation", "url": "https://docs.github.com/en/actions" },
    { "@type": "CreativeWork", "name": "Lovable documentation", "url": "https://docs.lovable.dev/" }
  ]
}
</script>

**Short answer:** connect your Lovable project to GitHub from Lovable's GitHub integration. Lovable creates a repository under your GitHub account and keeps it in two-way sync: changes made in Lovable are pushed to GitHub, and commits pushed to the synced branch appear back in Lovable. From then on, the code is yours, and you can keep building in Lovable, in Cursor or with a developer, as long as you agree on a workflow so the different sources of changes do not overwrite each other.

The setup takes minutes. The workflow is what makes it last.

## Key Takeaways

- **Connect your Lovable project to GitHub** through Lovable's integration; the repository stays in two-way sync with the branch Lovable uses.
- **Create the repository under a company organisation,** not a personal account, so the code clearly belongs to the business.
- **Scan for secrets before sharing access.** A key deleted in a later commit still exists in git history and must be rotated.
- **Choose a working model** - Lovable-first, branch-and-merge or hand-over - and agree on who changes what to avoid overwriting each other's work.
- **Protect logic Lovable should not rewrite** by moving it into database policies, database functions and edge functions, and by documenting protected files.

## Step 1: Connect to GitHub

1. Open your project in Lovable and find the GitHub integration in the project settings or toolbar.
2. Authorise Lovable to access your GitHub account or organisation.
3. Choose where the repository should be created. **Use a company GitHub organisation**, not a personal account, if the product belongs to a company.
4. Lovable creates the repository and pushes the current code.

Check the repository on GitHub. You should see your frontend code and, if you use Supabase, a `supabase` folder with migrations and edge functions.

## Step 2: Understand What the Sync Does

- Lovable commits to the repository's synced branch, usually `main`, whenever you make changes.
- Commits pushed to that branch from elsewhere are pulled into Lovable.
- Other branches are not automatically part of Lovable's working state.

This means `main` is shared territory. Anything pushed there by you, a developer or a tool like Cursor becomes Lovable's starting point for the next prompt.

## Step 3: Keep Secrets Out of the Repository

Before inviting anyone else, check the repository for secrets:

- Search for `sk_live`, `service_role`, `secret`, `api_key` and your provider names.
- Look in `.env` files and configuration files.
- Remember that removing a secret in a new commit does not remove it from history.

If any secret was committed, **rotate it** at the provider. Public keys designed for the browser, such as the Supabase anon or publishable key, are fine; secret keys are not. Our article on whether the [Supabase anon key is safe](https://launchstudio.eu/en/blog/is-the-supabase-anon-key-safe) explains the difference.

## Step 4: Choose a Working Model

| Model | How it works | Best for |
| --- | --- | --- |
| Lovable-first | Most changes in Lovable; developers make small, coordinated commits to `main` | Non-technical founders with occasional help |
| Branch and merge | Developers work on feature branches, review, then merge to `main` | Founders working with a developer or team |
| Hand-over | Lovable used less or not at all; development continues in an IDE | Products outgrowing prompt-based changes |

Most growing products move from the first to the second model.

## Step 5: Protect the Parts Lovable Should Not Rewrite

The most common problem after export: a developer fixes something carefully, then a Lovable prompt regenerates the same file and the fix disappears. To prevent that:

- **Move sensitive logic out of components.** Access control belongs in Supabase policies and edge functions, not in React components that Lovable frequently regenerates.
- **Document protected files.** Keep a short `README` section or a Lovable knowledge entry listing files and folders that prompts should not change.
- **Review Lovable's commits.** Treat them like a junior developer's pull requests: look at the diff before deploying.
- **Use staging.** Deploy `main` to a staging environment first, so a regression is caught before customers see it.

## Step 6: Deploy From GitHub

With the code in GitHub, you can deploy through a pipeline instead of publishing from the builder: Vercel or Netlify for the frontend, Supabase migrations applied through CI, environment variables per environment. That gives you previews, rollbacks and a record of what went live when.

## Why Git Matters More Than It Seems

For a non-technical founder, GitHub can feel like a developer tool you will never need. In practice, it is the single most important ownership step for an AI-built product. Git gives you a complete history of every change, the ability to restore any previous version, a place where developers can review and collaborate, and an independent copy of your code outside the builder. Investors and acquirers ask about code ownership; a repository in your company's GitHub organisation is the clearest answer.

## Branching Basics for Founders

A branch is a parallel line of work. Lovable usually works on `main`. A developer can create a branch, such as `fix-invoice-rounding`, make changes there and open a pull request: a proposal to merge those changes into `main`, which can be reviewed and tested first. GitHub's documentation on protected branches explains how to require reviews or passing checks before anything merges into important branches. For a small team, a simple rule works well: Lovable on `main`, developers on feature branches, and a separate `production` branch that only receives tested changes.

## Handling Secrets Properly

OWASP's Secrets Management Cheat Sheet recommends storing secrets in a dedicated secret store, never in source code, and rotating them after any exposure. For a Lovable project that means:

- Frontend environment variables contain only public values, such as the Supabase URL and publishable key
- Secret keys for payments, email or AI providers live in Supabase edge function secrets or your host's secret settings
- `.env` files with real values are listed in `.gitignore` and never committed
- A secret found in history is rotated at the provider, and optionally removed from history with a history-rewriting tool

GitHub's secret scanning can also alert you when known key formats are pushed to a repository.

## Code Review for AI-Generated Changes

When Lovable commits to your repository, each commit can be reviewed like a junior developer's work. You do not need to read every line. Focus on changes in four places: `supabase/migrations` (database and policies), `supabase/functions` (server logic), configuration files and anything touching payments or authentication. A quick look after each building session catches most risky changes, such as a new policy that grants broad access or a key added to frontend code.

## Continuous Integration

With code in GitHub, you can add automated checks that run on every change: building the app, linting for errors such as case-mismatched imports, type checking and a few end-to-end tests. If a check fails, the change does not reach production. This is one of the most effective protections against regressions introduced by prompts, and it costs little once set up.

## Documentation That Lives With the Code

Add a README to the repository with how to run the app, which environment variables are needed (names only), where the backend lives and which files or folders prompts should not modify. Keep a short `docs/` folder with the systems map and release procedure. Documentation in the repository travels with the code, which makes onboarding any future developer faster.

## When to Stop Using Lovable for a Part of the App

Over time, some parts of your app may be better maintained by hand: complex calculations, integrations with external systems, performance-critical queries. It is normal for a mature product to use Lovable for interface work while developers own specific modules. Mark those modules clearly in documentation and Lovable's project knowledge so prompts leave them alone. This hybrid model keeps the speed of AI-assisted building where it helps and the stability of hand-maintained code where it matters.

## Releases and Rollbacks

Once your code lives in GitHub and deploys through a host such as Vercel or Netlify, every deployment is tied to a specific commit. That gives you something the builder's publish button cannot: the ability to roll back instantly to the last known good version when a change causes problems. Practise a rollback once on staging so you know the steps before you need them under pressure. Pair it with additive database migrations, meaning you add new columns or tables rather than renaming or deleting existing ones in the same release, so that rolling back the app does not break the database.

## Working With More Than One Developer

As your product grows, you may have a freelancer for backend work, an agency for a mobile app and yourself in Lovable. GitHub keeps this manageable: each person works on their own branch, pull requests show what changed and why, and automated checks protect the main branch. Agree on naming conventions for branches, who approves merges and how often `main` is promoted to production. Small agreements like these prevent the confusion that otherwise appears as soon as a second contributor joins.

## A Simple Weekly Routine

Once a week, spend fifteen minutes in GitHub: skim the commits from Lovable and any developers, check that automated checks passed, confirm staging matches what you expect and promote tested changes to production. This small habit gives a non-technical founder real oversight of the codebase without needing to read code in depth, and it surfaces surprises while they are still small.

## Handling Conflicts

If Lovable and a developer change the same file around the same time, you can get conflicts or surprising results. Keep it simple: agree on who works on what, pull before you push, and when in doubt, let the developer resolve conflicts in an IDE and push the result to `main`, where Lovable will pick it up.

## Getting Help With the Transition

Setting up the repository, cleaning secrets, introducing branches and staging, and moving sensitive logic out of regenerated files is a common first step in LaunchStudio engagements. It usually fits within a Launch Ready package (€800-€3,500). Our engineers have shipped 160+ projects for enterprise clients through Manifera, and they work in your repository, never their own. See [Manifera's technologies](https://www.manifera.com/about-us/manifera-technologies/) for the tools involved, and GitHub's own guide to [protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) for the branch side.

## Real example

### An AI-Native Founder in Action: The Kitchen Quote Generator That Kept Losing Fixes

Jeroen Vink sells and installs kitchens in Ede. He built Keukenofferte in Lovable: customers configure a kitchen layout, choose fronts and worktops, and get an indicative quote; Jeroen's team turns it into a final offer. He connected the project to GitHub and hired a freelance developer to fix the price calculation, which rounded VAT incorrectly.

The fix worked for three days. Then Jeroen asked Lovable to add a new worktop material, and Lovable regenerated the quote component, bringing the rounding error back. It happened twice more with other fixes. The repository was also under Jeroen's personal GitHub account, and the freelancer had committed a `.env` file with the email provider's secret key.

LaunchStudio moved the repository into a company GitHub organisation, rotated the exposed key and cleaned the history, and moved the price calculation into a Postgres function in Supabase, which Lovable's frontend now called instead of calculating prices itself. Engineers added a staging deployment from `main`, a short protected-files list in Lovable's knowledge settings, and a feature-branch workflow for the freelancer.

**Result:** Jeroen kept adding materials and options in Lovable without breaking prices again. Over the next four months, Keukenofferte produced around 540 quotes, and the freelancer's work stopped disappearing.

> *"Every time I asked Lovable for something new, it quietly undid something old. Moving the important logic out of its reach fixed that."*
> - **Jeroen Vink, Founder, Keukenofferte (Ede)**

**Cost & Timeline:** €1,450 (Launch Ready package: repository migration, key rotation, price logic in database function, staging and workflow) - completed in 6 business days.

## Frequently Asked Questions

### Do I own the code Lovable generates?

Generally yes, under Lovable's terms the code you generate is yours to use. Connecting to GitHub puts a copy in a repository you control, which is what makes ownership practical. Always check the current terms for details.

### Can I stop using Lovable after exporting to GitHub?

Yes. The repository contains a standard React project, usually with Vite, Tailwind and Supabase. Any developer can continue with it in an IDE such as Cursor or VS Code. Many founders keep using Lovable for interface work and developers for backend changes.

### Why do my developer's fixes disappear after I prompt Lovable?

Because Lovable may regenerate the files containing those fixes. Moving critical logic into database functions, policies or edge functions, documenting protected files and reviewing Lovable's commits prevents most of these regressions.

### How does Manifera's engineering practice apply to a Lovable repository?

Manifera works with branches, reviews, staging environments and documented handovers on every client project. LaunchStudio applies the same practices to Lovable repositories, so a founder's codebase is ready for any developer or team to continue.

### Does exporting to GitHub help my app's search visibility?

Not directly. What helps is the deployment pipeline GitHub enables: stable production releases on your own domain, with server-rendered or well-structured pages that search engines and AI assistants can crawl reliably.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I own the code Lovable generates?",
      "acceptedAnswer": { "@type": "Answer", "text": "Generally yes under Lovable's terms. Connecting to GitHub puts the code in a repository the founder controls; check current terms for details." }
    },
    {
      "@type": "Question",
      "name": "Can I stop using Lovable after exporting to GitHub?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. The repository is a standard React project any developer can continue in an IDE, while many founders keep Lovable for interface work." }
    },
    {
      "@type": "Question",
      "name": "Why do my developer's fixes disappear after I prompt Lovable?",
      "acceptedAnswer": { "@type": "Answer", "text": "Lovable may regenerate those files. Move critical logic to database functions, policies or edge functions, document protected files and review Lovable's commits." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's engineering practice apply to a Lovable repository?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera's branches, reviews, staging and documented handovers are applied to Lovable repositories so any developer can continue." }
    },
    {
      "@type": "Question",
      "name": "Does exporting to GitHub help my app's search visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirectly, through stable production releases on your own domain that search engines and AI assistants can crawl reliably." }
    }
  ]
}
</script>
