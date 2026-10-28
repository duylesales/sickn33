---
Titel: "Lovable Supabase: CSV-imports Die Uw Data Niet Beschadigen"
Trefwoorden: lovable supabase, CSV-import, Excel-import, datavalidatie, tussentabel, bulkupload, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Lovable Supabase: CSV-imports Die Uw Data Niet Beschadigen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: CSV-imports Die Uw Data Niet Beschadigen",
  "description": "Elke B2B-klant begint met het importeren van een spreadsheet, en de import is waar schone databases ten onder gaan. Coderingen, Nederlandse getalnotaties, wat Excel kapotmaakt, een gefaseerde pijplijn met voorbeeldweergave en terugdraaien, ontdubbeling, en de beveiligingsrisico's in een CSV-bestand.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-11",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-supabase-csv-imports-that-do-not-corrupt-your-data" }
}
</script>

Niemand begint een B2B-product te gebruiken met een lege database. Het eerste wat een nieuwe klant doet, is zijn bestaande data meebrengen: klanten uit het oude systeem, producten uit een spreadsheet, leden uit een Excel-bestand dat iemand sinds 2014 bijhoudt. De importfunctie is de eerste echte ervaring van de klant met uw product, en het is de snelste manier om een schone database met rommel te vullen.

AI-tools bouwen imports die werken op het voorbeeldbestand waarmee ze zijn getest. Echte bestanden komen binnen in de verkeerde codering, met puntkomma's in plaats van komma's, Nederlandse decimale komma's, datums in drie notaties, telefoonnummers zonder voorloopnul, dubbele rijen, en een kolom "Opmerkingen" met regeleinden erin. Een import die elke rij direct in productietabellen zet, maakt van elk van die eigenaardigheden een dataprobleem dat moeilijk te vinden en nog moeilijker terug te draaien is.

Dit artikel behandelt de hele weg van bestand naar database: het inlezen van wat Nederlandse klanten werkelijk sturen, de notaties die stilletjes van betekenis veranderen, een gefaseerde pijplijn met voorbeeldweergave en terugdraaien, ontdubbeling, grote bestanden, en de beveiligingsrisico's die in een onschuldig ogende spreadsheet zitten.

## Wat Nederlandse Klanten Werkelijk Sturen

Het bestand dat uw klant uit zijn oude systeem exporteert of uit Excel opslaat, is niet de RFC 4180-CSV waarmee uw parser is getest.

**Het scheidingsteken is vaak een puntkomma.** Excel met Nederlandse landinstellingen gebruikt de komma als decimaalteken, en slaat "CSV" dus op met puntkomma's tussen de velden. Een parser die komma's verwacht, leest elke regel als één enorm veld - of erger, splitst op de komma's in bedragen.

**De codering is vaak Windows-1252.** Bestanden die door oudere Excel-versies en veel oude systemen worden opgeslagen, zijn geen UTF-8. Gelezen als UTF-8 wordt "Hélène" "HÃ©lÃ¨ne" en wordt "€" onzin. Bestanden die als "CSV UTF-8" uit moderne Excel worden opgeslagen, beginnen met een byte order mark die, onbehandeld, aan de eerste kolomnaam vast blijft zitten - zodat de kolom `naam` niet wordt gevonden omdat hij eigenlijk `﻿naam` heet.

**Velden bevatten regeleinden en aanhalingstekens.** Een adres of opmerking over twee regels, tussen aanhalingstekens, met aanhalingstekens erin verdubbeld. Het bestand vóór het inlezen op regeleinden splitsen, breekt deze rijen doormidden.

**Kopregels variëren.** Kolomnamen in het Nederlands of Engels, met spaties erachter, verschillende hoofdletters, soms twee kopregels, soms geen.

Het antwoord is nooit zelf een parser te schrijven. Gebruik een onderhouden CSV-bibliotheek, herken het scheidingsteken door de eerste regels te bekijken, herken de codering - of eenvoudiger, vraag het de gebruiker met de meest waarschijnlijke als standaard - verwijder de byte order mark, en normaliseer kolomnamen (spaties weg, kleine letters) vóór het matchen.

