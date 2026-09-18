---
Title: "Lovable Supabase: Storage Buckets and Who Can Read What"
Keywords: lovable supabase, storage buckets, signed URLs, file permissions, public bucket risk, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Supabase: Storage Buckets and Who Can Read What

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Storage Buckets and Who Can Read What",
  "description": "The public bucket is the most common data exposure in AI-built apps. How Supabase storage permissions actually work, when signed URLs are the answer, and how to move files to private without breaking your product.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-03",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-supabase-storage-buckets-and-who-can-read-what" }
}
</script>

Ask an AI tool to add file uploads and it will produce something that works within a minute. It creates a bucket, marks it public, uploads the file and stores the resulting URL. Every screenshot, invoice, identity document and medical form your users upload is then readable by anyone who has the address — and the addresses are frequently guessable.

"Public" in Supabase storage does not mean "public to logged-in users". It means a URL that requires no authentication at all: no session, no token, no expiry. The file is on the open internet.

This is the single most common serious finding in security reviews of Lovable applications, and it is entirely a default rather than a mistake anyone made.

## What Public Actually Costs You

Three consequences, escalating.

Anyone with the URL can read the file forever, including after the user deletes their account, because deleting a database row does not remove an object from storage.

URLs leak by ordinary means. They appear in support emails, in browser history, in the referrer header sent to third-party analytics, in screenshots shared in chat, and in any page that renders them. Once a URL exists it travels.

And if filenames are predictable — sequential numbers, user IDs, original filenames — the bucket can be walked. An attacker who finds one document at a guessable path will try the next hundred, and AI-generated upload code names files predictably far more often than not.

For a product handling anything a person would consider private, this is a data breach waiting for someone to notice, with notification obligations attached.

## When Public Is Fine

Not everything needs protecting, and treating every file as sensitive makes your product slower and more complicated than it needs to be.

Public buckets are correct for genuinely public assets: marketing images, logos, public profile pictures on a directory that is itself public, downloadable brochures. Anything a visitor could see anyway.

The test is simple and worth applying file by file. If this object appeared on a search engine, would anyone care? If the answer is no, public is fine and simpler. If the answer is yes — even slightly — it belongs in a private bucket.

Most products end up with both, and that is the right outcome: a public bucket for assets and a private one for everything users upload.

## How Private Buckets Work

A private bucket refuses anonymous access. Files are reached in one of two ways, and choosing between them is the main design decision.

**Through the authenticated client**, where the user's session is checked against storage policies you write — the same kind of conditions as row-level security, but applied to object paths. This suits files displayed inside your application to a logged-in user.

**Through a signed URL**, a temporary address your server generates that works for a defined period and then expires. This suits downloads, email links, and anything a browser must fetch directly, such as an image tag or a PDF viewer.

Signed URLs are generated on the server, never in the browser, because generating one requires credentials that must not be in frontend code. And the expiry should match the use: minutes for an inline image, an hour for a download link, a day at the outside for something emailed. An expiry of a year is a public URL wearing a disguise.

## Path Structure Is Your Permission Model

Storage policies match on the object's path, which makes the path layout the thing that determines whether your rules can be expressed at all.

A good default puts the owner at the front: `organisation-id/user-id/document-id.pdf`. A policy can then say that a user may read objects whose first path segment matches an organisation they belong to, which is a single rule covering every file the product will ever store.

The layout to avoid is a flat bucket of files named after the original upload, which makes ownership unknowable from the path and forces every check to become a database lookup — if it happens at all.

Two more habits. Generate the filename yourself rather than trusting the one the user's computer supplied, both because original names leak information and because they collide. And keep a database row per file recording who uploaded it, when, its path, size and content type, so that the storage bucket is never your only record of what exists.

## Validate Uploads on the Server

The extension in a filename is a claim, not a fact. A file called `photo.jpg` can contain anything at all, and a browser-side check of the file type is trivially bypassed.

What matters on the server: a size limit appropriate to the file type, an allowed list of content types verified from the file's actual contents rather than its name, and a rule that uploaded files are never served back with a content type the uploader controls. The specific danger is an HTML or SVG file served from your domain, which can run script in the context of your application and read whatever your users' sessions can reach.

Storing uploads on a separate domain rather than your application's own removes that class of problem entirely, which is one quiet argument for signed URLs from the storage host rather than proxying files through your own app.

## Moving an Existing Product to Private

The migration is straightforward and worth doing in one sitting, because the intermediate state is worse than either end.

Create the private bucket with its policies. Copy the objects across, rewriting paths into the owner-first layout as you go, and record each file's new path in your database. Change the application to request signed URLs instead of storing permanent ones — this is the part that touches the most code, because permanent URLs tend to have been saved into database columns and embedded in emails already sent.

Then leave the old bucket in place but blocked for a short period while you watch for anything still requesting it, and delete it afterwards.

The thing to check specifically: emails and exported documents that contain old public links. Those keep working after the migration unless you deliberately break them, and they are precisely the links most likely to have been forwarded outside your customer's company.

## Images Are a Special Case

Photographs and screenshots make up most uploads in most products, and they bring two problems that documents do not.

The first is size. A phone photograph is several megabytes, and a page displaying forty of them at thumbnail size while downloading the originals is slow for the user and expensive for you. Generate derivatives — a thumbnail and a display size — at upload time, store them alongside the original, and serve the smallest one that fits the context. Supabase can transform images on request, which is simpler than building a pipeline and adequate for most products.

