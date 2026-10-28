---
Titel: "Van Bolt naar Next.js: Overstappen op een Framework Dat U Beheert"
Trefwoorden: bolt naar next.js, migratie, serverrendering, frameworkkeuze, van prototype naar productie, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Van Bolt naar Next.js: Overstappen op een Framework Dat U Beheert

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Van Bolt naar Next.js: Overstappen op een Framework Dat U Beheert",
  "description": "Wanneer een Bolt-prototype naar een volwaardig framework moet, wat er werkelijk meegaat, de volgorde die het product laat draaien, en het eerlijke argument om het helemaal niet te doen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-13",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/bolt-to-next-js-moving-onto-a-framework-you-control" }
}
</script>

Bolt levert doorgaans een single-page application op: een React-frontend gebouwd met Vite, die vanuit de browser met Supabase praat. Voor een prototype is dat precies goed, en voor veel producten blijft het voor onbepaalde tijd goed.

Er zijn specifieke redenen om naar een volwaardig framework te gaan, en er zijn vaker genoemde redenen die bij nadere beschouwing niet standhouden. Het verschil kennen bespaart een maand.

## De Redenen Die Echt Zijn

**Uw publieke pagina's moeten gevonden worden.** Een marketingsite, een blog, publieke overzichten, documentatie. Een single-page application maakt die trager en kwetsbaarder voor zoekmachines, en serverrendering is de duurzame oplossing. Dit is met afstand de meest voorkomende echte reden.

**U hebt substantiële logica op de server nodig.** Niet één of twee functies, die elk platform biedt, maar een echte backend: integraties, gepland werk, bedrijfsregels die niet in een browser mogen draaien. Een framework met serverroutes geeft u één codebase in plaats van twee.

**U bent het ophalen van data alleen in de client ontgroeid.** Elk scherm wacht op verzoeken vanuit de browser, met overal laadtoestanden, terwijl de data op de server kon worden opgehaald en met de pagina meegestuurd.

**De eerste betekenisvolle weergave is te traag en anders niet op te lossen.** Echt bij producten met veel content, meestal op andere manieren op te lossen bij een applicatie achter een login.

## De Redenen Die Het Niet Zijn

**"Het is professioneler."** Niemand koopt een framework. Klanten ervaren snelheid, betrouwbaarheid, en of het product doet wat ze nodig hebben.

**"We hebben het later misschien nodig."** Later is wanneer de reden specifiek zal zijn en de migratie erdoor gerechtvaardigd wordt.

**"Een developer zei het."** Soms klopt het. Vraag welk probleem het oplost en of u dat probleem nu hebt.

**"De prestaties zijn slecht."** Vaak ontbrekende indexen, N+1-queries, te grote afbeeldingen of geen caching. Die reizen allemaal met u mee.

Een product achter een login, gebruikt door mensen die al klant zijn, zonder publieke pagina's die moeten ranken, heeft heel weinig te winnen.

## Wat Meegaat en Wat Niet

Het geruststellende deel: het meeste werk gaat mee.

React-componenten gaan bijna ongewijzigd mee. Uw Supabase-schema, policies en functies worden niet aangeraakt. Bedrijfslogica verhuist met bescheiden aanpassingen. Styling gaat mee.

Wat echt werk vraagt: de routingconventies verschillen; het ophalen van data verhuist van aanroepen in de browser naar servercomponenten of loaders, en dat is het grootste afzonderlijke stuk; omgevingsvariabelen worden anders benoemd en blootgesteld, en dat verkeerd doen is hoe een geheim in een bundel belandt; authenticatie verhuist naar een patroon dat de server kent, met cookies in plaats van browseropslag, wat een verbetering is en werk kost; en uw build- en deploymentconfiguratie wordt vervangen.

Voor een typische Bolt-applicatie van twintig tot veertig componenten is dit één tot drie weken, afhankelijk van hoeveel ophalen van data door de interface is verspreid.

## De Volgorde Die het Product Laat Draaien

Leg het werk aan functies niet een maand stil. Migreer in fasen.

