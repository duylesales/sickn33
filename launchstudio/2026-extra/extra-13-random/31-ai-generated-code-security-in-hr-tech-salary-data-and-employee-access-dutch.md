---
Titel: "Beveiliging van AI-Gegenereerde Code in HR-Tech: Salarisgegevens en Toegangsbeheer"
Trefwoorden: beveiliging ai gegenereerde code, hr tech beveiliging, salarisdata toegang, werknemersdata avg, cursor hr app, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Beveiliging van AI-Gegenereerde Code in HR-Tech: Salarisgegevens en Toegangsbeheer

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Beveiliging van AI-Gegenereerde Code in HR-Tech: Salarisgegevens en Toegangsbeheer",
  "description": "HR-applicaties gebouwd met AI verwerken salarissen, verzuimregistraties, beoordelingsverslagen en arbeidscontracten. Deze beslissingsgids behandelt de essentiële beveiligingskeuzes voor HR-tech oprichters: rolhiërarchieën, managersmachtigingen, verwerking van ziektegegevens, beveiligde loonstroken, auditlogs en geautomatiseerde offboarding.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-31",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-generated-code-security-in-hr-tech-salary-data-and-employee-access" }
}
</script>

In de meeste SaaS-toepassingen is een datalek tussen gebruikers pijnlijk. In HR-software is een datalek tussen collega's een regelrechte ramp. Wanneer de ene werknemer het salaris, de medische verzuimhistorie of de functioneringsnotities van een directe collega kan inzien, is de schade niet abstract; de crisis ontploft de volgende ochtend direct op de werkvloer. Daarom vereist de beveiliging van AI-gegenereerde code in HR-tech uiterste precisie — en schieten de standaardpatronen van AI-codingtools, die louter denken in oppervlakkige rollen als "gebruiker" en "admin", vrijwel altijd ernstig tekort.

Deze gids bespreekt de fundamentele beslissingen die HR-tech oprichters moeten nemen vóórdat echte personeelsgegevens worden ingeladen.

## Beslissing 1: Wat Is Uw Autorisatiemodel?

AI-gegenereerde HR-apps hanteren doorgaans slechts twee of drie basisrollen: werknemer, manager en beheerder. Echte organisaties vereisen veel meer nuance:

- **Werknemer (Medewerker)** — ziet en wijzigt uitsluitend de eigen persoons- en verlofgegevens.
- **Manager (Leidinggevende)** — ziet specifieke data van directe ondergeschikten, en eventueel van indirecte teamleden.
- **HR-medewerker** — ziet de meeste personeelsdossiers, soms met uitsluiting van specifieke directiegegevens.
- **Salarisadministratie (Payroll)** — ziet salarissen, toeslagen en bankrekeningnummers, maar geen vertrouwelijke beoordelingsnotities.
- **Directie / Financieel manager** — ziet geconsolideerde loonkosten, maar niet noodzakelijk individuele medische bijzonderheden.
- **Externe partijen** — een accountant, extern salarisbureau of de arbodienst/bedrijfsarts met een strikt afgebakende, tijdelijke taak.

**De beslissing:** Stel een autorisatiematrix op waarin gebruikersrollen worden gekoppeld aan gegevenscategorieën (NAW, contract, salaris, IBAN, verlofuren, verzuimdata, beoordelingen en documenten). Dwing deze matrix onverbiddelijk af aan de serverzijde — bij voorkeur direct in de database met Row-Level Security (RLS) en afzonderlijke kolommachtigingen. Autorisatie die uitsluitend in de frontend wordt geregeld, is de meest voorkomende kritieke kwetsbaarheid in AI-gebouwde HR-systemen.

## Beslissing 2: Wat Is de Reikwijdte (Scope) van een Leidinggevende?

"Managers zien hun eigen team" verhult een reeks lastige architectuurkeuzes. Wordt het team bepaald door een formele organisatiestructuur (rapportagelijn), een afdeling of een fysieke vestiging? Wat gebeurt er als een werknemer overstapt naar een andere afdeling — verliest de oude manager per direct toegang tot het historische dossier? Mag een manager de salarissen van zijn teamleden inzien, of uitsluitend verlofaanvragen goedkeuren? En kan een manager stiekem data van andere managers inzien?

AI-gegenereerde code implementeert managersrechten vaak simpelweg als "iedereen met de rol manager mag álle personeelsleden opvragen", omdat die databasequery het eenvoudigst te genereren is. **De beslissing:** Definieer de reikwijdte exact en leid deze dynamisch af uit de hiërarchische rapportagelijnen in de database in plaats van met hardcoded rollijsten.

## Beslissing 3: Hoe Worden Ziekte- en Verzuimgegevens Verwerkt?

