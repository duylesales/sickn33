---
Title: "Security in AI-Generated Code Is Opt-In, Not Automatic"
Keywords: security in ai, ai in it security, ai secure, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# Security in AI-Generated Code Is Opt-In, Not Automatic

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Security in AI-Generated Code Is Opt-In, Not Automatic",
  "description": "A real scenario-driven look at why security in AI-generated code has to be specifically requested, using a publicly readable storage bucket exposing uploaded ID documents as the concrete case.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/security-in-ai-generated-code-is-opt-in-not-automatic"
  }
}
</script>

It's a normal Tuesday. A parent uploads a scan of their child's ID as part of registering for after-school care through your platform. The upload succeeds, the confirmation screen appears, everything looks exactly right. What that parent has no way of knowing is whether the storage location that file just landed in requires any authentication at all to view — because in a surprising number of AI-generated apps, by default, it doesn't.

## Why Storage Buckets Default to the Wrong Setting More Often Than Expected

Cloud storage services like AWS S3, Firebase Storage, and similar platforms are built to be flexible, supporting both fully public and fully private access configurations depending on what a project needs. An AI coding tool wiring up file uploads quickly, optimizing for "does the upload work when I test it," frequently reaches for the simplest configuration that makes the upload-and-retrieve demo work smoothly — which is sometimes a public or loosely restricted bucket, since that avoids the additional complexity of properly signed, authenticated URLs.

## Why "The Upload Worked" Never Reveals This

Testing an upload feature means uploading a file and confirming it's retrievable afterward — both of which succeed identically whether the storage bucket is public or properly restricted. There is no natural point during ordinary testing where a founder would think to check whether the file's underlying storage URL is guessable or listable by someone who was never given a link to it. Even opening the browser's developer tools and looking at the URL directly doesn't obviously reveal the problem — a working link just looks like a working link, regardless of whether it also happens to be reachable by anyone else on the internet who stumbles onto the same pattern.

## Why Documents Are a Worse Case Than Photos

A publicly accessible bucket is a real problem for any file type, but documents like ID scans, medical forms, or signed contracts carry meaningfully higher stakes than, say, a public profile photo — the kind of information on those documents (full legal names, dates of birth, identification numbers) is exactly the category of data that causes the most damage if it becomes broadly accessible, and childcare-adjacent products specifically tend to collect exactly this kind of document as a matter of course. When the person on the document is a minor, the stakes rise again: a leaked ID scan gives someone everything needed to attempt identity theft against a child, a form of fraud that can go undetected for years precisely because nobody checks a child's credit history or identity records until they're old enough to need one themselves.

## Why This Isn't a Reason to Distrust AI Coding Tools Generally

The tool did precisely what it was asked to do — store an uploaded file and make it retrievable. It's not a flaw in the tool's competence; it's a reflection of the fact that "make it retrievable" and "make it retrievable only by people who should be able to retrieve it" are two different specifications, and only one of them was actually made explicit in most prompts describing a file upload feature.

## What Closing This Gap Actually Looks Like

