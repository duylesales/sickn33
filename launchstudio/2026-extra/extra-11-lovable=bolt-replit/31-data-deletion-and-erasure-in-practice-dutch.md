---
Titel: "Supabase-beveiliging: Gegevensverwijdering en AVG-recht op vergetelheid in de praktijk"
Trefwoorden: supabase beveiliging, recht op vergetelheid implementatie, dataretentie verwijdering, account verwijderen flow, ai app beveiliging, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Supabase-beveiliging: Gegevensverwijdering en AVG-recht op vergetelheid in de praktijk

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Supabase-beveiliging: Gegevensverwijdering en AVG-recht op vergetelheid in de praktijk",
  "description": "Verwijderen is makkelijk beloofd maar complex om te bouwen: referentiële integriteit, kopieën bij derden, backups en wettelijke bewaarplichten. Een praktische handleiding voor AI-gebouwde software.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-03",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/data-deletion-and-erasure-in-practice" }
}
</script>

Het verzoek is vier regels kort en volkomen redelijk: *"Wilt u alstublieft mijn account en alle gegevens die u over mij bewaart definitief wissen?"* Je privacyverklaring belooft dat je dit netjes doet. Je applicatie heeft een rode knop 'Account verwijderen' die één rij uit de tabel `users` wist - terwijl er op grofweg elf andere plekken nog steeds herleidbare persoonsgegevens van deze gebruiker rondzwerven.

Gegevensverwijdering is het duidelijkste voorbeeld van een belofte die eenvoudig opgeschreven is in een juridische policy, maar technisch aanzienlijke diepgang vereist. Het is bovendien functionaliteit die AI-codeertools vrijwel nooit uit zichzelf genereren, omdat niets in het beschrijven van een prototype impliceert dat data ooit daadwerkelijk moet verdwijnen.

*Let op: dit artikel biedt praktische en technische inzichten, geen formeel juridisch advies; de exacte reikwijdte van wettelijke verplichtingen verschilt per situatie.*

## Welke plekken een verwijdering werkelijk moet bereiken

Begin eens met het in kaart brengen van álle locaties waar de gegevens van één enkele gebruiker binnen jouw infrastructuur leven. Voor een typische SaaS-applicatie is die lijst veel langer dan oprichters verwachten:

**Het gebruikersrecord zelf.** Het eenvoudigste deel, en meestal het enige dat de wisknop daadwerkelijk verwijdert.

**Alles wat de gebruiker heeft aangemaakt.** Boekingen, geplaatste advertenties, chatberichten, reacties en bestanden. Een deel is puur van henzelf; een ander deel raakt direct andere gebruikers - en daar begint de complexiteit.

**Geüploade bestanden in cloudopslag.** Bestanden in Supabase Storage of S3 hebben een eigen levenscyclus en verdwijnen niet automatisch wanneer een database-rij wordt gewist.

**Kopieën bij externe diensten.** Het e-mailadres bij je e-mailprovider (zoals Resend of Postmark). Het unieke gebruikers-ID in je foutopsporingssoftware (zoals Sentry), gekoppeld aan stack traces. Klantgegevens en betaalhistorie bij Stripe of Mollie. Registraties in je analysetool of helpdesksysteem.

**Server- en applicatielogs.** Logs bevatten regelmatig IP-adressen, e-mailadressen en soms zelfs complete payloads van eerdere HTTP-verzoeken.

**Backups.** Databasebackups bevatten een bevroren momentopname van het volledige systeem op het tijdstip dat ze gemaakt werden.

Een verwijderprocedure die enkel het eerste punt raakt en de overige negeert, is geen gegevensverwijdering. Het is simpelweg het verbergen van een account.

## De gegevens die je mag - en soms verplicht moet - bewaren

Het recht op gegevenswissing onder de AVG (GDPR) is niet absoluut. Inzicht in de uitzonderingen voorkomt zowel ondoordacht overmatig wissen als de paniek dat je je complete financiële administratie zou moeten vernietigen:

**Financiële transacties en facturen.** Facturen en betaalgegevens vallen onder de wettelijke fiscale bewaarplicht (in Nederland doorgaans zeven jaar voor de Belastingdienst). Deze administratie móét bewaard blijven. De juiste aanpak: bewaar uitsluitend wat wettelijk verplicht is en verwijder alle niet-fiscale data.

