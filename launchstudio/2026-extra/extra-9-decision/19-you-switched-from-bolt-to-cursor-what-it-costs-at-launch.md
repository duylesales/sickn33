---
Title: "You Switched From Bolt to Cursor Mid-Build: What That Costs You at Launch"
Keywords: Bolt to Cursor migration, AI tool switch cost, orphaned config launch, duplicate environment variables, AI codebase archaeology, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# You Switched From Bolt to Cursor Mid-Build: What That Costs You at Launch

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "You Switched From Bolt to Cursor Mid-Build: What That Costs You at Launch",
  "description": "Exporting a Bolt project into a local repo and continuing in Cursor is the right call, and it leaves seven specific kinds of debris behind. An itemised account of what each one costs at launch, and how to clear it in a weekend.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2027-01-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/you-switched-from-bolt-to-cursor-what-it-costs-at-launch"
  }
}
</script>

Two commits, five weeks apart. The first says `initial commit` and contains 84 files, none of which you typed. The second, from last night, says `fix org invite flow` and is the 400th in a line of ordinary human work.

Everything between those two commits is the story of a good decision. Bolt got you a working full-stack app in a weekend; when the prompting cycle became slower than just writing the code, you exported to a repo and moved to Cursor. That's the correct sequence, and most founders who ship do some version of it.

But the switch has a cost, and it isn't paid at the moment of switching — it's paid at launch, in the form of debris that neither tool is responsible for cleaning up. Bolt has no idea you left. Cursor has no idea what came before it. Below is the itemised bill: seven categories of leftover, what each actually costs you, and how long clearing it takes.

## Item 1: git history that starts at the interesting part

`initial commit` with 84 files is not history. It's a snapshot with everything before it deleted.

The practical cost surfaces on the day you need `git bisect` — some behaviour has been subtly wrong for weeks and you want the commit that introduced it. If the cause is in the imported 84 files, bisect terminates at a wall and tells you the bug was always there, which is true and useless. The same applies to `git blame`: every line of the original scaffold is attributed to you, on one date, with no rationale attached.

You can't recover the history. What you can do, in twenty minutes, is write it down: add a `docs/ORIGINS.md` recording which tool generated the baseline, the date, the framework versions it chose, and any decision you know was Bolt's rather than yours. This sounds like bureaucracy until the first time someone else — a contractor, a technical co-founder, an acquirer's diligence team — asks why the project uses a particular library and nobody can answer.

**Cost if ignored:** hours of confused archaeology at the worst moment. **Cost to clear:** 20 minutes.

## Item 2: two deployment targets, both live

This is the one that produces real incidents.

Bolt deploys to Netlify with one click. When you moved to Cursor and pushed to GitHub, you probably connected Vercel, because that's what you know. Nobody disconnected Netlify — it's still building from whatever it was connected to, still serving a URL, and that URL is possibly still in a Slack message, a demo email, or your own bookmarks.

The failure mode is a customer, an investor or your past self using the stale URL and reporting a bug you already fixed. The severe version is that the stale deployment is pointing at your production database with old code, which is a data-integrity problem rather than a confusion problem.

Audit it explicitly: log into Netlify, Vercel, Cloudflare Pages and anything else you may have connected, and list every site still building from this repo. Delete the ones you're not using. Then check your DNS records for a subdomain pointing somewhere you forgot about.

**Cost if ignored:** one bad afternoon, or one real data incident. **Cost to clear:** 30 minutes.

## Item 3: environment variables defined in three places, agreeing on nothing

By the end of the switch, the same variable typically exists in four locations: Bolt's environment, the Netlify site, the Vercel project, and your local `.env`. They drift. The classic case is a Stripe key that's `sk_test_` in one place and `sk_live_` in another, which means test payments in production or, considerably worse, live charges from a staging environment.

Related and sneakier: Bolt's naming conventions differ from what you'd choose in Cursor, so you get `VITE_SUPABASE_URL` from the original scaffold and `NEXT_PUBLIC_SUPABASE_URL` from a file you wrote later — both read at runtime, both defined, both possibly pointing at different projects. And a variable renamed in one place while the old name survives elsewhere is a fallback that quietly resolves to something stale.

Make one authoritative list. `.env.example`, committed, with every variable the app reads, a one-line comment on each, and no values. Then reconcile every environment against it and delete what isn't on the list. While you're there, grep the build output for anything client-prefixed that carries a secret — the export from Bolt is exactly when that mistake gets frozen in.

**Cost if ignored:** the whole spectrum, from a broken deploy to real money charged wrongly. **Cost to clear:** 1–2 hours.

## Item 4: a Supabase project with two generations of schema in it

