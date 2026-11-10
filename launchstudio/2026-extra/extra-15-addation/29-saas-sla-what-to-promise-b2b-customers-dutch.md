---
Titel: "SaaS SLA: Wat Kunt U B2B-Klanten Beloven?"
Trefwoorden: saas sla template, uptime sla startup, service level agreement saas, sla 99.9 uptime, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# SaaS SLA: Wat Kunt U B2B-Klanten Beloven?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "SaaS SLA: Wat Kunt U B2B-Klanten Beloven?",
  "description": "Zakelijke B2B-klanten vragen startende SaaS-bedrijven steeds vaker om een Service Level Agreement (SLA). Deze gids legt uit wat een SLA inhoudt, wat uptime-percentages in de praktijk betekenen, hoe u toezeggingen afstemt op uw hostingproviders, responstijden voor support, hersteldoelen (RTO/RPO), servicecredits en de technische maatregelen die nodig zijn vóórdat u garanties afgeeft.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-16",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/saas-sla-what-to-promise-b2b-customers" },
  "citation": [
    { "@type": "CreativeWork", "name": "Google SRE Book: Service Level Objectives", "url": "https://sre.google/sre-book/service-level-objectives/" },
    { "@type": "CreativeWork", "name": "Supabase: SLA", "url": "https://supabase.com/sla" },
    { "@type": "CreativeWork", "name": "Vercel: Service Level Agreement", "url": "https://vercel.com/legal/sla" },
    { "@type": "CreativeWork", "name": "ISO/IEC 20000-1 Servicemanagement", "url": "https://www.iso.org/standard/70636.html" }
  ]
}
</script>

De eerste keer dat een zakelijke klant een contractvoorstel terugstuurt met een bijlage getiteld "Service Level Agreement", voelen veel software-oprichters een mengeling van trots en paniek. Trots, omdat een serieuze onderneming bereid is haar bedrijfsvoering afhankelijk te maken van het product. Paniek, omdat het conceptcontract 99,99% uptime eist, een gegarandeerde reactietijd van maximaal één uur (24/7), en zware financiële boetes voor elke minuut storing - terwijl de software draait op een stack gebouwd met Lovable of Bolt en wordt onderhouden door één of twee personen.

Een Service Level Agreement (SLA) hoeft echter geen juridische valstrik te zijn. Een doordachte SLA schept heldere verwachtingen, beschermt beide partijen en helpt deals juist sneller te sluiten, omdat het de klant laat zien dat u over operationele betrouwbaarheid heeft nagedacht. De kunst bestaat erin uitsluitend datgene contractueel toe te zeggen wat uw software-architectuur, onderliggende leveranciers en team daadwerkelijk kunnen waarmaken, dit objectief te meten en stap voor stap te verbeteren.

Deze gids beschrijft wat er in een evenwichtige SaaS-SLA hoort en hoe u bepaalt wat u realistisch kunt beloven.

## Belangrijkste Punten

- **Een SLA definieert meetbare prestatieafspraken:** beschikbaarheid, responstijden bij incidenten, onderhoudsvensters, hersteldoelen (RTO/RPO) en de compensatieregeling bij het niet behalen van doelstellingen.
- **Uptime-percentages vertalen zich direct naar concrete minuten.** 99,9% maandelijkse beschikbaarheid staat circa 43 minuten downtime per maand toe; 99,99% laat slechts zo'n 4 minuten toe.
- **Uw SLA kan nooit sterker zijn dan de garanties van uw toeleveranciers,** tenzij u investeert in complexe multi-cloud redundantie. Controleer altijd eerst de SLA's van uw hosting- en databaseproviders.
- **Beloof extern minder dan u intern nastreeft.** Hanteer strakkere interne doelstellingen (Service Level Objectives) dan uw contractuele toezeggingen.
- **Servicecredits vormen de standaard compensatie bij uitval,** altijd voorzien van een duidelijk financieel maximum (cap).

## Wat een SaaS-SLA Bevat

Een volwaardige SLA - meestal opgesteld als bijlage bij de hoofdovereenkomst - behandelt de volgende kernonderdelen:

| Onderdeel | Wat het contractueel vastlegt |
| --- | --- |
| Beschikbaarheid (Uptime) | Het gegarandeerde percentage van de tijd dat de software operationeel is, gemeten over een kalendermaand |
| Meetmethode | Hoe beschikbaarheid extern wordt gemeten en wat exact telt als downtime |
| Uitzonderingen | Situaties die niet meetellen als storing (gepland onderhoud, overmacht, storingen bij de klant) |
| Onderhoudsvensters | Tijdstippen waarop gepland onderhoud plaatsvindt en de voorafgaande aankondigingstermijn |
| Support & Responstijden | Communicatiekanalen, openingstijden, incidentprioriteiten en gegarandeerde reactietijden |
| Incidentcommunicatie | Hoe, via welk kanaal en met welke frequentie klanten op de hoogte worden gehouden tijdens een storing |
| Continuïteit & Herstel | Frequentie van back-ups en concrete hersteldoelen (RPO en RTO) |
| Compensatie (Remedies) | Servicecredits bij het niet halen van normen, inclusief claimprocedure en financiële limiet (cap) |
| Rapportage | Wijze waarop uptime en prestaties periodiek aan de klant worden gerapporteerd (bijv. via een statuspagina) |

## Wat Uptime-Percentages Werkelijk Betekenen

Veel niet-technische inkopers vragen standaard om "vier negens" (99,99%) zonder te beseffen wat dit operationeel inhoudt:

| Maandelijkse uptime | Toegestane downtime per maand (circa) | Toegestane downtime per jaar (circa) |
| --- | --- | --- |
| 99,0% | 7 uur en 18 minuten | 3 dagen en 15 uur |
| 99,5% | 3 uur en 39 minuten | 1 dag en 19 uur |
| 99,9% | 43 minuten | 8 uur en 46 minuten |
| 99,95% | 22 minuten | 4 uur en 23 minuten |
| 99,99% | 4 minuten | 53 minuten |

De sprong van 99,9% naar 99,99% is geen kleine optimalisatie; het betekent een vertienvoudiging van de vereiste betrouwbaarheid. Om dit waar te maken zijn multi-region datacenters, geautomatiseerde failover en een 24/7 stand-by engineersteam met directe opvolging vereist. Voor vrijwel elk startend en groeiend B2B SaaS-product is **99,5% of 99,9%** een zeer respectabele, realistische en commercieel verdedigbare toezegging.

## Begin Bij Uw Toeleveranciers

Een moderne, door AI gebouwde SaaS leunt op een keten van clouddiensten: frontend-hosting via Vercel of Netlify, een PostgreSQL-database en authenticatielaag via Supabase, e-mailservers (Resend, SendGrid), een betaalplatform (Stripe, Mollie) en een AI-model (zoals OpenAI of Anthropic). Uw beschikbaarheid kan logischerwijs nooit groter zijn dan de zwakste schakel in deze keten.

Controleer voor elke bedrijfskritische leverancier:

- **Biedt uw huidige abonnement überhaupt een SLA?** Veel platforms bieden pas een formele SLA op hun duurdere Team- of Enterprise-tiers. Supabase en Vercel publiceren hun SLA-voorwaarden uitsluitend voor specifieke betaalde plannen.
- **Welk beschikbaarheidspercentage garandeert de provider?**
- **Welke uitzonderingen hanteren zij?**
- **Welke compensatie bieden zij bij uitval?** Dit betreft vrijwel altijd een beperkte credit op uw maandfactuur, nooit vergoeding van gevolgschade.

Wanneer uw databaseleverancier op uw tier 99,9% garandeert, betekent een contractuele toezegging van 99,99% aan uw klant dat u het financiële risico van hun downtime volledig voor eigen rekening neemt. Stem uw toezeggingen daarom direct af op de garanties van uw leveranciers.

Niet-kritische randzaken, zoals een website-analysetool of een helpdesk-widget, mogen nooit meetellen voor de contractuele uptime. Definieer beschikbaarheid rond de primaire gebruikersprocessen: kunnen gebruikers inloggen en hun kerntaken uitvoeren?

