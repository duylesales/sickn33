---
Title: "AI in Development Workflows: What Changes, What Doesn't"
Keywords: ai in development, ai for development, ai coding, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI in Development Workflows: What Changes, What Doesn't

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI in Development Workflows: What Changes, What Doesn't",
  "description": "A technical deep-dive on server-side request forgery risk introduced by a convenient 'import from URL' feature, using a warehouse inventory tool as the concrete case of what AI in development workflows changes and what it doesn't.",
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
  "datePublished": "2026-07-29",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/ai-in-development-workflows-what-changes-what-doesnt"
  }
}
</script>

AI in development workflows changes how fast a feature gets built. It doesn't change what that feature is fundamentally capable of once it's live — and a convenient "import product image from a URL" feature, built quickly and correctly to satisfy exactly that description, is fundamentally capable of a lot more than displaying a picture, unless something specifically stops it.

## What an "Import From URL" Feature Actually Does Under the Hood

A feature letting a user paste a URL and having your server fetch whatever's at that address — an image, a document, any resource — necessarily means your own server is the one making that outbound request, not the user's browser. This is a genuinely convenient pattern, and AI coding tools implement it readily whenever a founder describes wanting this kind of "paste a link, we'll grab it" functionality.

## Why "Your Server Fetches It" Is the Specific Risk

If the URL a user provides isn't restricted in any way, there's nothing stopping a request from targeting internal network addresses your server can reach but the public internet can't — internal admin panels, cloud metadata services, or other backend systems that were never meant to be reachable from outside, but that your own server, making the request on the user's behalf, can reach directly.

## Why This Is Called Server-Side Request Forgery

The name describes exactly what happens: a request is forged (crafted by an outside party) but executed server-side (by your own trusted infrastructure), giving an attacker a way to probe or interact with internal systems using your server's own network position and trust level, rather than their own, far more restricted external vantage point.

## Why Testing With Real Image URLs Never Reveals This

Testing an "import from URL" feature by pasting real, external image links — which is the only thing a founder building and testing this feature would naturally do — confirms the feature correctly fetches and displays public images. It provides zero information about what happens if someone instead provides an internal network address, since that's simply not a URL a founder testing normal functionality has any reason to try.

## What Properly Restricting This Feature Requires

A safe implementation validates that a provided URL resolves to a genuinely public, external address before fetching it, explicitly blocking requests to internal or reserved network ranges regardless of how the URL is phrased or disguised. [LaunchStudio](https://launchstudio.eu/en/) implements exactly this kind of URL validation as part of its backend security review, backed by Manifera's 11+ years of experience securing server-side integrations across production systems.

Manifera's SSRF and backend integration security work is delivered through the Ho Chi Minh City development center on Pho Quang Street, coordinated with the Amsterdam headquarters at Herengracht 420.

[Talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: The Image Import That Reached Too Far

Wessel, a former logistics coordinator turned founder in Vlaardingen, built VoorraadVast, an AI-assisted warehouse inventory management tool built with Cursor, including a convenient feature letting warehouse staff import a product photo directly from a supplied URL rather than uploading a file manually.

A partner's security-conscious IT contact, reviewing VoorraadVast ahead of a potential integration, tested the import feature with an internal network address instead of a public image URL and found the server attempted to fetch and return whatever it found there — confirming the feature had no restriction on what kind of address it would reach out to. LaunchStudio's review confirmed the underlying fetch logic accepted and requested any URL without validating it was a genuinely public destination.

**Result:** LaunchStudio added strict validation ensuring the import feature only fetches from verified public, external addresses, explicitly blocking any request targeting internal or reserved network ranges, closing the exposure without changing how staff used the import feature for legitimate product photos.

> *"I built that feature to save staff a few clicks importing product photos. It never once crossed my mind that the same convenience could theoretically be pointed at something completely different from a photo."*
> — **Wessel Kramer, Founder, VoorraadVast (Vlaardingen)**

**Cost & Timeline:** €2,600 (SSRF remediation and URL fetch validation) — completed in 8 business days.

---

## Frequently Asked Questions

### Would a backend security specialist consider SSRF a common finding in AI-generated code specifically, or a rare, exotic one?

Increasingly common, specifically because "fetch a resource from a URL the user provides" is such a natural, frequently requested feature description, and validating that the fetched destination is safe is a separate, additional requirement that has to be specifically implemented rather than assumed to come bundled with the basic fetch functionality.

### Does this risk only affect features explicitly described as "import from URL," or does it show up elsewhere too?

It shows up in any feature where user input influences an outbound server-side request — webhook callback URLs, PDF generation services that fetch external content, or link-preview features all carry some version of the same underlying risk if the destination isn't properly restricted.

### Manifera's engineering has secured server-side integrations for enterprise clients — does that experience transfer to a smaller inventory tool like VoorraadVast?

Yes, directly — the specific validation pattern (confirm a destination is genuinely public before fetching it) is identical regardless of company size, and applying an already-proven enterprise pattern to a founder-scale product is considerably faster and more reliable than developing the correct approach from scratch for each new case.

### Herre Roelevink has described the current challenge as being about architecture rather than raw feature output — does an SSRF gap fit that framing well?

Very well — the import feature functioned exactly as described from a feature-output perspective; the missing piece was an architectural decision about what the server should and shouldn't be allowed to reach on a user's behalf, precisely the category Roelevink's commentary consistently points to.

### Is there a way for a founder to test for this kind of gap themselves before a professional review?

A founder with some technical comfort can try providing an internal address (like a local network address) to any "fetch from URL" feature and observe whether the request succeeds, though correctly and comprehensively blocking every possible way to disguise an internal destination typically requires the kind of systematic validation a dedicated security review implements.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is SSRF a common finding in AI-generated code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Increasingly common, since 'fetch a URL the user provides' is a natural feature request that needs separate validation."
      }
    },
    {
      "@type": "Question",
      "name": "Does this risk only affect explicit 'import from URL' features?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, it shows up anywhere user input influences an outbound server-side request, like webhooks or link previews."
      }
    },
    {
      "@type": "Question",
      "name": "Does enterprise server-side integration experience transfer to smaller tools?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, the validation pattern is identical regardless of company size, speeding up the fix considerably."
      }
    },
    {
      "@type": "Question",
      "name": "Does an SSRF gap fit the architecture-over-feature-output framing the CEO describes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Very well, since the feature worked as described; the missing piece was an architectural access decision."
      }
    },
    {
      "@type": "Question",
      "name": "Can a founder test for this gap themselves before a professional review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Partially, by trying an internal address, though comprehensive blocking typically requires a systematic review."
      }
    }
  ]
}
</script>
