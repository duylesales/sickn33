---
Title: "Replit Built and Deployed It — Why That's Not the Same as Launched"
Keywords: Replit deployment production, Replit Agent app security, replit.app custom domain, dev vs production database, AI code vulnerabilities, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Replit Built and Deployed It — Why That's Not the Same as Launched

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Replit Built and Deployed It — Why That's Not the Same as Launched",
  "description": "Replit's Deploy button produces a real, publicly reachable URL in about ninety seconds, which is why founders mistake it for launching. This is a side-by-side breakdown of the nine things Replit's deployment genuinely covers versus what a launched product requires, with the specific checks for each.",
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
  "datePublished": "2027-01-13",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/replit-deployed-it-why-thats-not-launched"
  }
}
</script>

Ninety seconds. That is roughly how long it takes, from clicking Deploy in Replit, to having a real HTTPS URL that anyone on the internet can open. Compared to the days it took to provision a server and configure nginx not that long ago, it is a genuine achievement, and it is not marketing — the URL works, the TLS certificate is valid, the app responds.

Which is exactly why it causes the confusion it does. In every other era of software, "publicly reachable at a real address" *was* the hard part, so it became shorthand for being launched. Replit collapsed that step to ninety seconds without collapsing anything else, and now a large number of founders are running production businesses on a setup whose only production-grade property is that it responds to requests. Below is a straight comparison: what the Deploy button genuinely gives you, and what still stands between that and a product you can responsibly charge for. This matters more with Agent-generated code than hand-written code — roughly 45% of AI-generated code ships with security vulnerabilities, and a deployment that works flawlessly gives you no signal at all about which 45%.

## Deployed: a URL. Launched: an identity.

Replit gives you `yourapp.replit.app` and a valid certificate. That is real hosting, not a preview link.

What it isn't is your product's address. Custom domains are supported and take about ten minutes to configure, and until you do it, three things are true: your marketing has a subdomain of someone else's brand in it, your cookies live on a shared parent domain, and moving later means every link anyone has shared breaks. Do the domain early — not because it's hard, but because the cost of doing it late is entirely made of other people's bookmarks.

The related item that founders skip entirely is email DNS. Password resets and receipts sent from a fresh domain without SPF, DKIM and DMARC records land in spam at rates that will make you think your product has an activation problem when it has a DNS problem. Send yourself a test through mail-tester.com before you conclude anything about your funnel.

## Deployed: one environment. Launched: two, deliberately separated.

This is the structural issue, and everything else in this article is downstream of it.

In Replit, your development workspace and your deployment are related but distinct — a deployment snapshots your code at publish time. The database usually is not snapshotted. If your Repl uses Replit's built-in Postgres (Neon-backed), or an external Supabase project, the default arrangement is that the workspace you are actively editing and the deployment your customers use point at the same data.

Which means your next casual experiment — testing the delete flow, running a quick backfill, letting the Agent "clean up the seed data" — runs against production. Not through carelessness; through architecture. The fix is a second database and a second set of secrets, so that `DATABASE_URL` in the workspace and `DATABASE_URL` in the deployment are genuinely different values. Replit's Secrets pane supports deployment-scoped values; use them. Then verify by connecting to each and comparing row counts, because assuming this is configured correctly is exactly the mistake.

While you're there: check `NODE_ENV`. A surprising number of Agent-built Express apps run in development mode in production, which typically means verbose error pages with stack traces served to whoever triggers them.

## Deployed: secrets in a pane. Launched: secrets never in the client.

Replit's Secrets feature is genuinely good — encrypted, injected as environment variables, not in your source. Credit where due.

The failure is the same one every browser-bundled framework produces: if the front end needs a value, it gets a `VITE_` or `NEXT_PUBLIC_` prefix, and that prefix means *inline this into the JavaScript everyone downloads*. Agent-built apps that call an LLM, send an email or hit a payments API directly from the browser will have done this, because in a demo it's the shortest path.

Build the deployment locally and grep the output for `sk_live`, `sk_test`, `service_role` and long JWT-shaped strings. Anything that appears is public and needs rotating at the provider and moving behind a server route. Also check the Repl's fork status — a public Repl that was ever forked carries whatever was in `.env` or hardcoded into the fork, permanently.

## Deployed: it runs. Launched: it runs under people who don't like you.

An Agent-built app has, essentially without exception, no rate limiting. Nothing throttles sign-up, password reset, or the endpoint that spends your money on an LLM call. It has no bot protection on registration, so your users table fills with disposable addresses. It usually has no request size limit, so an upload endpoint accepts a 400MB file until something falls over.

