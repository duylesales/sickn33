---
title: "Web Application Development Vendors: Test Code Quality Before Signing"
keywords: "web application development, code quality testing, vendor technical due diligence, software vendor evaluation, custom software development"
buyer_stage: "Decision"
target_persona: "CTO"
---

# Web Application Development Vendors: Test Code Quality Before Signing

What if the demo that just impressed your entire leadership team was built by a completely different team than the one who'll actually staff your project? It happens more often than vendors admit, and by the time a CTO discovers the gap, the contract is signed, the deposit is spent, and the sprint velocity has already collapsed. If you're down to a shortlist of **web application development** vendors and about to pick one, the pitch deck and the portfolio site have already done their job. What they haven't shown you is whether the code underneath will hold up in eighteen months, under load, with three more developers added to the team.

This is the gap most technical due diligence misses. Sales engineers walk you through architecture diagrams. Account managers share client logos. Almost nobody asks to see an actual pull request, a real test suite, or a static analysis report from a comparable project. That's the evaluation you need to run before signing, and it takes less time than most procurement teams assume.

## Why Code Quality Testing Belongs in Your Final Decision

Most CTOs evaluate web application development vendors on three axes: cost, timeline, and communication. Those matter, but they're lagging indicators. Code quality is the leading indicator of everything that happens after go-live — your maintenance cost, your ability to onboard new engineers, your incident rate, and how painful your next feature request will be to ship. A vendor that writes clean, tested, well-documented code will cost more per hour and less per feature over a two-year horizon. A vendor that ships fast and skips tests will look cheaper in month one and considerably more expensive in month twelve, once the technical debt compounds.

The problem is that code quality is invisible in a sales process unless you go looking for it. A finished web app looks the same in a browser whether it was built with disciplined test coverage or duct-taped together to hit a deadline. The only way to tell the difference is to inspect what's underneath, and that means asking for artifacts most vendors don't volunteer.

There's also a compounding effect that most procurement checklists miss entirely. Technical debt in a web application doesn't grow linearly — it grows the way interest does on an unpaid balance. A shortcut taken in month two to hit a sprint deadline might cost an extra day of rework in month four. By month twelve, that same shortcut, now tangled with a dozen other shortcuts and dependent features built on top of it, can cost weeks. Vendors who understand this dynamic build in the discipline early, even when it slows the first few sprints, because they know the alternative is a client who churns after eighteen months of escalating maintenance bills. Vendors who don't understand it, or who are incentivized purely by fixed-bid delivery speed, will make the opposite trade every time — and you won't see the bill until it's your problem, not theirs.

## Common Excuses That Should Raise Your Guard

Every experienced technical evaluator has heard the same handful of deflections when asking to see real code. "That project is under NDA" is legitimate for client-identifying details but not for a sanitized code excerpt with names and business logic redacted — a vendor that can't produce even that has likely never organized their codebases well enough to extract one. "Our best engineers are all staffed right now" is a scheduling problem, not a reason to skip the pairing session entirely; a serious vendor will find thirty minutes within a week, not push you to sign first and meet the team later. "We use an agile process, so we don't have fixed documentation" conflates agile delivery with an excuse to skip documentation altogether, which are unrelated things — plenty of disciplined Scrum teams maintain excellent living documentation as part of their definition of done. None of these excuses are automatically disqualifying on their own, but a vendor that offers two or three of them in the same conversation is telling you, indirectly, what your first year with them will look like.

## Request a Representative Code Sample, Not a Cherry-Picked One

The single highest-leverage request you can make before signing is a sample of production code from a project similar in scope to yours — not the flagship case study everyone gets shown, but a codebase built by the specific engineers who would be assigned to your account. Ask explicitly for this distinction. Vendors that resist naming the assigned team, or that only offer to show you their "best" project, are signaling something worth noting.

Once you have a sample, look for four concrete things:

1. **Test coverage percentage and test quality.** A coverage number above 70% on business logic is a reasonable baseline for a production web application; below 40% is a red flag regardless of what the sales team says about "moving fast." But coverage alone can be gamed — check whether tests actually assert meaningful behavior or just execute code without verifying outcomes.
2. **Static analysis results.** Run the sample (with permission) through a linter or static analyzer appropriate to the stack — ESLint for React/Node, PHPStan for Laravel, Roslyn analyzers for .NET. A clean or near-clean report tells you the team enforces standards; a wall of unaddressed warnings tells you they don't.
3. **Commit history discipline.** Small, atomic commits with descriptive messages indicate a team that reviews its own work carefully. A history of giant "final fixes" and "WIP" commits suggests code gets pushed under deadline pressure without review.
4. **Documentation embedded in the code.** Inline comments explaining *why*, not *what*, README files that actually onboard a new engineer, and API documentation that matches the current version of the code — these are cheap to produce and consistently skipped by vendors optimizing purely for delivery speed.

