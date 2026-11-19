# Manifera (manifera.com) - SEO & GEO Audit, 19 November 2026

**Supersedes:** `seo-geo-audit-manifera-com.md` (31 July 2026; kept for history, section 2 tracks each of its findings)
**Scope:** technical SEO, on-page, structured data, content and topical authority, GEO (visibility in ChatGPT, Perplexity, Claude, Gemini and Google AI Overviews)

**Method:**

- Raw HTTP crawl (`curl`) of `robots.txt`, `sitemap_index.xml` and all 12 sub-sitemaps, plus `llms.txt` and `llms-full.txt`.
- On-page parse of all 28 URLs in `page-sitemap.xml` and the 8 newest posts: title, meta, canonical, OG, headings, images, JSON-LD and word count.
- Access check with 25 crawler user-agents.
- Text-similarity test on suspected duplicate page pairs.
- WordPress data via MCP: plugins, post counts, and Yoast scores for the 40 most recently modified posts.
- Web search for third-party mentions.

**Limitations:**

- No Search Console or GA4 data.
- The PageSpeed Insights API was over its daily quota, so this audit has no Core Web Vitals. Performance uses TTFB, HTML weight and asset counts as proxies.
- The crawl sees raw HTML, not a JS-rendered DOM.

---

## 1. Executive summary

Manifera's foundations are healthy:

- Every AI crawler is allowed.
- The sitemaps are fresh. Posts were updated on 18 Nov.
- `llms.txt` exists.
- The new articles are long: 2,100-3,400 words, H2/H3-structured, with a real author name.
- The Yoast scores of recent posts are good or OK, never bad.
- Since July a `Corporation` node and `WebSite` schema have been added.

The problems sit in the **site template and the older page inventory**. That is the part buyers and LLMs read first when they try to understand "what Manifera is":

1. **The homepage H1 is still "Experiences of our clients working with us".** The homepage also still has only 1 H2. Neither has changed since July.
2. **9 key pages have an empty `<h1>`**, including 4 service pages and the contact page. The theme template outputs `<h1></h1>`.
3. **Blog posts are marked up as `ProfessionalService`, not `Article`.** They have no author `Person` and no dates in the schema. The cause is the *Schema & Structured Data for WP* plugin, which replaces Yoast's schema. The `Corporation` node has `sameAs: []` and no address.
4. **Duplicate pages are indexable** at 92-98% similarity:
   - `/contact-us/` = `/contact-us1/`
   - `/services/webshop-development/` ≈ `/services/web-shops-ecommerce-development/`
   - `/about-us/setting-up-your-offshore-team/` ≈ `/about-us/setting-up-your-team/`
5. **Internal numbering leaks into titles and H1s**: "04-Blog", "02-Portfolio page", "05-Contact", "06-Privacy Policy", "07-Terms of Service".
6. **About 600 thin archive URLs are in the index.** There are 457 tags, of which 263 have 1 post and 100 have 0. The 51 technology pages carry about 115 words each and no meta description. And `/category/` is blocked in `robots.txt` while `category-sitemap.xml` submits those same URLs.
7. **GEO entity data is thin and inconsistent.**
   - The schema has no `sameAs`.
   - The About page says "based in Singapore and Ho Chi Minh City" while the brand docs say Amsterdam HQ.
   - No Clutch profile was found in search.
   - **Not one link** goes from manifera.com to LaunchStudio.

**Verdict: 🟡 Good content engine on an outdated template.** Findings 1-5 are template and settings fixes, about 2-3 developer days. They affect every page that sells.

### Scorecard

| Area | Status | vs. 31 Jul |
|---|---|---|
| Crawlability (Google, Bing, AI bots) | 🟢 All 25 UAs return 200 | = |
| Sitemaps | 🟡 Fresh, but submit thin taxonomies and a robots-blocked category sitemap | ⬇ found new |
| Homepage on-page | 🔴 Wrong H1, 1 H2 | = |
| Service/landing pages | 🔴 Empty H1 on 9 pages, duplicates | ⬇ found new |
| Titles and meta | 🟠 Numbered titles, new-post titles 78-107 chars | ⬇ |
| Structured data | 🟠 Corporation + WebSite added; posts wrong type, no sameAs | ⬆ partial |
| Content depth (new posts) | 🟢 2,100-3,400 words | ⬆⬆ |
| Content freshness (old posts) | 🟠 Dated 2017-2022 event and "2020" posts still indexed | = |
| E-E-A-T and author | 🟡 "Duy Le" byline in meta, not in schema | ⬆ |
| Off-site entity | 🟡 GoodFirms, ITviec, TopDev, VietnamWorks, KVK, FeaturedCustomers; no Clutch found | = |
| llms.txt | 🟠 Auto list, oldest posts first, no company summary | = |
| Performance (proxy) | 🟠 TTFB 0.68-1.27 s, homepage 211 KB HTML, 37 scripts, 12 stylesheets | = |

