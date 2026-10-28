---
Titel: "Lovable Supabase: Storage Buckets en Wie Wat Mag Lezen"
Trefwoorden: lovable supabase, storage buckets, ondertekende URL's, bestandsrechten, risico publieke bucket, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Lovable Supabase: Storage Buckets en Wie Wat Mag Lezen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Storage Buckets en Wie Wat Mag Lezen",
  "description": "De publieke bucket is het meest voorkomende datalek in door AI gebouwde apps. Hoe opslagrechten in Supabase echt werken, wanneer ondertekende URL's het antwoord zijn, en hoe u bestanden naar privé verplaatst zonder uw product te breken.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-03",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-supabase-storage-buckets-and-who-can-read-what" }
}
</script>

Vraag een AI-tool om bestandsuploads toe te voegen en binnen een minuut hebt u iets wat werkt. Het maakt een bucket aan, markeert die als publiek, uploadt het bestand en slaat de resulterende URL op. Elke schermafbeelding, factuur, elk identiteitsbewijs en elk medisch formulier dat uw gebruikers uploaden, is dan leesbaar voor iedereen die het adres heeft - en de adressen zijn vaak te raden.

"Publiek" betekent in Supabase-opslag niet "publiek voor ingelogde gebruikers". Het betekent een URL waarvoor helemaal geen authenticatie nodig is: geen sessie, geen token, geen verloopdatum. Het bestand staat op het open internet.

Dit is de meest voorkomende ernstige bevinding bij beveiligingsreviews van Lovable-applicaties, en het is volledig een standaardinstelling, geen fout die iemand maakte.

## Wat Publiek U Werkelijk Kost

Drie gevolgen, oplopend in ernst.

Iedereen met de URL kan het bestand voor altijd lezen, ook nadat de gebruiker zijn account heeft verwijderd, omdat het verwijderen van een databaserij geen object uit de opslag verwijdert.

URL's lekken op gewone manieren. Ze verschijnen in supportmails, in de browsergeschiedenis, in de referrer-header die naar analysetools van derden wordt gestuurd, in schermafbeeldingen die in chats worden gedeeld, en op elke pagina die ze toont. Zodra een URL bestaat, reist hij.

En als bestandsnamen voorspelbaar zijn - oplopende nummers, gebruikers-ID's, originele bestandsnamen - kan de bucket worden afgelopen. Een aanvaller die één document op een te raden pad vindt, probeert de volgende honderd, en door AI gegenereerde uploadcode geeft bestanden veel vaker wel dan niet een voorspelbare naam.

Voor een product dat iets verwerkt wat een persoon als privé zou beschouwen, is dit een datalek dat wacht tot iemand het opmerkt, met meldplichten eraan vast.

## Wanneer Publiek Prima Is

Niet alles hoeft te worden beschermd, en elk bestand als gevoelig behandelen maakt uw product trager en ingewikkelder dan nodig.

Publieke buckets zijn juist voor werkelijk publieke bestanden: marketingafbeeldingen, logo's, publieke profielfoto's in een gids die zelf publiek is, downloadbare brochures. Alles wat een bezoeker toch al zou kunnen zien.

De test is eenvoudig en de moeite waard om per bestand toe te passen. Als dit object in een zoekmachine verscheen, zou iemand het erg vinden? Is het antwoord nee, dan is publiek prima en eenvoudiger. Is het antwoord ja - zelfs een beetje - dan hoort het in een privébucket.

De meeste producten eindigen met beide, en dat is de juiste uitkomst: een publieke bucket voor algemene bestanden en een privébucket voor alles wat gebruikers uploaden.

## Hoe Privébuckets Werken

Een privébucket weigert anonieme toegang. Bestanden worden op een van twee manieren bereikt, en daartussen kiezen is de belangrijkste ontwerpbeslissing.

**Via de geauthenticeerde client**, waarbij de sessie van de gebruiker wordt gecontroleerd tegen opslagpolicies die u schrijft - hetzelfde soort voorwaarden als row-level security, maar toegepast op objectpaden. Dit past bij bestanden die binnen uw applicatie aan een ingelogde gebruiker worden getoond.

**Via een ondertekende URL (signed URL)**, een tijdelijk adres dat uw server genereert, dat voor een vastgestelde periode werkt en daarna verloopt. Dit past bij downloads, links in e-mails, en alles wat een browser direct moet ophalen, zoals een afbeeldingstag of een pdf-viewer.

