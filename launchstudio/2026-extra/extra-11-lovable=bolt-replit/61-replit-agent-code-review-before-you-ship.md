---
Title: "Replit Agent Code Review: What to Check Before You Ship It"
Keywords: Replit, replit agent generated code, ai app security, dependency review, reviewing generated output, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Replit Agent Code Review: What to Check Before You Ship It

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Replit Agent Code Review: What to Check Before You Ship It",
  "description": "An agent that installs packages, writes files and changes configuration touches a wider surface than a code suggestion. The five things to read first, how to review output you did not write, and what the agent cannot decide for you.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-02",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/replit-agent-code-review-before-you-ship" }
}
</script>

There is a difference between an assistant that suggests a line of code and one that builds the thing. The first proposes; you accept or reject, and the surface of the decision is visible on screen. The second creates files you have not opened, installs packages you did not name, writes configuration you did not know existed, and reports back that the feature is working.

Both are useful. Only the second requires a review habit, and almost nobody has one, because the output arrives already functioning — which is precisely the property that removes the prompt to look.

## What an Agent Actually Touches

Worth listing, because founders underestimate the breadth.

**Application files,** created and modified across the project rather than in the file you were looking at.

**Dependencies,** installed to make something work. A request for a chart or a date picker adds packages and, with them, everything those packages depend on.

**Configuration.** Build settings, run commands, environment definitions — the parts that determine how your project starts and what it can reach.

**Secrets and environment variables,** sometimes created with placeholder values that look real.

**Database structure,** where a project has one. Tables created, columns added, occasionally data transformed.

A code suggestion changes a function. An agent changes the shape of your project, and the review has to match that scope.

## Why This Output Needs a Different Kind of Review

Three properties make agent-generated work distinctive.

**It optimises for "working".** The success criterion is that your request now functions. Nothing in that objective concerns who else can reach the data, what happens under load, or whether a package was necessary.

**It cannot see your intent.** You asked for a feature; it inferred everything else — the data structure, the access pattern, the error handling — from what seemed reasonable. Those inferences are invisible in the result.

**It is fluent.** Generated code reads well, is consistently formatted, and runs on the first attempt, which produces a confidence signal your brain has spent years learning to trust and which no longer correlates with correctness.

## The Five Things to Read First

You do not have to review everything. Reviewing these five catches most of what matters.

**One: the dependency list.** Open it after any significant agent session and look at what is new. Ask whether each addition was necessary, whether the name is what you expected, and how many further packages arrived with it. A plausible-looking package name is exactly what typosquatting relies on, and an agent installs confidently.

**Two: anything touching data access.** Where the code reads or writes your database, and whether those operations carry any check about who is asking. This is where the most serious flaw in AI-built products lives, and an agent will not add a rule nobody requested.

**Three: credentials.** Search the project for anything resembling a key. Then check whether the agent placed a privileged credential in code that runs in a browser — the one mistake that turns a working feature into an open database.

**Four: configuration changes.** Run commands, build settings, exposed ports, environment definitions. These are rarely read and they determine how your project behaves when deployed rather than when previewed.

**Five: anything that writes files.** Where uploads or generated files are stored. On a platform where environments are rebuilt, files written beside your code are a silent data-loss mechanism.

## Reviewing Code You Cannot Fully Judge

Many founders using an agent cannot evaluate implementation quality, and that does not prevent a useful review.

**Ask the agent to explain what it changed,** in plain language, before you accept. An explanation that does not match what you asked for is a signal you can act on without reading a line.

**Ask what it decided that you did not specify.** This single question surfaces the inferences — the data structure it chose, the library it picked, the assumption it made about who can see what.

**Ask what would break this.** Agents answer this surprisingly well and it produces a list you can test manually.

**Then test adversarially yourself.** Open the feature as a different user, change an identifier in a request, submit a value the form did not intend. Four minutes, and it tests the thing the agent had no reason to consider.

