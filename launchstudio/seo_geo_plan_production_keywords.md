# 🧭 SEO & GEO-Entity Plan — Production-Readiness Keywords
## LaunchStudio.eu · 🇬🇧 English ⟷ 🇳🇱 Nederlands

> **EN —** An organic counterpart to [`google_ads_production_keywords_plan_nl.md`](google_ads_production_keywords_plan_nl.md), built on the same 14 keywords from [`extra-keywords.md`](extra-keywords.md). Where the Ads plan buys visibility, this plan earns it — across classic search (SEO), AI answer engines (GEO — Generative Engine Optimization), and entity recognition (who LaunchStudio *is* to Google's Knowledge Graph and to LLMs).
>
> **NL —** Een organische tegenhanger van [`google_ads_production_keywords_plan_nl.md`](google_ads_production_keywords_plan_nl.md), gebouwd op dezelfde 14 zoekwoorden uit [`extra-keywords.md`](extra-keywords.md). Waar het advertentieplan zichtbaarheid koopt, verdient dit plan haar — in klassieke zoekmachines (SEO), in AI-antwoordmachines (GEO — Generative Engine Optimization) en in entiteitsherkenning (wie LaunchStudio *is* voor de Knowledge Graph van Google en voor LLM's).

| | |
|---|---|
| **Site** | 🇳🇱 `launchstudio.eu/` · 🇬🇧 `launchstudio.eu/en/` |
| **Primary market / Primaire markt** | Netherlands · Nederland (`nl-NL` primary, `en` secondary) |
| **Source keywords / Bronzoekwoorden** | 14 unique (see §2) |
| **Baseline audit / Nulmeting** | [`seo_geo_audit_2026-07-31.md`](seo_geo_audit_2026-07-31.md) |
| **Brand master brief** | [`launchstudio_info.md`](launchstudio_info.md) |
| **CMS** | WordPress + Yoast SEO v27.6 |
| **Status** | Draft v1.0 — implementation plan, not yet executed |

---

## 📑 Table of Contents / Inhoudsopgave

1. [Why this plan is not "write more articles" / Waarom dit plan geen "meer artikelen" is](#1)
2. [Keyword → intent → page mapping / Zoekwoord → intentie → pagina](#2)
3. [Site architecture: pillar & cluster / Site-architectuur: pijler & cluster](#3)
4. [Page briefs (5 new money pages) / Paginabriefings (5 nieuwe money pages)](#4)
5. [Mapping the existing 800 articles / De bestaande 800 artikelen inzetten](#5)
6. [Entity plan & Schema.org / Entiteitsplan & Schema.org](#6)
7. [GEO-entity: geographic positioning / GEO-entiteit: geografische positionering](#7)
8. [GEO: Generative Engine Optimization](#8)
9. [Bilingual strategy & hreflang / Tweetalige strategie & hreflang](#9)
10. [Technical SEO prerequisites / Technische SEO-randvoorwaarden](#10)
11. [Internal linking rules / Regels voor interne links](#11)
12. [90-day execution calendar / 90-dagen uitvoeringskalender](#12)
13. [KPIs & measurement / KPI's & meting](#13)
14. [Risks / Risico's](#14)
15. [Decisions required / Beslissingen die genomen moeten worden](#15)

---

<a id="1"></a>
## 1. ⚠️ Why This Plan Is Not "Write More Articles"
## ⚠️ Waarom Dit Plan Geen "Meer Artikelen Schrijven" Is

> **Read this before anything else. It changes what the work actually is.**
> **Lees dit eerst. Het verandert wat het werk daadwerkelijk inhoudt.**

**EN —** Three facts from the current state make the obvious approach the wrong one:

1. **There is no content shortage — there is a publishing and entity shortage.** The content inventory holds **800+ produced articles** for LaunchStudio, while the audit of 2026-07-31 counted **71 live articles** on the site. Writing a 15th article about AI-code security does not move these keywords; publishing and structuring what already exists does.
2. **These 14 keywords have no home page to rank.** They are commercial-intent, service-shaped queries ("productionize AI app", "AI application security audit"). Blog posts rarely win those SERPs — **service pages** do. LaunchStudio currently has a single-page site with anchors (`/#packages`, `/#calculator`); there is no indexable URL that *is* the answer to "AI prototype to production".
3. **The entity foundation is missing.** The audit found **no `Organization` schema anywhere**, no `sameAs`, no `FAQPage`, and a `Person` author schema reading `"phu.lt"`. For AI answer engines this is decisive: an LLM cannot cite a company it cannot identify. Fixing this lifts *every* keyword, not just these 14.

**NL —** Drie feiten uit de huidige situatie maken de voor de hand liggende aanpak de verkeerde:

1. **Er is geen tekort aan content — er is een tekort aan publicatie en entiteit.** De contentinventaris bevat **800+ geproduceerde artikelen** voor LaunchStudio, terwijl de audit van 31-07-2026 **71 live artikelen** telde. Een vijftiende artikel over AI-codebeveiliging verplaatst deze zoekwoorden niet; publiceren en structureren van wat er al ligt wel.
2. **Deze 14 zoekwoorden hebben geen pagina om op te ranken.** Het zijn commerciële, dienstgerichte zoekopdrachten ("productionize AI app", "AI application security audit"). Blogposts winnen die zoekresultaten zelden — **dienstpagina's** wel. LaunchStudio heeft nu een one-page site met ankers (`/#packages`, `/#calculator`); er is geen indexeerbare URL die hét antwoord *is* op "AI-prototype naar productie".
3. **Het entiteitsfundament ontbreekt.** De audit vond **nergens `Organization`-schema**, geen `sameAs`, geen `FAQPage` en een `Person`-auteurschema met `"phu.lt"`. Voor AI-antwoordmachines is dat doorslaggevend: een LLM kan geen bedrijf citeren dat het niet kan identificeren. Dit repareren tilt *elk* zoekwoord op, niet alleen deze 14.

### 1.1 What this plan therefore consists of / Waar dit plan dus uit bestaat

| Priority | Work / Werk | Effort | Impact |
|---|---|---|---|
| 🥇 **1** | Fix the entity layer: `Organization`, `Service`, `FAQPage`, `Person`, `sameAs` (§6) | 1–2 days dev | 🔴 Site-wide, permanent |
| 🥈 **2** | Build **5 indexable money pages** for the 14 keywords (§4) | 3–5 days | 🔴 These keywords cannot rank without them |
| 🥉 **3** | Rewrite `llms.txt` + add quotable answer blocks (§8) | 1 day | 🟡 AI answer-engine visibility |
| 4 | Publish and interlink existing articles as cluster support (§5) | Ongoing | 🟡 Topical authority |
| 5 | Technical fixes from the audit (§10) | 1 day | 🟡 Removes ranking blockers |

> **EN —** Note the ratio: roughly **one week of focused work** on structure and entity outranks months of additional article production for this particular keyword set.
> **NL —** Let op de verhouding: ruwweg **één week gericht werk** aan structuur en entiteit levert voor deze zoekwoordenset meer op dan maanden extra artikelproductie.

---

<a id="2"></a>
## 2. 🎯 Keyword → Intent → Page Mapping
## 🎯 Zoekwoord → Intentie → Pagina

**EN —** Every keyword is classified by **SERP intent** (what Google currently rewards for that query) and assigned to exactly one target page. Assigning two pages to one keyword causes cannibalisation — the most common self-inflicted SEO wound on small sites.

**NL —** Elk zoekwoord is geclassificeerd op **SERP-intentie** (wat Google momenteel beloont voor die zoekopdracht) en toegewezen aan precies één doelpagina. Twee pagina's op één zoekwoord veroorzaakt kannibalisatie — de meest voorkomende zelfveroorzaakte SEO-schade op kleine sites.

| # | Keyword (EN) | Dutch target term | Intent | Winning page type | Target page |
|---|---|---|---|---|---|
| 01 | AI prototype to production | `ai prototype naar productie` | Commercial-investigative | Service + guide hybrid | **P1** |
| 02 | AI app to production | `ai app live zetten` | Commercial-investigative | Service | **P1** |
| 03 | AI code to production | `ai code productieklaar` | Mixed (some DIY) | Guide section | **P1** § |
| 04 | AI generated code production | `ai gegenereerde code productie` | Informational-commercial | Guide section | **P2** § |
| 05 | productionize AI application | `applicatie productieklaar maken` | Commercial | Service | **P2** |
| 06 | productionize AI app | `ai app productieklaar maken` | Commercial | Service | **P2** |
| 07 | make AI generated app production ready | `ai app productieklaar maken` | Commercial | Service + checklist | **P2** |
| 08 | AI development | `ai ontwikkeling` | ⚠️ Navigational/broad | — | ❌ **Not targeted** |
| 09 | AI app production problems | `ai app werkt niet live` | Problem-aware | Guide + FAQ | **P1** § |
| 10 | AI application production ready | `applicatie productieklaar` | Commercial | Service | **P2** |
| 11 | AI generated app security | `ai app beveiligen` | Commercial | Service | **P3** |
| 12 | AI generated code security | `ai gegenereerde code beveiliging` | Informational-commercial | Guide | **P3** |
| 13 | AI application security audit | `security audit applicatie` | 💰 Transactional | Service (money page) | **P4** |
| 14 | AI application scalability | `applicatie schaalbaar maken` | Consideration | Guide + service | **P5** |

### 2.1 Why keyword #08 is deliberately excluded / Waarom zoekwoord #08 bewust wordt uitgesloten

**EN —** Consistent with the Ads plan: `AI development` is a head term whose SERP is dominated by AI *model-building* consultancies, university programmes and job listings. Ranking for it would attract visitors looking for a service LaunchStudio does not sell, raising bounce rate and diluting the topical signal of the whole cluster. **Topical precision is a ranking asset** — targeting a term you cannot satisfy damages the pages around it.

**NL —** Consistent met het advertentieplan: `AI development` is een hoofdterm waarvan de zoekresultaten worden gedomineerd door consultancybureaus die AI-*modellen* bouwen, universitaire opleidingen en vacatures. Ranken op die term trekt bezoekers die een dienst zoeken die LaunchStudio niet levert, wat het bouncepercentage verhoogt en het thematische signaal van het hele cluster verwatert. **Thematische precisie is een rankingfactor** — mikken op een term die je niet kunt bedienen, schaadt de pagina's eromheen.

**Exception / Uitzondering:** the term may appear *inside* body copy as natural language ("AI development is not the same as production engineering") — that is contextual relevance, not targeting.

### 2.2 Search-behaviour note carried over from the Ads plan / Zoekgedrag, overgenomen uit het advertentieplan

**EN —** Dutch technical buyers search technical concepts **in English**, and "productionize" has no Dutch equivalent. For SEO this has a different consequence than for Ads: instead of splitting budget, you **publish both language versions and let the Dutch page carry the English term naturally in body copy** (e.g. *"productieklaar maken — in het Engels vaak 'production-ready' genoemd"*). This captures the Dutch searcher who types the English term while keeping the page unambiguously Dutch for hreflang.

**NL —** Nederlandse technische kopers zoeken technische begrippen **in het Engels**, en "productionize" heeft geen Nederlands equivalent. Voor SEO heeft dat een ander gevolg dan voor advertenties: in plaats van budget te splitsen, **publiceer je beide taalversies en laat je de Nederlandse pagina de Engelse term natuurlijk in de lopende tekst dragen** (bijv. *"productieklaar maken — in het Engels vaak 'production-ready' genoemd"*). Zo vang je de Nederlandse zoeker die de Engelse term intypt, terwijl de pagina voor hreflang ondubbelzinnig Nederlands blijft.

---

<a id="3"></a>
## 3. 🏗️ Site Architecture — Pillar & Cluster
## 🏗️ Site-architectuur — Pijler & Cluster

**EN —** One pillar page, four supporting service/guide pages, and the existing article library as the outer ring. Every page links up to the pillar; the pillar links down to all four. This is the structure Google uses to infer topical authority, and the structure an LLM traverses when deciding which URL best answers a question.

**NL —** Eén pijlerpagina, vier ondersteunende dienst-/gidspagina's en de bestaande artikelbibliotheek als buitenste ring. Elke pagina linkt omhoog naar de pijler; de pijler linkt omlaag naar alle vier. Dit is de structuur waaruit Google thematische autoriteit afleidt, en de structuur die een LLM doorloopt bij de keuze welke URL een vraag het best beantwoordt.

```
                    ┌─────────────────────────────────────┐
                    │  P1 · PILLAR                        │
                    │  Van AI-prototype naar productie    │
                    │  /van-prototype-naar-productie/     │
                    │  KW #01 #02 #03 #09                 │
                    └───────────────┬─────────────────────┘
                                    │
        ┌───────────────┬───────────┴───────┬────────────────┐
        │               │                   │                │
┌───────▼──────┐ ┌──────▼───────┐ ┌─────────▼──────┐ ┌───────▼────────┐
│ P2           │ │ P3           │ │ P4  💰         │ │ P5             │
│ Productie-   │ │ Beveiliging  │ │ Security audit │ │ Schaalbaarheid │
│ klaar maken  │ │ AI-code      │ │ applicatie     │ │ applicatie     │
│ /productie-  │ │ /ai-code-    │ │ /security-     │ │ /applicatie-   │
│ klaar-maken/ │ │ beveiligen/  │ │ audit/         │ │ schaalbaar/    │
│ #04 #05 #06  │ │ #11 #12      │ │ #13            │ │ #14            │
│ #07 #10      │ │              │ │                │ │                │
└──────┬───────┘ └──────┬───────┘ └────────┬───────┘ └───────┬────────┘
       │                │                  │                 │
       └────────────────┴──────────────────┴─────────────────┘
                                    │
                    ┌───────────────▼─────────────────────┐
                    │  SUPPORTING ARTICLES (existing 800) │
                    │  extra-8/9/10-decision, extra-6, -7 │
                    │  Each links UP to its pillar page   │
                    └─────────────────────────────────────┘
```

### 3.1 URL structure / URL-structuur

| Page | 🇳🇱 Dutch URL | 🇬🇧 English URL |
|---|---|---|
| **P1** Pillar | `/van-prototype-naar-productie/` | `/en/prototype-to-production/` |
| **P2** Production-ready | `/productieklaar-maken/` | `/en/production-ready/` |
| **P3** Code security | `/ai-code-beveiligen/` | `/en/ai-code-security/` |
| **P4** Security audit 💰 | `/security-audit-applicatie/` | `/en/application-security-audit/` |
| **P5** Scalability | `/applicatie-schaalbaar-maken/` | `/en/application-scalability/` |

> **EN — Why not `/diensten/...`?** A shallow, keyword-bearing slug outranks a nested one on a small site, and each of these five is a top-level commercial entity in its own right. Keep the depth at one level; do not bury them under a `/services/` folder.
> **NL — Waarom geen `/diensten/...`?** Een ondiepe slug met het zoekwoord erin presteert op een kleine site beter dan een geneste, en elk van deze vijf is op zichzelf een commerciële entiteit. Houd de diepte op één niveau; stop ze niet weg onder een map `/diensten/`.

> **EN — Slug rules:** lowercase, hyphenated, no dates, no stop words, never change after publication (a changed slug costs 3–6 months of accumulated authority unless 301-redirected correctly).
> **NL — Slugregels:** kleine letters, koppeltekens, geen datums, geen stopwoorden, nooit wijzigen na publicatie (een gewijzigde slug kost 3–6 maanden opgebouwde autoriteit, tenzij correct 301-doorverwezen).

---

<a id="4"></a>
## 4. 📄 Page Briefs — 5 New Money Pages
## 📄 Paginabriefings — 5 Nieuwe Money Pages

**EN —** Each brief is complete enough to hand to a writer without further explanation: target keywords, title tag and meta description with character counts, H1, full heading outline, word count, required schema, internal links, and the **answer block** — the 40–60-word directly-quotable paragraph that AI answer engines extract (see §8).

**NL —** Elke briefing is compleet genoeg om zonder verdere uitleg aan een schrijver te geven: doelzoekwoorden, title tag en metabeschrijving met tekenaantallen, H1, volledige kopstructuur, woordenaantal, vereist schema, interne links en het **antwoordblok** — de direct citeerbare alinea van 40–60 woorden die AI-antwoordmachines eruit lichten (zie §8).

> **Character limits / Tekenlimieten:** Title ≤ 60 · Meta description ≤ 155 · H1 = one per page / één per pagina

---

### 📄 P1 — PILLAR · Van AI-prototype naar productie

| Field | 🇳🇱 Dutch | 🇬🇧 English |
|---|---|---|
| **URL** | `/van-prototype-naar-productie/` | `/en/prototype-to-production/` |
| **Primary KW** | `ai prototype naar productie` | `ai prototype to production` |
| **Secondary KW** | `ai app live zetten`, `prototype werkt niet in productie`, `ai code productieklaar` | `ai app to production`, `ai code to production`, `ai app production problems` |
| **Intent** | Commercial-investigative | Commercial-investigative |
| **Word count** | 1.800–2.400 | 1,800–2,400 |
| **Page type** | Pillar: service + guide hybrid | Pillar: service + guide hybrid |

**Title tag**
- 🇳🇱 `Van AI-prototype naar productie in 1-3 weken | LaunchStudio` *(59)*
- 🇬🇧 `AI Prototype to Production: What It Takes | LaunchStudio` *(56)*

**Meta description**
- 🇳🇱 `Je AI-prototype werkt, maar gaat niet live. Ontdek wat er tussen prototype en productie zit: beveiliging, database, betalingen en hosting. Vanaf €800.` *(150)*
- 🇬🇧 `Your AI prototype works but will not go live. See exactly what sits between prototype and production: security, database, payments, hosting. From €800.` *(151)*

**H1**
- 🇳🇱 `Van AI-prototype naar productie: wat er echt tussen zit`
- 🇬🇧 `AI Prototype to Production: What Actually Sits in Between`

**Heading outline / Kopstructuur**

| Level | 🇳🇱 Dutch | 🇬🇧 English |
|---|---|---|
| H2 | Waarom een werkend prototype nog niet live kan | Why a working prototype still cannot go live |
| H2 | De zes dingen die tussen prototype en productie staan | The six things between prototype and production |
| H3 | 1. Toegangsrechten en authenticatie | 1. Access rules and authentication |
| H3 | 2. Database en dataintegriteit | 2. Database and data integrity |
| H3 | 3. Betalingen en facturatie | 3. Payments and billing |
| H3 | 4. Hosting, domein en deployment | 4. Hosting, domain and deployment |
| H3 | 5. Monitoring, back-ups en herstel | 5. Monitoring, backups and recovery |
| H3 | 6. AVG en dataverwerking | 6. GDPR and data processing |
| H2 | Gebouwd in Lovable, Bolt of Cursor? Wat er per tool ontbreekt | Built in Lovable, Bolt or Cursor? What each tool leaves out |
| H2 | Wat het kost en hoe lang het duurt | What it costs and how long it takes |
| H2 | Zelf doen of uitbesteden — een eerlijke afweging | Do it yourself or outsource — an honest comparison |
| H2 | Zo werkt het bij LaunchStudio: in 3 stappen live | How it works at LaunchStudio: live in 3 steps |
| H2 | Veelgestelde vragen | Frequently asked questions |

**Answer block (GEO) — place directly under H1 / plaats direct onder H1**
- 🇳🇱 *"Een AI-prototype naar productie brengen betekent zes dingen afdichten die AI-tools zoals Lovable, Bolt en Cursor standaard niet regelen: toegangsrechten, database-integriteit, betalingen, hosting, monitoring en AVG-naleving. Bij LaunchStudio duurt dat 1 tot 3 weken tegen een vaste prijs van €800 tot €7.500, waarbij je frontend onaangeroerd blijft."*
- 🇬🇧 *"Taking an AI prototype to production means closing six gaps that AI tools such as Lovable, Bolt and Cursor do not handle by default: access rules, database integrity, payments, hosting, monitoring and GDPR compliance. At LaunchStudio this takes 1 to 3 weeks at a fixed price of €800 to €7,500, with your frontend left untouched."*

**Schema required:** `Service` + `FAQPage` + `BreadcrumbList` + `Organization` (site-wide) — see §6
**Internal links out:** P2, P3, P4, P5 + `/#calculator` + `/#contact` + 4–6 supporting articles
**Internal links in:** homepage nav, all supporting articles in the cluster
**Primary CTA:** `Plan een 15-minuten gesprek` / `Book a 15-minute call` → `/#contact`

---

### 📄 P2 — Applicatie productieklaar maken

| Field | 🇳🇱 Dutch | 🇬🇧 English |
|---|---|---|
| **URL** | `/productieklaar-maken/` | `/en/production-ready/` |
| **Primary KW** | `applicatie productieklaar maken` | `make ai generated app production ready` |
| **Secondary KW** | `ai app productieklaar maken`, `software productieklaar`, `in productie nemen applicatie`, `ai gegenereerde code productie` | `productionize ai application`, `productionize ai app`, `ai application production ready`, `ai generated code production` |
| **Intent** | Commercial | Commercial |
| **Word count** | 1.500–2.000 | 1,500–2,000 |
| **Page type** | Service + checklist | Service + checklist |

**Title tag**
- 🇳🇱 `Applicatie productieklaar maken | Vaste prijs vanaf €800` *(56)*
- 🇬🇧 `Make Your AI App Production Ready | Fixed Price From €800` *(57)*

**Meta description**
- 🇳🇱 `Wat betekent productieklaar precies? De complete checklist plus wat het kost om je AI-app veilig, stabiel en live te krijgen. Vaste prijs, 1-3 weken.` *(149)*
- 🇬🇧 `What does production-ready actually mean? The full checklist plus what it costs to get your AI app secure, stable and live. Fixed price, 1-3 weeks.` *(147)*

**H1**
- 🇳🇱 `Applicatie productieklaar maken: de complete checklist`
- 🇬🇧 `Make Your AI App Production Ready: The Complete Checklist`

**Heading outline**

| Level | 🇳🇱 Dutch | 🇬🇧 English |
|---|---|---|
| H2 | Wat "productieklaar" precies betekent | What "production-ready" actually means |
| H3 | Productieklaar versus "het werkt op mijn laptop" | Production-ready versus "it works on my machine" |
| H2 | De productieklaar-checklist: 24 punten | The production-ready checklist: 24 items |
| H3 | Beveiliging en toegangsrechten (6 punten) | Security and access control (6 items) |
| H3 | Data en database (5 punten) | Data and database (5 items) |
| H3 | Betrouwbaarheid en herstel (5 punten) | Reliability and recovery (5 items) |
| H3 | Prestaties en schaal (4 punten) | Performance and scale (4 items) |
| H3 | Compliance en juridisch (4 punten) | Compliance and legal (4 items) |
| H2 | Wat AI-tools standaard níét regelen | What AI tools do not handle by default |
| H2 | Zelf doen: wat je realistisch in een weekend haalt | Doing it yourself: what a weekend realistically buys |
| H2 | Wat het kost om het te laten doen | What it costs to have it done |
| H2 | Veelgestelde vragen | Frequently asked questions |

**Answer block (GEO)**
- 🇳🇱 *"Productieklaar betekent dat een applicatie veilig, herstelbaar en controleerbaar is met echte gebruikers en echte data — niet alleen dat hij werkt. Concreet: toegangsrechten afgedwongen op de server, een getest back-upherstel, betalingen die niet dubbel boeken, monitoring die jou als eerste waarschuwt en een AVG-grondslag voor elke opgeslagen persoonsgegeven."*
- 🇬🇧 *"Production-ready means an application is secure, recoverable and observable with real users and real data — not merely that it works. Concretely: access rules enforced on the server, a tested backup restore, payments that cannot double-charge, monitoring that alerts you before customers do, and a lawful basis for every piece of personal data stored."*

**Schema required:** `Service` + `HowTo` (the checklist) + `FAQPage` + `BreadcrumbList`
**Internal links out:** P1 (up), P3, P4, P5, `/#packages`, `/#calculator`
**Primary CTA:** `Bereken je prijs` / `Calculate your price` → `/#calculator`

> **EN — Note on the word "productionize":** it has no Dutch equivalent and should never be calqued as *productionaliseren*. Instead, include one natural sentence on the Dutch page: *"In het Engels heet dit 'productionize' of 'production-ready maken'."* This captures the English-typing Dutch searcher without damaging the page's language signal.
> **NL — Let op het woord "productionize":** het heeft geen Nederlands equivalent en mag nooit worden vertaald als *productionaliseren*. Neem in plaats daarvan één natuurlijke zin op: *"In het Engels heet dit 'productionize' of 'production-ready maken'."* Zo vang je de Nederlandse zoeker die de Engelse term intypt, zonder het taalsignaal van de pagina te schaden.

---

### 📄 P3 — AI-code beveiligen

| Field | 🇳🇱 Dutch | 🇬🇧 English |
|---|---|---|
| **URL** | `/ai-code-beveiligen/` | `/en/ai-code-security/` |
| **Primary KW** | `ai app beveiligen` | `ai generated app security` |
| **Secondary KW** | `beveiliging ai applicatie`, `ai gegenereerde code beveiliging`, `is ai code veilig`, `datalek voorkomen applicatie` | `ai generated code security`, `secure ai generated code`, `lovable app security`, `supabase rls security` |
| **Intent** | Informational → commercial | Informational → commercial |
| **Word count** | 1.600–2.200 | 1,600–2,200 |
| **Page type** | Guide + service | Guide + service |

**Title tag**
- 🇳🇱 `AI-code beveiligen: de 7 lekken die het vaakst voorkomen` *(56)*
- 🇬🇧 `AI Code Security: The 7 Most Common Leaks | LaunchStudio` *(56)*

**Meta description**
- 🇳🇱 `AI-gegenereerde code lekt vaker data dan founders denken. De 7 meestvoorkomende lekken, hoe je ze zelf test en wat het kost om ze te dichten.` *(141)*
- 🇬🇧 `AI-generated code leaks data more often than founders expect. The 7 most common flaws, how to test for them yourself, and what a fix costs.` *(139)*

**H1**
- 🇳🇱 `AI-code beveiligen: de 7 lekken die we het vaakst vinden`
- 🇬🇧 `AI Code Security: The 7 Flaws We Find Most Often`

**Heading outline**

| Level | 🇳🇱 Dutch | 🇬🇧 English |
|---|---|---|
| H2 | Waarom AI-gegenereerde code structureel anders faalt | Why AI-generated code fails in a structural way |
| H2 | De 7 lekken die we het vaakst aantreffen | The 7 flaws we find most often |
| H3 | 1. Toegangsregels alleen in de frontend | 1. Access rules enforced only in the frontend |
| H3 | 2. Ontbrekende row-level security in Supabase | 2. Missing row-level security in Supabase |
| H3 | 3. API-sleutels in de browserbundel | 3. API keys shipped in the browser bundle |
| H3 | 4. Onbeperkte endpoints zonder rate limiting | 4. Unlimited endpoints without rate limiting |
| H3 | 5. Bestandsuploads zonder validatie | 5. File uploads without validation |
| H3 | 6. Wachtwoordherstel dat accounts prijsgeeft | 6. Password reset that leaks account existence |
| H3 | 7. Persoonsgegevens in logbestanden | 7. Personal data written into logs |
| H2 | Zelf testen: 5 controles zonder technische kennis | Test it yourself: 5 checks with no technical knowledge |
| H2 | AVG: wat een lek juridisch betekent | GDPR: what a leak means legally |
| H2 | Wat een beveiligingsronde kost | What a security pass costs |
| H2 | Veelgestelde vragen | Frequently asked questions |

**Answer block (GEO)**
- 🇳🇱 *"AI-gegenereerde code is niet onveiliger door slechte code, maar doordat de beveiliging op de verkeerde plek staat: toegangsregels zitten in de frontend in plaats van in de database. De zeven lekken die wij het vaakst vinden zijn ontbrekende row-level security, sleutels in de browserbundel, endpoints zonder rate limiting, uploads zonder validatie, wachtwoordherstel dat accounts prijsgeeft en persoonsgegevens in logs."*
- 🇬🇧 *"AI-generated code is not insecure because the code is bad, but because the security sits in the wrong place: access rules live in the frontend instead of in the database. The seven flaws we find most often are missing row-level security, keys in the browser bundle, endpoints without rate limiting, unvalidated uploads, password reset that leaks account existence, and personal data written into logs."*

**Schema required:** `Service` + `FAQPage` + `BreadcrumbList`
**Internal links out:** P4 (audit — the conversion path), P1 (up), P2, `/#contact`
**Primary CTA:** `Laat je app controleren` / `Get your app checked` → P4, then `/#contact`

---

### 📄 P4 — Security audit applicatie 💰 MONEY PAGE

| Field | 🇳🇱 Dutch | 🇬🇧 English |
|---|---|---|
| **URL** | `/security-audit-applicatie/` | `/en/application-security-audit/` |
| **Primary KW** | `security audit applicatie` | `ai application security audit` |
| **Secondary KW** | `beveiligingsaudit software`, `pentest webapplicatie`, `security audit saas`, `security audit kosten` | `web app security audit`, `saas security audit`, `penetration test web app`, `security audit cost` |
| **Intent** | 💰 Transactional | 💰 Transactional |
| **Word count** | 1.200–1.600 | 1,200–1,600 |
| **Page type** | Service (conversion-first) | Service (conversion-first) |

**Title tag**
- 🇳🇱 `Security audit applicatie | Vaste prijs, rapport in 5 dagen` *(59)*
- 🇬🇧 `Application Security Audit | Fixed Price, Report in 5 Days` *(58)*

**Meta description**
- 🇳🇱 `Onafhankelijke beveiligingsaudit van je webapplicatie of SaaS. Vaste prijs, rapport met prioriteiten in begrijpelijke taal, plus offerte om het te dichten.` *(155)*
- 🇬🇧 `Independent security audit of your web app or SaaS. Fixed price, a prioritised report in plain English, plus a fixed quote to close every gap found.` *(148)*

**H1**
- 🇳🇱 `Security audit voor je applicatie — vaste prijs, geen nacalculatie`
- 🇬🇧 `Security Audit for Your Application — Fixed Price, No Hourly Billing`

**Heading outline**

| Level | 🇳🇱 Dutch | 🇬🇧 English |
|---|---|---|
| H2 | Wat de audit precies onderzoekt | What the audit actually examines |
| H2 | Wat je krijgt: het rapport | What you receive: the report |
| H2 | Wat het kost | What it costs |
| H2 | Ook voor AI-gebouwde applicaties (Lovable, Bolt, Cursor) | Also for AI-built applications (Lovable, Bolt, Cursor) |
| H2 | Audit én herstel in één traject | Audit and remediation in one engagement |
| H2 | Wie het uitvoert | Who performs it |
| H2 | Wanneer je een audit nodig hebt | When you need an audit |
| H3 | Voor een investeringsronde of due diligence | Before a funding round or due diligence |
| H3 | Voor je eerste enterprise-klant | Before your first enterprise customer |
| H3 | Na een incident of verdenking | After an incident or suspicion |
| H2 | Veelgestelde vragen | Frequently asked questions |

**Answer block (GEO)**
- 🇳🇱 *"Een security audit van LaunchStudio onderzoekt toegangsrechten, dataopslag, authenticatie, afhankelijkheden en AVG-naleving van een webapplicatie of SaaS, inclusief applicaties gebouwd met AI-tools. Je ontvangt een rapport met geprioriteerde bevindingen in begrijpelijke taal plus een vaste offerte om ze te herstellen. Vaste prijs vanaf €500, rapport binnen 5 werkdagen."*
- 🇬🇧 *"A LaunchStudio security audit examines access control, data storage, authentication, dependencies and GDPR compliance of a web application or SaaS, including applications built with AI tools. You receive a prioritised report in plain language plus a fixed quote to remediate every finding. Fixed price from €500, report within 5 working days."*

**Schema required:** `Service` + `Offer` (with `priceRange`) + `FAQPage` + `BreadcrumbList` + `AggregateRating` *(only if real reviews exist — never fabricate)*
**Internal links out:** P3 (up-context), P1 (up), `/#contact`
**Internal links in:** P1, P2, P3, P5 + every security-themed article
**Primary CTA:** `Vraag een audit aan` / `Request an audit` → `/#contact`

> **EN —** This is the highest-value page in the cluster: "audit" is an explicit purchase word. Give it the shortest path to conversion — form above the fold, price stated on the page, no gating.
> **NL —** Dit is de waardevolste pagina van het cluster: "audit" is een expliciet koopwoord. Geef het de kortste route naar conversie — formulier boven de vouw, prijs zichtbaar op de pagina, geen afscherming.

---

### 📄 P5 — Applicatie schaalbaar maken

| Field | 🇳🇱 Dutch | 🇬🇧 English |
|---|---|---|
| **URL** | `/applicatie-schaalbaar-maken/` | `/en/application-scalability/` |
| **Primary KW** | `applicatie schaalbaar maken` | `ai application scalability` |
| **Secondary KW** | `schaalbaarheid applicatie`, `applicatie traag bij veel gebruikers`, `database performance verbeteren` | `ai app scalability`, `app slow with many users`, `prototype breaks at scale` |
| **Intent** | Consideration | Consideration |
| **Word count** | 1.400–1.800 | 1,400–1,800 |
| **Page type** | Guide + service | Guide + service |

**Title tag**
- 🇳🇱 `Applicatie schaalbaar maken: van 10 naar 10.000 gebruikers` *(58)*
- 🇬🇧 `Application Scalability: From 10 to 10,000 Users` *(48)*

**Meta description**
- 🇳🇱 `Waarom een prototype breekt bij 1.000 gebruikers en niet bij 10. De vijf knelpunten, hoe je ze meet en wat het kost om ze op te lossen.` *(135)*
- 🇬🇧 `Why a prototype breaks at 1,000 users and not at 10. The five bottlenecks, how to measure them, and what it costs to remove them.` *(129)*

**H1**
- 🇳🇱 `Applicatie schaalbaar maken: waarom prototypes breken bij groei`
- 🇬🇧 `Application Scalability: Why Prototypes Break as They Grow`

**Heading outline**

| Level | 🇳🇱 Dutch | 🇬🇧 English |
|---|---|---|
| H2 | Waarom het werkt bij 10 gebruikers en niet bij 1.000 | Why it works at 10 users and not at 1,000 |
| H2 | De vijf knelpunten, op volgorde van hoe vaak ze voorkomen | The five bottlenecks, ordered by how often they occur |
| H3 | 1. Een query per rij in plaats van één query | 1. One query per row instead of a single query |
| H3 | 2. Ontbrekende database-indexen | 2. Missing database indexes |
| H3 | 3. Geen paginering op lijsten | 3. No pagination on lists |
| H3 | 4. Berekeningen bij elke paginaweergave | 4. Aggregations recomputed on every page view |
| H3 | 5. Zwaar werk in het verzoek in plaats van in de achtergrond | 5. Heavy work in the request instead of the background |
| H2 | Zelf meten: waar je het ziet voordat klanten het merken | Measure it yourself: where to see it before customers do |
| H2 | Wat je nú moet bouwen en wat kan wachten | What to build now and what can wait |
| H2 | Wat het kost om het op te lossen | What it costs to fix |
| H2 | Veelgestelde vragen | Frequently asked questions |

**Answer block (GEO)**
- 🇳🇱 *"Een prototype breekt bij groei zelden door de hoeveelheid gebruikers, maar door vijf patronen die bij tien records onzichtbaar zijn: één databasequery per rij, ontbrekende indexen, lijsten zonder paginering, totalen die bij elke weergave opnieuw worden berekend, en zwaar werk dat in het webverzoek draait in plaats van op de achtergrond."*
- 🇬🇧 *"A prototype rarely breaks at scale because of user numbers, but because of five patterns that are invisible at ten records: one database query per row, missing indexes, lists without pagination, totals recomputed on every page view, and heavy work running inside the web request instead of in the background."*

**Schema required:** `Service` + `FAQPage` + `BreadcrumbList`
**Internal links out:** P1 (up), P2, P4, `/#calculator`
**Primary CTA:** `Bereken je prijs` / `Calculate your price` → `/#calculator`

---

<a id="5"></a>
## 5. 📚 Putting the Existing 800 Articles to Work
## 📚 De Bestaande 800 Artikelen Inzetten

**EN —** The article library is already written; its problem is that it is largely unpublished and almost entirely unlinked. Each supporting article should link **up** to exactly one pillar page with descriptive anchor text. That single change converts a flat archive into a topical cluster Google can read.

**NL —** De artikelbibliotheek is al geschreven; het probleem is dat die grotendeels ongepubliceerd is en vrijwel niet gelinkt. Elk ondersteunend artikel moet **omhoog** linken naar precies één pijlerpagina, met beschrijvende ankertekst. Die ene ingreep maakt van een plat archief een thematisch cluster dat Google kan lezen.

### 5.1 Article → pillar mapping (examples from the real library)

| Pillar | Supporting articles already written / Reeds geschreven ondersteunende artikelen |
|---|---|
| **P1** Prototype → productie | `extra-9-decision/11-you-built-it-in-lovable-the-exact-gaps-to-production.md`<br>`extra-9-decision/13-your-cursor-codebase-works-production-readiness-review.md`<br>`extra-9-decision/15-replit-deployed-it-why-thats-not-launched.md`<br>`extra-7-longtail/31-how-to-make-your-own-ai-app-production.md`<br>`extra-6-random/52-ai-deployment-day-checklist.md` |
| **P2** Productieklaar maken | `extra-8-decision/19-what-production-ready-really-costs-pricing-breakdown.md`<br>`extra-6-random/35-production-readiness-score-measures.md`<br>`extra-9-decision/21-launching-an-ai-wrapper-what-production-ready-means.md`<br>`extra-6-random/25-rejected-enterprise-deal-not-production-ready.md`<br>`extra-10-decision/82-deploying-changes-without-holding-your-breath.md` |
| **P3** AI-code beveiligen | `extra-7-longtail/15-where-security-in-ai-generated-code-usually-breaks.md`<br>`extra-7-longtail/16-ai-and-security-the-gap-every-founder-discovers.md`<br>`extra-6-random/01-security-means-different-things.md`<br>`extra-8-decision/88-ssl-certificate-easy-part-real-security-work.md`<br>`extra-10-decision/19-logging-what-to-record-and-what-you-must-never-write-down.md` |
| **P4** Security audit 💰 | `extra-9-decision/34-what-a-real-security-audit-report-looks-like.md`<br>`extra-8-decision/33-non-technical-founder-reads-security-audit-case-study.md`<br>`extra-9-decision/60-your-first-enterprise-security-questionnaire.md`<br>`extra-8-decision/13-enterprise-security-review-without-rebuilding-frontend-case-study.md`<br>`extra-6-random/04-acronym-cheat-sheet-security-review.md` |
| **P5** Schaalbaarheid | `extra-8-decision/57-what-founders-get-wrong-about-scalable-architecture.md`<br>`extra-8-decision/43-prototype-survives-viral-traffic-spike-case-study.md`<br>`extra-10-decision/88-performance-when-your-biggest-customer-arrives.md`<br>`extra-10-decision/18-caching-decisions-before-your-first-traffic-spike.md`<br>`extra-8-decision/53-why-prototype-database-schema-breaks-at-1000-users.md` |

### 5.2 Publishing priority / Publicatieprioriteit

**EN —** With 71 of 800+ articles live, the sequence matters more than the volume. Publish in this order:

1. **The 5 pillar pages first** (§4) — they are the link destinations; publishing supporting articles before them wastes the internal-link equity.
2. **5 supporting articles per pillar** (25 total) — enough to establish the cluster; each links up on publication.
3. **Case studies with named founders and results** — these are the most quotable assets for AI answer engines (§8) and the most persuasive for buyers.
4. **Everything else**, at a steady cadence of 2–3 per week. The audit specifically flagged bursty publishing as a pattern to avoid.

**NL —** Met 71 van 800+ artikelen live telt de volgorde zwaarder dan het volume. Publiceer in deze volgorde:

1. **Eerst de 5 pijlerpagina's** (§4) — zij zijn de linkbestemming; ondersteunende artikelen eerder publiceren verspilt de interne linkwaarde.
2. **5 ondersteunende artikelen per pijler** (25 in totaal) — genoeg om het cluster te vestigen; elk linkt bij publicatie omhoog.
3. **Casestudy's met naam en resultaat** — dit zijn de best citeerbare assets voor AI-antwoordmachines (§8) en het overtuigendst voor kopers.
4. **De rest**, in een gelijkmatig tempo van 2–3 per week. De audit signaleerde publiceren in bursts expliciet als te vermijden patroon.

### 5.3 Anchor-text rules / Regels voor ankertekst

| ❌ Never / Nooit | ✅ Always / Altijd |
|---|---|
| `klik hier`, `lees meer`, `deze pagina` | `applicatie productieklaar maken` |
| `click here`, `read more`, `this page` | `AI prototype to production` |
| The exact same anchor on every article | Vary naturally: exact, partial, and branded |
| More than 3 links to the same page in one article | 1–2 contextual links per article, in the body |

> **EN —** Also add a link **down** from each pillar to 4–6 of its best supporting articles. One-way linking (spokes → hub only) is a common and avoidable mistake; Google reads the reciprocal structure as the cluster boundary.
> **NL —** Voeg ook vanaf elke pijler een link **omlaag** toe naar 4–6 van de beste ondersteunende artikelen. Eenrichtingslinken (alleen spaken → hub) is een veelgemaakte en vermijdbare fout; Google leest juist de wederzijdse structuur als de clustergrens.

---

<a id="6"></a>
## 6. 🏛️ Entity Plan & Schema.org / Entiteitsplan & Schema.org

**EN —** This is priority #1 of the whole plan. The audit of 2026-07-31 found **no `Organization` schema anywhere on the site**, no `sameAs`, no `FAQPage` on a homepage that already contains a full FAQ in plain HTML, and a blog `Person` node whose author name is the internal username `"phu.lt"`. Until these are fixed, both Google and every LLM must guess who LaunchStudio is — and neither guesses in your favour.

**NL —** Dit is prioriteit 1 van het hele plan. De audit van 31-07-2026 vond **nergens `Organization`-schema op de site**, geen `sameAs`, geen `FAQPage` op een homepage die al een volledige FAQ in platte HTML bevat, en een `Person`-node op blogposts met de interne gebruikersnaam `"phu.lt"` als auteur. Zolang dit niet is opgelost, moeten zowel Google als elke LLM raden wie LaunchStudio is — en dat raden pakt niet in jouw voordeel uit.

### 6.1 `Organization` — site-wide (highest priority) 🥇

**EN —** Place once, site-wide, in the `<head>` of every page. This is the node that establishes the entity, the parent-brand relationship with Manifera, and the Amsterdam address.

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://launchstudio.eu/#organization",
  "name": "LaunchStudio",
  "alternateName": ["Launch Studio", "Launch Studio door Manifera"],
  "url": "https://launchstudio.eu/",
  "logo": {
    "@type": "ImageObject",
    "url": "https://launchstudio.eu/wp-content/uploads/launchstudio-logo.png",
    "width": 512,
    "height": 512
  },
  "description": "LaunchStudio takes AI-generated prototypes from tools such as Lovable, Bolt and Cursor to production: security, payments, authentication, database, hosting and deployment. Fixed price EUR 800-7,500, live in 1-3 weeks.",
  "slogan": "Launch Your Real Ideas to the Real World",
  "foundingDate": "2026",
  "parentOrganization": {
    "@type": "Organization",
    "name": "Manifera Software Development Pte Ltd",
    "url": "https://www.manifera.com/"
  },
  "founder": {
    "@type": "Person",
    "@id": "https://launchstudio.eu/#herre-roelevink"
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Herengracht 420",
    "postalCode": "1017 BZ",
    "addressLocality": "Amsterdam",
    "addressCountry": "NL"
  },
  "areaServed": [
    { "@type": "Country", "name": "Netherlands" },
    { "@type": "Country", "name": "Belgium" },
    { "@type": "Place", "name": "European Union" }
  ],
  "knowsAbout": [
    "AI prototype to production",
    "production readiness",
    "application security audit",
    "AI-generated code security",
    "Lovable", "Bolt", "Cursor", "Replit", "v0",
    "Supabase", "Stripe", "GDPR compliance"
  ],
  "sameAs": [
    "https://www.manifera.com/",
    "FILL_IN: https://www.linkedin.com/company/…",
    "FILL_IN: X / Facebook / Instagram profile URLs if they exist"
  ]
}
```

> **⚠️ EN —** `sameAs` must contain **only profiles that genuinely exist and are controlled by LaunchStudio**. An invented or wrong URL actively damages entity confidence — it is worse than an empty array. If LaunchStudio has no company LinkedIn page yet, creating one is itself a high-value entity task.
> **⚠️ NL —** `sameAs` mag **uitsluitend profielen bevatten die echt bestaan en van LaunchStudio zijn**. Een verzonnen of verkeerde URL schaadt het entiteitsvertrouwen actief — dat is erger dan een lege array. Heeft LaunchStudio nog geen bedrijfspagina op LinkedIn, dan is het aanmaken daarvan zelf een waardevolle entiteitstaak.

### 6.2 `Person` — fix the author node 🥇

**EN —** Replace `"name": "phu.lt"` on every blog post. E-E-A-T evaluates *who wrote this*; an internal username signals an unmaintained site. Add the CEO node site-wide as well, since he is the entity's public face.

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://launchstudio.eu/#herre-roelevink",
  "name": "Herre Roelevink",
  "jobTitle": "Founder & Managing Director",
  "description": "Founder of Manifera and CEO of LaunchStudio. Background in Agile/Scrum, offshore software management and cybersecurity. Co-founder of CyberDevOps, now CFLW Cyber Strategies, which developed the Dark Web Monitor with TNO.",
  "worksFor": { "@id": "https://launchstudio.eu/#organization" },
  "nationality": { "@type": "Country", "name": "Netherlands" },
  "sameAs": [
    "https://www.linkedin.com/in/herre-roelevink-director-manifera/"
  ]
}
```

### 6.3 `Service` + `Offer` — for each of the 5 pages 🥈

**EN —** One `Service` node per money page. Pricing is one of the things people most often ask an AI assistant, and an `Offer` with a real `priceRange` is directly extractable. Example for **P4 (security audit)**:

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "https://launchstudio.eu/security-audit-applicatie/#service",
  "name": "Security audit voor webapplicaties en SaaS",
  "serviceType": "Application security audit",
  "provider": { "@id": "https://launchstudio.eu/#organization" },
  "areaServed": { "@type": "Country", "name": "Netherlands" },
  "audience": {
    "@type": "Audience",
    "audienceType": "Startups and scale-ups with AI-generated applications"
  },
  "description": "Onafhankelijke beveiligingsaudit van een webapplicatie of SaaS, inclusief applicaties gebouwd met AI-tools zoals Lovable, Bolt of Cursor. Rapport met geprioriteerde bevindingen plus vaste offerte voor herstel.",
  "offers": {
    "@type": "Offer",
    "priceCurrency": "EUR",
    "price": "500",
    "priceSpecification": {
      "@type": "PriceSpecification",
      "minPrice": "500",
      "maxPrice": "3500",
      "priceCurrency": "EUR",
      "valueAddedTaxIncluded": false
    },
    "availability": "https://schema.org/InStock",
    "url": "https://launchstudio.eu/security-audit-applicatie/"
  }
}
```

**Repeat with these values / Herhaal met deze waarden:**

| Page | `name` | `price` | `priceRange` |
|---|---|---|---|
| P1 | Van AI-prototype naar productie | 800 | €800 – €7.500 |
| P2 | Applicatie productieklaar maken | 800 | €800 – €3.500 |
| P3 | Beveiliging van AI-gegenereerde code | 500 | €500 – €2.000 |
| P4 | Security audit applicatie | 500 | €500 – €3.500 |
| P5 | Applicatie schaalbaar maken | 800 | €800 – €4.500 |

> **EN —** Only publish prices you will honour. A `priceRange` that disagrees with the on-page price calculator is a trust problem with both users and Google.
> **NL —** Publiceer alleen prijzen die je nakomt. Een `priceRange` die afwijkt van de prijscalculator op de site is een vertrouwensprobleem, bij gebruikers én bij Google.

### 6.4 `FAQPage` — homepage + all 5 pages 🥇

**EN —** The homepage already contains a full FAQ in plain HTML ("Wat kost het precies?", "Blijft mijn code van mij?") that is not marked up. Marking it costs an hour and is the single most reliably-extracted format for AI direct answers. Each of the 5 new pages ends with its own FAQ section, marked up the same way.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat kost het om een AI-prototype productieklaar te maken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Bij LaunchStudio kost dit een vaste prijs tussen €800 en €7.500, afhankelijk van wat er gebouwd moet worden en wat er al werkt. Je krijgt de offerte na een gesprek van 15 minuten, met vaste scope en vaste doorlooptijd van 1 tot 3 weken."
      }
    },
    {
      "@type": "Question",
      "name": "Blijft mijn code van mij?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. Alle code blijft 100% eigendom van de opdrachtgever, tijdens en na het traject. Er is geen licentieconstructie en geen lock-in."
      }
    }
  ]
}
```

### 6.5 Schema implementation checklist / Implementatiechecklist

- [ ] `Organization` in `<head>` site-wide, with correct `@id` / site-breed met correcte `@id`
- [ ] `Person` node for Herre Roelevink; blog author replaced (never `phu.lt`)
- [ ] `Service` + `Offer` on each of P1–P5
- [ ] `FAQPage` on the homepage **and** on P1–P5
- [ ] `BreadcrumbList` on all new pages
- [ ] `WebSite` with `SearchAction` retained (already present / al aanwezig)
- [ ] Every node linked by `@id` — one connected graph, not five orphans
- [ ] Validated in Google Rich Results Test **and** Schema.org validator
- [ ] ❌ No `AggregateRating` unless real, verifiable reviews exist / tenzij er echte, verifieerbare reviews zijn

---

<a id="7"></a>
## 7. 📍 GEO-Entity — Geographic Positioning / Geografische Positionering

**EN —** "GEO-entity" in this project means two things at once, and both matter here. §8 covers Generative Engine Optimization; this section covers the *geographic* entity — making LaunchStudio unambiguously a **Dutch** company to Google, which is what lets it compete for Dutch commercial queries against local agencies.

**NL —** "GEO-entiteit" betekent in dit project twee dingen tegelijk, en beide zijn hier van belang. §8 behandelt Generative Engine Optimization; deze sectie behandelt de *geografische* entiteit — LaunchStudio ondubbelzinnig als **Nederlands** bedrijf neerzetten bij Google, wat nodig is om op Nederlandse commerciële zoekopdrachten te concurreren met lokale bureaus.

### 7.1 The NAP consistency problem / Het NAP-consistentieprobleem

**EN —** NAP = Name, Address, Phone. Google cross-references these across the web to confirm a business is real and located where it claims. LaunchStudio inherits three offices from Manifera, and that inheritance is a risk as much as an asset: if the Amsterdam address appears only on Manifera's site and never on LaunchStudio's own, Google may treat LaunchStudio as an unlocated sub-brand.

**NL —** NAP = Naam, Adres, Telefoonnummer. Google vergelijkt deze gegevens over het hele web om te bevestigen dat een bedrijf echt bestaat en zit waar het beweert. LaunchStudio erft drie kantoren van Manifera, en die erfenis is net zo goed een risico als een bezit: staat het Amsterdamse adres alleen op de site van Manifera en nooit op die van LaunchStudio, dan kan Google LaunchStudio als een niet-gelokaliseerd submerk behandelen.

| Element | Value to use everywhere, identically / Overal identiek te gebruiken waarde |
|---|---|
| **Name** | `LaunchStudio` (never `Launch Studio` in structured data — pick one and never vary) |
| **Address** | `Herengracht 420, 1017 BZ Amsterdam, Nederland` |
| **Country** | `NL` |
| **Parent** | `Manifera Software Development Pte Ltd` |
| **Phone** | ⚠️ `FILL_IN` — a Dutch number (+31) is a meaningful local trust signal; a foreign number undermines it |

### 7.2 Where the Dutch entity signal must appear / Waar het Nederlandse entiteitssignaal moet staan

| # | Location / Plaats | Action / Actie | Priority |
|---|---|---|---|
| 1 | Site footer, every page | Full NAP block in plain HTML text (not an image) | 🔴 |
| 2 | `Organization` schema | `address` + `addressCountry: NL` (§6.1) | 🔴 |
| 3 | Contact section | Amsterdam address visible, not only a form | 🔴 |
| 4 | Google Business Profile | Create/claim for the Amsterdam location | 🟡 |
| 5 | LinkedIn company page | Location set to Amsterdam, Netherlands | 🟡 |
| 6 | Manifera.com | Link to launchstudio.eu describing it as the Dutch launch service | 🟡 |
| 7 | Dutch directories | KvK listing, Dutch startup directories, BNI profile | 🟢 |
| 8 | Page copy | Natural mentions of Amsterdam / Nederland in P1–P5 body text | 🟢 |

> **EN —** Item 6 was specifically flagged in the audit: the homepage says "door Manifera" but does **not hyperlink** it. A single link from `manifera.com` to `launchstudio.eu` — and back — turns two disconnected sites into one entity graph with 11 years of accumulated authority behind it. This is the cheapest authority gain available.
> **NL —** Punt 6 werd expliciet in de audit genoemd: de homepage zegt "door Manifera" maar **linkt er niet naar**. Eén link van `manifera.com` naar `launchstudio.eu` — en terug — maakt van twee losse sites één entiteitsgrafiek met elf jaar opgebouwde autoriteit erachter. Dit is de goedkoopst haalbare autoriteitswinst.

### 7.3 Local relevance without fake local pages / Lokale relevantie zonder nep-lokale pagina's

**EN —** The `extra-5-local` cluster already contains city-targeted articles (Amsterdam, Utrecht, Arnhem, Nijmegen …). Those support local long-tail queries and should link up to P1–P5. What must **not** happen is spinning the five money pages into 40 near-duplicate city variants — Google treats programmatic city pages with identical bodies as doorway pages, and the penalty applies site-wide.

**NL —** Het cluster `extra-5-local` bevat al artikelen gericht op steden (Amsterdam, Utrecht, Arnhem, Nijmegen …). Die ondersteunen lokale longtail-zoekopdrachten en moeten omhoog linken naar P1–P5. Wat **niet** mag gebeuren, is de vijf money pages uitrollen in 40 bijna-identieke stadsvarianten — Google beschouwt programmatische stadspagina's met dezelfde inhoud als doorway pages, en de sanctie treft de hele site.

---

<a id="8"></a>
## 8. 🤖 GEO — Generative Engine Optimization

**EN —** GEO is optimising to be **cited by** ChatGPT, Perplexity, Claude and Google AI Overviews, rather than clicked in a blue-link list. It rewards a different set of properties than classic SEO: entity clarity, directly-quotable statements, explicit numbers, comparison tables, and crawlable server-rendered HTML. The audit already identified two existing strengths (server-rendered content, an `llms.txt` file) and one decisive weakness (entity clarity — fixed in §6).

**NL —** GEO is optimaliseren om **geciteerd te worden door** ChatGPT, Perplexity, Claude en Google AI Overviews, in plaats van aangeklikt in een lijst blauwe links. Het beloont andere eigenschappen dan klassieke SEO: entiteitshelderheid, direct citeerbare uitspraken, expliciete getallen, vergelijkingstabellen en crawlbare server-gerenderde HTML. De audit stelde al twee bestaande sterktes vast (server-gerenderde content, een `llms.txt`-bestand) en één doorslaggevende zwakte (entiteitshelderheid — opgelost in §6).

### 8.1 The answer block — the single highest-leverage GEO technique

**EN —** Directly under each H1, place a **40–60-word paragraph that answers the page's core question completely, on its own, with a number in it**. LLMs extract self-contained passages; a paragraph that requires the surrounding page to make sense will not be quoted. Every one of the five page briefs in §4 already contains its answer block, ready to paste.

**NL —** Plaats direct onder elke H1 een **alinea van 40–60 woorden die de kernvraag van de pagina volledig en op zichzelf beantwoordt, met een getal erin**. LLM's lichten zelfstandige passages eruit; een alinea die de omringende pagina nodig heeft om te kloppen, wordt niet geciteerd. Elk van de vijf paginabriefings in §4 bevat al zijn antwoordblok, klaar om te plakken.

| ✅ Quotable / Citeerbaar | ❌ Not quotable / Niet citeerbaar |
|---|---|
| "Taking an AI prototype to production takes 1–3 weeks and costs €800–€7,500." | "It depends on your situation — read on to find out more." |
| Contains a number, a timeframe, a named entity | Vague, comparative, or dependent on earlier context |
| One idea, complete in itself | "As mentioned above…", "This is where we come in…" |

### 8.2 The prompts to target / De prompts om op te mikken

**EN —** In GEO you optimise for *prompts*, not keywords. These are the real questions a Dutch founder asks an AI assistant, and each maps to a page that must answer it explicitly.

| Prompt (as typed into an AI assistant) | Page that must answer it |
|---|---|
| "My Lovable app works but I can't launch it — what's missing?" | P1 |
| "Wat betekent productieklaar voor een webapplicatie?" | P2 |
| "Is code generated by AI tools secure enough for production?" | P3 |
| "Hoeveel kost een security audit voor een SaaS in Nederland?" | P4 |
| "Why does my app get slow after 1,000 users?" | P5 |
| "Who can take an AI prototype to production in the Netherlands?" | P1 + `Organization` (§6) |
| "What does LaunchStudio cost?" | Homepage `FAQPage` + `Offer` (§6) |

### 8.3 Rewrite `llms.txt` / `llms.txt` herschrijven

**EN —** The current file is Yoast's auto-generated version: it lists 5 of 71 articles, includes legal boilerplate, and **never mentions pricing, packages or the value proposition**. An LLM reading only this file would not know what LaunchStudio sells. Replace it with a curated file that leads with the offer.

**NL —** Het huidige bestand is de automatisch gegenereerde versie van Yoast: het noemt 5 van de 71 artikelen, bevat juridische standaardteksten en **noemt prijzen, pakketten of de waardepropositie nergens**. Een LLM die alleen dit bestand leest, weet niet wat LaunchStudio verkoopt. Vervang het door een gecureerd bestand dat met het aanbod begint.

```markdown
# LaunchStudio

> LaunchStudio takes AI-generated prototypes to production. Founders build in
> Lovable, Bolt, Cursor, Replit or v0; LaunchStudio adds the security, database,
> payments, hosting and deployment work needed to launch, without rebuilding the
> frontend. Fixed price EUR 800-7,500, live in 1-3 weeks. Based in Amsterdam,
> the Netherlands. Part of Manifera Software Development, 11+ years of
> engineering experience, 160+ delivered projects.

## What we do
- Prototype to production: https://launchstudio.eu/van-prototype-naar-productie/
- Production-ready checklist: https://launchstudio.eu/productieklaar-maken/
- AI code security: https://launchstudio.eu/ai-code-beveiligen/
- Application security audit: https://launchstudio.eu/security-audit-applicatie/
- Application scalability: https://launchstudio.eu/applicatie-schaalbaar-maken/

## Pricing
- Launch Ready (Klaar voor lancering): EUR 800-3,500 fixed price
- Launch & Grow (Lancering & Groei): EUR 2,500-7,500 fixed price + EUR 49/month
- Security audit: from EUR 500
- Price calculator: https://launchstudio.eu/#calculator
- All code remains 100% owned by the client.

## How it works
1. Describe your product (no technical knowledge required)
2. 15-minute intro call, then a fixed-price quote with fixed scope
3. We build, you launch - typically 1-3 weeks

## Who we serve
AI-native founders, technical solo founders, agencies needing a white-label
engineering partner, and SaaS scale-ups. Primary market: the Netherlands,
Belgium and the wider EU.

## Company
LaunchStudio (Launch Studio door Manifera)
Herengracht 420, 1017 BZ Amsterdam, Netherlands
Parent company: Manifera Software Development Pte Ltd - https://www.manifera.com/
Founder & CEO: Herre Roelevink
Enterprise clients of the parent company include Vodafone, TNO and CFLW.

## Key articles
[list 20-30 of the strongest published articles with title + URL]
```

### 8.4 Other GEO levers / Overige GEO-hefbomen

| Lever / Hefboom | Action / Actie | Why / Waarom |
|---|---|---|
| **Comparison tables** | One table per money page (LaunchStudio vs agency vs freelancer vs DIY) | LLMs extract tables far more reliably than prose |
| **Explicit numbers** | €800, 1–3 weeks, 11+ years, 160+ projects, 24-point checklist | Numbers are what get quoted verbatim |
| **Named case studies** | Founder name, product, problem, result, timeline | Specificity is the strongest citability signal |
| **Definition blocks** | Define "productieklaar" / "production-ready" explicitly on P2 | Definition queries are heavily AI-answered |
| **No JS dependency** | Keep key facts in server-rendered HTML | Most LLM crawlers do not execute JavaScript |
| **`robots.txt`** | Do **not** block `GPTBot`, `ClaudeBot`, `PerplexityBot` | Blocking them removes you from the answer set entirely |
| **Freshness** | Visible `dateModified` on every page | Recency is weighted in AI answer selection |

### 8.5 Measuring GEO / GEO meten

**EN —** There is no Search Console for AI answers, so measurement is manual and comparative. Run this once a month:

1. Ask the 7 prompts in §8.2 in **ChatGPT, Perplexity, Claude and Google AI Overviews**, in Dutch and English.
2. Record: was LaunchStudio mentioned? cited with a link? which URL? which competitor was cited instead?
3. Track referral traffic from `chat.openai.com`, `perplexity.ai` and `claude.ai` in GA4 as a secondary signal.
4. Keep the results in a simple sheet — the trend over months is the metric, not any single answer.

**NL —** Er bestaat geen Search Console voor AI-antwoorden, dus meten gebeurt handmatig en vergelijkend. Voer dit maandelijks uit:

1. Stel de 7 prompts uit §8.2 in **ChatGPT, Perplexity, Claude en Google AI Overviews**, in het Nederlands en Engels.
2. Noteer: werd LaunchStudio genoemd? met bronlink? welke URL? welke concurrent werd in plaats daarvan geciteerd?
3. Volg verwijzend verkeer van `chat.openai.com`, `perplexity.ai` en `claude.ai` in GA4 als secundair signaal.
4. Houd de resultaten bij in een eenvoudig overzicht — de trend over maanden is de maatstaf, niet één los antwoord.

---

<a id="9"></a>
## 9. 🌐 Bilingual Strategy & hreflang / Tweetalige Strategie & hreflang

**EN —** Every one of the five pages exists twice: Dutch at the root, English under `/en/`. The Dutch version is canonical for the Dutch market; the English version serves both the English-typing Dutch searcher and the wider EU audience.

**NL —** Elk van de vijf pagina's bestaat tweemaal: Nederlands in de root, Engels onder `/en/`. De Nederlandse versie is canoniek voor de Nederlandse markt; de Engelse bedient zowel de Nederlandse zoeker die Engels intypt als het bredere EU-publiek.

### 9.1 hreflang implementation

```html
<!-- On the Dutch page / Op de Nederlandse pagina -->
<link rel="alternate" hreflang="nl-NL" href="https://launchstudio.eu/productieklaar-maken/" />
<link rel="alternate" hreflang="en"    href="https://launchstudio.eu/en/production-ready/" />
<link rel="alternate" hreflang="x-default" href="https://launchstudio.eu/en/production-ready/" />
<link rel="canonical" href="https://launchstudio.eu/productieklaar-maken/" />
```

| Rule / Regel | EN | NL |
|---|---|---|
| Reciprocity | Both pages must reference each other, or Google ignores the pair | Beide pagina's moeten naar elkaar verwijzen, anders negeert Google het paar |
| Self-reference | Each page includes its own `hreflang` | Elke pagina bevat zijn eigen `hreflang` |
| Canonical | Always self-canonical, never cross-language | Altijd self-canonical, nooit cross-language |
| `x-default` | Point to the English version (widest audience) | Verwijs naar de Engelse versie (breedste publiek) |
| ❌ Never | Never use `nl-BE` unless a genuinely separate Belgian page exists | Gebruik nooit `nl-BE` tenzij er echt een aparte Belgische pagina is |

### 9.2 Translation ≠ localisation / Vertaling ≠ lokalisatie

**EN —** The English page is not a machine translation of the Dutch. Three things differ deliberately:

- **Terminology:** the Dutch page says *productieklaar* and mentions *"in het Engels: production-ready"* once. The English page uses *production-ready* and *productionize*, which have no Dutch counterpart.
- **Compliance framing:** the Dutch page leads with **AVG**; the English page leads with **GDPR** and adds a sentence on EU data residency, which matters more to non-Dutch EU readers.
- **Proof:** the Dutch page emphasises Amsterdam and Dutch clients; the English page emphasises the EU-wide track record of the parent company.

**NL —** De Engelse pagina is geen machinevertaling van de Nederlandse. Drie dingen verschillen bewust:

- **Terminologie:** de Nederlandse pagina zegt *productieklaar* en noemt eenmaal *"in het Engels: production-ready"*. De Engelse pagina gebruikt *production-ready* en *productionize*, die geen Nederlandse tegenhanger hebben.
- **Compliancekader:** de Nederlandse pagina begint met **AVG**; de Engelse met **GDPR**, plus een zin over EU-dataresidentie, wat voor niet-Nederlandse EU-lezers zwaarder weegt.
- **Bewijsvoering:** de Nederlandse pagina benadrukt Amsterdam en Nederlandse klanten; de Engelse benadrukt het EU-brede trackrecord van het moederbedrijf.

---

<a id="10"></a>
## 10. 🔧 Technical SEO Prerequisites / Technische SEO-randvoorwaarden

**EN —** These come straight from the audit of 2026-07-31 and are **blockers**: the five new pages will underperform until they are fixed, because the issues are site-wide.

**NL —** Deze komen rechtstreeks uit de audit van 31-07-2026 en zijn **blokkades**: de vijf nieuwe pagina's zullen onderpresteren zolang ze niet zijn opgelost, omdat de problemen site-breed zijn.

| # | Issue from audit / Bevinding uit audit | Fix | Effort | Priority |
|---|---|---|---|---|
| 1 | Duplicate hardcoded OG/meta-description block in the theme header — invalid duplicate meta tags site-wide | Remove the hardcoded block; let Yoast output them | 1h | 🔴 |
| 2 | EN homepage `<title>` is 131 chars and duplicates the meta description | Rewrite to ≤60 chars | 15m | 🔴 |
| 3 | Stray `rel="next"` on the homepage | Remove | 15m | 🟢 |
| 4 | `"door Manifera"` is not hyperlinked | Link to `manifera.com` (§7.2) | 15m | 🔴 |
| 5 | No `Organization` schema | §6.1 | 2h | 🔴 |
| 6 | Homepage FAQ not marked as `FAQPage` | §6.4 | 1h | 🔴 |
| 7 | Author schema reads `"phu.lt"` | §6.2 | 1h | 🔴 |
| 8 | No `Service`/`Offer` schema | §6.3 | 2h | 🟡 |
| 9 | `llms.txt` sparse and offer-free | §8.3 | 2h | 🟡 |
| 10 | Thin article bodies (case studies especially) | Extend toward 800–1,200 words | Ongoing | 🟡 |
| 11 | TTFB / Core Web Vitals | Page caching + CDN | 4h | 🟡 |
| 12 | 71 live of 800+ produced | Steady publishing cadence (§5.2) | Ongoing | 🔴 |

### 10.1 Checks for the 5 new pages specifically / Controles specifiek voor de 5 nieuwe pagina's

- [ ] Indexable: no `noindex`, present in `sitemap.xml` / Indexeerbaar: geen `noindex`, aanwezig in `sitemap.xml`
- [ ] Self-canonical + reciprocal `hreflang` (§9.1)
- [ ] One `<h1>` per page, headings in hierarchical order / Eén `<h1>`, koppen in hiërarchische volgorde
- [ ] LCP < 2.5s on mobile / op mobiel
- [ ] All images with descriptive `alt` and compressed / Alle afbeeldingen met beschrijvende `alt`, gecomprimeerd
- [ ] Answer block (§8.1) is in server-rendered HTML, not JS-injected
- [ ] Schema validates in Rich Results Test / valideert in Rich Results Test
- [ ] Submitted in Search Console after publication / Ingediend in Search Console na publicatie

---

<a id="11"></a>
## 11. 🔗 Internal Linking Rules / Regels voor Interne Links

| Direction / Richting | Rule / Regel |
|---|---|
| **Homepage → pillar** | Link P1 from the main navigation, not only from the footer |
| **Pillar → sub-pages** | P1 links to P2, P3, P4, P5 in body copy with keyword anchors |
| **Sub-page → pillar** | Every sub-page links back up to P1 within the first 300 words |
| **Sub-page ↔ sub-page** | P3 → P4 is the key conversion path (security concern → audit purchase) |
| **Article → pillar** | Every supporting article links up to exactly one pillar, once, in the body |
| **Pillar → article** | Each pillar links down to 4–6 of its strongest supporting articles |
| **Anywhere → Manifera** | At least one contextual link to `manifera.com` per money page (§7.2) |
| **Depth** | No money page more than 2 clicks from the homepage |

> **EN —** Do not add a "related articles" widget instead of contextual links. Automated widgets pass far less signal than a link inside a sentence that explains why the reader should follow it.
> **NL —** Voeg geen widget "gerelateerde artikelen" toe in plaats van contextuele links. Geautomatiseerde widgets geven veel minder signaal door dan een link in een zin die uitlegt waarom de lezer hem zou volgen.

---

<a id="12"></a>
## 12. 📅 90-Day Execution Calendar / 90-Dagen Uitvoeringskalender

### Weeks 1–2 · Foundation / Fundament
| # | Task | Owner | Deliverable |
|---|---|---|---|
| 1 | Fix audit items 1–4, 7 (§10) | Dev | Clean meta tags, real author, Manifera link |
| 2 | Implement `Organization` + `Person` schema (§6.1, §6.2) | Dev | Validated in Rich Results Test |
| 3 | Mark up homepage FAQ as `FAQPage` (§6.4) | Dev | Validated |
| 4 | Create/claim LinkedIn company page + Google Business Profile | Marketing | Real `sameAs` URLs |
| 5 | Decide final URLs and slugs (§3.1) | Marketing | Signed-off URL list |

### Weeks 3–5 · Money pages / Money pages
| # | Task | Owner | Deliverable |
|---|---|---|---|
| 6 | Write and publish **P4** (security audit) first | Content | Highest commercial intent ships first |
| 7 | Write and publish **P1** (pillar) | Content | Cluster hub live |
| 8 | Write and publish **P2** | Content | — |
| 9 | Add `Service` + `Offer` + `FAQPage` schema per page (§6.3) | Dev | Validated |
| 10 | hreflang pairs for every published page (§9.1) | Dev | Reciprocal, validated |

### Weeks 6–8 · Cluster / Cluster
| # | Task | Owner | Deliverable |
|---|---|---|---|
| 11 | Write and publish **P3** and **P5** | Content | All 5 pages live |
| 12 | Publish 25 supporting articles, 5 per pillar (§5.1) | Content | Each links up on publication |
| 13 | Add downward links from each pillar to its articles | Content | Reciprocal cluster |
| 14 | Rewrite `llms.txt` (§8.3) | Marketing | Offer-led file |
| 15 | First GEO measurement run (§8.5) | Marketing | Baseline sheet |

### Weeks 9–12 · Consolidation / Consolidatie
| # | Task | Owner | Deliverable |
|---|---|---|---|
| 16 | Publishing cadence 2–3 articles/week | Content | Backlog moving |
| 17 | Page caching + CDN (§10 item 11) | Dev | LCP < 2.5s |
| 18 | Extend thin case studies to 800–1,200 words | Content | Citability |
| 19 | Second GEO measurement run — compare to baseline | Marketing | Trend visible |
| 20 | Quarterly report: rankings, impressions, AI citations, leads | Marketing | Day 90 review |

---

<a id="13"></a>
## 13. 📊 KPIs & Measurement / KPI's & Meting

### 13.1 Targets / Doelen

| Metric | Day 30 | Day 60 | Day 90 | Day 180 |
|---|---|---|---|---|
| Money pages live / Money pages live | 3 | 5 | 5 | 5 |
| Indexed in Search Console | 3 | 5 | 5 | 5 |
| Keywords in top 100 (of the 14) | 4 | 8 | 11 | 13 |
| Keywords in top 10 | 0 | 1 | 3 | 6 |
| Organic sessions to the 5 pages | 40 | 150 | 400 | 1,200 |
| AI citations (7 prompts × 4 engines = 28) | 2 | 6 | 10 | 16 |
| Organic leads from the cluster | 0–1 | 1–2 | 3–5 | 8–12 |
| Live articles total / Live artikelen totaal | 80 | 100 | 125 | 180 |

### 13.2 Realistic timing / Realistische doorlooptijd

**EN —** New service pages on an established domain typically take **3–6 months** to reach stable rankings for commercial terms. The Dutch keywords will move faster than the English ones because competition is thinner; the English keywords compete against a global field. Do not judge the plan before day 90, and expect the ranking curve to be flat for the first 6–8 weeks — that is normal, not failure.

**NL —** Nieuwe dienstpagina's op een bestaand domein hebben doorgaans **3–6 maanden** nodig om stabiel te ranken op commerciële termen. De Nederlandse zoekwoorden bewegen sneller dan de Engelse, omdat de concurrentie dunner is; de Engelse concurreren met een wereldwijd veld. Beoordeel het plan niet vóór dag 90, en verwacht dat de rankingcurve de eerste 6–8 weken vlak blijft — dat is normaal, geen mislukking.

### 13.3 Tools / Gereedschap

| Purpose | Tool | Cadence |
|---|---|---|
| Rankings & impressions | Google Search Console | Weekly |
| Traffic & conversions | GA4 (with Consent Mode v2) | Weekly |
| Schema validation | Rich Results Test + Schema.org validator | On every publish |
| AI citations | Manual prompt log (§8.5) | Monthly |
| Crawl health | Screaming Frog or Ahrefs Site Audit | Monthly |
| Backlink growth | Ahrefs / Search Console links report | Monthly |

---

<a id="14"></a>
## 14. ⚠️ Risks / Risico's

| # | Risk / Risico | Impact | Mitigation / Maatregel |
|---|---|---|---|
| 1 | **Money pages never get built** and the plan reverts to writing more articles | 🔴 High | §1: articles cannot rank commercial service queries; the 5 pages are the deliverable |
| 2 | **Dutch keyword volume is genuinely small** | 🔴 High | Publish both languages (§9); judge on leads, not sessions |
| 3 | **Schema implemented but not validated** — silent failure | 🟡 Med | Validation is a step in the publish checklist (§10.1) |
| 4 | **`sameAs` filled with invented URLs** | 🔴 High | Only real, owned profiles; create the LinkedIn page if absent (§6.1) |
| 5 | **Cannibalisation** between P1 and P2 | 🟡 Med | Strict one-keyword-one-page mapping (§2); P1 is the guide, P2 is the checklist |
| 6 | **City-page spam temptation** for local reach | 🟡 Med | §7.3: never duplicate money pages per city |
| 7 | **Publishing stays bursty** then stops | 🟡 Med | Fixed cadence 2–3/week (§5.2); the audit flagged bursts specifically |
| 8 | **AI crawlers blocked in `robots.txt`** | 🔴 High | Verify `GPTBot`, `ClaudeBot`, `PerplexityBot` are allowed (§8.4) |
| 9 | **Prices in schema drift from the calculator** | 🟡 Med | Single source of truth: `launchstudio_info.md` §3 |
| 10 | **Results judged at week 4** | 🟡 Med | §13.2 agreed in advance: review at day 90 |

---

<a id="15"></a>
## 15. 🖊️ Decisions Required / Beslissingen Die Genomen Moeten Worden

| # | Decision / Beslissing | Recommendation / Advies | Status |
|---|---|---|---|
| 1 | Build 5 indexable money pages, moving off the one-page site structure | ✅ Yes — these keywords cannot rank without them | ☐ |
| 2 | Prioritise entity/schema work above new content | ✅ Yes — 1–2 dev days, site-wide permanent gain | ☐ |
| 3 | Exclude keyword #08 `AI development` from SEO as well as Ads | ✅ Yes — consistent with §2.1 | ☐ |
| 4 | Publish both Dutch and English versions of all 5 pages | ✅ Yes — Dutch canonical, English for the English-typing Dutch searcher | ☐ |
| 5 | Create a LinkedIn company page + Google Business Profile | ✅ Yes — required for real `sameAs` and Dutch entity signal | ☐ |
| 6 | Add reciprocal links between `manifera.com` and `launchstudio.eu` | ✅ Yes — cheapest authority gain available (§7.2) | ☐ |
| 7 | Adopt a fixed publishing cadence of 2–3 articles/week | ✅ Yes — 800 written, 71 live is the real bottleneck | ☐ |
| 8 | Review at day 90 on leads and AI citations, not week 4 on rankings | ✅ Agreed in advance | ☐ |

### Open items needing input / Openstaande punten die input vragen

| # | Item | Needed from / Nodig van |
|---|---|---|
| A | Real `sameAs` profile URLs (LinkedIn, X, etc.) — **do not invent** | LaunchStudio |
| B | A Dutch phone number (+31) for NAP consistency (§7.1) | LaunchStudio |
| C | Confirmed logo URL and dimensions for `Organization` schema | LaunchStudio |
| D | Sign-off on the 10 final URLs (§3.1) before anything is published | LaunchStudio |
| E | Whether real, verifiable reviews exist (for `AggregateRating`) | LaunchStudio |

---

> **Sources / Bronnen:** [`extra-keywords.md`](extra-keywords.md) · [`launchstudio_info.md`](launchstudio_info.md) (brand entity, pricing, personas, linking map) · [`seo_geo_audit_2026-07-31.md`](seo_geo_audit_2026-07-31.md) (technical baseline, schema gaps, GEO findings) · [`google_ads_production_keywords_plan_nl.md`](google_ads_production_keywords_plan_nl.md) (paid counterpart, shared keyword analysis) · `2026-extra/` article library (supporting content mapping).
>
> **Note / Let op:** Search volumes, ranking timelines and traffic targets are **planning estimates** for the Dutch B2B software-services market. Ranking outcomes depend on competition, domain authority and execution consistency, none of which can be guaranteed. Verify keyword data in Search Console and Keyword Planner before committing resources.
> Zoekvolumes, rankingdoorlooptijden en verkeersdoelen zijn **planningsschattingen** voor de Nederlandse B2B-softwaredienstenmarkt. Rankingresultaten hangen af van concurrentie, domeinautoriteit en consistente uitvoering, die geen van alle te garanderen zijn. Verifieer zoekwoorddata in Search Console en Keyword Planner voordat je middelen vastlegt.
