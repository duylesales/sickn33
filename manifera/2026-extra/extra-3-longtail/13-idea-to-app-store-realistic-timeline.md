---
title: "A Realistic Week-by-Week Map From First Sketch to App Store Approval"
keywords: "mobile app development, app to build, mobile application development, apps to develop"
buyer_stage: "Consideration"
target_persona: "B"
---

# A Realistic Week-by-Week Map From First Sketch to App Store Approval

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "A Realistic Mobile App Development Timeline From Idea to App Store",
  "description": "A week-by-week breakdown of how a standard mobile app moves from initial idea through discovery, design, development, QA, and app store submission.",
  "step": [
    { "@type": "HowToStep", "name": "Discovery and requirements (Weeks 1-3)", "text": "Stakeholder interviews, user flow mapping, and technical constraint identification before any design or code begins." },
    { "@type": "HowToStep", "name": "Design and prototyping (Weeks 3-6)", "text": "Wireframes, a design system, and a clickable prototype validated against real user flows." },
    { "@type": "HowToStep", "name": "Core development (Weeks 6-14)", "text": "Sprint-based building of frontend, backend, and integrations, with demoable increments every two to three weeks." },
    { "@type": "HowToStep", "name": "QA and device testing (Weeks 12-15, overlapping development)", "text": "Cross-device, cross-OS-version testing running in parallel with the final development sprints." },
    { "@type": "HowToStep", "name": "App store submission (Weeks 15-17)", "text": "Preparing store assets, submitting for Apple and Google review, and addressing any rejection feedback." },
    { "@type": "HowToStep", "name": "Post-launch stabilization (Weeks 17-19)", "text": "Monitoring real usage, fixing issues surfaced by actual users, and handing off into ongoing maintenance." }
  ]
}
</script>

A founder asked how long their app would take gets an answer somewhere between "eight weeks" and "eight months," depending entirely on which vendor is answering, how much genuine confidence sits behind their number, and what they're quietly not counting. Here's what a realistic timeline actually looks like for a standard consumer or B2B companion app, mapped week by week.

## Weeks 1-3: Discovery and Requirements

This is the stage nobody sees and everybody underestimates. Stakeholder interviews, competitive research, user flow mapping, and identifying technical constraints — like existing systems the app needs to connect to — happen here, before a single wireframe exists. A rushed discovery phase is the single biggest predictor of scope disputes later in the timeline, and the biggest source of exactly the kind of unknown unknown Hofstadter's Law describes.

## Weeks 3-6: Design and Prototyping

Wireframes evolve into a design system and a clickable prototype, tested against the user flows identified in discovery. This is also when technical architecture decisions get made in parallel — decisions largely invisible to the founder but critical to whether the app can scale past its first few thousand users without a rebuild.

## Weeks 6-14: Core Development

The longest stage, broken into two-to-three-week sprints, each producing a working, demoable increment rather than one long stretch of invisible progress. A standard-complexity consumer app (auth, profiles, moderate API integration, push notifications) typically needs 8-10 weeks of development; a more complex marketplace or real-time app can run 14-18 weeks or more.

## Weeks 12-15: QA and Device Testing (Overlapping Development)

Real QA, on a well-run project, doesn't wait until development is "finished" — it runs in parallel with the final development sprints, testing earlier-completed features across a device matrix while later features are still being built. Compressing this into a few days at the end, rather than running it in parallel throughout, is the most common way timelines quietly go wrong.

## Weeks 15-17: App Store Submission

Apple's review process typically takes 24-48 hours but can extend well past a week if the app is rejected for guideline issues and needs resubmission — a common occurrence for first-time submissions that didn't account for specific store requirements (privacy disclosures, permission justifications, metadata accuracy) early enough. Google Play review is generally faster but not instantaneous either, and both platforms' review timelines sit largely outside a development team's direct control regardless of how well the app itself is built.

## Weeks 17-19: Post-Launch Stabilization

Real usage surfaces bugs and edge cases no amount of pre-launch testing fully replicates. A defined two-to-four-week stabilization window — actively monitoring, triaging, and fixing what surfaces — is standard for a well-run launch, not a sign that something went wrong.

