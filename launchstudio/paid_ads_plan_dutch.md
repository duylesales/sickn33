# LaunchStudio — Paid Advertising Plan (Multi-Channel, Execution-Ready) — Nederlandse versie

> **Scope:** https://launchstudio.eu/ — productiegereedheidsdienst voor AI-native oprichters (moederbedrijf: Manifera)
> **Brondata:** `keyword-planner-https___launchstudio.eu_en_-2026-06-15.csv` (123 zoekwoorden, 214.280 totaal maandelijks zoekvolume)
> **Opgesteld:** 2026-07-24 · **Herzien:** uitvoeringsdetail-pass
> **Bijbehorend bestand:** `paid_ads_plan.md` (English version)
> **Hoe dit document te gebruiken:** Sectie 3 is de strategische onderbouwing (bewaar deze). Secties 4–13 zijn kant-en-klare campagnestructuren, advertentieteksten, budgetten en een week-voor-week bouwchecklist — dit is hoe een advertentieaccount er op dag 1 daadwerkelijk uit zou moeten zien.

---

## 1. Samenvatting

LaunchStudio's bestaande zoekwoorddata is uitsluitend gericht op Search en uitsluitend Engelstalig, maar de koper bevindt zich niet alleen in Google Search. Dit plan reinigt de CSV (het kopcijfer van "214.280/maand" bestaat voor 94% uit één mismatch-term — zie §3.1), breidt deze uit met tool-merktermen, probleemgerichte termen, vergelijkingstermen en Nederlandstalige zoekwoorden, en zet **exacte, direct te lanceren campagnestructuren voor 6 platforms** neer: Google Search, Microsoft/Bing, LinkedIn, Meta, X (Twitter) en Reddit — inclusief namen van advertentiegroepen, koppeling van zoekwoorden aan advertentiegroepen, voorgestelde biedingen, volledige advertentieteksten, doelgroepspecificaties, dagbudgetten, UTM-conventies en content-outlines voor landingspagina's.

**Aanbevolen startbudget: €5.000/maand (Tier 2, zie §9)** — dit document is rond dat bedrag opgebouwd, zodat elke campagne een concreet eurocijfer heeft, niet alleen een percentage. Schaal proportioneel op of af met de Tier 1-/Tier 3-tabellen in §9 als het daadwerkelijk beschikbare budget afwijkt.

---

## 2. Funnel-indeling (Koperfase → Kanaalrol)

| Fase | Denkwijze koper | Best passende kanalen | Zoekwoord-/targetinglogica |
|---|---|---|---|
| **Bewustzijn** | "Ik heb iets gebouwd met AI, is dat normaal?" | X, Reddit, Meta (video), YouTube | Tool-merktermen, plaatsing in communities |
| **Overweging** | "Hoe krijg ik dit live / veilig / betaald?" | Google Search, LinkedIn, Meta-retargeting | Probleem-/bouw-intentietermen |
| **Beslissing** | "Wie huur ik hier daadwerkelijk voor in?" | Google Search (merk + vergelijking), LinkedIn InMail, Bing | Vergelijkingstermen, merktermen |

---

## 3. Zoekwoordstrategie

### 3.1. De bestaande CSV opschonen — waar NIET op te bieden zoals het nu is

| Zoekwoord | Volume | Waarom het een valkuil is |
|---|---|---|
| `day ai` | 201.000 | 94% van het totale volume in de CSV. Vrijwel zeker een brede-match-/mismatch-zoekwoordgroep. **Volledig uitsluiten; voeg `-day` toe als gedeeld uitsluitingszoekwoord.** |
| `2 software`, `for you ai`, `back ai`, `ai low` | elk 10 | Fragmenten, geen samenhangende intentie. Uitsluiten. |
| `ai download*`, `*download free`, `app ai free`, `free software ai`, `no code ai free` | ~230 gecombineerd | Intentie van gratis-zoekers, geen koper van een betaalde dienst. Indien getest, isoleer met een harde budgetlimiet, nooit mengen met commerciële advertentiegroepen. |

**Netto bruikbaar volume na opschoning: ~12.700–13.000/maand**, niet 214.280. Alle bied- en budgetcijfers hieronder zijn gebaseerd op het opgeschoonde cijfer.

