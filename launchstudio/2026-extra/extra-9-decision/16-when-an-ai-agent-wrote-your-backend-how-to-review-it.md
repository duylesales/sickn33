---
Title: "When an AI Agent Wrote Most of Your Backend: How to Review What You Can't Read"
Keywords: review AI generated backend, agentic coding review, AI code audit method, trust boundary review, hallucinated dependencies, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# When an AI Agent Wrote Most of Your Backend: How to Review What You Can't Read

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "When an AI Agent Wrote Most of Your Backend: How to Review What You Can't Read",
  "description": "Reading 14,000 lines of agent-written backend code line by line is not a plan. This is a six-pass review method that finds the failures agentic coding actually produces, ordered so that each pass narrows what the next one has to look at.",
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
  "datePublished": "2027-01-15",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/when-an-ai-agent-wrote-your-backend-how-to-review-it"
  }
}
</script>

It's the Saturday after the sprint that finally worked. Sixty-one files in `server/`, about fourteen thousand lines, produced across nine agent sessions over three weeks. You directed all of it. You approved every plan. You have read, generously, perhaps a fifth of what shipped — and the fifth you read was mostly the parts that broke.

Now you want to charge money for it, and the honest position is uncomfortable: you are the owner of a codebase you did not write and cannot fully account for. Reading it end to end is not a plan; at a careful thirty lines a minute that is eight hours of the worst kind of attention, and you'd retain almost none of it. Skimming it is theatre.

What works instead is a review structured around the specific ways agentic coding fails — which are not the ways human juniors fail. Agents produce code that is locally correct and globally inconsistent: each file is plausible, each function does roughly what its name claims, and the failures live in the seams between sessions. Six passes, each one narrowing the surface the next has to examine. Budget one focused day.

## Pass 1: Find the trust boundary and draw it on paper

Before reading any code, establish the map. Every backend has a line where untrusted input becomes trusted data, and every serious bug in agent-written code is a place where that line was crossed without anyone noticing.

Enumerate every entry point — not by memory, by grep. Route definitions, queue consumers, cron handlers, webhook receivers, websocket message handlers, server actions, GraphQL resolvers, anything with a public URL.

```
rg -n "app\.(get|post|put|patch|delete)\(|router\.(get|post)|export async function (GET|POST|PUT|PATCH|DELETE)|@(Get|Post)\(" server/ app/ src/ --no-heading
```

Put the results in a table with four columns: path, authenticated?, authorized-by-what?, writes-what. Fill it in by looking, not by assuming. The table takes forty minutes and it is the single most valuable artefact of the whole review, because it converts "fourteen thousand lines" into "thirty-one entry points, of which eleven need a closer look."

Two categories will jump out immediately. Endpoints you had forgotten existed — a debug route, a seed endpoint, an admin helper from session four that was never removed. And endpoints where the authorization column is blank because you had to go and read the handler and still couldn't tell. Both are findings before you have read a single line properly.

## Pass 2: Trace four flows end to end, ignoring everything else

Now read code — but only along four paths, following the data rather than the file structure.

**Sign-up.** Where is the password hashed, with what, at what cost factor? Is the email verified before the account can do anything meaningful? Can I register with a role field in the request body? Is there any rate limit? Agents commonly generate a `users` table with a `role` column and an insert that spreads the request body into it — `...req.body` — which means self-service admin.

**Login and session.** What is in the token or session cookie? Is it signed with a secret from the environment or with a literal fallback string like `'secret'` that the agent added so local dev would work? Are cookies `httpOnly`, `secure`, `sameSite`? How does logout invalidate anything? Grep for `jwt.sign` and read every call site.

**Pay.** From the checkout call through to the moment access is granted. The single question that matters: what fact causes the database to record someone as paying? If the answer involves a browser redirect rather than a signature-verified server-to-server event, that is your most urgent finding.

**Delete.** Pick the most destructive action your product offers and follow it. Who may call it, what does it cascade to, and is it recoverable? Agents love `ON DELETE CASCADE` because it makes constraint errors go away.

Four flows is perhaps ninety minutes and covers the paths where a failure is expensive. Everything else in the codebase can be wrong in ways that merely annoy people.

## Pass 3: Grep for the patterns agents produce under pressure

Certain constructs appear specifically because a model needed to get past an obstacle in the moment. Each is a fingerprint.