---

## 2. Progress since the 31 July audit

| # | July finding | Status 19 Nov | Evidence |
|---|---|---|---|
| 1 | Homepage H1 = "Experiences of our clients working with us" | ❌ Open | Unchanged |
| 2 | No Organization / WebSite schema | 🟡 Partly | `Corporation` + `WebSite` + `ContactPoint` now on homepage; `sameAs: []`, no address, no foundingDate |
| 3 | Homepage has 1 H2 | ❌ Open | Still 1 H2 ("Our awards"), 6 H3 |
| 4 | Homepage image alt gaps (12 empty, 1 missing) | ❌ Open | Same: 43 images, 12 `alt=""`, 1 missing |
| 5 | `og:image` 225×225 logo | ❌ Open | Homepage and 12 other pages still use `Manifera-Software-Outsourcing-logo.png` |
| 6 | Legacy `/nl/` rules in robots.txt | ❌ Open | Unchanged |
| 7 | `/favicon.ico` 404 | ❌ Open | Still 404 |
| 8 | Run Lighthouse | ❌ Open | Not done (and API quota blocked it today) |

---

## 3. Findings and fixes

Priority key: **P0** = this week, **P1** = this month, **P2** = backlog. Effort: S < 2 h, M < 1 day, L > 1 day.

### F1 (P0, S) - Homepage H1 and heading structure

**Evidence.**

- `<title>`: `Manifera | Experienced, Reliable Software Development Teams`
- `<h1>`: `Experiences of our clients working with us`
- 1 H2 (`Our awards`) and 6 H3 on a 1,516-word page.

**Why it matters.**

- The H1 is the strongest on-page statement of what a page is about. Today it tells Google and LLM extractors that the homepage is a testimonials page.
- With 1 H2, the page's sections (services, model, process, clients) are not machine-separable.

**Fix (theme `manifera3`, homepage template).**

1. Hero heading becomes the only `<h1>`. Proposed: `Dedicated software development teams in Vietnam, managed from Amsterdam`, or keep closer to the title: `Experienced, reliable software development teams`.
2. Change the testimonial heading to `<h2>Experiences of our clients working with us</h2>`.
3. Give each homepage section a real `<h2>`, for example:
   - "Our services"
   - "How a dedicated team works"
   - "Why Manifera"
   - "Clients and projects"
   - "Awards"
   - "Talk to our Amsterdam team"
4. Check: `curl -s https://www.manifera.com/ | grep -o '<h1[^>]*>[^<]*'` should return exactly one, non-empty H1.

---

### F2 (P0, S) - Empty `<h1>` on 9 key pages

**Evidence.** Each of these pages renders `<h1></h1>` (empty). The visible heading is in another element.

| URL | Title |
|---|---|
| `/services/offshore-software-development/` | Offshore Software Development Teams - Manifera |
| `/services/web-app-develop/` | Web app development - Manifera |
| `/services/mobile-app-development/` | Mobile app development - Manifera |
| `/services/webshop-development/` | Webshop/eCommerce Developments - Manifera |
| `/services/migration-to-nl-euro-cloud/` | Migration to NL/Euro Cloud - Manifera |
| `/services/migration-to-nl-euro-cloud-en/` | Migration to NL/Euro Cloud English - Manifera |
| `/contact-us/` | Contact Us - Manifera |
| `/about-us/manifera-technologies/` | Technologies - Manifera |
| `/about-us/setting-up-your-offshore-team/` | Setting Up Your Offshore Development Team - Manifera |

These are the pages that rank for, and get cited for, the commercial terms "offshore software development", "web app development" and "mobile app development".

**Fix.** These pages share a template (see the shared `section9-bg.webp` / `custom-software.webp` OG images). In that template:

- Print the page's hero heading inside the `<h1>`, or
- Remove the empty `<h1>` and promote the hero heading to `<h1>`.

Proposed H1s:

| Page | H1 |
|---|---|
| offshore-software-development | `Offshore software development teams in Vietnam` |
| web-app-develop | `Custom web application development` |
| mobile-app-development | `Native and cross-platform mobile app development` |
| webshop-development | `Webshop and eCommerce development` |
| migration (NL) | `Migratie naar een Nederlandse of Europese cloud` |
| migration (EN) | `Migration to a Dutch or European cloud` |
| contact-us | `Contact Manifera` |
| manifera-technologies | `Technologies we work with` |

---

### F3 (P0, S) - Duplicate pages, all indexable

**Evidence.** Word-sequence similarity of main content:

| Keep | Duplicate | Similarity | Note |
|---|---|---|---|
| `/contact-us/` | `/contact-us1/` (title "Manifera 05-Contact - Manifera Software Company") | **98%** | Old version left published |
| `/services/webshop-development/` | `/services/web-shops-ecommerce-development/` (last modified 2022) | **92%** | Same H1 text |
| `/about-us/setting-up-your-offshore-team/` | `/about-us/setting-up-your-team/` (H1 "Setting Up Your Offshore Development Team") | **97%** | Same H1 text |

All of them return 200, are self-canonical and are listed in `page-sitemap.xml`.

**Related cannibalisation** (different text, same search intent):

- `/remote/` (title `Remote - Manifera`, 17 chars, H1 about remote front-end developers) vs `/remote/frontend-developer/`.
- `/remote/developer/` vs `/remote/developer-unlock-excellence-with-manifera/`.

**Fix.**

1. Add 301s with the **Redirection** plugin, which is already active:
   ```
   /contact-us1/                                   -> /contact-us/                              301
   /services/web-shops-ecommerce-development/      -> /services/webshop-development/            301
   /about-us/setting-up-your-team/                 -> /about-us/setting-up-your-offshore-team/  301
   /remote/developer-unlock-excellence-with-manifera/ -> /remote/developer/                     301
   ```
2. Trash the source pages so they leave the sitemap.
3. Turn `/remote/` into a hub ("Remote developers and teams from Vietnam") that links to `/remote/developer/`, `/remote/frontend-developer/` and `/remote/team/`. Give it a proper title, for example `Remote Developers and Teams from Vietnam | Manifera` (50).

---

### F4 (P0, S) - Numbered internal labels in titles and H1s

| URL | Current title | Current H1 | Proposed title (≤ 60) |
|---|---|---|---|
| `/blog/` | `Checking out new 04-Blog Posts here - Manifera Software Company` | Our insightful blog | `Software Development Blog: Guides for CTOs \| Manifera` |
| `/portfolio/` | `Our partners and clients - 02-Portfolio page - Manifera clients` | Some of our successful projects | `Portfolio: Software Projects We Delivered \| Manifera` |
| `/privacy-policy/` | `06-Privacy Policy - Manifera Offshore Software Development Service` | **06-Privacy Policy** | `Privacy Policy \| Manifera` (H1 `Privacy Policy`) |
| `/terms-of-service/` | `07-Terms of Service - Manifera Offshore Custom Software Development Service` | **07-Terms of Service** | `Terms of Service \| Manifera` (H1 `Terms of Service`) |
| `/about-us/careers/job-application/` | `Apply Jobs - Manifera` | Job Application | add a meta description; consider `noindex` |
| `/about-us/` | `About Our Company - Manifera Offshore Custom Software Service` | **Who we are?** | `About Manifera: Dutch-Managed Software Teams Since 2014` (H1 `About Manifera`) |

The numbers look like page-ordering prefixes that were typed into the WordPress page title. Rename the page titles in WP admin, and set the SEO titles in Yoast.

---

### F5 (P0, M) - Wrong schema on posts; empty `sameAs` on the organisation

**Evidence.**

- The site runs **Schema & Structured Data for WP & AMP** (v1.69). Yoast's own schema graph is not output, and the homepage has a single JSON-LD block from that plugin.
- **Posts:** `BreadcrumbList`, `ProfessionalService`, `ImageObject`. Every post is declared to be "a ProfessionalService named Manifera". There is no `Article`/`BlogPosting`, no `author` Person, and no `datePublished`/`dateModified` in the schema. The dates exist only in the `article:published_time` meta.
- **Homepage `Corporation`:** `name`, `url`, `logo`, `contactPoint` (+31619701001, sales). `sameAs: []` is empty. It has no `address`, `foundingDate`, `founder`, `numberOfEmployees` or `areaServed`.
- **`/about-us/` and `/contact-us/`:** carry a separate `Organization` node.
- **FAQPage** exists only on the 5 `/remote/` pages. The new posts have FAQ sections in plain HTML without markup.

