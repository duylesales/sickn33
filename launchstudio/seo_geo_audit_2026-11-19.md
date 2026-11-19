# LaunchStudio (launchstudio.eu) - SEO & GEO Audit, 19 November 2026

**Supersedes:** `seo_geo_audit_2026-07-31.md` (kept for history; section 2 tracks every finding from that audit)
**Scope:** technical SEO, on-page, structured data, content and topical authority, international (NL/EN), GEO (visibility in ChatGPT, Perplexity, Claude, Gemini and Google AI Overviews)
**Method:**

- Raw HTTP crawl (`curl`) of `robots.txt`, `sitemap_index.xml` plus all 5 sub-sitemaps, `llms.txt` and `llms-full.txt`.
- All 21 URLs in `page-sitemap.xml` and the 8 newest posts, parsed for title, meta, canonical, hreflang, OG, headings, images, JSON-LD and word count.
- The head of all 320 post URLs, checked for hreflang, duplicate title/description and OG tags.
- Access checks with 25 crawler user-agents.
- Text similarity between suspect page pairs.
- WordPress admin data via MCP: plugins, post counts, Yoast scores for the 40 most recently modified posts.
- Web search for third-party brand mentions.

**Limitations:**

- No Search Console or GA4 data was used.
- The PageSpeed Insights API had hit its daily quota, so there are no Core Web Vitals. Performance below uses TTFB, HTML weight and asset counts as proxies.
- The crawl sees raw HTML, not a JS-rendered DOM.

---

## 1. Executive summary

LaunchStudio has done a lot of content work since July:

- Published posts went from 71 to 160 NL/EN pairs (318 published).
- Article bodies are now 2,300-2,800 words.
- Bylines use a real name.
- `llms.txt` now lists every post.
- A Manifera link appears in the footer.

Most of the July technical and entity findings are still open, though. This crawl also found one new problem that outweighs everything else:

1. **🔴 The server blocks ChatGPT and Claude (new, critical).** `launchstudio.eu` returns **HTTP 403** to `GPTBot`, `ChatGPT-User`, `ClaudeBot`, `anthropic-ai`, `CCBot`, `Bytespider` and `cohere-ai`. That includes `robots.txt` and `llms.txt`. `robots.txt` itself allows everything, so the block sits in a server/WAF layer.
   - Manifera runs on the same server (136.243.57.57) and is **not** blocked.
   - When a ChatGPT user asks ChatGPT to open or read a LaunchStudio page, it fails today.
   - This undermines the whole GEO strategy and the planned ChatGPT Ads test (`chatgpt_ads_plan_launchstudio.md`).
2. **🔴 Every page has two `<title>` tags and, on 318 of 320 posts, two meta descriptions (still open from July).** A hardcoded block in the theme header duplicates Yoast. On the homepage its `og:url` still points to the newest blog post.
3. **🔴 The money pages are weak in the SERP.**
   - The NL homepage title is `Launch Studio` (13 chars).
   - The EN homepage title is 131 chars.
   - All 10 service landing pages have an **empty meta description** and no `og:image`.
4. **🟠 Duplicate and broken pages are indexable:**
   - `/vibe-coding-nederland/` is 99% identical to `/ai-app-naar-productie/`.
   - `/en/vibe-coding/` is 99% identical to `/en/ai-app-into-production/`.
   - `/privacybeleid-1/` renders the whole Insights archive under a privacy title.
   - `/en/homepage/` is a 136-word stub titled "Homepage".
5. **🟠 There is no Organization/ProfessionalService, FAQPage or Offer schema (open from July).** The homepage `CollectionPage` has `"name": ""`.
6. **🟠 The brand entity is ambiguous off-site.** A search for `"launchstudio.eu"` returns other "Launch Studio" companies (a Czech design agency on Clutch, a UK agency, a Product Hunt course) and none for this site. No third-party profile for LaunchStudio was found.

**Verdict: 🟠 Strong content engine, weak technical/entity layer.** The top 5 fixes are mostly one-off theme, server and settings changes, about 1-2 developer days. They unlock value from 318 published articles that is currently capped.

### Scorecard

| Area | Status | vs. 31 Jul |
|---|---|---|
| Crawlability for Google/Bing | 🟢 Good | = |
| Crawlability for AI assistants | 🔴 Blocked for OpenAI/Anthropic training and user agents | ⬇ new |
| Indexation hygiene (duplicates, stubs, tags) | 🔴 Weak | ⬇ more pages |
| Titles and meta | 🔴 Duplicate tags site-wide, empty on landing pages | = |
| Structured data | 🟠 Article + Person ok, no entity/FAQ/Offer | ⬆ slight |
| Content depth | 🟢 2,300-2,800 words per post | ⬆⬆ |
| Content volume | 🟢 318 posts, 302 with NL/EN hreflang | ⬆⬆ |
| International (hreflang/slugs) | 🟠 18 unpaired NL posts, 9 NL posts with English "-2" slugs | ⬇ new regression |
| E-E-A-T and author | 🟠 Real name, empty profile | ⬆ |
| Off-site entity / brand | 🔴 No third-party profiles, name collision | = |
| llms.txt | 🟠 Full post list, no offer summary | ⬆ |
| Performance (proxy) | 🟡 TTFB 0.68 s, no cache headers | = |

