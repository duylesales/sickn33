# 🎯 Google Search Ads — Three AI Brand Plan
## Lovable · Bolt · Replit → launchstudio.eu

> **Scope:** Google Search only, three AI tool brand names only. This is a **third-party brand targeting plan** — different rules apply than for ordinary keywords.
> **Date:** 2026-09-25 · **Markets:** EU-EN (primary) + NL/BE (secondary — see §2.2)
> **Keywords:** 157 terms — 85 English (8 ad groups) + 72 Dutch (10 ad groups). Listed in full with measured volume in §2.3, §5.1, §6.2, §7.2 and §8.2.
> **This document is self-contained.** Every figure, negative list and argument you need is inside it; no other file is required.

> 🇳🇱 **A note on Dutch keywords.** Dutch search terms are kept in their original form throughout, because that is what people actually type and what you will paste into Google Ads. An English gloss follows each one in parentheses the first time it appears in a section. Do not translate these terms when entering them into Google Ads.

---

> # 🔴 WARNING — THIS PLAN NOW HAS REAL VOLUME DATA (2026-09-25)
>
> Keyword Planner has been run against all 157 keywords. The results **contradict most of this plan's assumptions**:
>
> - **The core thesis — "finish my unfinished AI prototype" — draws 10 searches/month** across 27 keywords; 26 of the 27 are zero
> - **106 of 157 keywords (68%) have zero volume**; 4 of 18 ad groups are completely dead
> - **Budget is allocated backwards**: the EN branch is given €550 but can only spend €143; the NL branch is given €300 but could absorb €724
> - The claim in §7.3 that `N2-NL-AI-Tools` is "the cheapest asset in the account" **is wrong** — that campaign has 10 searches/month
>
> **Read §2 before using any budget figure in this document.**
> The campaign structure, negative lists, RSA copy and trademark rules here remain valid. The budgets and priority order do not.

---

## 📑 Table of contents

