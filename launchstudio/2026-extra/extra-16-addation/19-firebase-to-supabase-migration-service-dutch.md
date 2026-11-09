---
Titel: "Migratieservice van Firebase naar Supabase"
Trefwoorden: firebase naar supabase migratie, firestore naar postgres migreren, firebase auth naar supabase auth, firebase migratieservice, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Migratieservice van Firebase naar Supabase

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Migratieservice van Firebase naar Supabase",
  "description": "Een dienst tegen een vaste prijs die apps gebouwd met Firebase, vaak via AI-tools, migreert naar Supabase. De dienst omvat datamodellering van Firestore-documenten naar PostgreSQL-tabellen, migratie van gebruikers inclusief wachtwoordhashes, opslagbestanden, Security Rules naar Row Level Security, functies, realtime functies en een geplande overstap met terugvalplan, zodat klanten hun accounts en gegevens zonder onderbreking behouden.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-08-14",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/firebase-to-supabase-migration-service" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Migrate from Firebase", "url": "https://supabase.com/docs/guides/platform/migrating-to-supabase/firestore-data" },
    { "@type": "CreativeWork", "name": "Supabase: Migrate Firebase Auth users", "url": "https://supabase.com/docs/guides/platform/migrating-to-supabase/firebase-auth" },
    { "@type": "CreativeWork", "name": "Firebase: Export and import data", "url": "https://firebase.google.com/docs/firestore/manage-data/export-import" },
    { "@type": "CreativeWork", "name": "Supabase: Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" }
  ]
}
</script>

Firebase is een veelgebruikt startpunt voor apps die met AI-tools zijn gebouwd. Het is snel op te zetten, heeft ruime gratis niveaus en veel tutorials. Naarmate producten groeien, willen sommige oprichters overstappen naar Supabase: om een relationele PostgreSQL-database te krijgen voor rapportages en complexe query's, om gegevens te laten hosten in een EU-regio die ze zelf kiezen, om de kosten voorspelbaarder te maken dan facturatie per read of om aan te sluiten bij de AI-builders die standaard Supabase gebruiken, zoals Lovable en Bolt.

Een migratie is meer dan gegevens kopiëren. Firestore slaat geneste documenten op; PostgreSQL slaat gerelateerde tabellen op. Gebruikers van Firebase Authentication moeten hun wachtwoord behouden. Security Rules worden Row Level Security-policies. Cloud Functions worden Edge Functions of databasefuncties. Realtime listeners, opslagpaden en geplande taken hebben allemaal een nieuwe plek nodig. Als het slordig gebeurt, verliezen klanten de toegang, komen gegevens in de verkeerde vorm terecht en is het team maandenlang bezig met randgevallen.

De migratieservice van Firebase naar Supabase van LaunchStudio plant en voert de overstap uit tegen een vaste prijs, met een geteste overstap en een terugvalroute, zodat klanten hun accounts en gegevens behouden.

## Belangrijkste Punten

- **Migreer met een reden:** relationele query's, hosting in de EU, voorspelbare kosten of aansluiting bij tools zijn veelvoorkomende redenen.
- **Datamodellering is het kernwerk:** geneste documenten worden schone, gerelateerde tabellen.
- **Gebruikers behouden hun wachtwoord** als de hashes van Firebase correct worden gemigreerd.
- **Security Rules worden herschreven als Row Level Security,** met tests voor elke tabel.
- **Gebruikelijke prijs: €2.500-€7.500,** meestal binnen Launch & Grow, opgeleverd in twee tot vier weken.

## Signalen Dat een Migratie Zinvol Is

- U heeft rapportages, filters of joins nodig die in Firestore omslachtig of duur zijn.
- Uw Firebase-rekening groeit snel door het aantal documentreads.
- Klanten of partners vragen om gegevens die onder duidelijke voorwaarden in een specifieke EU-regio worden gehost.
- U wilt blijven bouwen met Lovable of Bolt, die native met Supabase werken.
- Uw gegevens zijn inconsistent geworden omdat gerelateerde informatie over documenten heen is gedupliceerd.
- U wilt SQL-toegang voor analyses, exports of koppelingen met BI-tools.