---

## 2. Progress since the 31 July audit

| # | July finding | Status 19 Nov | Evidence |
|---|---|---|---|
| 1 | Duplicate hardcoded OG/meta block in theme | ❌ Open | 320/320 posts have 2 `<title>`, 318/320 have 2 meta descriptions, 319/320 have 2 `og:title` |
| 2 | Homepage title NL too short, EN 131 chars | ❌ Open | NL `Launch Studio` (13), EN 131 chars, unchanged |
| 3 | Stray `rel="next"` on homepage | ❌ Open | `<link rel="next" href="https://launchstudio.eu/page/2/">` still present |
| 4 | No Organization schema | ❌ Open | Homepage graph: `CollectionPage`, `BreadcrumbList`, `WebSite` only |
| 5 | No FAQPage schema | ❌ Open | No `FAQPage` on any page crawled |
| 6 | Author `phu.lt` | ✅ Fixed | Byline and `Person` = "Duy Le" (profile still empty, see F9) |
| 7 | No Offer/Service schema | ❌ Open | none |
| 8 | No hyperlink to manifera.com | ✅ Fixed | Footer logo links to `manifera.com/?utm_source=launchstudio&utm_medium=logo-footer`; new posts link to `/services/offshore-software-development/` |
| 9 | `llms.txt` lists 5 posts, no offer | 🟡 Partly | Now lists all posts (550 lines), still no offer, pricing or process summary |
| 10 | 71 of 362 articles live | ✅ Much better | 318 published, 2 drafts |
| 11 | Thin posts (250-350 words) | ✅ Fixed for new posts | Newest posts 2,275-2,685 words in article body |
| 12 | Inline base64 testimonial image, empty alt | ❌ Open | 1 base64 image with empty alt on NL and EN homepage |
| 13 | No page cache/CDN | ❌ Open | No `Cache-Control` on HTML, TTFB 0.68 s on every page |

---

## 3. Findings and fixes

Priority key: **P0** = fix this week, **P1** = this month, **P2** = backlog. Effort: S under 2 h, M under 1 day, L more than 1 day.

### F1 (P0, S) - AI assistants blocked with 403 at the server

**Evidence.** Same URL, different user-agent, 19 Nov 2026:

| User-agent token | Owner / purpose | launchstudio.eu | manifera.com |
|---|---|---|---|
| `GPTBot` | OpenAI training crawler | **403** | 200 |
| `ChatGPT-User` | ChatGPT fetching a page for a user | **403** | 200 |
| `OAI-SearchBot` | ChatGPT search index | 200 | 200 |
| `ClaudeBot` | Anthropic crawler | **403** | 200 |
| `anthropic-ai` | Anthropic (legacy token) | **403** | 200 |
| `Claude-User` / `Claude-SearchBot` | Claude user fetch / search | 200 | 200 |
| `CCBot` | Common Crawl (feeds many LLMs) | **403** | 200 |
| `Bytespider`, `cohere-ai` | ByteDance, Cohere | **403** | 200 |
| `PerplexityBot`, `Perplexity-User` | Perplexity | 200 | 200 |
| `Google-Extended`, `Googlebot`, `bingbot`, `Applebot` | Google, Bing, Apple | 200 | 200 |

Other details:

- The 403 also applies to `/robots.txt`, `/llms.txt` and the sitemap.
- The block page says `403 | Forbidden`, carries a `Request ID` and the client IP, and sends its own strict CSP. This is the signature of a WAF or "bad bot" user-agent blacklist in front of WordPress, not WordPress itself. No WordPress security plugin is active on LaunchStudio.
- Manifera, on the same IP, passes all the same user-agents, so the rule is per site (vhost).

**Why it matters.**

- `ChatGPT-User` is how ChatGPT reads a page when a user pastes a link or asks it to check a site. Today ChatGPT gets a 403 for LaunchStudio.
- `GPTBot`, `ClaudeBot` and `CCBot` decide whether LaunchStudio's 318 articles can inform future model answers at all.
- The site publishes `llms.txt` precisely to invite these crawlers, and then blocks them. Fixing this makes every other GEO action in this audit pay off.

**Fix.**

1. In the server/WAF config for `launchstudio.eu`, remove these user-agents from the blocklist or add an allow rule above it: `GPTBot`, `ChatGPT-User`, `OAI-SearchBot`, `ClaudeBot`, `Claude-User`, `Claude-SearchBot`, `anthropic-ai`, `PerplexityBot`, `Perplexity-User`, `CCBot`, `Google-Extended`, `Applebot-Extended`. Keep `Bytespider` blocked if you want; it brings no B2B value. Copy whatever Manifera's vhost does, since it already passes them.
2. Leave `robots.txt` as is. It already allows all. Optionally add explicit `User-agent: GPTBot` / `Allow: /` groups as documentation.
3. Verify with the test below. Expected result: `200` for each line.

