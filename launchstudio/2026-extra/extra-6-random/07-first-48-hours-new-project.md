---
Title: "What LaunchStudio's Engineers Actually Do in the First 48 Hours of a New Project"
Keywords: ai app dev, ai prototype to production, engineering onboarding, ai code review process
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# What LaunchStudio's Engineers Actually Do in the First 48 Hours of a New Project

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What LaunchStudio's Engineers Actually Do in the First 48 Hours of a New Project",
  "description": "A behind-the-scenes walkthrough of LaunchStudio's first-48-hours process for ai app dev projects, following a real founder's onboarding from read-only review to fix plan.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/first-48-hours-new-project" }
}
</script>

Most founders who hand over a prototype have no idea what happens on the other side. You send a repo link, maybe a Loom video explaining what the app is supposed to do, and then... silence, until someone tells you what's wrong with it. That gap feels risky if you've never worked with an engineering team before. So here is exactly what happens in the first 48 hours after a project lands on our desk, using a real project as the walkthrough: a survey tool called MeetGoed, built in Cursor by a founder named Sven Kramer in Breda.

Sven had built MeetGoed to let event organizers collect structured feedback without wrestling with SurveyMonkey templates. The product worked. Demos went smoothly. He'd never had it touched by a professional engineer before he sent it to us, which is typical for ai app dev projects that start as one person and a chat window.

## Hours 0-4: The Read-Only Pass

Nobody touches the codebase in the first four hours. An engineer clones the repo, spins it up locally, and reads — every route, every database call, every environment variable reference — without changing a single line. The goal is a mental map: what does this app actually do, versus what the founder believes it does.

For MeetGoed, this pass turned up the first red flag within about ninety minutes: API keys for the email-sending service were hardcoded directly into a client-side file, visible to anyone who opened the browser's dev tools. Sven had no idea. Cursor had generated a working integration; it had not generated a secure one, and there's no reason it would — the tool was optimizing for "the emails send," not "the emails send safely."

## Hours 4-16: Vulnerability Triage

This is where the map from phase one turns into a prioritized list. Not everything found gets treated the same way. Our engineers separate findings into three buckets: fix before anything else touches production, fix before the next feature ships, and fix eventually.

For Sven's project, the "fix before anything else" bucket had three items stacked on top of each other, which is common — issues in AI-generated code rarely show up alone:

- The exposed API keys, already mentioned, which needed to move server-side immediately.
- No rate limiting on the survey submission endpoint, meaning a single script could flood the database with fake responses or run up his email-sending bill in an afternoon.
- Missing input validation on several form fields, which meant the backend trusted whatever the frontend sent it — a gap that AI coding tools frequently leave open because validation logic isn't visually obvious in a demo.

None of these would have shown up in a product demo. All three would have shown up the first week MeetGoed had real traffic.

## Hours 16-36: The Fix Plan and the Founder Conversation

By hour sixteen, there's usually a document, not just a conversation — a written list of what was found, why it matters in plain language, and what the fix involves. This is deliberately not a wall of jargon. Sven got a call where the API key issue was explained as "right now, anyone who opens their browser console can see the password to your email account," which is a sentence a non-technical founder can act on immediately.

This is also the stage where scope gets locked in. Our engineers are backed by Manifera, a software development company with 11+ years of production engineering experience, and that experience mostly shows up here: knowing which fixes are quick and which ones hide complexity underneath. The team working on Sven's review is part of the same Amsterdam-based group that runs LaunchStudio's European operations, and they've seen this exact stacked pattern — exposed keys, no rate limiting, no validation — often enough to know the order matters. Fix validation first and the rate limiter has less garbage traffic to filter.

## Hours 36-48: What Ships, What Waits

The last stretch is where the priority fixes actually get written, tested against the existing frontend, and confirmed not to break anything Sven's users already relied on. We don't touch his UI. The promise behind LaunchStudio is production infrastructure without a frontend rebuild, and that promise gets tested hardest right here, in the first 48 hours, when it would be fastest to just rewrite things from scratch instead of working around them.

