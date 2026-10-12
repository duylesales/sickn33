---
Titel: "Cursor Rules en Context: Gegenereerde Code Onderhoudbaar Houden"
Trefwoorden: Cursor, vibe coding developer, cursor rules bestand, codebase conventies ai, ai app beveiliging, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Cursor Rules en Context: Gegenereerde Code Onderhoudbaar Houden

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cursor Rules en Context: Gegenereerde Code Onderhoudbaar Houden",
  "description": "Waarom een Cursor-codebase na drie maanden uiteenvalt in drie verschillende programmeerdialecten, wat er in een rules-bestand thuishoort, hoe je het AI-model de juiste context geeft en de reviewgewoonten die je project leesbaar houden.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/cursor-rules-and-context-keeping-code-maintainable" }
}
</script>

De eerste maand in Cursor is voor de meeste solo-oprichters de meest productieve softwareontwikkelervaring die ze ooit hebben gehad. Maand vier is het moment waarop je een bestand opent, drie fundamenteel verschillende manieren aantreft om data uit dezelfde databasetabel op te halen, en je met geen mogelijkheid meer herinnert welke van de drie je als standaard had bedoeld.

Er is niets 'fout' gegaan. De tool deed telkens precies waar je om vroeg, en nam bij elke prompt een lokaal plausibele beslissing zonder te weten wat je een week eerder had vastgesteld. Consistentie is geen eigenschap die een taalmodel zomaar kan afleiden uit een codebase die het slechts in fragmenten ziet — het is iets wat je expliciet moet dicteren. Dat expliciet vastleggen kost weinig tijd en betaalt zich uit bij elke volgende prompt.

## Waarom AI-Gegenereerde Code Uiteenloopt

Drie mechanismen liggen hieraan ten grondslag, alle drie structureel van aard:

**Het model ziet een venster, niet je complete project.** Het werkt uitsluitend met de bestanden die in de actieve context staan, wat slechts een fractie is van je totale codebase. Patronen die zijn vastgelegd in een bestand dat het model niet ziet, hebben geen enkele invloed op wat het genereert.

**Elke prompt is een nieuwe onderhandeling.** De beslissing van gisteren over hoe foutmeldingen worden afgehandeld reist niet mee naar vandaag, tenzij dit direct zichtbaar is in de code die het model inspecteert of expliciet staat gedocumenteerd op een plek die het leest.

**Aannemelijke alternatieven zijn even eenvoudig beschikbaar.** Er zijn minstens vijf acceptabele manieren om een data-fetch te structureren. Zonder sturing kiest het model willekeurig een optie, waardoor de spreiding over je project vrijwel toevallig tot stand komt.

Het resultaat is een applicatie waarvan elk los bestand op zichzelf logisch oogt, maar die als geheel volstrekt onsamenhangend is — precies de faalmodus die software na zes maanden onveranderbaar maakt en onoverdraagbaar voor een nieuwe ontwikkelaar.

## Rules-bestanden: Vastleggen Hoe Dit Project Functioneert

Cursor leest regels op projectniveau (via `.cursorrules` of vergelijkbare configuratie) en past deze direct toe op alles wat het genereert. Dit is het kwartier met het allerhoogste rendement voor iedereen die op deze manier bouwt, en toch maakt het merendeel van de oprichters er nooit een aan.

Wat hierin thuishoort zijn geen persoonlijke stijlvoorkeuren, maar architectuurbeslissingen die onder geen beding mogen variëren:

**Data-toegang.** "Alle database-interacties verlopen uitsluitend via functies in deze specifieke directory. Schrijf nooit rechtstreeks een query binnen een UI-component." Eén enkele regel die het probleem van concurrerende stijlen direct oplost.

**Beveiligingsinvarianten.** "Elke tabel moet Row Level Security (RLS) hebben ingeschakeld. Gebruik nooit de service role key in code aan de clientzijde. Vertrouw nooit een parameter uit de request body voor autorisatie." Dit zijn de principes die door AI gegenereerde code het vaakst schendt, en het expliciet uitschrijven voorkomt het leeuwendeel van deze fouten.

