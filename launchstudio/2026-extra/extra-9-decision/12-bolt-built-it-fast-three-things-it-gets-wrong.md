---
Title: "Bolt Built It Fast: The Three Things It Almost Never Sets Up Correctly"
Keywords: Bolt.new production, bolt ai app security, WebContainer limitations, environment variables exposed, Supabase RLS Bolt, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Bolt Built It Fast: The Three Things It Almost Never Sets Up Correctly

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bolt Built It Fast: The Three Things It Almost Never Sets Up Correctly",
  "description": "Bolt gets a working full-stack app in front of you in under an hour, but three specific layers come out wrong almost every time: secret handling, server-side authorization, and everything about deployment persistence. A technical breakdown of what to check and how to fix each one.",
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
  "datePublished": "2027-01-06",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/bolt-built-it-fast-three-things-it-gets-wrong"
  }
}
</script>

Everyone talks about how fast Bolt is. Almost nobody talks about *why* it's that fast, which is the more useful conversation — because the architectural decisions that make Bolt produce a running app in forty minutes are the same decisions that leave three specific layers unfinished, every single time.

Bolt runs your project in a WebContainer: a Node runtime compiled to WebAssembly, executing inside your browser tab. There is no VM being provisioned, no container being pulled, no Postgres daemon starting up. That is the trick, and it is a genuinely impressive one. It also means Bolt's model of "your app works" is bounded by what can run in a browser sandbox — and the three things that live outside that boundary are exactly the three things that decide whether you can charge money safely. This is not a criticism of the tool. It is a description of where the tool's job ends and yours begins.

## Thing one: your secrets are in the bundle

Start here, because it is the fastest to check and the most likely to be true.

Bolt scaffolds Vite or Next projects and wires third-party services by reading keys from environment variables. In Vite, any variable exposed to client code must be prefixed `VITE_`. In Next, `NEXT_PUBLIC_`. Those prefixes are not a naming convention — they are an instruction to the bundler meaning *inline this value into the JavaScript that ships to the browser*. Bolt reaches for them by default, because in a browser-only WebContainer there is frequently nowhere else for a value to live.

For a Supabase anon key, that is correct and intended; the anon key is designed to be public and is safe precisely because RLS is supposed to be doing the real work (see thing two). For anything else, it is a leak. The ones we find most often, in rough order of frequency:

- `VITE_SUPABASE_SERVICE_ROLE_KEY` — a key that bypasses every RLS policy you have. Its presence in a client bundle means the entire database is readable and writable by anyone who opens devtools.
- OpenAI or Anthropic keys, so the AI feature can call the model "from the front end." Someone will find it and burn your quota; billing alerts are how most founders discover this.
- Stripe **secret** keys (`sk_live_…`) rather than publishable ones.
- Resend, SendGrid or Twilio credentials, which turn your account into someone else's spam relay.
- Admin webhook URLs and Slack tokens hardcoded in a helper file rather than an env var at all.

The check takes two minutes. Build the project, then grep the output:

```
npm run build
grep -rEo "(sk_live|sk_test|service_role|eyJ[A-Za-z0-9_-]{20,})" dist/ | sort -u
```

Anything that comes back is public. And note: rotating the key is only half the fix. If that key was ever committed, it lives in git history and in every fork and deploy log. Rotate at the provider, then fix the architecture — route those calls through a server: a Next route handler, a Supabase Edge Function, a small Hono or Express service. The pattern is always the same. The browser calls *your* endpoint; your endpoint holds the credential and calls the vendor.

## Thing two: authorization was never actually implemented

Bolt will happily build you auth. Sign-up, sign-in, session handling, a protected route that redirects to `/login` when there's no session. It looks complete, and for authentication it broadly is.

Authorization is the layer that decides whether *this* authenticated user may perform *this* action on *this* row, and it is almost always missing or fake. Three patterns show up repeatedly:

**Client-side route guards as the only gate.** A `<ProtectedRoute>` wrapper checking `session?.user`, with the actual data fetch running unguarded underneath. The redirect is cosmetic. The fetch is the security boundary, and it has no opinion about who is asking.

**Supabase tables with RLS off, or a permissive policy.** Bolt generates SQL that creates tables and often enables RLS with a policy along the lines of `USING (true)` — which satisfies the linter and protects nothing. Verify from psql or the SQL editor rather than trusting the migration file:

```sql
select relname, relrowsecurity from pg_class
where relnamespace = 'public'::regnamespace and relkind = 'r';

select tablename, policyname, cmd, qual, with_check from pg_policies
where schemaname = 'public';
```

Read the `qual` column carefully. `(auth.uid() = user_id)` is a real policy. `true` is not. And check `with_check` separately — a table can be correctly restricted for SELECT and wide open for INSERT, which is how people end up writing rows they don't own.

