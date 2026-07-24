---
Title: "A Day in the Life of an Engineer Reviewing AI-Generated Pull Requests"
Keywords: ai software developers, ai generated pull request review, code review ai, unescaped user input
Buyer Stage: Awareness
Target Persona: Technical Solo Founder
---

# A Day in the Life of an Engineer Reviewing AI-Generated Pull Requests

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "A Day in the Life of an Engineer Reviewing AI-Generated Pull Requests",
  "description": "A narrative walkthrough of a real day spent by one of LaunchStudio's ai software developers reviewing an AI-generated pull request, following a real founder's codebase.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/reviewing-ai-generated-pull-requests" }
}
</script>

8:52 AM. Coffee, laptop open, the queue for the day already has three pull requests waiting. This is a normal Tuesday for one of LaunchStudio's ai software developers, and the second item in the queue is a submission from Puck Willemsen, a founder in Haarlem who built BuurtHulp — a community help-request app — using Lovable. Her note in the PR description reads: "Added the request-detail page and comment threads, should be ready to go live this week." Let's follow the actual review, start to finish.

## 9:05 AM — First Pass, No Judgments Yet

The rule for a first pass is simple: read before you touch anything, and don't form conclusions about severity until you've seen the whole diff. Puck's PR touches the new request-detail page, a comment thread component, and a handful of backend routes that serve comment data. It's a reasonably contained change on paper — maybe 40 minutes of reading, tops.

Line 34 of the comment component is where the first thing catches. User-submitted comment text gets rendered directly into the page without being escaped first. On its own, in one file, this is a fixable ten-minute issue: sanitize the string before it renders, done. But a first pass isn't about fixing the first thing you see — it's about noticing whether it's a one-off or a pattern.

## 10:20 AM — Running the Pattern Check

This is the part that separates a review from a skim. Instead of just patching line 34, the next move is a repo-wide search for the same unsafe rendering pattern — the same unescaped-input construction, just written slightly differently depending on which component Lovable generated it for.

The search comes back with twelve files. Twelve separate places where user-submitted text — comments, request descriptions, a couple of profile fields — gets rendered without sanitization, all following the same underlying unsafe pattern. This is the signature of an AI-generated codebase more than a human-written one: a human developer who wrote an unsafe pattern once in file three would probably not reproduce the exact same mistake independently in file eleven. An AI tool asked to build twelve similar-looking components across separate sessions has no reason not to.

## 11:45 AM — The Decision: Patch Twelve Spots, or Fix the Root

This is the actual engineering judgment call of the day, and it's the part a founder reviewing their own PR would likely miss entirely: do you patch each of the twelve instances individually, or do you build one shared, sanitized rendering utility and route all twelve through it?

Twelve individual patches are faster today and slower forever — the thirteenth unsafe instance, added next month by the same AI tool following the same pattern, comes back unescaped again. Building the shared utility takes longer this afternoon but removes the pattern as a future risk entirely, because new comment or text-rendering components can import the safe version instead of regenerating the unsafe one. For BuurtHulp, where user-submitted text is the entire product — it's a community help-request app, practically every screen has user text on it — the shared utility is the obvious call.

## 1:30 PM — Writing and Testing the Fix

The afternoon is building the sanitization utility, running it against all twelve original call sites, and confirming Puck's actual UI renders identically to before — same layout, same styling, same interactions Lovable built. The whole point is that nothing about what Puck's users see should change. Only what happens to the raw text underneath changes.

## 3:15 PM — Writing the Review Back

This is the part that matters most for a non-security-background founder: translating twelve files of unescaped input into something Puck can actually act on without a computer science degree. The note back to her explains it as, in effect, "anyone could have typed code into a comment box and had it run in another user's browser — we've closed that everywhere it existed and made sure it can't come back the same way." No jargon walls. Just what was wrong, why it mattered, and what changed.