### 3.2–3.3. Zoekwoordclusters en uitbreidingstermen

*(Volledige clustertabellen behouden uit de oorspronkelijke onderzoekspass — hier compact herhaald; zie §4 voor de exacte opbouw van de advertentiegroepen.)*

- **Cluster A — Toolspecifiek:** `bolt ai` (1.300), `ai coding` (1.600), `ai to code` (1.600), `ai for coding` (1.000)
- **Cluster B — Bouw-/productie-intentie:** `make a ai` (480), `build ai` (260), `ai development` (260), `dev ai` (260), `build app with ai` (40), `build an app with ai` (30), `ai prototype` (20), `develop ai software` (70)
- **Cluster C — Beveiliging/vertrouwen:** `ai secure` (140), `security ai` (50), + ~20 varianten met laag volume rond beveiliging/privacy (~430/maand gecombineerd)
- **Cluster D — SaaS-/productframing:** `ai saas` (50), `saas ai` (30), `ai saas platform` (10), `ai saas products` (10)
- **Cluster E — Generiek/dubbelzinnig (voorzichtig testen):** `user ai` (1.900), `ai assist` (1.600), `ai websites` (720), `ai works` (90), `ai native` (110), `ai database` (110)
- **Uitbreiding — Tool-merk:** `lovable to production`, `lovable security`, `lovable backend`, `bolt.new deploy`, `bolt.new production`, `bolt.new security`, `cursor app deployment`, `cursor to production`, `v0 to production`, `v0 vercel backend`, `replit deployment security`, `vibe coding to production`, `vibe coding security`
- **Uitbreiding — Probleemgericht:** `is my ai app secure`, `ai generated code security risk`, `ai app security audit`, `lovable app hacked`, `exposed api keys frontend`, `ai prototype not production ready`, `freelancer doesn't understand ai code`, `ai code review service`
- **Uitbreiding — Vergelijking:** `launchstudio review`, `launchstudio vs`, `ai app developer netherlands`, `ai app agency vs freelancer`, `hire developer for ai prototype`
- **Uitbreiding — Nederlands:** `AI app laten bouwen`, `AI prototype beveiligen`, `software developer inhuren`, `AI applicatie live zetten`, `vibe coding productie klaar`, `app ontwikkelaar inhuren`, `AI SaaS laten maken`, `beveiligingsaudit AI code`, `Lovable app naar productie`
- **Uitbreiding — Lokaal (eerste 10 steden om mee te starten, later uitbreiden naar de volledige lijst van 60 steden uit `extra-5`):** Amsterdam, Rotterdam, Utrecht, Den Haag, Eindhoven, Groningen, Tilburg, Breda, Nijmegen, Enschede — gecombineerd met `software ontwikkelaar [stad]`, `AI app bouwen [stad]`, `app developer [stad]`

---

## 4. Google Ads — Search: Exacte Campagne- en Advertentiegroepopbouw

**Accountstructuurconventie:** `LaunchStudio – Search – [Language] – [Cluster Name]`. Minimaal één conversieactie per campagne; gedeelde lijst met uitsluitingszoekwoorden accountbreed toegepast (§4.9).

### 4.1. Campagne: `LS-Search-EN-ToolIntent` (Cluster A)

| Advertentiegroep | Zoekwoorden (matchtype) | Voorgestelde Max. CPC | Dagbudget |
|---|---|---|---|
| `AG-BoltAI` | `[bolt ai]`, `"bolt.new production"`, `"bolt.new deploy"`, `"bolt.new security"` | €3,50 | €15 |
| `AG-AICoding` | `[ai coding]`, `[ai to code]`, `"ai for coding"`, `"vibe coding to production"`, `"vibe coding security"` | €4,00 | €20 |
| `AG-ToolBrands` | `"lovable to production"`, `"lovable security"`, `"lovable backend"`, `"cursor app deployment"`, `"cursor to production"`, `"v0 to production"`, `"v0 vercel backend"`, `"replit deployment security"` | €3,00 | €10 |

**Dagbudget campagne: €45** (~€1.350/maand)

### 4.2. Campagne: `LS-Search-EN-ProductionIntent` (Cluster B)

