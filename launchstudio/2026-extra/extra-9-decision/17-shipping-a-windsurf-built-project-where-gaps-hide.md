---
Title: "Shipping a Windsurf-Built Project: Where the Gaps Usually Hide"
Keywords: Windsurf Cascade production, multi-file AI edits review, half-migrated codebase, AI coding conventions drift, ship AI built project, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Shipping a Windsurf-Built Project: Where the Gaps Usually Hide

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Shipping a Windsurf-Built Project: Where the Gaps Usually Hide",
  "description": "Windsurf's multi-file agentic editing produces a specific failure signature: half-completed refactors, competing conventions, and code that was correct when written and stale two sessions later. A field guide to the five places those gaps hide and how to surface them before launch.",
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
  "datePublished": "2027-01-18",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/shipping-a-windsurf-built-project-where-gaps-hide"
  }
}
</script>

It's 01:40 and you're staring at two functions that do the same thing. `getUserOrgs` in `lib/orgs.ts` and `fetchOrganizationsForUser` in `server/queries/organizations.ts`. Both work. Both are called from different parts of the app. One filters out archived organisations and one doesn't, and you have no memory of writing either, because Cascade wrote both — nine days apart, in service of two requests that seemed unrelated at the time.

This is the Windsurf signature, and it is a genuinely different failure mode from the one single-file autocomplete produces. Cascade's strength is that it edits across a whole codebase at once: ask for user impersonation for support staff and it touches the auth middleware, three route handlers, a database migration and a React hook, coherently, in one pass. That coherence is real *within* a session. Between sessions it decays, because the model rediscovers your codebase each time and cannot reliably tell which of the patterns it finds is the one you actually meant.

The result is a codebase where nothing is obviously broken and several things are quietly half-true. Here are the five places those gaps hide, in the order they're worth checking.

## Gap one: the refactor that finished 80% of the way

The most common finding, and the most consequential.

You asked for something structural: "move authentication to middleware," "switch from the anon Supabase client to a server client," "extract the permission checks into a helper." Cascade planned it, listed the files, made the edits, and you approved. Eleven files changed. It worked, you tested the main flow, you moved on.

The twelfth file was not in the plan, because it was in a directory the search didn't reach, or its call site was constructed dynamically, or it was added later in a different session. So now you have a codebase where authentication *is* handled by middleware — except in one route where the old inline check remains, subtly different, checking the session but not the role.

Half-finished refactors are dangerous specifically because they look finished. The old pattern still works, so nothing errors. The way to surface them is to search for the pattern you *migrated away from*, not the one you migrated to:

```
rg -n "createClient\(.*ANON" server/ app/          # supposedly replaced
rg -n "getSession\(\)" --files-with-matches | wc -l # should be near-zero after middleware
git log --oneline --all | head -40                  # find the refactor commit, read its diff
```

Take the refactor commit's file list and compare it against a fresh grep of the old pattern today. The difference is your gap list. This takes ten minutes per refactor and it is the highest-value check in this article.

## Gap two: two of everything, with different opinions

Beyond refactors, duplication accumulates on its own. The typical Windsurf project at launch time has:

- Two data-access helpers for the same table, as in the opening — one applying a filter the other doesn't.
- Two API clients for the same vendor, one using `fetch` and one using the official SDK, with different error handling and possibly different base URLs.
- Two validation approaches — Zod on newer routes, hand-rolled `if (!body.email) return 400` on the older ones.
- Two ways to read configuration, one from `process.env` directly and one via a config module, so a variable renamed in one place still resolves in the other.
- Occasionally two auth flows, when a session added social login without removing the assumptions of the email-password path.

None of this crashes. The risk is that a fix applied to one copy doesn't apply to the other, which is precisely what happens when you patch a security issue: you find the bug in `fetchOrganizationsForUser`, fix it, deploy, and `getUserOrgs` continues serving archived organisations to people who shouldn't see them.

Find them with a duplication detector rather than by eye — `npx jscpd src server --min-lines 8 --min-tokens 60` gets you a report in a couple of minutes. Then make a decision per pair: keep one, delete the other, and update the call sites in a single change. Resist the temptation to have Cascade do this without reading the diff, because the deletion is the part where things silently break.

## Gap three: rules and memories that are no longer true

Windsurf's rules files and persistent memories are a real advantage — they're how you stop re-explaining your conventions every session. They're also a source of a specific, quiet failure: they drift out of date, and the model keeps following them anyway.

