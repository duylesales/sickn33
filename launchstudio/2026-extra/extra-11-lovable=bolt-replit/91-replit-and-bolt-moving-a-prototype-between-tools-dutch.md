---
Titel: "Replit en Bolt: Een Prototype Migreren Tussen Tools"
Trefwoorden: Replit, Bolt, Lovable, prototype migratie, vibe coding developer, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-oprichters / Indie Hackers
---

# Replit en Bolt: Een Prototype Migreren Tussen Tools

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Replit en Bolt: Een Prototype Migreren Tussen Tools",
  "description": "Halverwege een project wisselen van ontwikkelplatform gebeurt regelmatig en is zelden vooraf gepland. Wat er daadwerkelijk meeverhuist, wat onlosmakelijk vastzit aan het oude platform en hoe je migreert zonder dataverlies of tijdverspilling.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-01",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/91-replit-and-bolt-moving-a-prototype-between-tools" }
}
</script>

Niemand plant dit vooraf in. Het gebeurt omdat je tegen een heel specifieke blokkade aanloopt: de huidige tool kan de gewenste functionaliteit niet aan, de platformkosten lopen uit de pas, een nieuwe ontwikkelaar werkt met een andere stack, of je ontdekt simpelweg een tool die veel beter aansluit bij jouw manier van werken.

Wanneer je vervolgens inventariseert wat een migratie behelst, wordt de situatie al snel ongemakkelijk. Het eerlijke antwoord is immers dat een deel van je project bestaat uit universele broncode, en een ander deel uit specifieke platformvoorzieningen. En slechts één van die twee reist moeiteloos met je mee.

## Wat er daadwerkelijk meeverhuist

**Je broncode verhuist volledig mee.** Het is standaard JavaScript, TypeScript, HTML, CSS en configuratiebestanden. Niets daaraan is gebonden aan een specifiek vendor-ecosysteem; elke volwaardige code-editor, server of hostingprovider kan ermee overweg. Dit is het goede nieuws en vormt het leeuwendeel van je applicatie.

**Je database verhuist mee als deze extern is ondergebracht.** Een managed PostgreSQL-omgeving zoals Supabase staat volledig los van waar je applicatielogica draait: je past de connection string aan en kunt direct door. Draait je database echter lokaal binnen het platform, dan vereist dit een export- en importtraject.

**Je domeinnaam verhuist via een simpele DNS-wijziging,** mits het domein op jouw eigen bedrijfsnaam geregistreerd staat.

**Geüploade mediabestanden verhuizen mee als ze in object storage staan.** Staan ze in een S3-compatibele bucket, dan blijft alles intact. Stonden uploads in een lokale projectmap naast de code, dan moeten ze handmatig worden geëxtraheerd en opnieuw worden opgebouwd.

Het patroon is glashelder: alles wat je destijds bewust en zelfstandig hebt ingericht verhuist probleemloos mee. Alles wat het platform standaard en geautomatiseerd voor je regelde, is waar het echte werk zit.

## Wat er beslist níét meeverhuist

**Platform-specifieke data-opslag.** Een ingebouwde key-value store of database van het platform zelf moet handmatig worden geëxporteerd en geconverteerd. De datastructuur is zelden de genormaliseerde opzet die je zelf zou kiezen.

**Deployment- en omgevingsconfiguraties.** Build-commando's, runtime-instellingen, omgevingsvariabelen, geplande taken (cron jobs) en hostingtypes. Dit moet allemaal opnieuw worden ingesteld. Omdat dit zelden gedocumenteerd is, moet iemand eerst exact uitzoeken hoe het huidige systeem functioneert.

**Geheime sleutels (secrets).** Elk platform slaat API-keys en tokens op een eigen manier op. De migratie is het uitgelezen moment om alle secrets te roteren — wat sowieso noodzakelijk is als meerdere teamleden toegang hebben gehad.

**Samenwerkingsstatus.** Wie beheerdersrechten heeft, de gedeelde bewerkingshistorie en interne commentaren: niets daarvan reist mee naar een nieuw platform.

**De context van de AI-assistent.** De verzamelde 'kennis' die de oude AI over je project had opgebouwd blijft achter. De eerste sessies op het nieuwe platform voelen daardoor alsof je samenwerkt met een stagiair die het project nog niet kent. Duidelijke projectinstructies (`.cursorrules` of repository-regels) lossen dit grotendeels op.

## De volgorde die voorkomt dat je een week verliest

Loop dit stappenplan strikt af om chaos te voorkomen:

