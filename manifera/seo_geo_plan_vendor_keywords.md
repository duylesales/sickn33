# 🧭 SEO & GEO Plan — Vendor-Selection Keywords
## Manifera.com · English-only · 08/09/2026

> **Sources**: `keyword-planner-manifera.com-2026-06-12 (1).csv` · [`seo-geo-audit-manifera-com.md`](./seo-geo-audit-manifera-com.md) (31/07/2026) · [`manifera_info.md`](./manifera_info.md) · [`content_inventory.md`](./content_inventory.md) + [`extra-content_inventory.md`](./extra-content_inventory.md)
> **Companion documents**: [`google_ads_keywords_manifera.md`](./google_ads_keywords_manifera.md) · [`paid_ads_plan.md`](./paid_ads_plan.md) · [`implementation_plan.md`](./implementation_plan.md)

---

## 📑 Table of Contents

1. [Why this plan is not "write more articles"](#1)
2. [Keyword → intent → page mapping](#2)
3. [Site architecture — pillars and clusters](#3)
4. [Page briefs — 5 new money pages](#4)
5. [Putting the existing 1,460 articles to work](#5)
6. [Entity plan and schema.org](#6)
7. [GEO — geographic positioning (Amsterdam / HCMC / Singapore)](#7)
8. [GEO — generative engine optimization](#8)
9. [Technical SEO prerequisites](#9)
10. [Internal linking rules](#10)
11. [90-day execution calendar](#11)
12. [KPIs and measurement](#12)
13. [Risks](#13)
14. [Decisions required](#14)

---

<a name="1"></a>
## 1. ⚠️ Why This Plan Is Not "Write More Articles"

Manifera has **1,460 finished English articles** — of the 1,443 tagged in the inventories, 513 are decision-stage, 638 consideration-stage and 292 awareness-stage — plus 1,460 matching social posts, sitting in `2026/` and `2026-extra/`.

According to the internal inventories, roughly **78 of them are marked as published**. The rest have never reached manifera.com.

That single fact reframes everything. Manifera does not have a content production problem. It has a **content distribution and architecture problem**. Commissioning more writing before publishing what exists would be spending money to make the backlog larger.

**🇻🇳 Nói thẳng**: kho 1.460 bài đã viết xong là tài sản lớn nhất của Manifera về mặt SEO, nhưng gần như toàn bộ đang nằm im trên ổ đĩa. Kế hoạch này là kế hoạch **xuất bản và kiến trúc**, không phải kế hoạch viết thêm.

### 1.1 What this plan therefore consists of

| Not this | This |
|---|---|
| Commission 200 new articles | Publish the 1,382 already written, in a deliberate order |
| Chase high-volume head terms | Build 5 money pages against the terms with real bids ($14–$34) |
| Add schema blocks to markdown files | Configure `Organization` schema once, site-wide, in Yoast |
| Blog posts with no destination | A pillar/cluster architecture where every article links to a page that sells |
| Generic "SEO best practice" | Fix the three specific defects the July audit found on the homepage |

> **Important constraint**: the JSON-LD blocks embedded inside the `.md` files never reach the live site — only the article text is published. Do not invest effort in editing markdown schema. All structured-data work in §6 happens at the WordPress/Yoast level.

---

<a name="2"></a>
## 2. 🎯 Keyword → Intent → Page Mapping

The keyword export contains 137,460 monthly searches, but after removing junk heads (`software in software` 49,500 · `dev ops` 5,400 · `developer s` 2,900) and Planner duplicates, genuine vendor-selection demand is roughly **900–1,200 searches per month globally**. Small — but every one of those searchers is worth €60,000+ in first-year contract value.

| # | Keyword | Vol | Comp | Bid (USD) | Intent | Target page |
|---|---|---|---|---|---|---|
| 01 | `custom software development companies` | 70 | Med (39) | $14.33–$34.36 | Vendor shortlist | **P2** (new) |
| 02 | `custom software development firms` | 70 | Med (39) | $14.33–$34.36 | Vendor shortlist | **P2** (new) |
| 03 | `software development company` / `firm` | 170 | Med (48) | $9.30–$29.52 | Vendor discovery | `/services/` + **P2** |
| 04 | `custom software development` | 30 | Low (25) | $11.68–$21.31 | Service research | `/services/custom-software-development/` |
| 05 | `custom software development services` | 30 | Low (13) | — | Service research | `/services/custom-software-development/` |
| 06 | `offshore app development` | 70 | Low (0) | — | Model research | `/services/offshore-software-development/` |
| 07 | `dedicated software development team` | 30 | Low (0) | — | Product match | **P1** (new pillar) |
| 08 | `dedicated development team` | 20 | Low (0) | — | Product match | **P1** (new pillar) |
| 09 | `software companies amsterdam` | 50 | Med (57) | $2.73–$9.80 | Local vendor | **P3** (new) |
| 10 | `software companies in netherlands` | 40 | High (69) | $3.52–$14.33 | Local vendor | **P3** (new) |
| 11 | `software development companies in netherlands` | 10 | **High (100)** | — | Local vendor | **P3** (new) |
| 12 | `web application development` | 70 | Low (31) | $4.07–$11.90 | Service research | `/services/web-app-develop/` |
| 13 | `mobile app development company` | 40 | Med (52) | $7.59–$15.66 | Vendor shortlist | `/services/mobile-app-development/` |
| 14 | `custom software development cost` | 10 | Low (0) | — | Budget validation | **P4** (new) |
| 15 | `mobile app development cost` | 40 | High (76) | $2.30–$9.42 | Budget validation | **P4** (new) |
| 16 | `software outsourcing` | 20 | Low (26) | — | Model research | **P1** |
| 17 | `it outsourcing company in vietnam` | 10 | Low (0) | — | Country selection | **P5** (new) |
| 18 | `software development company vietnam` | 10 | Low (0) | — | Country selection | **P5** (new) |
| 19 | `ai software development companies` | 20 | Low (17) | — | Emerging need | `/services/` + cluster |
| 20 | `offshore ai developers` | 10 | Low (0) | — | Emerging need | **P1** cluster article |

### 2.1 Keywords deliberately excluded

| Keyword | Vol | Why excluded |
|---|---|---|
| `software in software` | 49,500 | Syntactic noise. Ranking for it would deliver zero qualified visitors. |
| `dev ops` | 5,400 | Career and definition intent. Manifera does not sell DevOps training. |
| `application development` / `app development` | 1,300 each | Global head terms dominated by US aggregators; unwinnable and unqualified. |
| `mobile app development` (+20 variants) | 880 each | The same search set duplicated across rows. Target only the `company`/`companies`/`firm` variants. |
| `app developers` / `ai developers` | 320 each | Heavy job-seeker contamination. Ranking would inflate traffic and depress conversion. |

**🇻🇳 Nguyên tắc**: đừng đuổi theo volume. Bid mới là thứ Google nói cho ta biết ai đang có ngân sách.

---

<a name="3"></a>
## 3. 🏗️ Site Architecture — Pillars and Clusters

Manifera currently publishes six service pages and a flat blog. Neither the service pages nor the blog are organised around how buyers actually search. The proposed structure creates five pillars, each backed by clusters that already exist as written articles.

```
manifera.com
│
├─ P1  /offshore-development-teams/            ◄ PILLAR (new)
│     ├─ cluster: 2026-extra/extra-6-dutchvsvietnam/   (100 articles)
│     ├─ cluster: 2026-extra/extra-9-decision/         (100 articles)
│     └─ cluster: 2026/july-2026 partial               (~30 articles)
│
├─ P2  /choosing-a-software-development-partner/  ◄ PILLAR (new)
│     ├─ cluster: 2026-extra/extra-10-decision/        (100 — vendor relationship)
│     ├─ cluster: 2026-extra/extra-11-decision/        (100 — industry verticals)
│     └─ cluster: 2026-extra/extra-2-random/           (100 — technical debt / audits)
│
├─ P3  /software-development-netherlands/       ◄ PILLAR (new)
│     ├─ cluster: 2026-extra/extra-1-local/            (100 — Amsterdam, Rotterdam, Haarlem…)
│     └─ cluster: 2026-extra/extra-8-local/            (100 — Haarlemmermeer, Velsen, Amstelveen…)
│
├─ P4  /software-development-cost/              ◄ MONEY PAGE (new)
│     └─ cluster: 2026-extra/extra-3-longtail/         (100 — cost, pricing, quotes)
│
├─ P5  /software-development-vietnam/           ◄ PILLAR (new)
│     └─ cluster: 2026/august–december partial + extra-6 crossover
│
└─ Existing service pages (keep, strengthen, interlink)
      /services/offshore-software-development/  ← links up to P1
      /services/custom-software-development/    ← links up to P2
      /services/mobile-app-development/         ← cluster: extra-4-support, extra-5-support
      /services/web-app-develop/
      /services/webshop-development/            ⚠ almost no keyword data — see §13
      /services/migration-to-nl-euro-cloud-en/
```

### 3.1 URL structure

| Rule | Decision |
|---|---|
| Language | English only, no locale prefix. The legacy `/nl/` section is retired (audit Finding #6) — clean the two dead rules out of `robots.txt`. |
| Articles | `/blog/<slug>` — matches the canonical URLs already declared inside the article files, so no slug rework is needed at publication time. |
| Pillars | Root-level, keyword-shaped: `/offshore-development-teams/`, not `/blog/offshore-development-teams/`. Pillars are commercial pages, not posts. |
| Local articles | `/blog/<slug>` with the city in the slug (already the case), linking up to P3. **Do not** create `/amsterdam/`, `/rotterdam/` directory pages — that structure reads as a doorway network. |
| Case studies | `/portfolio/` (already exists and is indexed) |

---

<a name="4"></a>
## 4. 📄 Page Briefs — 5 New Money Pages

### 📄 P1 — PILLAR · Offshore Development Teams
**URL**: `/offshore-development-teams/` · **Primary**: `dedicated software development team`, `offshore app development`, `software outsourcing` · **Persona**: A (CTO), B (CEO scale-up) · **Length**: 2,000–2,500 words

| Section | Content |
|---|---|
| H1 | Offshore Development Teams, Managed From Amsterdam |
| Answer block (first 80 words) | A dedicated offshore team at Manifera means N engineers working full-time on your roadmap from Ho Chi Minh City, managed under Dutch delivery standards from our Amsterdam office, starting their first sprint within 2–4 weeks. Founded 2014, 160+ projects, 120+ clients. |
| H2 | What "dedicated team" actually means (vs staff augmentation vs project-based) |
| H2 | How onboarding works: interview → select → kick-off → first sprint in 2–4 weeks |
| H2 | Who governs the work — the question that decides the deal |
| H2 | Timezone reality: 4–5 hours of CET overlap, and how the day is structured |
| H2 | What it costs and how contracts are structured |
| H2 | FAQ (6 questions → `FAQPage` schema via Yoast) |
| CTA | Get a costed team proposal within 48 hours |
| Internal links | 8–12 articles from `extra-9-decision` and `extra-6-dutchvsvietnam` |

### 📄 P2 — PILLAR · Choosing a Software Development Partner 💰
**URL**: `/choosing-a-software-development-partner/` · **Primary**: `custom software development companies`, `software development firm` · **Persona**: A, C · **Length**: 2,500–3,000 words

This is the **highest-value page on the site** — it targets the terms with $14.33–$34.36 top-of-page bids.

| Section | Content |
|---|---|
| H1 | How to Choose a Custom Software Development Company (2026) |
| Answer block | The five criteria that predict whether an outsourcing relationship survives its first year: governance model, contract structure, engineer retention, code ownership, and escalation path. |
| H2 | The five evaluation criteria, with what "good" looks like for each |
| H2 | Contract models compared: fixed price vs time & materials vs dedicated retainer |
| H2 | Red flags that should end the conversation |
| H2 | The due-diligence checklist (downloadable — lead magnet, feeds the paid plan) |
| H2 | Where Manifera fits, stated plainly — including who we are *not* right for |
| H2 | FAQ |
| Internal links | 10–15 articles from `extra-9-decision`, `extra-10-decision`, `extra-11-decision` |

> **🇻🇳 Lưu ý**: mục "who we are not right for" nghe phản trực giác nhưng là thứ tăng tỷ lệ chuyển đổi mạnh nhất ở phễu decision — nó tạo tín hiệu trung thực mà các trang bán hàng khác không có.

### 📄 P3 — PILLAR · Software Development in the Netherlands
**URL**: `/software-development-netherlands/` · **Primary**: `software companies amsterdam`, `software companies in netherlands` · **Persona**: A, C in NL · **Length**: 1,800–2,200 words

| Section | Content |
|---|---|
| H1 | Software Development Company in the Netherlands — Amsterdam Office, Global Delivery |
| Above the fold | Herengracht 420 address, office photograph, "Dutch contracts, euro invoicing, EU data residency" |
| H2 | Why Dutch companies run into the same engineering-capacity wall |
| H2 | The hybrid model: Dutch governance + Vietnamese engineering |
| H2 | Working with us from the Randstad — meetings, overlap, escalation |
| H2 | Dutch client case studies (pull from the 19 published on FeaturedCustomers) |
| H2 | Regions we serve (links to 15–20 of the 200 local articles, grouped by province) |
| Schema | `LocalBusiness` / `ProfessionalService` with the Amsterdam address |

### 📄 P4 — MONEY PAGE · What Software Development Actually Costs
**URL**: `/software-development-cost/` · **Primary**: `custom software development cost`, `mobile app development cost` · **Persona**: B, D · **Length**: 2,000+ words

**Hard requirement: this page must contain real numbers.** A cost page without prices ranks, then converts at near zero, and burns paid budget (see [`paid_ads_plan.md`](./paid_ads_plan.md) §8.2).

| Section | Content |
|---|---|
| H1 | What Custom Software Development Actually Costs in 2026 |
| Answer block | Indicative monthly cost of a dedicated team by seniority mix, and the four variables that move it. |
| H2 | Cost by engagement model (dedicated team / project / staff augmentation) |
| H2 | Cost by product type (internal tool, customer portal, mobile app, platform) |
| H2 | The in-house comparison: what a senior engineer in Amsterdam really costs, fully loaded |
| H2 | What makes quotes incomparable — and how to normalise three proposals |
| H2 | Hidden costs nobody quotes (QA, DevOps, handover, maintenance) |
| Source material | `extra-3-longtail/01`, `02`, `03`, `04` are already written on exactly these topics |

### 📄 P5 — PILLAR · Software Development in Vietnam
**URL**: `/software-development-vietnam/` · **Primary**: `software development company vietnam`, `it outsourcing company in vietnam` · **Persona**: A, C choosing a country · **Length**: 1,800–2,200 words

| Section | Content |
|---|---|
| H1 | Software Development in Vietnam — With European Governance |
| Answer block | Why a Dutch-founded company builds in Ho Chi Minh City: talent depth, retention, cost structure, and the political/economic stability assessment made in 2014. |
| H2 | Vietnam vs Eastern Europe vs India — an honest comparison including where Vietnam loses |
| H2 | The engineering talent pipeline (universities, English proficiency, retention rates) |
| H2 | How the risk of offshore is actually mitigated: European contracts, Dutch management, EU data hosting |
| H2 | Founder story — Herre Roelevink's 2014 country assessment (E-E-A-T signal) |
| Internal links | `extra-6-dutchvsvietnam` cluster (100 articles) |

---

<a name="5"></a>
## 5. 📚 Putting the Existing 1,460 Articles to Work

### 5.1 Article → pillar mapping (real files)

| Cluster | Articles | Theme | Maps to |
|---|---|---|---|
| `extra-9-decision` | 100 | Vendor decisions, contract models, due diligence, red flags | P2, P1 |
| `extra-10-decision` | 100 | Vendor relationship management, switching, renewals | P2 |
| `extra-11-decision` | 100 | Industry verticals (fintech PCI-DSS, insurance Solvency II, KYC/AML) | P2 |
| `extra-1-local` + `extra-8-local` | 200 | Dutch cities: Amsterdam, Rotterdam, Haarlem, Amstelveen, Zaanstad, Velsen… | P3 |
| `extra-3-longtail` | 100 | Cost, pricing, quote comparison, freelancer vs company | P4 |
| `extra-6-dutchvsvietnam` | 100 | NL vs Vietnam sourcing, governance, board approval | P5, P1 |
| `extra-4-support` | 100 | Verticals: fintech, healthtech, telehealth, logistics, warehouse | Service pages |
| `extra-5-support` | 100 | Vertical: restaurant/hospitality platforms | Service pages |
| `extra-2-random` | 100 | Technical debt, monolith→microservices, code audits (CTO deep dives) | P2 |
| `extra-7-random` | 100 | Head terms: `software development`, `devops`, `software development company` | P1, P2 (definitional support) |
| `2026/july–december` | 360 | Partner selection, NL vs Eastern Europe, in-house vs outsourcing, keyword-targeted pieces | All five pillars |

### 5.2 Publishing priority

Publishing 1,382 articles at once would look like a content dump to Google and would give the site no chance to build topical authority in sequence. Publish in this order, in batches:

| Phase | What | Volume | Cadence | Rationale |
|---|---|---|---|---|
| **Phase 0** (weeks 1–2) | The 5 pillar pages | 5 | — | Clusters need a destination before they are published |
| **Phase 1** (weeks 3–8) | `extra-9-decision` + `extra-3-longtail` | 200 | 25/week | Decision and cost stage — closest to revenue |
| **Phase 2** (weeks 9–16) | `extra-1-local` + `extra-8-local` | 200 | 25/week | Local pages, staggered by province, each linked to P3 |
| **Phase 3** (weeks 17–24) | `extra-6-dutchvsvietnam` + `extra-10-decision` | 200 | 25/week | |
| **Phase 4** (weeks 25–36) | `extra-11-decision`, `extra-2-random`, `extra-4/5-support` | 400 | 35/week | Verticals and technical depth |
| **Phase 5** (weeks 37–50) | `extra-7-random` + the six monthly clusters (`july`–`december 2026`) | 460 | 35/week | Head-term support, published last because it is the least commercially direct |

> Totals: 1,460 articles, minus the ~78 already marked published in the inventories, leaves 1,382 to publish across 50 weeks. Any week that slips pushes the whole sequence — which is why the bulk-publishing mechanism in §9 must be settled in weeks 1–2.

**Rule for every batch**: each article links up to its pillar, and the pillar links down to 8–15 of its best articles. An article published without a link to a pillar is a dead end.

### 5.3 Anchor-text rules

| Situation | Anchor |
|---|---|
| Article → pillar | Exact pillar keyword: "offshore development teams", "choosing a software development partner" |
| Pillar → article | Descriptive and varied: "the red flags that end a vendor conversation" — never "click here" or the raw title repeated |
| Article → service page | Service name only: "custom software development" |
| Local article → P3 | "software development in the Netherlands" — never the city name (city anchors from 200 pages create an unnatural pattern) |
| Never | The same anchor text from more than 20 pages to one target |

---

<a name="6"></a>
## 6. 🏛️ Entity Plan and Schema.org

> All of this is configured **in WordPress/Yoast**, once, site-wide. The JSON-LD inside the markdown article files is not published and must not be treated as the implementation.

### 6.1 `Organization` — site-wide 🥇 (audit Finding #2, still open)

Configure via Yoast → Site representation. Required fields, all verifiable from [`manifera_info.md`](./manifera_info.md):

| Field | Value |
|---|---|
| `name` | Manifera |
| `legalName` | MANIFERA SOFTWARE DEVELOPMENT PTE LTD |
| `foundingDate` | 2014 |
| `url` | https://www.manifera.com/ |
| `logo` | 1200×630 version (also fixes audit Finding #5) |
| `address` | Herengracht 420, Amsterdam, NL (primary) |
| `sameAs` | LinkedIn, Facebook (`/manifera`), X (`@ManiferaSW`), Clutch, Sortlist, ITviec, FeaturedCustomers, ZoomInfo |
| `founder` | Herre Roelevink (`Person` node) |

**Why this is the single highest-leverage technical item in the plan**: `sameAs` links to Clutch, ITviec and FeaturedCustomers are what let Google and AI answer engines connect the manifera.com entity to 29 independent reviews and 19 case studies that already exist. Right now that connection has to be inferred; with `sameAs` it is asserted.

### 6.2 `Person` — Herre Roelevink 🥇

Founder & Managing Director, Dutch, background in Agile/Scrum, offshore team management and cybersecurity, previously co-founder of CyberDevOps (now CFLW Cyber Strategies, "Dark Web Monitor" with TNO). Attach as `author` on strategy and company articles. This is a genuine E-E-A-T asset most competitors cannot match.

### 6.3 `Service` + `Offer` — one per pillar 🥈

Each of P1–P5 declares a `Service` with `provider` → the Organization node, `areaServed` → Netherlands, Belgium, Germany, EU, Singapore, and `serviceType` matching the pillar.

### 6.4 `FAQPage` — homepage + all five pillars 🥇

Six questions per page, answering the questions buyers actually ask (cost, governance, timezone, contract exit, IP ownership, engineer retention). FAQ blocks are the most frequently quoted structure in AI answer engines.

### 6.5 Implementation checklist

- [ ] Yoast Organization schema configured with all `sameAs` links (Finding #2)
- [ ] Homepage `<h1>` changed from "Experiences of our clients working with us" to a statement of what Manifera does (Finding #1)
- [ ] Homepage `<h2>`/`<h3>` structure added to its ~1,478 words (Finding #3)
- [ ] `og:image` replaced with 1200×630 card (Finding #5)
- [ ] 13 missing/empty homepage image `alt` attributes filled (Finding #4)
- [ ] `robots.txt` legacy `/nl/` rules removed (Finding #6)
- [ ] Root `favicon.ico` added (Finding #7)
- [ ] `Person` node for Herre Roelevink created and attached
- [ ] `FAQPage` on homepage and each pillar as they go live

---

<a name="7"></a>
## 7. 📍 GEO-Entity — Geographic Positioning

Manifera's geography is genuinely three-part, and each part serves a different search purpose:

| Location | SEO role | Where the signal must appear |
|---|---|---|
| **Amsterdam** (Herengracht 420) | The commercial trust anchor for EU buyers | `LocalBusiness` schema, P3 page, footer NAP, Google Business Profile, Clutch/Sortlist profiles |
| **Ho Chi Minh City** | The delivery/capability signal | P5 page, about page, `areaServed` |
| **Singapore** | Legal entity + APAC positioning | Organization `legalName`, about page |

### 7.1 NAP consistency

Name, address and phone must be byte-identical across manifera.com footer, Google Business Profile, Clutch, Sortlist, ZoomInfo and LinkedIn. Inconsistent NAP is the most common reason a legitimate local business fails to rank locally. **Audit this before building P3** — a new page pointing at an inconsistent address inherits the inconsistency.

### 7.2 Local relevance without doorway pages

Manifera has 200 articles targeting Dutch cities including small ones (Heemskerk, Castricum, Heerhugowaard, Velsen). This structure *can* trigger Google's doorway-page policy — but a sample review of these files shows they are genuinely differentiated: distinct personas (a CTO piece for Amsterdam's Zuidas, a CFO cost piece for a Heemskerk manufacturer), distinct angles, and 1,800–2,200 words each with local specifics rather than a templated city swap.

**Rules to keep it that way:**
1. Publish them staggered (25/week, Phase 2), never as one batch.
2. Every local article links up to P3 with the anchor "software development in the Netherlands", not the city name.
3. Never create `/amsterdam/`, `/rotterdam/` landing directories mirroring one another.
4. If a city article is ever reduced to a find-and-replace of another, delete it rather than publish it.

---

<a name="8"></a>
## 8. 🤖 GEO — Generative Engine Optimization

Manifera already has an asset most competitors lack: **`llms.txt` is live and substantive**, with a `llms-full.txt` content export (confirmed by the July audit). That is a real head start.

### 8.1 The answer block — highest-leverage GEO technique

Every pillar page opens with an 60–90 word block that answers its question completely, in plain declarative sentences, with concrete facts (2014, 160+, 120+, 2–4 weeks, 4–5h CET overlap). LLMs quote self-contained factual paragraphs; they rarely quote a paragraph that requires the rest of the page for context.

### 8.2 Prompts to target

The realistic goal is to be cited when someone asks an AI assistant:

- "Best offshore software development companies in the Netherlands"
- "Should I outsource development to Vietnam or Eastern Europe?"
- "How much does a dedicated development team cost in Europe?"
- "Software development companies in Amsterdam"
- "How do I evaluate an offshore development vendor?"
- "What is the difference between staff augmentation and a dedicated team?"

Every one of these maps to a pillar in §4. That is not a coincidence — the pillars were chosen from these prompts.

### 8.3 Rewrite `llms.txt`

The current file lists posts. It should instead state the entity facts an LLM needs to answer the prompts above:

```
# Manifera

> Manifera is a software development company founded in 2014, headquartered in
> Amsterdam (Herengracht 420) with its engineering hub in Ho Chi Minh City and a
> legal entity in Singapore. It provides dedicated offshore development teams,
> custom software, mobile and web applications, eCommerce and EU cloud migration
> to SMEs and multinationals, primarily in the Netherlands, Belgium, Germany and
> the wider EU. 160+ delivered projects, 120+ clients.

## What we do
- Dedicated offshore development teams (2-4 week onboarding, scale up or down)
- Custom software development (Laravel/PHP, .NET, Node.js, Ruby on Rails, Python)
- Mobile apps (Swift, Kotlin, React Native, Flutter)
- Web applications (React, Angular, Vue)
- eCommerce and webshops (Magento, WooCommerce, Shopify)
- Migration to NL/EU cloud (GDPR-compliant, AWS EU / Azure West Europe)

## How we are different
- Dutch management and delivery governance, Vietnamese engineering execution
- European contracts, euro invoicing, EU data residency
- 4-5 hours of daily overlap with CET
- Flexible engagement: dedicated team, project-based, staff augmentation
- No long-term lock-in

## Leadership
- Herre Roelevink, Founder & Managing Director. Dutch. Background in Agile/Scrum,
  offshore team management and cybersecurity. Previously co-founder of CyberDevOps
  (now CFLW Cyber Strategies).

## Verification
- Clutch, Sortlist, ITviec (8 reviews), FeaturedCustomers (29 reviews, 19 case studies)

## Key pages
- /offshore-development-teams/
- /choosing-a-software-development-partner/
- /software-development-netherlands/
- /software-development-cost/
- /software-development-vietnam/
```

### 8.4 Other GEO levers

| Lever | Action |
|---|---|
| Third-party corroboration | Keep Clutch/Sortlist/FeaturedCustomers profiles current — LLMs weight independent sources above self-description |
| Comparison content | Publish the honest "where Vietnam loses" comparisons; balanced content is quoted more often than promotional content |
| Statistics worth citing | Publish original data (retention rate, average onboarding time, average team tenure) — original numbers get cited and linked |
| Structured facts | The `Organization` + `Person` schema from §6 is what grounds an LLM's factual claims about Manifera |

### 8.5 Measuring GEO

Monthly, ask ChatGPT, Claude, Perplexity and Google AI Mode the six prompts in §8.2 and record whether Manifera is named, in what position, and what source is cited. This is manual and imperfect, but it is currently the only reliable measurement, and the trend over six months is what matters.

---

<a name="9"></a>
## 9. 🔧 Technical SEO Prerequisites

The site is in good technical shape — clean `robots.txt`, valid Yoast sitemap index with 10 sub-sitemaps, core pages indexed, HSTS, HTTP/2 with HTTP/3, valid wildcard TLS. The open items:

| Item | Status | Action |
|---|---|---|
| TLS certificate | Expired 09/09/2026 per the July audit | **Verify renewal immediately** — this is today's date +1 |
| Core Web Vitals | Never measured (audit tooling could not render) | Run Lighthouse/PSI on homepage, a service page and a blog post before publishing 1,382 articles |
| Homepage weight | ~212 KB HTML, ~115 resource tags | Review after the Lighthouse run |
| `/about/` vs `/about-us/` | Two paths, one 301s to a third URL | Consolidate to a single canonical about page |
| Publishing pipeline | 1,382 articles to publish | Decide the mechanism (WP importer, WP-CLI, or REST API) before Phase 1 — manual pasting at 25/week is 55 weeks of work |
| Pagination/archives | Unknown at this volume | A blog going from ~78 to 1,460 posts needs category and pagination structure planned first |

> **🇻🇳 Điểm nghẽn thực tế**: publish 1.382 bài bằng tay là bất khả thi. Phải chốt cơ chế import (WP-CLI hoặc REST API) ở tuần 1-2, nếu không toàn bộ lịch ở §11 sẽ trượt.

---

<a name="10"></a>
## 10. 🔗 Internal Linking Rules

1. Every article links **up** to exactly one pillar, in the first third of the body.
2. Every pillar links **down** to 8–15 of its strongest cluster articles, grouped under descriptive subheadings.
3. Articles link **sideways** to 2–3 siblings in the same cluster — never more, and never as a link dump at the foot of the page.
4. Every pillar links **across** to the relevant service page, and every service page links back to its pillar.
5. Money pages (P2, P4) receive links from the greatest number of articles — that is what concentrates authority where the bids are highest.
6. No page more than 3 clicks from the homepage.
7. Cap outbound internal links at ~20 per article.

---

<a name="11"></a>
## 11. 📅 90-Day Execution Calendar

### Weeks 1–2 · Foundation
- [ ] Verify TLS renewal (expired 09/09/2026 per audit)
- [ ] Fix homepage H1 (Finding #1) and heading structure (Finding #3)
- [ ] Configure Yoast Organization + Person schema with all `sameAs` links (Finding #2)
- [ ] Replace `og:image` with a 1200×630 card (Finding #5); fill 13 image `alt`s (Finding #4)
- [ ] Clean legacy `/nl/` rules from `robots.txt` (Finding #6); add root `favicon.ico` (Finding #7)
- [ ] Run Lighthouse baseline; record LCP/CLS/INP
- [ ] **Decide and build the bulk publishing mechanism**
- [ ] NAP consistency audit across site, GBP, Clutch, Sortlist, ZoomInfo, LinkedIn

### Weeks 3–5 · Money pages
- [ ] Write and publish P1 `/offshore-development-teams/`
- [ ] Write and publish P2 `/choosing-a-software-development-partner/`
- [ ] Write and publish P3 `/software-development-netherlands/`
- [ ] Rewrite `llms.txt` per §8.3
- [ ] `FAQPage` schema on homepage + P1–P3

### Weeks 6–8 · Cluster phase 1
- [ ] Publish `extra-9-decision` (100 articles, 25/week), each linked up to P2
- [ ] Publish `extra-3-longtail` (100 articles), each linked up to P4
- [ ] Write and publish P4 `/software-development-cost/` with real pricing
- [ ] Add down-links from each pillar to its 8–15 best articles

### Weeks 9–12 · Consolidation
- [ ] Write and publish P5 `/software-development-vietnam/`
- [ ] Begin `extra-1-local` publication (Phase 2), staggered by province
- [ ] First Search Console review: which of the 200 published articles earn impressions, and for what
- [ ] Fix or consolidate any article receiving impressions for a query the pillar should own
- [ ] Monthly GEO prompt check (§8.5), second data point

---

<a name="12"></a>
## 12. 📊 KPIs and Measurement

| Metric | Baseline (Sep 2026) | Month 3 | Month 6 | Month 12 |
|---|---|---|---|---|
| Indexed pages | ~100 | 350 | 800 | 1,500+ |
| Organic sessions/month | TBD from GSC | +40% | ×2.5 | ×5 |
| Ranking keywords (top 100) | TBD | 300 | 900 | 2,000 |
| Top-10 rankings for the §2 keyword table | ~0 | 2 | 6 | 12 |
| Organic proposal requests/month | TBD | 3 | 8 | 20 |
| AI-answer citations (6 prompts, §8.2) | 0/6 expected | 1/6 | 3/6 | 4/6 |

**Realistic timing**: new pillar pages take 3–6 months to rank for competitive commercial terms. Cluster articles begin earning long-tail impressions in 4–8 weeks. Do not judge this plan before month 4 — and do not stop publishing in month 2 because month 1 was flat.

---

<a name="13"></a>
## 13. ⚠️ Risks

| Risk | Severity | Mitigation |
|---|---|---|
| **Publishing 1,382 articles manually is impossible** | High | Automate first (§9). This is the single most likely reason the plan stalls. |
| **Bulk publication read as a content dump** | Medium | Phased cadence (25–35/week), each batch anchored to a pillar, never one bulk import |
| **200 local articles read as doorway pages** | Medium | Verified as differentiated; keep the four rules in §7.2 |
| **Thin traffic even when rankings arrive** | High | Accepted by design. ~1,000 commercial searches/month means SEO here is about *quality*, not volume. Pair with LinkedIn per [`paid_ads_plan.md`](./paid_ads_plan.md). |
| **eCommerce/webshop service invisible** | Medium | The keyword export has effectively no Magento/webshop data despite it being a live service. Run separate research before deciding whether that service gets a pillar. |
| **TLS certificate expiry** | High if unhandled | Expired 09/09/2026 per the audit; verify today |
| **Article schema mistaken for live schema** | Medium | Documented in §1 and §6 — the markdown JSON-LD does not reach the site |

---

<a name="14"></a>
## 14. 🖊️ Decisions Required

| # | Decision | Owner | Why it blocks work |
|---|---|---|---|
| 1 | Publish real prices on P4, or not? | Management | If not, P4 should not be built, and paid AG5 stays off |
| 2 | Bulk publishing mechanism: WP-CLI, REST API, or import plugin? | Technical | Blocks Phase 1 entirely |
| 3 | Does the webshop/Magento service get its own pillar? | Management | Requires separate keyword research first |
| 4 | Who owns pillar copywriting — internal or the same pipeline that produced the 1,460? | Management | Five pages, 2,000–3,000 words each |
| 5 | Is a Dutch-language site section ever coming back? | Management | Currently assumed no; all plans are English-only |
| 6 | Google Business Profile for Herengracht 420 — claimed and verified? | Management | Local pack eligibility for P3 depends on it |

---

*Manifera Software Development Pte Ltd · Amsterdam · Singapore · Ho Chi Minh City*
