---
Title: "Supabase Storage Costs and CDN for User Files"
Keywords: supabase storage costs, supabase egress, supabase storage cdn, signed urls supabase storage, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Supabase Storage Costs and CDN for User Files

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Supabase Storage Costs and CDN for User Files",
  "description": "User uploads such as photos, documents and videos can quietly become the largest cost and the biggest security risk in an AI-built app. This guide explains how Supabase Storage is billed, why egress matters, how caching and the CDN work for public and private files, how to secure uploads with policies and signed URLs, and practical ways to reduce storage and bandwidth costs.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-02",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/supabase-storage-costs-and-cdn-for-user-files" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase Storage documentation", "url": "https://supabase.com/docs/guides/storage" },
    { "@type": "CreativeWork", "name": "Supabase Storage: Access control", "url": "https://supabase.com/docs/guides/storage/security/access-control" },
    { "@type": "CreativeWork", "name": "Supabase Storage: CDN and caching", "url": "https://supabase.com/docs/guides/storage/cdn/fundamentals" },
    { "@type": "CreativeWork", "name": "Supabase pricing", "url": "https://supabase.com/pricing" }
  ]
}
</script>

Most AI-built apps let users upload something: profile photos, receipts, product images, contracts, inspection photos, course videos. Lovable, Bolt and v0 make this easy with Supabase Storage, and in a demo, a few uploaded files cost nothing and load instantly.

At scale, files behave differently from database rows. They are large, they are downloaded repeatedly, and they accumulate without anyone noticing. Founders are sometimes surprised by a monthly bill dominated by storage egress, the bandwidth used when files are downloaded, or by a security report showing that private documents were reachable by anyone with the link.

This guide explains how Supabase Storage costs work, how caching and the CDN help, how to keep files secure and how to reduce costs without degrading the experience.

## Key Takeaways

- **Storage costs have two main parts:** the amount of data stored and the data transferred out, called egress. For apps with many downloads, egress often dominates.
- **Public buckets can be cached aggressively;** private files need signed URLs or authenticated requests, which affects caching.
- **Storage access is controlled by policies** on storage objects, similar to Row Level Security on tables. Weak policies expose files.
- **Compress and resize images before or during upload,** and serve appropriately sized versions instead of originals.
- **Clean up orphaned files** and define retention, because storage only grows unless you remove things.

## How Supabase Storage Is Billed

Supabase Storage pricing, as listed on its pricing page, includes a quota of storage and egress per plan, with usage-based charges beyond the quota. Image transformations, where available, may be billed separately. The details change over time, so check the current pricing, but the structure matters more than the exact numbers:

| Cost driver | What increases it | What reduces it |
| --- | --- | --- |
| Storage size | Large files, originals kept forever, duplicates, orphaned files | Compression, resizing, retention policies, cleanup |
| Egress | Files downloaded often, large files served to many users, no caching | CDN caching, smaller variants, lazy loading |
| Transformations | Many image size variants generated on demand | Fewer variants, caching transformed results |
| Requests | Very frequent small file operations | Batching, caching |

A useful exercise: estimate monthly egress as average file size multiplied by downloads per month. A 4 MB phone photo viewed 50 times generates 200 MB of egress. Multiply by thousands of photos and the numbers become significant quickly.

## Public vs Private Buckets

Supabase Storage organises files in buckets, which can be public or private.

**Public buckets** serve files to anyone with the URL, without authentication. They suit content that is genuinely public: product images in a webshop, blog images, public profile avatars. Public files can be cached by the CDN effectively.

**Private buckets** require authorisation. Files are accessed either through authenticated requests that pass storage policies, or through signed URLs that grant time-limited access. They suit anything personal or confidential: documents, receipts, medical images, contracts, photos of homes or people.

A common mistake in AI-built apps is putting everything in a public bucket because it makes images "just work". If a bucket contains invoices, identity documents or customer photos, a public bucket means anyone who obtains a URL, through sharing, logs, browser history or guessing a predictable path, can read the file.

## Storage Policies

Access to files in Supabase Storage is controlled by policies on the `storage.objects` table, written like Row Level Security policies. Typical patterns:

- **User folders:** files stored under a path starting with the user's ID, with a policy that allows users to read and write only within their own folder.
- **Organisation folders:** paths starting with an organisation ID, with policies checking membership.
- **Record-linked files:** a metadata table linking each file to a record, with policies checking access to that record.

Policies must cover each operation: upload, read, update and delete. Test them with two ordinary accounts, including attempts to read another user's file by changing the path.

## Signed URLs and Caching

