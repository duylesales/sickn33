---
Titel: "Lovable Supabase: Soft Deletes, Archivering en Wat Je Bewaart"
Trefwoorden: lovable supabase, soft delete, bewaartermijnen, archivering, avg verwijderverzoek, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-oprichters / Indie Hackers
---

# Lovable Supabase: Soft Deletes, Archivering en Wat Je Bewaart

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Soft Deletes, Archivering en Wat Je Bewaart",
  "description": "Verwijderen heeft vier fundamenteel verschillende betekenissen: verbergen, bewaren voor eigen gebruik, bewaren wegens wettelijke plicht en permanent vernietigen. Hoe je alle vier inricht en de botsing tussen de AVG en fiscale bewaarplicht oplost.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-04",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/94-lovable-supabase-soft-deletes-archiving-and-what-you-keep" }
}
</script>

Een gebruiker klikt op de knop 'Verwijderen'. Wat moet er op dat moment onder de motorkap gebeuren?

Bij een applicatie die met behulp van AI-prompts is gebouwd, luidt het antwoord nagenoeg altijd hetzelfde: het database-record wordt direct en permanent gewist via een `DELETE`-opdracht. Dat is immers wat verwijderen letterlijk betekent in programmacode, en de prompt heeft nooit om iets anders gevraagd.

In de echte bedrijfsvoering betekent 'verwijderen' echter minstens vier totaal verschillende dingen, afhankelijk van wie er klikt en welk type record het betreft. Wanneer je die betekenissen door elkaar haalt, ontstaan twee tegenovergestelde maar even ernstige incidenten: data vernietigen die je wettelijk verplicht was te bewaren, of data bewaren die je op grond van de privacywetgeving wettelijk verplicht was te vernietigen.

## Vier betekenissen van 'verwijderen'

**1. Verberg het uit mijn overzicht.** Een gebruiker die zijn scherm wil opruimen. Hij verwacht dat het item uit zijn actieve lijst verdwijnt en zou verbijsterd zijn als blijkt dat het onherstelbaar weg is. *"Ik bedoelde niet voor altijd"* is het meest gehoorde supportticket bij elk softwareproduct zonder herstelfunctie.

**2. Haal het uit actief gebruik, maar bewaar het voor naslag.** Een geannuleerde order, het dossier van een oud-werknemer of een afgerond project. Het bedrijf moet hier in de toekomst nog naar kunnen verwijzen.

**3. Bewaar het omdat de wet dat dwingend voorschrijft.** Facturen, salarisadministraties en contracten. In Nederland geldt voor de basisadministratie een wettelijke fiscale bewaarplicht van 7 jaar (en 10 jaar voor gegevens over onroerende zaken). Stem dit altijd af met een accountant in plaats van aannames te doen.

**4. Wis het definitief en permanent, omdat iemand daar recht op heeft.** Een formeel AVG-verwijderverzoek ('recht op vergetelheid'), of het aflopen van je eigen geformuleerde bewaartermijn.

Een applicatie die uitsluitend optie 4 uitvoert terwijl de eindgebruiker dacht optie 1 te kiezen, is een wijdverbreid en gevaarlijk fenomeen.

## Soft delete als vaste standaard

Voor nagenoeg elk record dat een eindgebruiker zelfstandig kan wissen, is soft delete (logisch verwijderen) de enige verstandige standaard: een datumkolom (`deleted_at`) die vastlegt wanneer het item is gemarkeerd, waarbij reguliere query's deze rijen automatisch uitsluiten.

Drie spelregels zorgen dat dit betrouwbaar functioneert:

**Filter op één centrale plek.** Als elke afzonderlijke SQL-query moet onthouden om `WHERE deleted_at IS NULL` toe te voegen, vergeet een ontwikkelaar (of AI-prompt) dat vroeg of laat. Een gewist record duikt dan plotseling weer op in een kwartaalrapportage. Richt dit centraal in via je Row-Level Security policies of via PostgreSQL database-views, zodat álle toekomstige query's de uitsluiting automatisch overerven.

**Bied gebruikers een herstelmogelijkheid.** Een zichtbare prullenbak waaruit verwijderde items binnen een afgesproken termijn (bijvoorbeeld 30 of 90 dagen) met één klik hersteld kunnen worden. Dit transformeert je meest frequente supportvraag in een moeiteloze self-service handeling.

**Ruim periodiek geautomatiseerd op.** Soft-deleted records blijven rijen in je database: ze nemen schijfruimte in beslag, vertragen query's en bevatten persoonsgegevens die je niet langer mag verwerken. Laat een geplande cron-job records waarvan de hersteltermijn is verstreken geautomatiseerd definitief wissen (`hard delete`).