| § | Contents |
|---|---|
| [1](#1) | Read first: four risks specific to this plan |
| [2](#2) | **Real volume data — and what follows from it** |
| [3](#3) | Trademark risk & brand-name collision risk |
| [4](#4) | Architecture: seven separate campaigns, never merged |
| [5](#5) | B1 · Lovable |
| [6](#6) | B2 · Bolt — the most dangerous campaign |
| [7](#7) | B3 · Replit — the cleanest campaign |
| [8](#8) | **N1–N4 · Four Dutch-language campaigns** |
| [9](#9) | Negative keywords per brand |
| [10](#10) | Landing pages |
| [11](#11) | Budget & rollout |
| [12](#12) | KPIs & kill thresholds |
| [13](#13) | Pre-launch checklist |

---

<a id="1"></a>
## 1. Read first: four risks specific to this plan

This plan differs from every previous one because **every keyword is another company's brand name**. Four things must be handled before budget is even discussed.

### ⚠️ Risk 1 — In the Netherlands, "Bolt" is a taxi company, not a coding tool

**Bolt is the second-largest ride-hailing brand in the Netherlands**, operating in Amsterdam, Rotterdam, The Hague and Utrecht. A Dutch person typing "bolt" is almost certainly looking for the taxi app.

On top of that, `bolt` also means: a bolt/screw · Usain Bolt · a lightning bolt · Bolt Threads (biomaterials) · Bolt electric scooters.

➡️ **Consequence:** `bolt ai` = 1,300 searches/month (Keyword Planner, 2026-06-15) was once the highest verified volume figure in the entire research effort — but it has to be assumed heavily contaminated by taxi queries. The latest measurement (§2) shows the whole B2-Bolt campaign down to **120 searches/month** once keywords carry `new` — meaning **roughly 90% of "bolt" volume is noise**, exactly as originally suspected.

### ⚠️ Risk 2 — Using brand names in ad copy is restricted

Under Google Ads trademark policy:

| | Permitted? |
|---|---|
| Using a trademark as a **keyword** | ✅ Google does **not** restrict this |
| Using a trademark in **ad text** | ⚠️ Restricted for **direct competitors**, or where use is **confusing/misleading** |
| Using a trademark in the **display URL** (second-level domain) | ✅ Not restricted |

**LaunchStudio's position is more favourable than the usual case:** LaunchStudio is **not a competitor** of Lovable/Bolt/Replit — it is a complementary service that helps those tools' own users get to production. That is a far safer position than bidding on a competitor's name.

The "confusing or misleading" condition still applies, however. Ads **must not imply an official partnership**. See §3.1 for how to handle this.

### ⚠️ Risk 3 — Keyword density across the three brands is heavily skewed

Inventory of keywords already held:

| Brand | Existing keywords | Ads-suitable |
|---|---:|---:|
| Lovable | 123 | 31 |
| Bolt | 7 | 2 |
| Replit | 7 | 2 |

➡️ Bolt and Replit were almost entirely unexploited. This plan brings the set to **85 keywords** with a more even split (Lovable 32 · Bolt 24 · Replit 29). The real volume gap between the three brands has since been measured — see §2.

### ⚠️ Risk 4 — Keyword language must match ad language

The first version of this plan made an error: English keywords paired with bilingual English/Dutch ad copy. **Dutch ads attached to English keywords are almost never served**, and Dutch speakers typing Dutch match no English keyword at all. Half the money went into a half that could never run.

Fixed by splitting into two campaign groups:

| Group | Keywords | Ads | Campaign language | Geo |
|---|---|---|---|---|
| **B1–B3** (§5–§7) | English, 85 kw | **English only** | English | EU-EN + NL (Dutch speakers still type technical errors in English) |
| **N1–N4** (§8) | Dutch, 72 kw | **Dutch only** | Dutch | Netherlands |

The Dutch set is **not a translation** of the English one — the intent distribution is entirely different. Full reasoning in §8.1.

---

<a id="2"></a>
## 2. Real volume data — and what follows from it

> Keyword Planner has been run against all 157 keywords (2026-09-25). Every number in this section is measured, not estimated.

### 2.1. Conclusion first, detail after

**The core thesis of the service — "finish my unfinished AI prototype" — has almost no search demand.**

27 keywords expressing exactly this idea (`afmaken` — *to finish*, `to production`, `naar productie` — *to production*, `production ready`, `live zetten` — *to put live*, `finish`, `preview vs production`) draw **10 searches/month in total**. 26 of 27 are zero. The only non-zero term is `replit agent stuck` = 10.

```
take my lovable app to production = 0      app laten afmaken             = 0
lovable app production ready      = 0      prototype laten afmaken       = 0
finish my lovable app             = 0      onafgemaakte app afmaken      = 0
lovable preview vs production     = 0      ai app laten afmaken          = 0
bolt new to production            = 0      ai gebouwde app laten afmaken = 0
bolt new app production ready     = 0      ai prototype naar productie   = 0
bolt new preview vs production    = 0      van prototype naar productie  = 0
replit app to production          = 0      app productieklaar maken      = 0
replit production ready           = 0      prototype niet live krijgen   = 0
lovable app laten afmaken         = 0      no code app laten afmaken     = 0
lovable app live zetten           = 0      bolt new app laten afmaken    = 0
replit app laten afmaken          = 0      bolt new app live zetten      = 0
replit app live zetten            = 0      app afmaken freelancer        = 0
```

> 🇳🇱 **Dutch terms above, glossed:** `app laten afmaken` (have an app finished) · `prototype laten afmaken` (have a prototype finished) · `onafgemaakte app afmaken` (finish an unfinished app) · `ai app laten afmaken` (have an AI app finished) · `ai gebouwde app laten afmaken` (have an AI-built app finished) · `ai prototype naar productie` (AI prototype to production) · `van prototype naar productie` (from prototype to production) · `app productieklaar maken` (make an app production-ready) · `prototype niet live krijgen` (can't get the prototype live) · `no code app laten afmaken` (have a no-code app finished) · `app afmaken freelancer` (freelancer to finish an app) · `lovable app live zetten` (put a Lovable app live)

| | Keywords | Searches/month |
|---|---:|---:|
| Thesis: "finish my AI prototype" | 27 | **10** |
| General demand: "build me a new app" | 12 | **1,170** |

People are not searching for a way to finish something half-done. They are searching for someone to build something new.

The same idea was written six different ways, in two languages, with and without brand names. All of it returned zero. **This is a finding about the market, not about the keyword list.**

### 2.2. The overall picture

| | Keywords | Searches/month | Kw = 0 |
|---|---:|---:|---:|
| EN branch (B1–B3) | 85 | 530 | 52 (61%) |
| NL branch (N1–N4) | 72 | 1,340 | 54 (75%) |
| **Total** | **157** | **1,870** | **106 (68%)** |

**68% of all keywords have zero volume.** In Keyword Planner, zero means fewer than 10 searches per month.

### 2.3. Every keyword with volume > 0

| Volume | Keyword | Campaign |
|---:|---|---|
| **480** | `app laten maken` *(have an app built)* | N1-NL-Service |
| **260** | `webapplicatie laten maken` *(have a web application built)* | N1-NL-Service |
| **210** | `replit agency` | B3-Replit |
| **140** | `app laten bouwen` *(have an app built — "bouwen" variant)* | N1-NL-Service |
| **110** | `software laten maken` *(have software built)* | N1-NL-Service |
| **90** | `maatwerk software laten maken` *(have custom software built)* | N1-NL-Service |
| **50** | `mvp laten maken` *(have an MVP built)* | N1-NL-Service |
| **40** | `technische due diligence` *(technical due diligence)* | N3-NL-Security |
| **30** | `mvp ontwikkeling` *(MVP development)* | N1-NL-Service |
| **20** | `developer inhuren app` *(hire a developer for an app)* | N1-NL-Service |
| **20** | `app laten maken rotterdam` *(have an app built, Rotterdam)* | N1-NL-Service |
| **20** | `app laten maken eindhoven` *(have an app built, Eindhoven)* | N1-NL-Service |
| **20** | `app laten maken amsterdam` *(have an app built, Amsterdam)* | N1-NL-Service |
| **10** | `webapp laten bouwen` *(have a web app built)* | N1-NL-Service |
| **10** | `web applicatie laten bouwen` *(have a web application built — spaced spelling)* | N1-NL-Service |
| **10** | `self host lovable app` | B1-Lovable |
| **10** | `replit security` | B3-Replit |
| **10** | `replit not working` | B3-Replit |
| **10** | `replit hosting cost` | B3-Replit |
| **10** | `replit export code` | B3-Replit |
| **10** | `replit deployment cost` | B3-Replit |
| **10** | `replit custom domain` | B3-Replit |
| **10** | `replit agent stuck` | B3-Replit |
| **10** | `replit agent not working` | B3-Replit |
| **10** | `pentest webapplicatie` *(web application pentest)* | N3-NL-Security |
| **10** | `mvp laten ontwikkelen` *(have an MVP developed)* | N1-NL-Service |
| **10** | `lovable to nextjs` | B1-Lovable |
| **10** | `lovable stripe integration` | B1-Lovable |
| **10** | `lovable not working` | B1-Lovable |
| **10** | `lovable freelancer` | B1-Lovable |
| **10** | `lovable export code` | B1-Lovable |
| **10** | `lovable developer` | B1-Lovable |
| **10** | `lovable custom domain not working` | B1-Lovable |
| **10** | `lovable alternative` | B1-Lovable |
| **10** | `is lovable secure` | B1-Lovable |
| **10** | `hire replit developer` | B3-Replit |
| **10** | `hire lovable developer` | B1-Lovable |
| **10** | `bolt new token limit` | B2-Bolt |
| **10** | `bolt new supabase` | B2-Bolt |
| **10** | `bolt new stripe` | B2-Bolt |
| **10** | `bolt new security` | B2-Bolt |
| **10** | `bolt new not working` | B2-Bolt |
| **10** | `bolt new export code` | B2-Bolt |
| **10** | `bolt new environment variables` | B2-Bolt |
| **10** | `bolt new developer` | N2-NL-AI-Tools |
| **10** | `bolt new developer` | B2-Bolt |
| **10** | `bolt new deployment` | B2-Bolt |
| **10** | `bolt new custom domain` | B2-Bolt |
| **10** | `bolt new blank page` | B2-Bolt |
| **10** | `bolt app developer` | B2-Bolt |
| **10** | `app laten maken utrecht` *(have an app built, Utrecht)* | N1-NL-Service |

Nine of the ten highest-volume terms belong to **a single campaign**: N1-NL-Service. And every one of them expresses "build me a new app", not "finish my old app".

> ⚠️ **`replit agency` = 210 is an anomalous figure.** It is unclear what this query means — it may be people looking for Replit's own agency programme rather than for an app-repair service. Run it on Exact match separately and read the Search Terms Report for a week before trusting the number.

### 2.4. The plan's budget is backwards

Spend ceiling calculated as `Volume × 1.8 (phrase match expansion) × 60% IS × 5% CTR × CPC`:

| Campaign | Kw | Volume | Kw=0 | Plan allocates | Real ceiling | Difference |
|---|---:|---:|---:|---:|---:|---:|
| B1-Lovable | 32 | 110 | 21 | €250 | **€30** | −€220 |
| B2-Bolt | 24 | 120 | 12 | €120 | **€32** | −€88 |
| B3-Replit | 29 | 300 | 19 | €180 | **€81** | −€99 |
| N1-NL-Service | 26 | 1,280 | 11 | €150 | **€691** | **+€541** |
| N2-NL-AI-Tools | 24 | 10 | 23 | €60 | **€5** | −€55 |
| N3-NL-Security | 12 | 50 | 10 | €60 | **€27** | −€33 |
| N4-NL-Payments | 10 | 0 | 10 | €30 | **€0** | −€30 |

| Branch | Plan allocates | Real ceiling |
|---|---:|---:|
| EN (B1–B3) | €550 | **€143** |
| NL (N1–N4) | €300 | **€724** |

**The plan gives €550 to a branch that can only spend €143, and €300 to a branch that could spend €724.** Exactly inverted.

### 2.5. Four ad groups with no volume at all

| Campaign | Ad group | Kw | Volume |
|---|---|---:|---:|
| N2-NL-AI-Tools | `AG-NL-AI-Afmaken` | 8 | 0 |
| N2-NL-AI-Tools | `AG-NL-Lovable` | 6 | 0 |
| N2-NL-AI-Tools | `AG-NL-Replit` | 6 | 0 |
| N4-NL-Payments | `AG-NL-Payments` | 10 | 0 |

### 2.6. The `evidence` Tier A/B/C method: sound for Dutch, worthless for English

| Set | Tier | Kw | Total volume | Share with volume > 0 | Max |
|---|---|---:|---:|---:|---:|
| **EN** | A | 34 | 120 | 35% | 10 |
| **EN** | B | 34 | 140 | 41% | 10 |
| **EN** | C | 17 | 270 | 41% | 210 |
| **NL** | A | 6 | 810 | 83% | 480 |
| **NL** | B | 17 | 470 | 52% | 260 |
| **NL** | C | 49 | 60 | 8% | 20 |

**Dutch set: the tier scale predicted accurately** — A 83% → B 52% → C 8%, monotonically decreasing.
**English set: the tier scale was worthless** — Tier A (the highest-confidence band) hit *less often* than Tier C, and the highest-volume term in the entire English branch sat in Tier C.

The difference lies in the kind of signal used to assign tiers:

| Set | Signal used | Nature | Result |
|---|---|---|---|
| NL | "Does any agency run a dedicated landing page or ads for this phrase?" | **Demand** signal — someone is paying to appear | ✅ Predicted well |
| EN | "Do Fiverr gigs / discussion threads / articles exist about this phrase?" | **Supply** signal — someone is producing content | ❌ Unrelated to volume |

Content existing does not prove anyone is searching. Paid competition does. From here on, only demand signals.

### 2.7. Economics of the only surviving campaign

N1-NL-Service: 1,280 volume → roughly 69 clicks/month.

| CPC | Spend/month | Scenario | Customers/month | CAC |
|---:|---:|---|---:|---:|
| €8 | €553 | ICP match (LP 5% · close 25%) | 0.86 | **€640** |
| €8 | €553 | ICP mismatch (LP 5% · close 10%) | 0.35 | **€1,600** |
| €10 | €691 | ICP match | 0.86 | **€800** |
| €10 | €691 | ICP mismatch | 0.35 | **€2,000** |
| €14 | €968 | ICP mismatch | 0.35 | **€2,800** |

Against the service packages: **Launch Ready €800–3,500** · **Launch & Grow €2,500–7,500**.

> ⚠️ **The "ICP mismatch" scenario is the default case, not the exception.** 1,080 of N1's 1,280 volume comes from `app laten maken`, `webapplicatie laten maken`, `app laten bouwen` and `software laten maken` — all of them people who want something **built from scratch**. A 25% close rate only holds if the searcher already has a half-finished prototype. They do not.
>
> At a CAC of €1,600–2,000, the €800 package loses money badly. Only Launch & Grow at €2,500–7,500 can absorb it — and that is a hard package to sell to someone arriving from a generic query.

### 2.8. Recommendations

| # | Action | Rationale |
|---|---|---|
| 1 | **Turn off N4-NL-Payments** | Zero volume across all 10 keywords |
| 2 | **Turn off N2-NL-AI-Tools** as a standalone campaign | 10 volume. Fold the 24 keywords into a reserve ad group with no separate budget |
| 3 | **Merge B1 + B2 + B3 into one campaign** `LS-EN-AI-Tools`, budget **€100–140** | 530 volume cannot sustain three campaigns. Three separate budgets only triple the management overhead |
| 4 | **Raise N1-NL-Service to €400–550** | The only campaign with real volume, currently under-funded by €541 |
| 5 | **Keep N3-NL-Security at €40** | `technische due diligence` at 40/month is a high-value query, worth holding even at small scale |
| 6 | **Verify `replit agency` = 210** | Anomalous — see the warning in §2.3 |

**New budget: roughly €540–730/month** instead of €850, allocated the opposite way round from the original plan.

#### The larger decision — this one needs a choice

The problem is not campaign configuration. It is that **Google Search Ads can only capture demand that already exists**, and demand for "finish my AI prototype" does not exist at a measurable level — in either language.

**Option A — Follow the volume.** Run N1-NL-Service into the "build me a new app" market, competing with full-service agencies. The landing page has to convert someone arriving with "I want something built" into "actually, I already have a prototype". There is volume here, but CAC runs €1,600–2,000 and the win has to come from messaging.

**Option B — Don't use Search Ads for this thesis.** Demand that does not exist has to be **created**, not bought: content/SEO, LinkedIn, the communities where Lovable/Bolt/Replit users gather (Discord, r/vibecoding), partnerships. Keep Search Ads at a minimal €100–150/month to catch the handful of genuine queries.

**Recommendation: B as the main channel, A as a controlled test.** Run N1 at €400 for eight weeks with a single decision metric: **the share of leads that already have a prototype**. Below 30%, stop A and put everything into B.

> 💡 The one piece of good news in the dataset: **Dutch-language demand is real and 2.5× the English branch** (1,340 vs 530). Building a Dutch keyword set was the right call. It is simply that the demand sits somewhere other than where the plan was aiming.

### 2.9. Cautions when reading these numbers

- **Zero means < 10/month**, not exactly zero. A term showing 0 may still get 3–8 searches a month.
- **Volume is for the exact phrase.** Phrase match captures more — the 1.8× factor used in §2.4 is an estimate, not yet verified.
- **Figures are rounded to Google's buckets** (10, 20, 30, 50, 90, 110, 140, 210, 260, 480). This is real data rather than a range, but precision only extends to the bucket.
- **CPC is still missing.** Every calculation in §2.7 uses an estimated CPC of €8–14. Re-run Keyword Planner for the `Top of page bid` column to settle this.
- **Accounts with no spend history see ranges** (`10–100`, `100–1K`) rather than precise figures. To unlock precision, run a small campaign for a few days.

---

<a id="3"></a>
## 3. Trademark risk & brand-name collision risk

### 3.1. Three layers of defence for ad copy

Because the whole plan rests on third-party brand names, every ad group needs **two RSA sets ready to go**:

| Set | Content | When to use |
|---|---|---|
| **A — with brand name** | Headlines contain `Lovable` / `Bolt.new` / `Replit` | Default. Markedly higher CTR because it matches the query |
| **B — without brand name** | Replaced with `AI App`, `AI-Built App`, `AI Builder` | Activate **immediately** if Google restricts ad text after a complaint |

**Three rules that apply to all ad text:**

1. **Never imply an official relationship.** Do not use `official`, `partner`, `certified`, `authorized`, `powered by`.
2. **Never use the brand's logo or distinctive characters.**
3. **State independence in at least one headline.** For example `Not Affiliated With Lovable` (27 characters) — this both reduces policy risk and builds reader trust.

> 💡 Rule 3 is slightly counter-intuitive but worth following: saying outright "we are not Lovable's partner" removes exactly what Google's policy is concerned about — confusion.

### 3.2. Brand-name collision risk by brand

| Brand | Noise level | Other meanings | Handling |
|---|---|---|---|
| **Bolt** | 🔴 **Very high** | #2 Dutch taxi company · a bolt/screw · Usain Bolt · lightning bolt · electric scooters · Bolt Threads | **Only bid `bolt.new` / `bolt new`, never bare `bolt`.** Exclude NL/BE from geo in phase 1 |
| **Lovable** | 🟠 High | English adjective · global lingerie brand · song lyrics · pet names | Negative list §9.1. Never use broad match |
| **Replit** | 🟢 **Low** | Virtually no other meaning | Shortest negative list. **This is the cleanest brand to start with** |

➡️ **Key conclusion for rollout order:** do not launch all three at once. Start with **Replit** (cleanest), then **Lovable** (most keywords), and only then **Bolt** (most dangerous). See §11.2.

---

<a id="4"></a>
## 4. Architecture: seven separate campaigns, never merged

### 4.1. Why the campaigns must be split

If the three brands shared one campaign:

1. **Bolt would eat the budget.** `bolt ai` has the highest volume in the dataset — most of it noise. A shared budget means money flowing into taxi queries.
2. **The negative lists are entirely different.** Bolt's negatives (taxi, screws) are meaningless for Replit and vice versa.
3. **Geo differs.** Bolt needs NL/BE excluded; Lovable and Replit do not.
4. **Performance cannot be compared** across the three brands on a shared budget.

### 4.2. Structure

```
LaunchStudio ACCOUNT — three AI brand branch
│
├── B1 · LS-Brand-Lovable            [EU-EN + NL · €250/mo]
│   ├── AG-LOV-Hire      (12 kw) → /en/fix-lovable-app
│   ├── AG-LOV-Problem   (11 kw) → /en/fix-lovable-app
│   └── AG-LOV-Migrate    (9 kw) → /en/lovable-tanstack-migration
│
├── B2 · LS-Brand-Bolt               [EU-EN · NO NL/BE · €120/mo]
│   ├── AG-BOLT-Hire      (8 kw) → /en/fix-bolt-app
│   └── AG-BOLT-Problem  (16 kw) → /en/fix-bolt-app
│
├── B3 · LS-Brand-Replit             [EU-EN + NL · €180/mo]
│   ├── AG-REP-Hire       (7 kw) → /en/fix-replit-app
│   ├── AG-REP-Problem   (12 kw) → /en/fix-replit-app
│   └── AG-REP-Cost      (10 kw) → /en/replit-hosting-costs
│
├── N1 · LS-NL-Service               [NL · Dutch language · €150/mo]
│   ├── AG-NL-MVP         (6 kw) ┐
│   ├── AG-NL-App         (8 kw) ├→ /nl/mvp-laten-afmaken
│   ├── AG-NL-Afmaken     (6 kw) │
│   └── AG-NL-Geo         (6 kw) ┘
│
├── N2 · LS-NL-AI-Tools              [NL · Dutch language · €60/mo]
│   ├── AG-NL-AI-Afmaken  (8 kw) ┐
│   ├── AG-NL-Lovable     (6 kw) ├→ /nl/ai-app-laten-afmaken
│   ├── AG-NL-Bolt        (4 kw) │
│   └── AG-NL-Replit      (6 kw) ┘
│
├── N3 · LS-NL-Security              [NL · Dutch language · €60/mo]
│   └── AG-NL-Security   (12 kw) → /nl/security-audit
│
└── N4 · LS-NL-Payments              [NL · Dutch language · €30/mo]
    └── AG-NL-Payments   (10 kw) → /nl/betalingen-koppelen
```

> 🇳🇱 **Dutch landing page slugs, glossed:** `/nl/mvp-laten-afmaken` (have an MVP finished) · `/nl/ai-app-laten-afmaken` (have an AI app finished) · `/nl/betalingen-koppelen` (connect payments). Keep the slugs in Dutch — they carry keyword relevance for Quality Score.

**Total: €850/month** at full configuration — €550 English branch + €300 Dutch branch.

> ⚠️ **B1–B3 still target Dutch geo, but the campaign language is set to English.** There is no contradiction: a Dutch speaker typing `lovable deployment failed` in English should still see an English ad. Geo and language are two independent settings — and conflating them is exactly what the first version of this plan got wrong.

> 🔴 **These budget figures are superseded.** See §2.4 for measured spend ceilings and §2.8 for the revised allocation.

### 4.3. Settings common to all seven

| Setting | Value | Reason |
|---|---|---|
| Match type | **Phrase** as the default, **Exact** for `[hire X developer]` | Broad match is never used — see §3.2 |
| Bid strategy | **Manual CPC** for the first 8 weeks | Volume is far too low for Smart Bidding |
| Location targeting | **"Presence"**, not "Presence or interest" | "Interest" pulls queries from outside the market |
| Ad rotation | **"Do not optimize"** for the first 4 weeks | To compare RSA sets A and B fairly |
| Ad schedule | All week for the first 4 weeks | Collect data before cutting time slots |
| **Language** | **B1–B3: English · N1–N4: Dutch** | **No campaign selects both** — see Risk 4 |

---

<a id="5"></a>
## 5. B1 · `LS-Brand-Lovable` — €250/month (€8.20/day)

### 5.1. Ad groups & keywords

| Ad group | Main keywords | Max CPC | Daily | Landing page |
|---|---|---:|---:|---|
| `AG-LOV-Hire` (12) | `"fix lovable app"`, `"lovable developer for hire"`, `[hire lovable developer]`, `"lovable developer"`, `"lovable app development service"`, `"take my lovable app to production"`, `"lovable app production ready"`, `"lovable audit service"`, `"lovable security audit"` … | €12.00 | €3.50 | `/en/fix-lovable-app` |
| `AG-LOV-Problem` (11) | `"lovable app not working"`, `"lovable deployment failed"`, `"lovable preview vs production"`, `"lovable custom domain not working"`, `"lovable stripe integration"`, `"lovable login not working"`, `"lovable supabase rls"`, `"is lovable secure"` … | €9.00 | €2.50 | `/en/fix-lovable-app` |
| `AG-LOV-Migrate` (9) | `"migrate off lovable"`, `"lovable migration service"`, `"lovable tanstack migration"`, `"migrate lovable to tanstack"`, `"lovable ssr upgrade"`, `"lovable export code"`, `"self host lovable app"` … | €11.00 | €2.20 | `/en/lovable-tanstack-migration` |

#### Complete keyword list — B1 Lovable

**`AG-LOV-Hire`** — 12 keywords · 30 searches/month · 3 terms with volume > 0

| Keyword | Match | Intent | Priority | Volume |
|---|---|---|---|---:|
| `hire lovable developer` | Exact | Hire | P1 | **10** |
| `lovable developer` | Phrase | Hire | P1 | **10** |
| `lovable freelancer` | Phrase | Hire | P2 | **10** |
| `fix lovable app` | Phrase | Hire | P1 | 0 |
| `lovable developer for hire` | Phrase | Hire | P1 | 0 |
| `lovable app development service` | Phrase | Hire | P1 | 0 |
| `lovable app agency` | Phrase | Hire | P2 | 0 |
| `take my lovable app to production` | Phrase | Hire | P1 | 0 |
| `lovable app production ready` | Phrase | Hire | P1 | 0 |
| `finish my lovable app` | Phrase | Hire | P2 | 0 |
| `lovable audit service` | Phrase | Service | P1 | 0 |
| `lovable security audit` | Phrase | Service | P1 | 0 |

**`AG-LOV-Problem`** — 11 keywords · 40 searches/month · 4 terms with volume > 0

| Keyword | Match | Intent | Priority | Volume |
|---|---|---|---|---:|
| `lovable not working` | Phrase | Fix | P2 | **10** |
| `lovable custom domain not working` | Phrase | Fix | P2 | **10** |
| `lovable stripe integration` | Phrase | Fix | P1 | **10** |
| `is lovable secure` | Phrase | Research | P2 | **10** |
| `lovable app not working` | Phrase | Fix | P2 | 0 |
| `lovable deployment failed` | Phrase | Fix | P2 | 0 |
| `lovable preview vs production` | Phrase | Fix | P2 | 0 |
| `lovable stripe not working` | Phrase | Fix | P1 | 0 |
| `lovable login not working` | Phrase | Fix | P2 | 0 |
| `lovable supabase rls` | Phrase | Security | P2 | 0 |
| `lovable security vulnerabilities` | Phrase | Research | P2 | 0 |

**`AG-LOV-Migrate`** — 9 keywords · 40 searches/month · 4 terms with volume > 0

| Keyword | Match | Intent | Priority | Volume |
|---|---|---|---|---:|
| `lovable export code` | Phrase | How-to | P2 | **10** |
| `self host lovable app` | Phrase | Decision | P2 | **10** |
| `lovable to nextjs` | Phrase | How-to | P2 | **10** |
| `lovable alternative` | Phrase | Decision | P2 | **10** |
| `migrate off lovable` | Phrase | Decision | P1 | 0 |
| `lovable migration service` | Phrase | Service | P1 | 0 |
| `lovable tanstack migration` | Phrase | Service | P1 | 0 |
| `migrate lovable to tanstack` | Phrase | Service | P1 | 0 |
| `lovable ssr upgrade` | Phrase | Service | P1 | 0 |

> 💡 **`AG-LOV-Migrate` — the TanStack opportunity, and why it still matters despite zero volume**
>
> Lovable changed its default stack from **React + Vite → TanStack Start**: default for new projects from **2026-05-13**, Enterprise from **2026-06-22**. Lovable **does not migrate existing projects automatically**. Three consequences create demand:
>
> 1. Every project created before May 2026 still runs the old stack — and its owner usually **does not know that**
> 2. The old stack has no SSR → a direct hit to SEO, a pain many founders have felt without knowing the cause
> 3. Migration is engineering work, not prompting — precisely LaunchStudio's "last-mile" definition
>
> **Commercial validation:** `nextlovable.com` sells a **$199** audit (`/lovable-tanstack-ssr`) and a **$299** one (`/migrate-lovable-tanstack`), plus a `/migration-guide` page. Three landing pages for one problem means they are making money from it.
>
> ⏳ **Time sensitivity:** this window closes once Lovable migrates projects itself or old projects die off. Estimated **6–12 months** remaining.
>
> ⚠️ **But all 9 keywords in this group measured zero volume** (§2.4). The need is technically real, yet users **do not know to search for it** — they are unaware their stack is outdated. This is demand that must be **created with content**, not bought with Search Ads.

### 5.2. RSA — set A (with brand name)

| # | Headline (English) | Ch | Pin |
|---|---|---:|---|
| H1 | `Lovable App Stuck in Preview?` | 29 | **P1** |
| H2 | `We Finish Lovable Builds` | 24 | **P2** |
| H3 | `Security, Stripe & Hosting` | 26 | |
| H4 | `Fixed Price From €800` | 21 | |
| H5 | `Live in 1-3 Weeks` | 17 | |
| H6 | `Your Frontend Stays` | 19 | |
| H7 | `11+ Years Engineering Exp.` | 26 | |
| H8 | `You Own 100% of the Code` | 24 | |
| H9 | `Not Affiliated With Lovable` | 27 | |
| H10 | `Get a Free Code Review` | 22 | **P3** |

| # | Description (English) | Ch |
|---|---|---:|
| D1 | `Built it with Lovable but cannot go live? We fix security, payments and hosting.` | 80 |
| D2 | `Fixed price from €800. Live in 1-3 weeks. Your frontend untouched, code 100% yours.` | 83 |
| D3 | `Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW.` | 73 |

### 5.3. RSA — set B (no brand name, for use if restricted)

| # | Headline (English) | Ch |
|---|---|---:|
| H1 | `AI App Stuck in Preview?` | 24 |
| H2 | `We Finish AI-Built Apps` | 23 |
| H3 | `Security, Stripe & Hosting` | 26 |
| D1 | `Built it with an AI builder but cannot go live? We fix security, payments, hosting.` | 83 |

> Headlines H4–H8, H10 and descriptions D2–D3 from set A **contain no brand name**, so they carry over unchanged into set B.

---

<a id="6"></a>
## 6. B2 · `LS-Brand-Bolt` — €120/month (€4/day) — THE MOST DANGEROUS CAMPAIGN

### 6.1. 🔴 Five mandatory rules

This is the only campaign in the account capable of burning the entire budget in a single day.

1. **Never bid on bare `bolt`.** Only `bolt.new` or `bolt new`.
2. **Exclude NL/BE from geo in phase 1.** Bolt is the #2 Dutch taxi company, operating in exactly LaunchStudio's four target cities: Amsterdam, Rotterdam, The Hague, Utrecht.
3. **The §9.2 negative list must be applied before the campaign runs for one minute.**
4. **Lowest budget of the three campaigns** until the Search Terms Report is clean for two consecutive weeks.
5. **Check Search Terms daily** for the first three weeks — not every second day as with the other campaigns.

### 6.2. Ad groups & keywords

| Ad group | Main keywords | Max CPC | Daily | Landing page |
|---|---|---:|---:|---|
| `AG-BOLT-Hire` (8) | `"fix bolt app"`, `"fix bolt new app"`, `"bolt new developer"`, `[hire bolt new developer]`, `"bolt new to production"`, `"bolt new app production ready"` … | €10.00 | €2.20 | `/en/fix-bolt-app` |
| `AG-BOLT-Problem` (16) | `"bolt new not working"`, `"bolt new preview vs production"`, `"bolt new production error"`, `"bolt new deployment"`, `"bolt new environment variables"`, `"bolt new cors error"`, `"bolt new bundle too large"`, `"bolt new netlify deploy"` … | €8.00 | €1.80 | `/en/fix-bolt-app` |

> ⚠️ **The keyword `"bolt app developer"` is flagged as risky.** It lacks the word "new" and therefore matches queries about the Bolt taxi app easily. Set it to **Exact** or drop it entirely in phase 1.

#### Complete keyword list — B2 Bolt

**`AG-BOLT-Hire`** — 8 keywords · 20 searches/month · 2 terms with volume > 0

| Keyword | Match | Intent | Priority | Volume |
|---|---|---|---|---:|
| `bolt new developer` | Phrase | Hire | P1 | **10** |
| `bolt app developer` | Phrase | Hire | P2 | **10** |
| `fix bolt app` | Phrase | Hire | P1 | 0 |
| `fix bolt new app` | Phrase | Hire | P1 | 0 |
| `hire bolt new developer` | Exact | Hire | P1 | 0 |
| `bolt new to production` | Phrase | Service | P1 | 0 |
| `bolt new app production ready` | Phrase | Service | P1 | 0 |
| `bolt new agency` | Phrase | Hire | P2 | 0 |

**`AG-BOLT-Problem`** — 16 keywords · 100 searches/month · 10 terms with volume > 0

| Keyword | Match | Intent | Priority | Volume |
|---|---|---|---|---:|
| `bolt new not working` | Phrase | Fix | P2 | **10** |
| `bolt new deployment` | Phrase | Fix | P2 | **10** |
| `bolt new environment variables` | Phrase | Fix | P2 | **10** |
| `bolt new supabase` | Phrase | How-to | P3 | **10** |
| `bolt new stripe` | Phrase | How-to | P3 | **10** |
| `bolt new custom domain` | Phrase | Fix | P3 | **10** |
| `bolt new blank page` | Phrase | Fix | P3 | **10** |
| `bolt new export code` | Phrase | How-to | P2 | **10** |
| `bolt new token limit` | Phrase | Cost | P3 | **10** |
| `bolt new security` | Phrase | Security | P2 | **10** |
| `bolt new preview vs production` | Phrase | Fix | P2 | 0 |
| `bolt new production error` | Phrase | Fix | P2 | 0 |
| `bolt new deploy error` | Phrase | Fix | P2 | 0 |
| `bolt new cors error` | Phrase | Fix | P3 | 0 |
| `bolt new bundle too large` | Phrase | Fix | P3 | 0 |
| `bolt new netlify deploy` | Phrase | Fix | P3 | 0 |

### 6.3. Bolt's distinctive sales angle

Bolt.new runs on WebContainer — an in-browser environment. This produces a very characteristic class of failure: **the preview works perfectly, production breaks immediately**. The usual causes are:

- Environment variables held in Bolt's Secrets **do not carry over** to Netlify/Vercel → the build runs with `undefined` values
- All traffic inside WebContainer is same-origin → **CORS errors only appear on a real deployment**
- The bundle exceeds size limits

➡️ Ad copy should say exactly this: *"Preview Works, Live Breaks?"* — anyone with this precise problem will recognise themselves instantly.

### 6.4. RSA — set A (with brand name)

| # | Headline (English) | Ch | Pin |
|---|---|---:|---|
| H1 | `Bolt.new App Not Deploying?` | 27 | **P1** |
| H2 | `Preview Works, Live Breaks?` | 27 | **P2** |
| H3 | `We Fix CORS, Env & Build` | 24 | |
| H4 | `Fixed Price From €800` | 21 | |
| H5 | `Live in 1-3 Weeks` | 17 | |
| H6 | `Your Frontend Stays` | 19 | |
| H7 | `11+ Years Engineering Exp.` | 26 | |
| H8 | `You Own 100% of the Code` | 24 | |
| H9 | `Get a Free Build Review` | 23 | **P3** |

| # | Description (English) | Ch |
|---|---|---:|
| D1 | `Bolt.new preview is not production. We fix env vars, CORS and build failures.` | 77 |
| D2 | `Fixed price from €800. Live in 1-3 weeks. Your frontend untouched, code 100% yours.` | 83 |
| D3 | `Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW.` | 73 |

> 💡 **Write `Bolt.new` with the dot; never bare `Bolt` in ad text.** It reduces confusion with the taxi company and matches tool users' queries more precisely.

---

<a id="7"></a>
## 7. B3 · `LS-Brand-Replit` — €180/month (€5.90/day) — THE CLEANEST CAMPAIGN

### 7.1. Why to start here

- **The name has almost no other meaning** → least noise of the three brands
- **Shortest negative list** → least operational risk
- **One clear commercial pain point the other two lack:** surprise hosting costs

Replit offers three deployment types with different pricing structures — Static, Autoscale (pay-per-use, scaling to zero when idle), and Reserved VM (always on, charged a fixed monthly fee whether or not anyone visits). Reserved VM cost accumulates **quietly** and is a common trigger for users to go looking for alternatives.

➡️ `AG-REP-Cost` targets exactly that moment: someone who has just received a bill and is looking for a way out.

### 7.2. Ad groups & keywords

| Ad group | Main keywords | Max CPC | Daily | Landing page |
|---|---|---:|---:|---|
| `AG-REP-Hire` (7) | `"fix replit app"`, `"replit developer for hire"`, `[hire replit developer]`, `"replit app to production"`, `"replit production ready"` … | €11.00 | €2.00 | `/en/fix-replit-app` |
| `AG-REP-Problem` (12) | `"replit app not working"`, `"replit deployment failed"`, `"replit deployment error"`, `"replit database connection error"`, `"replit agent not working"`, `"replit secrets not working"`, `"replit security"` … | €8.00 | €1.90 | `/en/fix-replit-app` |
| `AG-REP-Cost` (10) | `"replit reserved vm cost"`, `"replit autoscale vs reserved vm"`, `"replit deployment cost"`, `"replit pricing too expensive"`, `"migrate off replit"`, `"replit export to vercel"`, `"move replit app to own server"` … | €10.00 | €2.00 | `/en/replit-hosting-costs` |

#### Complete keyword list — B3 Replit

**`AG-REP-Hire`** — 7 keywords · 220 searches/month · 2 terms with volume > 0

| Keyword | Match | Intent | Priority | Volume |
|---|---|---|---|---:|
| `replit agency` | Phrase | Hire | P2 | **210** |
| `hire replit developer` | Exact | Hire | P1 | **10** |
| `fix replit app` | Phrase | Hire | P1 | 0 |
| `replit developer for hire` | Phrase | Hire | P1 | 0 |
| `replit app to production` | Phrase | Service | P1 | 0 |
| `replit app developer` | Phrase | Hire | P2 | 0 |
| `replit production ready` | Phrase | Service | P1 | 0 |

**`AG-REP-Problem`** — 12 keywords · 50 searches/month · 5 terms with volume > 0

| Keyword | Match | Intent | Priority | Volume |
|---|---|---|---|---:|
| `replit not working` | Phrase | Fix | P3 | **10** |
| `replit agent not working` | Phrase | Fix | P3 | **10** |
| `replit agent stuck` | Phrase | Fix | P3 | **10** |
| `replit custom domain` | Phrase | Fix | P3 | **10** |
| `replit security` | Phrase | Security | P2 | **10** |
| `replit app not working` | Phrase | Fix | P2 | 0 |
| `replit deployment failed` | Phrase | Fix | P2 | 0 |
| `replit deployment error` | Phrase | Fix | P2 | 0 |
| `replit database connection error` | Phrase | Fix | P2 | 0 |
| `replit secrets not working` | Phrase | Fix | P3 | 0 |
| `replit app slow` | Phrase | Fix | P3 | 0 |
| `replit app crashes` | Phrase | Fix | P3 | 0 |

**`AG-REP-Cost`** — 10 keywords · 30 searches/month · 3 terms with volume > 0

| Keyword | Match | Intent | Priority | Volume |
|---|---|---|---|---:|
| `replit deployment cost` | Phrase | Cost | P1 | **10** |
| `replit hosting cost` | Phrase | Cost | P2 | **10** |
| `replit export code` | Phrase | How-to | P2 | **10** |
| `replit reserved vm cost` | Phrase | Cost | P1 | 0 |
| `replit autoscale vs reserved vm` | Phrase | Decision | P1 | 0 |
| `replit pricing too expensive` | Phrase | Cost | P1 | 0 |
| `migrate off replit` | Phrase | Decision | P1 | 0 |
| `replit export to vercel` | Phrase | How-to | P2 | 0 |
| `replit alternative production` | Phrase | Decision | P2 | 0 |
| `move replit app to own server` | Phrase | Service | P1 | 0 |

### 7.3. RSA — set A (with brand name)

| # | Headline (English) | Ch | Pin |
|---|---|---:|---|
| H1 | `Replit App Not Deploying?` | 25 | **P1** |
| H2 | `Autoscale or Reserved VM?` | 25 | **P2** |
| H3 | `We Move Replit to Prod` | 22 | |
| H4 | `Fixed Price From €800` | 21 | |
| H5 | `Live in 1-3 Weeks` | 17 | |
| H6 | `Stop Surprise Hosting Bills` | 27 | |
| H7 | `11+ Years Engineering Exp.` | 26 | |
| H8 | `You Own 100% of the Code` | 24 | |
| H9 | `Get a Free Deploy Review` | 24 | **P3** |

| # | Description (English) | Ch |
|---|---|---:|
| D1 | `Replit deploy failing or costing too much? We move it to hosting you control.` | 77 |
| D2 | `Fixed price from €800. Live in 1-3 weeks. Your frontend untouched, code 100% yours.` | 83 |
| D3 | `Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW.` | 73 |

---

<a id="8"></a>
## 8. N1–N4 · Four Dutch-language campaigns

### 8.1. Why this section exists — and why it is not a translation

The first version of this plan had a logical flaw: **85 English keywords paired with bilingual English/Dutch ads.** Dutch ads only show against Dutch queries; attached to English keywords they are essentially never served. Conversely, a Dutch speaker typing Dutch matches no English keyword at all. The two halves never meet.

The fix is **not** to translate the 85 keywords into Dutch. Market data shows Dutch-language demand distributed very differently:

| Query type | Dutch speakers type it in | Evidence |
|---|---|---|
| Technical error strings (`deployment failed`, `RLS`, `CORS`) | **English** | The error message itself is in English; developers paste it verbatim into Google |
| Tool names (`Lovable`, `Bolt`, `Replit`) | **English** | Searching for Dutch-language content about these three tools returns only English results — local content is very thin |
| Service/hire intent | **Dutch** | At least 5 Dutch agencies run dedicated landing pages for `mvp laten maken` (Wiwi, Appfront, Agency 6, Zedrox, Creatix Code) — competition means volume |
| Legal compliance | **Dutch** | Dutch users type `AVG`, not `GDPR` |
| Payments | **Dutch + local PSP names** | `iDEAL`, `Mollie` — foreign competitors never mention these |

So the Dutch keyword set is **narrower but more commercial**. Compare the intent distributions:

| Intent | EN set (85 kw) | NL set (72 kw) |
|---|---:|---:|
| Fix (troubleshooting) | 30 | **1** |
| Hire + Service | 32 | **60** |
| Cost / Decision | 11 | 4 |
| Compliance | 0 | 3 |

> ⚠️ **This asymmetry is deliberate, not an omission.** The Dutch set has almost no troubleshooting keywords because Dutch speakers do not type technical errors in Dutch. If anyone proposes `lovable implementatie mislukt` (*Lovable implementation failed*), that is machine translation — nobody types that.

**The rule from here on: whatever language the keyword is in, the ad is in that language too.** B1–B3 (§5–§7) now carry English RSA only. N1–N4 use Dutch RSA only. No campaign mixes the two.

### 8.2. Architecture of the four Dutch campaigns

72 keywords, 4 campaigns, 10 ad groups.

```
N1-NL-Service    €150/mo   26 kw   General hire intent (MVP / app laten maken)
  ├─ AG-NL-MVP        6     mvp laten maken / bouwen / ontwikkeling
  ├─ AG-NL-App        8     app / webapp / saas laten bouwen
  ├─ AG-NL-Afmaken    6     app + prototype laten afmaken  ← closest to the pitch
  └─ AG-NL-Geo        6     + amsterdam / rotterdam / utrecht / eindhoven

N2-NL-AI-Tools    €60/mo   24 kw   Dutch + AI tool names
  ├─ AG-NL-AI-Afmaken 8     ai app laten afmaken, app productieklaar maken
  ├─ AG-NL-Lovable    6     lovable app laten afmaken / live zetten / beveiligen
  ├─ AG-NL-Bolt       4     ALWAYS with "new" — see §6.1
  └─ AG-NL-Replit     6     replit kosten te hoog, naar eigen server

N3-NL-Security    €60/mo   12 kw   Security + AVG (Dutch GDPR)
  └─ AG-NL-Security  12     beveiligingsaudit, avg proof, technische due diligence

N4-NL-Payments    €30/mo   10 kw   iDEAL / Mollie / Stripe
  └─ AG-NL-Payments  10     ideal betaling toevoegen, mollie koppelen app
```

> 🇳🇱 **Ad group names, glossed:** `AG-NL-Afmaken` — *afmaken* means "to finish" · `AG-NL-AI-Afmaken` — finishing AI-built apps · `beveiligingsaudit` — security audit · `AVG` — *Algemene Verordening Gegevensbescherming*, the Dutch name for GDPR.

**Dutch branch total: €300/month.** Plus €550 for B1–B3 → **€850/month.**

Common settings: Netherlands only · **language Dutch** (do not add English — this is the one difference from B1–B3) · Manual CPC or Maximize Clicks with a cap · Search only, Display & Search Partners off.

> 🔴 **These budget figures are superseded by the measured data.** See §2.4 and §2.8.

#### Complete keyword list — N1–N4 Dutch

**`AG-NL-MVP`** — 6 keywords · 90 searches/month · 3 terms with volume > 0

| Keyword | Match | Intent | Priority | Volume |
|---|---|---|---|---:|
| `mvp laten maken` *(have an MVP built)* | Phrase | Hire | P1 | **50** |
| `mvp ontwikkeling` *(MVP development)* | Phrase | Hire | P1 | **30** |
| `mvp laten ontwikkelen` *(have an MVP developed)* | Phrase | Hire | P1 | **10** |
| `mvp laten bouwen` *(have an MVP built — "bouwen" variant)* | Phrase | Hire | P1 | 0 |
| `mvp bureau` *(MVP agency)* | Phrase | Hire | P2 | 0 |
| `minimum viable product laten maken` *(have an MVP built, spelled out)* | Phrase | Hire | P2 | 0 |

**`AG-NL-App`** — 8 keywords · 1,100 searches/month · 7 terms with volume > 0

| Keyword | Match | Intent | Priority | Volume |
|---|---|---|---|---:|
| `app laten maken` *(have an app built)* | Phrase | Hire | P1 | **480** |
| `webapplicatie laten maken` *(have a web application built)* | Phrase | Hire | P2 | **260** |
| `app laten bouwen` *(have an app built — "bouwen" variant)* | Phrase | Hire | P1 | **140** |
| `software laten maken` *(have software built)* | Phrase | Hire | P2 | **110** |
| `maatwerk software laten maken` *(have custom software built)* | Phrase | Hire | P2 | **90** |
| `webapp laten bouwen` *(have a web app built)* | Phrase | Hire | P1 | **10** |
| `web applicatie laten bouwen` *(have a web application built — spaced spelling)* | Phrase | Hire | P2 | **10** |
| `saas laten bouwen` *(have a SaaS built)* | Phrase | Hire | P1 | 0 |

**`AG-NL-Afmaken`** — 6 keywords · 20 searches/month · 1 term with volume > 0

| Keyword | Match | Intent | Priority | Volume |
|---|---|---|---|---:|
| `developer inhuren app` *(hire a developer for an app)* | Phrase | Hire | P2 | **20** |
| `app laten afmaken` *(have an app finished)* | Phrase | Service | P1 | 0 |
| `prototype laten afmaken` *(have a prototype finished)* | Phrase | Service | P1 | 0 |
| `onafgemaakte app afmaken` *(finish an unfinished app)* | Phrase | Service | P2 | 0 |
| `app afmaken freelancer` *(freelancer to finish an app)* | Phrase | Hire | P2 | 0 |
| `freelance developer nederland` *(freelance developer, Netherlands)* | Phrase | Hire | P3 | 0 |

**`AG-NL-Geo`** — 6 keywords · 70 searches/month · 4 terms with volume > 0

| Keyword | Match | Intent | Priority | Volume |
|---|---|---|---|---:|
| `app laten maken amsterdam` *(have an app built, Amsterdam)* | Phrase | Hire | P1 | **20** |
| `app laten maken rotterdam` *(have an app built, Rotterdam)* | Phrase | Hire | P2 | **20** |
| `app laten maken eindhoven` *(have an app built, Eindhoven)* | Phrase | Hire | P2 | **20** |
| `app laten maken utrecht` *(have an app built, Utrecht)* | Phrase | Hire | P2 | **10** |
| `softwarebureau amsterdam` *(software agency, Amsterdam)* | Phrase | Hire | P2 | 0 |
| `mvp laten maken amsterdam` *(have an MVP built, Amsterdam)* | Phrase | Hire | P1 | 0 |

**`AG-NL-AI-Afmaken`** — 8 keywords · 0 searches/month · 0 terms with volume > 0

| Keyword | Match | Intent | Priority | Volume |
|---|---|---|---|---:|
| `ai app laten afmaken` *(have an AI app finished)* | Phrase | Service | P1 | 0 |
| `ai gebouwde app laten afmaken` *(have an AI-built app finished)* | Phrase | Service | P1 | 0 |
| `ai prototype naar productie` *(AI prototype to production)* | Phrase | Service | P1 | 0 |
| `van prototype naar productie` *(from prototype to production)* | Phrase | Decision | P1 | 0 |
| `app productieklaar maken` *(make an app production-ready)* | Phrase | Service | P1 | 0 |
| `prototype niet live krijgen` *(can't get the prototype live)* | Phrase | Fix | P2 | 0 |
| `vibe coding uitbesteden` *(outsource vibe coding)* | Phrase | Service | P2 | 0 |
| `no code app laten afmaken` *(have a no-code app finished)* | Phrase | Service | P2 | 0 |

**`AG-NL-Lovable`** — 6 keywords · 0 searches/month · 0 terms with volume > 0

| Keyword | Match | Intent | Priority | Volume |
|---|---|---|---|---:|
| `lovable app laten maken` *(have a Lovable app built)* | Phrase | Hire | P1 | 0 |
| `lovable app laten afmaken` *(have a Lovable app finished)* | Phrase | Service | P1 | 0 |
| `lovable developer nederland` *(Lovable developer, Netherlands)* | Phrase | Hire | P2 | 0 |
| `lovable app beveiligen` *(secure a Lovable app)* | Phrase | Security | P1 | 0 |
| `lovable app live zetten` *(put a Lovable app live)* | Phrase | Service | P1 | 0 |
| `lovable alternatief` *(Lovable alternative)* | Phrase | Decision | P3 | 0 |

**`AG-NL-Bolt`** — 4 keywords · 10 searches/month · 1 term with volume > 0

| Keyword | Match | Intent | Priority | Volume |
|---|---|---|---|---:|
| `bolt new developer` | Phrase | Hire | P2 | **10** |
| `bolt new app laten afmaken` *(have a Bolt.new app finished)* | Phrase | Service | P1 | 0 |
| `bolt new app live zetten` *(put a Bolt.new app live)* | Phrase | Service | P1 | 0 |
| `app gebouwd met bolt` *(app built with Bolt)* | Phrase | Service | P2 | 0 |

**`AG-NL-Replit`** — 6 keywords · 0 searches/month · 0 terms with volume > 0

| Keyword | Match | Intent | Priority | Volume |
|---|---|---|---|---:|
| `replit app laten afmaken` *(have a Replit app finished)* | Phrase | Service | P1 | 0 |
| `replit app live zetten` *(put a Replit app live)* | Phrase | Service | P1 | 0 |
| `replit kosten te hoog` *(Replit costs too high)* | Phrase | Cost | P1 | 0 |
| `weg van replit` *(away from Replit)* | Phrase | Decision | P2 | 0 |
| `replit app naar eigen server` *(Replit app to your own server)* | Phrase | Service | P1 | 0 |
| `replit developer nederland` *(Replit developer, Netherlands)* | Phrase | Hire | P2 | 0 |

**`AG-NL-Security`** — 12 keywords · 50 searches/month · 2 terms with volume > 0

| Keyword | Match | Intent | Priority | Volume |
|---|---|---|---|---:|
| `technische due diligence` *(technical due diligence)* | Phrase | Service | P1 | **40** |
| `pentest webapplicatie` *(web application pentest)* | Phrase | Service | P2 | **10** |
| `ai app beveiligen` *(secure an AI app)* | Phrase | Security | P1 | 0 |
| `beveiligingsaudit webapplicatie` *(web application security audit)* | Phrase | Service | P1 | 0 |
| `security audit laten uitvoeren` *(have a security audit performed)* | Phrase | Service | P1 | 0 |
| `code audit laten uitvoeren` *(have a code audit performed)* | Phrase | Service | P2 | 0 |
| `app avg proof maken` *(make an app GDPR-compliant)* | Phrase | Compliance | P1 | 0 |
| `avg compliance webapp` *(GDPR compliance, web app)* | Phrase | Compliance | P1 | 0 |
| `persoonsgegevens beveiligen app` *(secure personal data in an app)* | Phrase | Compliance | P2 | 0 |
| `datalek voorkomen app` *(prevent a data breach in an app)* | Phrase | Security | P2 | 0 |
| `supabase beveiliging` *(Supabase security)* | Phrase | Security | P2 | 0 |
| `due diligence software audit` | Phrase | Service | P1 | 0 |

**`AG-NL-Payments`** — 10 keywords · 0 searches/month · 0 terms with volume > 0

| Keyword | Match | Intent | Priority | Volume |
|---|---|---|---|---:|
| `ideal betaling toevoegen app` *(add an iDEAL payment to an app)* | Phrase | Service | P1 | 0 |
| `ideal koppelen webshop` *(connect iDEAL to a webshop)* | Phrase | Service | P2 | 0 |
| `mollie koppelen app` *(connect Mollie to an app)* | Phrase | Service | P1 | 0 |
| `mollie integratie laten bouwen` *(have a Mollie integration built)* | Phrase | Hire | P1 | 0 |
| `stripe koppelen app` *(connect Stripe to an app)* | Phrase | Service | P1 | 0 |
| `stripe integratie nederland` *(Stripe integration, Netherlands)* | Phrase | Hire | P2 | 0 |
| `betalingen toevoegen aan app` *(add payments to an app)* | Phrase | Service | P1 | 0 |
| `abonnementen in app bouwen` *(build subscriptions into an app)* | Phrase | Service | P2 | 0 |
| `inlogsysteem laten bouwen` *(have a login system built)* | Phrase | Service | P2 | 0 |
| `gebruikersbeheer app bouwen` *(build user management for an app)* | Phrase | Service | P3 | 0 |

### 8.3. Three important observations about the Dutch set

**① ~~`N2-NL-AI-Tools` is the cheapest asset in the account.~~ ❌ WRONG — contradicted by the data.**
The original claim: *"almost certainly nobody bidding, CPC at the floor, own the whole group for a few dozen euros"*. **Keyword Planner returned: the entire 24-keyword campaign draws 10 searches/month, with 23 of 24 terms at zero.** The three ad groups `AG-NL-AI-Afmaken`, `AG-NL-Lovable` and `AG-NL-Replit` are all at absolute zero. There is nothing there to own. See §2.5.

**② `N1-NL-Service` is the only campaign that can scale — and also the riskiest on ICP fit.**
`mvp laten maken` faces real competition from full-service agencies quoting €25,000–50,000. They will push CPC to €8–15. The person clicking may be looking for a partner to build from scratch, not someone to **finish** an existing prototype. The landing page must address this above the fold, or CPL will be dreadful.

**③ `app laten maken` needs negatives against mobile-app confusion.**
In the Netherlands, "app" defaults to meaning a phone application. Mandatory negatives: `ios`, `android`, `native`, `app store`, `google play`, `flutter`, `react native`, `iphone app`, `android app`. Without them, roughly a third of queries will be people wanting a native app built — outside the service's scope.

### 8.4. RSA — N1-NL-Service (Dutch only)

> 🇳🇱 Ad copy stays in Dutch; the English meaning follows in parentheses. Enter the Dutch text into Google Ads exactly as written.

| # | Headline (Nederlands) | English meaning | Ch | Pin |
|---|---|---|---:|---|
| H1 | `MVP Laten Bouwen?` | Want an MVP built? | 17 | **P1** |
| H2 | `Van Prototype Naar Live` | From prototype to live | 23 | **P2** |
| H3 | `Vaste Prijs Vanaf €800` | Fixed price from €800 | 22 | |
| H4 | `Live Binnen 1-3 Weken` | Live within 1-3 weeks | 21 | |
| H5 | `Geen Herbouw Nodig` | No rebuild needed | 18 | |
| H6 | `Wij Fixen Alleen Wat Moet` | We only fix what must be fixed | 25 | |
| H7 | `11+ Jaar Ervaring` | 11+ years of experience | 17 | |
| H8 | `100% Eigendom Van Je Code` | 100% ownership of your code | 25 | |
| H9 | `Security, Betalingen, Hosting` | Security, payments, hosting | 29 | |
| H10 | `Gratis Offerte In 1 Dag` | Free quote within 1 day | 23 | **P3** |

| # | Description (Nederlands) | English meaning | Ch |
|---|---|---|---:|
| D1 | `Prototype klaar maar niet live? Wij regelen security, betalingen en hosting.` | Prototype ready but not live? We handle security, payments and hosting. | 76 |
| D2 | `Vaste prijs vanaf €800, live in 1-3 weken. Alle code blijft 100% van jou.` | Fixed price from €800, live in 1-3 weeks. All code stays 100% yours. | 73 |
| D3 | `Bureau rekent €50.000 voor herbouw? Wij behouden je frontend en fixen wat nodig is.` | Agency charging €50,000 for a rebuild? We keep your frontend and fix what's needed. | 83 |

> 💡 **H5 `Geen Herbouw Nodig` and D3 are the two most important pieces in this campaign.** They attack head-on the weakness of the full-service agencies bidding on the same keywords: they sell rebuild-from-scratch projects, LaunchStudio sells finishing what is missing. This is what differentiates you on the results page, before anyone clicks.

### 8.5. RSA — N2-NL-AI-Tools (Dutch only)

| # | Headline (Nederlands) | English meaning | Ch | Pin |
|---|---|---|---:|---|
| H1 | `AI-App Niet Live Te Krijgen?` | Can't get your AI app live? | 28 | **P1** |
| H2 | `Wij Maken Je AI-App Af` | We finish your AI app | 22 | **P2** |
| H3 | `Gebouwd Met Lovable Of Bolt?` | Built with Lovable or Bolt? | 28 | |
| H4 | `Vaste Prijs Vanaf €800` | Fixed price from €800 | 22 | |
| H5 | `Live Binnen 1-3 Weken` | Live within 1-3 weeks | 21 | |
| H6 | `Je Frontend Blijft Staan` | Your frontend stays as it is | 24 | |
| H7 | `11+ Jaar Engineering Ervaring` | 11+ years of engineering experience | 29 | |
| H8 | `100% Eigendom Van Je Code` | 100% ownership of your code | 25 | |
| H9 | `Gratis Code Review` | Free code review | 18 | **P3** |

| # | Description (Nederlands) | English meaning | Ch |
|---|---|---|---:|
| D1 | `Met een AI-tool gebouwd maar niet live? Wij fixen security, betalingen en hosting.` | Built with an AI tool but not live? We fix security, payments and hosting. | 82 |
| D2 | `Vaste prijs vanaf €800. Live in 1-3 weken. Je frontend blijft, code 100% van jou.` | Fixed price from €800. Live in 1-3 weeks. Your frontend stays, code 100% yours. | 81 |
| D3 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW. | 78 |

> ⚠️ **H3 contains brand names.** Apply the three layers of defence in §3.1. If Google restricts it, replace H3 with `Gebouwd Met Een AI-Tool?` (*Built with an AI tool?*, 24 characters) and strip all brand names from this set. The `AG-NL-Bolt` ad group must **not** use an H3 containing the word "Bolt" standing alone — see §6.1.

### 8.6. RSA — N3-NL-Security (Dutch only)

| # | Headline (Nederlands) | English meaning | Ch | Pin |
|---|---|---|---:|---|
| H1 | `Is Je AI-App Wel Veilig?` | Is your AI app actually secure? | 24 | **P1** |
| H2 | `Security Audit Vaste Prijs` | Security audit, fixed price | 26 | **P2** |
| H3 | `45% AI-Code Heeft Lekken` | 45% of AI code has leaks | 24 | |
| H4 | `Wachtwoorden, Keys, Rechten` | Passwords, keys, permissions | 27 | |
| H5 | `Rapport In Dagen` | Report within days | 16 | |
| H6 | `11+ Jaar Cybersecurity` | 11+ years of cybersecurity | 22 | |
| H7 | `AVG-Proof Opgeleverd` | Delivered GDPR-compliant | 20 | |
| H8 | `Klaar Voor Due Diligence` | Ready for due diligence | 24 | |
| H9 | `Vraag Gratis Scan Aan` | Request a free scan | 21 | **P3** |

| # | Description (Nederlands) | English meaning | Ch |
|---|---|---|---:|
| D1 | `Open keys, geen rechten, geen limieten. Wij vinden wat AI-code achterlaat.` | Exposed keys, no permissions, no limits. We find what AI code leaves behind. | 74 |
| D2 | `Vaste prijs voor een audit van je AI-app. Helder rapport met prioriteiten, in dagen.` | Fixed price for an audit of your AI app. Clear prioritised report, within days. | 84 |
| D3 | `11+ jaar security-engineering, vertrouwd door Vodafone, TNO en CFLW. Gratis offerte.` | 11+ years of security engineering, trusted by Vodafone, TNO and CFLW. Free quote. | 84 |

> ⚠️ **H3 `45% AI-Code Heeft Lekken` is a statistical claim.** The landing page must cite a research source for this figure, or it breaches Google's Misrepresentation policy. If no source can be cited, replace it with `AI-Code Laat Gaten Achter` (*AI code leaves gaps behind*, 25 characters).

### 8.7. RSA — N4-NL-Payments (Dutch only)

| # | Headline (Nederlands) | English meaning | Ch | Pin |
|---|---|---|---:|---|
| H1 | `Betalingen In Je App?` | Payments in your app? | 21 | **P1** |
| H2 | `Stripe, Mollie Of iDEAL` | Stripe, Mollie or iDEAL | 23 | **P2** |
| H3 | `Wij Koppelen Het Goed` | We connect it properly | 21 | |
| H4 | `Vaste Prijs Vanaf €800` | Fixed price from €800 | 22 | |
| H5 | `Live Binnen 1-3 Weken` | Live within 1-3 weeks | 21 | |
| H6 | `Webhooks Die Wél Werken` | Webhooks that actually work | 23 | |
| H7 | `Abonnementen Of Eenmalig` | Subscriptions or one-off | 24 | |
| H8 | `11+ Jaar Ervaring` | 11+ years of experience | 17 | |
| H9 | `Gratis Adviesgesprek` | Free consultation | 20 | **P3** |

| # | Description (Nederlands) | English meaning | Ch |
|---|---|---|---:|
| D1 | `Betalingen werken niet in je app? Wij koppelen Stripe, Mollie of iDEAL correct.` | Payments not working in your app? We connect Stripe, Mollie or iDEAL correctly. | 79 |
| D2 | `Vaste prijs vanaf €800. Abonnementen, eenmalig of op gebruik. Live in 1-3 weken.` | Fixed price from €800. Subscriptions, one-off or usage-based. Live in 1-3 weeks. | 80 |
| D3 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW. | 78 |

> 💡 **`iDEAL` is a local advantage no foreign competitor uses.** iDEAL accounts for the majority of online payments in the Netherlands. A Dutch founder who built an app with Lovable will discover Stripe does not support iDEAL as fully as they assumed — that is the moment they start searching. Keep `iDEAL` in its correct lower-upper casing.

### 8.8. Character limit verification

All 49 Dutch RSA assets in §8.4–§8.7 have been counted by script:

| Type | Google limit | Longest in the Dutch set | Result |
|---|---:|---:|---|
| Headline | 30 | 29 (`Security, Betalingen, Hosting` · `11+ Jaar Engineering Ervaring`) | ✅ 0 violations |
| Description | 90 | 84 (`...Helder rapport met prioriteiten, in dagen.` · `...Gratis offerte.`) | ✅ 0 violations |

> ⚠️ **The `€` character and accented letters (`Wél`) count as one character** in Google Ads, not two. The counts above follow that convention. If you edit the copy, re-count by script rather than estimating — an earlier check caught a 33-character headline that had been declared as 30.

### 8.9. Negative keywords specific to the Dutch branch

In addition to the lists in §9, the Dutch branch needs:

| Block | Negative keywords | Reason |
|---|---|---|
| **Native apps** (broad) | `ios`, `android`, `native`, `flutter`, `iphone`, `ipad`, `smartphone`, `play store` | In Dutch, "app" defaults to a phone app |
| **Webshop** (phrase) | `webshop laten maken` *(have a webshop built)*, `woocommerce`, `shopify`, `magento`, `lightspeed` | `ideal koppelen` pulls a great deal of e-commerce traffic |
| **Training/jobs** (broad) | `cursus` *(course)*, `opleiding` *(training)*, `leren` *(to learn)*, `stage` *(internship)*, `vacature` *(job vacancy)*, `salaris` *(salary)*, `zzp tarief` *(freelance rate)* | Learning or job-seeking intent, not hiring intent |
| **Free/DIY** (broad) | `gratis` *(free)*, `zelf` *(yourself)*, `template`, `voorbeeld` *(example)*, `handleiding` *(manual)* | Except `gratis offerte` *(free quote)* — if you need to keep that, add it as a positive phrase keyword |
| **Manufacturing** (phrase + broad) | The full 218-term list in §9.6 below | `van prototype naar productie` collides exactly with Dutch metalworking terminology |

> 🔴 **The "Manufacturing" block is mandatory, not optional.** `van prototype naar productie` is standard phrasing in the Dutch metalworking/CNC industry. Without those 218 terms applied, campaign N2 will spend money on people looking for an aluminium machine shop.

### 8.10. Landing pages for the Dutch branch

The four English pages in §10 **cannot be reused** for the Dutch branch. Dutch ads pointing at English pages drop conversion rate and Quality Score.

| Campaign | Page required | Note |
|---|---|---|
| `N1-NL-Service` | `/nl/mvp-laten-afmaken` *(have an MVP finished)* | The most important page. Must state "finishing ≠ rebuilding" above the fold |
| `N2-NL-AI-Tools` | `/nl/ai-app-laten-afmaken` *(have an AI app finished)* | Name Lovable/Bolt/Replit in the body copy, with a non-affiliation disclaimer |
| `N3-NL-Security` | `/nl/security-audit` | Cite the source for the 45% figure. Say AVG, not GDPR |
| `N4-NL-Payments` | `/nl/betalingen-koppelen` *(connect payments)* | Mention iDEAL before Stripe |

The contact form, the autoresponder email and the person replying must all be in Dutch. A Dutch lead who receives an English reply is all but lost.

> ⚠️ **Do not launch the N group until these four Dutch pages exist.** Launch B1–B3 first (§11.2), build the Dutch pages in parallel, launch N afterwards.

---

<a id="9"></a>
## 9. Negative keywords per brand

### 9.1. B1 Lovable — guarding against dictionary and lingerie queries

```
-bra          -bras         -lingerie     -underwear    -intimates
-panties      -meaning      -definition   -synonym      -synonyms
-antonym      -quotes       -quote        -song         -songs
-lyrics       -lyric        -movie        -film         -book
-novel        -doll         -plush        -toy          -baby
-babies       -pet          -pets         -dog          -cat
-name         -names        -spelling     -loveable
```

### 9.2. 🔴 B2 Bolt — the single most important list in this plan

**Taxi / ride-hailing / delivery** *(the largest source of noise in the Dutch market)*
```
-taxi         -rit          -ritje        -rides        -ride
-driver       -chauffeur    -bestuurder   -uber         -lyft
-food         -eten         -bezorging    -delivery     -courier
-scooter      -step         -fiets        -bike         -ebike
-rental       -huren        -verhuur      -promo code   -kortingscode
-fare         -tarief       -app store    -play store   -download app
```
> 🇳🇱 Dutch terms here: `rit` (ride) · `ritje` (short ride) · `bestuurder` (driver) · `eten` (food) · `bezorging` (delivery) · `step` (scooter) · `fiets` (bicycle) · `huren` (to rent) · `verhuur` (rental) · `kortingscode` (discount code) · `tarief` (fare/rate).

**Hardware / bolts / screws**
```
-screw        -nut          -washer       -anchor       -fastener
-schroef      -moer         -bout         -m8           -m10
-stainless    -galvanized   -hex          -thread       -torque
-hardware store             -bouwmarkt    -gereedschap
```
> 🇳🇱 Dutch terms here: `schroef` (screw) · `moer` (nut) · `bout` (bolt) · `bouwmarkt` (DIY store) · `gereedschap` (tools).

**People & other brands**
```
-usain        -sprint       -olympic      -athletics    -record
-lightning    -thunder      -threads      -fabric       -mushroom
-disney       -cartoon      -movie        -game
```

**Electric vehicles & energy**
```
-ev           -charger      -charging     -battery      -motorcycle
-motor        -vehicle      -car
```

### 9.3. B3 Replit — the shortest list

```
-tutorial     -course       -cursus       -learn        -teach
-classroom    -education    -student      -school       -homework
-python tutorial            -free hosting -100 days     -curriculum
```
> 🇳🇱 Dutch term here: `cursus` (course).

### 9.4. Applied to all three campaigns

```
-free         -gratis       -crack        -cracked      -torrent
-jobs         -job          -vacature     -salary       -career
-reddit       -youtube      -github       -docs         -documentation
-alternative to             -vs           -review       -download
```
> 🇳🇱 Dutch terms here: `gratis` (free) · `vacature` (job vacancy).

> ⚠️ **Think twice about `-vs` and `-review`.** Both block comparison queries, which can be genuine prospects in the consideration stage. If `AG-LOV-Migrate` shows good signal, remove `-vs` from B1.

### 9.5. Technical notes

1. **Negative keywords do not match close variants automatically.** You must enter `-taxi` **and** `-taxis`, `-rit` **and** `-ritten` separately.
2. **Single words → negative broad · multi-word phrases → negative phrase.**
3. **Negative broad requires all words to appear together.** `-promo code` as broad only blocks queries containing both words.
4. **Create three separate Shared Negative Lists** (Lovable / Bolt / Replit) plus one shared list, attached to the right campaigns. Do not merge them — Bolt's negatives attached to Replit will block good traffic.

---

### 9.6. 🔴 Manufacturing / fabrication negative list — 218 terms

#### Why this list is necessary

These are not "just in case" negatives. LaunchStudio's core positioning **collides directly** with standard manufacturing terminology:

| Word in your keywords | Meaning in software | Meaning in manufacturing |
|---|---|---|
| **prototype** | an AI-generated app build | a physical sample: 3D print, CNC, mockup |
| **production** / **productie** | the live environment | a mass production line |
| **prototype to production** | getting an app live | **NPI/DFM — moving a physical product into series production** |
| **build** / **bouwen** | writing code | fabricating, constructing |
| **custom / op maat** | bespoke software | machined to order |
| **launch** | launching an app | launching a physical product |

`prototype naar productie` and `prototype to production` are **standard phrases in the hardware industry**. People searching them may need a CNC shop, a 3D printing service or a contract manufacturer — not someone to fix a Lovable app.

With an account that can only buy **69 clicks/month on its largest campaign** (§2.4), a handful of stray clicks at €10–14 CPC is already 2–5% of the monthly budget. This is the highest-impact list in §9.

#### 9.6.1. Materials

```
-aluminium    -aluminum     -staal        -steel        -metaal
-metal        -rvs          -inox         -stainless    -koper
-copper       -messing      -brass        -titanium     -gietijzer
-kunststof    -plastic      -acryl        -acrylic      -plexiglas
-hout         -wood         -mdf          -composiet    -composite
-carbon       -glasvezel    -rubber       -schuim       -foam
```
> 🇳🇱 Dutch terms: `staal` (steel) · `metaal` (metal) · `rvs` (stainless steel) · `koper` (copper) · `messing` (brass) · `gietijzer` (cast iron) · `kunststof` (plastic) · `acryl` (acrylic) · `hout` (wood) · `composiet` (composite) · `glasvezel` (fibreglass) · `schuim` (foam).

#### 9.6.2. Machining & fabrication

```
-cnc          -frezen       -freesmachine -milling      -draaien
-draaibank    -turning      -verspanen    -verspaning   -machining
-lasersnijden -laser        -waterjet     -plasma       -zetten
-kanten       -bending      -buigen       -lassen       -welding
-laswerk      -plaatwerk    -sheet        -metaalbewerking
-gieten       -casting      -spuitgieten  -injection    -molding
-moulding     -extrusie     -extrusion    -matrijs      -matrijzen
-mold         -mould        -tooling      -stansen      -stamping
-ponsen       -slijpen      -grinding     -polijsten    -anodiseren
-anodizing    -poedercoaten -coating      -galvaniseren -stralen
-fabricage    -fabrication  -fabricatie
```
> 🇳🇱 Dutch terms: `frezen` (milling) · `freesmachine` (milling machine) · `draaien` (turning) · `draaibank` (lathe) · `verspanen`/`verspaning` (machining) · `lasersnijden` (laser cutting) · `zetten`/`kanten`/`buigen` (bending) · `lassen`/`laswerk` (welding) · `plaatwerk` (sheet metal) · `metaalbewerking` (metalworking) · `gieten` (casting) · `spuitgieten` (injection moulding) · `extrusie` (extrusion) · `matrijs`/`matrijzen` (mould/moulds) · `stansen`/`ponsen` (stamping/punching) · `slijpen` (grinding) · `polijsten` (polishing) · `anodiseren` (anodising) · `poedercoaten` (powder coating) · `galvaniseren` (galvanising) · `stralen` (blasting) · `fabricage`/`fabricatie` (fabrication).

#### 9.6.3. 3D printing / additive

```
-3d           -3d print     -3d-print     -3dprint      -3d printing
-3d printer   -printen      -filament     -resin        -pla
-abs          -petg         -sls          -sla          -fdm
-dlp          -additive     -sintering    -stereolithografie
-slicer       -cura         -nozzle       -printbed
```
> 🇳🇱 Dutch terms: `printen` (printing) · `stereolithografie` (stereolithography).

> ⚠️ **Think carefully about `-3d` as a broad negative.** It blocks `3d` standing alone. If LaunchStudio has clients building apps with 3D models (configurators, viewers), drop `-3d` and keep only the two-word phrases.

#### 9.6.4. Physical prototyping — the most important block

```
-rapid prototyping        -prototyping service      -prototype fabrication
-prototype machining      -prototype parts          -hardware prototype
-physical prototype       -functional prototype     -prototype mold
-pcb                      -printed circuit          -breadboard
-enclosure                -housing                  -mockup model
-scale model              -maquette                 -proefmodel
-nulserie                 -pilot run                -tooling prototype
```
> 🇳🇱 Dutch terms: `maquette` (scale model) · `proefmodel` (test model) · `nulserie` (zero series / pre-production run).

#### 9.6.5. Manufacturing companies

```
-manufacturer   -manufacturers  -manufacturing  -fabrikant      -fabrikanten
-maakindustrie  -maakbedrijf    -productiebedrijf -machinebouw  -machinefabriek
-toeleverancier -toelevering    -contract manufacturing         -oem
-odm            -assembly line  -productielijn  -seriematig     -serieproductie
-massaproductie -mass production -batch production -moq
-minimum order  -werkplaats     -smederij       -gieterij       -constructiebedrijf
```
> 🇳🇱 Dutch terms: `fabrikant`/`fabrikanten` (manufacturer/s) · `maakindustrie` (manufacturing industry) · `maakbedrijf`/`productiebedrijf` (manufacturing company) · `machinebouw` (machine building) · `machinefabriek` (machine factory) · `toeleverancier`/`toelevering` (supplier/supply) · `productielijn` (production line) · `seriematig`/`serieproductie` (series production) · `massaproductie` (mass production) · `werkplaats` (workshop) · `smederij` (forge) · `gieterij` (foundry) · `constructiebedrijf` (structural engineering firm).

#### 9.6.6. Buying/renting machinery

```
-machine kopen      -machines te koop   -machine te koop
-machinepark        -occasion           -tweedehands
-gebruikte machine  -machine huren      -verhuur
-onderhoud          -reparatie          -onderdelen
-gereedschap        -tooling kopen      -3d printer kopen
-laser kopen        -cnc kopen
```
> 🇳🇱 Dutch terms: `kopen` (to buy) · `te koop` (for sale) · `machinepark` (machine fleet) · `occasion`/`tweedehands` (second-hand) · `gebruikte machine` (used machine) · `huren` (to rent) · `verhuur` (rental) · `onderhoud` (maintenance) · `reparatie` (repair) · `onderdelen` (parts) · `gereedschap` (tools).

#### 9.6.7. CAD/CAM software (a different software category)

```
-cad          -cam          -cadcam       -solidworks   -autocad
-fusion       -fusion 360   -freecad      -inventor     -catia
-creo         -mastercam    -nx           -sketchup     -rhino
-gcode        -g-code       -post processor             -dxf
-dwg          -step file    -iges         -stl
```

#### 9.6.8. Industry ERP vendors (people looking for competitors, not for you)

```
-mkg          -komdex       -snabbt       -halloy       -klaes
-reynapro     -logikal      -orgadata     -vtbo         -kozijncalculator
-paperless parts            -digifabster  -cloudnc      -proshop
-global shop
```
> 🇳🇱 Dutch term: `kozijncalculator` (window frame calculator).

#### 9.6.9. Construction & facade building

```
-aannemer     -bouwbedrijf  -verbouwing   -renovatie    -bestek
-constructie  -staalconstructie           -kozijn       -kozijnen
-gevel        -gevelbouw    -facade       -dakkapel     -serre
-beglazing    -ramen        -deuren       -schuifpui
```
> 🇳🇱 Dutch terms: `aannemer` (contractor) · `bouwbedrijf` (construction firm) · `verbouwing` (renovation) · `renovatie` (renovation) · `bestek` (specification/tender document) · `constructie` (structure) · `staalconstructie` (steel structure) · `kozijn`/`kozijnen` (window frame/s) · `gevel`/`gevelbouw` (facade/facade building) · `dakkapel` (dormer) · `serre` (conservatory) · `beglazing` (glazing) · `ramen` (windows) · `deuren` (doors) · `schuifpui` (sliding patio door).

#### 9.6.10. Technical notes for entering these into Google Ads

1. **Negative keywords do NOT match close variants automatically.** Unlike ordinary keywords, negatives do not catch plurals, misspellings or accents on their own. Enter them separately: `-machine` **and** `-machines`, `-matrijs` **and** `-matrijzen`.
2. **Single words → negative broad; multi-word phrases → negative phrase.** `-cnc` as broad blocks every query containing "cnc". `"-rapid prototyping"` goes in as phrase.
3. **Negative broad requires all the words to appear together.** `-machine kopen` as broad only blocks queries containing **both** words. To block reliably, use phrase.
4. **Apply at account level** (Shared Library → Negative keyword lists), not per campaign — the `prototype`/`production` risk applies to every campaign.
5. **Check before applying:** use the Search Terms Report to make sure no negative blocks good traffic. For example `-coating` could block `coating software` — if that is a potential client, drop it.

---

<a id="10"></a>
## 10. Landing pages

### 10.1. The four pages required

| URL | For campaign | Required? |
|---|---|---|
| `/en/fix-lovable-app` | B1 (Hire + Problem) | **Required** |
| `/en/fix-bolt-app` | B2 | **Required** |
| `/en/fix-replit-app` | B3 (Hire + Problem) | **Required** |
| `/en/replit-hosting-costs` | B3 (Cost) | Recommended |
| `/en/lovable-tanstack-migration` | B1 (Migrate) | Recommended |

### 10.2. Why not use one shared page

With brand keywords, **message match decides everything**. Someone typing `fix replit app`, clicking an ad that says "Replit", and landing on a generic page about "AI prototype to production" will bounce immediately. That drags down both Quality Score and conversion rate.

These three pages **do not need writing from scratch** — use a shared skeleton and change only:
- The H1 and opening paragraph, naming the specific tool
- The "common problems" section, listing that tool's actual failures (§6.3 for Bolt, §7.1 for Replit)
- One sentence stating independence: *"LaunchStudio is an independent studio and is not affiliated with [tool]."*

### 10.3. Content skeleton for each page

| Section | Content |
|---|---|
| H1 | Name that tool's specific problem |
| Opening paragraph | What you built · why it cannot go live |
| List | 5–6 concrete failures specific to that tool |
| Process | 3 steps · 1–3 week timeline |
| Price | From €800, fixed price |
| Independence statement | One clear sentence |
| CTA | Free quote / free code review |

---

<a id="11"></a>
## 11. Budget & rollout

### 11.1. Budget

| | Tier A — Exploratory | Tier B — Recommended | Tier C — Ceiling |
|---|---:|---:|---:|
| B1 Lovable | €150 | €250 | €400 |
| B2 Bolt | €60 | €120 | €200 |
| B3 Replit | €120 | €180 | €280 |
| *English branch subtotal* | *€330* | *€550* | *€880* |
| N1 NL Service | €100 | €150 | €300 |
| N2 NL AI-Tools | €40 | €60 | €90 |
| N3 NL Security | €40 | €60 | €120 |
| N4 NL Payments | €20 | €30 | €60 |
| *Dutch branch subtotal* | *€200* | *€300* | *€570* |
| **Total/month** | **€530** | **€850** | **€1,450** |

> 🔴 **THE TABLE ABOVE IS SUPERSEDED — the real volume data gives a very different answer.** Actual spend ceilings derived from measured volume:
>
> | Campaign | Real volume | Table above allocates | Real ceiling | New recommendation |
> |---|---:|---:|---:|---:|
> | B1-Lovable | 110 | €250 | €30 | ┐ |
> | B2-Bolt | 120 | €120 | €32 | ├ merge into 1 campaign at **€100–140** |
> | B3-Replit | 300 | €180 | €81 | ┘ |
> | N1-NL-Service | **1,280** | €150 | **€691** | **€400–550** |
> | N2-NL-AI-Tools | 10 | €60 | €5 | **turn off** |
> | N3-NL-Security | 50 | €60 | €27 | €40 |
> | N4-NL-Payments | **0** | €30 | €0 | **turn off** |
>
> **New recommended total: €540–730/month**, weighted toward the Dutch branch. Full reasoning in §2.8.

**Why Bolt gets the lowest budget despite the highest volume:** because that volume has never been shown to be genuine bolt.new demand. Raise Bolt's budget **only after** the Search Terms Report is clean for two consecutive weeks.

**Why N1 is the only Dutch campaign with a high ceiling (€300):** it is the only group facing real competition from Dutch agencies, which means there is real volume to spend against. N2–N4 have very low volume — extra money buys no extra impressions. If `IS lost (budget)` for N2–N4 sits near 0%, the budget is already more than enough; do not raise it.

> ⚠️ **Tier C at €1,450/month far exceeds the account's real volume ceiling.** Spend ceiling is calculated as:
>
> ```
> Max spend/month = Volume × %ads-suitable-kw × IS × CTR × CPC
>
> (IS = Impression Share · CTR = Click-Through Rate · CPC = Cost Per Click)
> ```
>
> With the measured volume (§2.4), all 157 keywords together buy only **about 100 clicks/month**, equal to **€540–730/month**. Setting a higher budget leaves money unspent — this account is constrained by **volume**, not by budget. Spending more requires **expanding the keyword surface** (more phrases, more geos), not raising bids.
>
> A second consequence: at roughly 100 clicks/month, **do not use Maximize Conversions**. Google needs 3–6 months to gather enough learning data. Use Manual CPC or Maximize Clicks with a cap.

### 11.2. Eight-week rollout — launch sequentially, never simultaneously

| Week | Task |
|---|---|
| **0** | Run Keyword Planner across the 85 keywords, geo = EU-EN and NL separately. **Update §11.1 with real figures.** Build 3 landing pages. Create 4 Shared Negative Lists |
| **1** | Launch **B3 Replit** at Tier A. One campaign only. Manual CPC |
| **2** | Check Search Terms every second day, add negatives. Assess Replit query quality |
| **3** | Launch **B1 Lovable** at Tier A. Run RSA sets A and B side by side to compare |
| **4** | **Review 1.** Compare Replit vs Lovable: CPC, CTR, query quality. Move whichever shows good signal from Tier A to Tier B |
| **5** | Launch **B2 Bolt** at Tier A, **with NL/BE excluded from geo**. Check Search Terms **daily** |
| **6** | Assess Bolt query cleanliness. If > 30% of queries are taxi/hardware → tighten keywords to Exact or turn it off |
| **7** | If Bolt has been clean for two consecutive weeks → consider reopening NL/BE geo with the full negative list |
| **8** | **Review 2.** Calculate real CPL per brand. Concentrate budget on the winner, cut the loser |

#### Dutch branch — weeks 9–14

The N group **does not launch alongside the English branch**, because it needs four Dutch landing pages that do not yet exist (§8.10).

| Week | Task |
|---|---|
| **1–8** | *(in parallel)* Build the four `/nl/…` pages. Run Keyword Planner across the 72 Dutch keywords, geo = Netherlands, language = Dutch. Prepare the Dutch autoresponder |
| **9** | Launch **N2-NL-AI-Tools** first at Tier A. Cheapest, cleanest, uncontested — use it to verify the entire Dutch path works (ad → page → form → email) |
| **10** | Launch **N3-NL-Security** and **N4-NL-Payments** at Tier A. Check Search Terms every second day — watch for webshop traffic leaking into N4 |
| **11** | Launch **N1-NL-Service** at Tier A. This is the most expensive Dutch campaign — check Search Terms **daily** during the first week |
| **12** | **Review 3.** Measure the ratio of "finish it" vs "build new" queries in N1. If > 70% want something built from scratch → fix the landing page first, don't rush to switch it off |
| **13–14** | Compare CPL for the EN branch vs the NL branch. Move budget to the winner |

> 💡 **Why N2 launches first despite the lowest volume:** it is cheap enough that operational mistakes cost nothing. If the Dutch form is broken or the autoresponder goes out in English, you find out on a €40/month campaign rather than a €150/month one.

> 🔴 **This rollout order predates the volume data.** With N1 holding 1,280 of the 1,870 total volume and the English branch capped at €143, consider reversing the sequence: build the Dutch pages first and lead with N1. See §2.8.

### 11.3. Why sequential rather than simultaneous

1. **Cause can be isolated.** Launch all three at once and a bad CPL tells you nothing about which brand caused it.
2. **Learn negatives on a clean campaign first.** Replit teaches you how to read Search Terms before you touch Bolt.
3. **Protect the budget.** Bolt is the only campaign that can burn money quickly — launch it last, once the routine is familiar.

---

<a id="12"></a>
## 12. KPIs & kill thresholds

### 12.1. KPI table for the brand plan

| Metric | Week 4 | Week 8 | Kill threshold |
|---|---|---|---|
| **CPC** (Cost Per Click) | ≤ €12 | ≤ €10 | > €16 sustained for 2 weeks |
| **CTR** (Click-Through Rate) | ≥ 5% | ≥ 8% | < 3% in any ad group |
| **Relevant query ratio** | ≥ 70% | ≥ 85% | **< 50% on B2 Bolt = switch off immediately** |
| **LP conversion** (landing page conversion rate) | ≥ 3% | ≥ 5% | < 2% after one round of fixes |
| **CPL** (Cost Per Lead) | ≤ €400 | ≤ €300 | > €500 |
| **QS** (Quality Score) | ≥ 5 | ≥ 6 | < 4 = fix the landing page |

> **CTR expectations are higher than for an ordinary plan** (8% rather than 6–7%) because brand keywords match queries very tightly. A CTR below 5% on brand keywords almost certainly means the ad copy is not naming the tool correctly.

### 12.2. This plan's own metric: relevant query ratio

This metric **does not exist in Google Ads** and has to be calculated by hand from the Search Terms Report:

```
Relevant query ratio = queries genuinely about the AI tool ÷ total queries
```

For B2 Bolt this is the make-or-break number. Weekly method:
1. Download B2's Search Terms Report
2. Label every query: relevant / taxi / hardware / other
3. If the "relevant" group is < 50% → **switch the campaign off**, rather than adding more negatives

### 12.3. Decision rules

| Situation | Action |
|---|---|
| B2 Bolt below 50% relevant queries after 2 weeks | **Switch off the campaign.** More negatives cannot fix a structural problem |
| Ad group has spent > €120 with 0 conversions after 4 weeks | Switch off the ad group |
| RSA set B (no brand name) has a higher CTR than set A | Keep set B, drop set A — it removes policy risk for free |
| Google restricts ad text after a trademark complaint | Switch to RSA set B **within 24 hours** |
| One brand shows CPL < €250 while the other two are > €450 | Move the entire budget to the winner |
| QS < 4 on brand keywords | The landing page does not match — fix the page, do not raise bids |

---

<a id="13"></a>
## 13. Pre-launch checklist

### Research & legal

- [x] ~~Run Keyword Planner across all 157 keywords~~ — **done 2026-09-25, results in §2**
- [ ] Re-run Keyword Planner for the `Top of page bid (low/high)` column — **CPC is still unknown**; every calculation in §2.7 currently uses an €8–14 estimate
- [ ] Apply the six restructuring recommendations in §2.8 before building campaigns: turn off N4, turn off N2, merge B1+B2+B3, raise N1 to €400–550
- [ ] Decide between Option A and Option B (§2.8) — this is a strategic decision, not a configuration one
- [ ] Verify `replit agency` = 210 with Exact match + one week of Search Terms (§2.3)
- [ ] Run **Netherlands** and **EU-EN** geos separately — compare to see Bolt's noise level
- [ ] **Update §11.1 with real volume**
- [ ] Compare volume for `mvp laten maken` vs `app laten maken` — if both are under 50/month, keep N1 at Tier A
- [ ] Re-read the current version of Google Ads trademark policy
- [ ] If budget allows, confirm with legal counsel: is the "complementary service, not a competitor" position safe enough for the target markets?

### Landing pages

- [ ] `/en/fix-replit-app` is live *(launches first)*
- [ ] `/en/fix-lovable-app` is live
- [ ] `/en/fix-bolt-app` is live
- [ ] Each page carries **one clear independence statement**

### Dutch landing pages *(needed only before week 9)*

- [ ] `/nl/ai-app-laten-afmaken` is live *(first to launch in the Dutch branch)*
- [ ] `/nl/security-audit` is live — **with a cited source for the 45% figure**
- [ ] `/nl/betalingen-koppelen` is live — iDEAL named before Stripe
- [ ] `/nl/mvp-laten-afmaken` is live — states **"finishing ≠ rebuilding"** above the fold
- [ ] All four pages are in native Dutch, **not machine translation**
- [ ] Contact form is in Dutch
- [ ] Autoresponder email is in Dutch
- [ ] Someone who speaks Dutch is available when leads reply
- [ ] Use **AVG**, not **GDPR**, across all Dutch pages
- [ ] Each page lists **that specific tool's failures**, not one shared list

### Inside Google Ads

- [ ] Create **6 Shared Negative Lists** before building campaigns: Lovable · Bolt · Replit · Shared · **NL-Shared** · **Manufacturing (218 terms, §9.6)**
- [ ] Attach the right list to the right campaign — **never merged**
- [ ] **Campaign language: B1–B3 = English · N1–N4 = Dutch.** No campaign selects both
- [ ] N1: apply the "Native apps" negative block (`ios`, `android`, `native`…) — without it, roughly a third of queries are phone apps
- [ ] N4: apply the "Webshop" negative block (`shopify`, `woocommerce`…) — `ideal koppelen` pulls heavy e-commerce traffic
- [ ] N2: attach the **Manufacturing** list — `van prototype naar productie` collides with Dutch metalworking terminology
- [ ] `AG-NL-Bolt`: every keyword carries `new` or `gebouwd met` — **no keyword is bare `bolt`**
- [ ] B2 Bolt: **exclude NL and BE from geo**
- [ ] Location targeting = **"Presence"**, not "Presence or interest"
- [ ] Bid strategy = **Manual CPC**
- [ ] Match types: Phrase as the default, Exact for `[hire X developer]`. **No broad match anywhere**
- [ ] Ad rotation = **"Do not optimize"**
- [ ] Load **both RSA sets** (A and B) — set B paused, ready to activate
- [ ] Schedule: Search Terms **daily for B2 and N1**, every second day for the rest

---

## 📌 Summary

> **Two language branches, seven separate campaigns, launched sequentially — never all at once.**
>
> **The English branch (B1–B3)** captures technical error strings and tool names — what Dutch speakers also type in English. **The Dutch branch (N1–N4)** captures service/hire intent, AVG compliance and iDEAL payments — things that only exist in Dutch. Each campaign uses exactly one language for both keywords and ads.
>
> Start with **Replit**: the cleanest name and a clear commercial pain point (Reserved VM costs). Then **Lovable**, with the most keywords and the TanStack migration opportunity. **Bolt last**, on the smallest budget with the Netherlands excluded from geo — because in LaunchStudio's primary market, "Bolt" is the second-largest taxi company.
>
> Every ad group keeps **two RSA sets**: one with brand names to run, one without as a fallback if Google restricts the copy. Google permits bidding on trademarks as keywords; the risk lies in using them in ad text.
>
> The deciding metric is neither CPC nor CTR but the **relevant query ratio**. Below 50% on Bolt, switch it off rather than trying to rescue it with negatives.
>
> The Dutch keyword set is **deliberately narrower**: 1 troubleshooting keyword against 30 in the English set, but 60 service/hire keywords against 32. Dutch speakers type errors in English and needs in Dutch — the keyword set reflects that rather than machine-translating.
>
> 🔴 **And the finding that overrides all of the above:** the core thesis — "finish my unfinished AI prototype" — draws 10 searches/month across 27 keywords. The demand this plan was built to capture does not measurably exist. See §2.

---

*157 keywords (85 EN + 72 NL) · 7 campaigns · 18 ad groups · 90 RSA assets (41 EN + 49 NL) verified by script against Google Ads character limits (headline ≤ 30, description ≤ 90) — 0 violations · One language per campaign*

*Every keyword is listed in full in this document: §5.1 (B1) · §6.2 (B2) · §7.2 (B3) · §8.2 (N1–N4) · §2.3 (all terms with volume > 0)*

*⚠️ **Volume measured 2026-09-25: 1,870 searches/month across all 157 keywords, with 106 terms at zero.** The core thesis "finish my AI prototype" draws 10 searches/month. The budgets and priority order in §11 are superseded — use §2.8 instead. CPC remains unmeasured.*

*🇳🇱 Dutch keywords and ad copy are kept in the original language throughout, with English glosses in parentheses. Enter them into Google Ads exactly as written — do not translate.*
