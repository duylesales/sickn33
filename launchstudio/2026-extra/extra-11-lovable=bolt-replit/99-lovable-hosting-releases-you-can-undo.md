---
Title: "Lovable Hosting: Releases You Can Undo"
Keywords: lovable hosting, staging, rollback, feature flags, safe releases, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Hosting: Releases You Can Undo

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting: Releases You Can Undo",
  "description": "Shipping fast is only safe when going back is boring. Staging with its own data, rollback that takes a minute, feature flags, and the database changes that make a release irreversible.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-09",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-hosting-releases-you-can-undo" }
}
</script>

The appeal of building with AI tooling is that changes are cheap. You have an idea in the morning and it is live by lunch, and for a product with no customers that is an unqualified advantage.

The moment customers arrive, one property of that workflow becomes a liability: a change that takes ten minutes to make can take three hours to undo, if undoing it is even possible. And the speed that made you productive now means a bad decision reaches everybody before anyone has looked at it.

The answer is not to slow down. It is to make going back so boring that shipping quickly stops being a gamble.

## Three Environments, and What Each Is For

**Development** is where you and your tooling work. It has fictional data, it can be broken at any moment, and nobody outside sees it.

**Staging** is a full copy of production — same code path, same configuration shape, its own database — where a change is confirmed working before anyone meets it. This is the environment small products skip and the one that pays for itself the first time.

**Production** is what customers use, and it should only ever receive changes that have been seen working somewhere else.

Two rules make this real rather than decorative. Staging gets its own data, anonymised from production rather than connected to it — a staging environment pointing at the live database means a test deletion is a real deletion. And staging is blocked from search engines and ideally password-protected, or you acquire a second version of your site competing with the first.

## Rollback Is the Feature

Ask yourself one question: if the change you are about to make turns out to be wrong, how long until it is undone, and do you know the steps?

If the answer involves thinking, you do not have a rollback — you have a hope. And the time to discover the steps is not while customers are affected.

Most platforms keep previous deployments and can restore one in a minute. Find out where that control is, once, today, while nothing is wrong. Then test it deliberately: deploy something trivial, roll it back, and time it. A rollback you have performed is a rollback you will reach for; one you have only read about is a rollback you will avoid at exactly the wrong moment.

## The Changes That Cannot Be Rolled Back

This is the part that matters most and is least understood.

Reverting code is easy. Reverting a database change is frequently impossible, because the data has moved on. If a release dropped a column, the previous version of the code expects a column that no longer holds anything. If a migration transformed values, the old values are gone.

So schema changes need the expand-and-contract discipline: add the new structure first, deploy code that writes to both old and new, backfill, deploy code that reads only the new, and remove the old structure in a later release once you are confident. Each step is individually reversible, and at no point do the running code and the live schema disagree.

The same applies to anything irreversible in the world: emails sent, payments taken, files deleted, notifications delivered. A release that does one of those on deploy cannot be undone by reverting it, which is a good reason to put such actions behind a flag rather than behind a deployment.

## Feature Flags Separate Deploying From Releasing

A small technique with a large effect.

A flag is a condition your code checks before showing a feature. With it, code can be deployed while the feature stays off, switched on for yourself, then a friendly customer, then everybody — and switched off in seconds if something is wrong.

Three uses justify the effort for a small product. Turning a new feature on gradually rather than for four hundred people at once. Turning an expensive feature off under load, which is what saves a launch day. And separating a risky change from a deploy, so the undo does not require another release.

Keep them simple: a configuration value or a small table, not a platform. And remove them once a feature is settled, or in a year your code will be a museum of conditions nobody can safely delete.

## A Release Routine That Fits One Person

**Before:** the change is on staging and you have used it as a real user would. If it touches data, money or permissions, someone else has looked — and if there is no one else, you have read the diff yourself, deliberately, rather than trusting that it worked.

**During:** deploy at a time you can watch. Not Friday evening, not before you leave.

**After:** ten minutes with the live product and the error tracker. Load the page, exercise the thing you changed, log in as a real user, and look at whether anything new is appearing.

That is the entire routine. It costs fifteen minutes per release and it catches the overwhelming majority of what reaches customers otherwise.

## When to Automate, and When Not To

Deploying automatically on every commit is excellent for a product with a test suite and poor for one without, because at that stage the only verification is a person looking at it.

The sensible progression: manual deploys with a rollback you have tested; then automatic deploys to staging with manual promotion to production; then automatic promotion once tests exist that you trust. Skipping to the end because it is what mature teams do gives you the speed of a mature team and none of the safety.

What is worth automating immediately regardless: the build itself, so that deploying is one action rather than a remembered sequence. Most bad releases at small companies are not bad code — they are a step somebody forgot.

## When a Release Goes Wrong Anyway

It will, and the difference between a bad twenty minutes and a bad week is entirely in what you do in the first five.

**Roll back first. Diagnose afterwards.** The instinct is to understand the problem before acting, and it is the wrong order when customers are affected. Restore the previous version, confirm the product works, and then investigate at your own pace with nothing at stake. Founders who try to fix forward under pressure routinely make a second mistake on top of the first.

**Do not deploy a hurried fix.** A change written in three minutes, unreviewed and untested, deployed to production while you are stressed, is how a broken feature becomes a broken product.

**Check whether data was affected.** This is the question that determines whether the rollback was sufficient. Code reverts cleanly; records created or altered by the broken version do not disappear with it. Look for what was written in the window, and correct it deliberately.

