---
Titel: "Back-ups Die U Nooit Heeft Teruggezet Zijn Geen Back-ups"
Trefwoorden: SaaS back-up herstel testen, point in time recovery, RPO RTO vroege startup, veilige back-up bestandsopslag, noodherstel drill procedure, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Back-ups Die U Nooit Heeft Teruggezet Zijn Geen Back-ups

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Back-ups Die U Nooit Heeft Teruggezet Zijn Geen Back-ups",
  "description": "Vrijwel elke SaaS-oprichter denkt dat zijn data veilig is omdat de hostingprovider 'automatische back-ups' belooft. Een gids over het testen van noodherstel, Point-in-Time Recovery, losse opslag van geüploade bestanden en het bepalen van uw RTO en RPO.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-03-22",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/backups-you-have-never-restored-are-not-backups" }
}
</script>

Vraag een software-oprichter of hij goede back-ups heeft, en het antwoord luidt vrijwel altijd: *"Ja, natuurlijk"*. Vaak uitgesproken met het zelfvertrouwen van iemand die tijdens de server-installatie een vinkje heeft gezet bij zijn cloudprovider (zoals Supabase, Railway of Render).

Stel vervolgens twee simpele vervolgvragen, en dat zelfvertrouwen verdampt ter plekke:
1. **Hoeveel uur aan klantdata bent u definitief kwijt als u nu direct moet terugzetten?**
2. **Hoeveel uur ligt uw hele platform plat terwijl u de back-up aan het inladen bent?**

Vrijwel niemand weet het antwoord. En dat betekent dat het eerlijke antwoord op de eerste vraag luidt: *"Ik heb ergens een bestandje staan, maar ik heb geen flauw idee of het werkt"*.

Dit is geen onwil. Back-ups zijn het ultieme voorbeeld van werk dat volstrekt onzichtbaar blijft — totdat het op een dag over het voortbestaan van uw hele onderneming beslist.

Er is echter één simpele, goedkope exercitie die een vage aanname omzet in harde feiten: **voer vóór de lancering één keer een complete hersteloefening (*restore drill*) uit**. 

Oprichters die dit doen, ontdekken gegarandeerd structurele gaten in hun beveiliging.

## De Twee Getallen Die Uw Echte Risico Bepalen

Negeer het technische jargon en focus op de zakelijke impact:

### 1. Hoeveel dataverlies kunt u zich permitteren? (*RPO - Recovery Point Objective*)
Draait uw databaseprovider één automatische snapshot per 24 uur? Dan betekent een crash om 17:00 uur dat al het werk dat uw klanten die dag hebben ingevoerd, **onomkeerbaar gewist is**. 

Voor een simpele hobby-app is dat misschien te overzien. Voor een zakelijke tool waarin accountants of planners hun dagelijkse werk doen, betekent dit direct contractbreuk en woedende klanten.

### 2. Hoe lang mag uw applicatie offline zijn? (*RTO - Recovery Time Objective*)
Dit is niet de tijd die het servercommando nodig heeft om een bestand in te lezen; het is het moment waarop uw klanten weer daadwerkelijk kunnen inloggen, inclusief het herstellen van API-sleutels, opslagkoppelingen en dataverificatie. 

Oprichters schatten dit vooraf op twintig minuten. In de praktijk — wanneer u dit voor het eerst doet onder immense stress om 02:00 uur 's nachts — duurt een ongeplande hersteloperatie **gemakkelijk vier tot acht uur**.

## Wat de Automatische Back-up van Uw Provider Wél en NIET Dekt

Moderne managed databaseplatforms — zoals Supabase, Railway, Render, Neon of managed PostgreSQL bij AWS/DigitalOcean — maken vrijwel allemaal automatisch back-ups. Dat is fantastisch en buitengewoon waardevol. Het is echter ook aanzienlijk beperkter dan de marketingpagina's suggereren, op manieren die u vóór de lancering helder voor ogen moet hebben:

**Frequentie en bewaartermijn verschillen drastisch per abonnementsvorm.** Gratis accounts en goedkope instappakketten bieden meestal slechts dagelijkse snapshots die maximaal zeven dagen worden bewaard, soms zelfs korter. *Point-in-time recovery* (PITR) — waarmee u de database kunt herstellen naar een specifieke minuut in het verleden in plaats van naar de snapshot van gisterennacht — is vrijwel altijd een betaalde premium-feature. Controleer wat uw specifieke hostingcontract daadwerkelijk levert, niet wat er op de algemene homepage staat.

