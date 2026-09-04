---
Title: "Your Cursor Codebase Works: A Production-Readiness Review Before You Sell It"
Keywords: Cursor codebase production ready, AI code review checklist, indie hacker security audit, secrets in git history, production readiness gates, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Your Cursor Codebase Works: A Production-Readiness Review Before You Sell It

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Your Cursor Codebase Works: A Production-Readiness Review Before You Sell It",
  "description": "A seven-gate review for a Cursor-built codebase that already runs correctly, aimed at the specific failure modes AI-assisted development produces rather than generic security advice. Each gate has a pass condition, a check you can run, and a rough cost to close.",
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
  "datePublished": "2027-01-08",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/your-cursor-codebase-works-production-readiness-review"
  }
}
</script>

*"Is it ready?"*
*"It works. I've been using it daily for three weeks."*
*"That's not what I asked."*

That exchange — some version of it, with a prospective customer, an advisor, or the more sceptical half of your own brain — is where this article starts. A Cursor codebase is a different object from a Lovable or Bolt export. It is a real repository that you have read, that you have shaped, that has your architectural decisions in it. You are not a passenger. Which is exactly why the standard advice ("AI code has security holes!") is useless to you: you already know that, and you also know your code is better than that framing implies.

So here is a review structured as gates rather than warnings. Seven of them, each with a pass condition, a check you can actually run, and an honest estimate of what closing it costs. These are the failure modes specific to AI-assisted development in a real repo — not generic OWASP material, but the things that go wrong when a competent developer accepts a lot of plausible-looking code quickly.

## Gate 1 — Secrets have never touched the repository

**Pass condition:** No credential appears anywhere in git history, in any branch, in any bundle.

The AI-assisted failure mode is specific. You asked for a working example, the model produced one with the key inline "for now," you meant to move it to `.env`, and the commit went in before you did. Or `.env` itself got committed early, before `.gitignore` caught up, and removing it later from the working tree left it permanently in history.

```
git log --all --full-history -- .env .env.local
npx trufflehog git file://. --only-verified
npm run build && grep -rEo "sk_(live|test)_[A-Za-z0-9]+|service_role|AKIA[0-9A-Z]{16}" dist/ .next/ 2>/dev/null | sort -u
```

If anything surfaces, the fix is rotation first, then history. Rotate at the provider — a key in git history is compromised regardless of whether the repo is private, because it has been in every clone, every CI log and every deploy artefact since. Then decide whether rewriting history with `git-filter-repo` is worth it; for a solo repo it usually is, and it takes an hour.

**Cost to close:** 1–3 hours, plus whatever the rotation breaks downstream.

## Gate 2 — Authorization is decided in exactly one place

**Pass condition:** You can name the single function or policy layer that answers "may this user do this to this record," and every path goes through it.

This is the gate most Cursor codebases fail, and it fails for an interesting reason: you didn't write all the endpoints in one sitting. You wrote three in one session, four more two weeks later, and the model — with no memory of the first session's convention — produced a slightly different shape for the second batch. Now `/api/projects/[id]` checks ownership inline, `/api/documents/[id]` relies on a `requireOwner` helper, and `/api/exports/[id]` checks nothing at all because the session it was written in was about CSV formatting.

Inventory it. List every route, and for each one write down where the authorization decision happens. The list itself is the finding — the routes where you have to go and look are the routes where nobody looked before.

```
rg -n "export async function (GET|POST|PATCH|DELETE)" app/ --files-with-matches
rg -n "params\.(id|slug)" app/api/ -A6 | rg -v "userId|auth\(\)|requireOwner|session"
```

Middleware is not a substitute here. `middleware.ts` matching on a path pattern tells you a session exists; it cannot tell you the record belongs to that session. And be alert to a subtle one: a matcher regex that was correct when you had four routes and silently stopped covering the ones added in October.

**Cost to close:** 4–12 hours, mostly inventory and consolidation rather than clever code.

## Gate 3 — The data layer refuses malformed input on its own

**Pass condition:** Invalid data cannot enter the database even if every line of application code is bypassed.

AI-assisted code tends to validate at the edge — a Zod schema on the route handler — and then trust everything downstream. That is a good start and an incomplete finish. Zod validates what came through that handler. It has no opinion about what a background job, a seed script, a manual SQL statement or next month's second endpoint writes.

Check what the database itself enforces. NOT NULL on the columns that matter, CHECK constraints on the ones with a legal range, UNIQUE where duplicates would be a business bug, and foreign keys with a deliberate ON DELETE behaviour rather than whichever default was in the generated migration. Then check whether numbers are stored as `numeric` rather than floats — every prototype that prices things in floating point eventually produces an invoice for €19.999999.