| Advertentiegroep | Zoekwoorden (matchtype) | Voorgestelde Max. CPC | Dagbudget |
|---|---|---|---|
| `AG-BuildWithAI` | `[build app with ai]`, `"build an app with ai"`, `"build ai"`, `"make a ai"` | €5,50 | €20 |
| `AG-PrototypeToProd` | `"ai prototype"`, `"ai prototype not production ready"`, `"ai development"`, `"develop ai software"` | €3,50 | €12 |
| `AG-FreelancerPain` | `"freelancer doesn't understand ai code"`, `"ai code review service"` | €4,00 | €8 |

**Dagbudget campagne: €40** (~€1.200/maand)

### 4.3. Campagne: `LS-Search-EN-SecurityIntent` (Cluster C — cluster met hoogste waarde)

| Advertentiegroep | Zoekwoorden (matchtype) | Voorgestelde Max. CPC | Dagbudget |
|---|---|---|---|
| `AG-SecureCore` | `[ai secure]`, `"security ai"` | €8,00 | €20 |
| `AG-SecurityLongtail` | Woordgroep-match op de ~20 zoekwoordvarianten met nul/laag volume rond beveiliging (`"ai security issues"`, `"ai security risk"`, `"ai vulnerabilities"`, `"ai data security"`, `"ai privacy issues"`, enz.) | €5,00 | €10 |
| `AG-SecurityProblemAware` | `"is my ai app secure"`, `"ai generated code security risk"`, `"lovable app hacked"`, `"exposed api keys frontend"`, `"ai app security audit"` | €4,50 | €10 |

**Dagbudget campagne: €40** (~€1.200/maand)

### 4.4. Campagne: `LS-Search-EN-SaaSFraming` (Cluster D)

| Advertentiegroep | Zoekwoorden | Max. CPC | Dagbudget |
|---|---|---|---|
| `AG-AISaaS` | `"ai saas"`, `"saas ai"`, `"ai saas platform"`, `"ai saas products"` | €4,00 | €5 |

### 4.5. Campagne: `LS-Search-EN-Comparison` (Beslissingsfase)

| Advertentiegroep | Zoekwoorden | Max. CPC | Dagbudget |
|---|---|---|---|
| `AG-Branded` | `[launchstudio]`, `"launchstudio review"`, `"launchstudio vs"` | €2,50 | €3 |
| `AG-Comparison` | `"ai app developer netherlands"`, `"ai app agency vs freelancer"`, `"hire developer for ai prototype"` | €5,00 | €5 |

### 4.6. Campagne: `LS-Search-EN-GenericTest` (Cluster E — verkennend met harde limiet)

| Advertentiegroep | Zoekwoorden | Max. CPC | Dagbudget |
|---|---|---|---|
| `AG-GenericTerms` | `"user ai"`, `"ai assist"`, `"ai websites"`, `"ai works"`, `"ai native"`, `"ai database"` | €2,00 | €10 (harde limiet — niet verhogen totdat de conversieratio zich bewijst) |

### 4.7. Campagne: `LS-Search-NL-Core` (Nederlands — de grootste onaangeboorde kans)

| Advertentiegroep | Zoekwoorden | Max. CPC | Dagbudget |
|---|---|---|---|
| `AG-AIAppBouwen` | `"AI app laten bouwen"`, `"app ontwikkelaar inhuren"`, `"software developer inhuren"`, `"AI applicatie live zetten"` | €3,00 | €15 |
| `AG-AIBeveiliging` | `"AI prototype beveiligen"`, `"beveiligingsaudit AI code"` | €3,50 | €10 |
| `AG-VibeCodingNL` | `"vibe coding productie klaar"`, `"Lovable app naar productie"`, `"AI prototype naar klanten"` | €2,50 | €5 |
| `AG-AISaaSNL` | `"AI SaaS laten maken"` | €3,00 | €3 |

**Dagbudget campagne: €33** (~€1.000/maand)

### 4.8. Campagne: `LS-Search-NL-Local` (Geo-laag, top 10 steden)

Eén advertentiegroep per stadscluster (groepeer 2–3 steden per advertentiegroep om het volume werkbaar te houden), locatietargeting ingesteld op een straal van 10 km rond elke stad, zoekwoorden: `"software ontwikkelaar [stad]"`, `"AI app bouwen [stad]"`, `"app developer [stad]"`. Start met Amsterdam, Rotterdam, Utrecht, Den Haag en Eindhoven als eerste 5 (hoogste bedrijfsdichtheid); voeg Groningen, Tilburg, Breda, Nijmegen en Enschede toe in week 4 als de eerste 5 signaal tonen.

