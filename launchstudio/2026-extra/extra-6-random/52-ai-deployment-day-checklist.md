---
Title: "The AI Deployment Day That Goes Wrong (And the Checklist That Prevents It)"
Keywords: ai deployment, deploy ai generated app, environment variables production, ai app launch checklist
Buyer Stage: Consideration
Target Persona: Technical Solo Founder
---

# The AI Deployment Day That Goes Wrong (And the Checklist That Prevents It)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The AI Deployment Day That Goes Wrong (And the Checklist That Prevents It)",
  "description": "A step-by-step account of how an AI deployment goes wrong when environment variables aren't separated by environment, plus the checklist that catches it before launch.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-deployment-day-checklist" }
}
</script>

9:14 AM: you push to production. 9:16 AM: the app loads, the demo works, you screenshot it for the team channel. 9:52 AM: someone opens dev tools out of curiosity and finds your AI provider's API key sitting in plain text in the frontend JavaScript bundle, visible to anyone who opens the same tab you just celebrated in. This is not a hypothetical. It is the single most common way an AI deployment goes from "we shipped" to "we have a problem," and it happens because deployment day has a hundred small decisions in it, and exactly one of them — where a secret lives — is the one that can't be undone by a quick fix.

## Why deployment day is where this specific mistake lives

Building an app with Cursor, Bolt, or similar tools tends to happen in one continuous environment: one project, one set of configuration values, one mental model of "the app." Deployment is the first moment that mental model has to split into at least two realities — development and production — each of which should have its own separate configuration, especially for anything resembling a secret. If that split never happens explicitly, the values that worked fine locally get carried forward as-is, including any API key that was only ever meant to live on a server, not inside code that ships to every visitor's browser.

This is exactly the mistake that's easy to make once and catch never, because nothing about it looks wrong at deploy time. The app works. The feature that calls the AI provider's API works. It's only when someone inspects what actually got sent to the browser that the key turns up in plain sight — and by then it's been live, and potentially harvestable, for as long as the deployment has been public.

## The checklist that catches it before it ships

- **Separate environment files for dev and production** — never let one `.env` file serve both; production secrets should exist only where production code runs.
- **Confirm which variables are frontend-exposed vs. server-only** — anything prefixed for client-side bundling (a common pattern in modern frameworks) gets shipped to every visitor's browser; anything meant to stay private must never carry that prefix.
- **Search the built frontend bundle for the literal string of any API key** before calling deployment done — not the source code, the actual compiled output that ships to browsers.
- **Rotate any key that touched a public repository or a client-bundled build**, even briefly, rather than assuming it wasn't noticed.
- **Confirm rate limits and quotas on any third-party API key** — a leaked key isn't just a privacy issue, it's a billing issue if someone else starts using it.
- **Test the deployed app from an incognito browser with dev tools open**, specifically looking at network requests and bundled scripts, not just the rendered page.

## Why this specific gap is so common in AI-built apps

AI coding assistants are excellent at wiring a feature end to end — call this API, render this response — but the tool has no independent awareness of which values in that wiring are secrets versus which are public configuration. If a prompt says "connect to the AI provider using this key," the tool will do exactly that, in whichever file makes the feature work, without necessarily flagging that the file in question ends up bundled and shipped to the browser. The distinction between server-side and client-side code is an architectural concept the tool assumes you already understand — and for founders moving fast on their first production deploy, that's often the one thing nobody explicitly checked.

Manifera brings 11+ years of production engineering experience to exactly this kind of gap, with engineers based in Singapore supporting founders across the region on deployment reviews before launch, not after. If you're approaching your own deployment day, you can [talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact) before you push, or look at how Manifera structures [offshore software development](https://www.manifera.com/services/offshore-software-development/) for teams that want this kind of review built into their process rather than bolted on afterward.

## Real example

### An AI-Native Founder in Action: The Key in Plain Sight

