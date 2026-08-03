---
Title: "AI for Coding in Hilversum: What Media-Sector Founders Are Building (and Missing)"
Keywords: ai for coding, ai app development, media tech startup, content platform security, Hilversum
Buyer Stage: Awareness
Target Persona: Non-Technical Founder
---

# AI for Coding in Hilversum: What Media-Sector Founders Are Building (and Missing)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI for Coding in Hilversum: What Media-Sector Founders Are Building (and Missing)",
  "description": "How Hilversum's media-industry founders are using AI for coding to build content and production tools, and the specific production gaps that show up in that sector.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-23",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-for-coding-hilversum" }
}
</script>

A freelance video producer in Hilversum opens Lovable on a Sunday afternoon, describes a scheduling tool for coordinating shoot days with freelance crews, and by Sunday evening has something that looks like a real product. This scene repeats constantly in a city built around Dutch public broadcasting — and it's exactly why Hilversum has become an unexpected pocket of founders using AI for coding to build tools for the media industry itself.

## Why Hilversum Is a Different Kind of AI Coding City

Hilversum's identity is unlike any other city in Noord-Holland: it's the historic home of Dutch public broadcasting, with NPO and a dense cluster of production houses, studios, and media agencies concentrated in and around the city. That means the founders experimenting with AI for coding here aren't building generic SaaS — they're building scheduling tools, rights-management dashboards, freelancer marketplaces, and content-review platforms, shaped directly by problems they've hit personally inside the media industry.

That specificity is a strength. It also creates a specific blind spot. Media and content platforms deal constantly with file uploads — video, audio, raw footage — and unpublished, embargoed, or rights-restricted material that absolutely cannot leak before an agreed release date. AI for coding tools are very good at building an upload button and a media player. They are not, by default, good at making sure that unpublished content sits behind proper authentication, or that a storage bucket isn't quietly readable by anyone with the right URL.

There's also a technical wrinkle specific to media that generic SaaS products don't deal with: large file sizes. A raw video file can run into gigabytes, and AI-generated upload logic frequently isn't built to handle that gracefully — uploads that time out partway through, no resumable upload support, no progress feedback for a crew member uploading footage over a shaky festival wifi connection. These aren't security issues exactly, but they're exactly the kind of production-plumbing gap that erodes trust with professional users who expect tools built for their workflow to actually handle their file sizes.

## What Media-Sector Founders in Hilversum Are Getting Right

To be fair to this founder community, a few things are working well:

- Product-market fit tends to be strong, because these founders are solving problems they've lived inside the industry
- Adoption within the local production network happens fast, since Hilversum's media scene is tightly connected and word travels between studios quickly
- The interfaces built with tools like Lovable are often genuinely well-designed, reflecting founders' own visual and production sensibilities

## What's Consistently Missing

The gaps tend to cluster around exactly the areas media platforms care about most: access control on sensitive files, proper video/audio storage configuration, and handling large file uploads reliably instead of timing out or corrupting mid-upload. In practice, fixing this rarely means touching the parts of the platform a founder is proudest of — the review interface, the commenting tools, the scheduling calendar. It means quietly rebuilding the layer underneath the upload button that decides who can reach a file and how long a link stays valid. LaunchStudio is powered by Manifera, a team of 120+ engineers with 11+ years of experience serving enterprise clients — and part of that team, based out of our Singapore hub, works alongside the Amsterdam office reviewing exactly this category of media-specific infrastructure gap for founders who never anticipated needing it.

As Herre Roelevink, CEO of LaunchStudio and Managing Director of Manifera, puts it: "We see a shift in software needs. The challenge is no longer turning good ideas into software. It's now about the architecture and security needed to bring those products to maturity. We have eleven years of experience in exactly that." For a Hilversum founder whose product depends on protecting unpublished media, that architecture question isn't optional — it's the whole product's credibility.

