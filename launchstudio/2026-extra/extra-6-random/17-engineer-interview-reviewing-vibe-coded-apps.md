---
Title: "An Interview With a LaunchStudio Engineer: What Nobody Tells You About Reviewing Vibe-Coded Apps"
Keywords: ai coding, vibe coding review, code review, cursor pull requests, ai-generated code audit
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# An Interview With a LaunchStudio Engineer: What Nobody Tells You About Reviewing Vibe-Coded Apps

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "An Interview With a LaunchStudio Engineer: What Nobody Tells You About Reviewing Vibe-Coded Apps",
  "description": "A conversation with a LaunchStudio engineer about what actually happens when a human reviews an AI-generated codebase, including a real example of reviewing pull requests from a Cursor-built CRM.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/engineer-interview-reviewing-vibe-coded-apps" }
}
</script>

We sat down with one of LaunchStudio's engineers — part of the team based in Amsterdam who reviews AI-generated codebases every week — to ask a simple question: what actually happens when a human opens up a "vibe-coded" app for the first time? The answer turned out to be less about bugs and more about a specific kind of blindness that AI coding tools create without meaning to. Below is the conversation, lightly edited for length.

## The interview

**Q: What's the first thing you look for when you open a project built with an AI coding tool?**

A: Honestly, not the code itself first. I look at what's missing — what a human engineer would have written a comment about, or asked a question about in a standup, that simply never got asked. AI coding tools are confident. They don't leave a trail of "I wasn't sure about this part, someone should check it." A junior developer would leave that trail. An AI tool just ships the decision silently, and it looks exactly as polished as the parts that are actually solid.

**Q: Is vibe-coded software worse than what a junior developer would write?**

A: Not necessarily worse — different. A junior developer's mistakes tend to cluster: if they misunderstand authentication, they'll probably misunderstand it consistently across the app, which is actually easier to catch. AI-generated mistakes are scattered. One function will handle edge cases beautifully. The function right next to it, doing something structurally similar, will have skipped a check entirely. There's no consistent "blind spot" to search for, because the tool isn't reasoning about the app as a whole the way a person would.

**Q: What's the most common thing founders assume is fine, that isn't?**

A: That "it worked in the demo" means it's handled. I reviewed a CRM tool recently — a founder named Milan Verhagen was building something called KlantStroom with Cursor — and pull request after pull request looked clean at a glance. Functions were named sensibly, the UI worked, nothing crashed. But when I traced how customer records actually got created, there was a gap where a webhook could fire twice for the same event and create a duplicate customer with no unique constraint stopping it. It never showed up in testing because nobody tested the exact timing that triggers it. That's the pattern: things that work every time you'd naturally try them, and fail only under conditions a human wouldn't think to simulate.

**Q: How do you actually review a codebase like that efficiently?**

A: We don't read every line — that doesn't scale and it's not where the risk lives. We trace the paths that matter most: how money moves, how auth decisions get made, how customer data gets written and deleted. We treat those as high-scrutiny zones regardless of how clean the surrounding code looks. Everything else gets a lighter pass. It's less "code review" in the traditional sense and more "risk mapping" — figuring out where a silent AI decision could actually hurt someone.

**Q: What do you wish founders understood before they hand over a vibe-coded app for review?**

A: That a clean-looking app and a safe app are not the same thing, and that's not a knock on the tools — Lovable, Bolt, Cursor, v0 are genuinely good at producing working software fast. It's just that "working" and "production-ready" are different bars, and nobody tells founders that the AI tool only cleared the first one.

