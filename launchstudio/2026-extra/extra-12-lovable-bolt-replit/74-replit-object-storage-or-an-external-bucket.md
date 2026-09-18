---
Title: "Replit Object Storage or an External Bucket"
Keywords: replit object storage, S3, file storage, signed URLs, portability, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Replit Object Storage or an External Bucket

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Replit Object Storage or an External Bucket",
  "description": "Where user files should live for a Replit product: why the filesystem is not an option, what the platform's storage gives you, when an external bucket is worth the extra setup, and how to keep the choice reversible.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-08",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/replit-object-storage-or-an-external-bucket" }
}
</script>

The first version of any upload feature writes the file to disk. It works immediately, it requires no setup, and on a platform where deployments are ephemeral it is the arrangement that loses your customers' documents.

Files written to a container's filesystem live as long as that container. A redeploy, a scale event, a restart — and they are gone, with no error and no record, discovered weeks later by a customer opening something that is no longer there.

So the real question is not whether to use object storage but which, and the answer turns on how portable you want to be.

## Why the Filesystem Is Not an Option

Three reasons, any one of which is sufficient.

**It does not survive.** Deployments replace the filesystem. Anything written at runtime is lost when the instance is replaced, which happens for reasons entirely outside your control.

**It does not scale.** More than one instance means files written by one are invisible to the others, producing the confusing situation where a document exists for some requests and not others.

**It is not backed up.** Your database backup does not include it, so a restore produces records pointing at files that never existed in the restored world.

The only legitimate filesystem use is genuinely temporary work — a file being processed within a single request, deleted immediately afterwards.

## What the Platform's Storage Gives You

Replit's own object storage is the path of least resistance: provisioned from the same place, authenticated without configuration, and adequate for most products.

For a product under a few hundred gigabytes, with ordinary access patterns, it is a reasonable default and it removes a set of decisions.

Two things to check rather than assume, as with any storage: whether objects are private by default, which determines whether your customers' documents are on the open internet, and what the backup arrangement is, since object storage is frequently outside whatever database backup you have configured.

## When an External Bucket Is Worth It

Four situations justify the additional setup.

**Data residency.** A customer requires their documents in a specific region, which an external provider lets you choose explicitly. This is the most common genuine reason for Dutch products selling to public bodies and healthcare organisations.

**Portability.** If the application may move to different hosting — likely for a product that started on a prototyping platform — files in a neutral bucket mean the migration does not include moving terabytes.

**Scale or cost.** At substantial volume the economics differ, particularly for egress, and a dedicated provider offers more control.

**Features you need.** Object lock for immutable backups, lifecycle rules to age content out, event notifications when a file arrives, or a CDN in front.

For most products none of these applies in year one, and adopting a provider "because it is more professional" is the same mistake as migrating a framework for the same reason.

## Make the Choice Reversible

Whichever you pick, three decisions keep it from being permanent — and they are the same decisions the Supabase storage article in this series recommends.

**Store paths, not URLs.** A database column holding a full URL to a specific provider is a column that must be rewritten at migration and that breaks in every email already sent. A column holding a path, with URLs generated at read time, is portable by construction.

**Put file access behind your own functions.** One module that stores, retrieves and signs. Changing provider then touches one file rather than thirty.

**Use an owner-first path layout.** Organisation, then record, then a generated file identifier. It is how permissions are expressed, it makes buckets unwalkable, and it transfers unchanged between providers.

With those three, moving storage later is an afternoon of copying plus a configuration change. Without them it is a project.

## The Things That Matter More Than the Choice

Whichever storage you use, the rules from the file security article in this series apply identically and matter considerably more than the provider.

Private by default, with access through signed URLs generated on the server. Type verified from the file's contents rather than its extension. Size limits per file and per account. Generated filenames rather than the uploader's. A database row per file recording who uploaded it, when, and its path. Deletion that removes the object as well as the record. And files served from an origin separate from your application.

A product that gets those right on the platform's own storage is in a far better position than one that chose a sophisticated provider and left the bucket public.

## Serving Files Efficiently

Once files are in object storage, how they reach the visitor determines both speed and cost, and the naive arrangement is wrong on both counts.

The naive version proxies everything through your application: a request arrives, your server fetches the object, and streams it back. It works, and it means every megabyte a customer downloads passes through your compute, is billed twice, and occupies an instance for the duration — which for a product serving photographs is a surprising share of everything it does.

The better arrangement is a redirect to a signed URL. Your application checks whether this person may have this file, generates a short-lived URL, and sends the browser there. The bytes go directly from storage to the visitor, your server does almost nothing, and the authorisation check still happens on every request.

Two refinements worth having. A CDN in front of the storage for anything public or frequently requested, which is usually a configuration option rather than a project. And derivatives generated at upload time — a thumbnail and a display size — so a gallery of forty photographs does not download forty full-resolution originals, which is the single largest cause of slow pages in products that handle images.

The one case for proxying through your application is when the URL itself must not be shareable even briefly. That is rare, and it is worth being sure the requirement is real before paying for it on every request.

## Storage Grows and Nobody Notices

Files accumulate in a way databases do not, because nothing ever prompts you to look.

Four sources, all avoidable. Originals retained forever when only derivatives are displayed. Orphans left by deleted records, which is the deletion problem this article already names. Uploads abandoned mid-form, which a multi-step process collects continuously. And duplicates created when a customer re-uploads after a failure.