## Ask for a Live Pairing Session, Not Just a Code Review

A code sample tells you about past work. A live pairing session tells you about the team you're about to hire. Request thirty minutes where one of the assigned engineers walks through a real pull request from a recent sprint, live, answering questions about design decisions. This single request filters out vendors that staff sales calls with senior architects and then delegate actual delivery to junior contractors you've never met.

During the session, ask specifically why a particular approach was chosen over an alternative. A strong engineer can articulate the trade-off — performance versus maintainability, for example, or why they chose a particular state management pattern for a **web app development** project of similar complexity. A weak or evasive answer, or a hurried hand-off to someone else on the call, tells you more than any portfolio page.

## Benchmark Performance, Not Just Functionality

Functional correctness is table stakes; performance under realistic load is where quality differences actually surface. If the vendor has a staging environment for a comparable past project, ask for load test results — response times at 100, 500, and 1,000 concurrent users, database query times under load, and how the application degrades when it exceeds capacity. A team that has never run a load test on a production application is a team that hasn't been forced to confront the consequences of sloppy architecture. That's a meaningful signal for any application you expect to scale.

As Gartner has observed, technical due diligence on outsourced software delivery is one of the most under-invested steps in the vendor selection process, precisely because the cost of skipping it doesn't show up until well after the contract is signed. The vendors who welcome this level of scrutiny are, almost by definition, the ones with nothing to hide.

It's worth being specific about what "realistic load" means for your application, because generic benchmarks are close to useless. A vendor might proudly report that their application handled 5,000 concurrent users in a synthetic test, but if that test used uniform, cached requests rather than the mixed read-write traffic pattern your actual users generate, the number tells you almost nothing. Ask instead for a benchmark that approximates your real usage: if you're building an internal dashboard for 200 employees, ask how the app performs when 40 of them run the same complex report simultaneously at 9 a.m. If you're building a customer-facing portal, ask about database query time under load once the underlying tables have millions of rows, not the few hundred used in a demo environment. The specificity of the vendor's answer is itself diagnostic — a team that has genuinely load-tested production systems will answer in concrete milliseconds and percentiles; a team that hasn't will answer in vague reassurances about "modern infrastructure."

## Watch How the Vendor Handles Being Told They're Wrong

One evaluation technique many technical buyers overlook: during the live pairing session, gently push back on a design decision, even one you privately think is reasonable. Ask why they didn't use a different caching strategy, or why they chose a relational database over a document store for a particular feature. You're not testing whether their original decision was correct — you're testing how they respond to challenge. An engineer who can defend a decision with clear reasoning, or who can say "actually, you're right, we'd reconsider that on your project given your requirements," demonstrates the kind of collaborative technical maturity that makes a multi-month engagement go smoothly. An engineer who gets defensive, deflects to a manager, or simply repeats the original answer more loudly is showing you exactly how technical disagreements will be handled once you're a paying client with less leverage than you have today, mid-negotiation.

## What Manifera Does Differently