Behind this one PR is Manifera's broader team of 120+ engineers, and reviews like this one typically run through our Amsterdam office at Herengracht 420, working alongside founders across Europe building with Lovable, Bolt, Cursor, and v0. If you want to see how a single review like this fits into the full production path, our [process page](https://launchstudio.eu/en/#process) lays out what comes before and after. For a look at the same review discipline applied to larger, longer-running codebases, Manifera's [portfolio](https://www.manifera.com/portfolio/) shows how it scales past a single founder's app.

## 5:40 PM — PR Approved, With Homework

By end of day, Puck's comment threads and request-detail page are approved and merged — with the sanitization fix included, not just flagged for her to handle herself. The queue still has one more PR waiting for tomorrow morning. This is, more or less, every day.

## Real example

### An AI-Native Founder in Action: BuurtHulp's Repeated Pattern

Puck Willemsen built BuurtHulp so neighbors in Haarlem could post and respond to small help requests — moving furniture, watering plants while someone's away, that kind of thing. She'd built the comment and request-detail features in Lovable and felt good enough about them to plan a public launch within the week.

The review described above found unescaped user input across twelve separate files — comments, request descriptions, and profile fields — all following the same unsafe rendering pattern Lovable had generated independently across different parts of the app. Left as-is, any user could have submitted a comment containing code that would execute in another BuurtHulp user's browser, a serious risk for an app whose entire purpose is connecting strangers in the same neighborhood.

Rather than patching all twelve spots as one-off fixes, our engineers built a single shared sanitization utility, routed every existing call site through it, and confirmed Puck's UI looked and behaved exactly as Lovable had built it. Any future text-rendering component she or her AI tool builds now inherits the safe pattern by default.

**Result:** BuurtHulp launched publicly on schedule with the entire class of unescaped-input risk closed, not just the one instance that happened to get noticed first.

> *"I had no idea the same mistake was sitting in twelve different places. I thought I was reviewing one feature. Turns out I was reviewing a pattern."*
> — **Puck Willemsen, Founder, BuurtHulp (Haarlem)**

**Cost & Timeline:** €1,050 (repo-wide input sanitization review and fix) — completed in 4 business days.

---

## Frequently Asked Questions

### Why did the same unsafe pattern show up in twelve files instead of just one?

AI coding tools like Lovable often regenerate similar-looking components independently across sessions, reproducing the same unsafe pattern each time rather than reusing a single safe implementation.

### Does a full pattern-wide review take much longer than a one-file fix?

It takes longer on the day it happens — Puck's review took about a day rather than an hour — but it removes the risk of the same issue reappearing in future features, which a one-off patch doesn't.

### Do LaunchStudio's engineers rewrite the founder's frontend during a review like this?

No — reviews like Puck's are scoped to fixing the underlying logic and rendering safety, leaving the UI exactly as it was built in Lovable, Bolt, Cursor, or v0.

### Where is the team doing these pull request reviews based?

Reviews for European founders like Puck typically run through LaunchStudio's Amsterdam office, backed by Manifera's broader 120+ engineer team.

### What's the actual output of a review like this — just a list of bugs?

No — the output is a merged, working fix along with a plain-language explanation of what was wrong and why, not just a flagged list for the founder to resolve alone.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Why did the same unsafe pattern show up in twelve files instead of just one?", "acceptedAnswer": { "@type": "Answer", "text": "AI coding tools like Lovable often regenerate similar-looking components independently across sessions, reproducing the same unsafe pattern each time rather than reusing one safe implementation." } },
    { "@type": "Question", "name": "Does a full pattern-wide review take much longer than a one-file fix?", "acceptedAnswer": { "@type": "Answer", "text": "It takes longer on the day it happens, but it removes the risk of the same issue reappearing in future features, which a one-off patch does not." } },
    { "@type": "Question", "name": "Do LaunchStudio's engineers rewrite the founder's frontend during a review like this?", "acceptedAnswer": { "@type": "Answer", "text": "No, reviews are scoped to fixing underlying logic and rendering safety, leaving the UI exactly as built in Lovable, Bolt, Cursor, or v0." } },
    { "@type": "Question", "name": "Where is the team doing these pull request reviews based?", "acceptedAnswer": { "@type": "Answer", "text": "Reviews for European founders typically run through LaunchStudio's Amsterdam office, backed by Manifera's broader 120+ engineer team." } },
    { "@type": "Question", "name": "What's the actual output of a review like this?", "acceptedAnswer": { "@type": "Answer", "text": "A merged, working fix along with a plain-language explanation of what was wrong and why, not just a flagged list for the founder to resolve alone." } }
  ]
}
</script>