Manifera brings 11+ years of production engineering experience to exactly this kind of review, and our Amsterdam-based engineers do this work daily across Lovable, Bolt, Cursor, and v0 projects. If you want a second pair of eyes on your own prototype, you can [send us your prototype link for free advice](https://launchstudio.eu/en/#contact) before you find your own version of Milan's webhook bug the hard way. For a broader look at how this kind of engineering review fits into larger builds, see Manifera's [web app development services](https://www.manifera.com/services/web-app-develop/).

## A Quick Self-Test: Three Questions to Ask About Your Own App Before You Ship

You don't need to be able to read code to run a rough version of the risk-mapping the engineer above described. You need to be willing to ask three specific questions about your own product and actually go looking for the answers, rather than assuming "it worked when I tried it" settles the matter.

**Question one: what happens if the same action gets triggered twice, close together?** Click a submit button twice quickly. Refresh mid-payment and try again. Trigger the same automated action (an email send, a webhook, a scheduled job) in a way that could plausibly fire more than once. If your product silently does the thing twice — creates two records, sends two charges, sends two emails — that's exactly the kind of gap the interview above describes: invisible in a single careful test, real the moment usage isn't perfectly orderly.

**Question two: what does a stranger see if they guess at a URL or an ID?** Log in as one test account, note the web address or ID for something that belongs to that account, then log in as a second test account and try changing the ID in the address bar to the first account's value. If you can see or edit something that isn't yours, that's not a minor cosmetic bug — it's one of the most common categories of gap in AI-generated apps, because a page working correctly for the person it was built for tells you nothing about whether it also, incorrectly, works for everyone else.

**Question three: what does your app show when something it depends on is slow or unavailable?** Turn off your wifi mid-action, or ask whoever built your integrations what happens if the payment processor or the AI provider your app calls takes ten seconds to respond instead of one. A product that only ever gets tested against a fast, cooperative internet connection has never actually been tested against the internet most of your real customers will use it on.

You won't be able to fix what these three questions surface on your own, and that's fine — that's not the point of running them. The point is walking into a review, whether with a hired engineer or a technical co-founder, already knowing roughly where the soft spots are, instead of handing over a project with no sense of where to direct attention first. A founder who shows up already having asked "what happens if this fires twice" gets a faster, more focused review than one who's only ever tested the version of their app that behaves.

## Real example

### An AI-Native Founder in Action: The Duplicate Customer Bug in KlantStroom

Milan Verhagen, a founder in Zwolle, built KlantStroom — a CRM tool for small sales teams — using Cursor. The product handled leads, deals, and customer records well enough to onboard several paying teams, and Milan had no reason to suspect anything was structurally wrong; every manual test he ran passed cleanly.

The gap our engineer described above surfaced during a scheduled review ahead of Milan's plan to integrate a billing provider. Tracing the webhook handler that created customer records revealed that a retried webhook delivery — something that happens routinely with most integration providers when a response is slow — could create two identical customer records instead of one, because there was no unique constraint or idempotency check on the incoming event. It hadn't caused visible damage yet, but it was a matter of time before duplicate records started corrupting reports and, eventually, billing.

LaunchStudio added an idempotency key check on the webhook handler and a unique constraint on the customer table to prevent duplicates outright, then cleaned up the handful of duplicate records that had already quietly accumulated. Nothing about the rest of KlantStroom needed to change — the fix was isolated to the exact path where the risk lived.

**Result:** KlantStroom now processes retried webhooks safely, with duplicate creation structurally impossible rather than merely unlikely.

> *"I'd tested that flow a dozen times myself and never hit the bug. It only showed up when the review traced what happens under conditions I'd never have thought to simulate."*
> — **Milan Verhagen, Founder, KlantStroom (Zwolle)**

**Cost & Timeline:** €750 (webhook idempotency fix, unique constraint, duplicate cleanup) — completed in 3 business days.

---

## Frequently Asked Questions

### What does "vibe-coded" actually mean?

It refers to software built largely by describing what you want in natural language to an AI coding tool like Lovable, Bolt, Cursor, or v0, rather than writing the code by hand — the term describes the process, not a judgment on the result.

### Do LaunchStudio's engineers rewrite vibe-coded apps or just review them?

Both, depending on what's found — most reviews end in a targeted fix rather than a rewrite, similar to how Milan's webhook issue was resolved without touching the rest of KlantStroom.

### Why does an AI-generated app look clean but still have hidden bugs?

Because AI coding tools optimize for producing working code for the cases you describe, not for flagging the edge cases you didn't think to mention — the result looks uniformly polished even where the logic is incomplete.

### Where is the engineer quoted in this interview based?

Part of the team is based in Amsterdam, LaunchStudio's European hub, though reviews like Milan's are handled by engineers across Manifera's broader team.

### How much does a code review like Milan's typically cost?

Targeted reviews and fixes like the one described here typically fall in the €400–€1,500 range depending on scope, well within LaunchStudio's standard €800–€7,500 project pricing.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "What does 'vibe-coded' actually mean?", "acceptedAnswer": { "@type": "Answer", "text": "It refers to software built largely by describing what you want in natural language to an AI coding tool like Lovable, Bolt, Cursor, or v0, rather than writing the code by hand." } },
    { "@type": "Question", "name": "Do LaunchStudio's engineers rewrite vibe-coded apps or just review them?", "acceptedAnswer": { "@type": "Answer", "text": "Both, depending on what's found. Most reviews end in a targeted fix rather than a full rewrite." } },
    { "@type": "Question", "name": "Why does an AI-generated app look clean but still have hidden bugs?", "acceptedAnswer": { "@type": "Answer", "text": "AI coding tools optimize for producing working code for the cases you describe, not for flagging edge cases you didn't mention, so the result looks uniformly polished even where logic is incomplete." } },
    { "@type": "Question", "name": "Where is the engineer quoted in this interview based?", "acceptedAnswer": { "@type": "Answer", "text": "Part of the team is based in Amsterdam, LaunchStudio's European hub, though reviews are handled across Manifera's broader engineering team." } },
    { "@type": "Question", "name": "How much does a code review like this typically cost?", "acceptedAnswer": { "@type": "Answer", "text": "Targeted reviews and fixes typically fall in the €400–€1,500 range, within LaunchStudio's standard €800–€7,500 project pricing." } }
  ]
}
</script>