**Back-ups dekken uitsluitend de database, niet uw complete applicatie.** Geüploade bestanden, factuur-PDF's en afbeeldingen in cloud-objectopslag (zoals AWS S3 of Supabase Storage) vallen hier buiten en vereisen hun eigen back-up- en replicatieconfiguratie. Hetzelfde geldt voor omgevingsvariabelen, API-sleutels en serverconfiguraties. Een databaseherstel waarbij alle geüploade klantbijlagen spoorloos zijn verdwenen, herstelt weliswaar de index, maar verliest de complete bibliotheek.

**Een back-up binnen hetzelfde cloud-account biedt slechts gedeeltelijke bescherming.** Het beschermt uitstekend tegen per ongeluk gewiste tabellen of softwarefouten. Het beschermt echter niet tegen een gehackt, geblokkeerd of door creditcardproblemen opgeschort cloud-account, waarbij uw back-ups exact even onbereikbaar zijn als de productiedatabase zelf. Eén periodieke kopie die extern wordt bewaard — bij een andere cloudprovider of op zijn minst in een strikt gescheiden cloud-account — dicht dit existentiële risico tegen minimale kosten.

**Een verwijderd project wist vaak direct alle gekoppelde back-ups mee.** Op meerdere platforms verwijdert het per ongeluk aanklikken van 'Delete Project' onmiddellijk alle daaraan gekoppelde automatische snapshots.
## Waar Back-ups Écht Voor Dienen

Het dramatische doemscenario — een meteorietinslag of een verwoestende brand in het datacenter van uw hostingprovider — is wat oprichters zich voorstellen, maar statistisch de minst waarschijnlijke oorzaak van dataverlies. De reële oorzaken zijn oneindig veel alledaagser en komen continu voor:

**Iemand voert een SQL-query uit zonder `WHERE`-clausule.** Een update- of delete-commando dat bedoeld was voor één testklant en per ongeluk álle rijen in de productietabel overschrijft. Dit is met afstand het meest voorkomende ernstige data-incident binnen vroege techbedrijven.

**Een databasemigratie loopt desastreus mis.** Een geautomatiseerd migratiescript dat per ongeluk een kolom verwijdert, hernoemt of verkeerd transformeert, wat pas wordt ontdekt nadat het live op productie is uitgerold.

**Een sluipende softwarefout wist data geruisloos.** Een foutieve cascade-verwijderingsregel (`ON DELETE CASCADE`) die stilletjes twee weken lang meer gerelateerde records wist dan de bedoeling was, voordat een klant het opmerkt. Dit scenario is bijzonder verraderlijk: alle back-ups van de afgelopen veertien dagen bevatten immers exact dezelfde corruptie. Dat is exact de reden waarom een langere bewaartermijn (retentie) vele malen belangrijker is dan louter back-upfrequentie.

**Een klant wist per ongeluk zijn eigen data en vraagt om herstel.** Geen nationale ramp, maar een doodgewone dinsdagochtend, en een verzoek dat zakelijke klanten als volkomen legitiem beschouwen.

Die laatste categorie verdient een eigen architectonische oplossing: het herstellen van een complete productiedatabase om de per ongeluk gewiste records van één klant terug te halen is volstrekt disproportioneel en wist alle recente data van al uw ándere klanten. *Soft deletion* — records in de database markeren met een vlaggetje `deleted_at` in plaats van ze direct met `DELETE` fysiek te vernietigen — lost 95% van deze supportvragen op zónder dat u ooit een back-up hoeft aan te raken. Het is oneindig veel goedkoper om dit vóór de livegang in te bouwen dan achteraf.
## De Hersteloefening (*Restore Drill*)

Hier ligt het daadwerkelijke werk dat telt, en het kost u precies één geconcentreerde middag:

Neem uw meest recente back-upbestand. Herstel het op een veilige plek die gegarandeerd géén productie is — een afzonderlijke testdatabase of een geïsoleerde staging-omgeving. Koppel een lokale kopie van uw applicatie aan deze herstelde database. Log in met een testaccount. Controleer persoonlijk of klantrecords intact zijn, of geüploade bestanden en afbeeldingen openen, en of de meest recente gegevens net zo actueel zijn als u verwachtte. Noteer elke handeling die u heeft verricht, elke vertraging en elk onverwacht probleem.

