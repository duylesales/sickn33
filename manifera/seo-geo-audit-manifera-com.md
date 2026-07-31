# SEO/GEO Audit: manifera.com

**Date:** July 31, 2026
**Auditor:** Automated SEO/GEO analysis (external, black-box)
**Target:** https://www.manifera.com/

---

## Executive Summary

Unlike a fully crawler-blocked site, **manifera.com is healthy at the infrastructure and indexation level**: robots.txt is clean and reachable, the sitemap is valid and fresh (last modified July 30, 2026), core pages are indexed by Google, and the site already has real third-party citation signals (Clutch, ITviec, Sortlist, FeaturedCustomers, ZoomInfo) that materially help GEO/AI-answer-engine trust. Notably, **the site already publishes `llms.txt` with a full content export** — a forward-looking GEO signal most competitors don't have.

The gaps found are not about crawlability — they're **on-page and structured-data execution issues** that quietly cap how well the homepage converts crawl budget into rankings, rich results, and LLM-citable entity data:

1. **The homepage `<h1>` is "Experiences of our clients working with us"** — a testimonials-section heading, not a statement of what Manifera does. This is the single highest-value on-page fix on the site.
2. **No Organization/WebSite schema.org markup** — the only structured data present is a `VideoObject` block for embedded YouTube videos. There is no `Organization` entity declaring Manifera's name, logo, founding date, offices, or `sameAs` social/review-platform links, despite that data existing in prose across the site.
3. **The homepage has almost no heading hierarchy** — one single `<h2>` ("Our awards") structures ~1,478 words of homepage copy. Search engines and LLMs rely on headings to segment and understand page topics.
4. Minor image, social-preview, and legacy-URL hygiene issues detailed below.

**Overall verdict: 🟡 Good foundation, medium-impact on-page/structured-data gaps — fixable in days, not months.**

---

## Methodology & Limitations

This audit used external, unauthenticated tooling only — no Google Search Console, GA4, or CMS access.

1. Direct HTTP requests (`curl`) to the homepage, `robots.txt`, `sitemap.xml`, `llms.txt`, and several internal pages — inspecting status codes, headers, and raw HTML.
2. Parsing of the raw homepage HTML for title/meta tags, canonical tags, Open Graph tags, JSON-LD structured data, heading hierarchy, and image `alt` attribute coverage.
3. DNS resolution (`dig`) and TLS certificate inspection (`openssl s_client`).
4. Web search verification (`site:` operator and brand-name queries) to check indexation depth and off-page/third-party mentions.

**Limitation:** this audit could not measure real Core Web Vitals (LCP/CLS/INP) or run a rendered-DOM Lighthouse pass — those require a headless browser this tooling doesn't have. Raw HTML size and resource-tag counts are reported as rough proxies only; a PageSpeed Insights / Lighthouse run is recommended as a follow-up (see Recommendations).

---

## What's Already Working Well

- **Crawlability is clean.** `robots.txt` returns `200` with sensible rules; `sitemap.xml` `301`-redirects to Yoast's `sitemap_index.xml` (a normal, expected pattern — not a block), which in turn lists 10 well-formed sub-sitemaps (posts, pages, portfolio, testimonials, technology, categories, tags, authors) with real, recent `lastmod` dates.
- **Indexation is healthy.** A `site:manifera.com` search returns the homepage, `/portfolio/`, `/remote/`, `/about-us/`, `/blog/`, `/services/`, and `/contact-us/` — the core navigation pages are all indexed with sensible titles.
- **`llms.txt` already exists and is substantive** — it lists dozens of real posts/pages and points to a `llms-full.txt` for full-content export. This is a genuinely rare, forward-looking GEO signal; most competitor sites in this space don't have this at all.
- **Strong third-party/off-site presence**, which matters enormously for GEO (LLMs cite and cross-reference these platforms) and for classic link-equity SEO: Clutch (client reviews), ITviec (8 reviews), Sortlist, FeaturedCustomers (29 reviews / 19 case studies), ZoomInfo. This gives both Google and AI answer engines independent corroboration of who Manifera is and what clients say about them — exactly the kind of E-E-A-T signal a services business needs.
- **Security/transport layer is solid**: HSTS with `preload` and `includeSubDomains`, `X-Frame-Options: SAMEORIGIN`, `X-Content-Type-Options: nosniff`, HTTP/2 with HTTP/3 advertised via `alt-svc`, and a valid, auto-renewing wildcard Let's Encrypt certificate (`*.manifera.com`).
- **Canonical tags, viewport meta, and Open Graph basics are present and correct** on the homepage (`og:title`, `og:description`, `og:url`, `og:site_name` all populated).

---

## Finding #1 (High Priority): Homepage H1 Doesn't Match the Page's Purpose

The homepage `<title>` is:

> `Manifera | Experienced, Reliable Software Development Teams`

But the actual `<h1>` rendered on the page is:

> `Experiences of our clients working with us`

This is a heading that belongs on a testimonials block, not the single most important on-page SEO element of the homepage. Search engines weight `<h1>` heavily as a summary of page intent, and it is one of the first things an LLM crawler extracts to understand "what is this page about." Right now, the strongest on-page signal on manifera.com's homepage tells crawlers this is a testimonials page, not a software development company's homepage.

**Fix:** Set the `<h1>` to a clear statement of what Manifera does and for whom — e.g. something aligned with the title tag ("Experienced, Reliable Software Development Teams for AI-Native Founders and SMEs"), and demote "Experiences of our clients working with us" to an `<h2>` on the testimonials section where it belongs.

---

## Finding #2 (High Priority): No Organization / WebSite Structured Data

The homepage contains exactly **one** JSON-LD block, and it's a `VideoObject`/`ItemList` schema auto-generated for two embedded YouTube videos. There is no:

- `Organization` schema (company name, logo, founding date, `sameAs` links to LinkedIn/Clutch/etc.)
- `WebSite` schema (enables sitelinks search box eligibility)
- `LocalBusiness` schema for the Amsterdam office (or `ProfessionalService`), despite Manifera having a real, citable address

This matters for two distinct reasons:

- **Classic SEO:** `Organization` schema is what feeds Google's Knowledge Panel eligibility and helps disambiguate "Manifera" from unrelated uses of the word.
- **GEO specifically:** LLM-based answer engines increasingly rely on structured entity data (schema.org, Wikidata-style facts) to ground factual claims about a company — founding year, locations, services, leadership. Right now that information exists only in prose scattered across pages, which is harder for an LLM to extract reliably than a single structured `Organization` block with `sameAs` links to the Clutch, ITviec, and FeaturedCustomers profiles this audit found.

