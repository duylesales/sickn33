---
Title: "Shipping a Big Change to Customers Who Depend on You"
Keywords: rolling out redesign to customers, breaking change communication saas, migrating customers new version, opt in beta period, change management small saas, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# Shipping a Big Change to Customers Who Depend on You

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Shipping a Big Change to Customers Who Depend on You",
  "description": "A redesign or restructure that customers have not asked for is the riskiest thing a small product can do. How to sequence it: who sees it first, how long both versions coexist, what to communicate and when, and the decision to abandon it if the evidence says so.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-05-11",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/shipping-a-big-change-to-customers-who-depend-on-you" }
}
</script>

There is a difference between adding a feature and changing something people already rely on. New features are optional; nobody is worse off if they ignore one. A redesigned workspace, a restructured navigation, or a changed data model reaches customers who had a working routine and did not ask for a new one, and for some of them your improvement is a Monday morning spent relearning software they had already learned.

This is not an argument against improving your product. It is an argument for treating a significant change as an operation with a sequence, rather than as a release — because the technical risk is only half of it, and the half founders underestimate is that a change customers experience as being done *to* them produces cancellations even when the new version is genuinely better.

## Establish What Must Not Break

Before any of it, write down what has to keep working, in the customer's terms: they can log in, find their existing records, complete the main task, and their integrations keep receiving data. Four or five statements.

This list does two jobs. It becomes your verification checklist at each stage of rollout, and it defines what would make you stop. Without it, the assessment of whether the rollout is going well drifts toward whether anyone has complained loudly, which is a much weaker signal.

Be specific about the data, too. A significant change often involves restructuring how records are stored, and the requirement is not merely that new records work — it is that every existing record remains correct and reachable. That is a backfill with verification, not a schema change, and it is the part most likely to produce a quiet disaster: a transformation that worked for 97% of records and silently mangled the rest.

## Sequence: Small, Willing, Reversible

The rollout order that works is the same as for any risky change, with one addition — the people who go first should have volunteered.

**Yourself**, on production, doing real work rather than a demonstration.

**Volunteers.** Announce the change is coming and ask who wants early access. The customers who put their hand up are collaborators rather than subjects, they report problems generously, and their feedback arrives before anything is irreversible. Five is plenty.

**A small share of accounts**, ideally chosen to include one large customer, since problems that only appear at volume will not surface among small ones.

**Everyone, with a way back.** The old version remains available for a stated period.

That last point is the one that changes outcomes most. A customer who can switch back to what they know does not panic; they use the old version, get their week's work done, and try the new one when they have time. Take away the option and the same customer's only recourse is to email you angrily or leave.

Keeping both versions running has a real cost — two paths to maintain, two sets of bugs — which is why the period should be defined and finite. Four to eight weeks is usually enough to be generous without becoming permanent.

## What to Say, and When

Three communications, and the first is the one most often skipped.

**Before.** Tell customers a change is coming, what it improves, roughly when, and that they will be able to switch back. This does more than manage expectations: it is the moment you learn who depends on something you did not know mattered. A customer replying "does this affect the CSV export we run every Monday?" has just told you something worth knowing while it is still cheap.

**At the moment they see it.** A short in-product note: what has changed, where the two or three things they used most have moved, and the link to switch back. Not a tour — a map. The most common complaint about redesigns is not that the new version is worse but that people cannot find things, and a short list of "X is now here" resolves most of it.

**After.** Ask, once, what is worse than before. Framed that way rather than "what do you think", because you already know what is better and the useful information is the friction you cannot see.

For anything affecting integrations or exported data, the notice period is not a courtesy. A customer whose script parses your export needs weeks and specifics, and finding out through breakage is how a technically successful rollout loses an account.

Making a large change safely — with the flag infrastructure, the verified backfill, and a working path back to the old version — is a well-defined piece of production engineering. LaunchStudio, backed by Manifera's 11+ years of production engineering, plans and executes changes of this kind on live products with customers depending on them. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Watch the Right Signals

During a rollout, the instinct is to watch for complaints. Complaints are a lagging and biased signal: most unhappy customers say nothing.

Better indicators, compared between the group on the new version and the group still on the old. **Task completion**: are people who start the main action finishing it at the same rate? A drop is the clearest evidence of a usability problem. **Time to complete it**, which will rise initially through unfamiliarity and should return to baseline within a fortnight; if it does not, the new version is genuinely harder. **The switch-back rate**, which is the most honest number available — customers voting with an action rather than an opinion. **Support volume and its content**, where a spike in "where is X" is navigation and a spike in "X is broken" is a defect.