At Manifera, our approach to [web app development](https://www.manifera.com/services/web-app-develop/) is built around exactly the kind of transparency this evaluation demands: European project governance paired with Southeast Asian engineering talent, meaning the architects who scope your project in Amsterdam stay accountable for the code quality delivered by the engineering team in Ho Chi Minh City. We don't route prospective clients to a highlight reel — we'll walk you through an actual sprint, a real code review, and our QA process, because we've built our reputation on 160+ delivered projects that clients extend rather than replace.

We also structure our teams so that English-fluent engineers communicate directly with your technical stakeholders rather than through a layered account-management filter, which means the person answering your questions about test coverage is the same person who wrote the tests. If you're comparing us against other [offshore software development](https://www.manifera.com/services/offshore-software-development/) partners, ask every vendor on your shortlist for the same live pairing session — the contrast tends to be the clearest signal you'll get in the entire evaluation.

## Build a Simple Scoring Rubric Before the Calls

Don't leave this evaluation to gut feeling after the fact. Before your final round of vendor calls, build a one-page rubric scoring each finalist on: test coverage evidence, static analysis cleanliness, commit discipline, live pairing session quality, and load test transparency. Score each 1-5 and weight them according to what matters most for your specific application — a fintech dashboard should weight security and testing heavily; a marketing site can weight speed more. Score immediately after each call while details are fresh, and compare totals only after every finalist has been through the identical process. This removes recency bias, where the last vendor you spoke to unfairly benefits from being freshest in memory, and gives your final decision a defensible, auditable basis if leadership asks how you chose.

## Making the Final Call

By the time you've run these four checks — code sample review, live pairing session, performance benchmarking, and a scored rubric comparison — you'll have a materially clearer picture than anything a proposal document or reference call could offer. The vendors that pass this bar aren't just claiming quality; they're demonstrating it under conditions they don't fully control, which is the entire point of due diligence at the decision stage.

Talk to one of our senior architects about your specific code-quality challenge — we're happy to walk through our own process under exactly this kind of scrutiny before you sign anything.

## Frequently Asked Questions

### What test coverage percentage should I expect from a web application development vendor?
For business-critical logic, 70% or higher is a reasonable baseline for a production web application, though the number matters less than whether the tests verify meaningful behavior rather than simply executing code paths. Ask to see the actual test assertions, not just the coverage report, since a high percentage can still hide shallow tests.

### How do I know if a vendor will staff my project with the same engineers who built their portfolio examples?
Ask explicitly, in writing, for the names and backgrounds of the engineers who will be assigned to your account, and request a live session with those specific people before signing. Vendors that hesitate to name the assigned team or substitute a different presenter at the last minute are a meaningful warning sign.

### Is it reasonable to ask a web app development vendor for a live code review before signing a contract?
Yes, and most established vendors will accommodate a thirty-minute session without hesitation, since it's a standard part of technical due diligence. If a vendor resists or treats the request as unusual, that reluctance itself is useful information about how transparent their delivery process really is.

### What's the difference between reviewing code quality and reviewing a vendor's portfolio?
A portfolio shows finished, polished output selected specifically to impress; code quality review examines the underlying craftsmanship — test coverage, static analysis results, commit discipline, and documentation — that determines how expensive the application will be to maintain and extend after launch. Portfolios answer "can they build something that works," while code quality answers "will it still be healthy in eighteen months."

### How long does a proper technical due diligence process take before choosing a web application development vendor?
A focused evaluation — code sample review, one live pairing session, and a performance benchmark discussion — typically takes two to three hours spread across a single week per finalist, which is a small time investment relative to a multi-month, multi-thousand-euro engagement. Rushing this step to save a few hours is the single most common reason vendor relationships underperform expectations.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Web Application Development Vendors: Test Code Quality Before Signing",
  "description": "A technical due diligence guide for CTOs comparing web application development vendors, covering code sample review, live pairing sessions, static analysis, and performance benchmarking before signing a contract.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-08-21",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/web-application-development-vendor-code-quality-testing"}
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What test coverage percentage should I expect from a web application development vendor?",
      "acceptedAnswer": {"@type": "Answer", "text": "For business-critical logic, 70% or higher is a reasonable baseline for a production web application, though the number matters less than whether the tests verify meaningful behavior rather than simply executing code paths. Ask to see the actual test assertions, not just the coverage report, since a high percentage can still hide shallow tests."}
    },
    {
      "@type": "Question",
      "name": "How do I know if a vendor will staff my project with the same engineers who built their portfolio examples?",
      "acceptedAnswer": {"@type": "Answer", "text": "Ask explicitly, in writing, for the names and backgrounds of the engineers who will be assigned to your account, and request a live session with those specific people before signing. Vendors that hesitate to name the assigned team or substitute a different presenter at the last minute are a meaningful warning sign."}
    },
    {
      "@type": "Question",
      "name": "Is it reasonable to ask a web app development vendor for a live code review before signing a contract?",
      "acceptedAnswer": {"@type": "Answer", "text": "Yes, and most established vendors will accommodate a thirty-minute session without hesitation, since it's a standard part of technical due diligence. If a vendor resists or treats the request as unusual, that reluctance itself is useful information about how transparent their delivery process really is."}
    },
    {
      "@type": "Question",
      "name": "What's the difference between reviewing code quality and reviewing a vendor's portfolio?",
      "acceptedAnswer": {"@type": "Answer", "text": "A portfolio shows finished, polished output selected specifically to impress; code quality review examines the underlying craftsmanship that determines how expensive the application will be to maintain and extend after launch. Portfolios answer whether they can build something that works, while code quality answers whether it will still be healthy in eighteen months."}
    },
    {
      "@type": "Question",
      "name": "How long does a proper technical due diligence process take before choosing a web application development vendor?",
      "acceptedAnswer": {"@type": "Answer", "text": "A focused evaluation, including code sample review, one live pairing session, and a performance benchmark discussion, typically takes two to three hours spread across a single week per finalist, which is a small time investment relative to a multi-month engagement. Rushing this step is the most common reason vendor relationships underperform expectations."}
    }
  ]
}
</script>
