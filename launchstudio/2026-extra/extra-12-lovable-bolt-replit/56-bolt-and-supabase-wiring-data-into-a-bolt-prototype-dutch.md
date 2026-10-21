---
Titel: "Bolt en Supabase: Data Aansluiten op een Bolt-Prototype"
Trefwoorden: bolt supabase, database-integratie, schemaontwerp, row level security, van prototype naar product, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Bolt en Supabase: Data Aansluiten op een Bolt-Prototype

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bolt en Supabase: Data Aansluiten op een Bolt-Prototype",
  "description": "Een Bolt-prototype met nepdata wordt een product wanneer er een echte database achter zit. Het schema ontwerpen voordat u ertegen genereert, de fouten die duur zijn om terug te draaien, en wat u als eerste doet.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-03",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/bolt-and-supabase-wiring-data-into-a-bolt-prototype" }
}
</script>

Een Bolt-prototype begint meestal met verzonnen data — arrays in de code, aannemelijke namen, alles aanwezig en consistent. Het demonstreert het product prachtig en het heeft geen geheugen.

Een echte database aansluiten is de stap die het verandert in iets wat mensen kunnen gebruiken, en het is de stap waarin beslissingen worden genomen die nu goedkoop zijn en over acht maanden duur. Het schema waartegen u genereert, bepaalt elk scherm, elke query en elke migratie die volgt.

## Ontwerp het Schema Voordat U Ertegen Genereert

De neiging is de tool te vragen een database toe te voegen en haar de structuur te laten bepalen. Ze levert iets op wat werkt, afgeleid van de schermen in plaats van van het bedrijf.

Een uur vooraf is veel meer waard dan het kost. Schrijf de dingen op waar uw product over gaat — de zelfstandige naamwoorden die een klant zou gebruiken — en hoe ze samenhangen. Organisaties hebben leden. Projecten horen bij een organisatie. Taken horen bij een project. Facturen verwijzen naar een project en een klant.

Drie beslissingen die u in dat uur bewust neemt, omdat alle drie later pijnlijk zijn om te veranderen.

**Uw tenantmodel.** Hoe wordt data tussen klanten gescheiden? Bijna altijd een organisatie-identificatie op elke tabel, de kolom waarop elke query filtert en waarnaar elke policy verwijst.

**Uw identificaties.** Willekeurige identificaties als primaire sleutels, met aparte leesbare referenties waar mensen een nummer moeten kunnen noemen.

**Uw naamgevingsafspraken.** Eén woord per concept, consequent, omdat het schema leert aan wat er daarna tegen schrijft — inclusief de tool.

Geef die beschrijving aan Bolt in plaats van het er een te laten verzinnen, en de gegenereerde code zal haar volgen.

## Begin met Minder Tabellen

Prototypes genereren enthousiast tabellen. Een product met vijf echte entiteiten krijgt er vijftien, waarvan verschillende één kolom bevatten die op een andere tabel thuishoort.

Begin met de kleinste set die het bedrijf weergeeft, en voeg toe wanneer een echte eis daarom vraagt. Een tabel later opsplitsen is eenvoudig; vier tabellen samenvoegen die één hadden moeten zijn niet, omdat elk scherm en elke query de verkeerde vorm heeft geleerd.

Hetzelfde geldt voor kolommen. Een veld dat later misschien nuttig is, is een veld om later toe te voegen, wanneer de betekenis bekend is.

## Zet Row-Level Security Direct Aan

Het allerbelangrijkste wanneer u Supabase aan een Bolt-applicatie koppelt: zet row-level security aan op elke tabel, met policies, vanaf de eerste tabel.

Het aan het begin doen betekent dat elk scherm wordt gebouwd tegen een database die scheiding al afdwingt, en dat alles wat kapot is direct opvalt. Het later doen betekent policies inbouwen in een applicatie die uitging van onbeperkte toegang, wat zowel meer werk is als veel waarschijnlijker een gat laat.

Policies zijn voorwaarden, en voor de meeste tabellen is de voorwaarde dezelfde: de organisatie van de rij komt overeen met de organisatie van de aanroeper. Schrijf haar één keer, pas haar consequent toe, en test haar met twee accounts voordat u er iets bovenop bouwt.

