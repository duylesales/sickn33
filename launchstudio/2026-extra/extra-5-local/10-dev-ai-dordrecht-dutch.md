---
Titel: "Dev AI-tools in Dordrecht: De kloof tussen prototype en productie dichten"
Trefwoorden: dev ai, ai dev tools, production readiness, hosting infrastructure, Dordrecht
Koperfase: Overweging
Doelgroep: Technische solo-oprichter
---
# Dev AI-tools in Dordrecht: De kloof tussen prototype en productie dichten

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Dev AI-tools in Dordrecht: De kloof tussen prototype en productie dichten",
  "description": "Een kostenoverzicht van wat het daadwerkelijk kost voor Dordtse oprichters die dev AI-tools gebruiken om van een werkend prototype naar een betrouwbaar productieproduct te gaan.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-23",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/dev-ai-dordrecht" }
}
</script>

Wat kost het daadwerkelijk om een door dev AI gegenereerd prototype om te zetten in iets dat betrouwbaar online blijft? Voor een oprichter in Dordrecht, de oudste stad van Nederland, gelegen op het samenvloeiingspunt van drie rivieren en historisch gebouwd op handel die via haar waterwegen liep, is die vraag niet abstract — het is het verschil tussen een product dat stilletjes uitvalt tijdens het drukste uur van een klant en een product dat dat niet doet.

## Wat dev AI-tools u opleveren, in euro's uitgedrukt

Tools zoals Lovable, Bolt, Cursor en v0 — breed gezegd, dev AI-tools — hebben de kosten van het bouwen van een eerste versie van een product drastisch verlaagd. Wat vroeger een ontwikkelteam en tienduizenden euro's vereiste, kan nu door een enkele oprichter worden geprototypet voor de prijs van een abonnement. Dat is een echte, goed gedocumenteerde verschuiving. Wat deze tools niet verlagen, zijn de kosten om dat product betrouwbaar te laten draaien zodra het echte gebruikers heeft — hosting die schaalt, monitoring die problemen opvangt vóór klanten dat doen, en een deploymentproces dat geen handmatige tussenkomst vereist bij elke wijziging.

De economie van Dordrecht is altijd gevormd door haar geografie — historisch een belangrijke binnenlandse handelshaven, en vandaag nog steeds thuisbasis van een aanzienlijke concentratie logistieke, scheepvaart- en maritiem-gerelateerde bedrijven die werken langs de waterwegen die de stad verbinden met Rotterdam en verder. Oprichters die hier tools bouwen voor die sector erven een klantenbasis die draait op uptime: een planning- of trackingtool die uitvalt tijdens een verzendvenster is geen klein ongemak, het is een operationeel probleem voor de klant die het gebruikt.

## Een kostenoverzicht: prototype versus productie

Hier is ruwweg wat een dev-AI-prototype scheidt van een productieklaar product, in termen van wat er daadwerkelijk gebouwd moet worden:

- **Hosting die schaalt:** Een enkele niet-schalende serverinstantie, gebruikelijk in standaard dev-AI-deployments, kost doorgaans weinig maar valt om bij elke echte verkeerspiek. Correcte auto-scaling-infrastructuur is een eenmalige opzetkost, geen grote terugkerende kost.
- **Monitoring en alerting:** Zonder dit horen oprichters over storingen via klanten. Met dit systeem koopt een kleine opzetkost vroegtijdige waarschuwing voordat een klein probleem een groot probleem wordt.
- **Een echte deploymentpijplijn:** Handmatige deploys zijn gratis totdat de eerste slechte deploy downtime veroorzaakt; een correcte CI/CD-pijplijn is een bescheiden vaste kost die dat risico permanent wegneemt.
- **Databaseveerkracht:** Back-ups en failover zijn niet zichtbaar in een demo, maar ze zijn het verschil tussen een slechte dag en een bedrijfsbeëindigend gegevensverlies.

Zoals Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera, het heeft verwoord: "De uitdaging is niet langer het omzetten van goede ideeën in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot volwassenheid te brengen." Voor een Dordtse oprichter die logistieke en scheepvaartklanten bedient die uptime als basisvereiste verwachten, is dat architectuurwerk geen optionele poets — het is het daadwerkelijke product.