**Dagbudget campagne: €8** (~€240/maand) — dit is een long-tail merk-halo-speel, geen volumedrijver; houd het goedkoop.

### 4.9. Accountbrede gedeelde lijst met uitsluitingszoekwoorden

`day`, `free`, `download`, `torrent`, `crack`, `jobs`, `salary`, `course`, `tutorial`, `definition`, `meaning`, `wikipedia`, `pdf`, `template`, `openai`, `chatgpt`, `internship`, `hiring` (als losstaande term). Toepassen op het niveau van de gedeelde bibliotheek, zodat dit automatisch wordt overgenomen door elke campagne, inclusief later toegevoegde campagnes.

**Totaal maandbudget Google Search: ~€5.040** — zie §9 voor hoe dit past binnen de totale kanaalmix per budgettier (de bovenstaande cijfers gaan uit van Tier 2 EN+NL gecombineerd; schaal proportioneel volgens §9).

---

## 5. Google Ads-advertentieteksten — Kant-en-klare RSA's

### 5.1. RSA voor `AG-BuildWithAI` / `AG-PrototypeToProd` (Cluster B, Engelstalig)

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

### 5.2. RSA voor `AG-SecureCore` / `AG-SecurityProblemAware` (Cluster C, Engelstalig)

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

### 5.3. RSA voor `LS-Search-NL-Core` (Nederlands)

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

## 6. LinkedIn Ads — Exacte Campagneopbouw

**Campaign Group:** `LaunchStudio – Founder Acquisition NL/Benelux`

### 6.1. Campagne 1 — `LI-Awareness-SponsoredContent`
- **Doel:** Website visits
- **Doelgroep — Functietitels (OF):** Founder, Co-Founder, Chief Executive Officer, Chief Technology Officer, Head of Product, Solo Founder
- **Bedrijfsgrootte:** Self-employed, 1–10, 11–50
- **Geografie:** Nederland (primair, 70% van budget), België + Luxemburg (secundair, 20%), bredere EU (tertiair, 10%)
- **Interesse-/vaardighedenlaag (indien voorraad het toelaat):** Startups, SaaS, Software Development, No-code Development
- **Biedstrategie:** Maximum Delivery gedurende de eerste 2 weken (volume nodig om te leren), overschakelen naar Cost Cap zodra er 50+ kliks zijn geregistreerd
- **Budget:** €30/dag (~€900/maand)
- **Creatief:** Single-image- of carrouseladvertentie — "5 tekenen dat je AI-prototype niet productieklaar is" → linkt naar de landingspagina met de productiegereedheidschecklist
- **Advertentietekst:** "Je hebt het in een weekend gebouwd met Lovable, Bolt of Cursor. Dit is wat de meeste oprichters missen voordat er echte gebruikers komen. Gratis checklist inbegrepen." + CTA-knop "Learn More"

### 6.2. Campagne 2 — `LI-Retargeting-Consideration` (activeren zodra de LinkedIn Insight Tag 500+ getagde bezoekers heeft)
- **Doel:** Conversions (Lead Gen Form of website-conversie)
- **Doelgroep:** Website-retargeting, vensters van 30/60/90 dagen, gecombineerd met hetzelfde functietitelfilter als Campagne 1
- **Budget:** €15/dag (~€450/maand)
- **Creatief:** Case-study-carrousel (echte resultaatcijfers, indien nodig geanonimiseerd) + een statische advertentie met een directe testimonial-quote
- **Advertentietekst:** "€2.800 en 9 dagen. Dat was alles wat [Case Study-oprichter] nodig had om van Lovable-prototype naar betalende klanten te gaan." + CTA "Get Your Free Estimate"