The related check is money and quantity fields specifically. Grep for every place a value that costs you something arrives from a request body: price, quantity, credits, plan, role, discount. Each one either comes from your own database, or it needs a server-side check against something authoritative. A `price` field trusted from the client is the oldest bug in e-commerce and AI writes it constantly, because in a demo it is the obvious way to do it.

**Cost to close:** 3–8 hours.

## Gate 4 — Schema state is reproducible from the repository

**Pass condition:** A fresh developer can clone, run one command, and get a database structurally identical to production.

The AI-assisted anti-pattern here is distinctive: the model generates a migration file, you look at it, it looks right, and then you apply the change through a dashboard or an ad-hoc `ALTER TABLE` because that was faster in the moment. Six weeks later the migrations directory describes a schema that resembles but does not match your live database. Drift like this is invisible until the day you need to restore, replicate, or hire.

With Prisma, `prisma migrate diff --from-schema-datamodel --to-schema-datasource` tells you the truth. With Drizzle, generate against the live database and see whether the diff is empty. With raw Supabase, `supabase db diff --linked`. An empty diff is the pass. A non-empty diff is a specific, enumerated list of the lies your repo is telling.

While you are there, confirm backups exist and that you have restored one. An untested backup is a belief, not a capability, and testing it takes twenty minutes.

**Cost to close:** 2–6 hours to reconcile, plus a permanent change in habit.

## Gate 5 — Third-party callbacks are authenticated

**Pass condition:** Every inbound webhook verifies a signature and processes each event exactly once.

Stripe, Mollie, Clerk, Resend, GitHub — anything that calls you back. The endpoint is public by necessity, which means the signature is the only thing distinguishing a real event from a forged one. AI-generated handlers frequently construct the event, catch the verification error, log it, and continue to the business logic, because that pattern makes the local test pass when you don't have the signing secret set.

Read your own handler and answer three questions. Does a verification failure return a 4xx and process nothing? Is the raw body being verified rather than a re-serialised object? Does a repeated event ID become a no-op? Webhook providers retry aggressively on timeouts, so a non-idempotent handler will eventually double-credit an account — and it will happen at 3am on the day traffic spikes, not on a quiet Tuesday.

Then audit event coverage. Most AI-built Stripe integrations handle the happy path only. Cancellations, failed renewals and disputes arrive as separate events, and unhandled means your access control silently diverges from your billing.

**Cost to close:** 3–6 hours per provider.

## Gate 6 — Dependencies are real, current, and few

**Pass condition:** Every package in `package.json` is one you can justify, resolves to a genuinely maintained project, and has no known critical advisory.

Two AI-specific risks live here. The first is hallucinated or squatted packages: models occasionally suggest a plausible-sounding package name that doesn't exist, and attackers have begun registering exactly those names. Any dependency you don't remember choosing deserves a look at its download count, its repository and its publish history.

The second is quieter — dependency sprawl. Across a dozen sessions the model reached for `date-fns` in one file, `dayjs` in another, `moment` in a third; three HTTP clients; two validation libraries. Nothing is broken, but your bundle is larger than it should be and your security surface is three times bigger than the problem justifies.

```
npm audit --omit=dev
npx depcheck
npm ls --all 2>/dev/null | wc -l
```

**Cost to close:** 2–5 hours.

## Gate 7 — Failure is observable

**Pass condition:** When something breaks in production, you find out from your tooling and not from a customer.

