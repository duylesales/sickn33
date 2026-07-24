# LaunchStudio — Paid Advertising Plan (Multi-Channel, Execution-Ready)

> **Scope:** https://launchstudio.eu/ — AI-native founder production-readiness service (parent: Manifera)
> **Source data:** `keyword-planner-https___launchstudio.eu_en_-2026-06-15.csv` (123 keywords, 214,280 total monthly volume)
> **Prepared:** 2026-07-24 · **Revised:** execution-detail pass
> **Companion file:** `paid_ads_plan_dutch.md` (Nederlandse versie)
> **How to use this doc:** Section 3 is the strategic rationale (keep it). Sections 4–13 are copy-paste-ready campaign structures, ad copy, budgets, and a week-by-week build checklist — this is what an ad account should actually look like on day 1.

---

## 1. Executive Summary

LaunchStudio's existing keyword data is Search-only and English-only, but the buyer doesn't live only in Google Search. This plan cleans the CSV (the headline "214,280/month" figure is 94% one mismatched term — see §3.1), expands it with tool-brand, problem-based, comparison, and Dutch-language keywords, and lays out **exact, launchable campaign structures across 6 platforms**: Google Search, Microsoft/Bing, LinkedIn, Meta, X (Twitter), and Reddit — including ad group names, keyword-to-ad-group mapping, suggested bids, full ad copy, audience specs, daily budgets, UTM conventions, and landing page content outlines.

**Recommended starting budget: €5,000/month (Tier 2, see §9)** — this document is written around that number so every campaign has a concrete euro figure attached, not just a percentage. Scale up or down proportionally using the Tier 1 / Tier 3 tables in §9 if the actual available budget differs.

---

## 2. Funnel Mapping (Buyer Stage → Channel Role)

| Stage | Buyer mindset | Best-fit channels | Keyword/targeting logic |
|---|---|---|---|
| **Awareness** | "I built something with AI, is that normal?" | X, Reddit, Meta (video), YouTube | Tool-brand terms, community placement |
| **Consideration** | "How do I get this live / secure / paid?" | Google Search, LinkedIn, Meta retargeting | Problem/build-intent terms |
| **Decision** | "Who do I actually hire?" | Google Search (branded + comparison), LinkedIn InMail, Bing | Comparison terms, branded terms |

---

## 3. Keyword Strategy

### 3.1. Cleaning the existing CSV — what NOT to bid on as-is

| Keyword | Volume | Why it's a trap |
|---|---|---|
| `day ai` | 201,000 | 94% of the CSV's total volume. Almost certainly a broad-match/mismatched query bucket. **Exclude entirely; add `-day` as a shared negative keyword.** |
| `2 software`, `for you ai`, `back ai`, `ai low` | 10 each | Fragments, no coherent intent. Exclude. |
| `ai download*`, `*download free`, `app ai free`, `free software ai`, `no code ai free` | ~230 combined | Freebie-seeker intent, not a buyer of a paid service. If tested, isolate with a hard budget cap, never mix with commercial ad groups. |

**Net usable volume after cleaning: ~12,700–13,000/month**, not 214,280. All bid and budget figures below are built on the cleaned number.

### 3.2–3.3. Keyword clusters and expansion terms

*(Full cluster tables retained from the original research pass — restated compactly here; see §4 for the exact ad-group build.)*

