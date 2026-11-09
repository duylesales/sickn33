---
Title: "How Do I Clean Up Duplicate Code in a Lovable Project?"
Keywords: duplicate code lovable, refactor lovable project, clean up ai generated code, lovable code quality technical debt, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# How Do I Clean Up Duplicate Code in a Lovable Project?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How Do I Clean Up Duplicate Code in a Lovable Project?",
  "description": "After months of prompting, Lovable projects often contain the same logic in many places: several ways to fetch data, repeated permission checks, duplicated components and multiple libraries for the same job. This guide explains why duplication happens, why it causes bugs, how to find it, what to consolidate first, how to refactor safely without breaking the app or Lovable's workflow, and how to prevent duplication from returning.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-08-04",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-clean-up-duplicate-code-in-a-lovable-project" },
  "citation": [
    { "@type": "CreativeWork", "name": "Lovable documentation", "url": "https://docs.lovable.dev/" },
    { "@type": "CreativeWork", "name": "Martin Fowler: Refactoring", "url": "https://martinfowler.com/books/refactoring.html" },
    { "@type": "CreativeWork", "name": "jscpd: Copy/paste detector", "url": "https://github.com/kucherenko/jscpd" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A01 Broken Access Control", "url": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/" }
  ]
}
</script>

**Short answer:** find the duplication that causes risk first, not all of it. In Lovable projects, the most harmful duplication is usually in data access, permission checks, money and date calculations and core components. Consolidate those into shared modules, protected by tests, in small steps, with each change verified in staging. Keep the project compatible with Lovable by syncing through GitHub and avoiding a single massive restructuring, and write project instructions that tell Lovable to reuse the shared modules, so duplication does not return with the next prompt.

## Key Takeaways

- **Duplication is a natural result of prompt-driven development:** each prompt solves its own problem, often by writing new code instead of reusing existing code.
- **Duplicated logic causes inconsistent behaviour and recurring bugs,** because fixes land in one copy while others remain broken.
- **Security-related duplication is the most dangerous:** permission checks repeated inconsistently across screens and functions.
- **Refactor in small, tested steps** rather than rewriting large parts at once.
- **Prevent recurrence** with shared modules, clear conventions and project instructions for AI tools.

## Why Lovable Projects Accumulate Duplication

When you ask Lovable for a feature, it generates code that makes that feature work. It may not know, or prioritise, that similar code already exists elsewhere. Over months, this produces:

- Several functions that fetch the same data with slightly different filters
- Repeated permission checks, some stricter than others
- Multiple formatting helpers for dates and money
- Similar components with small visual differences
- Two or three libraries doing the same job, such as date handling or icons
- Copies of the Supabase client initialised in several places
- Validation rules repeated in forms, sometimes contradicting each other

None of this is unusual. Human teams create duplication too. AI tools just do it faster.

## Why It Matters

| Problem | Example |
| --- | --- |
| Inconsistent behaviour | The invoice list shows amounts with VAT, the dashboard without |
| Recurring bugs | A bug is fixed in one copy of a function and reappears through another |
| Security gaps | One screen checks organisation membership, another loads the same data without the check |
| Slower development | Every change must be made in several places |
| Larger bundles | Multiple libraries for the same purpose slow down the app |
| Confusing for developers | New developers cannot tell which version is correct |
| Confusing for AI tools | Lovable picks up inconsistent patterns and repeats them |

The security row deserves emphasis. Broken access control is the top risk in the OWASP Top 10. When permission logic is duplicated, it is easy for one copy to be weaker, and that weakest copy defines your real security.

## Step 1: Make Sure the Code Is in GitHub