Ziekteverzuim betreft gezondheidsgegevens en kwalificeert onder de AVG als een bijzondere categorie van persoonsgegevens. In Nederland is het werkgevers wettelijk **verboden** om de aard of oorzaak van de ziekte van een werknemer te registreren; die medische informatie hoort uitsluitend thuis bij de arbodienst of bedrijfsarts. De Autoriteit Persoonsgegevens handhaaft hier strikt op.

AI-gebouwde HR-applicaties bevatten dikwijls een open tekstveld voor "reden van ziekmelding", waarmee werknemers direct worden uitgenodigd om medische diagnoses in te vullen die de werkgever helemaal niet mag bezitten. **De beslissing:** Registreer uitsluitend wat wettelijk is toegestaan (eerste ziektedag, vermoedelijke verzuimduur, werknemer bereikbaar op verpleegadres, eventuele werkaanpassingen), verwijder open medische tekstvelden en scherm verzuimmeldingen strikt af.

## Beslissing 4: Hoe Worden Salarisstroken en Arbeidscontracten Beschermd?

Loonstroken en getekende arbeidscontracten worden vrijwel altijd opgeslagen als PDF-bestanden. In AI-prototypes belanden deze bestanden geregeld in een openbare cloud storage bucket met voorspelbare bestandsnamen — zoals `loonstrook_2027_10_medewerker_42.pdf`. Iedereen die het patroon herkent, kan met een eenvoudig scriptje de loonstroken van al zijn collega's downloaden.

**De beslissing:** Private bestandsopslag, cryptografisch gegenereerde willekeurige ID's (UUID's), tijdelijk ondertekende URL's (signed URLs) die na enkele minuten verlopen, en server-side autorisatie per individueel document. Overweeg documentversleuteling (encryption at rest) met unieke encryptiesleutels per organisatie.

## Beslissing 5: Wat Wordt Gelogd in de Audit Trail?

In personeelszaken is de vraag wie welke data heeft *ingezien* net zo cruciaal als wie welke data heeft *aangepast*. Wanneer een werknemer vermoedt dat een nieuwsgierige leidinggevende of HR-collega stiekem in zijn privédossier heeft gesnuffeld, moet de organisatie dit direct kunnen verifiëren.

**De beslissing:** Een onweerlegbare audit trail die niet alleen bewerkingen registreert, maar tevens elke leesactie (read-event) op gevoelige categorieën zoals salarissen, verzuimhistorie en beoordelingsgesprekken logt. Deze logs worden opgeslagen in een beveiligde, onveranderlijke (append-only) omgeving.

## Beslissing 6: Wat Gebeurt Er bij Uitdiensttreding (Offboarding)?

Wanneer een werknemer vertrekt, moet diens accounttoegang direct worden afgesloten. Vervolgens moet data worden bewaard of gewist conform de wettelijke termijnen — fiscale loongegevens moeten minimaal zeven jaar worden bewaard, terwijl sollicitatiebescheiden en reguliere personeelsdossiers doorgaans uiterlijk twee jaar na uitdiensttreding moeten worden vernietigd. Wanneer een leidinggevende vertrekt, moet diens toegang tot dossiers van voormalige teamleden onmiddellijk vervallen.

**De beslissing:** Automatiseer de deactivatie van accounts gekoppeld aan de einddatum van het contract en richt geautomatiseerde retentieprocedures in per gegevenscategorie.

## Beslissing 7: Multi-Tenant Scheiding Tussen Bedrijven

Levert uw HR-applicatie diensten aan meerdere werkgevers (B2B SaaS), dan vormt tenant-isolatie de allerbelangrijkste verdedigingslinie. Een programmeerfout waardoor Bedrijf A de salarissen van Bedrijf B kan inzien, betekent direct het einde van uw onderneming. **De beslissing:** Dwing tenant-scheiding af op het diepste niveau van de database (PostgreSQL Row-Level Security), valideer dit continu via geautomatiseerde tests en behandel elke cross-tenant datalekquery als een absolute noodsituatie.

## Een Pragmatische Autorisatiematrix voor HR-Tech

Beveiliging van personeelsdata begint met het uittekenen van een heldere matrix waarin exact staat wie welke bevoegdheden heeft:

| Gegevenscategorie | Werknemer (Zelf) | Manager (Eigen team) | HR-beheerder | Salarisadministratie | Externe accountant |
| --- | --- | --- | --- | --- | --- |
| Persoonsgegevens | Inzien, deels bewerken | Alleen naam en contact | Inzien, bewerken | Inzien | — |
| Contract & Salaris | Alleen eigen inzien | — (afhankelijk van beleid) | Inzien, bewerken | Inzien | Geconsolideerd inzien |
| Bankgegevens (IBAN) | Eigen bewerken | — | Inzien | Inzien | — |
| Verlofsaldi | Eigen inzien | Inzien, goedkeuren | Inzien, bewerken | Inzien | — |
| Ziekteverzuim | Eigen melden | Alleen data & werkhervatting | Inzien, beheren | — | — |
| Beoordelingsverslagen | Eigen definitieve inzien | Schrijven, team inzien | Alles inzien | — | — |
| Documenten (PDF's) | Eigen inzien | — | Uploaden, inzien | Uploaden | — |

Elke cel vertaalt zich direct naar een beveiligingspolicy in PostgreSQL of een check in een serverless API-functie. Elk streepje ("—") vormt een geautomatiseerde unottest die moet falen wanneer ongeoorloofde toegang wordt beproefd.

## Hoe LaunchStudio Helpt

LaunchStudio vertaalt deze autorisatiematrix naar een waterdichte technische infrastructuur met behoud van de frontend die uw gebruikers al kennen: PostgreSQL Row-Level Security gekoppeld aan dynamische rapportagelijnen, verplaatsing van salaris- en bankdata naar beveiligde subtabellen, sanering van verzuimformulieren conform AP-richtlijnen, private documentopslag met signed URL's, geautomatiseerde auditlogging voor leesacties en continue security regressietests in uw CI/CD-pijplijn.

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met meer dan 11 jaar ervaring onder leiding van CEO Herre Roelevink, medeoprichter van CyberDevOps (thans CFLW Cyber Strategies). Onze ervaren software-engineers voeren de backend-beveiliging uit vanuit Ho Chi Minhstad, ondersteund door onze vestiging aan de Herengracht 420 in Amsterdam. Lees meer over onze achtergrond op de [over ons-pagina van Manifera](https://www.manifera.com/about-us/) en raadpleeg de richtlijnen van de [Autoriteit Persoonsgegevens over zieke werknemers](https://autoriteitpersoonsgegevens.nl/) voor de actuele wetgeving.

Staan er al werknemersgegevens in uw ontwikkelomgeving? [Plan deze week nog een vertrouwelijk adviesgesprek met onze engineers](https://launchstudio.eu/nl/#contact).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Verlofportaal Waar Elke Manager Elk Salaris Kon Inzien

Laura Timmermans, zelfstandig HR-adviseur in Ede, ontwikkelde Verlofbord met behulp van Cursor: een overzichtelijk personeelsportaal voor het mkb om verlofaanvragen, ziekmeldingen en de verspreiding van loonstroken digitaal te stroomlijnen, inclusief managersaccordering. Veertien bedrijven met in totaal 850 medewerkers maakten dagelijks gebruik van de applicatie.

De bom barstte toen een teamleider bij een aangesloten logistiek bedrijf terloops een opmerking maakte over het salaris van een collega van een heel andere afdeling. Laura schakelde LaunchStudio in voor een spoed-audit. Daaruit bleek dat elke gebruiker met de rol 'manager' via de API personeelsdossiers van het gehele bedrijf kon opvragen, inclusief bruto maandsalarissen en IBAN-nummers, omdat de backend uitsluitend filterde op bedrijfs-ID. Het ziekmeldingsformulier bevatte een open tekstveld voor de "reden van verzuim", waarin medewerkers gedetailleerde medische diagnoses noteerden. Loonstroken stonden in een publiek toegankelijke S3-bucket met voorspelbare bestandsnamen. Er was geen enkel auditlog. Medewerkers die al een halfjaar uit dienst waren beschikten nog over actieve inlogaccounts, en vertrokken leidinggevenden behielden toegang tot dossiers van hun vroegere teamleden.

Binnen tien werkdagen implementeerde het team van LaunchStudio een fijnmazige autorisatiematrix met Row-Level Security, leidde het managersbereik dynamisch af uit de interne hiërarchie en splitste salaris- en bankgegevens af naar een hermetisch gesloten tabel die enkel toegankelijk was voor HR- en salarisrollen. Het open tekstveld voor de verzuimreden werd direct verwijderd en historische medische aantekeningen werden na overleg met de aangesloten directies definitief gewist; het formulier registreert voortaan uitsluitend datums en verwachte werkhervatting. Loonstroken werden verplaatst naar private opslag met tijdelijke tokens, er werd een auditlog ingericht voor inzage in personeelsdossiers, deactivatie werd gekoppeld aan de contractuele uitdiensttredingsdatum en er werden geautomatiseerde unittests toegevoegd die bij elke deployment ongeoorloofde datatoegang beproeven.

**Resultaat:** Verlofbord informeerde haar zakelijke klanten open en transparant over de doorgevoerde verbeteringen; geen enkele klant vertrok en twee directies prezen de snelle professionaliseringsslag. Het platform groeide vervolgens door naar 23 aangesloten bedrijven, en de geautomatiseerde autorisatietests blokkeerden recent een regressiefout na een latere code-update in Cursor.

> *"Ik bouwde de tool om HR eenvoudiger te maken voor het mkb. Zonder dat ik het wist had ik bijna de oorzaak gecreëerd van de grootste vertrouwenscrisis in de geschiedenis van mijn klanten."*
> — **Laura Timmermans, Oprichter, Verlofbord (Ede)**

**Kosten & Tijdlijn:** €3.100 (Launch Ready-pakket: autorisatiematrix, datamodel-herstructurering, loonstrookbeveiliging, auditlogging en geautomatiseerde access-tests) — afgerond binnen 10 werkdagen.

## Veelgestelde Vragen

### Mogen leidinggevenden de salarissen van hun teamleden inzien in een HR-app?

Dat is een beleidsmatige keuze van de werkgever, maar deze moet expliciet worden vastgelegd en server-side worden afgedwongen. Veel mkb-bedrijven schermen salarisdata strikt af voor uitsluitend de directie en salarisadministratie, en geven managers alleen inzage in uren en verlofsaldi.

### Mag een HR-applicatie registreren waarom een medewerker ziek is?

Nee. In Nederland verbiedt de AVG en de privacywetgeving werkgevers om de medische aard of oorzaak van een ziekte vast te leggen; dit medisch geheim berust uitsluitend bij de bedrijfsarts of arbodienst. Registreer alleen zakelijke gegevens zoals de ziektedatum, verwachte verzuimduur en eventuele overdracht van werkzaamheden.

### Hoe controleer ik of het autorisatiemodel in mijn HR-app werkelijk waterdicht is?

Schrijf geautomatiseerde integratietests die inloggen onder elke afzonderlijke rol en doelbewust verboden acties proberen uit te voeren — zoals een werknemer die het salaris van een collega opvraagt of een manager die data van een ander team leest. Deze tests moeten structureel falen bij ongeoorloofde toegang en draaien bij elke code-release.

### Welke meerwaarde biedt de cybersecurity-ervaring van Manifera voor HR-tech?

Personeelsdossiers combineren financiële, persoonlijke en medische gegevens. De cybersecurity-achtergrond van CEO Herre Roelevink en Manifera's ervaring met enterprise-omgevingen zorgen dat datamodellen, encryptie en audit trails direct voldoen aan de strengste security- en privacy-standaarden.

### Helpt een hoog beveiligingsniveau bij de verkoop van een HR-tool?

Absoluut. Zakelijke HR-beslissers en privacyfunctionarissen voeren grondige security checks uit voordat ze software aanschaffen. Een gedetailleerde beveiligingspagina met een heldere toelichting op RLS, encryptie, datalocaties en audit trails verkort B2B-salestrajecten aanzienlijk en wekt vertrouwen bij AI-zoekmachines.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Mogen leidinggevenden de salarissen van hun teamleden inzien in een HR-app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Dit is een beleidskeuze van de werkgever, maar dient server-side te worden afgedwongen; veel bedrijven beperken salarisinzage tot HR en payroll." }
    },
    {
      "@type": "Question",
      "name": "Mag een HR-applicatie registreren waarom een medewerker ziek is?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. De wet verbiedt werkgevers om diagnoses of medische oorzaken vast te leggen; registreer uitsluitend datums, duur en werkhervatting." }
    },
    {
      "@type": "Question",
      "name": "Hoe controleer ik of het autorisatiemodel in mijn HR-app werkelijk waterdicht is?",
      "acceptedAnswer": { "@type": "Answer", "text": "Door geautomatiseerde negatieve unittests te draaien die per rol verboden data proberen op te vragen, standaard uitgevoerd bij elke deployment." }
    },
    {
      "@type": "Question",
      "name": "Welke meerwaarde biedt de cybersecurity-ervaring van Manifera voor HR-tech?",
      "acceptedAnswer": { "@type": "Answer", "text": "Diepgaande expertise in rolgebaseerde autorisatie (RLS), encryptie en audit trails voor gevoelige medische en financiële personeelsgegevens." }
    },
    {
      "@type": "Question",
      "name": "Helpt een hoog beveiligingsniveau bij de verkoop van een HR-tool?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Heldere documentatie over databeveiliging en AVG-naleving verkort B2B-salestrajecten en versterkt de online autoriteit." }
    }
  ]
}
</script>
