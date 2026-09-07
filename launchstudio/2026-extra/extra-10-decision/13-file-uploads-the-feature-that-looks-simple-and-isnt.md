---
Title: "File Uploads: The Feature That Looks Simple and Isn't"
Keywords: presigned upload vs proxy upload, MIME type sniffing security, file upload size limits, public storage bucket exposure, secure file uploads, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# File Uploads: The Feature That Looks Simple and Isn't

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "File Uploads: The Feature That Looks Simple and Isn't",
  "description": "A technical breakdown of the file upload decisions AI-generated prototypes get wrong by default: presigned direct-to-storage uploads versus proxying through your server, MIME sniffing, size limits, malware scanning, and public bucket exposure.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-02-08",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/file-uploads-the-feature-that-looks-simple-and-isnt" }
}
</script>

Bram had built an avatar-upload feature into his community platform in an afternoon with Lovable, and it worked perfectly through fifty test users. Then user fifty-one uploaded a 380MB video file renamed to `photo.jpg`, his serverless function timed out mid-upload three times in a row, and the partial file sat in his storage bucket at a public URL indexable by Google. None of that showed up in testing, because testing never uploads a video file with a spoofed extension, or two hundred files in a row, or a file crafted to look like an image until a browser actually parses it.

File uploads are deceptive because the happy path — one small image, one user, one upload — is genuinely a few lines of code in any AI tool. Everything that makes uploads a real subsystem rather than a feature is what happens outside the happy path, and none of it shows up until it does.

## Presigned Uploads vs. Proxying Through Your Server: The Architecture Decision

There are two fundamentally different ways a file gets from a user's browser into your storage, and most AI-generated apps pick one without evaluating the other.

**Proxying through your server** means the browser sends the file to your backend, and your backend forwards it to S3, Supabase Storage, or Cloudflare R2. It's the simpler mental model and the default most tutorials teach, but it means every byte of every upload passes through your application server, consuming its memory and bandwidth, and — critically — running into your serverless function's execution time and payload size limits. Vercel's default function payload limit is 4.5MB; a lot of "why won't my upload work" tickets trace straight back to this ceiling, hit invisibly because local development never enforces it.

