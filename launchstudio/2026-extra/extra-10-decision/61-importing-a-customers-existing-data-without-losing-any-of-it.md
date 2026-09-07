---
Title: "Importing a Customer's Existing Data Without Losing Any of It"
Keywords: CSV import SaaS implementation, data migration onboarding, import validation errors, partial import rollback, encoding problems CSV, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Importing a Customer's Existing Data Without Losing Any of It

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Importing a Customer's Existing Data Without Losing Any of It",
  "description": "Import is the first serious thing a new customer asks your product to do, and the place prototypes fail hardest. What a trustworthy import needs: validation before writing, partial failure handling, encoding and format realities, and why a preview step converts more customers than any feature.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-03-16",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/importing-a-customers-existing-data-without-losing-any-of-it" }
}
</script>

Nobody adopts a business tool from zero. They arrive carrying four years of records in a spreadsheet, an export from the system they are leaving, or a list a colleague maintains, and the first real question they ask your product is whether it can take that in. Import is therefore not a convenience feature — it is the gate between trying your product and using it, and a customer who cannot get their data in will not evaluate anything else you built.

It is also, reliably, one of the weakest parts of an AI-generated product. Ask a code generator for a CSV import and you will get a working demonstration: read the file, loop through the rows, insert each one. That implementation is fine for the tidy file you tested with and fails in a specific, damaging way on the messy file a real customer has — partway through, having already written half the rows, with no clear account of what happened.

## The Failure That Defines Everything Else

Consider the naive loop against a real file of 800 rows, where row 431 has a date in an unexpected format. The import writes 430 records, throws an error, and stops. The customer sees a red message. Their account now contains 430 of 800 records and they have no idea which.

What do they do next? Almost always the wrong thing: fix the file and import again, producing 430 duplicates. Then they either delete everything by hand or abandon the product. This single behaviour — partial writes with no accounting — causes more early abandonment than any missing feature, because it happens at the moment the customer is most invested and least forgiving.

Everything that follows is really about avoiding this one outcome.

## Validate Everything Before Writing Anything

The correct shape is two distinct phases, and it is not much more work than the naive version.

**Phase one reads and checks the entire file without writing a single record.** Every row is parsed, every field validated, every reference resolved. The result is a report: how many rows are valid, how many are not, and precisely what is wrong with each bad one, by row number.

**Phase two writes**, and only after the customer has seen the report and chosen to proceed.

This changes the customer's experience completely. Instead of a partial import and a mystery, they get "742 of 800 rows are ready; 58 rows have problems: 41 have a date we cannot read, 12 are missing an email, 5 duplicate an existing record." That is actionable. They can fix the file, or choose to import the valid rows and handle the rest afterwards.

The write phase then needs its own protection. Either write everything or nothing — a transaction, so a failure halfway leaves no trace — or, for very large files, write in batches while recording exactly which batches completed, so a resumption knows where to continue. What must never happen is an unrecorded partial write.

## The Preview Step Is Worth More Than It Costs

Before the write, show the customer what the first several rows will become in your product's own terms: this column becomes the client name, this becomes the invoice date, this one is being ignored.

This does two things. It catches column mapping mistakes, which are the most common cause of a technically successful import producing nonsense — phone numbers in the postcode field, everything shifted one column because the export had a leading blank. And it builds the confidence needed to press the button at all. Customers hesitate to import their real data into an unfamiliar product precisely because they fear an unrecoverable mess; showing them the result before committing removes that fear better than any reassurance.

Column mapping itself deserves attention. A rigid import that demands headers named exactly as your product expects will be defeated by the first real export, which will call it "Customer Name" rather than "client_name". Let the customer map their columns to your fields, guess sensibly by default, and remember the mapping for next time.

## What Real Files Actually Contain

The gap between test data and customer data is where imports die. A short list of what will arrive, all of which a production-grade import handles as routine.

**Encoding that is not UTF-8.** Files exported from older systems, and anything produced by Excel on a Dutch or German Windows machine, frequently arrive in Windows-1252. Read as UTF-8, names containing é, ü, or ø become mangled characters — or the parse fails outright. Detecting and converting encoding is a solved problem and a required one in Europe.

**Separators that are not commas.** Excel in most European locales writes semicolon-separated files while still calling them CSV, because the comma is the decimal separator. An import that assumes commas will see one enormous column.

**Dates in every conceivable order.** 03/04/2027 is 3 April to your Dutch customer and 4 March to your American one. Guessing is dangerous; ask, or infer and show the interpretation in the preview.

**Numbers with European formatting.** `1.234,56` means one thousand two hundred and thirty-four. Parsed naively, it becomes 1.234 or fails. In a financial product, silently importing a wrong number is worse than failing.

**Duplicates, blank rows, merged headers, and trailing notes.** Real spreadsheets contain a summary row at the bottom, an empty row in the middle, and a column of someone's comments.

Each of these is small individually. Collectively they are why import is real engineering work rather than a loop, and why the version generated from a one-line prompt does not survive contact with a customer's actual file. LaunchStudio, backed by Manifera's 11+ years of production engineering, builds imports that validate first, handle European encodings and formats, and never leave a customer with a half-populated account. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Duplicates, Re-imports, and Undo

