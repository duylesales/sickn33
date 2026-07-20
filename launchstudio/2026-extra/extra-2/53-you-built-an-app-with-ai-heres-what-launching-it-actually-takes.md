---
Title: "You Built an App With AI. Here's What Launching It Actually Takes"
Keywords: app with ai, build app with ai, ai native, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# You Built an App With AI. Here's What Launching It Actually Takes

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "You Built an App With AI. Here's What Launching It Actually Takes",
  "description": "A how-to guide for what genuinely launching an app built with AI requires, using a scraped volunteer directory in a fire brigade scheduling tool as the concrete case of a missing rate limit.",
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
  "datePublished": "2026-08-03",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/you-built-an-app-with-ai-heres-what-launching-it-actually-takes"
  }
}
</script>

You built an app with AI, it works, and now you want it genuinely live. One specific step in getting there that's easy to skip: checking whether any of your app's public-facing search or directory features can be systematically scraped by an automated script, quietly harvesting far more data than any single legitimate user would ever need to see at once.

## Step One: Identify Every Feature That Returns a List of Records

Any feature returning a searchable or browsable list — a member directory, a volunteer roster, a public listings page — is a candidate for this specific check, regardless of how innocuous the underlying data might initially seem, since even seemingly low-stakes directory information can become meaningfully more sensitive once it's aggregated in bulk rather than viewed one entry at a time.

## Step Two: Understand Why Aggregated Data Is Riskier Than It Looks Individually

A single volunteer's name and contact details, viewable through the intended interface, might reasonably be considered acceptable public information for the platform's purpose. The same information, systematically collected across an entire directory through repeated automated requests, becomes a complete, exportable dataset — a meaningfully different and more sensitive artifact than any single, individually-viewed record.

## Step Three: Recognize That This Requires No Special Access, Just Patience

Scraping a public directory doesn't require breaching any authentication or exploiting any complex vulnerability — it simply requires repeatedly requesting the same public search or listing feature, systematically, until the entire underlying dataset has been collected, which is exactly why a rate limit on this kind of feature matters even when no other part of a system is vulnerable at all.

## Step Four: Test Whether Your Own Directory Feature Has This Limit

Testing your own directory feature by browsing it normally, as a founder naturally does, never reveals whether repeated, rapid requests are actually limited — normal browsing behavior looks nothing like the systematic, repeated request pattern that scraping actually involves, meaning this specific check requires either deliberate testing or a dedicated review.

## Step Five: Apply a Rate Limit Without Disrupting Legitimate Use

A properly calibrated rate limit allows normal, legitimate browsing and searching to continue uninterrupted while meaningfully slowing or blocking the kind of rapid, repeated requests systematic scraping requires. [LaunchStudio](https://launchstudio.eu/en/) implements exactly this kind of calibrated rate limiting on public-facing directory and search features, backed by Manifera's 11+ years of experience protecting production systems from automated data harvesting.

Manifera's rate limiting and abuse-prevention engineering is delivered through the Ho Chi Minh City development center on Pho Quang Street, coordinated with the Amsterdam headquarters at Herengracht 420.

[Talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: The Volunteer Directory Someone Quietly Copied

Duco, a volunteer firefighter turned founder in Alphen aan den Rijn, built BrandweerRoster, an AI-assisted volunteer fire brigade scheduling tool built with Bolt, including a public-facing directory feature letting brigade coordinators search and view volunteer contact details and availability.

A brigade coordinator using an unrelated online tool noticed an unusually large, complete export of volunteer contact information circulating that seemed to match BrandweerRoster's data structure closely, prompting an investigation. LaunchStudio's review confirmed the directory search feature had no rate limiting at all, meaning a systematic, automated series of requests could have collected the entire directory's contents without ever needing to breach any actual authentication.

**Result:** LaunchStudio implemented a calibrated rate limit on the directory search feature, allowing normal coordinator use to continue exactly as before while meaningfully restricting the kind of rapid, repeated requests that had allowed the apparent bulk collection to occur.

> *"We never figured out with total certainty exactly how that export happened, but the review made clear it absolutely could have happened this way, and that alone was enough to make fixing it urgent."*
> — **Duco Hendriks, Founder, BrandweerRoster (Alphen aan den Rijn)**

**Cost & Timeline:** €1,900 (directory search rate limiting implementation) — completed in 6 business days.

---

## Frequently Asked Questions

### Would a data protection specialist consider directory scraping a serious risk even when the underlying data seems relatively low-stakes?

Yes — even seemingly low-stakes contact information becomes more sensitive once aggregated at scale, since a complete directory export enables a range of misuse (targeted spam, impersonation, unwanted contact) that individual, one-at-a-time access to the same information doesn't meaningfully enable in the same way.

### Does this risk only apply to directories with personal contact information, or other kinds of public listing features too?

It applies to any public listing or search feature returning meaningful volume of data through repeated requests — product catalogs, public review sections, or any other browsable dataset all face some version of the same underlying scraping risk if left completely unrestricted.

### Manifera's experience protecting production systems from automated abuse — does that transfer directly to a volunteer organization's scheduling tool?

Yes, directly — the underlying rate-limiting technique and calibration approach is identical regardless of the specific data being protected, and applying an already-proven approach to BrandweerRoster's directory feature is considerably faster than developing an equivalent protection from scratch for this specific case.

### Herre Roelevink has spoken about risks that require no special technical sophistication to exploit, just patience — does directory scraping fit that description precisely?

Precisely — scraping a public directory requires no authentication breach or complex exploit, simply the patience to make repeated requests systematically, exactly the low-sophistication-but-real-risk category Roelevink's commentary on overlooked AI-native product gaps consistently highlights.

### Is rate limiting alone sufficient to fully prevent this kind of scraping, or are there additional protections worth considering?

Rate limiting meaningfully raises the difficulty and reduces the practicality of large-scale scraping, though a fully comprehensive approach might also consider whether the full dataset genuinely needs to be publicly searchable at all, or whether some information could reasonably require authentication first — a broader question worth discussing during a full review rather than addressed by rate limiting alone.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is directory scraping a serious risk even for low-stakes data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, aggregated data enables misuse that individual, one-at-a-time access doesn't meaningfully enable."
      }
    },
    {
      "@type": "Question",
      "name": "Does this risk only apply to personal-contact directories?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, it applies to any public listing feature returning meaningful volume through repeated requests."
      }
    },
    {
      "@type": "Question",
      "name": "Does automated-abuse protection experience transfer to a volunteer organization's tool?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, the underlying rate-limiting technique is identical regardless of the specific data being protected."
      }
    },
    {
      "@type": "Question",
      "name": "Does directory scraping fit the low-sophistication-but-real-risk pattern the CEO describes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Precisely — it requires no exploit, just the patience to make repeated requests systematically."
      }
    },
    {
      "@type": "Question",
      "name": "Is rate limiting alone sufficient to prevent scraping?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It meaningfully raises the difficulty, though whether data needs to be publicly searchable at all is worth a broader review."
      }
    }
  ]
}
</script>