- **Cluster A — Tool-specific:** `bolt ai` (1,300), `ai coding` (1,600), `ai to code` (1,600), `ai for coding` (1,000)
- **Cluster B — Build/production intent:** `make a ai` (480), `build ai` (260), `ai development` (260), `dev ai` (260), `build app with ai` (40), `build an app with ai` (30), `ai prototype` (20), `develop ai software` (70)
- **Cluster C — Security/trust:** `ai secure` (140), `security ai` (50), + ~20 low-volume security/privacy variants (~430/month combined)
- **Cluster D — SaaS/product framing:** `ai saas` (50), `saas ai` (30), `ai saas platform` (10), `ai saas products` (10)
- **Cluster E — Generic/ambiguous (test cautiously):** `user ai` (1,900), `ai assist` (1,600), `ai websites` (720), `ai works` (90), `ai native` (110), `ai database` (110)
- **Expansion — Tool-brand:** `lovable to production`, `lovable security`, `lovable backend`, `bolt.new deploy`, `bolt.new production`, `bolt.new security`, `cursor app deployment`, `cursor to production`, `v0 to production`, `v0 vercel backend`, `replit deployment security`, `vibe coding to production`, `vibe coding security`
- **Expansion — Problem-based:** `is my ai app secure`, `ai generated code security risk`, `ai app security audit`, `lovable app hacked`, `exposed api keys frontend`, `ai prototype not production ready`, `freelancer doesn't understand ai code`, `ai code review service`
- **Expansion — Comparison:** `launchstudio review`, `launchstudio vs`, `ai app developer netherlands`, `ai app agency vs freelancer`, `hire developer for ai prototype`
- **Expansion — Dutch:** `AI app laten bouwen`, `AI prototype beveiligen`, `software developer inhuren`, `AI applicatie live zetten`, `vibe coding productie klaar`, `app ontwikkelaar inhuren`, `AI SaaS laten maken`, `beveiligingsaudit AI code`, `Lovable app naar productie`
- **Expansion — Local (top 10 cities to start, expand to the full 60-city `extra-5` list later):** Amsterdam, Rotterdam, Utrecht, Den Haag, Eindhoven, Groningen, Tilburg, Breda, Nijmegen, Enschede — paired with `software ontwikkelaar [city]`, `AI app bouwen [city]`, `app developer [city]`

---

## 4. Google Ads — Search: Exact Campaign & Ad Group Build

**Account structure convention:** `LaunchStudio – Search – [Language] – [Cluster Name]`. One conversion action per campaign minimum; shared negative keyword list applied account-wide (§4.6).

### 4.1. Campaign: `LS-Search-EN-ToolIntent` (Cluster A)

| Ad group | Keywords (match type) | Suggested Max CPC | Daily budget |
|---|---|---|---|
| `AG-BoltAI` | `[bolt ai]`, `"bolt.new production"`, `"bolt.new deploy"`, `"bolt.new security"` | €3.50 | €15 |
| `AG-AICoding` | `[ai coding]`, `[ai to code]`, `"ai for coding"`, `"vibe coding to production"`, `"vibe coding security"` | €4.00 | €20 |
| `AG-ToolBrands` | `"lovable to production"`, `"lovable security"`, `"lovable backend"`, `"cursor app deployment"`, `"cursor to production"`, `"v0 to production"`, `"v0 vercel backend"`, `"replit deployment security"` | €3.00 | €10 |

**Campaign daily budget: €45** (~€1,350/month)

### 4.2. Campaign: `LS-Search-EN-ProductionIntent` (Cluster B)

| Ad group | Keywords (match type) | Suggested Max CPC | Daily budget |
|---|---|---|---|
| `AG-BuildWithAI` | `[build app with ai]`, `"build an app with ai"`, `"build ai"`, `"make a ai"` | €5.50 | €20 |
| `AG-PrototypeToProd` | `"ai prototype"`, `"ai prototype not production ready"`, `"ai development"`, `"develop ai software"` | €3.50 | €12 |
| `AG-FreelancerPain` | `"freelancer doesn't understand ai code"`, `"ai code review service"` | €4.00 | €8 |

**Campaign daily budget: €40** (~€1,200/month)

### 4.3. Campaign: `LS-Search-EN-SecurityIntent` (Cluster C — highest-value cluster)

| Ad group | Keywords (match type) | Suggested Max CPC | Daily budget |
|---|---|---|---|
| `AG-SecureCore` | `[ai secure]`, `"security ai"` | €8.00 | €20 |
| `AG-SecurityLongtail` | Phrase match on the ~20 zero/low-volume security variants (`"ai security issues"`, `"ai security risk"`, `"ai vulnerabilities"`, `"ai data security"`, `"ai privacy issues"`, etc.) | €5.00 | €10 |
| `AG-SecurityProblemAware` | `"is my ai app secure"`, `"ai generated code security risk"`, `"lovable app hacked"`, `"exposed api keys frontend"`, `"ai app security audit"` | €4.50 | €10 |

**Campaign daily budget: €40** (~€1,200/month)

### 4.4. Campaign: `LS-Search-EN-SaaSFraming` (Cluster D)

| Ad group | Keywords | Max CPC | Daily budget |
|---|---|---|---|
| `AG-AISaaS` | `"ai saas"`, `"saas ai"`, `"ai saas platform"`, `"ai saas products"` | €4.00 | €5 |