### 6.3. Campagne 3 — `LI-MessageAds` (Fase 2, zodra er een warme, betrokken doelgroep bestaat — niet eerder lanceren dan week 7)
- **Doelgroep:** Betrokken bij Campagnes 1–2 (geopend, geklikt, of >50% van de video bekeken) maar niet geconverteerd
- **Format:** Message Ads / Conversation Ads
- **Copy:** Kort, in de ik-vorm, afkomstig van een met naam genoemd LaunchStudio-teamlid — niet corporate. "Hoi {{firstName}}, ik zag dat je onze productiegereedheidsgids hebt bekeken. Wil je een gratis review van 15 minuten van je daadwerkelijke prototype? Geen verkooppraatje, gewoon een tweede mening." + CTA "Book 15 Min"
- **Budget:** €10/dag (~€300/maand)

**Totaal maandbudget LinkedIn: ~€1.650** (Fase 1: uitsluitend Campagne 1, ~€900/maand; Fase 2 voegt Campagnes 2–3 toe)

---

## 7. Meta Ads (Facebook + Instagram) — Exacte Campagneopbouw

*Niet eerder lanceren dan week 7 — heeft pixeldata van Search nodig om retargeting-/lookalike-doelgroepen op te bouwen (§10).*

### 7.1. Campagne 1 — `META-Prospecting`
- **Doel:** Traffic of Leads (test beide, kies de winnaar na 2 weken)
- **Advertentieset — Interessestack:** SaaS founders, Indie hackers, Startup entrepreneurship, Y Combinator (interesse), No-code development
- **Leeftijd:** 24–48 · **Geografie:** Nederland, België, bredere EU
- **Plaatsingen:** Instagram Reels + Facebook Feed (zet Audience Network- en Messenger-plaatsingen aanvankelijk uit — lagere kwaliteit voor dit aanbod)
- **Creatief:** verticale video van 15 seconden, echte voor/na-schermopname — rommelig Lovable-prototype → live productieapp met werkende betaalflow
- **Budget:** €20/dag (~€600/maand)

### 7.2. Campagne 2 — `META-Retargeting`
- **Doel:** Conversions
- **Advertentieset 1 (prioriteit):** Calculatorgebruikers die niet hebben ingediend, laatste 14 dagen
- **Advertentieset 2:** Alle websitebezoekers, laatste 30 dagen, exclusief Advertentieset 1
- **Creatief:** dynamische carrousel — pakket Launch Ready (€800–3.500) versus pakket Launch & Grow (€2.500–7.500), waarbij de specifieke dienst die de bezoeker heeft bekeken als eerste wordt getoond
- **Budget:** €25/dag (~€750/maand)

### 7.3. Campagne 3 — `META-Lookalike` (Fase 3, zodra er 100+ conversies bestaan)
- **Advertentieset:** 1% Lookalike (Nederland) opgebouwd vanuit een Custom Audience van geconverteerde klanten, gecombineerd met SaaS-/startupinteresse
- **Creatief:** testimonial-video-advertentie
- **Budget:** €15/dag (~€450/maand)

**Totaal maandbudget Meta: ~€1.800** (geleidelijk activeren, niet allemaal tegelijk)

---

## 8. X (Twitter), Reddit en Bing — Exacte Opbouw

### 8.1. X (Twitter) Ads
- **Campagnedoel:** Websiteklikken
- **Targeting:** Follower-lookalike op basis van de officiële Lovable-, Bolt.new-, Cursor- en v0/Vercel-accounts (controleer de exacte handles vóór lancering — deze veranderen), plus zoekwoordtargeting op tweets die "lovable" / "bolt.new" / "cursor ai" bevatten in combinatie met "security" / "backend" / "deploy" / "production"
- **Budget:** €10/dag (~€300/maand)
- **Kant-en-klare copy (3 varianten, wekelijks roteren):**
  1. "80% van de AI-gebouwde apps haalt nooit productie. Wij lossen de laatste 20% op — beveiliging, betalingen, hosting. Vaste prijs, 1–3 weken. [link]"
  2. "Je hebt in een weekend een hele app vibe-coded. Respect. Laten we er nu voor zorgen dat de data van je gebruikers niet lekt. [link]"
  3. "Lovable/Bolt/Cursor bracht je 80% van de weg. Wij regelen de saaie-maar-cruciale laatste loodjes. [link]"