**Why it matters.**

- Google uses `Article` + `author` + dates for article understanding and Top Stories/Discover eligibility.
- LLMs use them to judge freshness and authorship.
- Calling every post a `ProfessionalService` is semantically wrong and duplicates the entity 347 times.
- An empty `sameAs` throws away Manifera's real asset: its third-party profiles.

**Fix (in SASWP, Structured Data → Schema Types).**

1. Edit the schema type targeting "Post Type = post": change `ProfessionalService` to **BlogPosting**. Map:
   - `headline` = post title
   - `author` = post author (Person)
   - `datePublished` / `dateModified`
   - `image` = featured image
   - `publisher` = the organisation
2. Restrict `ProfessionalService` (or `LocalBusiness`) to `/contact-us/` and the homepage only.
3. In SASWP → Settings → Knowledge Graph:
   - Set Organization type (`Organization` or `Corporation`) and the logo (min 112×112, square preferred).
   - Add `sameAs` with the real profiles: Facebook (`https://www.facebook.com/manifera`), LinkedIn company page, GoodFirms (`https://www.goodfirms.co/company/manifera`), ITviec (`https://itviec.com/companies/manifera-software-development`), FeaturedCustomers (`https://www.featuredcustomers.com/vendor/manifera`), YouTube channel, and Clutch if the profile exists.
   - Add the address (Herengracht 420, Amsterdam, NL, per `manifera_info.md`), `foundingDate` 2014, and founder Herre Roelevink with his LinkedIn.
4. Enable SASWP's FAQ schema for posts, or add FAQPage on posts with a visible FAQ. Google shows FAQ rich results only for government/health sites since 2023, so this is for LLM extraction and Bing.
5. Validate 3 posts in Google's Rich Results Test.

Alternative: disable SASWP and let Yoast output the graph (Yoast → Settings → Site representation). Choose one; never run both.

---

### F6 (P1, S) - New-post titles and descriptions get truncated

**Evidence.** The 8 newest posts have titles of 78-107 chars and meta descriptions of 150-233 chars. Google shows about 60 chars of title and 155 of description. Some titles lead with a hook rather than the keyword:

| Post (slug) | Title chars | Desc chars | Proposed SEO title (≤ 60, keyword first) |
|---|---|---|---|
| `cheapest-software-development-quote-risk` | 107 | 201 | `Cheapest Software Development Quote: The Hidden Risk` (52) |
| `custom-software-development-cost-breakdown` | 95 | 199 | `Custom Software Development Cost Breakdown (2026)` (49) |
| `mobile-app-development-cost-2026` | 98 | 178 | `Mobile App Development Cost 2026: The Full Breakdown` (52) |
| `evaluate-custom-software-development-company` | 85 | 150 | `How to Evaluate a Custom Software Development Company` (53) |
| `offshore-web-development-company` | 91 | 227 | `Offshore Web Development Company: 3 Warning Signs` (49) |
| `mobile-app-and-web-development-company` | 94 | 233 | `Mobile and Web App Development With React Native Web` (52) |
| `full-stack-web-application` | 89 | 208 | `Full Stack Web Application Scaling: 3 DB Bottlenecks` (52) |
| `ai-software-development-vendors-comparison` | 78 | 151 | `AI Software Development Vendors: Track Records Compared` (55) |

**Fix.**

- Keep the long, editorial H1. Put the short version in Yoast's **SEO title** field and trim meta descriptions to ≤ 155.
- Add this as a rule in the article upload workflow, so every new post gets an SEO title ≤ 60 and a meta description ≤ 155.

**Yoast focus keyphrases:** 3 of the 40 recent posts use the bare phrase `Software Development` and 2 use `Mobile App Development`. Those posts compete with each other and with the service pages. Give each post a distinct long-tail keyphrase, and leave the head terms to the service pages.

---

### F7 (P1, M) - About 600 thin archive URLs in the index; robots/sitemap conflict

**Evidence.**

| Taxonomy | URLs in sitemap | Problem |
|---|---|---|
| Tags | 357 in sitemap; 457 tags exist, **263 with 1 post, 100 with 0** | Indexable (`index, follow`), no unique text |
| Technology (`/technology/…`) | 51 | About 115 words each, no meta description (sample `/technology/android/`) |
| Testimonial categories | 13 | Thin |
| Portfolio / job categories | 4 + 4 | Thin |
| Categories | 8 | **Blocked by `Disallow: /category/` in robots.txt, but submitted in `category-sitemap.xml`** |

