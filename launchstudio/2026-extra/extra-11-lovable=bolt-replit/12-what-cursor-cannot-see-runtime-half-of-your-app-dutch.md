---
Titel: "Cursor kan de runtime-helft van je app niet zien"
Trefwoorden: Cursor, ai code review limieten, runtime fouten productie, observability klein product, ai app beveiliging, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Cursor kan de runtime-helft van je app niet zien

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cursor kan de runtime-helft van je app niet zien",
  "description": "Een AI-code-editor redeneert over code die het kan lezen. Productiefouten ontstaan door configuratie, concurrency, datastatus en gedrag van derden dat de editor niet kan zien. Wat dit praktisch betekent en de minimale observability die een klein product nodig heeft.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-14",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/what-cursor-cannot-see-runtime-half-of-your-app" }
}
</script>

Je code-editor heeft elk bestand in je project gelezen. Hij kan elke functie aan je uitleggen, refactorings doorvoeren over de hele codebase en vragen beantwoorden over hoe alle onderdelen met elkaar verbonden zijn. Het is dus logisch om te veronderstellen dat als er iets ernstig mis zou zijn, de editor dat wel had gemeld.

Dat doet hij niet, en de reden daarvoor is geen beperking van het onderliggende AI-model. De reden is dat ongeveer de helft van wat jouw applicatie daadwerkelijk *is*, simpelweg niet in je git-repository bestaat. Configuratie leeft in het dashboard van je hostingprovider. Toegangsregels leven in een database. Status en records leven in rijen die zijn aangemaakt door gebruikers die je nog nooit hebt ontmoet. En het gedrag van je app hangt af van het antwoord van een betaalprovider om 03:00 uur op zondagochtend. Niets daarvan is tekst die Cursor kan lezen, terwijl vrijwel alle productie-incidenten precies daar ontstaan.

## De twee helften, helder benoemd

**De statische helft** is je broncode: logica, structuur, dependencies, types. AI-editors zijn hier uitzonderlijk goed in - het signaleren van inconsistenties, voorstellen doen voor refactoring, een vergeten null-check opvangen en onbekende code sneller uitleggen dan je het zelf kunt lezen.

**De runtime-helft** is alles wat pas bestaat zodra de app daadwerkelijk draait op echte infrastructuur met echte gebruikers. Omgevingsvariabelen en hun actuele waarden. Toegangsbeleid van databases. Netwerkgrenzen en welke service met welke andere service mag communiceren. Gegevens die patronen hebben aangenomen die niemand vooraf had ontworpen. Concurrency en gelijktijdige requests. Externe API-koppelingen van derden met hun eigen kuren en downtimes.

Een AI-editor redeneert met veel verstand over de eerste helft, maar heeft structureel gezien nul zicht op de tweede helft.

## Vier fouten die alleen tijdens runtime bestaan

**De correcte code met de verkeerde configuratie.** Je betaalintegratie is feilloos geïmplementeerd, maar verwijst naar een test-endpoint. Of je database-client is perfect opgezet, maar maakt verbinding met een project in een verkeerde cloudregio. De code doorstaat elke review omdat de code zelf vlekkeloos is. De waarde die hij uitleest, bevindt zich echter op een heel andere plek.

**De race condition.** Twee gebruikers reserveren binnen dezelfde seconde het allerlaatste beschikbare tijdslot. Als je de boekingsfunctie doorleest, klopt de logica ogenschijnlijk helemaal: controleer eerst de beschikbaarheid en schrijf vervolgens de boeking weg. In runtime gebeuren beide controles echter vóórdat een van beide wegschrijvingen is afgerond. Het resultaat: je hebt exact dezelfde stoel twee keer verkocht. Er staat geen enkele syntax- of logicafout in het bestand; de fout zit puur in de gelijktijdige afhandeling van processen.

**De data-vormige bug.** Je rapportagefunctie werkt vlekkeloos voor elk testrecord dat je handmatig hebt aangemaakt. Maar dan voert een echte gebruiker een naam in met een apostrof, een bestelhoeveelheid van nul, of een geboortedatum uit 1970, en een query retourneert plotseling een absurde fout. De code kan alleen overweg met de data waarvoor hij is geschreven - en dat was de ideale data die jij in je hoofd had.

