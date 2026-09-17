---
Title: "Lovable Security: The Dependencies You Did Not Choose"
Keywords: lovable security, ai app security, dependency vulnerabilities, lockfile reproducible build, supply chain small saas, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Security: The Dependencies You Did Not Choose

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Security: The Dependencies You Did Not Choose",
  "description": "AI builders install packages on your behalf, and a small app routinely depends on hundreds. Which risks are real for a product your size, what a lockfile actually protects, and the update routine that is worth the hour.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-26",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-security-dependencies-you-did-not-choose" }
}
</script>

Open the package list of a Lovable or Bolt project and count. A modest application — a few screens, a form, a chart — routinely depends on several hundred packages, almost none of which you selected, most of which you have never heard of, and all of which run with the same privileges as the code you wrote.

That is not a scandal. It is how modern web development works, and the same is true of applications built entirely by hand. What is different in AI-built projects is that nobody paused at any point to consider whether a package was necessary, maintained, or the one it appeared to be — because the tool added it silently while solving the problem you described.

## What Gets Installed on Your Behalf

Ask a builder for a date picker and it installs a date library. Ask for a chart and it installs a charting package, which installs a rendering utility, which installs three helpers. Ask for animation, icons, form validation, file handling — each request adds a package you chose and several you did not.

The ones you did not choose are called transitive dependencies, and in a typical project they outnumber your direct choices by roughly ten to one. They are also where nearly all the risk sits, because you have no relationship with them at all: you have never read their name, never checked whether they are maintained, and would not notice if one changed hands.

## Why This Is a Security Question and Not Only Housekeeping

Every package in your dependency tree executes with your application's privileges. A compromised package in your frontend can read what your users type. One in your server code can read your environment variables, which is where your database credentials live.

The realistic threats for a small product, in order of likelihood:

**Known vulnerabilities in old versions.** The overwhelming majority of real incidents. A package has a documented flaw, a fix exists, and the project never updated because nobody was watching.

**Abandoned packages.** Maintained by one person who stopped three years ago. No fix will arrive when a flaw is found, and it is not a compromise so much as a slow accumulation of risk.

**Typosquatting.** A package with a name one character from a popular one, published to catch mistakes. This is where an AI tool's confident installation deserves a second look, because a plausible-looking name is exactly what these rely on.

**Compromised maintainer accounts.** Rare, well-publicised, and the reason the industry pays attention to this subject at all. A legitimate package publishes a malicious version, and everyone who updates without pinning gets it.

Note what is not on this list: someone specifically targeting your product through a package. For a small Dutch SaaS, the realistic exposure is being caught in something indiscriminate rather than being singled out.

## What a Product Your Size Should Actually Do

Proportionality matters here. A founder with two hundred users does not need a supply-chain security programme, and the small set of measures below covers the realistic threats.

**Keep a lockfile, committed.** This is the single most important item and it is frequently missing from AI-built projects.

**Run an audit command occasionally** and read what it says rather than what it counts.

**Update deliberately, on a schedule,** rather than never or constantly.

**Know what your direct dependencies are** and remove the ones you no longer use.

**Look at anything new that was installed for you,** particularly by an agent that can add packages without asking.

That is the entire programme. An hour a month, and it puts you ahead of most products of your size.

## Lockfiles and Why They Matter More Than the Audit

A lockfile records the exact version of every package, direct and transitive, that your project uses. Without one, a build tomorrow may install different versions than a build today, which means your production environment can differ from what you tested for reasons nobody introduced deliberately.

Two consequences for security. A lockfile means a compromised new release does not reach you automatically — you upgrade when you choose. And it means that when something does break, the set of things that changed is knowable rather than mysterious.

If your project has no lockfile committed, that is the first fix, and it takes a minute.

## Automated Updates: Useful and Noisy

Tools that open a pull request when a dependency has a new version are genuinely helpful and, on default settings, overwhelming for a solo founder — a project with hundreds of packages produces updates faster than one person can review them, and the outcome is that all of them get ignored, including the one that mattered.

The configuration that works for a small product: security updates raised immediately and separately, everything else batched monthly, and patch-level updates grouped rather than individual. The goal is a small number of notifications you actually read.

## Deciding Whether to Add a Package at All

The best dependency management is not adding things. Three questions before accepting a new package, whether suggested by a tool or by yourself.

**Do I need the whole library for this?** A date library added to format one timestamp is a large surface for a small task, and modern language features often cover it.

**Is it maintained?** Recent releases, open issues being answered, more than one contributor.

**How many things come with it?** A package that installs forty others is forty more things you now depend on.

When an AI tool proposes a dependency, this is exactly the moment to intervene — it optimises for solving your immediate request, not for the size of the tree it leaves behind.

## The Audit You Can Run Today

Open your project and run your package manager's audit command. Then do the part most people skip: read the output rather than counting it.

For each reported issue, ask two questions. **Does this affect code that runs in production**, or a build tool that never reaches your users? And **is the vulnerable path one my application actually uses**? A flaw in a function nobody calls is different from one in your authentication path.

This distinction matters because an unfiltered audit report on a typical project produces an alarming number and paralysis. Triaged properly, most projects have a handful of items that deserve action and a long tail that does not.

Then check your direct dependency list by hand and remove anything you no longer use — projects accumulate packages from features that were deleted, and the dependency survived.

## When an Alert Actually Matters

Treat as urgent: anything in code that runs on your server, anything in your authentication or payment path, anything described as allowing code execution, and anything in a package handling user input.

Treat as scheduled: build tooling, development-only dependencies, and flaws in code paths your application does not exercise.

