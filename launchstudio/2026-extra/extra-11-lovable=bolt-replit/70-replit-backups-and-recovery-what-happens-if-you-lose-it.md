---
Title: "Replit Backups and Recovery: What Happens If You Lose It"
Keywords: Replit, backups, disaster recovery, point in time restore, data loss, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Replit Backups and Recovery: What Happens If You Lose It

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Replit Backups and Recovery: What Happens If You Lose It",
  "description": "Three different disasters, only one of which most people plan for. What platform backups actually cover, the two numbers that define a backup, why an untested restore is a hypothesis, and how to rehearse recovery in half a day.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-11",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/replit-backups-and-recovery-what-happens-if-you-lose-it" }
}
</script>

An agent session at eleven in the morning is asked to clean up an unused column. It generates a migration, runs it, and reports success. The column was not unused — a report written four months earlier still read it — and the migration dropped it along with fourteen months of values.

Nothing is broken. The application runs. The data is gone, and the question that decides how the rest of the week goes is one nobody has asked before: what exactly can be restored, from when, and by whom?

Most founders discover their answer during the incident. It is a bad time to find out.

## Three Different Disasters

They require different preparations, and planning for one does not cover the others.

**The platform has a problem.** A provider outage, a region issue, a hardware failure. This is what people imagine when they hear "backup", and it is the least likely of the three. Managed providers handle it better than you would.

**Somebody destroys data.** A migration that drops a column, a query without a filter, a bulk delete with the wrong condition, a synchronisation that overwrites good records with bad ones. Overwhelmingly the most common cause of real data loss in small products, and the one where the damage is done by an authorised action rather than a failure.

**You lose access.** An account closed, a payment method expired, a domain registered by someone unreachable, a workspace belonging to a former collaborator. No data is lost and you cannot reach it, which is the same thing from your customers' point of view.

The second is the one to prepare for, and it is the one platform backups protect against least well — because from the system's perspective, nothing went wrong.

## What Your Platform Actually Backs Up

Read your provider's documentation rather than assuming, because the coverage is narrower than most people expect.

**Managed databases** typically have automated backups with a retention window, and better tiers offer point-in-time recovery — the ability to restore the state as of a specific moment, which is exactly what the dropped-column scenario needs. Check which you have, and check the retention period, because "we have backups" and "we have backups covering the last seven days" are different sentences when a problem surfaces after three weeks.

**Object storage** may or may not have versioning enabled. Without it, an overwritten or deleted file is gone.

**Your code** is protected only if it is in version control that lives somewhere other than the environment you are working in.

**Secrets and configuration** are generally not backed up in any useful sense. Losing the environment can mean reconstructing every credential by hand.

**State held in third-party services** — subscriptions at your payment provider, contacts at your email service — is theirs, not yours, and restoring your database to an earlier point does not roll those back. This mismatch is the most awkward part of a real recovery.

## The Two Numbers That Define a Backup

Every backup arrangement answers two questions, whether or not anybody has stated them.

**How much data can you afford to lose?** If backups run nightly, a failure at four in the afternoon loses the working day. For some products that is fine; for a product processing customer payments it is not.

**How long can you be down while recovering?** A restore takes time, and a large database takes more. If your answer is "an hour" and you have never timed a restore, you do not have an answer, you have a hope.

Write both numbers down and check your arrangement matches them. Most founders discover the two are out of alignment — either paying for protection they do not need, or assuming protection they do not have.

## An Untested Restore Is a Hypothesis

This is the sentence worth taking away from the whole article.

A backup that has never been restored is an assumption about a file. Things that go wrong on first attempt, routinely: the restore requires a permission the account does not have; it takes four hours rather than twenty minutes; the dump excludes something nobody noticed; the restored database lacks the extensions the application needs; the application cannot connect because the credentials are different and nobody remembers where they are set.

Every one of those is discovered calmly in a rehearsal and painfully in an incident.