**Presigned direct-to-storage uploads** have your server generate a short-lived, scoped URL (via the S3 SDK, Supabase's `createSignedUploadUrl`, or equivalent) that the browser uses to upload the file straight to storage, bypassing your server entirely. This scales far better — your server does a cheap operation (issue a URL) instead of an expensive one (stream a large file) — and it's the architecture serious file-handling products use. The cost is complexity: you now need to validate the file *after* it's already in storage, since your server never saw its bytes, which means a webhook or a background job that checks the uploaded object and rejects or quarantines it if it fails validation, rather than rejecting it inline before it's accepted.

The decision isn't which is "correct" — it's which fits your volume and file sizes. Profile pictures and documents under a few megabytes, low volume: proxying is simpler and the limits rarely bite. Video, large PDFs, bulk imports, or any product where uploads are a core feature rather than an accessory: presigned uploads are close to mandatory, and building it as a proxy first means rebuilding the entire upload path later under pressure once the size limit becomes a support queue.

## MIME Sniffing: Why the File Extension Was Never the Security Boundary

A shocking amount of AI-generated upload validation looks like this: check that the filename ends in `.jpg`, `.png`, or `.pdf`, and accept it. This is not a security check — a filename is just a string the uploader chose, and nothing stops someone naming an executable `invoice.pdf` or an HTML file containing a script tag `image.jpg`.

The `Content-Type` header the browser sends is barely better — it's also client-controlled and trivially spoofed by anyone using a tool other than a browser form to make the request, which describes exactly the kind of person you're trying to defend against.

The correct check is **magic byte inspection**: reading the first few bytes of the actual file content and comparing them against known signatures — a JPEG starts with `FF D8 FF`, a PNG with `89 50 4E 47`, a PDF with `%PDF`. Libraries exist for this in every stack (`file-type` in Node, `python-magic` in Python), and the check takes microseconds. This is what actually confirms a file is what it claims to be, independent of what the filename or header says.

Beyond sniffing, two related risks matter specifically for images: **decompression bombs**, where a tiny file expands to gigabytes when decoded, overwhelming any image-processing step, mitigated by capping decoded dimensions before processing rather than after; and **embedded scripts in SVG files**, which are XML and can contain inline JavaScript — SVGs uploaded and later rendered directly in a browser context are a genuine cross-site scripting vector, and the safe defaults are either rejecting SVG uploads entirely or sanitizing them server-side before storage, never trusting an uploaded SVG to be inert just because it "looks like an image."

## Size Limits: The Number Nobody Chose on Purpose

Ask a founder what their upload size limit is and the honest answer, if their prototype came from an AI tool, is usually "whatever the default was" — which might be the storage provider's platform maximum (5GB on S3 per single-part upload), the serverless function's payload ceiling, or effectively unlimited if nothing was set at all.

An unset limit is not a neutral choice. It means a single malicious or careless upload can exhaust storage quota, spike your bill on usage-based storage pricing, or — combined with a slow multipart upload — hold a connection or a function invocation open long enough to become a low-effort denial-of-service vector against a small number of legitimate users. Every field that accepts a file needs a limit chosen for that field's actual purpose: a profile picture rarely needs to exceed 5MB, a document upload might reasonably need 25MB, a video product needs a genuinely large limit paired with the presigned/chunked upload pattern above rather than a naive single-request upload.

The limit needs enforcement in at least two places to be real: client-side, so users get instant feedback instead of a failed upload after waiting for a multi-minute transfer, and server-side or storage-policy-side, because client-side validation is cosmetic and any request crafted outside the browser skips it entirely.

## Malware and the Files You Didn't Write Any Code For

If your product accepts uploads from anyone other than yourself — user documents, resumes, attachments in a messaging feature, images in a marketplace listing — you are running a small file hosting service for strangers' files, and some percentage of strangers will upload something malicious, whether deliberately or because their own machine is already infected.

This risk is invisible in an AI-generated prototype because nothing about "accept an upload and store it" naturally surfaces it — the code works identically whether the file is clean or not. The exposure is downstream: another user or an employee downloads and opens the file, or the file is served back to browsers in a way that lets it execute.

Practical, proportionate mitigation for most early-stage products: run uploaded files through a scanning API (ClamAV self-hosted, or a hosted scanning service) asynchronously after upload and before the file is made available to anyone but the uploader, quarantining anything flagged; never serve user-uploaded files from the same origin as your application (use a separate subdomain or storage domain), which prevents an uploaded HTML or SVG file from ever running with your app's cookies and permissions even if a scanner misses it; and set a strict `Content-Disposition: attachment` header on anything that isn't an image meant for inline display, so browsers download rather than execute unknown file types. None of this needs to be built from scratch — it needs to be turned on, and most prototypes simply never had anyone ask the question.

## Public Buckets: The Default That Feels Convenient Until It Isn't

The single most common file-upload finding in AI-generated prototypes is a storage bucket set to public read access — because it's the easiest way to get an uploaded image to display back in the UI without writing any additional authorization logic, and it works flawlessly in every demo, because demos don't have data that needs protecting.

The consequence: any file in that bucket is reachable by anyone who has or guesses its URL, indefinitely, including by search engine crawlers if the URL is ever linked anywhere public. For profile pictures on a public social product, that might be an acceptable, even intended, tradeoff. For ID documents in a KYC flow, medical intake forms, or private client files in a B2B tool, a public bucket is a data exposure with no attacker required — just a URL that leaks through a referrer header, a shared link, or a crawler.

The fix is private-by-default storage with time-limited signed URLs generated per request, scoped to the requesting user's actual permission to view that specific file — checked against your application's authorization logic, not just "is this URL guessable." This is a small architectural change (signed URL generation instead of a public path) but it requires threading an authorization check through every place a file gets displayed, which is exactly the kind of cross-cutting change that's cheap before launch and a genuine audit-and-fix project once dozens of features already assume public URLs.

## A Decision Checklist Before You Ship Uploads

Before any upload feature goes live, five yes/no questions cover most of what matters. Does every upload get validated by magic bytes, not filename or client-reported MIME type? Is there an explicit, purpose-appropriate size limit enforced server-side, not just in the frontend form? Is the storage bucket or path private by default, with access granted through signed URLs checked against actual user permissions? Are uploaded files served from a separate origin from your main application, with a `Content-Disposition` header preventing unintended execution? And for any product accepting files from more than a handful of trusted users, is there a scanning step before a file is available to anyone but its uploader?

A "no" on any of these isn't automatically a blocker — a purely internal admin tool with three trusted users has a different risk profile than a public marketplace — but it should be a deliberate "no," made by someone who understood the tradeoff, not an unexamined default inherited from a code generator.

## What This Costs to Fix Properly

Retrofitting proper upload handling — signed URLs, magic byte validation, private storage with per-file authorization, and basic malware scanning — on an existing feature is typically a contained, well-scoped piece of work, because it touches the upload pathway specifically rather than the surrounding product. It sits comfortably within LaunchStudio's Launch Ready range for most single-purpose upload features, and it's exactly the kind of narrow, well-defined fix that doesn't require touching the interface your AI tool already built. LaunchStudio is powered by Manifera, a [software development company](https://www.manifera.com/services/custom-software-development/) with 11+ years of experience, which is why this specific pattern — a working demo hiding a public bucket — gets caught in review rather than discovered by a stranger with a guessed URL. If uploads are core to your product rather than incidental to it, [use the price calculator](https://launchstudio.eu/en/#calculator) to see where a proper implementation lands before you scale a feature built on the defaults.

## Real example

### A Freelance Marketplace Discovers Its "Portfolio Upload" Was a Public File Server

Nadia Kowalski built Craftlink, a marketplace connecting freelance artisans with local clients, using Lovable — including a portfolio feature where artisans uploaded photos of past work. The bucket backing it was set to public read by default, which was fine for the photos, but the same upload component was reused, unmodified, for a "verification document" step where artisans uploaded ID for account approval.

The reuse meant ID documents landed in the same public bucket as portfolio photos, at predictable, sequentially-generated URLs. Nothing was actively exploited before it was caught, but a routine review found that anyone who could guess or enumerate a URL pattern could view another artisan's ID document — with no login, no authorization check, and no log of who accessed what.

The fix split the two upload flows onto separate storage paths, moved verification documents to a private bucket with signed URLs scoped to admin review only, added magic byte validation to reject the handful of malformed uploads already sitting in the bucket, and set expiring, single-use signed URLs for the admin review interface.

**Result:** verification documents are no longer publicly reachable under any URL, and the portfolio upload — genuinely fine to keep public — was left untouched, so artisans' work still displays exactly as it did before.

> "It hadn't occurred to me that 'reuse the upload component' meant reusing its public bucket too. That's the kind of gap you don't see until someone who isn't you looks at it."
> — **Nadia Kowalski, Founder, Craftlink (Wrocław)**

**Cost & Timeline:** Launch Ready engagement, upload and storage hardening — delivered in 5 business days.

## Frequently Asked Questions

### Do I really need presigned uploads if my files are small?

Not necessarily — for profile pictures or small documents under a few megabytes, proxying through your server is simpler and the payload limits rarely become a problem. Presigned direct-to-storage uploads earn their added complexity once file sizes or volume grow, or once uploads become a core feature rather than an accessory.

### How do I check if my storage bucket is publicly readable right now?

Open an uploaded file's URL in a private/incognito browser window with you logged out of everything. If the file loads without any authentication, the bucket or the specific object is public. In Supabase Storage or S3, check the bucket policy or the "public" toggle directly in the provider's dashboard.

### Is virus scanning overkill for a small SaaS product?

It depends on who uploads and who downloads. If uploads are limited to a handful of trusted internal users, it's reasonable to defer. If any signed-up user can upload a file that another user or your team will later open or download, scanning is a proportionate, low-cost safeguard rather than overkill.

### What's the fastest fix if I can't rebuild the whole upload system right now?

Two changes deliver most of the risk reduction fast: switch the bucket to private with signed URLs, and add magic byte validation on the upload endpoint. Both are narrow, isolated changes that don't require restructuring how files are stored or how the feature works from a user's perspective.

### Will fixing file uploads break the UI my AI tool built?

No — this work happens in the storage configuration and the backend validation layer, not the upload button or preview component your frontend already renders. LaunchStudio's approach keeps that interface exactly as built while replacing what happens to the file underneath it.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Do I really need presigned uploads if my files are small?", "acceptedAnswer": { "@type": "Answer", "text": "Not necessarily. For small profile pictures or documents under a few megabytes, proxying through your server is simpler and payload limits rarely become an issue. Presigned direct-to-storage uploads become worthwhile once file sizes, volume, or upload centrality to the product grow." } },
    { "@type": "Question", "name": "How do I check if my storage bucket is publicly readable right now?", "acceptedAnswer": { "@type": "Answer", "text": "Open an uploaded file's URL in a private browser window while logged out of everything. If it loads without authentication, the bucket or object is public. In Supabase Storage or S3, this can also be confirmed directly in the bucket policy settings." } },
    { "@type": "Question", "name": "Is virus scanning overkill for a small SaaS product?", "acceptedAnswer": { "@type": "Answer", "text": "It depends on who uploads and who downloads. If uploads are limited to a handful of trusted internal users, it's reasonable to defer. If any signed-up user's file may be opened by another user or your team, scanning is a proportionate safeguard rather than overkill." } },
    { "@type": "Question", "name": "What's the fastest fix if I can't rebuild the whole upload system right now?", "acceptedAnswer": { "@type": "Answer", "text": "Switching the storage bucket to private with signed URLs and adding magic byte validation on the upload endpoint delivers most of the risk reduction and are both narrow, isolated changes." } },
    { "@type": "Question", "name": "Will fixing file uploads break the UI my AI tool built?", "acceptedAnswer": { "@type": "Answer", "text": "No. The fix happens in storage configuration and backend validation, not the upload button or preview component the frontend already renders, so the interface stays exactly as built." } }
  ]
}
</script>