A proper fix reconfigures storage access to require authentication, replaces any public or guessable URLs with signed, time-limited ones, and audits what may have already been exposed during the period the misconfiguration was live. [LaunchStudio](https://launchstudio.eu/en/) checks exactly this kind of storage configuration as a standard part of its production-readiness review, backed by Manifera's 11+ years of experience with AWS, Firebase, and Supabase-based storage systems.

Manifera's storage security reviews are performed by the engineering team based at the Ho Chi Minh City development center on Pho Quang Street, coordinated with the Amsterdam headquarters at Herengracht 420.

[Send over your prototype's link for a free review](https://launchstudio.eu/en/#contact).

## A Checklist for Auditing Every Storage Bucket Your App Uses

A fully public bucket is the most obvious version of this problem, but it's rarely the only one worth checking. A single-issue mental model — "is my bucket public, yes or no" — misses several related misconfigurations that cause the same underlying exposure.

**Work through these questions for every storage bucket your app writes to, not just the one you remember setting up:**

- **Is the bucket itself listable, even if individual files require a direct link?** A bucket that allows directory listing lets anyone enumerate every filename it contains, turning "you'd need to guess the exact URL" into "you can just browse the full contents."
- **How long do your signed URLs stay valid?** A signed URL is only as protective as its expiration window — a link generated to last 30 days behaves, for practical purposes, almost as openly as a permanently public one if that link is ever shared, cached, or logged somewhere outside your control.
- **Do you have forgotten staging, backup, or test buckets from earlier development?** These are frequently created quickly to unblock a feature, never get the same access review as the production bucket, and often contain copies of the same sensitive files.
- **Is your CORS configuration scoped to your actual domain, or left at a permissive default?** An overly broad CORS policy can let a malicious site running in a victim's browser make authenticated requests against your storage on the victim's behalf.
- **Are filenames predictable or sequential?** Even with authentication required, a filename pattern like `id-scan-1042.jpg` invites simple enumeration attempts; random, non-guessable identifiers remove that avenue entirely.

None of these individually require deep cloud infrastructure expertise to understand, but checking all of them systematically, across every bucket a fast-moving AI-assisted build has created, is exactly the kind of thorough pass that's easy to skip when you're focused on shipping the next feature instead.

## Real example

### An AI-Native Founder in Action: The ID Scans Anyone Could Open

Anouk, a Dutch founder based in Antwerp building for the broader Benelux market, built KinderKring, an AI-assisted childcare booking platform built with Lovable, requiring parents to upload a scan of their child's ID as part of enrollment verification.

A technically minded parent, curious after noticing the uploaded file's URL pattern in her browser, tried modifying the filename portion of the link and found she could view a different family's uploaded ID scan without ever logging in. LaunchStudio's review confirmed the storage bucket holding uploaded documents had no access restriction — any correctly guessed or sequentially discovered file URL was fully viewable.

**Result:** LaunchStudio reconfigured the storage bucket to require authenticated, signed access for every document, replaced all existing public URLs, and confirmed no other file types in KinderKring shared the same misconfiguration, closing the exposure across the entire platform.

> *"She could have just quietly said nothing. Instead she told us directly, and I still think about how differently that could have gone if she hadn't."*
> — **Anouk Peeters, Founder, KinderKring (Antwerp)**

**Cost & Timeline:** €2,200 (storage access audit and signed-URL remediation) — completed in 7 business days.

---

## Frequently Asked Questions

### Would a cloud infrastructure specialist call this a rare misconfiguration, or a common one?

Common enough to be one of the most frequently cited real-world cloud misconfigurations across the industry broadly, not specific to AI-generated code — the difference with AI-assisted building is simply that nobody experienced is necessarily reviewing the default configuration before it goes live.

### Does this risk apply equally to major cloud providers, or are some inherently safer by default?

Default behavior varies by provider and by which specific service is used, but the underlying risk — a storage location reachable without proper authentication — is possible across virtually all major providers if not deliberately configured otherwise, so provider choice alone doesn't eliminate the need for a specific review.

### Is childcare-sector data uniquely sensitive compared to other verticals LaunchStudio has worked with?

It's among the more sensitive categories given that it involves both minors and identity documents simultaneously, though the underlying technical fix — proper access control on stored files — is identical regardless of vertical; what changes is how urgently the review should happen before real users are involved.

### CEO Herre Roelevink has described LaunchStudio's mission around the architecture gap AI tools leave behind — is a storage misconfiguration a good example of that gap?

A very direct one — this is architecture in the most literal sense, a configuration decision about how data is stored and accessed, made once during setup and then invisible to everyone unless specifically reviewed, exactly the category Roelevink's public commentary consistently returns to.

### Can a founder check their own storage bucket's access settings without engineering help?

Partially — most cloud storage dashboards display a visible "public" or "private" access indicator that a founder can check directly, though confirming that every specific file and folder within the bucket actually follows the intended setting, rather than an exception slipping through, typically benefits from a full technical review.

### Is a signed URL with a long expiration date basically the same risk as a public bucket?

Not identical, but closer than most founders assume — a signed URL that stays valid for weeks or months behaves, in practice, almost the same as a permanently public link if it's ever cached, shared, or logged somewhere outside your control, so the expiration window itself is a deliberate security setting worth reviewing, not just an incidental technical detail.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is a public storage bucket a rare or common misconfiguration?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Common industry-wide — the AI-assisted difference is that no experienced reviewer checks the default before going live."
      }
    },
    {
      "@type": "Question",
      "name": "Are some cloud providers inherently safer by default for storage?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Default behavior varies, but the underlying risk exists across virtually all major providers without deliberate configuration."
      }
    },
    {
      "@type": "Question",
      "name": "Is childcare data uniquely sensitive compared to other verticals?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Among the more sensitive given minors and identity documents combined, though the technical fix is identical elsewhere."
      }
    },
    {
      "@type": "Question",
      "name": "Is a storage misconfiguration a good example of the architecture gap the CEO describes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, a very direct example — a configuration decision made once and invisible unless specifically reviewed."
      }
    },
    {
      "@type": "Question",
      "name": "Can a founder check their storage bucket's access settings themselves?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Partially, via the dashboard's public/private indicator, though confirming every file follows it needs a full review."
      }
    },
    {
      "@type": "Question",
      "name": "Is a long-lived signed URL basically the same risk as a public bucket?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Close to it — a signed URL valid for weeks behaves like a public link if cached or shared, so its expiration window matters."
      }
    }
  ]
}
</script>
