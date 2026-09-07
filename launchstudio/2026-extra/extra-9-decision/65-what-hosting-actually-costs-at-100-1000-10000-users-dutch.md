---
Titel: "Wat hosting daadwerkelijk kost bij 100, 1.000 en 10.000 gebruikers"
Trefwoorden: SaaS hostingkosten, schalen van infrastructuurkosten, database hosting prijzen, hostingbudget indie hacker, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technisch Solo-Oprichter / Indie Hacker
---

# Wat hosting daadwerkelijk kost bij 100, 1.000 en 10.000 gebruikers

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wat hosting daadwerkelijk kost bij 100, 1.000 en 10.000 gebruikers",
  "description": "Een realistische uitsplitsing van maandelijkse infrastructuurkosten — hosting, database, opslag, e-mail, monitoring en AI API-uitgaven — over drie groeifasen, voor technische solo-oprichters die een lanceerbudget plannen.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/nl/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2027-01-13",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/what-hosting-actually-costs-at-100-1000-10000-users"
  }
}
</script>

Uw hostingfactuur bij 100 gebruikers: waarschijnlijk dicht bij de € 0. Uw hostingfactuur bij 10.000 gebruikers: zeer waarschijnlijk € 500 tot € 2.000 per maand. De sprong tussen die twee bedragen verloopt niet via een geleidelijke lijn — deze vindt plaats in een aantal specifieke stappen, bij concrete drempelwaarden. De meeste technische solo-oprichters ontdekken elke stap pas op het moment dat ze ertegenaan lopen, in plaats van erop te anticiperen. Dit artikel is geen rigide prijstabel, aangezien exacte bedragen afhangen van uw tech-stack, uw gebruikspatroon en tarieven die leveranciers regelmatig wijzigen. De vorm van de kostencurve en de specifieke posten die als eerste omhoogschieten zijn echter consistent genoeg om een realistisch budget omheen te plannen.

## Waarom er geen eenduidig antwoord is op 'Wat kost hosting?'

Het eerlijke uitgangspunt is dat hostingkosten niet bestaan uit één enkel bedrag, maar een optelsom zijn van verschillende onafhankelijke posten — compute (rekenkracht), database, bestandsopslag, uitgaande e-mail, foutmonitoring en, in toenemende mate, AI API-kosten als uw product een taalmodel aanroept. Elk van deze componenten schaalt in zijn eigen tempo en bereikt het plafond van het gratis instapniveau (free tier) op een ander moment. Een applicatie die hoofdzakelijk bestaat uit statische pagina's met licht databasegebruik blijft aanzienlijk langer goedkoop dan een product met intensieve bestandsuploads of een LLM-aanroep bij elke gebruikersactie, zelfs bij exact hetzelfde aantal gebruikers. Beschouw elk onderstaand bedrag als een typische bandbreedte voor een gangbare SaaS- of webapplicatie, niet als een garantie — de enige manier om uw exacte kosten te kennen is door uw verbruik vroegtijdig te meten en nauwlettend te volgen welke post als eerste in beweging komt wanneer echte gebruikers arriveren.

## Bij 100 gebruikers: gratis tiers dekken vrijwel alles

Bij circa 100 gebruikers met licht tot gemiddeld gebruik draaien de meeste moderne hosting-stacks volledig of nagenoeg volledig op gratis tiers. Frontend- en serverless hosting op platforms zoals Vercel of Netlify blijft bij dit volume doorgaans gratis. Een beheerde database op Supabase, Firebase of een vergelijkbare leverancier past vrijwel altijd binnen de gratis opslag- en rekencapaciteit, tenzij het product buitengewoon dataintensief is. Transactionele e-mail via Resend, Postmark of vergelijkbare diensten omvat meestal enkele duizenden gratis verzendingen per maand, wat registratiebevestigingen en notificaties op deze schaal ruimschoots dekt. Foutmonitoring via de gratis tier van Sentry vangt het foutvolume van een applicatie met weinig verkeer probleemloos op. Een realistisch totaal in deze fase is € 0 tot € 30 per maand. Oprichters die bij 100 gebruikers een aanzienlijk hogere factuur zien, kampen vrijwel altijd met een inefficiënt query-patroon dat databasecapaciteit verslindt of een AI API-aanroep die bij elke paginaweergave wordt uitgevoerd in plaats van alleen wanneer dit strikt noodzakelijk is.