**Tell anyone who hit it.** Briefly and specifically: what was wrong, for how long, what you have done, and what they should do. A customer who reported a problem and then hears nothing assumes you did not care; the same customer told within the hour usually remembers the response rather than the fault.

**Write down the sequence while it is fresh.** What changed, when it broke, how you noticed, what you did. Tomorrow you will remember a simplified version, and the details are where the real cause lives.

**Then ask what would have caught it.** A staging check, a test, a review, a flag. One improvement per incident, applied immediately, is how a release process gets better — and it should be a change to the process, never a resolution to be more careful, which is not a thing anybody can actually do.

## Setting This Up

For a running product this is about a day: a staging environment with its own anonymised data, blocked from indexing; the build made reproducible from a repository so any commit can be deployed; rollback identified, tested and timed; a simple feature flag mechanism; the expand-and-contract pattern applied to schema changes so no release leaves code and database disagreeing; and a written release routine short enough that you will actually follow it.

LaunchStudio sets this up as part of production readiness and keeps it running under the €49 per month managed hosting arrangement. The engineers are Manifera's: eleven years of releasing production systems for clients including Vodafone, TNO and CFLW, from Amsterdam Herengracht 420, Singapore and Ho Chi Minh City.

[Tell us how you deploy today](https://launchstudio.eu/en/#contact) for a specific plan, or see the [packages](https://launchstudio.eu/en/#packages).

## Real example

### A Column Dropped at Half Past Four

Mark Oudshoorn built Kassakoppeling with Lovable: point-of-sale integration for independent retailers, used by 34 shops around Gorinchem and Leerdam to synchronise sales into their stock and accounting systems.

He deployed directly to production from his working environment, which had been fine for a year. There was no staging, and he had never performed a rollback.

On a Thursday afternoon he asked an agent session to tidy up the sales table, and the migration it generated dropped a column recording which till a transaction came from. The application still worked. Nothing errored. But the per-till breakdown that eleven of his retailers used for staff reconciliation returned empty, and the accounting export now attributed every sale to a single till.

He discovered it at half past four when a retailer phoned. Reverting the code changed nothing, because the data was gone. The backup was from that morning, and restoring it would have discarded a day of trading for all 34 shops — so he could not simply restore either.

Six business days of work: the till column reconstructed for the affected day by matching transactions against the retailers' own till receipts, which two shops could not fully supply and which was written off with their agreement; a staging environment created with anonymised data and blocked from indexing; the build made reproducible from a repository with every deploy tied to a commit; rollback tested and timed at 40 seconds; the expand-and-contract pattern adopted for schema changes, with a rule that any migration touching data is read by Mark before it runs and preceded by a manual snapshot; a simple feature flag mechanism added; database credentials separated so the application's ordinary account cannot drop anything; and a five-line release routine written and stuck to the side of his monitor.

**Result:** eleven months without an incident, and Mark reports that the change he values most is the smallest one — the rule that a migration touching data is read before it runs, which has caught two further destructive suggestions since.

> *"Reverting the code took thirty seconds and changed nothing, because the column was gone. That was the afternoon I learned that undo and rollback are not the same thing."*
> — **Mark Oudshoorn, Founder, Kassakoppeling (Gorinchem)**

**Cost & Timeline:** €3,400 (data reconstruction, staging environment, reproducible builds with tested rollback, expand-and-contract migrations, feature flags, credential separation) — completed in 6 business days.

## Frequently Asked Questions

### Do I really need a staging environment?

Once customers depend on the product, yes. It is a full copy with its own anonymised data where a change is seen working before anyone meets it. Pointing staging at the live database defeats the purpose, since a test deletion becomes a real one.

### How fast should a rollback be?

A minute or two, and you should have performed one. Find the control on your platform today while nothing is wrong, deploy something trivial, roll it back and time it. A rollback you have never used is one you will avoid when it matters.

### Why can I not roll back a database change?

Because reverting code does not bring data back. A dropped column or a transformed value is gone. Use expand-and-contract — add, write to both, backfill, switch reads, remove later — so every step is individually reversible.

### What are feature flags for in a small product?

Turning a feature on gradually, turning an expensive one off under load, and separating a risky change from a deploy so undoing it takes seconds rather than another release. Keep them simple and remove them once a feature settles.

### Should I deploy automatically on every commit?

Not until you have tests you trust. Progress from manual deploys with a tested rollback, to automatic staging with manual promotion, to full automation. Automate the build immediately, though — most bad releases are a forgotten step rather than bad code.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I really need a staging environment?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Once customers depend on the product, yes — a full copy with its own anonymised data, never pointed at the live database."
      }
    },
    {
      "@type": "Question",
      "name": "How fast should a rollback be?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A minute or two, and you should have performed one already — deploy something trivial, roll it back and time it while nothing is wrong."
      }
    },
    {
      "@type": "Question",
      "name": "Why can I not roll back a database change?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Reverting code does not restore data. Use expand-and-contract so each step is individually reversible and code never disagrees with the schema."
      }
    },
    {
      "@type": "Question",
      "name": "What are feature flags for in a small product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Gradual rollout, switching an expensive feature off under load, and separating a risky change from a deploy so undoing takes seconds."
      }
    },
    {
      "@type": "Question",
      "name": "Should I deploy automatically on every commit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not before you have trusted tests. Automate the build immediately, then staging, then full promotion."
      }
    }
  ]
}
</script>