**De verrassing van een externe partij.** Een externe provider retourneert een statuscode die je tijdens de ontwikkelingsfase nooit bent tegengekomen, heeft een time-out halverwege een verzoek, of wijzigt stilletjes de structuur van een JSON-respons in een tussenversie. Je integratie klopt exact volgens de officiële documentatie, maar faalt tegen de daadwerkelijke werkelijkheid.

Hoe vaak je de repository ook laat scannen: geen enkele analyse brengt dit aan het licht, simpelweg omdat het probleem zich niet in de code bevindt.

## Waarom vloeiendheid aanvoelt als correctheid

Er zit een psychologische dimensie aan dit probleem die benoemd moet worden, omdat het zowel ervaren ontwikkelaars als beginners beïnvloedt.

Code die is geschreven of beoordeeld door een capabele AI-assistent leest soepel. De code is idiomatisch, consistent geformatteerd, logisch gestructureerd en draait meestal direct bij de eerste poging. Die combinatie genereert een krachtig betrouwbaarheidssignaal dat je brein in de loop der jaren heeft leren vertrouwen - historisch gezien betekende code die er zó coherent uitzag meestal dat er grondig over was nagedacht.

Die correlatie gaat vandaag de dag niet meer op. Vloeiendheid is tegenwoordig goedkoop; daadwerkelijke correctheid is dat niet. En de kloof tussen die twee is precies waar productie-incidenten ontstaan. De praktische implicatie is niet dat je het gereedschap moet wantrouwen. Het betekent dat je moet stoppen met het behandelen van "het ziet er goed uit en het draait" als bewijs voor iets anders dan dat het er goed uitziet en draait.

## Wat het lezen van code vervangt

Zodra je accepteert dat de helft van je systeem onzichtbaar is voor statische inspectie, wordt de kernvraag: hoe observeer je die andere helft? Voor een klein product dekken vier elementen vrijwel alles af:

**Foutopsporing (Error tracking).** Elke niet-afgevangen exceptie, inclusief stack trace, gebruikerscontext en het specifieke verzoek dat de fout veroorzaakte, doorgestuurd naar een plek waar je ook daadwerkelijk kijkt (zoals Sentry). Dit ene onderdeel transformeert "een klant zegt dat iets stuk is" in een direct analyseerbare gebeurtenis.

**Gestructureerde, doorzoekbare logs.** Geen willekeurige `console.log`-regels door de code verspreid, maar een consistente registratie van gebeurtenissen met unieke verzoek-ID's waarmee je de actie van een specifieke gebruiker van begin tot eind kunt traceren.

**Uptime-monitoring.** Een externe controle die periodiek verifieert of je applicatie reageert, uitgevoerd vanaf een locatie buiten je eigen infrastructuur, met notificaties die je direct bereiken wanneer de boel down gaat.

**Basale systeemstatistieken.** Responstijden, foutpercentages en het aantal actieve databaseverbindingen. Je hoeft geen complex observability-platform te bouwen; je wilt simpelweg een antwoord kunnen geven op de vraag "is dit normaal voor ons?" zodra het systeem traag aanvoelt.

Voor een product met enkele honderden gebruikers kost dit een middag configuratie en een minimale maandelijkse uitgave. Het transformeert je relatie met productie van hopen naar weten.

## De helft testen die Cursor niet kan lezen

Statische analyse en unittests controleren de leesbare helft van je codebase. De runtime-helft vereist andere oefeningen, en voor een klein product zijn die grotendeels handmatig uit te voeren:

**Voer de kernflow uit op echte infrastructuur met echte inloggegevens,** inclusief een kleine echte betaling via iDEAL of creditcard die je direct daarna terugstort. De testmodus van betaalproviders doorloopt vaak niet exact dezelfde interne codepaden als echte transacties.

**Creëer opzettelijk gelijktijdigheid (concurrency).** Open twee verschillende browsers, navigeer naar hetzelfde record en klik binnen dezelfde seconde. Probeer het allerlaatste beschikbare tijdslot twee keer tegelijk te reserveren. Verstuur een formulier twee keer achter elkaar door dubbel te klikken.

**Vervuil je eigen testdata bewust.** Gebruik apostroffen, vreemde leestekens, emoji's, extreem lange teksten, nulwaarden, negatieve getallen en data ver in het verleden. Je app zal al deze invoer binnen een maand na lancering tegenkomen.

