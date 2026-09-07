# 🎯 Google Search Ads Plan — Production-Readiness Keywords (NL Market)
## LaunchStudio.eu · 🇬🇧 English ⟷ 🇳🇱 Nederlands

> **EN —** A complete, import-ready Google Search Ads plan built on the 14 new keywords in [`extra-keywords.md`](extra-keywords.md). Primary market: **the Netherlands**. Primary ad language: **Dutch**. English keyword coverage is retained inside the Dutch market for reasons explained in §2.
>
> **NL —** Een compleet, importklaar Google Search Ads-plan gebouwd op de 14 nieuwe zoekwoorden uit [`extra-keywords.md`](extra-keywords.md). Primaire markt: **Nederland**. Primaire advertentietaal: **Nederlands**. Engelse zoekwoorden blijven binnen de Nederlandse markt actief, om de redenen die in §2 worden uitgelegd.

| | |
|---|---|
| **Advertiser / Adverteerder** | LaunchStudio (Launch Studio door Manifera) |
| **Landing pages** | 🇳🇱 `https://launchstudio.eu/` · 🇬🇧 `https://launchstudio.eu/en/` |
| **Offer / Aanbod** | Prototype → productie: security, payments, auth, database, hosting |
| **Price / Prijs** | Fixed €800–€7,500 · Vaste prijs €800–€7.500 (+ €49/mnd hosting) |
| **USP** | 11+ yrs engineering (Manifera) · 100% code ownership · live in 1–3 weeks |
| **Status** | Draft v1.0 — verify all volumes/CPCs in Keyword Planner before import |

---

## 📑 Table of Contents / Inhoudsopgave

