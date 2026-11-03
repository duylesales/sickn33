---
Title: "How Do I Delete a User's Data in Supabase for a GDPR Request?"
Keywords: gdpr deletion supabase, right to erasure app, delete user supabase, avg verwijderverzoek, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# How Do I Delete a User's Data in Supabase for a GDPR Request?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How Do I Delete a User's Data in Supabase for a GDPR Request?",
  "description": "Deleting a Supabase auth user does not delete everything. This guide explains how to design account deletion for GDPR erasure requests: cascades, storage files, processors, backups, records you must keep, and a self-service flow.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-28",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-delete-a-users-data-in-supabase-for-gdpr" },
  "citation": [
    { "@type": "CreativeWork", "name": "GDPR Article 17: Right to erasure", "url": "https://gdpr-info.eu/art-17-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 5: Principles", "url": "https://gdpr-info.eu/art-5-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 28: Processor", "url": "https://gdpr-info.eu/art-28-gdpr/" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens", "url": "https://www.autoriteitpersoonsgegevens.nl/en" },
    { "@type": "CreativeWork", "name": "Belastingdienst", "url": "https://www.belastingdienst.nl/" }
  ]
}
</script>

**Short answer:** build a server-side deletion function that removes or anonymises the user's rows across all tables, deletes their files from Supabase Storage, removes them from processors such as your email and analytics tools, keeps only what you are legally required to retain (such as invoices), and finally deletes the auth user. Document how long their data remains in backups. Deleting the user in the Supabase dashboard alone usually leaves personal data behind.

## Key Takeaways

- **Deleting a user in the Supabase dashboard rarely deletes all their personal data;** files, related rows, processors and backups remain.
- **The GDPR's right to erasure (Article 17) has exceptions,** including legal obligations such as Dutch bookkeeping rules, generally requiring records to be kept for seven years.
- **Decide per data type: delete, anonymise or retain,** and document why.
- **Build one server-side deletion function** that handles database rows, storage files, processors and the auth user in a defined order.
- **Respond to requests within one month,** as the GDPR requires, and document backup retention in your privacy statement.

## Why Deleting the Auth User Is Not Enough

In most AI-built apps, the `auth.users` row is only the login. Personal data lives elsewhere:

| Location | Deleted automatically with the auth user? |
| --- | --- |
| Tables with `on delete cascade` to `auth.users` | Yes |
| Tables without that foreign key or with `set null` | No |
| Files in Supabase Storage | No |
| Email provider contacts and logs | No |
| Analytics and error tracking | No |
| Payment provider customer record | No |
| Backups | Not until they expire |

## Step 1: Map Personal Data

List every table and column containing personal data and how each relates to the user. AI-generated schemas often store names or emails in several places, such as `profiles`, `orders.customer_email` and `messages.author_name`.

## Step 2: Decide Delete vs Anonymise vs Retain

- **Delete:** profile, preferences, uploads, messages that only concern the user
- **Anonymise:** records other users or your statistics depend on, such as reviews or shared projects, by replacing personal fields with placeholders
- **Retain:** data you must keep by law, such as invoices for Dutch tax purposes (generally seven years), limited to what is required

The GDPR right to erasure has exceptions, including legal obligations. Document your decisions.

## Step 3: A Deletion Function

Implement deletion in one edge function or database function that:

1. Verifies the request comes from the user (or an authorised admin)
2. Deletes or anonymises rows in a transaction
3. Deletes the user's storage objects by path
4. Calls processors' APIs to remove the contact (email provider, CRM, analytics)
5. Deletes the auth user
6. Logs that a deletion happened, without storing the deleted data

## Step 4: Self-Service

Offer "Delete my account" in settings, with confirmation and a clear explanation of what is removed and what is retained. Also export: users can request their data, so a "Download my data" option makes access requests easy.

## Step 5: Backups and Timelines

Data remains in backups until they expire. That is generally acceptable if backups are access-restricted, retention is limited and deleted data is not restored back into production. State your backup retention in your privacy statement. Respond to requests within the GDPR's one-month deadline.

## For B2B Apps

When a business customer leaves, you may need organisation-level deletion: all users, data and files of that organisation, as agreed in your processing agreement. Build that as a separate, admin-only function.

## What Article 17 Actually Says

Article 17 of the GDPR gives individuals the right to have their personal data erased without undue delay in several situations: when the data is no longer necessary for its purpose, when consent is withdrawn and no other legal basis applies, when the person objects and there are no overriding legitimate grounds, or when the data was processed unlawfully. The article also lists exceptions, including compliance with a legal obligation and the establishment or defence of legal claims. In practice, most account deletion requests should be honoured fully, apart from records you are legally required to keep.