## Constraints Zijn Niet Optioneel

De data van een prototype wordt door u aangemaakt en is dus redelijk. De data van een product wordt aangemaakt door gebruikers, imports, integraties en AI-sessies, en dat zal niet zo zijn.

Zet de regels in de database: foreign keys zodat een rij niet kan verwijzen naar iets wat niet bestaat, not-null op de kolommen die het product echt nodig heeft, unieke constraints waar duplicaten een probleem zouden zijn, en checks waar een waarde een geldig bereik heeft.

Elk is één regel en elk overleeft elke toekomstige wijziging in uw applicatie, inclusief die geschreven door een tool die uw bedoelingen niet heeft gelezen.

## Vervang Nepdata Bewust

De overgang van verzonnen data naar een echte database is waar prototypes breken op manieren die moeilijk te diagnosticeren zijn, omdat de code is geschreven tegen data die altijd compleet en altijd consistent was.

Echte data heeft ontbrekende optionele velden, relaties die naar verwijderde dingen wijzen, lastige tekens, en hoeveelheden die een lijstpagina traag maken. Genereer een seedset met die eigenschappen voordat u de echte database aansluit in plaats van erna, zodat de mislukkingen gebeuren terwijl u kijkt.

En verwijder de nepdata volledig zodra de database is aangesloten. Terugvallen op verzonnen data wanneer een query niets teruggeeft, is een patroon dat in gegenereerde code voorkomt en de meest verwarrende categorie fouten oplevert die er is: een product dat lijkt te werken terwijl het informatie toont die niet bestaat.

## Queries Horen Achter een Grens

Een Bolt-applicatie praat direct vanuit de browser met Supabase, de opzet die het snel maakt om te bouwen en die kennis van de database over elk component verspreidt.

Binnen een week kennen dertig bestanden uw tabelnamen, uw kolomnamen en de vorm van uw joins. Een kolom hernoemen betekent dan dertig plekken zoeken, en een schemawijziging wordt een zoek-en-vervangoefening zonder manier om zeker te weten dat ze volledig is.

De oplossing is klein en het waard om vroeg te doen: zet datatoegang achter uw eigen functies. Eén module — of één per entiteit — die blootstelt wat de applicatie nodig heeft, met de queries erin. Componenten vragen om "de projecten van deze organisatie" in plaats van een query op te bouwen.

Drie voordelen, in oplopend belang. Het schema kan veranderen zonder de interface aan te raken. De beperking tot de huidige organisatie gebeurt op één plek, dus ze kan niet worden vergeten in een component dat later wordt geschreven. En een AI-sessie die een scherm toevoegt, pakt een bestaande functie in plaats van een nieuwe query te schrijven, en dat voorkomt dat het patroon zich opnieuw verspreidt.

Dit is dezelfde grens waarvoor elders in deze reeks wordt gepleit als verzekering tegen het wisselen van platform. De dagelijkse waarde ervan is groter: het is het verschil tussen een schema dat u kunt laten evolueren en een schema dat naar elke hoek van uw applicatie is gekopieerd.

## Opslag en Auth Zijn Ook Schemabeslissingen

Twee Supabase-functies worden tijdens het prototypen aangesloten en verdienen dezelfde bewuste behandeling als tabellen.

**Authenticatie** maakt een eigen gebruikerstabel aan, en de verleiding is daar alles over een persoon op te slaan. Houd in plaats daarvan een eigen tabel bij, met een eigen identificatie, gekoppeld aan de auth-identiteit — omdat rollen, lidmaatschap van organisaties, voorkeuren en alles wat uw product verder weet bij u horen en niet bij de authprovider. Dat maakt de provider ook vervangbaar, en het betekent dat de applicatiedata van een gebruiker wijzigingen in hoe hij inlogt overleeft.

**Opslag** heeft een padstructuur nodig die vóór de eerste upload wordt bepaald, omdat paden de manier zijn waarop policies worden uitgedrukt. Eigenaar eerst — organisatie, dan gebruiker of record, dan een gegenereerde bestandsidentificatie — en een databaserij per bestand die vastlegt wie het uploadde, wanneer, het pad, de grootte en het type. Een indeling achteraf toepassen op bestanden die al over een bucket verspreid staan, betekent objecten verplaatsen en elke opgeslagen URL herschrijven.