Begin met de publieke pagina's - marketing, blog, alles wat moet ranken - als een nieuwe applicatie op hetzelfde domein, waarbij de bestaande applicatie nog alles achter de login serveert. Dat levert direct het belangrijkste voordeel op en raakt niets waar klanten van afhangen.

Verplaats daarna de schermen van de applicatie één voor één, te beginnen met de eenvoudigste en de minst gebruikte, en controleer elk voordat u aan het volgende begint. Beide applicaties delen de hele tijd dezelfde database, dus er is helemaal geen datamigratie.

Daarna authenticatie, de stap met zichtbaar effect voor gebruikers, omdat sessies eindigen. Doe het op een rustig uur, met aankondiging.

Verwijder daarna de oude applicatie, zodra er niets meer naartoe routeert.

In elke fase werkt het product. Loopt de migratie vast - en dat gebeurt, wanneer er iets urgenters opduikt - dan zit u in een werkende toestand in plaats van halverwege een herschrijving.

## De Middenweg Die het Overwegen Waard Is

Overweeg vóór u zich vastlegt op een migratie of u twee applicaties nodig hebt in plaats van één.

Een statisch gegenereerde marketingsite en blog, volledig gescheiden, op hetzelfde domein in de root, met de bestaande Bolt-applicatie geserveerd onder `/app`. De publieke pagina's krijgen op de server opgebouwde HTML, snelheid en indexeerbaarheid; de applicatie blijft precies zoals ze is.

Dat is een dag werk in plaats van drie weken, het pakt de meest voorkomende echte reden voor migreren aan, en het laat de migratie van de applicatie een beslissing die u later op haar eigen merites kunt nemen. Voor een groot deel van de oprichters die hiernaar vragen, is dit het juiste antwoord.

## Wat Er Verandert in het Werken met AI-Tools

Eén gevolg van migreren wordt zelden genoemd en doet ertoe voor producten die zo zijn gebouwd: de tools gedragen zich anders tegen een volwaardig framework dan tegen de applicatie die ze zelf genereerden.

Bolt en vergelijkbare tools zijn op hun best bij het vanaf nul maken van een op zichzelf staande applicatie. Tegen een gevestigde frameworkcodebase met servercomponenten, routeconventies en eigen patronen past een algemene assistent zoals Cursor of Claude Code beter - die leest de bestaande code, volgt de afspraken die hij vindt, en maakt afgebakende wijzigingen.

Een migratie is dus meestal ook een verandering in hoe u werkt: van functies beschrijven aan een bouwer die ze genereert, naar een codebase bewerken met een assistent die helpt. Dat is een echte verschuiving, en oprichters die geen developer zijn, vinden die soms moeilijker in plaats van makkelijker, en dat is het weten waard voordat u zich vastlegt.

Twee dingen maken de overgang comfortabel. Een afsprakenbestand dat uw patronen beschrijft, wat in een frameworkproject meer uitmaakt, omdat er meer beslissingen zijn om consistent in te zijn. En een werkende testsuite, ook een kleine, omdat een assistent die een grotere codebase bewerkt enorm baat heeft bij de mogelijkheid te controleren of hij iets brak.

Spreekt geen van beide u aan, dan is dat op zichzelf een argument voor de middenweg: houd de applicatie zoals ze is, en los het specifieke probleem op dat u werkelijk hebt.

## Het Framework Kiezen, Kort

Is een migratie echt gerechtvaardigd, dan doet de keuze tussen de serieuze opties er minder toe dan oprichters verwachten, en de beslissing kan in een middag worden genomen.

**Next.js** is de standaard voor React-applicaties, en dat is wat Bolt oplevert, met het grootste ecosysteem en het meeste materiaal waarvan codeerassistenten hebben geleerd. Dat laatste is niet onbelangrijk in een product dat zo is gebouwd - een assistent schrijft betere Next.js dan bijna wat dan ook, simpelweg omdat er meer van bestaat.

**Remix** heeft in verschillende opzichten een schoner datamodel en een kleinere gemeenschap.

**Astro** is uitstekend wanneer het grootste deel van uw site content is met eilanden van interactiviteit, wat een product met veel marketing goed beschrijft en een applicatie slecht.