1. [Source keyword audit / Audit van bronzoekwoorden](#1)
2. [⚠️ Strategic finding: Dutch vs English search behaviour](#2)
3. [Dutch translation table / Nederlandse vertaaltabel](#3)
4. [Campaign architecture / Campagnestructuur](#4)
5. [Ad groups & keywords / Advertentiegroepen & zoekwoorden](#5)
6. [Negative keywords / Uitsluitingszoekwoorden](#6)
7. [Ad copy (RSA) / Advertentieteksten](#7)
8. [Extensions / Advertentie-extensies](#8)
9. [Landing pages & conversion tracking](#9)
10. [Budget & bidding / Budget & biedstrategie](#10)
11. [90-day roadmap / 90-dagen routekaart](#11)
12. [KPIs & optimisation rules / KPI's & optimalisatieregels](#12)
13. [Import notes / Importinstructies (Google Ads Editor)](#13)
14. [Risks / Risico's](#14)
15. [🖊️ Decisions required / Beslissingen die genomen moeten worden](#15)

---

<a id="1"></a>
## 1. 🔍 Source Keyword Audit / Audit van Bronzoekwoorden

**EN —** The source file contains 22 lines but only **14 unique keywords**. Duplicates ("AI prototype to production" ×3, "AI generated code production" ×2) were removed. Each keyword is scored on commercial intent, i.e. how likely the searcher is to buy a service rather than to read, learn, or build it themselves.

**NL —** Het bronbestand bevat 22 regels maar slechts **14 unieke zoekwoorden**. Duplicaten ("AI prototype to production" ×3, "AI generated code production" ×2) zijn verwijderd. Elk zoekwoord is beoordeeld op commerciële intentie: hoe waarschijnlijk het is dat de zoeker een dienst koopt in plaats van leest, leert of het zelf bouwt.

| # | Source keyword (EN) | Intent / Intentie | Verdict / Oordeel | Ad group |
|---|---|---|---|---|
| 01 | AI prototype to production | 🟢 Commercial-investigative | **Core keyword.** Exactly describes the service. | AG1 |
| 02 | AI app to production | 🟢 Commercial-investigative | Core variant. Same intent, different noun. | AG1 |
| 03 | AI code to production | 🟡 Mixed | Some developer/DIY intent. Phrase match only. | AG1 |
| 04 | AI generated code production | 🟡 Mixed | Ambiguous ("production" as noun/adjective). Phrase + negatives. | AG2 |
| 05 | productionize AI application | 🟢 Commercial | High intent, near-zero volume. Keep as Exact. | AG2 |
| 06 | productionize AI app | 🟢 Commercial | Same. Very low volume, very high relevance. | AG2 |
| 07 | make AI generated app production ready | 🟢 Commercial | Long-tail, best converter of the set. | AG2 |
| 08 | AI development | 🔴 **Too broad** | ⚠️ **Do not run as-is.** See warning below. | AG6 (paused) |
| 09 | AI app production problems | 🟢 Problem-aware | Excellent. Pain-first searcher = ready to hire. | AG1 |
| 10 | AI application production ready | 🟢 Commercial | Core. Mirrors the LaunchStudio "Launch Ready" package. | AG2 |
| 11 | AI generated app security | 🟢 Commercial | Maps directly to the +€500 security add-on. | AG3 |
| 12 | AI generated code security | 🟡 Mixed | Attracts researchers/students. Needs negatives. | AG3 |
| 13 | AI application security audit | 🟢 **Highest value** | Explicit service purchase. Highest CPC, highest CVR. | AG4 |
| 14 | AI application scalability | 🟡 Consideration | Earlier-stage. Support/nurture, not direct sale. | AG5 |

> ### ⚠️ Warning on keyword #08 "AI development"
> **EN —** This is a **head term with a completely different intent** from everything LaunchStudio sells. People searching "AI development" want someone to *build AI models, chatbots or ML pipelines* — not to harden an existing prototype. In the Netherlands this term is bid on by large AI consultancies at €8–€15 CPC. Running it will consume the entire budget in days and convert at near zero.
> **Recommendation:** create it as a **paused** ad group (AG6). Only activate it later as `[AI development agency Nederland]` Exact, with the full negative list applied, once you have conversion data from AG1–AG4.
>
> **NL —** Dit is een **hoofdterm met een totaal andere intentie** dan wat LaunchStudio verkoopt. Wie op "AI development" zoekt, wil dat iemand *AI-modellen, chatbots of ML-pipelines bouwt* — niet dat een bestaand prototype productieklaar wordt gemaakt. In Nederland bieden grote AI-consultancybureaus €8–€15 CPC op deze term. Live zetten betekent: budget in dagen op, conversie vrijwel nul.
> **Advies:** maak hem aan als **gepauzeerde** advertentiegroep (AG6). Activeer pas later als `[AI development agency Nederland]` Exact, mét de volledige uitsluitingslijst, zodra AG1–AG4 conversiedata opleveren.

---

<a id="2"></a>
## 2. ⚠️ Strategic Finding — Dutch vs English Search Behaviour
## ⚠️ Strategische Bevinding — Nederlands vs Engels Zoekgedrag

> **This is the single most important section of this document. Read it before setting up anything.**
> **Dit is verreweg de belangrijkste sectie van dit document. Lees het vóór je iets instelt.**

### 2.1 The problem / Het probleem

**EN —** All 14 source keywords are English technical terms. If they are translated literally into Dutch and run as Dutch-only keywords, the campaign will have almost no traffic. There are three compounding reasons:

1. **Dutch tech professionals search in English for technical concepts.** A Dutch founder who built an app in Lovable does not type *"AI-prototype naar productie brengen"*. They type *"AI prototype to production"* or *"Lovable app deploy"*. The Dutch technical vocabulary for this is borrowed English anyway.
2. **"Productionize" has no Dutch equivalent.** The closest phrases — *productieklaar maken*, *live zetten*, *in productie nemen* — are three different phrasings with split, tiny volume.
3. **The Dutch market is small.** 17.9M people. A niche B2B term with 40 monthly searches in English worldwide may have **0–10** in Dutch.

**NL —** Alle 14 bronzoekwoorden zijn Engelse technische termen. Als je ze letterlijk naar het Nederlands vertaalt en alleen Nederlandse zoekwoorden inzet, krijgt de campagne bijna geen verkeer. Er zijn drie oorzaken die elkaar versterken:

1. **Nederlandse tech-professionals zoeken technische begrippen in het Engels.** Een Nederlandse oprichter die een app in Lovable bouwde, typt niet *"AI-prototype naar productie brengen"*. Die typt *"AI prototype to production"* of *"Lovable app deploy"*. Het Nederlandse vakjargon hiervoor is toch al leenengels.
2. **"Productionize" heeft geen Nederlands equivalent.** De dichtstbijzijnde varianten — *productieklaar maken*, *live zetten*, *in productie nemen* — zijn drie verschillende formuleringen met versnipperd, minimaal volume.
3. **De Nederlandse markt is klein.** 17,9 miljoen mensen. Een niche-B2B-term met 40 maandelijkse zoekopdrachten wereldwijd in het Engels heeft er in het Nederlands **0–10**.

### 2.2 The solution / De oplossing

**EN —** Keep the Netherlands as the *market* and Dutch as the *ad language*, but run **both Dutch and English keywords inside the Dutch market**, in two separate campaigns. This is not a contradiction of the brief — it is how you actually reach Dutch buyers who search in English.

**NL —** Houd Nederland als *markt* en Nederlands als *advertentietaal*, maar zet **zowel Nederlandse als Engelse zoekwoorden in binnen de Nederlandse markt**, in twee gescheiden campagnes. Dit is geen afwijking van de opdracht — zo bereik je juist Nederlandse kopers die in het Engels zoeken.

| | Campaign A — NL 🇳🇱 | Campaign B — NL-EN 🇬🇧 |
|---|---|---|
| **Geo / Locatie** | Netherlands only / Alleen Nederland | Netherlands only / Alleen Nederland |
| **Keywords** | Dutch translations (§3) | Original English keywords (§1) |
| **Ad language / Advertentietaal** | Dutch / Nederlands | English / Engels |
| **Landing page** | `launchstudio.eu/` | `launchstudio.eu/en/` |
| **Budget share** | **70%** | **30%** |
| **Role / Rol** | Primary — brand voice, local trust | Volume — captures the real search demand |

### 2.3 The language-targeting trap / De taalinstellingsval

**EN —** In Google Ads, the *Languages* setting does **not** filter by the language of the search query. It filters by the user's Google interface language and the language of the content they typically consume. A very large share of Dutch developers and founders run their Google account in **English**. If you set Campaign A to "Dutch only", you will exclude a meaningful part of your own Dutch audience.

**Setting for BOTH campaigns:** Languages = **Dutch + English**. Location = **Netherlands**, with *Presence: People in or regularly in your targeted locations* (never "interest", which pulls in people abroad merely researching the Netherlands).

**NL —** In Google Ads filtert de instelling *Talen* **niet** op de taal van de zoekopdracht. Het filtert op de interfacetaal van de gebruiker en de taal van de content die diegene doorgaans bekijkt. Een groot deel van de Nederlandse developers en oprichters gebruikt Google in het **Engels**. Zet je campagne A op "alleen Nederlands", dan sluit je een aanzienlijk deel van je eigen Nederlandse doelgroep uit.

**Instelling voor BEIDE campagnes:** Talen = **Nederlands + Engels**. Locatie = **Nederland**, met *Aanwezigheid: mensen die zich in uw doellocaties bevinden of daar regelmatig zijn* (nooit "interesse", dat trekt mensen uit het buitenland aan die Nederland alleen onderzoeken).

### 2.4 Expected volume — be realistic / Verwacht volume — wees realistisch

**EN —** These are niche B2B terms. Estimated combined monthly search volume in the Netherlands across all 14 keywords + variants: **200–600 searches/month**. At a 6–9% CTR that is roughly **15–50 clicks/month** from exact/phrase alone. This is a *low-volume, high-intent* account. Judge it on cost per qualified lead, never on impression counts.

**NL —** Dit zijn niche-B2B-termen. Geschat gecombineerd maandelijks zoekvolume in Nederland over alle 14 zoekwoorden + varianten: **200–600 zoekopdrachten/maand**. Bij een CTR van 6–9% zijn dat ruwweg **15–50 klikken/maand** uit alleen exact/phrase. Dit is een account met *laag volume en hoge intentie*. Beoordeel het op kosten per gekwalificeerde lead, nooit op vertoningen.

---

<a id="3"></a>
## 3. 🌐 Dutch Translation Table / Nederlandse Vertaaltabel

**EN —** Two Dutch columns are given deliberately. The **literal translation** shows what the phrase means; the **natural search variant** is what a Dutch person actually types into Google. **Always bid on the natural variant.** Literal calques of English technical phrases get zero impressions.

**NL —** Er staan bewust twee Nederlandse kolommen. De **letterlijke vertaling** toont de betekenis; de **natuurlijke zoekvariant** is wat een Nederlander daadwerkelijk in Google typt. **Bied altijd op de natuurlijke variant.** Letterlijke vertalingen van Engelse vakjargon krijgen nul vertoningen.

| # | 🇬🇧 English keyword | 🇳🇱 Literal translation (do **not** bid) | 🇳🇱 Natural search variant (**bid on this**) | Est. NL vol. | Note |
|---|---|---|---|---|---|
| 01 | AI prototype to production | AI-prototype naar productie | `ai prototype naar productie`<br>`prototype productieklaar maken` | 10–30 | Best Dutch-language term of the set |
| 02 | AI app to production | AI-app naar productie | `ai app live zetten`<br>`app van prototype naar live` | 10–30 | "live zetten" is the everyday Dutch phrasing |
| 03 | AI code to production | AI-code naar productie | `ai code productieklaar`<br>`ai gegenereerde code live zetten` | <10 | Very low; keep phrase match |
| 04 | AI generated code production | AI-gegenereerde code productie | `ai gegenereerde code productie`<br>`code van ai in productie nemen` | <10 | "in productie nemen" = enterprise phrasing |
| 05 | productionize AI application | AI-applicatie productionaliseren ❌ | `ai applicatie productieklaar maken` | <10 | ⚠️ "productionaliseren" is **not** a Dutch word |
| 06 | productionize AI app | AI-app productionaliseren ❌ | `ai app productieklaar maken` | <10 | Same — never use the calque |
| 07 | make AI generated app production ready | AI-app productieklaar maken | `ai app productieklaar maken`<br>`ai app klaar voor lancering` | 10–20 | Matches package name "Klaar voor lancering" |
| 08 | AI development | AI-ontwikkeling | `ai ontwikkeling` ⚠️ | 500+ | ⚠️ Too broad — keep paused (§1) |
| 09 | AI app production problems | AI-app productieproblemen | `ai app werkt niet live`<br>`prototype werkt niet in productie` | 10–30 | Pain-first; strongest lead quality |
| 10 | AI application production ready | AI-applicatie productieklaar | `applicatie productieklaar maken`<br>`software productieklaar` | 20–50 | Broadest useful Dutch term |
| 11 | AI generated app security | Beveiliging AI-gegenereerde app | `ai app beveiligen`<br>`beveiliging ai applicatie` | 10–30 | Ties to +€500 security add-on |
| 12 | AI generated code security | Beveiliging AI-gegenereerde code | `ai gegenereerde code beveiliging`<br>`is ai code veilig` | 10–30 | Second phrase is research intent — negative-guard it |
| 13 | AI application security audit | Beveiligingsaudit AI-applicatie | `security audit applicatie`<br>`beveiligingsaudit software`<br>`pentest webapplicatie` | 50–150 | 💰 Highest commercial value in Dutch |
| 14 | AI application scalability | Schaalbaarheid AI-applicatie | `applicatie schaalbaar maken`<br>`webapp schaalbaarheid` | 10–30 | Consideration stage |

### 3.1 Dutch terminology reference / Nederlandse terminologiereferentie

| English term | ✅ Use in Dutch ads | ❌ Avoid |
|---|---|---|
| production-ready | **productieklaar** / *klaar voor lancering* | *productie-gereed* (stiff) |
| to go live / launch | **live zetten** / *lanceren* | *uitrollen* (means rollout, different) |
| security | **beveiliging** | *veiligheid* (means physical safety) |
| GDPR | **AVG** | *GDPR* (correct but AVG builds local trust) |
| hosting | **hosting** | *webhosting* (consumer-sounding) |
| fixed price | **vaste prijs** | *vastgesteld tarief* (bureaucratic) |
| quote | **offerte** | *citaat* (a literary quotation!) |
| scalable | **schaalbaar** | *opschaalbaar* (uncommon) |
| deployment | **deployment** / *uitrol naar productie* | *inzet* (ambiguous) |
| audit | **audit** | *controle* (too generic) |

> **EN —** Note on "u" vs "je": LaunchStudio's site voice is startup-friendly, so **"je"** is the correct register for ad copy — except in the security/audit ad groups (AG3, AG4), where buyers are more formal and **"u"** performs better. This split is reflected in §7.
> **NL —** Let op "u" versus "je": de sitestem van LaunchStudio is startup-vriendelijk, dus **"je"** is het juiste register voor advertentieteksten — behalve in de beveiligings-/auditgroepen (AG3, AG4), waar kopers formeler zijn en **"u"** beter presteert. Deze splitsing is verwerkt in §7.

---

<a id="4"></a>
## 4. 🏗️ Campaign Architecture / Campagnestructuur

| Setting / Instelling | Campaign A — `LS_NL_Production_NL` | Campaign B — `LS_NL_Production_EN` |
|---|---|---|
| **Type** | Search only (no Display partners) | Search only (no Display partners) |
| **Search partners** | ❌ Off / Uit | ❌ Off / Uit |
| **Display expansion** | ❌ Off / Uit | ❌ Off / Uit |
| **Locations / Locaties** | Netherlands | Netherlands |
| **Location option** | Presence only / Alleen aanwezigheid | Presence only / Alleen aanwezigheid |
| **Languages / Talen** | Dutch + English | Dutch + English |
| **Ad language / Advertentietaal** | 🇳🇱 Dutch | 🇬🇧 English |
| **Landing page** | `launchstudio.eu/` | `launchstudio.eu/en/` |
| **Budget (month 1)** | €700 (~€23/day) | €300 (~€10/day) |
| **Bidding (month 1)** | Manual CPC or Maximise Clicks, CPC cap €6 | Maximise Clicks, CPC cap €7 |
| **Bidding (from month 3)** | Maximise Conversions → tCPA €120 | Maximise Conversions → tCPA €140 |
| **Ad rotation** | Optimise for best performing | Optimise for best performing |
| **Ad schedule** | Mon–Fri 07:00–20:00, Sat–Sun −40% bid | Mon–Fri 07:00–20:00, Sat–Sun −40% bid |
| **Devices** | Desktop +15%, Mobile −20% | Desktop +15%, Mobile −20% |
| **Ad groups** | AG1–AG5 (AG6 paused) | AG1–AG5 (AG6 paused) |

> **EN — Why desktop bid adjustment?** B2B service research and quote requests happen on desktop during working hours. Mobile traffic on these terms is disproportionately students and casual readers.
> **NL — Waarom bodaanpassing op desktop?** B2B-dienstverleningsonderzoek en offerteaanvragen gebeuren op desktop tijdens werktijd. Mobiel verkeer op deze termen bestaat onevenredig vaak uit studenten en toevallige lezers.

> **EN — Optional Campaign C (month 4+):** `LS_BE_Production_NL` — same Dutch ad groups targeted at **Flanders (Belgium)**. Dutch-language, separate budget, so NL performance stays clean. Do not merge Belgium into Campaign A: CPCs and conversion rates differ materially.
> **NL — Optionele campagne C (vanaf maand 4):** `LS_BE_Production_NL` — dezelfde Nederlandstalige advertentiegroepen gericht op **Vlaanderen (België)**. Nederlandstalig, apart budget, zodat de Nederlandse prestaties zuiver blijven. Voeg België niet samen met campagne A: CPC's en conversieratio's verschillen wezenlijk.

---

<a id="5"></a>
## 5. 🎯 Ad Groups & Keywords / Advertentiegroepen & Zoekwoorden

**EN —** Six ad groups, each built around one intent — never one topic. Google's Quality Score rewards tight keyword→ad→landing-page alignment, and at this low volume a tight structure is what keeps CPC affordable. Match-type strategy for month 1–2: **Phrase + Exact only**. Broad match is added only in month 3, once conversion data exists to steer Smart Bidding; broad match without conversion data on a €700 budget is how niche accounts lose their budget to irrelevant traffic.

**NL —** Zes advertentiegroepen, elk gebouwd rond één intentie — nooit rond één onderwerp. De kwaliteitsscore van Google beloont strakke afstemming tussen zoekwoord, advertentie en landingspagina, en juist bij dit lage volume houdt een strakke structuur de CPC betaalbaar. Zoektypestrategie voor maand 1–2: **alleen Phrase + Exact**. Breed zoeken voegen we pas in maand 3 toe, zodra er conversiedata is om Smart Bidding te sturen; breed zoeken zónder conversiedata op een budget van €700 is precies hoe nichecampagnes hun budget aan irrelevant verkeer verliezen.

**Match type legend:** `[exact]` = Exact · `"phrase"` = Phrase · `+broad +match` = Broad (month 3+)

---

### 🎯 AG1 — Prototype → Production (Core) / Prototype → Productie (Kern)

> **EN —** The searcher has a working prototype that will not go live. Highest intent in the account after AG4. Ad promise: *"we take it live, fixed price, 1–3 weeks."*
> **NL —** De zoeker heeft een werkend prototype dat niet live komt. Op AG4 na de hoogste intentie in het account. Advertentiebelofte: *"wij zetten het live, vaste prijs, 1–3 weken."*

#### 🇳🇱 Campaign A — Dutch keywords

| # | Keyword | Match | Priority | Est. CPC | Search intent (NL) |
|---|---|---|---|---|---|
| A1.1 | `[ai prototype naar productie]` | Exact | 🔴 High | €4–6 | Prototype productieklaar laten maken |
| A1.2 | `"prototype naar productie"` | Phrase | 🔴 High | €4–6 | Algemene productie-overgang |
| A1.3 | `"prototype productieklaar maken"` | Phrase | 🔴 High | €4–7 | Directe dienstvraag |
| A1.4 | `"ai app live zetten"` | Phrase | 🔴 High | €3–6 | App live krijgen |
| A1.5 | `"app van prototype naar live"` | Phrase | 🟡 Med | €3–5 | Beschrijvende variant |
| A1.6 | `"prototype werkt niet in productie"` | Phrase | 🔴 High | €4–7 | 🔥 Pijngedreven — beste leadkwaliteit |
| A1.7 | `"ai app werkt niet live"` | Phrase | 🔴 High | €4–7 | 🔥 Pijngedreven |
| A1.8 | `"lovable app live zetten"` | Phrase | 🔴 High | €3–6 | Toolspecifiek — zeer relevant |
| A1.9 | `"bolt app naar productie"` | Phrase | 🟡 Med | €3–5 | Toolspecifiek |
| A1.10 | `"cursor project live zetten"` | Phrase | 🟡 Med | €3–5 | Toolspecifiek |

#### 🇬🇧 Campaign B — English keywords

| # | Keyword | Match | Priority | Est. CPC | Search intent |
|---|---|---|---|---|---|
| B1.1 | `[ai prototype to production]` | Exact | 🔴 High | €5–8 | Source keyword #01 |
| B1.2 | `"ai prototype to production"` | Phrase | 🔴 High | €5–8 | Variants incl. "service", "cost" |
| B1.3 | `[ai app to production]` | Exact | 🔴 High | €5–8 | Source keyword #02 |
| B1.4 | `"ai app to production"` | Phrase | 🔴 High | €5–8 | — |
| B1.5 | `"ai code to production"` | Phrase | 🟡 Med | €4–7 | Source #03 — some DIY intent |
| B1.6 | `"ai app production problems"` | Phrase | 🔴 High | €4–7 | 🔥 Source #09 — pain-first |
| B1.7 | `"prototype to production service"` | Phrase | 🔴 High | €5–9 | Explicit service search |
| B1.8 | `"lovable app to production"` | Phrase | 🔴 High | €4–7 | Tool-specific |
| B1.9 | `"bolt new deploy production"` | Phrase | 🟡 Med | €4–6 | Tool-specific |
| B1.10 | `"take prototype live"` | Phrase | 🟡 Med | €4–6 | Natural phrasing |

**Landing page:** 🇳🇱 `launchstudio.eu/` · 🇬🇧 `launchstudio.eu/en/`

---

### 🎯 AG2 — Production-Ready / Productionize · Productieklaar Maken

> **EN —** Searcher already knows the term "production-ready". More technical, often a technical co-founder or the developer being asked by the founder. Ad promise: *"security, database, payments, hosting — done properly, fixed scope."*
> **NL —** De zoeker kent de term "productieklaar" al. Technischer, vaak een technische medeoprichter of de developer die door de oprichter wordt gevraagd. Advertentiebelofte: *"beveiliging, database, betalingen, hosting — goed geregeld, vaste scope."*

#### 🇳🇱 Campaign A — Dutch keywords

| # | Keyword | Match | Priority | Est. CPC | Search intent (NL) |
|---|---|---|---|---|---|
| A2.1 | `[ai app productieklaar maken]` | Exact | 🔴 High | €4–7 | Bron #06/#07 — natuurlijke variant |
| A2.2 | `"applicatie productieklaar maken"` | Phrase | 🔴 High | €4–7 | Breedste bruikbare NL-term |
| A2.3 | `"software productieklaar"` | Phrase | 🟡 Med | €4–6 | Generieker |
| A2.4 | `"ai applicatie productieklaar"` | Phrase | 🔴 High | €4–7 | Bron #05/#10 |
| A2.5 | `"in productie nemen applicatie"` | Phrase | 🟡 Med | €4–6 | Enterprise-formulering |
| A2.6 | `"ai gegenereerde code productie"` | Phrase | 🟡 Med | €3–6 | Bron #04 |
| A2.7 | `"klaar voor lancering software"` | Phrase | 🟡 Med | €3–5 | Matcht pakketnaam |
| A2.8 | `"webapp productieklaar maken"` | Phrase | 🟡 Med | €4–6 | Producttype-variant |

#### 🇬🇧 Campaign B — English keywords

| # | Keyword | Match | Priority | Est. CPC | Search intent |
|---|---|---|---|---|---|
| B2.1 | `[productionize ai application]` | Exact | 🔴 High | €5–9 | Source #05 — very low vol, very high intent |
| B2.2 | `[productionize ai app]` | Exact | 🔴 High | €5–9 | Source #06 |
| B2.3 | `"productionize ai"` | Phrase | 🟡 Med | €5–8 | Catches variants |
| B2.4 | `[make ai generated app production ready]` | Exact | 🔴 High | €5–8 | Source #07 — best converter |
| B2.5 | `"ai application production ready"` | Phrase | 🔴 High | €5–8 | Source #10 |
| B2.6 | `"ai generated code production"` | Phrase | 🟡 Med | €4–7 | Source #04 — needs negatives |
| B2.7 | `"production ready ai app"` | Phrase | 🔴 High | €5–8 | Word-order variant |
| B2.8 | `"make prototype production ready"` | Phrase | 🔴 High | €5–8 | Non-AI variant, same buyer |

**Landing page:** 🇳🇱 `launchstudio.eu/#packages` · 🇬🇧 `launchstudio.eu/en/#packages`

---

### 🎯 AG3 — AI Code Security / Beveiliging van AI-code

> **EN —** Fear-driven. The founder has read that AI-generated code leaks data and now cannot sleep. Maps to the **+€500 security hardening** add-on. Register: **"u"** — this buyer wants a serious counterpart, not a startup buddy.
> **NL —** Angstgedreven. De oprichter heeft gelezen dat AI-gegenereerde code data lekt en ligt er wakker van. Sluit aan op de add-on **beveiliging (+€500)**. Register: **"u"** — deze koper wil een serieuze gesprekspartner, geen startup-maatje.

#### 🇳🇱 Campaign A — Dutch keywords

| # | Keyword | Match | Priority | Est. CPC | Search intent (NL) |
|---|---|---|---|---|---|
| A3.1 | `[ai app beveiligen]` | Exact | 🔴 High | €5–8 | Bron #11 |
| A3.2 | `"beveiliging ai applicatie"` | Phrase | 🔴 High | €5–8 | Bron #11 variant |
| A3.3 | `"ai gegenereerde code beveiliging"` | Phrase | 🔴 High | €5–8 | Bron #12 |
| A3.4 | `"is ai code veilig"` | Phrase | 🟢 Low | €2–4 | ⚠️ Onderzoeksintentie — blog-LP, geen offerte |
| A3.5 | `"webapplicatie beveiligen"` | Phrase | 🟡 Med | €5–9 | Breder, hoger volume |
| A3.6 | `"applicatie avg proof maken"` | Phrase | 🔴 High | €5–9 | 💰 AVG = sterk NL-koopsignaal |
| A3.7 | `"datalek voorkomen applicatie"` | Phrase | 🟡 Med | €4–8 | Angstgedreven |
| A3.8 | `"beveiliging saas applicatie"` | Phrase | 🟡 Med | €5–8 | Producttype |

#### 🇬🇧 Campaign B — English keywords

| # | Keyword | Match | Priority | Est. CPC | Search intent |
|---|---|---|---|---|---|
| B3.1 | `[ai generated app security]` | Exact | 🔴 High | €6–10 | Source #11 |
| B3.2 | `"ai generated code security"` | Phrase | 🔴 High | €6–10 | Source #12 |
| B3.3 | `"secure ai generated code"` | Phrase | 🔴 High | €6–9 | Action-phrasing variant |
| B3.4 | `"ai code security review"` | Phrase | 🔴 High | €6–10 | Explicit service |
| B3.5 | `"lovable app security"` | Phrase | 🔴 High | €5–8 | Tool-specific |
| B3.6 | `"supabase rls security"` | Phrase | 🟡 Med | €4–8 | Technical — the #1 real defect |
| B3.7 | `"ai app gdpr compliance"` | Phrase | 🔴 High | €6–10 | EU buyer signal |

**Landing page:** 🇳🇱 `launchstudio.eu/#contact` · 🇬🇧 `launchstudio.eu/en/#contact`

---

### 🎯 AG4 — Security Audit / Beveiligingsaudit 💰

> **EN —** **The most valuable ad group in the account.** "Audit" is an explicit purchase word — nobody searches it for curiosity. Highest CPC, highest conversion rate, largest deal size. Give it its own bid priority even if impressions are few. Register: **"u"**.
> **NL —** **De waardevolste advertentiegroep van het account.** "Audit" is een expliciet koopwoord — niemand zoekt daarop uit nieuwsgierigheid. Hoogste CPC, hoogste conversieratio, grootste dealwaarde. Geef deze groep eigen biedprioriteit, ook als er weinig vertoningen zijn. Register: **"u"**.

#### 🇳🇱 Campaign A — Dutch keywords

| # | Keyword | Match | Priority | Est. CPC | Search intent (NL) |
|---|---|---|---|---|---|
| A4.1 | `[beveiligingsaudit applicatie]` | Exact | 🔴 High | €8–14 | Bron #13 |
| A4.2 | `"security audit applicatie"` | Phrase | 🔴 High | €8–14 | Engels leenwoord — meeste volume |
| A4.3 | `"beveiligingsaudit software"` | Phrase | 🔴 High | €8–14 | Variant |
| A4.4 | `"pentest webapplicatie"` | Phrase | 🔴 High | €9–15 | 💰 Hoogste koopintentie |
| A4.5 | `"security audit saas"` | Phrase | 🔴 High | €8–13 | Producttype |
| A4.6 | `"code review beveiliging"` | Phrase | 🟡 Med | €6–10 | Zachtere variant |
| A4.7 | `"security audit kosten"` | Phrase | 🟡 Med | €6–11 | Prijsvergelijker — toon vaste prijs |
| A4.8 | `"beveiligingsonderzoek applicatie"` | Phrase | 🟢 Low | €6–10 | Formeel, laag volume |

#### 🇬🇧 Campaign B — English keywords

| # | Keyword | Match | Priority | Est. CPC | Search intent |
|---|---|---|---|---|---|
| B4.1 | `[ai application security audit]` | Exact | 🔴 High | €9–15 | Source #13 |
| B4.2 | `"ai application security audit"` | Phrase | 🔴 High | €9–15 | — |
| B4.3 | `"ai app security audit"` | Phrase | 🔴 High | €9–15 | Short variant |
| B4.4 | `"security audit web application"` | Phrase | 🔴 High | €9–15 | Broader, real volume |
| B4.5 | `"saas security audit"` | Phrase | 🔴 High | €8–14 | Product type |
| B4.6 | `"penetration test web app"` | Phrase | 🔴 High | €10–16 | 💰 Highest intent, highest CPC |
| B4.7 | `"security audit cost"` | Phrase | 🟡 Med | €7–12 | Price shopper — show fixed price |

**Landing page:** 🇳🇱 `launchstudio.eu/#contact` · 🇬🇧 `launchstudio.eu/en/#contact`

---

### 🎯 AG5 — Scalability / Schaalbaarheid

> **EN —** Consideration-stage. The product works but the founder fears it will break at 1,000 users. Lower urgency, so treat this as **lead nurture**: send it to the calculator/packages page rather than straight to the contact form.
> **NL —** Overwegingsfase. Het product werkt, maar de oprichter vreest dat het breekt bij 1.000 gebruikers. Minder urgentie, dus behandel dit als **leadnurturing**: stuur naar de calculator-/pakketpagina in plaats van direct naar het contactformulier.

#### 🇳🇱 Campaign A — Dutch keywords

| # | Keyword | Match | Priority | Est. CPC | Search intent (NL) |
|---|---|---|---|---|---|
| A5.1 | `[applicatie schaalbaar maken]` | Exact | 🟡 Med | €4–7 | Bron #14 |
| A5.2 | `"schaalbaarheid applicatie"` | Phrase | 🟡 Med | €4–7 | Bron #14 variant |
| A5.3 | `"webapp schaalbaarheid"` | Phrase | 🟡 Med | €4–7 | Producttype |
| A5.4 | `"applicatie traag bij veel gebruikers"` | Phrase | 🔴 High | €4–8 | 🔥 Pijngedreven — hoogste waarde in AG5 |
| A5.5 | `"database performance verbeteren"` | Phrase | 🟡 Med | €5–9 | Technisch, vaak de echte oorzaak |
| A5.6 | `"saas klaar voor groei"` | Phrase | 🟢 Low | €3–6 | Zacht |

#### 🇬🇧 Campaign B — English keywords

| # | Keyword | Match | Priority | Est. CPC | Search intent |
|---|---|---|---|---|---|
| B5.1 | `[ai application scalability]` | Exact | 🟡 Med | €5–8 | Source #14 |
| B5.2 | `"ai app scalability"` | Phrase | 🟡 Med | €5–8 | Variant |
| B5.3 | `"make app scalable"` | Phrase | 🟡 Med | €4–8 | Action phrasing |
| B5.4 | `"app slow with many users"` | Phrase | 🔴 High | €4–8 | 🔥 Pain-first |
| B5.5 | `"prototype breaks at scale"` | Phrase | 🔴 High | €5–9 | 🔥 Very high intent, tiny volume |

**Landing page:** 🇳🇱 `launchstudio.eu/#calculator` · 🇬🇧 `launchstudio.eu/en/#calculator`

---

### ⏸️ AG6 — AI Development (PAUSED / GEPAUZEERD)

> **EN —** Built but **not enabled**. See the warning in §1. Activate only after AG1–AG4 have produced at least 10 conversions, and then only in the restricted form below, with the full negative list attached.
> **NL —** Wel aangemaakt, **niet actief**. Zie de waarschuwing in §1. Activeer pas nadat AG1–AG4 minimaal 10 conversies hebben opgeleverd, en dan uitsluitend in de beperkte vorm hieronder, mét de volledige uitsluitingslijst.

| # | Keyword | Match | Est. CPC | Why restricted / Waarom beperkt |
|---|---|---|---|---|
| A6.1 | `[ai development bureau nederland]` | Exact | €8–14 | Alleen met locatie + bureau-intentie |
| A6.2 | `[ai ontwikkeling uitbesteden]` | Exact | €7–12 | "Uitbesteden" = koopsignaal |
| B6.1 | `[ai development agency netherlands]` | Exact | €9–15 | Location qualifier is mandatory |
| B6.2 | `[ai development company netherlands]` | Exact | €9–15 | Same |
| ❌ | ~~`ai development`~~ | — | €8–15 | **Never run.** Head term, wrong intent, budget killer |

---

<a id="6"></a>
## 6. 🚫 Negative Keywords / Uitsluitingszoekwoorden

**EN —** With a €1,000 monthly budget and CPCs of €5–15, a single day of irrelevant traffic costs a week of qualified clicks. These five shared lists must be attached to **both campaigns before the first ad is enabled** — not added later in response to a bad search-terms report. Lists 1–4 are non-negotiable; List 5 is reviewed monthly against the actual search-terms report.

**NL —** Met een maandbudget van €1.000 en CPC's van €5–15 kost één dag irrelevant verkeer een week aan gekwalificeerde klikken. Deze vijf gedeelde lijsten moeten aan **beide campagnes gekoppeld zijn vóórdat de eerste advertentie live gaat** — niet achteraf toegevoegd na een teleurstellend zoektermenrapport. Lijst 1–4 zijn niet onderhandelbaar; lijst 5 wordt maandelijks getoetst aan het werkelijke zoektermenrapport.

### 📋 List 1 — Jobs & Careers / Vacatures & Carrière
> **Why:** "AI developer" searches are dominated by jobseekers. This is the single largest source of wasted spend in dev-services accounts.
> **Waarom:** Zoekopdrachten op "AI developer" worden gedomineerd door werkzoekenden. Dit is de grootste bron van verspild budget in accounts voor ontwikkeldiensten.

| 🇳🇱 Dutch | 🇬🇧 English |
|---|---|
| `vacature`, `vacatures`, `baan`, `banen`, `werken bij`, `solliciteren`, `sollicitatie`, `salaris`, `stage`, `stageplaats`, `traineeship`, `zzp gezocht`, `freelancer gezocht`, `cv`, `loondienst`, `uurtarief developer` | `job`, `jobs`, `career`, `careers`, `hiring`, `vacancy`, `vacancies`, `salary`, `wage`, `intern`, `internship`, `resume`, `recruiter`, `remote job`, `freelance developer wanted` |

### 📋 List 2 — Education, DIY & Research / Onderwijs, Zelf Doen & Onderzoek
> **Why:** "how to", "what is" and "tutorial" searchers will never buy a €3,000 service. Note: `is ai code veilig` (A3.4) is deliberately kept as a *keyword* on a blog landing page — do not let this list block it.
> **Waarom:** Zoekers op "hoe", "wat is" en "tutorial" kopen nooit een dienst van €3.000. Let op: `is ai code veilig` (A3.4) staat bewust als *zoekwoord* op een bloglandingspagina — laat deze lijst dat niet blokkeren.

| 🇳🇱 Dutch | 🇬🇧 English |
|---|---|
| `cursus`, `cursussen`, `opleiding`, `training`, `leren`, `zelf leren`, `zelf maken`, `zelf bouwen`, `handleiding`, `uitleg`, `wat is`, `hoe werkt`, `betekenis`, `voorbeeld`, `voorbeelden`, `template`, `boek`, `scriptie`, `student`, `studenten`, `hbo`, `universiteit`, `wikipedia`, `youtube` | `tutorial`, `course`, `courses`, `learn`, `learning`, `how to`, `what is`, `meaning`, `definition`, `guide`, `example`, `examples`, `template`, `boilerplate`, `book`, `thesis`, `student`, `students`, `bootcamp`, `certification`, `wikipedia`, `youtube`, `reddit` |

### 📋 List 3 — Free, Cheap & Tools / Gratis, Goedkoop & Tools
> **Why:** LaunchStudio's floor price is €800. Anyone with "gratis" or "goedkoop" in the query is outside the market. `open source` and `github` indicate someone looking for code, not for a supplier.
> **Waarom:** De ondergrens van LaunchStudio is €800. Wie "gratis" of "goedkoop" in de zoekopdracht zet, valt buiten de markt. `open source` en `github` duiden op iemand die code zoekt, geen leverancier.

| 🇳🇱 Dutch | 🇬🇧 English |
|---|---|
| `gratis`, `goedkoop`, `goedkoopste`, `budget`, `zelf regelen`, `open source`, `download`, `downloaden`, `plugin`, `wordpress plugin`, `proefversie`, `gratis proberen`, `crack`, `torrent` | `free`, `cheap`, `cheapest`, `low cost`, `open source`, `download`, `plugin`, `trial`, `free trial`, `github`, `npm`, `library`, `crack`, `nulled` |

### 📋 List 4 — Wrong AI Intent / Verkeerde AI-intentie
> **Why:** This is the list that protects you from keyword #08 and from broad match. LaunchStudio does not train models, build chatbots or generate content. Every term here signals a completely different service.
> **Waarom:** Deze lijst beschermt je tegen zoekwoord #08 en tegen breed zoeken. LaunchStudio traint geen modellen, bouwt geen chatbots en genereert geen content. Elke term hier wijst op een totaal andere dienst.

| 🇳🇱 Dutch | 🇬🇧 English |
|---|---|
| `chatgpt`, `prompt`, `prompts`, `tekst schrijven`, `content schrijven`, `afbeelding`, `afbeeldingen`, `video`, `muziek`, `stem`, `vertalen`, `chatbot bouwen`, `model trainen`, `machine learning`, `dataset`, `algoritme`, `ai schilderij`, `ai avatar` | `chatgpt`, `openai`, `claude`, `gemini`, `midjourney`, `prompt`, `prompts`, `image generator`, `text generator`, `content writer`, `video`, `music`, `voice`, `translate`, `chatbot builder`, `train model`, `machine learning`, `ml pipeline`, `dataset`, `algorithm`, `llm fine tuning` |

### 📋 List 5 — Geo, Competitor & Junk / Geo, Concurrentie & Ruis
> **Why:** Location terms outside the target market, plus the offshore-rate searchers who will never pay Dutch prices. Review monthly.
> **Waarom:** Locatietermen buiten de doelmarkt, plus zoekers naar offshore-tarieven die nooit Nederlandse prijzen betalen. Maandelijks herzien.

| 🇳🇱 Dutch | 🇬🇧 English |
|---|---|
| `india`, `pakistan`, `oekraïne`, `polen`, `outsourcing india`, `goedkope developer buitenland`, `usa`, `amerika` | `india`, `pakistan`, `bangladesh`, `philippines`, `ukraine`, `poland`, `offshore rates`, `hourly rate india`, `usa`, `united states`, `australia`, `dubai` |

### 6.1 Negative match-type rules / Regels voor zoektypes van uitsluitingen

| Rule / Regel | EN | NL |
|---|---|---|
| **Default** | Add all list terms as **Phrase** negatives | Voeg alle lijsttermen toe als **Phrase**-uitsluiting |
| **Broad negatives** | Use only for unambiguous words (`vacature`, `gratis`, `chatgpt`) | Alleen voor ondubbelzinnige woorden (`vacature`, `gratis`, `chatgpt`) |
| **Never** | Never negate `ai`, `code`, `app`, `productie` alone | Sluit nooit `ai`, `code`, `app`, `productie` los uit |
| **Cross-campaign** | Attach lists at account level as *shared* lists | Koppel lijsten op accountniveau als *gedeelde* lijsten |
| **Cadence** | Review search terms 2×/week in month 1, weekly after | Bekijk zoektermen 2×/week in maand 1, daarna wekelijks |

---

<a id="7"></a>
## 7. ✍️ Ad Copy (Responsive Search Ads) / Advertentieteksten

**EN —** Google requires up to **15 headlines (≤30 chars)** and **4 descriptions (≤90 chars)** per RSA. Character counts are given for every asset so you can paste directly into Google Ads Editor without validation errors. Dutch is the primary set (Campaign A); English mirrors it (Campaign B). Note the **"je" vs "u"** split: AG1, AG2 and AG5 use informal *je*; AG3 and AG4 use formal *u*, because security and audit buyers respond to a more serious register.

**NL —** Google staat maximaal **15 koppen (≤30 tekens)** en **4 beschrijvingen (≤90 tekens)** per RSA toe. Bij elk element staat het aantal tekens, zodat je direct in Google Ads Editor kunt plakken zonder validatiefouten. Nederlands is de primaire set (campagne A); Engels spiegelt die (campagne B). Let op de splitsing **"je" versus "u"**: AG1, AG2 en AG5 gebruiken het informele *je*; AG3 en AG4 gebruiken het formele *u*, omdat kopers van beveiliging en audits beter reageren op een serieuzer register.

### 📌 Pinning strategy / Vastzetstrategie

| Position | Pin | Reason / Reden |
|---|---|---|
| **Headline 1** | Pin the keyword-matching headline | Keyword in H1 lifts Quality Score / Zoekwoord in K1 verhoogt kwaliteitsscore |
| **Headline 2** | Unpinned (let Google rotate) | Google tests value props / Google test waardeproposities |
| **Headline 3** | Pin the price or speed asset | Fixed price is the strongest differentiator / Vaste prijs is de sterkste onderscheider |
| **Description 1** | Pin the offer description | Guarantees the offer is always shown / Garandeert dat het aanbod altijd zichtbaar is |
| **Rest** | Unpinned | Minimum 8 unpinned assets to avoid "Poor" ad strength / Minimaal 8 losse elementen om "Slecht" te vermijden |

---

### 🇳🇱 AG1 — Prototype → Productie (Dutch, register: *je*)

| # | Headline (kop) | Chars | Type | Pin |
|---|---|---|---|---|
| H1 | `AI-prototype Naar Productie` | 27 | Keyword | 📌 Pos 1 |
| H2 | `Prototype Live in 1-3 Weken` | 27 | Speed | — |
| H3 | `Vaste Prijs Vanaf €800` | 22 | Price | 📌 Pos 3 |
| H4 | `Wij Zetten Je App Live` | 22 | Value | — |
| H5 | `Werkt Je Prototype Niet?` | 24 | Pain | — |
| H6 | `Geen Herbouw, Wel Live` | 22 | Differentiator | — |
| H7 | `Je Code Blijft 100% Jouw` | 24 | Trust | — |
| H8 | `11+ Jaar Engineering` | 20 | Authority | — |
| H9 | `Backed by Manifera` | 18 | Brand | — |
| H10 | `Offerte Binnen 1 Werkdag` | 24 | CTA | — |
| H11 | `Gebouwd in Lovable of Bolt` | 26 | Qualifier | — |
| H12 | `Beveiliging, DB & Hosting` | 25 | Scope | — |
| H13 | `Plan Een 15-min Gesprek` | 23 | CTA | — |
| H14 | `Amsterdam · Heel Nederland` | 26 | Geo | — |
| H15 | `Van Prototype Naar Klant` | 24 | Outcome | — |

| # | Description (beschrijving) | Chars | Pin |
|---|---|---|---|
| D1 | `Je AI-prototype werkt, maar gaat niet live? Wij regelen beveiliging, database en hosting.` | 89 | 📌 Pos 1 |
| D2 | `Vaste prijs vanaf €800, live binnen 1-3 weken. Alle code blijft 100% van jou.` | 77 | — |
| D3 | `Gebouwd in Lovable, Bolt of Cursor? Wij maken het productieklaar zonder herbouw.` | 80 | — |
| D4 | `11+ jaar engineering van Manifera. Offerte met vaste scope binnen 1 werkdag.` | 76 | — |

### 🇬🇧 AG1 — Prototype → Production (English)

| # | Headline | Chars | # | Description | Chars |
|---|---|---|---|---|---|
| H1 | `AI Prototype To Production` | 26 | D1 | `Your AI prototype works but won't go live? We fix security, database and hosting.` | 81 |
| H2 | `Live In Just 1-3 Weeks` | 22 | D2 | `Fixed price from €800, live in 1-3 weeks. All code stays 100% yours. Start now.` | 79 |
| H3 | `Fixed Price From €800` | 21 | D3 | `Built in Lovable, Bolt or Cursor? We make it production-ready without a rebuild.` | 80 |
| H4 | `We Take Your App Live` | 21 | D4 | `11+ years of engineering from Manifera. Fixed-scope quote within 1 working day.` | 79 |
| H5 | `Prototype Won't Go Live?` | 24 | | | |
| H6 | `No Rebuild, Just Launch` | 23 | | | |
| H7 | `Your Code Stays 100% Yours` | 26 | | | |
| H8 | `11+ Years Engineering` | 21 | | | |
| H9 | `Backed By Manifera` | 18 | | | |
| H10 | `Quote Within 1 Working Day` | 26 | | | |
| H11 | `Built In Lovable Or Bolt` | 24 | | | |
| H12 | `Security, DB & Hosting` | 22 | | | |
| H13 | `Book A 15-Min Call` | 18 | | | |
| H14 | `Amsterdam · Netherlands` | 23 | | | |
| H15 | `From Prototype To Customer` | 26 | | | |

---

### 🇳🇱 AG2 — Productieklaar Maken (Dutch, register: *je*)

| # | Headline | Chars | # | Description | Chars |
|---|---|---|---|---|---|
| H1 | `App Productieklaar Maken` | 24 | D1 | `Van werkend prototype naar productieklaar: auth, database, betalingen en hosting.` | 81 |
| H2 | `Klaar Voor Lancering` | 20 | D2 | `Vaste scope, vaste prijs vanaf €800. Geen uurtarief, geen verrassingen achteraf.` | 80 |
| H3 | `Vaste Scope, Vaste Prijs` | 24 | D3 | `Wij raken je frontend niet aan. Wij fixen alleen wat de lancering tegenhoudt.` | 77 |
| H4 | `Auth, DB & Betalingen` | 21 | D4 | `Getest, beveiligd en live op je eigen domein. Inclusief 48 uur support na launch.` | 81 |
| H5 | `Live Binnen 1-3 Weken` | 21 | | | |
| H6 | `Wij Bouwen, Jij Lanceert` | 24 | | | |
| H7 | `Geen Uurtarief` | 14 | | | |
| H8 | `Getest Voor Je Live Gaat` | 24 | | | |
| H9 | `48u Support Na Lancering` | 24 | | | |
| H10 | `Vanaf €800 Vaste Prijs` | 22 | | | |
| H11 | `Frontend Blijft Van Jou` | 23 | | | |
| H12 | `Bekijk De Prijscalculator` | 25 | | | |

### 🇬🇧 AG2 — Production-Ready (English)

| # | Headline | Chars | # | Description | Chars |
|---|---|---|---|---|---|
| H1 | `Make Your App Production Ready` | 30 | D1 | `From working prototype to production-ready: auth, database, payments and hosting.` | 81 |
| H2 | `Productionize Your AI App` | 25 | D2 | `Fixed scope, fixed price from €800. No hourly rates and no surprises afterwards.` | 80 |
| H3 | `Fixed Scope, Fixed Price` | 24 | D3 | `We don't touch your frontend. We only fix what is blocking your launch.` | 71 |
| H4 | `Auth, DB & Payments` | 19 | D4 | `Tested, secured and live on your own domain. Includes 48h post-launch support.` | 78 |
| H5 | `Live In 1-3 Weeks` | 17 | | | |
| H6 | `We Build, You Launch` | 20 | | | |
| H7 | `No Hourly Billing` | 17 | | | |
| H8 | `Tested Before You Go Live` | 25 | | | |
| H9 | `48h Post-Launch Support` | 23 | | | |
| H10 | `From €800 Fixed Price` | 21 | | | |
| H11 | `Your Frontend Stays Intact` | 26 | | | |
| H12 | `See The Price Calculator` | 24 | | | |

---

### 🇳🇱 AG3 — Beveiliging AI-code (Dutch, register: *u*)

| # | Headline | Chars | # | Description | Chars |
|---|---|---|---|---|---|
| H1 | `AI-code Veilig Live Zetten` | 26 | D1 | `AI-gegenereerde code lekt vaak data. Wij vinden en dichten de gaten vóór uw launch.` | 83 |
| H2 | `Beveiliging AI-applicatie` | 25 | D2 | `Toegangsrechten, encryptie en AVG. Vaste prijs, rapport in begrijpelijke taal.` | 78 |
| H3 | `AVG-proof Voor U Live Gaat` | 26 | D3 | `11+ jaar security-ervaring van Manifera. Vertrouwd door Vodafone, TNO en CFLW.` | 78 |
| H4 | `Datalek Voorkomen` | 17 | D4 | `Wij herbouwen niets. Wij beveiligen wat u al heeft, binnen een vaste scope.` | 75 |
| H5 | `Beveiliging Vanaf €500` | 22 | | | |
| H6 | `11+ Jaar Security-ervaring` | 26 | | | |
| H7 | `Vodafone · TNO · CFLW` | 21 | | | |
| H8 | `Rapport In Klare Taal` | 21 | | | |
| H9 | `Toegangsrechten Getest` | 22 | | | |
| H10 | `Backed by Manifera` | 18 | | | |
| H11 | `Offerte Binnen 1 Werkdag` | 24 | | | |
| H12 | `Veilig Live In 1-3 Weken` | 24 | | | |

### 🇬🇧 AG3 — AI Code Security (English)

| # | Headline | Chars | # | Description | Chars |
|---|---|---|---|---|---|
| H1 | `Secure Your AI-Built App` | 24 | D1 | `AI-generated code often leaks data. We find and close the gaps before you launch.` | 81 |
| H2 | `AI Code Security Review` | 23 | D2 | `Access rules, encryption and GDPR. Fixed price, report written in plain English.` | 80 |
| H3 | `GDPR-Ready Before Launch` | 24 | D3 | `11+ years of security engineering from Manifera. Trusted by Vodafone, TNO, CFLW.` | 80 |
| H4 | `Prevent A Data Breach` | 21 | D4 | `We rebuild nothing. We secure what you already have, within a fixed scope.` | 74 |
| H5 | `Security From €500` | 18 | | | |
| H6 | `11+ Years Security Work` | 23 | | | |
| H7 | `Vodafone · TNO · CFLW` | 21 | | | |
| H8 | `Report In Plain English` | 23 | | | |
| H9 | `Access Rules Tested` | 19 | | | |
| H10 | `Backed By Manifera` | 18 | | | |
| H11 | `Quote Within 1 Working Day` | 26 | | | |
| H12 | `Secure & Live In 1-3 Weeks` | 26 | | | |

---

### 🇳🇱 AG4 — Beveiligingsaudit (Dutch, register: *u*) 💰

| # | Headline | Chars | # | Description | Chars |
|---|---|---|---|---|---|
| H1 | `Security Audit Applicatie` | 25 | D1 | `Onafhankelijke beveiligingsaudit van uw webapplicatie. Vaste prijs, geen nacalculatie.` | 86 |
| H2 | `Beveiligingsaudit Software` | 26 | D2 | `U krijgt een rapport met prioriteiten en een vaste offerte om de gaten te dichten.` | 82 |
| H3 | `Pentest Webapplicatie` | 21 | D3 | `Uitgevoerd door engineers met 11+ jaar ervaring. Vodafone, TNO en CFLW gingen u voor.` | 85 |
| H4 | `Vaste Prijs, Geen Nacalc.` | 25 | D4 | `Ook geschikt voor AI-gebouwde apps uit Lovable, Bolt of Cursor. Plan een gesprek.` | 81 |
| H5 | `Rapport Met Prioriteiten` | 24 | | | |
| H6 | `Audit Én Herstel Mogelijk` | 25 | | | |
| H7 | `11+ Jaar Ervaring` | 17 | | | |
| H8 | `Vodafone · TNO · CFLW` | 21 | | | |
| H9 | `Klaar Voor Due Diligence` | 24 | | | |
| H10 | `AVG & Enterprise-proof` | 22 | | | |
| H11 | `Offerte Binnen 1 Werkdag` | 24 | | | |
| H12 | `Ook Voor AI-gebouwde Apps` | 25 | | | |

### 🇬🇧 AG4 — Security Audit (English) 💰

| # | Headline | Chars | # | Description | Chars |
|---|---|---|---|---|---|
| H1 | `AI Application Security Audit` | 29 | D1 | `Independent security audit of your web application. Fixed price, no hourly billing.` | 83 |
| H2 | `Web App Security Audit` | 22 | D2 | `You get a prioritised report plus a fixed quote to close every gap we find.` | 75 |
| H3 | `Penetration Test Web App` | 24 | D3 | `Run by engineers with 11+ years' experience. Vodafone, TNO and CFLW came first.` | 79 |
| H4 | `Fixed Price, No Surprises` | 25 | D4 | `Also for AI-built apps from Lovable, Bolt or Cursor. Book a 15-minute call.` | 75 |
| H5 | `Prioritised Report` | 18 | | | |
| H6 | `Audit And Fix In One` | 20 | | | |
| H7 | `11+ Years Experience` | 20 | | | |
| H8 | `Vodafone · TNO · CFLW` | 21 | | | |
| H9 | `Due Diligence Ready` | 19 | | | |
| H10 | `GDPR & Enterprise Proof` | 23 | | | |
| H11 | `Quote Within 1 Working Day` | 26 | | | |
| H12 | `Built By AI? Still Fine.` | 24 | | | |

---

### 🇳🇱 AG5 — Schaalbaarheid (Dutch, register: *je*)

| # | Headline | Chars | # | Description | Chars |
|---|---|---|---|---|---|
| H1 | `Applicatie Schaalbaar Maken` | 27 | D1 | `Werkt je app prima met 10 gebruikers maar niet met 1.000? Wij lossen dat op.` | 76 |
| H2 | `Klaar Voor 10.000 Gebruikers` | 28 | D2 | `Database, queries en hosting geoptimaliseerd. Vaste prijs, live in 1-3 weken.` | 77 |
| H3 | `Trage App? Wij Fixen Het` | 24 | D3 | `Bereken direct wat het kost met onze prijscalculator. Geen verplichtingen.` | 74 |
| H4 | `Database Sneller Maken` | 22 | D4 | `11+ jaar engineering van Manifera. Wij weten waar prototypes stukgaan bij groei.` | 80 |
| H5 | `Groeien Zonder Downtime` | 23 | | | |
| H6 | `Vaste Prijs Vanaf €800` | 22 | | | |
| H7 | `Bekijk De Prijscalculator` | 25 | | | |
| H8 | `11+ Jaar Engineering` | 20 | | | |
| H9 | `Backed by Manifera` | 18 | | | |
| H10 | `Schaalbaar Zonder Herbouw` | 25 | | | |

### 🇬🇧 AG5 — Scalability (English)

| # | Headline | Chars | # | Description | Chars |
|---|---|---|---|---|---|
| H1 | `Make Your App Scalable` | 22 | D1 | `App fine with 10 users but not with 1,000? We find and fix the bottleneck.` | 74 |
| H2 | `Ready For 10,000 Users` | 22 | D2 | `Database, queries and hosting optimised. Fixed price, live within 1-3 weeks.` | 76 |
| H3 | `Slow App? We Fix It` | 19 | D3 | `Calculate the cost instantly with our price calculator. No obligations.` | 71 |
| H4 | `Speed Up Your Database` | 22 | D4 | `11+ years of engineering from Manifera. We know where prototypes break at scale.` | 80 |
| H5 | `Grow Without Downtime` | 21 | | | |
| H6 | `Fixed Price From €800` | 21 | | | |
| H7 | `See The Price Calculator` | 24 | | | |
| H8 | `11+ Years Engineering` | 21 | | | |
| H9 | `Backed By Manifera` | 18 | | | |
| H10 | `Scalable, No Rebuild` | 20 | | | |

---

<a id="8"></a>
## 8. 🔗 Extensions / Advertentie-extensies

**EN —** Extensions are free real estate: they raise CTR by 10–20% and take up more of the results page, pushing competitors down. At this budget level, *not* filling them in is the cheapest mistake you can still avoid. All are applied at campaign level unless noted.

**NL —** Extensies zijn gratis ruimte: ze verhogen de CTR met 10–20% en nemen meer van de resultatenpagina in beslag, waardoor concurrenten wegzakken. Op dit budgetniveau is ze *niet* invullen de goedkoopste fout die je nog kunt voorkomen. Alles wordt op campagneniveau ingesteld, tenzij anders vermeld.

### 📌 8.1 Sitelinks (max 25 chars + 2 × 35-char descriptions)

| 🇳🇱 Sitelink | Desc 1 | Desc 2 | URL |
|---|---|---|---|
| `Prijscalculator` | `Bereken je prijs in 1 minuut` | `Vrijblijvend, geen account nodig` | `/#calculator` |
| `Pakketten & Prijzen` | `Vaste prijs €800 – €7.500` | `Launch Ready of Launch & Grow` | `/#packages` |
| `Zo Werkt Het` | `In 3 stappen live` | `Start met een 15-min gesprek` | `/#howitworks` |
| `Plan Een Gesprek` | `15 minuten, vrijblijvend` | `Offerte binnen 1 werkdag` | `/#contact` |
| `Beveiliging & AVG` | `Security-audit vanaf €500` | `Rapport in begrijpelijke taal` | `/#contact` |
| `Over Manifera` | `11+ jaar engineering` | `160+ projecten, 120+ klanten` | `/#about` |

| 🇬🇧 Sitelink | Desc 1 | Desc 2 | URL |
|---|---|---|---|
| `Price Calculator` | `Estimate your price in 1 min` | `No account, no obligation` | `/en/#calculator` |
| `Packages & Pricing` | `Fixed price €800 – €7,500` | `Launch Ready or Launch & Grow` | `/en/#packages` |
| `How It Works` | `Live in 3 steps` | `Starts with a 15-min call` | `/en/#howitworks` |
| `Book A Call` | `15 minutes, no obligation` | `Quote within 1 working day` | `/en/#contact` |
| `Security & GDPR` | `Security audit from €500` | `Report in plain English` | `/en/#contact` |
| `About Manifera` | `11+ years of engineering` | `160+ projects, 120+ clients` | `/en/#about` |

### 📌 8.2 Callouts (max 25 chars)

| 🇳🇱 Dutch | 🇬🇧 English |
|---|---|
| `Vaste prijs vanaf €800` · `Live in 1-3 weken` · `100% code-eigendom` · `Geen uurtarief` · `11+ jaar ervaring` · `Backed by Manifera` · `48u support na launch` · `Frontend blijft intact` · `Offerte in 1 werkdag` · `Amsterdam, Nederland` | `Fixed price from €800` · `Live in 1-3 weeks` · `100% code ownership` · `No hourly billing` · `11+ years experience` · `Backed by Manifera` · `48h post-launch support` · `Frontend stays intact` · `Quote in 1 working day` · `Amsterdam, Netherlands` |

### 📌 8.3 Structured Snippets

| Header | 🇳🇱 Values | 🇬🇧 Values |
|---|---|---|
| **Diensten / Services** | Beveiliging · Betalingen · Database · Hosting · Deployment · Gebruikersaccounts · E-mailintegratie | Security · Payments · Database · Hosting · Deployment · User accounts · Email integration |
| **Types** | Website · Webshop · SaaS · Mobiele app · Dashboard · Interne tool | Website · Webshop · SaaS · Mobile app · Dashboard · Internal tool |

### 📌 8.4 Price extension / Prijsextensie

| Item (NL) | Price | Description |
|---|---|---|
| `Klaar voor lancering` | vanaf €800 | `Veilig, getest en live op je domein` |
| `Lancering & Groei` | vanaf €2.500 | `Inclusief betalingen en hosting` |
| `Beveiligingsaudit` | vanaf €500 | `Rapport met prioriteiten` |
| `Managed hosting` | €49/mnd | `SSL, monitoring en back-ups` |

### 📌 8.5 Other extensions / Overige extensies

| Extension | Setting / Instelling |
|---|---|
| **Call / Bellen** | Business hours only (Mon–Fri 09:00–18:00 CET) · Alleen kantooruren |
| **Location / Locatie** | Herengracht 420, 1017 BZ Amsterdam — builds local trust in NL |
| **Lead form** | ⚠️ Optional. Lower lead quality than the site form; test only after month 2 |
| **Image** | Product screenshot + Manifera logo lockup (1200×1200 and 1200×628) |

---

<a id="9"></a>
## 9. 🎯 Landing Pages & Conversion Tracking

### 9.1 Ad group → landing page mapping

| Ad group | 🇳🇱 Landing page | 🇬🇧 Landing page | Reason / Reden |
|---|---|---|---|
| AG1 Prototype→Production | `launchstudio.eu/` | `launchstudio.eu/en/` | Homepage tells the full story |
| AG2 Production-ready | `launchstudio.eu/#packages` | `launchstudio.eu/en/#packages` | Buyer wants scope + price |
| AG3 Code security | `launchstudio.eu/#contact` | `launchstudio.eu/en/#contact` | Fear-driven — shortest path |
| AG4 Security audit | `launchstudio.eu/#contact` | `launchstudio.eu/en/#contact` | Explicit purchase intent |
| AG5 Scalability | `launchstudio.eu/#calculator` | `launchstudio.eu/en/#calculator` | Nurture — let them self-qualify |
| AG6 AI development | *paused* | *paused* | — |

> **EN — Language must match the ad.** A Dutch ad must never land on `/en/`. Mismatched language is the second-most-common cause of a high bounce rate in bilingual accounts, after slow mobile load.
> **NL — De taal moet met de advertentie overeenkomen.** Een Nederlandse advertentie mag nooit op `/en/` landen. Taalmismatch is na trage mobiele laadtijd de meest voorkomende oorzaak van een hoog bouncepercentage in tweetalige accounts.

### 9.2 Conversion actions / Conversieacties

| # | Conversion | Category | Count | Value | Primary? |
|---|---|---|---|---|---|
| 1 | Contact form submitted / Contactformulier verzonden | Submit lead form | One | €150 | ✅ Primary |
| 2 | 15-min call booked / Gesprek ingepland | Book appointment | One | €250 | ✅ Primary |
| 3 | Phone call ≥60s / Telefoongesprek ≥60s | Phone call lead | One | €200 | ✅ Primary |
| 4 | Calculator completed / Calculator voltooid | Qualified visit | One | €25 | ⬜ Secondary |
| 5 | Packages page ≥45s / Pakketpagina ≥45s | Page view | One | €5 | ⬜ Secondary |

**EN —** Values are *proxy* values used to teach Smart Bidding which actions matter — they are not revenue. Set them from your real funnel: if 1 in 6 form submissions becomes a €2,500 project, a submission is worth roughly €400 gross; €150 is a deliberately conservative starting point. Revise after 30 real leads.

**NL —** De waarden zijn *proxywaarden* om Smart Bidding te leren welke acties ertoe doen — het is geen omzet. Stel ze in op basis van je echte funnel: als 1 op de 6 formulierinzendingen een project van €2.500 wordt, is een inzending ruwweg €400 bruto waard; €150 is bewust een conservatief startpunt. Herzie na 30 echte leads.

### 9.3 Offline conversion import / Offline conversie-import ⭐

**EN —** With only 15–50 clicks a month, Google's algorithm will never learn from online form fills alone. **Import offline conversions**: when a lead becomes a booked call, a sent quote, and finally a signed project, push those stages back into Google Ads with their real values (GCLID captured in a hidden form field). This is the single highest-leverage technical step in a low-volume, high-value account like this one — without it, Smart Bidding optimises towards *any* lead, including the unqualified ones.

**NL —** Met slechts 15–50 klikken per maand leert het algoritme van Google nooit genoeg uit alleen online formulierinzendingen. **Importeer offline conversies**: zodra een lead een ingepland gesprek, een verstuurde offerte en uiteindelijk een getekend project wordt, stuur je die fases met hun echte waarde terug naar Google Ads (GCLID vastleggen in een verborgen formulierveld). Dit is de technisch meest waardevolle stap in een account met laag volume en hoge waarde — zonder dit optimaliseert Smart Bidding richting *elke* lead, ook de ongekwalificeerde.

| Stage / Fase | Import value | When / Wanneer |
|---|---|---|
| Qualified lead / Gekwalificeerde lead | €300 | After the 15-min call |
| Quote sent / Offerte verstuurd | €800 | Same day |
| Project won / Project gewonnen | Actual deal value / Werkelijke dealwaarde | On signature |

### 9.4 Tracking checklist

- [ ] Google Ads conversion tag + enhanced conversions enabled / ingeschakeld
- [ ] GA4 linked to Google Ads / GA4 gekoppeld aan Google Ads
- [ ] GCLID stored in a hidden form field and in the CRM / GCLID opgeslagen in verborgen veld én CRM
- [ ] Consent Mode v2 implemented (mandatory in the EU) / Consent Mode v2 geïmplementeerd (verplicht in de EU)
- [ ] Cookie banner does not block conversion tags before consent / Cookiebanner blokkeert geen tags vóór toestemming
- [ ] Auto-tagging ON / Automatisch taggen AAN
- [ ] Phone-call conversions via a forwarding number / Beltrackingnummer actief
- [ ] UTM parameters on all final URLs / UTM-parameters op alle final URL's

---

<a id="10"></a>
## 10. 💰 Budget & Bidding / Budget & Biedstrategie

### 10.1 Three budget scenarios / Drie budgetscenario's

| | 🐢 Conservative / Voorzichtig | 🚶 Standard / Standaard | 🏃 Aggressive / Agressief |
|---|---|---|---|
| **Total / Totaal per month** | €600 | **€1,000** ⭐ | €2,000 |
| Campaign A (NL) 70% | €420 (€14/day) | **€700 (€23/day)** | €1,400 (€46/day) |
| Campaign B (EN) 30% | €180 (€6/day) | **€300 (€10/day)** | €600 (€20/day) |
| Expected clicks/mo | 60–90 | **100–160** | 200–320 |
| Expected leads/mo | 2–4 | **4–8** | 8–16 |
| Expected CPL | €150–€300 | **€125–€250** | €125–€250 |
| Learning period | 3–4 months | **2–3 months** | 6–8 weeks |

> **EN —** ⭐ **Standard is recommended.** At €600 the account gathers data too slowly for Smart Bidding to ever exit the learning phase; at €2,000 you outrun the available search volume on these niche terms and Google will start showing ads on looser matches.
> **NL —** ⭐ **Standaard is het advies.** Bij €600 verzamelt het account te traag data om ooit uit de leerfase te komen; bij €2.000 loop je harder dan het beschikbare zoekvolume op deze nichetermen en gaat Google adverteren op lossere matches.

### 10.2 Bidding roadmap / Biedstrategie in fasen

| Phase / Fase | Weeks | Strategy | Why / Waarom |
|---|---|---|---|
| **1 — Data** | 1–4 | Manual CPC or Maximise Clicks, CPC cap €6 (A) / €7 (B) | Control cost while search terms are still unknown / Kosten beheersen zolang zoektermen onbekend zijn |
| **2 — Signal** | 5–10 | Maximise Conversions (no tCPA yet) | Needs ~15 conversions before a target is meaningful / Pas zinvol vanaf ~15 conversies |
| **3 — Target** | 11–16 | Maximise Conversions with tCPA €120 (A) / €140 (B) | Now enough data to set a target / Nu genoeg data voor een doel |
| **4 — Value** | 17+ | Maximise Conversion Value with tROAS, using offline values | Optimises for deal size, not lead count / Optimaliseert op dealwaarde, niet leadaantal |

### 10.3 Bid adjustments / Bodaanpassingen

| Dimension | Adjustment | Reason / Reden |
|---|---|---|
| Desktop | **+15%** | B2B quote requests happen on desktop |
| Mobile | **−20%** | Higher bounce, lower lead quality on these terms |
| Tablet | **−40%** | Negligible qualified volume |
| Mon–Fri 09:00–18:00 | **+20%** | Business hours = business buyers |
| Sat–Sun | **−40%** | Research traffic, rarely converts |
| Amsterdam / Utrecht / Rotterdam / Den Haag | **+15%** | Startup + scale-up density |
| Returning visitors (RLSA) | **+30%** | Consideration cycle is 2–6 weeks |

---

<a id="11"></a>
## 11. 📅 90-Day Roadmap / 90-Dagen Routekaart

### Days 1–14 — Setup & first data / Opzet & eerste data

| # | Task / Taak | Owner |
|---|---|---|
| 1 | Verify all volumes and CPCs in Keyword Planner (NL, Dutch + English) | Marketing |
| 2 | Build Campaign A + B, AG1–AG5 (AG6 paused) | Marketing |
| 3 | Attach all 5 shared negative lists **before** enabling ads | Marketing |
| 4 | Install conversion tags, Consent Mode v2, GCLID capture | Dev |
| 5 | Upload all RSAs (min. 12 headlines, 4 descriptions each) | Marketing |
| 6 | Configure all extensions (§8) | Marketing |
| 7 | Enable Phrase + Exact only. **No broad match.** | Marketing |
| 8 | Check search terms report on days 3, 7, 10 and 14 | Marketing |

### Days 15–30 — Cleanup / Opschonen

| # | Task | Target |
|---|---|---|
| 9 | Add every irrelevant search term as a negative | 2×/week |
| 10 | Pause keywords with >30 clicks and 0 conversions | Weekly |
| 11 | Pause RSA assets rated "Low" | Day 30 |
| 12 | Check landing-page mobile speed (target <2.5s LCP) | Once |
| 13 | Review Auction Insights: who else bids on AG4? | Day 30 |

### Days 31–60 — Optimise / Optimaliseren

| # | Task | Target |
|---|---|---|
| 14 | Switch to Maximise Conversions once ≥15 conversions | Week 6 |
| 15 | Start offline conversion import (§9.3) | Week 6 |
| 16 | Add a second RSA per ad group for A/B comparison | Week 7 |
| 17 | Shift budget towards the ad group with lowest CPL | Weekly |
| 18 | Add broad match **only** on AG1 + AG4 top keywords | Week 8 |
| 19 | Build RLSA audience lists (site visitors, calculator users) | Week 8 |

### Days 61–90 — Scale / Opschalen

| # | Task | Target |
|---|---|---|
| 20 | Set tCPA €120 / €140 once 30+ conversions | Week 10 |
| 21 | Consider Campaign C for Flanders (BE) — separate budget | Week 11 |
| 22 | Evaluate whether AG6 can be safely activated | Week 12 |
| 23 | Add Performance Max **only** if Search is already profitable | Week 12 |
| 24 | Write the quarterly report: CPL, CAC, closed deals, ROAS | Day 90 |

---

<a id="12"></a>
## 12. 📊 KPIs & Optimisation Rules / KPI's & Optimalisatieregels

### 12.1 Targets by month / Doelen per maand

| Metric / Statistiek | Month 1 | Month 2 | Month 3 | Month 6 |
|---|---|---|---|---|
| CTR (Search) | >4% | >6% | >7% | >8% |
| Avg. CPC | €5–8 | €5–7 | €4–7 | €4–6 |
| Conversion rate | >2% | >3.5% | >5% | >6% |
| Cost per lead (CPL) | <€300 | <€200 | <€150 | <€125 |
| Qualified leads/mo | 2–4 | 4–6 | 5–8 | 8–12 |
| Quality Score (avg) | ≥5 | ≥6 | ≥7 | ≥7 |
| Impression share (AG4) | >40% | >55% | >65% | >70% |
| Closed deals/mo | 0–1 | 1 | 1–2 | 2–3 |

### 12.2 The number that actually matters / Het getal dat er echt toe doet

**EN —** With an average deal of €2,000–€3,000 and a healthy 3:1 LTV:CAC target, an acceptable **cost per closed deal is €400–€800**. At a 20% lead-to-deal close rate, that permits a CPL of €80–€160. Everything above €300 CPL for more than one month means the structure — not the budget — needs fixing.

**NL —** Bij een gemiddelde deal van €2.000–€3.000 en een gezonde LTV:CAC-verhouding van 3:1 zijn **kosten per gesloten deal van €400–€800** acceptabel. Bij een conversieratio van 20% van lead naar deal mag de CPL €80–€160 zijn. Alles boven €300 CPL gedurende meer dan één maand betekent dat de structuur moet worden aangepast — niet het budget.

### 12.3 Fixed optimisation rules / Vaste optimalisatieregels

| Rule / Regel | Action / Actie |
|---|---|
| Keyword: >30 clicks, 0 conversions | Pause / Pauzeren |
| Keyword: CPL > 2× target for 30 days | Pause or lower bid −40% |
| Search term: irrelevant, ≥2 impressions | Add as phrase negative immediately |
| Ad group: 0 impressions for 14 days | Check match types and bids, then broaden |
| RSA: asset rated "Low" | Replace, never just delete |
| Ad strength: "Poor"/"Average" | Add unpinned assets until "Good"+ |
| Impression share lost (budget) >25% | Raise budget on that campaign only |
| Impression share lost (rank) >40% | Improve Quality Score before raising bids |

---

<a id="13"></a>
## 13. ⚙️ Import Notes / Importinstructies (Google Ads Editor)

**EN —** Build the account offline in Google Ads Editor, then post everything at once. This prevents the classic failure where ads go live before the negative lists are attached.

**NL —** Bouw het account offline in Google Ads Editor en post daarna alles in één keer. Dat voorkomt de klassieke fout waarbij advertenties live gaan vóórdat de uitsluitingslijsten zijn gekoppeld.

### 13.1 CSV column structure for keyword import

```
Campaign, Ad Group, Keyword, Criterion Type, Max CPC, Final URL, Campaign Status, Ad Group Status
LS_NL_Production_NL, AG1_Prototype_Productie, ai prototype naar productie, Exact, 6.00, https://launchstudio.eu/, Paused, Enabled
LS_NL_Production_NL, AG1_Prototype_Productie, prototype productieklaar maken, Phrase, 6.00, https://launchstudio.eu/, Paused, Enabled
LS_NL_Production_EN, AG1_Prototype_Production, ai prototype to production, Exact, 8.00, https://launchstudio.eu/en/, Paused, Enabled
```

### 13.2 Naming convention / Naamgevingsconventie

| Level | Pattern | Example |
|---|---|---|
| Campaign | `LS_[GEO]_[THEME]_[LANG]` | `LS_NL_Production_NL` |
| Ad group | `AG[n]_[Theme]` | `AG4_Security_Audit` |
| Negative list | `NEG_[Theme]_[LANG]` | `NEG_Jobs_NL_EN` |
| Audience | `AUD_[Type]_[Window]` | `AUD_Visitors_30d` |

### 13.3 Pre-launch checklist / Checklist vóór livegang

- [ ] Campaigns created **paused** / Campagnes aangemaakt op **gepauzeerd**
- [ ] All 5 negative lists attached to both campaigns / Alle 5 lijsten gekoppeld
- [ ] Location = Netherlands, **Presence only** / Locatie = Nederland, **alleen aanwezigheid**
- [ ] Languages = Dutch **+ English** in both campaigns / Talen = Nederlands **+ Engels**
- [ ] Search partners OFF, Display expansion OFF / Zoekpartners UIT, Display-uitbreiding UIT
- [ ] Every ad group has ≥12 headlines and 4 descriptions
- [ ] Every final URL returns 200 and matches the ad language
- [ ] Conversion tracking verified with a live test submission
- [ ] Daily budget caps set; shared budget **not** used
- [ ] Calendar reminder: review search terms on days 3, 7, 14

---

<a id="14"></a>
## 14. ⚠️ Risks & Mitigations / Risico's & Maatregelen

| # | Risk / Risico | Impact | Mitigation / Maatregel |
|---|---|---|---|
| 1 | **Dutch keyword volume near zero** / Nederlands zoekvolume vrijwel nul | 🔴 High | Campaign B (English-in-NL) carries volume; judge Campaign A on lead quality, not clicks |
| 2 | **"AI development" drains budget** if enabled | 🔴 High | AG6 stays paused; List 4 negatives attached account-wide |
| 3 | **Too few conversions for Smart Bidding** | 🔴 High | Offline conversion import (§9.3) + secondary conversions as signal |
| 4 | **Job seekers on "AI developer" terms** | 🟡 Med | List 1 negatives applied before launch, reviewed 2×/week |
| 5 | **CPC inflation on `pentest` / `security audit`** | 🟡 Med | Separate ad group with its own bid cap; never merge into AG3 |
| 6 | **Language mismatch ad → landing page** | 🟡 Med | Hard-coded final URLs per campaign; verified in the pre-launch checklist |
| 7 | **Consent Mode blocks conversion data** | 🟡 Med | Test Consent Mode v2 with a real submission before enabling ads |
| 8 | **Competitor bidding on brand "LaunchStudio"** | 🟢 Low | Separate brand campaign at ~€100/mo, Target Impression Share 95% |
| 9 | **Seasonality: Dutch summer + Christmas** | 🟢 Low | Expect −30–40% volume in Jul–Aug and late Dec; do not cut budget structurally |
| 10 | **Attribution: 2–6 week consideration cycle** | 🟡 Med | Use a 30-day click window and data-driven attribution, not last-click |

---

## ✅ Summary — What to do first / Samenvatting — Wat als eerste te doen

**EN —**
1. Read §2 before anything else — the Dutch/English split decides whether this account works at all.
2. Verify volumes in Keyword Planner; expect them to be low and plan for quality, not scale.
3. Build both campaigns paused, attach all five negative lists, then enable.
4. Start Phrase + Exact only, at €1,000/month split 70/30.
5. Get offline conversion import working in month 2 — it is the difference between Smart Bidding helping and hurting.
6. Judge the account at day 90 on **cost per closed deal**, not on clicks or impressions.

**NL —**
1. Lees §2 als eerste — de splitsing Nederlands/Engels bepaalt of dit account überhaupt werkt.
2. Verifieer volumes in Keyword Planner; verwacht lage aantallen en stuur op kwaliteit, niet op schaal.
3. Bouw beide campagnes gepauzeerd, koppel alle vijf uitsluitingslijsten en zet ze daarna aan.
4. Start met alleen Phrase + Exact, op €1.000/maand verdeeld 70/30.
5. Krijg offline conversie-import werkend in maand 2 — dat bepaalt of Smart Bidding helpt of schaadt.
6. Beoordeel het account op dag 90 op **kosten per gesloten deal**, niet op klikken of vertoningen.

---

> **Sources / Bronnen:** [`extra-keywords.md`](extra-keywords.md) (14 unique keywords) · [`launchstudio_info.md`](launchstudio_info.md) (pricing, packages, USP, GEO-entities) · existing [`google_ads_keywords_launchstudio.md`](google_ads_keywords_launchstudio.md) and [`google_ads_rsa_copy_launchstudio.md`](google_ads_rsa_copy_launchstudio.md) (structure and voice alignment).
>
> **Note / Let op:** All search volumes and CPCs in this document are **estimates for planning purposes**, based on the Dutch B2B software-services market. Verify every figure in Google Keyword Planner with location = Netherlands and languages = Dutch + English before committing budget.
> Alle zoekvolumes en CPC's in dit document zijn **schattingen voor planningsdoeleinden**, gebaseerd op de Nederlandse B2B-softwaredienstenmarkt. Verifieer elk getal in Google Keyword Planner met locatie = Nederland en talen = Nederlands + Engels voordat je budget vastlegt.

---

<a id="15"></a>
## 15. 🖊️ Decisions Required Before Launch / Beslissingen Vóór Livegang

**EN —** Four points in this plan need an explicit yes or no before the account is built. Three of them are recommendations that deviate from an intuitive reading of the brief, and one is an expectation that has to be agreed in advance so the campaign is not judged by the wrong yardstick in week three. Each carries a recommendation, the reasoning, and what happens if the opposite is chosen.

**NL —** Vier punten in dit plan vragen om een expliciet ja of nee voordat het account wordt gebouwd. Drie ervan zijn adviezen die afwijken van een intuïtieve lezing van de opdracht, en één is een verwachting die vooraf moet worden vastgelegd zodat de campagne in week drie niet langs de verkeerde meetlat wordt gelegd. Bij elk punt staan het advies, de onderbouwing en het gevolg van de tegenovergestelde keuze.

---

### 🔴 Decision 1 — Run English keywords inside the Dutch market
### 🔴 Beslissing 1 — Engelse zoekwoorden inzetten binnen de Nederlandse markt

| | |
|---|---|
| **Recommendation / Advies** | ✅ **Yes** — Campaign A (Dutch, 70%) **+** Campaign B (English, 30%), both geo-targeted to the Netherlands only. |
| **Why / Waarom** | 🇬🇧 Dutch tech founders type technical terms in English. All 14 source keywords are English technical vocabulary, and "productionize" has no Dutch equivalent at all. Dutch-only keywords would reach a fraction of the actual Dutch demand.<br>🇳🇱 Nederlandse tech-oprichters typen vaktermen in het Engels. Alle 14 bronzoekwoorden zijn Engels vakjargon, en "productionize" heeft geen Nederlands equivalent. Alleen Nederlandse zoekwoorden bereiken maar een fractie van de werkelijke Nederlandse vraag. |
| **Does this break the brief? / Wijkt dit af van de opdracht?** | No. The market stays **the Netherlands only**, and the primary ad language stays **Dutch** with 70% of the budget. Only the keyword layer is bilingual. |
| **If you decide no / Bij een nee** | Dutch-only is workable but expect roughly **60–70% fewer qualified clicks** and a materially higher cost per lead. In that case, raise the AG4 (audit) budget share, because `security audit` is the one theme with genuine Dutch-language volume. |
| **Your decision / Uw beslissing** | ☐ Approved · ☐ Dutch only · Date: ________ |

---

### 🔴 Decision 2 — Keep keyword #08 "AI development" paused
### 🔴 Beslissing 2 — Zoekwoord #08 "AI development" gepauzeerd houden

| | |
|---|---|
| **Recommendation / Advies** | ✅ **Yes, keep AG6 paused** at launch. |
| **Why / Waarom** | 🇬🇧 It is a head term with a different intent: searchers want someone to *build AI models, chatbots or ML pipelines*, not to harden an existing prototype. Dutch AI consultancies bid €8–€15 CPC on it. On a €700 daily-capped campaign it would absorb the budget within days at a near-zero conversion rate.<br>🇳🇱 Het is een hoofdterm met een andere intentie: zoekers willen dat iemand *AI-modellen, chatbots of ML-pipelines bouwt*, niet dat een bestaand prototype productieklaar wordt gemaakt. Nederlandse AI-consultancybureaus bieden er €8–€15 CPC op. Op een campagne met een dagbudgetplafond zou het het budget binnen dagen opslokken bij vrijwel nul conversie. |
| **Activation rule / Activatieregel** | Only after AG1–AG4 have produced **≥10 conversions**, and then only as `[ai development bureau nederland]` / `[ai development agency netherlands]` Exact, with negative List 4 attached. |
| **If you decide to run it anyway / Bij toch activeren** | Give it a **separate campaign with its own €150/month cap**, never inside Campaigns A or B. That way it cannot cannibalise the budget of the ad groups that actually convert. |
| **Your decision / Uw beslissing** | ☐ Keep paused · ☐ Activate in a separate capped campaign · Date: ________ |

---

### 🟡 Decision 3 — Accept that this is a low-volume, high-intent account
### 🟡 Beslissing 3 — Accepteren dat dit een account is met laag volume en hoge intentie

| | |
|---|---|
| **Recommendation / Advies** | ✅ **Agree the yardstick in advance:** judge the account on **cost per closed deal (€400–€800)**, not on impressions, clicks or CTR. |
| **Reality / Realiteit** | 🇬🇧 Estimated 200–600 searches/month in the Netherlands across all 14 keywords and variants ⇒ roughly **15–50 clicks/month** and **4–8 leads/month** at the standard budget. This is normal and expected for a niche B2B service.<br>🇳🇱 Geschat 200–600 zoekopdrachten/maand in Nederland over alle 14 zoekwoorden en varianten ⇒ ruwweg **15–50 klikken/maand** en **4–8 leads/maand** bij het standaardbudget. Dat is normaal en verwacht voor een niche-B2B-dienst. |
| **The risk of not agreeing this / Het risico van geen afspraak** | 🇬🇧 In week 3 the dashboard will show a few hundred impressions and it will *feel* like a failure. The usual reaction — pause the campaign or widen the keywords — destroys the account: broad match on a small budget converts a precise campaign into an expensive irrelevant one.<br>🇳🇱 In week 3 laat het dashboard een paar honderd vertoningen zien en dat *voelt* als een mislukking. De gebruikelijke reactie — campagne pauzeren of zoekwoorden verbreden — sloopt het account: breed zoeken op een klein budget maakt van een precieze campagne een dure irrelevante. |
| **Agreed review point / Afgesproken evaluatiemoment** | **Day 90**, on cost per closed deal — not day 21 on impressions. |
| **Your decision / Uw beslissing** | ☐ Agreed · Date: ________ |

---

### 🟡 Decision 4 — Budget level and ownership of the tracking work
### 🟡 Beslissing 4 — Budgetniveau en eigenaarschap van het trackingwerk

| | |
|---|---|
| **Recommendation / Advies** | ✅ **€1,000/month (Standard)**, split 70/30, **and** offline conversion import built in month 2. |
| **Why this budget / Waarom dit budget** | 🇬🇧 At €600 the account gathers conversion data too slowly for Smart Bidding ever to leave the learning phase. At €2,000 you outrun the available search volume and Google starts matching looser queries.<br>🇳🇱 Bij €600 verzamelt het account te traag conversiedata om ooit uit de leerfase te komen. Bij €2.000 loop je harder dan het beschikbare zoekvolume en gaat Google lossere zoekopdrachten matchen. |
| **The dev dependency / De ontwikkelafhankelijkheid** | 🇬🇧 Offline conversion import (§9.3) requires a developer to capture the GCLID in a hidden form field and store it in the CRM. **Without it, Smart Bidding optimises towards any lead, including unqualified ones.** In a low-volume account this is the difference between the algorithm helping and actively hurting.<br>🇳🇱 Offline conversie-import (§9.3) vereist dat een ontwikkelaar de GCLID in een verborgen formulierveld vastlegt en in het CRM opslaat. **Zonder dat optimaliseert Smart Bidding richting elke lead, ook de ongekwalificeerde.** In een account met laag volume bepaalt dit of het algoritme helpt of juist schaadt. |
| **Needed from your side / Nodig van uw kant** | ☐ Budget approved: €______/month · ☐ Developer assigned for GCLID + Consent Mode v2 · ☐ CRM stage names agreed for import (§9.3) |
| **Your decision / Uw beslissing** | ☐ Standard €1,000 · ☐ Conservative €600 · ☐ Aggressive €2,000 · Date: ________ |

---

### 📋 Sign-off summary / Overzicht ter accordering

| # | Decision / Beslissing | Recommended / Aanbevolen | Status |
|---|---|---|---|
| 1 | English keywords inside the NL market / Engelse zoekwoorden binnen de NL-markt | ✅ Yes, 70/30 split | ☐ |
| 2 | "AI development" paused / "AI development" gepauzeerd | ✅ Yes, keep paused | ☐ |
| 3 | Judge on cost per closed deal / Beoordelen op kosten per gesloten deal | ✅ Agreed, review at day 90 | ☐ |
| 4 | €1,000/month + offline conversion import | ✅ Standard scenario | ☐ |

> **EN —** Nothing in §§1–14 needs to change if all four are approved as recommended; the plan is written on that basis. If decision 1 or 2 is answered differently, only §4 (campaign architecture) and §10 (budget split) need adjusting — the keyword, negative and ad-copy work stays valid.
>
> **NL —** Als alle vier de punten worden goedgekeurd zoals aanbevolen, hoeft er niets in §§1–14 te wijzigen; het plan is daarop geschreven. Wordt beslissing 1 of 2 anders beantwoord, dan hoeven alleen §4 (campagnestructuur) en §10 (budgetverdeling) te worden aangepast — het zoekwoord-, uitsluitings- en advertentiewerk blijft geldig.
