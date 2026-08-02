# LaunchStudio (launchstudio.eu) — SEO & GEO Audit

**Date:** 2026-07-31
**Scope:** Technical SEO, on-page SEO, structured data, content/topical authority, and GEO (Generative Engine Optimization — visibility in AI answer engines like ChatGPT, Perplexity, Google AI Overviews).
**Method:** Live inspection of raw HTML/HTTP responses for the homepage (NL + EN), a sample blog post, `robots.txt`, `sitemap_index.xml`, `post-sitemap.xml`, `page-sitemap.xml`, and `llms.txt`. Findings are based on what crawlers and LLMs actually receive over HTTP, not a rendered/JS-executed view.

---

## 1. Executive Summary

LaunchStudio has the fundamentals of a well-built WordPress/Yoast site: clean `robots.txt`, a working XML sitemap, server-rendered content (not JS-only), correct `hreflang` NL↔EN pairing, and — notably — it already publishes an **`llms.txt`** file, which most competitors don't have yet. That puts it ahead of the curve on raw GEO readiness.

However, the audit surfaced one **systemic technical bug** (duplicate, conflicting `<meta>`/OG tags site-wide) and several **structural gaps** that are actively limiting both classic SEO performance and AI-answer-engine visibility:

1. A **duplicate/conflicting Open Graph & meta-description block** ships on every page (homepage and blog posts alike), with a second, broken, hardcoded tag sitting alongside the correct Yoast-generated one.
2. **No `Organization`/`LocalBusiness` schema anywhere on the site** — despite the brand strategy explicitly calling LaunchStudio a "GEO-entity" with three real office addresses (Amsterdam, Singapore, Ho Chi Minh City). None of that entity data is machine-readable.
3. **No `FAQPage` schema**, even though a full FAQ exists on the homepage in plain HTML — a straightforward, high-leverage win for both SERP rich results and LLM extraction.
4. **Blog posts are thin** (~250–350 words of actual article body in the sample checked) and use a **raw system username ("phu.lt") as the visible author**, which undermines E-E-A-T/author-trust signals.
5. **A large content-production/publication gap**: `content_inventory.md` in this project records **362 articles** produced, but the live `post-sitemap.xml` only contains **71 unique articles** (142 URLs incl. NL/EN pairs). The majority of produced content appears to never have been published.
6. The homepage **never links to `manifera.com`** anywhere in its HTML, despite the brand's own content guidelines (`launchstudio_info.md`, §1.2 and §10) requiring a Manifera mention/link for E-E-A-T — text mentions exist, but zero outbound hyperlinks.
7. `llms.txt` exists but is **auto-generated and incomplete** — it lists only 5 of the 71 live articles and omits pricing, packages, and the process/offer entirely, so an LLM reading it gets almost no picture of what LaunchStudio actually sells.

None of these are catastrophic on their own, but together they mean LaunchStudio is under-representing itself to both Google and AI answer engines relative to the amount of content work already invested.

---

## 2. Technical SEO

### 2.1 Duplicate/conflicting meta tags (High priority — site-wide bug)

