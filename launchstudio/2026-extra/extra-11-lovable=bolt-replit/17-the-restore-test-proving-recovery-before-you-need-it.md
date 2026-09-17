---
Title: "Supabase Backups: The Restore Test You Have Never Run"
Keywords: supabase security, database backup restore test, disaster recovery small saas, point in time recovery, AI app data loss, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Supabase Backups: The Restore Test You Have Never Run

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Supabase Backups: The Restore Test You Have Never Run",
  "description": "Backups that have never been restored are assumptions. A practical guide to recovery for small AI-built products: what can actually destroy your data, what your plan really covers, and how to rehearse a restore in an afternoon.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-19",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/the-restore-test-proving-recovery-before-you-need-it" }
}
</script>

Ask a founder whether they have backups and the answer is almost always yes. Ask when they last restored one and the conversation changes shape.

That second question is the only one that matters, because a backup is a claim and a restore is evidence. The gap between them is where a specific and avoidable category of disaster lives: the founder who discovers, on the worst morning of their year, that the backups have been failing silently for two months, or that they cover the database but not the uploaded files, or that restoring takes eleven hours during which the business is simply closed.

## What Actually Destroys Data in Small Products

Not what people imagine. Infrastructure providers lose data very rarely; the realistic threats are closer to home.

**Someone deletes the wrong thing.** A cleanup script with a filter that matched more than intended, a bulk operation run against production instead of staging, an "are you sure" dismissed at speed. In small teams this is the single most common cause of real loss.

**A bad migration.** A schema change that drops a column, transforms values incorrectly, or truncates a table. Generated migration code is entirely capable of this and it executes confidently.

**A logic bug that corrupts quietly.** Not deletion but degradation: a rounding error applied to stored balances, a batch job that overwrites the wrong rows, a broken deduplication that merges unrelated records. This is the worst version, because the damage propagates into your backups before anyone notices.

**An exposed credential used destructively.** Less common than the cost-fraud version, and it happens.

**Account loss.** A payment card expires on the provider account, notifications go to an address nobody checks, and the project is suspended.

Notice that only one of these is a technical failure of the platform. The rest are ordinary human and code events, which is why "the provider handles backups" is not a plan.

## What Your Backup Plan Actually Covers

Read your provider's current documentation rather than assuming, because the details differ by plan and change over time. Establish four things concretely.

**Frequency.** Daily is common. Daily means your worst case is losing a day of customer activity — acceptable for some products, unacceptable for anything transactional.

**Retention.** How far back can you go? This matters most for quiet corruption, which is often discovered weeks later. A seven-day window is useless if the bug started three weeks ago.

**Point-in-time recovery.** The ability to restore to a specific moment rather than to a nightly snapshot is usually a paid feature and is what turns "we lost today" into "we lost four minutes".

**What is excluded.** This is the one that surprises people. Database backups typically do not include your uploaded files, which live in object storage with their own arrangements. A perfect database restore alongside missing photographs is a partial recovery at best.

## The Two Numbers Worth Deciding

Professional practice reduces this to two questions, and both are business decisions rather than technical ones.

**How much data can you afford to lose?** An hour, a day, a week. This determines backup frequency and whether you need point-in-time recovery.

**How long can you afford to be down?** An hour, a day, a weekend. This determines whether you need a rehearsed restore procedure or can improvise.

Write both numbers down and compare them to what your current arrangement actually provides. Most founders find a gap, and most find the gap is cheaper to close than they expected — frequently one paid tier plus an afternoon.

## Rehearsing a Restore in an Afternoon

This is the part almost nobody does and it is genuinely straightforward.

**Create a separate project or instance.** Never restore into production; the point is to prove the mechanism without risking anything.

**Restore your most recent backup into it.** Time it. That number is your actual recovery time, and it is usually longer than people guess.

**Verify the contents by hand.** Count rows in your three most important tables and compare with production. Open five specific records you recognise. Check the most recent entries — a backup that silently stops at last month's data is a real failure mode.

