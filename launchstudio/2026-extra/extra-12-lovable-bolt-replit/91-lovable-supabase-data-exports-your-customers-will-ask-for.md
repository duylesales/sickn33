---
Title: "Lovable Supabase: Data Exports Your Customers Will Ask For"
Keywords: lovable supabase, data export, data portability, CSV export, account export, GDPR, exit clause, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable Supabase: Data Exports Your Customers Will Ask For

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Data Exports Your Customers Will Ask For",
  "description": "Customers ask how they get their data out before they sign, during audits and when they leave. The four kinds of export a B2B product needs, how to design files people can actually use, and why an export button is also the largest data leak in your product.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-13",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-supabase-data-exports-your-customers-will-ask-for" }
}
</script>

There is a question that comes up in almost every serious B2B sale, usually from procurement rather than the person who wants the product: "If we stop using this, how do we get our data out?"

It comes up again during audits, when an accountant needs a year of transactions, when an inspector asks for every record of a certain kind, and when a customer's own reporting team wants to combine your data with theirs. And it comes up, unavoidably, on the day a customer leaves.

AI-built products typically have an export button on one or two screens that downloads the current page as a CSV with internal column names. That answers none of the questions above. When the real request arrives, the founder writes a query by hand on a Saturday, and a hand-written query run against a multi-customer database is how one company's data ends up in another company's inbox.

Exports are a trust feature, a sales feature and a compliance feature at the same time - and an export button is also the single most efficient way to extract everything from your product, which makes it a security feature too. This article covers what customers actually need, how to build it, and how to keep it from becoming the leak.

## Four Kinds of Export

Customers mean different things by "export", and a product that serves B2B customers for long enough needs all four.

**View export.** The list on screen - filtered, sorted - as a spreadsheet. "Give me this month's overdue invoices in Excel." The most frequently used and the easiest to build well.

**Full account export.** Everything the organisation has in your product: every entity, every relationship, every uploaded file, in a structure another system could import. This is what procurement means by "getting our data out", and what a departing customer needs.

**Scheduled export.** The same report delivered automatically - every month to the accountant, every week to a shared drive. It replaces a recurring manual task and a recurring support request.

**Programmatic access.** An API or a direct feed for customers who want to integrate. The API versioning article in this series covers this; here it is enough to note that it is the export option larger customers eventually prefer.

## Designing Files People Can Use

An export is only useful if the person who opens it can work with it. Most exports fail here rather than in the code.

**Use the customer's words, not your column names.** `created_at`, `org_id` and `status_code` mean nothing to an office manager. Headers should match what the interface calls things - "Factuurdatum", "Klant", "Status" - in the user's language, with internal identifiers included as clearly labelled extra columns for those who need them.

**Prefer XLSX for people, CSV for systems.** An XLSX file stores numbers as numbers and dates as dates, so Excel displays them correctly in any locale and the customer can sum a column immediately. A CSV opened in Dutch Excel needs semicolons as separators and a UTF-8 byte order mark to show accented characters - the same issues as the CSV import article in this series describes, in reverse. Offer both; default to XLSX in the interface.

**Write values, not codes.** Status `paid` becomes "Betaald" in the export, translated as the internationalisation article in this series describes. Include the code as well in full account exports, where another system may need it.

**Keep amounts exact.** Export money as a number with two decimals and a separate currency column, not as a formatted string like "€ 1.250,50", which a spreadsheet treats as text and cannot add up.

**Include identifiers that connect files.** A full export of invoices and clients must let someone match each invoice to its client. Every file includes the record's ID and the IDs it refers to.

**Respect the filters on screen.** A view export of "Amsterdam, last month" exports exactly that - not the first page of it, and not everything. AI-generated exports often export only the rows currently loaded in the browser: page one of fifty.

## The Full Account Export

The export that answers the procurement question has a specific shape.