Bolt created your tables and, most likely, some RLS policies. Cursor then generated migration files — but the tables already existed, so the early migrations were either skipped, or hand-edited, or applied against a project whose state didn't match what they assumed.

What you end up with is a live database containing artefacts from both eras: a `profiles` table from Bolt and a `users` table from Cursor, both partly populated. Policies written in the Bolt phase that were never revisited after the schema changed underneath them — a policy referencing a column that no longer exists, or one written against `user_id` on a table that now scopes by `org_id`. Two of these can be *broken open*: a policy whose condition no longer matches anything can fail permissively depending on how it was written.

Run the diff and look at the reality:

```
supabase db diff --linked
```

Then read every policy directly rather than trusting the migration files:

```sql
select tablename, policyname, cmd, qual, with_check from pg_policies where schemaname='public';
select relname, relrowsecurity from pg_class where relnamespace='public'::regnamespace and relkind='r';
```

Any table with RLS off, any `qual` of `true`, and any policy referencing a column that's gone are all findings. The clean end state is a squashed baseline migration reflecting production exactly, with everything after it applied through the pipeline.

**Cost if ignored:** the most likely source of an actual data exposure in a switched codebase. **Cost to clear:** half a day.

## Item 5: dependencies frozen at the moment of export

Bolt pinned versions that were current on the day it generated your project, and pinned them to what runs in a browser-based WebContainer. Two consequences.

First, versions have moved. Some of those pins now carry advisories; `npm audit --omit=dev` will tell you in seconds. Second, and less obvious, WebContainer can't run native Node addons, so Bolt routed around them — meaning if your app processes images, generates PDFs, or does anything cryptographic beyond the basics, it may be using a pure-JS package chosen for sandbox compatibility rather than for production performance. That's not automatically wrong, but it's a decision made for you, for a reason that no longer applies.

Then there's duplication, same as any multi-session AI project: Bolt reached for one date library, you reached for another in Cursor, and both are installed. `npx depcheck` and `npm ls --depth=0` sort this out in an afternoon.

**Cost if ignored:** slow accumulation, plus one avoidable CVE. **Cost to clear:** 2–3 hours.

## Item 6: two idioms for the same job, and no rule about which wins

The Bolt-generated code has a house style: how it fetches, how it handles errors, how it shapes API responses. Your Cursor code has yours. Both are present, and Cursor — reading the file it's currently in — will happily continue whichever one it finds locally, which entrenches the split.

Concretely, expect to find: two ways of calling your own API, two error-response shapes, two patterns for reading the session, sometimes two auth flows if you added social login later. Nothing is broken. The cost is that a fix applied to one path doesn't apply to the other, which matters enormously when the fix is a security fix.

The remedy isn't a grand refactor. It's a `.cursorrules` file — or whatever your editor's equivalent is — stating the conventions explicitly: how authorization is enforced, where API calls live, what an error response looks like. Then converge the files that matter (auth, data access, payments) and let the rest converge naturally as you touch it.

**Cost if ignored:** the security fix you applied to one of two paths. **Cost to clear:** 2 hours for the rules, ongoing for convergence.

## Item 7: assumptions that were true in a browser sandbox

Last and most subtle. Code written for WebContainer carries assumptions about the file system, about process lifetime, about what's available at runtime. On a real Node host — especially serverless — background work started with a bare `setTimeout` may never run, because the function froze after the response. File writes to a local path vanish. Long-running processes get killed at the platform's timeout.

If your app has anything that happens "after" a request — sending an email, generating a report, calling an LLM — check how it's invoked. If it isn't awaited or handed to a real queue, it's a coin flip in production.

**Cost if ignored:** intermittent failures that resist reproduction. **Cost to clear:** varies; usually 2–4 hours to move the affected work onto an awaited path or a proper queue.

## Adding it up

Seven items, roughly one focused weekend of work: an hour of documentation, two hours of environment and deployment hygiene, half a day on the database, an afternoon on dependencies, and a couple of hours on conventions. That's assuming you find what's there. The reason people underestimate the bill is that none of it presents as a bug — the app works throughout, which is exactly what makes the debris survive to launch.