## Why "Eight Weeks" Quotes Usually Mean Something Else

A vendor quoting eight weeks for a standard-complexity app is either quoting only the development stage (excluding discovery, dedicated QA, and stabilization), or planning to compress those other stages into gaps that don't really exist. The full realistic range for a standard app, done properly, runs 16-19 weeks — closer to four months than two.

## Why "Padding the Estimate" Doesn't Actually Fix This

Douglas Hofstadter's famous, self-referential observation from his 1979 book "Gödel, Escher, Bach" — "it always takes longer than you expect, even when you take into account Hofstadter's Law" — has become a durable piece of software industry folklore precisely because it names something real: adding a buffer to an estimate doesn't fix the underlying problem, because the estimate was systematically optimistic to begin with, and a fixed percentage buffer applied to a systematically optimistic number is still systematically optimistic, just by a smaller margin. Teams that respond to chronic timeline slippage by simply padding the next estimate by 20% often find themselves slipping past the padded number too, for the same underlying reason the original estimate was wrong.

The more durable fix isn't a bigger buffer — it's addressing what actually makes software timelines resistant to accurate estimation in the first place: unknown unknowns that only surface once work is underway. A discovery phase reduces some of this, converting unknown unknowns into known risks that can be estimated properly. But some genuine uncertainty survives even good discovery, particularly around third-party integrations and platform review processes outside a team's direct control — which is exactly why the realistic ranges in this article are ranges, not single numbers, and why a serious project plan should show a range with an explicit confidence level rather than a single deceptively precise date.

This is also why the specific failure mode described earlier — a vendor quoting eight weeks for a project that realistically needs seventeen — is worse than an honest range would be, even though the honest range sounds less reassuring in a sales conversation. A wrong single number isn't more useful than an honest range; it's less useful, because it fails the exact test Hofstadter's observation predicts it will fail, just later, when the founder has already built external commitments — a launch event, an investor update, a marketing campaign — around a date that was never realistic to begin with.

## Manifera's Approach: A Timeline That Holds

- **Amsterdam (Governance/Timeline Integrity):** Dutch project leads scope all six stages explicitly into the initial timeline, so the number a founder is given at kickoff is the number that holds through app store approval.
- **Vietnam (Execution/Parallel Velocity):** The engineering pod runs QA in parallel with late-stage development rather than sequentially after it, keeping the realistic 16-19 week range achievable without compressing any individual stage.

