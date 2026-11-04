---
Titel: "Hoe Importeer Ik Mijn Bestaande Klanten in een Lovable-App?"
Trefwoorden: klanten importeren lovable, csv import supabase, klantgegevens migreren ai-app, lovable data import, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Hoe Importeer Ik Mijn Bestaande Klanten in een Lovable-App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Importeer Ik Mijn Bestaande Klanten in een Lovable-App?",
  "description": "Bestaande klanten overzetten vanuit spreadsheets, een oud systeem of een no-codetool naar een Lovable-app is een kleine datamigratie. Deze gids behandelt opschonen, koppelen, accounts zonder wachtwoord aanmaken, gebruikers uitnodigen en het resultaat controleren.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-29",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-do-i-import-my-existing-customers-into-a-lovable-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Import data", "url": "https://supabase.com/docs/guides/database/import-data" },
    { "@type": "CreativeWork", "name": "Supabase: Admin create user", "url": "https://supabase.com/docs/reference/javascript/auth-admin-createuser" },
    { "@type": "CreativeWork", "name": "GDPR Article 5: Principles", "url": "https://gdpr-info.eu/art-5-gdpr/" },
    { "@type": "CreativeWork", "name": "OWASP Secrets Management Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html" }
  ]
}
</script>

**Kort antwoord:** exporteer uw klanten naar CSV, schoon de gegevens op en verwijder dubbelingen, koppel elke kolom aan uw Supabase-tabellen, importeer de records met een script of de tabelimport van Supabase na een proefrun in staging, maak gebruikersaccounts aan via de admin-API van Supabase zonder wachtwoorden in te stellen, en stuur daarna uitnodigingen zodat klanten zelf een wachtwoord kiezen of inloggen met een magic link. Controleer aantallen en een steekproef van records voordat u de overstap aankondigt.

## Belangrijkste Punten

- **Bestaande klanten importeren in een Lovable-app is een kleine datamigratie:** opschonen, koppelen, testen in staging, importeren, accounts aanmaken, uitnodigen en controleren.
- **Plak nooit honderden records in de AI-chat;** gebruik scripts of de importtools van Supabase, met een generale repetitie in staging.
- **Maak accounts aan zonder wachtwoord** via de admin-API van Supabase vanuit code op de server, en laat klanten daarna zelf een wachtwoord kiezen of magic links gebruiken.
- **Informeer klanten over de overstap** en gebruik hun gegevens voor hetzelfde doel; het beginsel van doelbinding uit de AVG geldt.
- **Stem totalen af,** zoals saldi of tegoeden, na de import, niet alleen het aantal rijen.

## Voordat U Importeert

**Controleer uw rechtsgrond.** Bestaande klanten hebben een relatie met u, wat het overzetten van hun gegevens naar een nieuw systeem met hetzelfde doel meestal dekt. Gebruik de import niet om marketingmails te gaan sturen waarvoor ze nooit toestemming hebben gegeven.

**Bepaal wat u meeneemt.** Niet alles in een oude spreadsheet hoort in de nieuwe app. Minder importeren betekent minder te beveiligen en minder op te schonen.

## Stap 1: Schoon de Gegevens Op

| Probleem | Voorbeeld | Oplossing |
| --- | --- | --- |
| Dubbelingen | Dezelfde persoon twee keer met een andere spelling | Ontdubbelen op e-mailadres |
| Inconsistente formaten | Telefoonnummers en datums in verschillende formaten | Normaliseren vóór de import |
| Ontbrekende verplichte velden | Geen e-mailadres bij sommige klanten | Beslissen: overslaan, of importeren als contacten zonder account |
| Problemen met tekencodering | Kapotte tekens in namen zoals "Müller" | Exporteren als UTF-8 |
| Gemengde gegevens in één kolom | "Jan & Petra de Vries" | Zo nodig splitsen in aparte records |

## Stap 2: Koppel Kolommen aan Tabellen