For private files, signed URLs are often the most practical way to display images and offer downloads. Your backend, or the client with the right permissions, creates a URL with an expiry time. Considerations:

- **Short expiry for sensitive files,** such as minutes for identity documents.
- **Longer expiry for less sensitive private files,** such as hours for gallery images, to reduce the number of URL generations and allow some browser caching.
- **Do not store signed URLs in the database** as permanent links; store the file path and generate URLs when needed.
- **Understand caching effects:** each new signed URL is a different URL, so browser and CDN caching are less effective than for public files. Reasonable expiry times balance security and performance.

Supabase's CDN caches files according to cache headers and bucket type; its documentation explains how caching behaves for public and private assets. Set appropriate cache control values when uploading.

## Reducing Image Costs

Images are usually the largest share of storage and egress. Practical measures:

1. **Resize before upload.** Phone photos are often several megabytes and thousands of pixels wide. Resize in the browser to a sensible maximum, such as 2,000 pixels on the longest side, and compress to a modern format.
2. **Serve smaller variants.** Thumbnails in lists, medium sizes on detail pages, originals only when needed. Supabase offers image transformations on some plans, or you can generate variants during upload.
3. **Lazy load images** so only visible images are downloaded.
4. **Strip metadata.** Photo metadata may contain GPS location, which is both a privacy issue and unnecessary bytes.
5. **Cache public images** with long cache durations and versioned paths.

## Large Files and Uploads

For large files, such as videos or long PDFs:

- **Use resumable uploads,** which Supabase Storage supports, so interrupted uploads can continue on mobile networks.
- **Set file size limits** per bucket to prevent abuse.
- **Restrict file types** to what the feature needs, and validate on the server, not only in the browser.
- **Process heavy files in background jobs,** such as video transcoding or PDF processing, rather than in request handlers.
- **Consider specialised services** for video streaming, which handle adaptive bitrate and delivery more efficiently than serving raw files.

## Orphaned Files and Retention

AI-generated upload flows often upload a file first and create the database record afterwards. If the user abandons the form, the file remains. Deleted records may also leave their files behind. Over months, orphaned files accumulate.

Fixes:

- **Track files in a metadata table** linked to records, with status such as pending or attached.
- **Delete files when their record is deleted,** using a backend function or trigger-driven job.
- **Run a scheduled cleanup** that removes pending files older than a day and files without a linked record.
- **Define retention periods** for categories of files, for example deleting event photos 90 days after the event, as agreed with customers or required by your privacy policy.

Retention is also a GDPR obligation: personal data, including photos and documents, should not be kept longer than necessary.

## When to Use External Object Storage

For apps with very high egress, such as media-heavy platforms, external object storage with a CDN can be cheaper. Some providers offer low or no egress fees, which can change the economics significantly for download-heavy workloads. The trade-off is more integration work: you lose the convenience of Supabase Storage policies and need to implement access control and signed URLs yourself.

A hybrid is common: Supabase Storage for documents and moderate-volume private files, external storage with CDN for large public media.

## Designing the Upload Flow Properly

Many storage problems start with the upload flow that an AI builder generated. A robust flow looks like this:

1. **The user selects a file.** The browser checks type and size and shows a clear message if the file is not accepted.
2. **The browser prepares the file:** resizing and compressing images, stripping metadata and, for large files, preparing a resumable upload.
3. **The app creates a pending metadata record** in the database, linked to the user and the record the file belongs to, with a generated file path.
4. **The file is uploaded** to that path, with storage policies verifying that the user may write there.
5. **The server confirms the upload,** validates type and size again, generates any variants and marks the metadata record as attached.
6. **The interface shows the result** using a thumbnail variant, not the original.
7. **A scheduled job removes pending files** that were never confirmed.

Each step addresses a specific problem: invalid files, oversized uploads, orphaned files, unauthorised writes and slow galleries. Together they turn file handling from a hidden liability into a predictable part of the system.

## Monitoring Storage Usage

- Check storage size and egress in Supabase's usage dashboard regularly.
- Set budget alerts or spending caps where available.
- Track the largest buckets and folders, and which features drive egress.
- Watch for sudden egress spikes, which can indicate hotlinking or scraping of public files.

## Common Mistakes

**Everything in a public bucket.** Private documents reachable by anyone with the URL.

**Original photos served everywhere.** Multi-megabyte images in thumbnail lists.

**Signed URLs stored permanently.** Links that stop working, or that last far too long.

**No cleanup.** Orphaned files growing every month.

**Client-side checks only.** File type and size validated in the browser but not enforced.

**GPS metadata left in photos.** Exposes where photos were taken, sometimes users' homes.

## How LaunchStudio Helps