Beter nog: accepteer `.xlsx` direct. Het spreadsheetformaat inlezen met een bibliotheek vermijdt problemen met scheidingstekens en codering volledig, en het is wat de meeste klanten toch al hebben; CSV is vaak alleen het formaat waarnaar ze moesten omzetten.

## Notaties Die Stilletjes van Betekenis Veranderen

Fouten bij het inlezen zijn zichtbaar: rijen falen, kolommen ontbreken. De gevaarlijke fouten zijn die waarbij een waarde succesvol wordt gelezen en iets anders betekent.

**Getallen.** "1.250,00" is in het Nederlands twaalfhonderdvijftig. Een parser met Engelse conventies leest het als 1.25, of faalt, afhankelijk van de bibliotheek. "1,250" is in het Nederlands één komma vijfentwintig en in het Engels twaalfhonderdvijftig. Bepaal de verwachte notatie per import - uit de locale van de gebruiker of een expliciete keuze - en weiger waarden die er niet bij passen in plaats van te gokken.

**Datums.** "03-04-2028" is in Nederland 3 april en in de Verenigde Staten 4 maart. "3-4-28" voegt een eeuwvraag toe. Excel kan de datum ook als volgnummer hebben geëxporteerd, zoals 46115. Accepteer een expliciete set notaties, lees strikt in, en toon de geïnterpreteerde datum in de voorbeeldweergave zodat de klant "3 april 2028" ziet en kan bevestigen.

**Voorloopnullen.** Excel haalt ze weg bij alles wat het voor een getal houdt. Telefoonnummers verliezen hun 0, artikelcodes "00451" worden 451, KvK-nummers en sommige codes veranderen. Behandel deze kolommen per definitie als tekst, leid ze nooit af als getal, en controleer hun lengte - een Nederlands mobiel nummer heeft tien cijfers.

**Lange getallen.** IBAN's overleven omdat ze letters bevatten. Lange numerieke identificatoren niet: Excel zet alles boven de vijftien cijfers om naar wetenschappelijke notatie en verliest de precisie definitief. Bevat het bestand van een klant "8,71234E+15", dan is de oorspronkelijke waarde weg; herken het patroon en weiger de rij met een uitleg in plaats van het verkeerde getal op te slaan.

**Ja/nee-waarden en opsommingen.** "Ja", "ja", "J", "1", "waar", "yes", "x". Koppel een expliciete set geaccepteerde waarden aan uw codes en weiger de rest - en onthoud de regel uit het artikel over internationalisering dat statussen als codes worden opgeslagen, niet als Nederlandse woorden.

## De Gefaseerde Pijplijn

De structurele oplossing voor imports is nooit direct in productietabellen te schrijven. Elke robuuste import volgt dezelfde vijf fasen.

**1. Uploaden.** Het bestand gaat naar de opslag, er wordt een rij aangemaakt in een tabel `import_batches` met de organisatie, de gebruiker, de bestandsnaam en een status. Er is nog niets aan de data veranderd.

**2. Inlezen en koppelen.** Het bestand wordt ingelezen en de klant koppelt zijn kolommen aan uw velden - "Klantnaam" aan `name`, "Postcode" aan `postal_code`. Onthoud de koppeling per organisatie, want ze importeren volgende maand dezelfde export opnieuw.

**3. Valideren in een tussentabel.** Elke rij wordt weggeschreven naar een tussentabel met de ingelezen waarden en een lijst fouten en waarschuwingen. Validatie is dezelfde als bij een formulier - verplichte velden, notaties, bereiken, verwijzingen naar bestaande records - plus controles specifiek voor imports, zoals duplicaten binnen het bestand.

```sql
create table import_rows (
  batch_id uuid not null references import_batches(id) on delete cascade,
  row_number int not null,
  raw jsonb not null,             -- de oorspronkelijke waarden, onaangeroerd
  parsed jsonb,                   -- genormaliseerde waarden
  errors text[] not null default '{}',
  warnings text[] not null default '{}',
  action text,                    -- 'create' | 'update' | 'skip'
  target_id uuid,                 -- gevonden bestaand record, indien van toepassing
  primary key (batch_id, row_number)
);
```

