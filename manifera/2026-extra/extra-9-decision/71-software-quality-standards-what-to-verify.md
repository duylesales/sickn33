---
title: "Software Quality Standards: What to Verify Before You Sign a Deal"
keywords: "software quality, QA process vendor evaluation, code review standards, offshore software development team, software defect rate"
buyer_stage: "Decision"
target_persona: "CTO"
---

# Software Quality Standards: What to Verify Before You Sign a Deal

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Software Quality Standards: What to Verify Before You Sign a Deal",
  "description": "A technical deep-dive for CTOs evaluating a software vendor's QA architecture, code review discipline, and defect benchmarks before signing a contract, with a checklist for what to verify in writing.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-08-25",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/software-quality-standards-what-to-verify"}
}
</script>

Sixty percent. That is roughly the share of enterprise software defects, according to industry defect-tracking studies cited by testing bodies like the QA Research Institute, that are traced back not to code itself but to requirements that were never properly reviewed before development started. If you are three vendor proposals deep into a procurement process, that number should worry you more than any pricing sheet. A contract can promise "rigorous testing" in a single bullet point, but software quality is not a marketing claim — it is an architecture, a set of gates, and a body of evidence you can ask to see before you sign anything.

This is the deep-dive most RFP processes skip. Sales decks talk about "quality-first culture." They rarely show you the actual test pyramid, the code review checklist, or the defect-escape numbers from a comparable past project. As a CTO or VP of Engineering staring down a multi-month, six-figure commitment, you need to interrogate software quality the way you'd interrogate a system architecture diagram: layer by layer, with evidence at each level.

The problem is that "quality" is one of the easiest words to say and one of the hardest to verify from a proposal document alone. Every vendor shortlisted for a serious engagement will claim strong QA. What separates a vendor who will actually protect your release schedule from one who will quietly let defects pile up until the deadline forces a rushed ship, is whether their software quality process is documented, measurable, and enforced by tooling rather than by good intentions. That distinction is exactly what this article is built to help you surface before a signature makes it expensive to find out the hard way.

## The Software Quality Architecture Vendors Rarely Show You

Every serious engineering organization structures testing as a pyramid, not a flat list. At the base sit unit tests — fast, numerous, cheap to run on every commit. In the middle sit integration and API tests, verifying that services talk to each other correctly. At the top sit a smaller number of end-to-end and exploratory tests that simulate real user journeys. When a vendor's software quality process is healthy, this pyramid is visible in their CI/CD pipeline configuration, not just described in a slide.

Ask to see the actual test suite composition for a comparable project: how many unit tests, what percentage of the codebase they cover, and how often the suite runs. A vendor with real software quality discipline will use tools like Jest, Mocha, or Playwright as part of an automated gate — meaning a pull request cannot merge until the suite passes. A vendor without it will describe testing as something that happens "before release," which is a euphemism for testing too late to catch anything cheaply.

Ask specifically what breaks the build. If the answer is "failing tests block the merge," that is architecture. If the answer is "the QA team files a ticket afterward," that is a checklist pretending to be a pipeline.

There is also a question of ownership that most buyers forget to ask: who writes the tests, and when? In a mature software quality architecture, developers write unit tests alongside the feature code itself, as part of the same pull request — not as a separate task handed to a QA engineer days later. When test-writing is deferred, coverage becomes an afterthought squeezed in before a deadline, and the pyramid inverts: a handful of manual, end-to-end checks trying to compensate for a missing foundation. Ask the vendor directly whether developers or a separate QA function write the bulk of unit and integration tests, and how the two roles collaborate on test design for complex business logic. The answer tells you whether quality is embedded in the engineering culture or bolted on afterward as a compliance step.

## Code Review Standards: What "Peer Reviewed" Actually Means

Every vendor claims code review. Few can describe their review standard with any precision. A defensible code review process has three concrete components: a required second reviewer before merge, a documented checklist the reviewer works against, and a maximum time-to-review SLA so reviews don't rot in a queue for a week.

Here is what a real pull request gate typically enforces, and what you should ask a shortlisted vendor to confirm in writing:

- Minimum one approving review from a developer who did not write the code
- Automated linting and static analysis (SonarQube or equivalent) passing before human review starts
- A checklist covering security basics (input validation, secrets handling), test coverage on new logic, and adherence to agreed naming and architecture conventions
- No direct commits to the main branch — every change travels through a pull request

If a vendor cannot produce a sample pull request template or review checklist during due diligence, that is a signal, not an oversight. Teams with mature software quality practices document this because it is how they onboard new engineers quickly — the standard exists independent of any one senior developer's memory. This is one area where an [offshore software development team](https://www.manifera.com/services/offshore-software-development/) with a codified process actually outperforms an in-house team that relies on informal, tribal-knowledge review habits.