### 4.5. Campaign: `LS-Search-EN-Comparison` (Decision stage)

| Ad group | Keywords | Max CPC | Daily budget |
|---|---|---|---|
| `AG-Branded` | `[launchstudio]`, `"launchstudio review"`, `"launchstudio vs"` | €2.50 | €3 |
| `AG-Comparison` | `"ai app developer netherlands"`, `"ai app agency vs freelancer"`, `"hire developer for ai prototype"` | €5.00 | €5 |

### 4.6. Campaign: `LS-Search-EN-GenericTest` (Cluster E — hard-capped exploratory)

| Ad group | Keywords | Max CPC | Daily budget |
|---|---|---|---|
| `AG-GenericTerms` | `"user ai"`, `"ai assist"`, `"ai websites"`, `"ai works"`, `"ai native"`, `"ai database"` | €2.00 | €10 (hard cap — do not raise until conversion rate proves out) |

### 4.7. Campaign: `LS-Search-NL-Core` (Dutch — the biggest untapped opportunity)

| Ad group | Keywords | Max CPC | Daily budget |
|---|---|---|---|
| `AG-AIAppBouwen` | `"AI app laten bouwen"`, `"app ontwikkelaar inhuren"`, `"software developer inhuren"`, `"AI applicatie live zetten"` | €3.00 | €15 |
| `AG-AIBeveiliging` | `"AI prototype beveiligen"`, `"beveiligingsaudit AI code"` | €3.50 | €10 |
| `AG-VibeCodingNL` | `"vibe coding productie klaar"`, `"Lovable app naar productie"`, `"AI prototype naar klanten"` | €2.50 | €5 |
| `AG-AISaaSNL` | `"AI SaaS laten maken"` | €3.00 | €3 |

**Campaign daily budget: €33** (~€1,000/month)

### 4.8. Campaign: `LS-Search-NL-Local` (Geo layer, top 10 cities)

One ad group per city cluster (group 2–3 cities per ad group to keep volume workable), location targeting set to a 10km radius around each city, keywords: `"software ontwikkelaar [stad]"`, `"AI app bouwen [stad]"`, `"app developer [stad]"`. Start with Amsterdam, Rotterdam, Utrecht, Den Haag, Eindhoven as the first 5 (highest business density); add Groningen, Tilburg, Breda, Nijmegen, Enschede in week 4 if the first 5 show signal.

**Campaign daily budget: €8** (~€240/month) — this is a long-tail brand-halo play, not a volume driver; keep it cheap.

### 4.9. Account-wide shared negative keyword list

`day`, `free`, `download`, `torrent`, `crack`, `jobs`, `salary`, `course`, `tutorial`, `definition`, `meaning`, `wikipedia`, `pdf`, `template`, `openai`, `chatgpt`, `internship`, `hiring` (as a standalone term). Apply at the shared-library level so it's inherited by every campaign automatically, including new ones added later.

**Total Google Search monthly budget: ~€5,040** — see §9 for how this fits the overall channel mix at each budget tier (the figures above assume Tier 2 EN+NL combined; scale proportionally per §9).

---

## 5. Google Ads Copy — Ready-to-Paste RSAs

### 5.1. RSA for `AG-BuildWithAI` / `AG-PrototypeToProd` (Cluster B, English)

**Headlines (15, ≤30 characters):**
1. From AI Prototype to Live
2. Ship Your Lovable App Fast
3. €800–€7,500 Fixed Price
4. 1–3 Weeks, Not Months
5. Keep Your Frontend As-Is
6. We Fix Only What's Broken
7. Backed by Manifera, 11+ Yrs
8. 80% of AI Apps Never Launch
9. Talk to a Real Engineer
10. Free Project Cost Estimate
11. Built With Bolt or Cursor?
12. Launch-Ready in Days
13. No Rebuild, Just Fixes
14. Trusted by Vodafone, TNO
15. Get Your Free Launch Plan

**Descriptions (4, ≤90 characters):**
1. Turn your AI-built prototype into a secure, production-ready app in 1–3 weeks.
2. Fixed price from €800. No rebuild — we keep your Lovable, Bolt, or Cursor frontend.
3. Backed by Manifera's 11+ years of engineering. 160+ projects delivered globally.
4. Security, payments, hosting, database — all handled. You focus on your users.