**Gegevens ter onderbouwing van een rechtsvordering.** Informatie die noodzakelijk is om juridische claims te onderbouwen of af te weren, mits proportioneel bewaard en niet oneindig.

**Gegevens die andere personen aangaan.** Een chatgesprek tussen twee gebruikers, een recensie over een verkoper of een gedeeld document: het verwijderen van het account van partij A geeft je niet het recht om de context van partij B zomaar te vernietigen. Anonimiseren van de vertrekkende partij is hier doorgaans de juiste route.

**Geaggregeerde statistieken** die op geen enkele wijze meer herleidbaar zijn tot een individu.

Dit betekent dat verwijdering zelden een blinde `CASCADE DELETE` is. Het is een doordachte set beslissingen per datatype: definitief wissen, anonimiseren of bewaren met een expliciete juridische grondslag en bewaartermijn.

## Anonimiseren is meestal de praktische oplossing

Voor alle data die verweven is met andere gebruikers of met je eigen bedrijfshistorie, is het vervangen van identificerende velden vrijwel altijd beter dan het botweg verwijderen van de databaserij.

Een boeking verandert in een anonieme boeking die nog steeds meetelt in de omzethistorie en bezettingsgraad van een locatie. Een recensie behoudt zijn tekst en sterrenscore, maar verliest de naam en profielfoto van de auteur. Een conversatie blijft leesbaar voor de overblijvende gebruiker, waarbij de gesprekspartner wordt getoond als "Verwijderde gebruiker".

Het cruciale detail: anonimisering moet waterdicht zijn. Het vervangen van een voornaam terwijl je het e-mailadres, telefoonnummer, woonadres of een uniek account-ID laat staan, is geen anonimisering - het is slechts een ander label. Als de overgebleven velden iemand direct of indirect kunnen identificeren, is er juridisch nog steeds sprake van persoonsgegevens.

## Het probleem van referentiële integriteit in je database

Verwijder je een gebruikersrij waar andere tabellen naar verwijzen (foreign keys)? Dan weigert PostgreSQL de bewerking, óf er ontstaan zwevende weesrecords (orphans) die je applicatie niet verwacht. Dat leidt vervolgens tot 500-serverfouten op pagina's die proberen gegevens op te halen van een niet-bestaande gebruiker.

Dit is de praktische reden waarom gegevenswissing een software-engineeringtaak is en geen simpel knopje. Voor elke databaserelatie moet vooraf een expliciete keuze worden vastgelegd in het databaseschema (`ON DELETE SET NULL`, `ON DELETE CASCADE` of een aangepaste triggerfunctie die velden anonimiseert), in plaats van te hopen dat de frontend-code dit netjes afhandelt.

Applicaties die dit overslaan, eindigen met een verwijderfunctie die niemand durft uit te voeren. Verwijderverzoeken worden dan handmatig afgehandeld met gevaarlijke SQL-scripts - en uiteindelijk, door tijdgebrek, helemaal niet meer.

## Externe diensten en backups, eerlijk uitgelegd

**Externe platformen** vereisen een eigen geautomatiseerd pad. De meeste SaaS-leveranciers bieden API's om een contactpersoon of profiel definitief te wissen. Neem deze API-aanroepen op in je centrale verwijderingsfunctie. Handmatige stappen overleven de drukte van een werkweek immers zelden.

**Backups** vormen het onderdeel waar oprichters vaak omheen draaien. Gewiste data blijft aanwezig in gemaakte backups totdat die backups volgens hun rotatieschema verlopen en worden overschreven. Dit is een algemeen geaccepteerde technische realiteit onder de AVG. De juiste handelwijze: leg de retentietijd van je backups helder vast (bijvoorbeeld 30 dagen), zorg ervoor dat bij een eventuele backupherstelactie eerder gewiste gebruikers opnieuw worden verwijderd, en claim nooit onmogelijke 'onmiddellijke vernietiging in alle universums tegelijk'.

Wees hier eerlijk en transparant over in je privacyverklaring; dat schept oneindig veel meer vertrouwen dan een vage belofte die technisch onhaalbaar is.