A ZIP archive containing one file per entity - clients, invoices, invoice lines, appointments, users - in both CSV and JSON, all uploaded documents in folders named by the record they belong to, a manifest listing every file and its row count, and a short README explaining the structure, the relationships between files and the meaning of each status code.

```
export-acme-2028-03-13/
  README.txt
  manifest.json
  clients.csv          clients.json
  invoices.csv         invoices.json
  invoice_lines.csv    invoice_lines.json
  documents/
    invoices/8f3c.../factuur-2028-0142.pdf
```

Three properties matter.

**Complete.** Everything the organisation created, including archived and soft-deleted records still within retention, and the files - not only the database rows. An export without the uploaded documents is the export customers complain about.

**Consistent.** Generated from a single point in time, so that an invoice in the export does not refer to a client that was added a minute later and missing from the clients file. A database snapshot or a read inside one transaction achieves this.

**Re-importable.** The test of a full export is whether it can be imported - into your own product for a new organisation, or into a reasonable alternative. Run that round trip in a test, and the export will stay usable as the schema changes.

## Exports Are Background Jobs

A view export of a few hundred rows can be generated during the request. A full account export of a customer with five years of data and four gigabytes of documents cannot.

Treat large exports as jobs, as the background work article in this series describes: the request creates an export record and returns, a worker generates the file in the background, and the user is notified - in the product and by email - when it is ready. The email contains a link to the product, not the file.

Store the generated archive in private storage and deliver it through a signed URL that expires after a day or two, as the storage articles in this series describe. Delete the archive after a week. An export sitting indefinitely in a bucket is a complete copy of a customer's data waiting for a misconfigured policy.

## The Export Button Is the Largest Leak in Your Product

Every other data exposure in a product leaks something. An export leaks everything, in a convenient format, in one click. That deserves deliberate controls.

**A permission of its own.** Not every member who can see invoices should be able to export all of them. Use a specific permission - `data.export`, and for full account exports `data.export_all` - as the roles and permissions article in this series describes. Accountants and administrators typically hold it; most staff do not need it.

**Row level security still applies.** Exports run through the same policies as the screens. If the export is generated by a background job with the service role, the job must apply the organisation and the requesting user's permissions explicitly - the service role bypasses every policy, and a job that forgets this exports the entire database.

**Audit every export.** Who exported what, with which filters, how many rows, when. Visible to the organisation's administrators. A former employee who exported the full client list on their last day is a common story, and the audit is how the customer finds out.

**Rate and size awareness.** An unusual pattern - a member exporting everything repeatedly, or a sudden full export from an account that never exports - is worth an alert to the organisation's owner.

**Formula neutralisation.** Values beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe in spreadsheet exports, so that data entered by one user cannot execute as a formula in another user's Excel. The CSV import article covers the mechanism.

**No personal data in email attachments.** Send a link to the product, behind sign-in, rather than the file. An attachment is forwarded, archived and backed up in places you do not control.

## Never Export by Hand

The most dangerous export in an AI-built product is the one that is not a feature: the founder running a SQL query in the Supabase dashboard because a customer asked for something the product cannot produce.

The dashboard runs with full privileges. A query that forgets `where organisation_id = ...`, or joins through a table that is not scoped, returns rows from every customer. Saved as a CSV and attached to an email, it is a data breach with the founder's name on it.

The rule is simple: if a customer needs data the product cannot export, build the export - even a rough one - rather than running a query. If an exception is truly unavoidable, have a second person review the query and the row count before anything is sent.

## Individual Requests Versus Organisation Exports

Two legal regimes ask for data, and they are easy to confuse.

**The organisation's data** belongs to your customer, under your agreement. Your processing agreement typically commits you to returning it on request and at the end of the contract, in a usable format. The full account export is how you fulfil that.