**Validatie.** "Valideer aan de serverzijde met het gedeelde schema; checks aan de clientzijde dienen uitsluitend voor de gebruikerservaring."

**Foutafhandeling.** Welk patroon wordt gehanteerd, wat wordt gelogd, en wat krijgt de eindgebruiker te zien?

**Projectstructuur.** Waar nieuwe bestanden geplaatst worden, hoe ze genoemd worden, en wat in een component hoort versus in een service-laag.

**Verboden patronen,** expliciet benoemd: "Voeg geen nieuwe packages of dependencies toe zonder uitdrukkelijke toestemming. Introduceer geen tweede state management library. Maak geen nieuwe databasetabel aan zonder migratiebestand."

Houd het beknopt. Een regelsbestand dat niemand bijhoudt loopt snel achter op de werkelijkheid, en een lijst van veertig punten houdt niemand actueel. Tien tot vijftien regels die de werkelijk kritieke beslissingen afdekken werken veel beter dan een vuistdik document.

## Context: Het Model Bieden Wat Het Nodig Heeft voor Consistentie

Regels beschrijven het beleid; context levert de specifieke voorbeelden.

**Verwijs naar bestanden die het gewenste patroon al toepassen.** Wanneer je om een nieuwe functionaliteit vraagt, neem dan een bestaande vergelijkbare module mee in de context. Een model dat één goed voorbeeld krijgt, volgt die structuur nauwgezet. Dat werkt veel betrouwbaarder dan het patroon in abstracte woorden proberen uit te leggen.

**Houd het databaseschema zichtbaar.** Datastructuren zijn het onderdeel waar AI-code het meest ingrijpend de mist in gaat. Een model dat het actuele schema kan inzien, stopt met het verzinnen van kolomnamen die 'bijna' kloppen.

**Benoem het doel van de code, niet alleen de actie.** "Dit draait op de server en verwerkt financiële transacties" levert fundamenteel andere code op dan "schrijf een functie die een betaling opslaat".

**Wees kraakhelder over wat níet gewijzigd mag worden.** Het model zal met alle plezier omliggende code refactoren, tenzij je expliciet de grenzen aangeeft.

## Documentatie Die Tegelijk Dient als Prompt-materiaal

Hier ligt een enorme efficiëntiewinst. De documentatie die jouw codebase begrijpelijk maakt voor een mens — een korte architectuurnotitie, een beknopt overzicht van het datamodel, een lijstje met conventies — is exact hetzelfde materiaal dat zorgt voor consistente output van het AI-model.

Eén keer geschreven bedient het drie doelgroepen tegelijk: jou over vier maanden, de freelance engineer die je later inhuurt, en het AI-model bij iedere afzonderlijke prompt. Dat is een uitzonderlijk hoog rendement voor één pagina tekst, en het overtuigt zelfs oprichters die documentatie normaliter als tijdverspilling zien.

## Het Databaseschema Maatgevend Houden

Eén specifieke discipline verdient extra aandacht, omdat het de allerduurste vorm van inconsistentie voorkomt:

Je databaseschema hoort vastgelegd te zijn in migratiebestanden binnen je git-repository, en niet handmatig aangepast te worden via een grafisch dashboard van Supabase of vergelijkbare tools. Wanneer het schema in de codebase leeft, kan het model het zien, zijn wijzigingen traceerbaar via code reviews, en blijven ontwikkel-, staging- en productieomgevingen synchroon. Wanneer aanpassingen alleen in een webdashboard plaatsvinden, gaat gegenereerde code gokken, gaan omgevingen uit elkaar lopen en weet niemand meer wat de exacte staat van de data is.

Dit weegt in een AI-gedreven workflow zwaarder dan traditioneel, juist omdat het model voortdurend structuren probeert af te leiden.

