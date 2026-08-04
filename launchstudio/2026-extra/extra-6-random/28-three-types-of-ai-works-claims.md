---
Title: "The Three Types of 'AI Works' Claims — and Which One Actually Matters"
Keywords: ai works, it works claim, ai testing gap, role based testing
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# The Three Types of 'AI Works' Claims — and Which One Actually Matters

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Three Types of 'AI Works' Claims — and Which One Actually Matters",
  "description": "A three-category explainer breaking down what founders actually mean when they say their AI-built app 'works,' and why the gap between them causes silent production failures.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/three-types-of-ai-works-claims" }
}
</script>

Three founders can each say "my app works" and mean three completely different things, and none of them will realize the gap until something breaks in front of the wrong person. The phrase "ai works" gets used constantly in founder circles as if it's a single, stable claim. It isn't. It's actually three separate claims wearing the same four words, and only one of them is safe to build a business on.

## Type one: "it works for me"

This is the most common and the most dangerous version of the claim, precisely because it feels the most solid to the person making it. A founder builds a feature, clicks through it themselves a few times using their own account, watches it behave correctly, and concludes it works. What this actually proves is narrower than it sounds: the feature works for one specific person, using one specific account, testing one specific path through the app, on one specific occasion. It says nothing about what happens for a different user, a different account type, or a different sequence of actions. This type of "it works" is a starting point, not a conclusion.

## Type two: "it works for the people I've shown it to"

This is a meaningful step up — a handful of other people have now clicked through the app too, which surfaces problems the founder's own testing never would have. But it's still bounded by exactly who those people are and what they happened to try. If everyone who's tested the app so far has the same account type, the same use case, or the same general behavior pattern, this type of "it works" can look thorough while still having enormous blind spots. It feels more validated than type one because more humans were involved, but more humans testing the same narrow path isn't the same as testing a wider range of paths.

## Type three: "it works under conditions I haven't personally tried yet"

This is the only version of the claim that actually matters for a product handling real customers, and it's the hardest to achieve because it requires deliberately testing things nobody has a natural reason to try. What happens for a user type you don't personally have? What happens when someone does the steps out of the expected order? What happens under a permission level you never gave yourself? This type of "it works" isn't built by more casual clicking — it's built by structured testing designed to find the gaps between what's been tried and what's possible. It's also, not coincidentally, exactly the category of testing most AI-native founders skip, because it doesn't feel necessary until the moment it very obviously was.

## Why the gap between type one and type three stays invisible until it doesn't

The dangerous part of this whole framework is that types one, two, and three look identical from the outside. A founder confidently saying "it works" gives no signal about which of the three claims they actually mean, and often the founder themselves doesn't realize which type they're making. This is exactly the gap LaunchStudio's engineers are trained to look for during a production readiness review — not "does this work," but "which version of working has actually been verified, and what hasn't been touched at all." Manifera's team of 120+ engineers, with a hub in Singapore serving founders across the region, approaches every review by explicitly testing for what type three requires, since that's the only version that holds up once real customers with real account types and real usage patterns arrive.

