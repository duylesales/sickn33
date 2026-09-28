# 🇳🇱 Google Search Ads — Three AI Brands, Entirely in Dutch
## B1 Lovable · B2 Bolt · B3 Replit → launchstudio.eu

> **Scope:** The same 3-campaign / 8-ad-group structure as the English plan, but with **all 85 keywords translated into Dutch** and **all ad copy written in Dutch**.
> **Date:** 2026-09-28 · **Market:** Netherlands · **Campaign language:** Dutch
> **This document is self-contained.** Keywords, RSA copy, extensions, negatives and rollout are all inside it.

> 🇳🇱 **Convention:** every keyword and every piece of ad copy stays in Dutch, because that is what gets pasted into Google Ads. The English meaning sits in the adjacent column. **Do not translate when entering into Google Ads.**

---

> # 🔴 READ FIRST — THE ASSUMPTION THIS PLAN RESTS ON
>
> This plan was built exactly as requested: translate the 85 B1/B2/B3 keywords into Dutch and write Dutch ad copy.
>
> **But the data measured on 2026-09-25 says the opposite.** In the previous Keyword Planner run, 24 Dutch keywords carrying AI tool names (`lovable app laten afmaken`, `replit app live zetten`, `bolt new app laten afmaken`…) returned **10 searches/month in total, with 23 of 24 at zero**. The three ad groups `AG-NL-Lovable`, `AG-NL-Replit` and `AG-NL-AI-Afmaken` were all at absolute zero.
>
> The verified reason: **Dutch speakers type technical error strings in English**, because the error message itself is in English and developers paste it verbatim. Searching for Dutch-language content about these three tools returns only English results.
>
> **So this plan should be treated as:**
> - ✅ **A cheap land-grab experiment** — if real volume is zero, CPC sits at the floor and holding the position costs almost nothing. Recommended budget €90–150/month for all three campaigns combined.
> - ✅ **An asset ready for later** — if Dutch-language content about vibe coding grows over the next 12–24 months, the keyword set and ad copy already exist.
> - ❌ **Not a primary channel.** Do not fund it as though it had volume. Verify with Keyword Planner (geo Netherlands, language Dutch) before launching — see §10.
>
> **Mandatory before launch:** run Keyword Planner against the 85 keywords in `kp_upload_NL_translated.txt`. If total volume is under 100/month, launch only B1 at €50/month and drop B2 and B3.

---

## 📑 Table of contents

