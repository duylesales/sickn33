---
Title: "Server-Side Rendering, API Routes, and Where Secrets Actually Belong in Next.js Apps"
Keywords: from vibe coding to production, ai frontend, ai secure, ai deployment, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Server-Side Rendering, API Routes, and Where Secrets Actually Belong in Next.js Apps

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Server-Side Rendering, API Routes, and Where Secrets Actually Belong in Next.js Apps",
  "description": "Next.js's blended frontend-backend model, common in AI-generated apps, introduces a specific, easy-to-miss distinction between server-side and client-side code — and getting it wrong is a particularly common way secrets end up exposed.",
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
  "datePublished": "2026-12-31",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/server-side-rendering-api-routes-secrets-belong-nextjs"
  }
}
</script>

Next.js, a common output framework for AI-generated web apps, blends frontend and backend code within a single project structure in a way that's genuinely convenient for development speed and genuinely easy to get subtly wrong regarding a specific, consequential question: which parts of your code actually run on the server, and which parts ship, in full, to every visitor's browser.

## Why This Distinction Is Specifically Easy to Miss in Next.js

Unlike a traditional architecture with an obviously separate frontend and backend codebase, Next.js lets you write server-side logic (API routes, server components) and client-side logic (client components) within a structurally similar-looking project, sometimes in adjacent files. This convenience is exactly what makes the distinction easy to blur — a developer, or an AI tool generating code, can reference an environment variable in what looks like a reasonable place without it being obvious, at a glance, whether that specific location executes on the server (safe) or gets bundled into client-side JavaScript (exposed to anyone who views your site's source).

## The Specific Mechanism: `NEXT_PUBLIC_` and What It Actually Means

Next.js specifically requires environment variables intended for client-side use to be prefixed with `NEXT_PUBLIC_`, a deliberate, explicit signal that a given value will be bundled into client-facing code and is therefore visible to anyone who inspects your site. The risk arises when a genuinely sensitive value — an API secret key, not a public-facing configuration value — gets this prefix, either through a copy-paste pattern from a tutorial, or through an AI tool applying the prefix without distinguishing which specific values are actually meant to be public.

## Where This Specifically Goes Wrong

**A secret key referenced in a client component.** Any environment variable read from within code that Next.js identifies as client-side, regardless of whether it has the `NEXT_PUBLIC_` prefix, will fail at build time if unprefixed — which paradoxically sometimes leads a developer or AI tool to simply add the prefix to make the error go away, without recognizing that "making the build succeed" and "keeping this secret" are now in direct conflict.

**An API call that should happen server-side, made client-side instead.** If a call to a third-party service requiring a secret API key is written in client-side code rather than routed through a Next.js API route (which runs server-side), the only way to make it function is exposing the key to the client — a structural problem best solved by moving the call to an API route, not by exposing the credential to work around it.

**Server components correctly used, but a specific sub-component incorrectly marked as client-side.** Next.js's newer app router model defaults to server components, but any component using client-side interactivity needs an explicit client marker — and a broader marking than necessary can inadvertently pull server-only logic, including secret references, into the client bundle.

## How to Verify Your Own Next.js App Isn't Exposing Secrets This Way

The direct check: search your codebase for every environment variable reference, and for each one, confirm it's either genuinely meant to be public (and correctly prefixed) or is only ever referenced within server-side code (API routes, server components, or server-only utility functions) — never within a client component or any code that ends up in the client-side bundle. Building your app and inspecting the actual client-side JavaScript bundle for any sensitive-looking values is a further, concrete verification step beyond just reading the source.

## Why This Deserves Specific Attention Beyond the General Secrets Guidance

The git history and hardcoded-credential risks covered elsewhere in this series concern secrets embedded directly in source code. This is a structurally different, Next.js-specific risk: a secret correctly stored in environment configuration, never hardcoded, that still ends up exposed because of where in your code structure it's referenced — a subtler, framework-specific version of the same underlying exposure concern.

[LaunchStudio](https://launchstudio.eu/en/) specifically reviews Next.js applications for exactly this server-client boundary issue, checking both source code references and the actual compiled client bundle, backed by Manifera's engineering experience across production Next.js applications.

[Get your Next.js app checked for secrets crossing the server-client boundary](https://launchstudio.eu/en/#calculator) — a framework-specific gap that general secrets scanning alone can miss.

## Real example

### An AI-Native Founder in Action: A Build Error "Fix" That Exposed an API Key

Jelle, a former data analyst turned founder in Dordrecht, built AnalyseHub, an AI-generated Next.js tool providing small businesses with automated data visualization from uploaded spreadsheet exports, using Cursor, and had encountered a build error early in development when a data-processing API's secret key, referenced in what turned out to be client-side code, failed Next.js's build process.

Following a suggestion from an AI coding assistant aimed at resolving the immediate build error, Jelle added the `NEXT_PUBLIC_` prefix to the environment variable — which successfully resolved the build error by making the value available client-side, without either Jelle or the immediate fix recognizing that this specific "solution" meant the secret API key was now bundled directly into AnalyseHub's public-facing JavaScript, visible to anyone who inspected the site's source.

**Result:** LaunchStudio's review identified the exposed key during a routine Next.js-specific check, rotated the credential immediately, and restructured the data-processing call to run through a proper server-side API route instead — resolving the original build error's underlying cause correctly rather than through the prefix workaround that had inadvertently exposed the key for months.

> *"The build error went away the moment I added that prefix, so as far as I could tell, the problem was solved. It never occurred to me that 'fixed' in that specific sense meant 'now visible to literally anyone who looked at my site's JavaScript,' since nothing about the app breaking or working differently ever signaled that."*
> — **Jelle Verstegen, Founder, AnalyseHub (Dordrecht)**

**Cost & Timeline:** €800 (Next.js secret exposure remediation and API route restructuring) — completed in 3 business days.

---

## Frequently Asked Questions

### How would I check whether my own Next.js app has this specific issue without deep framework expertise?

Searching your codebase for any `NEXT_PUBLIC_`-prefixed environment variable and confirming each one is genuinely meant to be public, rather than a workaround for a build error like Jelle's case, is a reasonable first check achievable without deep framework expertise, though a thorough review of the actual compiled client bundle provides more complete verification.

### Is this risk specific to Next.js, or does it apply to other similarly blended frontend-backend frameworks too?

The specific mechanism (a `NEXT_PUBLIC_`-style prefix) is Next.js-specific, but the underlying risk category — a framework that blends server and client code in a way that makes the boundary easy to blur — applies conceptually to other similarly-structured frameworks, each with their own specific mechanism for marking public versus private values.

### If a secret has already been exposed this way, is rotating the key sufficient, similar to the git history guidance covered elsewhere in this series?

Yes, the same underlying principle applies — rotating the exposed credential at the source neutralizes the exposure going forward, regardless of how long the previous value was accessible in the client bundle, though confirming no unauthorized usage occurred during the exposure window, as covered in this series' secrets guidance, is also worth checking.

### Why did the AI coding assistant in Jelle's case suggest a fix that created a security problem?

The suggestion resolved the immediate, visible symptom (the build error) without independently reasoning about the security implication of making a secret client-visible — consistent with this series' broader guidance on why AI-generated solutions optimize for functional correctness against the immediate problem, not for security properties nobody specifically asked about.

### How can a founder avoid this specific mistake going forward as they continue developing their Next.js app?

Establishing a habit of pausing specifically when a build error involves an environment variable, and asking whether the fix is "make this build" or "make this build correctly and safely," rather than accepting the first suggestion that resolves the visible error, is the practical discipline this specific risk calls for.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How can a founder check for this specific issue without deep Next.js expertise?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Searching the codebase for NEXT_PUBLIC_-prefixed variables and confirming each is genuinely meant to be public is a reasonable first check."
      }
    },
    {
      "@type": "Question",
      "name": "Is this risk specific to Next.js, or does it apply to other blended frontend-backend frameworks?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The specific mechanism is Next.js-specific, but the underlying risk category applies conceptually to other similarly-structured frameworks."
      }
    },
    {
      "@type": "Question",
      "name": "If a secret has already been exposed this way, is rotating the key sufficient?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, rotating the credential at the source neutralizes the exposure, though checking for unauthorized usage during the exposure window is also worth doing."
      }
    },
    {
      "@type": "Question",
      "name": "Why did an AI coding assistant suggest a fix that created a security problem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The suggestion resolved the immediate visible symptom without independently reasoning about the security implication of making a secret client-visible."
      }
    },
    {
      "@type": "Question",
      "name": "How can a founder avoid this specific mistake going forward?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Pausing when a build error involves an environment variable and asking whether the fix is safe, not just whether it makes the build pass."
      }
    }
  ]
}
</script>