Een migratie is niet altijd het juiste antwoord. Als uw app goed werkt, de kosten redelijk zijn en u geen relationele query's nodig heeft, kan op Firebase blijven en verbeteren wat u heeft goedkoper zijn. Na de beoordeling vertellen we u wat van toepassing is.

## Wat de Dienst Omvat

| Gebied | Firebase | Doel in Supabase |
| --- | --- | --- |
| Gegevens | Firestore-collecties en -documenten, subcollecties | PostgreSQL-tabellen met relaties, constraints en indexen |
| Gebruikers | Firebase Authentication met e-mail, wachtwoord, sociale logins | Supabase Auth met gemigreerde gebruikers en wachtwoordhashes |
| Toegangscontrole | Security Rules van Firestore en Storage | Row Level Security-policies en storagepolicies |
| Bestanden | Cloud Storage for Firebase | Supabase Storage met privébuckets en signed URL's |
| Backendlogica | Cloud Functions, triggers | Edge Functions, databasefuncties en triggers |
| Realtime | Firestore-listeners | Supabase Realtime waar nodig |
| Geplande taken | Geplande functies | Cron-taken in de database of geplande Edge Functions |
| Frontend | Aanroepen via de Firebase SDK | Aanroepen via de Supabase-client |
| Integraties | Webhooks, betaal- en e-mailproviders | Opnieuw gekoppeld aan nieuwe endpoints |

## Hoe het Werk Wordt Gedaan

1. **Kennismakingsgesprek** om uw redenen voor de migratie, uw app en uw planning te begrijpen.
2. **Beoordeling** van uw Firestore-structuur, regels, functies, opslag en frontendcode, afgesloten met een migratieplan en een vaste offerte.
3. **Ontwerp van het datamodel** dat documenten en subcollecties aan tabellen koppelt, in een document dat u goedkeurt voordat er code verandert.
4. **Inrichting van het Supabase-project** in de EU-regio van uw keuze, met schema, constraints, indexen en Row Level Security-policies.
5. **Migratiescripts** die gegevens omzetten en laden, herhaaldelijk gedraaid op kopieën tot de resultaten kloppen.
6. **Migratie van gebruikers** inclusief wachtwoordhashes, zodat gebruikers met hun bestaande wachtwoord kunnen inloggen.
7. **Codewijzigingen** die aanroepen via de Firebase SDK vervangen door aanroepen naar Supabase, met een ongewijzigde interface.
8. **Testen** van elke belangrijke route op staging met gemigreerde gegevens en meerdere gebruikersrollen.
9. **Overstap** in een gepland tijdvak, met een laatste synchronisatie van gegevens, een configuratiewissel en een terugvalplan.
10. **Nazorg** met monitoring, een controle van supportverzoeken en een korte overdracht.

## Wat U Ontvangt

- Een Supabase-project in uw account met schema, policies, functies en opslag
- Migratiescripts en een vastlegging van de omzetting van gegevens
- Gemigreerde gebruikers die hun wachtwoord en sociale logins behouden
- Bijgewerkte frontendcode die compatibel is met uw AI-tool
- Tests voor Row Level Security-policies en belangrijke routes
- Een overstapplan, samen met u uitgevoerd, en een terugvalplan
- Documentatie van het nieuwe datamodel en projectinstructies voor uw AI-tool
- Ondersteuning na de overstap

## De Lastigste Onderdelen van een Firebase-Migratie

| Uitdaging | Waarom het lastig is | Hoe we het aanpakken |
| --- | --- | --- |
| Geneste en gedenormaliseerde gegevens | Dezelfde gegevens staan in meerdere documenten, soms inconsistent | Een genormaliseerd model ontwerpen, conflicten met u oplossen, een rapport bijhouden van wat er veranderde |
| Ontbrekende of inconsistente velden | Firestore dwingt geen schema af | Elke collectie analyseren, standaardwaarden en validatieregels vastleggen |
| Document-ID's gebruikt in URL's en links | Oude links moeten blijven werken | ID's bewaren als kolommen of ze koppelen |
| Wachtwoordhashes | Firebase gebruikt een aangepaste scrypt met projectspecifieke parameters | Hashes migreren met de juiste parameters, logins testen vóór de overstap |
| Logica in Security Rules | Regels mengen authenticatie, gegevensvalidatie en bedrijfslogica | Vertalen naar Row Level Security, constraints en functies met tests |
| Overal realtime listeners | Door AI gegenereerde code luistert vaak naar hele collecties | Realtime alleen gebruiken waar nodig, de rest vervangen door query's |
| Live gegevens tijdens de migratie | Gebruikers blijven gegevens aanmaken terwijl u migreert | Laatste synchronisatie in een kort overstapvenster, of een met u afgesproken periode waarin alleen lezen mogelijk is |