Beide zijn beslissingen van tien minuten aan het begin en migraties van meerdere dagen achteraf, wat ze in dezelfde categorie plaatst als het tenantmodel: het uur nadenken waard voordat er iets tegen wordt gegenereerd.

De algemene regel achter dit alles: in een prototype zijn de kosten van een structurele beslissing de tijd die het kost om haar uit te spreken. In een product met klanten zijn het de kosten van een migratie. Besteed de eerste zolang het nog kan.

Het is ook de enige fase waarin u ze alleen kunt nemen. Zodra zes klanten van het product afhangen, is een schemawijziging een migratie met een onderhoudsvenster en een rollbackplan, en het uur dat u aan het begin niet besteedde, wordt een week die u onder druk besteedt.

Een nuttige manier om dit tijdens het prototypen vast te houden: elke tabel die u aanmaakt, is een belofte aan uw toekomstige zelf over wat het product is. Doe zo min mogelijk beloftes, doe ze bewust, en schrijf ze op waar de volgende sessie ze kan lezen.

## Dit Inrichten

Voor een Bolt-prototype dat overgaat op een echte database, kost dit doorgaans één tot twee dagen: een schema ontworpen vanuit het bedrijf in plaats van vanuit de schermen, met tenantmodel, identificaties en naamgeving bewust bepaald; de kleinste set tabellen die het product weergeeft; row-level security vanaf het begin ingeschakeld met policies op elke tabel en gecontroleerd met twee accounts; foreign keys, not-null-, unieke en checkconstraints; een realistische seedset met ontbrekende velden, lastige tekens en volume; nepdata verwijderd zonder terugval; migraties in de repository in plaats van wijzigingen die in een dashboard zijn getypt; en gegenereerde types opnieuw gegenereerd, zodat de applicatie de echte vorm kent.

LaunchStudio doet dit als onderdeel van het naar productie brengen van een prototype binnen het Launch Ready-pakket, vanaf €800. De engineers zijn van Manifera — elf jaar Postgres in productie, 160+ projecten, vanuit Amsterdam en Ho Chi Minh-stad.