**Fix.**

1. Yoast → Settings → Taxonomies:
   - Tags = not in search results.
   - Testimonial categories, portfolio categories and job categories = not in search results.
2. Technology pages:
   - Either enrich the 10-15 that match services (React, .NET, Node.js, Flutter, Laravel...) to 400+ words, with a meta description and links to projects.
   - Or set the whole type to noindex.
3. Categories:
   - Decide. Either remove `Disallow: /category/` (recommended: categories are useful hubs, so add a 150-300 word intro per category), or keep the block and drop categories from the sitemap.
   - Never block and submit at the same time.
4. Stop auto-creating one tag per article in the upload workflow.

---

### F8 (P1, M) - Old, dated content still indexed and listed first in llms.txt

**Evidence.**

- At least 13 posts in `llms.txt` carry a year from 2017-2022 in the title:
  - `4 Best eCommerce platforms to choose in 2020`
  - `B2B vs. B2C E-Commerce: Trends & Insights for 2020`
  - `Comparison between B2B and B2C eCommerce and Trends for 2020`
  - `[Web development languages 2022] ...`
  - `Fireside Chat Event in Singapore on 8 July 2019`
  - `Manifera trip in Nha Trang 2017`
  - `Thank You To Everyone Who Joined Us At Our Christmas 2018 Event!`
  - etc.
- `llms.txt` is alphabetical, so `.Net Core: Things You Need To Know (2021)` and the 2020 posts are what an LLM reads first.

**Fix.**

| Type | Action |
|---|---|
| Two near-identical 2020 B2B/B2C posts | Merge into one updated 2026 post; 301 the other |
| "Best X in 2020/2022" posts with search demand | Update content and title to 2026, keep URL |
| Company trips, Christmas events, 2018-2020 events | Keep for culture, set `noindex`, or move to a "Life at Manifera" page |
| Everything else older than 2023 | Review in GSC: no clicks in 12 months and no backlinks → noindex or consolidate |

---

### F9 (P1, S) - GEO: llms.txt without a company summary

**Evidence.**

- The file is generated by the **LLMS Full TXT Generator** plugin (2.1.2).
- Its header is only the WordPress tagline ("Offshore Software Development Team - Custom Software Development") and `Contact: vu@manifera.com`, followed by 300+ alphabetical post links.
- `llms-full.txt` is 3.0 MB.

**Fix.** Add a curated header, or a static `llms.txt` with the generated full file kept. Use only facts the site already publishes, and a role inbox instead of a personal address.

```markdown
# Manifera

> Manifera is a Dutch-managed software development company founded in 2014 by Herre Roelevink. Headquarters in Amsterdam (Herengracht 420), engineering centre in Ho Chi Minh City, Vietnam, office in Singapore. We build custom web, mobile and cloud software and provide dedicated offshore development teams for European companies.

## Services
- [Offshore software development teams](https://www.manifera.com/services/offshore-software-development/)
- [Custom software development](https://www.manifera.com/services/custom-software-development/)
- [Web app development](https://www.manifera.com/services/web-app-develop/)
- [Mobile app development](https://www.manifera.com/services/mobile-app-development/)
- [Migration to a Dutch/European cloud](https://www.manifera.com/services/migration-to-nl-euro-cloud-en/)
- [Remote developers](https://www.manifera.com/remote/)
- [AI prototype to production: LaunchStudio](https://launchstudio.eu/en/)

## Company
- [About](https://www.manifera.com/about-us/) · [Way of working](https://www.manifera.com/about-us/our-way-of-working/) · [Portfolio](https://www.manifera.com/portfolio/) · [Contact](https://www.manifera.com/contact-us/)

## Cornerstone guides (2026)
- (10-15 newest buyer guides: cost, vendor evaluation, offshore teams, AI vendors)
```

Then sort the post list newest first, or by cluster, if the plugin allows it. Update the plugin to 2.1.3.

---

### F10 (P1, M) - GEO: inconsistent entity facts and missing corroboration

**Evidence.**