**1. Plaats de code in een Git-repository die jij bezit.** Vóórdat je ook maar iets anders aanraakt. Als dit nog niet is gebeurd, is dit veruit de belangrijkste stap; het maakt elke volgende actie direct omkeerbaar.

**2. Maak een complete inventarisatie van platform-specifieke onderdelen.** Loop het hele project door en noteer elke omgevingsvariabele, elke cron-job, elke hosting-instelling en elke opslaglocatie. Deze lijst ís de daadwerkelijke migratie. Eén uur inventariseren bespaart je twee dagen storingzoeken.

**3. Haal data eerst uit de oude platform-opslag,** terwijl het oude platform nog actief draait. Een veilige export in eigen beheer maakt de rest van het migratietraject nagenoeg risicoloos.

**4. Bouw de nieuwe omgeving op náást de oude.** Schakel nog niets om. Compileer de code, start de applicatie, verbind met een kopie van de database en controleer of de werking identiek is.

**5. Roteer alle geheime API-sleutels direct in het nieuwe platform** in plaats van oude sleutels klakkeloos te kopiëren.

**6. Schakel om via de DNS,** terwijl de oude omgeving nog stand-by blijft draaien. Een tijdelijke overlap van een paar dagen kost vrijwel niets en biedt een direct terugvalscenario als er onverhoopt iets misgaat.

**7. Schakel het oude platform pas na een week definitief uit,** nadat de nieuwe omgeving zich zeven dagen foutloos heeft bewezen. Bewaar altijd een definitieve backup-export.

## De valkuil: migreren en gelijktijdig refactoren

Dit is veruit de meest voorkomende manier waarop migraties ontsporen:

Een verhuizing lijkt een ideaal moment om direct de mappenstructuur op te schonen, libraries te upgraden, functies te hernoemen en die ene hardnekkige bug op te lossen. Doe dit niet. Wanneer er dan iets breekt — en er breekt altijd iets — is het onmogelijk om te achterhalen of de fout wordt veroorzaakt door het nieuwe platform of door jouw codewijzigingen.

Migreer eerst, waarbij je de codebase zo identiek mogelijk houdt. Valideer dat alles naar behoren werkt. Pas daarna ga je verbeteren en refactoren. Het voelt contra-intuïtief, maar het is veruit de snelste route naar succes.

## Welke richting heeft zin?

Welke overstap is strategisch logisch?

**Richting een volwaardige ontwikkelomgeving (zoals Cursor / eigen Git)** wanneer je product de fase van een pure frontend is ontgroeid: je hebt server-side logica nodig, achtergrondprocessen, of je gaat samenwerken met professionele ontwikkelaars.

**Richting een generatieve visuele builder (zoals Lovable of Bolt)** wanneer je vooral bezig bent met het ontwerpen van schermen en iteratiesnelheid van de gebruikersinterface prioriteit heeft boven diepgaande infrastructuur.

**Richting een eigen Git-repository gekoppeld aan professionele cloud-hosting** zodra je betalende klanten hebt. Dit is de eindbestemming voor vrijwel elk succesvol SaaS-product: de bovengenoemde tools worden dan de omgevingen waarin je bouwt, niet de plekken waar je software daadwerkelijk live draait.

Bekijk de migratie niet vanuit de vraag *"welke tool vind ik leuker?"*, maar *"waar moet dit product betrouwbaar in productie draaien?"*. Dat beantwoordt de vraag voor vrijwel elke ondernemer direct.

## Wat te verifiëren na de verhuizing

Controleer deze punten direct na de DNS-omzetting:
- De applicatie laadt foutloos op je eigen domeinnaam met een geldig SSL-certificaat.
- Nieuwe data die wordt ingevoerd blijft permanent bewaard na een herstart of hercompileersessie.
- File-uploads functioneren en historische bestanden zijn foutloos op te vragen.
- Elke geplande cron-job heeft minimaal één keer succesvol gedraaid — controleer dit actief in de logs.
- Webhooks van betaalproviders bereiken het nieuwe endpoint en worden gevalideerd.
- Geen enkele geheime sleutel staat in de gedownloade frontend-bestanden.
- Foutmeldingen komen binnen in je centrale error-tracker.
- De terugvalprocedure (rollback) naar het oude platform is helder.

Geplande achtergrondtaken zijn het grootste risico: wanneer ze uitvallen, doen ze dat in stilte. Het uitblijven van taken lijkt aan de oppervlakte immers op een rustige week.

## Beslissen of je überhaupt moet migreren

Voordat je de technische stappen in gang zet, is er een gewetensvraag: is het platform daadwerkelijk het probleem?