Treat as noise: advisories about packages you removed, duplicates, and anything a triage confirms cannot be reached in your usage.

Writing that triage down, once, turns future audits from an anxiety into a ten-minute task.

## Getting the Baseline Right

For most AI-built products this is a short piece of work that then stays manageable: lockfile committed and builds made reproducible, dependencies audited and triaged rather than counted, unused packages removed, automated updates configured to produce a signal instead of noise, and a written triage rule so the next alert is a decision rather than a scare.

It sits alongside the access control, secrets and deployment work in the [Launch Ready package](https://launchstudio.eu/en/#packages), done without touching the interface you built in Lovable. The engineers are Manifera's: eleven years of maintaining production systems for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City, where dependency hygiene is routine rather than an event.

If your audit command returns a number you have been avoiding, [describe your project](https://launchstudio.eu/en/#contact) and we will tell you which items actually matter, usually within one business day.

## Frontend Packages and Server Packages Are Different Risks

A distinction that makes triage far faster once you hold it, and that most audit output does not make for you.

**A package running in the browser** executes on your user's device with access to what they see and type on your page. A compromise there can read form inputs, session tokens held in the page, and anything displayed. It cannot reach your database credentials, because those are not there.

**A package running on your server or in a function** executes with your application's privileges. A compromise there can read environment variables — your database credentials, your payment secret, your model API key — and act as your application against your own data.

**Build-time packages** run on the machine that builds your project and never reach users at all. A vulnerability in one is a real concern for a large organisation with a shared build system and a minor one for a solo founder building from a laptop.

The practical consequence: when an audit reports fifty issues, sort them by which of those three categories they fall into before doing anything else. Server-side dependencies come first, browser-side second, build tooling last. That single sort usually reduces an alarming list to a handful of items that deserve an afternoon.

## Real example

### Two Hundred Alerts, Four That Mattered

Denise Kuiper ran Boekhoudmaat in Lovable: a lightweight bookkeeping helper used by around 150 freelancers across Utrecht and Amersfoort. A prospective customer's accountant asked whether she kept her dependencies up to date, and she ran an audit for the first time in fourteen months.

It reported over two hundred issues. She spent an evening reading about supply-chain attacks and concluded her product was indefensible.

The triage took three hours. Roughly three-quarters of the reports concerned build tooling that never reaches a user's browser or her server. Another portion were in code paths her application did not exercise. What remained were four items that genuinely mattered: an outdated authentication helper with a documented flaw, two packages in her file-upload path, and one abandoned library handling input parsing that had not been updated in four years.

Four business days of work: a lockfile committed, since the project had none and builds were not reproducible; the four material issues resolved, with the abandoned library replaced by a maintained equivalent; thirty-one unused packages removed, which had accumulated from deleted features; automated updates configured to raise security issues immediately and batch everything else monthly; and a one-page triage rule written so future audits could be assessed in ten minutes.

**Result:** the accountant's question was answered with a documented process, and the monthly update review has since taken Denise under fifteen minutes, with two security items acted on in nine months.

> *"Two hundred alerts made me feel like my product was made of wet paper. Four of them were real, and I could not tell which four without someone showing me how to look."*
> — **Denise Kuiper, Founder, Boekhoudmaat (Utrecht)**

**Cost & Timeline:** €1,450 (lockfile and reproducible builds, triage, four remediations, update configuration, triage documentation) — completed in 4 business days.

## Frequently Asked Questions

### How many dependencies does a typical AI-built app have?

Often several hundred once transitive dependencies are counted, with roughly ten indirect packages for every one you chose. That is normal for modern web development; what differs is that nobody reviewed whether each was necessary.

### What is a lockfile and why does it matter?

It records the exact version of every package your project uses, so builds are reproducible and a newly published version cannot reach you automatically. If your project has no committed lockfile, that is the first thing to fix.

### My audit reports hundreds of vulnerabilities. Is my app unsafe?

Usually not to that degree. Most reports concern build tooling that never runs in production or code paths your app does not exercise. Triage by asking whether the code runs in production and whether your application actually reaches it.

### Should I enable automated dependency updates?

Yes, configured carefully. On default settings a small project produces more updates than one person can review, so everything gets ignored. Raise security issues immediately and separately, and batch the rest monthly.

### How do I stop my AI tool adding unnecessary packages?

Intervene when one is proposed: ask whether the whole library is needed for the task, whether it is actively maintained, and how many further packages it brings. The tool optimises for solving your request, not for the size of the tree.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How many dependencies does a typical AI-built app have?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Often several hundred once transitive dependencies are counted, roughly ten indirect for every direct choice — normal for modern web development, but unreviewed in AI-built projects."
      }
    },
    {
      "@type": "Question",
      "name": "What is a lockfile and why does it matter?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It records exact versions so builds are reproducible and newly published versions cannot reach you automatically. A missing committed lockfile is the first thing to fix."
      }
    },
    {
      "@type": "Question",
      "name": "My audit reports hundreds of vulnerabilities. Is my app unsafe?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually not to that degree — most concern build tooling or unreachable code paths. Triage by asking whether the code runs in production and whether your app exercises it."
      }
    },
    {
      "@type": "Question",
      "name": "Should I enable automated dependency updates?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, but configured so security issues are raised immediately and separately while everything else is batched monthly, otherwise the volume means all of it gets ignored."
      }
    },
    {
      "@type": "Question",
      "name": "How do I stop my AI tool adding unnecessary packages?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Intervene when one is proposed: is the whole library needed, is it maintained, and how many further packages does it bring?"
      }
    }
  ]
}
</script>