There is a subtler test you can run during the sales process itself: ask two different people at the vendor — a sales lead and a technical lead — to describe the code review standard independently. If the descriptions match down to specifics like SLA turnaround time and checklist content, the standard is real and operational. If the sales lead gives you a confident but vague answer and the technical lead gives you a different, more hedged one, you are looking at a process that exists on paper for some teams but not others. This single cross-check has saved more than one buyer from discovering, three sprints in, that "code review" meant something different to the team actually writing their code than it did to the person who sold the contract.

## The Benchmark Numbers That Separate Real QA From Theater

Words like "thorough" and "rigorous" are not benchmarks. Numbers are. Before you sign, ask a vendor for figures from a past, comparable engagement on these four metrics:

1. **Defect escape rate** — the percentage of bugs found in production versus caught pre-release. Healthy engagements report escape rates in the low single digits; anything above 10-15% suggests testing happens too late in the cycle.
2. **Test coverage percentage** — not a vanity number alone, but paired with which parts of the codebase are covered. 80% coverage on business-critical logic matters more than 95% coverage that's mostly boilerplate.
3. **Mean time to detect and mean time to resolve** — how quickly a defect is caught after introduction, and how quickly it's fixed once reported.
4. **Deployment frequency without rollback** — a proxy for whether the pipeline's quality gates are actually trustworthy, or whether releases are routinely reverted.

Gartner has repeatedly flagged inconsistent QA measurement as one of the recurring root causes behind failed outsourcing relationships — not a skills gap, but a visibility gap. Vendors who can produce these four numbers from a reference project, unprompted, are demonstrating that quality is measured as routine practice rather than assembled for your benefit during the sales cycle.

It's worth noting what these numbers should not be used for: a single blended score to rank vendors against each other on a spreadsheet. Context matters enormously. A vendor building a payments platform with a 3% defect escape rate is doing meaningfully harder work than a vendor building a marketing microsite with the same figure, because the surface area for subtle logic errors in a payments flow is much larger. Ask for the benchmark numbers alongside the type of system they were measured on, and weight your evaluation accordingly. A vendor who volunteers that context without being asked is telling you something about how carefully they think about quality measurement in general — it is rarely something a vendor gaming the numbers bothers to mention.

## Five Questions to Ask About a Vendor's QA Process Before You Sign

Use these verbatim in your next vendor call, and insist on specific answers rather than general reassurance:

1. "Walk me through what happens between a developer finishing a feature and it reaching production — every gate, in order."
2. "What percentage of your last three projects shipped with a documented defect-escape rate under 5%?"
3. "Show me a sample QA test plan from a project similar in scope to ours."
4. "What testing tools and frameworks does the team use day-to-day, and who owns test maintenance as the codebase grows?"
5. "If a critical bug reaches production, what is your documented incident response and root-cause process?"

A vendor's hesitation, vagueness, or redirection to generic marketing language on any of these five is more diagnostic than anything in their proposal document.

## Red Flags That Show Up Before the Contract Is Signed

Certain patterns in a vendor's due-diligence behavior correlate strongly with software quality problems that surface later. Watch for a proposal that mentions testing only as a line item near the bottom of a Gantt chart, positioned as a phase that happens after development rather than throughout it — that sequencing usually reflects how the vendor actually thinks about QA, not just how they scheduled the document. Watch for reference clients who, when you ask about defect rates or post-launch stability, respond only in generalities about "great communication" without mentioning technical outcomes; strong client references for engineering quality usually include at least one specific number or incident they can describe concretely.

Also watch for a vendor who cannot explain how their QA process would need to adapt to your specific system — a payments integration, a healthcare data pipeline, a high-traffic consumer app each demand a different balance of automated coverage, manual exploratory testing, and compliance-specific checks. A generic answer that would apply equally to any client's project is a sign the QA process is a marketing slide rather than a living discipline shaped by real project experience.

## Where Communication and Track Record Fit Into the Quality Equation

Software quality is not purely a technical discipline — it is also a communication discipline. A defect that is caught but not clearly reported, with reproduction steps and severity classification communicated in a shared language, causes as much delay as a defect that was never caught at all. This is where Manifera's development teams lean on strong English-language communication and consistent working-hour overlap with European clients, so that QA findings are documented clearly and escalated quickly rather than lost in translation across time zones.

