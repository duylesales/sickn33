---
Title: "Keeping Dependencies Updated Without Breaking Everything"
Keywords: dependency updates saas, npm vulnerability alerts, lockfile importance, breaking change major version, abandoned package risk, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Keeping Dependencies Updated Without Breaking Everything

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Keeping Dependencies Updated Without Breaking Everything",
  "description": "Your product is mostly other people's code, and that code keeps changing. How to stay current without a weekly upgrade project: which updates matter, why a lockfile is not optional, and what to do about the package nobody maintains any more.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-05-03",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/keeping-dependencies-updated-without-breaking-everything" }
}
</script>

A typical web product contains a few dozen libraries you chose and several hundred that arrived as dependencies of those. All of them are maintained by other people on their own schedule, and all of them keep changing. This is not a problem to be solved so much as a maintenance obligation to be managed, and it becomes visible in exactly two ways: a security advisory you are told to act on, or a product that has drifted so far behind that upgrading anything requires upgrading everything.

Founders whose products were built by AI tools tend to inherit an unusually large dependency list, because a code generator reaches for a library rather than writing twenty lines. It is worth knowing what you have taken on.

## Lock Your Versions, Then Update Deliberately

The first requirement is a lockfile — the file recording the exact version of every package installed, including the ones you did not choose. It is generated automatically and its only job is to guarantee that the code running in production is the code you tested.

Without it committed to your repository, two deployments a week apart install different versions, and a failure appears with no corresponding change from you. This is one of the most confusing categories of bug available, and it is entirely preventable by committing a file that already exists.

With a lockfile in place, updates become something you choose to do rather than something that happens to you. Which then raises the question of when.

## Which Updates Actually Matter

Not all updates are equal, and treating them equally is why the task feels endless.

**Security advisories affecting code you actually run** are the priority, and the qualifier matters. Many advisories concern packages used only in development, or affect a function your product never calls. Assess before reacting: a critical vulnerability in a build tool is not the same as one in your web framework's request handling.

**Patch and minor updates** to libraries you depend on directly are usually safe, valuable, and worth taking on a routine schedule. They contain bug fixes, and staying close to current is what keeps the eventual major upgrade manageable.

**Major versions** contain deliberate breaking changes and deserve to be handled individually, with the release notes read and time set aside. One major upgrade at a time.

**Everything else** — indirect dependencies, packages you use for one function, tooling — can be updated on a periodic sweep rather than reactively.

The failure mode to avoid is the opposite of neglect: reacting to every automated alert immediately, which consumes real time and occasionally introduces breakage in pursuit of a vulnerability that does not apply to you.

## A Routine That Fits a Small Product

Monthly is a reasonable cadence for most small products, and it is short enough to keep each batch small.

Once a month: review outstanding advisories and assess which affect running code; apply patch and minor updates in one batch; run your tests; deploy; watch for a day. Handle major versions separately, one at a time, when there is a reason — a feature you need, security support ending, or the version you are on falling out of maintenance.

Automated dependency tools that open update proposals are helpful, provided they are configured to group minor updates rather than producing a stream of individual ones. Configured badly they become noise, and noise gets ignored, which returns you to neglect by a different route.

Two things make the routine survivable. **Tests**, because without them "did this update break anything" can only be answered by clicking through the product, which is why untested products stop updating. And **a rollback you have used**, since the point of a fast rollback is to make routine changes low-stakes.

## Runtimes and Platforms Have Deadlines

Beyond libraries, the platform itself moves, and these updates have dates attached rather than being optional.

Language runtimes reach end of life on published schedules, after which they stop receiving security fixes. Hosting platforms eventually stop supporting old versions and will, with notice, migrate or disable applications that have not moved. Managed databases have upgrade windows. Certificates expire, and increasingly so do API versions at providers such as payment processors.

These are the updates most likely to cause an unplanned emergency, because they are announced by email months ahead and then forgotten. Keeping a short list of everything with a date — runtime end of life, database version support, provider API deprecations, certificate and domain renewals — and reviewing it quarterly converts each from a surprise into a scheduled task.

Establishing a dependency and platform maintenance routine, with the tests that make it safe, is ordinary production work and one of the things most often missing from AI-generated products, which typically arrive with a large dependency list and no test suite. LaunchStudio, backed by Manifera's 11+ years of production engineering, puts both in place. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## The Package Nobody Maintains Any More

Every product eventually depends on something abandoned: last release three years ago, open issues unanswered, and now an advisory against it with no fix coming.