This is the gate people skip because it feels like polish. It is not — it is the difference between a bug that costs you one afternoon and a bug that costs you eleven customers who simply left. The minimum viable set: error tracking with source maps uploaded (Sentry's free tier is plenty), structured logs you can search with a request ID that ties a user's report to an actual trace, an uptime check that pings a real endpoint rather than the homepage, and one alert that reaches your phone.

Add rate limiting to this gate, because it is the same category of thinking. Sign-up, password reset, and any endpoint that costs you money per call — an LLM, an email send, an SMS — need a limit before launch, not after the first scripted abuse.

**Cost to close:** 4–8 hours for a genuinely useful setup.

## Scoring, and what the score means

Count your failures. Zero to two, you are in good shape — close them this weekend and launch. Three to four is the most common result for a well-built Cursor project and represents roughly a solid week of infrastructure work you have never done before. Five or more means the gap is not knowledge, it is time, and the honest question becomes whether that week is better spent on gates or on customers.

That trade-off is the entire premise of [LaunchStudio](https://launchstudio.eu/en/): the code you wrote stays yours and stays put, the seven gates get closed by people who have closed them several hundred times, and you get a documented handover so you can keep building in Cursor afterwards without inheriting someone else's conventions. Behind it sits [Manifera](https://www.manifera.com/portfolio/), a software company that has been shipping production systems for enterprise clients since 2014 — the same review discipline, scoped down to a one-to-three-week engagement instead of a six-month contract.

If a second opinion would help before you commit either way, book a fifteen-minute call and bring your worst gate. We'll tell you honestly whether it's a weekend or a fortnight.

## Real example

### Seven Gates, Two Failures, One Very Expensive Near-Miss

Ruben Aksoy had spent four months building Kantoorplan in Cursor — a desk-booking and office-capacity tool he was about to sell to three Rotterdam co-working operators on annual contracts. He is a competent developer; the code was well organised and genuinely readable, and he passed five of the seven gates on the first pass.

Gate 2 was the problem. Twenty-three API routes, written across roughly forty Cursor sessions, in three different authorization idioms. Nineteen were correct. Three used a helper that checked the user's organisation but not their role, so any employee could delete a booking belonging to a colleague. One — a CSV export endpoint added late for a demo — took an `orgId` query parameter and checked nothing at all, which meant an authenticated user at one co-working operator could export the full booking history of another. Gate 4 failed too: the Prisma diff against production came back with eleven statements.

**Result:** Authorization was consolidated into a single `assertCan(user, action, resource)` layer that all twenty-three routes call, the export endpoint was rewritten to derive the org from the session rather than the query string, and the schema was reconciled with a squashed baseline migration. Six working days, no front-end changes, and Ruben had a written findings document to show the operators' IT contacts.

> *"Nineteen out of twenty-three routes were right. That's the part that scared me — I wasn't sloppy, I just wrote them across four months and Cursor had no idea what I'd decided in August. The wrong ones looked exactly like the right ones."*
> — **Ruben Aksoy, Founder, Kantoorplan (Rotterdam)**

**Cost & Timeline:** €2,900 (Launch Ready) — six working days.

---

## Frequently Asked Questions

### My repo is private. Do secrets in git history still count as compromised?

Yes. Private repos are cloned to laptops, forked into CI runners, cached by build systems and occasionally made public by accident, and history persists through all of it. Treat any credential that was ever committed as burned, rotate it at the provider, and only then decide whether rewriting history is worth the hour.

### Isn't a Zod schema on every route enough validation?

It handles the request path well, which is most of the traffic but not all of it. Background jobs, seeders, admin scripts and future endpoints all write to the same tables without passing through that schema, which is why the database needs its own constraints. The two layers do different jobs and both are cheap.

### How do I find authorization gaps without reading all twenty-something routes?

You mostly can't, and that is the point of the inventory — but you can narrow it fast by grepping for route handlers that read an ID from params or query without any nearby reference to the session or user. That gets you a shortlist in minutes, and the shortlist is almost always where the real findings are.

### Does closing these gates mean giving up on Cursor for future work?

Not at all, and a good handover should make Cursor more effective afterwards. Once authorization lives in one named function and the schema is reproducible from migrations, the conventions are explicit enough that the model follows them instead of inventing a fourth idiom each session.

### Which gate should I close first if I only have one weekend?

Gate 1, then Gate 2. A leaked credential is an active, ongoing exposure that costs nothing to check, and broken authorization is the failure most likely to end in a disclosure conversation with a customer. Observability and dependency hygiene matter, but they don't lose you someone else's data.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "My repo is private. Do secrets in git history still count as compromised?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Private repos are cloned to laptops, forked into CI runners and cached by build systems, and history persists through all of it. Rotate any credential that was ever committed, then decide separately whether to rewrite history."
      }
    },
    {
      "@type": "Question",
      "name": "Isn't a Zod schema on every route enough validation?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It covers the request path but not background jobs, seeders, admin scripts or future endpoints, all of which write to the same tables. Database constraints enforce the rules regardless of which code path writes, and both layers are cheap."
      }
    },
    {
      "@type": "Question",
      "name": "How do I find authorization gaps without reading all twenty-something routes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Grep for handlers that read an ID from params or query with no nearby reference to the session or user. That produces a shortlist in minutes, and the shortlist is usually where the real findings are."
      }
    },
    {
      "@type": "Question",
      "name": "Does closing these gates mean giving up on Cursor for future work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Once authorization lives in one named function and the schema is reproducible from migrations, the conventions are explicit enough that the model follows them rather than inventing a new idiom each session."
      }
    },
    {
      "@type": "Question",
      "name": "Which gate should I close first if I only have one weekend?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Gate 1 then Gate 2. A leaked credential is an active exposure that costs nothing to check, and broken authorization is the failure most likely to end in a disclosure conversation with a customer."
      }
    }
  ]
}
</script>