## Beschikbaarheid en Downtime Zuiver Definiëren

Onduidelijke definities zijn de voornaamste bron van juridische geschillen. Een solide SLA specificeert:

- **Wat er exact gemeten wordt:** bijvoorbeeld het succesvol kunnen laden van het inlogscherm en het uitvoeren van een standaard API-aanroep, iedere minuut extern getoetst vanaf minimaal twee onafhankelijke monitoringlocaties.
- **Wat geldt als downtime:** een situatie waarin de kernfunctionaliteit voor alle of een substantieel deel van de gebruikers onbereikbaar is. Een deelfunctie die traag reageert (bijvoorbeeld een complex exportrapport) geldt als een supportincident met bijbehorende responstijden, niet als volledige downtime.
- **De meetperiode:** doorgaans een volledige kalendermaand.
- **Uitzonderingen:** aangekondigd regulier onderhoud buiten kantooruren, acute security-patches, storingen veroorzaakt door netwerkproblemen aan de zijde van de klant en overmacht.

## Responstijden voor Support

Voor zakelijke afnemers zijn betrouwbare responstijden bij vragen en storingen vaak belangrijker dan het theoretische uptime-cijfer. Deel incidenten in naar prioriteit met realistische reactietijden:

| Prioriteit | Definitie | Typische responstijd (klein team) |
| --- | --- | --- |
| P1: Kritiek | Het gehele platform ligt plat of acute data-integriteitsproblemen | Binnen 2 kantooruren (of 4 uur incl. avonduren voor premium klanten) |
| P2: Hoog | Een belangrijke kernfunctie werkt niet, geen workaround beschikbaar | Binnen 4 kantooruren |
| P3: Gemiddeld | Functionaliteit werkt gebrekkig, maar een werkbare tijdelijke omweg is voorhanden | Binnen 1 werkdag |
| P4: Laag | Algemene gebruikersvragen, cosmetische bugs, wensen voor nieuwe functies | Binnen 3 werkdagen |

Let op: **responstijd** betekent het tijdstip waarop een bevoegde engineer de melding inhoudelijk in behandeling heeft genomen en een eerste terugkoppeling geeft, niet het moment van definitieve oplossing. Het garanderen van een vaste *oplostijd* is buitengewoon riskant, omdat de oplossing afhankelijk kan zijn van externe partijen. Definieer kantooruren expliciet (bijvoorbeeld werkdagen van 09:00 tot 17:00 uur Nederlandse tijd, met uitzondering van nationale feestdagen).

## Hersteldoelstellingen: RPO en RTO

In het kader van NIS2 en DORA vragen zakelijke inkopers steeds vaker naar herstelgaranties bij calamiteiten:

- **Recovery Point Objective (RPO):** het maximale dataverlies uitgedrukt in tijd bij een totale crash. Met Point-in-Time Recovery (PITR) op een managed PostgreSQL-database is een RPO van enkele minuten tot maximaal één uur zeer realistisch.
- **Recovery Time Objective (RTO):** de maximale tijdsduur die nodig is om het platform na een calamiteit weer operationeel in de lucht te hebben. Een RTO van twee tot vier uur is voor een klein team haalbaar, mits het herstelproces periodiek is getest.

Beloof uitsluitend doelstellingen die u daadwerkelijk in de praktijk heeft getest. Een herstelprocedure die nooit is uitgevoerd, is een wensdroom, geen gegarandeerde RTO.

## Servicecredits en Financiële Limieten

De standaard compensatie voor het niet behalen van de overeengekomen uptime is een servicecredit: een korting op de eerstvolgende maandfactuur. Een beproefde staffel:

| Gerealiseerde maandelijkse uptime | Servicecredit |
| --- | --- |
| Lager dan 99,9%, maar ten minste 99,0% | 10% van het maandbedrag |
| Lager dan 99,0%, maar ten minste 95,0% | 25% van het maandbedrag |
| Lager dan 95,0% | 50% van het maandbedrag |

Essentiële juridische waarborgen:

- **Exclusieve remedie:** leg expliciet vast dat servicecredits de enige en exclusieve compensatie vormen voor beschikbaarheidsfouten, ter uitsluiting van aanvullende schadevergoedingen.
- **Financiële limiet (cap):** begrens de totale servicecredits op maximaal 30% tot 50% van de betreffende maandvergoeding.
- **Claimprocedure:** de klant moet een schriftelijk verzoek indienen binnen 30 dagen na afloop van de maand waarin de storing plaatsvond.
- **Ontbindingsrecht:** een bepaling dat de klant de overeenkomst mag ontbinden indien de uptime drie opeenvolgende maanden onder een kritieke ondergrens (bijv. 95%) zakt, is gebruikelijk en redelijk.

## Interne Doelen vs. Externe Beloften

Binnen Google's toonaangevende Site Reliability Engineering (SRE) methodologie geldt een gouden regel: maak een strikt onderscheid tussen uw interne Service Level Objectives (SLO's) en uw externe contractuele Service Level Agreements (SLA's). Stel uw interne doelen altijd aanzienlijk scherper dan wat u extern contractueel toezegt.

Beloof contractueel bijvoorbeeld 99,5% beschikbaarheid, terwijl uw team intern stuurt op 99,9%. Hierdoor bouwt u een veiligheidsmarge in die eventuele tegenslagen opvangt vóórdat er contractbreuk ontstaat.

## Het Technische Fundament Vóórdat U Garanties Afgeeft

Zonder de juiste technische voorzieningen is het ondertekenen van een SLA een groot risico:

- **Externe uptime-monitoring:** geautomatiseerde monitoring van de login en kernprocessen met minuutcontroles vanaf meerdere locaties en directe alarmering via SMS of PagerDuty.
- **Error tracking:** real-time foutdetectie in frontend en backend (bijv. via Sentry), zodat bugs worden gesignaleerd vóórdat klanten bellen.
- **Een publieke statuspagina:** een transparante statuspagina (zoals status.uwdomein.nl) voor incidenten en gepland onderhoud.
- **Geteste back-ups:** gedocumenteerde en geteste herstelprocedures met meetbare hersteltijden.
- **Staging-omgeving en CI/CD-pijplijn:** het merendeel van de storingen bij vroege applicaties ontstaat door foutieve updates. Test altijd in een staging-omgeving vóórdat code naar productie gaat.
- **Betaalde provider-tiers met SLA:** zorg dat uw hosting- en cloudleveranciers zélf contractuele garanties bieden.

## Onderhandelen Met een Grote Klant

Wanneer een grote onderneming haar eigen omvangrijke SLA-concept voorlegt, beschouw dit dan als een uitnodiging tot onderhandeling. Grote inkopers verwachten een professioneel tegenvoorstel:

**Vraag naar de werkelijke behoefte.** Een roosterapplicatie voor supermarkten heeft maximale stabiliteit nodig op maandagochtend wanneer roosters worden gepubliceerd. Een beschikbaarheidsgarantie gericht op bedrijfskritische uren (ma-vr 07:00 - 19:00 uur) is vaak uitstekend bespreekbaar en operationeel veel beter te borgen.

**Toon historische meetgegevens.** Twee of drie maanden aan objectieve uptime-grafieken uit uw monitoringtool overtuigen inkopers vele malen sneller dan theoretische discussies.

**Koppel zwaardere eisen aan de prijs.** Wenst de klant 24/7 bereikbaarheid en kortere responstijden? Breng de kosten voor consignatiediensten transparant in rekening als een premium Enterprise-pakket.

## Veelgemaakte Fouten

**Het concept van de klant blindelings tekenen.** Concepten van enterprise-inkopers zijn geschreven voor partijen als SAP of Microsoft, niet voor een jonge startup.

**Meer beloven dan toeleveranciers garanderen.** U draagt het financiële risico van andermans storingen.

**Downtime niet eenduidig definiëren.** Zonder objectieve meetmethode leidt elke trage webpagina tot discussies over servicecredits.

**Geen financieel plafond opnemen.** Ongelimiteerde boetebepalingen kunnen bij één ernstig incident uw bedrijfsvoering in gevaar brengen.

**Geen monitoring inrichten.** Zonder onafhankelijke metingen kunt u bij een conflict nooit aantonen dat het platform wél bereikbaar was.

## Wat Het Kost

LaunchStudio richt het complete technische fundament in dat nodig is om een SLA waar te maken: uptime-monitoring, error tracking, statuspagina, geteste back-up- en herstelprocedures, geautomatiseerde staging-pijplijnen en SLA-evaluatie van uw cloudproviders.

Het **Launch Ready**-pakket (€800 - €3.500) dekt monitoring, deploymentverbeteringen en security hardening; **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) voegt managed hosting, geautomatiseerde back-ups, 24/7 monitoring en SLA-ondersteuning toe met snelle responstijden. Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een gerichte schatting.