### 8.2. Reddit Ads
- **Subreddits:** r/lovable, r/nocode, r/SaaS, r/startups, r/webdev, r/EntrepreneurRideAlong
- **Format:** tekst-/linkadvertenties opgemaakt als een native post, geen banner
- **Budget:** €8/dag (~€240/maand)
- **Kant-en-klare copy (2 varianten):**
  1. Titel: "Mijn SaaS gebouwd met Bolt in een weekend — dit ging kapot toen er echte gebruikers kwamen" → linkt naar een echte (of geanonimiseerde/samengestelde) case-study-blogpost, niet direct naar een verkooppagina
  2. Titel: "PSA: als je je app vibe-coded hebt, check deze 5 dingen vóór lancering" → linkt naar de productiegereedheidschecklist

### 8.3. Microsoft (Bing) Ads
- **Actie:** importeer de volledige campagnestructuur van `LS-Search-EN-*` en `LS-Search-NL-*` 1-op-1 met Bing's importtool voor Google Ads. Niet handmatig opnieuw opbouwen.
- **Aanpassingen na import:** voeg `torrent` en `crack` apart toe aan Bing's uitsluitingslijst (import neemt uitsluitingszoekwoorden niet altijd correct over — controleren), verlaag alle Max. CPC's als startpunt met ~30% (Bing-advertentieruimte is doorgaans goedkoper).
- **Budget:** €17/dag (~€500/maand)

---

## 9. Budgettiers — Concrete Eurocijfers

### Tier 1 — Lean (€2.500/maand)
| Kanaal | Maandelijks € | Dagelijks € |
|---|---|---|
| Google Search EN | €1.000 | €33 |
| Google Search NL | €500 | €17 |
| LinkedIn (uitsluitend Campagne 1) | €625 | €21 |
| Bing | €250 | €8 |
| Reddit | €125 | €4 |

### Tier 2 — Standaard (€5.000/maand) — *de standaard van dit document, gebruikt voor alle cijfers in §4–8*
| Kanaal | Maandelijks € |
|---|---|
| Google Search EN (§4.1–4.6) | €3.795 |
| Google Search NL (§4.7–4.8) | €1.240 |
| *(subtotaal EN+NL Search, geschaald om binnen de envelop van €5k te passen — zie onderstaande opmerking)* | |
| LinkedIn | €900 (uitsluitend Campagne 1 in Fase 1) |
| Bing | €500 |
| Reddit | €240 |

> **Opmerking bij de Tier 2-rekensom:** de dagbudgetten op advertentiegroepniveau in §4 tellen op tot meer dan een strikte verdeling van €5.000/maand (~€166/dag → ~€5.040/maand voor Search alleen, vóór LinkedIn/Bing/Reddit). Dat is bewust: de cijfers in §4 zijn de **beoogde eindstaat zodra Fase 1 zich heeft bewezen**, niet de dag-1-uitgave. **Start voor een daadwerkelijke Tier 2-lancering (totaal €5.000/maand) alle §4-campagnes op 60% van de vermelde dagbudgetten** en verhoog wekelijks naarmate er data binnenkomt. Dit voorkomt de grootste fout bij betaalde advertenties: elke advertentiegroep op dag 1 op volledig bod lanceren zonder conversiedata.

### Tier 3 — Agressief (€10.000/maand, alleen opschalen vanaf Fase 2+)
| Kanaal | Maandelijks € |
|---|---|
| Google Search EN+NL | €3.500 |
| LinkedIn (alle 3 campagnes) | €2.500 |
| Meta (alle 3 campagnes) | €1.800 |
| Bing | €1.000 |
| X | €700 |
| Reddit | €500 |

---

## 10. UTM-conventie (vanaf dag 1 afdwingen)

```
utm_source   = google | bing | linkedin | meta | twitter | reddit
utm_medium   = cpc
utm_campaign = {cluster}-{lang}-{phase}        e.g. security-en-phase1
utm_content  = {ad-group-or-creative-id}       e.g. rsa-v1, video-15s-v2, msg-ads-v1
utm_term     = {keyword}                       (Google/Bing dynamic keyword insertion only)
```

**Voorbeeld van live URL:**
`https://launchstudio.eu/en/from-prototype-to-production?utm_source=google&utm_medium=cpc&utm_campaign=production-en-phase1&utm_content=rsa-v1&utm_term={keyword}`

Houd één gedeeld UTM-trackingsheet bij (of gebruik de ingebouwde UTM-builder van elk platform), zodat campagnenamen in het advertentieplatform en `utm_campaign`-waarden altijd exact overeenkomen — afwijkingen hierin zijn de #1-oorzaak van kapotte attributierapportage later.