**An individual's personal data**, under GDPR's rights of access and portability, belongs to the person. When an employee of your customer, or a person whose data your customer stores, asks for their data, the request normally goes to your customer as the controller, and your role is to help them answer it. That means being able to export everything about one person - across entities - not only everything about one organisation. The data breach and deletion articles in this series describe the surrounding obligations.

Build the person-level export as a filter on the same machinery: the same files, restricted to records concerning one person.

## The Exit Clause

Larger customers will ask you to commit, in the contract, to what happens when they leave. Having the full account export makes the answer easy to give and easy to keep.

A reasonable clause: on termination, the customer can generate a full export for thirty days; after that period you delete their data from production within a further thirty days and from backups as they expire; on request you confirm deletion in writing. Write it down once, put it in your standard terms and your processing agreement, and point to the export feature as the mechanism.

This is one of the cheapest ways to win a procurement conversation. "You can export everything yourself, at any time, in an open format" is a sentence that removes the vendor lock-in objection before it is raised.

## Scheduled Exports

The same customers who ask for a one-off export usually ask for the same thing next month.

A scheduled export is a saved export definition - entity, filters, format - with a schedule and a destination. The destination is usually a set of recipients who receive a link, occasionally a shared drive or SFTP location for larger customers. Run it as a scheduled job with the monitoring the cron article in this series recommends, so a failed monthly export is noticed by you rather than by the accountant at the end of the quarter.

Each run is recorded in the export audit, like any other export.

## When Customers Want a Feed, Not a File

Larger customers eventually stop wanting files at all. Their reporting team uses Power BI or a data warehouse, and they want your data to arrive there every night without anyone downloading anything.

There are three ways to meet that, in increasing order of effort.

**A stable export URL.** A scheduled export written to a fixed, private location that their tooling fetches - an authenticated endpoint returning the latest file, or a shared storage location under their control. Cheap, and enough for most.

**Incremental exports.** Instead of the full dataset every night, only rows created or changed since the last run, identified by an `updated_at` column with an index and a record of the last successful export. Deletions need care: either soft deletes that the export includes, or a separate list of removed IDs, so the customer's copy does not keep records you have deleted - which matters under GDPR as much as for accuracy.

**An API.** The full answer, with authentication, pagination and versioning, as the API versioning article in this series describes.

Whatever the mechanism, define the columns as a contract. A customer's dashboard that breaks because you renamed a column in the export is a support incident, and it is avoided the same way as for an API: add columns freely, never rename or remove them without notice, and document the format alongside the product.

## Testing Exports

Three tests catch most problems.

**Scope.** Generate a full export for organisation A and assert that no row and no file belongs to organisation B. Run it for a user without the export permission and assert it is refused.

**Round trip.** Export an organisation, import the export into a fresh organisation, and compare. This keeps the full export complete as tables and columns are added.

**Spreadsheet behaviour.** Open a generated XLSX in a test and check that amounts are numbers, dates are dates, accented characters survive, and a cell beginning with `=` is text.

## Setting This Up

For a Lovable product, this is typically two to four days: view exports that respect the on-screen filters and export all matching rows rather than the loaded page, XLSX as default with typed numbers and dates and CSV with semicolons and a byte order mark for Dutch Excel, headers in the customer's language with identifiers included, a full account export as a background job producing a consistent ZIP of CSV and JSON files plus documents, manifest and README, a person-level export for GDPR requests, scheduled exports with monitoring, dedicated export permissions, organisation and permission scoping applied explicitly in background jobs, an export audit visible to administrators, formula neutralisation, delivery by expiring signed link rather than attachment, automatic deletion of generated archives, an exit clause in your terms, and tests for scope, round trip and spreadsheet behaviour.

LaunchStudio builds this when procurement starts asking how customers get their data out. Behind it is Manifera - eleven years, 160+ projects, 120+ engineers, from Herengracht 420 in Amsterdam.

