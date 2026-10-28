---
Title: "Lovable Supabase: CSV Imports That Do Not Corrupt Your Data"
Keywords: lovable supabase, CSV import, Excel import, data validation, staging table, bulk upload, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Supabase: CSV Imports That Do Not Corrupt Your Data

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: CSV Imports That Do Not Corrupt Your Data",
  "description": "Every B2B customer starts by importing a spreadsheet, and the import is where clean databases go to die. Encodings, Dutch number formats, Excel's damage, a staged pipeline with preview and rollback, deduplication, and the security issues hidden in a CSV file.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-11",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-supabase-csv-imports-that-do-not-corrupt-your-data" }
}
</script>

Nobody starts using a B2B product with an empty database. The first thing a new customer does is bring their existing data: clients from the old system, products from a spreadsheet, members from an Excel file somebody has maintained since 2014. The import feature is the customer's first real experience of your product, and it is the single fastest way to fill a clean database with garbage.

AI tools build imports that work on the sample file used to test them. Real files arrive in the wrong encoding, with semicolons instead of commas, Dutch decimal commas, dates in three formats, phone numbers missing their leading zeros, duplicate rows, and a column called "Opmerkingen" that contains line breaks. An import that inserts each row directly into production tables turns every one of those quirks into a data problem that is difficult to find and harder to undo.

This article covers the whole path from file to database: parsing what Dutch customers actually send, the formats that silently change meaning, a staged pipeline with preview and rollback, deduplication, large files, and the security issues hidden in an innocent-looking spreadsheet.

## What Dutch Customers Actually Send

The file your customer exports from their old system or saves from Excel is not the RFC 4180 CSV your parser was tested on.

**The delimiter is often a semicolon.** Excel with Dutch regional settings uses the comma as the decimal separator, so it saves "CSV" with semicolons between fields. A parser that assumes commas reads each line as one enormous field - or, worse, splits on the commas inside amounts.

**The encoding is often Windows-1252.** Files saved by older Excel versions and many legacy systems are not UTF-8. Read as UTF-8, "Hélène" becomes "HÃ©lÃ¨ne" and "€" becomes garbage. Files saved as "CSV UTF-8" from modern Excel start with a byte order mark that, unhandled, ends up glued to the first column name - so the column `naam` is not found because it is actually `﻿naam`.

**Fields contain line breaks and quotes.** An address or a note spanning two lines, wrapped in quotes, with quotes inside it doubled. Splitting the file on newlines before parsing breaks these rows in half.

**Header rows vary.** Column names in Dutch or English, with trailing spaces, different capitalisation, sometimes two header rows, sometimes none.

The response is to never hand-write a parser. Use a maintained CSV library, detect the delimiter by inspecting the first lines, detect the encoding - or, simpler, ask the user and default to the most likely - strip the byte order mark, and normalise header names (trim, lowercase) before matching.

Better still, accept `.xlsx` directly. Reading the spreadsheet format with a library avoids delimiter and encoding problems entirely, and it is what most customers have anyway; CSV is often just the format they were told to convert to.

## Formats That Silently Change Meaning

Parsing errors are visible: rows fail, columns are missing. The dangerous errors are the ones where a value is read successfully and means something different.

**Numbers.** "1.250,00" is twelve hundred and fifty in Dutch. A parser using English conventions reads it as 1.25, or fails, depending on the library. "1,250" is one and a quarter in Dutch and one thousand two hundred and fifty in English. Decide the expected format per import - from the user's locale or an explicit choice - and reject values that do not match it rather than guessing.

**Dates.** "03-04-2028" is the third of April in the Netherlands and the fourth of March in the United States. "3-4-28" adds a century question. Excel may also have exported the date as a serial number, such as 46115. Accept an explicit set of formats, parse strictly, and show the interpreted date in the preview so the customer can see "3 april 2028" and confirm it.

**Leading zeros.** Excel strips them from anything it believes is a number. Phone numbers lose their 0, article codes "00451" become 451, KvK numbers and some postcodes change. Treat these columns as text by definition, never infer them as numbers, and validate their length - a Dutch mobile number has ten digits.