Three decisions that must be made explicitly.

**What counts as a duplicate, and what happens then?** Choose a matching field — email, reference number — and a behaviour: skip, update the existing record, or create a second one. Then tell the customer which will happen before they import. Silent duplication is the most common complaint after a second import attempt.

**What happens when the same file is imported twice?** It will happen, usually because the first attempt appeared to fail. Recording a fingerprint of each imported file and warning that it looks familiar prevents most of the damage.

**Can an import be undone?** This is the feature customers value most and prototypes never have. Tagging every record created by a given import allows a single "undo this import" action, which is straightforward to implement if it is designed in and nearly impossible to retrofit once records have been edited. Even without full undo, showing an import history — when, how many rows, by whom — turns an opaque event into something a customer can reason about.

## Large Files and the Timeout Nobody Anticipates

A 50,000-row import will not finish inside a web request. Hosting platforms terminate requests after somewhere between 10 and 60 seconds, and the result is an import that stops halfway with the browser showing an error — the partial-write scenario again, now caused by infrastructure rather than data.

The production answer is to accept the file, hand the work to a background job, and show progress. That requires background job infrastructure, which is a broader capability worth having anyway and which prototypes typically lack entirely.

If you are launching without it, be explicit about the limit: cap file size at whatever genuinely completes in time, say so before upload, and reject larger files with a clear message rather than accepting them and failing. A customer told "files up to 2,000 rows; contact us for larger migrations" will email you. A customer whose 8,000-row file times out silently will leave.

## Real example

### The Import That Half-Worked Eleven Times

Pieter Vandenberghe launched Ledenlijst, a membership-administration tool for Belgian sports clubs, built in Lovable. The import worked flawlessly in testing with a file he had made himself.

The first real customer had 1,240 members exported from Excel on a Dutch-language Windows machine: semicolon-separated, Windows-1252 encoded, dates as DD/MM/YYYY, and a summary row at the bottom. The import read it as one column, failed, and left nothing behind — the visibly better of the two outcomes, as it turned out.

The second customer's file was comma-separated and parsed. It failed on row 380 at a member with no email address, after writing 379 records. She fixed that row and re-imported, producing 379 duplicates. Over two days she made eleven attempts and ended with roughly 3,000 records for a club of 620 members, then asked to cancel.

**Result:** the import was rebuilt with encoding and separator detection, a validate-then-write structure, a mapping and preview step, duplicate matching on email with a stated behaviour, transactional writes, and per-import tagging enabling undo. The customer who had asked to cancel migrated successfully at the second attempt and stayed.

> "My import worked on my file. It turned out that was the only file in the world it worked on."
> — **Pieter Vandenberghe, Founder, Ledenlijst**

**Cost & Timeline:** import rebuild delivered in 4 business days, fixed price.

## Frequently Asked Questions

### Why do imports fail halfway and leave partial data?

Because the common implementation writes each row as it reads it, so any bad row stops the process after earlier rows are already saved. Validating the entire file before writing anything, and writing inside a transaction, prevents it.

### What are the most common problems in real customer CSV files?

Non-UTF-8 encoding from older systems and European Excel, semicolon separators, ambiguous date orders, European number formatting such as 1.234,56, and stray summary or blank rows.

### Should customers be able to undo an import?

Ideally yes, and it is cheap if designed in: tag every record created by an import so all of them can be removed together. Retrofitting undo after records have been edited is considerably harder.

### How large a file can a normal import handle?

Anything that cannot complete within roughly 10 to 30 seconds needs background processing, which usually means a few thousand rows. Without background jobs, cap the file size explicitly and say so rather than letting large uploads fail.

### How should duplicate rows be handled during import?

Decide the matching field and the behaviour — skip, update, or create — and tell the customer before the import runs. Silent duplication after a second attempt is the most common post-import complaint.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Why do imports fail halfway and leave partial data?", "acceptedAnswer": { "@type": "Answer", "text": "Because the common implementation writes each row as it reads it, so a bad row stops the process after earlier rows are saved. Validating the whole file first and writing in a transaction prevents it." } },
    { "@type": "Question", "name": "What are the most common problems in real customer CSV files?", "acceptedAnswer": { "@type": "Answer", "text": "Non-UTF-8 encoding from older systems and European Excel, semicolon separators, ambiguous date orders, European number formatting such as 1.234,56, and stray summary or blank rows." } },
    { "@type": "Question", "name": "Should customers be able to undo an import?", "acceptedAnswer": { "@type": "Answer", "text": "Ideally yes, and it is cheap if designed in by tagging every record created by an import. Retrofitting undo after records have been edited is much harder." } },
    { "@type": "Question", "name": "How large a file can a normal import handle?", "acceptedAnswer": { "@type": "Answer", "text": "Anything that cannot finish within roughly 10 to 30 seconds needs background processing, usually meaning a few thousand rows. Without background jobs, cap file size explicitly." } },
    { "@type": "Question", "name": "How should duplicate rows be handled during import?", "acceptedAnswer": { "@type": "Answer", "text": "Decide the matching field and behaviour — skip, update, or create — and tell the customer before the import runs. Silent duplication is the most common post-import complaint." } }
  ]
}
</script>