**Sitelinks:** Price Calculator (`#calculator`) · Packages (`#packages`) · How It Works (`#process`) · Book a Call (`#contact`)
**Callouts:** Fixed Price · 1–3 Week Delivery · Code Ownership Stays With You · Backed by Manifera

### 5.2. RSA for `AG-SecureCore` / `AG-SecurityProblemAware` (Cluster C, English)

**Headlines (15):**
1. Is Your AI Code Secure?
2. 45% of AI Code Has Bugs
3. Free Security Audit Quote
4. AI Code Security Experts
5. Close the Gaps AI Missed
6. Security Review in Days
7. Don't Ship Vulnerable Code
8. Backed by Manifera Since '14
9. Trusted by TNO & Vodafone
10. Fix Security, Not Rebuild
11. AI-Generated ≠ Secure
12. Get a Real Security Review
13. Protect Your User Data Now
14. Talk to a Security Engineer
15. Launch With Confidence

**Descriptions (4):**
1. Nearly half of AI-generated code has security vulnerabilities. Get yours reviewed.
2. Manifera's engineers audit and fix your AI-built app's security gaps. Fast.
3. Fixed-price security review from €800. Results in days, not weeks.
4. Protect user data, secure your APIs, and launch with real confidence.

### 5.3. RSA for `LS-Search-NL-Core` (Dutch)

**Headlines (15, ≤30 tekens):**
1. Van AI-Prototype naar Live
2. Vaste Prijs Vanaf €800
3. Live Binnen 1–3 Weken
4. Behoud Je Eigen Frontend
5. Wij Fixen Alleen Wat Nodig Is
6. Ondersteund Door Manifera
7. 80% Haalt Productie Nooit
8. Praat Met Een Engineer
9. Gratis Prijsindicatie
10. Gebouwd Met Bolt of Cursor?
11. Snel Live, Geen Gedoe
12. Geen Rebuild, Alleen Fixes
13. Vertrouwd Door Vodafone
14. Vraag Je Lanceerplan Aan
15. Beveiliging Inbegrepen

**Descriptions (4, ≤90 tekens):**
1. Maak van je AI-prototype een veilige, productieklare app. Binnen 1–3 weken live.
2. Vaste prijs vanaf €800. Geen rebuild — we behouden je Lovable, Bolt of Cursor code.
3. Ondersteund door 11+ jaar engineering-ervaring van Manifera. 160+ projecten.
4. Beveiliging, betalingen, hosting, database — allemaal geregeld. Jij focust op groei.

---

## 6. LinkedIn Ads — Exact Campaign Build

**Campaign Group:** `LaunchStudio – Founder Acquisition NL/Benelux`

### 6.1. Campaign 1 — `LI-Awareness-SponsoredContent`
- **Objective:** Website visits
- **Audience — Job titles (OR):** Founder, Co-Founder, Chief Executive Officer, Chief Technology Officer, Head of Product, Solo Founder
- **Company size:** Self-employed, 1–10, 11–50
- **Geography:** Netherlands (primary, 70% of budget), Belgium + Luxembourg (secondary, 20%), broader EU (tertiary, 10%)
- **Interest/skills layer (if inventory allows):** Startups, SaaS, Software Development, No-code Development
- **Bid strategy:** Maximum Delivery for first 2 weeks (need volume to learn), switch to Cost Cap once 50+ clicks recorded
- **Budget:** €30/day (~€900/month)
- **Creative:** Single-image or carousel ad — "5 Signs Your AI Prototype Isn't Production-Ready" → links to the production-readiness checklist landing page
- **Ad copy:** "You built it with Lovable, Bolt, or Cursor in a weekend. Here's what most founders miss before real users show up. Free checklist inside." + CTA button "Learn More"

### 6.2. Campaign 2 — `LI-Retargeting-Consideration` (activate once LinkedIn Insight Tag has 500+ tagged visitors)
- **Objective:** Conversions (Lead Gen Form or website conversion)
- **Audience:** Website retargeting, 30/60/90-day windows, layered with the same job-title filter as Campaign 1
- **Budget:** €15/day (~€450/month)
- **Creative:** Case-study carousel (real result numbers, anonymized if needed) + a direct testimonial-quote static ad
- **Ad copy:** "€2,800 and 9 days. That's what it took [Case Study Founder] to go from Lovable prototype to paying customers." + CTA "Get Your Free Estimate"