**4. Voorbeeldweergave.** De klant ziet een samenvatting - 812 rijen worden aangemaakt, 64 bijgewerkt, 23 hebben fouten - en kan elke fout en elke update bekijken. Fouten kunnen worden gedownload als bestand met de oorspronkelijke rij en de reden, in Excel worden gecorrigeerd en opnieuw worden geüpload. Dit is de fase die een stil probleem zichtbaar maakt.

**5. Vastleggen.** Pas na bevestiging worden de geldige rijen naar productietabellen geschreven, in een transactie, met elke aangemaakte of bijgewerkte rij voorzien van het batch-ID. De batch legt de uitkomst vast: aantallen, duur, en wie het bevestigde.

De voorbeeldweergave is geen luxe. Het is het moment waarop "1.250,00 gelezen als 1,25" een regel op het scherm wordt met "Huur: € 1,25" die een mens opmerkt voordat achthonderd huurders dat bedrag krijgen afgeschreven.

## Beslis Wat Er met Foute Rijen Gebeurt

Twee beleidslijnen zijn verdedigbaar, en de import moet zeggen welke ze gebruikt.

**Alles of niets.** Heeft één rij een fout, dan wordt niets geïmporteerd totdat het bestand is gecorrigeerd. Passend voor financiële data, openingsbalansen, alles waarbij een gedeeltelijke import inconsistente totalen oplevert.

**Geldige rijen gaan door.** Correcte rijen worden geïmporteerd, rijen met fouten worden gemeld voor correctie. Passend voor contactlijsten, productcatalogi en de meeste stamdata, waar een gedeeltelijke import nuttig is en de rest later kan volgen.

Wat niet verdedigbaar is, is het standaardgedrag dat AI genereert: rijen één voor één invoegen, stoppen bij de eerste fout, en de eerste helft van het bestand geïmporteerd laten zonder vast te leggen waar het stopte. De klant uploadt het gecorrigeerde bestand opnieuw en importeert de eerste helft twee keer.

## Ontdubbelen en Bijwerken

Klanten importeren dezelfde data meer dan eens - een gecorrigeerd bestand, de export van volgende maand, de lijst van een tweede vestiging. Een import die alleen records aanmaakt, levert elke keer duplicaten op.

Bepaal per entiteit een sleutel om te matchen: een externe identificator uit het bronsysteem als die er is, anders een natuurlijke sleutel - e-mailadres voor contacten, artikelnummer voor producten, postcode plus huisnummer plus toevoeging voor adressen. Sla de externe identificator op in een eigen kolom met een unieke constraint per organisatie, en gebruik die voor een upsert:

```sql
insert into clients (organisation_id, external_ref, name, email, import_batch_id)
select organisation_id, parsed->>'external_ref', parsed->>'name', parsed->>'email', batch_id
from import_rows where batch_id = $1 and action in ('create', 'update')
on conflict (organisation_id, external_ref) do update
  set name = excluded.name, email = excluded.email, import_batch_id = excluded.import_batch_id;
```

Toon gevonden records in de voorbeeldweergave als updates, met de velden die veranderen. En beslis of lege cellen in het bestand "ongewijzigd laten" of "dit veld leegmaken" betekenen - de veilige standaard is het eerste, omdat een kolom die de klant niet exporteerde geen data mag wissen die hij in uw product invoerde.

Duplicaten binnen het bestand zelf - dezelfde klant twee keer omdat twee vestigingen hem allebei vermeldden - worden tijdens de validatie gemarkeerd, niet stilletjes samengevoegd.

## Terugdraaien Is een Functie

Elke rij die door een import wordt geschreven, draagt haar batch-ID. Dat maakt de waardevolste importfunctie mogelijk: een batch terugdraaien.

Voor een batch die alleen records aanmaakte, verwijdert terugdraaien die records - mits niets anders er al naar is gaan verwijzen, wat de foreign keys van de database u vertellen. Voor een batch die records bijwerkte, zijn de vorige waarden nodig, en dat is een reden om ze vóór het vastleggen in de tussenrij op te slaan.

Bied terugdraaien aan voor een beperkte periode - een dag, een week - en aan beheerders. Het maakt van "we hebben het verkeerde bestand geïmporteerd" een knop in plaats van een supportnoodgeval, en het is het sterkste argument voor het gefaseerde ontwerp.

## Grote Bestanden en Time-outs

