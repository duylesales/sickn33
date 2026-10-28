---
Titel: "Lovable Hosting: Deploys Zonder Downtime Terwijl Mensen Het Gebruiken"
Trefwoorden: lovable hosting, deployment zonder downtime, expand-and-contract-migraties, atomaire deploys, geleidelijke releases, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Lovable Hosting: Deploys Zonder Downtime Terwijl Mensen Het Gebruiken

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting: Deploys Zonder Downtime Terwijl Mensen Het Gebruiken",
  "description": "Deployen naar een product met actieve gebruikers betekent dat er twee versies tegelijk draaien. Wat er in die overlap breekt, hoe expand-and-contract-migraties dat voorkomen, en waarom het verouderde browsertabblad de mislukking is die niemand test.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-04",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-hosting-zero-downtime-deploys-while-people-are-using-it" }
}
</script>

De eerste maanden is deployen gratis. Niemand gebruikt het product, dus wat er in die negentig seconden gebeurt, gebeurt met niemand.

Dan is er op een dag iemand halverwege een formulier wanneer u deployt, en de aanname dat een deployment direct is, klopt niet meer. Gedurende een periode - seconden op een goed platform, minuten op een slecht - bestaan er twee versies van uw applicatie tegelijk, en de oude wordt nog gebruikt door mensen van wie de browser niet opnieuw heeft geladen.

De meeste deploymentincidenten in kleine producten spelen zich volledig af in die overlap. Ze worden niet veroorzaakt door slechte code; ze worden veroorzaakt door twee correcte versies die het oneens zijn.

## Wat Er Werkelijk Overlapt

Drie dingen, en elk faalt anders.

**De browser.** Een klant laadde uw applicatie een uur geleden. Zijn tabblad draait het oude JavaScript, dat uw API blijft aanroepen zolang hij het openlaat. Sommige van die gebruikers zitten er morgen nog.

**De server.** Verzoeken die al onderweg waren toen de nieuwe versie startte, worden afgerond onder de oude. Serverless platforms gaan hier meestal goed mee om; één server die herstart doet het slecht, tenzij hij is ingesteld om eerst leeg te lopen.

**De database.** Dit is degene die schade veroorzaakt in plaats van ergernis, omdat een schemawijziging direct en overal tegelijk op beide versies van toepassing is.

## De Regel Die het Meeste Voorkomt

Elke deployment moet in beide richtingen veilig zijn: de oude code moet werken met de nieuwe database, en de nieuwe code moet werken met de oude database.

Als dat klopt, doet de volgorde van handelingen er niet meer toe en wordt terugdraaien mogelijk. Klopt het niet, dan hebt u een moment - soms een lang moment - waarop er iets kapot is, welke versie er ook draait.

Daarom is een kolom verwijderen gevaarlijk en een kolom toevoegen niet. Op het moment dat de kolom verdwijnt, faalt elke instantie van de vorige versie die haar nog verwacht, inclusief het tabblad dat uw klant sinds vanochtend openheeft.

## Expand and Contract, Concreet

Het patroon dat schemawijzigingen veilig maakt, heeft vier stappen, verdeeld over minstens twee deployments.

**Uitbreiden (expand).** Voeg de nieuwe structuur toe - een kolom, een tabel - zonder iets te verwijderen. Nullable, met een standaardwaarde indien nodig. Niets gebruikt haar nog en niets kan breken.

**Migreren.** Deploy code die naar zowel de oude als de nieuwe structuur schrijft, en vul de bestaande rijen aan in batches in plaats van in één statement dat de tabel vergrendelt.

**Lezen omzetten.** Deploy code die uit de nieuwe structuur leest. De oude wordt nog bijgehouden, dus terugdraaien is nog steeds veilig.

**Inkrimpen (contract).** Stop in een latere release, als u zeker bent, met schrijven naar de oude structuur en verwijder haar.

Hernoemen is dezelfde volgorde: toevoegen, naar beide schrijven, nieuw lezen, oud verwijderen. Het kost twee of drie deployments in plaats van één, die elk afzonderlijk terug te draaien zijn, en op geen enkel moment zijn draaiende code en live schema het oneens.