### 6.3. Campaign 3 — `LI-MessageAds` (Phase 2, once a warm engaged audience exists — do not launch before week 7)
- **Audience:** Engaged with Campaigns 1–2 (opened, clicked, or watched >50% of video) but not converted
- **Format:** Message Ads / Conversation Ads
- **Copy:** Short, first-person, from a named LaunchStudio team member — not corporate. "Hi {{firstName}}, saw you checked out our production-readiness guide. Want a free 15-min review of your actual prototype? No pitch, just a second opinion." + CTA "Book 15 Min"
- **Budget:** €10/day (~€300/month)

**Total LinkedIn monthly budget: ~€1,650** (Phase 1: Campaigns 1 only, ~€900/month; Phase 2 adds Campaigns 2–3)

---

## 7. Meta Ads (Facebook + Instagram) — Exact Campaign Build

*Do not launch before week 7 — needs pixel data from Search to build retargeting/lookalike audiences (§10).*

### 7.1. Campaign 1 — `META-Prospecting`
- **Objective:** Traffic or Leads (test both, pick winner after 2 weeks)
- **Ad set — Interest stack:** SaaS founders, Indie hackers, Startup entrepreneurship, Y Combinator (interest), No-code development
- **Age:** 24–48 · **Geography:** Netherlands, Belgium, broader EU
- **Placements:** Instagram Reels + Facebook Feed (turn off Audience Network and Messenger placements initially — lower quality for this offer)
- **Creative:** 15-second vertical video, real before/after screen recording — messy Lovable prototype → live production app with a payment flow working
- **Budget:** €20/day (~€600/month)

### 7.2. Campaign 2 — `META-Retargeting`
- **Objective:** Conversions
- **Ad set 1 (priority):** Calculator users who didn't submit, last 14 days
- **Ad set 2:** All website visitors, last 30 days, excluding Ad set 1
- **Creative:** Dynamic carousel — Launch Ready package (€800–3,500) vs. Launch & Grow package (€2,500–7,500), with the specific service the visitor viewed shown first
- **Budget:** €25/day (~€750/month)

### 7.3. Campaign 3 — `META-Lookalike` (Phase 3, once 100+ conversions exist)
- **Ad set:** 1% Lookalike (Netherlands) seeded from converted-customer Custom Audience, layered with SaaS/startup interest
- **Creative:** Testimonial video ad
- **Budget:** €15/day (~€450/month)

**Total Meta monthly budget: ~€1,800** (activate progressively, not all at once)

---

## 8. X (Twitter), Reddit, and Bing — Exact Build

### 8.1. X (Twitter) Ads
- **Campaign objective:** Website clicks
- **Targeting:** Follower look-alike off the official Lovable, Bolt.new, Cursor, and v0/Vercel accounts (verify exact handles before launch — these change), plus keyword targeting on tweets containing "lovable" / "bolt.new" / "cursor ai" combined with "security" / "backend" / "deploy" / "production"
- **Budget:** €10/day (~€300/month)
- **Ready-to-post copy (3 variants, rotate weekly):**
  1. "80% of AI-built apps never make it to production. We fix the last 20% — security, payments, hosting. Fixed price, 1–3 weeks. [link]"
  2. "You vibe-coded a whole app in a weekend. Respect. Now let's make sure it doesn't leak your users' data. [link]"
  3. "Lovable/Bolt/Cursor got you 80% there. We handle the boring-but-critical last mile. [link]"

### 8.2. Reddit Ads
- **Subreddits:** r/lovable, r/nocode, r/SaaS, r/startups, r/webdev, r/EntrepreneurRideAlong
- **Format:** Text/link ads styled as a native post, not a banner
- **Budget:** €8/day (~€240/month)
- **Ready-to-post copy (2 variants):**
  1. Title: "Built my SaaS with Bolt in a weekend — here's what broke when real users showed up" → links to a real (or anonymized composite) case-study blog post, not directly to a sales page
  2. Title: "PSA: if you vibe-coded your app, check these 5 things before launch" → links to the production-readiness checklist