**Long numbers.** IBANs survive because they contain letters. Long numeric identifiers do not: Excel converts anything above fifteen digits to scientific notation and loses precision permanently. If a customer's file contains "8,71234E+15", the original value is gone; detect the pattern and reject the row with an explanation rather than storing the wrong number.

**Booleans and enumerations.** "Ja", "ja", "J", "1", "waar", "yes", "x". Map an explicit set of accepted values to your codes and reject the rest - and remember the internationalisation article's rule that statuses are stored as codes, not as Dutch words.

## The Staged Pipeline

The structural fix for imports is to never write directly into production tables. Every robust import follows the same five stages.

**1. Upload.** The file goes to storage, a row is created in an `import_batches` table with the organisation, the user, the filename and a status. Nothing has touched the data yet.

**2. Parse and map.** The file is parsed and the customer maps their columns to your fields - "Klantnaam" to `name`, "Postcode" to `postal_code`. Remember the mapping per organisation, because they will import the same export again next month.

**3. Validate into staging.** Each row is written to a staging table with its parsed values and a list of errors and warnings. Validation is the same as for a form - required fields, formats, ranges, references to existing records - plus import-specific checks such as duplicates within the file.

```sql
create table import_rows (
  batch_id uuid not null references import_batches(id) on delete cascade,
  row_number int not null,
  raw jsonb not null,             -- the original values, untouched
  parsed jsonb,                   -- normalised values
  errors text[] not null default '{}',
  warnings text[] not null default '{}',
  action text,                    -- 'create' | 'update' | 'skip'
  target_id uuid,                 -- matched existing record, if any
  primary key (batch_id, row_number)
);
```

**4. Preview.** The customer sees a summary - 812 rows will be created, 64 updated, 23 have errors - and can inspect each error and each update. Errors can be downloaded as a file with the original row and the reason, fixed in Excel and re-uploaded. This is the stage that turns a silent problem into a visible one.

**5. Commit.** Only on confirmation are the valid rows written to production tables, in a transaction, with every created or updated row tagged with the batch ID. The batch records its outcome: counts, duration, and who confirmed it.

The preview is not a nicety. It is the point at which "1.250,00 read as 1.25" becomes a line on screen saying "Huur: € 1,25" that a human notices before eight hundred tenants are charged it.

## Decide What Happens to Bad Rows

Two policies are defensible, and the import should state which it uses.

**All or nothing.** If any row has an error, nothing is imported until the file is corrected. Appropriate for financial data, opening balances, anything where a partial import produces inconsistent totals.

**Valid rows proceed.** Correct rows are imported, rows with errors are reported for correction. Appropriate for contact lists, product catalogues and most master data, where a partial import is useful and the remainder can follow.

What is not defensible is the default AI-generated behaviour: insert rows one by one, stop at the first error, and leave the first half of the file imported with no record of where it stopped. The customer re-uploads the corrected file and imports the first half twice.

## Deduplication and Updates

Customers import the same data more than once - a corrected file, next month's export, a second branch's list. An import that only creates records produces duplicates every time.

Decide on a matching key per entity: an external identifier from the source system if there is one, otherwise a natural key - email for contacts, article number for products, postcode plus house number plus addition for addresses. Store the external identifier in its own column with a unique constraint per organisation, and use it to upsert:

```sql
insert into clients (organisation_id, external_ref, name, email, import_batch_id)
select organisation_id, parsed->>'external_ref', parsed->>'name', parsed->>'email', batch_id
from import_rows where batch_id = $1 and action in ('create', 'update')
on conflict (organisation_id, external_ref) do update
  set name = excluded.name, email = excluded.email, import_batch_id = excluded.import_batch_id;
```

Show matched records in the preview as updates, with the fields that will change. And decide whether empty cells in the file mean "leave unchanged" or "clear this field" - the safe default is the former, because a column the customer did not export should not wipe data they entered in your product.

Duplicates within the file itself - the same client twice because two branches both listed them - are flagged during validation, not silently merged.

## Undo Is a Feature

Every row written by an import carries its batch ID. That makes the most valuable import feature possible: undoing a batch.

For a batch that only created records, undo deletes those records - provided nothing else has started referring to them, which the database's foreign keys will tell you. For a batch that updated records, undo requires the previous values, which is a reason to store them in the staging row before committing.

