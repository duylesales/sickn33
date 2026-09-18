---
Title: "Replit File Uploads: Where User Files Should Live"
Keywords: Replit, file uploads, object storage, signed urls, ai app security, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Replit File Uploads: Where User Files Should Live

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Replit File Uploads: Where User Files Should Live",
  "description": "File uploads are where three problems meet: durability, access control and cost. Why files must not live beside your code, how signed links work, what to validate, and what deletion means under GDPR.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-08",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/replit-file-uploads-where-user-files-should-live" }
}
</script>

Adding file upload to a project takes about four minutes and works immediately. That is the problem. The generated version writes the file next to your application, gives it a predictable name, serves it back through a public address, and accepts whatever the browser sent. Four separate decisions, none of which you made, all of which will matter.

Uploads are where three distinct problems intersect — durability, access control and cost — and they are the part of an AI-built product most likely to contain something genuinely serious, because the files people upload are rarely trivial. Invoices, identity documents, medical referrals, contracts, photographs of somebody's house.

## Why Files Beside Your Code Disappear

The first problem is the simplest to explain and the most common.

A file written into your project's directory lives in that environment. Environments are rebuilt — on redeploy, on restart, on platform maintenance, when you change the run configuration. The rebuild produces a clean copy of your code, and your code does not include the files your users uploaded last Tuesday.

The failure is silent. The application works perfectly; a record in the database points at a file that no longer exists; the customer clicks download and gets an error, usually weeks later, usually when they need the document.

There is a second version of this on any deployment running multiple copies for capacity. A file uploaded to one copy does not exist on the others, so a download succeeds or fails depending on which copy answers. This produces the worst kind of bug report: intermittent, unreproducible, and blamed on the user's browser.

Both have the same fix. Files belong in object storage — a service whose only job is holding files durably, independent of your application's lifecycle.

## Public Buckets and the Guessable Filename

The second problem is access, and it has two halves.

**A public bucket** serves anything in it to anyone who knows the address. Perfectly appropriate for logos and marketing images; catastrophic for customer documents. A generated implementation will frequently make the bucket public because that is what makes the file appear in the browser with the least code.

**A predictable filename** makes the first problem worse. Files stored as `invoice-1041.pdf` invite anyone with an invoice to try `invoice-1042.pdf`. Storing the original filename directly does the same — `contract-VanDijk.pdf` tells a stranger who your customers are.

The combination is a data breach that requires no skill to execute. Use a private bucket, name stored files with a random identifier while keeping the original name as metadata for display, and serve them through signed links.

## How Signed Links Work

A signed link is a temporary, unguessable address to one private file, created by your server after it has confirmed that the person asking is allowed to have it.

Three properties make this the right pattern. The authorisation check happens in your code, where it can consult your data model. The link expires, so a URL that leaks in a forwarded email stops working. And the file itself is never publicly reachable, so there is no address to guess.

Two practical notes. Generate the link at the moment of the request rather than embedding long-lived links in pages or emails, since anything embedded outlives the context it was created for. And make the expiry short — minutes for a download, not days.

## Validating What You Accept

Every upload endpoint accepts input from strangers, and the checks are cheap.

**Size limits, enforced on the server.** A limit in the browser is a suggestion. Without a server-side cap, one person can consume your storage budget in an afternoon.

**Type checks based on content, not filename.** The extension tells you what the uploader wants you to believe. Check the actual file signature and reject what does not match.

**Never trust the filename.** Path characters in a filename are how attackers write files outside the intended directory. Store a generated name and keep the original only as a display label, escaped when rendered.

**Rate limits per account.** Upload endpoints are expensive and are a natural target for abuse.

**Scan or isolate what you serve back.** If users upload files that other users download, you are distributing content you did not create. At minimum, serve from a domain separate from your application and force download rather than in-browser rendering for types that can execute.

## Images Deserve Their Own Pipeline

Photographs from a phone are several megabytes. Serving them unmodified is slow for the visitor and expensive for you, and it is the most common cause of a bandwidth line that climbs without explanation.

Resize on upload, store a small number of variants, serve the smallest that fits the context, and use a modern format where the browser supports it. This is one of the few changes that simultaneously improves perceived speed, search performance and cost.

## Deletion Actually Has to Delete

Under GDPR a person can ask you to erase their personal data, and files are personal data as much as database rows.

The common gap: deleting the record removes the row and leaves the file, orphaned in storage, still retrievable by anyone holding an old link and still yours to account for. Deletion must remove both, and your backups have a retention window that means "deleted" is a process with a defined end rather than an instant.

Write down a retention policy — how long files are kept, what deletion removes, how long backups hold a copy — and implement erasure as a real operation rather than a support request somebody handles by hand. Specifics depend on your data and situation, so verify current requirements rather than relying on a general summary.

## What This Looks Like Done Properly

An upload endpoint that authenticates the caller, enforces a size limit and a content-based type check, stores the file in a private bucket under a random name with the original as metadata, records ownership in the database, generates resized variants for images, serves downloads through short-lived signed links issued after an authorisation check, rate-limits per account, and deletes both row and object when erasure is requested.

That is perhaps a day of work on an existing project, and it converts the most sensitive part of your product from the weakest to an unremarkable one.

## The Cost Side of Files

Storage is cheap and the other two lines are not, which is why file handling shows up on invoices before it shows up anywhere else.

**Transfer costs more than storage.** Holding a file is inexpensive; sending it to people repeatedly is where the money goes. A product serving full-resolution photographs on every page view pays for that resolution every single time, which is the most common explanation for a bandwidth line nobody can account for.

