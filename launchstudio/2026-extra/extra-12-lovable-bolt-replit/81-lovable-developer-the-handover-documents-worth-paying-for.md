---
Title: "Lovable Developer: The Handover Documents Worth Paying For"
Keywords: lovable developer, handover, documentation, knowledge transfer, offboarding, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable Developer: The Handover Documents Worth Paying For

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Developer: The Handover Documents Worth Paying For",
  "description": "The work ends and the knowledge leaves with it unless you asked for something specific. What a handover should contain, why it belongs in the original agreement, and how to verify you actually received it.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-22",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-developer-the-handover-documents-worth-paying-for" }
}
</script>

The work finishes, the invoice is paid, and six weeks later something breaks at seven in the morning. The person who built it is on another engagement, and what you have is a product you own and cannot explain.

This is avoidable and it is not avoided by hoping. A handover is a deliverable like any other: specified in the agreement, produced as part of the work, and checked before the final payment.

It costs perhaps half a day of an engagement and it is the difference between owning a product and renting a dependency.

## The Five Documents

**A system overview.** What the product consists of, what each part does, which external services it uses and why. Two pages, in language you can follow.

**A runbook.** What to do when specific things happen: the site is down, a payment failed, a job did not run, a customer reports missing data, you need to restore a backup. Each with steps, not principles.

**The services and accounts list.** Every provider, what it is for, which account holds it, roughly what it costs, and when it renews. This is the document that prevents a domain expiring because the reminder went to someone who left.

**A decisions record.** Why the significant choices were made — the ones described in the documentation article in this series. Three sentences each, and the most valuable thing in the set.

**What was not done.** Known issues, deferred work, accepted risks, and things to watch. A supplier willing to write this is one you should keep.

Alongside them: the repository with its history, the conventions file, the tests, and the environment configuration documented.

## Ask For It in the Agreement

The reason handovers are poor is that they are requested at the end, when the budget is spent and everyone has moved on.

Put it in the scope at the start, as a named deliverable with the five items listed, and make final acceptance depend on it. Any competent supplier will agree, because it is a small proportion of the work and they know it is reasonable.

The suppliers who resist are telling you something useful.

## The Walkthrough Matters as Much as the Documents

An hour, recorded, going through the product with you: here is how it fits together, here is the part that is unusual, here is what I would watch, here is what I would do first if this happened.

The recording is the valuable artefact. It captures the things that do not get written down — the hesitation before explaining something, the aside about a part that is fragile — and you can watch it again in six months when the context has faded.

Do it before the last day, so that questions arising from it can still be answered.

## Verify Before the Final Payment

A handover is checkable, and checking it takes an afternoon.

Follow the runbook for one scenario and see whether it works — restoring a backup is the best test, because it exercises documentation, access and the backup itself.

Set the product up from the repository on a fresh machine using only the README. Whatever you cannot do is what is missing.

Check that every account in the services list is one you can access. This is where you discover that a provider account is in the supplier's name, which is a small problem now and a significant one in a year.

And read the decisions record. If it is empty or generic, ask for it properly — it is the document that is hardest to reconstruct later and the one most often skipped.

## Transfer What They Own

The administrative half of a handover, and the part that causes problems eighteen months later.

Accounts registered in the supplier's name transferred to yours. Domains moved to your registrar account. Two-factor authentication moved to your own devices or a shared vault you control. Payment methods changed to yours. Their access removed and every credential they held rotated, as the secrets article in this series describes.

Do this at the end of the engagement, deliberately, from a list. It takes an hour and it is the difference between a clean separation and a phone call to somebody you no longer have a relationship with.

## Keep It Alive Afterwards

A handover is a snapshot, and a product that changes weekly outdates it within months. What was accurate in March describes a product that no longer exists by autumn, which is how founders end up with documentation they no longer trust and therefore do not use.

Three habits keep it current at almost no cost, and they are the same ones the documentation article in this series recommends.

**Update the runbook when something happens.** Every incident either follows a procedure that worked, or reveals one that is missing. Ten minutes afterwards, while it is fresh.

**Add a decision entry when you make one.** Three sentences at the moment. Retrospective entries are guesses.

**Review the services list twice a year.** Providers added, providers abandoned, renewal dates, costs. This is the list that quietly becomes wrong, and it is the one that causes the domain-expiry class of problem.

The system overview needs attention roughly annually, and only when the shape of the product has genuinely changed.

The test of whether this is working is the same as the handover test: could somebody else operate this product from what is written? Asking that once a year, and fixing whatever the answer reveals, keeps the value of the handover rather than letting it decay into a document about a product that used to exist.

## Handover Is Also for You

The framing so far assumes someone else will need this. The more immediate beneficiary is usually the founder, and for two reasons that arrive sooner than a departure.

**You forget.** Four months on another priority and the details of how the payment reconciliation works are gone. The runbook you asked a supplier to write is the document you read at seven on a Sunday morning, and the alternative is reconstructing it under pressure.

**You want a holiday.** A product one person can operate is a product that person cannot leave. Founders describe this as the moment the documentation stopped being a compliance exercise — the week they went away and somebody else could answer a customer's question about a failed payment because the runbook covered it.

There is a third reason that matters commercially. The same set of documents is what a buyer, an investor or a larger customer's technical reviewer asks for, and having it ready turns a diligence exercise into a reading task. As the documentation article in this series notes, a product only one person can explain carries a risk that any serious counterparty identifies immediately.