Offer undo for a limited period - a day, a week - and to administrators. It converts "we imported the wrong file" from a support emergency into a button, and it is the strongest argument for the staged design.

## Large Files and Timeouts

A file of five hundred rows can be processed in a request. A file of fifty thousand cannot, and it meets the timeout described in the background work article in this series halfway through.

Process imports as background jobs. The upload returns immediately with the batch ID; a worker parses and validates in chunks of a few hundred rows; the interface polls the batch status and shows progress. Commit in chunks inside a single logical operation, with the batch status recording how far it got so that a retry continues rather than restarts.

Set explicit limits: a maximum file size, a maximum number of rows per import, and a sensible number per organisation per day. State them on the import screen. A customer who hits a limit with a clear message splits the file; one who hits a timeout with a generic error emails support.

## Security in a Spreadsheet

Imports are an input like any other, and they come with risks of their own.

**Organisation scoping.** Imports often run with the service role, which bypasses row level security. Every write must set the organisation from the batch - which comes from the authenticated user - never from a column in the file. A file with an `organisation_id` column must not be able to place data in someone else's account.

**Formula injection.** A cell beginning with `=`, `+`, `-` or `@` is executed as a formula when the data is later exported and opened in Excel: `=HYPERLINK("https://evil.example","Klik hier")`. Store the value as text, and when exporting, prefix such cells with an apostrophe so spreadsheet software treats them as text. The data exports article in this series covers the export side.

**File size and content.** Limit the size, check that the file actually is CSV or XLSX rather than trusting the extension, and process it outside the request path, as the file upload articles in this series describe.

**Personal data.** An import file often contains more personal data than your product needs - a full export from an old CRM with dates of birth and notes. Import only mapped columns, delete the uploaded file after the batch is committed or abandoned, and keep the staging rows only as long as undo requires.

## Test With Nasty Files

An import tested with a clean sample file is untested. Keep a folder of deliberately difficult fixtures and run them in CI:

- A semicolon-delimited Windows-1252 file with é, ë and €.
- A UTF-8 file with a byte order mark.
- Dutch amounts with thousands separators and decimal commas.
- Dates in three formats, including an Excel serial number.
- Phone numbers and article codes with leading zeros.
- A twenty-digit identifier in scientific notation.
- A note field with line breaks and doubled quotes.
- Duplicate rows, empty rows and a trailing empty line.
- A cell starting with `=HYPERLINK(`.
- A row with an `organisation_id` column pointing at another organisation.

Each fixture has an expected outcome - parsed values, errors, or rejection - and the tests assert it. When a customer's real file breaks something, it becomes a fixture.

## Import Is Onboarding

The technical pipeline is half the work. The other half is that the import is usually the customer's first hour with your product, and how it feels decides a surprising amount about whether they stay.

**Offer a template.** A downloadable XLSX with your columns, an example row, and a second sheet explaining each field and its accepted formats. Customers who start from the template produce clean files; customers who start from their old system's export need the mapping step.

**Recognise the common sources.** If most customers come from the same two or three systems - a particular accounting package, a well-known industry tool - save a ready-made column mapping for each. "Importing from Exact? We have mapped the columns for you" removes the most tedious step entirely.

**Write errors for the person fixing the file.** Not `invalid_date at row 412`, but "Row 412: the date '31-02-2028' does not exist. Use the format DD-MM-YYYY." The error file should open in Excel with the original row and a final column explaining what to change.

**Measure it.** Record how many batches are started, how many reach preview, how many are committed and how long each stage takes. An import where half of all batches are abandoned at preview is telling you which validation messages customers cannot act on - and that number is one of the most useful onboarding metrics a B2B product has.

## Setting This Up

For a Lovable product with an import feature, this is typically three to four days: a maintained CSV and XLSX library with delimiter and encoding detection and byte order mark handling, saved column mappings per organisation, explicit number, date and boolean formats with strict parsing, identifier columns treated as text with length validation, a staged pipeline of upload, parse, validate into staging, preview and transactional commit, a stated policy for rows with errors and a downloadable error file, external identifiers with upsert-based deduplication, batch IDs on every imported row and undo within a defined period, background processing with progress and explicit limits, organisation set from the authenticated batch, formula injection neutralised, uploaded files deleted after processing, and a CI suite of difficult fixtures.