Rehearse once, properly: restore into a new, separate database, point a copy of the application at it, confirm the data is there and complete, and write down how long it took and every step required. Then do it again in six months, because the system will have changed.

## Accidental Deletion Deserves Its Own Defences

Since destruction by authorised action is the most common cause, it is worth defending against directly rather than only recovering from.

**Soft deletion for anything that matters.** Mark records as deleted rather than removing them, and clean up on a schedule. This converts most incidents from a restore into a one-line correction.

**An audit trail on important tables.** Who changed what, when. Without it, the question "when did this go wrong?" is unanswerable, and point-in-time recovery needs an answer to be useful.

**Migrations reviewed and reversible.** A migration that drops or rewrites data should be read by a person before it runs, and should exist as a file so it is reviewable at all. Take a manual snapshot immediately beforehand.

**Separate credentials for destructive access.** Day-to-day application access should not be able to drop tables. This alone prevents a category of agent-generated accident.

## An Export You Own

Independent of the platform's arrangements, keep your own copy somewhere else.

A weekly export of the database and the uploaded files, stored with a different provider, is protection against the third disaster — the one where nothing failed and you simply cannot get in. It also happens to be the answer when a business customer asks whether they can get their data out.

Automate it, check occasionally that the files are non-empty and recent, and keep enough history that a problem discovered late is still recoverable.

## A Runbook Worth Half a Page

When something goes wrong you will be stressed and possibly working at an unusual hour. Write the steps down in advance: where the backups are, who can access them, the exact commands, where the credentials live, how long it takes, who tells customers and what they are told, and who is responsible for deciding to do it.

Store it somewhere that is not the system it describes, which sounds obvious and is exactly the mistake people make once.

## What You Tell Customers While You Are Fixing It

The technical recovery is half of an incident. The other half is what the people depending on you hear, and it is the half that determines whether they stay.

**Tell them before they tell you.** A customer who discovers the problem themselves and then contacts you has already concluded that you were not watching. The same customer, told first, concludes that you were. The facts are identical; the relationship is not.

**Say what you know, when you knew it, and what you are doing.** Not a diagnosis you do not yet have. "Stock figures entered between Tuesday and this morning may be incorrect. We identified it at 09:20, we are restoring from a backup, and we expect to confirm by two o'clock" is a complete and honest message that takes two minutes to write.

**Be specific about what is affected and what is not.** Vagueness makes every customer assume they are affected. A precise scope lets most of them stop worrying and lets the rest act.

**Say what they should do in the meantime.** Stop entering data, keep paper records, use last week's export. Practical instructions are what people remember afterwards.

**Follow up once it is over,** with what happened, what was lost if anything, and what you changed so it does not recur. This message is the one that rebuilds trust, and it is the one founders skip because the crisis has passed and the subject is uncomfortable.

**Decide in advance who writes it.** In a two-person business that seems unnecessary until both people assume the other is handling communication while both are handling the database.

Customers forgive incidents. They rarely forgive discovering that something was wrong for nine days and nobody mentioned it.

## Making Recovery a Known Quantity

For a running product this is half a day of setup and one rehearsal: backup coverage confirmed across database, files, code, secrets and configuration; retention aligned to written tolerances; a restore actually performed and timed; versioning enabled on storage; an independent export automated to a different provider; soft deletion and an audit trail added where they matter; destructive database access separated from application access; and a runbook written and stored outside the system.

LaunchStudio includes this in production readiness work and in the €49 per month managed hosting arrangement, where the rehearsal is repeated rather than done once. The engineers are Manifera's: eleven years of running production systems for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City.