---

## 11. Landingspagina's — Content-outline (bouw deze 3 vóórdat er ook maar één euro wordt uitgegeven)

### 11.1. `/en/from-prototype-to-production` (verkeer van Cluster B + A)
- **H1:** Your AI Prototype Is 80% Done. We Handle the Other 20%.
- **Subhead:** Security, payments, database, hosting — fixed price, 1–3 weeks, your frontend untouched.
- **Sectie — The 6 things every AI prototype is missing:** (korte lijst: auth hardening, payment integration, database persistence, hosting/deployment, secrets management, rate limiting)
- **Sectie — How it works:** 3 stappen (describe → 15-min call → we build, you launch)
- **Sectie — Pricing snapshot:** €800–€7.500, link naar volledige calculator
- **Sectie — Case study / testimonial** (roteren per verkeersbron via URL-parameter indien haalbaar)
- **Sectie — FAQ:** 5 vraag-en-antwoordparen uit de bestaande FAQ-bank van de site, niet gedupliceerd uit een blogartikel
- **CTA (herhaald boven + onder):** "Get Your Free Project Estimate" → `#calculator`

### 11.2. `/en/ai-code-security-audit` (verkeer van Cluster C)
- **H1:** 45% of AI-Generated Code Has Security Vulnerabilities. Is Yours One of Them?
- **Subhead:** A fixed-price security review of your AI-built app, done in days.
- **Sectie — What we check:** auth, RLS, API key exposure, rate limiting, input validation
- **Sectie — Real vulnerability patterns we've found** (geanonimiseerde/samengestelde voorbeelden — verzin hier geen specifieke klantnamen)
- **Sectie — Pricing** en **CTA:** "Get a Free Security Review Quote"

### 11.3. `/nl/van-prototype-naar-productie` (Nederlandse spiegel van 11.1)
- Zelfde structuur als 11.1, **native in het Nederlands geschreven, niet machinaal vertaald** — hergebruik de toon van de RSA-copy uit §5.3 als stemreferentie:

- **H1:** Je AI-Prototype Is Voor 80% Klaar. Wij Regelen De Andere 20%.
- **Subhead:** Beveiliging, betalingen, database, hosting — vaste prijs, 1–3 weken, jouw frontend blijft ongewijzigd.
- **Sectie — De 6 dingen die elk AI-prototype mist:** (korte lijst: verharding van authenticatie, betalingsintegratie, database-persistentie, hosting/deployment, beheer van secrets, rate limiting)
- **Sectie — Hoe het werkt:** 3 stappen (beschrijf je situatie → gesprek van 15 minuten → wij bouwen, jij lanceert)
- **Sectie — Prijsoverzicht:** €800–€7.500, link naar de volledige calculator
- **Sectie — Case study / testimonial** (roteren per verkeersbron via URL-parameter indien haalbaar)
- **Sectie — FAQ:** 5 vraag-en-antwoordparen uit de bestaande FAQ-bank van de site, niet gedupliceerd uit een blogartikel
- **CTA (herhaald boven + onder):** "Vraag Je Gratis Projectinschatting Aan" → `#calculator`

---

## 12. KPI's (ongewijzigde doelen, nu gekoppeld aan het bovenstaande concrete budget)

| Metriek | Fase 1-doel | Opmerkingen |
|---|---|---|
| Kosten per gekwalificeerde lead | Baseline vaststellen in weken 1–2, optimaliseren vanaf week 3 | Beoordeel week 1 niet |
| Search-vertoningsaandeel (Cluster A/B) | >60% bij week 6 | Verhoog hieronder de biedingen richting de streefcijfers uit §4 |
| LinkedIn-CPA versus gemiddelde dealwaarde | CPA <15–20% van de gemiddelde projectwaarde | Meet op dealgrootte, niet op CPC |
| Conversieratio landingspagina | >3% | Herstel hieronder eerst de berichtmatch voordat het kanaal de schuld krijgt |

---

## 13. Week-voor-week uitvoeringschecklist (90 dagen)