**Point a copy of your app at it** and use it for ten minutes. Log in. Create something. Confirm the schema is complete, not just the rows.

**Test file recovery separately.** Take a handful of uploaded files, delete them from a test bucket, and restore them. If you cannot, you have found the gap before it cost you anything.

**Write down what you did,** with the exact steps and the time each took. This document is what you will follow while stressed, and it is the difference between a two-hour recovery and a two-day one.

## The Human Part of the Plan

Technology is half of it. The other half is a page that answers: who notices, who decides, what is communicated, and to whom.

For a solo founder this is short. For a product with customers, three things belong in it. A monitoring alert that reaches an actual human when the app is unreachable. A decision rule — how much loss justifies restoring versus repairing forward. And a customer communication line drafted in advance, because writing honestly about an outage while fixing it is harder than it sounds.

If your product holds personal data, this is also where breach obligations live. A data loss is not automatically a notifiable breach, but the assessment has to be made quickly under GDPR timelines, and knowing in advance who makes that call saves hours you will not have.

## What Good Looks Like

Backups running at a frequency matched to what you can afford to lose. Retention long enough to cover slow-moving corruption. Point-in-time recovery if you handle transactions. Files backed up separately and verified. A restore rehearsed at least once, with a written procedure and a known duration. Monitoring that tells you about failures rather than customers telling you. And a calendar reminder to repeat the rehearsal twice a year, because arrangements drift.

That is perhaps a day of work in total and a small monthly cost. Set against the alternative — reconstructing customer data from email threads and hoping — it is one of the cheapest forms of insurance available to a small product.

## Getting It Set Up and Proven

LaunchStudio treats recovery as part of making an AI-built product production-ready rather than as an optional extra: backup configuration matched to your tolerance, file storage included rather than forgotten, a restore rehearsed and timed in a scratch environment, monitoring wired to alert a human, and a written runbook handed over with the rest of the documentation. Managed hosting keeps it maintained afterwards at €49 per month, which mostly means somebody notices when a backup starts failing.

The interface you built in Lovable, Bolt or Cursor is untouched, and the engineering comes from Manifera's team — eleven years of production systems for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City.