De prijzen van LaunchStudio voor dit soort productiegereedheidswerk lopen van € 800 tot € 7.500 als vaste omvang, ruwweg een vijfde van wat een traditioneel ontwikkelbureau zou rekenen voor dezelfde infrastructuuropbouw. LaunchStudio wordt mogelijk gemaakt door Manifera, met een klantgericht kantoor aan de Herengracht 420 in Amsterdam en meer dan 160 opgeleverde projecten, waaronder werk voor klanten zoals Statler BI en Maployer. U kunt [rechtstreeks contact opnemen](https://launchstudio.eu/en/#contact) om te bepalen wat uw specifieke kloof tussen prototype en productie zou kosten, en het werk in [webapplicatieontwikkeling](https://www.manifera.com/services/web-app-develop/) van Manifera toont dezelfde infrastructuurdiscipline toegepast bij klanten van verschillende omvang.

## Echt voorbeeld

### Een AI-native oprichter in actie: de single-instance-storing van Dockflow

Eva Mulder bouwde Dockflow in Dordrecht met Lovable — een tool voor ligplaatsplanning en vrachtoverdrachtcoördinatie voor kleine scheepvaartagenten die werken langs de rivieren rond de stad. Het werd zonder problemen gelanceerd en haalde binnen de eerste twee maanden vier regionale scheepvaartagenten binnen als vroege gebruikers, gehost op een enkele niet-schalende serverinstantie die tijdens het testen goed had gewerkt.

Tijdens een week met ongewoon druk scheepvaartverkeer bereikte de server zijn resourcelimiet en viel vier uur uit zonder enige waarschuwing — er was geen monitoring ingesteld, dus Eva kwam erachter toen twee agenten belden om te vragen waarom ze hun ligplaatsschema's niet konden bereiken tijdens een operatie. Er was ook geen deploymentpijplijn, wat betekende dat de noodoplossing die ze pushte om de server weer online te krijgen, handmatig en live moest worden uitgevoerd, zonder enige teststap ertussen.

**Resultaat:** LaunchStudio verplaatste Dockflow naar auto-scaling-infrastructuur, voegde uptime-monitoring toe met realtime meldingen, en bouwde een CI/CD-pijplijn met een staging-omgeving, en het product heeft in de vier maanden sindsdien geen enkele ongeplande downtime meer gehad.

> *"Vier uur klinkt niet als veel totdat het vier uur is tijdens een echt verzendvenster, en twee klanten je tegelijk bellen."*
> — **Eva Mulder, oprichter, Dockflow (Dordrecht)**

**Kosten en tijdlijn:** € 1.850 (migratie naar auto-scaling, opzetten van monitoring, CI/CD-pijplijn) — voltooid in 6 werkdagen.

---

## Veelgestelde vragen

### Hoeveel kost het doorgaans om de kloof tussen prototype en productie te dichten?

De meeste projecten vallen binnen het vaste prijsbereik van € 800–€ 7.500 van LaunchStudio, afhankelijk van de omvang, wat ruwweg een vijfde is van traditionele bureauprijzen voor vergelijkbaar infrastructuurwerk.

### Is Dordrecht een te kleine markt voor dit soort toegewijd productiewerk?

Nee. LaunchStudio werkt met oprichters in heel Nederland en de Benelux, ongeacht de grootte van de stad, en de logistiekgerichte bedrijvenbasis van Dordrecht is een sterke match voor het hier beschreven uptime-gerichte werk.

### Wat bedoelde Herre Roelevink met architectuur als de echte uitdaging nu?

Hij beschrijft een verschuiving waarbij AI-tools het probleem van het snel bouwen van software hebben opgelost, waardoor het moeilijkere, minder zichtbare werk — beveiliging en productiearchitectuur — bepaalt of een product overleeft.

### Is er doorlopende ondersteuning na de initiële productiereparatie, of is het een eenmalig traject?

LaunchStudio biedt een optionele doorlopende ondersteuningsadd-on van € 49/maand voor oprichters die voortgezette monitoring en onderhoud willen na afronding van het initiële productiegereedheidswerk.

### Wie bouwt deze infrastructuur eigenlijk — wordt dit uitbesteed aan willekeurige contractanten?

Nee. Het wordt gebouwd door het interne technische team van Manifera van meer dan 120 engineers, hetzelfde team achter meer dan 160 opgeleverde projecten voor zakelijke klanten waaronder Vodafone, TNO en Statler BI.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "How much does closing the prototype-to-production gap typically cost?", "acceptedAnswer": { "@type": "Answer", "text": "Most projects fall within LaunchStudio's €800–€7,500 fixed-price range, roughly a fifth of traditional agency pricing." } },
    { "@type": "Question", "name": "Is Dordrecht too small a market for this kind of dedicated production work?", "acceptedAnswer": { "@type": "Answer", "text": "No. LaunchStudio works with founders across the Netherlands and Benelux regardless of city size, and Dordrecht's logistics-heavy base is a strong fit for uptime-focused work." } },
    { "@type": "Question", "name": "What did Herre Roelevink mean about architecture being the real challenge now?", "acceptedAnswer": { "@type": "Answer", "text": "He's describing a shift where AI tools have solved building software quickly, leaving security and production architecture as what actually determines if a product survives." } },
    { "@type": "Question", "name": "Is there ongoing support after the initial production fix, or is it a one-time engagement?", "acceptedAnswer": { "@type": "Answer", "text": "LaunchStudio offers an optional ongoing support add-on at €49/month for continued monitoring and maintenance." } },
    { "@type": "Question", "name": "Who is actually building this infrastructure — is it outsourced to random contractors?", "acceptedAnswer": { "@type": "Answer", "text": "It's built by Manifera's in-house engineering team of 120+ engineers, behind 160+ delivered projects for clients including Vodafone, TNO, and Statler BI." } }
  ]
}
</script>