| Week | Concrete taken |
|---|---|
| **1** | Installeer GA4 + definieer conversiegebeurtenissen (`calculator_complete`, `contact_form_submit`, `call_booked`). Installeer de Google Ads-conversietag, LinkedIn Insight Tag, Meta Pixel (+ Conversions API), X Pixel, Reddit Pixel. Bouw landingspagina's 11.1 en 11.2. Stel de gedeelde lijst met uitsluitingszoekwoorden in (§4.9). |
| **2** | Bouw alle `LS-Search-EN-*`-campagnes volgens §4.1–4.6 op 60% van de vermelde dagbudgetten. Bouw `LS-Search-NL-*` (§4.7) — laat de Nederlandse copy eerst door een native speaker nakijken. Lanceer LinkedIn Campagne 1 (§6.1). Lanceer Meta/X/PMax NOG NIET. |
| **3** | Dagelijkse biedmonitoring. Eerste zoektermenrapport ophalen — voeg eventuele nieuw gevonden uitsluitingszoekwoorden toe. Bouw en QA landingspagina 11.3 (Nederlands). |
| **4** | Lanceer `LS-Search-NL-Local` (§4.8) met de eerste 5 steden. Wekelijkse opschoning van zoektermen wordt vanaf nu een vaste taak. |
| **5** | Verhoog de dagbudgetten van elke advertentiegroep met een CPA onder het doel richting de volledige cijfers uit §4. Pauzeer/herstructureer elke advertentiegroep met nul conversies en >€150 besteed. |
| **6** | Lanceer de Bing-import (§8.3). Lanceer de Reddit-test (§8.2). |
| **7** | **Fase 1-evaluatie.** Vergelijk de daadwerkelijke CPA/CPL per campagne met de doelen uit §12. Stop of herstructureer onderpresteerders. Controleer of de LinkedIn-pixel 500+ getagde bezoekers heeft — zo ja, lanceer `LI-Retargeting-Consideration` (§6.2). Controleer of de Meta Pixel voldoende signaal heeft — zo ja, lanceer uitsluitend `META-Retargeting` (§7.2) (nog geen prospectie). |
| **8–9** | Monitor de CPA van Meta-retargeting. Indien gezond, voeg `META-Prospecting` (§7.1) toe. Lanceer de X-test (§8.1). |
| **10** | Eerste volledige maandelijkse cross-channel rapportage — kosten per gekwalificeerde lead per kanaal, niet alleen per klik. Herverdeel budget naar het kanaal dat wint op CPA, volgens de richting Tier 2→3 in §9. |
| **11** | Als het totaal aantal conversies 100+ bedraagt, zaai `META-Lookalike` (§7.3) en overweeg `LI-MessageAds` (§6.3) als de LinkedIn-CPA stand heeft gehouden. |
| **12–13** | Tweede volledige maandelijkse evaluatie. Besluit over de Performance Max-test — alleen als de retargetinglijst 1.000+ bezoekers uit de laatste 30 dagen heeft (PMax heeft dit minimale signaal nodig om te presteren; eerder lanceren verspilt budget aan koud leren). |

---

## 14. Risico's & opmerkingen

- **Risico van overschat volume:** het kopcijfer van "214.280/maand" in de CSV bestaat voor 94% uit één mismatch-term (§3.1). Alle cijfers in dit document gaan uit van de opgeschoonde basis van ~13.000/maand.
- **Nederlandstalige leemte:** nog steeds de leemte met de hoogste hefboomwerking. Laat, voordat §4.7–4.8 wordt opgeschaald tot boven het Tier 2-budget, een gedegen Nederlandstalig zoekwoordonderzoek uitvoeren (geen vertaling van de Engelse lijst) om de formuleringen te vangen waarop native speakers daadwerkelijk zoeken.
- **Dag-1-discipline:** de meest voorkomende manier waarop dit soort plannen in de praktijk mislukt, is elke campagne op dag 1 met het volledige streefbudget lanceren. Volg §13 — start op 60%, verhoog wekelijks op basis van data, niet ineens op basis van optimisme.
- **Attributie:** met 6 kanalen die vanaf week 9 draaien, stel een datagedreven of positiegebaseerd attributiemodel in GA4 in zodra het volume dit ondersteunt (doorgaans 300+ conversies/maand) — last-click zal X en Reddit structureel te weinig credit geven, aangezien deze kanalen bewustzijnswerk doen dat later via Search of direct verkeer converteert.