LaunchStudio reviews and improves file handling in AI-built apps: moving private files to private buckets, writing and testing storage policies, implementing signed URLs with appropriate expiry, adding client-side resizing and compression, metadata stripping, image variants, resumable uploads, metadata tables, cleanup jobs and retention rules, plus monitoring of storage and egress.

The **Launch Ready** package (€800-€3,500) covers storage security and optimisation along with deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate. For upload security in more depth, see our guide on [letting users upload files safely](https://launchstudio.eu/en/blog/how-do-i-let-users-upload-files-safely).

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Real Estate Photo App With a Growing Bill

Lieke Mol built Woningfoto with Bolt and Supabase: a tool for estate agents to upload property photos, organise them per listing, share galleries with sellers and export them to listing websites. After a year with 60 agencies, the Supabase bill had grown several times faster than revenue, driven mostly by storage egress.

The review found the causes quickly. Photographers uploaded originals of 8 to 15 MB each, which were stored and served everywhere, including the thumbnail grid of every gallery. Everything was in a public bucket with paths based on listing addresses, so galleries for unsold homes, including interior photos, were reachable by anyone who guessed a path. Photos retained GPS metadata, and photos of withdrawn or sold listings were never deleted. About 30% of storage consisted of orphaned uploads from abandoned forms.

LaunchStudio added browser-side resizing to 2,400 pixels with compression and metadata stripping before upload, and generated thumbnail and medium variants at upload time. Gallery and seller photos moved to a private bucket with organisation-based storage policies and signed URLs valid for a few hours, while photos marked for public listings were copied to a public bucket with long cache durations. A metadata table linked every file to a listing, a nightly job removed orphaned uploads, and photos of sold listings were deleted after a retention period agreed with the agencies.

**Result:** Total storage dropped by about 70%, egress fell by over 80% and the monthly bill returned to a sensible share of revenue. Interior photos of unsold homes are no longer publicly reachable, which two agencies specifically checked before renewing their subscriptions.

> *"I was paying to send fifteen-megabyte photos to thumbnails the size of a stamp, and anyone could see inside my clients' homes. Fixing it saved money and my reputation."*
> - **Lieke Mol, Founder, Woningfoto (Haarlem)**

**Cost & Timeline:** €2,900 (Launch Ready package: image processing, private and public bucket redesign, storage policies, signed URLs, metadata table, cleanup and retention jobs) - completed in 8 business days.

## Frequently Asked Questions

### Why is my Supabase Storage bill so high?

Usually because large files are downloaded often, which drives egress, or because storage grows from originals, duplicates and orphaned files. Resizing and compressing images, serving smaller variants, caching public files and cleaning up unused files typically reduce costs substantially.

### Should my uploads be in a public or private bucket?

Use public buckets only for content intended to be public, such as product images or public avatars. Anything personal or confidential, such as documents, receipts or photos of people and homes, belongs in a private bucket with storage policies and signed URLs.

### How long should signed URLs last?

It depends on sensitivity. Minutes for identity documents and sensitive files, hours for less sensitive private images. Generate URLs when needed rather than storing them, and balance security with the caching benefits of longer expiry.

### How does Manifera's experience help with file handling?

Manifera has built document and media systems for enterprise clients for 11+ years, where security, retention and cost control are essential. LaunchStudio applies that experience to file handling in AI-built apps, which is often where the largest hidden risks and costs sit.

### Do image optimisations help SEO and AI visibility?

Yes. Smaller, properly sized images improve page speed, which supports user experience and search performance. Public images with descriptive alt text and stable URLs also help search engines and AI answer engines understand your content.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why is my Supabase Storage bill so high?",
      "acceptedAnswer": { "@type": "Answer", "text": "Usually egress from frequently downloaded large files, plus growth from originals and orphaned files. Resize, use variants, cache public files and clean up." }
    },
    {
      "@type": "Question",
      "name": "Should my uploads be in a public or private bucket?",
      "acceptedAnswer": { "@type": "Answer", "text": "Public only for intended public content; personal or confidential files belong in private buckets with policies and signed URLs." }
    },
    {
      "@type": "Question",
      "name": "How long should signed URLs last?",
      "acceptedAnswer": { "@type": "Answer", "text": "Minutes for sensitive files, hours for less sensitive private images; generate them when needed rather than storing them." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with file handling?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built enterprise document and media systems for 11+ years, and LaunchStudio addresses file security, retention and cost." }
    },
    {
      "@type": "Question",
      "name": "Do image optimisations help SEO and AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Smaller images improve speed, and public images with alt text and stable URLs help search and AI engines." }
    }
  ]
}
</script>