```bash
for ua in GPTBot/1.1 ChatGPT-User/1.0 ClaudeBot/1.0 anthropic-ai CCBot/2.0; do
  printf "%-18s %s\n" $ua $(curl -s -o /dev/null -w '%{http_code}' -A "Mozilla/5.0 (compatible; $ua)" https://launchstudio.eu/en/)
done
```

**Owner:** server admin. **Do this before the ChatGPT Ads test starts on 24 Nov.**

---

### F2 (P0, S) - Duplicate `<title>`, meta description and OG block on every page

**Evidence.** The homepage `<head>` has a theme block (lines 11-26) and then Yoast (lines 32-44):

```html
<title>Launch Studio</title>                          <!-- theme -->
<meta name="description" content="LaunchStudio helps ...">    <!-- theme -->
<meta property="og:title" content="Launch Studio">            <!-- theme -->
<meta property="og:url" content="https://launchstudio.eu/app-development-cost-2026-three-year-total-cost-compared-2/"> <!-- theme: newest post, wrong -->
...
<!-- This site is optimized with the Yoast SEO plugin v27.6 -->
<title>Launch Studio</title>                          <!-- Yoast -->
<meta property="og:url" content="https://launchstudio.eu/" />  <!-- Yoast, correct -->
```

Across all 320 posts: 320 have 2 `<title>`, 318 have 2 `meta description`, and 319 have 2 `og:title`. On posts the theme description is a raw, cut-off excerpt.

**Why it matters.**

- Two titles and two descriptions is invalid HTML, and Google picks one unpredictably.
- LinkedIn, Facebook, Slack and WhatsApp read the **first** `og:url` and `og:title`. A shared homepage link therefore previews the newest blog post.
- LLM crawlers that read the head see conflicting summaries.

**Fix.** In `wp-content/themes/<launchstudio theme>/header.php`, delete the hardcoded `<title>`, `meta description`, `og:*` and `twitter:*` lines. Keep `wp_head()` and `add_theme_support('title-tag')`, so Yoast stays the only source of the title and meta. Test: `curl -s https://launchstudio.eu/ | grep -c '<title'` should return `1`.

---

### F3 (P0, S) - Homepage titles, landing-page meta descriptions and OG images

**Evidence.**

| URL | Title (chars) | Meta description | og:image |
|---|---|---|---|
| `/` | `Launch Studio` (13) | theme default (115) | none |
| `/en/` | 131-char title that repeats the tagline | theme default (115) | none |
| `/ai-app-naar-productie/`, `/en/ai-app-into-production/` | 37 / 38 | **empty** | none |
| `/ai-app-beveiliging/`, `/en/ai-app-security/` | 33 / 31 | **empty** | none |
| `/ai-app-integraties/`, `/en/ai-app-integrations/` | 34 / 35 | **empty** | none |
| `/ai-app-bouwen-vanaf-scratch/`, `/en/build-ai-app-from-scratch/` | 43 / 41 | **empty** | none |
| `/vibe-coding-nederlands/`, `/en/vibe-coding-netherlands/` | 38 / 39 | **empty** | none |

These 10 landing pages are the Google Ads and ChatGPT Ads destinations. Titles like `Ai App Security - Launch Studio` also use wrong casing ("Ai").

**Fix.** Set these in Yoast (SEO title + meta description + social image per page). The proposed copy uses only facts already on the site: €800-7,500 fixed price, 1-3 weeks, Lovable/Bolt/Cursor.

