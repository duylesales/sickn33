---
Title: "How Do I Let Users Upload Files Safely in My AI-Built App?"
Keywords: secure file uploads supabase, lovable file upload, private storage bucket, signed urls supabase, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# How Do I Let Users Upload Files Safely in My AI-Built App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How Do I Let Users Upload Files Safely in My AI-Built App?",
  "description": "File uploads are one of the riskiest features in AI-built apps: public buckets, guessable paths, unlimited sizes and dangerous file types. This guide covers private buckets, storage policies, signed URLs, validation, image processing and retention in Supabase.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-12",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-let-users-upload-files-safely" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Storage access control", "url": "https://supabase.com/docs/guides/storage/security/access-control" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A01 Broken Access Control", "url": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/" },
    { "@type": "CreativeWork", "name": "GDPR Article 32: Security of processing", "url": "https://gdpr-info.eu/art-32-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 17: Right to erasure", "url": "https://gdpr-info.eu/art-17-gdpr/" }
  ]
}
</script>

**Short answer:** store user files in a private Supabase Storage bucket, organise paths by organisation or user ID, write storage policies that only allow uploads and reads within the user's own folder or organisation, serve files through short-lived signed URLs, and enforce file size and type limits on the bucket and server side. Use public buckets only for files that are meant to be public, such as product images on a public catalogue.

## Key Takeaways

- **File uploads are one of the riskiest features in AI-built apps:** public buckets, guessable paths, missing storage policies, unlimited sizes and dangerous file types.
- **Supabase Storage has its own access policies,** separate from table policies; both must be configured.
- **Serve private files through short-lived signed URLs** generated after an ownership check.
- **Validate type and size, be careful with SVG and HTML, and strip metadata** such as GPS location from photos.
- **Files are personal data too:** include them in deletion, retention and backup plans under the GDPR.

## The Risks AI Builders Introduce

| Default in many AI-built apps | Risk |
| --- | --- |
| Public bucket for everything | Anyone with a link can open private documents |
| Predictable file names (`invoice-1043.pdf`) | Links can be guessed |
| No storage policies | Users can overwrite or delete others' files |
| No size limits | Storage costs and abuse |
| Any file type accepted | Malicious files, HTML or SVG with scripts served from your domain |
| Original photos stored as-is | Location data (EXIF) and huge files |

## Step 1: Private Buckets by Default

Create private buckets for anything personal or business-related: documents, contracts, invoices, ID scans, user photos. Public buckets only for content you would also put on your public website.

## Step 2: Structured Paths

Use paths like `org/{organisation_id}/{record_id}/{random-name}.pdf`. Random file names prevent guessing; the organisation prefix lets policies check ownership.

## Step 3: Storage Policies

Storage access is governed by policies on `storage.objects`, separate from your table policies. Allow insert and select only where the path's organisation matches one the user belongs to; restrict delete to owners or admins.

## Step 4: Signed URLs

To display or download a private file, create a signed URL with a short expiry, such as a few minutes, after checking the user's access. Do not store signed URLs permanently in the database; generate them when needed.

## Step 5: Validate Uploads

- Set maximum file size and allowed MIME types on the bucket
- Check type and size again server-side for sensitive flows
- Be careful with SVG and HTML files; serve them as downloads or disallow them
- For images, resize and strip metadata, especially location data from phone photos

## Step 6: Retention and Deletion