If you've said "it works" about a feature recently and aren't sure which type you meant, that uncertainty is worth resolving before customers resolve it for you. [Send us your prototype link for free advice](https://launchstudio.eu/en/#contact) on which type of "it works" your app is actually operating under right now. Manifera's [web app development](https://www.manifera.com/services/web-app-develop/) team applies this same structured-testing discipline to enterprise products, where the cost of an undiscovered type-one claim is measured in a different order of magnitude.

## A Starter Checklist for Reaching Type Three on Your Own

Getting from "it works for me" to "it works under conditions I haven't personally tried" doesn't require a formal QA department or specialized tooling to start — it requires deliberately trying things you have no natural instinct to try, because your own use of your own app will never generate these test cases on its own. Here's a starting checklist that surfaces a meaningful share of the gap without outside help.

**Create a second account with a different role, and never touch your original one again for testing.** If your app has any concept of roles or permission levels, spin up a genuinely separate account at the most restricted level available and run your core flows exclusively from there. Whatever silently breaks is invisible from an admin account and often invisible from any account that happens to share your own permission level.

**Do the steps out of the expected order.** Click "confirm" before filling in every field. Go back a step using the browser's back button instead of the app's own navigation. Submit a form twice in quick succession. Founders naturally follow the path they designed; real users don't, and the app's behavior under an unexpected sequence is often untested by definition, because nobody designed a test for a sequence nobody expected.

**Try a boundary value on every numeric or date field.** Zero, a negative number, a date far in the past or future, a number far larger than any realistic input. These aren't edge cases in the dismissive sense — they're the specific inputs that separate "works for the values I tried" from "works for the values that are actually possible."

**Open the app in two browser tabs and act as two different users at once.** Book the same slot, edit the same record, or submit the same form from both tabs within seconds of each other. Concurrent actions are one of the most reliable sources of bugs that never appear in single-user testing, because a single person testing alone can't accidentally create a race condition.

**Let the network fail on purpose.** Most browsers let you throttle or disable the network connection through developer tools. Submit a form, then kill the connection mid-request, and see what the app tells the user. A silent failure with no feedback is a far worse experience than a clear error message, and it's a gap that a working demo, tested only under a stable connection, will never reveal.

**Ask someone who's never used the app to try it cold, with no guidance.** Not a friend who already knows how it's "supposed" to work — someone genuinely unfamiliar, watching what they naturally try first. Their first three actions are frequently the ones you'd never have tested yourself, precisely because you already know what the app expects.

Running through this list won't get you all the way to a genuine type-three claim — some gaps only surface under real usage volume or genuinely adversarial conditions a founder can't easily simulate alone. But it closes a meaningful share of the distance, and more importantly, it changes what "it works" means when you say it next: not a feeling based on your own comfortable path through the app, but a claim backed by at least a few conditions you deliberately tried to break.

## Real example

### An AI-Native Founder in Action: Jesse van Dam's Admin-Only App

Jesse van Dam, founder of MeldPunt, a municipal reporting app in Vlaardingen built with v0, told early stakeholders confidently that the app worked. What he meant, without fully realizing it, was type one — it worked for his own personal test account, which happened to have admin-level permissions from the start of development. He had never tested the app as any other account type, because he'd never needed to; admin access let him see and do everything, so nothing ever appeared broken to him.

The gap surfaced when a municipal employee tried to use the app with a standard, non-admin account. A role-based bug meant the reporting form silently failed to submit for any account type other than admin — no error message, no visible feedback, just a submission that appeared to go through and then vanished. Because Jesse's own testing had exclusively used the one account type that didn't trigger the bug, it had remained completely invisible through every round of his own verification.

LaunchStudio's engineers, brought in after the failure was reported, traced the issue to a permissions check that had been scoped correctly for admin accounts but never extended to handle standard roles, causing the submission logic to fail silently instead of returning a clear error. The fix involved correcting the role-based permission logic and adding structured testing across every account type MeldPunt would actually need to support, not just the one Jesse had used personally.

**Result:** MeldPunt's reporting form was fixed across all account types and re-tested under each role before being reintroduced to municipal staff, with no further submission failures reported.

> *"I said it worked and I believed it completely, because it always had — for me. I just never tested it as anyone else."*
> — **Jesse van Dam, Founder, MeldPunt (Vlaardingen)**

**Cost & Timeline:** €890 (role-based bug diagnosis, permission fix, and multi-role testing) — completed in 5 business days.

---

## Frequently Asked Questions

### What's the difference between the three types of "it works" claims?

Type one means it works for the founder's own account only. Type two means a small group of testers have tried it, still within a limited range of conditions. Type three means it's been deliberately tested under conditions the founder wouldn't naturally try themselves.

### Why is type three so hard to reach on your own?

Because it requires testing scenarios you have no personal reason to try — different account types, out-of-order actions, edge-case permissions — which don't reveal themselves through normal use of your own product.

### How do role-based bugs like Jesse van Dam's usually get discovered?

Usually by accident, when someone with a different account type or permission level uses the app for the first time and something silently fails that never failed for the founder.

### Does reaching type three require rebuilding the app?

No. It typically requires structured testing and targeted fixes to specific logic, as in MeldPunt's case, not a rebuild of the product itself.

### How does Manifera's team approach testing for this gap?

Manifera's engineers, including those based in Singapore, are trained to explicitly test across account types and conditions the founder hasn't personally tried, rather than accepting a single successful test as proof the feature works.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "What's the difference between the three types of \"it works\" claims?", "acceptedAnswer": { "@type": "Answer", "text": "Type one means it works for the founder's own account only. Type two means a small group has tried it within limited conditions. Type three means it's been deliberately tested beyond the founder's own use." } },
    { "@type": "Question", "name": "Why is type three so hard to reach on your own?", "acceptedAnswer": { "@type": "Answer", "text": "It requires testing scenarios you have no personal reason to try, like different account types or out-of-order actions." } },
    { "@type": "Question", "name": "How do role-based bugs like Jesse van Dam's usually get discovered?", "acceptedAnswer": { "@type": "Answer", "text": "Usually by accident, when someone with a different account type uses the app and something silently fails that never failed for the founder." } },
    { "@type": "Question", "name": "Does reaching type three require rebuilding the app?", "acceptedAnswer": { "@type": "Answer", "text": "No, it typically requires structured testing and targeted fixes rather than a full rebuild." } },
    { "@type": "Question", "name": "How does Manifera's team approach testing for this gap?", "acceptedAnswer": { "@type": "Answer", "text": "Manifera's engineers, including those based in Singapore, explicitly test across account types and conditions the founder hasn't personally tried." } }
  ]
}
</script>