That discipline is easier to sustain when it has been proven across many engagements rather than assembled for one deal. Manifera has delivered more than 160 projects for over 120 clients across a decade of operation, and the QA processes described above — pull request gates, defect-escape tracking, documented test plans — are standard practice across those engagements, not a one-time pitch. You can review how this operational discipline is structured on our [way of working page](https://www.manifera.com/about-us/our-way-of-working/), and see the specific testing and DevOps tooling involved on our [technology stack page](https://www.manifera.com/about-us/manifera-technologies/).

This is also where the working relationship between European engagement management and the engineering team doing the actual testing matters more than buyers often expect. A defect report that arrives without severity classification, reproduction steps, or a clear owner costs your team hours of back-and-forth to interpret — and those hours compound across a multi-month engagement. Consistent overlap between GMT+7 development hours and CET business hours means a defect flagged in the morning can be triaged, clarified, and often fixed before your own team's next standup, rather than sitting in a queue for a full day while questions travel across time zones.

## Making the Final Call

Before you sign, insist on seeing the pyramid, not just hearing about it. Ask for the four benchmark numbers, not the adjectives. Request a sample code review checklist and a real defect-escape figure from a comparable project. Push past the red flags outlined above — vague reference calls, testing tucked into the tail end of a project timeline, generic answers about compliance-specific QA needs — because each one is cheap to spot now and expensive to discover after the statement of work is signed.

Software quality that survives contact with a live production environment is built from documented gates and enforced habits, not from a single slide in a sales deck. Any vendor confident in their process will hand you the pull request checklist, the defect-escape numbers, and the test plan without hesitation, because none of it was assembled for your benefit — it's simply how they already work.

Talk to one of our senior architects about your specific quality requirements before you finalize any vendor decision — we'll walk you through our actual QA architecture, not a summary of it.

## Frequently Asked Questions

### What software quality metrics should I request from a vendor before signing a contract?
Ask for defect escape rate, test coverage percentage on business-critical code, mean time to detect and resolve defects, and deployment frequency without rollback. These four numbers, sourced from a past comparable project, tell you more than any general description of "rigorous testing."

### How do I verify a vendor's code review process is real and not just a claim?
Ask for a sample pull request template or review checklist, confirm whether a second reviewer approval is mandatory before merge, and ask what automated checks (linting, static analysis) run before human review. A vendor with a documented, enforced standard can produce these artifacts on request.

### What is a healthy defect escape rate for a software vendor?
Most mature QA processes keep defect escape rates — bugs discovered in production versus pre-release — in the low single digits, often under 5%. Rates consistently above 10-15% suggest testing is happening too late in the development cycle to catch issues cheaply.

### Does an offshore development team affect software quality compared to an in-house team?
Not inherently — quality depends on process discipline, not location. A codified pull request gate, automated test suite, and documented QA standard travel with the team regardless of geography, and in many cases an offshore team with a formalized process outperforms an in-house team relying on informal review habits.

### Should software quality standards be written into the vendor contract itself?
Yes. Defect-escape thresholds, code review requirements, and reporting cadence for QA metrics should appear as measurable terms in the statement of work, not just described verbally during sales conversations, so both sides have an enforceable reference point after the contract is signed.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What software quality metrics should I request from a vendor before signing a contract?",
      "acceptedAnswer": {"@type": "Answer", "text": "Ask for defect escape rate, test coverage percentage on business-critical code, mean time to detect and resolve defects, and deployment frequency without rollback. These four numbers, sourced from a past comparable project, tell you more than any general description of 'rigorous testing.'"}
    },
    {
      "@type": "Question",
      "name": "How do I verify a vendor's code review process is real and not just a claim?",
      "acceptedAnswer": {"@type": "Answer", "text": "Ask for a sample pull request template or review checklist, confirm whether a second reviewer approval is mandatory before merge, and ask what automated checks (linting, static analysis) run before human review. A vendor with a documented, enforced standard can produce these artifacts on request."}
    },
    {
      "@type": "Question",
      "name": "What is a healthy defect escape rate for a software vendor?",
      "acceptedAnswer": {"@type": "Answer", "text": "Most mature QA processes keep defect escape rates in the low single digits, often under 5%. Rates consistently above 10-15% suggest testing is happening too late in the development cycle to catch issues cheaply."}
    },
    {
      "@type": "Question",
      "name": "Does an offshore development team affect software quality compared to an in-house team?",
      "acceptedAnswer": {"@type": "Answer", "text": "Not inherently — quality depends on process discipline, not location. A codified pull request gate, automated test suite, and documented QA standard travel with the team regardless of geography."}
    },
    {
      "@type": "Question",
      "name": "Should software quality standards be written into the vendor contract itself?",
      "acceptedAnswer": {"@type": "Answer", "text": "Yes. Defect-escape thresholds, code review requirements, and reporting cadence for QA metrics should appear as measurable terms in the statement of work, not just described verbally during sales conversations."}
    }
  ]
}
</script>
