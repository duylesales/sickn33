---
Title: "AI App Security: Dependency Updates Without Breaking Production"
Keywords: ai app security, dependency updates, supply chain, lockfiles, vulnerability scanning, npm audit, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI App Security: Dependency Updates Without Breaking Production

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Security: Dependency Updates Without Breaking Production",
  "description": "An AI-built app depends on hundreds of packages nobody chose. How to know which of them are vulnerable, which updates are urgent, and how to apply them without spending every Friday on a broken build.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-18",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-app-security-dependency-updates-without-breaking-production" }
}
</script>

Count the packages your product installs. Not the ones you asked for — the total, including everything those packages depend on. For a typical Lovable or Bolt application it is somewhere between six hundred and fifteen hundred.

You chose perhaps fifteen of them. The rest arrived because something you chose needed them, and they run with the same permissions as the code you wrote.

This is not an argument for building everything yourself. It is an argument for knowing what you have, because the alternative is a product whose security depends entirely on code you have never seen and cannot name.

## The Lockfile Is the Fact

Your package file says what you want. Your lockfile says what you actually have — every package, every version, every transitive dependency, pinned exactly.

Two consequences. It must be committed, or your production build may install different versions from the ones you tested, which is both a reliability and a security problem. And it is the document that answers "are we affected by this" when a vulnerability is announced — one search through the lockfile, thirty seconds, rather than an afternoon of uncertainty.

Products built by AI tools sometimes lack a committed lockfile entirely, because the tool managed dependencies on its own and the concept never surfaced. If yours is missing, that is the first thing to fix.

## Knowing What Is Vulnerable

The baseline costs nothing. Your package manager has an audit command that compares your lockfile against a public vulnerability database and lists what matches. Run it today; the first run on a year-old AI-built project typically returns dozens of results.

Automate it after that: a check on every build, and a service that opens a pull request when a new advisory affects you. The free tiers of the common tools are more than adequate at this scale.

The output will be noisy, and learning to read it is the real skill.

## Not Every Advisory Is Your Problem

Two questions decide whether a reported vulnerability matters to you.

**Is the affected code reachable in your product?** A vulnerability in a package that only runs during the build, on your machine, is not exposed to your users. One in a package handling incoming requests is.

**Does the attack require conditions you have?** Many advisories require a specific configuration, a particular function called with untrusted input, or an environment you do not run.

This is why "critical" in an advisory is not the same as critical for you. A high-severity issue in a development-only tool can reasonably wait for the next batch; a moderate one in your request-handling path may need attention today.

The judgement is worth making deliberately rather than either updating everything reflexively or ignoring the list because it is long. Both are failures, and the second is much more common.

## An Update Routine That Survives Contact With Reality

The pattern that works for a small product has three speeds.

**Security updates, promptly.** Anything reachable from user input, applied within days and out of band if serious.

**Patch and minor updates, on a schedule.** Once a fortnight or once a month, in one batch, when you have time to test. These are mostly safe and letting them accumulate for a year is what makes upgrading painful.

**Major versions, deliberately.** One at a time, read the migration notes, allow real time. Never several at once, and never on a Friday.

The habit that makes the middle speed sustainable: update, run your checks, deploy to staging, use the product for ten minutes, deploy. If your product has no automated tests, the ten minutes of use is doing all the work and should be a written list of what to click rather than an improvisation.

## Reduce What You Depend On

The cheapest security improvement in this area is to have fewer dependencies.

AI coding tools install packages readily — a date library for one format string, a utility package for one function, a component library used for a single button. Each is a permanent liability with its own dependency tree, its own maintainer, and its own chance of being abandoned or compromised.

Once a quarter, list your direct dependencies and ask of each: what does this do, do we still use it, and could we do without it. Removing three or four is typical, and each removal takes a subtree of transitive packages with it.

Pay attention to signals of abandonment as well: no release in two years, an archived repository, a single maintainer with no activity. These are not urgent, but they are the packages where a future vulnerability will have no fix.

## The Supply Chain Attack Is Real Now

The attack that has become common is not a vulnerability discovered in good code. It is malicious code published deliberately — a popular package's maintainer account compromised, or a new version containing something that reads your environment variables and posts them elsewhere.

Three practices reduce the exposure meaningfully. Pin exact versions in the lockfile, which you already do. Delay adopting brand-new releases of packages that touch anything sensitive, since most malicious releases are caught within days. And check what runs during installation: scripts that execute automatically on install are the usual delivery mechanism, and most package managers can disable them.

For a small product this is proportionate. Nobody expects you to review a thousand packages. Knowing which fifteen you chose, and not installing a sixteenth without a reason, is most of the benefit.

## The Packages AI Tools Invent

One failure mode belongs specifically to products built with coding assistants, and it is worth checking for directly: a dependency that does not exist, or did not until somebody noticed the mistake.

Models occasionally suggest a plausible-sounding package name that was never published. Usually the install fails and the error is obvious. The dangerous version is when someone registers that name afterwards precisely because assistants keep suggesting it — a technique with a name in security circles and a growing number of real cases. The package installs cleanly, does something useful enough not to raise questions, and runs with your application's permissions.

The check is quick. Go through your direct dependencies and, for each one you do not recognise, look at its repository: how long it has existed, how many people use it, who maintains it, and whether it is what the name implies. A package with forty weekly downloads and one commit, sitting in a production application, deserves an explanation.

The same look catches a related problem — a dependency that is real but wrong. Assistants sometimes reach for a package that solves a different problem, or a deprecated predecessor of the one intended, because both were common in training data. These do not install malware; they simply add weight and eventual friction.