Een bestand van vijfhonderd rijen kan binnen een verzoek worden verwerkt. Een bestand van vijftigduizend niet, en dat loopt halverwege tegen de time-out aan die het artikel over achtergrondwerk in deze reeks beschrijft.

Verwerk imports als achtergrondtaken. De upload komt direct terug met het batch-ID; een worker leest in en valideert in blokken van een paar honderd rijen; de interface vraagt de batchstatus op en toont de voortgang. Leg vast in blokken binnen één logische operatie, waarbij de batchstatus vastlegt hoe ver ze kwam, zodat een nieuwe poging verdergaat in plaats van opnieuw begint.

Stel expliciete limieten: een maximale bestandsgrootte, een maximaal aantal rijen per import, en een redelijk aantal per organisatie per dag. Vermeld ze op het importscherm. Een klant die tegen een limiet aanloopt met een duidelijke melding, splitst het bestand; een klant die tegen een time-out aanloopt met een algemene fout, mailt support.

## Beveiliging in een Spreadsheet

Imports zijn invoer zoals elke andere, en ze brengen eigen risico's mee.

**Afbakening op organisatie.** Imports draaien vaak met de service role, die row level security omzeilt. Elke schrijfactie moet de organisatie uit de batch halen - die van de ingelogde gebruiker komt - en nooit uit een kolom in het bestand. Een bestand met een kolom `organisation_id` mag geen data in het account van iemand anders kunnen zetten.

**Formule-injectie.** Een cel die begint met `=`, `+`, `-` of `@` wordt als formule uitgevoerd wanneer de data later wordt geëxporteerd en in Excel geopend: `=HYPERLINK("https://evil.example","Klik hier")`. Sla de waarde op als tekst, en zet bij het exporteren een apostrof voor zulke cellen zodat spreadsheetsoftware ze als tekst behandelt. Het artikel over data-exports in deze reeks behandelt de exportkant.

**Bestandsgrootte en inhoud.** Beperk de grootte, controleer dat het bestand echt CSV of XLSX is in plaats van op de extensie te vertrouwen, en verwerk het buiten het verzoekpad, zoals de artikelen over bestandsuploads in deze reeks beschrijven.

**Persoonsgegevens.** Een importbestand bevat vaak meer persoonsgegevens dan uw product nodig heeft - een volledige export uit een oud CRM met geboortedata en notities. Importeer alleen gekoppelde kolommen, verwijder het geüploade bestand nadat de batch is vastgelegd of afgebroken, en bewaar de tussenrijen alleen zo lang als terugdraaien vereist.

## Import Is Onboarding

De technische pijplijn is de helft van het werk. De andere helft is dat de import meestal het eerste uur van de klant met uw product is, en hoe dat voelt, bepaalt verrassend veel over of hij blijft.

**Bied een sjabloon aan.** Een downloadbare XLSX met uw kolommen, een voorbeeldrij, en een tweede tabblad dat elk veld en de geaccepteerde notaties uitlegt. Klanten die met het sjabloon beginnen, leveren schone bestanden; klanten die met de export van hun oude systeem beginnen, hebben de koppelstap nodig.

**Herken de gangbare bronnen.** Komen de meeste klanten uit dezelfde twee of drie systemen - een bepaald boekhoudpakket, een bekende branchetool - sla dan voor elk een kant-en-klare kolomkoppeling op. "Importeert u uit Exact? We hebben de kolommen al voor u gekoppeld" haalt de saaiste stap volledig weg.

**Schrijf fouten voor degene die het bestand corrigeert.** Niet `invalid_date at row 412`, maar "Rij 412: de datum '31-02-2028' bestaat niet. Gebruik de notatie DD-MM-JJJJ." Het foutenbestand moet in Excel openen met de oorspronkelijke rij en een laatste kolom die uitlegt wat er moet veranderen.

**Meet het.** Leg vast hoeveel batches worden gestart, hoeveel de voorbeeldweergave bereiken, hoeveel worden vastgelegd en hoe lang elke fase duurt. Een import waarbij de helft van alle batches bij de voorbeeldweergave wordt afgebroken, vertelt u op welke validatiemeldingen klanten niet kunnen handelen - en dat getal is een van de nuttigste onboardingmetingen die een B2B-product heeft.