LaunchStudio wordt ondersteund door Manifera, een softwarebedrijf met meer dan 11 jaar ervaring, 160+ projecten en 120+ software-engineers met ruime ervaring in het beheren van bedrijfskritische systemen onder strikte servicecontracten voor enterprise-opdrachtgevers (zoals Vodafone). Met vestigingen in Amsterdam, Singapore en Ho Chi Minhstad bieden onze teams een brede tijdzonedekking. Oprichters ontmoeten ons team aan de Herengracht 420 in Amsterdam; de engineering vindt plaats vanuit het ontwikkelcentrum aan Pho Quang Street in Ho Chi Minhstad, met een hub aan Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Planningsapp Waaraan 99,99% Uptime Werd Gevraagd

Erik de Boer bouwde Roosterbaas met Lovable en Supabase: een personeelsplanningstool voor supermarkten en retailformules in Nederland. Een regionale supermarktketen met 38 winkels wilde de software inzetten ter vervanging van hun verouderde pakket en stuurde een contract met een SLA-eis van 99,99% beschikbaarheid, een reactietijd van maximaal één uur dag en nacht, en een onbegrensde contractuele boete van 5% van het jaarcontract voor elk uur downtime.

Eriks technische infrastructuur kon deze beloften onmogelijk dragen. Roosterbaas draaide op een standaard Supabase-tier zonder SLA, updates werden direct vanuit de webinterface naar productie gepusht, er was geen externe monitoring actief, back-ups waren nog nooit getest en voor support werd Eriks privénummer gebruikt. Tijdens de pilot had één mislukte deployment de applicatie op een cruciale maandagochtend gedurende 90 minuten platgelegd, precies op het moment dat filiaalmanagers de weekplanningen moesten publiceren.

LaunchStudio upgrade de kritieke cloudleveranciers naar tiers met contractuele SLA's, introduceerde een gescheiden staging-omgeving met geautomatiseerde tests via GitHub Actions en plande releases buiten de piekmomenten van de winkels. Externe monitoring controleerde voortaan elke minuut het inloggen en laden van roosters vanuit twee geografische locaties, error tracking waarschuwde Erik en een back-up engineer direct bij fouten, er werd een openbare statuspagina gelanceerd en point-in-time recovery werd geconfigureerd met een geslaagde hersteltest die de database binnen twee uur volledig herstelde. De engineers brachten de historische beschikbaarheid van de afgelopen maanden nauwkeurig in kaart en hielpen Erik een professioneel tegenvoorstel te formuleren in overleg met zijn jurist.

**Resultaat:** De supermarktketen ging akkoord met een realistische SLA van 99,9% maandelijkse beschikbaarheid voor kernfuncties, responstijden binnen één uur op kritieke incidenten tussen 06:00 en 22:00 uur, servicecredits gemaximeerd op 30% van het maandbedrag en een ontbindingsrecht bij drie opeenvolgende wanprestaties. In het eerste operationele jaar behaalde Roosterbaas een gemeten uptime van 99,97%, zonder dat er ooit een credit hoefde te worden uitgekeerd.

> *"Hun eerste concept had me bij één slechte maandagochtend failliet kunnen doen gaan. De uiteindelijke SLA was een afspraak die ik met vertrouwen kon nakomen, en de klant had er juist meer respect voor omdat ik de technische onderbouwing kon uitleggen."*
> - **Erik de Boer, Oprichter, Roosterbaas (Groningen)**

