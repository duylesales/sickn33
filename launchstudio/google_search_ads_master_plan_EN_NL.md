# 🎯 Google Search Ads — Master Plan
## LaunchStudio.eu · 🇬🇧 English ⟷ 🇳🇱 Nederlands

> **Scope / Reikwijdte:** Google Search only. For multi-channel see [`paid_ads_plan.md`](paid_ads_plan.md).
> **Date / Datum:** 2026-09-24 · **Markets / Markten:** NL/BE (primary) + EU-EN (secondary)
> **Status:** Execution plan — §3 must be completed before the first euro is spent.
> **Bron VN / Vietnamese source:** [`google_search_ads_master_plan.md`](google_search_ads_master_plan.md)

---

## 📑 Contents / Inhoud

| § | English | Nederlands |
|---|---|---|
| [1](#1) | Executive summary — 6 decisions | Samenvatting — 6 beslissingen |
| [2](#2) | Unit economics | Kosteneconomie per klant |
| [3](#3) | Blocking prerequisites | Blokkerende randvoorwaarden |
| [4](#4) | Account architecture | Accountstructuur |
| [5](#5) | Campaigns in detail | Campagnes in detail |
| [6](#6) | Negative keywords | Uitsluitingszoekwoorden |
| [7](#7) | Conversion tracking | Conversiemeting |
| [8](#8) | Ad extensions | Advertentie-extensies |
| [9](#9) | Budget & 90-day roadmap | Budget & 90-dagen routekaart |
| [10](#10) | KPIs, glossary & thresholds | KPI's, begrippenlijst & drempels |
| [11](#11) | Risks | Risico's |
| [12](#12) | Day-1 checklist | Checklist dag 1 |

---

<a id="1"></a>
## 1. Executive Summary — 6 Decisions / Samenvatting — 6 Beslissingen

### ① Search budget is €300–900/month, not €5,000 / Zoekbudget is €300–900 per maand, niet €5.000

**EN —** This contradicts [`paid_ads_plan.md`](paid_ads_plan.md), which proposed €3,795/month for Google Search EN. The reason: **this account is capped by search volume, not by money.** At an estimated volume for the three AI-tool clusters, with 65% impression share and 6–9% CTR, you can only buy **15–70 clicks per month**. At €8–14 CPC that is €120–1,000. Spending €5,000 means €4,000 cannot be spent — or worse, Google spends it on irrelevant queries. Full calculation in §2.2.

**NL —** Dit spreekt [`paid_ads_plan.md`](paid_ads_plan.md) tegen, dat €3.795 per maand voorstelde voor Google Search EN. De reden: **dit account wordt begrensd door zoekvolume, niet door geld.** Bij het geschatte volume voor de drie AI-tool-clusters, met 65% vertoningsaandeel en 6–9% CTR, kun je maar **15–70 klikken per maand** kopen. Bij €8–14 CPC is dat €120–1.000. €5.000 inzetten betekent dat €4.000 niet uitgegeven kan worden — of erger, dat Google het aan irrelevante zoekopdrachten besteedt. Volledige berekening in §2.2.

### ② Run only 60 of 129 keywords / Gebruik slechts 60 van de 129 zoekwoorden

**EN —** Campaigns C1–C3 take only keywords with **Hire, Service, Decision or Compliance** intent (55 keywords), plus 5 Fix/How-to keywords isolated in test campaign C5 with a hard kill threshold. The remaining 25 Fix-intent keywords are **not** advertised — they belong to SEO. Someone typing `lovable custom domain not working` wants a free fix in five minutes, not an €800–7,500 engagement.

**NL —** Campagnes C1–C3 gebruiken alleen zoekwoorden met **Hire-, Service-, Decision- of Compliance-intentie** (55 zoekwoorden), plus 5 Fix/How-to-zoekwoorden die apart staan in testcampagne C5 met een harde stopdrempel. De overige 25 Fix-zoekwoorden worden **niet** geadverteerd — die horen bij SEO. Iemand die `lovable custom domain not working` typt wil binnen vijf minuten een gratis oplossing, geen traject van €800–7.500.

### ③ Never broad-match anything containing `lovable` / Gebruik nooit breed zoeken op `lovable`

**EN —** `lovable` is both a common English adjective and a global lingerie brand. The 149,500/month volume Semrush reports is almost entirely irrelevant to LaunchStudio. This repeats the `day ai` = 201,000 trap already identified in `paid_ads_plan.md` §3.1. See the negative list in §6.1.

**NL —** `lovable` is zowel een gangbaar Engels bijvoeglijk naamwoord als een wereldwijd lingeriemerk. Het volume van 149.500 per maand dat Semrush meldt is vrijwel volledig irrelevant voor LaunchStudio. Dit herhaalt de `day ai`-val van 201.000 die al in `paid_ads_plan.md` §3.1 werd vastgesteld. Zie de uitsluitingslijst in §6.1.

### ④ Two landing pages must exist first / Twee landingspagina's zijn eerst nodig

**EN —** The site is currently one page with anchors. The highest-value campaign (Security & Cleanup) has nowhere to send traffic. See §3.

**NL —** De site is nu één pagina met ankers. De campagne met de hoogste waarde (Security & Cleanup) heeft geen bestemming voor verkeer. Zie §3.

### ⑤ Survival threshold: ≥5% landing page conversion and ≥40% close rate / Overlevingsdrempel

**EN —** At 3% conversion (the KPI target in the previous plan) and €10 CPC, **the model loses money**. Table in §2.3.

**NL —** Bij 3% conversie (de KPI-doelstelling in het vorige plan) en €10 CPC **verliest het model geld**. Tabel in §2.3.

### ⑥ C6 Migration — the only legitimate way to raise the spend ceiling / de enige manier om het bestedingsplafond te verhogen

**EN —** §2.2 concludes the account is volume-capped, and the only way to spend more is to **widen the keyword surface**. Changelog mining ([`keyword_idea_playbook.md`](keyword_idea_playbook.md)) produced 78 new keywords, of which **21 qualify for paid search**.

The strongest finding: **Lovable switched its default stack to TanStack Start** (13 May 2026) and **does not auto-migrate older projects**. Every project created before May 2026 still runs the old stack without server-side rendering. Competitor `nextlovable.com` already sells **$199–299 audits** for exactly this, across three dedicated landing pages — proof that people are paying.

Budget: €900 → **€1,080/month**, still below the €1,300 ceiling.

**NL —** §2.2 concludeert dat het account door volume wordt begrensd, en dat de enige manier om meer uit te geven is het **zoekwoordoppervlak te verbreden**. Changelog-onderzoek ([`keyword_idea_playbook.md`](keyword_idea_playbook.md)) leverde 78 nieuwe zoekwoorden op, waarvan er **21 geschikt zijn voor betaald zoeken**.

De belangrijkste vondst: **Lovable is overgestapt op TanStack Start als standaard** (13 mei 2026) en **migreert bestaande projecten niet automatisch**. Elk project van vóór mei 2026 draait nog op de oude stack zonder server-side rendering. Concurrent `nextlovable.com` verkoopt hier al **audits van $199–299** voor, verspreid over drie aparte landingspagina's — bewijs dat mensen ervoor betalen.

Budget: €900 → **€1.080 per maand**, nog steeds onder het plafond van €1.300.

---

<a id="2"></a>
## 2. Unit Economics / Kosteneconomie per Klant

**EN —** This section answers the only question that matters before spending: *is paid search profitable for this service?*

**NL —** Dit hoofdstuk beantwoordt de enige vraag die telt vóór besteding: *is betaald zoeken rendabel voor deze dienst?*

### 2.1. Deal value / Orderwaarde

| Package / Pakket | Range | Average / Gemiddeld |
|---|---|---:|
| Launch Ready | €800–3,500 | **€2,150** |
| Launch & Grow | €2,500–7,500 | **€5,000** *(+ €49/mo hosting)* |
| **Conservative blend / Voorzichtige mix** | | **€2,500** |

### 2.2. 🔴 Spend ceiling is set by volume / Bestedingsplafond wordt bepaald door volume

```
Max spend per month = Volume × %ads-suitable-kw × Impression Share × CTR × CPC
Max besteding per maand = Volume × %geschikte-zw × Vertoningsaandeel × CTR × CPC
```

| Market | Est. volume/mo | × 40% suitable | × 65% IS | × CTR 6–9% | **× CPC €8–14** |
|---|---:|---:|---:|---:|---:|
| NL/BE | 60–250 | 24–100 | 16–65 | 1–6 clicks | **€7–82** |
| EU-EN | 900–2,800 | 360–1,120 | 234–728 | 14–66 clicks | **€112–917** |
| **Total** | | | | **15–72 clicks** | **€120–1,000** |

> **EN — Source of the volume estimate:** `seo_geo_plan_production_keywords.md` estimates 200–600 searches/month in NL across 14 production keywords. `paid_ads_plan.md` cleaned the existing CSV down to ~13,000/month for the full English set. The three new clusters are narrower. **These are estimates, not measurements — verify in Keyword Planner (§12).**
>
> **NL — Bron van de volumeschatting:** `seo_geo_plan_production_keywords.md` schat 200–600 zoekopdrachten per maand in NL over 14 productiezoekwoorden. `paid_ads_plan.md` schoonde de bestaande CSV op tot ~13.000 per maand voor de volledige Engelse set. De drie nieuwe clusters zijn smaller. **Dit zijn schattingen, geen metingen — verifieer in Keyword Planner (§12).**

**Three consequences / Drie gevolgen:**

1. **EN —** €300–900/month is the right range. Above that the money cannot be spent. · **NL —** €300–900 per maand is de juiste bandbreedte. Daarboven kan het geld niet worden besteed.
2. **EN —** To spend more, widen the keyword surface — do not raise bids. · **NL —** Om meer te besteden: verbreed het zoekwoordoppervlak — verhoog niet de biedingen.
3. **EN —** Do not use Maximize Conversions early. At 15–70 clicks/month Google needs 3–6 months of data. · **NL —** Gebruik Maximaliseer conversies niet te vroeg. Bij 15–70 klikken per maand heeft Google 3–6 maanden data nodig.

### 2.3. 🔴 Sensitivity: what conversion rate is required? / Gevoeligheid: welke conversieratio is nodig?

```
CAC = CPC ÷ (Landing page conversion rate × Close rate)
```

**EN —** Benchmarks at €2,500 average deal and an assumed 50% gross margin: healthy CAC ≤ **€625** (25% of revenue) · break-even CAC **€1,250** · above that, a loss on the first deal.

**NL —** Referentiepunten bij €2.500 gemiddelde order en een aangenomen brutomarge van 50%: gezonde CAC ≤ **€625** (25% van de omzet) · break-even CAC **€1.250** · daarboven verlies op de eerste order.

| CPC | LP conv. | Close rate | **CAC** | Verdict / Oordeel |
|---:|---:|---:|---:|---|
| €8 | 3% | 25% | €1,067 | 🟡 Tight / Krap |
| €8 | 3% | 40% | €667 | 🟡 Tight / Krap |
| €8 | 5% | 25% | €640 | 🟡 Tight / Krap |
| €8 | **5%** | **40%** | **€400** | ✅ OK |
| €8 | 8% | 25% | €400 | ✅ OK |
| €10 | **3%** | **25%** | **€1,333** | 🔴 Loss / Verlies |
| €10 | 3% | 40% | €833 | 🟡 Tight / Krap |
| €10 | 5% | 25% | €800 | 🟡 Tight / Krap |
| €10 | **5%** | **40%** | **€500** | ✅ OK |
| €10 | 8% | 25% | €500 | ✅ OK |
| €14 | 3% | 25% | €1,867 | 🔴 Heavy loss / Fors verlies |
| €14 | 8% | 40% | €438 | ✅ OK |

**Three conclusions / Drie conclusies:**

1. **EN —** The ">3% landing page conversion" target in `paid_ads_plan.md` §12 is **too low** for this model. Raise it to **≥5%**. · **NL —** Het doel van ">3% landingspaginaconversie" in `paid_ads_plan.md` §12 is **te laag**. Verhoog naar **≥5%**.
2. **EN —** Close rate is a stronger lever than CPC. Moving 25% → 40% cuts CAC by 37%. Investing in the sales process beats bid optimisation. · **NL —** Closingratio is een sterkere hefboom dan CPC. Van 25% naar 40% verlaagt de CAC met 37%. Investeren in het verkoopproces levert meer op dan biedoptimalisatie.
3. **EN —** If only Package 1 (€2,150) sells, margins are thin. Ads should open the relationship; **LTV** justifies the CAC, not the first invoice. · **NL —** Als alleen Pakket 1 (€2.150) verkoopt, is de marge dun. Advertenties openen de relatie; **LTV** rechtvaardigt de CAC, niet de eerste factuur.

### 2.4. Targets / Doelstellingen

| Metric / Maatstaf | Target / Doel |
|---|---|
| Average CPC | ≤ €10 |
| Landing page conversion | **≥ 5%** |
| Lead → customer / Lead → klant | ≥ 30% |
| CAC | ≤ €625 |
| Leads/month · Leads per maand | 3–8 |
| Customers/month · Klanten per maand | **1–3** |

---

<a id="3"></a>
## 3. Blocking Prerequisites / Blokkerende Randvoorwaarden

**EN —** Do not launch any campaign until all six are done. Each one is a direct cause of wasted spend.
**NL —** Start geen enkele campagne voordat alle zes gereed zijn. Elk punt is een directe oorzaak van verspilling.

| # | Task / Taak | Why blocking / Waarom blokkerend |
|---|---|---|
| **1** | Build `/en/ai-code-security-audit` | **EN —** C3 has no destination. Sending `vibe code audit` traffic to a general homepage lowers Quality Score and raises CPC 30–50%. · **NL —** C3 heeft geen bestemming. Verkeer naar een algemene homepage verlaagt de kwaliteitsscore en verhoogt de CPC met 30–50%. |
| **2** | Build `/en/from-prototype-to-production` + `/nl/van-prototype-naar-productie` | Destination for C1, C2 · Bestemming voor C1, C2 |
| **3** | Install GA4 + 3 conversion events: `calculator_complete`, `contact_form_submit`, `call_booked` | **EN —** No tracking = no idea which campaign is profitable. · **NL —** Geen meting = geen idee welke campagne rendabel is. |
| **4** | Import conversions into Google Ads, mark as Primary | Required for reporting and bidding · Nodig voor rapportage en bieden |
| **5** | Add `Organization` schema; fix author schema currently reading `"phu.lt"` | **EN —** The 2026-07-31 audit found no `Organization` schema anywhere. · **NL —** De audit van 31-07-2026 vond nergens `Organization`-schema. |
| **6** | Create shared negative keyword lists (§6) **before** any campaign goes live | **EN —** The `lovable` lingerie/dictionary trap burns budget on day one. · **NL —** De `lovable`-val (lingerie/woordenboek) verbrandt het budget op dag één. |

> **EN —** Estimated time: 1–2 weeks with a developer. Landing pages are the long pole. If urgent, C1 (NL) may launch first since `/nl/van-prototype-naar-productie` is closest to existing homepage content. **C3 must not launch before its page exists.**
>
> **NL —** Geschatte doorlooptijd: 1–2 weken met een ontwikkelaar. De landingspagina's kosten de meeste tijd. Bij haast mag C1 (NL) eerst starten, omdat `/nl/van-prototype-naar-productie` het dichtst bij de huidige homepage ligt. **C3 mag niet starten vóór die pagina bestaat.**

---

<a id="4"></a>
## 4. Account Architecture / Accountstructuur

### 4.1. Design principles / Ontwerpprincipes

1. **EN —** One ad group = one intent. · **NL —** Eén advertentiegroep = één intentie.
2. **EN —** One ad group = one landing page. This determines message match. · **NL —** Eén advertentiegroep = één landingspagina. Dit bepaalt de boodschapafstemming.
3. **EN —** Separate NL and EN into different **campaigns**, not ad groups — otherwise English volume absorbs the Dutch budget. · **NL —** Scheid NL en EN in verschillende **campagnes**, niet advertentiegroepen — anders slokt Engels volume het Nederlandse budget op.
4. **EN —** Brand campaign separate, small budget, Target Impression Share 95–100%. · **NL —** Merkcampagne apart, klein budget, doelvertoningsaandeel 95–100%.

### 4.2. Structure / Structuur

```
LaunchStudio ACCOUNT
│
├── C1 · LS-Search-NL-Service           [NL/BE · Dutch · €200/mo]
│   ├── AG-NL-Rescue        (6 kw)  → /nl/van-prototype-naar-productie
│   ├── AG-NL-Security      (6 kw)  → /nl/beveiligingsaudit-ai-app
│   └── AG-NL-Vibe          (3 kw)  → /nl/van-prototype-naar-productie
│
├── C2 · LS-Search-EN-Hire              [EU-EN · English · €250/mo]
│   ├── AG-LOV-Hire         (10 kw) → /en/from-prototype-to-production
│   ├── AG-VIBE-Hire        (6 kw)  → /en/from-prototype-to-production
│   └── AG-TOOL-Hire        (7 kw)  → /en/from-prototype-to-production
│
├── C3 · LS-Search-EN-Security          [EU-EN · English · €300/mo]
│   ├── AG-SEC-Cleanup      (10 kw) → /en/ai-code-security-audit
│   ├── AG-SEC-Audit        (7 kw)  → /en/ai-code-security-audit
│   ├── AG-SEC-Tool         (12 kw) → /en/ai-code-security-audit
│   └── AG-SEC-Compliance   (3 kw)  → /en/ai-code-security-audit
│
├── C4 · LS-Search-Brand                [NL+EU · both · €50/mo]
│   └── AG-Brand            (4 kw)  → /en/ or /
│
├── C5 · LS-Search-EN-FixTest           [EU-EN · OPTIONAL · €100/mo]
│   └── AG-FIX-Test         (5 kw exact) → /en/from-prototype-to-production
│       ⚠️ Only after C2/C3 stable 4 weeks. Kill if CPL > €400.
│
└── C6 · LS-Search-EN-Migration         [EU-EN · €180/mo · NEW]
    ├── AG-MIG-TanStack     (6 kw)  → /en/lovable-tanstack-migration
    ├── AG-MIG-Service      (4 kw)  → /en/from-prototype-to-production
    └── AG-MIG-Platform     (6 kw)  → /en/from-prototype-to-production
```

**Total / Totaal: €1,080/month** — below the €1,300 volume ceiling in §2.2.

---

<a id="5"></a>
## 5. Campaigns in Detail / Campagnes in Detail

> **EN — RSA rules applied throughout:** headlines ≤ **30 characters**, descriptions ≤ **90 characters**, as required by Google Ads. Every line below has been character-counted in both languages. Counts shown in the `Ch` column.
>
> **NL — RSA-regels overal toegepast:** koppen ≤ **30 tekens**, beschrijvingen ≤ **90 tekens**, conform de eisen van Google Ads. Elke regel hieronder is in beide talen geteld. Aantallen in de kolom `Ch`.

### 5.1. C1 · `LS-Search-NL-Service` — €200/month (€6.50/day)

**EN —** Highest priority. This is LaunchStudio's home market, CPCs are lower, and competition for terms like `code audit laten uitvoeren` is close to zero.

**NL —** Hoogste prioriteit. Dit is de thuismarkt van LaunchStudio, de CPC's liggen lager en de concurrentie op termen als `code audit laten uitvoeren` is vrijwel nul.

| Ad group | Keywords | Max CPC | Daily | Landing page |
|---|---|---:|---:|---|
| `AG-NL-Rescue` | `"prototype naar productie"`, `"ai app laten bouwen"`, `"ai app laten afmaken"`, `"mvp laten bouwen"`, `"prototype live zetten"`, `"app productieklaar maken"` | €6.00 | €3.00 | `/nl/van-prototype-naar-productie` |
| `AG-NL-Security` | `"beveiligingsaudit webapplicatie"`, `"code audit laten uitvoeren"`, `"security audit software laten doen"`, `"avg compliance app"`, `"pentest webapplicatie"`, `"applicatie beveiliging laten testen"` | €7.00 | €2.50 | `/nl/beveiligingsaudit-ai-app` |
| `AG-NL-Vibe` | `"vibe coding nederland"`, `"vibe coding beveiliging"`, `"vibe coding uitbesteden"` | €5.00 | €1.00 | `/nl/van-prototype-naar-productie` |

#### RSA — `AG-NL-Rescue`

| # | 🇬🇧 English Headline | Ch | 🇳🇱 Nederlandse Kop | Ch | Pin |
|---|---|---:|---|---:|---|
| H1 | `Need Your MVP Launched?` | 23 | `MVP Laten Bouwen?` | 17 | **P1** |
| H2 | `Prototype → Production Fast` | 27 | `Wij Maken Het Launch-Ready` | 26 | **P2** |
| H3 | `Fixed Price From €800` | 21 | `Vaste Prijs Vanaf €800` | 22 | |
| H4 | `Live in Just 1-3 Weeks` | 22 | `Live Binnen 1-3 Weken` | 21 | |
| H5 | `No Rebuild — We Fix & Ship` | 26 | `Geen Herbouw — Wij Fixen` | 24 | |
| H6 | `Security & Hosting Included` | 27 | `Beveiliging & Hosting Geregeld` | 30 | |
| H7 | `11+ Years Engineering Exp.` | 26 | `11+ Jaar Engineering Ervaring` | 29 | |
| H8 | `You Keep 100% of Your Code` | 26 | `100% Eigendom Van Je Code` | 25 | |
| H9 | `Stripe, Auth & DB Handled` | 25 | `Stripe, Auth & DB Inbegrepen` | 28 | |
| H10 | `Get a Free Quote Today` | 22 | `Gratis Offerte Binnen 1 Dag` | 27 | **P3** |

| # | 🇬🇧 English Description | Ch | 🇳🇱 Nederlandse Beschrijving | Ch |
|---|---|---:|---|---:|
| D1 | `AI prototype ready but not live? We fix security, hosting & Stripe. Request a quote!` | 84 | `AI-prototype klaar maar niet live? We fixen security, hosting & Stripe. Vraag offerte!` | 86 |
| D2 | `Fixed price from €800, live in 1-3 weeks. All code stays 100% yours. Start immediately!` | 87 | `Vaste prijs vanaf €800, live in 1-3 weken. Alle code blijft 100% van jou. Start direct!` | 87 |
| D3 | `Agency charges €50K to rebuild? We keep your frontend and only fix what is needed.` | 82 | `Bureau rekent €50K voor herbouw? Wij behouden je frontend en fixen enkel wat nodig is.` | 86 |

> ⚠️ **EN —** All Dutch copy must be reviewed by a native speaker before launch. · **NL —** Alle Nederlandse teksten moeten vóór livegang door een moedertaalspreker worden nagelezen.

---

### 5.2. C2 · `LS-Search-EN-Hire` — €250/month (€8/day)

| Ad group | Keywords | Max CPC | Daily |
|---|---|---:|---:|
| `AG-LOV-Hire` | `"fix lovable app"`, `"lovable developer for hire"`, `"lovable developer"`, `[hire lovable developer]`, `"lovable app development service"`, `"take my lovable app to production"`, `"lovable app production ready"`, `"finish my lovable app"`, `"lovable app agency"`, `"lovable freelancer"` | €10.00 | €3.50 |
| `AG-VIBE-Hire` | `"hire vibe coding developer"`, `"vibe coding agency"`, `"fix my vibe coded app"`, `"vibe coding help"`, `"vibe coding consultant"`, `"vibe coding development service"` | €10.00 | €3.00 |
| `AG-TOOL-Hire` | `"fix bolt app"`, `"fix replit app"`, `"bolt app developer"`, `"replit app to production"`, `"v0 to production"`, `"base44 to production"`, `"figma make to production"` | €8.00 | €1.50 |

#### ⚠️ 5.2.1. The Fiverr problem / Het Fiverr-probleem

**EN —** SERPs and marketplaces for `fix lovable app` and `fix bolt app` are dominated by **Fiverr/Upwork gigs at $10–30**. LaunchStudio sells at €800–7,500 — a 30–200× difference. If the ad copy only says *"we fix your Lovable app"*, you are inviting a price comparison you will lose.

Ad copy must do three things, in order:
1. **Reframe the problem** from "fixing a bug" to "security risk and inability to go live"
2. **Anchor on evidence** — research cited by Superblocks scanned 1,645 public Lovable projects and found ~170 (10.3%) with inadequate Row Level Security, exposing 303 endpoints containing names, emails, phone numbers, addresses, payment data and third-party API keys
3. **Lean on the Manifera entity** — 11+ years, 160+ projects, clients including Vodafone, TNO and CFLW

**NL —** Zoekresultaten en marktplaatsen voor `fix lovable app` en `fix bolt app` worden gedomineerd door **Fiverr/Upwork-opdrachten van $10–30**. LaunchStudio verkoopt voor €800–7.500 — een verschil van 30–200×. Als de advertentietekst alleen zegt *"we fix your Lovable app"*, nodig je uit tot een prijsvergelijking die je verliest.

De advertentietekst moet drie dingen doen, in deze volgorde:
1. **Herdefinieer het probleem** van "een bug oplossen" naar "beveiligingsrisico en niet live kunnen"
2. **Veranker met bewijs** — onderzoek aangehaald door Superblocks scande 1.645 openbare Lovable-projecten en vond er ~170 (10,3%) met ontoereikende Row Level Security, waarbij 303 endpoints namen, e-mailadressen, telefoonnummers, adressen, betaalgegevens en API-sleutels van derden blootlegden
3. **Leun op de entiteit Manifera** — 11+ jaar, 160+ projecten, klanten als Vodafone, TNO en CFLW

#### RSA — `AG-LOV-Hire`

| # | 🇬🇧 English Headline | Ch | 🇳🇱 Nederlandse Kop | Ch | Pin |
|---|---|---:|---|---:|---|
| H1 | `Lovable App Stuck in Preview?` | 29 | `Lovable App Niet Live?` | 22 | **P1** |
| H2 | `We Fix Security, Not Just Bugs` | 30 | `Wij Fixen Security, Niet Bugs` | 29 | **P2** |
| H3 | `1 in 10 Lovable Apps Leak Data` | 30 | `1 op 10 Lovable Apps Lekt Data` | 30 | |
| H4 | `Fixed Price From €800` | 21 | `Vaste Prijs Vanaf €800` | 22 | |
| H5 | `Live in 1-3 Weeks` | 17 | `Live Binnen 1-3 Weken` | 21 | |
| H6 | `We Keep Your Frontend` | 21 | `Je Frontend Blijft Intact` | 25 | |
| H7 | `Backed by 11+ Yrs Engineering` | 29 | `11+ Jaar Engineering Ervaring` | 29 | |
| H8 | `You Own 100% of the Code` | 24 | `100% Eigendom Van Je Code` | 25 | |
| H9 | `Trusted by Vodafone & TNO` | 25 | `Vertrouwd Door Vodafone & TNO` | 29 | |
| H10 | `Get a Free Code Review` | 22 | `Gratis Code Review` | 18 | **P3** |

| # | 🇬🇧 English Description | Ch | 🇳🇱 Nederlandse Beschrijving | Ch |
|---|---|---:|---|---:|
| D1 | `A $25 gig fixes a bug. We fix the RLS gap that leaks your users' data. Free review.` | 83 | `Een goedkope fix lost een bug op. Wij fixen het RLS-lek in je data. Gratis review.` | 82 |
| D2 | `Fixed price from €800. Live in 1-3 weeks. Your frontend untouched, code 100% yours.` | 83 | `Vaste prijs vanaf €800. Live in 1-3 weken. Je frontend blijft, code 100% van jou.` | 81 |
| D3 | `Built by Manifera engineers — 160+ projects for Vodafone, TNO, CFLW. Get a quote.` | 81 | `Gebouwd door Manifera-engineers — 160+ projecten voor Vodafone, TNO en CFLW.` | 76 |

> ⚠️ **EN —** `H1` previously read *"Lovable App Not Production Ready?"* — **33 characters, over the 30-character limit.** Corrected above. · **NL —** `H1` luidde eerder *"Lovable App Not Production Ready?"* — **33 tekens, boven de limiet van 30.** Hierboven gecorrigeerd.

---

### 5.3. C3 · `LS-Search-EN-Security` — €300/month (€10/day)

**EN —** Highest-value campaign. `vibe coding cleanup specialist` has **at least four agencies with dedicated landing pages** (Redwerk, Suffescom, ThirdRock, AleaIT) — someone is paying to rank, which means someone is buying.

**NL —** Campagne met de hoogste waarde. Voor `vibe coding cleanup specialist` hebben **minstens vier bureaus een eigen landingspagina** (Redwerk, Suffescom, ThirdRock, AleaIT) — er wordt betaald om te ranken, dus er wordt gekocht.

| Ad group | Keywords | Max CPC | Daily |
|---|---|---:|---:|
| `AG-SEC-Cleanup` | `"vibe coding cleanup specialist"`, `"vibe code cleanup"`, `"vibe code audit"`, `"vibe coding rescue"`, `"clean up ai generated code"`, `"refactor ai generated code"`, `"fix ai generated code"`, `"ai code cleanup service"`, `"rescue failed mvp"`, `"mvp rescue service"` | €12.00 | €4.50 |
| `AG-SEC-Audit` | `"ai app security audit"`, `"ai generated code security audit"`, `"ai code security review"`, `"web app security audit"`, `"production readiness audit"`, `"code audit service"`, `"technical due diligence code audit"` | €12.00 | €4.00 |
| `AG-SEC-Tool` | `"lovable security"`, `"is lovable secure"`, `"lovable security vulnerabilities"`, `"lovable security audit"`, `"supabase rls"`, `"supabase security"`, `"supabase rls audit"`, `"supabase security checklist"`, `"exposed api key frontend"`, `"ai app data leak"`, `"lovable security scanner"`, `"vibeappscanner"` | €10.00 | €0.00* |
| `AG-SEC-Compliance` | `"gdpr ai app"`, `"gdpr compliance web application"`, `"owasp llm top 10"` | €8.00 | €1.50 |

\* **EN —** `AG-SEC-Tool` shares the campaign budget; activate after week 5. · **NL —** `AG-SEC-Tool` deelt het campagnebudget; activeer na week 5.

#### RSA — `AG-SEC-Cleanup` / `AG-SEC-Audit`

| # | 🇬🇧 English Headline | Ch | 🇳🇱 Nederlandse Kop | Ch | Pin |
|---|---|---:|---|---:|---|
| H1 | `Is Your AI-Built App Secure?` | 28 | `Is Je AI-App Wel Veilig?` | 24 | **P1** |
| H2 | `Fixed-Price Security Audit` | 26 | `Security Audit, Vaste Prijs` | 27 | **P2** |
| H3 | `45% of AI Code Has Flaws` | 24 | `45% AI-Code Heeft Lekken` | 24 | |
| H4 | `RLS, Keys, Auth, Rate Limits` | 28 | `RLS, Keys, Auth, Rate Limits` | 28 | |
| H5 | `Report in Days, Not Weeks` | 25 | `Rapport In Dagen, Niet Weken` | 28 | |
| H6 | `11+ Years in Cybersecurity` | 26 | `11+ Jaar Cybersecurity` | 22 | |
| H7 | `Built for Lovable & Supabase` | 28 | `Voor Lovable & Supabase` | 23 | |
| H8 | `Ready for Investor Due Dil.` | 27 | `Klaar Voor Due Diligence` | 24 | |
| H9 | `Get Your Free Scan Quote` | 24 | `Vraag Gratis Scan Aan` | 21 | **P3** |

| # | 🇬🇧 English Description | Ch | 🇳🇱 Nederlandse Beschrijving | Ch |
|---|---|---:|---|---:|
| D1 | `Exposed keys, open RLS, no rate limits. We find what AI code leaves behind.` | 75 | `Open keys, geen RLS, geen rate limits. Wij vinden wat AI-code achterlaat.` | 73 |
| D2 | `Fixed-price audit of your AI-built app. Clear report, prioritised fixes, days not weeks.` | 88 | `Vaste prijs voor een audit van je AI-app. Helder rapport, prioriteiten, in dagen.` | 81 |
| D3 | `11+ years in security engineering, trusted by Vodafone, TNO and CFLW. Free quote.` | 81 | `11+ jaar security-engineering, vertrouwd door Vodafone, TNO en CFLW. Gratis offerte.` | 84 |

> ⚠️ **EN —** The "45%" figure appears on the LaunchStudio website. **Verify its source before running it in an ad** — Google Ads has policies on unsubstantiated claims, and the landing page should be able to cite it. · **NL —** Het cijfer "45%" staat op de website van LaunchStudio. **Verifieer de bron vóór gebruik in een advertentie** — Google Ads heeft beleid over niet-onderbouwde claims, en de landingspagina moet de bron kunnen noemen.

---

### 5.4. C4 · `LS-Search-Brand` — €50/month

| Keyword | Match | Max CPC |
|---|---|---:|
| `[launchstudio]`, `[launch studio]` | Exact | €2.00 |
| `"launchstudio eu"`, `"launchstudio review"`, `"launchstudio vs"` | Phrase | €2.50 |
| `"launch studio manifera"` | Phrase | €2.00 |

**EN —** Bid strategy: Target Impression Share 95%, Absolute Top. Cheap, protects the brand from competitors bidding on it, and captures traffic from the 800+ existing blog articles.
**NL —** Biedstrategie: doelvertoningsaandeel 95%, absolute bovenkant. Goedkoop, beschermt het merk tegen concurrenten en vangt verkeer op van de 800+ bestaande blogartikelen.

---

### 5.5. C5 · `LS-Search-EN-FixTest` — €100/month (OPTIONAL)

**EN —** A controlled test of the hypothesis that people stuck on an error will also buy a service. Only activate after C2/C3 have run stably for four weeks.
**NL —** Een gecontroleerde test van de hypothese dat mensen die vastlopen op een fout ook een dienst kopen. Alleen activeren nadat C2/C3 vier weken stabiel draaien.

| Keyword (Exact only) | Max CPC |
|---|---:|
| `[lovable stripe integration]` · `[lovable stripe not working]` | €8.00 |
| `[migrate off lovable]` | €9.00 |
| `[lovable export code]` · `[self host lovable app]` | €7.00 |

**Kill rule / Stopregel:** **EN —** after 4 weeks, if CPL > €400 or zero conversions with >€150 spent → switch off permanently and move all Fix-intent keywords to the SEO plan. · **NL —** na 4 weken, bij CPL > €400 of nul conversies met >€150 besteed → definitief uitzetten en alle Fix-zoekwoorden naar het SEO-plan verplaatsen.

---

### 5.6. C6 · `LS-Search-EN-Migration` — €180/month (€6/day)

#### 5.6.1. Why this cluster, now / Waarom dit cluster, nu

**EN —** Lovable changed its default stack from **React + Vite → TanStack Start**: default for new projects from **13 May 2026**, for new Enterprise projects from **22 June 2026**. Lovable **does not auto-migrate existing projects**.

Three consequences create search demand:
1. Every project created before May 2026 still runs the old stack — and owners often **do not know**
2. The old stack has no server-side rendering → direct impact on search ranking, a pain many founders feel without knowing the cause
3. Migration is engineering work, not prompting — precisely LaunchStudio's "last-mile" definition

**Commercial proof:** `nextlovable.com` sells a **$199** audit (`/lovable-tanstack-ssr`) and a **$299** audit (`/migrate-lovable-tanstack`), plus a `/migration-guide` page. Three landing pages for one problem means it earns.

⏳ **Time-sensitivity:** this window closes when Lovable auto-migrates or old projects die off. Estimated **6–12 months**.

**NL —** Lovable veranderde de standaardstack van **React + Vite → TanStack Start**: standaard voor nieuwe projecten vanaf **13 mei 2026**, voor nieuwe Enterprise-projecten vanaf **22 juni 2026**. Lovable **migreert bestaande projecten niet automatisch**.

Drie gevolgen creëren zoekvraag:
1. Elk project van vóór mei 2026 draait nog op de oude stack — en eigenaren **weten dat vaak niet**
2. De oude stack heeft geen server-side rendering → directe impact op vindbaarheid, een pijn die veel oprichters voelen zonder de oorzaak te kennen
3. Migratie is engineeringwerk, geen prompten — precies de "last-mile"-definitie van LaunchStudio

**Commercieel bewijs:** `nextlovable.com` verkoopt een audit van **$199** (`/lovable-tanstack-ssr`) en van **$299** (`/migrate-lovable-tanstack`), plus een `/migration-guide`-pagina. Drie landingspagina's voor één probleem betekent dat het geld oplevert.

⏳ **Tijdgevoeligheid:** dit venster sluit wanneer Lovable automatisch migreert of oude projecten verdwijnen. Geschat **6–12 maanden**.

#### 5.6.2. Ad groups & keywords

| Ad group | Keywords | Max CPC | Daily | Landing page |
|---|---|---:|---:|---|
| `AG-MIG-TanStack` | `"lovable tanstack migration"`, `"migrate lovable to tanstack"`, `"lovable tanstack migration service"`, `"lovable ssr upgrade"`, `"upgrade lovable project tanstack"`, `[lovable tanstack start]` | €10.00 | €3.00 | `/en/lovable-tanstack-migration` |
| `AG-MIG-Service` | `"lovable migration service"`, `"lovable audit service"`, `"nextlovable"`, `"nextlovable alternative"` | €10.00 | €1.50 | `/en/from-prototype-to-production` |
| `AG-MIG-Platform` | `"lovable cloud vs supabase"`, `"lovable payments vs stripe"`, `"lovable cloud pricing"`, `"lovable payments fees"`, `"paddle vs stripe for saas"`, `"do i need lovable cloud"` | €8.00 | €1.50 | `/en/from-prototype-to-production` |

#### 5.6.3. ⚠️ Bidding on competitor brand names / Bieden op merknamen van concurrenten

**EN —** `nextlovable` and `vibeappscanner` are competitor **brand names**. Bidding on them is legal in the EU but carries three constraints:
1. **Do not use the competitor name in ad copy.** Google permits bidding but prohibits trademarks in ad text once the owner complains. Keep headlines neutral: `"Lovable Migration Done Right"`, not `"Better Than NextLovable"`.
2. **Quality Score will be low** → higher CPC. Acceptable for a small ad group.
3. **Expect retaliation** — they may bid on `launchstudio`. C4 Brand (§5.4) exists precisely for this.

If you prefer to avoid the risk, drop these two keywords; the remaining 19 are sufficient.

**NL —** `nextlovable` en `vibeappscanner` zijn **merknamen** van concurrenten. Erop bieden mag in de EU, maar kent drie beperkingen:
1. **Gebruik de merknaam niet in de advertentietekst.** Google staat bieden toe maar verbiedt handelsmerken in de tekst zodra de eigenaar klaagt. Houd koppen neutraal.
2. **De kwaliteitsscore wordt laag** → hogere CPC. Aanvaardbaar voor een kleine advertentiegroep.
3. **Verwacht vergelding** — zij kunnen op `launchstudio` bieden. C4 Merk (§5.4) bestaat hier juist voor.

Wil je het risico vermijden, laat deze twee zoekwoorden weg; de overige 19 volstaan.

#### 5.6.4. RSA — `AG-MIG-TanStack`

| # | 🇬🇧 English Headline | Ch | 🇳🇱 Nederlandse Kop | Ch | Pin |
|---|---|---:|---|---:|---|
| H1 | `Lovable App Still on Vite?` | 26 | `Lovable App Nog Op Vite?` | 24 | **P1** |
| H2 | `We Handle the TanStack Move` | 27 | `Wij Regelen De TanStack-Stap` | 28 | **P2** |
| H3 | `No SSR = No Google Ranking` | 26 | `Geen SSR = Geen Ranking` | 23 | |
| H4 | `Fixed Price, No Surprises` | 25 | `Vaste Prijs, Geen Verrassing` | 28 | |
| H5 | `Your Frontend Stays Intact` | 26 | `Je Frontend Blijft Intact` | 25 | |
| H6 | `Done in Days, Not Sprints` | 25 | `Klaar In Dagen, Niet Sprints` | 28 | |
| H7 | `11+ Years Engineering Exp.` | 26 | `11+ Jaar Engineering Ervaring` | 29 | |
| H8 | `You Keep 100% of the Code` | 25 | `100% Eigendom Van Je Code` | 25 | |
| H9 | `Free Migration Assessment` | 25 | `Gratis Migratie-Analyse` | 23 | **P3** |

| # | 🇬🇧 English Description | Ch | 🇳🇱 Nederlandse Beschrijving | Ch |
|---|---|---:|---|---:|
| D1 | `Lovable switched to TanStack Start in May 2026. Older projects were not migrated.` | 81 | `Lovable stapte in mei 2026 over op TanStack Start. Oude projecten niet meegenomen.` | 82 |
| D2 | `No SSR means search engines see an empty page. We migrate and keep your UI intact.` | 82 | `Geen SSR? Dan ziet Google een lege pagina. Wij migreren, je UI blijft intact.` | 77 |
| D3 | `Fixed price, code stays yours, built by Manifera engineers. Get a free assessment.` | 82 | `Vaste prijs, code blijft van jou, gebouwd door Manifera. Vraag een gratis analyse aan.` | 86 |

> ⚠️ **EN —** `D1` states a fact about a third-party product. **Verify the 13 May 2026 date from Lovable's own documentation before running it.** False claims about another company's product are a policy and legal risk. · **NL —** `D1` bevat een feitelijke bewering over het product van een derde. **Verifieer de datum 13 mei 2026 in de documentatie van Lovable vóór livegang.** Onjuiste beweringen over andermans product vormen een beleids- en juridisch risico.

#### 5.6.5. New landing page / Nieuwe landingspagina

| URL | Required? | Content |
|---|---|---|
| `/en/lovable-tanstack-migration` | **Recommended, not blocking** | **EN —** Old vs new stack · how to check which stack your project runs · SEO consequences of missing SSR · fixed price · quote CTA. **NL —** Oude vs nieuwe stack · hoe je controleert op welke stack je project draait · SEO-gevolgen van ontbrekende SSR · vaste prijs · offerte-CTA. |

**EN —** You may launch `AG-MIG-TanStack` pointing temporarily at `/en/from-prototype-to-production` for 2–4 weeks to measure real volume. If the cluster performs, build the dedicated page — message match drives both Quality Score and conversion rate.
**NL —** Je mag `AG-MIG-TanStack` tijdelijk laten verwijzen naar `/en/from-prototype-to-production` gedurende 2–4 weken om echt volume te meten. Presteert het cluster, bouw dan de eigen pagina — boodschapafstemming bepaalt zowel kwaliteitsscore als conversie.

#### 5.6.6. The other 57 new keywords — SEO backlog, not ads / De overige 57 — SEO-backlog, geen advertenties

**EN —** Of 78 new keywords found by changelog mining, **57 carry How-to / Research / Fix intent** → unsuitable for paid search per §2.3, but **well suited to SEO** because competition is near zero (many features shipped July–September 2026).

**NL —** Van de 78 nieuwe zoekwoorden uit het changelog-onderzoek hebben er **57 een How-to-, Research- of Fix-intentie** → ongeschikt voor betaald zoeken volgens §2.3, maar **zeer geschikt voor SEO** omdat de concurrentie vrijwel nul is (veel functies zijn van juli–september 2026).

| Group / Groep | # | Note / Opmerking |
|---|---:|---|
| New connectors (WhatsApp, Power BI, Cloudflare, Mapbox, PostHog, Xero…) | 14 | One overview article, split later if signal appears |
| Lovable Cloud (scaling, storage, pressure) | 5 | New infrastructure surface |
| MCP & Agents | 6 | Nobody has written about this yet |
| Enterprise & security (SSO, SCIM, 2FA, Trust Center) | 7 | Links to cluster ③ |
| Community FAQ (favicon, mobile layout, drafts…) | 6 | Easy to write, steady volume |
| Paddle/Payments How-to & Fix | 7 | |
| TanStack Research-intent | 6 | |
| Other tools (Base44, Windsurf, Firebase Studio…) | 6 | |

---

<a id="6"></a>
## 6. Negative Keywords / Uitsluitingszoekwoorden

### 6.1. Shared list #1 — `lovable` disambiguation (highest priority)

**EN —** Apply to **all** campaigns. This blocks the account's single largest waste risk: `lovable` is both a common adjective and a global lingerie brand.
**NL —** Toepassen op **alle** campagnes. Dit blokkeert het grootste verspillingsrisico: `lovable` is zowel een gangbaar bijvoeglijk naamwoord als een wereldwijd lingeriemerk.

```
-bra          -bras         -lingerie     -underwear    -intimates
-panties      -meaning      -definition   -synonym      -synonyms
-antonym      -quotes       -quote        -song         -songs
-lyrics       -lyric        -movie        -film         -book
-novel        -doll         -plush        -toy          -baby
-babies       -pet          -pets         -dog          -cat
-name         -names        -spelling     -loveable
```

### 6.2. Shared list #2 — non-buyers / niet-kopers

```
-free         -gratis       -tutorial     -tutorials    -course
-courses      -learn        -learning     -training     -certification
-jobs         -job          -vacature     -salary       -career
-internship   -stage        -download     -crack        -cracked
-torrent      -reddit       -youtube      -github       -template
-templates    -coupon       -promo        -discount     -open source
-day
```

> **EN —** `-day` is inherited from `paid_ads_plan.md` §3.1 to block the `day ai` = 201,000/month trap. · **NL —** `-day` is overgenomen uit `paid_ads_plan.md` §3.1 om de `day ai`-val van 201.000 per maand te blokkeren.

### 6.3. 🔴 Shared list #3 — Manufacturing / Fabrication

#### Why this list matters more than it looks / Waarom deze lijst belangrijker is dan hij lijkt

**EN —** This is not a precautionary list. LaunchStudio's core positioning **collides directly** with standard manufacturing terminology:

| Term in your keywords | Meaning in software | Meaning in manufacturing |
|---|---|---|
| **prototype** | an AI-built app draft | a physical sample: 3D print, CNC, mockup |
| **production** / **productie** | the live environment | a mass-production line |
| **prototype to production** | taking an app live | **NPI/DFM — moving a physical product into series production** |
| **build** / **bouwen** | writing code | fabricating, constructing |
| **custom / op maat** | bespoke software | made-to-order machining |

`prototype naar productie` and `prototype to production` — the two central keywords of C1 and C2 — are **standard hardware-industry phrases**. People searching them may want a CNC shop, a 3D printing service or a contract manufacturer, not someone to fix a Lovable app.

With an account that can only buy 15–72 clicks per month (§2.2), **a few stray clicks at €10–14 already represent 2–5% of the monthly budget.** This is the highest-impact list in §6.

**NL —** Dit is geen voorzorgslijst. De kernpositionering van LaunchStudio **botst rechtstreeks** met standaardterminologie uit de maakindustrie:

| Term in je zoekwoorden | Betekenis in software | Betekenis in de maakindustrie |
|---|---|---|
| **prototype** | een met AI gebouwd concept | een fysiek monster: 3D-print, CNC, mockup |
| **production** / **productie** | de live-omgeving | een serieproductielijn |
| **prototype to production** | een app live zetten | **NPI/DFM — een fysiek product in serie brengen** |
| **build** / **bouwen** | code schrijven | fabriceren, construeren |
| **custom / op maat** | maatwerksoftware | maakwerk op order |

`prototype naar productie` en `prototype to production` — de twee centrale zoekwoorden van C1 en C2 — zijn **standaarduitdrukkingen in de hardware-industrie**. Wie ze zoekt kan op zoek zijn naar een CNC-bedrijf, een 3D-printservice of een contractfabrikant, niet naar iemand die een Lovable-app repareert.

Bij een account dat maar 15–72 klikken per maand kan kopen (§2.2) vertegenwoordigen **enkele verkeerde klikken van €10–14 al 2–5% van het maandbudget.** Dit is de lijst met de grootste impact in §6.

#### 6.3.1. Materials / Materialen
```
-aluminium    -aluminum     -staal        -steel        -metaal
-metal        -rvs          -inox         -stainless    -koper
-copper       -messing      -brass        -titanium     -gietijzer
-kunststof    -plastic      -acryl        -acrylic      -plexiglas
-hout         -wood         -mdf          -composiet    -composite
-carbon       -glasvezel    -rubber       -schuim       -foam
```

#### 6.3.2. Machining & fabrication / Verspaning & fabricage
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

#### 6.3.3. 3D printing / additive
```
-3d           -3d print     -3d-print     -3dprint      -3d printing
-3d printer   -printen      -filament     -resin        -pla
-abs          -petg         -sls          -sla          -fdm
-dlp          -additive     -sintering    -stereolithografie
-slicer       -cura         -nozzle       -printbed
```

> ⚠️ **EN —** Consider `-3d` carefully as broad match: it blocks `3d` standing alone. If LaunchStudio has clients building apps with 3D models (configurator, viewer), drop `-3d` and keep only the two-word phrases. · **NL —** Overweeg `-3d` zorgvuldig als breed zoeken: het blokkeert `3d` als losstaand woord. Heeft LaunchStudio klanten met 3D-modellen in hun app, laat `-3d` dan weg en houd alleen de tweewoordcombinaties.

#### 6.3.4. Physical prototyping — the most important block / Fysiek prototypen — het belangrijkste blok
```
-rapid prototyping        -prototyping service      -prototype fabrication
-prototype machining      -prototype parts          -hardware prototype
-physical prototype       -functional prototype     -prototype mold
-pcb                      -printed circuit          -breadboard
-enclosure                -housing                  -mockup model
-scale model              -maquette                 -proefmodel
-nulserie                 -pilot run                -tooling prototype
```

#### 6.3.5. Manufacturing businesses / Productiebedrijven
```
-manufacturer   -manufacturers  -manufacturing  -fabrikant      -fabrikanten
-maakindustrie  -maakbedrijf    -productiebedrijf -machinebouw  -machinefabriek
-toeleverancier -toelevering    -contract manufacturing         -oem
-odm            -assembly line  -productielijn  -seriematig     -serieproductie
-massaproductie -mass production -batch production -moq
-minimum order  -werkplaats     -smederij       -gieterij       -constructiebedrijf
```

#### 6.3.6. Buying/renting machines / Machines kopen of huren
```
-machine kopen      -machines te koop   -machine te koop
-machinepark        -occasion           -tweedehands
-gebruikte machine  -machine huren      -verhuur
-onderhoud          -reparatie          -onderdelen
-gereedschap        -tooling kopen      -3d printer kopen
-laser kopen        -cnc kopen
```

#### 6.3.7. CAD/CAM software (different category / andere categorie)
```
-cad          -cam          -cadcam       -solidworks   -autocad
-fusion       -fusion 360   -freecad      -inventor     -catia
-creo         -mastercam    -nx           -sketchup     -rhino
-gcode        -g-code       -post processor             -dxf
-dwg          -step file    -iges         -stl
```

#### 6.3.8. Industry ERP vendors / ERP-leveranciers in de branche
```
-mkg          -komdex       -snabbt       -halloy       -klaes
-reynapro     -logikal      -orgadata     -vtbo         -kozijncalculator
-paperless parts            -digifabster  -cloudnc      -proshop
-global shop
```

#### 6.3.9. Construction & facades / Bouw & gevelbouw
```
-aannemer     -bouwbedrijf  -verbouwing   -renovatie    -bestek
-constructie  -staalconstructie           -kozijn       -kozijnen
-gevel        -gevelbouw    -facade       -dakkapel     -serre
-beglazing    -ramen        -deuren       -schuifpui
```

#### 6.3.10. Technical notes for entry into Google Ads / Technische aandachtspunten bij invoer

1. **EN —** Negative keywords do **not** match close variants. Unlike normal keywords they do not catch plurals, misspellings or accents automatically. Enter `-machine` **and** `-machines`, `-matrijs` **and** `-matrijzen` separately. · **NL —** Uitsluitingszoekwoorden matchen **geen** nauwe varianten. Voer `-machine` **en** `-machines` apart in.
2. **EN —** Single words → negative broad; multi-word phrases → negative phrase. · **NL —** Losse woorden → breed uitsluiten; woordcombinaties → woordgroep uitsluiten.
3. **EN —** Negative broad requires **all** words to appear. `-machine kopen` as broad only blocks queries containing both words; use phrase to be certain. · **NL —** Breed uitsluiten vereist dat **alle** woorden voorkomen; gebruik woordgroep voor zekerheid.
4. **EN —** Apply at **account level** (Shared Library → Negative keyword lists), not per campaign — the `prototype`/`production` risk applies everywhere. · **NL —** Toepassen op **accountniveau** (Gedeelde bibliotheek), niet per campagne.
5. **EN —** Check before applying: make sure no negative blocks a good query. `-coating` could block `coating software`. · **NL —** Controleer vooraf dat geen uitsluiting een goede zoekopdracht blokkeert.

### 6.4. Campaign-specific negatives / Campagnespecifieke uitsluitingen

| Campaign | Add / Toevoegen |
|---|---|
| C1 (NL) | `-engels`, `-english`, `-vacature`, `-cursus`, `-opleiding` |
| C2 (Hire) | `-fiverr`, `-upwork`, `-freelancer.com`, `-hourly rate`, `-cheap`, `-goedkoop`, `-india`, `-pakistan` |
| C3 (Security) | `-antivirus`, `-vpn`, `-firewall`, `-malware`, `-soc 2`, `-iso 27001` *(drop last two if offered)* |
| C5 (Fix) | `-how to`, `-guide`, `-step by step`, `-documentation`, `-docs`, `-forum` |
| C6 (Migration) | `-tutorial`, `-docs`, `-free guide`, `-youtube` |

### 6.5. Ongoing negative process / Doorlopend uitsluitingsproces

**EN —** Weeks 1–4: check the Search Terms Report **every 2 days**. After that, weekly. With an account this small, one stray €14 query is 2% of the monthly budget — nothing may be left to drift.

**NL —** Week 1–4: controleer het zoektermenrapport **elke 2 dagen**. Daarna wekelijks. Bij een account van deze omvang is één verkeerde zoekopdracht van €14 al 2% van het maandbudget — niets mag wegglijden.

---

<a id="7"></a>
## 7. Conversion Tracking / Conversiemeting

### 7.1. Three conversion actions / Drie conversieacties

| Name | Type | Value | Count | Primary? |
|---|---|---:|---|---|
| `contact_form_submit` | Lead | €150 | One | ✅ |
| `call_booked` | Lead | €250 | One | ✅ |
| `calculator_complete` | Micro | €25 | One | ❌ Secondary |

> **EN — On the assigned values:** these are *estimated lead values*, not revenue. Method: average deal €2,500 × assumed close rate. At 10% that is €250; €150 is deliberately conservative for the first quarter. Revisit after three months with real data.
>
> **NL — Over de toegekende waarden:** dit zijn *geschatte leadwaarden*, geen omzet. Methode: gemiddelde order €2.500 × aangenomen closingratio. Bij 10% is dat €250; €150 is bewust voorzichtig voor het eerste kwartaal. Herzie na drie maanden met echte data.

### 7.2. Setup / Inrichting

1. **GA4** → create the three events → mark as Key Events
2. Import into Google Ads (Tools → Conversions → Import → GA4)
3. **EN —** Enable Enhanced Conversions — at this volume every conversion counts; none may be lost to cookie blocking. · **NL —** Schakel Enhanced Conversions in — bij dit volume telt elke conversie.
4. **EN —** **Consent Mode v2 is mandatory in the EU.** Without it, conversion data in the Dutch market will be materially incomplete. · **NL —** **Consent Mode v2 is verplicht in de EU.** Zonder dit is de conversiedata in de Nederlandse markt wezenlijk onvolledig.
5. **EN —** Offline conversion import from month 2: when a lead becomes a real customer, upload back with GCLID + actual revenue. This is the only way to know which campaign brings **customers**, not just leads. · **NL —** Offline conversie-import vanaf maand 2: upload met GCLID + werkelijke omzet zodra een lead klant wordt.

### 7.3. Measure quality, not only quantity / Meet kwaliteit, niet alleen aantal

**EN —** At 3–8 leads per month, a single junk lead distorts everything. Add one required form field — *"Do you already have a prototype?"* (Yes / Design only / Idea only). Only "Yes" counts as qualified.

**NL —** Bij 3–8 leads per maand vertekent één rommellead alles. Voeg één verplicht formulierveld toe — *"Heb je al een prototype?"* (Ja / Alleen ontwerp / Alleen een idee). Alleen "Ja" telt als gekwalificeerd.

---

<a id="8"></a>
## 8. Ad Extensions / Advertentie-extensies

### 8.1. Sitelinks (4, required / verplicht)

| # | 🇬🇧 English | 🇳🇱 Nederlands | URL |
|---|---|---|---|
| 1 | `Packages & Pricing` | `Pakketten & Prijzen` | `/en/#packages` |
| 2 | `Free Price Calculator` | `Gratis Prijscalculator` | `/en/#calculator` |
| 3 | `Security Audit` | `Beveiligingsaudit` | `/en/ai-code-security-audit` |
| 4 | `How It Works` | `Zo Werkt Het` | `/en/#process` |

### 8.2. Callouts

- 🇬🇧 `Fixed Price From €800` · `Live in 1-3 Weeks` · `You Own 100% Code` · `No Rebuild Needed` · `11+ Years Experience`
- 🇳🇱 `Vaste Prijs Vanaf €800` · `Live in 1-3 Weken` · `100% Code Eigendom` · `Geen Herbouw` · `11+ Jaar Ervaring`

### 8.3. Structured snippets

- **Services / Diensten:** Security · Payments · Authentication · Database · Hosting · Deployment
- **Types:** Website · Webshop · SaaS · Mobile App · Dashboard · Internal Tool

### 8.4. Price extension

| 🇬🇧 Package | 🇳🇱 Pakket | Price | Description / Omschrijving |
|---|---|---|---|
| Launch Ready | Klaar voor lancering | from €800 | Security, auth, database, live on your own domain |
| Launch & Grow | Lancering & Groei | from €2,500 | + Stripe payments, managed hosting, monitoring |
| Managed Hosting | Managed Hosting | €49/mo | SSL, backups, uptime monitoring, security updates |

### 8.5. Also enable / Ook inschakelen

- **EN —** **Call extension** if a Dutch phone number exists. For B2B services, calls convert better than forms. · **NL —** **Bel-extensie** als er een Nederlands nummer is. Bij B2B-diensten converteren telefoongesprekken beter dan formulieren.
- **EN —** **Location extension** — Herengracht 420, Amsterdam. Materially increases trust in the Dutch market. · **NL —** **Locatie-extensie** — Herengracht 420, Amsterdam. Verhoogt het vertrouwen in de Nederlandse markt aanzienlijk.
- **EN —** **Lead form extension** — test separately; lead quality is usually lower than a landing page. · **NL —** **Leadformulier-extensie** — apart testen; de leadkwaliteit ligt meestal lager.

---

<a id="9"></a>
## 9. Budget & 90-Day Roadmap / Budget & 90-dagen Routekaart

### 9.1. Three budget scenarios / Drie budgetscenario's

| | **Tier A — Cautious** | **Tier B — Recommended** | **Tier C — Volume ceiling** |
|---|---:|---:|---:|
| C1 NL Service | €120 | €200 | €300 |
| C2 EN Hire | €150 | €250 | €350 |
| C3 EN Security | €180 | €300 | €450 |
| C4 Brand | €50 | €50 | €50 |
| C5 Fix Test | — | €100 | €150 |
| C6 Migration | €120 | €180 | €250 |
| **Total / Totaal** | **€620** | **€1,080** | **€1,550** |
| Est. clicks / Geschatte klikken | 10–30 | 18–55 | 30–85 |
| Est. leads @5–8% | 1–2 | 2–5 | 3–7 |
| Est. customers @30% | 0–1 | 1–2 | 1–3 |

**EN —** Start at Tier A for four weeks; move to Tier B from week 5 if CPL < €300. Above €1,550/month is waste — widen the keyword surface or change channel instead.
**NL —** Begin vier weken met Tier A; ga vanaf week 5 naar Tier B als de CPL < €300 is. Boven €1.550 per maand is verspilling — verbreed het zoekwoordoppervlak of kies een ander kanaal.

### 9.2. Roadmap / Routekaart

| Week | Task / Taak |
|---|---|
| **0** | Complete the six prerequisites in §3. Run Keyword Planner for real volume and **update §2.2 and §9.1 with actual figures**. |
| **1** | Build C1 + C4 at Tier A. Two campaigns only. Manual CPC. |
| **2** | Check Search Terms every 2 days; add negatives. Build C2 but do not enable. |
| **3** | Enable C2. Dutch copy reviewed by a native speaker. |
| **4** | **Review 1.** If C1 has ≥1 lead, keep. If zero leads with >€120 spent, fix the landing page before adding budget. |
| **5** | Enable C3 (if the security page is live). Raise Tier A → B for any campaign with CPL < €300. |
| **6–7** | Optimise bids per keyword. Split out any keyword with ≥3 conversions into its own ad group. |
| **8** | **Review 2.** Calculate real CAC per §2.3. If CAC > €1,250, stop and fix the funnel — do not raise budget. |
| **9** | Enable C5 if C2/C3 are stable. **Enable C6** — start with `AG-MIG-TanStack` only, pointing temporarily at `/en/from-prototype-to-production`. |
| **10–11** | Begin offline conversion import. Add new keywords from the Search Terms Report. If `AG-MIG-TanStack` produces ≥1 lead, build `/en/lovable-tanstack-migration` and enable the other two C6 ad groups. |
| **12** | **Quarterly review.** Decide: widen geography, add keyword clusters, or move budget to another channel. Re-run changelog mining ([`keyword_idea_playbook.md`](keyword_idea_playbook.md) Part C). |

### 9.3. Bid strategy by phase / Biedstrategie per fase

| Phase / Fase | Strategy | Reason / Reden |
|---|---|---|
| Weeks 1–6 | **Manual CPC** or Maximize Clicks + CPC cap | Volume too low for Smart Bidding |
| Weeks 7–12 | Keep Manual CPC | Still under 30 conversions |
| After 30+ conversions | Maximize Conversions | Typically month 4–6, not month 2 |
| After 50+ conversions | Target CPA @ €300 | |

> ⚠️ **EN —** `google_ads_keywords_launchstudio.md` proposes switching to Maximize Conversions early. At this account's real volume that is **premature** — Google will spend budget on learning. · **NL —** `google_ads_keywords_launchstudio.md` stelt voor vroeg over te schakelen op Maximaliseer conversies. Bij het werkelijke volume van dit account is dat **te vroeg**.

---

<a id="10"></a>
## 10. KPIs, Glossary & Thresholds / KPI's, Begrippenlijst & Drempels

### 10.1. KPI table / KPI-tabel

| Metric / Maatstaf | Week 4 | Week 8 | Week 12 | Kill threshold / Stopdrempel |
|---|---|---|---|---|
| **CPC** (Cost Per Click) average | ≤ €12 | ≤ €10 | ≤ €10 | > €16 for 2 weeks |
| **CTR** (Click-Through Rate) | ≥ 4% | ≥ 6% | ≥ 7% | < 2% in any ad group |
| **LP conversion** (Landing Page conversion rate) | ≥ 3% | **≥ 5%** | ≥ 6% | < 2% after one fix attempt |
| **CPL** (Cost Per Lead), qualified | ≤ €400 | ≤ €300 | ≤ €250 | > €500 |
| **CAC** (Customer Acquisition Cost) | — | ≤ €900 | **≤ €625** | > €1,250 (break-even) |
| **IS** (Impression Share) | ≥ 40% | ≥ 60% | ≥ 65% | — |
| **IS lost (budget)** (Search Lost Impression Share — budget) | — | < 20% | < 15% | > 40% = raise budget |
| **IS lost (rank)** (Search Lost Impression Share — rank) | — | < 30% | < 25% | > 50% = raise bid or fix **QS** (Quality Score) |

### 10.2. Metric glossary / Begrippenlijst maatstaven

> **EN —** The "Where" column gives the exact column name in the Google Ads interface. · **NL —** De kolom "Waar" geeft de exacte kolomnaam in de Google Ads-interface.

| Metric | Full name / Volledige naam | Formula / Formule | Where / Waar | What it tells you / Wat het zegt |
|---|---|---|---|---|
| **CPC** | Cost Per Click · Kosten per klik | Total cost ÷ clicks | `Avg. CPC` | **EN —** Price per click. Low CPC from the wrong query is worse than high CPC from the right one. · **NL —** Prijs per klik. Lage CPC op een verkeerde zoekopdracht is slechter dan hoge CPC op de juiste. |
| **CTR** | Click-Through Rate · Doorklikratio | (Clicks ÷ impressions) × 100 | `CTR` | **EN —** Match between ad and query. Low CTR is a copy problem, not a bid problem. · **NL —** Aansluiting tussen advertentie en zoekopdracht. Lage CTR is een tekstprobleem, geen biedprobleem. |
| **LP conversion** | Landing Page conversion rate · Conversieratio landingspagina | (Leads ÷ clicks) × 100 | `Conv. rate` *(same number, different name)* | **EN —** Of 100 clicks, how many leave contact details. **This is the plan's survival threshold** (§2.3). · **NL —** Van 100 klikken, hoeveel laten contactgegevens achter. **Dit is de overlevingsdrempel** (§2.3). |
| **CPL** | Cost Per Lead · Kosten per lead | Total cost ÷ **qualified** leads | `Cost / conv.` — but that counts **all** leads; qualified CPL must be calculated manually | **EN —** True price of a usable lead. See §7.3 for how "qualified" is defined. · **NL —** Werkelijke prijs van een bruikbare lead. Zie §7.3. |
| **CAC** | Customer Acquisition Cost · Klantacquisitiekosten | CPL ÷ close rate | ❌ **Not in Google Ads** — requires sales data (§7.2 step 5) | **EN —** Ad spend to win one paying customer. At 25% close rate, CAC = 4 × CPL. · **NL —** Advertentiekosten voor één betalende klant. |
| **Close rate** | Closing ratio · Closingratio | (Customers ÷ qualified leads) × 100 | ❌ In your CRM, not Google Ads | **EN —** Quality of the sales process. 25% → 40% cuts CAC by 37% (§2.3). · **NL —** Kwaliteit van het verkoopproces. |
| **IS** | Impression Share · Vertoningsaandeel | (Impressions ÷ eligible impressions) × 100 | `Search impr. share` *(Competitive metrics, enable manually)* | **EN —** How often you appear out of the times you could. 100% usually means bids are too high. · **NL —** Hoe vaak je verschijnt van alle keren dat het kon. |
| **IS lost (budget)** | Search Lost Impression Share (budget) | — | `Search lost IS (budget)` | **EN —** Demand you could not buy because the daily budget ran out. >40% with good CPL = raise budget. · **NL —** Vraag die je niet kon kopen omdat het dagbudget op was. |
| **IS lost (rank)** | Search Lost Impression Share (rank) | — | `Search lost IS (rank)` | **EN —** You had money but ranked too low. Check QS first; if QS < 5, fix message match — do not raise the bid. · **NL —** Je had budget maar stond te laag. Controleer eerst de kwaliteitsscore. |
| **QS** | Quality Score · Kwaliteitsscore | 1–10, at keyword level | `Quality Score` *(Keywords tab; shows `—` without data)* | **EN —** Three parts: Expected CTR, Ad relevance, Landing page experience. High QS = lower CPC. · **NL —** Drie onderdelen: verwachte CTR, advertentierelevantie, landingspagina-ervaring. |

### 10.3. Other abbreviations / Overige afkortingen

| Abbr. | Full name | Nederlands |
|---|---|---|
| **CPA** | Cost Per Acquisition | Kosten per acquisitie — Google's name for `Target CPA` bidding |
| **LTV** | Lifetime Value | Klantlevenswaarde |
| **KPI** | Key Performance Indicator | Kernprestatie-indicator |
| **RSA** | Responsive Search Ad | Responsieve zoekadvertentie |
| **SERP** | Search Engine Results Page | Zoekresultatenpagina |
| **SEO** | Search Engine Optimization | Zoekmachineoptimalisatie |
| **CTA** | Call To Action | Oproep tot actie |
| **USP** | Unique Selling Proposition | Uniek verkoopargument |
| **GA4** | Google Analytics 4 | — |
| **GCLID** | Google Click Identifier | Klik-identificatie voor offline conversies |
| **UTM** | Urchin Tracking Module | URL-parameters voor bronherkenning |
| **B2B** | Business-to-Business | Zakelijke markt |
| **MVP** | Minimum Viable Product | Minimaal levensvatbaar product |
| **SaaS** | Software as a Service | Software als dienst |
| **API** | Application Programming Interface | Programmeerinterface |
| **UI** | User Interface | Gebruikersinterface |
| **URL** | Uniform Resource Locator | Webadres |
| **CSV** | Comma-Separated Values | Bestandsformaat met kommascheiding |
| **FAQ** | Frequently Asked Questions | Veelgestelde vragen |
| **SSL** | Secure Sockets Layer | Beveiligd webcertificaat (https) |
| **DNS** | Domain Name System | Domeinnaamsysteem |
| **SSR** | Server-Side Rendering | Rendering aan serverzijde — bepalend voor vindbaarheid |
| **RLS** | Row Level Security | Beveiliging op rijniveau (Supabase) |
| **MCP** | Model Context Protocol | Protocol om apps aan AI-assistenten te koppelen |
| **SSO** | Single Sign-On | Eenmalige aanmelding |
| **SCIM** | System for Cross-domain Identity Management | Standaard voor gebruikerssynchronisatie |
| **2FA** | Two-Factor Authentication | Tweefactorauthenticatie |
| **ERP** | Enterprise Resource Planning | Bedrijfsbeheersysteem |
| **CAD / CAM** | Computer-Aided Design / Manufacturing | Computerondersteund ontwerpen / fabriceren |
| **CNC** | Computer Numerical Control | Computergestuurde verspaning |
| **NPI / DFM** | New Product Introduction / Design For Manufacturing | Productintroductie / ontwerpen voor maakbaarheid |
| **TNO** | Nederlandse Organisatie voor toegepast-natuurwetenschappelijk onderzoek | — |
| **CFLW** | CFLW Cyber Strategies | Cybersecuritybedrijf (voorheen CyberDevOps) |
| **GKP** | Google Keyword Planner | Zoekwoordplanner |
| **GSC** | Google Search Console | — |

### 10.4. Naming conventions / Naamgevingsconventies

| Symbol | Meaning | Example |
|---|---|---|
| **C1–C6** | Campaign 1–6 · Campagne 1–6 | `C3` = Security campaign |
| **LS-** | LaunchStudio — campaign name prefix | `LS-Search-EN-Hire` |
| **AG-** | Ad Group · Advertentiegroep | `AG-LOV-Hire` |
| **H1–H15** | Headline 1–15 (max 30 characters) | |
| **D1–D4** | Description 1–4 (max 90 characters) | |
| **P1–P3** | Pin position 1–3 · Vastzetpositie | `P1` = always shown first |
| **Ch** | Characters · Tekens | Character-count column in RSA tables |

> ⚠️ **EN —** `P1–P3` carries two meanings depending on context: **Pin position** in RSA tables (§5), and **Priority** in the keyword CSV. Inherited from [`google_ads_rsa_copy_launchstudio.md`](google_ads_rsa_copy_launchstudio.md). · **NL —** `P1–P3` heeft twee betekenissen afhankelijk van de context: **vastzetpositie** in RSA-tabellen en **prioriteit** in het zoekwoordbestand.

### 10.5. ⚠️ Statistical significance warning / Waarschuwing over statistische betrouwbaarheid

**EN —** At **15–72 clicks per month** (§2.2), nearly every metric in §10.1 is noise at week 4.

**NL —** Bij **15–72 klikken per maand** (§2.2) is vrijwel elke maatstaf in §10.1 in week 4 ruis.

| Metric | Data needed to be reliable / Benodigde data |
|---|---|
| CTR | ~500 impressions per ad group |
| LP conversion | ~100 clicks per landing page |
| CPL | ~10 leads |
| CAC | ~10 customers — **may take 6–12 months** |

➡️ **EN —** The "Week 4" column is a reference point for spotting large deviations, not a basis for optimisation decisions. Real decisions start at week 8. · **NL —** De kolom "Week 4" dient om grote afwijkingen te signaleren, niet om optimalisatiebeslissingen op te baseren. Echte beslissingen beginnen in week 8.

### 10.6. Decision rules / Beslisregels

| Situation / Situatie | Action / Actie |
|---|---|
| Ad group spent > €150, zero conversions, after 4 weeks | **Switch off.** No "one more chance" · **Uitzetten.** Geen extra kans |
| Keyword spent > €80, zero conversions | Switch off the keyword, keep the ad group |
| CPL < €200 in an ad group | Raise that ad group's budget by 50%; review next week |
| IS lost (budget) > 40% **and** CPL is good | Raise budget — you are missing available demand |
| IS lost (rank) > 50% | Check QS. If QS < 5, fix landing page message match **before** raising bids |
| CTR < 2% in an ad group | Copy does not match intent → rewrite the RSA, do not raise the bid |
| LP conversion < 2% | **Stop funding that ad group.** The problem is the page, not the ads |
| CAC > €1,250 after week 8 | **Stop everything**, revisit §2.3, fix the sales funnel |

### 10.7. Do not judge by these / Beoordeel niet op deze cijfers

**EN —** With an account of 15–72 clicks per month: ❌ impression count · ❌ click volume · ❌ week-1 CTR. ✅ **Cost per qualified lead** early on · ✅ **CAC and LTV** later.

**NL —** Bij een account van 15–72 klikken per maand: ❌ aantal vertoningen · ❌ klikvolume · ❌ CTR in week 1. ✅ **Kosten per gekwalificeerde lead** in het begin · ✅ **CAC en LTV** later.

---

<a id="11"></a>
## 11. Risks / Risico's

| # | Risk / Risico | Level | Mitigation / Beheersing |
|---|---|---|---|
| 1 | **EN —** `lovable` lingerie/dictionary trap burns budget on day 1 · **NL —** `lovable`-val verbrandt budget op dag 1 | 🔴 High | §6.1 + never broad match |
| 2 | **EN —** Real volume lower than estimated; budget cannot be spent · **NL —** Werkelijk volume lager dan geschat | 🟠 Med-high | Verify in Keyword Planner week 0. If < 200 searches/month, move budget to LinkedIn (`paid_ads_plan.md` §6) |
| 3 | **EN —** CPC above €14 due to B2B SaaS competition · **NL —** CPC boven €14 door concurrentie | 🟠 Medium | 2026 benchmark for B2B SaaS median non-brand is $8.50–14.00. If exceeded, focus on NL and long-tail |
| 4 | **EN —** Landing page converts < 3% → model loses money · **NL —** Landingspagina converteert < 3% | 🔴 High | §2.3. Measure from week 2, fix before raising budget |
| 5 | **EN —** Price competition with $25 Fiverr gigs · **NL —** Prijsconcurrentie met Fiverr | 🟠 Medium | §5.2.1 — reframe, do not compete on price |
| 6 | **EN —** Smart Bidding enabled too early · **NL —** Smart Bidding te vroeg ingeschakeld | 🟡 Med-low | §9.3 — Manual CPC until 30+ conversions |
| 7 | **EN —** The "45%" and "80%" website figures lack a cited source · **NL —** De cijfers 45% en 80% missen bronvermelding | 🟡 Med-low | Verify before use in ad copy; Google Ads has claim policies |
| 8 | **EN —** Missing Consent Mode v2 → conversion data loss in EU · **NL —** Ontbrekende Consent Mode v2 | 🟠 Medium | §7.2 step 4 |
| 9 | **EN —** C6 TanStack window closes · **NL —** Het TanStack-venster sluit | 🟠 Medium | Estimated 6–12 months. Launch in week 9, not next year |
| 10 | **EN —** Competitor-brand bidding triggers retaliation · **NL —** Bieden op merknamen lokt vergelding uit | 🟡 Med-low | C4 Brand protects. Or drop those two keywords |
| 11 | **EN —** False claim about a third-party product in ad copy · **NL —** Onjuiste bewering over andermans product | 🟠 Medium | §5.6.4 — verify the 13 May 2026 date from Lovable's documentation |

---

<a id="12"></a>
## 12. Day-1 Checklist / Checklist Dag 1

### Before opening Google Ads / Voordat je Google Ads opent

- [ ] Export the seed list: `awk -F',' 'NR>1{print $3}' keyword_seeds_google_ads_3_clusters.csv`
- [ ] Run Keyword Planner: Location = **Netherlands** (pass 1), then DE/FR/ES/IT/SE/DK/PL/PT/IE/BE (pass 2)
- [ ] Delete any keyword with volume > 20,000 — almost certainly a trap
- [ ] **Update §2.2 and §9.1 of this document with the real figures**
- [ ] `/en/ai-code-security-audit` is live
- [ ] `/en/from-prototype-to-production` is live
- [ ] `/nl/van-prototype-naar-productie` is live, reviewed by a Dutch native speaker
- [ ] GA4 + three conversion events installed and tested
- [ ] Conversions imported into Google Ads, marked Primary
- [ ] Enhanced Conversions + Consent Mode v2 enabled
- [ ] `Organization` schema added; author schema `"phu.lt"` corrected

### In Google Ads

- [ ] Create the three Shared Negative Lists (§6.1, §6.2, §6.3) **before** creating campaigns
- [ ] Create C1 (NL) + C4 (Brand) at Tier A
- [ ] Attach the negative lists to both campaigns
- [ ] Bid strategy = **Manual CPC**
- [ ] Location targeting: C1 = Netherlands + Flanders, **"Presence" not "Presence or interest"**
- [ ] Ad schedule: all week for the first 4 weeks to gather data
- [ ] Ad rotation: **"Do not optimize"** for the first 4 weeks so RSAs compare fairly
- [ ] All 4 sitelinks + callouts + structured snippets + price extension attached
- [ ] Recurring reminder: check the Search Terms Report every 2 days

### C6 Migration (week 9, not day 1)

- [ ] Verify the Lovable → TanStack Start date before using it in ad copy (§5.6.4)
- [ ] Decide whether to bid on `nextlovable` / `vibeappscanner` (§5.6.3)
- [ ] If bidding: confirm no competitor name appears in ad text
- [ ] Enable `AG-MIG-TanStack` first, pointing temporarily at `/en/from-prototype-to-production`
- [ ] Build `/en/lovable-tanstack-migration` if there is signal after 2–4 weeks
- [ ] Move the 57 SEO-only keywords into the content calendar, **not** into Ads (§5.6.6)

---

## 📌 Summary / Samenvatting

> **EN —** Run €620/month across 60 commercial-intent keywords, Netherlands first, on Manual CPC, with negative lists blocking the `lovable` and manufacturing traps. Judge by cost per qualified lead. Fix the landing page until it converts at ≥5% — below that the model does not pay, no matter how well the bids are tuned. Volume ceiling €1,550/month.
>
> **NL —** Besteed €620 per maand aan 60 zoekwoorden met commerciële intentie, Nederland eerst, op handmatige CPC, met uitsluitingslijsten die de `lovable`- en maakindustrievallen blokkeren. Beoordeel op kosten per gekwalificeerde lead. Verbeter de landingspagina tot deze op ≥5% converteert — daaronder is het model niet rendabel, hoe goed de biedingen ook zijn afgesteld. Volumeplafond €1.550 per maand.

---

*RSA character limits verified: 92 headlines and descriptions across 4 ad groups in both languages, all within Google Ads limits (headlines ≤ 30, descriptions ≤ 90). · RSA-tekenlimieten geverifieerd: 92 koppen en beschrijvingen in beide talen, alle binnen de limieten van Google Ads.*