The diagnostic is a monthly comparison: the number of objects and total bytes in storage against the number of files your database knows about. When those numbers diverge, you have orphans, and a cleanup job that removes objects with no corresponding row — with a dry run first, and a report of what it removed — usually reclaims more than expected.

The prevention is two rules. Deletion is a single operation covering both the row and the object, so they cannot get out of step. And an unattached upload expires after a day, because a file nobody claimed was not wanted.

Add a retention rule for the things that genuinely age out — originals once derivatives exist, exports older than a month, documents past the retention period your privacy policy states — and storage becomes a line that grows with your customer base rather than with time.

That distinction is worth checking against your own bill once: storage that grows with customers is a business doing well, and storage that grows with the calendar is a cleanup job you have not written.

It is the sort of check that takes two minutes a month and prevents the conversation, a year later, about why storage costs more than everything else combined.

## Setting This Up

For a Replit product this is typically half a day: any runtime filesystem writes identified and moved, object storage chosen — the platform's by default, external where residency, portability, scale or specific features justify it — with paths rather than URLs stored in the database, all file access behind your own functions, an owner-first path layout, private buckets with server-generated signed URLs, type verification from content, size limits, generated filenames, a file registry table, deletion covering objects as well as rows, a backup arrangement that actually includes the files, and a documented restore.

LaunchStudio does this as part of taking a Replit product to production, where files on the filesystem are among the most common findings. The engineers are Manifera's — eleven years, 160+ projects, from Amsterdam and Ho Chi Minh City.

[Ask us where your uploads currently go](https://launchstudio.eu/en/#contact). If the answer is a folder, they are not there any more.

## Real example

### Documents That Vanished With a Deploy

Freek Batenburg built Keuringsdossier on Replit: inspection documentation for lift and machine inspection companies, where engineers upload photographs and signed reports from site, used by six companies covering around 3,200 assets.

Uploads were written to a folder in the project. It had worked throughout development and for the first four months of use, because he had not redeployed during a period when anyone was uploading.

A deployment on a Tuesday afternoon replaced the instance. Every photograph and report uploaded since the previous deployment — eleven days, about 340 files — was gone. The database still held the records, so the product showed 340 inspections with documents attached and produced an error when anyone opened one.

There was no backup, because the database backup contained only the database.

Three business days: object storage adopted, using the platform's own since none of the residency, portability or scale reasons applied; all file access moved behind a storage module, with the database storing paths rather than URLs so a later change of provider is a configuration change; an owner-first path layout of company, asset and generated file identifier; buckets private with signed URLs generated server-side, expiring in fifteen minutes for viewing and an hour for download; type verification from file contents, since the previous implementation had accepted anything; size limits of 20 MB per file; a file registry table recording uploader, timestamp, path, size and type; deletion extended to remove objects; a backup of the storage bucket to a separate account with a tested restore; and the 340 lost files identified from the database records, with the six companies asked to re-upload what they still had — which recovered about 260.

**Result:** roughly 80 inspection documents were permanently lost, which for two assets meant the inspection had to be repeated at a cost the companies absorbed. Freek's assessment is that he had no idea the filesystem was temporary, and that nothing in four months of successful operation had suggested it.

> *"It had worked for four months. Then I deployed on a Tuesday and eleven days of inspection photographs simply were not there any more, with no error and nothing in any log."*
> — **Freek Batenburg, Founder, Keuringsdossier (Barneveld)**

**Cost & Timeline:** €2,800 (object storage adoption with a storage module and path-based references, owner-first layout, private buckets with signed URLs, type verification and size limits, file registry, deletion handling, separate-account backup with tested restore, loss identification and recovery coordination) — completed in 3 business days.

## Frequently Asked Questions

### Can I store uploads on the filesystem?

No. Deployments replace it, multiple instances cannot see each other's files, and it is not in your backups. Use it only for work within a single request.

### Should I use the platform's storage or an external bucket?

The platform's by default. An external bucket when you need a specific region for data residency, portability away from the platform, substantial scale, or features like object lock and lifecycle rules.

### How do I keep the choice reversible?

Store paths rather than URLs, put all file access behind your own functions, and use an owner-first path layout. Changing provider is then an afternoon rather than a project.

### What matters more than which storage I choose?

Private by default with server-generated signed URLs, type verified from content, size limits, generated filenames, a file registry, deletion covering objects, and serving from a separate origin.

### Are my files in my database backup?

Almost certainly not. Object storage is usually outside it, which means a restore produces records pointing at files that do not exist. Back up the files separately and test it.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can uploads be stored on the filesystem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — deployments replace it, instances cannot share it, and it is not backed up. Use it only within a single request."
      }
    },
    {
      "@type": "Question",
      "name": "Platform storage or an external bucket?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The platform's by default; external when you need a specific region, portability, large scale, or features like object lock."
      }
    },
    {
      "@type": "Question",
      "name": "How do I keep the storage choice reversible?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Store paths not URLs, keep file access behind your own module, and use an owner-first path layout."
      }
    },
    {
      "@type": "Question",
      "name": "What matters more than the storage provider?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Private buckets with server-signed URLs, content-based type verification, size limits, generated filenames, a file registry and complete deletion."
      }
    },
    {
      "@type": "Question",
      "name": "Are uploaded files included in database backups?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually not — object storage sits outside them, so a restore leaves records pointing at missing files. Back files up separately and test it."
      }
    }
  ]
}
</script>
