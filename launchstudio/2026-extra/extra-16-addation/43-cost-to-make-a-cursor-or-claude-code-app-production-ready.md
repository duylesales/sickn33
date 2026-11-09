---
Title: "Cost to Make a Cursor or Claude Code App Production Ready"
Keywords: cursor app production ready cost, claude code app launch cost, vibe coded nextjs app production, fix ai generated codebase cost, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Cost to Make a Cursor or Claude Code App Production Ready

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cost to Make a Cursor or Claude Code App Production Ready",
  "description": "A cost guide for making apps built with Cursor or Claude Code production ready: typical price ranges, the issues common in code-first AI projects such as inconsistent architecture, custom authentication, missing tests, dependency sprawl, environment handling and deployment, what each fix involves, ongoing costs and how to keep your AI coding workflow productive afterwards.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-09-07",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/cost-to-make-a-cursor-or-claude-code-app-production-ready" },
  "citation": [
    { "@type": "CreativeWork", "name": "Cursor documentation", "url": "https://docs.cursor.com/" },
    { "@type": "CreativeWork", "name": "Anthropic: Claude Code documentation", "url": "https://docs.anthropic.com/en/docs/claude-code/overview" },
    { "@type": "CreativeWork", "name": "Next.js: Deploying", "url": "https://nextjs.org/docs/app/building-your-application/deploying" },
    { "@type": "CreativeWork", "name": "OWASP Application Security Verification Standard", "url": "https://owasp.org/www-project-application-security-verification-standard/" }
  ]
}
</script>

**Short answer:** Making an app built with Cursor or Claude Code production ready typically costs €1,200 to €2,000 for a focused app with one stack and few integrations, €2,000 to €3,500 for a SaaS with authentication, payments and several services, both within Launch Ready, and €3,500 to €7,500 within Launch & Grow when the codebase needs structural consolidation, migrations or enterprise features. Code-first AI projects tend to cost slightly more than visual builder projects of similar size, because they have more freedom to diverge: several patterns for the same task, custom authentication and many dependencies.

Cursor and Claude Code give founders a different kind of power than visual builders. You work in a real codebase, choose your own framework, database and hosting, and can build almost anything. Many non-technical founders have shipped impressive products this way. The flip side is that nothing enforces consistency. After months of sessions, a codebase can contain three ways of fetching data, two authentication approaches, unused libraries, hard-coded secrets in old scripts and no tests. This page explains what it costs to turn that into a codebase you can launch and keep building on.

## Key Takeaways

- **Typical cost: €1,200-€3,500 within Launch Ready,** more for structural consolidation.
- **Code-first projects vary more** than visual builder projects, so the review matters.
- **Common fixes:** authentication, access control, secrets, dependencies, tests, environments and deployment.
- **Your AI workflow stays,** with project rules that keep future sessions consistent.
- **Most projects take five to ten business days.**

## Cost by Type of Project

| Project type | Typical stack | Indicative price | Duration |
| --- | --- | --- | --- |
| Focused web app | Next.js or similar, Supabase, one hosting provider | €1,200-€2,000 | 4-6 business days |
| SaaS with payments and emails | Next.js, Supabase or PostgreSQL, Stripe or Mollie, email provider | €2,000-€3,500 | 6-10 business days |
| App with separate backend | Frontend plus Node, Python or other API, several services | €2,500-€3,500, or Launch & Grow | 1-3 weeks |
| Codebase needing consolidation | Mixed patterns, several databases or auth systems, large scope | Within Launch & Grow (€2,500-€7,500 plus €49 per month) | 2-4 weeks |

## Issues Common in Code-First AI Projects

| Issue | How it shows up | Why it matters |
| --- | --- | --- |
| Inconsistent architecture | Several ways to fetch data, validate input or handle errors | Bugs in one path but not another; hard to secure |
| Custom or mixed authentication | Homemade sessions next to a provider, or two providers | Account takeover risks, broken logins |
| Missing authorisation checks | API routes that check login but not ownership | Users can access others' data |
| Secrets in code or history | Keys in config files, scripts or old commits | Exposed credentials |
| Dependency sprawl | Dozens of libraries, some unused or outdated | Vulnerabilities, slow builds, larger bundles |
| No tests | Every change risks breaking something unnoticed | Regressions reach customers |
| Environment confusion | Same keys for development and production, missing variables | Test actions affect live data |
| Manual deployment | Deploying from a laptop, no pipeline | Inconsistent releases, no rollback |
| Database without migrations | Schema changed by hand or by scripts | Staging and production drift apart |
| No logging or monitoring | Errors visible only in the browser console | Problems discovered by customers |

## What the Price Includes