- **Location is inconsistent across sources:**
  - The `/about-us/` meta description says "based in Singapore and Ho Chi Minh City".
  - The `Corporation` schema has no address.
  - `manifera_info.md` defines Amsterdam (Herengracht 420) as the European HQ.
  - The Dutch KVK register lists *Manifera Software Development* with KVK 83156135, an Amsterdam registered office and a 2021 registration date ([liza.nl](https://www.liza.nl/en/83156135/manifera-software-development)).
  - Job boards say either "Singapore and HCMC" ([ITviec](https://itviec.com/companies/manifera-software-development)) or "Vietnam, Singapore and the Netherlands".
- **Third-party profiles found on 19 Nov:**
  - [GoodFirms](https://www.goodfirms.co/company/manifera)
  - [ITviec](https://itviec.com/companies/manifera-software-development)
  - [TopDev](https://topdev.vn/companies/manifera-software-development-79865)
  - [VietnamWorks](https://www.vietnamworks.com/nha-tuyen-dung/manifera-software-development-c182942)
  - [FeaturedCustomers](https://www.featuredcustomers.com/vendor/manifera)
  - [ADB DutchCham Singapore member list](https://adb-dutchcham.sg/members-directories/corporate-members/page/4)
  - **No Clutch profile surfaced in search.** The July audit listed one, so check whether it still exists and is linked.
- **manifera.com links to LaunchStudio from 0 of 36 pages crawled.** LaunchStudio links back in its footer and articles.

**Why it matters.** Answer engines cross-check a company's facts across its site, its schema and directories. When they disagree, assistants hedge or leave the company out. Founding year, HQ city, team size and services should read the same everywhere.

**Fix.**

1. Write one canonical "entity sheet" and apply it to the About page, `Corporation` schema, llms.txt, LinkedIn, GoodFirms, Clutch, ITviec and the Google Business Profile. It should contain:
   - legal name(s)
   - founding year (2014)
   - founder
   - HQ (Amsterdam) plus engineering centre (HCMC) plus Singapore
   - headcount range
   - 5 core services
   - 3 flagship clients/projects that may be named
2. Rewrite the `/about-us/` meta description to include Amsterdam.
3. Claim or refresh the Clutch profile and ask 3-5 clients for reviews. Clutch is the directory LLMs cite most for "best offshore development company" lists.
4. Add a LaunchStudio mention and link on `/services/` and `/about-us/`, for example "Built an app with AI tools? Our LaunchStudio service takes it to production". Also add `subOrganization` → LaunchStudio in the schema. This strengthens both entities.

---

### F11 (P1, S) - Dutch page on an English site, and screenshot filenames as alt text

**Evidence.**

- `/services/migration-to-nl-euro-cloud/` is written in Dutch ("Migratie naar Nederlandse/Europese Cloud"), but:
  - its title is English
  - the page declares `lang="en-US"`
  - there is no hreflang to its English twin `/services/migration-to-nl-euro-cloud-en/`
- Both pages use alt texts such as `Screenshot from 2025-05-14 10-59-54` and contain 2 inline base64 images.

**Fix.**

1. On the Dutch page:
   - set `lang="nl-NL"`, for example with a per-page language field in the template
   - Dutch title: `Migratie naar Nederlandse of Europese cloud | Manifera`
   - add reciprocal `<link rel="alternate" hreflang="nl">` / `hreflang="en"` between the two pages
2. Make the EN slug cleaner if you can: `/services/cloud-migration-netherlands-eu/` with a 301.
3. Replace the alt texts with descriptions of what each screenshot shows.

---

### F12 (P1, S) - Social images and image alt text

**Evidence.**

- `og:image` = the 225×225 logo on the homepage, `/blog/`, `/portfolio/`, `/services/`, `/remote/*`, `/privacy-policy/` and others.
- Other templates use a background image (`section9-bg.webp`) or an **icon** (`arrow-right-alt.svg` on `/services/offshore-software-development/`) as the share image.
- Empty `alt` counts: homepage 12 of 43; `/services/web-app-develop/` 34 of 55; `/services/mobile-app-development/` 16 of 35; `/remote/developer-unlock-excellence-with-manifera/` 14 of 30; `/services/webshop-development/` 12 of 33.

**Fix.**

- Create a 1200×630 default share image (logo + "Software development teams, Amsterdam & Vietnam") and set it in Yoast → Settings → Site basics.
- Create one per service page.
- Logos and badges get `alt="<Client> logo"` or `alt="<Award name> badge"`. Decorative shapes keep `alt=""`.

---

### F13 (P2, M) - Performance, robots.txt and housekeeping

| Item | Evidence | Fix |
|---|---|---|
| TTFB | 0.68-1.27 s (homepage 1.27 s, `/portfolio/` 1.20 s) | Page cache + CDN; target < 0.3 s |
| Page weight | Homepage 211 KB HTML, 37 `<script>`, 12 stylesheets; service pages 164-246 KB HTML | Audit Visual Composer + Smart Slider output on templates that don't need them; defer non-critical JS |
| Core Web Vitals | Not measured (PSI quota) | Run PageSpeed Insights on `/`, 3 service pages, 1 post; record here |
| robots.txt | Still disallows `/nl/how-to-choose-a-custom-software-company/` (301) and `/nl/in-house-vs-outsourcing-software-development-2/` (404) | Remove both lines; resolve `/category/` (F7) |
| `/favicon.ico` | 404 | Upload root favicon.ico |
| PHP | 8.2.35; Contact Form 7 6.2.5 needs 8.3 | Plan the PHP 8.3 upgrade (security updates for the main form plugin are blocked) |
| Plugins behind | Yoast 28.8 → 28.9, SASWP 1.69 → 1.70, ACF, UpdraftPlus, WP Mail SMTP, Easy MCP AI 2.3.2 → 2.4.1 | Update after backup |
| Job application page | No meta description, thin (197 words) | `noindex` |

---

## 4. Yoast content scores (40 most recently modified posts)

- **SEO score:** 23 good, 17 OK, 0 bad.
- **Weak spots:**
  - The generic keyphrases in F6 (`Software Development` ×3, `Mobile App Development` ×2, `Outsourcing`, `development software`).
  - The keyphrase is often not at the start of the SEO title, because the SEO title equals the long H1.

---

## 5. KPIs and measurement

| KPI | Baseline (19 Nov) | Target by 28 Feb 2027 | Where |
|---|---|---|---|
| Pages with exactly 1 non-empty H1 (page-sitemap) | 18 / 28 | 28 / 28 | crawl |
| Indexable duplicate pages | 4 | 0 | `page-sitemap.xml` |
| Titles with numbered prefixes | 5 | 0 | crawl |
| Posts with `BlogPosting` + author + dates in schema | 0 / 347 | 347 / 347 | Rich Results Test on 3 samples |
| `sameAs` entries in organisation schema | 0 | ≥ 6 | homepage JSON-LD |
| Indexable thin archives (tags, technology, testimonial cats) | about 430 | under 30 | sitemaps |
| manifera.com pages linking to launchstudio.eu | 0 | ≥ 3 (services, about, footer) | crawl |
| AI referral sessions (chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com, claude.ai) | measure now | +100% vs Dec | GA4, session source regex `chatgpt\|perplexity\|gemini\|copilot\|claude` |
| Brand answer accuracy (prompt test) | measure now | ≥ 7 / 10 correct | monthly manual test |
| GSC clicks on `/services/*` | measure now | +30% | Search Console |

**Monthly GEO prompt test.** Run each prompt in ChatGPT, Perplexity and Gemini. Record whether Manifera is named, and whether its location, founding year and services are described correctly.

1. What is Manifera (manifera.com)?
2. Best offshore software development companies in Vietnam for Dutch companies
3. Dutch-managed software development team in Vietnam
4. How much does a dedicated development team in Vietnam cost?
5. Software development company Amsterdam with offshore team
6. Who founded Manifera and where is it based?
7. Alternatives to hiring in-house developers in the Netherlands
8. Custom software development company for European SMEs with fixed teams
9. Migrate my application to a Dutch or European cloud provider
10. Manifera reviews

---

## 6. Action plan

| When | Action | Finding | Owner | Effort |
|---|---|---|---|---|
| Week of 19 Nov | Homepage H1 + H2 structure | F1 | Dev | S |
| Week of 19 Nov | Fix empty H1 in service template | F2 | Dev | S |
| Week of 19 Nov | 4 redirects, trash duplicates | F3 | Content | S |
| Week of 19 Nov | Rename numbered titles/H1s | F4 | Content | S |
| Week of 24 Nov | SASWP: BlogPosting on posts, sameAs, address, founder | F5 | Dev | M |
| Week of 24 Nov | SEO titles ≤ 60 / descriptions ≤ 155 for 8 newest posts; add the rule to the upload workflow | F6 | Content | S |
| Week of 24 Nov | Noindex tags and thin taxonomies; resolve the `/category/` conflict | F7 | Content | S |
| Week of 1 Dec | Curated llms.txt header | F9 | Content | S |
| Week of 1 Dec | Entity sheet; About meta; Manifera → LaunchStudio links | F10 | Marketing | M |
| Week of 1 Dec | Dutch cloud page lang/hreflang, alt texts | F11 | Dev | S |
| December | Share images, alt texts on service pages | F12 | Design/content | M |
| December | Old-post review: merge, update, noindex | F8 | Content | L |
| December | Claim/refresh Clutch; client reviews | F10 | Marketing | L |
| Jan 2027 | PHP 8.3, cache/CDN, PageSpeed baseline | F13 | Server admin | M |
| Monthly | GEO prompt test + KPI table update | 5 | Marketing | S |

---

## Appendix A - Raw data

**Infrastructure**

- IP 136.243.57.57 (shared with launchstudio.eu); DNS at DigitalOcean.
- HTTP/1.1 with h3 advertised; HSTS preload.
- WordPress 7.1.4, PHP 8.2.35, theme `manifera3`.
- 24 active plugins, including Yoast 28.8, Schema & Structured Data for WP 1.69, Visual Composer, Smart Slider 3, Redirection, Wordfence, Site Kit and LLMS Full TXT Generator.

**AI crawler access (all 200):**

- OpenAI: GPTBot, OAI-SearchBot, ChatGPT-User
- Anthropic: ClaudeBot, Claude-User, Claude-SearchBot, anthropic-ai
- Perplexity: PerplexityBot, Perplexity-User
- Google: Google-Extended, Googlebot
- Others: bingbot, Applebot(-Extended), CCBot, meta-externalagent, Amazonbot, Bytespider, cohere-ai, DuckAssistBot, MistralAI-User

**Sitemaps (19 Nov)**

| Sitemap | URLs | Last modified |
|---|---|---|
| post | 347 | 2026-11-18 |
| page | 28 | 2026-10-07 |
| dt_portfolio | 27 | 2026-06-08 |
| dt_job | 2 | 2026-10-12 |
| dt_testimonial | 13 | 2026-06-02 |
| dt_technology | 51 | 2025-02-10 |
| category | 8 | 2026-11-18 (blocked in robots.txt) |
| post_tag | 357 | 2026-11-18 |
| dt_portfolio_category | 4 | 2026-06-08 |
| dt_job_category | 4 | 2026-10-12 |
| dt_testimonial_category | 13 | 2026-06-02 |
| author | 3 | 2026-05-07 |

**Post lastmod by month:** Jan 1, May 86, Jun 83, Jul 33, Aug 28, Sep 24, Oct 17, Nov 24. Post status: 347 published, 3 private.

**Page-sitemap on-page summary**

| URL | Title chars | H1 | H2 | Words | Schema (main types) |
|---|---|---|---|---|---|
| `/` | 59 | Experiences of our clients working with us | 1 | 1,516 | Corporation, WebSite, VideoObject |
| `/about-us/` | 61 | Who we are? | 5 | 754 | AboutPage, Organization |
| `/about-us/careers/` | 75 | 3 H1s (Join us; Your future - Our values; Our efficient recruitment process) | 2 | 413 | Breadcrumb |
| `/about-us/our-way-of-working/` | 69 | Our Way Of Working | 4 | 1,396 | Breadcrumb |
| `/services/` | 58 | Our software development services | 5 | 470 | Breadcrumb |
| `/services/custom-software-development/` | 61 | Custom-made software development services | 3 | 710 | Breadcrumb |
| `/services/offshore-software-development/` | 46 | (empty) | 5 | 873 | Breadcrumb |
| `/services/web-app-develop/` | 30 | (empty) | 4 | 856 | Breadcrumb |
| `/services/mobile-app-development/` | 33 | (empty) | 4 | 784 | VideoObject |
| `/remote/` | 17 | Elevate with Manifera's Skilled Remote Front-End Developers | 10 | 1,620 | FAQPage |
| `/portfolio/` | 63 | Some of our successful projects | 0 | 957 | Breadcrumb |
| `/contact-us/` | 21 | (empty) | 1 | 722 | ContactPage, Organization |

`/about-us/careers/` has 3 H1s. Keep one ("Careers at Manifera") and make the others H2.

**Crawler test command used:** `curl -s -o /dev/null -w '%{http_code}' -A "Mozilla/5.0 (compatible; <UA>)" <url>`