## Bij 1.000 gebruikers: waar de eerste echte facturen verschijnen

Ergens tussen enkele honderden en een paar duizend gebruikers beginnen de gratis limieten te worden overschreden — meestal één voor één in plaats van allemaal tegelijk. Databasegebruik is vaak het eerste dat omslaat: zowel de datavolumes als de query-frequenties groeien mee met het aantal actieve gebruikers. De overstap naar een betaalde databasetier kost doorgaans tussen de € 20 en € 100 per maand, afhankelijk van de provider en hoeveel rekenkracht en opslag het product feitelijk vereist. E-mailvolumes passeren rond dit punt de gratis drempel voor producten met reguliere transactionele of notificatiemails, wat neerkomt op enkele tientallen euro's per maand. Foutmonitoring en logging-tools vereisen vaak een betaald abonnement zodra het volume van fouten en gebeurtenissen de gratis limieten overstijgt, doorgaans nog eens € 20 tot € 50 per maand. Hosting en rekenkracht zelf kunnen op serverless platforms nog steeds gratis of zeer goedkoop blijven als het verkeer schoksgewijs plaatsvindt, maar producten met continue achtergrondtaken of langdurige processen moeten hier vaak ook overschakelen naar een betaalde rekentier. Een realistisch totaal bij 1.000 actieve gebruikers ligt gewoonlijk tussen de € 100 en € 400 per maand, hoewel producten met zwaar verbruik hier aanzienlijk boven kunnen uitkomen.

## Bij 10.000 gebruikers: wat lineair schaalt versus wat stapsgewijs stijgt

Bij 10.000 gebruikers zijn de kosten definitief niet langer "grotendeels gratis met enkele kleine betaalde tiers", maar een serieuze, geplande maandelijkse kostenpost — doorgaans ergens tussen de € 500 en € 2.000 per maand voor een standaard SaaS-product. Dit bereik wordt aanzienlijk breder voor alles wat zware bestandsopslag, video of AI-aanroepen per interactie omvat. Wat in deze fase essentieel is om te begrijpen, is welke kosten min of meer lineair meegroeien met gebruikers en welke met abrupte sprongen omhooggaan. Databaserrekenkracht en opslag schalen over het algemeen nagenoeg lineair met het actieve datavolume, waardoor een oprichter dit vrij betrouwbaar kan voorspellen aan de hand van groeitrends. Hosting- en serverless-kosten kunnen daarentegen niet-lineair omhoogschieten als verkeerspatronen veranderen: een product dat overgaat van piekbelastingen naar een constante continue belasting kan een abrupte sprong in de hostingfactuur veroorzaken die in niets lijkt op een vloeiende groeicurve. Bestandsopslag en vooral bandbreedtekosten voor uitgaand dataverkeer (egress — de kosten voor data die het netwerk van de provider verlaat, wat vaak los van opslag wordt beprijsd en gemakkelijk wordt onderschat) kunnen uitgroeien tot een verrassend grote kostenpost voor applicaties die afbeeldingen, video's of grote downloads op schaal uitserveren.

## De kostenpost die oprichters vergeten: AI API-kosten

Voor producten met een AI-functionaliteit — een chatbot, een contentgenerator of een aanbevelingssysteem dat een LLM aanroept — verdienen de API-kosten een geheel eigen budgetpost. Dit gedraagt zich wezenlijk anders dan traditionele infrastructuurkosten: het schaalt rechtstreeks met het verbruik op een manier die gemakkelijk verkeerd wordt ingeschat, en de kosten per aanroep variëren enorm afhankelijk van het gekozen model en hoeveel context (tokens) er bij elk verzoek wordt meegestuurd. Een applicatie die één LLM-aanroep per gebruikerssessie uitvoert tegen bescheiden kosten lijkt bij 100 gebruikers nagenoeg gratis, maar kan bij 10.000 gebruikers uitgroeien tot de grootste kostenpost op de gehele begroting, zeker als de AI-functie een centrale rol speelt in de kernervaring. Deze kosten kennen bovendien op schaal geen noemenswaardige gratis tier zoals bij hosting of databases — de meeste AI API-providers factureren vanaf het allereerste token. Dit betekent dat een oprichter die een product bouwt met zwaar AI-verbruik in de kernlus, deze kosten vanaf het begin expliciet moet modelleren in plaats van verrast te worden door de eerste factuur na echte gebruikersgroei. Het cachen van herhaalde query's, het inzetten van kleinere modellen voor taken die geen topmodel vereisen en het instellen van harde verbruikslimieten per gebruiker zijn de beproefde methoden om deze uitgaven onder controle te houden.