[Stuur ons uw prototype en een beschrijving van uw bedrijf](https://launchstudio.eu/nl/#contact) en wij ontwerpen het schema voordat er iets tegen wordt gegenereerd.

## Echt voorbeeld

### Negentien Tabellen voor Vijf Dingen

Hidde Kwakernaak bouwde Ritmeester met Bolt: stal- en pensionbeheer voor manegebedrijven — paarden, eigenaren, stallen, voerschema's, dierenartsafspraken en facturatie — voor zes manegebedrijven in Gelderland en Utrecht.

Hij had de tool gevraagd een database toe te voegen terwijl hij elk scherm bouwde. Na drie weken had het schema 19 tabellen. Paarden bestonden in twee ervan. Contactgegevens van eigenaren in drie, met verschillende kolomnamen en inmiddels verschillende waarden. Er waren geen foreign keys, geen row-level security, en één tabel was aangemaakt voor een functie die hij in week één had laten varen.

Het probleem kwam naar boven toen het tweede manegebedrijf het ging gebruiken en hun paarden in de stallenlijst van het eerste bedrijf verschenen.

Drie werkdagen: het bedrijf goed beschreven, met vijf kernentiteiten als resultaat — manegebedrijven, paarden, eigenaren, stallen en afspraken — met facturatie als zesde; een schema ontworpen rond die entiteiten met een organisatie-identificatie op elke tabel, willekeurige primaire sleutels met een leesbare paardreferentie die mensen kunnen noemen, en consequente naamgeving; 19 tabellen samengevoegd tot acht, waarbij de dubbele paard- en eigenaarrecords werden samengevoegd nadat de drie kopieën van contactgegevens met de hand waren afgestemd; row-level security ingeschakeld met policies op alle acht, gecontroleerd met accounts in twee manegebedrijven; foreign keys toegevoegd, wat 40 verweesde records blootlegde; not-null-, unieke en checkconstraints; een seedset van 400 paarden over vier bedrijven met ongelijke verdeling, ontbrekende optionele velden en diakritische tekens in namen; terugvallen op nepdata verwijderd uit vier schermen waar een leeg resultaat stilletjes verzonnen paarden had getoond; migraties gecommit; en types opnieuw gegenereerd.

**Resultaat:** het lek tussen manegebedrijven werd structureel gedicht in plaats van opgelapt. Hidde vertelt dat het samenvoegen ongemakkelijk was — drie dagen werk zonder zichtbare functie — en dat de zes bedrijven die daarna aansloten elk een dag kostten in plaats van de week die de eerste twee hadden gekost, omdat er niets hoefde te worden afgestemd.

> *"Negentien tabellen voor een bedrijf met vijf dingen erin. Elke tabel was een redelijk antwoord op een scherm dat ik die middag bouwde, en samen waren ze een product waarin een paard twee keer kon bestaan met verschillende eigenaren."*
> — **Hidde Kwakernaak, Oprichter, Ritmeester (Barneveld)**

**Kosten & Doorlooptijd:** €3.200 (schemaontwerp vanuit het bedrijf, samenvoegen van 19 naar 8 tabellen met afstemming van data, row-level security met policies, constraints en oplossen van wezen, realistische seeddata, verwijderen van nepdata, migraties en opnieuw genereren van types) — afgerond in 3 werkdagen.

## Veelgestelde vragen

### Moet ik de tool mijn schema laten ontwerpen?

Geef het er een. Een uur besteed aan het beschrijven van uw bedrijfsentiteiten, tenantmodel, identificaties en naamgeving levert een structuur op die de gegenereerde code volgt, en voorkomt een ontwerp dat is afgeleid van het scherm dat u toevallig als eerste bouwde.

### Wanneer moet row-level security worden ingeschakeld?

Vanaf de eerste tabel. Bouwen tegen een database die scheiding al afdwingt, maakt gaten direct zichtbaar; het achteraf inbouwen in een applicatie die van open toegang uitging, is trager en lekt meer.

### Met hoeveel tabellen moet ik beginnen?

Met de minste die het bedrijf weergeven. Later opsplitsen is makkelijk; tabellen samenvoegen die één hadden moeten zijn niet, omdat elk scherm de verkeerde vorm heeft geleerd.

### Heb ik foreign keys en constraints nodig in een klein product?

Ja. Ze zijn elk één regel en ze houden stand wanneer data binnenkomt via imports, integraties en AI-sessies die uw bedoelingen nooit lazen.

### Wat breekt er als nepdata wordt vervangen?

Code die is geschreven tegen data die altijd compleet was. Genereer vóór het aansluiten een realistische seedset — ontbrekende velden, lastige tekens, volume — en verwijder terugvallen op nepdata volledig.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet Bolt mijn databaseschema ontwerpen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Geef het er in plaats daarvan een. Een uur entiteiten, tenantmodel, identificaties en naamgeving beschrijven levert een structuur op die de gegenereerde code volgt."
      }
    },
    {
      "@type": "Question",
      "name": "Wanneer moet row-level security worden ingeschakeld?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vanaf de eerste tabel, zodat elk scherm wordt gebouwd tegen afgedwongen scheiding in plaats van dat het later wordt ingebouwd."
      }
    },
    {
      "@type": "Question",
      "name": "Met hoeveel tabellen moet een prototype beginnen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Met de minste die het bedrijf weergeven. Later opsplitsen is makkelijk; tabellen samenvoegen die één hadden moeten zijn niet."
      }
    },
    {
      "@type": "Question",
      "name": "Zijn foreign keys het waard in een klein product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja — één regel elk, en ze houden stand tegen imports, integraties en AI-sessies die uw bedoelingen nooit lazen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat breekt er als nepdata door een database wordt vervangen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Code die uitgaat van complete, consistente data. Seed eerst realistisch, en verwijder terugvallen op nepdata zodat lege resultaten niet worden verborgen."
      }
    }
  ]
}
</script>
