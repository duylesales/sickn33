---
Titel: "Zoeken in Lovable en Supabase: Waarom het faalt en hoe je het oplost"
Trefwoorden: Lovable, lovable supabase, full text search postgres, zoekrelevantie kleine app, typfouttolerantie zoeken, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Zoeken in Lovable en Supabase: Waarom het faalt en hoe je het oplost

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Zoeken in Lovable en Supabase: Waarom het faalt en hoe je het oplost",
  "description": "Het zoekveld in de meeste AI-gegenereerde apps is een simpele substring-match die voor de hand liggende resultaten mist en vertraagt zodra data groeit. Wat gebruikers verwachten, wat Postgres standaard kan en wanneer een aparte zoekservice nodig is.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-29",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/search-in-ai-built-apps-what-actually-works" }
}
</script>

Typ "fiets" in je app en je krijgt nul resultaten, simpelweg omdat het item "Fietsen" heet. Typ "amsterdam" en je mist alles wat gecategoriseerd is onder "Amsterdam-Noord". Zoek naar een klant genaamd "de Vries" en vind niets omdat de database "Vries, de" bevat.

Zoekfunctionaliteit is dé feature waarvan oprichters aannemen dat het al lang is opgelost, terwijl AI-bouwers het op de meest basale manier implementeren: een hoofdlettergevoelige substring-match op één enkele kolom. Dat werkt vlekkeloos in een demo met twaalf rijen aan testdata, maar faalt geruisloos in productie. Gebruikers die zoeken en niets vinden, concluderen immers niet dat je zoekfunctie stuk is - ze concluderen dat je platform niet heeft wat ze zoeken en vertrekken.

## Wat gegenereerd zoeken daadwerkelijk doet

Vraag een willekeurige AI-tool om een zoekbalk en je krijgt vrijwel altijd een query die een patroon vergelijkt met één enkele tekstkolom. Dat betekent in de praktijk:

**Geen verwerking van hoofdletters**, tenzij iemand daar expliciet over heeft nagedacht. "Fiets" en "fiets" zijn voor de database twee compleet verschillende strings.

**Geen woordherkenning.** Een substring-match vindt "fiets" wel binnen "fietsenmaker" en zelfs binnen willekeurige lettercombinaties, maar mist het meervoud in vrijwel alle talen.

**Geen tolerantie voor typfouten.** "Amsterdma" levert niets op - terwijl grofweg één op de tien zoekopdrachten een typfout bevat.

**Geen relevantiescore of ranking.** Elk resultaat is even belangrijk, waardoor het item dat de gebruiker daadwerkelijk zoekt vaak op positie veertien belandt.

**Slechts één kolom.** Een productzoekfunctie die naar de titel kijkt, maar de omschrijving, categorie en merknaam compleet negeert.

**Geen indexering.** Hierdoor leest de database bij elke toetsaanslag van een live zoekopdracht de complete tabel uit. Dat is precies de reden waarom de pagina steeds trager wordt naarmate je assortiment groeit.

Die combinatie vormt het verschil tussen een zoekbalk die er alleen mooi uitziet en een zoekfunctie die daadwerkelijk resultaten oplevert.

## Wat gebruikers daadwerkelijk verwachten

Gebruikers verwachten bescheiden dingen, maar die ontbreken allemaal in de standaardopzet:

Ze verwachten dat hoofdletters er niet toe doen, dat woordvolgorde flexibel is ("rode fiets" moet ook "fiets, rood" vinden), dat gedeeltelijke woorden logisch matchen, dat typfouten worden vergeven, dat de beste resultaten bovenaan staan en dat er in meerdere velden tegelijk wordt gezocht. In het Nederlands verwachten ze specifiek dat samengestelde woorden functioneren - zoeken op "fietsslot" moet ook "slot voor fiets" kunnen vinden - iets wat een simpele match nooit doet.

Voor niets van dit alles is direct een zware, externe zoekmachine nodig. Het overgrote deel zit al ingebouwd in de database die je nu al gebruikt.

## Wat Postgres je gratis biedt