De stappen die u in één deployment volledig moet vermijden: een kolom verwijderen of hernoemen waarnaar de vorige versie nog verwijst, een niet-nullable kolom toevoegen zonder standaardwaarde, en een constraint toevoegen die bestaande data schendt - waarbij de laatste de migratie laat mislukken en u half gedeployd achterlaat.

## Aanvullen Vraagt om Batches

Een aanvulling die een miljoen rijen in één statement bijwerkt, houdt locks vast zolang ze duurt, wat op een live tabel betekent dat uw product niet werkt terwijl ze draait.

Doe het in batches van een paar duizend, met een pauze ertussen, en maak het hervatbaar, zodat het kan worden gestopt en opnieuw gestart. Laat het draaien als achtergrondtaak in plaats van als deel van de migratie, zodat een deployment er nooit op wacht.

Laat bij grote tabellen de aanvulling ruim vóór de release draaien die ervan afhangt. De uitbreidingsstap kan dagen eerder plaatsvinden; er is geen eis dat de vier stappen dicht bij elkaar liggen, en ze scheiden haalt de tijdsdruk weg bij het deel dat het meest waarschijnlijk misgaat.

## Het Verouderde Tabblad Dat Niemand Test

Uw gebruikers laden niet opnieuw. Een browsertabblad dat sinds maandag openstaat, draait op donderdag het JavaScript van maandag, en het blijft uw API aanroepen.

Twee gevolgen zijn het afhandelen waard. Een endpoint waarvan de oude versie afhangt, kan niet worden verwijderd op het moment dat niets nieuws het meer aanroept - laat het een periode staan, ook als het niets nuttigs doet. En een antwoordvorm die de oude versie verwacht, mag niet onverenigbaar veranderen; voeg velden toe in plaats van ze te hernoemen of te verwijderen.

De oplossing voor de gebruiker is klein en het bouwen waard: wanneer de applicatie merkt dat er een nieuwere versie beschikbaar is - door een build-identificatie te vergelijken die de server teruggeeft - toon dan een bescheiden melding die de gebruiker uitnodigt opnieuw te laden. Geen geforceerde verversing, die weggooit wat hij aan het typen was, maar een zichtbaar aanbod. De meeste mensen nemen het binnen minuten aan, wat begrenst hoe lang u de vorige versie moet ondersteunen.

## Deploy op een Moment Dat U Kunt Kijken

De laatste stap is gedrag in plaats van techniek.

Deploy wanneer u tien minuten naar het resultaat kunt kijken: niet als u vertrekt, niet op een vrijdagavond, niet vlak voor een vergadering. De meeste slechte releases worden niet ontdekt door monitoring; ze worden ontdekt door degene die ze uitbracht, door te kijken.

Kijk dan ook echt. Laad het product als een echte gebruiker, probeer uit wat u veranderde, en controleer de error tracker op iets nieuws. Tien minuten, elke keer, is de goedkoopste verzekering in softwareoplevering.

En ken uw weg terug. Het terugdraaien moet zijn vastgesteld en getimed voordat u het nodig hebt, en betekent een schemawijziging dat terugdraaien niet mogelijk is, dan is het de moeite waard dat te weten vóór het deployen in plaats van tijdens.

## Feature Flags Maken de Moeilijke Releases Makkelijk

Er is een soort wijziging die niet in beide richtingen compatibel te maken is, hoe zorgvuldig u de volgorde ook kiest - een opnieuw ontworpen proces, een vervangen berekening, een nieuwe integratie die verandert wat klanten zien. Scheid hierbij de deployment van de release.

Een flag is een voorwaarde die wordt gecontroleerd voordat het nieuwe gedrag draait. De code wordt uitgerold, uitgeschakeld, en door niemand gebruikt. U zet haar aan voor uw eigen account, dan voor één welwillende klant, dan voor een tiende van de lijst, dan voor iedereen. Is er iets mis, dan gaat ze in seconden uit - geen deployment, geen terugdraaien, geen migratie om terug te zetten.