**SvelteKit** en andere zijn prima en betekenen dat u uw React-componenten weggooit, en dat is het meeste van wat meegaat.

Voor een Bolt-applicatie met een echte reden om te verhuizen, is Next.js de verstandige standaard en ligt de bewijslast bij elk alternatief. De ene echte splitsing is Astro voor een product dat grotendeels content is - en in dat geval bereikt de optie van een dag, een aparte statische marketingsite, hetzelfde zonder de applicatie aan te raken.

## Stel een Budget en een Stopregel

Migraties van deze soort hebben een kenmerkende mislukking: ze duren twee keer zo lang als gepland, het werk aan functies stopt, en drie maanden later is het product voor klanten niet veranderd terwijl de oprichter elke dag druk was.

Twee beschermingen, vooraf met uzelf afgesproken.

**Een tijdsbudget met een evaluatiemoment.** Drie weken, met een eerlijke beoordeling aan het eind van week twee. Zijn de publieke pagina's klaar en gaan de schermen van de applicatie traag, dan is daar stoppen een legitieme uitkomst - u hebt het voordeel dat het werk rechtvaardigde, en de rest kan voor onbepaalde tijd wachten.

**Een regel dat het product blijft opleveren.** Minstens één zichtbare verbetering voor klanten per week tijdens de migratie, hoe klein ook. Het houdt u in contact met de mensen die u betalen en voorkomt dat u stilletjes een kwartaal aan infrastructuur besteedt.

De gefaseerde aanpak hierboven maakt beide mogelijk, omdat er geen punt is waarop de migratie af moet zijn om de moeite waard te zijn geweest. Dat is de eigenschap om te eisen in elk plan dat iemand u voorlegt: is het antwoord op "wat gebeurt er als we halverwege stoppen" iets anders dan "dan houden we het deel dat af is", dan is het plan een herschrijving in de kleren van een migratie, en herschrijvingen zijn waar kleine producten een jaar verliezen.

## Dit Inrichten

Voor een product met een echte reden om te migreren, kost dit doorgaans één tot drie weken: de reden specifiek benoemd en getoetst aan de alternatieven, publieke pagina's eerst verplaatst als aparte applicatie op hetzelfde domein, schermen één voor één gemigreerd van minst naar meest gebruikt met beide applicaties op dezelfde database, het ophalen van data naar de server verplaatst, omgevingsvariabelen hernoemd met de bundel gecontroleerd op geheimen, authenticatie gemigreerd naar een cookiegebaseerd patroon dat de server kent, op een rustig uur met aankondiging, de oude applicatie opgeheven zodra er niets meer naartoe routeert, en het geheel in elke fase werkend gehouden.

LaunchStudio doet deze migratie, en vertelt oprichters ook wanneer het alternatief van een dag volstaat - en dat is vaak zo. De engineers zijn van Manifera - elf jaar, 160+ projecten, vanuit Amsterdam en Ho Chi Minh-stad.