Connect your Lovable project to GitHub if it is not already. This gives you a full history, lets you work on branches, run tools on the code and roll back if something goes wrong. Our guide on [exporting Lovable code to GitHub and continuing to build](https://launchstudio.eu/en/blog/how-to-export-lovable-code-to-github-and-keep-building) explains the workflow.

## Step 2: Find the Duplication

Practical ways to find duplicates:

- **Copy-paste detection tools,** such as jscpd, scan the codebase and list blocks of duplicated code.
- **Search for patterns:** for example, every place that calls `supabase.from('invoices')`, every `createClient(` call or every date formatting function.
- **Check dependencies:** list packages in `package.json` and look for overlapping libraries.
- **Ask an AI tool:** "List all functions that fetch invoices and how they differ" or "Find all places where organisation membership is checked."
- **Look at large files:** very large components often contain logic that exists elsewhere too.

Record findings in a short list, grouped by area.

## Step 3: Prioritise

Not all duplication is worth fixing now. Prioritise by risk and frequency of change:

| Priority | Area | Why |
| --- | --- | --- |
| 1 | Permission and access checks | Security risk |
| 2 | Data access for core entities | Consistency, performance, security |
| 3 | Money, VAT and date calculations | Correctness, customer trust |
| 4 | Validation rules | Data quality |
| 5 | Core UI components, such as forms, tables and dialogs | Consistency, accessibility |
| 6 | Duplicate libraries | Bundle size, maintenance |
| 7 | Small helpers and styling | Low risk, fix opportunistically |

## Step 4: Add Tests Before Refactoring

Refactoring means changing structure without changing behaviour. Tests are how you know behaviour did not change. Before consolidating an area, add tests for the behaviour that matters:

- **Access control:** user A cannot read or modify user B's data, through every route that touches it
- **Calculations:** totals, VAT and rounding for representative cases
- **Key flows:** sign-up, checkout, creating and editing core records

Even a modest test suite around the areas you change makes refactoring far safer.

## Step 5: Consolidate in Small Steps

For each area:

1. **Create a shared module,** such as a data access file for invoices with functions like `listInvoices(ctx)` and `getInvoice(ctx, id)`, or a `formatMoney` helper.
2. **Move the best version of the logic** into the module, choosing the correct behaviour where copies differ, and confirming with the product owner when unclear.
3. **Replace one usage at a time,** running tests after each change.
4. **Remove the old copies** once all usages point to the shared module.
5. **Deploy to staging,** test manually and then release.

For permission logic in Supabase apps, consolidate at the database level where possible: Row Level Security policies enforce rules for every query, regardless of which frontend function makes it. That removes the need to trust each duplicated check.

## Step 6: Remove Duplicate Libraries

Pick one library per purpose, replace usages of the others and remove them from `package.json`. Check the bundle size before and after; the improvement is often visible in page load times.

## Keeping the Project Lovable-Friendly

If you continue building in Lovable after cleaning up:

- **Work through GitHub,** so Lovable syncs the refactored code.
- **Refactor incrementally,** rather than restructuring the whole project at once, which can confuse Lovable's understanding of the codebase.
- **Keep familiar structures** where Lovable expects them, such as components and pages folders.
- **Test Lovable prompts after refactoring** on a branch or staging project, to see whether it reuses the new modules.

## Preventing Duplication From Returning

The most important step. Without it, the next few weeks of prompts recreate the duplication:

- **Project instructions:** describe shared modules and conventions, such as "All database access goes through `src/data/`", "Use `formatMoney` for all amounts", "Use the `DataTable` component for lists" and "Do not add new date libraries."
- **Prompt habits:** when asking for a feature, mention which existing modules to use.
- **Review new code:** check for new functions that duplicate shared ones.
- **Automated checks:** run duplication detection in CI and watch the trend.
- **Periodic clean-up:** schedule small consolidation sessions every month or two.

## An Example Consolidation: Data Access

Consider a project where invoices are loaded in five places: the invoice list, the dashboard widget, the client detail page, the export function and an email reminder function. Each uses a slightly different query; two forget to filter by organisation, one selects all columns including internal notes and one calculates totals in the browser.

A consolidation might look like this:

1. **Write tests** confirming that a user can only see their organisation's invoices, and that totals match expected values for a few test invoices.
2. **Enable or tighten Row Level Security** on the invoices table so every query is scoped to the user's organisation, regardless of frontend code.
3. **Create a module** with `listInvoices`, `getInvoice` and `getInvoiceTotals`, selecting only needed columns and calculating totals on the server or in a database view.
4. **Replace the invoice list's query** with `listInvoices`, run the tests and check the page.
5. **Repeat** for the dashboard, client page, export and reminder function, one at a time.
6. **Delete the old queries,** search the codebase to confirm none remain, and add the module to the project instructions.

Each step is small and reversible, and the app keeps working throughout. The result is one place to fix bugs, one place to optimise performance and one place where AI tools find the pattern to follow.

## Measuring Progress

Track a few simple numbers before and after: duplicated blocks reported by the detection tool, number of dependencies, bundle size, and the count of bugs that reappear after being fixed. Seeing these move in the right direction helps justify the time spent and shows when to stop.

## When to Stop

Perfect deduplication is not the goal. Some duplication is harmless or even sensible, such as two similar components that are likely to diverge. Stop when the high-risk areas are consolidated, tests protect them and new code follows the conventions. Spend the remaining time on customers and features.

## When a Cleanup Becomes a Rebuild

If duplication is so extensive that nearly every feature is implemented several times in incompatible ways, and tests are absent, a structured partial rebuild of the backend layer may be faster than incremental consolidation. Even then, the interface Lovable generated can usually be kept. Our guide on [rebuild vs refactor](https://launchstudio.eu/en/blog/rebuild-vs-refactor-an-ai-built-app) helps decide.

## Unused Code

Alongside duplication, Lovable projects collect unused code: abandoned pages, components from features that were removed and helpers nobody calls. Tools that detect unused exports and files help find them. Removing dead code reduces confusion for developers and AI tools alike.

## How LaunchStudio Helps

LaunchStudio cleans up AI-generated codebases without rebuilding them: finding and prioritising duplication, adding tests around critical behaviour, consolidating data access, permissions and calculations into shared modules, enforcing access in the database with Row Level Security, removing duplicate libraries, keeping projects compatible with Lovable and writing project instructions that prevent duplication from returning.

The **Launch Ready** package (€800-€3,500) covers a focused clean-up of high-risk areas along with security hardening and deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and priority support for ongoing development. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, maintaining and refactoring codebases for enterprise clients. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: Seven Ways to Load a Project

Daan Hofstra built Projectkompas in Lovable over ten months: a project management tool for small marketing agencies, with clients, projects, tasks, time tracking and invoicing. It worked, but every new feature seemed to break something else. A bug in the invoice totals was fixed three times and kept returning, and a user at one agency once saw a project from another agency on a dashboard widget.

A duplication scan found seven different functions that loaded projects, with different filters and only four of them checking the agency. Money was formatted in five ways, two of which ignored VAT. There were three date libraries, two icon libraries, four similar table components and the Supabase client was initialised in six files. The recurring invoice bug turned out to be three copies of the total calculation, each fixed separately at different times.

LaunchStudio first added Row Level Security policies per agency on all tables, so no frontend function could load another agency's data, and wrote tests for access control and invoice calculations. Projects, tasks and invoices received shared data access modules, and the seven project loaders were replaced one by one. A single money module handled VAT and rounding, one date library and one icon library remained, the table components were merged into one accessible component, and a single Supabase client was exported from one file. Project instructions told Lovable which modules and components to use, and a duplication check was added to CI.

**Result:** The invoice bug has not returned, the cross-agency exposure was closed, and the app's bundle size fell by about a third. Daan continued building in Lovable, and the new features now reuse the shared modules, with the duplication check staying flat.

> *"Every time I fixed something, Lovable had another copy somewhere. Consolidating the core made the app finally behave like one product."*
> - **Daan Hofstra, Founder, Projectkompas (Groningen)**

**Cost & Timeline:** €3,500 (Launch Ready package: duplication analysis, RLS per agency, tests, shared modules, library consolidation, component merge and AI instructions) - completed in 10 business days.

## Frequently Asked Questions

### Why does my Lovable project have so much duplicate code?

Because each prompt generates code to solve a specific request, often without reusing what already exists. Over many prompts, similar logic appears in many places. This is normal in prompt-driven development and can be managed with shared modules, tests and project instructions.

### Is duplicate code dangerous?

It can be. Duplicated logic leads to inconsistent behaviour and recurring bugs, and duplicated permission checks can leave security gaps where one copy is weaker. Consolidating access control in database policies and shared modules removes that risk.

### Can I keep using Lovable after refactoring?

Yes, if you work through GitHub, refactor incrementally and keep familiar project structures. Write project instructions describing the shared modules so Lovable reuses them, and test a few prompts on a branch after the clean-up.

### How does Manifera's experience help with code clean-up?

Manifera has maintained and refactored codebases for enterprise clients for 11+ years. LaunchStudio applies that experience to AI-generated projects, consolidating high-risk areas safely without rewriting the parts that already work.

### Does cleaning up code improve my app's speed and visibility?

Often, yes. Removing duplicate libraries and inefficient data loading makes pages smaller and faster, which improves user experience and helps search engines and AI answer engines access your public pages reliably.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why does my Lovable project have so much duplicate code?",
      "acceptedAnswer": { "@type": "Answer", "text": "Each prompt solves its own request without reusing existing code; manage it with shared modules, tests and instructions." }
    },
    {
      "@type": "Question",
      "name": "Is duplicate code dangerous?",
      "acceptedAnswer": { "@type": "Answer", "text": "It can cause inconsistent behaviour, recurring bugs and weak permission checks; consolidate in RLS and shared modules." }
    },
    {
      "@type": "Question",
      "name": "Can I keep using Lovable after refactoring?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, via GitHub, incremental changes and instructions describing shared modules." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with code clean-up?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has refactored enterprise codebases for 11+ years, consolidating safely without rewrites." }
    },
    {
      "@type": "Question",
      "name": "Does cleaning up code improve my app's speed and visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Often; smaller bundles and efficient data loading make pages faster for users and crawlers." }
    }
  ]
}
</script>