**Drie legitieme redenen om te migreren:**
1. Je hebt functionaliteit nodig die het huidige platform structureel niet ondersteunt (zoals complexe serverless architectuur of specifieke achtergrondtaken).
2. De platformkosten zijn structureel onevenredig hoog geworden over meerdere maanden gemeten.
3. Een tweede teamlid sluit aan en het huidige platform biedt geen veilige samenwerkingsstructuur.

**Drie redenen die een verhuizing zelden rechtvaardigen:**
1. Eén vervelende week met vage storingen (dat ligt zelden aan het platform zelf).
2. Een trage applicatie (dat ligt vrijwel altijd aan ongeïndexeerde databasequery's of logge frontend-bundels; op een nieuw platform is de app net zo traag).
3. Een advies van iemand op LinkedIn die jouw specifieke product nog nooit heeft gezien.

Een verhuizing brengt altijd reële kosten met zich mee: een week van je volledige aandacht, dubbele hostingkosten en een periode van operationele onzekerheid. Die investering is de moeite waard voor structurele platformbeperkingen, maar niet voor een persoonlijke voorkeur.

Er is bovendien een tussenweg: blijf de tool gebruiken om visueel te bouwen, maar verhuis louter de database naar een managed provider (zoals Supabase) en de bestanden naar veilige object storage. Dat lost de meeste problemen op zonder complexe migratie.

## De migratie uitvoeren zonder tijdverlies

Voor een actieve applicatie is dit een afgebakend en voorspelbaar traject: code veiligstellen in een eigen repository met reproduceerbare builds, platforminstellingen inventariseren en herinrichten, data en bestanden exporteren naar managed cloud-diensten binnen de EU met strikte autorisatieregels, secrets roteren, webhooks en achtergrondtaken herstellen met monitoring, en de nieuwe omgeving parallel testen vóór de DNS-switch.

LaunchStudio voert deze platformmigraties uit zonder de vertrouwde gebruikersinterface aan te tasten. De software engineers zijn van Manifera: elf jaar ervaring met complexe datamigraties voor klanten zoals Vodafone, TNO en CFLW vanuit Amsterdam Herengracht 420 en Ho Chi Minhstad.

[Vertel ons waar je project nu staat en waar je naartoe wilt](https://launchstudio.eu/nl/#contact) voor een helder migratieplan binnen één werkdag, of bekijk onze [pakketten](https://launchstudio.eu/nl/#packages).

## Echt voorbeeld

### Een verhuizing die de lesherinneringen achterliet

Ties Kroeze bouwde met Bolt het platform Zwemles: een planningssysteem voor zwemlessen, in gebruik bij vier zwemscholen in de regio Purmerend en Volendam, met circa 1.900 ingeschreven kinderen verspreid over wekelijkse lesgroepen.

Hij besloot het project te migreren naar een volwaardige ontwikkelomgeving omdat hij server-side code nodig had voor een automatische incassokoppeling en omdat een parttime collega aansloot. De verhuizing kostte hem een weekend en op maandagochtend leek alles vlekkeloos te werken.

Drie cruciale elementen waren echter achtergebleven. De nachtelijke cron-job die ouders een automatische herinneringsmail stuurde voor de les van de volgende dag, was geconfigureerd in de ingebouwde taakplanner van het oude platform en stond nergens in de broncode. De taak stopte geruisloos — en het ontbreken van een e-mail valt niemand direct op. Pasfoto's van kinderen, die zweminstructeurs gebruikten om lesgroepen te controleren, stonden opgeslagen in een lokale tijdelijke servermap op het oude platform en ontbraken in de export. En de webhook van de betaalprovider wees nog altijd naar het oude webadres, dat nog elf dagen online bleef reageren voordat de container werd gewist. Vanaf dat moment werden annuleringen van zwemabonnementen niet meer geregistreerd.

Het uitvallen van de herinneringsmails werd pas na negentien dagen ontdekt, toen een zwemschoolhouder vroeg waarom zoveel bezorgde ouders plotseling telefonisch informeerden naar de lestijden.

In acht werkdagen werd de schade vakkundig hersteld: de nachtelijke herinneringstaak werd opnieuw opgebouwd als een robuuste achtergrondtaak met audit logging en automatische waarschuwingen bij uitval; de volledige configuratie-inventarisatie werd alsnog uitgevoerd, waarbij twee verstopte instellingen aan het licht kwamen — een tijdzone-instelling en een uploadlimiet — die geruisloos waren teruggevallen naar standaarden waardoor lestijden voor een deel van de ouders een uur verschoven werden weergegeven; foto's werden gemigreerd naar beveiligde object storage met strikte tenant-autorisatie; de betaalwebhook werd omgezet met handtekeningverificatie en de elf dagen aan gemiste opzeggingen werden handmatig gereconcilieerd, waarbij drie gezinnen werden opgespoord die onterecht nog lesgeld betaalden; API-sleutels werden geroteerd; en de volledige architectuur werd gedocumenteerd.

**Resultaat:** De drie onterecht gefactureerde gezinnen ontvingen binnen een week hun lesgeld terug. Ties omschrijft het tijdzoneprobleem als het meest pijnlijke incident: negentien dagen lang toonde zijn systeem ouders de verkeerde aanvangstijden zonder dat hij er ook maar enig vermoeden van had.

> *"Alles wat ik met het blote oog kon zien functioneerde op maandagochtend. Wat niet was meeverhuisd, was alles wat onzichtbaar was: een nachtelijke e-mailjob, een tijdzone-instelling en een webhook die bleef antwoorden op een webadres dat ik op het punt stond te wissen."*
> — **Ties Kroeze, Oprichter, Zwemles (Purmerend)**

**Kosten & Doorlooptijd:** € 3.600 (herbouw en monitoring van cron-jobs, configuratie-inventarisatie en correctie, veilige opslagmigratie, webhook-herstel met datareconciliatie, sleutelrotatie, documentatie) — opgeleverd in 8 werkdagen.

## Veelgestelde vragen

### Wat verhuist er daadwerkelijk mee wanneer ik wissel van platform?

Je broncode verhuist volledig mee, een externe managed database (zoals Supabase) blijft ongewijzigd functioneren, je domeinnaam schakel je om via DNS, en bestanden verhuizen mee mits ze in object storage staan. Alles wat het oude platform geautomatiseerd regelde, moet handmatig opnieuw worden ingericht.

### Welke onderdelen blijven structureel achter bij een migratie?

Platform-specifieke databases, hosting- en runtime-instellingen, geplande achtergrondtaken (cron jobs), opgeslagen API-sleutels, samenwerkingsgeschiedenis en het contextuele geheugen van de AI-assistent. Maak daarom altijd eerst een complete inventarisatie.

### Wat is de gevaarlijkste omissie tijdens een platformverhuizing?

Geplande achtergrondtaken. Wanneer een cron-job uitvalt, gebeurt dat geruisloos. Het ontbreken van automatische mails of rapportages lijkt aan de buitenkant op een probleemloze week, totdat klanten gaan klagen. Controleer na livegang actief of elke taak daadwerkelijk heeft gedraaid.

### Is het slim om tijdens de migratie direct de code op te schonen?

Nee, beslist niet. Verhuis de applicatie zo identiek mogelijk, valideer dat alles foutloos draait, en voer pas daarna refactorings door. Als je beide tegelijk doet en er ontstaat een fout, weet je niet of het aan het nieuwe platform of aan je code ligt.

### Hoe voer ik een veilige en vlekkeloze omzetting (cut-over) uit?

Bouw de nieuwe omgeving volledig op naast de oude, test met een kopie van de database, roteer alle geheime API-sleutels, schakel om via DNS terwijl het oude platform nog actief blijft, en hef het oude platform pas op na een volle week probleemloos draaien.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat verhuist er daadwerkelijk mee wanneer ik wissel van platform?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Broncode verhuist volledig, een externe database blijft intact, domeinen verhuizen via DNS en bestanden in object storage blijven behouden."
      }
    },
    {
      "@type": "Question",
      "name": "Welke onderdelen blijven structureel achter bij een migratie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Platform-opslag, hosting-instellingen, geplande taken (cron jobs), API-secrets, gebruikersrechten en de context van de AI-assistent."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de gevaarlijkste omissie tijdens một platformverhuizing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Geplande cron-jobs. Ze vallen geruisloos uit en hun afwezigheid valt pas op wanneer gebruikers melden dat herinneringen of exports ontbreken."
      }
    },
    {
      "@type": "Question",
      "name": "Is het slim om tijdens de migratie direct de code op te schonen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Migreer eerst identiek, valideer de werking, en ga pas refactoren als de nieuwe omgeving bewezen stabiel draait."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voer ik een veilige en vlekkeloze omzetting (cut-over) uit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Bouw parallel op, test met kopiedata, roteer secrets, schakel om via DNS met het oude systeem live, en ontkoppel pas na een stabiele week."
      }
    }
  ]
}
</script>