Draait je app op Supabase of een andere PostgreSQL-database? Dan dekt de ingebouwde full-text search de behoeften van vrijwel elke beginnende of middelgrote applicatie volledig af. Veel oprichters betalen maandelijks voor een losse zoekdienst zonder te weten dat deze kracht al in hun database aanwezig is.

**Taalbewuste tekstverwerking.** Postgres kan woorden herleiden tot hun stam (stemming), zodat een zoekopdracht naar één vorm ook varianten vindt. Er is standaard ondersteuning voor het Nederlands ingebouwd, wat essentieel is voor samenstellingen en verbuigingen die simpele matching mist.

**Ranking en relevantie.** Resultaten worden gescoord op relevantie in plaats van een willekeurige volgorde. Je kunt velden eenvoudig wegen: een match in de titel telt zwaarder mee dan een match in de omschrijving.

**Zoeken over meerdere kolommen**, gecombineerd in één enkele doorzoekbare vectorrepresentatie.

**Fuzzy matching** via trigram-overeenkomsten (`pg_trgm`). Dit vangt typfouten en gedeeltelijke matches soepel op en kan worden geïndexeerd zodat het razendsnel blijft.

**Degelijke indexen (zoals GIN).** Hierdoor scant de zoekactie niet de hele tabel, wat direct een einde maakt aan de prestatieproblemen bij een groeiende database.

De overstap van een simpele match naar deze robuuste aanpak kost doorgaans één werkdag: voeg een doorzoekbare kolom toe die automatisch door de database wordt bijgewerkt, indexeer deze, herschrijf de query en stel logische wegingen in.

## Wanneer een speciale zoekservice gerechtvaardigd is

Soms schiet de database tekort, maar de eerlijke drempelwaarden liggen aanzienlijk hoger dan softwareleveranciers je willen doen geloven:

- Honderdduizenden records of meer, waarbij zoeken de primaire gebruikersinteractie vormt.
- Uitgebreide facetfilters over tientallen dimensies tegelijk, die direct en zonder vertraging moeten updaten zodra gebruikers klikken.
- Realtime zoeken tijdens het typen (search-as-you-type) waarbij resultaten binnen tientallen milliseconden op het scherm moeten staan.
- Voortdurende afstemming van relevantie - synoniemenlijsten, promoties van specifieke producten en complexe bedrijfsregels.
- Meertalig zoeken over radicaal verschillende taalfamilies.

Blijf je onder deze drempels? Dan voegt een externe zoekdienst alleen maar extra operationele complexiteit toe: een tweede kopie van je data die continu gesynchroniseerd moet blijven en extra maandelijkse abonnementskosten voor functionaliteit die je niet benut. Boven die drempels verdient een speciale zoekdienst zichzelf direct terug.

## De praktische verbeteringen, op volgorde

**Maak het hoofdletterongevoelig en woordbewust.** Dit is de grootste kwaliteitsverbetering met de laagste investering.

**Doorzoek de velden die gebruikers verwachten.** Vraag vijf gebruikers waarop ze verwachten te kunnen zoeken en neem die kolommen op in de zoekvector.

**Voeg een index toe.** Dit lost zowel relevantieproblemen op als de vertraging die ontstaat zodra de tabel groeit.

**Rangschik de resultaten**, waarbij matches in titels zwaarder wegen dan in lopende tekst.

**Voeg tolerantie voor typfouten toe** via similarity-matching, die intreedt wanneer een exacte zoekopdracht te weinig resultaten oplevert.

**Richt de 'geen resultaten'-status goed in.** Een zoekopdracht zonder resultaten moet suggesties doen - gerelateerde categorieën, een spellingcorrectie of een alternatieve navigatie - in plaats van een blanco pagina die overkomt als "wij hebben dit product niet".

**Log wat mensen zoeken.** Dit is de meest waardevolle en minst geïmplementeerde actie. Zoekopdrachten met nul resultaten tonen exact waar gebruikers naar verlangen en wat jij nog niet aanbiedt, of waar het taalgebruik van je gebruikers afwijkt van jouw catalogus.

## Wat niemand meet

Vraag jezelf eens af welk percentage van de zoekopdrachten in jouw app nul resultaten oplevert. De meeste oprichters hebben geen flauw idee, omdat niets dit bijhoudt.

