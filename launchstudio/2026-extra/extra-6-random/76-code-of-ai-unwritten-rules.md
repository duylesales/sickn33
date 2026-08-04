---
Title: "The Unwritten Code Every AI Coding Tool Follows (and Why It's Not Yours)"
Keywords: code of ai, ai coding tool defaults, ai default decisions, ai generated code assumptions
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# The Unwritten Code Every AI Coding Tool Follows (and Why It's Not Yours)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Unwritten Code Every AI Coding Tool Follows (and Why It's Not Yours)",
  "description": "Every AI coding tool has an unwritten code of defaults it falls back on at every ambiguous decision — and that code favors speed, not your caution.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/code-of-ai-unwritten-rules" }
}
</script>

Every professional has an unwritten code — a cautious engineer's is roughly "when in doubt, restrict access, ask permission, add the guardrail." It's a personality, formed by years of watching what goes wrong. AI coding tools have an unwritten code too, formed by an entirely different pressure: satisfy the prompt, produce working code, do it fast. Those two codes are not the same, and founders who assume they are get an unpleasant surprise the first time an ambiguous decision gets made on their behalf.

## The default is speed, not caution

When an AI coding tool hits a decision point that your prompt didn't specify — what permission level should this new database table have, should this endpoint require authentication, how permissive should this file upload be — it has to pick something. Trained overwhelmingly on getting things to *work*, its unwritten code of a default is almost always the option that gets the feature functioning fastest, with the fewest additional steps. That is very often the least restrictive option available, because restrictive options require more configuration, more decisions, more back-and-forth that a cautious human would normally insist on and a tool optimizing for a working demo has no reason to add.

## You inherited a code you never agreed to

This is the part that trips up non-technical founders specifically: you didn't choose this unwritten code. You didn't sit down and decide "when in doubt, favor open access over restricted access." The tool decided that, silently, at every ambiguous fork in the road, and it did so consistently across your entire application — not once, but potentially dozens of times, at every table permission, every endpoint, every configuration default that your prompt didn't explicitly pin down.

The result is a codebase that reflects a philosophy you never signed off on. If you'd been asked directly, "should this data be readable by anyone with a link, or only by the account that owns it," you would have said the latter, obviously. Nobody asked. The unwritten code answered for you, and it answered in favor of whatever got the demo working with the least friction.

## Why this is worse than a single bug

A single bug is a single bug — fixable, contained, findable with enough testing. An unwritten code operating across your whole codebase is different: it's not one mistake, it's a *pattern* of the same kind of decision made dozens of times, each individually invisible, each individually defensible as "well, you didn't say otherwise." Finding all of them requires someone to go looking specifically for the pattern, not just testing whether features work — because every one of them will appear to work perfectly.

