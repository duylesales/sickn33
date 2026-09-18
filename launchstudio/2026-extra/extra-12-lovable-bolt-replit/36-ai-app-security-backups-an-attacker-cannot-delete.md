---
Title: "AI App Security: Backups an Attacker Cannot Delete"
Keywords: ai app security, backups, ransomware, immutable storage, restore testing, point in time recovery, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI App Security: Backups an Attacker Cannot Delete

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Security: Backups an Attacker Cannot Delete",
  "description": "A backup reachable with the credentials that run your application is not a backup against a compromise. Separate control, immutability, what to include beyond the database, and proving a restore works.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-24",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-app-security-backups-an-attacker-cannot-delete" }
}
</script>

Most founders think about backups in terms of accidents: a bad migration, a mistaken delete, a hardware failure. Those are real and the platform's automatic backups usually handle them well.

There is a second scenario the automatic arrangement does not handle, and it is now the more common cause of catastrophic data loss at small companies. Somebody obtains your credentials. They do not only take the data — they delete it, and then they delete the backups, because the same account that runs your product can reach both.

The distinction is simple to state. A backup that can be destroyed by whoever compromises your application is a backup against mistakes, not against attacks.

## Separate Control, Not Just Separate Storage

The property that matters is not location. It is who can delete it.

A copy in another region of the same account, deletable with the same credentials, is protection against a regional outage and nothing else. A copy in a separate account or a separate provider, with its own credentials that your application does not hold, is protection against compromise.

For a small product this is not elaborate: a scheduled export to storage in a different account, where the writing credential can create objects but cannot delete or overwrite them. The application can add to the archive and can do nothing else to it.

That write-only property is the whole trick, and it is available on every major object storage service as a permissions policy.

## Immutability Makes It Certain

One step further, and worth taking for anything you would be unable to recover from: object lock, or its equivalent, which prevents deletion for a defined retention period regardless of permissions.

With it enabled, a backup written today cannot be removed for thirty days by anyone — not an attacker with full credentials, not a mistaken script, not you. That is occasionally inconvenient and precisely the point.

Combine the two ideas with a retention rule that keeps daily copies for a month, weekly for a quarter, and monthly for a year, and you have an arrangement that survives both a compromise and the slower problem of corruption that is only noticed weeks later.

## Back Up More Than the Database

The database is where attention goes and it is not the whole product. Four other things matter.

**Uploaded files.** For many products the documents are more valuable than the rows, and object storage often has no automatic backup at all — a deleted object is simply gone.

**Configuration.** Environment variables, provider settings, DNS records, webhook endpoints, scheduled jobs. Not large, and the difference between a restore that takes hours and one that takes days.

**The schema, in a form you can apply.** Your migration files in a repository, which is why they belong there.

**The list of what your product depends on**, so a rebuild does not begin with an inventory exercise.

Write these down as a recovery document. The person doing a restore under pressure — quite possibly you, tired — should be following instructions rather than remembering.

## A Backup You Have Not Restored Is a Hypothesis

The single most common finding when a restore is first attempted is that it does not work: the export was incomplete, the format is unreadable, a required extension is missing, the file has been zero bytes since March because a credential changed and nothing checked.

So test it. Restore to a scratch environment, run the application against it, check that recent records exist and that files referenced by the database are actually present. Time the whole thing.

Twice a year is enough for most products, plus once after any significant change to your infrastructure. Write down the date and the duration. That number — how long a full recovery takes — is the one your business customers will ask for, and it is the one nobody can answer without having done it.

## Know Your Two Numbers

Two questions define what your arrangement must achieve, and answering them turns backup from a vague good intention into a specification.

**How much data can you afford to lose?** If backups run nightly, the answer is up to a day. For a product where customers do a day's work in your application, that is usually too much, and point-in-time recovery — available on most managed database plans — reduces it to minutes.

**How long can you be down?** A restore of a small database takes minutes; a restore that includes reconstructing configuration and re-uploading files can take a day. If the answer needs to be two hours, that shapes what you prepare in advance.

Neither number needs to be impressive. It needs to be known, stated, and consistent with what you tell customers.

## Backups Are Personal Data Too

An archive of your database is a copy of everything your customers gave you, and it inherits every obligation the original carries.

Three consequences that founders meet at awkward moments.

**Encryption.** Backups should be encrypted at rest and in transit, which most services do by default — but verify rather than assume, particularly for exports you wrote yourself to a bucket. The key should not be stored beside the data.

**Access.** Whoever can read a backup can read every record in your product, without any of the controls your application enforces. That access list should be shorter than your production access list, and it should be reviewed.

**Deletion.** When a customer exercises their right to erasure, their data remains in backups. The accepted position is that backups may retain it for a defined retention period, provided you do not restore it into production without re-applying the deletion, and provided the period is stated. What is not defensible is indefinite retention with no policy — which is what a bucket of exports going back three years amounts to.

So write the retention rule and enforce it automatically, keep a note of what your recovery procedure does about erasure requests, and mention backup retention in your privacy documentation. It is a short paragraph, and it is the difference between a considered position and an oversight.

## The Failures Backups Do Not Cover

Two scenarios defeat an otherwise good arrangement, and both are worth a moment's thought because the fix is cheap.

**Corruption you do not notice.** A bug writes wrong values for three weeks. Every nightly backup faithfully preserves the wrong values, and by the time anyone notices, the last clean copy has aged out of retention. This is the argument for a monthly copy kept for a year: not because you expect to need eleven-month-old data, but because the moment of discovery is sometimes far from the moment of damage.