## Hoe een deugdelijk verwijderingsproces eruitziet in je product

**Een self-service verwijderoptie in de app.** Verschillende appstores en platformen stellen dit tegenwoordig verplicht. Het is bovendien efficiënter dan een eindeloze stroom support-e-mails.

**Bevestiging en een bedenktijd (grace period).** Een kort venster (bijvoorbeeld 14 dagen) waarin een account desgewenst nog hersteld kan worden, voorkomt paniek na een impulsieve actie en bespaart je supporttijd.

**Een centrale verwijderprocedure** die in een vaste volgorde de database, storage, externe API's en logs bijwerkt, en een definitieve status vastlegt zodra alles is voltooid.

**Verantwoording en audit-trail.** Een minimaal logrecord dat registreert dát de verwijdering heeft plaatsgevonden, op welk tijdstip, en welke data op basis van welke wettelijke bewaarplicht behouden is gebleven.

**Geautomatiseerde bewaartermijnen (retentie)** voor overige tijdelijke data, zodat gegevens vanzelf verouderen en verdwijnen zonder dat iemand eraan hoeft te denken.

## Een test die je deze week zelf kunt uitvoeren

Maak een nieuw account aan in je eigen app. Gebruik het product zoals een echte klant: maak een boeking, upload een bestand, trigger een e-mailnotificatie en forceer een foutmelding. Klik vervolgens op 'Account verwijderen' en ga direct op onderzoek uit:

- Is de rij uit de `users`-tabel verdwenen?
- Staan de geüploade bestanden nog in je storage bucket?
- Staat het contact nog in je mailingtool?
- Is het gebruikers-ID nog traceerbaar in Sentry?
- Crasht er een openbare pagina waar deze gebruiker ooit iets heeft geplaatst?
- Vind je het e-mailadres nog terug als je de hele database doorzoekt?

Vrijwel elke oprichter die deze test voor het eerst uitvoert, ontdekt persoonsgegevens op minstens drie onverwachte plekken. Die bevindingen vormen je directe actielijst. Het is aanzienlijk prettiger om die zelf te ontdekken dan geconfronteerd te worden door een alerte klant of een toezichthouder.

## Het daadwerkelijke verwijderpad inrichten

Dit is overzichtelijk, afgebakend ingenieurswerk dat een permanent en robuust antwoord biedt op vragen die elke zakelijke klant uiteindelijk stelt. LaunchStudio richt dit in als onderdeel van het productierijp maken van AI-gebouwde software: een datamatrix per datatype (wissen, anonimiseren of bewaren), regels op databaseschemaniveau zodat er geen zwevende data achterblijft, geautomatiseerde opschoning van bestanden en externe API's, automatische retentie-routines, een self-service flow met bedenktijd en sluitende documentatie voor privacy-audits.