## Test met Lastige Bestanden

Een import die met een schoon voorbeeldbestand is getest, is ongetest. Houd een map met opzettelijk lastige testbestanden bij en draai ze in CI:

- Een Windows-1252-bestand met puntkomma's, met é, ë en €.
- Een UTF-8-bestand met een byte order mark.
- Nederlandse bedragen met duizendtallen en decimale komma's.
- Datums in drie notaties, inclusief een Excel-volgnummer.
- Telefoonnummers en artikelcodes met voorloopnullen.
- Een identificator van twintig cijfers in wetenschappelijke notatie.
- Een opmerkingenveld met regeleinden en verdubbelde aanhalingstekens.
- Dubbele rijen, lege rijen en een lege laatste regel.
- Een cel die begint met `=HYPERLINK(`.
- Een rij met een kolom `organisation_id` die naar een andere organisatie wijst.

Elk testbestand heeft een verwachte uitkomst - ingelezen waarden, fouten, of weigering - en de tests controleren die. Wanneer het echte bestand van een klant iets breekt, wordt het een testbestand.

## Dit Inrichten

Voor een Lovable-product met een importfunctie is dit doorgaans drie tot vier dagen: een onderhouden bibliotheek voor CSV en XLSX met herkenning van scheidingsteken en codering en afhandeling van de byte order mark, opgeslagen kolomkoppelingen per organisatie, expliciete notaties voor getallen, datums en ja/nee-waarden met strikt inlezen, identificatiekolommen als tekst met lengtecontrole, een gefaseerde pijplijn van uploaden, inlezen, valideren in een tussentabel, voorbeeldweergave en vastleggen in een transactie, een vastgelegd beleid voor rijen met fouten en een downloadbaar foutenbestand, externe identificatoren met ontdubbeling via upsert, batch-ID's op elke geïmporteerde rij en terugdraaien binnen een vastgestelde periode, verwerking op de achtergrond met voortgang en expliciete limieten, de organisatie bepaald door de geauthenticeerde batch, geneutraliseerde formule-injectie, geüploade bestanden verwijderd na verwerking, een sjabloon en kant-en-klare koppelingen voor gangbare bronnen, en een CI-suite met lastige testbestanden.

LaunchStudio bouwt dit wanneer onboarding wordt tegengehouden door de import. De engineers zijn van Manifera - elf jaar, 120+ engineers, 160+ projecten, vanuit Amsterdam en Ho Chi Minh-stad.