Our engineers based in Amsterdam spend a significant part of every codebase review looking specifically for this pattern — the accumulated trail of least-restrictive defaults chosen at every point your prompt left open. LaunchStudio is powered by Manifera, a software development company with 11+ years of production engineering experience, and this kind of default-auditing is exactly the discipline that experience brings to a review. You can explore [what LaunchStudio actually does](https://launchstudio.eu/en/) before deciding whether your own app needs this kind of pass. For the broader engineering philosophy behind it, see [Manifera's about page](https://www.manifera.com/about-us/).

## A Fast Way to Surface the Defaults You Never Actually Chose

Waiting for a security review or a client's questionnaire to surface these accumulated defaults is one way to find them. A faster, more deliberate way is to go looking on purpose, using a short list of questions that don't require reading code — just knowing what to ask, and who to ask it of.

1. **List every place your app stores data, then ask "who can read this by default?"** For each table or data store, the honest question isn't "does the feature work correctly" — it's "if someone with valid login access queried this directly, bypassing the app's interface entirely, what would they see?" If the answer is "more than their own data," that's an unwritten default made without your input.

2. **Ask specifically whether new features default to public or private.** When a new feature gets added — a shared document, a public profile, an exported report — the tool made a call about who can see it by default. Ask, feature by feature, whether that default was ever stated explicitly in your original prompt, or whether it was simply whatever the tool produced when the question wasn't raised.

3. **Check whether "logged in" and "authorized" were treated as the same thing.** A significant share of least-restrictive defaults hide in this exact gap — the tool correctly required someone to be logged in, but never separately checked whether that specific logged-in person should see that specific piece of data. Ask this question about every sensitive action in your app individually, since the answer can differ feature by feature even within the same product.

4. **Ask what happens with no explicit instruction, not what happens with the instruction you gave.** You already know your app does what you asked for. The unwritten code lives in what it does when you *didn't* specify — file upload size limits you never mentioned, session timeouts you never set, password requirements you never defined. Each of these was decided by default, in favor of speed, and it's worth listing them out explicitly rather than assuming reasonable defaults were applied simply because nothing looked broken.

5. **Bring someone technical in to verify the answers, not just generate them.** A non-technical founder can ask all four questions above and get a useful first read, but confirming the actual answer — what a database table's permissions genuinely allow, independent of what the app's interface shows — requires someone who can inspect the configuration directly rather than test the feature through its normal use.

Running through this list takes an hour of thinking and a shorter follow-up conversation with whoever built or is reviewing your app — considerably cheaper than discovering the same pattern mid-review, with a client's security questionnaire already sitting open in front of you and no good answer ready.

## Real example

### An AI-Native Founder in Action: The Defaults Nobody Chose

Yara Loman, a founder based in Zwijndrecht, built "EthiekGids," a compliance-training app for corporate clients, using Bolt. Yara assumed, reasonably from her perspective, that a modern AI coding tool would default to conservative choices the way a careful engineer would — restrict first, open up only when asked. She never specified detailed permission rules for most of the app's data, trusting the tool to fill those gaps sensibly.

It didn't. At nearly every ambiguous decision point Bolt encountered while building EthiekGids, it chose the fastest, least-restrictive option rather than the cautious one — including on database permissions, where several tables ended up configured with broader read access than any feature actually required. None of this broke anything visibly. The app worked exactly as demoed. The gap only became apparent when Yara, preparing for a corporate client's own security questionnaire, had someone actually inspect the database configuration directly rather than testing the app's behavior through its interface.

LaunchStudio was engaged to audit every table and endpoint specifically for this pattern of least-restrictive defaults, rather than testing feature-by-feature. Our engineers reset database permissions to the minimum each feature actually required, tightened access controls table by table, and documented every change so Yara's compliance-training clients could see exactly what had been corrected.

**Result:** EthiekGids passed its client's security questionnaire on the next attempt, with permissions now matching the actual access each feature needed rather than whatever was fastest to build.

> *"I thought caution was the default. It turned out speed was, and nobody had told me."*
> — **Yara Loman, Founder, EthiekGids (Zwijndrecht)**

**Cost & Timeline:** €1,100 (full permissions audit and reconfiguration) — completed in 5 business days.

---

## Frequently Asked Questions

### Why do AI coding tools default to the least-restrictive option?

Because restrictive configurations require more decisions and setup, and a tool optimized for producing fast, working code has no built-in reason to add friction the prompt didn't request.

### How would a founder even notice this kind of gap?

Usually not through normal use — the app behaves exactly as intended. It typically surfaces during a security review, a client's compliance questionnaire, or a direct inspection of database and permission settings.

### Is this a bug, or is it working as designed?

It's working exactly as designed from the tool's perspective — it fulfilled the prompt as given. The gap is that the prompt never specified caution, so the tool never applied it.

### Does Manifera specifically audit for this pattern of defaults?

Yes. Engineers on Manifera's team, including those based in Amsterdam, review codebases specifically for accumulated least-restrictive defaults, not just individual bugs.

### Can these defaults be corrected without rebuilding the app?

Yes, correcting permissions and access defaults is typically a configuration and backend-layer fix that doesn't require changes to the existing frontend.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Why do AI coding tools default to the least-restrictive option?", "acceptedAnswer": { "@type": "Answer", "text": "Restrictive configurations require more setup and decisions, and a tool optimized for fast working code has no built-in reason to add friction the prompt didn't request." } },
    { "@type": "Question", "name": "How would a founder even notice this kind of gap?", "acceptedAnswer": { "@type": "Answer", "text": "Usually not through normal use since the app behaves as intended. It typically surfaces during a security review, a compliance questionnaire, or a direct inspection of settings." } },
    { "@type": "Question", "name": "Is this a bug, or is it working as designed?", "acceptedAnswer": { "@type": "Answer", "text": "It's working as designed from the tool's perspective. The gap is that the prompt never specified caution, so the tool never applied it." } },
    { "@type": "Question", "name": "Does Manifera specifically audit for this pattern of defaults?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, Manifera's team, including engineers based in Amsterdam, reviews codebases specifically for accumulated least-restrictive defaults." } },
    { "@type": "Question", "name": "Can these defaults be corrected without rebuilding the app?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, correcting permissions and access defaults is typically a configuration and backend-layer fix that doesn't require frontend changes." } }
  ]
}
</script>
