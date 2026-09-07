---
Title: "Deploying Changes Without Holding Your Breath"
Keywords: safe deployment small team, rollback strategy saas, ci pipeline for solo founder, deploy friday, database migration deploy order, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Deploying Changes Without Holding Your Breath

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Deploying Changes Without Holding Your Breath",
  "description": "If deploying feels risky, you will deploy less often, and less frequent deployments are larger and riskier still. How to make releases boring: automated checks, a rollback that works, deploy order for migrations, and knowing within minutes whether it worked.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-04-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/deploying-changes-without-holding-your-breath" }
}
</script>

There is a state most solo founders reach a few months after launch, where deploying has become slightly frightening. Nothing catastrophic has happened, but something broke once, and now every release carries a small dread. The rational response is to deploy less often — and that is the trap, because batching two weeks of changes into one release means that when something breaks you have fourteen changes to search through instead of one.

The way out is not more care at the moment of deployment. It is making the deployment itself unremarkable: automated checks that run before anything reaches customers, a rollback you have actually performed, and enough visibility to know within five minutes whether the release was good.

## Deploy Small, Deploy Often

The counterintuitive rule that experienced teams operate by: frequent small deployments are safer than infrequent large ones, and the reason is diagnostic rather than moral.

When a deployment contains one change and something breaks, you know what caused it. When it contains twenty, you have a search problem, during an incident, under pressure. Rolling back is also cleaner: reverting one change is safe, while reverting twenty means discarding nineteen that were fine.

For a small product this suggests deploying whenever a change is ready and verified, rather than accumulating a release. It also argues against the "never deploy on Friday" rule as usually stated. The real rule is: do not deploy when you cannot watch the result. A small, well-tested change on a Friday morning with an hour free is safer than a large one on a Tuesday when you are about to leave.

## The Minimum Pipeline

Between "it works on my machine" and "customers are using it" there should be automatic steps that do not depend on your remembering.

**Run the tests.** Even a small suite covering login, payment, and the two or three flows that must not break catches a meaningful share of regressions. This is the highest-value item and the one AI-generated products most often lack entirely, since generated code rarely arrives with tests.

**Check the build.** Anything that fails to compile or bundle should fail before deployment, not after.

**Apply migrations in the right order**, which is a specific trap covered below.

**Verify afterwards.** An automated check hitting the deployed application and confirming it responds correctly, so that a broken release is detected in seconds rather than when a customer reports it.

**Be able to roll back with one command.** Not a rebuild from an older commit — an actual, tested return to the previous version.

Most hosting platforms provide much of this. The part founders skip is the tests, and the part they discover late is that they have never verified the rollback.

## Migration Order Is Where Deployments Break

The most common self-inflicted deployment failure has nothing to do with the code being wrong. It is applying a schema change and a code change in an order that leaves them briefly disagreeing.

Deploy code expecting a new column before the migration adds it, and every request fails until the migration completes. Run a migration that removes a column while the old code is still serving requests, and the same. During a deployment both versions may be running simultaneously, which means the database must be compatible with both.

The rule that resolves this is the same expand-and-contract discipline used for any live schema change: **additive changes go first, destructive changes go last, and never in the same deployment as the code that depends on them.** Add the column, deploy code that writes to it, backfill, deploy code that reads from it, and only in a later deployment remove the old one. Each step leaves the database compatible with both the running and the incoming version.

This is slower than changing everything at once, and it is the difference between a deployment that is boring and one that requires a maintenance window.

## Roll Forward or Roll Back

When a deployment causes a problem, two options exist and choosing quickly matters more than choosing correctly.

**Roll back** — return to the previous version — is right when the problem is significant, the cause is not immediately obvious, or customers are affected now. It is fast and it stops the bleeding.

**Roll forward** — deploy a fix — is right when the cause is obvious and trivial, or when rolling back is impossible because a migration has already changed data in a way the old code cannot handle.

That last caveat is the one to plan around: a deployment including a destructive migration is difficult to reverse, which is another reason to keep destructive changes in their own later deployment. If the code can always be reverted independently of the database, rollback stays available.

Two habits make this work. Decide the threshold in advance — for example, if it is not fixed within ten minutes, roll back — because during an incident the temptation to keep trying one more thing is strong and usually wrong. And test the rollback before you need it: perform one deliberately, once, and time it. A rollback nobody has executed is a plan, not a capability.