| Page | SEO title (≤ 60) | Meta description (≤ 155) |
|---|---|---|
| `/` | `AI-prototype live in 1-3 weken \| LaunchStudio` | `Gebouwd met Lovable, Bolt of Cursor? Wij maken je app launch-ready: beveiliging, betalingen, hosting en deployment. Vaste prijs €800-7.500.` |
| `/en/` | `Get Your AI-Built App Launch-Ready \| LaunchStudio` | `Built with Lovable, Bolt or Cursor? We make it launch-ready: security, payments, hosting and deployment. Fixed price €800-7,500, live in 1-3 weeks.` |
| `/ai-app-naar-productie/` | `AI-app naar productie in 1-3 weken \| LaunchStudio` | `Je AI-app werkt in de demo, maar is hij klaar voor echte gebruikers? Wij doen de 6 checks voor lancering. Vaste prijs vanaf €800.` |
| `/en/ai-app-into-production/` | `AI App Into Production in 1-3 Weeks \| LaunchStudio` | `Your AI app works in the demo. Is it ready for real users? We run the 6 launch checks and fix what fails. Fixed price from €800.` |
| `/ai-app-beveiliging/` | `AI-app beveiliging en security audit \| LaunchStudio` | `Publieke Supabase-keys, open databases, geen RLS? Wij controleren en repareren de beveiliging van je AI-gebouwde app voor lancering.` |
| `/en/ai-app-security/` | `AI App Security Audit and Fixes \| LaunchStudio` | `Public Supabase keys, open databases, missing RLS? We audit and fix the security of your AI-built app before launch. Fixed price.` |
| `/ai-app-integraties/` | `Betalingen en integraties voor AI-apps \| LaunchStudio` | `Mollie, Stripe, iDEAL en webhooks die echt werken. Wij koppelen betalingen en integraties aan je Lovable- of Bolt-app.` |
| `/en/ai-app-integrations/` | `Payments and Integrations for AI Apps \| LaunchStudio` | `Stripe, Mollie, iDEAL and webhooks that actually fire. We connect payments and integrations to your Lovable or Bolt app.` |
| `/ai-app-bouwen-vanaf-scratch/` | `AI-app laten bouwen vanaf nul \| LaunchStudio` | `Nog geen prototype? Wij bouwen je app van idee tot live product, met beveiliging, betalingen en hosting vanaf dag één.` |
| `/en/build-ai-app-from-scratch/` | `Build an AI App From Scratch \| LaunchStudio` | `No prototype yet? We build your app from idea to live product, with security, payments and hosting in place from day one.` |
| `/vibe-coding-nederlands/` | `Vibe coding app laten afmaken \| LaunchStudio` | `Je AI zei "Klaar." Dat was het niet. Wij maken je vibe-coded app af en klaar voor productie, met vaste prijs en duidelijke planning.` |
| `/en/vibe-coding-netherlands/` | `Finish Your Vibe-Coded App \| LaunchStudio` | `Your AI said "Done." It wasn't. We finish your vibe-coded app and get it production-ready, at a fixed price with a clear timeline.` |

Then:

- Design one 1200×630 social image per landing pair, plus a default one in Yoast → Settings → Site basics.
- Fix "Ai" to "AI" in the page titles.
- Remove `rel="next"` on the homepage. It means the front page is running the blog loop; set Settings → Reading to a static page, or drop the pagination link in the template.

---

### F4 (P0, S) - Duplicate, broken and stub pages in the index

**Evidence.** Word-sequence similarity, measured on the main content:

| URL A | URL B | Similarity | Issue |
|---|---|---|---|
| `/vibe-coding-nederland/` | `/ai-app-naar-productie/` | **99%** | Exact duplicate, competes with an ad landing page |
| `/en/vibe-coding/` | `/en/ai-app-into-production/` | **99%** | Exact duplicate |
| `/vibe-coding-nederland/` | `/vibe-coding-nederlands/` | 20% | Two URLs for one keyword ("vibe coding nederland(s)") |
| `/privacybeleid-1/` | `/inzichten/` | **100%** | Privacy URL renders the full Insights archive (514 KB, H1 "Inzichten") |
| `/en/homepage/` | `/en/` | n/a | 136-word stub, title and H1 "Homepage", no hreflang, in sitemap |

All of them return `200`, are `index, follow`, self-canonical and listed in `page-sitemap.xml`.

**Fix.** Use 301 redirects. There is no Redirection plugin on LaunchStudio, so either install `Redirection` or add the rules in the server config.

```
/vibe-coding-nederland/   -> /vibe-coding-nederlands/        301
/en/vibe-coding/          -> /en/vibe-coding-netherlands/    301
/privacybeleid-1/         -> /privacybeleid/                 301
/en/homepage/             -> /en/                            301
```

Then delete or trash the 4 source pages so they leave the sitemap. Of these, only `/ai-app-naar-productie/`, `/en/ai-app-into-production/` and `/vibe-coding-nederlands/` appear in the ads docs. None of the redirected URLs are referenced as ad destinations in this project.

---

### F5 (P1, M) - No entity schema: Organization / ProfessionalService, FAQPage, Offer

**Evidence.**

- Homepage graph: `CollectionPage` (with `"name": ""`), `BreadcrumbList`, `WebSite`.
- Landing pages: `WebPage` only.
- Posts: `Article`, `WebPage`, `Person`, with no `publisher` organization.
- The homepage has the price calculator and the FAQ ("Wat kost jouw project?") in plain HTML, with no markup.

**Why it matters.** Answer engines ground "who is LaunchStudio, what does it cost, where is it" on structured entity data. With the name collision in F11, an explicit entity graph with `sameAs` and `parentOrganization: Manifera` is the main way to tell machines which "Launch Studio" this is.

Google shows FAQ rich results only for government and health sites since 2023. So FAQPage is for LLM extraction and Bing, not for SERP stars.

**Fix.**

1. Yoast → Settings → Site representation:
   - Organization, name `LaunchStudio`, logo 512×512.
   - Add the social profiles created in F11.
   - Set the homepage title separator.

   This makes Yoast output an `Organization` node and use it as `publisher` on all Articles.