**Breek met opzet een externe koppeling.** Laat een webhook of API-client verwijzen naar een ongeldig adres en kijk wat de eindgebruiker te zien krijgt. Als het resultaat een wit scherm of een oneindig draaiend icoontje is, heb je direct een kritieke bug te pakken die opgelost moet worden.

**Test als een kwaadwillende geauthenticeerde gebruiker.** Pas een ID aan in de netwerk-request van je browser en probeer het record van een andere gebruiker op te vragen. Dit is het meest voorkomende beveiligingslek in met AI gebouwde applicaties, en geen enkele code-editor zal je hierop wijzen.

## Waar de editor écht helpt bij runtime-problemen

Dit is geen pleidooi om zonder AI-tools te werken. Zodra je over degelijke observability beschikt, wordt een AI-editor juist aanzienlijk waardevoller. Je kunt de editor dan namelijk voorzien van concreet bewijs: een stack trace, een trage SQL-query of een reeks logregels die precies tonen wat er direct voorafgaand aan het incident gebeurde. Met echte runtime-gegevens kan de AI uitstekend verklaren wat de code deed en een gerichte oplossing voorstellen.

De volgorde is hierbij cruciaal: observeer eerst, vraag daarna pas om advies. Een editor vragen om een runtime-probleem uitsluitend op basis van de broncode op te sporen, is vragen om giswerk over een systeem dat hij niet kan zien.

## De onzichtbare helft onder controle krijgen

Die runtime-laag is exact wat LaunchStudio bouwt onder een bestaand prototype: configuratie expliciet en controleerbaar maken in plaats van verstopt in willekeurige dashboards; database-beveiligingsregels schrijven en testen door er actief op in te breken; concurrency en race conditions afvangen waar het commercieel telt; integraties van derden voorzien van robuuste foutafhandeling; en error tracking, logregistratie, uptime-checks en alerts inrichten zodat jij incidenten ontdekt vóór je klanten erover klagen.

De frontend die je hebt gebouwd in Cursor, Lovable of Bolt blijft volledig intact, de codebase blijft conventioneel en leesbaar voor AI, en alle intellectuele eigendom blijft van jou. Dit werk wordt uitgevoerd door de senior engineers van Manifera, die al elf jaar lang productiesystemen realiseren voor organisaties zoals Vodafone, TNO en CFLW - werk dat voor het overgrote deel bestaat uit precies die runtime-helft.