**Ownership never checked in API routes.** Where Bolt did generate server code, the typical shape is `const { id } = params; return db.query('select * from invoices where id = $1', [id])`. Authentication passed. Nobody asked whether that invoice belongs to the caller. Classic IDOR, and it is trivially discoverable by incrementing an integer.

The structural fix is to decide, once, where authorization is enforced — in RLS policies or in a server layer — and make everything go through it. Mixed models are where the holes appear: half your reads honour RLS, half go through a service-role client that ignores it, and nobody can tell you which is which six weeks later.

## Thing three: what Bolt calls "deployed" is a preview, not an environment

Bolt's one-click Netlify deploy is a real deploy. It is also a single environment with no separation between what you are experimenting with and what your users depend on, and that distinction is the whole of production discipline.

Concretely, here is what does not exist yet in a fresh Bolt project:

**Schema migration history.** In WebContainer there is no local Postgres, so schema changes happen against your live Supabase project — from the dashboard, from a chat prompt, from an ad-hoc SQL snippet. The result is a database whose structure exists in exactly one place: production. You cannot rebuild it, cannot stand up a staging copy that matches, cannot review a schema change in a PR, cannot roll one back. Getting onto `supabase db diff` and a checked-in `supabase/migrations` directory is genuinely a few hours of work and it is the single highest-leverage cleanup available to you.

**Separate projects for dev and prod.** One Supabase project used for both means your first "let me just test the delete flow" is run against customer data.

**Backups.** Free-tier Supabase gives you nothing to restore from. Daily backups start on Pro; point-in-time recovery is a further add-on. Decide which one your data justifies before you need it, not after.

**Anything watching the runtime.** No Sentry, no structured logging, no uptime check, no alert. Netlify tells you the build succeeded. Nothing tells you that a null reference has been crashing checkout for eleven hours.

**Native-dependency assumptions.** WebContainer cannot run native Node addons, so Bolt steers around them. Code that ran fine in the browser sandbox can behave differently on a real Node runtime — around file system access, `crypto` usage, streaming and image processing especially. Test on the actual target before you announce a date.

**Rate limiting and abuse control.** No throttle on sign-up, on password reset, on the endpoint that calls a paid LLM. The first person who scripts against your `/api/generate` route will explain this to you via your invoice.

## The webhook problem that sits across all three

Payments deserve their own mention because they fail through a combination of the three issues above. Bolt-generated Stripe integrations typically create a Checkout Session correctly, then mark the user as subscribed on the success redirect. That is not payment confirmation — it is a browser landing on a URL, which is forgeable, bookmarkable, and skippable when the network drops mid-redirect.

The server-side path is `stripe.webhooks.constructEvent(rawBody, signature, endpointSecret)`. Two details break it in practice. First, it needs the **raw** request body: any framework that has already parsed JSON will produce a signature mismatch, which is why so many AI-written handlers quietly wrap the verification in a try/catch and continue anyway. Read your handler and check that a failed verification returns 400 and processes nothing. Second, webhooks retry, so handlers must be idempotent — key on the Stripe event ID and ignore duplicates, or a retried `invoice.paid` will grant credits twice.

Then ask which events you actually handle. `checkout.session.completed` alone is not a subscription business. Without `customer.subscription.updated`, `customer.subscription.deleted` and `invoice.payment_failed`, cancelled and delinquent customers keep full access indefinitely and your database's view of who is paying drifts permanently away from Stripe's.

## A one-hour audit you can run tonight

In order, because each step informs the next:

1. Build and grep the bundle for secrets. Rotate anything found, at the provider.
2. Query `pg_policies` and read every `qual` and `with_check`. Note tables with RLS off entirely.
3. Grab a session token from your own browser, then curl a detail endpoint with another user's record ID. If it returns data, you have IDOR.
4. Open the Stripe handler. Confirm signature verification, raw body, 400 on failure, idempotency key, and which event types are handled.
5. `ls supabase/migrations`. Empty or missing means your schema is undocumented.
6. Check whether prod and dev point at the same Supabase project and the same Stripe mode.
7. Trigger a deliberate server error and see whether anything anywhere notices.

Score yourself honestly. Two or fewer findings and you are in normal indie-hacker territory — fix them over a weekend. Five or more and you are looking at a week of unfamiliar infrastructure work you are unlikely to enjoy, at exactly the moment your attention should be on customers.