You wrote a rule in week one saying the project uses the Pages Router. In week four you moved to the App Router. The rule is still there, and Cascade is still, occasionally, generating Pages-shaped code that mostly works. Or a memory records "we use `supabase.auth.getUser()` for session checks" from before you moved to a server-side client, so new code reaches for the old pattern and reintroduces the very thing gap one is about.

Before a launch push, read every rules file and every stored memory as though someone else wrote them, and delete anything that describes the codebase as it was rather than as it is. Then add the rules that matter for production specifically: where authorization is enforced, that schema changes go through migration files, that no secret gets a client-visible prefix. Rules are the cheapest mechanism you have for stopping the drift from starting again.

## Gap four: the code that was never really exercised

Cascade writes complete-looking implementations, including branches you have never run.

The error paths are the usual suspects. A `catch` that logs and returns a 200 with `{ success: false }`, so your front end treats a failure as a success. A retry loop with no backoff and no ceiling that turns a transient vendor blip into a self-inflicted denial of service. A `finally` that closes a connection that a different code path already closed.

Then there are the endpoints nobody uses. Route handlers built for a feature you cut, a `/api/admin/*` group from an admin panel you never finished, an export endpoint added for a single demo. They are live, they are unauthenticated more often than not, and they are invisible in your analytics because no legitimate user calls them. Take the entry-point list from a route grep and mark every path that hasn't appeared in your access logs in the last thirty days. Delete rather than protect — an endpoint you don't need is a liability with no offsetting benefit.

And check the tests, if Cascade wrote any. Generated tests skew toward asserting that a call returns something rather than that it returns the right thing for the wrong user, which means a passing suite is compatible with every authorization bug in this article.

## Gap five: migrations written, migrations not applied

Cascade is good at generating migration files. It has no way to know whether you ever ran them against production.

The typical sequence: it generates `0007_add_team_invites.sql`, you apply it locally, the feature works, and then a deploy happens through a path that doesn't run migrations — because your deploy step is `git push` and nothing else. Or the reverse: you were in a hurry and made the change directly in the Supabase or Neon console, so production has the column and the migrations directory doesn't.

Either way the repo and the live database disagree, and you find out during an incident. Check it directly rather than trusting the file list: `supabase db diff --linked`, or `prisma migrate diff --from-schema-datamodel --to-schema-datasource`, or Drizzle's generate-against-live. An empty diff is a pass. A non-empty one is a specific enumeration of what your repository is wrong about.

Fix it by reconciling to a squashed baseline that reflects production exactly, then never touching the console again. And add migration execution to the deploy pipeline, so the two can't diverge in future without someone deliberately making it happen.

## The half-day sweep, in order

If you have one afternoon before you start telling people about your product:

1. Identify your two or three largest refactors from git history. Grep for the old pattern. Fix what survived. (60 min)
2. Run `jscpd`. Resolve every duplicated pair that touches auth, data access or payments. (60 min)
3. Read your rules and memories. Delete the stale, add the production ones. (20 min)
4. List routes, cross-reference access logs, delete the unused. (30 min)
5. Diff schema against production. Reconcile. Wire migrations into deploy. (60 min)
6. Run the cross-tenant test: two accounts, one requesting the other's records on every ID-accepting endpoint. (30 min)

Six items, roughly four and a half hours, and it addresses the failure signature that agentic multi-file editing actually produces — as opposed to a generic security checklist, most of which will not apply to you.

What the sweep won't do is make the structural decisions. Which of the two auth flows survives, where authorization is enforced from now on, how the schema is owned — those need someone holding the entire system in their head at once, and that is the one thing a per-session agent is architecturally unable to do. [LaunchStudio](https://launchstudio.eu/en/) is built for exactly that handoff: your front end and your workflow stay as they are, the structural inconsistencies get resolved by engineers who read this kind of codebase every week, and you get the decisions written down so your rules file can enforce them afterwards. The team comes from [Manifera](https://www.manifera.com/portfolio/), where over a decade of production delivery for enterprise clients built the habit of insisting a codebase have exactly one way to do each important thing.