Ondertekende URL's worden op de server gegenereerd, nooit in de browser, omdat er inloggegevens voor nodig zijn die niet in frontendcode mogen staan. En de verlooptijd moet passen bij het gebruik: minuten voor een afbeelding in de pagina, een uur voor een downloadlink, hooguit een dag voor iets wat per e-mail wordt verstuurd. Een verlooptijd van een jaar is een publieke URL in vermomming.

## De Padstructuur Is Uw Rechtenmodel

Opslagpolicies matchen op het pad van het object, waardoor de padindeling bepaalt of uw regels überhaupt uit te drukken zijn.

Een goede standaard zet de eigenaar vooraan: `organisatie-id/gebruiker-id/document-id.pdf`. Een policy kan dan zeggen dat een gebruiker objecten mag lezen waarvan het eerste padsegment overeenkomt met een organisatie waartoe hij behoort - één regel voor elk bestand dat het product ooit zal opslaan.

De indeling die u moet vermijden, is een platte bucket met bestanden genoemd naar de originele upload, waardoor eigenaarschap niet uit het pad af te leiden is en elke controle een database-opzoeking wordt - als die al plaatsvindt.

Nog twee gewoontes. Genereer de bestandsnaam zelf in plaats van de naam te vertrouwen die de computer van de gebruiker aanleverde, omdat originele namen informatie lekken en omdat ze botsen. En houd per bestand een databaserij bij die vastlegt wie het uploadde, wanneer, het pad, de grootte en het contenttype, zodat de opslagbucket nooit uw enige registratie is van wat er bestaat.

## Valideer Uploads op de Server

De extensie in een bestandsnaam is een bewering, geen feit. Een bestand genaamd `foto.jpg` kan van alles bevatten, en een controle van het bestandstype in de browser is kinderlijk eenvoudig te omzeilen.

Wat er op de server toe doet: een groottelimiet passend bij het bestandstype, een toegestane lijst van contenttypes gecontroleerd aan de hand van de werkelijke inhoud van het bestand in plaats van de naam, en een regel dat geüploade bestanden nooit worden teruggeserveerd met een contenttype dat de uploader bepaalt. Het specifieke gevaar is een HTML- of SVG-bestand dat vanaf uw domein wordt geserveerd, dat script kan uitvoeren in de context van uw applicatie en kan lezen waar de sessies van uw gebruikers bij kunnen.

Uploads op een apart domein opslaan in plaats van op het domein van uw applicatie neemt die hele categorie problemen weg, wat een stil argument is voor ondertekende URL's vanaf de opslaghost in plaats van bestanden via uw eigen app door te sturen.

## Een Bestaand Product naar Privé Verplaatsen

De migratie is overzichtelijk en de moeite waard om in één keer te doen, omdat de tussenstand slechter is dan beide uiteinden.

Maak de privébucket aan met zijn policies. Kopieer de objecten over, herschrijf de paden onderweg naar de indeling met de eigenaar vooraan, en leg het nieuwe pad van elk bestand vast in uw database. Pas de applicatie aan om ondertekende URL's op te vragen in plaats van permanente op te slaan - dit is het deel dat de meeste code raakt, omdat permanente URL's meestal al in databasekolommen zijn opgeslagen en in verstuurde e-mails zijn opgenomen.

Laat de oude bucket daarna een korte periode staan maar geblokkeerd, terwijl u kijkt of er nog iets naar vraagt, en verwijder hem daarna.

Wat u specifiek moet controleren: e-mails en geëxporteerde documenten met oude publieke links. Die blijven na de migratie werken tenzij u ze bewust breekt, en het zijn precies de links die het meest waarschijnlijk buiten het bedrijf van uw klant zijn doorgestuurd.

## Afbeeldingen Zijn een Speciaal Geval

Foto's en schermafbeeldingen vormen in de meeste producten het grootste deel van de uploads, en ze brengen twee problemen mee die documenten niet hebben.

Het eerste is grootte. Een telefoonfoto is enkele megabytes, en een pagina die er veertig op miniatuurformaat toont terwijl de originelen worden gedownload, is traag voor de gebruiker en duur voor u. Genereer afgeleide versies - een miniatuur en een weergaveformaat - bij het uploaden, sla ze op naast het origineel, en serveer de kleinste die in de context past. Supabase kan afbeeldingen op verzoek omzetten, wat eenvoudiger is dan een eigen pipeline bouwen en voor de meeste producten volstaat.