**Deletion that propagates.** A cascading delete removes a customer's records along with everything referencing them, and the backup taken an hour later records the result. Point-in-time recovery helps here where a nightly snapshot does not, which is the main reason to enable it.

Both argue for the same habit: keep the ability to go back further than feels necessary, and be able to restore a single table or a single account rather than only the entire database. A full restore to recover one customer's records means discarding everyone else's work since the backup, which is rarely an acceptable trade and is the position founders find themselves in when the only tool available is all-or-nothing.

Practising a partial restore once — one table, into a scratch database, then copying the rows back — takes an hour and turns the worst kind of incident into an ordinary repair.

## Setting This Up

For an existing product this is typically one day: platform backups confirmed and their retention understood, an independent copy written to storage in a separate account with a write-only credential your application does not hold, object lock or equivalent immutability with a retention schedule of daily, weekly and monthly copies, uploaded files included in the backup, configuration and DNS recorded, migrations in the repository, a written recovery document, a scheduled restore test with the duration recorded, monitoring that alerts when a backup does not appear or is unexpectedly small, and recovery point and recovery time objectives stated.

LaunchStudio sets this up as part of production readiness and runs the restore tests under the managed arrangement at €49 per month. The engineers are Manifera's — eleven years, 160+ projects, and recovery procedures for clients including Vodafone, TNO and CFLW.

[Ask us when you last restored a backup](https://launchstudio.eu/en/#contact). The answer is usually never, and that is the finding.

## Real example

### The Backups Were in the Same Account

Youri Landman built Praktijkdossier in Lovable: client records and session notes for psychology and coaching practices, 64 practitioners with around 3,200 clients.

A practitioner reused a password that appeared in an unrelated breach. The attacker signed in, found the practice administration area, and — because Youri had given practice administrators an export function with broad database access — retrieved a substantial amount of data before deleting records across the practice.

That much was recoverable. What made the evening long was that Youri's only additional backup was a nightly export written to a bucket in the same cloud account as the application, using the same credentials, with a lifecycle rule and no protection. It had not been deleted in this case, but it was reachable, and a slightly more thorough attacker would have removed it.

The restore itself then took eleven hours, because the export contained the database and nothing else. Session note attachments — the most sensitive and least replaceable part of the product — were in a storage bucket that had never been backed up at all, and 340 of them were gone.

Three business days: an independent backup to a separate provider account with a write-only credential the application does not hold; object lock with 35-day immutability and a retention schedule of daily for a month, weekly for a quarter and monthly for a year; uploaded session attachments included, having never been backed up; point-in-time recovery enabled on the database, reducing potential loss from 24 hours to five minutes; configuration, DNS and webhook endpoints recorded in the repository; a written recovery document with numbered steps; a restore test performed and timed at 47 minutes for the full product; monitoring that alerts if a backup does not arrive or is more than 20 percent smaller than the previous one; the export function narrowed so practice administrators can export their own practice rather than query broadly; and two-factor authentication required for administrator accounts.

**Result:** 340 attachments were unrecoverable and the affected clients were informed, which Youri describes as the worst professional experience of his life. The arrangement since would have prevented it: an eleven-hour reconstruction became a 47-minute restore, and the backups are now in a place his own credentials cannot reach.

> *"I had backups. I had them in the same account, with the same keys, and I had never once restored one. What I actually had was a file I hoped was useful."*
> — **Youri Landman, Founder, Praktijkdossier (Utrecht)**

**Cost & Timeline:** €3,300 (independent immutable backup with write-only credentials, retention schedule, file backup, point-in-time recovery, configuration capture, recovery documentation, timed restore test, backup monitoring, export scoping, administrator two-factor) — completed in 3 business days.

## Frequently Asked Questions

### Are my platform's automatic backups enough?

For accidents, usually. For a compromise, no — if the credentials that run your application can also delete the backups, an attacker who takes one takes both.

### What makes a backup safe from an attacker?

Separate control: a different account with a credential that can write but not delete or overwrite, ideally with object lock so removal is impossible during the retention period.

### What gets forgotten in backups?

Uploaded files, which often have no automatic backup at all, plus configuration, DNS records, webhook endpoints and scheduled jobs. The database alone rarely restores a working product.

### How often should I test a restore?

Twice a year and after any infrastructure change. Record the duration — that number is what customers ask for and what you cannot estimate without doing it.

### What are recovery point and recovery time objectives?

How much data you can afford to lose, and how long you can be down. Nightly backups mean up to a day of loss; point-in-time recovery reduces it to minutes.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Are automatic platform backups sufficient?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For accidents yes; for a compromise no. If your application's credentials can delete the backups, an attacker who obtains them can delete both."
      }
    },
    {
      "@type": "Question",
      "name": "What makes a backup resistant to an attacker?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Separate control — a different account, a write-only credential your application does not hold, and object lock preventing deletion during retention."
      }
    },
    {
      "@type": "Question",
      "name": "What is usually left out of backups?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Uploaded files, which often have none at all, plus configuration, DNS, webhook endpoints and scheduled jobs."
      }
    },
    {
      "@type": "Question",
      "name": "How often should a restore be tested?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Twice a year and after infrastructure changes, recording the duration — that figure is what customers ask for."
      }
    },
    {
      "@type": "Question",
      "name": "What are recovery point and recovery time objectives?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "How much data you can lose and how long you can be down. Nightly backups risk a day; point-in-time recovery cuts it to minutes."
      }
    }
  ]
}
</script>