## Waarom Firebase-Apps Gebouwd met AI een Zorgvuldige Migratie Nodig Hebben

AI-tools die Firebase-code genereren, slaan gegevens meestal op in de vorm van het scherm dat wordt gebouwd. Een projectpagina wordt een document met een array van taken, elk met een geneste array van reacties en kopieën van de naam en avatar van de gebruiker. Dat werkt om één project te tonen, maar het maakt rapportages over projecten heen, taken per gebruiker tellen of de naam van een gebruiker wijzigen lastig. Tijdens de migratie moeten deze structuren worden ontward tot tabellen voor projecten, taken, reacties en gebruikers, en moeten de dubbelingen worden afgestemd.

Security Rules die door AI-tools zijn gegenereerd, zijn vaak zeer ruim, zodat elke ingelogde gebruiker kan lezen en schrijven, of na veel iteraties complex en inconsistent. Ze letterlijk vertalen zou de problemen meenemen naar Supabase. We gebruiken de migratie als kans om het toegangsmodel goed vast te leggen en het af te dwingen met geteste Row Level Security-policies.

## Wat We van U Nodig Hebben

- Een kennismakingsgesprek van 15 minuten en een korte beschrijving van waarom u wilt migreren
- Toegang tot uw Firebase-project, repository en hosting
- Een Supabase-account, of toestemming om een project aan te maken dat uw eigendom wordt
- Beslissingen over vragen rond het datamodel, zoals hoe dubbele of tegenstrijdige gegevens worden opgelost
- Overeenstemming over een overstapvenster, meestal buiten de piekuren
- Tijd om belangrijke routes op staging te testen vóór de overstap

## Prijs en Doorlooptijd

| Scope | Gebruikelijke app | Indicatieve prijs | Duur |
| --- | --- | --- | --- |
| Kleine app | Enkele collecties, inloggen met e-mail, weinig opslag, weinig functies | €2.500-€3.500 | 2 weken |
| Standaard SaaS | Organisaties, rollen, opslag, functies, betalingen | €3.500-€5.500 | 2-3 weken |
| Complexe app | Veel collecties, realtime functies, integraties, grote hoeveelheden gegevens | €5.500-€7.500 | 3-4 weken |

Migraties worden meestal opgeleverd binnen Launch & Grow, inclusief doorlopende ondersteuning voor €49 per maand na de overstap. Kleinere migraties passen soms binnen Launch Ready. De offerte staat vast na de beoordeling. Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een indicatie.

## Niet Inbegrepen

De migratie houdt de functies en interface van uw app gelijk. Nieuwe functies, herontwerpen en wijzigingen in uw prijsmodel worden apart afgebakend. De hostingkosten voor Supabase worden door Supabase aan u gefactureerd. We migreren geen analytics, Crashlytics of andere Firebase-diensten die u misschien blijft gebruiken; veel oprichters houden Firebase voor pushnotificaties of analytics terwijl ze gegevens en authenticatie naar Supabase verplaatsen.

## De Overstap Plannen

De overstap is het moment waarop gebruikers Supabase gaan gebruiken in plaats van Firebase. We plannen die zo dat hij kort, omkeerbaar en saai is. Vóór de overstap zijn de migratiescripts vele keren op kopieën gedraaid en is elke belangrijke route getest met gemigreerde gegevens. Op de dag zelf pauzeren we het schrijven of zetten we de app voor een kort venster in onderhoudsmodus, draaien we een laatste synchronisatie van de gegevens die sinds de laatste kopie zijn gewijzigd, zetten we de nieuwe versie live en testen we logins en belangrijke acties met echte accounts.

Als er iets onverwachts opduikt, zet het terugvalplan de vorige versie terug, die naar Firebase wijst en niet is aangepast. Zodra de nieuwe versie een afgesproken periode stabiel is, meestal een week of twee, kan het Firebase-project worden gearchiveerd. We helpen u een laatste back-up te exporteren voordat er iets wordt verwijderd.