2. Add this block site-wide, for example in a small mu-plugin or the theme `footer.php`. The addresses are from `launchstudio_info.md` §1.3; fill `sameAs` when the profiles exist.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "@id": "https://launchstudio.eu/#organization",
  "name": "LaunchStudio",
  "alternateName": ["Launch Studio", "LaunchStudio by Manifera"],
  "url": "https://launchstudio.eu/",
  "logo": "https://launchstudio.eu/wp-content/uploads/<logo-512.png>",
  "description": "LaunchStudio takes apps built with AI tools such as Lovable, Bolt and Cursor to production: security, payments, hosting and deployment, at a fixed price of €800-7,500 in 1-3 weeks.",
  "priceRange": "€800-€7,500",
  "areaServed": ["NL", "BE", "DE", "EU"],
  "knowsAbout": ["Lovable", "Bolt", "Cursor", "Replit", "Supabase", "Stripe", "Mollie", "iDEAL", "AI app security", "vibe coding"],
  "parentOrganization": {
    "@type": "Organization",
    "@id": "https://www.manifera.com/#Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com/"
  },
  "founder": {"@type": "Person", "name": "Herre Roelevink", "sameAs": "https://www.linkedin.com/in/herre-roelevink-director-manifera/"},
  "address": [
    {"@type": "PostalAddress", "streetAddress": "Herengracht 420", "postalCode": "1017 BZ", "addressLocality": "Amsterdam", "addressCountry": "NL"},
    {"@type": "PostalAddress", "streetAddress": "100 Tras Street #16-01", "postalCode": "079027", "addressLocality": "Singapore", "addressCountry": "SG"},
    {"@type": "PostalAddress", "streetAddress": "Floor 11, Block C, 10 Pho Quang Street", "addressLocality": "Ho Chi Minh City", "addressCountry": "VN"}
  ],
  "sameAs": []
}
</script>
```

3. Add `FAQPage` on the homepage (NL and EN), with the visible FAQ questions verbatim. Also add it on each landing page that has a FAQ block.
4. Add an `OfferCatalog` with the two packages (Launch Ready, Launch & Grow). Use the exact prices displayed on the page, so markup and visible text match.
5. Fix the empty `CollectionPage.name`. This goes away once the homepage is a static page with a Yoast title (F3).
6. Validate with Google's Rich Results Test and validator.schema.org.

---

### F6 (P1, S) - Posts: English slugs with "-2" on NL versions (workflow regression)

**Evidence.** 9 NL posts use an English slug with a `-2` suffix, because the EN version took the slug first. **The 3 newest NL posts (Nov 2026) all have it**, so the upload workflow is producing it now.

```
/app-development-cost-2026-three-year-total-cost-compared-2/
/github-copilot-agent-code-review-production-checks-for-agent-pull-requests-2/
/bolt-cloud-or-your-own-backend-taking-a-bolt-app-to-production-2/
/lovable-hosting-environment-variables-across-three-environments-2/
/supabase-data-processing-agreement-what-dutch-founders-need-2/
/mollie-integration-for-ai-built-apps-step-by-step-2/
/ai-gegenereerde-data-naar-notion-pushen-via-api-ai-software-engineering-best-practices-2/
/bolt-ai-alkmaar-2/
/waarom-90-van-ai-prototypes-nooit-live-gaat-2/
```

**Why it matters.**

- Dutch searchers and LLMs see an English URL on a Dutch page, which weakens the NL keyword in the URL.
- The `-2` suffix looks like a duplicate.
- Example: NL title "Kosten van App-Ontwikkeling in 2026", but the URL is `app-development-cost-2026-...-2`.

**Fix.**

1. In the upload script, set the NL `slug` explicitly from the NL title, for example `kosten-app-ontwikkeling-2026-totaal-drie-jaar`. Polylang allows the same slug in two languages only with the "share slugs" option (Pro), so a translated slug is the clean way.
2. For the 9 existing posts:
   - Change the slug.
   - Add a 301 from the old URL.
   - Update `social_link_map.tsv` and any social posts that link to the old URL.

---

### F7 (P1, S) - 18 NL posts without an EN counterpart (no hreflang)

**Evidence.** 302 of 320 post URLs carry `hreflang nl + en + x-default`. 18 NL-only posts have none, mostly from the March 2026 batch:

- `wat-kost-het-om-je-prototype-live-te-krijgen`
- `bureau-vs-freelancer-vs-launchstudio`
- `wie-zitten-er-achter-launchstudio`
- `kan-mijn-lovable-code-echt-in-productie`
- `hoe-wij-werken-van-intake-tot-oplevering-in-5-stappen`
- 13 more (full list in the appendix).

**Fix.** Several of these are decision-stage pages (price, who we are, how we work, agency vs freelancer) that EN buyers and LLMs also ask about. Translate the top 6 and link them as Polylang translations.

---

### F8 (P1, M) - Thin, indexable tag archives

**Evidence.**

- 445 tags: **292 have 1 post, 75 have 0 posts**.
- All tag archives are `index, follow` and listed in `post_tag-sitemap.xml` (370 URLs).
- Sample `/en/tag/ai-app/` is an archive with no unique text.

**Why it matters.** About 370 near-empty URLs dilute crawl budget and site quality signals, at roughly 1 tag page per article.

**Fix.**

1. Yoast → Settings → Tags → "Show tags in search results" = **Off**. This sets noindex and removes them from the sitemap.
2. Keep categories indexable (14 URLs) and give each category a 150-300 word intro.
3. Stop creating a new tag per article in the upload script. Reuse a fixed list of about 30 tags.

---

### F9 (P1, S) - Author entity is a name without a profile

**Evidence.**

- `Person` = "Duy Le", Gravatar placeholder image, `url` `/en/author/duy-le/`.
- No `jobTitle`, `description` or `sameAs`.
- The author archive has no bio.

**Fix.**

1. In WordPress → Users, add a bio (2-3 sentences: role at LaunchStudio/Manifera and what the author reviews), a real photo, and a LinkedIn URL.
2. Yoast reads the "Website" and social fields into `sameAs`.
3. For technical posts, consider a named reviewer line ("Technically reviewed by …, Manifera engineering") if that is true. Do not invent reviewers.

---

### F10 (P1, S) - Insights archives are heavy and inaccessible

**Evidence.**

| Page | HTML size | Images | Empty alt | H2 count |
|---|---|---|---|---|
| `/inzichten/` | 513 KB | 169 | 168 | 0 |
| `/en/insights/` | 460 KB | 151 | 150 | 0 |

Both have a TTFB of about 1.0 s, versus 0.68 s elsewhere. The EN title is `Blogs - Launch Studio`.

**Fix.**

- Paginate to 12-24 posts per page.
- Use the post title as `alt` for thumbnails, or `alt=""` with the title in a linked heading. Each card should have an `<h2>`/`<h3>` title.
- Add a 100-word intro per archive and group posts by category (Security, Payments, Hosting, Tools).
- Title: `Insights: AI App Security, Payments and Launch Guides | LaunchStudio`, or a shorter version (≤ 60).

---

### F11 (P1, L) - GEO: brand entity collision and no third-party footprint

**Evidence.**

- A web search for `"launchstudio.eu"` (19 Nov) returns:
  - [Launch Studio on Clutch](https://clutch.co/profile/launch-studio), a Czech design agency founded in 2025
  - [a UK agency](https://launch-studio-ltd.squarespace.com/services)
  - [a crowdfunding course on Product Hunt](https://www.producthunt.com/products/launch-studio)
  - [an NFT tool](https://saasbrowser.com/saas/966783/launch-studio)
- The search returned no page about this LaunchStudio and found no review profile, directory listing or press mention.
- On-site, the name is spelled both "Launch Studio" (site name, titles, WebSite schema) and "LaunchStudio" (copy, llms.txt intro).

**Why it matters.**

- LLMs answer "who is LaunchStudio" from the web's consensus, and right now that consensus describes other companies.
- Without independent corroboration, AI answers also rarely recommend a vendor for "who can take my Lovable app to production".

**Fix.**

1. Pick **one** spelling, "LaunchStudio", and use it in Yoast site name, titles, schema, footer, social profiles and llms.txt. Keep "Launch Studio" only as `alternateName`.
2. Create profiles that say "LaunchStudio by Manifera" and link to launchstudio.eu:
   - LinkedIn Company Page
   - Clutch
   - GoodFirms (the project already has a `goodfirms/` folder for Manifera)
   - Crunchbase
   - Product Hunt (launch the free checklist or price calculator)
   - G2 or Sortlist
   - KVK/Google Business Profile, only if a real registered address applies
3. Ask 3-5 past clients for reviews on Clutch or Google. Use only real ones.
4. Add a line to Manifera's site, for example on `/services/` and `/about-us/`: "AI prototype to production: see LaunchStudio, our launch service" with a link. Manifera currently links to LaunchStudio from **0** of 36 pages crawled. A link from the parent's domain is the cheapest corroboration available.
5. Put all of these profile URLs in the `sameAs` array (F5).

---

### F12 (P1, S) - llms.txt: complete list, no summary of what you sell

**Evidence.**

- `llms.txt` is generated by the **LLMS Full TXT Generator** plugin (v2.1.2), not Yoast.
- It starts with the site tagline and `Contact: phu.le@manifera.com`, then 320 links in alphabetical order, NL and EN mixed.
- It has no offer, prices, process, service pages or FAQ.
- `llms-full.txt` is 3.7 MB.

**Fix.** If the plugin allows a custom header, add the block below at the top; otherwise replace the file with a static curated `llms.txt` and keep `llms-full.txt` generated. Only use facts already published on the site. Use a role inbox (for example `hello@`) instead of a personal address.

```markdown
# LaunchStudio