Neither check takes long, and both are best done once now and then whenever an assistant adds something you did not ask for by name.

## What to Do When a Package Is Abandoned

Eventually one of your dependencies stops being maintained. The repository goes quiet, an issue about a vulnerability sits unanswered, and there is no fix coming.

Four options, in roughly the order to consider them.

**Replace it.** Usually the right answer if an actively maintained alternative exists and the change is contained. The cost is a day; the benefit is that the problem is gone permanently.

**Remove it.** Check first whether you use enough of it to justify a dependency at all. A package providing one function you could write in twenty lines is a package to delete, and this is more often the case than it feels like.

**Fork and patch it.** Reasonable when the package is small and the fix is understood. You now maintain it, which is a real commitment, but for a hundred lines of code it is a smaller commitment than it sounds.

**Pin and isolate it.** When replacing is genuinely expensive, keep the version fixed, document why, and reduce what it touches — ensuring it never handles untrusted input directly if that is what the vulnerability requires.

What is not an option is leaving it unexamined with a note that says an update is available. Write down the decision and the reason, so that the next person to look — including you, in a year — does not repeat the investigation from the beginning.

## Setting This Up

For an existing product this is typically half a day: a committed lockfile, an audit run with the results triaged by reachability rather than by severity label, automated scanning on every build with alerts routed somewhere you read, a written update routine at three speeds, a short manual test list for products without automated tests, unused and abandoned direct dependencies removed, install scripts reviewed, and a note recording what each direct dependency is for so the next review is faster than this one.

LaunchStudio covers dependencies in security review and keeps them current under the managed arrangement at €49 per month, where updates are applied and tested rather than accumulating. The engineers are Manifera's — eleven years, 120+ engineers, clients including Vodafone, TNO and CFLW.

[Ask us what your lockfile contains](https://launchstudio.eu/en/#contact). Most founders have never looked.

## Real example

### Fourteen Months Without an Update

Menno Zwartjes built Werkbonnen in Lovable: digital work orders and signatures for installation and maintenance companies, 47 firms with around 400 field engineers.

He had never updated a dependency. The application worked, nothing appeared broken, and the subject had not come up. Fourteen months after launch, an audit run returned 63 advisories, 11 of them in packages handling incoming requests.

One mattered immediately: a request-parsing library with a known flaw allowing a crafted payload to consume unbounded memory. His product accepted work order submissions from engineers' phones on public endpoints, which is exactly the exposure the advisory described. It had been published nine months earlier.

Three business days: the lockfile committed, having never been in the repository, so builds had been resolving versions freshly each time; the 63 advisories triaged, of which 11 were reachable from user input, 34 were development-only and the remainder required configurations he did not run; the 11 applied immediately, including the parsing library, with the product exercised against a written test list; the development-only set applied in one batch the following week; two major version upgrades scheduled separately and done one at a time over two weeks; automated scanning wired into the build with alerts to his phone and a service opening pull requests for new advisories; 9 direct dependencies removed as unused, including a date library used for one format string and a component library used for one button, which removed 190 transitive packages; install scripts disabled by default; and an update routine written down — security within days, minor monthly, major deliberately.

**Result:** the memory exhaustion issue was closed after nine months of exposure with no evidence it had been exploited. Total package count fell from 1,340 to 1,150. Menno now spends about 40 minutes a month on updates, and reports that the routine's main benefit is that nothing accumulates into the kind of upgrade that takes a week.

> *"Nobody told me dependencies were a thing I owned. They arrived with the code, they worked, and for fourteen months I did not know there was a list to look at."*
> — **Menno Zwartjes, Founder, Werkbonnen (Hengelo)**

**Cost & Timeline:** €2,600 (lockfile remediation, advisory triage and application, major version upgrades, automated scanning and alerting, dependency reduction, install script hardening, update routine documentation) — completed in 3 business days.

## Frequently Asked Questions

### Do I need to fix every vulnerability my audit reports?

No. Triage by reachability: a flaw in a build-time tool is not exposed to users, while one in request handling may be urgent. Severity labels describe the flaw, not your exposure.

### How often should I update dependencies?

Security fixes within days, patch and minor updates in a monthly batch, major versions one at a time with real time allowed. Letting everything accumulate is what makes upgrading painful.

### Why does the lockfile matter?

It records exactly what you have, so your production build matches what you tested and you can answer "are we affected" in thirty seconds when an advisory appears.

### How do I reduce supply chain risk?

Have fewer dependencies, pin exact versions, delay adopting brand-new releases of sensitive packages, and disable install scripts. Reviewing a thousand packages is not expected; not adding the thousand-and-first without a reason is.

### What if my app has no tests?

Write a short list of what to click after an update — the five or six paths that matter. It is not a test suite, but it is repeatable, and improvisation is not.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Must I fix every reported vulnerability?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Triage by whether the affected code is reachable from user input. Build-time-only flaws are not exposed to your users."
      }
    },
    {
      "@type": "Question",
      "name": "How often should dependencies be updated?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Security fixes within days, minor and patch updates monthly in a batch, major versions individually with time allowed."
      }
    },
    {
      "@type": "Question",
      "name": "Why does a committed lockfile matter?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It guarantees production matches what you tested and lets you answer whether an advisory affects you in seconds."
      }
    },
    {
      "@type": "Question",
      "name": "How do I reduce supply chain risk in a small product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Fewer dependencies, exact pinned versions, a delay before adopting brand-new releases, and install scripts disabled."
      }
    },
    {
      "@type": "Question",
      "name": "How do I update safely without automated tests?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Keep a written list of the five or six paths to exercise after each update. Repeatable beats improvised."
      }
    }
  ]
}
</script>