### 8.3. Microsoft (Bing) Ads
- **Action:** Import the full `LS-Search-EN-*` and `LS-Search-NL-*` campaign structure 1:1 using Bing's Google Ads import tool. Do not rebuild manually.
- **Adjustments after import:** add `torrent` and `crack` to Bing's negative list separately (import doesn't always carry negatives cleanly — verify), reduce all Max CPCs by ~30% as a starting point (Bing inventory is typically cheaper).
- **Budget:** €17/day (~€500/month)

---

## 9. Budget Tiers — Concrete Euro Figures

### Tier 1 — Lean (€2,500/month)
| Channel | Monthly € | Daily € |
|---|---|---|
| Google Search EN | €1,000 | €33 |
| Google Search NL | €500 | €17 |
| LinkedIn (Campaign 1 only) | €625 | €21 |
| Bing | €250 | €8 |
| Reddit | €125 | €4 |

### Tier 2 — Standard (€5,000/month) — *this document's default, used for all figures in §4–8*
| Channel | Monthly € |
|---|---|
| Google Search EN (§4.1–4.6) | €3,795 |
| Google Search NL (§4.7–4.8) | €1,240 |
| *(EN+NL Search subtotal, scaled to fit €5k envelope — see note below)* | |
| LinkedIn | €900 (Campaign 1 only in Phase 1) |
| Bing | €500 |
| Reddit | €240 |

> **Note on Tier 2 arithmetic:** §4's ad-group-level daily budgets sum to more than a strict €5,000/month split (~€166/day → ~€5,040/month for Search alone, before LinkedIn/Bing/Reddit). That's intentional: §4's figures are the **target end-state once Phase 1 proves out**, not the day-1 spend. **For an actual Tier 2 (€5,000/month total) launch, start all §4 campaigns at 60% of their listed daily budgets** and raise weekly as data comes in. This avoids the single biggest paid-ads mistake: launching every ad group at full bid on day 1 with zero conversion data.

### Tier 3 — Aggressive (€10,000/month, Phase 2+ scale only)
| Channel | Monthly € |
|---|---|
| Google Search EN+NL | €3,500 |
| LinkedIn (all 3 campaigns) | €2,500 |
| Meta (all 3 campaigns) | €1,800 |
| Bing | €1,000 |
| X | €700 |
| Reddit | €500 |

---

## 10. UTM Convention (enforce from day 1)

```
utm_source   = google | bing | linkedin | meta | twitter | reddit
utm_medium   = cpc
utm_campaign = {cluster}-{lang}-{phase}        e.g. security-en-phase1
utm_content  = {ad-group-or-creative-id}       e.g. rsa-v1, video-15s-v2, msg-ads-v1
utm_term     = {keyword}                       (Google/Bing dynamic keyword insertion only)
```

**Example live URL:**
`https://launchstudio.eu/en/from-prototype-to-production?utm_source=google&utm_medium=cpc&utm_campaign=production-en-phase1&utm_content=rsa-v1&utm_term={keyword}`

