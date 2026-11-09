---
Title: "How Do I Recover Deleted Data in Supabase?"
Keywords: recover deleted data supabase, supabase restore backup, supabase point in time recovery, undo delete supabase table, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# How Do I Recover Deleted Data in Supabase?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How Do I Recover Deleted Data in Supabase?",
  "description": "Accidentally deleted rows, a dropped table or a bad migration can happen in any AI-built app. This guide explains what to do immediately, which recovery options Supabase offers through backups and point-in-time recovery, why restoring a whole project is risky, how to recover specific records safely, what happens to files in storage and how to prevent data loss with soft delete, safeguards and tested restores.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-08-02",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-recover-deleted-data-in-supabase" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Database backups", "url": "https://supabase.com/docs/guides/platform/backups" },
    { "@type": "CreativeWork", "name": "Supabase: Point-in-time recovery", "url": "https://supabase.com/docs/guides/platform/backups#point-in-time-recovery" },
    { "@type": "CreativeWork", "name": "PostgreSQL: Backup and restore", "url": "https://www.postgresql.org/docs/current/backup.html" },
    { "@type": "CreativeWork", "name": "GDPR Article 32: Security of processing", "url": "https://gdpr-info.eu/art-32-gdpr/" }
  ]
}
</script>

**Short answer:** stop further damage first, then check which backups you have. On paid Supabase plans, daily backups and, with the add-on, point-in-time recovery let you restore the database to an earlier moment, but restoring the whole project also rolls back every legitimate change made since then. For accidental deletions of specific records, it is usually safer to restore a backup into a separate project, extract the missing rows and reinsert them into production. Files in Supabase Storage are handled separately from database backups. Prevent the next incident with soft delete, restricted delete permissions, reviewed migrations and regularly tested restores.

## Key Takeaways

- **Act quickly but carefully:** stop the process causing the damage, note the time and avoid making things worse with hasty fixes.
- **Know your backup situation before you need it:** which plan you are on, how far back backups go and whether point-in-time recovery is enabled.
- **A full project restore rolls back everything,** including new orders, users and changes since the restore point.
- **Selective recovery** from a restored copy is usually the right approach for deleted records.
- **Prevention beats recovery:** soft delete, limited delete rights, migration reviews and tested backups.

## Step 1: Stop the Damage

Data loss often continues after it starts: a bug deleting records on every run, a sync job overwriting data, an AI agent repeating a destructive script.

- **Stop the source:** disable the feature, pause the job, revert the deployment or revoke the access that caused it.
- **Note the time** when the problem started, as precisely as possible. Logs, audit entries and user reports help.
- **Inform your team** and agree that nobody makes manual changes to production without coordination.
- **Do not run more "fixes"** directly in production until you understand what happened.

## Step 2: Understand What Was Lost

- Which tables and records are affected?
- Was data deleted, overwritten or corrupted?
- When exactly did it happen?
- Which legitimate changes have happened since then?
- Are files in storage affected as well?

Logs, audit tables and the migration history help answer these questions. If your app has an audit log, deleted records and their values may even be visible there.

## Step 3: Check Your Recovery Options

| Option | What it offers | Considerations |
| --- | --- | --- |
| Soft-deleted records | Records marked as deleted but still in the table | Instant restore, if your app uses soft delete |
| Audit log or history tables | Previous values recorded by triggers | Can rebuild specific records |
| Daily backups | Snapshot of the database once a day, retained for a period depending on plan | Restore point may be many hours before the incident |
| Point-in-time recovery | Restore to a specific moment within the retention window | Available as an add-on on paid plans; very precise |
| Your own exports | Logical dumps you created, for example before migrations | Only as current as the last export |

Supabase describes backups and point-in-time recovery in its platform documentation, including which plans include daily backups and how long they are retained. Check the current details for your plan and project, ideally before any incident.

## Why a Full Restore Is Risky

Restoring the entire database to a point before the incident sounds like a clean solution. It also removes everything that happened after that point: new sign-ups, orders, payments recorded through webhooks, messages and edits. For an app with active users, that can be worse than the original problem, and it creates inconsistencies with external systems such as your payment provider.

A full restore is appropriate when the whole database is corrupted, the incident is very recent and little legitimate activity happened since, or the damage is so widespread that selective recovery is impractical. Otherwise, recover selectively.

## Selective Recovery

The safer approach for most accidental deletions:

1. **Restore a backup or point-in-time copy into a separate project,** or obtain a database dump from the backup, without touching production. Check Supabase's current options for restoring to a new project or downloading backups.
2. **Find the missing data** in the restored copy: the deleted rows, with their IDs and related records.
3. **Export those rows,** including child records that were deleted through cascades.
4. **Check for conflicts** with data created since, such as reused unique values.
5. **Reinsert into production** in a controlled way, ideally through a script reviewed by someone else, within a transaction.
6. **Verify** with counts and spot checks, and confirm with affected users.
7. **Delete the temporary copy** when done, because it contains production data.

This preserves all legitimate activity while restoring what was lost.

## Cascading Deletes

Many AI-generated schemas use `on delete cascade`, so deleting one record silently deletes all related records: deleting a client removes their projects, invoices and documents. When recovering, find all affected child records in the restored copy, not only the parent. And review cascades afterwards, as described in our guide on [soft delete vs hard delete](https://launchstudio.eu/en/blog/soft-delete-vs-hard-delete-in-saas).

## Files in Storage

Database backups cover database data. Files in Supabase Storage, such as uploaded documents and images, are stored separately, and their recovery depends on how storage is configured and backed up. Metadata about files lives in the database, but the file contents do not. If files were deleted, check whether you have your own copies or versioned storage, and plan file backups explicitly if files matter to your business.

## After Recovery: Learn and Prevent

Once data is restored, find the root cause and prevent recurrence:

- **Soft delete** for important business records, with a trash and restore feature
- **Restrict delete permissions** in Row Level Security, so ordinary users cannot hard-delete important data
- **Confirmations for destructive actions,** with a summary of what will be affected
- **Review migrations,** especially those generated by AI tools, before they run in production; watch for `drop table`, `drop column` and broad `delete` statements
- **Separate environments,** so experiments and AI agent sessions run against staging, not production
- **Audit logs** that record deletions with actors and values
- **Point-in-time recovery** enabled for production databases with important data
- **Tested restores:** practise selective recovery at least once, so you know the steps before an emergency

## Practising a Restore Before You Need It

The worst time to learn how restores work is during an incident. A restore drill, done once or twice a year, turns recovery into a routine:

1. **Pick a realistic scenario,** such as "a customer's project and all its tasks were deleted yesterday at 14:00".
2. **Restore a backup or point-in-time copy** into a separate project, following Supabase's documented steps.
3. **Locate the data** and export the affected rows, including related records.
4. **Reinsert into staging,** not production, using a reviewed script.
5. **Time each step** and write down what was unclear or slow.
6. **Update your runbook** with the exact steps, commands and contacts.
7. **Delete the temporary project** afterwards.

Founders who have practised once typically recover from real incidents in hours rather than days, and make fewer mistakes under pressure.

## Keeping Your Own Exports

Platform backups are essential, but an independent copy adds resilience: regular logical exports of the database to storage you control, encrypted and retained for a defined period, and copies of important files. These protect against scenarios such as account access problems or mistakes that are only discovered after the platform's backup retention window has passed. Treat these exports as sensitive data, with the same access control and retention discipline as production.

## Communicating With Users

If users lost data, tell them what happened, what you recovered, what could not be recovered and what you changed to prevent it. If the incident involved personal data being lost or made unavailable, consider whether it counts as a personal data breach under GDPR, which includes loss of availability, and whether notification obligations apply. Our guide on [GDPR breach response](https://launchstudio.eu/en/blog/gdpr-data-breach-response-the-72-hours-for-a-small-saas) explains the assessment.

## Recovering From Overwritten Data

Not all data loss is deletion. Sometimes values are overwritten: a bulk update without a filter sets every customer's status to inactive, or a sync job replaces addresses with empty values. Recovery follows the same principle: restore a copy from before the incident into a separate project, compare affected columns with production, and write back only the changed values for affected rows, leaving later legitimate changes intact. Audit or history tables, if your app records previous values, can make this much faster.

## Common Causes of Data Loss in AI-Built Apps

| Cause | Example |
| --- | --- |
| AI-generated migration | An agent drops and recreates a table to "simplify" the schema |
| Cascading delete | Deleting a duplicate client removes all its projects |
| Bulk action bug | A "delete selected" button deletes everything when nothing is selected |
| Sync job error | An integration overwrites local data with empty values from an external system |
| Missing filter | An update without a filter changes every row |
| Manual SQL in production | A quick fix in the SQL editor with an unintended scope |
| Seed or test script | A reset script runs against production instead of staging |

Most of these are preventable with environments, reviews and least-privilege access.

## Who Should Be Able to Restore

Restoring production data is a powerful action. Limit it to a small number of people with MFA-protected accounts, require a second person to review restore and reinsert scripts, and record every restore in an operations log with the reason and outcome.

## How LaunchStudio Helps

LaunchStudio helps founders recover from data loss and prevent it: assessing the incident, restoring backups or point-in-time copies to separate projects, recovering specific records including cascaded data, reinserting safely and then implementing soft delete, restricted permissions, audit logs, migration reviews, separate environments, file backup strategies and tested restore procedures.

The **Launch Ready** package (€800-€3,500) covers recovery support and preventive safeguards; **Launch & Grow** (€2,500-€7,500 plus €49 per month) includes managed hosting with backups, monitoring and priority support, so incidents are handled quickly. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, operating and recovering production databases for enterprise clients. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Migration That Dropped the Orders Table

Thomas Brink built Bloemenabonnement with Cursor and Supabase: a subscription service delivering fresh flowers weekly to offices and homes in Utrecht. While asking an agent to add a delivery note field, the agent decided to restructure the orders table and generated a migration that dropped and recreated it. Thomas ran it directly against production on a Tuesday afternoon. Around 14,000 past orders and the current week's deliveries disappeared.

He was on a paid plan with daily backups but without point-in-time recovery. The last backup was from early that morning. A full restore would have removed the new orders placed since then, payments recorded through Mollie webhooks and several new subscriptions. Thomas's first instinct was to restore everything immediately.

LaunchStudio advised against a full restore. The latest daily backup was restored into a separate project, and the orders table, along with order lines deleted through a cascade, was exported from it. Orders created after the backup were reconstructed from Mollie payment records and webhook logs, which had been stored in a separate table. The data was reinserted into production in a reviewed transaction, with counts verified per day and spot checks against delivery lists. The new delivery note field was added with a proper additive migration. Afterwards, point-in-time recovery was enabled, migrations moved to a reviewed pipeline with staging, destructive statements were flagged automatically, and a restore procedure was documented and tested.

**Result:** All historical orders and that week's deliveries were restored by the next morning, and no customer missed a delivery. Thomas has since run dozens of migrations through the reviewed pipeline without incident.

> *"The agent was trying to be helpful. I learned that the database needs a gate between a good idea and production."*
> - **Thomas Brink, Founder, Bloemenabonnement (Utrecht)**

**Cost & Timeline:** €2,300 (Launch Ready package: emergency selective recovery, data reconstruction, migration pipeline, PITR setup and restore procedure) - recovery within 18 hours, safeguards completed in 5 business days.

## Frequently Asked Questions

### Can I undo a delete in Supabase?

Not directly with an undo button. If your app uses soft delete, records can be restored immediately. Otherwise, recovery depends on backups: daily backups on paid plans and point-in-time recovery if enabled. Selective recovery from a restored copy is usually safer than restoring the whole project.

### What is point-in-time recovery?

Point-in-time recovery lets you restore a database to a specific moment within a retention window, rather than only to the last daily backup. On Supabase it is available as an add-on on paid plans. It is valuable for production databases where losing hours of data would be costly.

### Are files in Supabase Storage included in database backups?

Database backups cover database contents, including metadata about files, but not the file contents in storage. If files are important to your business, plan separate backups or versioning for them.

### How does Manifera's experience help with data recovery?

Manifera has operated and recovered production databases for enterprise clients for 11+ years. LaunchStudio applies that experience to recover lost data selectively, without rolling back legitimate activity, and to put safeguards in place so it does not happen again.

### Does data loss affect my app's reputation?

Yes. Customers who lose data often lose trust quickly, and incidents can lead to negative reviews and public discussion. A fast, transparent recovery and visible improvements limit the damage and influence how customers, search engines and AI answer engines later describe your reliability.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I undo a delete in Supabase?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not with an undo button; use soft delete, daily backups or point-in-time recovery, preferably selectively from a restored copy." }
    },
    {
      "@type": "Question",
      "name": "What is point-in-time recovery?",
      "acceptedAnswer": { "@type": "Answer", "text": "Restoring to a specific moment within a retention window; an add-on on paid Supabase plans." }
    },
    {
      "@type": "Question",
      "name": "Are files in Supabase Storage included in database backups?",
      "acceptedAnswer": { "@type": "Answer", "text": "No, only metadata; plan separate backups for files." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with data recovery?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has recovered enterprise databases for 11+ years and LaunchStudio recovers selectively and adds safeguards." }
    },
    {
      "@type": "Question",
      "name": "Does data loss affect my app's reputation?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; fast, transparent recovery limits damage to trust and reputation." }
    }
  ]
}
</script>