## The Prompt That Produces Reviewable Output

Small changes in how you ask produce output that is easier to check.

**Ask for one thing at a time.** A session that adds a feature, refactors two files and installs three packages is unreviewable. A session that does one thing has a diff you can read.

**State the constraints you care about.** "Do not add new dependencies without telling me. Access to this table must be restricted to the owner. This runs on the server." Constraints stated up front are honoured far more reliably than corrections applied afterwards.

**Ask it to list what it changed** at the end, including packages and configuration. Then verify the list rather than trusting it.

**Keep the work in small commits,** so that when something breaks a week later, the set of changes to examine is bounded.

## What an Agent Cannot Decide For You

Four decisions remain yours regardless of how capable the tooling becomes, because they depend on knowledge the agent does not have.

**What your data means.** Which fields are sensitive, which combinations identify a person, what must never be exposed to another customer.

**Who is allowed to do what.** Your permission model encodes your business, and an agent asked to fix a permissions error will frequently remove the permission check.

**What happens when something fails.** Whether a failed payment should retry, notify, or block access is a commercial decision.

**What you are willing to depend on.** Each package, each service, each platform behaviour is a commitment you will maintain.

Delegating the writing is reasonable. Delegating these is how a product ends up with decisions nobody made.

## A Review Routine Worth Adopting

After each substantial agent session: read the change list, check new dependencies, look at anything touching data access or credentials, and test the feature as a hostile user. Ten minutes.

Weekly: read the full dependency list, remove what is unused, and confirm nothing privileged has drifted into client-side code.

Before any release: run the six checks from a production readiness list — two accounts reading each other's data, keys in the bundle, a real payment abandoned mid-flow, a file upload of the wrong type, a logged-out attempt at a protected page, and the error tracker checked afterwards.

None of this slows you down meaningfully. It converts speed into speed you can rely on.

## The Failures That Appear Weeks Later

The findings above are visible if you look on the day. A second category only emerges later, and it is worth knowing about because the review habit that catches it is slightly different.

**Version drift.** If your dependencies are not pinned to exact versions and your project has no lockfile committed, a rebuild weeks later can install newer versions of packages than the ones your project was tested against. The application worked in June and fails in August with nobody having changed anything, which is one of the most disorienting experiences in software. Committing a lockfile and rebuilding from it removes the entire class.

**Accumulated permissiveness.** Agents are asked to fix errors, and a permissions error has two solutions: grant the caller the right access, or remove the check. The second is faster, always works, and is what gets generated when the request is phrased as "this is returning an error, fix it". Across a dozen sessions a product can lose most of its access checks without any single session looking wrong.

**Duplicated logic.** Ask for the same capability in three places across three sessions and you get three implementations that behave slightly differently — three date formats, three ways of calculating a total, three definitions of an active customer. Nothing breaks; the numbers simply stop agreeing, and reconciling them later is more work than preventing them now.

**Dead code that still runs.** Features replaced rather than removed, endpoints nobody uses that still accept requests, scheduled work for a process that no longer exists. Each one is a surface somebody can reach and a thing you will have to reason about during an incident.

**Configuration that only exists in one place.** An environment variable set by hand in one deployment, a setting changed in a dashboard, a value that lives in somebody's memory. Reproducing the deployment becomes archaeology.

The habit that catches these is a monthly half-hour: read the dependency list, grep for access checks on the tables that matter, list your endpoints and delete the ones nothing calls, and confirm that a fresh rebuild from committed files produces a working application. Half an hour a month, and it prevents the afternoon where nothing has changed and nothing works.

## When the Review Finds More Than You Expected

That is the common outcome on a project that has had several agent sessions, and it is not a reason to start again.

LaunchStudio handles it as bounded work: an audit of what was generated, dependencies triaged rather than counted, access rules written and verified by attempting to bypass them, credentials consolidated and rotated, file storage moved somewhere durable, and configuration made explicit so deployment is reproducible — with the interface you built left untouched and the codebase kept conventional so you can keep working with the agent afterwards.