The `<head>` on **every page checked** (homepage NL, homepage EN, and the sample blog post) contains **two separate blocks of Open Graph tags**, apparently from two sources (a hardcoded block, likely in the custom `launchstudio` theme header, plus Yoast SEO's own output):

```html
<!-- Block 1 — hardcoded, appears first -->
<meta property="og:title" content="Launch Studio">
<meta property="og:description" content="LaunchStudio helps AI-native founders...">
<meta property="og:type" content="website">
<meta property="og:url" content="https://launchstudio.eu/ai-agents-vs-ai-copilots-hoe-bouw-je-jouw-ai/">
<!-- ^ stale URL pointing to an unrelated blog post, not the current page -->

<!-- Block 2 — Yoast-generated, appears later, correct -->
<meta property="og:locale" content="nl_NL" />
<meta property="og:type" content="website" />
<meta property="og:title" content="Launch Studio" />
<meta property="og:url" content="https://launchstudio.eu/" />
<meta property="og:site_name" content="Launch Studio" />
```

The same pattern repeats on the EN homepage (stale `og:url` pointing to `/en/ai-agents-vs-ai-copilots-which-way-to-build-your-ai/`) and on the sample blog post, where it shows up as **two duplicate `<meta name="description">` tags** — one Yoast-correct, one a raw, mid-sentence-truncated auto-excerpt:

```html
<meta name="description" content="Lieke&#8217;s story Lieke is an HR consultant. She had a problem she encountered with every client: teams that didn&#8217;t know...">
<meta name="description" content="Lieke&#039;s story Lieke is an HR consultant. She had a problem she encountered with every client: teams that didn&#039;t know how to give each other feedback. She" />
```

**Why it matters:** Facebook, LinkedIn, and most social-preview scrapers take the **first** OG tag they encounter — meaning link previews for the homepage may show the wrong URL/thumbnail (pointing at an old blog post instead of the page actually being shared). Two `<meta name="description">` tags is invalid HTML; browsers/crawlers pick one unpredictably, and it's pure noise for LLM crawlers trying to extract a canonical summary.

**Fix:** Find and remove the hardcoded OG/description block in the theme (`wp-content/themes/launchstudio/header.php` or equivalent) and let Yoast be the single source of truth. This is a one-time theme fix that benefits every page on the site simultaneously.

### 2.2 Title tags — inconsistent and, on EN, malformed

| Page | Title tag | Length |
|---|---|---|
| NL homepage | `Launch Studio` | 14 chars — too short, no keywords, wastes the SERP title opportunity |
| EN homepage | `Launch Studio – LaunchStudio helps AI-native founders get prototypes launch-ready with security, payments, hosting, and deployment.` | 131 chars — will be truncated in every SERP; duplicates the meta description almost verbatim instead of being a distinct, front-loaded, keyword-focused title |
| Sample blog post | `From prototype to 47 paying customers in 3 weeks - Launch Studio` | 66 chars — good length, but no primary keyword (e.g. "AI prototype", "launch-ready") |

**Recommendation:** Standardize on ~50–60 character titles, front-load the primary keyword, and stop reusing the meta description as the title on EN pages. Something like: `Launch Studio — Ship Your AI Prototype to Production` (NL homepage) and a parallel EN version, both under 60 characters.

### 2.3 Stray `rel="next"` on the homepage (Low priority)

The homepage `<head>` contains `<link rel="next" href="https://launchstudio.eu/page/2/" />`, implying the homepage is paginated content. Google deprecated `rel=next/prev` in 2019, so this has no real ranking effect today, but it's a signal the front page's query loop isn't fully decoupled from the blog archive loop. Low priority cleanup.

### 2.4 What's already correct

- `robots.txt` is clean (`Disallow:` empty, sitemap referenced correctly).
- `sitemap_index.xml` is valid, segmented (post/page/category/tag/author), and freshly generated (`lastmod` today).
- Canonical tags are present and self-referencing correctly on every page checked.
- `hreflang` NL↔EN pairing is implemented correctly on both the homepage and blog posts (reciprocal `nl`/`en` alternates).
- Security headers are solid: HSTS with `preload`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`.
- Content is **server-rendered** — all key homepage copy (stats, pricing, testimonials, FAQ) is present in the raw HTML with no JavaScript execution required. This is good for both traditional crawlers and the many LLM crawlers that don't render JS.
- Viewport meta tag present (mobile-friendly baseline).

### 2.5 Performance signals

- TTFB ~0.56–0.58s on both homepage and a blog post — acceptable but not fast; no `Cache-Control`, `Age`, or CDN headers (e.g. Cloudflare `CF-Ray`) were observed on either request, suggesting pages may be served without an edge cache/CDN layer. Adding page-level caching (WP Rocket/W3TC) or a CDN would improve Core Web Vitals, which is a ranking factor and also affects crawl efficiency.
- Homepage weighs ~228 KB of HTML alone (before CSS/JS/images) — not excessive, but worth monitoring as more sections get added.
- Images: at least one avatar/testimonial image is shipped as a large inline base64 `data:` URI with `alt=""` (empty alt). Inline base64 images bypass browser caching and bloat HTML weight; empty `alt` on a person's photo is a missed accessibility/SEO signal (should describe the person, e.g. `alt="Marieke, founder"`).

---

## 3. Structured Data (Schema.org)

Current state:

| Page | Schema types present |
|---|---|
| Homepage | `CollectionPage`, `BreadcrumbList`, `WebSite` (with `SearchAction`) |
| Blog post | `Article`, `WebPage`, `ImageObject`, `BreadcrumbList`, `WebSite`, `Person` (author) |

**Missing — and each is a concrete opportunity:**

- **`Organization` schema (site-wide).** There is no `Organization` node anywhere — no `logo`, no `sameAs` (LinkedIn, etc.), no `address`. This is the single biggest structured-data gap relative to LaunchStudio's own stated strategy: `launchstudio_info.md` §1.3 explicitly defines three offices (Amsterdam, Singapore, Ho Chi Minh City) as a "GEO-Entity" that should be reinforced in every article, but **none of that entity data is expressed in machine-readable schema**. AI answer engines and Google's Knowledge Graph lean heavily on `Organization`/`sameAs`/`address` markup to resolve "who is this company, where are they based, is this a real, connectable entity" — right now that resolution has to happen from prose alone.
- **`FAQPage` schema.** The homepage already contains a full FAQ in plain HTML ("Wat kost het precies?", "Blijft mijn code van mij?", etc. — matching almost verbatim the FAQ list in `launchstudio_info.md` §7), but it isn't marked up as `FAQPage`. This is normally a quick win (FAQ rich results in Google, and FAQ blocks are exactly the shape LLMs prefer to lift verbatim for direct-answer citations).
- **`Person` schema for the author is under-specified.** The blog post's `Person` node uses `"name":"phu.lt"` — an internal username, not a real byline. There's no `jobTitle`, `image`, `sameAs`, or `description`. For E-E-A-T (and for GEO — LLMs weight named, credentialed authors when deciding what to cite as a trustworthy source), this should be a real name (e.g. a LaunchStudio/Manifera team member) with a short bio and LinkedIn `sameAs`, or explicitly attributed to "LaunchStudio Team" / "Herre Roelevink" per the brand doc.
- **No `Service`/`Product`/`Offer` schema** for the two packages ("Launch Ready" €800–3,500, "Launch & Grow" €2,500–7,500+€49/mo) or the price calculator. Pricing is one of the most common things people ask AI assistants about ("how much does it cost to launch an AI prototype") — structured `Offer` data is exactly what lets an LLM answer that question citing LaunchStudio directly and correctly, instead of paraphrasing loosely from prose (or not surfacing it at all).

---

## 4. Content & Topical Authority

### 4.1 A large produced-vs-published gap

The project directory contains a full content-inventory (`content_inventory.md`) claiming **362 articles** produced (302 converted from HTML + 38 recovered), each with title, keywords, buyer stage, and summary, plus a WordPress uploader script.

The live site's `post-sitemap.xml`, however, contains only **142 URLs = 71 unique articles** (each mirrored NL/EN). That means **roughly 80% of the produced content is not live on the site**. Publish dates on the live posts also show an uneven cadence — 38 in March 2026, 14 in June, then a burst of 90 in July — consistent with batches of a larger backlog being published irregularly rather than a steady drip.

**Why it matters for both SEO and GEO:** topical authority (the thing that makes Google *and* LLMs treat a domain as a trustworthy source on "AI prototype to production") compounds with sustained, broad keyword coverage over time. A large ready-made backlog sitting unpublished is the single largest opportunity on the table here — bigger than any on-page fix — because the content work is already done; it just isn't live.

**Recommendation:** Reconcile `content_inventory.md` against `post-sitemap.xml` to get an exact published/unpublished list, then resume publishing on a steady cadence (e.g. 3–5/week) rather than large batch-bursts, which read more naturally to Google and avoid any appearance of manipulative publishing velocity.

### 4.2 Thin article bodies

The sample post checked (`from-prototype-to-47-paying-customers-in-3-weeks`) has a full page word count of only ~500 words **including all navigation, footer, and chrome text** — meaning the actual case-study body (4 H2 sections: "Lieke's story," "The roadblock," "What we found," "The lesson") is roughly 250–350 words. That's thin for a case-study format competing for AI/SaaS-adjacent keywords, and thin content also gives an LLM very little to actually quote or summarize when deciding whether to cite the page.

If this word count is representative of the broader 71-article set (worth spot-checking a few more), lengthening flagship articles — especially the case studies and comparison/how-to formats called out in `launchstudio_info.md` §8.3 — to 800–1,200 words would meaningfully improve both rankings and LLM-citability without needing new topics.

### 4.3 Manifera cross-linking isn't actually happening

`launchstudio_info.md` (§1.2, §10) mandates that content mention Manifera for E-E-A-T and link to specific Manifera pages (About, Portfolio, Services). In practice:

- The homepage mentions "Manifera" as **plain text only, 3 times** (logo tagline "door Manifera," and in the CEO testimonial attribution) — **zero hyperlinks** to `manifera.com` anywhere in the homepage HTML.
- The sample blog post does link to `manifera.com` once — so it's happening in at least some articles, but not consistently on the homepage, which is the page most likely to be crawled and cited.

**Recommendation:** Turn the "door Manifera" logo subtitle into an actual link to `manifera.com/about-us/`, and audit a sample of published posts to confirm the Manifera link is present per the internal linking map in §10 of the brand doc.

---

## 5. GEO (Generative Engine Optimization) — AI Answer Engine Readiness

This section evaluates LaunchStudio specifically for visibility in ChatGPT, Perplexity, Claude, and Google AI Overviews — which rely on crawlable, well-structured, entity-clear, directly-quotable content rather than classic keyword density.

### 5.1 `llms.txt` exists — ahead of most competitors, but incomplete

`https://launchstudio.eu/llms.txt` returns 200 and is auto-generated by Yoast SEO. Having this file at all is a genuine advantage — most competitor sites won't have one yet. However, the current version is sparse:

- Lists only **5 blog posts** out of 71 live articles.
- Lists 5 static pages, but **two are legal boilerplate** (Terms, Privacy) taking up scarce space.
- **Does not mention pricing, packages, the 3-step process, or the core value proposition at all** — an LLM reading only `llms.txt` would have no idea LaunchStudio takes AI prototypes to production for €800–7,500 in 1–3 weeks.

**Recommendation:** Yoast's auto-generated `llms.txt` is a starting point, not a finished asset. Consider a manually-curated (or scripted, non-Yoast) `llms.txt` that leads with a clear one-paragraph company/offer summary, links the pricing/packages page and process page explicitly, and lists more of the 71 live articles (or at least the highest-value ones by cluster, per the keyword taxonomy already defined in §9 of `launchstudio_info.md`).

### 5.2 Server-rendered content is a real GEO strength

Because the homepage's key facts (the 80% AI-code-in-production-failure stat, package pricing, the 3-step process, testimonials, FAQ answers) are all present in the raw HTML with no JavaScript required, LLM crawlers that don't execute JS (a large share of them) can actually read this content today. This should be preserved as a hard constraint in any future redesign — don't let key facts move behind client-side rendering.

### 5.3 Entity clarity is the weakest link for GEO specifically

GEO depends heavily on an LLM being able to confidently answer "who is this," "is this a real company," and "can I trust this source" — which is exactly what `Organization` schema, `sameAs` social links, real named authors, and address data are for (see §3 above). Right now this entity data lives only in an internal strategy doc (`launchstudio_info.md`) and in page prose, not in the site's actual markup. This is the highest-leverage GEO fix available: it's a one-time schema addition (not new content) that directly strengthens how confidently any AI system can identify and cite LaunchStudio.

### 5.4 FAQ content not marked as `FAQPage`

Already covered in §3, but worth repeating in GEO terms: `FAQPage` schema with clean Q&A pairs is one of the most reliably-extracted formats for direct-answer AI responses ("How much does it cost to launch an AI prototype with LaunchStudio?"). The content already exists on the homepage; only the markup is missing.

---

## 6. Prioritized Recommendations

**Quick wins (hours, high impact, no new content needed):**
1. Remove the duplicate hardcoded OG/meta-description block from the theme header — fixes stale social-preview URLs and invalid duplicate meta tags site-wide.
2. Add `FAQPage` schema around the existing homepage FAQ content.
3. Shorten and rewrite the EN homepage `<title>` (currently 131 chars, duplicates the meta description).
4. Hyperlink "door Manifera" in the homepage logo to `manifera.com`.
5. Fix the `Person` author schema on blog posts — replace `"phu.lt"` with a real name/role and add `sameAs`.

**Medium effort, high impact:**
6. Add `Organization` schema site-wide with `logo`, `sameAs` (LinkedIn), and the Amsterdam/Singapore/HCMC addresses already documented internally.
7. Add `Offer`/`Service` schema for the two packages and price ranges.
8. Manually curate `llms.txt` to lead with the value prop, pricing, and a fuller article list instead of relying on Yoast's sparse auto-generation.

**Larger, ongoing effort:**
9. Reconcile `content_inventory.md` (362 articles) against `post-sitemap.xml` (71 live) and resume publishing the backlog on a steady, non-bursty cadence.
10. Lengthen thin article bodies (case studies especially) toward 800–1,200 words to improve both ranking depth and LLM-citability.
11. Add page-level caching/CDN to reduce TTFB and improve Core Web Vitals.

---

*Compiled from a live inspection of launchstudio.eu on 2026-07-31 (raw HTTP responses, not a rendered browser view). Internal context cross-referenced from `launchstudio_info.md` and `content_inventory.md` in this project directory.*