So the half day is not a favour to a hypothetical successor. It is the thing that lets you stop being the only person who can keep your own product running.

## The Version for a Product You Built Yourself

Not every founder has a supplier to ask. A great many have built the whole product with AI tools and have no handover to request, which does not remove the need for one.

The same five documents apply and you write them yourself, and there is a shortcut that works well for exactly this situation: an assistant reading your codebase can produce the system overview and much of the reference material in an afternoon, as the documentation article in this series describes. What it cannot produce is the decisions record and the known issues, because neither is in the code.

So: generate the structural half, write the two documents that require memory, and assemble the services list from your own billing — which is the most reliable source and the one nobody thinks of.

Then test it the same way. Set the product up on a different machine from the README alone. Follow your own runbook to restore a backup. Confirm every account is in your name rather than in an email address you no longer check.

An afternoon, once, and the result is the same asset a paid handover would have produced — and considerably more likely to be accurate, since you are the person who made the decisions it records.

## Setting This Up

For any engagement this belongs in the original scope: a system overview, a runbook covering the specific failures that occur, a services and accounts list with costs and renewals, a decisions record, and a written statement of what was not done; the repository with history, conventions file, tests and documented configuration; a recorded walkthrough held before the final day; verification by following the runbook, setting the product up from the README on a fresh machine and confirming access to every account; and a deliberate transfer of accounts, domains, two-factor and payment methods with the supplier's access removed and credentials rotated.

LaunchStudio produces all of this as part of every engagement, because a product you cannot operate is not one we have finished. Behind it is Manifera — eleven years, 160+ projects, 120+ engineers, from Herengracht 420 in Amsterdam.

[Ask us what our handover contains](https://launchstudio.eu/en/#contact) before you compare quotes on price.

## Real example

### A Domain That Expired on a Saturday

Ingrid Ravenstijn built Cateringplanner in Lovable and paid a freelancer €5,400 to secure it, add payments and launch. The work was good and the engagement ended amicably after five weeks.

There was no handover. The scope had not mentioned one and she had not thought to ask.

Fourteen months later the domain expired. The registration was in the freelancer's account, registered during the engagement because it was convenient, with the renewal notice going to his email. He had changed address, the notice bounced, and Cateringplanner was unreachable for three days over a weekend while Ingrid established who held the registration and reached him.

Twenty-six catering companies could not access their event schedules during a weekend in June, which is the busiest period of their year.

Three business days afterwards: an inventory of every service the product uses, which found four accounts in the freelancer's name — the domain, the error tracking, the email provider and one storage account; all four transferred or recreated under her own accounts, with credentials rotated; a system overview written from the code by a second supplier; a runbook covering the eleven failures that had occurred or could plausibly occur, including domain and certificate expiry; a services list with costs, renewal dates and a calendar reminder 60 days before each; a decisions record reconstructed as far as possible, with the freelancer generously answering questions by email; a statement of known issues; and a recorded walkthrough with the second supplier.

**Result:** the reconstruction cost €3,100 and took three days, against perhaps half a day if it had been part of the original engagement. Ingrid's note is that the original work was competent and that she had no way to benefit from it independently.

> *"The work was good. Fourteen months later my domain expired in someone else's account over a weekend in June, and twenty-six caterers could not see their bookings."*
> — **Ingrid Ravenstijn, Founder, Cateringplanner (Breda)**

**Cost & Timeline:** €3,100 (service inventory and account transfers with credential rotation, system overview, runbook, services list with renewal reminders, reconstructed decisions record, known issues statement, recorded walkthrough) — completed in 3 business days.

## Frequently Asked Questions

### What should a handover contain?

A system overview, a runbook for specific failures, a services and accounts list with costs and renewals, a decisions record, and a written statement of what was not done — plus the repository, tests and documented configuration.

### When should I ask for it?

In the original agreement, as a named deliverable with final acceptance depending on it. Requested at the end, it competes with a spent budget and a supplier who has moved on.

### How do I know the handover is adequate?

Follow the runbook for one scenario — restoring a backup is the best test. Set the product up from the README on a fresh machine. Confirm you can access every account listed.

### What is the most valuable document?

The decisions record. It is the hardest thing to reconstruct later and the reason a future change does not remove something load-bearing.

### What administrative steps belong in a handover?

Transferring accounts and domains into your name, moving two-factor authentication to your control, changing payment methods, removing the supplier's access and rotating every credential they held.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What should a developer handover include?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A system overview, a runbook, a services and accounts list, a decisions record, a known-issues statement, plus repository, tests and configuration."
      }
    },
    {
      "@type": "Question",
      "name": "When should a handover be agreed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In the original scope, as a named deliverable with acceptance depending on it — not at the end when the budget is spent."
      }
    },
    {
      "@type": "Question",
      "name": "How do I verify a handover is adequate?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Follow the runbook to restore a backup, set the product up from the README on a fresh machine, and confirm access to every listed account."
      }
    },
    {
      "@type": "Question",
      "name": "Which handover document matters most?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The decisions record — hardest to reconstruct and the reason a later change does not remove something load-bearing."
      }
    },
    {
      "@type": "Question",
      "name": "What administrative transfers belong in a handover?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Accounts and domains into your name, two-factor under your control, payment methods changed, supplier access removed and credentials rotated."
      }
    }
  ]
}
</script>
