---
Title: "Supabase Security: Data Deletion and GDPR Erasure in Practice"
Keywords: supabase security, right to erasure implementation, data retention deletion, account deletion flow, ai app security, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Supabase Security: Data Deletion and GDPR Erasure in Practice

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Supabase Security: Data Deletion and GDPR Erasure in Practice",
  "description": "Deletion is easy to promise and hard to implement: referential integrity, copies in third-party services, backups, and the records you are required to keep. A practical guide for AI-built products.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-03",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/data-deletion-and-erasure-in-practice" }
}
</script>

The request is four lines long and entirely reasonable: please delete my account and everything you hold about me. Your privacy statement says you will. Your app has a delete button that removes a row from a users table, and roughly eleven other places still hold that person's information.

Deletion is the clearest example of a promise that is cheap to make in a policy and genuinely involved to implement. It is also the one AI builders never produce, because nothing about describing a product to a tool implies that data should ever go away.

This article is general information rather than legal advice; the scope of any specific obligation depends on facts a lawyer should see.

## What Deletion Actually Has to Reach

Start by listing where one user's data exists in your product. For a typical AI-built application the answer is longer than founders expect.

**The user record itself.** The easy part, and the only part most delete buttons touch.

**Everything they created.** Bookings, listings, messages, uploads, comments. Some of it is theirs alone; some involves other people, which is where it gets interesting.

**Uploaded files,** in storage, which have their own lifecycle and do not disappear when a database row does.

**Third-party copies.** Their email address in your transactional email provider. Their identifier in your error tracker, attached to a stack trace. Their details in your payment provider. Their record in whatever analytics or support tool you added.

**Logs.** Application logs frequently contain identifiers, addresses and sometimes request bodies.

**Backups,** which contain the state of everything at the time they were taken.

A deletion that covers the first item and none of the others is not deletion. It is a hidden account.

## The Parts You Are Allowed — and Sometimes Required — to Keep

Erasure is not absolute, and understanding the exceptions prevents both over-deletion and the panic of believing you must destroy your accounting.

**Transaction records.** Invoices and payment records are generally subject to retention obligations under tax and administrative rules, which in the Netherlands run for a number of years. Those records typically stay, and the appropriate approach is to keep what the obligation requires and remove what it does not.

**Data needed for a legal claim or defence,** kept proportionately and not indefinitely.

**Other people's data.** A message thread between two users, a review of a seller, a shared document — deleting one participant's account does not entitle you to erase content that concerns someone else. Anonymising the departed party is usually the right answer.

**Aggregate figures** that cannot identify anyone.

The design implication is that deletion is rarely a single cascade. It is a set of decisions per data type: delete, anonymise, or retain with a stated basis and period.

## Anonymisation Is Usually the Practical Answer

For anything entangled with other users or with your own records, replacing identifying fields is normally better than removing the row.

A booking becomes an anonymous booking that still counts in a venue's history. A review keeps its text and rating and loses the reviewer's name. A message thread survives with one participant marked as a deleted user.

The important detail: anonymisation has to be real. Replacing a name while leaving the email address, the phone number, the address and a user identifier that links to other records is not anonymisation — it is relabelling. If the remaining fields can identify the person alone or in combination, the data is still personal data.

## The Referential Integrity Problem

Delete a user row that other records point to and your database will either refuse or, worse, leave orphans your application does not expect, producing pages that fail on a missing reference.

This is the practical reason deletion is engineering work rather than a button. Every relationship needs a decision made in advance — cascade, set to null, anonymise, or block deletion until something else is resolved — and those decisions must be expressed in the schema rather than hoped for in application code.

Products that skip this end up with a delete function nobody dares to run, which is how deletion requests start being handled manually and, eventually, not at all.

## Third Parties and Backups, Stated Honestly

**Third parties** each need their own path. Most providers offer deletion of a contact or a record, sometimes via an interface and sometimes via an API. Build this into your deletion routine rather than remembering it, because manual steps do not survive contact with a busy week.

**Backups** are the part founders try to avoid explaining. Deleted data persists in backups until those backups expire. This is normal, accepted practice — the appropriate answer is to state the retention period, ensure restored data is re-deleted if a restore happens, and not claim instantaneous erasure everywhere.

Saying this plainly in your privacy statement is better than a vaguer claim you cannot honour.

## What Good Looks Like in the Product

**A self-service account deletion path,** which some platforms also require of applications they distribute. It is also simply better than an email queue.

**Confirmation and a grace period.** A short window during which the account can be restored prevents both accidental loss and the support burden of recovering it.

**A deletion routine that runs everywhere,** covering database, storage, third parties and logs, in a defined order, recorded when it completes.

**Evidence.** A record that the deletion happened, when, and what was retained and why. That record is itself minimal personal data kept for accountability.

**Retention rules that run automatically** for everything else, so data ages out without anyone remembering to act.

## A Test You Can Run This Week

Create an account, use the product properly — book something, upload a file, trigger an email, cause an error. Then delete the account and go looking.

Is the user row gone? Their files? Their contact in the email provider? Their identifier in the error tracker? Does any page break? Can you still find them by searching your database for the email address?

Nearly every founder who runs this test for the first time finds at least three places. That list is your implementation plan, and finding it yourself is considerably better than a customer finding it for you.

## Building the Deletion Path

This is well-bounded work that produces a permanent answer to a question every business customer eventually asks. LaunchStudio implements it as part of preparing an AI-built product for real customers: a per-data-type decision map of delete, anonymise or retain; schema-level rules so deletion cannot leave orphans; a routine covering storage, third-party services and logs; retention rules that run automatically; a self-service deletion path with a grace period; and the documentation your customers' privacy officers will ask for.