Heb je al een product live staan zonder inzicht in wanneer en waarom het faalt? [Praat met een engineer die AI-gegenereerde code begrijpt](https://launchstudio.eu/nl/#contact) - of bekijk wat [Launch Ready](https://launchstudio.eu/nl/#packages) inhoudt voordat je het wiel zelf probeert uit te vinden.

## Een foutmelding lezen zonder paniek

Zodra je error tracking actief is, ontvang je meldingen die je wellicht nog nooit eerder hoefde te ontcijferen. Een beknopte handleiding scheelt een hoop stress:

**Lees eerst de onderkant van de stack trace, en daarna pas de bovenkant.** De onderkant vertelt je waar de fout daadwerkelijk aan de oppervlakte kwam; de bovenkant toont wat je eigen code aan het doen was toen het misging. De tussenliggende regels uit externe libraries zijn bij een eerste diagnose meestal alleen maar ruis.

**Maak onderscheid tussen frequentie en ernst.** Een fout die één gebruiker eenmalig raakt, is een curiositeit. Dezelfde fout die veertig keer in een uur optreedt, is een acuut incident. Een enkele fout die het afrekenproces blokkeert is vele malen ernstiger dan duizend meldingen over een haperende tooltip. Error trackers groeperen en tellen meldingen om precies die reden.

**Kijk naar wat de gebruiker probeerde te doen,** niet alleen naar de code. Goede tracking registreert het http-verzoek, het gebruikersaccount en de voorafgaande reeks acties. Drie foutmeldingen die dezelfde pagina en hetzelfde tijdvenster delen, hebben vrijwel altijd dezelfde achterliggende oorzaak.

**Onderscheid een 'verwachte fout' van een 'gebroken applicatie'.** Een geweigerde creditcard of mislukte iDEAL-transactie is een normale gebeurtenis die je app hoort op te vangen. Als dit als een onafgevangen uitzondering (unhandled exception) binnenkomt, is de ontbrekende foutafhandeling de bug, niet de geweigerde transactie zelf.

**Voorkom dat je puur de symptomen in de stack trace fixt.** De foutmelding beschrijft het symptoom op het moment dat alles omviel - wat vaak pas enkele stappen na de daadwerkelijke programmeerfout plaatsvindt. Zoek naar de allereerste aanname in de keten die niet klopte, niet naar het laatste onderdeel dat brak.

Oprichters die hiermee leren omgaan, stoppen met het ervaren van productie als iets dat hen overkomt. Het is het fundamentele verschil tussen een applicatie beheren en simpelweg hopen dat alles blijft werken.

## De eerste week na lancering

Observability bewijst zijn waarde vooral in de eerste zeven dagen, wanneer je app voor het eerst in contact komt met gebruikersgedrag dat hij nog nooit heeft meegemaakt. Drie gewoontes maken die week leerzaam in plaats van angstaanjagend:

**Bekijk je error tracker elke ochtend,** zelfs als er ogenschijnlijk niets aan de hand is. Nieuwe fouten in de eerste week zijn doorgaans klein en goedkoop te verhelpen. Ze laten je precies zien welke aannames onjuist waren, op een moment dat het aantal actieve gebruikers nog laag genoeg is om fixes zonder reputatieschade door te voeren.

**Let op het patroon van je netwerkverkeer, niet alleen op het volume.** Tien registraties vanaf één IP-adres binnen één minuut is geen succesvolle lancering; het is een geautomatiseerd script. Door vroeg te leren wat normaal gedrag is, herken je afwijkende patronen later direct.

**Houd een logboek bij van wat je hebt aangepast en wanneer.** Als er op dag vijf iets minder goed presteert, is de eerste nuttige vraag wat er op dag vier naar productie is gedeployed. Oprichters die dit uit hun hoofd proberen te reconstrueren, maken stelselmatig verkeerde aannames.

Geen van deze gewoontes kost meer dan tien minuten per dag. Ze transformeren de lanceringsweek van een periode van overleven naar de fase waarin het daadwerkelijke gedrag van je product voor het eerst helder zichtbaar wordt.

## Echt voorbeeld

### Een ticketing-tool die dezelfde stoel twee keer verkocht

Wouter Bleeker bouwde Podiumkaart in Cursor: een ticketing-tool voor kleinere theaterpodia in Haarlem en Leiden. De code zag er verzorgd uit, was herhaaldelijk gereviewd met behulp van AI en gedekt door een nette set unittests.

Bij de allereerste voorstelling die écht populair bleek, verkocht het podium plotseling 214 kaartjes voor een zaal met slechts 210 stoelen. De beschikbaarheidscontrole en het wegschrijven van de reservering waren twee losse database-operaties. Onder een plotselinge piek van gelijktijdige verzoeken overlapten meerdere transacties elkaar. Elke vooraf geschreven test was geslaagd, simpelweg omdat geautomatiseerde unittests sequentieel achter elkaar draaien.

Tot overmaat van ramp werd het probleem pas twee dagen later ontdekt. Er was geen error tracking actief, waardoor de dubbele boekingen pas aan het licht kwamen toen een theaterbezoeker bij binnenkomst zag dat er al iemand op haar stoel zat. Omdat er geen gestructureerde logging was, moest Wouter handmatig door ruwe databaserijen spitten om te reconstrueren wat er was misgegaan.

Zes werkdagen waren nodig voor het herstel: de boekingstransactie werd herschreven als één ondeelbare, atomische databasetransactie met een unieke database-constraint, waardoor een stoel ongeacht de timing technisch nooit twee keer verkocht kan worden. Daarnaast werden error tracking en gestructureerde logging ingericht, werd uptime-monitoring gekoppeld aan Wouters telefoon en werd er een stresstest aan de deployment-pipeline toegevoegd die vijftig gelijktijdige aankopen simuleert.

**Resultaat:** hetzelfde theater draaide twee maanden later een reeks van elf volledig uitverkochte voorstellingen zonder een enkele dubbele boeking. En het enige incident dat zich voordeed - een time-out bij de betaalprovider - verscheen al elf minuten voordat de theatermanager belde in het dashboard van Wouter.

> *"Mijn editor had die functie tientallen keren gelezen. De logica klopte. Hij klopte alleen niet wanneer twee mensen op exact dezelfde milliseconde klikten, en er was voor de AI geen enkele manier om dat vanuit de broncode te weten."*
> - **Wouter Bleeker, Oprichter, Podiumkaart (Haarlem)**

**Kosten & Doorlooptijd:** € 2.800 (herschrijven van transacties, inrichten van observability, load-testing in pipeline) - afgerond binnen 6 werkdagen.

## Veelgestelde vragen

### Kan een AI-editor beveiligingsproblemen in mijn code vinden?

Hij kan bepaalde patronen ontdekken in code die hij kan lezen - zoals een ontbrekende validatie of een onveilige query-constructie. Maar hij kan niet beoordelen hoe je database-toegangsregels zijn geconfigureerd, wat er in je hostingdashboard staat ingesteld of waar een geauthenticeerde vreemdeling bij kan, omdat niets daarvan in de git-repository staat.

### Als mijn tests slagen, ben ik dan gedekt voor runtime-problemen?

Slechts gedeeltelijk. Unittests draaien sequentieel tegen vooraf gedefinieerde testdata. Ze testen daardoor geen gelijktijdigheid (concurrency), geen afwijkend gedrag van externe leveranciers, geen productieconfiguraties en geen onverwachte datavormen. Daarvoor zijn gerichte handmatige stresstests en actieve observability noodzakelijk.

### Wat is de minimale monitoring die een klein product nodig heeft?

Foutopsporing (error tracking), doorzoekbare gestructureerde logs, een externe uptime-check en basisstatistieken over responstijden en foutpercentages. Voor een product met enkele honderden gebruikers is dit binnen één middag ingericht tegen minimale maandelijkse kosten.

### Hoe test ik op race conditions zonder speciale tooling?

In eerste instantie handmatig: open twee verschillende browsers, selecteer hetzelfde record en verstuur gelijktijdig formulieren of klik snel dubbel op knoppen. Alles wat te maken heeft met beperkte voorraad, stoelen, reserveringen of saldi verdient deze handmatige test vóór lancering, gecombineerd met een strikte constraint op databaseniveau.

### Betekent dit dat bouwen met behulp van AI onveilig is?

Nee. Het betekent dat het betrouwbaarheidssignaal fundamenteel is veranderd. Code die soepel leest en direct draait, is niet langer een garantie voor zorgvuldig doordachte randvoorwaarden. De echte verificatie moet daarom komen van het observeren van het draaiende systeem in plaats van het beoordelen van het uiterlijk van de broncode.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan een AI-editor beveiligingsproblemen in mijn code vinden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hij kan patronen ontdekken in leesbare code, zoals een ontbrekende controle of onveilige query. Hij kan echter geen database-toegangsbeleid, hostingconfiguraties of autorisaties van vreemden evalueren, omdat dat niet in de repository staat."
      }
    },
    {
      "@type": "Question",
      "name": "Als mijn tests slagen, ben ik dan gedekt voor runtime-problemen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Slechts gedeeltelijk. Unittests draaien sequentieel tegen gekozen testdata, waardoor ze concurrency, gedrag van derden, productieconfiguratie en afwijkende datavormen missen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de minimale monitoring die een klein product nodig heeft?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Error tracking, doorzoekbare gestructureerde logs, een externe uptime-controle en basisstatistieken over responstijden en foutpercentages - een middag werk voor een klein product."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe test ik op race conditions zonder speciale tooling?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Eerst handmatig: twee browsers, hetzelfde record, gelijktijdig verzenden en dubbelklikken op knoppen. Alles met beperkte voorraad, stoelen of saldi vereist bovendien een constraint op databaseniveau."
      }
    },
    {
      "@type": "Question",
      "name": "Betekent dit dat bouwen met behulp van AI onveilig is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, het betekent dat het betrouwbaarheidssignaal is veranderd. Vloeiende code is geen garantie voor zorgvuldig doordachte randvoorwaarden, dus verificatie moet komen van het observeren van het draaiende systeem."
      }
    }
  ]
}
</script>