> LaunchStudio (by Manifera) takes apps built with AI tools such as Lovable, Bolt, Cursor and Replit to production. We fix security, payments, hosting and deployment. Fixed price €800-7,500, delivered in 1-3 weeks. Based in Amsterdam, engineering in Ho Chi Minh City.

## Services
- [AI app into production](https://launchstudio.eu/en/ai-app-into-production/): the 6 launch checks
- [AI app security](https://launchstudio.eu/en/ai-app-security/): Supabase RLS, exposed keys, auth
- [Payments and integrations](https://launchstudio.eu/en/ai-app-integrations/): Stripe, Mollie, iDEAL, webhooks
- [Finish a vibe-coded app](https://launchstudio.eu/en/vibe-coding-netherlands/)
- [Build from scratch](https://launchstudio.eu/en/build-ai-app-from-scratch/)

## Pricing
- Launch Ready: <exact range from site>
- Launch & Grow: <exact range from site>

## Best guides
- (10-15 cornerstone articles, EN, by cluster)

## Nederlands
- (same structure, NL URLs)
```

Also update the plugin (2.1.2 → 2.1.3).

---

### F13 (P2, M) - Performance and housekeeping

| Item | Evidence | Fix |
|---|---|---|
| TTFB | 0.68 s on all pages, 1.0 s on archives; no `Cache-Control` on HTML | Page cache (server FastCGI cache or WP plugin) + CDN; target TTFB < 0.3 s |
| Core Web Vitals | Not measured (PSI quota) | Run PageSpeed Insights for `/`, `/en/`, 2 landings, 1 post; record in this file |
| Inline base64 image | 1 large `data:` image with `alt=""` on both homepages | Serve as WebP file; alt = person's name and role |
| Google AdSense meta | `Google AdSense meta tags toegevoegd door Site Kit` on the homepage | If AdSense is not used, disconnect it in Site Kit (display ads on a B2B services site hurt trust) |
| `/favicon.ico` | 404 | Upload a root favicon.ico |
| Plugins behind | Yoast 27.6 → 28.9, Polylang 3.8.3 → 3.9.2, WP Mail SMTP 4.8.0 → 4.10.4, UpdraftPlus, Flying Scripts | Update after a backup, Yoast and Polylang first |
| Analytics | Site Kit (GA4 + Ads) present | Add an "AI referrals" exploration in GA4 (section 5) |

---

## 4. Yoast content scores (40 most recently modified posts)

- **SEO score:** 21 good, 19 OK, 0 bad.
- **Weak spots:**
  - The focus keyphrase is sometimes a fragment, for example `AI-Gegenereerde`, `AI-Generated`, `App-Ontwikkeling`, `Offshore-Ontwikkelteam`. A fragment is not a query anyone searches, so the score is meaningless for it.
  - NL keyphrases are sometimes left in English or half-translated (`Bolt App` on the NL Bolt post).
- **Action:** in the upload script, take the focus keyphrase from the validated keyword lists (`nl_security_verified_keywords.csv`, `payments_nl_keywords_validated.csv`, `lovable_5_seeds_volume_validated.csv`) instead of deriving it from the title.

---

## 5. KPIs and measurement

| KPI | Baseline (19 Nov) | Target by 28 Feb 2027 | Where to measure |
|---|---|---|---|
| AI user-agents returning 200 | 5 of 10 key UAs | 10 of 10 | curl test in F1 (weekly) |
| Pages with exactly 1 `<title>` | 0% | 100% | `curl \| grep -c '<title'` on 5 URLs |
| Landing pages with meta description + og:image | 0 / 10 | 10 / 10 | Yoast |
| Indexable duplicate/stub pages | 4 | 0 | `page-sitemap.xml` |
| Indexable tag archives | 370 | 0 | `post_tag-sitemap.xml` |
| Third-party profiles linking to launchstudio.eu | 0 found | ≥ 5 | manual |
| AI referral sessions (chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com, claude.ai) | measure now | +100% vs Dec baseline | GA4 → Traffic acquisition → session source, regex `chatgpt\|perplexity\|gemini\|copilot\|claude` |
| Brand answer accuracy (prompt test below) | measure now | ≥ 7 / 10 prompts describe LaunchStudio correctly | monthly manual test |
| GSC impressions on landing pages | measure now | +50% | Search Console → Pages filter `/ai-app-` |

**Monthly GEO prompt test.** Ask each prompt in ChatGPT (logged-out and logged-in), Perplexity and Gemini. Record whether LaunchStudio is named and whether the description, price and location are correct.

1. What is LaunchStudio (launchstudio.eu)?
2. Who can take my Lovable app to production in the Netherlands?
3. How much does it cost to make an AI prototype production-ready?
4. Is my Supabase anon key safe in a Lovable app? Who can audit it?
5. Bureau die mijn Bolt-app live kan zetten met iDEAL-betalingen?
6. Wat kost het om een AI-prototype live te krijgen?
7. Vibe coding app laten afmaken door een developer in Nederland
8. LaunchStudio vs hiring a freelancer to fix a Lovable app
9. Who is behind LaunchStudio and Manifera?
10. Best services to secure an AI-built app before launch in Europe

---

## 6. Action plan

| When | Action | Finding | Owner | Effort |
|---|---|---|---|---|
| Week of 19 Nov | Unblock AI user-agents in the server/WAF | F1 | Server admin | S |
| Week of 19 Nov | Remove theme meta/OG block | F2 | Dev | S |
| Week of 19 Nov | 4 redirects + delete stubs | F4 | Dev | S |
| Week of 19 Nov | Titles, descriptions, social images for 12 pages | F3 | Content | S |
| Week of 24 Nov | Fix NL slug in upload script; rename 9 posts + 301 | F6 | Content/dev | S |
| Week of 24 Nov | Tags noindex; tag list in script | F8 | Content | S |
| Week of 24 Nov | Organization + FAQPage + Offer schema | F5 | Dev | M |
| Week of 1 Dec | Author profile; brand spelling unified | F9, F11 | Content | S |
| Week of 1 Dec | Curated llms.txt header | F12 | Content | S |
| December | LinkedIn, Clutch, GoodFirms, Crunchbase, Product Hunt profiles; Manifera → LaunchStudio links | F11 | Marketing | L |
| December | Translate 6 decision-stage NL-only posts | F7 | Content | M |
| December | Page cache + CDN; PageSpeed baseline | F13 | Server admin | M |
| Monthly | GEO prompt test + KPI table update | 5 | Marketing | S |

---

## Appendix A - Raw data

**Infrastructure**

- IP 136.243.57.57 (same as manifera.com); DNS at DigitalOcean.
- HTTP/1.1 with h3 advertised; HSTS preload.
- WordPress 7.1.5, Yoast 27.6, Polylang 3.8.3, Site Kit 1.192.0, LLMS Full TXT Generator 2.1.2.

**Sitemaps (19 Nov)**

| Sitemap | URLs | Last modified |
|---|---|---|
| post | 320 (169 NL / 151 EN) | 2026-11-19 |
| page | 21 | 2026-10-26 |
| category | 14 | 2026-11-19 |
| post_tag | 370 | 2026-11-19 |
| author | 2 | 2026-06-22 |

**Post URLs by month (sitemap lastmod):** Mar 17, Jun 13, Jul 88, Aug 74, Sep 20, Oct 32, Nov 76.

**18 NL posts without hreflang pair:**

- `mijn-eerste-klant-betaalde-er-gebeurde-niets`
- `hoeveel-is-jouw-gebruikersdata-waard-voor-een-hacker`
- `de-echte-kosten-van-niet-lanceren`
- `van-prototype-naar-47-betalende-klanten-in-3-weken`
- `wat-gebeurt-er-als-je-app-gehackt-wordt`
- `hoe-behoud-je-eigendom-als-je-met-developers-werkt`
- `de-launch-checklist-die-je-wel-begrijpt`
- `bureau-vs-freelancer-vs-launchstudio`
- `wat-kost-het-om-je-prototype-live-te-krijgen`
- `waarom-90-van-ai-prototypes-nooit-live-gaat-2`
- `kan-mijn-lovable-code-echt-in-productie`
- `wie-zitten-er-achter-launchstudio`
- `wat-als-het-niet-werkt-hoe-wij-risico-wegnemen`
- `je-eerste-100-gebruikers-wat-breekt-er-het-eerst`
- `zelf-doorbouwen-of-uitbesteden-na-de-launch`
- `van-bijbaan-idee-naar-200-gebruikers-in-6-weken`
- `hoe-een-fysiotherapeut-zijn-wachtlijst-oploste-met-een-app`
- `hoe-wij-werken-van-intake-tot-oplevering-in-5-stappen`

**Newest posts, on-page (all 200, canonical self, hreflang nl/en/x-default, H1 = title)**

| Post | Article words | H2 | Title chars |
|---|---|---|---|
| EN app-development-cost-2026 | 2,275 | 16 | 75 |
| NL kosten app-ontwikkeling 2026 | 2,344 | 16 | 89 |
| EN github-copilot-agent-code-review | 2,459 | 10 | 91 |
| NL github-copilot … productiechecks | 2,658 | 10 | 90 |
| EN bolt-cloud-or-your-own-backend | 2,367 | 11 | 79 |
| NL bolt cloud of een eigen backend | 2,685 | 11 | 84 |

Titles over 60 chars get truncated in Google. Set a shorter Yoast SEO title, and keep the long H1.

**Crawler test command used:** `curl -s -o /dev/null -w '%{http_code}' -A "Mozilla/5.0 (compatible; <UA>)" <url>`