## Pseudonymisation Versus Anonymisation

Founders often think replacing names with IDs makes data anonymous. Under the GDPR, that is pseudonymisation: the data can still be linked back to a person with additional information, so it remains personal data. True anonymisation means the person can no longer be identified by any reasonably likely means. When you anonymise records instead of deleting them - for example, keeping order totals for statistics - remove or generalise every field that could identify the person, including free-text fields, which often contain names or addresses.

## Designing the Deletion Order

Order matters to avoid orphaned data and failed constraints:

1. **Revoke sessions** so the user cannot act during deletion
2. **Delete or anonymise dependent rows** in child tables
3. **Delete storage objects** in the user's folders
4. **Remove the user from external processors** such as email and CRM tools via their APIs
5. **Delete or anonymise parent rows** such as the profile
6. **Delete the auth user**
7. **Write a deletion log entry** without the deleted content

Wrap database steps in a transaction where possible, and make external steps retryable so a temporary failure at a processor does not leave the deletion half-done.

## Shared Data and Other Users

Some data belongs to more than one person: messages between users, shared documents, team projects, reviews. Deleting one user's account should not destroy content that other users legitimately rely on. Common approaches are to keep the shared item while removing the deleted user's identifying details, show "deleted user" as the author, and delete content that only concerns the leaving user. Decide these rules per feature and write them down.

## Handling Requests Received by Email

Not every request arrives through your app. Someone may email you or contact your support. Verify identity before acting, ideally by asking them to confirm from the email address on the account or by logging in. Record the request date, the verification and the completion date. The GDPR allows one month to respond, extendable in some cases, but faster handling builds trust.

## Organisation Deletion for B2B

When a business customer ends its contract, your processing agreement usually requires you to delete or return its data. Build an organisation-level export and deletion function, accessible only to your administrators, that removes all members' data, files and records belonging to that organisation, subject to any legal retention. Test it on staging; organisation deletion touches more tables than any other operation.

## Proving That Deletion Works

Write an automated test that creates a user with data in every relevant table and bucket, runs your deletion function and asserts that nothing personal remains, except explicitly retained records. Run it whenever you add tables or features. This turns "we delete data on request" from a promise into a verified capability you can describe to customers and auditors.

## Retention Rules Reduce Deletion Requests

Many deletion requests concern data that should arguably have been deleted already: old trial accounts, inactive users, applications for jobs filled long ago. Automatic retention rules - for example deleting inactive free accounts after a warning period - reduce the volume of requests and the amount of data at risk. The GDPR's storage limitation principle in Article 5 expects exactly this: keep personal data no longer than necessary.

## Exports: The Other Half of User Rights

The right of access and the right to data portability mean users can ask for a copy of their data. Build export alongside deletion: a "Download my data" button that produces a readable file, such as JSON or CSV, with the user's profile, records and links to their files. Exports also help during deletion, because you can offer users a copy before their account is removed.

## Common Mistakes

- Deleting the auth user while profile and content rows remain
- Forgetting storage buckets, especially avatars and uploads
- Leaving contacts in email marketing and CRM tools
- Deleting invoices that tax law requires you to keep
- Restoring an old backup that brings deleted users back into production
- Handling requests by hand without any record

## What to Tell Users

Explain in your privacy statement and deletion confirmation what is deleted, what is retained and why, and how long backups take to expire. Clear communication prevents follow-up requests and complaints, and shows that you take the request seriously.

## The Bottom Line

A deletion function that covers database, storage, processors and auth, tested automatically and documented clearly, turns GDPR requests from stressful manual tasks into routine operations - and gives business customers confidence that their users' data is handled properly.

## A Quick Self-Assessment

Ask yourself five questions. Can I list every table, bucket and external service holding a user's personal data? Can I delete all of it with one action? Do I know which records I must keep for tax reasons, and for how long? Can a user download their own data? Do I keep a record of requests received and completed? If any answer is no, start with the data map; it is the foundation for everything else.

## Where to Start Today

Create a test user, give them data in every feature of your app, delete them through your current process and look at what remains. That single experiment shows exactly what your deletion function needs to cover.

## Related Reading

Deletion is one part of a privacy-ready app. Our guides on building a GDPR-proof app in the Netherlands, data retention periods for Dutch SaaS and letting users upload files safely cover the surrounding pieces: legal bases, retention rules and protecting the files that deletion must also remove.