De interface die je hebt ontwikkeld in Lovable blijft exact behouden. De engineering is van Manifera - elf jaar ervaring met bedrijfskritische systemen voor partijen zoals Vodafone, TNO en CFLW, vanuit Amsterdam en Ho Chi Minhstad - en maakt deel uit van het [Launch Ready-pakket](https://launchstudio.eu/nl/#packages).

Wist jouw applicatie momenteel slechts één enkele databaserij? [Beschrijf je project](https://launchstudio.eu/nl/#contact) en wij brengen binnen één werkdag in kaart wat een veilige verwijderprocedure vereist.

## Bewaartermijnen: Verwijderen waar niemand om heeft gevraagd

Verwijderverzoeken van gebruikers vormen slechts de helft van het vraagstuk. De grotere helft betreft data die uit zichzelf moet verdwijnen. Dit is waar AI-apps geruisloos risico's opstapelen, omdat een gegenereerd prototype standaard nooit iets opruimt.

**Koppel een vaste bewaartermijn aan elk datatype.** Accounts die al meerdere jaren inactief zijn. Oude chatsessies van de helpdesk. Applicatielogs en audit-trails. Foutrapporten met request payloads. Verlopen exports in cloudopslag. Concepten die halverwege zijn verlaten. Elk datatype verdient een bewaartermijn - een zakelijke beslissing, geen puur technische.

**Automatiseer de opruiming.** Een bewaarbeleid dat afhankelijk is van handmatige acties is een dode letter. Een geplande cronjob die periodiek verouderde data wist en rapporteert hoeveel records zijn opgeruimd, is dat wel.

**Log wat er is verwijderd, niet de inhoud.** Noteer uitsluitend aantallen en categorieën, zodat je kunt aantonen dat het beleid wordt gehandhaafd zonder opnieuw persoonsgegevens vast te leggen.

**Waarschuw gebruikers vóór accountverwijdering.** Stuur twee weken voordat een inactief account definitief wordt gewist een vriendelijke herinnering. Dit voorkomt teleurstellingen en reactiveert regelmatig slapende klanten.

**Test de eerste run grondig.** De allereerste keer dat een opschoonscript draait op een database die nog nooit data heeft gewist, verwijdert het vaak enorme hoeveelheden data. Test dit altijd eerst op een staging-kopie vóórdat je het op productie loslaat.

Het oneindig bewaren van persoonsgegevens is precies waar toezichthouders en zakelijke inkopers over vallen. "Wij bewaren alles voor altijd omdat niemand een opschoonroutine heeft gebouwd" is een onverdedigbaar antwoord.

## Ontwerp de hersteloptie vóórdat je de definitieve wisknop bouwt

Een correct uitgevoerde verwijdering is per definitie onomkeerbaar. Dat introduceert direct een menselijk risico: vergissingen.

Een gebruiker die in een vlaag van frustratie zijn account wist en een uur later spijt heeft, een supportmedewerker die per ongeluk het verkeerde account aanklikt, of een retentiescript met een verkeerd geconfigureerde datumfilter - al deze situaties komen regelmatig voor, en geen enkele is te herstellen zodra data fysiek gewist is.

De beproefde standaard is een **bedenktijd (grace period)**: markeer het record direct als verwijderd (`deleted_at`), sluit de gebruiker onmiddellijk buiten van de applicatie zodat de verwijdering direct voelbaar is, en wis de data pas na een vooraf vastgestelde periode definitief (bijvoorbeeld na 14 dagen).

Twee voorwaarden maken dit integer: de gegevens moeten tijdens de bedenktijd daadwerkelijk ontoegankelijk zijn voor normale queries (afgedwongen via RLS), en de bewaartermijn moet vooraf duidelijk aan de gebruiker worden gecommuniceerd.

## Echt voorbeeld

### Een buurtplatform waarvan verwijderde leden continu bleven opduiken

Hanneke Doorn runde Buurtkracht, een lokaal vrijwilligersplatform dat door meerdere wijkteams en gemeentelijke instellingen rond Zwolle werd gebruikt. Buurtbewoners plaatsten hulpvragen en boden ondersteuning aan; veel van die conversaties bevatten privacygevoelige zorg- en leefsituaties.

De 'Account verwijderen'-knop in de Lovable-app deed slechts één ding: de rij uit de tabel `users` verwijderen. Alle overige data bleef onaangeroerd: de volledige naam van de persoon bleef zichtbaar op alle geplaatste hulpvragen, geüploade pasfoto's bleven opvraagbaar in de openbare storage bucket, het e-mailadres bleef actief in de mailingtool waardoor wekelijkse buurtupdates gewoon doorgingen, en het gebruikers-ID bleef opduiken in Sentry.

Twee leden trokken aan de bel. De ene ontving zes weken na uitschrijving nog steeds wekelijkse overzichten; de andere ontdekte dat haar volledige naam nog steeds gekoppeld stond aan een kwetsbare hulpvraag over haar thuissituatie.

In zeven werkdagen werd het complete proces herzien: een datamatrix over veertien verschillende datatypes (wissen, anonimiseren of bewaren met motivering); databaseschema-triggers herschreven zodat verwijdering nooit weesrecords achterlaat; geplaatste oproepen en reacties geanonimiseerd ("Oud-lid") zodat de buurthistorie behouden bleef; bestanden direct en geverifieerd uit storage verwijderd; de mailingprovider en Sentry via API's gekoppeld aan de verwijderprocedure; een self-service flow met een bedenktijd van veertien dagen; automatische retentie voor inactieve accounts; en een sluitend auditlogboek.

**Resultaat:** beide leden ontvingen een feitelijk en geruststellend rapport van wat er exact was verwijderd en geanonimiseerd. Vier maanden later doorstond het platform glansrijk een formele privacy-audit van een deelnemende gemeente, waarbij de gegevensverwijdering expliciet als pluspunt werd genoemd.

> *"In mijn privacyverklaring stond dat mensen het recht hadden om vergeten te worden. In de praktijk had ik een knop gebouwd die alleen hun inlog verborg en alle gevoelige data gewoon liet staan."*
> - **Hanneke Doorn, Oprichter, Buurtkracht (Zwolle)**

**Kosten & Doorlooptijd:** € 3.400 (datamatrix, schemaregels, API-integraties derden, self-service flow, geautomatiseerde retentie) - afgerond in 7 werkdagen.

## Veelgestelde vragen

### Verwijdert het wissen van een gebruikersrecord automatisch alle bijbehorende data?
Vrijwel nooit. Geüploade bestanden, content, records bij je e-mailprovider, transactiehistorie bij je betaalprovider en gegevens in applicatielogs blijven zelfstandig bestaan. Een deugdelijke verwijderprocedure moet elk van die systemen expliciet opschonen.

### Moet ik verplicht alle gegevens wissen wanneer een klant daarom vraagt?
Nee. Gegevens die onder een wettelijke bewaarplicht vallen (zoals facturen voor de belastingdienst) móét je bewaren. Ook gegevens ter verdediging van juridische claims of content die andere gebruikers aangaat hoef je niet integraal te vernietigen. Hanteer een specifiek beleid per datatype.

### Hoe ga ik om met persoonsgegevens in databasebackups?
Data in backups blijft aanwezig totdat de backup volgens het vaste rotatieschema wordt overschreven. Dit is algemeen geaccepteerd onder de AVG. Vermeld deze bewaartermijn eerlijk in je privacyverklaring en zorg dat gewiste data bij een eventueel herstel opnieuw wordt verwijderd.

### Is anonimiseren een acceptabel alternatief voor definitief wissen?
Ja, en voor gegevens die verweven zijn met andere gebruikers is het meestal de enige werkbare oplossing. De anonimisering moet wel écht zijn: als de overgebleven data direct of indirect herleidbaar blijft tot een individu, is er nog steeds sprake van persoonsgegevens.

### Hoe weet ik zeker of mijn verwijderfunctie daadwerkelijk werkt?
Maak een testaccount aan, gebruik alle functies van je product (uploaden, boeken, mails ontvangen) en klik op verwijderen. Doorzoek daarna al je systemen (database, storage, e-mailprovider, error tracker en logs) op dat specifieke e-mailadres. Vrijwel elke oprichter vindt bij de eerste test data op minstens drie plekken terug.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Verwijdert het wissen van een gebruikersrecord automatisch alle bijbehorende data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vrijwel nooit. Bestanden, geplaatste content en records in externe diensten zoals mailproviders en logs blijven bestaan en moeten expliciet worden opgeschoond."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik verplicht alle gegevens wissen wanneer een klant daarom vraagt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Gegevens onder wettelijke bewaarplichten (zoals facturen) blijven bewaard, evenals data die nodig is voor juridische claims of die andere gebruikers aangaat."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe ga ik om met persoonsgegevens in databasebackups?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Data blijft bewaard totdat backups volgens het rotatieschema verlopen. Vermeld deze termijn transparant en verwijder herstelde data opnieuw na een eventuele restore."
      }
    },
    {
      "@type": "Question",
      "name": "Is anonimiseren een acceptabel alternatief voor definitief wissen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, mits de anonimisering onomkeerbaar is en de overgebleven gegevens op geen enkele wijze meer herleidbaar zijn tot het individu."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe weet ik zeker of mijn verwijderfunctie daadwerkelijk werkt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Maak een testaccount aan, gebruik het intensief, verwijder het en doorzoek daarna handmatig je database, cloudopslag, mailingtools en foutenlogboeken op herleidbare sporen."
      }
    }
  ]
}
</script>
