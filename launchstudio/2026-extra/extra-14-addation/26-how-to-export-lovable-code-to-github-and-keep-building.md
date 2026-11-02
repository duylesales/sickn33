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
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-to-export-lovable-code-to-github-and-keep-building" }
}
</script>

**Short answer:** connect your Lovable project to GitHub from Lovable's GitHub integration. Lovable creates a repository under your GitHub account and keeps it in two-way sync: changes made in Lovable are pushed to GitHub, and commits pushed to the synced branch appear back in Lovable. From then on, the code is yours, and you can keep building in Lovable, in Cursor or with a developer, as long as you agree on a workflow so the different sources of changes do not overwrite each other.

The setup takes minutes. The workflow is what makes it last.

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