## Reviewgewoonten Die Schaalbaar Blijven

**Lees aandachtig wat je accepteert.** Niet om opmaakdetails te controleren, maar om de aannames te spotten die je niet expliciet had benoemd. Dit is de belangrijkste gewoonte die ontwikkelaars met een schone Cursor-codebase onderscheidt van hen bij wie het project verzandt.

**Verwijder dubbelingen onmiddellijk.** Wanneer het model een tweede implementatie van een bestaande functie schrijft, voeg ze dan direct samen in plaats van te wachten tot er een derde variant opduikt.

**Laat het model zijn eigen code toelichten** wanneer een voorgestelde wijziging groter uitvalt dan verwacht. De toelichting onthult vaak een verkeerde aanname die je met één corrigerende zin kunt rechtzetten.

**Houd commits compact en duidelijk omschreven.** Je commit-geschiedenis dient als waardevolle context voor zowel een toekomstige collega als een volgende prompt.

## Wanneer Twee Mensen in Dezelfde Repository Werken

Al het voorgaande verandert dan van een goed advies in een absolute noodzaak.

Twee ontwikkelaars die onafhankelijk van elkaar prompts uitvoeren veroorzaken inconsistenties in dubbel tempo, omdat beiden patronen introduceren die de ander niet kent. De werkwijze die standhoudt: een gedeeld rules-bestand dat beiden hanteren, duidelijke afspraken over eigenaarschap van modules, en wederzijdse code review van elkaars AI-output — het beoordelen van gegenereerde code van een collega voelt ongewoon, maar is net zo essentieel als bij handgeschreven code.

Teams die dit overslaan lopen niet na vier maanden, maar al na zes weken tegen een onbeheersbare codebase aan.

## Signalen Dat Je Codebase Begint af te Dwalen

- Je aarzelt om een component aan te passen omdat je niet overziet wat er elders van afhangt.
- Je ontdekt twee functies die exact hetzelfde doen onder verschillende namen.
- Een prompt vereist een ellelange inleiding over je project voordat het model iets bruikbaars genereert.
- Nieuwe features toevoegen kost meer tijd dan drie maanden geleden, zonder dat ze complexer zijn.
- Je kunt het datamodel niet uitleggen zonder eerst de databaseconsole te openen.

Twee van deze signalen betekenen dat technisch onderhoud over tijd is. Het is vele malen goedkoper om dit nu op te lossen dan na de bouw van je volgende functionaliteit.

## Een Onderhoudsroutine van Eén Uur per Maand

Lees het regelsbestand door en pas het aan naar hoe je tegenwoordig daadwerkelijk werkt. Voeg gedupliceerde functies samen. Werk de architectuurnotitie bij als er modules zijn verschoven. Controleer of de migraties in de repository overeenkomen met de productiedatabase. Verwijder dode code die nergens meer wordt aangeroepen.

Eén uur per maand houdt een gegenereerde codebase in een staat waarin zowel jij als het model logisch kunnen redeneren over de werking — en daar draait alles om. Zodra dat overzicht verdwijnt, stort je ontwikkelsnelheid in en wordt de tool die je snel maakte de reden dat je stilstaat.

## Wanneer de Consistentie Al Verloren Is

Ben je dat station al gepasseerd, dan is een complete herbouw niet de oplossing. Het antwoord is een consolidatieslag: breng de botsende patronen in kaart, kies per vraagstuk één standaard, migreer de afwijkende code naar die standaard, stel het rules-bestand op om herhaling te voorkomen, en voeg geautomatiseerde tests toe rondom kritieke onderdelen zodat de opschoning veilig verloopt.

Dat is een vast onderdeel van wat LaunchStudio doet wanneer we een AI-gebouwd product productieklaar maken — naast toegangsbeheer, betalingsverkeer en infrastructuur — simpelweg omdat een ondoorzichtige codebase een omgeving is waarin security-fixes onbetrouwbaar worden. Het eindresultaat blijft netjes, gedocumenteerd en AI-leesbaar, zodat je na afloop vlot kunt blijven prompten zonder je vertrouwde werkwijze te verliezen.