## Keuzes voor hostingproviders die de kostencurve beïnvloeden

De specifieke leveranciers die u kiest, bepalen waar deze drempelwaarden liggen, soms aanzienlijk. Volledig beheerde platforms zoals Vercel of een beheerd Supabase-project ruilen een steilere kostencurve op schaal in voor nagenoeg nul configuratie- en onderhoudsinspanning — u betaalt meer per verbruikseenheid, maar besteedt vrijwel geen engineeringtijd aan infrastructuurbeheer. Zelfbeheerde infrastructuur op een provider zoals DigitalOcean, Hetzner of een kale AWS/Azure-omgeving kan per eenheid rekenkracht en opslag bij grotere volumes aanzienlijk goedkoper zijn. Dit verschuift echter aanzienlijke doorlopende engineeringtijd naar de oprichter om servers te configureren, beveiligen en patchen — tijd die een reële prijs heeft, zelfs wanneer deze niet direct op een hostingfactuur verschijnt. Voor een solo-oprichter zonder toegewijde DevOps-capaciteit is de hogere eenheidsprijs van een beheerd platform vaak de juiste economische afweging, zelfs wanneer de rekening begint op te lopen: het alternatief is immers niet gratis, maar wordt betaald in uren in plaats van euro's. Die uren zijn doorgaans veel waardevoller wanneer ze in het product zelf worden gestoken, totdat er een concrete reden is — aanhoudend hoog volume of een structurele kostenpost die te pijnlijk wordt — om de complexiteit van zelfbeheer op zich te nemen.

## Verborgen kosten: egress, back-ups en support-tiers

Verschillende kostencategorieën worden gemakkelijk over het hoofd gezien wanneer men budgetteert op basis van de openbare tarievenpagina van een provider. Bandbreedte-egress — de kosten van data die het datacenter van de hosting- of opslagprovider verlaat — wordt vaak apart berekend en kan aanzienlijk oplopen voor producten die media of downloads aanbieden. Dit getal staat zelden prominent vermeld in prijsvergelijkingen. Automatische back-ups, met name voor databases, kosten soms extra bovenop de standaard databasetier; het overslaan hiervan om een bescheiden maandelijks bedrag te besparen is een gevaarlijke vorm van valse zuinigheid vergeleken met de kosten van daadwerkelijk dataverlies. Upgrades naar betaalde support-tiers — de overstap van communityforums naar gegarandeerde reactietijden — worden relevant zodra het product substantiële omzet draait en downtime direct geld kost. Dit is echter een optionele post die de meeste oprichters kunnen uitstellen totdat ze daadwerkelijk een keer snelle ondersteuning hebben gemist.

## Een realistisch infrastructuurbudget voor 12 maanden opstellen

De praktische oefening die de moeite waard is vóór de lancering, is niet het zoeken naar één exact getal, maar het bouwen van een eenvoudig model: schat uw kostenposten (rekenkracht, database, opslag, e-mail, monitoring en eventueel AI API) in bij uw huidige of verwachte gebruikersaantal, schat ze vervolgens opnieuw in bij een vertienvoudiging (10x), en analyseer welke posten het hardst stijgen. Die vergelijking toont u waar u later kostenoptimalisaties moet doorvoeren en, belangrijker nog, of uw huidige verdienmodel de infrastructuurkosten per gebruiker wel dekt naarmate u schaalt. Een product dat € 10 per maand per gebruiker rekent met een infrastructuurkost van € 3 per gebruiker bij 10.000 gebruikers kent een volstrekt andere unit economics dan een product waar die infrastructuurkost € 0,30 bedraagt. Door dit model elke paar maanden te herijken aan de hand van actuele gebruiksdata, voorkomt u dat de hostingfactuur van een groeiend product een onaangename verrassing wordt in plaats van een voorspelbare post.