De operationele consequentie van soft delete is dat elke unieke constraint aandacht vereist: een verwijderd gebruikersaccount mag een nieuwe registratie met hetzelfde e-mailadres doorgaans niet blokkeren.

## Archiveren is een ander probleem

Soft delete beantwoordt de vraag: *"de gebruiker heeft dit weggegooid"*. Archiveren beantwoordt de vraag: *"dit proces is afgerond en we willen het niet langer in de weg hebben staan"*.

Afgesloten dossiers, voorgaande boekjaren en beëindigde abonnementen. Ze moeten opvraagbaar blijven voor audits, maar horen niet thuis in de operationele werkset. De technische uitvoering hangt af van je datavolume: een statuskolom (`is_archived`) die standaardviews uitsluiten is de eenvoudigste variant; het overhevelen van rijen naar aparte archieftabellen of het toepassen van PostgreSQL table partitioning op jaartal is de variant die telt zodra datavolumes substantieel worden.

Dit levert direct enorme prestatiewinst op. Een applicatie waarin elke zoekopdracht door vijf jaar aan historische data ploegt terwijl gebruikers uitsluitend naar het huidige kwartaal kijken, verricht viervoudig overbodig werk.

## Waar wettelijke bewaarplicht en het recht op vergetelheid botsen

Dit is het juridisch meest complexe vraagstuk, waar generieke adviezen vaak tekortschieten:

Een klant beroept zich op zijn recht op gegevenswissing onder de AVG (GDPR). Echter, een deel van zijn persoonsgegevens bevindt zich op verkoopfacturen die jij op grond van de Algemene wet inzake rijksbelastingen (AWR) minimaal zeven jaar moet bewaren. Deze twee verplichtingen wijzen in tegengestelde richtingen.

De juridische consensus is helder: het AVG-recht op gegevenswissing weegt niet op tegen een dwingende wettelijke bewaarplicht. De facturen moeten blijven bestaan, maar alle gegevens die níét onder die wettelijke plicht vallen moeten wél worden gewist. In de praktijk betekent dit dat je verplicht bewaarde data (de factuur met NAW-gegevens) strikt moet scheiden van niet-verplichte data: inloghistorie, browsegedrag, voorkeuren, geüploade documenten, marketingprofielen en supportgesprekken.

Systemen die alle klantgegevens op één grote hoop in één tabel gooien kunnen dit onderscheid technisch niet maken. Die scheiding is een architectuurbeslissing, geen beleidsdocument. Je moet dit inrichten vóórdat het eerste verwijderverzoek binnenkomt.

## Verwijderen moet overal reiken

Wanneer je een definitieve verwijdering uitvoert, is het wissen van de database-rij slechts de eerste stap. De verwijdering moet het gehele ecosysteem doordringen:

**Geüploade bestanden in object storage.** PDF-contracten, scans van identiteitsbewijzen en pasfoto's die in cloud storage buckets staan moeten direct worden gewist.

**Audit trails en systeemlogs.** Dit vraagt om nuance: het feit dát een mutatie heeft plaatsgevonden moet voor compliance behouden blijven, maar de herleidbare persoonsgegevens daarin moeten worden geanonimiseerd. Gebruik daarom onomkeerbare identifiers of pseudoniemen in plaats van platte persoonsnamen in logs.

**Zoekindexen en caches.** Verwijder de gegevens direct uit externe zoekmachines (zoals Algolia of Elasticsearch) en Redis-caches.

**Back-ups.** Het handmatig wissen van specifieke rijen uit historische database-back-ups is technisch onmogelijk. De toezichthouder (Autoriteit Persoonsgegevens) accepteert dat back-ups data vasthouden tot het einde van hun rotatiecyclus, mits je bewaartermijn voor back-ups strikt gedefinieerd, gedocumenteerd en gehandhaafd is (bijvoorbeeld maximaal 30 dagen).

**Verwerkers (derde partijen).** Externe SaaS-diensten waarnaar data is doorgestuurd (e-mailproviders, analytics, CRM) moeten eveneens een verwijderopdracht ontvangen.

Anonimiseren is vaak een superieure oplossing ten opzichte van wissen: het overschrijven van identificeerbare velden met geanonimiseerde waarden behoudt de datarelaties en geaggregeerde omzetstatistieken. Echte geanonimiseerde data kwalificeert juridisch niet langer als persoonsgegeven.

## Wat te bouwen, en in welke volgorde

1. **Soft delete** met een zichtbare prullenbak en automatische opschoning voor reguliere gebruikersacties.
2. **Strikte dataseparatie** tussen fiscaal verplichte documenten en overige persoonsgegevens.
3. **Archiveringsmechanismen** voor afgeronde projecten en historische jaargangen.
4. **Een complete wis-procedure** die naast de database ook cloudopslag, zoekindexen en externe tools bereikt.
5. **Een formeel bewaarbeleid** waarin per datacategorie exact staat vastgelegd hoe lang het bewaard wordt en waarom.
6. **Een audit-log voor verwijderverzoeken**, waarmee je bij een controle van toezichthouders kunt aantonen dat en wanneer een verzoek correct is afgehandeld.