If the weekend is available, spend it. If it isn't — and at the point where you're switching tools mid-build, the reason is usually that you're finally close enough to launch that your attention belongs on customers — this is a well-defined enough scope to hand over. It's the standard shape of a [LaunchStudio](https://launchstudio.eu/en/) engagement: your code stays yours, both generations of it, and someone who has untangled a dozen of these clears the debris, consolidates the database, and hands back a documented codebase you keep building in Cursor. Fixed price in the €800–€3,500 band, one to three weeks, about a fifth of an agency's number for the same outcome — because an agency would quote you a rebuild and you don't need one. The engineers come out of [Manifera](https://www.manifera.com/services/custom-software-development/), where over eleven years of production delivery has mostly consisted of inheriting other people's decisions and making them coherent.

Curious what your own switch left behind? [See how other founders' projects went from mixed-tool codebases to live products](https://launchstudio.eu/en/#proof) — then send yours over for a look.

## Real example

### The Netlify Deploy Nobody Had Thought About Since October

Sem Vaandrager built Rittenboek in Bolt over a weekend — a mileage and expense logger for Dutch ZZP'ers, with automatic categorisation and a quarterly export for their accountant. Three weeks later he exported to a repo and continued in Cursor, adding multi-vehicle support, accountant sharing and Mollie subscriptions. By January he had 240 paying users at €7 a month.

The pre-launch review of his growth push found the debris in almost exactly the order above. The original Netlify deployment was still building from a stale branch and still connected to the production Supabase project — four months of code drift, live, on a URL a handful of early users had bookmarked. Two of the RLS policies dated from the Bolt era and referenced a `user_id` column on a table that had since been re-scoped to organisations, so the policies matched nothing and the tables' behaviour depended on which client connected. And the quarterly export — the feature accountants actually cared about — was kicked off with an unawaited async call, which is why roughly one in fifteen exports never arrived and Sem had assumed it was an email deliverability issue.

**Result:** The stale Netlify site was removed, environment variables reconciled to a single committed `.env.example`, RLS policies rewritten and verified against the current schema with a squashed baseline migration, and the export job moved onto a real queue with retries. Five working days, no changes to the interface.

> *"The export bug was the funny one. I'd spent two weeks on SPF and DKIM records convinced it was email. The report was never being generated in the first place — the function had already returned."*
> — **Sem Vaandrager, Founder, Rittenboek (Zwolle)**

**Cost & Timeline:** €2,300 (Launch Ready) — five working days.

---

## Frequently Asked Questions

### Should I have avoided the switch and stayed in one tool?

No — switching at the point where prompting gets slower than typing is the right instinct, and staying in a browser-based tool past that point costs more than the debris does. The mistake isn't switching; it's assuming the export was a clean handover when it's really two codebases sharing a directory.

### Can I recover the git history from my Bolt project?

Not meaningfully. Bolt's editing history isn't a git history you can import, so the practical move is documenting the origin — tool, date, framework versions, and any decision you know wasn't yours — rather than trying to reconstruct commits that never existed in that form.

### How do I find deployments I've forgotten about?

Check each hosting provider's dashboard for sites connected to the repository, then check your domain's DNS records for subdomains you don't recognise, then search your own sent email and Slack for `.netlify.app` and `.vercel.app` URLs. The last one usually finds the link that's still circulating.

### Are the RLS policies Bolt generated worth keeping?

Some are, but every one needs re-reading against the current schema rather than being trusted because it exists. Policies referencing columns that were later renamed or re-scoped are the specific hazard, since a condition that matches nothing behaves very differently from one that correctly restricts access.

### Is a rules file for my editor actually worth writing?

Yes, and it's the cheapest item on the list. Without it, the model continues whichever convention it finds in the file it's editing, which permanently entrenches the split between the imported code and yours. A short explicit statement of how authorization, data access and errors work is enough to make new code converge instead of diverge.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should I have avoided the switch and stayed in one tool?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Switching when prompting becomes slower than typing is the right instinct, and staying in a browser-based tool past that point costs more than the debris does. The mistake is assuming the export was a clean handover rather than two codebases sharing a directory."
      }
    },
    {
      "@type": "Question",
      "name": "Can I recover the git history from my Bolt project?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not meaningfully, since Bolt's editing history isn't a git history you can import. The practical move is documenting the origin — tool, date, framework versions and any decision that wasn't yours — instead of reconstructing commits that never existed."
      }
    },
    {
      "@type": "Question",
      "name": "How do I find deployments I've forgotten about?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Check every hosting provider's dashboard for sites connected to the repository, review your DNS records for unfamiliar subdomains, and search your own email and Slack for .netlify.app and .vercel.app URLs. The last search usually finds the link still circulating."
      }
    },
    {
      "@type": "Question",
      "name": "Are the RLS policies Bolt generated worth keeping?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Some are, but each needs re-reading against the current schema rather than being trusted because it exists. Policies referencing columns later renamed or re-scoped are the hazard, since a condition matching nothing behaves very differently from one that restricts correctly."
      }
    },
    {
      "@type": "Question",
      "name": "Is a rules file for my editor actually worth writing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, and it is the cheapest item on the list. Without it the model continues whichever convention it finds locally, entrenching the split between imported and hand-written code. A short statement of how authorization, data access and errors work makes new code converge."
      }
    }
  ]
}
</script>