LaunchStudio builds this when onboarding is held back by the import. The engineers are Manifera's - eleven years, 120+ engineers, 160+ projects, from Amsterdam and Ho Chi Minh City.

[Send us the worst file a customer has given you](https://launchstudio.eu/en/#contact) and we will tell you what your import does with it.

## Real example

### Rent of One Euro Twenty-Five

Annelies Vos built Huurbeheer in Lovable: rental administration for small housing corporations and property managers, used by 31 organisations managing around 9,500 rental units.

New customers imported their tenants from Excel. The import read each row and inserted it directly; it had been tested with a comma-separated file the founder had made herself.

A new property manager uploaded a semicolon-separated export with Dutch amounts. The parser happened to handle the semicolons but read "1.250,00" as 1.25. The import reported success. The monthly direct debit run collected €1.25 from 214 tenants, and the property manager found out from their bank statement. The same customer had re-imported the file twice while trying to fix a different problem, creating 380 duplicate tenants, and every phone number had lost its leading zero.

Three business days: an XLSX and CSV parser with delimiter and encoding detection; explicit Dutch number and date formats per import, rejecting values that did not match; phone numbers, postcodes and house number additions treated as text with length checks; a staged pipeline with a preview showing interpreted amounts and dates and a downloadable error file; upsert on the source system's tenant number, with empty cells leaving existing values unchanged; batch IDs on every row and undo for seven days; background processing with progress for files above five hundred rows; organisation scoping from the batch rather than the file; formula neutralisation on export; and a CI suite of fourteen difficult fixtures, including the original file.

**Result:** the 214 tenants were collected correctly the following week and the 380 duplicates merged using the source system's tenant number. In the next quarter, eleven new organisations imported their data; the preview caught amount or date problems in four of the files before anything was written.

> *"The import said it had worked. Our customer found out from their bank that two hundred and fourteen tenants had paid one euro twenty-five in rent."*
> - **Annelies Vos, Founder, Huurbeheer (Zwolle)**

**Cost & Timeline:** €3,600 (robust CSV and XLSX parsing, explicit Dutch formats, staged import with preview and error files, upsert-based deduplication, batch undo, background processing, organisation scoping, formula neutralisation, fourteen-fixture test suite, cleanup of affected data) - completed in 3 business days.

## Frequently Asked Questions

### Why do CSV files from Dutch customers break imports?

Dutch Excel saves CSV with semicolons because the comma is the decimal separator, often in Windows-1252 encoding, with amounts like 1.250,00 and day-first dates. Parsers tested with English-style files misread all of these.

### Should imports write directly to production tables?

No. Parse and validate into a staging table, show the customer a preview with errors and interpreted values, and commit only on confirmation, in a transaction, with a batch ID on every row.

### How do I avoid duplicates when customers import twice?

Store the source system's identifier, or a natural key such as email, with a unique constraint per organisation, and upsert on it. Show matched records as updates in the preview.

### Can an import be undone?

Yes, if every imported row carries its batch ID and previous values are kept for updates. Offering undo for a limited period turns a wrong import into a button rather than a support emergency.

### What is CSV formula injection?

A cell starting with `=`, `+`, `-` or `@` that runs as a formula when the data is later opened in Excel. Store such values as text and prefix them with an apostrophe on export.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why do Dutch CSV files break app imports?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They use semicolons, Windows-1252 encoding, decimal commas and day-first dates, which parsers built for English files misread."
      }
    },
    {
      "@type": "Question",
      "name": "Should a CSV import write directly to production tables?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No - validate into a staging table, show a preview with errors, then commit in a transaction with a batch ID on each row."
      }
    },
    {
      "@type": "Question",
      "name": "How can repeated imports avoid creating duplicates?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use an external or natural key with a unique constraint per organisation and upsert on it, showing matches as updates."
      }
    },
    {
      "@type": "Question",
      "name": "Can a data import be rolled back?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, when every imported row carries its batch ID and previous values are stored, allowing a time-limited undo."
      }
    },
    {
      "@type": "Question",
      "name": "What is CSV formula injection?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cells starting with =, +, - or @ that execute as formulas in Excel; store them as text and prefix with an apostrophe on export."
      }
    }
  ]
}
</script>