Keep a single shared UTM tracking sheet (or use each platform's built-in UTM builder) so campaign names in the ad platform and `utm_campaign` values always match exactly — mismatches here are the #1 cause of broken attribution reporting later.

---

## 11. Landing Pages — Content Outline (build these 3 before spending a single euro)

### 11.1. `/en/from-prototype-to-production` (Cluster B + A traffic)
- **H1:** Your AI Prototype Is 80% Done. We Handle the Other 20%.
- **Subhead:** Security, payments, database, hosting — fixed price, 1–3 weeks, your frontend untouched.
- **Section — The 6 things every AI prototype is missing:** (short list: auth hardening, payment integration, database persistence, hosting/deployment, secrets management, rate limiting)
- **Section — How it works:** 3 steps (describe → 15-min call → we build, you launch)
- **Section — Pricing snapshot:** €800–€7,500, link to full calculator
- **Section — Case study / testimonial** (rotate per traffic source via URL parameter if feasible)
- **Section — FAQ:** 5 Q&A pulled from the site's existing FAQ bank, not duplicated from a blog article
- **CTA (repeated top + bottom):** "Get Your Free Project Estimate" → `#calculator`

### 11.2. `/en/ai-code-security-audit` (Cluster C traffic)
- **H1:** 45% of AI-Generated Code Has Security Vulnerabilities. Is Yours One of Them?
- **Subhead:** A fixed-price security review of your AI-built app, done in days.
- **Section — What we check:** auth, RLS, API key exposure, rate limiting, input validation
- **Section — Real vulnerability patterns we've found** (anonymized/composite examples — do not fabricate specific client names here)
- **Section — Pricing** and **CTA:** "Get a Free Security Review Quote"

### 11.3. `/nl/van-prototype-naar-productie` (Dutch mirror of 11.1)
- Same structure as 11.1, **written natively in Dutch, not machine-translated** — reuse the RSA copy tone from §5.3 as the voice reference.

---

## 12. KPIs (unchanged targets, now tied to the concrete budget above)

| Metric | Phase 1 target | Notes |
|---|---|---|
| Cost per qualified lead | Baseline weeks 1–2, optimize from week 3 | Don't judge week 1 |
| Search impression share (Cluster A/B) | >60% by week 6 | Below this, raise bids toward the §4 target figures |
| LinkedIn CPA vs. avg. deal value | CPA <15–20% of avg. project value | Measure by deal size, not CPC |
| Landing page conversion rate | >3% | Below this, fix message match before blaming the channel |

---

## 13. Week-by-Week Execution Checklist (90 Days)

| Week | Concrete tasks |
|---|---|
| **1** | Install GA4 + define conversion events (`calculator_complete`, `contact_form_submit`, `call_booked`). Install Google Ads conversion tag, LinkedIn Insight Tag, Meta Pixel (+ Conversions API), X Pixel, Reddit Pixel. Build landing pages 11.1 and 11.2. Set up shared negative keyword list (§4.9). |
| **2** | Build all `LS-Search-EN-*` campaigns per §4.1–4.6 at 60% of listed daily budgets. Build `LS-Search-NL-*` (§4.7) — get Dutch copy reviewed by a native speaker first. Launch LinkedIn Campaign 1 (§6.1). Do NOT launch Meta/X/PMax yet. |
| **3** | Daily bid monitoring. First search-term report pull — add any new negative keywords found. Build and QA landing page 11.3 (Dutch). |
| **4** | Launch `LS-Search-NL-Local` (§4.8) with first 5 cities. Weekly search-term cleanup becomes a standing task from here on. |
| **5** | Raise daily budgets on any ad group with CPA below target toward the full §4 figures. Pause/restructure any ad group with zero conversions and >€150 spent. |
| **6** | Launch Bing import (§8.3). Launch Reddit test (§8.2). |
| **7** | **Phase 1 review.** Compare actual CPA/CPL per campaign against §12 targets. Kill or restructure underperformers. Confirm LinkedIn pixel has 500+ tagged visitors — if yes, launch `LI-Retargeting-Consideration` (§6.2). Confirm Meta Pixel has enough signal — if yes, launch `META-Retargeting` (§7.2) only (not prospecting yet). |
| **8–9** | Monitor Meta retargeting CPA. If healthy, add `META-Prospecting` (§7.1). Launch X test (§8.1). |
| **10** | First full monthly cross-channel report — cost per qualified lead by channel, not just by click. Reallocate budget toward whichever channel is winning on CPA, following the Tier 2→3 direction in §9. |
| **11** | If conversions total 100+, seed `META-Lookalike` (§7.3) and consider `LI-MessageAds` (§6.3) if LinkedIn CPA has held. |
| **12–13** | Second full monthly review. Decide on Performance Max test — only if the retargeting list has 1,000+ visitors from the last 30 days (PMax needs this minimum signal to perform; launching earlier wastes budget on cold learning). |

---

## 14. Risks & Notes

- **Volume overstatement risk:** the CSV's "214,280/month" headline is 94% one mismatched term (§3.1). All figures in this document use the cleaned ~13,000/month base.
- **Dutch-language gap:** still the single highest-leverage gap. Before scaling §4.7–4.8 beyond Tier 2 budget, commission a proper Dutch-native keyword research pass (not a translation of the English list) to catch phrasing native speakers actually search for.
- **Day-1 discipline:** the single most common way this kind of plan fails in practice is launching every campaign at its full target budget on day 1. Follow §13 — start at 60%, raise weekly based on data, not all at once based on optimism.
- **Attribution:** with 6 channels running by week 9, set up a data-driven or position-based attribution model in GA4 as soon as volume supports it (typically 300+ conversions/month) — last-click will structurally undercredit X and Reddit, which do awareness work that converts later through Search or direct.