Decide in advance what each would have to show for you to pause. A stated threshold — task completion falling by more than a fifth, or more than a quarter of customers switching back — turns a fraught judgement into a decision you can make calmly.

## Be Willing to Stop

The hardest part is that three months of work may produce something customers genuinely do not want, and the sunk cost makes it very difficult to see.

If the evidence says so, the options are to pause and fix specific problems, to keep both versions for longer while learning why, or to abandon it. Abandoning is expensive and it is sometimes correct — a change that measurably makes customers slower at their own work is not going to become good through persistence.

The intermediate outcome is more common and worth watching for: the new version is better for new customers and worse for experienced ones, because it optimises for learning rather than for speed once learned. That is a real and specific finding, and it usually points to keeping the new default while restoring the shortcuts and density that experienced customers had relied on.

## Real example

### The Redesign Nobody Could Switch Back From

Anouk Steenbergen ran Praktijkplan, a scheduling tool for physiotherapy practices, built in Cursor. After four months of work she replaced the appointment calendar with a redesigned version, deployed to all 140 practices on a Tuesday, with no way back.

The new calendar was, by most measures, better: cleaner, faster, and with a booking flow that tested well with new users. It also moved the day view — which experienced receptionists used constantly, several hundred times a day — behind an extra click, and changed a keyboard shortcut that long-standing customers had built their routine around.

Support volume went from about four messages a week to sixty in three days. Nothing was broken; people simply could not work at their previous speed and had no alternative. Two practices cancelled in the first fortnight and a third asked whether the old version could be restored, which it could not, since it had been removed from the code.

**Result:** the day view restored as the default and the keyboard shortcut reinstated, both within a week. The subsequent major change was rolled out behind a flag to nine volunteer practices, then 20% of accounts, then all, with the previous version available for six weeks and a switch-back rate that peaked at 8% and fell to under 1% by week three.

> "It was a better calendar and it made my customers slower at their jobs. Nobody could go back, so they had to either relearn everything that week or leave."
> — **Anouk Steenbergen, Founder, Praktijkplan**

**Cost & Timeline:** rollout infrastructure and staged migration process delivered in 3 business days.

## Frequently Asked Questions

### Should customers be able to switch back to the old version?

Yes, for a defined period of four to eight weeks. It converts a forced disruption into a choice, and the switch-back rate is the most honest measure of how the change is landing.

### Who should see a significant change first?

Volunteers. Announce it and ask who wants early access; the customers who put their hand up report problems generously and their feedback arrives while changes are still cheap.

### What should the announcement say?

What is changing, why, roughly when, and that a way back will exist. The replies are valuable in themselves, because they reveal dependencies you did not know customers had.

### How do I tell whether a redesign is working?

Compare task completion rate and time to complete between the new and old groups, watch the switch-back rate, and read support volume for whether it is navigation confusion or genuine defects. Complaints alone are lagging and biased.

### When should I abandon a change I have spent months on?

When the evidence shows customers are measurably slower or less successful at their own work and specific fixes have not resolved it. A common intermediate finding is that a change suits new customers and harms experienced ones, which points to restoring the shortcuts they relied on.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Should customers be able to switch back to the old version?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, for a defined four to eight week period. It converts forced disruption into a choice, and the switch-back rate is the most honest measure of how the change is landing." } },
    { "@type": "Question", "name": "Who should see a significant change first?", "acceptedAnswer": { "@type": "Answer", "text": "Volunteers. Announcing it and asking who wants early access produces collaborators who report problems generously while changes are still cheap." } },
    { "@type": "Question", "name": "What should the announcement say?", "acceptedAnswer": { "@type": "Answer", "text": "What is changing, why, roughly when, and that a way back will exist. The replies reveal dependencies you did not know customers had." } },
    { "@type": "Question", "name": "How do I tell whether a redesign is working?", "acceptedAnswer": { "@type": "Answer", "text": "Compare task completion and time to complete between groups, watch the switch-back rate, and read support volume for navigation confusion versus defects." } },
    { "@type": "Question", "name": "When should I abandon a change I have spent months on?", "acceptedAnswer": { "@type": "Answer", "text": "When customers are measurably slower or less successful and specific fixes have not helped. Often the finding is that it suits new customers and harms experienced ones." } }
  ]
}
</script>