Files are personal data too. Delete them when the related record or account is deleted, and define retention periods. Our [GDPR deletion guide](https://launchstudio.eu/en/blog/how-do-i-delete-a-users-data-in-supabase-for-gdpr) covers how storage fits into erasure requests.

## Step 7: Back Them Up

Database backups do not include storage. Back up files that matter, such as contracts and invoices, separately.

## How Supabase Storage Access Control Works

Supabase Storage stores files in buckets and keeps file metadata in a table, `storage.objects`, protected by Row Level Security policies. A bucket can be public, meaning anyone with the URL can download files, or private, meaning access is governed by policies and signed URLs. Supabase's storage access control documentation describes how policies check the bucket, the file path and the user. Because policies can inspect the path, a folder structure such as `org/{organisation_id}/...` lets you write rules like "members of this organisation can read files in its folder".

## The Most Common Upload Vulnerabilities

| Vulnerability | Example | Consequence |
| --- | --- | --- |
| Public bucket for private files | Invoices stored in a public bucket | Anyone with or guessing a link can read them |
| Predictable paths | `/documents/1043/payslip.pdf` | Enumeration of other users' files |
| No upload policies | Any user can write to any folder | Overwriting or planting files in others' folders |
| No type checks | Uploading HTML or SVG with scripts | Script execution on your domain when files are viewed |
| No size limits | Multi-gigabyte uploads | Storage costs and denial of service |
| Long-lived links stored in the database | Signed URLs valid for months | Links shared or leaked remain usable |

OWASP classes several of these under broken access control, the top risk in its web application Top 10.

## Upload Flow Design

A secure upload flow typically works like this: the user selects a file; the app checks size and type in the browser for convenience; the upload goes to a private bucket under a path that includes the user's or organisation's ID and a random file name; a storage policy allows the insert only into that path; a database record links the file to its owner and business object; and processing such as image resizing or metadata stripping happens in a server function before the file is used. Downloads request a signed URL from a function that first verifies ownership.

## Images: Resizing and Metadata

Photos from phones are often large and contain EXIF metadata, including GPS coordinates, device model and timestamps. Storing originals wastes space and can expose where photos were taken, which may reveal home addresses. Resize images to the sizes your app displays, convert to efficient formats and strip metadata on upload. This improves performance and privacy at the same time.

## Dangerous File Types

Some files can execute code or render content in browsers. HTML and SVG files served from your domain can run scripts in your users' sessions. Unless your app needs them, block these types. If you must accept them, serve them with headers that force download rather than display, or from a separate domain. For documents, accept the formats your users actually need, such as PDF and common image types, and reject the rest.

## Virus and Malware Scanning

If users share files with each other, consider scanning uploads for malware, especially for B2B products where files travel between companies. Scanning services and open-source scanners can run in a background function after upload, marking files as clean before they become available to others. For many founder apps this is optional; for document-sharing platforms it is a reasonable expectation.

## Files and the GDPR

Uploaded files often contain the most sensitive personal data in an app: ID scans, payslips, medical letters, contracts. Treat them accordingly. Keep them in EU regions, restrict access to those who need it, include them in data deletion and export features, set retention periods and back them up separately, since database backups do not include storage. Article 32 of the GDPR requires security appropriate to the risk, and few things raise the risk more than identity documents in a public bucket.

## A Practical Bucket Layout

A simple layout covers most apps:

| Bucket | Visibility | Contents | Path pattern |
| --- | --- | --- | --- |
| `public-assets` | Public | Logos, marketing images, public product photos | `/{category}/{file}` |
| `user-files` | Private | Avatars, personal uploads | `/{user_id}/{random}.{ext}` |
| `org-documents` | Private | Contracts, invoices, shared documents | `/{org_id}/{object_id}/{random}.{ext}` |
| `archive` | Private, restricted | Copies of legally required documents | `/{year}/{org_id}/{file}` |

Separate buckets by sensitivity so policies stay simple and mistakes in one bucket do not affect another.

## Migrating Files From a Public Bucket

If private files already sit in a public bucket, migrate them: create a private bucket, copy files with new random names into owner-based paths, update database references, test downloads through signed URLs and then delete the public copies. Check whether the public URLs were shared or indexed; if sensitive documents were exposed, assess your obligations under the GDPR, which may include notifying the Autoriteit Persoonsgegevens within 72 hours.

## Testing Upload Security

Test as two users in different organisations: upload, list, download and delete each other's files through the interface and the API; try uploading disallowed types and oversized files; check that photos no longer contain GPS metadata; confirm signed URLs expire. Automate the cross-organisation download test.

## Summary

Private buckets, owner-based paths, storage policies, signed URLs, validation, metadata stripping and inclusion in deletion and backups: seven habits that turn file uploads from a common breach source into a safe feature.

## Performance and Cost of File Storage

Files drive storage and bandwidth costs. Resize images to the sizes your app displays, compress documents where possible, use a CDN for public assets and set cache headers for files that rarely change. For private files, short-lived signed URLs still benefit from caching within their lifetime. Review storage usage monthly; a single feature that stores original 12-megapixel photos can quietly dominate your bill.

## Common Mistakes

- Using one public bucket for everything because the preview worked
- Saving signed URLs in the database as if they were permanent
- Allowing any file type "for flexibility"
- Forgetting storage when deleting user accounts
- Assuming database backups include files

## Related Reading

See our guides on GDPR deletion in Supabase and on backing up a Lovable app's database for the deletion and backup sides of file handling.

## Questions to Ask Before Building Uploads

Which file types do users really need? How large can files be? Who may see each file, and for how long? Do files need to be shared outside the app? Must any files be kept for legal reasons? Are files scanned before others can open them? Clear answers make policies, limits and retention straightforward to implement and easy to explain to customers.

## The Payoff

Secure uploads protect your users' most sensitive documents and your reputation. They also let you answer customers' storage questions with confidence: private by default, owner-only access, short-lived links and documented retention.

## Where to Start Today

List your buckets and mark each public or private. Any bucket with personal or business documents that is public is your first fix.

## Getting It Fixed

Securing file uploads is one of the most common LaunchStudio fixes, usually one to three days within a Launch Ready package. LaunchStudio is backed by Manifera, trusted by Vodafone, TNO and CFLW, whose engineers build secure document handling for enterprise clients from Amsterdam and Ho Chi Minh City; see [Manifera's portfolio](https://www.manifera.com/portfolio/). Supabase explains [storage access control](https://supabase.com/docs/guides/storage/security/access-control) in its documentation.

## Real example

### An AI-Native Founder in Action: The Rental Application App With Public Payslips

Bart Smulders built Huurdossier in Bolt: tenants applying for rental homes upload ID, payslips and employer statements once, then share a dossier link with landlords. Around 900 tenants in Eindhoven used it within two months.

A landlord noticed that dossier file links looked like `/storage/v1/object/public/documents/1234/payslip.pdf`. Changing the number opened other tenants' payslips. The bucket was public, paths were sequential IDs, and there were no storage policies. Phone photos of ID cards also contained location data showing where they were taken.

LaunchStudio moved all documents to a private bucket with random file names, migrated existing files and updated references, wrote storage policies so tenants could only access their own folder, implemented dossier sharing through time-limited signed links that landlords received via a share page, stripped metadata from images, set size and type limits and added deletion of all files when a tenant closed their account. Bart documented the incident and informed affected users.

**Result:** No file was reachable without authorisation after the fix. Bart added a public page explaining how dossiers are protected, which several landlords mentioned as a reason to accept Huurdossier links.

> *"The whole point of my app was keeping sensitive documents in one safe place. They were in one place. It just wasn't safe."*
> - **Bart Smulders, Founder, Huurdossier (Eindhoven)**

**Cost & Timeline:** €1,950 (Launch Ready package: private storage, file migration, storage policies, signed sharing, metadata stripping, limits and deletion) - completed in 5 business days.

## Frequently Asked Questions

### Are Supabase Storage buckets private by default?

You choose when creating a bucket. Many AI-generated setups create public buckets because they make previews work easily. Check each bucket and make anything personal or business-related private.

### Do my database RLS policies protect uploaded files?

No. Storage has its own policies on `storage.objects`. You need storage policies in addition to table policies, ideally based on the same organisation or user ownership.

### How long should signed URLs be valid?

As short as practical, often a few minutes for viewing or downloading. Generate them on demand after checking access, rather than storing long-lived links.

### Why does Manifera strip metadata from uploaded images?

Because phone photos often contain GPS coordinates and device details. Manifera's security-minded delivery, shaped by Herre Roelevink's cybersecurity background, treats metadata as personal data that should not be stored or shared unnecessarily.

### Can exposed files appear in search engines?

Yes. Public files linked anywhere can be crawled and indexed, and some may later appear in AI-generated answers. Private buckets and signed URLs prevent that.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Are Supabase Storage buckets private by default?",
      "acceptedAnswer": { "@type": "Answer", "text": "You choose at creation; AI-generated setups often make them public, so check and make sensitive buckets private." }
    },
    {
      "@type": "Question",
      "name": "Do my database RLS policies protect uploaded files?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. Storage needs its own policies on storage.objects." }
    },
    {
      "@type": "Question",
      "name": "How long should signed URLs be valid?",
      "acceptedAnswer": { "@type": "Answer", "text": "As short as practical, often minutes, generated on demand after access checks." }
    },
    {
      "@type": "Question",
      "name": "Why does Manifera strip metadata from uploaded images?",
      "acceptedAnswer": { "@type": "Answer", "text": "Phone photos contain GPS and device data, which is personal data that should not be kept unnecessarily." }
    },
    {
      "@type": "Question",
      "name": "Can exposed files appear in search engines?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Linked public files can be indexed; private buckets and signed URLs prevent it." }
    }
  ]
}
</script>