The bare minimum before you take real traffic: a limiter on auth endpoints (5–10 attempts per IP per fifteen minutes), a per-user limit on anything that costs you per call, a body size cap, and a hard spending limit configured at the LLM provider — the last one because it is the only control that works when the other three have been circumvented.

And know your deployment type's behaviour under load. Autoscale deployments scale to zero and cold-start, which is fine for a dashboard and bad for a webhook receiver with a short timeout. Reserved VM keeps a machine warm and costs more. Static is for a front end with no server at all. Choosing the wrong one produces intermittent failures that look like bugs in your code.

## Deployed: data exists. Launched: data survives.

Ask a direct question: if the database were emptied right now — bad migration, a `DELETE` without a `WHERE`, an Agent session that went sideways — what would you restore from?

For most Replit projects the honest answer is nothing. Neon-backed Postgres offers history within a retention window depending on plan; Supabase gives daily backups on Pro and point-in-time recovery as an add-on. Neither is on by default at the free tier, and neither has been tested by you. Untested backups are a belief.

Schema history has the same problem in a sharper form. The Agent applies schema changes directly and describes them in chat, which is not a migration file. There is no reviewable record of what changed and when, no way to reproduce the structure in a second environment, and no rollback. Getting onto Drizzle or Prisma migrations, with a squashed baseline reflecting current production, is a half-day of work and it is what makes every subsequent change safe rather than exciting.

## Deployed: checkpoints. Launched: tests.

Replit's checkpoint system is a good undo mechanism and a poor safety net. It restores state; it does not tell you that a change broke checkout.

Agent-generated tests, where they exist, tend to be written to pass — asserting that a function returns something rather than that it returns the right thing under adversarial input. What you want before launch is small and specific: an end-to-end test for sign-up, one for the paid conversion, and one for the single action that would embarrass you most if it silently failed. Three tests running in CI on every deploy is worth more than eighty unit tests generated in one session.

CI itself is worth setting up. Replit deploys from the workspace; connecting the Repl to a GitHub repository and running a build plus those three tests before publish converts "I hope that worked" into a gate.

## Deployed: logs in a tab. Launched: someone gets woken up.

Replit shows you deployment logs while you're looking at them. Nobody looks at 22:00 on a Sunday.