| § | Contents |
|---|---|
| [1](#1) | Translation principles — what gets translated, what does not |
| [2](#2) | Architecture: 3 campaigns · 8 ad groups |
| [3](#3) | Risks specific to the Dutch version |
| [4](#4) | Overlap with the existing Dutch keyword set |
| [5](#5) | B1 · Lovable — full keywords & RSA |
| [6](#6) | B2 · Bolt — full keywords & RSA |
| [7](#7) | B3 · Replit — full keywords & RSA |
| [8](#8) | Dutch ad extensions |
| [9](#9) | Negative keywords |
| [10](#10) | Budget, rollout & KPIs |
| [11](#11) | Pre-launch checklist |

---

<a id="1"></a>
## 1. Translation principles — what gets translated, what does not

Not every word gets translated. Dutch developers mix the two languages according to a clear pattern:

| Word type | Handling | Examples |
|---|---|---|
| **Verbs, adjectives, ordinary nouns** | ✅ Translate | `not working` → `werkt niet` · `failed` → `mislukt` · `cost` → `kosten` · `too expensive` → `te duur` |
| **Commercial actions** | ✅ Translate, preferring native Dutch phrasing | `for hire` → `inhuren` · `agency` → `bureau` · `development service` → `laten ontwikkelen` |
| **Product & brand names** | ❌ Keep as-is | `Lovable`, `Bolt.new`, `Replit`, `Supabase`, `Stripe`, `Netlify`, `Vercel`, `Next.js`, `TanStack` |
| **Technical terms developers never translate** | ❌ Keep as-is | `deployment`, `RLS`, `SSR`, `CORS`, `secrets`, `agent`, `token`, `hosting`, `upgrade` |
| **Service tier names** | ❌ Keep as-is | `Reserved VM`, `Autoscale` |
| **Half-and-half terms** | ⚠️ Both forms are used — pick the Dutch form but remember the English one | `environment variables` ↔ `omgevingsvariabelen` · `error` ↔ `foutmelding` |

**Three translations worth noting:**

1. **`blank page` → `witte pagina`** (*white page*). Dutch speakers say "white page", not "empty page". Machine translation gives `blanco pagina` — nobody types that.
2. **`agent stuck` → `agent loopt vast`** (*agent runs stuck*). `loopt vast` is the standard idiom for hanging or freezing. `agent vast` is machine translation.
3. **`fix` → `repareren` / `fixen`.** Dutch developers use both; `fixen` is more common in conversation, `repareren` more common when typing a search. Keywords use `repareren`, ad copy uses `fixen`.

> ⚠️ **One keyword was replaced outright rather than translated.** `fix bolt app` was not rendered as `bolt app repareren` — that phrase would almost certainly match queries about the Bolt taxi app. It became `app gebouwd met bolt new laten afmaken` (*have an app built with Bolt.new finished*): longer, lower volume, but impossible to confuse.

---

<a id="2"></a>
## 2. Architecture: 3 campaigns · 8 ad groups

```
LaunchStudio ACCOUNT — Dutch-language branch for three AI brands
│                                    [All of it: geo Netherlands · language Dutch]
├── B1 · LS-NL-Lovable                                    32 keywords
│   ├── AG-LOV-NL-Hire      (12) → /nl/lovable-app-laten-afmaken
│   ├── AG-LOV-NL-Problem   (11) → /nl/lovable-app-werkt-niet
│   └── AG-LOV-NL-Migrate    (9) → /nl/lovable-tanstack-migratie
│
├── B2 · LS-NL-Bolt                                       24 keywords
│   ├── AG-BOLT-NL-Hire      (8) → /nl/bolt-new-app-laten-afmaken
│   └── AG-BOLT-NL-Problem  (16) → /nl/bolt-new-deployt-niet
│
└── B3 · LS-NL-Replit                                     29 keywords
    ├── AG-REP-NL-Hire       (7) → /nl/replit-app-laten-afmaken
    ├── AG-REP-NL-Problem   (12) → /nl/replit-app-werkt-niet
    └── AG-REP-NL-Cost      (10) → /nl/replit-hosting-kosten
```

> 🇳🇱 **Landing page slugs, glossed:** `lovable-app-laten-afmaken` (have a Lovable app finished) · `lovable-app-werkt-niet` (Lovable app not working) · `lovable-tanstack-migratie` (Lovable TanStack migration) · `bolt-new-deployt-niet` (Bolt.new not deploying) · `replit-hosting-kosten` (Replit hosting costs). Keep the slugs in Dutch — they carry keyword relevance for Quality Score.

The structure is kept 1:1 with the English plan so that performance can be compared between the two languages on identical intent.

| Setting | Value | Reason |
|---|---|---|
| Location | **Netherlands**, "Presence" mode | Never "Presence or interest" |
| **Language** | **Dutch — Dutch only** | Do not add English, or this competes internally with the EN branch |
| Match type | **Phrase** as the default · **Exact** for 4 risky keywords | No broad match anywhere |
| Bid strategy | **Manual CPC** | Expected volume is far too low for Smart Bidding |
| Ad rotation | "Do not optimize" for the first 4 weeks | Collect data fairly |
| Networks | Search only | Display & Search Partners off |

**Intent distribution** (identical to the English set, since this is a 1:1 translation):

| Intent | Keywords |
|---|---:|
| Fix (troubleshooting) | 30 |
| Hire | 17 |
| Service | 15 |
| How-to | 7 |
| Decision | 6 |
| Cost | 5 |
| Security | 3 |
| Research | 2 |

> ⚠️ **30 of 85 keywords carry Fix intent.** This is precisely the group the data says Dutch speakers search in English. If the `*-Problem` ad groups record no impressions after 4 weeks, switch them off and keep only `Hire` + `Cost` + `Migrate`.

---

<a id="3"></a>
## 3. Risks specific to the Dutch version

### 3.1. `gezocht` collides with job advertisements

`lovable developer gezocht` and `replit developer gezocht` (*developer wanted*) are **exactly how job ads are headlined** in the Netherlands. The person clicking may be a developer looking for work, not a founder looking to hire.

➡️ Set both to **Exact match** and apply mandatory negatives: `vacature`, `vacatures`, `baan`, `werk`, `solliciteren`, `cv`, `salaris`, `zzp tarief`, `stage`, `traineeship`.

### 3.2. `bolt` is still a taxi company — in Dutch too

This risk is **worse** in the Dutch version, because geo is necessarily Netherlands — the very market where Bolt taxi is strongest (Amsterdam, Rotterdam, The Hague, Utrecht). The English plan could exclude NL/BE from geo; this one cannot.

➡️ **Three non-negotiable rules:**
1. Every keyword carries `new` or the phrase `gebouwd met bolt new`
2. The entire §9.2 negative list is applied **before** the campaign runs for one minute
3. Read Search Terms **daily** for the first three weeks, not every second day

### 3.3. `naar productie` collides with metalworking terminology

Four keywords contain `naar productie` or `productieklaar`: `lovable app naar productie brengen`, `bolt new naar productie`, `replit app naar productie`, `lovable app productieklaar maken`.

`van prototype naar productie` is **standard phrasing in the Dutch metalworking/CNC industry** (NPI/DFM). Without the manufacturing negative list applied, these four keywords will pull people looking for an aluminium machine shop.

➡️ **Attaching the "Manufacturing" Shared Negative List (218 terms) is mandatory** for all three campaigns. The complete list is in §9.4 below.

### 3.4. `lovable werkt niet` — an English adjective inside a Dutch sentence

`lovable` remains an English adjective and a global lingerie brand. Inside the Dutch sentence `lovable werkt niet` the risk is lower than for the English `lovable not working`, but the lingerie/dictionary negatives in §9.1 are still required.

---

<a id="4"></a>
## 4. Overlap with the existing Dutch keyword set

Four keywords in this translated set **already exist** in `keyword_seeds_3_ai_brands_NL.csv` (the original Dutch set, campaigns N1–N4):

| Keyword | In the old NL set | In this translated set | Resolution |
|---|---|---|---|
| `lovable developer nederland` | `AG-NL-Lovable` | `AG-LOV-NL-Hire` | Keep **here**, remove from N2 |
| `lovable alternatief` | `AG-NL-Lovable` | `AG-LOV-NL-Migrate` | Keep **here** (better intent fit with Migrate) |
| `weg van replit` | `AG-NL-Replit` | `AG-REP-NL-Cost` | Keep **here** (same group as `te duur`) |
| `replit app naar eigen server` | `AG-NL-Replit` | `AG-REP-NL-Cost` | Keep **here** |

> 🔴 **Identical keywords in two campaigns with the same geo and language compete internally.** Google picks one, usually the one with the higher Ad Rank, and you lose control over which ad shows. Remove one side before launching.
>
> Since this translated set fully covers the old `AG-NL-Lovable` and `AG-NL-Replit` — and both of those measured **zero volume** — the recommendation is to **switch off campaign N2-NL-AI-Tools entirely** and let this set replace it.

---

---

<a id="5"></a>
## 5. B1 · Lovable · `B1-NL-Lovable` — 32 keywords

### 5.1. `AG-LOV-NL-Hire` — 12 keywords · Max CPC €12.00

**Hire intent — people actively looking for someone to do the work** · Landing page: `/nl/lovable-app-laten-afmaken`

| Keyword (Nederlands) | English meaning / original | Match | Intent | Priority | Note |
|---|---|---|---|---|---|
| `lovable app repareren` | `fix lovable app` | Phrase | Hire | P1 | `repareren` = to repair. The standard Dutch verb. |
| `lovable developer inhuren` | `lovable developer for hire` | Phrase | Hire | P1 | `inhuren` = to hire. The most commercial phrasing. |
| `lovable developer gezocht` | `hire lovable developer` | Exact | Hire | P1 | `gezocht` = wanted. ⚠️ Also how job ads are headlined — needs `vacature` negatives. |
| `lovable developer nederland` | `lovable developer` | Phrase | Hire | P1 | `nederland` added to avoid colliding with the English set. |
| `lovable app laten ontwikkelen` | `lovable app development service` | Phrase | Hire | P1 | `laten ontwikkelen` = to have developed. |
| `lovable app naar productie brengen` | `take my lovable app to production` | Phrase | Service | P1 | ⚠️ Manufacturing negatives (§9.4) are mandatory — `naar productie` collides with metalworking. |
| `lovable app productieklaar maken` | `lovable app production ready` | Phrase | Service | P1 | `productieklaar` = production-ready. |
| `mijn lovable app laten afmaken` | `finish my lovable app` | Phrase | Service | P2 | Closest match to the actual pitch in this group. |
| `lovable audit laten uitvoeren` | `lovable audit service` | Phrase | Service | P1 | `laten uitvoeren` = to have performed. |
| `lovable beveiligingsaudit` | `lovable security audit` | Phrase | Service | P1 | `beveiligingsaudit` = security audit. Standard Dutch compound. |
| `lovable app bureau` | `lovable app agency` | Phrase | Hire | P2 | `bureau` = agency. |
| `lovable freelancer` | `lovable freelancer` | Phrase | Hire | P2 | `freelancer` is unchanged in Dutch. |

#### RSA — `AG-LOV-NL-Hire` (entirely in Dutch)

| # | Headline (Nederlands) | English meaning | Ch | Pin |
|---|---|---|---:|---|
| H1 | `Lovable App Laten Afmaken?` | Want your Lovable app finished? | 26 | **P1** |
| H2 | `Lovable Developer Inhuren` | Hire a Lovable developer | 25 | **P2** |
| H3 | `Vaste Prijs Vanaf €800` | Fixed price from €800 | 22 |  |
| H4 | `Live Binnen 1-3 Weken` | Live within 1-3 weeks | 21 |  |
| H5 | `Wij Maken Het Productieklaar` | We make it production-ready | 28 |  |
| H6 | `Je Frontend Blijft Staan` | Your frontend stays as it is | 24 |  |
| H7 | `11+ Jaar Engineering` | 11+ years of engineering | 20 |  |
| H8 | `100% Eigendom Van Je Code` | 100% ownership of your code | 25 |  |
| H9 | `Geen Partner Van Lovable` | Not affiliated with Lovable | 24 |  |
| H10 | `Security, Stripe En Hosting` | Security, Stripe and hosting | 27 |  |
| H11 | `Nederlandse Developers` | Dutch developers | 22 |  |
| H12 | `Gratis Code Review` | Free code review | 18 | **P3** |

| # | Description (Nederlands) | English meaning | Ch |
|---|---|---|---:|
| D1 | `Met Lovable gebouwd maar niet live? Wij regelen security, betalingen en hosting.` | Built with Lovable but not live? We handle security, payments and hosting. | 80 |
| D2 | `Vaste prijs vanaf €800. Live in 1-3 weken. Je code blijft 100% van jou.` | Fixed price from €800. Live in 1-3 weeks. Your code stays 100% yours. | 71 |
| D3 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW. | 78 |
| D4 | `Geen uurtarief en geen verrassingen. Vraag vandaag een gratis review aan.` | No hourly rate, no surprises. Request a free review today. | 73 |

### 5.2. `AG-LOV-NL-Problem` — 11 keywords · Max CPC €9.00

**Failures — the app will not run** · Landing page: `/nl/lovable-app-werkt-niet`

| Keyword (Nederlands) | English meaning / original | Match | Intent | Priority | Note |
|---|---|---|---|---|---|
| `lovable app werkt niet` | `lovable app not working` | Phrase | Fix | P2 | `werkt niet` = not working. The most natural phrasing. |
| `lovable deployment mislukt` | `lovable deployment failed` | Phrase | Fix | P2 | `mislukt` = failed. `deployment` stays — Dutch devs don't translate it. |
| `lovable preview versus productie` | `lovable preview vs production` | Phrase | Fix | P2 | `versus` is used in Dutch too. |
| `lovable eigen domein werkt niet` | `lovable custom domain not working` | Phrase | Fix | P2 | `eigen domein` = own/custom domain. |
| `lovable stripe integratie` | `lovable stripe integration` | Phrase | Fix | P1 | `integratie` = integration. |
| `lovable inloggen werkt niet` | `lovable login not working` | Phrase | Fix | P2 | `inloggen` = to log in. |
| `lovable supabase rls` | `lovable supabase rls` | Phrase | Security | P2 | Not translated — RLS is a technical term. |
| `is lovable veilig` | `is lovable secure` | Phrase | Research | P2 | `veilig` = safe/secure. |
| `lovable werkt niet` | `lovable not working` | Phrase | Fix | P2 | Shorter — risks the adjective sense. Phrase only. |
| `lovable stripe werkt niet` | `lovable stripe not working` | Phrase | Fix | P1 | A more specific variant. |
| `lovable beveiligingslekken` | `lovable security vulnerabilities` | Phrase | Research | P2 | `beveiligingslekken` = security leaks/holes. |

#### RSA — `AG-LOV-NL-Problem` (entirely in Dutch)

| # | Headline (Nederlands) | English meaning | Ch | Pin |
|---|---|---|---:|---|
| H1 | `Lovable App Werkt Niet?` | Lovable app not working? | 23 | **P1** |
| H2 | `Wij Fixen Lovable Apps` | We fix Lovable apps | 22 | **P2** |
| H3 | `Deployment Mislukt?` | Deployment failed? | 19 |  |
| H4 | `Eigen Domein Werkt Niet?` | Custom domain not working? | 24 |  |
| H5 | `Stripe Koppeling Kapot?` | Stripe connection broken? | 23 |  |
| H6 | `Inloggen Werkt Niet?` | Login not working? | 20 |  |
| H7 | `Supabase RLS Goed Ingesteld` | Supabase RLS set up properly | 27 |  |
| H8 | `Vaste Prijs Vanaf €800` | Fixed price from €800 | 22 |  |
| H9 | `Opgelost In Dagen` | Solved within days | 17 |  |
| H10 | `11+ Jaar Engineering` | 11+ years of engineering | 20 |  |
| H11 | `Geen Partner Van Lovable` | Not affiliated with Lovable | 24 |  |
| H12 | `Gratis Foutanalyse` | Free fault analysis | 18 | **P3** |

| # | Description (Nederlands) | English meaning | Ch |
|---|---|---|---:|
| D1 | `Werkt je Lovable app niet? Wij vinden de oorzaak en lossen het definitief op.` | Lovable app not working? We find the cause and fix it for good. | 77 |
| D2 | `Preview werkt maar live niet? Dat is bijna altijd configuratie, niet je code.` | Preview works but live doesn't? That's almost always config, not your code. | 77 |
| D3 | `Vaste prijs vanaf €800. Opgelost in dagen. Je code blijft 100% van jou.` | Fixed price from €800. Solved within days. Your code stays 100% yours. | 71 |
| D4 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW. | 78 |

### 5.3. `AG-LOV-NL-Migrate` — 9 keywords · Max CPC €11.00

**Leaving the platform — TanStack, Next.js, self-hosting** · Landing page: `/nl/lovable-tanstack-migratie`

| Keyword (Nederlands) | English meaning / original | Match | Intent | Priority | Note |
|---|---|---|---|---|---|
| `weg van lovable` | `migrate off lovable` | Phrase | Decision | P1 | `weg van` = away from. ⚠️ Duplicate of the old NL set — pick one campaign. |
| `lovable migratie laten uitvoeren` | `lovable migration service` | Phrase | Service | P1 | `migratie` = migration. |
| `lovable tanstack migratie` | `lovable tanstack migration` | Phrase | Service | P1 | TanStack unchanged — technology name. |
| `lovable naar tanstack migreren` | `migrate lovable to tanstack` | Phrase | Service | P1 | `migreren` = to migrate. |
| `lovable ssr upgrade` | `lovable ssr upgrade` | Phrase | Service | P1 | Not translated — SSR and upgrade are technical terms. |
| `lovable code exporteren` | `lovable export code` | Phrase | How-to | P2 | `exporteren` = to export. |
| `lovable app zelf hosten` | `self host lovable app` | Phrase | Decision | P2 | `zelf hosten` = to self-host. |
| `lovable naar nextjs` | `lovable to nextjs` | Phrase | How-to | P2 | Framework name unchanged. |
| `lovable alternatief` | `lovable alternative` | Phrase | Decision | P2 | `alternatief` = alternative. |

#### RSA — `AG-LOV-NL-Migrate` (entirely in Dutch)

| # | Headline (Nederlands) | English meaning | Ch | Pin |
|---|---|---|---:|---|
| H1 | `Weg Van Lovable?` | Moving away from Lovable? | 16 | **P1** |
| H2 | `Lovable Naar TanStack` | Lovable to TanStack | 21 | **P2** |
| H3 | `Of Naar Next.js` | Or to Next.js | 15 |  |
| H4 | `Wij Migreren Je Code` | We migrate your code | 20 |  |
| H5 | `Zelf Hosten Zonder Lock-in` | Self-host without lock-in | 26 |  |
| H6 | `SSR Voor Betere SEO` | SSR for better SEO | 19 |  |
| H7 | `Vaste Prijs Vanaf €800` | Fixed price from €800 | 22 |  |
| H8 | `Klaar In 1-3 Weken` | Done within 1-3 weeks | 18 |  |
| H9 | `Code 100% Van Jou` | Code 100% yours | 17 |  |
| H10 | `11+ Jaar Engineering` | 11+ years of engineering | 20 |  |
| H11 | `Geen Partner Van Lovable` | Not affiliated with Lovable | 24 |  |
| H12 | `Gratis Migratiescan` | Free migration scan | 19 | **P3** |

| # | Description (Nederlands) | English meaning | Ch |
|---|---|---|---:|
| D1 | `Lovable draait sinds mei 2026 op TanStack. Oude projecten migreren niet mee.` | Lovable has run on TanStack since May 2026. Old projects don't migrate along. | 76 |
| D2 | `Geen SSR betekent slechte SEO. Wij migreren je app naar een moderne stack.` | No SSR means poor SEO. We migrate your app to a modern stack. | 74 |
| D3 | `Vaste prijs vanaf €800. Je code exporteren en zelf hosten, zonder lock-in.` | Fixed price from €800. Export your code and self-host, without lock-in. | 74 |
| D4 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW. | 78 |


---

<a id="6"></a>
## 6. B2 · Bolt · `B2-NL-Bolt` — 24 keywords

### 6.1. `AG-BOLT-NL-Hire` — 8 keywords · Max CPC €10.00

**Hire intent — ALWAYS carries `new`** · Landing page: `/nl/bolt-new-app-laten-afmaken`

| Keyword (Nederlands) | English meaning / original | Match | Intent | Priority | Note |
|---|---|---|---|---|---|
| `bolt new app repareren` | `fix bolt new app` | Phrase | Hire | P1 | Always carries `new`. |
| `bolt new developer inhuren` | `hire bolt new developer` | Exact | Hire | P1 | Exact match for maximum control. |
| `bolt new developer nederland` | `bolt new developer` | Phrase | Hire | P1 | Geo added to avoid colliding with the English set. |
| `bolt new naar productie` | `bolt new to production` | Phrase | Service | P1 | ⚠️ Manufacturing negatives (§9.4) are mandatory. |
| `bolt new app productieklaar` | `bolt new app production ready` | Phrase | Service | P1 | `productieklaar` = production-ready. |
| `bolt new bureau` | `bolt new agency` | Phrase | Hire | P2 | `bureau` = agency. |
| `app gebouwd met bolt new laten afmaken` | `fix bolt app` | Phrase | Service | P1 | Replaces `bolt app repareren` — the longer phrase excludes taxi queries far better. |
| `bolt new app developer` | `bolt app developer` | Exact | Hire | P3 | 🔴 HIGH RISK. Exact only. See the warning in §6.1. |

#### RSA — `AG-BOLT-NL-Hire` (entirely in Dutch)

| # | Headline (Nederlands) | English meaning | Ch | Pin |
|---|---|---|---:|---|
| H1 | `Bolt.new App Laten Afmaken?` | Want your Bolt.new app finished? | 27 | **P1** |
| H2 | `Bolt.new Developer Inhuren` | Hire a Bolt.new developer | 26 | **P2** |
| H3 | `Voor Bolt.new Bouwers` | For Bolt.new builders | 21 |  |
| H4 | `Vaste Prijs Vanaf €800` | Fixed price from €800 | 22 |  |
| H5 | `Live Binnen 1-3 Weken` | Live within 1-3 weeks | 21 |  |
| H6 | `Wij Maken Het Productieklaar` | We make it production-ready | 28 |  |
| H7 | `Je Frontend Blijft Staan` | Your frontend stays as it is | 24 |  |
| H8 | `11+ Jaar Engineering` | 11+ years of engineering | 20 |  |
| H9 | `100% Eigendom Van Je Code` | 100% ownership of your code | 25 |  |
| H10 | `Geen Partner Van Bolt.new` | Not affiliated with Bolt.new | 25 |  |
| H11 | `Nederlandse Developers` | Dutch developers | 22 |  |
| H12 | `Gratis Build Review` | Free build review | 19 | **P3** |

| # | Description (Nederlands) | English meaning | Ch |
|---|---|---|---:|
| D1 | `Met Bolt.new gebouwd maar niet live? Wij fixen env vars, CORS en de build.` | Built with Bolt.new but not live? We fix env vars, CORS and the build. | 74 |
| D2 | `Vaste prijs vanaf €800. Live in 1-3 weken. Je code blijft 100% van jou.` | Fixed price from €800. Live in 1-3 weeks. Your code stays 100% yours. | 71 |
| D3 | `Wij zijn geen partner van Bolt.new. Wel de studio die je app live krijgt.` | We're not Bolt.new's partner. We are the studio that gets your app live. | 73 |
| D4 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW. | 78 |

### 6.2. `AG-BOLT-NL-Problem` — 16 keywords · Max CPC €8.00

**Failures — preview works, production breaks** · Landing page: `/nl/bolt-new-deployt-niet`

| Keyword (Nederlands) | English meaning / original | Match | Intent | Priority | Note |
|---|---|---|---|---|---|
| `bolt new werkt niet` | `bolt new not working` | Phrase | Fix | P2 | 'werkt niet' = not working. |
| `bolt new preview versus productie` | `bolt new preview vs production` | Phrase | Fix | P2 | The failure mode characteristic of WebContainer. |
| `bolt new productiefout` | `bolt new production error` | Phrase | Fix | P2 | `productiefout` = production error. |
| `bolt new deployment` | `bolt new deployment` | Phrase | Fix | P2 | Not translated — Dutch devs use `deployment` as-is. |
| `bolt new deploy foutmelding` | `bolt new deploy error` | Phrase | Fix | P2 | `foutmelding` = error message. |
| `bolt new omgevingsvariabelen` | `bolt new environment variables` | Phrase | Fix | P2 | `omgevingsvariabelen` = environment variables. Dutch devs use both forms. |
| `bolt new cors foutmelding` | `bolt new cors error` | Phrase | Fix | P3 | CORS unchanged. |
| `bolt new bundel te groot` | `bolt new bundle too large` | Phrase | Fix | P3 | `bundel te groot` = bundle too large. |
| `bolt new netlify deployen` | `bolt new netlify deploy` | Phrase | Fix | P3 | `deployen` = the Dutch-ised verb form of 'deploy'. |
| `bolt new supabase` | `bolt new supabase` | Phrase | How-to | P3 | Product name unchanged. |
| `bolt new stripe` | `bolt new stripe` | Phrase | How-to | P3 | Product name unchanged. |
| `bolt new eigen domein` | `bolt new custom domain` | Phrase | Fix | P3 | `eigen domein` = custom domain. |
| `bolt new witte pagina` | `bolt new blank page` | Phrase | Fix | P3 | `witte pagina` = white page. The Dutch idiom for this failure. |
| `bolt new code exporteren` | `bolt new export code` | Phrase | How-to | P2 | `exporteren` = to export. |
| `bolt new token limiet` | `bolt new token limit` | Phrase | Cost | P3 | `limiet` = limit. |
| `bolt new beveiliging` | `bolt new security` | Phrase | Security | P2 | `beveiliging` = security. |

#### RSA — `AG-BOLT-NL-Problem` (entirely in Dutch)

| # | Headline (Nederlands) | English meaning | Ch | Pin |
|---|---|---|---:|---|
| H1 | `Bolt.new Deployt Niet?` | Bolt.new not deploying? | 22 | **P1** |
| H2 | `Preview Werkt, Live Niet?` | Preview works, live doesn't? | 25 | **P2** |
| H3 | `Wij Fixen CORS En Env` | We fix CORS and env vars | 21 |  |
| H4 | `Bundel Te Groot?` | Bundle too large? | 16 |  |
| H5 | `Witte Pagina Na Deploy?` | Blank page after deploy? | 23 |  |
| H6 | `Omgevingsvariabelen Kwijt?` | Environment variables lost? | 26 |  |
| H7 | `Netlify Of Vercel` | Netlify or Vercel | 17 |  |
| H8 | `Vaste Prijs Vanaf €800` | Fixed price from €800 | 22 |  |
| H9 | `Opgelost In Dagen` | Solved within days | 17 |  |
| H10 | `11+ Jaar Engineering` | 11+ years of engineering | 20 |  |
| H11 | `Geen Partner Van Bolt.new` | Not affiliated with Bolt.new | 25 |  |
| H12 | `Gratis Build Review` | Free build review | 19 | **P3** |

| # | Description (Nederlands) | English meaning | Ch |
|---|---|---|---:|
| D1 | `Bolt.new preview is geen productie. Wij fixen env vars, CORS en buildfouten.` | Bolt.new preview is not production. We fix env vars, CORS and build errors. | 76 |
| D2 | `Witte pagina na deploy? Meestal ontbrekende omgevingsvariabelen. Wij fixen het.` | Blank page after deploy? Usually missing env variables. We fix it. | 79 |
| D3 | `Vaste prijs vanaf €800. Opgelost in dagen. Je code blijft 100% van jou.` | Fixed price from €800. Solved within days. Your code stays 100% yours. | 71 |
| D4 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW. | 78 |


---

<a id="7"></a>
## 7. B3 · Replit · `B3-NL-Replit` — 29 keywords

### 7.1. `AG-REP-NL-Hire` — 7 keywords · Max CPC €11.00

**Hire intent** · Landing page: `/nl/replit-app-laten-afmaken`

| Keyword (Nederlands) | English meaning / original | Match | Intent | Priority | Note |
|---|---|---|---|---|---|
| `replit app repareren` | `fix replit app` | Phrase | Hire | P1 | 'repareren' = to repair. |
| `replit developer inhuren` | `replit developer for hire` | Phrase | Hire | P1 | 'inhuren' = to hire. |
| `replit developer gezocht` | `hire replit developer` | Exact | Hire | P1 | Needs `vacature` negatives — easily confused with job ads. |
| `replit app naar productie` | `replit app to production` | Phrase | Service | P1 | ⚠️ Manufacturing negatives (§9.4) are mandatory. |
| `replit app developer nederland` | `replit app developer` | Phrase | Hire | P2 | Them geo de tranh trung. |
| `replit bureau` | `replit agency` | Phrase | Hire | P2 | `bureau` = agency. The EN version measured 210 — under verification. |
| `replit productieklaar` | `replit production ready` | Phrase | Service | P1 | `productieklaar` = production-ready. |

#### RSA — `AG-REP-NL-Hire` (entirely in Dutch)

| # | Headline (Nederlands) | English meaning | Ch | Pin |
|---|---|---|---:|---|
| H1 | `Replit App Laten Afmaken?` | Want your Replit app finished? | 25 | **P1** |
| H2 | `Replit Developer Inhuren` | Hire a Replit developer | 24 | **P2** |
| H3 | `Vaste Prijs Vanaf €800` | Fixed price from €800 | 22 |  |
| H4 | `Live Binnen 1-3 Weken` | Live within 1-3 weeks | 21 |  |
| H5 | `Wij Maken Het Productieklaar` | We make it production-ready | 28 |  |
| H6 | `Je Frontend Blijft Staan` | Your frontend stays as it is | 24 |  |
| H7 | `Security En Betalingen` | Security and payments | 22 |  |
| H8 | `11+ Jaar Engineering` | 11+ years of engineering | 20 |  |
| H9 | `100% Eigendom Van Je Code` | 100% ownership of your code | 25 |  |
| H10 | `Geen Partner Van Replit` | Not affiliated with Replit | 23 |  |
| H11 | `Nederlandse Developers` | Dutch developers | 22 |  |
| H12 | `Gratis Deploy Review` | Free deploy review | 20 | **P3** |

| # | Description (Nederlands) | English meaning | Ch |
|---|---|---|---:|
| D1 | `Met Replit gebouwd maar niet live? Wij regelen deploy, security en hosting.` | Built with Replit but not live? We handle deploy, security and hosting. | 75 |
| D2 | `Van Replit Agent-prototype naar een app die je klanten echt kunnen gebruiken.` | From a Replit Agent prototype to an app your customers can actually use. | 77 |
| D3 | `Vaste prijs vanaf €800. Live in 1-3 weken. Je code blijft 100% van jou.` | Fixed price from €800. Live in 1-3 weeks. Your code stays 100% yours. | 71 |
| D4 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW. | 78 |

### 7.2. `AG-REP-NL-Problem` — 12 keywords · Max CPC €8.00

**Failures — Agent, secrets, database** · Landing page: `/nl/replit-app-werkt-niet`

| Keyword (Nederlands) | English meaning / original | Match | Intent | Priority | Note |
|---|---|---|---|---|---|
| `replit app werkt niet` | `replit app not working` | Phrase | Fix | P2 | 'werkt niet' = not working. |
| `replit deployment mislukt` | `replit deployment failed` | Phrase | Fix | P2 | 'mislukt' = failed. |
| `replit deployment foutmelding` | `replit deployment error` | Phrase | Fix | P2 | `foutmelding` = error message. |
| `replit database verbindingsfout` | `replit database connection error` | Phrase | Fix | P2 | `verbindingsfout` = connection error. |
| `replit agent werkt niet` | `replit agent not working` | Phrase | Fix | P3 | `agent` unchanged — feature name. |
| `replit secrets werken niet` | `replit secrets not working` | Phrase | Fix | P3 | `secrets` unchanged — Replit feature name. |
| `replit eigen domein` | `replit custom domain` | Phrase | Fix | P3 | `eigen domein` = custom domain. |
| `replit beveiliging` | `replit security` | Phrase | Security | P2 | `beveiliging` = security. |
| `replit werkt niet` | `replit not working` | Phrase | Fix | P3 | Short — Phrase only. |
| `replit agent loopt vast` | `replit agent stuck` | Phrase | Fix | P3 | `loopt vast` = gets stuck/hangs. Dutch idiom. |
| `replit app is langzaam` | `replit app slow` | Phrase | Fix | P3 | `langzaam` = slow. |
| `replit app crasht` | `replit app crashes` | Phrase | Fix | P3 | `crasht` = crashes. Dutch-ised verb. |

#### RSA — `AG-REP-NL-Problem` (entirely in Dutch)

| # | Headline (Nederlands) | English meaning | Ch | Pin |
|---|---|---|---:|---|
| H1 | `Replit App Werkt Niet?` | Replit app not working? | 22 | **P1** |
| H2 | `Wij Fixen Replit Apps` | We fix Replit apps | 21 | **P2** |
| H3 | `Agent Loopt Vast?` | Agent getting stuck? | 17 |  |
| H4 | `Deployment Mislukt?` | Deployment failed? | 19 |  |
| H5 | `Database Verbindingsfout?` | Database connection error? | 25 |  |
| H6 | `Secrets Werken Niet?` | Secrets not working? | 20 |  |
| H7 | `App Crasht Of Traag?` | App crashing or slow? | 20 |  |
| H8 | `Vaste Prijs Vanaf €800` | Fixed price from €800 | 22 |  |
| H9 | `Opgelost In Dagen` | Solved within days | 17 |  |
| H10 | `11+ Jaar Engineering` | 11+ years of engineering | 20 |  |
| H11 | `Geen Partner Van Replit` | Not affiliated with Replit | 23 |  |
| H12 | `Gratis Foutanalyse` | Free fault analysis | 18 | **P3** |

| # | Description (Nederlands) | English meaning | Ch |
|---|---|---|---:|
| D1 | `Werkt je Replit app niet? Wij vinden de oorzaak en lossen het definitief op.` | Replit app not working? We find the cause and fix it for good. | 76 |
| D2 | `Agent loopt vast, secrets werken niet, database valt weg? Wij fixen het.` | Agent stuck, secrets failing, database dropping out? We fix it. | 72 |
| D3 | `Vaste prijs vanaf €800. Opgelost in dagen. Je code blijft 100% van jou.` | Fixed price from €800. Solved within days. Your code stays 100% yours. | 71 |
| D4 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW. | 78 |

### 7.3. `AG-REP-NL-Cost` — 10 keywords · Max CPC €10.00

**Cost — Reserved VM, migration** · Landing page: `/nl/replit-hosting-kosten`

| Keyword (Nederlands) | English meaning / original | Match | Intent | Priority | Note |
|---|---|---|---|---|---|
| `replit reserved vm kosten` | `replit reserved vm cost` | Phrase | Cost | P1 | `kosten` = cost. Reserved VM unchanged — service tier name. |
| `replit autoscale versus reserved vm` | `replit autoscale vs reserved vm` | Phrase | Decision | P1 | Service tier names unchanged. |
| `replit deployment kosten` | `replit deployment cost` | Phrase | Cost | P1 | `kosten` = cost. |
| `replit te duur` | `replit pricing too expensive` | Phrase | Cost | P1 | `te duur` = too expensive. The strongest churn trigger. |
| `weg van replit` | `migrate off replit` | Phrase | Decision | P1 | ⚠️ Duplicate of the old NL set — pick one campaign. |
| `replit naar vercel exporteren` | `replit export to vercel` | Phrase | How-to | P2 | Platform name unchanged. |
| `replit code exporteren` | `replit export code` | Phrase | How-to | P2 | `exporteren` = to export. |
| `replit hosting kosten` | `replit hosting cost` | Phrase | Cost | P2 | `hosting` unchanged. |
| `replit alternatief voor productie` | `replit alternative production` | Phrase | Decision | P2 | `alternatief` = alternative. |
| `replit app naar eigen server` | `move replit app to own server` | Phrase | Service | P1 | `eigen server` = own server. |

#### RSA — `AG-REP-NL-Cost` (entirely in Dutch)

| # | Headline (Nederlands) | English meaning | Ch | Pin |
|---|---|---|---:|---|
| H1 | `Replit Te Duur Geworden?` | Replit become too expensive? | 24 | **P1** |
| H2 | `Reserved VM Kosten Hoog?` | Reserved VM costs high? | 24 | **P2** |
| H3 | `Wij Verhuizen Je App` | We move your app | 20 |  |
| H4 | `Naar Je Eigen Server` | To your own server | 20 |  |
| H5 | `Of Naar Vercel` | Or to Vercel | 14 |  |
| H6 | `Autoscale Of Reserved?` | Autoscale or Reserved? | 22 |  |
| H7 | `Geen Verrassingen Meer` | No more surprises | 22 |  |
| H8 | `Vaste Prijs Vanaf €800` | Fixed price from €800 | 22 |  |
| H9 | `Klaar In 1-3 Weken` | Done within 1-3 weeks | 18 |  |
| H10 | `Code 100% Van Jou` | Code 100% yours | 17 |  |
| H11 | `Geen Partner Van Replit` | Not affiliated with Replit | 23 |  |
| H12 | `Gratis Kostenanalyse` | Free cost analysis | 20 | **P3** |

| # | Description (Nederlands) | English meaning | Ch |
|---|---|---|---:|
| D1 | `Reserved VM rekent door terwijl niemand je app gebruikt. Dat kan anders.` | Reserved VM keeps billing while nobody uses your app. It doesn't have to. | 72 |
| D2 | `Wij verhuizen je Replit app naar hosting die je zelf beheert en betaalt.` | We move your Replit app to hosting you control and pay for yourself. | 72 |
| D3 | `Vaste prijs vanaf €800. Klaar in 1-3 weken. Je code blijft 100% van jou.` | Fixed price from €800. Done in 1-3 weeks. Your code stays 100% yours. | 72 |
| D4 | `Onafhankelijke studio van Manifera. 160+ projecten voor Vodafone, TNO en CFLW.` | Independent studio by Manifera. 160+ projects for Vodafone, TNO and CFLW. | 78 |

---

<a id="8"></a>
## 8. Dutch ad extensions

Shared across all three campaigns. Google Ads limits: sitelink text ≤ 25, each description line ≤ 35, callout ≤ 25, structured snippet ≤ 25 characters per value.

**Sitelink extensions**

| # | Link text (NL) | English meaning | Description line 1 (NL) | Description line 2 (NL) |
|---|---|---|---|---|
| 1 | `Prijzen` (7) | Pricing | `Vaste prijs vanaf €800` (22) | `Geen uurtarief, geen verrassing` (31) |
| 2 | `Werkwijze` (9) | How we work | `Intake, fix en live in 1-3 weken` (32) | `Drie stappen, vaste planning` (28) |
| 3 | `Beveiligingsaudit` (17) | Security audit | `Wij vinden wat AI-code achterlaat` (33) | `Rapport binnen enkele dagen` (27) |
| 4 | `Cases` (5) | Cases | `Vodafone, TNO, CFLW en meer` (27) | `160+ projecten opgeleverd` (25) |
| 5 | `Gratis Code Review` (18) | Free code review | `Stuur je repo, wij kijken mee` (29) | `Antwoord binnen 1 werkdag` (25) |
| 6 | `Over Ons` (8) | About us | `Onafhankelijke studio, Amsterdam` (32) | `Onderdeel van Manifera` (22) |

**Callout extensions** (≤ 25 characters)

| Callout (NL) | English meaning | Ch |
|---|---|---:|
| `Vaste prijs vanaf €800` | Fixed price from €800 | 22 |
| `Live in 1-3 weken` | Live in 1-3 weeks | 17 |
| `Code 100% van jou` | Code 100% yours | 17 |
| `11+ jaar ervaring` | 11+ years experience | 17 |
| `160+ projecten` | 160+ projects | 14 |
| `Kantoor in Amsterdam` | Amsterdam office | 20 |
| `Gratis intakegesprek` | Free intake call | 20 |
| `AVG-proof opgeleverd` | Delivered GDPR-proof | 20 |

**Structured snippet** — Header: `Diensten` (Services), ≤ 25 characters per value

| Value (NL) | English meaning | Ch |
|---|---|---:|
| `Beveiligingsaudit` | Security audit | 17 |
| `Betalingen koppelen` | Payment integration | 19 |
| `Hosting en deploy` | Hosting and deploy | 17 |
| `Code migratie` | Code migration | 13 |
| `Inlogsysteem` | Login system | 12 |
| `Database opzetten` | Database setup | 17 |
| `Performance fix` | Performance fix | 15 |
| `AVG-compliance` | GDPR compliance | 14 |
> 💡 **`AVG-proof opgeleverd` is the most valuable callout in the list.** AVG is the Dutch name for GDPR. Foreign competitors write "GDPR compliant" — Dutch users search for "AVG". That single word signals you are a local supplier.

---

<a id="9"></a>
## 9. Negative keywords

### 9.1. B1 Lovable — guarding against dictionary and lingerie queries

```
-bra          -bras         -lingerie     -ondergoed    -beha
-betekenis    -definitie    -synoniem     -vertaling    -uitspraak
-liedje       -songtekst    -film         -boek         -knuffel
-pop          -speelgoed    -baby         -huisdier     -hond
-kat          -naam         -namen        -loveable
```
> 🇳🇱 `ondergoed` (underwear) · `beha` (bra) · `betekenis` (meaning) · `definitie` (definition) · `synoniem` (synonym) · `vertaling` (translation) · `uitspraak` (pronunciation) · `liedje` (song) · `songtekst` (lyrics) · `boek` (book) · `knuffel` (plush toy) · `pop` (doll) · `speelgoed` (toy) · `huisdier` (pet) · `hond` (dog) · `kat` (cat) · `naam`/`namen` (name/names).

### 9.2. 🔴 B2 Bolt — the most important list here

**Taxi / ride-hailing / delivery**
```
-taxi         -taxis        -rit          -ritje        -ritten
-chauffeur    -bestuurder   -uber         -bolt driver  -rijden
-eten         -maaltijd     -bezorging    -bezorger     -koerier
-scooter      -step         -fiets        -ebike        -huren
-verhuur      -kortingscode -promocode    -tarief       -ritprijs
-app store    -play store   -app download -inloggen bolt
```
> 🇳🇱 `rit`/`ritje`/`ritten` (ride/s) · `bestuurder` (driver) · `rijden` (to drive) · `eten` (food) · `maaltijd` (meal) · `bezorging`/`bezorger` (delivery/courier) · `koerier` (courier) · `step` (kick scooter) · `fiets` (bicycle) · `huren`/`verhuur` (rent/rental) · `kortingscode` (discount code) · `tarief`/`ritprijs` (fare/ride price) · `inloggen` (to log in).

**Bolts / screws / hardware**
```
-schroef      -schroeven    -moer         -moeren       -bout
-bouten       -ring         -plug         -m8           -m10
-draadeind    -zeskant      -bouwmarkt    -gereedschap  -ijzerwaren
```
> 🇳🇱 `schroef`/`schroeven` (screw/s) · `moer`/`moeren` (nut/s) · `bout`/`bouten` (bolt/s) · `ring` (washer) · `plug` (wall plug) · `draadeind` (threaded rod) · `zeskant` (hex) · `bouwmarkt` (DIY store) · `gereedschap` (tools) · `ijzerwaren` (hardware).

**People & other brands**
```
-usain        -sprint       -olympisch    -atletiek     -record
-bliksem      -onweer       -threads      -stof         -disney
```
> 🇳🇱 `olympisch` (Olympic) · `atletiek` (athletics) · `bliksem` (lightning) · `onweer` (thunderstorm) · `stof` (fabric).

**Electric vehicles**
```
-ev           -laadpas      -laadstation  -opladen      -accu
-batterij     -motor        -auto         -voertuig
```
> 🇳🇱 `laadpas` (charging card) · `laadstation` (charging station) · `opladen` (to charge) · `accu`/`batterij` (battery) · `auto` (car) · `voertuig` (vehicle).

### 9.3. B3 Replit — the shortest list

```
-cursus       -opleiding    -leren        -les          -lessen
-tutorial     -handleiding  -school       -student      -huiswerk
-onderwijs    -gratis hosting             -100 days     -curriculum
```
> 🇳🇱 `cursus` (course) · `opleiding` (training) · `leren` (to learn) · `les`/`lessen` (lesson/s) · `handleiding` (manual) · `huiswerk` (homework) · `onderwijs` (education) · `gratis hosting` (free hosting).

### 9.4. Applied to all three campaigns

**Recruitment block — mandatory because of `gezocht` (§3.1)**
```
-vacature     -vacatures    -baan         -banen        -werk
-solliciteren -sollicitatie -cv           -salaris      -uurloon
-zzp tarief   -stage        -traineeship  -bijbaan
```
> 🇳🇱 `vacature/s` (job vacancy/ies) · `baan`/`banen` (job/s) · `werk` (work) · `solliciteren`/`sollicitatie` (to apply/application) · `salaris` (salary) · `uurloon` (hourly wage) · `zzp tarief` (freelance rate) · `stage` (internship) · `bijbaan` (side job).

**Free / DIY block**
```
-gratis       -zelf doen    -zelf maken   -template     -voorbeeld
-handleiding  -kraken       -gekraakt     -torrent      -download
```
> 🇳🇱 `gratis` (free) · `zelf doen`/`zelf maken` (do/make it yourself) · `voorbeeld` (example) · `handleiding` (manual) · `kraken`/`gekraakt` (to crack/cracked).

**Research / comparison block**
```
-reddit       -youtube      -github       -docs         -documentatie
-forum        -review       -beoordeling  -ervaringen
```
> 🇳🇱 `documentatie` (documentation) · `beoordeling` (review/rating) · `ervaringen` (experiences).

> ⚠️ **Think twice about `-review` and `-ervaringen`.** They block comparison queries, which can be prospects in the consideration stage. If `AG-LOV-NL-Migrate` shows good signal, remove both from B1.

**Manufacturing block — MANDATORY, 218 terms**

Four keywords contain `naar productie` / `productieklaar` (§3.3) and collide exactly with Dutch metalworking terminology. All 218 terms in 9 blocks, attached at **account level** (Shared Library → Negative keyword lists) rather than per campaign:

##### 9.4.1. Materials

```
-aluminium    -aluminum     -staal        -steel        -metaal
-metal        -rvs          -inox         -stainless    -koper
-copper       -messing      -brass        -titanium     -gietijzer
-kunststof    -plastic      -acryl        -acrylic      -plexiglas
-hout         -wood         -mdf          -composiet    -composite
-carbon       -glasvezel    -rubber       -schuim       -foam
```

##### 9.4.2. Machining & fabrication

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

##### 9.4.3. 3D printing / additive

```
-3d           -3d print     -3d-print     -3dprint      -3d printing
-3d printer   -printen      -filament     -resin        -pla
-abs          -petg         -sls          -sla          -fdm
-dlp          -additive     -sintering    -stereolithografie
-slicer       -cura         -nozzle       -printbed
```

> ⚠️ **Think carefully about `-3d` as a broad negative.** It blocks `3d` standing alone. If LaunchStudio has clients building apps with 3D models (configurators, viewers), drop `-3d` and keep only the two-word phrases.

##### 9.4.4. Physical prototyping — the most important block

```
-rapid prototyping        -prototyping service      -prototype fabrication
-prototype machining      -prototype parts          -hardware prototype
-physical prototype       -functional prototype     -prototype mold
-pcb                      -printed circuit          -breadboard
-enclosure                -housing                  -mockup model
-scale model              -maquette                 -proefmodel
-nulserie                 -pilot run                -tooling prototype
```

##### 9.4.5. Manufacturing companies

```
-manufacturer   -manufacturers  -manufacturing  -fabrikant      -fabrikanten
-maakindustrie  -maakbedrijf    -productiebedrijf -machinebouw  -machinefabriek
-toeleverancier -toelevering    -contract manufacturing         -oem
-odm            -assembly line  -productielijn  -seriematig     -serieproductie
-massaproductie -mass production -batch production -moq
-minimum order  -werkplaats     -smederij       -gieterij       -constructiebedrijf
```

##### 9.4.6. Buying/renting machinery

```
-machine kopen      -machines te koop   -machine te koop
-machinepark        -occasion           -tweedehands
-gebruikte machine  -machine huren      -verhuur
-onderhoud          -reparatie          -onderdelen
-gereedschap        -tooling kopen      -3d printer kopen
-laser kopen        -cnc kopen
```

##### 9.4.7. CAD/CAM software (a different software category)

```
-cad          -cam          -cadcam       -solidworks   -autocad
-fusion       -fusion 360   -freecad      -inventor     -catia
-creo         -mastercam    -nx           -sketchup     -rhino
-gcode        -g-code       -post processor             -dxf
-dwg          -step file    -iges         -stl
```

##### 9.4.8. Industry ERP vendors (people looking for competitors, not for you)

```
-mkg          -komdex       -snabbt       -halloy       -klaes
-reynapro     -logikal      -orgadata     -vtbo         -kozijncalculator
-paperless parts            -digifabster  -cloudnc      -proshop
-global shop
```

##### 9.4.9. Construction & facade building

```
-aannemer     -bouwbedrijf  -verbouwing   -renovatie    -bestek
-constructie  -staalconstructie           -kozijn       -kozijnen
-gevel        -gevelbouw    -facade       -dakkapel     -serre
-beglazing    -ramen        -deuren       -schuifpui
```


> 🇳🇱 **Key Dutch terms glossed:** `staal` (steel) · `metaal` (metal) · `rvs` (stainless) · `koper` (copper) · `messing` (brass) · `gietijzer` (cast iron) · `kunststof` (plastic) · `hout` (wood) · `glasvezel` (fibreglass) · `frezen` (milling) · `draaien` (turning) · `verspanen` (machining) · `lasersnijden` (laser cutting) · `buigen`/`zetten`/`kanten` (bending) · `lassen`/`laswerk` (welding) · `plaatwerk` (sheet metal) · `metaalbewerking` (metalworking) · `gieten` (casting) · `spuitgieten` (injection moulding) · `matrijs`/`matrijzen` (mould/s) · `stansen`/`ponsen` (stamping/punching) · `slijpen` (grinding) · `polijsten` (polishing) · `anodiseren` (anodising) · `poedercoaten` (powder coating) · `galvaniseren` (galvanising) · `stralen` (blasting) · `fabricage`/`fabricatie` (fabrication) · `printen` (printing) · `maquette` (scale model) · `proefmodel` (test model) · `nulserie` (pre-production run) · `fabrikant`/`fabrikanten` (manufacturer/s) · `maakindustrie` (manufacturing industry) · `maakbedrijf`/`productiebedrijf` (manufacturing company) · `machinebouw` (machine building) · `machinefabriek` (machine factory) · `toeleverancier`/`toelevering` (supplier/supply) · `productielijn` (production line) · `seriematig`/`serieproductie` (series production) · `massaproductie` (mass production) · `werkplaats` (workshop) · `smederij` (forge) · `gieterij` (foundry) · `constructiebedrijf` (structural engineering firm) · `kopen` (to buy) · `te koop` (for sale) · `machinepark` (machine fleet) · `occasion`/`tweedehands` (second-hand) · `huren`/`verhuur` (rent/rental) · `onderhoud` (maintenance) · `reparatie` (repair) · `onderdelen` (parts) · `gereedschap` (tools) · `kozijncalculator` (window frame calculator) · `aannemer` (contractor) · `bouwbedrijf` (construction firm) · `verbouwing`/`renovatie` (renovation) · `bestek` (tender specification) · `staalconstructie` (steel structure) · `kozijn`/`kozijnen` (window frame/s) · `gevel`/`gevelbouw` (facade/facade building) · `dakkapel` (dormer) · `serre` (conservatory) · `beglazing` (glazing) · `ramen` (windows) · `deuren` (doors) · `schuifpui` (sliding patio door).

### 9.5. Technical notes

1. **Negative keywords do NOT match close variants automatically.** Dutch forms plurals with `-en` and `-s`, so each must be entered separately: `-vacature` **and** `-vacatures`, `-schroef` **and** `-schroeven`, `-rit` **and** `-ritten`.
2. **Single words → negative broad · multi-word phrases → negative phrase.**
3. **Negative broad requires all words to appear together.** `-zzp tarief` as broad only blocks queries containing both words.
4. **Create 5 Shared Negative Lists:** NL-Lovable · NL-Bolt · NL-Replit · NL-Shared · Manufacturing.
5. **Dutch compounds are written as one word.** `beveiligingsaudit` is a single word. A `-audit` negative will **not** block it — but `-beveiligingsaudit` will not block `beveiliging audit` written apart either. Check both spellings in Search Terms.

---

<a id="10"></a>
## 10. Budget, rollout & KPIs

### 10.1. Budget — deliberately low

| Campaign | Keywords | Tier A (experiment) | Tier B (if volume exists) | Ceiling |
|---|---:|---:|---:|---:|
| B1-NL-Lovable | 32 | €40 | €80 | €150 |
| B2-NL-Bolt | 24 | €25 | €45 | €80 |
| B3-NL-Replit | 29 | €35 | €70 | €120 |
| **Total/month** | **85** | **€100** | **€195** | **€350** |

> 🔴 **Start at Tier A, €100/month, and no higher.** The Dutch keyword set carrying AI tool names measured 10 searches/month in the previous run. If this translated set behaves the same way, €100 is already more than enough. Only move to Tier B when `IS lost (budget)` exceeds 20% — meaning there is genuine demand being missed.

### 10.2. Six-week rollout

| Week | Task |
|---|---|
| **0** | Run Keyword Planner across the 85 keywords: paste `kp_upload_NL_translated.txt`, **Location = Netherlands, Language = Dutch**. If the total is under 100/month → launch only B1 at €50 and stop there |
| **0** | Build 8 `/nl/…` landing pages, or a minimum of 3 (one per campaign). Create the 5 Shared Negative Lists |
| **1** | Launch **B3-NL-Replit** first at Tier A. Cleanest name, no brand collision. Manual CPC |
| **2** | Launch **B1-NL-Lovable** at Tier A. Check Search Terms every second day |
| **3** | Launch **B2-NL-Bolt** at Tier A. Check Search Terms **daily**. If more than 30% of queries are taxi-related → switch off immediately |
| **4** | **Review 1.** Count impressions per ad group. Switch off every ad group with zero impressions after 14 days |
| **5** | Compare CTR and CPC for the `*-Problem` groups (Dutch) against their counterparts in the English branch. This is a direct test of the assumption that Dutch developers search errors in English |
| **6** | **Review 2.** Decide: keep everything · keep only the Hire/Cost/Migrate groups · or switch off entirely and consolidate into the English branch |

### 10.3. KPIs — different thresholds from the English plan

| Metric | Week 3 | Week 6 | Kill threshold |
|---|---|---|---|
| **Impressions** | > 0 in ≥ 5 of 8 ad groups | > 50/month per campaign | **0 impressions after 14 days = switch off the ad group** |
| **CPC** (Cost Per Click) | ≤ €8 | ≤ €6 | > €12 — anomalous at this volume |
| **CTR** (Click-Through Rate) | ≥ 6% | ≥ 9% | < 4% = the ad does not match the query |
| **Relevant query ratio** | ≥ 70% | ≥ 85% | **< 50% on B2 Bolt = switch off** |
| **QS** (Quality Score) | ≥ 5 | ≥ 6 | < 4 = the landing page is not native Dutch |

> 💡 **The most important metric in this plan is Impressions, not CPL.** The first question to answer is not "is this profitable" but **"does anyone type these words in Dutch at all"**. An ad group with zero impressions after 14 days has answered no — switch it off, do not raise bids.

### 10.4. The decisive experiment: a side-by-side language test

This is the greatest value in the plan, more than any revenue it might produce.

Run identical intent in both languages simultaneously and compare:

| Comparison pair | EN branch | NL branch (this plan) |
|---|---|---|
| Lovable failure | `lovable app not working` | `lovable app werkt niet` |
| Hiring for Replit | `hire replit developer` | `replit developer gezocht` |
| Replit cost | `replit pricing too expensive` | `replit te duur` |
| Bolt deployment | `bolt new not working` | `bolt new werkt niet` |

After six weeks, the NL/EN impression ratio settles the question that has been in dispute throughout: **which language Dutch speakers use when searching about AI tools**. That answer then guides every SEO and content decision, not just ads.

---

<a id="11"></a>
## 11. Pre-launch checklist

### Verify volume — before anything else

- [ ] Paste `kp_upload_NL_translated.txt` into Keyword Planner, **Location = Netherlands, Language = Dutch**
- [ ] Record the total volume across all 85 keywords. **If under 100/month → launch only B1 at €50 and drop B2 and B3**
- [ ] Compare volume for each NL/EN pair in §10.4 — this is the single most valuable data point
- [ ] Pull the `Top of page bid (low/high)` column to establish real CPC

### Landing pages

- [ ] At minimum 3 `/nl/…` pages, one per campaign. Ideally all 8
- [ ] All content in **native Dutch, not machine translation** — Quality Score depends directly on this
- [ ] Each page carries **one independence statement**: *"LaunchStudio is een onafhankelijke studio en geen partner van [tool]."* (*LaunchStudio is an independent studio and not a partner of [tool].*)
- [ ] Contact form, autoresponder and the person replying are all in Dutch
- [ ] Use **AVG**, not **GDPR**
- [ ] The `/nl/lovable-tanstack-migratie` page explains the 2026-05-13 milestone in Dutch

### Inside Google Ads

- [ ] **Language = Dutch, Dutch only.** Do not add English — it would compete internally with the EN branch
- [ ] Location = Netherlands, **"Presence"** mode
- [ ] Create **5 Shared Negative Lists**: NL-Lovable · NL-Bolt · NL-Replit · NL-Shared · **Manufacturing (218 terms)**
- [ ] Attach the **Manufacturing** list to all three campaigns — 4 keywords contain `naar productie` (§3.3)
- [ ] Attach the **recruitment** block (`vacature`, `baan`, `salaris`…) to all three — because of `gezocht` (§3.1)
- [ ] Set `lovable developer gezocht` and `replit developer gezocht` to **Exact match**
- [ ] Set `bolt new app developer` to **Exact match** or drop it entirely in phase 1
- [ ] Confirm **no keyword is bare `bolt`**
- [ ] Remove the 4 duplicate keywords from campaign N2-NL-AI-Tools (§4) — or switch N2 off entirely
- [ ] Enter plural variants separately for every negative (`-vacature` **and** `-vacatures`)
- [ ] Bid strategy = **Manual CPC**
- [ ] Ad rotation = **"Do not optimize"**
- [ ] Load the full **12 headlines + 4 descriptions** for each ad group
- [ ] Load 6 sitelinks · 8 callouts · 1 structured snippet (§8)
- [ ] Schedule Search Terms reviews: **daily for B2**, every second day for B1 and B3

---

## 📌 Summary

> **The same 85 keywords, the same 8 ad groups, but entirely in Dutch — keyword and ad language matched absolutely.**
>
> Not everything gets translated: verbs and commercial actions go into Dutch (`werkt niet`, `inhuren`, `te duur`, `kosten`), while product names and developer terminology stay as they are (`deployment`, `RLS`, `SSR`, `CORS`, `Reserved VM`). Three places needed genuinely native phrasing: `witte pagina` rather than `blanco pagina`, `agent loopt vast` rather than `agent vast`, and `fix bolt app` replaced outright with `app gebouwd met bolt new laten afmaken` because the collision with the taxi brand is otherwise unavoidable.
>
> **Opening budget €100/month, deliberately low.** The previous measurement showed Dutch keywords carrying AI tool names drawing just 10 searches/month. This plan is a cheap land-grab experiment, not a primary channel.
>
> **The deciding metric is Impressions, not CPL.** The first question is whether anyone types these words in Dutch at all. Any ad group at zero impressions after 14 days gets switched off.
>
> The greatest value here may not be revenue but the **side-by-side language test in §10.4** — after six weeks you have a definitive answer to which language Dutch speakers use for AI tools, and that answer guides both SEO and content from then on.

---

*85 Dutch keywords (translated 1:1 from the English set) · 3 campaigns · 8 ad groups · 162 Dutch ad assets verified by script — 96 headlines (longest 28/30) · 32 descriptions (longest 80/90) · 6 sitelinks · 8 callouts · 8 structured snippets — **0 Google Ads character-limit violations***

*Keyword file: `keyword_seeds_3_ai_brands_NL_translated.csv` · Keyword Planner paste file: `kp_upload_NL_translated.txt`*

*🇳🇱 All keywords and ad copy remain in Dutch, with English meanings in the adjacent column. **Do not translate when entering into Google Ads.***