If your Hilversum-built platform handles any kind of sensitive or embargoed content, it's worth exploring LaunchStudio's [full production process](https://launchstudio.eu/en/#process) before scaling further. Manifera's [custom software development](https://www.manifera.com/services/custom-software-development/) work applies the same access-control discipline used for enterprise clients to founder-scale media platforms.

## Choosing the Right Storage Configuration for Sensitive Media Files

Most AI for coding tools default to the simplest storage setup that makes an upload button work — often a public or semi-public bucket, because that configuration requires the least friction during generation. For a to-do list app, that default barely matters. For a platform holding unpublished footage, rough cuts, or embargoed press materials, it's the single most consequential setting in the entire product.

**The core distinction: public, private, and signed**

- **Public storage** means anyone with the direct file URL can view it, forever, with no authentication check at all — this is the default a lot of AI-generated apps land on, because it's the easiest to wire up and the easiest to accidentally leave in place
- **Private storage** requires authentication to access anything, but poorly configured private buckets can still leak through predictable URL patterns or misconfigured permission rules
- **Signed, time-limited URLs** are the standard for genuinely sensitive media: a link is generated on demand, tied to an authenticated session, and expires after a set window — so even a leaked link stops working shortly after

**Why this matters more for embargoed content than for typical user data**

A leaked customer email address is a privacy problem. A leaked pre-release episode, an unpublished interview, or a client's unreleased promotional video is a contractual and financial problem, often with real damages attached — the kind of leak that can end a production house's relationship with a broadcaster or a brand client entirely. That asymmetry is exactly why a Hilversum media platform can't treat storage configuration as a "get to it later" item the way another SaaS product reasonably might.

**A few checks worth running directly**

1. Try opening a file URL from your platform in a private browser window, logged out — if it loads, your storage isn't actually access-controlled
2. Check whether your storage URLs are predictable (sequential IDs, guessable patterns) versus random, unguessable tokens
3. Confirm whether links you've shared for review actually expire, or remain valid indefinitely once generated

Getting this right doesn't require rebuilding the upload flow a founder already validated with real production teams — it's a configuration and access-control layer added around it. It's also worth doing before a platform's second or third production house comes on board, not after, since expanding usage means expanding exactly how many people are one guessed URL away from finding out.

## Real example

### An AI-Native Founder in Action: MediaFlow's Public Storage Bucket

Lotte Jansen, a Hilversum-based production coordinator, built MediaFlow with Lovable — a scheduling and rough-cut review tool for freelance video crews working across the region's production houses. Directors could upload unpublished footage for client review directly through the platform. It worked well enough that three small production companies started using it within weeks of launch.

What Lotte hadn't realized was that the storage bucket holding uploaded footage had no access restrictions — anyone with a direct link could view unpublished, client-embargoed footage without logging in at all. It was discovered when a client noticed their own unreleased promotional video appearing in a Google image cache preview, traced back to a publicly indexable storage URL.

**Result:** LaunchStudio locked down the storage bucket behind signed, time-limited access URLs tied to authenticated sessions, and added upload validation to prevent similar misconfigurations going forward, with no further exposure detected in a follow-up scan.

> *"In media, an unpublished asset leaking isn't just embarrassing — it can break a client relationship instantly. I had no idea the storage itself was the weak point."*
> — **Lotte Jansen, Founder, MediaFlow (Hilversum)**

**Cost & Timeline:** €1,300 (storage access audit, signed-URL implementation, upload validation) — completed in 5 business days.

---

## Frequently Asked Questions

### Why does media content specifically need extra security compared to a typical SaaS app?
Unpublished, embargoed, or rights-restricted media has real financial and contractual consequences if it leaks, unlike most SaaS data. Storage and access control need to be deliberately configured, not left at default settings.

### Does LaunchStudio understand the media industry specifically, or just general software?
LaunchStudio's engineers, backed by Manifera's 11+ years of experience and enterprise clients like Vodafone, apply general production-engineering discipline — access control, storage security, upload handling — that transfers directly to media-specific platforms.

### Is Hilversum's media-founder scene big enough to matter, or is this a niche case?
It's a genuine local pattern. Hilversum's concentration of broadcasting and production companies means a steady stream of founders build media-adjacent tools, often hitting the same storage and access-control gaps.

### What did Herre Roelevink mean about "architecture and security" being the real challenge now?
He's pointing to a shift: AI tools have solved the problem of generating working software quickly. What's left is the harder, less visible work of making that software secure and stable enough to run in production — which is exactly what LaunchStudio does.

### How do I get a security review of my own media platform?
Talk to an engineer who actually reads AI-generated code before judging it — LaunchStudio offers a free initial review of your prototype's architecture before any paid work begins.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Why does media content specifically need extra security compared to a typical SaaS app?", "acceptedAnswer": { "@type": "Answer", "text": "Unpublished or rights-restricted media has real financial and contractual consequences if it leaks, so storage and access control need deliberate configuration rather than defaults." } },
    { "@type": "Question", "name": "Does LaunchStudio understand the media industry specifically, or just general software?", "acceptedAnswer": { "@type": "Answer", "text": "LaunchStudio's engineers apply general production-engineering discipline, backed by Manifera's 11+ years of experience and enterprise clients like Vodafone, which transfers directly to media-specific platforms." } },
    { "@type": "Question", "name": "Is Hilversum's media-founder scene big enough to matter, or is this a niche case?", "acceptedAnswer": { "@type": "Answer", "text": "It's a genuine local pattern. Hilversum's concentration of broadcasting and production companies produces a steady stream of media-adjacent founder tools." } },
    { "@type": "Question", "name": "What did Herre Roelevink mean about 'architecture and security' being the real challenge now?", "acceptedAnswer": { "@type": "Answer", "text": "He means AI tools have solved generating working software quickly; what remains is making that software secure and stable enough for production, which is LaunchStudio's focus." } },
    { "@type": "Question", "name": "How do I get a security review of my own media platform?", "acceptedAnswer": { "@type": "Answer", "text": "LaunchStudio offers a free initial review of your prototype's architecture before any paid work begins." } }
  ]
}
</script>