Het tweede is metadata. Foto's bevatten EXIF-gegevens, vaak inclusief de GPS-coördinaten van waar ze zijn genomen. Een product waarin gebruikers foto's uploaden van schade, vastgoed, apparatuur of zichzelf, is een product dat ongemerkt locatiegeschiedenis verzamelt. Verwijder EXIF bij het uploaden tenzij u een reden hebt om het te bewaren, en bewaart u het, zeg dat dan in uw privacyverklaring.

Nog een gewoonte die het overnemen waard is: vertrouw ook de afmetingen van een afbeelding niet van de client. Een gemanipuleerd bestand dat beweert enorm te zijn, kan het geheugen uitputten van wat het ook verwerkt. Stel een limiet in, weiger wat erboven zit, en behandel de mislukking als een normale uitkomst in plaats van een uitzondering die het verzoek onderuithaalt.

## Opslagkosten Groeien Stil

Anders dan een database kondigt opslag zelden een probleem aan - het verschijnt gewoon op de factuur.

Drie dingen drijven het in door AI gebouwde producten, en alle drie zijn te vermijden. Originelen die voor altijd worden bewaard terwijl alleen afgeleide versies ooit worden getoond. Wezen die achterblijven bij verwijderde records, uploads die halverwege een formulier zijn afgebroken, en duplicaten die ontstaan wanneer een gebruiker na een mislukking opnieuw uploadt. En egress, de kosten van het steeds opnieuw serveren van hetzelfde grote bestand omdat er niets in de cache staat.

Een maandelijkse telling van objecten en totale bytes, vergeleken met het aantal bestanden dat uw database kent, vangt alle drie op. Lopen de twee getallen uiteen, dan hebt u wezen, en een opruimtaak die objecten zonder bijbehorende databaserij verwijdert - voorzichtig uitgevoerd, eerst als proefrun - levert meestal meer ruimte op dan oprichters verwachten.

## Dit Inrichten

Voor een bestaande app kost dit doorgaans twee tot drie dagen: buckets gecontroleerd en ingedeeld, een privébucket aangemaakt met padgebaseerde policies, objecten gemigreerd naar een indeling met de eigenaar vooraan en een databaserij per bestand, ondertekende URL's op de server gegenereerd met verlooptijden passend bij het gebruik, uploadvalidatie op werkelijk contenttype en grootte, gegenereerde bestandsnamen, de applicatie aangepast zodat ze geen permanente URL's meer opslaat, oude publieke links opgespoord en buiten gebruik gesteld, en een controle dat het verwijderen van het record van een gebruiker ook zijn objecten verwijdert.

LaunchStudio pakt dit aan in beveiligingswerk aan door AI gebouwde producten, waar het een van de meest voorkomende bevindingen is. De engineering komt van Manifera - elf jaar, 120+ engineers, en klanten als Vodafone, TNO en CFLW die bestandsafhandeling behoorlijk serieus nemen.