De engineers zijn van Manifera, met elf jaar ervaring met productiesystemen voor opdrachtgevers als Vodafone, TNO en CFLW, vanuit Amsterdam en Ho Chi Minhstad. [Beschrijf je project](https://launchstudio.eu/nl/#contact) voor een eerlijk oordeel over de vraag of consolidatie nodig is (meestal binnen één werkdag), of bekijk de [pakketten](https://launchstudio.eu/nl/#packages).

## Kiezen Wat Je Juist Níet Laat Genereren

Een subtiele discipline die software beheersbaar houdt: vooraf bepalen welke onderdelen je bewust zélf schrijft.

**Het datamodel.** Schema-beslissingen zijn duur om later te herstellen en verdienen denkwerk vooraf in plaats van automatische generatie. Laat het model gerust het migratiebestand schrijven nadat jij de structuur hebt vastgesteld.

**Autorisatielogica.** De regels die bepalen wie wat mag zien coderen je bedrijfslogica, en vormen precies de plek waar een ogenschijnlijk werkende AI-code levensgevaarlijk is. Schrijf deze regels zelf uit en vraag het model hooguit om ze te controleren tegen je beleid.

**Alles wat met geld te maken heeft.** Berekeningen, afrondingen, valuta en btw. AI-code genereert dit overtuigend, maar een subtiele afrondingsfout wordt pas ontdekt door een boze klant of de belastingdienst, niet door een simpele test.

**De interfaces tussen de deelsystemen.** Wat een functie accepteert en teruggeeft, wat een API-endpoint verwacht. Zodra deze contracten vastliggen, is codegeneratie daarbinnen veilig en snel.

Dit is geen kwestie van wantrouwen jegens AI. Het gaat erom je eigen aandacht te richten op de plekken waar fouten kostbaar zijn, en het model het brede speelveld te laten vullen waar fouten goedkoop en direct zichtbaar zijn.

## Echt voorbeeld

### Drie Manieren om een Klant op te Halen, en Niemand Wist Welke Klopte

Pepijn Aalbers bouwde Offertetool in Cursor: een calculatie- en offertetool gebruikt door circa 120 installatie- en bouwbedrijven in Noord-Holland. Hij had er zeven maanden alleen aan gewerkt en nam vervolgens een parttime ontwikkelaar in de arm om sneller te kunnen uitbreiden.

Tijdens de overdracht kwam het probleem direct aan het licht. Er waren drie verschillende manieren waarop klantgegevens werden ingeladen, twee afzonderlijke foutafhandelingspatronen, en twee verschillende validatiemethoden. Drie databasetabellen waren rechtstreeks via het Supabase-dashboard aangepast en stonden nergens in de repository, waardoor de lokale ontwikkelomgeving van de nieuwe engineer direct vastliep ten opzichte van productie.

Geen van beiden kon aangeven welk patroon de bedoeling was, simpelweg omdat alle drie de methoden correct waren op de dag dat ze werden geprompt.

Zes werkdagen werk: één centrale data-toegangslaag waar de andere twee naar gemigreerd werden; invoervalidatie geconsolideerd in gedeelde schema's voor client en server; de drie ontbrekende tabellen vastgelegd in versiebeheerde migraties zodat git weer de enige bron van waarheid werd; een rules-bestand van vijftien regels met harde afspraken over datatoegang, RLS en validatie; een architectuurnotitie van één pagina; en geautomatiseerde tests rondom de offerteberekeningen zodat het opschonen direct geverifieerd kon worden.

**Resultaat:** de eerste nieuwe feature van de nieuwe ontwikkelaar stond binnen drie dagen live in plaats van de twee weken die de eerdere poging had gekost. Pepijn gaf aan dat prompts sindsdien direct code produceren die aansluit op de bestaande architectuur, zonder dat hij bij elke opdracht opnieuw hoeft uit te leggen hoe het project in elkaar zit.

> *"Ik was al maanden aan het vechten met mijn eigen codebase en gaf de tool de schuld. Maar de tool had geen flauw idee van wat ik eerder had besloten, omdat ik het nergens had opgeschreven."*
> — **Pepijn Aalbers, Oprichter, Offertetool (Alkmaar)**

**Kosten & Doorlooptijd:** € 2.600 (consolidatieslag, schemamigraties, regelsbestand, architectuurnotitie en testsuite) — afgerond in 6 werkdagen.

## Veelgestelde vragen

### Wat hoort er precies in een Cursor rules-bestand te staan?

De beslissingen die onder geen beding mogen variëren: hoe datatoegang verloopt, beveiligingsinvarianten (zoals nooit een service key aan de clientkant gebruiken), waar validatie plaatsvindt, foutafhandeling, projectstructuur en expliciet verboden patronen. Houd het beknopt: tien tot vijftien regels die actueel worden gehouden.

### Waarom wordt door AI gegenereerde code na verloop van tijd inconsistent?

Omdat het model uitsluitend werkt met de bestanden die op dat moment in het contextvenster staan in plaats van je hele project, en elke prompt een nieuwe lokale beslissing is. Zonder regels en voorbeeldcode kiest het willekeurig uit gelijkwaardige patronen.

### Moet mijn databaseschema per se in de git-repository staan?

Ja, absoluut. Migraties in de repository houden ontwikkel- en productieomgevingen synchroon, maken wijzigingen inzichtelijk bij reviews en stellen het AI-model in staat de werkelijke datastructuur te lezen. Schema-aanpassingen via een dashboard zorgen ervoor dat AI gaat gokken en omgevingen uit de pas lopen.

### Hoe voorkom ik wildgroei wanneer twee mensen met AI in dezelfde codebase werken?

Door een gedeeld regelsbestand dat beiden naleven, duidelijke taakverdeling per module, en wederzijdse code review van elkaars gegenereerde code. Twee mensen die los van elkaar prompts draaien, verdubbelen het tempo waarin de codebase divergeert.

### Mijn codebase is al inconsistent geworden. Moet ik alles opnieuw bouwen?

Nee. Een gerichte consolidatieslag — kies per onderdeel één patroon, migreer de afwijkingen, leg het schema vast in migraties, stel een regelsbestand op en voeg tests toe rond kritieke logica — is veel goedkoper dan opnieuw beginnen en behoudt al het werk dat je al hebt gedaan.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat hoort er precies in een Cursor rules-bestand te staan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De beslissingen die niet mogen variëren: datatoegang, beveiligingsregels, server-validatie, foutafhandeling, mappenstructuur en verboden patronen — 10 tot 15 actuele regels."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom wordt door AI gegenereerde code na verloop van tijd inconsistent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het model baseert zich op geopende bestanden in plaats van het hele project; elke prompt is een nieuwe afweging tussen plausibele patronen."
      }
    },
    {
      "@type": "Question",
      "name": "Moet mijn databaseschema per se in de git-repository staan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. Versiebeheerde migraties houden omgevingen synchroon, maken reviews mogelijk en tonen het model de echte datastructuur."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom ik wildgroei wanneer twee mensen met AI in dezelfde codebase werken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Via een gedeeld regelsbestand, afgebakende domeinen en wederzijdse review van gegenereerde code; zonder dit verdubbelt het tempo van wildgroei."
      }
    },
    {
      "@type": "Question",
      "name": "Mijn codebase is al inconsistent geworden. Moet ik alles opnieuw bouwen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Een consolidatieslag waarbij je één patroon kiest, migraties vastlegt en tests toevoegt is vele malen goedkoper en behoudt wat je hebt gebouwd."
      }
    }
  ]
}
</script>