[Ask us what your export button actually exports](https://launchstudio.eu/en/#contact).

## Real example

### A Saturday Query and the Wrong Company's Guards

Wendy Kramer built Opleidingsportaal in Lovable: training records and certificate tracking for private security companies, used by 22 companies with around 4,100 security officers.

The product had an export button on the officers list that downloaded the rows currently on screen - the first 25 - as a CSV with internal column names and dates in ISO format. Certificate PDFs could not be exported at all.

When one customer's auditor asked for every officer's training history and certificates for the previous three years, Wendy wrote a query in the Supabase dashboard on a Saturday, exported the result and emailed it. The query joined certificates to officers through a table she had not filtered by organisation. The file contained 1,900 rows, of which 640 belonged to officers at two other security companies - names, dates of birth and certificate numbers.

Three business days: a full account export built as a background job, producing a ZIP with CSV and JSON per entity, every certificate PDF in a folder per officer, a manifest and a README; view exports rebuilt to export every matching row with Dutch headers, typed dates and XLSX as default; a person-level export for individual requests; new `data.export` and `data.export_all` permissions held by administrators only; organisation and permission scoping applied explicitly in the export job with a test asserting no cross-organisation rows; an export audit visible to each company's administrators; delivery by signed link expiring after 48 hours and deletion of archives after seven days; and a rule, written into the operations page, that no customer data is ever exported by hand from the dashboard.

**Result:** the incident was assessed as a personal data breach and reported to the two affected companies and to the Autoriteit Persoonsgegevens within the 72-hour window; the recipient confirmed deletion in writing. The auditor received the correct export, generated by the customer themselves, the following week. Two security companies later cited the self-service export and the exit clause in their procurement decisions.

> *"I wrote one query on a Saturday because the product could not do what the auditor asked. It joined through a table I had not filtered, and six hundred and forty officers from two other companies were in the file."*
> - **Wendy Kramer, Founder, Opleidingsportaal (Apeldoorn)**

**Cost & Timeline:** €3,200 (full account export with documents, rebuilt view exports, person-level export, export permissions, scoping tests, export audit, signed delivery and archive expiry, breach assessment support) - completed in 3 business days.

## Frequently Asked Questions

### What kinds of export does a B2B product need?

View exports of filtered lists, a full account export of everything the organisation holds, scheduled exports for recurring reports, and eventually programmatic access through an API.

### Should exports be CSV or Excel?

XLSX for people, because numbers and dates keep their types in any locale. CSV for systems, with semicolons and a UTF-8 byte order mark if it will be opened in Dutch Excel.

### What should a full account export contain?

One file per entity in CSV and JSON, all uploaded documents, identifiers linking the files, a manifest and a README - generated consistently from one point in time.

### Why are exports a security risk?

An export extracts everything in one click. Give it its own permission, apply organisation scoping explicitly in background jobs, audit every export, and deliver files through expiring links rather than email attachments.

### Is it acceptable to export data by hand for a customer?

No. Dashboard queries run with full privileges, and a missing filter sends one customer's data to another. Build the export feature instead.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What data exports should a B2B SaaS offer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "View exports of filtered lists, a full account export, scheduled exports, and eventually programmatic API access."
      }
    },
    {
      "@type": "Question",
      "name": "Should exports be CSV or Excel files?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "XLSX for people because types survive in any locale; CSV for systems, with semicolons and a UTF-8 BOM for Dutch Excel."
      }
    },
    {
      "@type": "Question",
      "name": "What belongs in a full account export?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "One CSV and JSON file per entity, all documents, linking identifiers, a manifest and a README, generated from a single point in time."
      }
    },
    {
      "@type": "Question",
      "name": "Why are data exports a security risk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They extract everything at once; protect them with dedicated permissions, explicit scoping, audit logs and expiring download links."
      }
    },
    {
      "@type": "Question",
      "name": "Can I export customer data by hand from the database?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No - dashboard queries bypass all access controls and a missing filter leaks other customers' data. Build the export feature."
      }
    }
  ]
}
</script>
