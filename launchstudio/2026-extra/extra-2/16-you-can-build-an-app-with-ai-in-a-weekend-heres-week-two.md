---
Title: "You Can Build an App With AI in a Weekend. Here's Week Two"
Keywords: build an app with ai, build app with ai, ai coding, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# You Can Build an App With AI in a Weekend. Here's Week Two

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "You Can Build an App With AI in a Weekend. Here's Week Two",
  "description": "A production-readiness checklist for the specific week after the weekend build, centered on a real example of a service account key that sat exposed in a public repository.",
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
  "datePublished": "2026-07-24",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/you-can-build-an-app-with-ai-in-a-weekend-heres-week-two"
  }
}
</script>

Week one is the fun part: you build an app with AI, watch it come together faster than you thought possible, and by Sunday night you have something real to show people. Week two is quieter and less visible, and it's where most of the actual risk in a weekend build tends to live — starting with a simple question almost nobody asks during the excitement of week one: where exactly did your API keys end up?

## Checklist Item One: Search Your Repository for Exposed Keys

A weekend of fast iteration often means copying working code between files, committing frequently without much scrutiny, and occasionally pasting a key directly into a config file to get something working quickly, with every intention of moving it somewhere safer "later." Checking whether that "later" ever actually happened — searching your own repository history for anything resembling an API key or credential — is a five-minute check with outsized value.

## Checklist Item Two: Confirm Your Repository's Visibility Setting

A surprising number of founder-built projects sit in a public GitHub repository by default, either because the founder didn't think to change it or didn't realize the setting existed. A public repository means anything committed to it — including a key missed during the search above — is visible to literally anyone, indexed by automated scanners that specifically search public repositories for exactly this pattern.

## Checklist Item Three: Rotate Anything That Was Ever Exposed, Even Briefly

If a key was ever committed to a public repository, even if it was later removed, the safest assumption is that it was already seen — git history preserves old commits, and automated scanners work fast enough that "it was only public for an hour" isn't a meaningful safety margin. Rotating (generating a new key and revoking the old one) is the only way to be certain an old exposure isn't still usable.

## Checklist Item Four: Move Remaining Secrets Into Proper Environment Configuration

Beyond the immediate cleanup, secrets belong in environment variables or a dedicated secrets manager, never directly in committed code — this is a permanent habit change, not a one-time fix, since the same convenient shortcut that caused the first exposure is just as available during every future feature added afterward.

## Checklist Item Five: Get a Second Set of Eyes Before Real Users Arrive

None of the above is exotic or hard to understand once pointed out, which is exactly the problem — a founder deep in their own weekend build has no natural prompt to stop and specifically check for it, which is precisely the gap a second, independent review closes. [LaunchStudio](https://launchstudio.eu/en/) runs exactly this kind of secrets and repository audit as a standard first step in its Launch Ready package, backed by Manifera's 11+ years of production engineering experience.

Manifera's secrets and configuration audits are performed by the engineering team based at the Ho Chi Minh City development center on Pho Quang Street, with client conversations handled through the Amsterdam headquarters at Herengracht 420.

[Let's get moving — prototype to production in weeks, not months](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: The Key Sitting in Plain Sight for a Month

Noa, a former wedding coordinator turned founder in Middelburg, built TrouwPlan, an AI-assisted wedding planning tool built with Bolt over a single weekend, publishing the project to a public GitHub repository without giving the visibility setting much thought.

A month later, preparing for a small local launch, Noa mentioned the project to a developer friend, who did a quick scan out of habit and found a cloud storage service account key sitting in an early commit, fully exposed the entire time. LaunchStudio's review confirmed the key had broad storage access and had never been rotated since the initial commit.

**Result:** LaunchStudio rotated the exposed key immediately, migrated all remaining secrets to proper environment configuration, and set the repository to private, closing the exposure with no changes to TrouwPlan's actual features.

> *"A month of that key just sitting there in a public repo, and I found out purely because a friend happened to look. That's not a system I want to rely on going forward."*
> — **Noa Bergsma, Founder, TrouwPlan (Middelburg)**

**Cost & Timeline:** €1,200 (secrets audit, key rotation, and repository hardening) — completed in 4 business days.

---

## Frequently Asked Questions

### Would a security researcher consider a month of public exposure a serious window, or a minor one?

Serious — automated scanners that specifically search public repositories for exposed credentials typically operate on a timescale of minutes to hours, not weeks, so a month of exposure should be treated as though the key was definitely found, not merely possibly found.

### Is this specifically a GitHub problem, or does it apply to other code-hosting platforms too?

It applies universally to any code-hosting platform with a public visibility option — GitLab, Bitbucket, and others all face the identical underlying risk, since the vulnerability is about what's committed and visible, not which specific platform hosts it.

### Manifera works with clients with far more sensitive data exposure risk than a wedding-planning app — does that experience change how a case like Noa's gets handled?

The specific handling doesn't change, only the stakes framing does — the same rotate-and-migrate process applies whether the exposed key belongs to a wedding-planning tool or an enterprise client's production system, since the technical remediation itself isn't scaled by company size.

### Herre Roelevink has spoken about founders needing security expertise they didn't previously have access to — does a case like this fit that description?

Precisely — a public repository visibility setting is the kind of default a founder without a security background has no particular reason to question, and that exact gap between what founders instinctively check and what a trained eye instinctively checks is the space Roelevink has described LaunchStudio as filling.

### If a founder catches this themselves before launch, is a professional audit still worth the cost?

If a founder can confidently confirm every key was found, rotated, and never appeared anywhere else in git history, a full audit may add limited additional value — though confirming that confidently, across an entire repository history, is exactly the kind of systematic check that's easy to do partially and believe was done completely.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is a month of public key exposure a serious risk window?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, automated scanners typically operate on a timescale of minutes to hours, so a month should be treated as definitely found."
      }
    },
    {
      "@type": "Question",
      "name": "Is exposed-key risk specific to GitHub?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, it applies universally to any code-hosting platform with a public visibility option."
      }
    },
    {
      "@type": "Question",
      "name": "Does handling change for higher-stakes clients versus a small founder app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, the same rotate-and-migrate process applies regardless of company size or stakes."
      }
    },
    {
      "@type": "Question",
      "name": "Does a public repo default fit the gap the CEO has described founders facing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, it's a default founders have no particular reason to question without a security background."
      }
    },
    {
      "@type": "Question",
      "name": "Is a professional audit still worth it if a founder catches this themselves?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Possibly limited value if confirmed thoroughly, but confirming that completely across history is easy to do only partially."
      }
    }
  ]
}
</script>