Vincent Voskuil, a founder based in Enkhuizen, built "MeldStroom" — an incident-reporting tool for small operational teams — using Cursor. The app used an AI provider's API to help categorize incoming reports automatically, a feature Vincent had wired up early and tested extensively in development. When deployment day came, he pushed the same configuration straight to production, without separating which environment variables belonged where.

The AI provider's API key, which had only ever needed to be called from the server, ended up bundled directly into the public frontend JavaScript — visible to anyone who opened their browser's developer tools and looked at the network tab or the compiled scripts. Nobody had done anything malicious to cause this; the key simply lived in a configuration file that got pulled into the client-side build the same way it had in local development, because nothing in the deployment step had separated the two.

It was discovered when a technically curious early user, poking around the app out of general interest, noticed the key sitting in plain view in a script file. Vincent brought MeldStroom to LaunchStudio immediately. Our engineers rotated the exposed key, restructured the app so all AI provider calls route through a server-side endpoint instead of directly from the browser, and set up properly separated environment configurations for development and production going forward.

**Result:** MeldStroom's API calls to the AI provider now happen entirely server-side, with the key never present in any code shipped to a browser, and rate-limit monitoring in place to catch any future misuse of that key.

> *"I tested the feature a hundred times in development and it worked perfectly every time. It never once occurred to me that 'working' and 'safe to deploy' were different questions."*
> — **Vincent Voskuil, Founder, MeldStroom (Enkhuizen)**

**Cost & Timeline:** €1,100 (key rotation, server-side API routing, environment separation) — completed in 4 business days.

---

## Frequently Asked Questions

### Why do API keys end up exposed in the frontend so often?

Because development environments frequently mix client-side and server-side configuration in one place, and unless that's explicitly split before deployment, secrets meant for the server can get bundled into code that ships to the browser.

### How can I check if my own app has this issue right now?

Open your deployed app in a browser, open dev tools, and search the network requests and loaded scripts for any API key string — if it appears anywhere in that view, it's exposed.

### What should I do if I find an exposed key?

Rotate it immediately with the provider, then move the code that uses it to a server-side endpoint so the key never needs to leave your own infrastructure.

### Does LaunchStudio review deployments before they go live?

Yes — this is a standard part of our pre-launch review, and our engineers, including the team based in Singapore, specifically check for exactly this class of exposure before a founder pushes to production.

### Is this only a risk with Cursor?

No, it's a deployment-process risk that applies regardless of which AI coding tool built the app — the fix is the same either way: separate environments, and never let secrets reach client-side code.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Why do API keys end up exposed in the frontend so often?", "acceptedAnswer": { "@type": "Answer", "text": "Because development environments frequently mix client-side and server-side configuration in one place, and unless that's explicitly split before deployment, secrets meant for the server can get bundled into code that ships to the browser." } },
    { "@type": "Question", "name": "How can I check if my own app has this issue right now?", "acceptedAnswer": { "@type": "Answer", "text": "Open your deployed app in a browser, open dev tools, and search the network requests and loaded scripts for any API key string — if it appears anywhere in that view, it's exposed." } },
    { "@type": "Question", "name": "What should I do if I find an exposed key?", "acceptedAnswer": { "@type": "Answer", "text": "Rotate it immediately with the provider, then move the code that uses it to a server-side endpoint so the key never needs to leave your own infrastructure." } },
    { "@type": "Question", "name": "Does LaunchStudio review deployments before they go live?", "acceptedAnswer": { "@type": "Answer", "text": "Yes — this is a standard part of our pre-launch review, and our engineers, including the team based in Singapore, specifically check for exactly this class of exposure before a founder pushes to production." } },
    { "@type": "Question", "name": "Is this only a risk with Cursor?", "acceptedAnswer": { "@type": "Answer", "text": "No, it's a deployment-process risk that applies regardless of which AI coding tool built the app — the fix is the same either way: separate environments, and never let secrets reach client-side code." } }
  ]
}
</script>