This is Dutch Management × Vietnamese Mastery applied to timeline honesty itself: European planning discipline paired with delivery speed that comes from genuine parallelization, not from quietly skipping stages. Explore [mobile app development](https://www.manifera.com/services/mobile-app-development/) timelines at Manifera.

## Case Study: A Helsinki Marketplace's On-Time Launch

Revonta, a Helsinki-based local-services marketplace, had been quoted eight weeks by a previous vendor for a comparable app — a timeline that stalled in week 10 with QA barely started and no app store assets prepared.

Manifera's Amsterdam team scoped the full project at 17 weeks from the outset, including three weeks of discovery and QA running in parallel with the final four development sprints. The Vietnam pod delivered on that 17-week timeline, with the app approved on first App Store submission because store requirements had been addressed during design, not discovered during submission.

> *"The honest 17-week number felt worse to hear than the dishonest 8-week number. It was the only one that turned out to be true."*
> — **Founder, Revonta**

Revonta's founder has since adopted the same range-with-confidence-level format for internal planning conversations with investors, presenting a realistic window rather than a single date, and reports that stakeholders have responded better to an honest range than they ever did to a confident but repeatedly missed single number.

## Reading a Timeline's Confidence Level, Not Just Its Number

A useful habit borrowed directly from Hofstadter's observation: ask any vendor not just for a date, but for how confident they are in it and why. A discovery-based estimate for a well-understood feature set can carry genuine confidence, because the unknowns have been substantially reduced before the number was committed to. A timeline for a project still carrying open questions about a critical third-party integration or an unresolved app store policy question should carry visibly less confidence, reflected honestly in a wider range rather than false precision.

This distinction matters because it changes what a founder should do with the number once they have it. A high-confidence estimate can reasonably anchor external commitments — a launch event, a press date, an investor update. A low-confidence estimate should not, no matter how much organizational pressure exists to have a firm date to share. Committing external plans to a number a vendor has already flagged as uncertain is asking Hofstadter's Law to prove itself again, on a schedule the founder no longer controls once the commitment is public.

## Realistic Timeline by App Complexity

| App Complexity | Discovery | Development | QA + Submission | Total |
|---|---|---|---|---|
| Simple utility app | 1-2 weeks | 5-7 weeks | 2-3 weeks | 8-12 weeks |
| Standard consumer app | 2-3 weeks | 8-10 weeks | 3-4 weeks | 13-17 weeks |
| Complex marketplace/real-time app | 3-4 weeks | 14-18 weeks | 4-6 weeks | 21-28 weeks |

## Planning Your Own Timeline

Ask any vendor to break their quoted timeline down by these six stages before accepting it, and ask how confident they are in each stage specifically — a single undifferentiated number is the easiest place for a timeline to quietly go wrong, and the easiest place for genuine uncertainty to hide behind false precision. [Get a custom team proposal within 48 hours](https://www.manifera.com/contact-us/), timeline included.

## Frequently Asked Questions

### (Scenario: founder comparing an 8-week quote to a 17-week quote for a similar app) Why would two vendors quote such different timelines for a similar app?

The shorter quote is almost always excluding stages like discovery, dedicated QA, or stabilization — or planning to compress them under deadline pressure. Ask both vendors to break the timeline down stage by stage before comparing.

### (Scenario: founder wanting to launch faster) Can I compress the discovery phase to launch faster?

You can shorten it for a very simple, well-understood app, but compressing discovery for a complex project usually costs more time later in scope disputes and rework than it saves upfront.

### (Scenario: founder worried about app store rejection delays) How much time should I budget for app store approval?

Budget 1-2 weeks for a smooth first submission, but 3-4 weeks if this is your first submission, since first-time rejections for guideline issues are common and each resubmission cycle adds days.

### (Scenario: founder trying to understand why QA overlaps development) Why does QA start before development is finished?

Because testing earlier-completed features while later ones are still being built catches issues sooner and avoids compressing all testing into a rushed period at the very end of the timeline.

### (Scenario: founder planning launch marketing around a release date) How far in advance should I plan a launch date around this timeline?

Treat the stabilization window as part of the timeline before a "hard" public launch push — plan marketing around the end of stabilization, not the initial app store approval date, since that's when the app is genuinely ready for scale.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: founder comparing an 8-week quote to a 17-week quote for a similar app) Why would two vendors quote such different timelines for a similar app?", "acceptedAnswer": { "@type": "Answer", "text": "The shorter quote is almost always excluding stages like discovery, dedicated QA, or stabilization, or planning to compress them under deadline pressure." } },
    { "@type": "Question", "name": "(Scenario: founder wanting to launch faster) Can I compress the discovery phase to launch faster?", "acceptedAnswer": { "@type": "Answer", "text": "You can shorten it for a very simple app, but compressing discovery for a complex project usually costs more time later in scope disputes and rework." } },
    { "@type": "Question", "name": "(Scenario: founder worried about app store rejection delays) How much time should I budget for app store approval?", "acceptedAnswer": { "@type": "Answer", "text": "Budget 1-2 weeks for a smooth submission, but 3-4 weeks if it's your first, since first-time rejections for guideline issues are common." } },
    { "@type": "Question", "name": "(Scenario: founder trying to understand why QA overlaps development) Why does QA start before development is finished?", "acceptedAnswer": { "@type": "Answer", "text": "Testing earlier-completed features while later ones are still being built catches issues sooner and avoids compressing all testing into a rushed final period." } },
    { "@type": "Question", "name": "(Scenario: founder planning launch marketing around a release date) How far in advance should I plan a launch date around this timeline?", "acceptedAnswer": { "@type": "Answer", "text": "Plan marketing around the end of the stabilization window, not the initial app store approval date, since that's when the app is genuinely ready for scale." } }
  ]
}
</script>