Error tracking with source maps (Sentry's free tier is ample), an uptime check against a real endpoint rather than the homepage, and one alert that reaches your phone. That is thirty minutes of setup and it is the difference between finding out about a broken checkout from your dashboard and finding out from a refund request.

## Deployed: works for you. Launched: works for someone hostile.

The security checks that Agent-built code most often fails, in the order worth running them:

Ownership checks on every endpoint that takes an ID. Create two accounts, note a record ID belonging to the second, request it as the first via curl. Anything but 403 or 404 is a finding.

Server-side validation on every consequential field — price, quantity, plan, role, credits. If the value arrives from the client and is trusted, someone will send a different one.

Webhook signature verification, with the raw body, returning 400 on failure, and idempotent on retries. Agent-written Stripe handlers frequently catch the verification error and proceed anyway, because that makes local testing work without a signing secret.

CORS. `Access-Control-Allow-Origin: *` combined with credentialed requests is a real problem and a common default.

Error responses. Development-mode stack traces expose file paths, dependency versions and sometimes query fragments.

## Deployed: a technical state. Launched: a commercial one.

The last set is not engineering and gets forgotten by engineers. Terms and a privacy policy that reflect what your app actually stores. A cookie banner that gates analytics rather than decorating the page. A working route for a deletion request, which requires knowing every place a user's data lives. VAT handling on invoices if you sell B2B in the EU. A support address someone reads.

None of it appears in a deployment log. All of it appears in your first month of real customers.

## What to do with this list

Score it. If you fail two or three items, you have a productive weekend ahead. If you fail six or more — which is the common result for an Agent-built app that has never been reviewed by a second person — you are looking at a fortnight of infrastructure work in territory you have no particular reason to enjoy, at precisely the point where your attention belongs on customers.

That is the case [LaunchStudio](https://launchstudio.eu/en/) exists for: the app Replit built stays intact, the environment separation, secrets, migrations, rate limits, webhooks and monitoring get done properly, and you keep working in Replit afterwards on code that is documented for exactly that. It runs at roughly a fifth of what an agency charges to rebuild from scratch, on a fixed price agreed before anyone touches the repo — the engineers come from [Manifera](https://www.manifera.com/about-us/), whose eleven-plus years of production work happened mostly for clients where a shared dev-and-prod database would have ended a contract.

Tell us what you've built and what's worrying you — a short description gets a real answer from an engineer within one business day, not a brochure.

## Real example

### The Backfill That Ran Against the Wrong Database

Timo Reijnders, an indie hacker in Groningen, built Ploegrooster with the Replit Agent — a shift-scheduling tool for hospitality teams. Eleven bars and restaurants were on it, paying €19 a month, and it had been running without incident for two months.

Then he asked the Agent to clean up some test rosters left over from development. The Agent did exactly what it was asked, against the only database it had ever known — which was also the one eleven venues had their October schedules in. About 340 published shifts vanished on a Thursday afternoon. Nothing to restore from: free-tier database, no backups, no migration history, no separate environment. He rebuilt what he could from customers' screenshots.

The review afterwards found four more items from the list above. Same database for workspace and deployment, obviously. But also: `NODE_ENV` unset, so production was serving development stack traces; no rate limit on password reset; and a shift-detail endpoint that took an ID and never checked which venue it belonged to, meaning any logged-in manager could read another venue's staffing and hourly costs.

**Result:** Separate dev and production databases with deployment-scoped secrets, Drizzle migrations with a squashed baseline, daily backups plus a tested restore, per-venue ownership checks on all seventeen endpoints, and rate limiting on the auth routes. Seven working days, and Timo kept building in Replit afterwards.

> *"The data loss was survivable — embarrassing, but survivable. What actually kept me up was finding out the endpoint that leaked one venue's labour costs to another had been live the entire time. Nobody had found it. That's not the same as it being safe."*
> — **Timo Reijnders, Founder, Ploegrooster (Groningen)**

**Cost & Timeline:** €2,750 (Launch & Grow) — seven working days.

---

## Frequently Asked Questions

### Do I have to move off Replit to run a real product?

No. Replit's deployments are legitimate hosting and plenty of paying products run on them. What has to change is the configuration around the app: separate environments, deployment-scoped secrets, real backups, migration history and monitoring. Those are setup decisions, not a reason to migrate platforms.

### How do I tell whether my workspace and deployment share a database?

Connect to each using the `DATABASE_URL` visible in the workspace and the one scoped to the deployment, and compare the host and a row count on a busy table. If the values are identical, they are the same database. Do not infer this from the Agent's description — check the connection strings directly.

### Which Replit deployment type should I be on?

Autoscale suits request-driven apps that tolerate cold starts and is cheapest at low volume. Reserved VM suits anything with background jobs, websockets, or webhook endpoints where a cold start risks a timeout from the sender. Static is only for a front end with no server. Mismatches show up as intermittent failures that look like application bugs.

### Are the tests the Agent wrote worth keeping?

Keep them, but don't count on them. Generated tests tend to assert that code runs rather than that it behaves correctly under bad input, so they pass while real bugs survive. Three end-to-end tests covering sign-up, payment and your single most important action are worth more than a large generated unit suite.

### If my app has been live for months with no incident, is it probably fine?

Not necessarily — most of the failures described here are silent by nature. An endpoint leaking data between customers produces no errors, no alerts and no complaints; it simply works, for the wrong person. Absence of incident is evidence about traffic and luck, not about the code.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I have to move off Replit to run a real product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Replit deployments are legitimate hosting. What has to change is the configuration around the app: separate environments, deployment-scoped secrets, real backups, migration history and monitoring. Those are setup decisions rather than a reason to migrate."
      }
    },
    {
      "@type": "Question",
      "name": "How do I tell whether my workspace and deployment share a database?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Compare the DATABASE_URL visible in the workspace with the one scoped to the deployment, checking host and a row count on a busy table. Identical values mean one database. Verify the connection strings directly rather than trusting a description of the setup."
      }
    },
    {
      "@type": "Question",
      "name": "Which Replit deployment type should I be on?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Autoscale suits request-driven apps that tolerate cold starts. Reserved VM suits background jobs, websockets or webhook receivers where a cold start risks a sender timeout. Static is only for a serverless front end. Mismatches appear as intermittent failures resembling application bugs."
      }
    },
    {
      "@type": "Question",
      "name": "Are the tests the Agent wrote worth keeping?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Keep them but don't rely on them. Generated tests often assert that code runs rather than that it behaves correctly under bad input. Three end-to-end tests covering sign-up, payment and your most important action are worth more than a large generated unit suite."
      }
    },
    {
      "@type": "Question",
      "name": "If my app has been live for months with no incident, is it probably fine?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not necessarily, because most of these failures are silent. An endpoint leaking data between customers produces no errors and no complaints; it simply works for the wrong person. Absence of incident is evidence about traffic and luck, not about the code."
      }
    }
  ]
}
</script>