If you have backups and have never restored one, [describe your project](https://launchstudio.eu/en/#contact) and we will tell you what your actual recovery position is within one business day.

## What a Customer Asks Afterwards

Recovery is technical. The conversation after it is not, and founders are consistently unprepared for how specific the questions become.

**"What exactly was lost?"** Not "some data" — which records, over which period. This requires knowing your backup timestamp and being able to describe the gap in terms the customer understands: bookings made between Tuesday evening and Wednesday morning, for example.

**"Was anything exposed?"** Loss and exposure are different events with different obligations. If you cannot distinguish them, the honest answer is that you are investigating, which is why access logging matters as much as backups.

**"Will it happen again?"** They are asking what changed. A specific answer — staging environment added, migrations no longer run directly against production, restore procedure rehearsed and timed — is reassuring. "We'll be more careful" is not.

**"How long were you down, and why did it take that long?"** This is where a rehearsed restore pays for itself twice: once in the shorter outage, and once in being able to say the procedure was tested and the timing was known.

**"What do we need to tell our own users?"** For business customers, your incident may trigger their obligations. Give them the facts promptly and in writing, and let their privacy officer make that judgement rather than making it for them.

Draft short versions of these answers before you need them. Writing honestly while your product is down is considerably harder than it sounds, and a customer's confidence recovers faster from a clear account than from a fast fix nobody explained.

## Backups Are Not Version Control, and Neither Replaces the Other

A confusion worth clearing up, because founders sometimes believe one covers the other.

**Version control protects your code.** It lets you see who changed what, revert a bad change, and reconstruct the application at any past point. It contains no customer data and restoring it does not bring back a deleted booking.

**Backups protect your data.** They contain what your users created and none of the reasoning behind your code. Restoring one brings back rows and tells you nothing about which deployment introduced the bug that corrupted them.

Real incidents usually need both: the database restored to a point before the damage, and the code reverted to the version that was running when it was correct. Knowing which deploy coincided with which data state is what makes that possible, which is why a simple deployment log — what shipped, when — is quietly part of your recovery plan rather than a separate nicety.

## Real example

### A Membership Platform That Lost Eleven Days and Got Them Back

Bas Oosterhuis ran Sportief, a membership and scheduling platform used by six amateur sports clubs around Almere. A migration intended to normalise how membership types were stored was generated, reviewed, and run against production on a Tuesday evening. It transformed the wrong column, overwriting eleven days of membership renewals with default values.

The mistake was noticed on Wednesday morning when treasurers from two clubs reported members showing as unpaid. Bas had daily backups on his database plan and had never restored one.

The recovery took nine hours rather than the one he expected. The most recent backup restored cleanly into a scratch project, but the schema had changed since it was taken, so the data could not be pushed back directly. Reconciling renewals recorded by the payment provider after the backup point with the restored rows was manual work. Uploaded club logos and member photographs, stored separately, were unaffected — which he confirmed only after two hours of worry, having never checked what was in scope.

Afterwards, five business days of work: point-in-time recovery enabled, file storage backed up on its own schedule, a rehearsed restore procedure written down and timed at 40 minutes, staging environment created so migrations are never again run first against production, and monitoring added that alerts on backup failure.

**Result:** a subsequent migration error four months later was resolved in 50 minutes using the written procedure, with no customer noticing.

> *"I had backups. What I didn't have was any idea what restoring one involved, and I found out on the morning I could least afford to."*
> — **Bas Oosterhuis, Founder, Sportief (Almere)**

**Cost & Timeline:** €1,850 (recovery configuration, file backup, rehearsed restore, staging environment) — completed in 5 business days.

## Frequently Asked Questions

### My provider takes backups automatically. Is that enough?

It is the foundation, not the plan. You still need to know the frequency, the retention window, whether uploaded files are included, how long a restore takes and whether it works — and only a rehearsal answers the last two.

### What is point-in-time recovery and do I need it?

It restores to a specific moment rather than to a nightly snapshot. If your product handles transactions, bookings or payments, losing a whole day is usually unacceptable, which makes it worth the paid tier.

### Are my uploaded files covered by database backups?

Usually not. Files live in object storage with separate arrangements, so a complete database restore can still leave you without photographs, documents or attachments. Check and back them up on their own schedule.

### How often should I rehearse a restore?

Twice a year is a reasonable rhythm for a small product, plus after any significant change to your schema or infrastructure. Each rehearsal takes an afternoon and updates the timing you would quote to a customer during an incident.

### What if the corruption is already inside my backups?

That is the argument for longer retention and for monitoring data quality, not just uptime. Slow corruption is discovered late, so a window that only reaches back a week gives you nothing to restore from.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "My provider takes backups automatically. Is that enough?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It is the foundation, not the plan. You still need the frequency, retention window, whether files are included, how long a restore takes and whether it works — and only a rehearsal answers the last two."
      }
    },
    {
      "@type": "Question",
      "name": "What is point-in-time recovery and do I need it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It restores to a specific moment rather than a nightly snapshot. For products handling transactions, bookings or payments, losing a whole day is usually unacceptable."
      }
    },
    {
      "@type": "Question",
      "name": "Are my uploaded files covered by database backups?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually not. Files live in object storage with separate arrangements, so a complete database restore can still leave you without photographs or documents."
      }
    },
    {
      "@type": "Question",
      "name": "How often should I rehearse a restore?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Twice a year for a small product, plus after significant schema or infrastructure changes. Each rehearsal takes an afternoon and refreshes your real recovery timing."
      }
    },
    {
      "@type": "Question",
      "name": "What if the corruption is already inside my backups?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "That is the argument for longer retention and for monitoring data quality rather than only uptime, since slow corruption is discovered late."
      }
    }
  ]
}
</script>