## Kosten Vóór en Na

Oprichters migreren vaak deels om de kosten voorspelbaar te maken. Firebase factureert per gelezen, geschreven en verwijderd document, dus een app die naar grote collecties luistert of vaak gegevens herlaadt, kan verrassende rekeningen opleveren. Supabase factureert vooral op abonnement, rekenkracht, opslag en bandbreedte, zodat de kosten meer de capaciteit volgen dan individuele reads. Of u geld bespaart, hangt af van uw gebruik; voor apps met veel reads kan het verschil aanzienlijk zijn. We nemen een schatting van uw verwachte Supabase-kosten op in de beoordeling, zodat de beslissing is gebaseerd op cijfers en niet op aannames.

## Uw AI-Tool Productief Houden na de Migratie

Veel oprichters zijn bang dat de overstap naar Supabase hun werkwijze met Cursor, Claude Code of een andere AI-tool verstoort. In de praktijk wordt het meestal makkelijker. We voegen een bestand met projectinstructies toe dat het nieuwe datamodel, de tabellen, de aanpak voor Row Level Security en de afspraken voor query's beschrijft, zodat de tool code genereert die past. Oprichters die in Lovable of Bolt willen doorgaan, kunnen het gemigreerde Supabase-project koppelen, omdat beide er native mee werken.

We laten ook een kleine set voorbeeldquery's achter en een korte handleiding voor veelvoorkomende wijzigingen, zoals een kolom toevoegen, een nieuwe tabel met een policy aanmaken of een rapportagequery schrijven. Zo maakt de eerste nieuwe functie na de migratie de structuur die de migratie heeft opgeleverd niet ongedaan.

## Waarom Oprichters voor LaunchStudio Kiezen

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, 160+ opgeleverde projecten en 120+ engineers, inclusief datamigraties voor klanten zoals Vodafone en TNO waar het verliezen van records geen optie was. Oprichters ontmoeten het team aan de Herengracht 420 in Amsterdam; de engineering gebeurt in het ontwikkelcentrum van Manifera aan de Pho Quang Street in Ho Chi Minh City, met een hub aan de Tras Street in Singapore. We werken in uw accounts, plannen elke overstap met een terugvalplan en laten de code compatibel met de AI-tools die u al gebruikt.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Coachingapp met Twaalf Kopieën van Elke Naam

Femke Smit leidt een netwerk van zelfstandige hardloopcoaches vanuit Nijmegen en bouwde Looplijn met Cursor en Firebase. Coaches maken trainingsschema's, atleten leggen hun loopjes vast en beiden zien voortgangsgrafieken. Na twee jaar en zo'n 3.000 atleten wilde Femke maandelijkse rapportages per coach, een export voor een sportwetenschappelijke partner en gegevens die onder duidelijke voorwaarden in een EU-regio worden gehost. De Firebase-rekening was bovendien in zes maanden verdrievoudigd.

De beoordeling vond schema's die waren opgeslagen als documenten met geneste weken, trainingen en reacties, waarbij elke reactie een kopie van de naam en foto-URL van de auteur bevatte. Namen van atleten stonden op wel twaalf plekken. De voortgangsgrafiek luisterde in realtime naar de volledige loopgeschiedenis van een atleet, wat het grootste deel van de reads verklaarde. De Security Rules lieten elke coach de gegevens van elke atleet lezen.

LaunchStudio ontwierp een relationeel model met tabellen voor coaches, atleten, schema's, trainingen, loopjes en reacties, loste met goedkeuring van Femke meer dan 400 inconsistente kopieën van namen en e-mailadressen op en maakte Row Level Security-policies zodat coaches alleen hun eigen atleten zagen. Gebruikers werden gemigreerd met hun wachtwoordhashes, en een test met 50 echte accounts bevestigde vóór de overstap dat inloggen werkte. De voortgangsgrafiek werd omgezet naar een query met een samenvattende view, en realtime bleef alleen bestaan voor nieuwe reacties. De overstap duurde 40 minuten op een zondagavond.

**Resultaat:** Geen enkele atleet hoefde zijn wachtwoord opnieuw in te stellen. Maandelijkse rapportages per coach werden één query, de export voor de onderzoekspartner kostte een dag in plaats van weken en de maandelijkse databasekosten van Femke daalden tot ongeveer een derde van de laatste Firebase-rekening.