## Wanneer een hele klant vertrekt

Het wissen van één record is eenvoudig. Het vertrek van een complete zakelijke klant (offboarding) is het scenario waar bijna niemand vooraf over nadenkt:

**De klant wil zijn data meenemen in een bruikbaar formaat.** Geen schermafbeeldingen of losse printjes, maar een machine-leesbare export (JSON/CSV) die in een ander systeem geïmporteerd kan worden. Bouw een self-service exportfunctie per tenant. Dit is overigens een standaardvraag bij zakelijke inkooptrajecten.

**Hanteer een coulanceperiode (grace period).** Directe verwijdering op de dag dat het contract afloopt is juridisch rigide maar zakelijk onverstandig: klanten bedenken zich, er ontstaat discussie over eindfacturen, of een medewerker herinnert zich na een week een vitaal document. Een contractueel vastgelegde periode (bijvoorbeeld 30 dagen) waarin het account geblokkeerd is maar herstelbaar blijft, voorkomt drama's.

**Voer de definitieve verwijdering geautomatiseerd uit.** Na afloop van de termijn moet het tenant-account geautomatiseerd en volledig worden gesaneerd. Slapende klantaccounts die jarenlang blijven rondzwerven omdat niemand een opschoonscript schreef, vormen een ernstig datalek- en compliancerisico.

**Bewaar verplichte facturen apart.** De facturen die jij aan de vertrekkende klant hebt gestuurd vallen onder jouw fiscale bewaarplicht; hun operationele data beslist niet.

## Verwijderlogica goed inrichten vóórdat iemand erom vraagt

Voor een actieve applicatie is dit een overzichtelijke ingreep: centrale soft delete via databasepolicies, automatische purge-jobs, archivering van gesloten dossiers, ontkoppeling van fiscale data, end-to-end verwijderoperaties over storage en indexen, en een gedocumenteerd bewaarbeleid.

LaunchStudio richt dit in als integraal onderdeel van de productiegereedheid, omdat privacytoezichthouders en zakelijke inkopers hier direct naar vragen. De software engineers zijn van Manifera: elf jaar ervaring met enterprise data-architectuur en AVG-naleving voor klanten zoals Vodafone, TNO en CFLW vanuit Amsterdam Herengracht 420 en Ho Chi Minhstad.