Every Launch Ready project includes a production readiness review, security basics, an ownership check, a production setup with domain and HTTPS, backups, monitoring, agreed fixes, a written summary, project rules for Cursor or Claude Code and 48 hours of post-launch support. For code-first projects, fixes typically also include consolidating authentication, adding authorisation checks to every route, moving secrets into environment management and rotating exposed ones, removing unused dependencies, adding tests for critical flows, setting up database migrations and creating a deployment pipeline with preview environments.

## Why Code-First Projects Drift

AI coding assistants work session by session. Each session solves the task in front of it, using whatever approach seems best in that context. Without strong project rules, one session adds a data-fetching library, another writes raw queries and a third uses a different pattern again. Authentication may start with a provider and later gain a custom middleware written to fix a bug. Secrets are pasted into files to make something work quickly, then forgotten.

None of this is a failure of the tools; human teams drift too without conventions and review. The fix is to establish the conventions, consolidate the code towards them and give the AI assistant clear instructions so future sessions follow the same patterns.

## Project Rules for Your AI Assistant

One of the most valuable deliverables for Cursor and Claude Code users is a set of project rules: instructions the assistant reads in every session. Cursor supports project rules files and Claude Code reads project memory files such as CLAUDE.md. We write rules that describe your architecture, the one approved way to fetch data, how authentication and authorisation work, where secrets live, how to write migrations, which tests to run and what never to do, such as exposing service keys or disabling database policies. Founders consistently report that sessions become more predictable after these rules are in place.

## Tests: How Much Is Enough?

Founders sometimes worry that adding tests means months of work. For production readiness, a focused set is enough: tests for authentication, authorisation between users and organisations, payment state changes and the two or three journeys that matter most to your business. These run automatically in the pipeline on every change. They are the safety net that lets you keep building quickly with AI assistance without breaking what already works.

## Ongoing Costs After Launch

After launch, you pay your providers directly: hosting such as Vercel, Netlify or a container platform, your database, email, payments and AI providers if your app uses them. Your Cursor or Claude subscription continues if you keep building. Optional ongoing care through Launch & Grow costs €49 per month for monitoring, dependency updates, backup checks and small fixes. Code-first projects benefit particularly from regular dependency updates, because they usually include more libraries.

## Keeping the Price Low

- Share the repository early so the review can start immediately
- Remove experiments, abandoned branches and unused folders you know about
- List the services and accounts the app uses
- Describe user types and what each may access
- Pause large new features during the project
- Note recurring bugs or areas that feel fragile

## Consolidate or Rewrite?

When a codebase feels messy, rewriting can seem tempting. For most AI-built apps that already work, consolidation is cheaper and safer: pick the best existing pattern for each concern, move the rest of the code towards it, delete what is unused and add tests along the way. A rewrite throws away working behaviour and usually takes far longer than expected. We recommend a rewrite of a specific part only when consolidation would cost more, and we explain that before starting.

## Comparing the Alternatives

| Option | Typical cost | What you get |
| --- | --- | --- |
| Continue alone with your AI assistant | Your time and subscription | Fixes for what you know to ask; risk in unknown areas |
| Hourly freelance developer | Hourly, total uncertain | Help on chosen issues; quality varies |
| AI code review tools | Monthly subscription | Automated comments on changes; no fixes or setup |
| LaunchStudio Launch Ready | €1,200-€3,500 fixed | Review, fixes, setup, tests, rules, documentation and support |
| Full rewrite by an agency | Often many times higher | New code; usually unnecessary |

## What We Need From You

- A 15-minute intro call
- Access to your repository, including history
- Access to hosting, database, payment and email accounts
- A description of users, roles and key journeys
- Time for a check on staging before release

## Price Overview

| Package | Typical code-first work |
| --- | --- |
| Launch Ready (€800-€3,500) | Security, authentication, secrets, tests, pipeline, deployment, monitoring |
| Launch & Grow (€2,500-€7,500 plus €49 per month) | Consolidation, migrations, multi-tenancy, enterprise features, ongoing care |