Voor een klein product hoeft dit geen platform te zijn. Een rij in een tabel met een naam en een status, gelezen aan het begin van een verzoek en kort gecachet, dekt bijna alles. De twee verfijningen die het hebben waard zijn: de mogelijkheid om een flag voor een specifiek account aan te zetten in plaats van voor iedereen, en een registratie van wie haar wijzigde en wanneer.

De discipline die voorkomt dat dit een eigen probleem wordt: verwijder de flag zodra de functie vastligt. Flags die hun doel overleven, stapelen zich op tot een codebase waarin elk pad vier voorwaarden heeft en niemand er veilig een kan verwijderen - een tragere versie van het probleem waarvoor ze werden ingevoerd.

Goed gebruikt, veranderen flags hoe een release aanvoelt. De deployment wordt routine en onopvallend, en de beslissing om iets aan klanten te tonen wordt een aparte, omkeerbare handeling die u neemt wanneer u kijkt.

Nog een praktisch voordeel, specifiek voor producten als deze: een flag is de enige veilige manier om iets uit te rollen wat een AI-sessie snel bouwde. De code kan in productie staan, op uw gemak worden beoordeeld, alleen door u worden gebruikt, en op basis van bewijs in plaats van vertrouwen worden doorgezet of verwijderd.

Dat is een werkelijk andere manier van werken, en ze past bij hoe deze producten echt worden gebouwd: snel, in pieken, door een oprichter die niet alles kan beoordelen voordat het wordt uitgerold, maar absoluut kan beslissen wat klanten te zien krijgen.

## Dit Inrichten

Voor een bestaand product kost dit doorgaans een halve dag plus een gewoonte: migraties beoordeeld tegen de regel van compatibiliteit in twee richtingen, expand-and-contract ingevoerd voor elke verwijdering of hernoeming van een kolom, aanvullingen in batches en als hervatbare achtergrondtaken vóór de release die ze nodig heeft, API-antwoorden alleen aanvullend gewijzigd met oude endpoints met vertraging opgeheven, een build-identificatie beschikbaar zodat de client een nieuwere versie kan detecteren en een herlaadactie kan aanbieden, een deploymentchecklist die kort genoeg is om te volgen, en terugdraaien vastgesteld en getimed.

LaunchStudio richt dit in als onderdeel van productieklaar maken en voert het uit binnen de managed regeling van €49 per maand. De engineers zijn van Manifera - elf jaar uitrollen in live systemen voor klanten als Vodafone, TNO en CFLW, vanaf de Herengracht 420 in Amsterdam.