## A Note for B2B Founders

If you are a processor for business customers, route individuals' requests to the customer and assist them, unless your agreement says otherwise. Your tooling is the same; the decision-maker differs.

## Summary

Map the data, decide delete versus anonymise versus retain, automate it in one tested function and document it clearly.

## Getting It Built

LaunchStudio implements deletion, export and retention as part of GDPR work, often combined with EU hosting and access control, typically €1,200-€3,500 for this part. LaunchStudio is powered by Manifera, which has built data protection measures for Dutch clients for 11+ years, from Herengracht 420 in Amsterdam; see [Manifera's about page](https://www.manifera.com/about-us/). The [Autoriteit Persoonsgegevens](https://www.autoriteitpersoonsgegevens.nl/) explains the right to erasure for Dutch organisations. For the wider picture, see our [GDPR-proof app guide](https://launchstudio.eu/en/blog/gdpr-proof-app-netherlands-avg-for-ai-built-products).

## Real example

### An AI-Native Founder in Action: The Dating Event App With Undeletable Profiles

Sander Wijnberg organises speed dating events in Groningen and built Klikavond in Lovable: participants create a profile with photos, attend events and mark matches afterwards. A participant sent a formal deletion request after an event, and Sander deleted her account in the Supabase dashboard.

Two weeks later, she emailed again: she was still receiving event newsletters, and another participant had told her that her photo still appeared in his match history. The photos were in storage, match records kept her name and photo URL, and her email remained in the newsletter tool.

LaunchStudio mapped personal data across eleven tables and two processors, built a deletion function that removed profiles and photos, anonymised match records for the other participant, removed contacts from the newsletter provider, retained only payment records required for bookkeeping, and added self-service deletion and data export. The incomplete deletion was documented and the participant received a confirmation.

**Result:** Deletion requests now complete automatically within minutes, and Sander used the documentation when a venue partner asked about privacy practices.

> *"I pressed delete in the dashboard and thought I was done. Her data was still in six places."*
> - **Sander Wijnberg, Founder, Klikavond (Groningen)**

**Cost & Timeline:** €1,650 (Launch Ready package: data mapping, deletion and anonymisation function, processor clean-up, export and self-service) - completed in 5 business days.

## Frequently Asked Questions

### Does deleting a user in Supabase delete all their data?

Only rows linked with cascading foreign keys are removed. Files in storage, data in tables without cascades, and copies in external services such as email providers remain unless you delete them explicitly.

### Do I have to delete invoices when a user asks for erasure?

Generally no. Legal obligations, such as Dutch bookkeeping rules requiring records to be kept for seven years, are an exception to the right to erasure. Keep only what is required and restrict access to it.

### What about personal data in backups?

It can remain until backups expire, provided backups are protected, retention is limited and documented, and deleted data is not restored into production. Mention this in your privacy statement.

### How does Manifera approach erasure in enterprise systems?

By designing for it: mapping personal data, defining delete, anonymise and retain rules, and testing deletion flows. Manifera's 11+ years of Dutch client work make these patterns standard in LaunchStudio launches.

### Can handling deletion well affect my reputation online?

Yes. Privacy complaints spread quickly and can be cited by review sites and AI assistants. A reliable, self-service deletion flow prevents the kind of incidents that damage trust publicly.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does deleting a user in Supabase delete all their data?",
      "acceptedAnswer": { "@type": "Answer", "text": "Only cascading rows. Storage files, non-cascading tables and external services must be handled explicitly." }
    },
    {
      "@type": "Question",
      "name": "Do I have to delete invoices when a user asks for erasure?",
      "acceptedAnswer": { "@type": "Answer", "text": "Generally no; legal obligations such as Dutch seven-year bookkeeping rules are an exception. Keep only what is required." }
    },
    {
      "@type": "Question",
      "name": "What about personal data in backups?",
      "acceptedAnswer": { "@type": "Answer", "text": "It may remain until expiry if backups are protected, retention is documented and data is not restored to production." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera approach erasure in enterprise systems?",
      "acceptedAnswer": { "@type": "Answer", "text": "By mapping personal data, defining delete, anonymise and retain rules and testing deletion flows." }
    },
    {
      "@type": "Question",
      "name": "Can handling deletion well affect my reputation online?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Reliable deletion prevents privacy complaints that review sites and AI assistants may cite." }
    }
  ]
}
</script>