Schrijf een eenvoudige koppeling: welke CSV-kolom naar welke tabel en kolom gaat, en hoe relaties ontstaan (bijvoorbeeld bestellingen die tijdens de import via het e-mailadres aan klanten worden gekoppeld, en daarna via een ID).

## Stap 3: Test in Staging

Importeer eerst in een stagingproject. Log in als een geïmporteerde gebruiker, controleer dat de gegevens goed verschijnen en bevestig dat Row Level Security alleen de eigen records toont. Onze gids over [staging voor Lovable-apps](https://launchstudio.eu/nl/blog/how-do-i-set-up-a-staging-environment-for-a-lovable-app) legt de opzet uit.

## Stap 4: Maak Accounts Aan Zonder Wachtwoord

Gebruik de admin-API van Supabase vanuit een script op de server om auth-gebruikers aan te maken met bevestigde e-mailadressen en zonder wachtwoord, en koppel elk account daarna aan het profiel en de gegevens. Stel nooit wachtwoorden in namens gebruikers, en zet nooit admin-sleutels in de browser.

## Stap 5: Nodig Klanten Uit

Stuur een duidelijke uitnodiging: wie u bent, waarom ze deze ontvangen, wat de nieuwe app doet en een link om een wachtwoord in te stellen of in te loggen met een magic link. Verstuur in batches om de bezorgbaarheid te beschermen, en gebruik uw geauthenticeerde verzenddomein.

## Stap 6: Controleer

- Het aantal rijen komt overeen met de opgeschoonde bron
- Twintig willekeurige records met de hand gecontroleerd
- Totalen zoals openstaande saldi of tegoeden komen overeen
- Uitnodigingen afgeleverd, met de lijst van bounces bekeken

## Veelgemaakte Fouten bij de Uitvoering

- Bij de eerste poging direct in productie importeren
- De chat van Lovable gebruiken om "deze 800 klanten toe te voegen" vanuit geplakte tekst
- Dubbelingen veroorzaken wanneer klanten zich registreren voordat ze de uitnodiging ontvangen
- Vergeten de geschiedenis te importeren die klanten verwachten te zien, zoals eerdere bestellingen of resterende tegoeden

## De Migratie Plannen

Een kort plan voorkomt de meeste importproblemen. Schrijf op:

- **Bronnen:** spreadsheets, oude systemen, exports uit andere tools
- **Entiteiten:** klanten, contactpersonen, bestellingen, abonnementen, tegoeden, bestanden
- **Koppeling:** welke bronvelden waarheen gaan, en welke vervallen
- **Identiteit:** hoe records worden gematcht, meestal op e-mailadres of een extern ID
- **Accounts:** wie een login krijgt, met welke rol
- **Validatie:** welke totalen en aantallen na de import moeten kloppen
- **Communicatie:** wat klanten te horen krijgen, wanneer en van wie

Deze ene pagina wordt de checklist voor elke repetitie en voor de definitieve import.

## Gegevenskwaliteit Vóór de Import

Oude gegevens zijn zelden schoon. Gangbare problemen en hoe u ze aanpakt:

| Probleem | Aanpak |
| --- | --- |
| Dubbele klanten | Ontdubbelen op genormaliseerd e-mailadres; zorgvuldig samenvoegen |
| Ongeldige e-mailadressen | Duidelijke typfouten herstellen, de rest markeren voor handmatige controle |
| Gemengde datumformaten | Normaliseren naar ISO-datums vóór de import |
| Vrije notities met persoonsgegevens | Beslissen of ze nodig zijn; minimaliseren |
| Inactieve of voormalige klanten | Alleen importeren als er een reden is om hun gegevens te bewaren |

De beginselen van dataminimalisatie en opslagbeperking uit de AVG gelden ook voor imports: een migratie is een goed moment om achter te laten wat u niet meer nodig heeft.

## Relaties Behouden

Klanten hebben bestellingen, bestellingen hebben regels, gezinnen hebben kinderen, bedrijven hebben contactpersonen. Importeer eerst de bovenliggende records, houd een tijdelijke koppeling bij tussen oude en nieuwe ID's, en importeer daarna de onderliggende records met die koppeling. Controleer na de import dat elk onderliggend record een bovenliggend record heeft en dat er geen relaties verloren zijn gegaan. Bij complexe structuren is een repetitie in staging met de volledige dataset onmisbaar.

## Accounts op Grote Schaal Aanmaken

Maak gebruikersaccounts aan vanuit een script op de server met de admin-API van Supabase, met bevestigde e-mailadressen en zonder wachtwoorden. Koppel elk account via de profiel- of lidmaatschapstabellen aan de geïmporteerde gegevens en ken de juiste rol toe. Werk in batches met logging, zodat u kunt hervatten als er iets misgaat. Stel de service role key die u hiervoor gebruikt nooit bloot buiten de omgeving van het script, en roteer hem daarna als hij met een externe ontwikkelaar is gedeeld.

## Klanten Uitnodigen

Uw uitnodigingsmail is de eerste indruk van het nieuwe systeem. Maak hem duidelijk en betrouwbaar: uw bedrijfsnaam en logo, waarom ze deze ontvangen, wat de nieuwe app biedt, één knop om een wachtwoord in te stellen of in te loggen, en een contactpersoon voor vragen. Verstuur vanaf uw geauthenticeerde domein in batches om de bezorgbaarheid te beschermen, en stuur na een week één herinnering naar wie nog niets heeft gedaan.

## Oud en Nieuw Naast Elkaar Draaien

Gedurende een korte periode moet u het oude systeem misschien alleen-lezen houden terwijl klanten overstappen. Kondig een einddatum aan, stop wijzigingen in het oude systeem vóór de definitieve import en stuur oude links door naar de nieuwe app. Langer dan nodig parallel draaien leidt tot tegenstrijdige gegevens; houd het kort.

## Het Resultaat Controleren

Controleren gaat verder dan rijen tellen. Vergelijk totalen die voor het bedrijf tellen - openstaande saldi, resterende tegoeden, actieve abonnementen - tussen de bron en de nieuwe app. Vraag twee of drie vertrouwde klanten om vroeg in te loggen en te bevestigen dat hun gegevens kloppen. Los verschillen op voordat de bredere uitnodiging de deur uit gaat.

## Bestanden en Bijlagen Importeren

Klantgegevens bevatten vaak bestanden: contracten, foto's, certificaten, facturen. Plan de migratie daarvan apart. Upload bestanden naar privé-buckets in Supabase Storage met paden die het ID van de organisatie of gebruiker bevatten, werk databaserecords bij met de nieuwe storagepaden en controleer of een steekproef via uw app goed opent met signed URLs. Grote verzamelingen bestanden kunnen uren kosten om over te zetten, dus voer de bestandsmigratie uit vóór de definitieve gegevensimport en synchroniseer daarna alleen wijzigingen.

## Abonnementen en Betaalgegevens

Als klanten actieve abonnementen in een oud systeem hebben, importeer dan zelf geen kaartgegevens; daarmee valt u onder de beveiligingseisen van de kaartindustrie. Vraag in plaats daarvan uw betaalprovider naar migratiemogelijkheden, of vraag klanten om de betaling in de nieuwe app opnieuw in te stellen, bij voorkeur met een duidelijke boodschap en een kleine beloning. Controleer voor SEPA-machtigingen bij uw provider of bestaande machtigingen kunnen worden overgezet.

## Veelgemaakte Fouten in de Planning

- Direct in productie importeren zonder repetitie
- Accounts aanmaken met wachtwoorden die u zelf heeft gekozen
- Uitnodigingen versturen voordat de gegevens zijn gecontroleerd
- Elk historisch record importeren "voor de zekerheid"
- Relaties tussen records verliezen door een ontbrekende koppeling van ID's
- Vergeten de privacyverklaring bij te werken voor het nieuwe systeem

## De Kern

Een zorgvuldige import respecteert de geschiedenis en het vertrouwen van uw klanten. Schoon de gegevens op, repeteer in staging, maak accounts veilig aan, nodig duidelijk uit en controleer wat voor het bedrijf telt. Goed uitgevoerd ervaren klanten de overstap als een verbetering in plaats van een verstoring.

## Tijdlijn van een Gangbare Import

Voor een paar honderd klanten met bestellingen of tegoeden is een realistisch plan twee tot drie dagen voor opschonen en koppelen, een tot twee dagen voor repetities in staging en oplossingen, één dag voor de import in productie, het aanmaken van accounts en controle, en een week voor gespreide uitnodigingen en opvolging. Grotere of rommeligere datasets duren langer, vooral door het opschonen; de import zelf is zelden het trage deel.

## Wie de Import Moet Bezitten

Ook als een ontwikkelaar de scripts draait, hoort de oprichter de beslissingen te nemen: welke records mee gaan, hoe dubbelingen worden opgelost, wat klanten te horen krijgen en welke totalen moeten kloppen. Dat zijn zakelijke beslissingen die het vertrouwen van klanten raken, en geen script kan ze voor u nemen.

## Gerelateerde Onderwerpen

Imports raken verschillende andere onderwerpen: staging inrichten voor repetities, e-mails versturen die echt aankomen en verwijdering regelen voor records die u besluit niet te bewaren. Onze gidsen over elk daarvan behandelen de details.

## De Verandering Communiceren

Vertel klanten vóór de import wat er verandert, wanneer en waarom het hen helpt. Bevestig na de import dat hun account klaarstaat en hoe ze inloggen. Een kort, eerlijk bericht voorkomt verwarring, vermindert supportvragen en zorgt dat het nieuwe systeem als een verbetering voelt in plaats van een verstoring. Vermeld waar hun gegevens nu worden opgeslagen en link naar uw bijgewerkte privacyverklaring.

## Samenvatting

Schoon op voordat u verhuist, repeteer voordat u importeert, maak accounts veilig aan, controleer waar het bedrijf op draait en communiceer duidelijk. Klanten beoordelen de nieuwe app op hoe soepel hun bestaande gegevens aankomen.

## Verder Lezen

Zie voor de stappen rond een import onze gidsen over stagingomgevingen, het inrichten van transactionele e-mail en AVG-conforme verwijdering.

## Het Laten Regelen

LaunchStudio verzorgt klantimports als onderdeel van lanceringen, meestal een paar dagen binnen een Launch Ready-pakket. LaunchStudio wordt ondersteund door Manifera, dat in 11+ jaar gegevens heeft gemigreerd voor enterpriseklanten, vanuit het ontwikkelcentrum in Ho Chi Minh-stad met klantcontact in Amsterdam en Singapore; zie [de maatwerksoftwareontwikkeling van Manifera](https://www.manifera.com/services/custom-software-development/). Supabase documenteert [het importeren van gegevens](https://supabase.com/docs/guides/database/import-data) en [de admin-API voor gebruikers](https://supabase.com/docs/reference/javascript/auth-admin-createuser).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Pianoschool met 17 Jaar aan Spreadsheets

Gerda Hofstra runt een pianoschool in Sneek met negen docenten. Ze bouwde Pianoles in Lovable, zodat leerlingen en ouders lessen konden boeken, hun lestegoed konden zien en online konden betalen. Haar bestaande gegevens bestonden uit 17 jaar aan spreadsheets: 640 huidige en voormalige leerlingen, gezinskoppelingen, vooruitbetaalde lestegoeden en de toewijzing aan docenten.

Haar eerste poging was rijen plakken in de chat van Lovable. Die maakte 212 leerlingen aan voordat hij stopte, met meerdere broers en zussen samengevoegd in één record en tegoeden gekoppeld aan de verkeerde gezinnen. Twee ouders die zich vroeg hadden geregistreerd, hadden nu dubbele accounts.

LaunchStudio schoonde de spreadsheets op en verwijderde dubbelingen, scheidde huidige van voormalige leerlingen (alleen huidige leerlingen kregen een account), koppelde gezinnen, leerlingen en tegoeden aan het schema, draaide de gedeeltelijke import terug, voerde twee testimports in staging uit, maakte accounts aan via de admin-API en verstuurde Nederlandstalige uitnodigingen in drie batches. De totalen van de tegoeden werden afgestemd met de boekhouding van Gerda.

**Resultaat:** 312 huidige leerlingen en hun ouders werden uitgenodigd; 88% activeerde het account binnen twee weken. De saldi van de tegoeden kwamen tot op de euro overeen met de boekhouding.

> *"De app was in een paar weken klaar. Zeventien jaar aan spreadsheets erin overzetten was het deel dat ik volledig had onderschat."*
> - **Gerda Hofstra, Oprichter, Pianoles (Sneek)**

**Kosten & Doorlooptijd:** €1.800 (Launch Ready-pakket: gegevens opschonen, koppelen, imports in staging, accounts aanmaken, uitnodigingen en afstemming) - afgerond in 6 werkdagen.

## Veelgestelde Vragen

### Kan ik een CSV direct in mijn Lovable-app importeren?

U kunt CSV-bestanden via het dashboard of met scripts in Supabase-tabellen importeren. Voor klanten die een account nodig hebben, moet u ook auth-gebruikers aanmaken en aan hun gegevens koppelen, wat het beste met een script op de server gebeurt.

### Moet ik wachtwoorden instellen voor geïmporteerde gebruikers?

Nee. Maak accounts aan zonder wachtwoord en laat klanten er zelf een kiezen via een uitnodiging of magic links gebruiken. Wachtwoorden instellen voor gebruikers is een risico voor de beveiliging en het vertrouwen.

### Is het AVG-conform om bestaande klanten in een nieuwe app te importeren?

Meestal wel, als de nieuwe app hetzelfde doel dient als uw bestaande relatie. Informeer klanten over de verandering, werk uw privacyverklaring bij en gebruik de import niet voor marketing die daar los van staat.

### Hoe beperkt Manifera fouten bij gegevensimports?

Door te repeteren in staging, totalen af te stemmen en steekproeven met de hand te controleren. De 11+ jaar migraties van Manifera laten zien dat de meeste importfouten bij repetities worden gevonden, niet in productie, als het proces zo is ingericht.

### Helpt het importeren van oude content de zichtbaarheid van mijn app?

Openbare content, zoals overzichten of artikelen van een oude site, kan helpen als die met dezelfde URL's of goede redirects wordt overgezet. Klantgegevens zijn privé en mogen nooit zichtbaar zijn voor zoekmachines.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan ik een CSV direct in mijn Lovable-app importeren?",
      "acceptedAnswer": { "@type": "Answer", "text": "In Supabase-tabellen wel; klanten die een account nodig hebben, vragen ook auth-gebruikers die een script op de server aanmaakt en koppelt." }
    },
    {
      "@type": "Question",
      "name": "Moet ik wachtwoorden instellen voor geïmporteerde gebruikers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. Maak accounts zonder wachtwoord en laat klanten zelf een wachtwoord kiezen via een uitnodiging of magic links." }
    },
    {
      "@type": "Question",
      "name": "Is het AVG-conform om bestaande klanten in een nieuwe app te importeren?",
      "acceptedAnswer": { "@type": "Answer", "text": "Meestal, voor hetzelfde doel, met informatie aan klanten, een bijgewerkte privacyverklaring en geen losstaande marketing." }
    },
    {
      "@type": "Question",
      "name": "Hoe beperkt Manifera fouten bij gegevensimports?",
      "acceptedAnswer": { "@type": "Answer", "text": "Met repetities in staging, afgestemde totalen en handmatige steekproeven." }
    },
    {
      "@type": "Question",
      "name": "Helpt het importeren van oude content de zichtbaarheid van mijn app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Openbare content wel, met behouden URL's of redirects; klantgegevens moeten privé blijven." }
    }
  ]
}
</script>