Use the [price calculator](https://launchstudio.eu/en/#calculator) for an indication.

## Not Included

Launch Ready does not include new features, redesigns, provider costs or a complete rewrite. If parts of the codebase genuinely need rebuilding, we explain why and quote it separately. Legal advice, certifications and accredited penetration tests are outside the scope.

## Cleaning Secrets From Repository History

A common finding in code-first projects is a secret that was committed months ago and later removed. Removing it from the current files does not remove it from the repository history, where anyone with access, or anyone who gains access later, can still find it. The safe approach has two steps. First, rotate the secret at the provider so the old value no longer works; this is the step that actually removes the risk. Second, where appropriate, clean the history and enable secret scanning so new leaks are caught before they are pushed. We do both, and list every rotated key in the handover so you know which values changed.

## Separate Backends and Background Workers

Some Cursor and Claude Code projects include a separate backend, such as a Node or Python API, or background workers for imports, emails and AI tasks. These add moving parts: another deployment, another set of environment variables, another place where errors happen. Production readiness for these projects includes the same basics for each service: authenticated and authorised endpoints, secrets in environment management, logs and monitoring, health checks and a deployment pipeline. Where a separate service exists only because a session created it, we sometimes recommend merging it into the main app to reduce cost and complexity. That recommendation comes with a clear explanation and is never done without your approval.

## What Changes in Your Daily Workflow

After the project, your daily workflow with Cursor or Claude Code looks familiar but safer. You work on a branch, the assistant follows the project rules, the pipeline runs tests and creates a preview deployment and you merge when it looks right. Database changes arrive as migrations, applied automatically to staging and then production. If something slips through, monitoring alerts you and a rollback is a click away. Founders often say they build faster after the project, because they spend less time chasing regressions.

## Why Founders Choose LaunchStudio

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, maintaining large codebases for clients such as Vodafone and TNO. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at Manifera's development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore. We consolidate rather than rewrite, keep your product working and leave rules that make your AI assistant a better collaborator.

## Real example

### An AI-Native Founder in Action: Three Ways to Log In

Floor Bakker runs a recruitment SaaS for hospitality businesses from Utrecht, built over eight months with Cursor and later Claude Code, using Next.js, Supabase and Stripe. Restaurants post shifts and workers apply. The app had around 300 businesses and 4,000 workers, but bugs were increasing and Floor was afraid to touch certain files.

The review found three authentication paths: Supabase Auth for workers, a custom session system written during a debugging session for businesses and an old magic-link route still reachable. Several API routes checked that a user was logged in but not that the shift belonged to their business. Two Stripe keys were in a committed script, the repository included 140 dependencies of which around 30 were unused and there were no tests. Deployments happened from Floor's laptop.

LaunchStudio quoted €3,400 within Launch Ready. Authentication was consolidated on Supabase Auth with existing business accounts migrated, the old route removed and ownership checks added to every API route through a shared helper. Keys were rotated and moved to environment variables, and the repository history was cleaned. Unused dependencies were removed and the rest updated. Tests were added for login, access between businesses, applications and Stripe webhooks. A GitHub pipeline deployed previews and production on Vercel with database migrations, and project rules were written for both Cursor and Claude Code.

**Result:** Bug reports dropped noticeably in the following two months, and build times fell by around a third. Floor resumed building weekly; the tests blocked two changes that would have broken access between businesses.

> *"I had built a product I was scared of. Now I have a codebase with rules, and my AI assistant follows them better than I did."*
> - **Floor Bakker, Founder, Shiftwerk (Utrecht)**

**Cost & Timeline:** €3,400 (Launch Ready package: authentication consolidation, ownership checks, key rotation, dependency clean-up, tests, pipeline, migrations and AI project rules) - completed in 9 business days.

## Frequently Asked Questions

### How much does it cost to make a Cursor or Claude Code app production ready?

Typically €1,200 to €3,500 within Launch Ready, depending on the stack, authentication, payments, integrations and how consistent the code is. Codebases needing structural consolidation or migrations are scoped within Launch & Grow. You receive a fixed quote after reviewing the repository.

### Why can code-first projects cost more than Lovable or Bolt projects?

Because they have more freedom. Code-first projects can mix frameworks, authentication systems and patterns, which takes more time to review and consolidate. Visual builders constrain choices, which often makes their issues more predictable.

### Will I be able to keep using Cursor or Claude Code?

Yes. We work in your repository and add project rules that both tools read, describing your architecture and conventions. Tests and a pipeline catch changes that would break critical behaviour.

### How does Manifera's experience help with AI-generated codebases?

Manifera has maintained codebases for 11+ years across 160+ projects with 120+ engineers, for clients such as Vodafone and TNO. LaunchStudio applies those engineering practices to consolidate AI-generated code without rewriting working products.

### Does a production-ready codebase help SEO and AI visibility?

Yes. Faster builds, smaller bundles, correct rendering of public pages, proper metadata and fewer errors help search engines crawl and rank your site. A stable product also earns the reviews and mentions that AI answer engines pick up.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How much does it cost to make a Cursor or Claude Code app production ready?",
      "acceptedAnswer": { "@type": "Answer", "text": "Typically €1,200-€3,500 within Launch Ready; consolidation projects within Launch & Grow." }
    },
    {
      "@type": "Question",
      "name": "Why can code-first projects cost more than Lovable or Bolt projects?",
      "acceptedAnswer": { "@type": "Answer", "text": "They have more freedom to mix patterns, which takes longer to review and consolidate." }
    },
    {
      "@type": "Question",
      "name": "Will I be able to keep using Cursor or Claude Code?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, with project rules, tests and a pipeline." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with AI-generated codebases?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has 11+ years and 160+ projects maintaining codebases." }
    },
    {
      "@type": "Question",
      "name": "Does a production-ready codebase help SEO and AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; speed, rendering, metadata and stability support crawling and citation." }
    }
  ]
}
</script>