[Vraag ons naar uw bucketinstellingen te kijken](https://launchstudio.eu/nl/#contact). Het kost tien minuten om te controleren en het is meestal het eerste waar we naar kijken.

## Echt voorbeeld

### Twaalfhonderd Documenten op het Open Internet

Bram Nieuwenhuijs bouwde Hypotheekmap met Lovable: een tool waarmee hypotheekadviseurs documenten van klanten verzamelen - loonstroken, arbeidscontracten, bankafschriften, identiteitsbewijzen - en een compleet dossier aan de geldverstrekker doorgeven.

Uploads gingen naar een publieke bucket, genoemd naar de achternaam van de klant en het documenttype. De applicatie werkte goed en 26 adviseurs gebruikten haar met zo'n 400 klanten.

Een klant merkte het op. Hij kopieerde de URL van zijn eigen loonstrook, veranderde de achternaam erin in die van een vriend die dezelfde adviseur had, en het arbeidscontract van de vriend werd geladen. Hij mailde Bram, beleefd, op een zondag.

Drie werkdagen: een privébucket met policies die matchen op het organisatiesegment van het pad; alle 1.247 objecten gemigreerd naar een indeling `adviseur-id/klant-id/document-id`, met gegenereerde identificaties in plaats van namen, en een `documents`-tabel die uploader, pad, grootte, type en tijdstip vastlegt; het genereren van ondertekende URL's verplaatst naar de server, met een verlooptijd van vijftien minuten voor bekijken en een uur voor downloaden; uploadvalidatie op werkelijk contenttype met een limiet van 25 MB; de oude bucket geblokkeerd en daarna verwijderd; de 180 eerder uitgegeven documentlinks die in verstuurde e-mails stonden ongeldig gemaakt, met adviseurs geïnformeerd om opnieuw te delen vanuit het product; en het verwijderen van een account uitgebreid zodat ook opgeslagen objecten worden verwijderd, wat nooit was gebeurd.

**Resultaat:** het lek was binnen de week gedicht. Bram meldde het incident bij de Autoriteit Persoonsgegevens met een beschrijving van de oplossing, en informeerde de 26 adviseurs en de klanten van wie documenten bereikbaar waren geweest. Twee adviseurs zeiden dat de transparantie de reden was dat ze bleven.

> *"Hij raadde één URL. Er kwam geen hacken aan te pas - mijn bestandsnaamgeving was de kwetsbaarheid, en ik had die gekozen omdat het beheerscherm er makkelijker door te lezen was."*
> - **Bram Nieuwenhuijs, Oprichter, Hypotheekmap (Nieuwegein)**

**Kosten & Doorlooptijd:** €3.300 (bucketmigratie en policyontwerp, herstructurering van paden, bestandsregister, ondertekende URL's op de server, uploadvalidatie, buiten gebruik stellen van links, afhandeling bij verwijderen, incidentdocumentatie) - afgerond in 3 werkdagen.

## Veelgestelde vragen

### Betekent een publieke Supabase-bucket publiek voor mijn ingelogde gebruikers?

Nee. Het betekent leesbaar voor iedereen op internet die de URL heeft - geen sessie, geen token, geen verloopdatum. Gebruik voor alles wat een gebruiker uploadt een privébucket.

### Zijn ondertekende URL's veilig om naar klanten te mailen?

Ja, met een verstandige verlooptijd. Een uur is redelijk voor een downloadlink. Een ondertekende URL die een jaar geldig is, is in de praktijk een publieke URL en moet ook zo worden behandeld.

### Waar moeten ondertekende URL's worden gegenereerd?

Op de server, altijd. Ze in de browser genereren vereist inloggegevens die nooit in frontendcode mogen staan, en die sleutel geeft toegang tot alles in de bucket.

### Wat is er mis met het bewaren van de originele bestandsnaam van de gebruiker?

Hij lekt informatie, hij botst, en voorspelbare namen maken een bucket af te lopen. Genereer uw eigen identificatie en bewaar de originele naam in een databasekolom als u die wilt tonen.

### Verwijdert het verwijderen van een gebruiker ook zijn bestanden?

Niet tenzij u dat hebt gebouwd. Opslagobjecten en databaserijen zijn aparte systemen, en weesbestanden die een accountverwijdering overleven, zijn zowel een privacyprobleem als een groeiende opslagrekening.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Betekent een publieke Supabase-bucket publiek voor ingelogde gebruikers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee - hij is leesbaar voor iedereen met de URL, zonder authenticatie of verloopdatum. Uploads van gebruikers horen in een privébucket."
      }
    },
    {
      "@type": "Question",
      "name": "Zijn ondertekende URL's veilig om naar klanten te mailen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, met een korte verlooptijd. Een uur past bij een downloadlink; een URL die een jaar geldig is, is in feite publiek."
      }
    },
    {
      "@type": "Question",
      "name": "Waar moeten ondertekende URL's worden gegenereerd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Op de server. Ze in de client genereren vereist inloggegevens die toegang geven tot de hele bucket en nooit in frontendcode mogen komen."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik de originele bestandsnaam van de gebruiker bewaren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Genereer uw eigen identificatie - originele namen lekken informatie, botsen en maken buckets af te lopen. Sla de weergavenaam op in de database."
      }
    },
    {
      "@type": "Question",
      "name": "Verwijdert het verwijderen van een gebruiker ook de geüploade bestanden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Alleen als u dat hebt gebouwd. Opslag en database zijn gescheiden, en weesobjecten zijn zowel een privacyprobleem als een groeiende rekening."
      }
    }
  ]
}
</script>