The interface you built in Lovable stays exactly as it is. The engineering comes from Manifera — eleven years of production systems for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City — and it sits inside the [Launch Ready package](https://launchstudio.eu/en/#packages).

If your delete button removes one row, [describe your project](https://launchstudio.eu/en/#contact) and we will map what it actually needs to reach, usually within one business day.

## Retention: Deleting What Nobody Asked You To

Erasure requests are the visible half. The larger half is data that should go away on its own, and this is where AI-built products accumulate liability quietly, because nothing generated ever deletes anything.

**Decide a period per data type.** Accounts inactive for a stated number of years. Support conversations. Application logs. Error reports containing request data. Old exports sitting in storage. Draft records abandoned mid-creation. Each deserves a number, and the number is a business decision rather than a technical one.

**Make it run automatically.** A retention rule that depends on someone remembering is not a retention rule. A scheduled job that reports what it removed is.

**Log what was removed, not what it contained.** Counts and categories, so you can show the process ran without recreating the data you just deleted.

**Warn before deleting accounts.** An email a fortnight before an inactive account is removed prevents an unpleasant surprise and occasionally reactivates a customer.

**Review after the first run.** The first execution of a retention job on a product that has never deleted anything usually removes far more than expected. Run it against a copy first and look at the numbers before letting it near production.

The reason to do this before anyone asks: holding personal data longer than necessary is exactly the sort of thing a privacy review examines, and "we keep everything forever because nobody built deletion" is a weaker answer than a stated period you actually enforce.

## Plan the Undo Before You Build the Delete

Deletion done properly is irreversible by design, which creates a second problem: mistakes.

A customer who deletes an account in frustration and writes back an hour later, a support action taken against the wrong record, a retention job configured with the wrong period — all of these are ordinary, and none of them are recoverable once the data is genuinely gone.

The standard answer is a grace period: mark the record as deleted, hide it from the product immediately so the user experiences deletion, and remove it permanently after a stated interval. Fourteen days is common and any period works provided you state it.

Two details make it honest rather than a loophole. The data must actually be inaccessible during the grace period, not merely hidden behind a flag your queries forget to check. And the interval must be disclosed, because "deleted" meaning "hidden for a fortnight" is something a customer is entitled to know.

## Real example

### A Community Platform Whose Deleted Members Kept Coming Back

Hanneke Doorn ran Buurtkracht, a neighbourhood volunteering platform used by several municipalities' community organisations around Zwolle. Members offered and requested help; some conversations were sensitive.

The delete button removed the user row. Everything else stayed: the person's name remained on every request they had posted, their uploaded photographs stayed in storage at guessable addresses, their email address remained in the transactional email provider and kept receiving digest emails, and their identifier persisted in the error tracker.

Two members noticed. One kept receiving weekly digests six weeks after deleting her account; the other found her name still attached to a request she had posted about a personal situation.

Seven business days of work: a decision map across fourteen data types marking each as delete, anonymise or retain with a basis; schema constraints rewritten so deletion could never orphan a record; requests and offers anonymised rather than removed so the neighbourhood history stayed intact; files deleted from storage with the routine verified; the email provider and error tracker wired into the deletion routine via their APIs; a self-service deletion flow with a fourteen-day grace period; automatic retention removing inactive accounts after a stated period; and a deletion log recording what ran and what was retained.

**Result:** both members received a written explanation of exactly what had been removed and what was anonymised, and the platform passed a data-protection review from a municipality four months later with deletion cited as a strength.

> *"I had written in my own privacy statement that people could have their data deleted. I had built a button that hid their account and left everything else exactly where it was."*
> — **Hanneke Doorn, Founder, Buurtkracht (Zwolle)**

**Cost & Timeline:** €3,400 (deletion map, schema rules, third-party integration, self-service flow, retention automation) — completed in 7 business days.

## Frequently Asked Questions

### Does deleting a user row delete their data?

Almost never. Their uploaded files, their content, their record in your email provider, error tracker and payment provider, and entries in your logs all persist independently. A deletion routine has to reach each one explicitly.

### Do I have to delete everything when someone asks?

No. Records subject to retention obligations, such as invoices under tax and administrative rules, are typically kept, as is data needed to defend a legal claim and content that concerns other people. The right approach is a decision per data type rather than a blanket cascade.

### What about data in my backups?

It persists until the backups expire, which is normal and accepted. State the retention period plainly, and make sure that if a restore happens, previously deleted data is removed again afterwards.

### Is anonymising instead of deleting acceptable?

Often, and it is usually the practical answer for content entangled with other users. It must be genuine: if the remaining fields still identify the person alone or in combination, nothing has been anonymised.

### How do I know my deletion actually works?

Create a real account, use the product fully, delete it, then search every system for that person — database, storage, email provider, error tracker, logs. Most founders find at least three places on the first attempt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does deleting a user row delete their data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Almost never. Files, content, and records in your email provider, error tracker, payment provider and logs persist independently and must each be reached explicitly."
      }
    },
    {
      "@type": "Question",
      "name": "Do I have to delete everything when someone asks?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Records under retention obligations such as invoices are typically kept, as is data needed to defend a claim and content concerning other people."
      }
    },
    {
      "@type": "Question",
      "name": "What about data in my backups?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It persists until backups expire, which is accepted practice. State the retention period and re-delete after any restore."
      }
    },
    {
      "@type": "Question",
      "name": "Is anonymising instead of deleting acceptable?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Often, especially for content entangled with other users, provided it is genuine and the remaining fields cannot identify the person."
      }
    },
    {
      "@type": "Question",
      "name": "How do I know my deletion actually works?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Create a real account, use the product, delete it, then search every system for that person. Most founders find at least three places on the first attempt."
      }
    }
  ]
}
</script>