Assess honestly. If it is small and does one thing, the best answer is often to replace it with your own code — many such packages are fifty lines. If a maintained alternative exists, migrate. If it is deeply embedded and the vulnerability does not affect how you use it, documenting that assessment and moving on is legitimate, provided the decision is recorded rather than forgotten.

The prevention is worth more than the cure: when adding a dependency, spend two minutes checking when it was last updated, how many people rely on it, and whether it is maintained by more than one person. AI-generated code frequently reaches for obscure packages that happened to be in its training data, and reviewing what has been added — rather than accepting the list — is a cheap habit.

There is also a supply-chain dimension worth a sentence. Compromised packages are a real attack vector, and the practical defences are unremarkable: pin exact versions through your lockfile, avoid installing packages you have not looked at, and be sceptical of a dependency that appeared without your choosing it.

## Real example

### Two Years Behind, and a Weekend to Catch Up

Sam Verhagen ran Zaalplanner, a room-booking tool for community centres, built in Lovable and launched two years earlier. Dependencies had never been updated; the lockfile had not been committed.

The prompt was a platform notice: the runtime version his product ran on would stop being supported in six weeks, after which the application would not be redeployable. Moving forward one runtime version required updating the web framework, which required updating six other libraries, three of which had breaking changes across two major versions each.

Two further problems emerged. Because the lockfile was not committed, the versions running in production were not knowable with certainty, and a rebuild produced a subtly different set. And one library — a date-handling utility with 40 usages throughout the code — had been abandoned 18 months earlier, with an unpatched advisory and no maintained successor with a compatible interface.

There were no tests, so verifying that anything still worked meant clicking through every flow by hand, repeatedly.

**Result:** the lockfile committed, the runtime and framework brought current through a sequence of individual major upgrades, the abandoned date library replaced with the platform's own capabilities, a test suite covering the eight critical flows added, and a monthly update routine established with grouped automated proposals. Nine business days in total, most of it spent on work that a monthly hour would have avoided.

> "Two years of not updating anything cost me nine days and a deadline I did not choose. The individual updates would have taken about an hour a month."
> — **Sam Verhagen, Founder, Zaalplanner**

**Cost & Timeline:** dependency modernisation, test suite, and maintenance routine delivered in 9 business days.

## Frequently Asked Questions

### Do I need to act on every security advisory?

No. Assess whether the vulnerable code path is one your product actually uses, and whether the package runs in production or only during development. Prioritise advisories affecting running code, and record the reasoning for those you do not act on.

### Why does a lockfile matter?

It guarantees that the versions running in production are the versions you tested. Without it committed, two deployments can install different code, producing failures with no corresponding change from you.

### How often should dependencies be updated?

Monthly works for most small products: assess advisories, apply patch and minor updates as one batch, run tests, deploy, and observe. Major versions are handled individually when there is a reason.

### What should I do about an abandoned package?

Replace it with your own code if it is small, migrate to a maintained alternative if one exists, or document an assessment that the vulnerability does not affect your usage. The decision should be recorded rather than forgotten.

### Which updates cause emergencies?

Runtime end of life, hosting platform support windows, database version deadlines, provider API deprecations, and certificate expiry. All are announced in advance, which is why a quarterly review of everything with a date prevents them.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Do I need to act on every security advisory?", "acceptedAnswer": { "@type": "Answer", "text": "No. Assess whether the vulnerable path is one your product uses and whether the package runs in production or only in development, and record the reasoning for those you skip." } },
    { "@type": "Question", "name": "Why does a lockfile matter?", "acceptedAnswer": { "@type": "Answer", "text": "It guarantees production runs the versions you tested. Without it committed, two deployments can install different code, producing failures with no change from you." } },
    { "@type": "Question", "name": "How often should dependencies be updated?", "acceptedAnswer": { "@type": "Answer", "text": "Monthly suits most small products: assess advisories, batch patch and minor updates, run tests, deploy, observe. Major versions are handled individually." } },
    { "@type": "Question", "name": "What should I do about an abandoned package?", "acceptedAnswer": { "@type": "Answer", "text": "Replace it if small, migrate to a maintained alternative, or document that the vulnerability does not affect your usage. Record the decision rather than forgetting it." } },
    { "@type": "Question", "name": "Which updates cause emergencies?", "acceptedAnswer": { "@type": "Answer", "text": "Runtime end of life, platform support windows, database deadlines, provider API deprecations, and certificate expiry, all announced ahead, which a quarterly date review prevents." } }
  ]
}
</script>