Vrijwel niemand voert deze oefening voor de eerste keer uit zonder op minimaal één onaangename verrassing te stuiten. Veelvoorkomende ontdekkingen tijdens een restore drill:
- De back-up bevat de database, maar de applicatie kan niet opstarten omdat cruciale encryptiesleutels of geheimen alleen in de productie-omgeving stonden en nergens zijn gedocumenteerd.
- Geüploade bestanden ontbreken volledig omdat cloudopslag nooit in het back-upscript zat.
- Het herstelproces duurt veertig minuten in plaats van de aangenomen vijf minuten.
- De meest recente data blijkt achttien uur oud te zijn in plaats van het veronderstelde ene uur.
- Het herstel vereist beheerdersrechten die slechts één persoon bezit, en diegene zit net in het vliegtuig.

Het concrete eindresultaat van deze middag is een beproefd, schriftelijk draaiboek met reële tijdsindicaties. Midden in de nacht, onder gigantische druk en met tierende klanten aan de telefoon, is het verschil tussen een beproefde checklist en paniekerige improvisatie het verschil tussen een beheersbaar incident en het faillissement van uw startup.

Het inrichten van complete back-updekking (inclusief bestandsopslag en configuraties), het toevoegen van een externe offsite-kopie en het opstellen van een getest hersteldraaiboek is standaard productiewerk. LaunchStudio, ondersteund door meer dan 11 jaar software engineering ervaring bij Manifera, maakt dit een vast onderdeel van uw livegangvoorbereiding. Een product dat echte klantdata verwerkt zonder geteste restore-procedure is simpelweg nog niet af. [Beschrijf uw project](https://launchstudio.eu/nl/#contact) voor een audit binnen één werkdag.
## Richtlijnen Voor een Betrouwbare SaaS

Hanteer deze nuchtere en bewezen standaarden, afgestemd op wat uw klanten feitelijk te verliezen hebben:

**Frequentie:** Dagelijkse geautomatiseerde snapshots als absolute ondergrens. Kies voor *point-in-time recovery* zodra klanten gedurende de werkdag intensief data invoeren, wat voor vrijwel elk zakelijk B2B-product geldt.

**Bewaartermijn (Retentie):** Minimaal dertig dagen. Zeven dagen is veel te kort om een sluipende softwarebug te overleven, wat precies het scenario is waarbij u verder terug in de tijd moet kunnen grijpen dan verwacht.

**Reikwijdte (Scope):** De database, alle geüploade bestanden en media, plus een veilige, versleutelde export van uw configuratieparameters en omgevingsvariabelen.

**Locatie:** Minimaal één periodieke kopie buiten het cloud-account waarin uw productieomgeving draait.

**Verificatie:** Eén complete hersteloefening (*restore drill*) vóór de officiële livegang, direct herhalen na grote infrastructurele wijzigingen, en daarna minimaal één à twee keer per jaar als vaste routine.

**Monitoring:** Een directe waarschuwing (alert via Slack of e-mail) wanneer een geplande back-up faalt. Stille uitval is de norm; back-upprocessen lopen vaak vast door triviale oorzaken — een verlopen API-token of een volle schijf — en niemand merkt het totdat de nood aan de man is.
## Echt voorbeeld

### De Back-ups Die Zes Weken Achterliepen op de Werkelijkheid

Emre Kaplan runde Loonstrook, een beveiligd portaal voor salarisstroken en personeelsdossiers voor kleine Nederlandse MKB-werkgevers, gebouwd in Lovable en draaiend op een beheerde Postgres-database. Dagelijkse automatische back-ups stonden aan, dus Emre maakte zich nergens zorgen om.

Tijdens een database-update werd een relationele `CASCADE`-regel per ongeluk verkeerd geconfigureerd. Telkens wanneer een werkgever een personeelsmutatie doorvoerde, wiste de database geruisloos de documentmetadata van eerdere jaargangen.

Het probleem werd pas **vijf weken later** ontdekt, toen een werkgever klaagde dat de jaaropgaven van vorig jaar niet meer zichtbaar waren.

Toen Emre de back-ups wilde raadplegen, kwam de schokkende realiteit naar boven:
1. De retentieperiode op zijn hostingpakket was slechts **14 dagen**. Alle beschikbare back-upbestanden bevatten de fout dus al!
2. De automatische back-ups bevatten **uitsluitend de SQL-tabellen**. De feitelijke PDF-documenten stonden in een losse S3-bucket waarvoor nooit een back-up was ingericht.

De daadwerkelijke PDF-bestanden stonden nog wel in de storage-bucket, maar de koppelingen naar werknemers en jaartallen waren definitief gewist. 

Het handmatig reconstrueren van de database aan de hand van ruwe bestandsnamen kostte vier volle werkdagen. Bij ruim 7% van de documenten kon de koppeling niet met 100% zekerheid worden vastgesteld, waardoor Emre werkgevers moest vragen om oude documenten opnieuw aan te leveren — een enorme deuk in het vertrouwen.

**Resultaat:** Binnen drie werkdagen implementeerde LaunchStudio een complete noodherstel-infrastructuur: Point-in-Time Recovery met 90 dagen retentie, geautomatiseerde dagelijkse back-ups van de S3-opslag, wekelijkse offsite kopieën naar een onafhankelijke cloudprovider, en Soft Deletion op alle gebruikersdossiers. De geteste herstelprocedure klaarde de klus voortaan in **35 minuten**.

> *"Ik had back-ups aanstaan. Ik had alleen nog nooit gecontroleerd wat er werkelijk in zat. Het antwoord bleek: ongeveer de helft van wat ik dacht."*
> — **Emre Kaplan, Oprichter, Loonstrook**

**Kosten & Doorlooptijd:** Volledige back-up- en herstelinrichting inclusief S3-synchronisatie en herstelprocedure opgeleverd binnen 3 werkdagen.

## Veelgestelde Vragen

### Zijn de automatische back-ups van mijn hostingprovider voldoende?
Nee. Ze dekken vrijwel uitsluitend de database en vergeten geüploade bestanden in object storage (S3). Bovendien is de bewaartermijn op goedkope plannen vaak te kort (7–14 dagen) en beschermen ze niet tegen een gehackt cloudaccount.

### Hoe vaak moet een SaaS-applicatie een back-up maken?
Minimaal dagelijks, aangevuld met Point-in-Time Recovery (PITR) als gebruikers continue data invoeren. Zorg voor een bewaartermijn van minstens 30 tot 90 dagen om sluipende bugs op te vangen.

### Wat is een 'restore drill' en hoe lang duurt dat?
Een brandoefening voor data: u zet een echte back-up terug in een testomgeving en controleert of de applicatie foutloos opstart en data toont. Dit kost een middag en legt vrijwel altijd ontbrekende configuraties of trage processen bloot.

### Hoe help je een klant die per ongeluk zijn eigen data heeft gewist?
Met 'Soft Deletion' in plaats van back-ups. Door records te markeren met `deleted_at` kunt u per ongeluk gewiste data met één klik terughalen, zonder een back-up te hoeven inladen die andermans recente werk overschrijft.

### Waarom moeten back-ups extern (offsite) worden opgeslagen?
Omdat een back-up binnen hetzelfde cloudaccount verloren gaat als uw account wordt opgeschort, gehackt of per ongeluk gewist. Een wekelijkse kopie bij een tweede opslagpartij sluit dit risico uit.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is het verschil tussen een back-up hebben en een back-up kunnen herstellen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een back-up is slechts een bestand; pas na een succesvolle hersteloefening weet u zeker dat de data compleet, functioneel en tijdig inzetbaar is."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom zijn standaard cloud-backups vaak incompleet?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat ze meestal alleen de relationele database bewaren en geüploade documenten in S3-opslag of omgevingsvariabelen negeren."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het gevaar van een korte bewaartermijn (retentie) van 7 dagen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sluipende softwarebugs wissen data vaak ongemerkt over weken; bij een retentie van 7 dagen zijn alle back-ups al met de fout besmet."
      }
    },
    {
      "@type": "Question",
      "name": "Wat betekenen RTO en RPO voor een SaaS?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "RPO is hoeveel uur dataverlies acceptabel is bij uitval; RTO is het aantal uren dat nodig is om de software weer volledig operationeel te krijgen."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom moet een back-up ook offsite worden bewaard?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Om dataverlies te voorkomen bij een volledige accountblokkade, gecompromitteerde credentials of een hostingbrede storing."
      }
    }
  ]
}
</script>