## Stel budgetwaarschuwingen in in plaats van handmatig controleren

Het laatste praktische onderdeel hiervan is operationeel in plaats van analytisch: vrijwel elke hosting-, database- en API-provider biedt budget- of verbruikswaarschuwingen, en vrijwel geen enkele solo-oprichter stelt deze in totdat een factuur hen al een keer onaangenaam heeft verrast. Het configureren van een alert op bijvoorbeeld 50% en 90% van een acceptabel maandelijks plafond kost slechts enkele minuten per dienst. Het transformeert een mogelijke schok aan het einde van de maand in een vroegtijdige waarschuwing met voldoende tijd om in te grijpen — of die reactie nu bestaat uit het optimaliseren van een query, het toevoegen van een caching-laag of simpelweg de conclusie dat de groei die de kosten drijft het geld dubbel en dwars waard is. Dit is een kleine configuratietaak die makkelijk naar de achtergrond verdwijnt zolang een product klein en goedkoop draait, en dat is precies de reden waarom het moet gebeuren terwijl het nog klein en goedkoop is.

Het Launch & Grow-pakket van [LaunchStudio](https://launchstudio.eu/nl/#calculator) omvat beheerde hosting, uptime-monitoring en automatische back-ups, specifiek zodat solo-oprichters deze infrastructuurplanning niet alleen hoeven uit te voeren. Hierbij putten we uit de ervaring met productie-infrastructuur van [Manifera](https://www.manifera.com/about-us/manifera-technologies/) opgebouwd over meer dan 160 opgeleverde projecten.

[Beschrijf uw project en ontvang binnen één werkdag een realistische inschatting van uw infrastructuurkosten](https://launchstudio.eu/nl/#contact) — vóórdat u moet gissen naar wat een vertienvoudiging van uw gebruikersaantal u werkelijk gaat kosten.

## Praktijkvoorbeeld

### Een technisch solo-oprichter in actie: De factuur die van de ene op de andere dag verdrievoudigde

Sander Willems, een indie hacker die Notarize bouwde — een tool voor digitaal ondertekenen van documenten voor kleine Nederlandse bedrijven met behulp van Cursor en een zelfbeheerde backend — zag zijn maandelijkse hostingfactuur in één facturatiecyclus omhoogschieten van circa € 40 naar meer dan € 300 nadat een nieuwe functionaliteit leidde tot een forse piek in bestandsuploads. Hij had weliswaar gebudgetteerd voor database- en rekencapaciteit, maar had bandbreedte-egress niet als een afzonderlijke post meegenomen. De kosten voor gebruikers die hun ondertekende documenten downloaden — vaak bestanden van meerdere megabytes die herhaaldelijk werden gedownload — bleken de werkelijke boosdoener, niet de opslag of database die hij nauwlettend volgde.

Een infrastructuuraudit door LaunchStudio bracht aan het licht dat Notarize elke documentdownload rechtstreeks vanuit de opslagbucket bij de database uitserveerde tegen het volle bandbreedtetarief, in plaats van via een CDN-laag die herhaalde downloads buffert en de egress-kosten substantieel verlaagt. De oplossing vereiste geen groter budget — het vereiste het routeren van de documentlevering via een correct geconfigureerd CDN, een stap die de meeste AI-ondersteunde setups overslaan omdat het een infrastructuurbeslissing is en geen softwarefeature.

**Resultaat:** Het toevoegen van een CDN-laag voor documentlevering verlaagde de maandelijkse bandbreedtekosten van Notarize binnen de allereerste facturatiecyclus met meer dan de helft, zonder enige wijziging aan het product zelf of een enkele regel klantgerichte code.

> *"Ik hield mijn databaserekening nauwlettend in de gaten en miste volledig dat bandbreedte juist de boosdoener was die explodeerde. Niemand vertelt je dat data-egress een eigen budgetpost is totdat je naar een factuur staart die in niets lijkt op wat je verwachtte."*
> — **Sander Willems, Oprichter, Notarize (Groningen)**

**Kosten & Doorlooptijd:** € 1.100 (gerichte infrastructuuraudit en CDN-configuratie) — opgelost in 5 werkdagen.

---

## Veelgestelde Vragen

### Bij welk aantal gebruikers moet ik stoppen met vertrouwen op gratis hosting-tiers?

Er is geen vast getal — het hangt af van de gebruiksintensiteit per gebruiker — maar de meeste oprichters zien de eerste gratis limiet bereikt worden tussen enkele honderden en een paar duizend actieve gebruikers, meestal op database- of e-mailvolume nog vóór rekenkracht een knelpunt wordt.

### Is zelfbeheerde infrastructuur daadwerkelijk goedkoper dan een beheerd platform zoals Vercel of Supabase?

Per eenheid rekenkracht en opslag vaak wel bij grotere volumes, maar in de vergelijking moet de benodigde engineeringtijd voor configuratie, beveiliging en onderhoud worden meegenomen. Dat zijn reële kosten, ook al verschijnen ze niet rechtstreeks op een factuur.

### Hoe schat ik AI API-kosten in voordat ik echte gebruiksdata heb?

Schat een ruw aantal AI-aanroepen per actieve gebruiker per maand, vermenigvuldig dit met de kosten per aanroep voor uw gekozen model, en bouw vanaf dag één caching en gebruikslimieten in. Deze post schaalt recht evenredig met gebruik en kent geen substantiële gratis tier bij reële volumes.

### Wat is de meest onderschatte hostingkostenpost?

Bandbreedte-egress (uitgaand dataverkeer), met name voor producten die bestanden, afbeeldingen of video's leveren. Dit wordt apart van opslag gefactureerd en staat zelden prominent vermeld op de tarievenpagina van een provider.

### Dekt het Launch & Grow-pakket van LaunchStudio doorlopende hostingkosten, of alleen de initiële inrichting?

Het omvat beheerde hosting, SSL, uptime-monitoring en automatische back-ups voor € 49 per maand bovenop het vaste instaptarief. Dit dekt het doorlopende infrastructuurbeheer af in plaats van louter een eenmalige inrichting.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Bij welk aantal gebruikers moet ik stoppen met vertrouwen op gratis hosting-tiers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Er is geen vast getal aangezien dit afhangt van de gebruiksintensiteit per gebruiker, maar de meeste oprichters bereiken de eerste gratis limiet tussen enkele honderden en een paar duizend actieve gebruikers, meestal op database- of e-mailvolume nog vóór rekenkracht."
      }
    },
    {
      "@type": "Question",
      "name": "Is zelfbeheerde infrastructuur daadwerkelijk goedkoper dan een beheerd platform zoals Vercel of Supabase?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Per eenheid rekenkracht en opslag vaak wel bij hogere volumes, maar de vergelijking moet ook de engineeringtijd omvatten voor configuratie, beveiliging en onderhoud, wat reële kosten zijn."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe schat ik AI API-kosten in voordat ik echte gebruiksdata heb?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Schat een ruw aantal AI-aanroepen per actieve gebruiker per maand, vermenigvuldig met de kosten per aanroep voor uw model, en bouw vanaf de start caching of limieten in, aangezien deze post direct met verbruik meeschaalt."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de meest onderschatte hostingkostenpost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Bandbreedte-egress, met name voor producten die bestanden, afbeeldingen of video's serveren, omdat dit los van opslag wordt beprijsd en zelden prominent op tarievenpagina's staat."
      }
    },
    {
      "@type": "Question",
      "name": "Dekt het Launch & Grow-pakket van LaunchStudio doorlopende hostingkosten, of alleen de initiële inrichting?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het omvat beheerde hosting, SSL, uptime-monitoring en automatische back-ups voor € 49 per maand bovenop de vaste setup fee, waarmee doorlopend infrastructuurbeheer wordt gedekt."
      }
    }
  ]
}
</script>