[Vertel ons wat u probeert op te lossen](https://launchstudio.eu/nl/#contact) en wij vertellen u of een migratie de manier is om het op te lossen.

## Echt voorbeeld

### Drie Weken, Daarna Eén Dag

Ties Grootveld bouwde Aanbestedingsradar met Bolt: een dienst die Nederlandse publicaties van aanbestedingen volgt en 90 abonnees waarschuwt voor relevante kansen, €79 per maand.

Hem was herhaaldelijk verteld dat hij naar Next.js moest. Zijn genoemde redenen waren dat zijn marketingpagina's niet rankten en dat het product traag aanvoelde.

De beoordeling haalde de twee uit elkaar. De marketingpagina's hadden echt serverrendering nodig - ze waren een single-page application die een leeg document serveerde, en daarom was geen van zijn elf artikelen geïndexeerd. De traagheid van de applicatie was iets heel anders: de aanbestedingslijst haalde elke rij op waarmee een bedrijf ooit was gematcht en pagineerde in de browser, wat voor zijn grootste abonnee 41.000 rijen waren.

Eén werkdag, geen drie weken: de marketingsite en blog opnieuw gebouwd als statisch gegenereerde applicatie die echte HTML serveert, gedeployd in de root van het domein, met de bestaande Bolt-applicatie verplaatst naar `/app` en uitgesloten van indexering; canonieke URL's en een sitemap toegevoegd; de aanbestedingslijst omgezet naar cursorpaginering met een index op de matchtabel, wat de lijst van de grootste abonnee van 9 seconden naar 210 milliseconden bracht; en een notitie geschreven dat een volledige frameworkmigratie beschikbaar blijft als logica op de server dat ooit rechtvaardigt.

**Resultaat:** negen van de elf artikelen werden binnen een maand geïndexeerd en voor het eerst kwamen er organische aanvragen binnen. Het snelheidsprobleem van de applicatie, dat de migratie niet zou hebben opgelost, werd opgelost met een index en een aangepaste query. Ties heeft de applicatie niet gemigreerd en, twee jaar later, is dat ook niet nodig geweest.

> *"Iedereen zei me dat het framework het probleem was. De marketingpagina's moesten inderdaad worden opgelost. Het trage scherm was een query die eenenveertigduizend rijen ophaalde, en die zou in Next.js net zo traag zijn geweest."*
> - **Ties Grootveld, Oprichter, Aanbestedingsradar (Den Haag)**

**Kosten & Doorlooptijd:** €2.400 (statische marketingapplicatie met op de server opgebouwde HTML, verplaatsen van de applicatie en uitsluiten van indexering, canonieke URL's en sitemap, cursorpaginering met indexering, gedocumenteerde migratieoptie) - afgerond in 1 werkdag.

## Veelgestelde vragen

### Wanneer moet een Bolt-app naar Next.js?

Wanneer publieke pagina's moeten ranken, wanneer u substantiële logica op de server nodig hebt, of wanneer data op de server moet worden opgehaald. Niet omdat een framework professioneler klinkt of omdat iets traag is om redenen die met u meereizen.

### Wat gaat er mee bij de migratie?

Componenten, bedrijfslogica, styling en uw hele Supabase-schema en policies. Routing, het ophalen van data, omgevingsvariabelen, authenticatie en deploymentconfiguratie vragen allemaal werk.

### Hoe lang duurt het?

Eén tot drie weken voor een typische applicatie van twintig tot veertig componenten, het grootste deel ervan het verplaatsen van het ophalen van data van de browser naar de server.

### Kan ik migreren zonder het product stil te leggen?

Ja, en dat moet u ook. Verplaats eerst de publieke pagina's, daarna schermen één voor één van minst naar meest gebruikt, met de hele tijd dezelfde database, en authenticatie als laatste.

### Is er een goedkoper alternatief?

Vaak wel. Een aparte statisch gegenereerde marketingsite in de root van het domein, met de bestaande applicatie onder `/app`, is een dag werk en pakt de meest voorkomende echte reden voor migreren aan.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wanneer moet een Bolt-app naar een volwaardig framework?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Wanneer publieke pagina's moeten ranken, substantiële logica op de server nodig is, of data op de server moet worden opgehaald - niet om professionaliteit of onverklaarde traagheid."
      }
    },
    {
      "@type": "Question",
      "name": "Wat gaat er mee bij migreren van Bolt naar Next.js?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Componenten, bedrijfslogica, styling en het hele Supabase-schema. Routing, het ophalen van data, omgevingsvariabelen, auth en deployment moeten opnieuw."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt een migratie van Bolt naar Next.js?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Eén tot drie weken voor twintig tot veertig componenten, grotendeels bepaald door het verplaatsen van het ophalen van data van browser naar server."
      }
    },
    {
      "@type": "Question",
      "name": "Kan de migratie zonder downtime?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja - eerst publieke pagina's, daarna schermen één voor één op dezelfde database, met authenticatie als laatste."
      }
    },
    {
      "@type": "Question",
      "name": "Is er een goedkoper alternatief voor migreren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vaak: een aparte statische marketingsite in de root van het domein met de bestaande app onder /app, wat een dag werk is."
      }
    }
  ]
}
</script>