[Vertel ons welk type data jouw applicatie opslaat](https://launchstudio.eu/nl/#contact) voor een concreet advies, of bekijk onze [pakketten](https://launchstudio.eu/nl/#packages).

## Echt voorbeeld

### Een verwijderde medewerker en een loonstrook die mee verdween

Wendy Bosman bouwde met Lovable het platform Personeelsdossier: digitaal personeelsbeheer voor het mkb, in gebruik bij 29 bedrijven in de regio Hengelo en Enschede - arbeidsovereenkomsten, verzuimregistraties, beoordelingsverslagen en historische loonstroken.

Een 'verwijder'-actie voerde een directe SQL `DELETE` uit op het werknemersrecord. Er was geen prullenbak, geen archieffunctie en geen scheiding tussen operationele personeelsdata en gekoppelde salarisdocumenten.

Binnen één maand ontstonden twee ernstige incidenten. Een salarisadministrateur bij een klant verwijderde het dossier van een uitdienstgetreden medewerker om de lijst op te schonen, en wiste daarmee onbedoeld zeven jaar aan historische loonstroken - documenten die het bedrijf wettelijk verplicht was te bewaren en nergens anders meer bezat na een overstap van salarissoftware.

Vervolgens diende een voormalig werknemer bij een andere klant een officieel AVG-verwijderverzoek in. Wendy had geen technische mogelijkheid om het dossier gedeeltelijk te schonen: alle data over deze persoon zat in één tabel, inclusief de salarisdocumenten die haar klant wettelijk moest behouden. Haar opties waren het verzoek onrechtmatig weigeren of de wettelijke administratie van haar klant vernietigen.

In elf werkdagen werd de datastructuur professioneel herzien: soft delete werd ingevoerd op alle tabellen met een herstelperiode van 90 dagen (alleen herstelbaar door beheerders), waarbij de filtering centraal in de Supabase RLS-policies werd verankerd zodat alle query's de uitsluiting automatisch overnemen; een nachtelijke cron-job werd ingericht voor definitieve opschoning na 90 dagen; operationele personeelsdossiers werden fysiek ontkoppeld van fiscaal verplichte loonstroken; een archiefstatus werd geïntroduceerd zodat uitdienstgetreden personeel uit de actieve lijst verdwijnt zónder dataverlies; er werd een complete AVG-verwijderfunctie gebouwd die records, cloud storage-documenten en audit logs anonimiseert; er werd een categorie-specifiek bewaarbeleid opgesteld in overleg met een accountant en afgestemd met de 29 klanten; en een formeel verzoeklogboek werd geactiveerd.

De gewiste loonstroken van zeven jaar konden gelukkig grotendeels worden hersteld vanuit een databaseback-up van negen dagen oud. Het kleine resterende gat werd transparant aan de klant gerapporteerd.

**Resultaat:** Het AVG-verzoek werd vlekkeloos afgehandeld tot tevredenheid van zowel de burger als de werkgever (persoonsgegevens gewist, verplichte loongegevens behouden onder de wettelijke uitzondering), en het formele bewaarbeleid wordt tegenwoordig standaard meegeleverd bij de onboarding van elke nieuwe klant.

> *"Eén muisklik wiste een medewerker én zeven jaar aan loonstroken die mijn klant wettelijk verplicht was te bewaren. Diezelfde week vroeg iemand om gegevenswissing, en ik kon dat niet uitvoeren zonder de administratie van een ander te slopen."*
> - **Wendy Bosman, Oprichter, Personeelsdossier (Hengelo)**

**Kosten & Doorlooptijd:** € 5.100 (centrale soft delete met herstelvenster en policy-filtering, archivering, ontkoppeling van bewaarplichtige documenten, complete AVG-verwijderoperatie, anonimisering, bewaarbeleid, compliance-logging) - opgeleverd in 11 werkdagen.

## Veelgestelde vragen

### Moet een verwijderknop direct het databaserecord wissen?

Vrijwel nooit. In de meeste gevallen bedoelt de gebruiker *"haal dit uit mijn actieve scherm"* en verwacht hij een herstelmogelijkheid bij vergissingen. Gebruik een datumstempel (`deleted_at`), filter dit centraal in je policies, bied een herstelbare prullenbak aan en wis data pas geautomatiseerd na afloop van de hersteltermijn.

### Hoe voorkom ik dat verwijderde records per ongeluk opduiken in rapportages?

Door de uitsluiting van soft-deleted data op één centrale plek af te dwingen - in je Supabase Row-Level Security policies of via centrale database-views - in plaats van te hopen dat elke losse query in de applicatiecode `WHERE deleted_at IS NULL` onthoudt.

### Wat gebeurt er als de fiscale bewaarplicht botst met een AVG-verwijderverzoek?

Ze heffen elkaar niet op: data die je wettelijk verplicht bent te bewaren (zoals facturen) blijft behouden, terwijl alle overige data (activiteit, profielen, voorkeuren) definitief wordt gewist. Dit kan alleen als je fiscaal verplichte data strikt gescheiden opslaat van operationele gebruikersdata.

### Betekent een AVG-verwijderverzoek louter het wissen van database-rijen?

Nee. De verwijdering moet eveneens worden doorgevoerd in object storage buckets (geüploade bestanden), zoekindexen, server-caches, audit logs en bij externe partners (subverwerkers). Back-ups mogen data vasthouden tot het einde van hun gedocumenteerde retentiecyclus.

### Waarom is anonimiseren vaak beter dan data wissen?

Omdat het vervangen van identificeerbare gegevens door anonieme placeholders je historische omzetstatistieken en referentiële data-integriteit intact houdt. Echte geanonimiseerde data is juridisch geen persoonsgegeven meer en voldoet daarmee volledig aan de eisen van de AVG.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet een verwijderknop direct het databaserecord wissen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Gebruikers bedoelen meestal verbergen. Hanteer een deleted_at timestamp, filter centraal via policies en wis pas definitief na een hersteltermijn."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom ik dat verwijderde records per ongeluk opduiken in rapportages?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dwing de uitsluiting centraal af via database Row-Level Security policies of views, zodat alle huidige en toekomstige query's dit automatisch overnemen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat gebeurt er als de fiscale bewaarplicht botst met een AVG-verwijderverzoek?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Wettelijk verplichte administratie blijft bewaard, overige persoonsgegevens worden gewist. Dit vereist dat beide datastromen gescheiden worden opgeslagen."
      }
    },
    {
      "@type": "Question",
      "name": "Betekent een AVG-verwijderverzoek louter het wissen van database-rijen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, het moet ook bestanden in cloudopslag, zoekindexen, caches en logs bereiken. Back-ups vallen onder een vooraf gedocumenteerde retentieperiode."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom is anonimiseren vaak beter dan data wissen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het overschrijven van persoonsgegevens met anonieme waarden behoudt data-integriteit en historische totalen, terwijl het juridisch niet langer geldt als persoonsdata."
      }
    }
  ]
}
</script>