The engineers are Manifera's: eleven years of production systems for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City, where reviewing code somebody else wrote is most of the job.

[Send us your project](https://launchstudio.eu/en/#contact) and you will get a specific list within one business day, or see what the [Launch Ready package](https://launchstudio.eu/en/#packages) covers.

## Real example

### An Agent Session That Installed a Database Nobody Needed

Freek Wiersma built Werkbriefje on Replit: a job-sheet tool for a group of four installation companies around Zutphen. He asked the agent to add PDF export for completed job sheets, which it delivered in about twenty minutes and which worked immediately.

He shipped it without reading the change list.

Three weeks later his project would not start after a restart, and the investigation surfaced what the session had actually done. The PDF feature had installed eleven packages, one of which pulled in a headless browser runtime that made the project slow to start and occasionally exceed its memory allowance. It had also added a second storage mechanism to cache generated files — writing them beside the application, where a rebuild removed them, which is why some job sheets could no longer be downloaded. And it had created an environment variable holding a licence key for a library, in a file committed to the project.

Five business days of work: the PDF pipeline rebuilt using a lighter approach appropriate to the volume, nine packages removed, generated files moved to external object storage with per-company access, the committed key rotated and moved into proper secret storage, memory usage brought back within the allowance, and a review routine adopted — one request per session, a change list read before accepting.

**Result:** start-up time returned to normal, the missing job sheets were regenerated from source data, and Freek reports that reading the change list now takes him two minutes per session and has caught two further unnecessary packages.

> *"It built the feature in twenty minutes and I was delighted. It also installed an entire browser to make a PDF and put a licence key in my repository, and I found out three weeks later."*
> — **Freek Wiersma, Founder, Werkbriefje (Zutphen)**

**Cost & Timeline:** €2,200 (dependency cleanup, PDF pipeline rebuild, storage migration, key rotation) — completed in 5 business days.

## Frequently Asked Questions

### Is agent-generated code less safe than code I write myself?

Not inherently, and it needs a different review because the surface is wider. An agent installs packages, writes configuration and creates files across the project, so the review must cover what changed rather than only the function you were looking at.

### What should I check after every agent session?

The new dependencies, anything touching data access, anywhere a credential appears, configuration changes, and anything that writes files. Then test the feature as a hostile user by changing an identifier or submitting an unexpected value.

### How do I review code I cannot fully evaluate?

Ask the agent to explain what it changed in plain language, ask what it decided that you did not specify, and ask what would break it. Then test behaviour yourself, which requires no code reading at all.

### How can I make agent output easier to review?

Ask for one thing per session, state your constraints up front — no new dependencies without telling you, this table is owner-only, this runs on the server — and ask for a change list at the end that you then verify.

### What should never be delegated to an agent?

Which data is sensitive, who is allowed to do what, what happens when something fails, and what you are willing to depend on. Those decisions encode your business and the agent has no way to know them.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is agent-generated code less safe than code I write myself?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not inherently, but it needs a wider review because an agent installs packages, writes configuration and creates files across the project rather than editing one function."
      }
    },
    {
      "@type": "Question",
      "name": "What should I check after every agent session?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "New dependencies, anything touching data access, anywhere a credential appears, configuration changes and anything writing files — then test as a hostile user."
      }
    },
    {
      "@type": "Question",
      "name": "How do I review code I cannot fully evaluate?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ask for a plain-language explanation, ask what it decided that you did not specify, ask what would break it, then test behaviour yourself."
      }
    },
    {
      "@type": "Question",
      "name": "How can I make agent output easier to review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "One request per session, constraints stated up front, and a change list at the end that you verify rather than trust."
      }
    },
    {
      "@type": "Question",
      "name": "What should never be delegated to an agent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Which data is sensitive, who may do what, what happens on failure, and what you are willing to depend on."
      }
    }
  ]
}
</script>