Setting up automated checks, safe migration ordering, and a verified rollback path is a small, bounded piece of production engineering that removes most of the risk from routine releases. LaunchStudio, backed by Manifera's 11+ years of production engineering, puts this in place for AI-built products that have been deployed by hand until now. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Watching the Five Minutes After

A deployment is not finished when it completes. It is finished when you know it worked.

Three things to watch, for a few minutes: the error rate, which should return to its previous level rather than stepping up; response times, since a change that is functionally correct can still be much slower; and the core flow, verified by loading it yourself. This takes two minutes and catches most bad releases before customers do.

It helps to have a way to notice regressions that appear later, too. A change that only fails for customers with a particular configuration might not surface for hours, which is why error tracking with account context — and reading the new errors after each deployment — is the companion practice to deploying frequently.

Finally, keep a record of what was deployed and when. When something is discovered to be broken on Thursday and you need to know what changed on Tuesday, a deployment log answers in seconds. Most platforms keep this automatically; the discipline is looking at it.

## Real example

### The Deployment That Failed for Ninety Seconds Every Time

Ilja Pietersen ran Contractbeheer, a contract-renewal tracker for facility management firms, built in Lovable and deployed by pushing to the hosting platform. Migrations were applied by running them manually against production after the deploy completed.

Every deployment involving a schema change therefore produced a window — usually 60 to 120 seconds — in which the new code was live and the database had not yet changed. Every request in that window failed. It had happened eleven times over four months, each time attributed to "the platform being slow after a deploy."

It stopped being tolerable when a migration failed halfway, leaving the new code running against a database it did not match, and the product returned errors for 40 minutes while the cause was identified. There was no rollback path, because reverting the code would not have undone the partially applied migration, and nobody had ever attempted one.

**Result:** a pipeline running tests and build checks before deployment, migrations applied automatically as an ordered step with additive changes separated from destructive ones, an automated post-deploy verification check, and a one-command rollback tested deliberately and timed at 90 seconds. Deployment frequency went from roughly weekly to several times a week, and the deploy-window failures stopped entirely.

> "I had been deploying in a way that broke the product for ninety seconds every single time, and I had explained it away eleven times because it always fixed itself."
> — **Ilja Pietersen, Founder, Contractbeheer**

**Cost & Timeline:** deployment pipeline and rollback capability delivered in 3 business days.

## Frequently Asked Questions

### Is it safer to deploy less often?

No. Infrequent deployments are larger, which makes diagnosing a failure harder and rollback more costly. Frequent small deployments are safer because each one contains a single identifiable change.

### Should I avoid deploying on Fridays?

The useful version of the rule is to avoid deploying when you cannot watch the result. A small, tested change on a Friday morning with time to observe is safer than a large one at any time.

### Why do deployments break when a database change is involved?

Because code and schema briefly disagree. Additive migrations should be applied before the code that uses them, destructive ones only in a later deployment, so the database stays compatible with both running versions.

### Should I roll back or deploy a fix?

Roll back when customers are affected and the cause is not immediately obvious; roll forward when the fix is trivial or a migration makes reversal impossible. Decide a time threshold in advance rather than during the incident.

### What is the minimum worth automating before launch?

Tests covering login, payment, and the flows that must not break; a build check; ordered migrations; a post-deploy verification; and a rollback you have executed at least once.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Is it safer to deploy less often?", "acceptedAnswer": { "@type": "Answer", "text": "No. Infrequent deployments are larger, making failures harder to diagnose and rollback costlier. Frequent small deployments each contain a single identifiable change." } },
    { "@type": "Question", "name": "Should I avoid deploying on Fridays?", "acceptedAnswer": { "@type": "Answer", "text": "The useful rule is to avoid deploying when you cannot watch the result. A small tested change with time to observe is safer than a large one at any time." } },
    { "@type": "Question", "name": "Why do deployments break when a database change is involved?", "acceptedAnswer": { "@type": "Answer", "text": "Code and schema briefly disagree. Additive migrations go before the code using them and destructive ones in a later deployment, so the database stays compatible with both versions." } },
    { "@type": "Question", "name": "Should I roll back or deploy a fix?", "acceptedAnswer": { "@type": "Answer", "text": "Roll back when customers are affected and the cause is unclear; roll forward when the fix is trivial or a migration prevents reversal. Decide the threshold in advance." } },
    { "@type": "Question", "name": "What is the minimum worth automating before launch?", "acceptedAnswer": { "@type": "Answer", "text": "Tests for login, payment, and critical flows; a build check; ordered migrations; a post-deploy verification; and a rollback executed at least once." } }
  ]
}
</script>