[Stuur ons het slechtste bestand dat een klant u ooit gaf](https://launchstudio.eu/nl/#contact) en wij vertellen u wat uw import ermee doet.

## Echt voorbeeld

### Een Huur van Een Euro Vijfentwintig

Annelies Vos bouwde Huurbeheer in Lovable: huuradministratie voor kleine woningcorporaties en vastgoedbeheerders, gebruikt door 31 organisaties die samen zo'n 9.500 huurwoningen beheren.

Nieuwe klanten importeerden hun huurders uit Excel. De import las elke rij en voegde haar direct in; ze was getest met een kommagescheiden bestand dat de oprichter zelf had gemaakt.

Een nieuwe vastgoedbeheerder uploadde een export met puntkomma's als scheidingsteken en Nederlandse bedragen. De parser kon toevallig met de puntkomma's overweg, maar las "1.250,00" als 1,25. De import meldde succes. De maandelijkse incassorun inde €1,25 bij 214 huurders, en de vastgoedbeheerder ontdekte het via het bankafschrift. Dezelfde klant had het bestand twee keer opnieuw geïmporteerd tijdens het oplossen van een ander probleem, wat 380 dubbele huurders opleverde, en elk telefoonnummer was zijn voorloopnul kwijt.

Drie werkdagen: een parser voor XLSX en CSV met herkenning van scheidingsteken en codering; expliciete Nederlandse notaties voor getallen en datums per import, met weigering van waarden die niet pasten; telefoonnummers, postcodes en huisnummertoevoegingen als tekst met lengtecontrole; een gefaseerde pijplijn met een voorbeeldweergave van geïnterpreteerde bedragen en datums en een downloadbaar foutenbestand; upsert op het huurdernummer van het bronsysteem, waarbij lege cellen bestaande waarden ongewijzigd laten; batch-ID's op elke rij en terugdraaien gedurende zeven dagen; verwerking op de achtergrond met voortgang voor bestanden boven vijfhonderd rijen; afbakening op organisatie vanuit de batch in plaats van het bestand; neutralisatie van formules bij export; en een CI-suite met veertien lastige testbestanden, inclusief het oorspronkelijke bestand.

**Resultaat:** bij de 214 huurders werd de week erna het juiste bedrag geïncasseerd en de 380 duplicaten werden samengevoegd op basis van het huurdernummer uit het bronsysteem. In het kwartaal daarna importeerden elf nieuwe organisaties hun data; de voorbeeldweergave ving in vier van de bestanden problemen met bedragen of datums op voordat er iets werd weggeschreven.

> *"De import zei dat het had gewerkt. Onze klant ontdekte via de bank dat tweehonderdveertien huurders een euro vijfentwintig huur hadden betaald."*
> - **Annelies Vos, Oprichter, Huurbeheer (Zwolle)**

**Kosten & Doorlooptijd:** €3.600 (robuust inlezen van CSV en XLSX, expliciete Nederlandse notaties, gefaseerde import met voorbeeldweergave en foutenbestanden, ontdubbeling via upsert, terugdraaien per batch, verwerking op de achtergrond, afbakening op organisatie, neutralisatie van formules, testsuite met veertien testbestanden, opschoning van getroffen data) - afgerond in 3 werkdagen.

## Veelgestelde vragen

### Waarom breken CSV-bestanden van Nederlandse klanten imports?

Nederlandse Excel slaat CSV op met puntkomma's omdat de komma het decimaalteken is, vaak in Windows-1252-codering, met bedragen als 1.250,00 en datums die met de dag beginnen. Parsers die met Engelstalige bestanden zijn getest, lezen dit allemaal verkeerd.

### Moeten imports direct in productietabellen schrijven?

Nee. Lees in en valideer in een tussentabel, toon de klant een voorbeeldweergave met fouten en geïnterpreteerde waarden, en leg pas na bevestiging vast, in een transactie, met een batch-ID op elke rij.

### Hoe voorkom ik duplicaten wanneer klanten twee keer importeren?

Sla de identificator van het bronsysteem op, of een natuurlijke sleutel zoals een e-mailadres, met een unieke constraint per organisatie, en doe een upsert daarop. Toon gevonden records als updates in de voorbeeldweergave.

### Kan een import worden teruggedraaid?

Ja, als elke geïmporteerde rij haar batch-ID draagt en vorige waarden bij updates worden bewaard. Terugdraaien aanbieden voor een beperkte periode maakt van een verkeerde import een knop in plaats van een supportnoodgeval.

### Wat is CSV-formule-injectie?

Een cel die begint met `=`, `+`, `-` of `@` en als formule wordt uitgevoerd wanneer de data later in Excel wordt geopend. Sla zulke waarden op als tekst en zet er bij het exporteren een apostrof voor.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom breken Nederlandse CSV-bestanden app-imports?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ze gebruiken puntkomma's, Windows-1252-codering, decimale komma's en datums die met de dag beginnen, wat parsers voor Engelstalige bestanden verkeerd lezen."
      }
    },
    {
      "@type": "Question",
      "name": "Mag een CSV-import direct in productietabellen schrijven?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee - valideer in een tussentabel, toon een voorbeeldweergave met fouten, en leg dan vast in een transactie met een batch-ID op elke rij."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkomen herhaalde imports dat er duplicaten ontstaan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Gebruik een externe of natuurlijke sleutel met een unieke constraint per organisatie en doe daarop een upsert, met gevonden records als updates."
      }
    },
    {
      "@type": "Question",
      "name": "Kan een data-import worden teruggedraaid?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, wanneer elke geïmporteerde rij haar batch-ID draagt en vorige waarden worden bewaard, wat terugdraaien binnen een beperkte periode mogelijk maakt."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is CSV-formule-injectie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cellen die beginnen met =, +, - of @ en in Excel als formule worden uitgevoerd; sla ze op als tekst en zet er bij export een apostrof voor."
      }
    }
  ]
}
</script>