[Tell us what your product holds](https://launchstudio.eu/en/#contact) and you will get an honest assessment of what you could actually recover, usually within one business day, or see the [packages](https://launchstudio.eu/en/#packages).

## Real example

### Fourteen Months of Stock History, Removed in One Migration

Daan Poelman built Voorraadje on Replit: a stock-tracking tool used by six specialist shops around Venlo — a bicycle dealer, two bookshops, a lighting retailer and two hardware stores.

An agent session asked to tidy the schema generated a migration removing a column it judged unused. It held the purchase price at which each stock movement had been recorded, which no screen displayed but which the annual valuation report calculated from. Fourteen months of values, across roughly 90,000 stock movements.

Daan discovered it nine days later, when a shop asked for its valuation report and the figures came back as zero.

The recovery was possible and awkward. Automated backups existed with a seven-day retention window, which had passed. Point-in-time recovery was not enabled on his tier. What saved him was a manual export he had taken three months earlier, before an unrelated change, and had left in a folder on his laptop — which meant three months of purchase prices were recoverable and six weeks were not.

Seven business days of work: the three-month export restored into a separate database and the missing column reconstructed by matching stock movements on identifier and timestamp; the six irrecoverable weeks reconstructed for four of the six shops from supplier invoices they still had, and written off for the other two after a conversation; point-in-time recovery enabled; a weekly automated export to a second provider configured; versioning enabled on file storage; soft deletion and an audit trail added to the stock tables; the application's database credentials separated from a second set holding destructive rights, so no agent session can drop anything; a rule adopted that migrations touching data are read by Daan and preceded by a manual snapshot; and a restore rehearsed end to end, timed at 34 minutes.

**Result:** the two shops that lost six weeks of valuation history stayed, though Daan describes the conversation as the worst of his working life. Nothing has been lost since, and the restore has been rehearsed twice more.

> *"My backups were seven days old and the mistake was nine days old. Two days. The only reason I recovered anything was a file I had forgotten about on my own laptop."*
> — **Daan Poelman, Founder, Voorraadje (Venlo)**

**Cost & Timeline:** €3,800 (data reconstruction, point-in-time recovery, independent export automation, soft deletion and audit trail, credential separation, restore rehearsal) — completed in 7 business days.

## Frequently Asked Questions

### Does my platform already back up everything?

Almost certainly not everything. Managed databases usually have automated backups with a retention window; object storage may lack versioning; secrets and configuration are generally not covered; and state held in third-party services is not yours to restore.

### What is the most likely way I lose data?

Not a platform failure. An authorised action — a migration that drops a column, a query without a filter, a bulk delete with the wrong condition. From the system's point of view nothing went wrong, which is why that case needs its own defences.

### How do I know my backup works?

Restore it. Into a separate database, with a copy of the application pointed at it, and time the whole process. Until that has happened, a backup is an assumption about a file rather than a recovery plan.

### What is point-in-time recovery and do I need it?

It restores the database as of a specific moment rather than the last scheduled backup. It is what saves you when a mistake is discovered days later, and it is worth checking whether your tier includes it before you need it.

### Should I keep my own export as well?

Yes. A weekly export of database and files to a different provider protects against losing access rather than losing data — a closed account, an expired card, a workspace owned by someone unreachable — and answers customers who ask whether they can get their data out.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does my platform already back up everything?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Rarely. Databases usually have backups with a retention window, but storage versioning, secrets, configuration and third-party state are frequently not covered."
      }
    },
    {
      "@type": "Question",
      "name": "What is the most likely way I lose data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "An authorised action — a migration dropping a column, an unfiltered query, a bulk delete — rather than a platform failure."
      }
    },
    {
      "@type": "Question",
      "name": "How do I know my backup works?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Restore it into a separate database with a copy of the app pointed at it, and time the process. An untested backup is a hypothesis."
      }
    },
    {
      "@type": "Question",
      "name": "What is point-in-time recovery and do I need it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It restores the database as of a specific moment rather than the last scheduled backup, which is what helps when a mistake is found days later."
      }
    },
    {
      "@type": "Question",
      "name": "Should I keep my own export as well?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — a weekly export to a different provider protects against losing access rather than losing data, and answers customer data-portability questions."
      }
    }
  ]
}
</script>