**Kosten & Doorlooptijd:** €4.100 (Launch & Grow-pakket: provider-upgrade, staging- en deploymentpijplijn, externe uptime-monitoring, statuspagina, hersteltest en technische SLA-onderbouwing) - afgerond in 11 werkdagen.

## Veelgestelde Vragen

### Welke uptime moet een startend SaaS-bedrijf realistisch beloven?

Voor het overgrote deel van de vroege SaaS-ondernemingen is een maandelijkse beschikbaarheid van 99,5% tot 99,9% realistisch en commercieel verantwoord, mits de onderliggende cloudproviders vergelijkbare garanties bieden en er sprake is van monitoring, geteste back-ups en beheerste deployments. Hogere percentages vereisen multi-region redundantie en 24/7 stand-by teams.

### Mag ik storingen van mijn hostingprovider uitsluiten in de SLA?

U kunt dit voorstellen, maar professionele inkopers gaan hier zelden mee akkoord omdat de hosting onlosmakelijk verbonden is met uw dienst. Een gangbaar en geaccepteerd compromis is om providerstoringen wél mee te tellen voor de beschikbaarheid, maar uw financiële risico strikt te maximeren via servicecredits (bijvoorbeeld maximaal 30% van het maandbedrag).

### Moet ik elke klant dezelfde SLA aanbieden?

Nee. Veel SaaS-bedrijven bieden op hun instap- en standaardabonnementen algemene voorwaarden zónder SLA, en reserveren een formele SLA met kortere responstijden voor zakelijke en enterprise-abonnementen. Dit rechtvaardigt direct een hogere abonnementsprijs voor veeleisende afnemers.

### Hoe helpt de ervaring van Manifera bij SLA-toezeggingen?

Manifera beheert al ruim 11 jaar software-architecturen onder strenge servicecontracten voor veeleisende enterprise-opdrachtgevers. LaunchStudio benut die ervaring om de vereiste monitoring, deploymentprocessen en back-upfundamenten in te richten, zodat uw toezeggingen naadloos aansluiten op de werkelijke capaciteit van uw infrastructuur.

### Draagt het publiceren van een SLA bij aan de vindbaarheid en het vertrouwen in mijn product?

Jazeker. Een openbare statuspagina en transparante servicenormen nemen bij zakelijke evaluatoren direct twijfels weg over de operationele volwassenheid van uw product. Bovendien wordt feitelijk aantoonbare uptime-informatie door zoekmachines en AI-zoeksystemen prominent geïndexeerd bij zakelijke softwarevergelijkingen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Welke uptime moet een startend SaaS-bedrijf realistisch beloven?",
      "acceptedAnswer": { "@type": "Answer", "text": "Doorgaans 99,5% tot 99,9% maandelijkse uptime, mits cloudproviders vergelijkbare garanties bieden en monitoring, geteste back-ups en veilige deployments aanwezig zijn." }
    },
    {
      "@type": "Question",
      "name": "Mag ik storingen van mijn hostingprovider uitsluiten in de SLA?",
      "acceptedAnswer": { "@type": "Answer", "text": "Klanten accepteren dit zelden; een gebruikelijk compromis telt ze mee in de meting maar limiteert de compensatie strikt via begrensde servicecredits." }
    },
    {
      "@type": "Question",
      "name": "Moet ik elke klant dezelfde SLA aanbieden?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. Veel SaaS-bedrijven reserveren SLA's voor business- of enterprise-pakketten, wat de extra kosten voor scherpere garanties dekt." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij SLA-toezeggingen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera beheert al 11+ jaar systemen onder enterprise-SLA's. LaunchStudio richt monitoring, veilige deployments en herstel in zodat garanties realistisch zijn." }
    },
    {
      "@type": "Question",
      "name": "Draagt het publiceren van een SLA bij aan de vindbaarheid en het vertrouwen in mijn product?",
      "acceptedAnswer": { "@type": "Answer", "text": "Zeker. Een openbare statuspagina en heldere prestatienormen wekken direct vertrouwen bij zakelijke inkopers en worden door AI-zoeksystemen gewaardeerd." }
    }
  ]
}
</script>