**Fix:** Add a site-wide `Organization` JSON-LD block (via the Yoast SEO plugin's built-in Organization schema settings, since the site already runs Yoast) with `name`, `logo`, `foundingDate`, `address` (Amsterdam/Singapore/Ho Chi Minh City), and `sameAs` pointing to LinkedIn, Clutch, and other verified profiles.

---

## Finding #3 (Medium Priority): Thin Heading Hierarchy on the Homepage

The homepage has roughly 1,478 words of visible text but only **one `<h2>`** ("Our awards") and no other subheadings detected in the raw HTML. A page with this much content and no topic-segmenting headings is harder for both search engines and LLMs to parse into distinct sections (services, process, team, awards, testimonials, etc.), and it's a missed opportunity for secondary-keyword targeting that a proper H2/H3 structure would naturally capture.

**Fix:** Add descriptive `<h2>`/`<h3>` tags to each homepage section (e.g., "Our Services," "Why Work With Manifera," "Our Process," "Client Results") instead of relying on styled `<div>`s with no semantic heading markup.

---

## Finding #4 (Low-Medium Priority): Image `alt` Text Gaps

Of 43 `<img>` tags on the homepage, **12 have an empty `alt=""`** and **1 is missing the `alt` attribute entirely**. Empty `alt` is sometimes intentional for purely decorative images, but at this volume it's worth an audit — every client-logo, award-badge, or team photo without descriptive alt text is a missed opportunity for image search visibility and a real accessibility gap (screen readers skip or announce nothing useful for these).

---

## Finding #5 (Low Priority): Social Share Image Is Favicon-Sized

`og:image` points to `Manifera-Software-Outsourcing-logo.png` at **225×225px**. Most social platforms (LinkedIn, X/Twitter, Slack, Facebook) expect roughly **1200×630px** for link-preview cards; a 225×225 square logo will render small, cropped, or blank depending on the platform. Since Manifera is actively cited on review platforms and likely shared in B2B contexts (LinkedIn especially), this is a low-effort, visible-impact fix.

---

## Finding #6 (Low Priority): Legacy `/nl/` Cruft in robots.txt

`robots.txt` disallows two Dutch-language URLs:
- `/nl/how-to-choose-a-custom-software-company/` → currently `301`-redirects
- `/nl/in-house-vs-outsourcing-software-development-2/` → currently `404`s

Disallowing a URL that already 404s is a no-op (dead weight in the file), and disallowing a URL that 301-redirects is unusual — normally you'd let the redirect do the work rather than also blocking it. This looks like leftover configuration from a discontinued Dutch-language section of manifera.com (distinct from the separate NL translations that live on the LaunchStudio property). Not urgent, but worth cleaning up during the next robots.txt review so the file only contains rules that are still doing something.

---

## Finding #7 (Low Priority): `/favicon.ico` Returns 404

The site correctly serves a favicon via `<link rel="icon">` tags pointing to `/wp-content/uploads/.../cropped-Manifera-Software-32x32.png`, which is what modern browsers use. However, the conventional root-level `/favicon.ico` path 404s. Some older tools, browser tab fallbacks, and third-party services that hardcode a check against `/favicon.ico` (rather than reading the `<link>` tag) won't find an icon. Cheap fix: place a `favicon.ico` at the site root.

---

## Technical & Infrastructure Snapshot

| Item | Value |
|---|---|
| CMS | WordPress (Yoast SEO plugin detected via sitemap XSL and meta patterns) |
| A record (`www` and apex) | `136.243.57.57` |
| Nameservers | `ns1/ns2/ns3.digitalocean.com` |
| TLS certificate | Let's Encrypt wildcard `*.manifera.com`, issued 2026-06-11, expires 2026-09-09 |
| HTTP protocol | HTTP/2, with HTTP/3 advertised via `alt-svc` |
| `robots.txt` | `200`, clean, points to correct sitemap index |
| `sitemap.xml` | `301` → `sitemap_index.xml` (normal Yoast behavior), 10 sub-sitemaps, most recently updated 2026-07-30 |
| `llms.txt` | `200`, substantial content list + link to `llms-full.txt` |
| `/favicon.ico` | `404` (favicon is served via `<link>` tags instead — see Finding #7) |
| Homepage HTML size | ~212 KB |
| Homepage resource tag count | ~115 `<script>`/`<link>`/`<img>` tags (rough proxy only; not a substitute for a real Lighthouse run) |

---

## Off-Page / GEO Signal Summary

External verification found genuine, substantive third-party presence — a strong foundation for both classic backlink SEO and GEO entity grounding:

- **Clutch.co** — client review profile
- **ITviec** — 8 employer/company reviews
- **Sortlist** — agency directory listing
- **FeaturedCustomers** — 29 customer reviews, 19 case studies
- **ZoomInfo** — company data profile

No evidence of negative signals (spam penalties, deindexation, broken core pages) was found during this audit.

---

## Prioritized Recommendations

**P0 — High impact, low effort:**
1. Fix the homepage `<h1>` to state what Manifera does, not "Experiences of our clients working with us" (Finding #1).
2. Add `Organization` (and ideally `WebSite`) JSON-LD schema via Yoast's built-in schema settings, including `sameAs` links to Clutch/ITviec/LinkedIn (Finding #2).

**P1 — Medium effort, compounding value:**
3. Add proper `<h2>`/`<h3>` structure to the homepage sections (Finding #3).
4. Audit and fill in missing/empty `alt` text on the 13 flagged homepage images (Finding #4).
5. Replace the 225×225 `og:image` with a proper 1200×630 social share card (Finding #5).

**P2 — Housekeeping:**
6. Clean up the two dead/legacy `/nl/` rules in `robots.txt` (Finding #6).
7. Add a root-level `favicon.ico` for legacy compatibility (Finding #7).
8. Run a real Lighthouse/PageSpeed Insights pass to get actual Core Web Vitals (LCP, CLS, INP) — this audit's tooling could only proxy page weight, not real rendering performance.

---

## Appendix: Raw Evidence Summary

- `curl -D - https://www.manifera.com/` → `HTTP/2 200`, WordPress `link` headers (`wp-json`), full HSTS/security headers present.
- `robots.txt` → `200`, disallows `/category/`, `/feed/`, and two legacy `/nl/` URLs; points to `sitemap_index.xml`.
- `sitemap.xml` → `301` → `sitemap_index.xml` → 10 sub-sitemaps, most recent `lastmod` 2026-07-30.
- `llms.txt` → `200`, real content list + `llms-full.txt` reference.
- `favicon.ico` → `404` (favicon served via `<link>` tag instead, at a different path).
- Homepage `<title>`: "Manifera | Experienced, Reliable Software Development Teams"; `<h1>`: "Experiences of our clients working with us" (mismatch — Finding #1).
- Homepage JSON-LD: 1 block, type `VideoObject`/`ItemList` only — no `Organization`/`WebSite` schema.
- Homepage images: 43 total, 12 with `alt=""`, 1 missing `alt` entirely.
- `og:image`: 225×225px (favicon-sized, not a proper social card).
- `/about/` → `301` → `/about-offshore-software-development-vietnam/`; separately, `/about-us/` (`200`, correct canonical) is the page actually indexed by Google — two different "about" paths exist, worth a routing review.
- `/home/` → `301` (redirects, not a duplicate-content risk).
- TLS: Let's Encrypt wildcard `*.manifera.com`, issued 2026-06-11, expires 2026-09-09.
- `site:manifera.com` search → homepage, `/portfolio/`, `/remote/`, `/about-us/`, `/blog/`, `/services/`, `/contact-us/` all indexed.
- Off-site mentions confirmed: Clutch, ITviec (8 reviews), Sortlist, FeaturedCustomers (29 reviews/19 case studies), ZoomInfo.

---

*This audit was conducted externally and automatically, without access to Manifera's Search Console, analytics, or CMS admin. Findings reflect what public, unauthenticated crawlers and tools observe when reaching manifera.com.*