**Caching is the lever.** Files that do not change should be served with instructions telling browsers and intermediate caches to keep them, and anything public and frequently requested belongs behind a content delivery network. Done once, it typically removes most of the repeat transfer.

**Nobody deletes anything.** Files accumulate: old versions, abandoned uploads from forms never submitted, temporary files a process created and forgot, and objects orphaned when their database record was deleted. A year in, a meaningful fraction of what you are paying to store is not reachable by any user.

The remedies are dull and effective. Lifecycle rules that move rarely accessed files to cheaper storage after a defined period and delete genuinely temporary files automatically. A retention policy for old versions, agreed rather than implied. And a periodic reconciliation between database records and stored objects, which finds the orphans in both directions — files with no record, and records pointing at files that no longer exist. The second list is the more alarming one, because each entry is a customer who will eventually click download.

**Watch the interaction with backups.** Storage versioning and backup retention both keep copies, and both are billed. That is a reasonable price for recoverability, and it is worth knowing it is there rather than discovering it as an unexplained line.

Set the lifecycle rules when you set up the bucket. Retrofitting them means deciding what to delete under time pressure while trying to remember which folder meant what — and the honest answer, at that point, is usually that nobody knows, so nothing gets deleted and the bill keeps climbing.

## Fixing Uploads on a Project That Already Has Users

The migration matters as much as the design, because files already exist in the wrong place.

LaunchStudio handles it as bounded work: existing files inventoried and copied into private object storage with ownership recorded, public buckets closed, predictable names replaced, signed-link serving put in place with authorisation checks tested by attempting to fetch another account's file, validation and rate limiting added, an image pipeline introduced, orphaned objects cleaned up, and a retention and erasure policy implemented and documented — with the interface you built left untouched.

The engineers are Manifera's: eleven years of production systems for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City. [Tell us what your users upload](https://launchstudio.eu/en/#contact) and you will get a specific assessment, usually within one business day, or see the [packages](https://launchstudio.eu/en/#packages).

## Real example

### Referral Letters at a Guessable Address

Nadia el Amrani built Verwijzing on Replit: a referral-handling tool used by a general practice and two allied-health clinics in Roosendaal. Doctors uploaded referral letters as PDFs; the receiving clinic downloaded them.

The upload feature had been generated in one session and had worked for seven months. Files were written into the project directory, served from a public path, and named from the patient's surname and a sequence number.

Two things surfaced in the same week. A clinic reported that four older referrals could no longer be downloaded — those files had been written before a redeploy that rebuilt the environment. And a practice manager, checking a link she had been sent, changed the number at the end of the address out of curiosity and was shown a different patient's referral letter.

That second finding was a personal data breach involving health data, and it was handled as one: the feature was taken offline the same afternoon, access logs were examined to establish what had actually been retrieved, and the practice's data protection officer was involved in assessing notification obligations.

Six business days of work: all existing files moved into a private bucket under random identifiers with ownership recorded per clinic; public serving removed entirely; downloads issued through signed links valid for five minutes after an authorisation check, tested by attempting to fetch another clinic's file from a second account; server-side size limits and content-based type validation added; per-account rate limiting added; the four lost files re-requested from the sending practice; access logging added so a future question about retrieval has an answer; and a retention policy written with erasure implemented as a real operation across storage and backups.

**Result:** the log review indicated the exposed pattern had been accessed only by the practice manager who reported it, the clinics remained customers, and the notification assessment was documented rather than improvised.

> *"Somebody changed a number in a web address and saw another patient's referral letter. Nothing had gone wrong technically. That was exactly how I had built it."*
> — **Nadia el Amrani, Founder, Verwijzing (Roosendaal)**

**Cost & Timeline:** €3,400 (storage migration, signed-link serving with authorisation, validation and rate limiting, access logging, retention and erasure implementation) — completed in 6 business days.

## Frequently Asked Questions

### Why do uploaded files disappear from my Replit project?

Because they were written beside your code, inside an environment that gets rebuilt on redeploy or restart. The database row survives and the file does not. Files belong in object storage, whose lifecycle is separate from the application's.

### What is wrong with a public storage bucket?

Anything in it is available to anyone who knows the address, and generated implementations often pair that with predictable filenames — so changing a number in a URL reveals someone else's document. Use a private bucket with random names.

### How should private files be served?

Through short-lived signed links your server issues after confirming the requester is allowed the file. The authorisation check stays in your code, the link expires, and the file itself is never publicly reachable.

### What should I validate on upload?

Size and file type on the server — type by actual content rather than extension — plus a generated storage name instead of the user's filename, and a per-account rate limit. Browser-side limits are suggestions.

### Does deleting a record delete the file?

Not unless you wrote it that way, and orphaned files remain retrievable and remain your responsibility. Erasure must remove the object as well as the row, with a documented retention window covering backups.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why do uploaded files disappear from my Replit project?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They were written beside your code in an environment that gets rebuilt, so the database row survives and the file does not. Files belong in object storage."
      }
    },
    {
      "@type": "Question",
      "name": "What is wrong with a public storage bucket?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Everything in it is reachable by anyone with the address, and predictable filenames mean changing a number in a URL can reveal another customer's document."
      }
    },
    {
      "@type": "Question",
      "name": "How should private files be served?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Via short-lived signed links issued by your server after an authorisation check, so the file is never publicly reachable and leaked links expire."
      }
    },
    {
      "@type": "Question",
      "name": "What should I validate on upload?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Server-side size limits, content-based type checks, a generated storage name rather than the user's filename, and per-account rate limiting."
      }
    },
    {
      "@type": "Question",
      "name": "Does deleting a record delete the file?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Only if you implemented it that way. Erasure must remove the stored object as well as the row, with a documented retention window covering backups."
      }
    }
  ]
}
</script>