Fixed price, agreed after a short scoping call and before anyone opens a pull request — [tell us what you've built](https://launchstudio.eu/en/#contact) and you'll know the number and the timeline the same week.

## Real example

### Two Functions, One Filter, Eleven Hundred Rows

Nadia el Amrani built Werkstroom in Windsurf over seven weeks — a compliance workflow tool for facility management companies, tracking inspections, certifications and expiry dates across client sites. Four companies were piloting it. A fifth, considerably larger, had asked for a security summary before signing.

The sweep found the opening example almost immediately. Two functions fetched a user's accessible sites: one written in week two, one generated in week five during a refactor that was supposed to replace it. The newer one filtered by the user's organisation. The older one filtered by a `siteIds` array passed in from the caller — and one dashboard component was still calling it with an unfiltered list assembled client-side. Any pilot user hitting that dashboard could, with a modified request, retrieve inspection records for roughly eleven hundred sites belonging to the other three companies. The refactor commit had touched nine files. The tenth was the one that mattered.

The schema check failed too: three columns existed in production that no migration described, added by hand during a demo crunch.

**Result:** The duplicate query paths collapsed into one organisation-scoped accessor, all site access moved behind a single authorization helper, the schema reconciled to a squashed baseline with migrations wired into the deploy step, and a cross-tenant test added to CI. Six working days. Nadia sent the larger client a written findings-and-remediation document and closed the contract three weeks later.

> *"Both functions were fine. That's what I keep coming back to. Neither one was badly written — they just disagreed about one filter, and I'd have had to read both of them side by side to ever notice."*
> — **Nadia el Amrani, Founder, Werkstroom (Tilburg)**

**Cost & Timeline:** €3,200 (Launch Ready) — six working days.

---

## Frequently Asked Questions

### Why do half-finished refactors happen even when I approve the plan?

Because the plan is built from what Cascade could find at that moment. Files reached through dynamic imports, code in directories outside the search scope, and call sites added in a later session don't appear in it. The plan is honest about what it saw, and what it saw is not always everything.

### Are Windsurf rules and memories worth using at all, given the drift problem?

Yes — they're the cheapest way to keep conventions consistent, which is the underlying issue. The discipline is treating them as code: review them when the architecture changes, delete stale entries deliberately, and keep them short enough that reading all of them takes two minutes rather than twenty.

### How do I decide which of two duplicate implementations to keep?

Keep the one whose behaviour matches what you'd write today, not the newer one by default — the later version was sometimes generated with less context than the original. Read both, pick deliberately, then delete the loser in the same commit that updates its call sites so there's no window where both exist unowned.

### Should I let Cascade do the deduplication work itself?

For finding candidates, yes. For executing the deletion, review every diff line yourself. Removing a function is the operation where a missed dynamic call site produces a runtime error in a path you don't test, and that is exactly the kind of reference a search-based plan is most likely to miss.

### Does having generated tests mean the isolation problem is already covered?

Almost never. Generated tests typically assert that an authorized user gets the expected result, which is the happy path. Cross-tenant isolation requires asserting that an *unauthorized* user gets a 403, and that inverted case has to be asked for explicitly — it doesn't appear on its own.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why do half-finished refactors happen even when I approve the plan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The plan reflects what Cascade could find at that moment. Files reached through dynamic imports, code outside the search scope, and call sites added in later sessions never appear in it, so the plan is honest about what it saw rather than complete."
      }
    },
    {
      "@type": "Question",
      "name": "Are Windsurf rules and memories worth using at all, given the drift problem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, they are the cheapest way to keep conventions consistent. The discipline is treating them as code: review them when the architecture changes, delete stale entries deliberately, and keep them short enough to re-read in two minutes."
      }
    },
    {
      "@type": "Question",
      "name": "How do I decide which of two duplicate implementations to keep?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Keep the one matching what you would write today rather than the newer one by default, since the later version was sometimes generated with less context. Delete the loser in the same commit that updates its call sites."
      }
    },
    {
      "@type": "Question",
      "name": "Should I let Cascade do the deduplication work itself?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use it to find candidates, but review every deletion diff yourself. Removing a function is exactly where a missed dynamic call site produces a runtime error in an untested path, and dynamic references are what search-based plans miss most often."
      }
    },
    {
      "@type": "Question",
      "name": "Does having generated tests mean the isolation problem is already covered?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Rarely. Generated tests usually assert that an authorized user gets the expected result. Cross-tenant isolation requires asserting that an unauthorized user receives a 403, and that inverted case has to be requested explicitly."
      }
    }
  ]
}
</script>