[Vraag ons of uw volgende migratie omkeerbaar is](https://launchstudio.eu/nl/#contact). Het is de vraag die bepaalt hoe erg een fout kan worden.

## Echt voorbeeld

### De Kolom Die Iedereen Brak Die Nog Ingelogd Was

Ferdi Aalbersberg bouwde Routeplanning in Lovable: routeplanning voor regionale bakkerijen en voedingsdistributeurs, 24 bedrijven, waarvan de chauffeurs de app vanaf vijf uur 's ochtends op hun telefoon gebruiken.

Een opruimwijziging hernoemde een kolom van `adres` naar `address` en paste de applicatie in dezelfde deployment aan. Hij deployde om 06:40 op een woensdag, in de overtuiging dat het triviaal was.

Elke chauffeur die al onderweg was, had de applicatie open. Hun browsers draaiden de vorige versie, die vroeg om een kolom die niet meer bestond, en elke verversing van de route gaf een fout. Omdat ze aan het rijden waren, laadden de meesten niet opnieuw; ze belden hun planners, die Ferdi belden. Zo'n 60 chauffeurs bij negen bedrijven werden geraakt gedurende de 25 minuten die hij nodig had om het te begrijpen en terug te draaien - en het terugdraaien werkte ook niet, omdat de oude code een kolom nodig had die hij had verwijderd.

Hij zette de kolom om 07:20 met de hand terug, op basis van een schema dat hij onder flinke druk las.

Eén werkdag daarna: expand-and-contract ingevoerd, met de hernoeming opnieuw en correct gedaan over drie deployments - `address` toevoegen, naar beide schrijven en aanvullen in batches van 2.000 als hervatbare taak, het lezen een dag later omzetten, `adres` een week daarna verwijderen; een regel op papier dat geen deployment een kolom mag verwijderen of hernoemen waarnaar de draaiende versie verwijst; API-antwoorden alleen nog aanvullend gewijzigd, met verwijderde endpoints 30 dagen bewaard als lege handeling; een build-identificatie die de server teruggeeft, met een rustige melding "er is een nieuwe versie beschikbaar" in de app, die chauffeurs bij hun volgende stop accepteren; een deploymentchecklist van vier regels inclusief een getimede rollback; en deployments volledig uit het tijdvak 05:00 tot 09:00 gehaald, het tijdvak waarin Ferdi's klanten echt werken.

**Resultaat:** twaalf maanden zonder deploymentincident, inclusief twee verdere schemawijzigingen van vergelijkbare omvang. De versiemelding bleek net zo belangrijk als de migratiediscipline - daarvóór had Ferdi chauffeurs die zonder het te weten een build van drie dagen oud draaiden.

> *"Het was een hernoeming. Ik heb nog nooit iets sneller of onzorgvuldiger gedaan, en zestig chauffeurs stonden er om zeven uur 's ochtends door naast hun busjes."*
> - **Ferdi Aalbersberg, Oprichter, Routeplanning (Sneek)**

**Kosten & Doorlooptijd:** €1.600 (expand-and-contract-migratie van de hernoeming, hervatbare aanvulling in batches, aanvullend API-beleid, versiedetectie in de client en herlaadmelding, deploymentchecklist met geteste rollback) - afgerond in 1 werkdag.

## Veelgestelde vragen

### Waarom breekt deployen dingen als de code correct is?

Omdat er twee versies tegelijk draaien. Browsers houden het oude JavaScript vast, verzoeken die onderweg zijn worden afgerond op de oude server, en een schemawijziging geldt direct voor beide versies.

### Hoe hernoem ik veilig een databasekolom?

Voeg de nieuwe toe, deploy code die naar beide schrijft en vul aan, deploy code die de nieuwe leest, en verwijder de oude kolom in een latere release. Elke stap is afzonderlijk terug te draaien.

### Waarom moeten aanvullingen in batches draaien?

Eén statement dat een grote tabel bijwerkt, houdt locks vast zolang het duurt, waardoor uw product stopt. Batches van een paar duizend rijen met pauzes, als hervatbare achtergrondtaak, voorkomen dat.

### Hoe zit het met gebruikers die de pagina nooit opnieuw laden?

Ondersteun de vorige versie een periode: houd endpoints in leven, wijzig antwoorden alleen aanvullend, en toon een melding wanneer er een nieuwere build wordt gedetecteerd, zodat de meeste gebruikers binnen minuten bijwerken.

### Wanneer kan ik het beste deployen?

Wanneer u tien minuten naar het resultaat kunt kijken, buiten het drukste tijdvak van uw klanten. De meeste slechte releases worden gevonden door degene die ze uitbracht, door te kijken - niet door monitoring.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom breken deployments dingen als de code correct is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Twee versies overlappen: browsers draaien oud JavaScript, lopende verzoeken worden afgerond op de oude server, en schemawijzigingen gelden direct voor beide."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe hernoem ik een kolom zonder downtime?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voeg de nieuwe kolom toe, schrijf naar beide en vul aan, zet het lezen om in een latere deploy, en verwijder de oude kolom zodra u zeker bent."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom moeten aanvullingen in batches?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Eén grote update houdt locks vast zolang ze duurt en legt het product stil. Gebruik hervatbare batches van een paar duizend rijen met pauzes."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe ga ik om met gebruikers die de pagina nooit opnieuw laden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Houd oude endpoints een periode in leven, wijzig antwoorden alleen aanvullend, en bied een herlaadmelding aan wanneer de client een nieuwere build detecteert."
      }
    },
    {
      "@type": "Question",
      "name": "Wanneer moet ik deployen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Wanneer u daarna tien minuten kunt kijken, buiten de drukste uren van uw klanten. De meeste slechte releases worden gevonden door degene die kijkt, niet door monitoring."
      }
    }
  ]
}
</script>