```
rg -n "catch\s*\([^)]*\)\s*\{\s*\}" --type ts --type js          # swallowed errors
rg -n "\|\|\s*['\"](secret|dev|changeme|test)" --type ts          # literal fallbacks for env vars
rg -n "process\.env\.[A-Z_]+\s*\|\|" --type ts                    # same, generalised
rg -n "eslint-disable|@ts-ignore|@ts-expect-error|as any"         # suppressed complaints
rg -n "SELECT .*\$\{|query\(\s*[\"'`].*\+\s*" --type ts           # string-built SQL
rg -n "Access-Control-Allow-Origin.*\*"                           # permissive CORS
rg -n "TODO|FIXME|for now|in production you would"                # the agent told you
```

That last one is worth dwelling on. Models frequently write a comment explaining that the code is a placeholder — "In production, verify this signature" — and then the code ships with the comment intact. Grepping for those phrases regularly finds three or four real issues in an afternoon, and they come pre-annotated with what's wrong.

The swallowed-error pattern is the one that hides the others. An empty catch block around a signature verification, a permission check, or a transaction commit turns a loud failure into a silent success, and silent success is why an app can be broken for months without anyone noticing.

## Pass 4: Verify the dependency list is real

Open `package.json` and read every line of it, which takes four minutes and is the highest ratio of value to effort in this entire process.

For each package: do you remember deciding on it? If not, check that it exists as a real, maintained project with meaningful download numbers and a repository that predates your project. Models occasionally invent plausible package names, and attackers have started registering exactly the names models tend to invent — so an unfamiliar dependency with 200 weekly downloads and a first publish two months ago deserves genuine suspicion.

Then look for redundancy. Three date libraries, two HTTP clients, two validation libraries, `bcrypt` and `argon2` both present with only one actually used. None of it is broken; all of it is attack surface and bundle weight accumulated because session six had no memory of session two.

```
npm audit --omit=dev
npx depcheck
npm ls --depth=0
```

Delete what nothing imports. Consolidate the duplicates. Pin what remains.

## Pass 5: Ask the agent to explain, then verify independently

This pass uses the tool that wrote the code, carefully, because its explanations are useful evidence and terrible proof.

Good questions, asked one at a time in a fresh session with the repo available: *List every endpoint that reads a record by ID and does not verify ownership.* *Where is authorization enforced in this codebase, and is it consistent across all routes?* *Which environment variables are read in code that ships to the browser?* *Show me every place a value from the request body is written to the database without validation.*

The answers are leads. Every one has to be confirmed by looking at the file yourself, because a model asked to audit its own output has a marked tendency toward reassurance, and because it will confidently describe a check that exists in a file it wrote in a different session and no longer has in context.

The inverted question is more reliable than the direct one. Instead of "is this secure," ask "write me a curl command that would exploit this endpoint if authorization were missing." Then run it. A model is considerably better at generating an attack than at assessing a defence, and the result is an actual test rather than an opinion.

## Pass 6: Prove three things with tests, not with reading

End with evidence. Not a test suite — three tests, each proving a fact you currently only believe.

**Cross-tenant isolation.** Two accounts, one record owned by B, requested by A, on every endpoint that accepts an ID. Automate it as a loop over the table from Pass 1. This finds more real bugs than any other single activity, because IDOR is what agent-written code produces most reliably: the model has the record ID in scope and no reason to think about ownership unless the prompt mentioned it.

**Webhook forgery.** Post an unsigned, hand-written payload to your payment webhook. It must return 4xx and change nothing. Then post a valid event twice and confirm the second is a no-op.

**Privilege escalation on write.** Send a legitimate profile-update request with `"role": "admin"` and `"credits": 999999` appended. Then re-read the record. Anything that changed which shouldn't have is a mass-assignment bug, and this is the single most common way agent-written CRUD is wrong.

Three tests, an hour, and they run in CI forever after — so the same class of bug cannot come back in session ten.

## What the review produces, and what to do with it

At the end of one focused day you have an entry-point table, a list of findings ranked by blast radius, and three regression tests. That is a genuinely defensible position, and it is more review than most funded startups perform on their own code.

The harder question is what to do about the findings. Some are twenty-minute fixes. Others — consolidating authorization into a single enforced layer, introducing migration discipline, reworking a payment flow that grants access on a redirect — are structural, and they are exactly the work that agents are worst at, because they require holding the whole system in mind at once rather than one file at a time. That is the point at which people bring in [LaunchStudio](https://launchstudio.eu/en/): you keep the code and the front end, an engineer who reads agent-written code daily closes the structural findings, and you get the reasoning documented so your next agent session builds on a convention instead of inventing one. Behind the work sits [Manifera](https://www.manifera.com/services/custom-software-development/) and eleven-plus years of production engineering — the review discipline is the same one applied to enterprise systems, scoped to a one-to-three-week engagement at a fixed price.

Run the six passes yourself first. Then, if the findings list is longer than your appetite, send us read-only access to the repository and we'll come back with our own — findings first, quote second, and no obligation between the two.

## Real example

### Thirty-One Endpoints, Two That Mattered

Wessel Duijn built Merkwacht over five weeks with an agentic coding tool — a brand-monitoring service that scrapes mentions across forums and marketplaces for consumer brands, sold at €149 a month to six agencies during a private beta. He is a solid developer; he had directed every session and reviewed the plans. He had read maybe 20% of what shipped.

Pass 1 produced thirty-one entry points, four of which he did not recognise, including a `/api/_debug/reindex` route from an early session that accepted a client ID and triggered a full re-scrape — unauthenticated, and expensive, since each run cost real money in proxy fees. Pass 6's isolation loop found the second real issue: the mentions export endpoint scoped results by a `clientId` query parameter rather than by the session, so any agency user could export another agency's competitive monitoring data. The remaining findings were routine: an empty catch block around the Stripe signature verification, a JWT secret with a literal fallback, and two abandoned date libraries.

**Result:** Authorization consolidated behind one `assertClientAccess` layer used by all thirty-one endpoints, the debug route removed, webhook verification made strict and idempotent, and a cross-tenant isolation test added to CI that iterates every ID-accepting endpoint automatically. Five working days, and Wessel's front end and agent workflow both stayed exactly as they were.

> *"The debug endpoint was the one that got me. I didn't forget about it — I never knew it existed. It was in a plan I approved at 1am in week one and it had been sitting there, live, costing me proxy credits, for a month."*
> — **Wessel Duijn, Founder, Merkwacht (Nijmegen)**

**Cost & Timeline:** €2,600 (Launch Ready) — five working days.

---

## Frequently Asked Questions

### Can I just ask the agent to audit its own code and act on the report?

Use it for leads, not conclusions. A model auditing its own output skews toward reassurance and will describe checks that exist in files it wrote in a session it no longer has in context. The reliable inversion is asking it to write the exploit rather than assess the defence, then running what it gives you.

### How long does this six-pass review actually take on a mid-sized backend?

One focused day for something in the ten-to-twenty-thousand-line range: about forty minutes for the entry-point table, ninety for the four flow traces, half an hour of grepping, a few minutes on dependencies, and the rest split between the agent-assisted pass and writing three tests. It scales with entry points, not with line count.

### Which finding should I fix first if they all look serious?

Rank by blast radius rather than severity labels. Anything letting one customer reach another customer's data comes first, then anything granting paid access without payment, then anything that loses data irreversibly. Swallowed errors and dependency sprawl are real but they cost you time rather than trust.

### Is agent-written backend code worse than what a junior developer would produce?

Different, not strictly worse. It is usually more idiomatic and better structured per file than junior work, and considerably less consistent across files, because each session has no memory of the conventions the last one established. The bugs cluster in the seams rather than inside functions.

### Do I need to stop using agentic tools once the codebase is in production?

No — but the conventions need to be explicit enough for the model to follow. Once authorization lives in one named function, the schema comes from migration files and CI runs your isolation test, an agent session is far less likely to introduce a fourth way of doing things, because the existing pattern is visible in every file it reads.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I just ask the agent to audit its own code and act on the report?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use it for leads, not conclusions. A model auditing its own output skews toward reassurance and describes checks written in sessions it no longer has in context. Asking it to write the exploit rather than assess the defence, then running that, is far more reliable."
      }
    },
    {
      "@type": "Question",
      "name": "How long does this six-pass review actually take on a mid-sized backend?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "About one focused day for a ten-to-twenty-thousand-line backend: forty minutes for the entry-point table, ninety for the flow traces, half an hour of grepping, minutes on dependencies, and the rest on the agent-assisted pass and three tests. It scales with entry points, not line count."
      }
    },
    {
      "@type": "Question",
      "name": "Which finding should I fix first if they all look serious?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Rank by blast radius. Anything letting one customer reach another's data comes first, then anything granting paid access without payment, then anything that loses data irreversibly. Swallowed errors and dependency sprawl cost time rather than trust."
      }
    },
    {
      "@type": "Question",
      "name": "Is agent-written backend code worse than what a junior developer would produce?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Different rather than worse. It is usually more idiomatic per file than junior work but far less consistent across files, since each session lacks memory of the last one's conventions. The bugs cluster in the seams rather than inside functions."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need to stop using agentic tools once the codebase is in production?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, but the conventions must be explicit. Once authorization lives in one named function, the schema comes from migrations and CI runs an isolation test, an agent session is much less likely to invent a fourth pattern, because the existing one is visible in every file it reads."
      }
    }
  ]
}
</script>