> *"Ik verwachtte een pijnlijk weekend en een stroom supportmails. We kregen drie vragen, allemaal over de nieuwe rapportageknop."*
> - **Femke Smit, Oprichter, Looplijn (Nijmegen)**

**Kosten & Doorlooptijd:** €5.200 (Launch & Grow-pakket: ontwerp van het datamodel, migratie van gegevens en gebruikers, Row Level Security, opslag, functies, overstap en nazorg, plus €49 per maand) - afgerond in 15 werkdagen.

## Veelgestelde Vragen

### Wat kost een migratie van Firebase naar Supabase?

De meeste migraties kosten tussen €2.500 en €7.500, afhankelijk van het aantal collecties, de complexiteit van de gegevens, functies, opslag, realtime functies en integraties. Ze worden meestal opgeleverd binnen Launch & Grow. U ontvangt een vaste offerte na een beoordeling.

### Moeten mijn gebruikers hun wachtwoord opnieuw instellen?

Nee, in bijna alle gevallen niet. Wachtwoordhashes van Firebase kunnen met de juiste parameters naar Supabase worden gemigreerd, zodat gebruikers met hun bestaande wachtwoord inloggen. Sociale logins worden opnieuw gekoppeld met dezelfde providers. We testen logins met echte accounts vóór de overstap.

### Hoe lang is mijn app onbereikbaar tijdens de migratie?

Meestal minder dan een uur, in een venster dat u kiest. Het meeste werk gebeurt parallel, terwijl uw app op Firebase blijft draaien. De overstap zelf is een laatste synchronisatie van gegevens en een configuratiewissel, met een terugvalplan als er iets onverwachts opduikt.

### Hoe helpt de ervaring van Manifera bij migraties?

Manifera levert al 11+ jaar software over 160+ projecten, inclusief datamigraties voor organisaties waar elk record telde. LaunchStudio past die discipline toe op Firebase-migraties: herhaalde testruns, afstemmingsrapporten en geplande overstappen.

### Heeft migreren invloed op mijn SEO of zichtbaarheid in AI?

Niet als het goed wordt gedaan. Openbare URL's, pagina-inhoud en metadata blijven hetzelfde, en oude links blijven werken. Snellere query's kunnen de paginasnelheid verbeteren, en een stabiele overstap voorkomt de fouten en onbereikbaarheid die kunnen beïnvloeden hoe zoekmachines en AI-antwoordmachines uw site zien.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat kost een migratie van Firebase naar Supabase?",
      "acceptedAnswer": { "@type": "Answer", "text": "De meeste migraties kosten tussen €2.500 en €7.500, afhankelijk van het aantal collecties, de complexiteit van de gegevens, functies, opslag, realtime functies en integraties. Ze worden meestal opgeleverd binnen Launch & Grow." }
    },
    {
      "@type": "Question",
      "name": "Moeten mijn gebruikers hun wachtwoord opnieuw instellen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee, in bijna alle gevallen niet. Wachtwoordhashes van Firebase kunnen met de juiste parameters naar Supabase worden gemigreerd, zodat gebruikers met hun bestaande wachtwoord inloggen." }
    },
    {
      "@type": "Question",
      "name": "Hoe lang is mijn app onbereikbaar tijdens de migratie?",
      "acceptedAnswer": { "@type": "Answer", "text": "Meestal minder dan een uur, in een venster dat u kiest. Het meeste werk gebeurt parallel, terwijl uw app op Firebase blijft draaien." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij migraties?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera levert al 11+ jaar software over 160+ projecten, inclusief datamigraties voor organisaties waar elk record telde. LaunchStudio past die discipline toe op Firebase-migraties: herhaalde testruns, afstemmingsrapporten en geplande overstappen." }
    },
    {
      "@type": "Question",
      "name": "Heeft migreren invloed op mijn SEO of zichtbaarheid in AI?",
      "acceptedAnswer": { "@type": "Answer", "text": "Niet als het goed wordt gedaan. Openbare URL's, pagina-inhoud en metadata blijven hetzelfde, en oude links blijven werken." }
    }
  ]
}
</script>