If you want to see how this fits into the fuller engagement, our [process breakdown](https://launchstudio.eu/en/#process) walks through what happens after these first two days. For teams evaluating whether their own codebase needs this kind of pass before it goes live, Manifera's [custom software development](https://www.manifera.com/services/custom-software-development/) work follows the same read-first, fix-second discipline on a larger scale.

## Real example

### An AI-Native Founder in Action: MeetGoed's First Weekend Review

Sven Kramer built MeetGoed alone over several weekends, using Cursor to generate most of the backend logic for survey creation, response collection, and email notifications to organizers. It worked well enough that two local event companies had already agreed to pilot it. He hadn't touched a line of the generated code himself and had no way to judge whether it was safe to put in front of real customers.

Our engineers' first 48-hour review found the stacked issues described above: hardcoded API keys visible client-side, no rate limiting on submissions, and form fields with no server-side validation. Any one of these alone would have been a manageable fix. Together, they meant MeetGoed was one curious visitor away from a leaked email password, a flooded inbox, or corrupted survey data.

The fix moved the email credentials server-side behind an environment variable, added request throttling on the submission endpoint, and layered validation onto every public-facing form field — all without changing how MeetGoed looked or felt to Sven's pilot users. He kept his frontend exactly as Cursor had built it.

**Result:** MeetGoed launched its two pilot programs on schedule, with the founder able to tell prospective event clients, honestly, that the data pipeline had been professionally reviewed.

> *"I thought sending the code over meant a rewrite. Instead they told me what was actually broken and fixed just that. I still don't fully understand rate limiting, but I understand why I needed it now."*
> — **Sven Kramer, Founder, MeetGoed (Breda)**

**Cost & Timeline:** €1,200 (security triage and fixes for exposed keys, rate limiting, and input validation) — completed in 6 business days.

---

## Frequently Asked Questions

### What happens if the founder doesn't know what their own code does?

That's the default, not the exception. The 48-hour review is built for founders who built with Cursor, Lovable, Bolt, or v0 and have never audited a codebase themselves — the read-only pass exists precisely so nobody has to explain their own code before it gets reviewed.

### Does the first 48 hours involve any changes to the frontend?

No. The review and triage stages are entirely backend, infrastructure, and security-focused. LaunchStudio's engineers, backed by Manifera's 120+ engineers, work around your existing frontend rather than replacing it.

### How does LaunchStudio decide what to fix first?

Findings get bucketed into immediate risk, pre-launch priority, and long-term cleanup. Immediate risk items — like the exposed API keys found in Sven's project — get addressed before anything else, regardless of what else is on the roadmap.

### Is this process different for a Lovable or Bolt project versus a Cursor project?

The tools leave different fingerprints — Bolt projects tend to have different deployment quirks than Cursor projects, for example — but the 48-hour read-first, triage-second structure stays the same across all of them.

### Where is the team doing this review based?

Project reviews for European founders typically run through LaunchStudio's Amsterdam team, working out of Herengracht 420, though the underlying engineering group spans multiple offices.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "What happens if the founder doesn't know what their own code does?", "acceptedAnswer": { "@type": "Answer", "text": "That's the default, not the exception. The 48-hour review is built for founders who built with Cursor, Lovable, Bolt, or v0 and have never audited a codebase themselves." } },
    { "@type": "Question", "name": "Does the first 48 hours involve any changes to the frontend?", "acceptedAnswer": { "@type": "Answer", "text": "No, the review and triage stages are entirely backend, infrastructure, and security-focused, and LaunchStudio's engineers work around the existing frontend rather than replacing it." } },
    { "@type": "Question", "name": "How does LaunchStudio decide what to fix first?", "acceptedAnswer": { "@type": "Answer", "text": "Findings are bucketed into immediate risk, pre-launch priority, and long-term cleanup, with immediate risk items addressed before anything else on the roadmap." } },
    { "@type": "Question", "name": "Is this process different for a Lovable or Bolt project versus a Cursor project?", "acceptedAnswer": { "@type": "Answer", "text": "The tools leave different fingerprints, but the read-first, triage-second structure stays consistent across all of them." } },
    { "@type": "Question", "name": "Where is the team doing this review based?", "acceptedAnswer": { "@type": "Answer", "text": "Project reviews for European founders typically run through LaunchStudio's Amsterdam team, working out of Herengracht 420, though the underlying engineering group spans multiple offices." } }
  ]
}
</script>