The second is metadata. Photographs carry EXIF data including, frequently, the GPS coordinates where they were taken. A product where users upload photographs of damage, property, equipment or themselves is a product quietly collecting location history. Strip EXIF on upload unless you have a reason to keep it, and if you keep it, say so in your privacy policy.

One more habit worth adopting: never trust an image's dimensions from the client either. A crafted file claiming to be enormous can exhaust memory in whatever processes it. Set a limit, reject what exceeds it, and handle the failure as a normal outcome rather than an exception that takes down the request.

## Storage Costs Grow Quietly

Unlike a database, storage rarely announces a problem — it simply appears on the invoice.

Three things drive it in AI-built products and all are avoidable. Originals kept forever when only derivatives are ever displayed. Orphans left behind by deleted records, uploads abandoned half-way through a form, and duplicates created when a user re-uploads after a failure. And egress, the cost of serving the same large file repeatedly because nothing is cached.

A monthly count of objects and total bytes, compared against the number of files your database knows about, catches all three. When the two numbers diverge you have orphans, and a cleanup job that removes objects with no corresponding database row — run carefully, with a dry run first — usually reclaims more than founders expect.

## Setting This Up

For an existing app this is typically two to three days: buckets audited and classified, a private bucket created with path-based policies, objects migrated into an owner-first layout with a database row per file, server-side signed URL generation with expiries matched to use, upload validation by actual content type and size, generated filenames, the application updated to stop storing permanent URLs, old public links identified and retired, and a check that deleting a user's record also removes their objects.

LaunchStudio handles this in security work on AI-built products, where it is among the most frequent findings. The engineering comes from Manifera — eleven years, 120+ engineers, and clients including Vodafone, TNO and CFLW who take file handling rather seriously.

[Ask us to look at your bucket settings](https://launchstudio.eu/en/#contact). It takes ten minutes to check and it is usually the first thing we look at.

## Real example

### Twelve Hundred Documents on the Open Internet

Bram Nieuwenhuijs built Hypotheekmap with Lovable: a tool mortgage advisers use to collect documents from clients — payslips, employment contracts, bank statements, identity documents — and pass a complete file to the lender.

Uploads went into a public bucket, named by the client's surname and the document type. The application worked well and 26 advisers were using it with around 400 clients.

A client noticed. He copied the URL of his own payslip, changed the surname in it to a friend's who used the same adviser, and the friend's contract of employment loaded. He emailed Bram, politely, on a Sunday.

Three business days: a private bucket with policies matching the organisation segment of the path; all 1,247 objects migrated to an `adviser-id/client-id/document-id` layout with generated identifiers replacing names, and a `documents` table recording uploader, path, size, type and timestamp; signed URL generation moved server-side with a fifteen-minute expiry for viewing and one hour for download; upload validation by actual content type with a 25 MB limit; the old bucket blocked and then deleted; the 180 previously issued document links that appeared in sent emails invalidated, with advisers notified to re-share from inside the product; and account deletion extended to remove stored objects, which it had never done.

**Result:** the exposure closed within the week. Bram reported the incident to the Autoriteit Persoonsgegevens with a description of the fix, and informed the 26 advisers and the clients whose documents had been reachable. Two advisers said the transparency was the reason they stayed.

> *"He guessed one URL. There was no hacking involved — my file naming was the vulnerability, and I had chosen it because it made the admin screen easier to read."*
> — **Bram Nieuwenhuijs, Founder, Hypotheekmap (Nieuwegein)**

**Cost & Timeline:** €3,300 (bucket migration and policy design, path restructuring, file registry, server-side signed URLs, upload validation, link retirement, deletion handling, incident documentation) — completed in 3 business days.

## Frequently Asked Questions

### Does a public Supabase bucket mean public to my logged-in users?

No. It means readable by anyone on the internet with the URL — no session, no token, no expiry. For anything a user uploads, use a private bucket.

### Are signed URLs safe to email to customers?

Yes, with a sensible expiry. An hour is reasonable for a download link. A signed URL valid for a year is functionally a public URL and should be treated as one.

### Where should signed URLs be generated?

On the server, always. Generating them in the browser requires credentials that must never be in frontend code, and that key grants access to everything in the bucket.

### What is wrong with keeping the user's original filename?

It leaks information, it collides, and predictable names make a bucket walkable. Generate your own identifier and keep the original name in a database column if you need to display it.

### Does deleting a user remove their files?

Not unless you built it. Storage objects and database rows are separate systems, and orphaned files surviving account deletion is both a privacy problem and a growing storage bill.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does a public Supabase bucket mean public to logged-in users?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — it is readable by anyone with the URL, with no authentication or expiry. User uploads belong in a private bucket."
      }
    },
    {
      "@type": "Question",
      "name": "Are signed URLs safe to email to customers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, with a short expiry. An hour suits a download link; a URL valid for a year is effectively public."
      }
    },
    {
      "@type": "Question",
      "name": "Where should signed URLs be generated?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "On the server. Generating them client-side requires credentials that grant access to the whole bucket and must never reach frontend code."
      }
    },
    {
      "@type": "Question",
      "name": "Should I keep the user's original filename?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Generate your own identifier — original names leak information, collide, and make buckets walkable. Store the display name in the database."
      }
    },
    {
      "@type": "Question",
      "name": "Does deleting a user remove their uploaded files?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Only if you built that. Storage and database are separate, and orphaned objects are both a privacy problem and a growing bill."
      }
    }
  ]
}
</script>