That is the actual decision this article is about: not whether Bolt was the wrong choice — it wasn't, it saved you a month of front-end work — but whether hardening it yourself is the best use of the next two weeks. [LaunchStudio](https://launchstudio.eu/en/) exists for the second answer: the front end stays exactly as Bolt built it, the three layers above get done properly, and the work runs at roughly a fifth of what an agency would quote to rebuild the whole thing. The engineers on it come out of [Manifera's team](https://www.manifera.com/services/custom-software-development/), which has spent eleven-plus years doing precisely this class of work for clients with considerably less tolerance for a leaked service-role key.

Want a second pair of eyes from someone who reads AI-generated code every day? Send over the repo and we'll come back with the findings list, not a sales deck.

## Real example

### The Grep That Cost €340 in API Credits

Joost Brinkman, an indie hacker in Eindhoven, built Draftpilot in Bolt over a long weekend — a tool that turns meeting transcripts into structured project briefs using an LLM. He posted it in two Slack communities and had 140 signups in five days, which felt like validation right up until the OpenAI usage alert arrived.

The key was in the bundle. `VITE_OPENAI_API_KEY`, inlined into the client JavaScript, because the transcript-processing call was made straight from the browser. Somebody had extracted it and used it for their own workload. The same review turned up two more issues: RLS was enabled on the `transcripts` table with a `USING (true)` policy, and the Stripe upgrade flow granted the paid plan on redirect with no webhook listener at all.

**Result:** The LLM calls moved behind a Supabase Edge Function with per-user rate limiting, RLS policies were rewritten against `auth.uid()`, and a signed webhook handler took over subscription state — with idempotency keyed on the event ID. Four working days, and Joost's front end was never opened.

> *"I knew about the VITE_ prefix. I'd read about it. I just never connected 'this gets inlined' with 'this is my credit card.' The grep took eleven seconds and I felt sick for the rest of the afternoon."*
> — **Joost Brinkman, Founder, Draftpilot (Eindhoven)**

**Cost & Timeline:** €1,850 (Launch Ready) — four working days.

---

## Frequently Asked Questions

### Is the Supabase anon key in my client bundle a security problem?

No — it is designed to be public, and Supabase's architecture assumes it will be visible. It only becomes a problem when RLS policies are missing or permissive, because the anon key is then a fully functional database credential. The key to panic about is `service_role`, which bypasses RLS entirely and must never leave your server.

### Why does my Stripe webhook signature verification fail even though the secret is right?

Almost always because the body was parsed before verification. `constructEvent` needs the exact raw bytes Stripe signed, so any JSON body-parser middleware running first will produce a mismatch. In Next route handlers use `await req.text()`; in Express, mount `express.raw({ type: 'application/json' })` on that route specifically.

### Does moving off Bolt require rewriting the front end?

No, and you generally shouldn't. Bolt outputs standard Vite or Next projects with ordinary React components — once exported to a git repo they are simply a codebase, editable in any editor. The work worth doing is on the server, data and deployment layers, none of which touches your components.

### How do I test whether my app has IDOR without a security tool?

Create two accounts, note a record ID belonging to the second, then request that record while authenticated as the first — with curl or Postman, not the UI, since the UI will never construct that request. Any response other than a 403 or 404 is a finding. Repeat for each endpoint that takes an ID.

### Is WebContainer's lack of a real database an actual production risk?

Indirectly, yes. It is the reason schema changes get applied ad hoc to a live Supabase project instead of through migration files, which leaves you with no reviewable history, no staging environment that matches production, and no rollback path. That absence tends to cost more over a year than any single security finding.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is the Supabase anon key in my client bundle a security problem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, it is designed to be public and Supabase assumes it will be visible. It becomes dangerous only when RLS policies are missing or permissive. The key that must never reach the client is service_role, which bypasses RLS entirely."
      }
    },
    {
      "@type": "Question",
      "name": "Why does my Stripe webhook signature verification fail even though the secret is right?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually because the body was parsed before verification. constructEvent needs the exact raw bytes Stripe signed, so JSON body-parser middleware causes a mismatch. Use await req.text() in Next route handlers, or express.raw on that route in Express."
      }
    },
    {
      "@type": "Question",
      "name": "Does moving off Bolt require rewriting the front end?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Bolt outputs standard Vite or Next projects with ordinary React components, which are just a codebase once exported to git. The work worth doing sits in the server, data and deployment layers and does not touch your components."
      }
    },
    {
      "@type": "Question",
      "name": "How do I test whether my app has IDOR without a security tool?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Create two accounts, note a record ID owned by the second, and request it with curl while authenticated as the first. Anything other than a 403 or 404 is a finding. Repeat for every endpoint that accepts an ID."
      }
    },
    {
      "@type": "Question",
      "name": "Is WebContainer's lack of a real database an actual production risk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Indirectly. It is why schema changes get applied ad hoc to a live Supabase project rather than through migration files, leaving no reviewable history, no matching staging environment and no rollback path."
      }
    }
  ]
}
</script>