In applicaties waar dit voor het eerst wordt gemeten, ligt dit cijfer schrikbarend hoog. De oorzaken zijn doorgaans banaal: meervoudsvormen, hoofdletters, synoniemen die de klant wél gebruikt maar de catalogus niet, of een veld dat simpelweg nooit in de databasequery is opgenomen. Elk van die mislukte zoekopdrachten was een potentiële klant die dacht dat je zijn probleem niet kon oplossen.

Het loggen van mislukte zoekopdrachten kost een middag werk en verandert regelmatig de complete koers van je productroadmap.

## Zoekfunctionaliteit bouwen die standhoudt

Dit is een overzichtelijk, afgebakend project met een directe positieve impact op het gebruiksgemak van je applicatie. LaunchStudio implementeert dit als onderdeel van de afronding van AI-gebouwde software: native full-text search met de juiste taalinstellingen, doordachte veldwegingen, typfouttolerantie waar nodig, solide indexen zodat het systeem snel blijft bij groei, duidelijke lege statussen en logging van zoekopdrachten.

De interface die je in Lovable hebt gebouwd blijft onaangetast - de verbeteringen vinden plaats onder de motorkap van hetzelfde zoekveld. De code blijft gedocumenteerd en leesbaar voor AI, zodat je snel kunt blijven itereren. Dit maakt deel uit van het [Launch Ready-pakket](https://launchstudio.eu/nl/#packages), uitgevoerd door de engineers van Manifera vanuit Amsterdam en Ho Chi Minhstad, met elf jaar productie-ervaring voor opdrachtgevers als Vodafone en TNO.

Verliest jouw zoekveld geruisloos klanten? [Beschrijf je project](https://launchstudio.eu/nl/#contact) en ontvang binnen één werkdag een concrete analyse.

## Filters, facetten en de rest van vinden wat je zoekt

Zoeken is slechts de helft van hoe mensen navigeren. De andere helft bestaat uit filteren, en AI-apps gaan hier vaak op een specifieke manier de mist in: filters die op zichzelf prima werken, maar elkaar tegenwerken zodra je ze combineert.

**Filters moeten zoekresultaten verfijnen, niet vervangen.** Een veelvoorkomend AI-patroon past een gekozen filter toe op de complete database en gooit de ingevoerde zoekterm weg. Het selecteren van een categorie na het intypen van een zoekopdracht verbreedt dan plotseling de resultaten. Gebruikers ervaren dit alsof de app hen negeert.

**Toon actieve filters duidelijk.** Laat actieve filters zien als verwijderbare tags (chips), inclusief een knop om alles in één keer te wissen. Als gebruikers niet zien waarom een lijst beperkt is, denken ze dat het aanbod leeg is.

**Aantallen voorkomen doodlopende wegen.** Door direct te tonen hoeveel items er achter elke filteroptie zitten op basis van de huidige zoekterm, voorkom je dat mensen op filters klikken die nul resultaten opleveren. Dit vraagt om een snelle aggregatiequery per facet - goedkoop met indexen, traag zonder.

**Maak filters deelbaar via de URL.** Filterstatussen in de URL zorgen ervoor dat gebruikers een specifieke zoekopdracht kunnen bookmarken of doorsturen naar een collega. AI-gegenereerde apps bewaren dit vaak alleen in het componentgeheugen, waardoor een paginarefresh alles wist - een detail waardoor software amateuristisch aanvoelt.

**Kies logische standaarden.** Sorteren op "nieuwste" is zelden de juiste keuze voor een productcatalogus, maar wel voor een berichtenlijst. Wat de standaardsortering ook is: leg duidelijk uit hoe de resultaten geordend zijn.

**Analyseer filtergebruik.** Wordt een filter nooit gebruikt? Verwijder het. Zoeken gebruikers voortdurend naar eigenschappen die eigenlijk een filter zouden moeten zijn (zoals maat, regio of status)? Dan is dat een waardevol productsignaal.

Het goed inrichten van deze interacties heeft doorgaans meer impact op de ervaren kwaliteit dan geavanceerde relevantietuning, en het is een kwestie van een dag werk.

## Zoeken op een mobiele telefoon is een andere functionaliteit

Het merendeel van de zoekopdrachten in compacte SaaS-applicaties vindt plaats op mobiele apparaten. De beperkingen van een telefoonscherm veranderen wat een goede implementatie vereist:

**Typen kost moeite.** Elk karakter vergt inspanning op een touchscreen, waardoor typfouttolerantie en zoeken op korte voorvoegsels op mobiel veel belangrijker zijn dan op een desktop. Een zoekfunctie die vier foutloos gespelde woorden vereist, wordt op mobiel simpelweg genegeerd.

**Suggesties werken beter dan complete resultaten.** Toon direct drie of vier relevante suggesties zodra de gebruiker begint met typen. Hierdoor kan iemand aantikken in plaats van doortypen - de grootste gebruiksvriendelijkheidsverbetering voor mobiel zoeken.

**Voer geen query uit bij iedere toetsaanslag.** Een netwerkverzoek per letterteken is duur voor je server en traag op een mobiele verbinding. Wacht tot de gebruiker een fractie van een seconde pauzeert (debouncing), verstuur dan één query en annuleer het vorige verzoek zodra er weer getypt wordt.

**Houd de zoekterm in beeld.** Gebruikers die door een lange lijst scrollen, vergeten wat ze precies hebben ingetypt. Een zoekbalk die verdwijnt achter een toetsenbord leidt tot frustratie en herhaald zoeken.

**Zorg dat filters op het scherm passen.** Een filterpaneel dat ontworpen is voor een desktop-sidebar werkt niet op een telefoon. Een compact uitschuifmenu (bottom sheet) met de twee of drie meestgebruikte filters werkt vele malen beter dan een complete filterlijst die niet met één duim te bedienen is.

Dit zijn beslissingen op het gebied van interface-ontwerp in plaats van pure database-engineering, maar ze bepalen voor een groot deel of gebruikers vinden wat ze zoeken.

## Echt voorbeeld

### Een onderdelencatalogus waar een derde van de zoekopdrachten niets opleverde

Wietse Kamphuis runde Onderdeelshop, een catalogus voor reserveonderdelen van landbouwmachines gericht op dealers in Friesland en Groningen. Het platform was gebouwd in Lovable en bevatte circa 18.000 artikelen. Dealers zochten dagelijks op onderdeelnummer, machinemodel of tekstuele omschrijving.

De klachten waren vaag - "de zoekfunctie werkt niet lekker" - dus de eerste stap was gericht meten. Uit de logging bleek dat maar liefst 34% van alle zoekopdrachten nul resultaten opleverde. De oorzaken waren bijna puur mechanisch: de zoekopdracht was hoofdlettergevoelig en doorzocht uitsluitend de producttitel. Onderdeelnummers die in het systeem met een koppelteken stonden maar door de dealer zonder streepje werden ingevoerd, gaven geen match. Machinemodellen met een spatie verschil faalden, en zoektermen die alleen in de beschrijving stonden bleven onvindbaar.

In vier werkdagen voerden we een gerichte optimalisatie door: een gecombineerde zoekvector over titel, onderdeelnummer, omschrijving en machinecompatibiliteit die automatisch door de database wordt bijgewerkt; Nederlandse taalconfiguratie voor stamherkenning; trigram similarity voor artikelnummers zodat koppeltekens en spaties geen rol meer spelen; relevantieweging met de hoogste prioriteit voor artikelnummers; GIN-indexering; een lege status met suggesties voor vergelijkbare nummers; en continue monitoring van mislukte zoekopdrachten.

**Resultaat:** het percentage zoekopdrachten zonder resultaat daalde van 34% naar minder dan 6%. De overgebleven nulmetingen leverden wekelijks een waardevol overzicht op van onderdelen die dealers zochten maar die de groothandel nog niet in het assortiment had - waarvan er direct drie structureel op voorraad zijn genomen.

> *"Ik dacht dat ik een probleem had met mijn assortiment. Maar het lag aan de zoekfunctie: een derde van mijn dealers kreeg te horen dat we artikelen niet hadden, terwijl ze gewoon in ons magazijn lagen."*
> - **Wietse Kamphuis, Oprichter, Onderdeelshop (Drachten)**

**Kosten & Doorlooptijd:** € 1.900 (full-text search, similarity-matching, indexering, logging en statussen voor lege resultaten) - afgerond in 4 werkdagen.

## Veelgestelde vragen

### Heb ik een speciale externe zoekservice nodig, zoals een gehoste zoekmachine?
Meestal niet zolang je onder enkele honderdduizenden records blijft. Postgres full-text search met goede indexering en de juiste taalconfiguratie volstaat voor vrijwel alle vroege en middelgrote SaaS-applicaties, zonder dat je een extra extern systeem hoeft te beheren en synchroniseren.

### Waarom mist mijn zoekbalk voor de hand liggende resultaten?
Dat wordt vrijwel altijd veroorzaakt door hoofdlettergevoeligheid, zoeken op slechts één kolom of het ontbreken van meervouds- en stamherkenning. Standaard gegenereerde zoekfuncties doen enkel een ruwe substring-match op één veld, wat faalt bij normaal menselijk zoekgedrag.

### Hoe voeg ik tolerantie voor typfouten toe aan Supabase?
Trigram-overeenkomsten (`pg_trgm`) in Postgres vangen typfouten uitstekend op en kunnen efficiënt worden geïndexeerd. Een bewezen aanpak is om eerst een exacte zoekopdracht uit te voeren en automatisch terug te vallen op fuzzy similarity wanneer die te weinig resultaten oplevert.

### Wat moet een pagina tonen als er geen resultaten zijn?
Toon altijd gerichte suggesties: vergelijkbare artikelen, een spellingsuggestie ("bedoelde je...?"), relevante categorieën of een knop om door het aanbod te bladeren. Een blanco pagina geeft de gebruiker de indruk dat je product niet bestaat.

### Hoe weet ik of mijn zoekfunctie daadwerkelijk tekortschiet?
Log elke zoekopdracht inclusief het aantal gevonden resultaten. Het percentage zoekacties met nul resultaten is vrijwel altijd hoger dan oprichters verwachten, en de lijst met mislukte termen vormt een van de meest waardevolle productdocumenten die je kunt bezitten.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Heb ik een speciale externe zoekservice nodig, zoals een gehoste zoekmachine?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Meestal niet zolang je onder enkele honderdduizenden records blijft. Postgres full-text search met goede indexering en de juiste taalconfiguratie volstaat voor vrijwel alle vroege en middelgrote SaaS-applicaties, zonder dat je een extra extern systeem hoeft te beheren en synchroniseren."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom mist mijn zoekbalk voor de hand liggende resultaten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dat wordt vrijwel altijd veroorzaakt door hoofdlettergevoeligheid, zoeken op slechts één kolom of het ontbreken van meervouds- en stamherkenning. Standaard gegenereerde zoekfuncties doen enkel een ruwe substring-match op één veld, wat faalt bij normaal menselijk zoekgedrag."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voeg ik tolerantie voor typfouten toe aan Supabase?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Trigram-overeenkomsten (pg_trgm) in Postgres vangen typfouten uitstekend op en kunnen efficiënt worden geïndexeerd. Een bewezen aanpak is om eerst een exacte zoekopdracht uit te voeren en automatisch terug te vallen op fuzzy similarity wanneer die te weinig resultaten oplevert."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet een pagina tonen als er geen resultaten zijn?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Toon altijd gerichte suggesties: vergelijkbare artikelen, een spellingsuggestie, relevante categorieën of een knop om door het aanbod te bladeren. Een blanco pagina geeft de gebruiker de indruk dat je product niet bestaat."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe weet ik of mijn zoekfunctie daadwerkelijk tekortschiet?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Log elke zoekopdracht inclusief het aantal gevonden resultaten. Het percentage zoekacties met nul resultaten is vrijwel altijd hoger dan oprichters verwachten, en de lijst met mislukte termen vormt een van de meest waardevolle productdocumenten die je kunt bezitten."
      }
    }
  ]
}
</script>
