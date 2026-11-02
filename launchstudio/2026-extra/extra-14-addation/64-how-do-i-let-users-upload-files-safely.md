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
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-let-users-upload-files-safely" }
}
</script>

**Short answer:** store user files in a private Supabase Storage bucket, organise paths by organisation or user ID, write storage policies that only allow uploads and reads within the user's own folder or organisation, serve files through short-lived signed URLs, and enforce file size and type limits on the bucket and server side. Use public buckets only for files that are meant to be public, such as product images on a public catalogue.

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
