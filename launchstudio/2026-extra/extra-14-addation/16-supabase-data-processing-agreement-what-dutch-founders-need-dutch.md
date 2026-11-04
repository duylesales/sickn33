---
Titel: "Verwerkersovereenkomst met Supabase: Wat Nederlandse Oprichters Nodig Hebben"
Trefwoorden: verwerkersovereenkomst supabase, supabase dpa, supabase avg, supabase data processing agreement, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Verwerkersovereenkomst met Supabase: Wat Nederlandse Oprichters Nodig Hebben

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Verwerkersovereenkomst met Supabase: Wat Nederlandse Oprichters Nodig Hebben",
  "description": "Als uw Lovable- of Bolt-app persoonsgegevens in Supabase opslaat, heeft u een verwerkersovereenkomst met Supabase nodig. Deze gids legt uit waarom, hoe u die regelt, wat u moet controleren rond regio's en subverwerkers, en wat de overeenkomst niet dekt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-24",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/supabase-data-processing-agreement-what-dutch-founders-need" },
  "citation": [
    { "@type": "CreativeWork", "name": "GDPR Article 28: Processor", "url": "https://gdpr-info.eu/art-28-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 32: Security of processing", "url": "https://gdpr-info.eu/art-32-gdpr/" },
    { "@type": "CreativeWork", "name": "Supabase Security", "url": "https://supabase.com/security" },
    { "@type": "CreativeWork", "name": "European Commission: EU-US data transfers", "url": "https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/eu-us-data-transfers_en" },
    { "@type": "CreativeWork", "name": "Supabase: Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" }
  ]
}
</script>

De privacyfunctionaris van uw klant stelt een korte vraag: "Heeft u een verwerkersovereenkomst met uw databaseprovider?" Als uw app is gebouwd met Lovable, Bolt of een vergelijkbare tool, is die provider waarschijnlijk Supabase, en het eerlijke antwoord van veel oprichters is "dat weet ik niet". Dit artikel legt uit wat een verwerkersovereenkomst met Supabase is, hoe u die regelt en wat u tegelijk nog meer moet controleren.

## Belangrijkste Punten

- **Supabase is uw verwerker** wanneer het persoonsgegevens van uw gebruikers opslaat, dus vereist artikel 28 van de AVG een verwerkersovereenkomst met Supabase.
- **In B2B is Supabase uw subverwerker,** en uw zakelijke klanten willen zien dat de keten is afgedekt.
- **De overeenkomst is nodig, maar niet voldoende.** Regio, toegangspolicies, opslaginstellingen, logs en het eigendom van het account bepalen of uw opzet overeenkomt met de overeenkomst.
- **De regio is de keuze met de meeste impact.** Een project in een Amerikaanse regio blijft daar; verhuizen naar een EU-regio zoals Frankfurt betekent een geplande migratie.
- **LaunchStudio doet het technische werk** - migratie naar de EU, eigendom, RLS, bewaartermijnen en documentatie - doorgaans voor €1.500-€4.500.

## Waarom U Er Een Nodig Heeft

Onder de AVG moet u, wanneer een ander bedrijf namens u persoonsgegevens verwerkt, een schriftelijke overeenkomst met dat bedrijf hebben: een verwerkersovereenkomst. Supabase slaat de namen, e-mailadressen, (gehashte) wachtwoorden en bestanden van uw gebruikers op, en alles wat uw app verder bewaart. Daarmee is Supabase uw verwerker, en is de overeenkomst een wettelijke plicht, geen formaliteit.

Als u een B2B-app heeft, is de keten langer. Uw zakelijke klant is de verwerkingsverantwoordelijke, u bent hun verwerker en Supabase is uw subverwerker. Uw klant wil weten dat deze schakel is afgedekt.

## Hoe U Het Regelt

Supabase biedt zijn klanten een standaard verwerkersovereenkomst (DPA). Het precieze proces kan veranderen, dus kijk op de juridische en privacypagina's van Supabase of in de instellingen van uw organisatie voor de actuele route. In het algemeen:

1. Zorg dat de Supabase-organisatie op naam van uw bedrijf staat, niet op een persoonlijk account of dat van een voormalige freelancer.
2. Vraag de DPA aan of teken hem via de route die Supabase op dat moment biedt.
3. Bewaar de getekende kopie bij uw andere privacydocumenten.
4. Neem Supabase op in uw verwerkingsregister en uw lijst van subverwerkers.

Doe dit voor elke Supabase-organisatie die u gebruikt. Oprichters hebben soms één organisatie voor productie en een andere, vergeten organisatie met een kopie van echte data die voor testen werd gebruikt.

## Wat U Naast de Overeenkomst Controleert

De overeenkomst regelt de juridische relatie. Deze praktische punten bepalen of uw opzet er werkelijk mee overeenkomt:

| Controle | Waarom het belangrijk is | Waar u kijkt |
| --- | --- | --- |
| Projectregio | Bepaalt waar data wordt opgeslagen | Projectinstellingen |
| Subverwerkers | Supabase gebruikt cloudinfrastructuurproviders | De gepubliceerde lijst van subverwerkers van Supabase |
| Doorgiftemechanisme | Supabase is een bedrijf met hoofdkantoor in de VS | Voorwaarden van de DPA, status onder het Data Privacy Framework, standaardcontractbepalingen |
| Back-ups | Locatie en bewaartermijn van back-updata | Project- en abonnementsinstellingen |
| Storage buckets | Bestanden zijn ook persoonsgegevens | Opslaginstellingen, privacy van buckets |
| Logs | Logs kunnen e-mails, IP-adressen en queryparameters bevatten | Loginstellingen en bewaartermijn |
| Eigendom van het account | Alleen u hoort de organisatie te beheren | Leden van de organisatie |

De keuze met de meeste impact is de **regio**. Een project dat in een Amerikaanse regio is aangemaakt, houdt zijn data daar. Verhuizen naar een EU-regio zoals Frankfurt betekent een nieuw project aanmaken en data migreren; dat is een geplande klus, maar voor Nederlandse klanten zeker de moeite waard.

## Wat de Overeenkomst Niet voor U Doet

Een getekende overeenkomst maakt uw app op zichzelf niet compliant. Ze:

- Beschermt geen data die uw Row Level Security-policies aan de verkeerde gebruikers tonen
- Verwijdert geen data waarvoor u nooit een verwijderfunctie heeft gebouwd
- Dekt niet de andere diensten waarnaar uw app data stuurt, zoals e-mail, analytics of AI-API's
- Vervangt niet uw eigen privacyverklaring, verwerkingsregister of verwerkersovereenkomsten met uw klanten

Zie de verwerkersovereenkomst met Supabase als één regel in een langere lijst. Onze [AVG-checklist voor SaaS-oprichters](https://launchstudio.eu/nl/blog/gdpr-checklist-for-saas-founders-in-the-netherlands) behandelt de rest.

## Een Gangbare Privacy-Inrichting in Supabase voor een Nederlandse App

1. Supabase-organisatie in eigendom van het bedrijf, met tweestapsverificatie voor alle leden
2. Productieproject in een EU-regio, apart stagingproject zonder echte persoonsgegevens
3. Verwerkersovereenkomst getekend en bewaard
4. Volledige Row Level Security, privé storage buckets, servicesleutels alleen op de server
5. Bewaartaken voor data die u niet meer nodig heeft
6. Accountverwijdering die ook bestanden en gerelateerde records verwijdert
7. Supabase opgenomen in het verwerkingsregister en in de lijst van subverwerkers die met klanten wordt gedeeld

## De Verwerkersketen Uitgelegd

Verwerkingsrelaties vormen een keten, en elke schakel heeft een eigen overeenkomst nodig:

| Schakel | Rollen | Overeenkomst |
| --- | --- | --- |
| Uw zakelijke klant → u | Verwerkingsverantwoordelijke → verwerker | Uw verwerkersovereenkomst met de klant |
| U → Supabase | Verwerker → subverwerker (of verantwoordelijke → verwerker voor uw eigen gebruikers) | De DPA van Supabase |
| Supabase → zijn infrastructuurproviders | Subverwerker → verdere subverwerkers | Gedekt in de DPA van Supabase en de gepubliceerde lijst |

Uw klant vraagt u te bevestigen dat elke schakel is afgedekt en dat subverwerkers gelijkwaardige garanties bieden als u. Met de DPA van Supabase en de gepubliceerde lijst van subverwerkers in uw dossier kunt u dat in één e-mail beantwoorden.

## Doorgiften en een Hoofdkantoor in de VS

Supabase heeft zijn hoofdkantoor in de VS. Zelfs met een project in een EU-regio kunnen klanten naar doorgiften vragen. Het standaardantwoord combineert drie feiten: de data is opgeslagen in een EU-regio, de DPA van de provider bevat de waarborgen voor doorgifte waarop die steunt (zoals standaardcontractbepalingen of certificering onder het Data Privacy Framework, voor zover van toepassing), en de toegang tot productiedata is beperkt. De richtlijnen van de Europese Commissie over doorgiften tussen de EU en de VS beschrijven de mechanismen. Controleer de actuele juridische documentatie van Supabase voor de precieze waarborgen voordat u ze citeert.

## Toegangscontrole als Onderdeel van de Overeenkomst

Een verwerkersovereenkomst belooft passende beveiliging, en artikel 32 van de AVG legt uit wat dat betekent: maatregelen die passen bij het risico, waaronder vertrouwelijkheid, integriteit en het vermogen om data te herstellen. In een Supabase-project worden die beloften waargemaakt of gebroken door Row Level Security, storage policies en het beheer van sleutels. Een verwerkersovereenkomst bovenop een tabel met uitgeschakelde RLS biedt weinig echte bescherming. Daarom horen de technische controles in dit artikel naast het juridische papierwerk.

## Logs, Back-ups en Bewaartermijnen

Drie vaak vergeten plekken bevatten persoonsgegevens in Supabase-projecten:

- **Logs** kunnen e-mailadressen, IP-adressen en queryparameters bevatten. Ken de bewaartermijn en vermijd onnodige logging van persoonsgegevens in uw eigen functies.
- **Back-ups** bevatten alles in de database. Documenteer hun bewaartermijn, zodat u verwijderverzoeken juist kunt beantwoorden.
- **Authenticatietabellen** bevatten e-mails en metadata van elke gebruiker, ook van wie de onboarding nooit afrondde. Neem ze op in uw bewaarregels.

## Een Privacyreview van Supabase in Eén Uur

Als u uw eigen project snel wilt beoordelen:

1. Bevestig dat de organisatie eigendom is van het bedrijf en dat elk lid tweestapsverificatie heeft.
2. Noteer de regio van elk project en of een project buiten productie echte persoonsgegevens bevat.
3. Controleer of RLS is ingeschakeld op elke tabel in blootgestelde schema's.
4. Maak een lijst van storage buckets en bevestig welke openbaar zijn en waarom.
5. Zoek in uw frontendbundel naar geheime sleutels.
6. Bevestig dat de verwerkersovereenkomst is getekend en bewaard.
7. Schrijf de bewaartermijnen van back-ups en logs op.

Alles wat u in dat uur niet kunt bevestigen, is een taak voor uw volgende sprint of voor een specialist.

## Wanneer een Klant om Bewijs Vraagt

Zakelijke klanten vragen steeds vaker om bewijs in plaats van geruststelling. Bereid voor het Supabase-deel van uw stack een kleine bewijsmap voor: de getekende verwerkersovereenkomst, een screenshot of export van de regio van elk project, de actuele lijst van subverwerkers van Supabase, een korte beschrijving van uw Row Level Security-model, uw instellingen voor back-ups en bewaartermijnen, en een lijst van wie toegang heeft tot de Supabase-organisatie. Werk die elk kwartaal bij. Wanneer een privacyfunctionaris een vervolgvraag stelt, antwoordt u in minuten met documenten in plaats van in dagen met e-mails, en dat is vaak het verschil tussen een soepele en een vastgelopen inkoop.

## Een Regiomigratie Plannen

Als uw project in een regio buiten de EU staat, plan de verhuizing dan in plaats van die uit te stellen. Een gangbare migratie duurt dagen, geen weken: maak het EU-project aan, voer de migraties uit, kopieer data en bestanden, migreer de authenticatie zorgvuldig, werk redirect-URL's en webhooks bij en schakel over tijdens een kort onderhoudsvenster. Oefen het één keer op staging. Oprichters die uitstellen, migreren meestal onder druk, midden in het inkoopproces van een klant, en dat is het slechtste moment voor verrassingen.

## Overeenkomsten en Werkelijkheid op Één Lijn Houden

Het meest voorkomende gat dat we vinden, is geen ontbrekende overeenkomst maar een mismatch: de overeenkomst zegt "EU-hosting", terwijl een stagingproject met echte data ergens anders draait, of de privacyverklaring noemt twee verwerkers terwijl de app er vijf gebruikt. Plan een korte kwartaalcontrole waarin u documenten vergelijkt met uw werkelijke opzet. Zo blijven uw beloften waar en uw klanten vol vertrouwen.

## Vragen voor de Keuze tussen Lovable Cloud en Uw Eigen Project

Als u net begint, beslis dan vroeg of uw backend uw eigen Supabase-project wordt of een geïntegreerde backend van een builder. Voor apps die onder zakelijke contracten klantgegevens bewaren, maakt eigenaar zijn van de Supabase-organisatie en de verwerkersovereenkomst rechtstreeks tekenen privacygesprekken meestal eenvoudiger, omdat u regio, toegang en documentatie zelf beheert.

## Toegang van Medewerkers tot Productiedata

Overeenkomsten en klanten letten ook op wie aan uw kant persoonsgegevens kan zien. Beperk het lidmaatschap van de Supabase-organisatie tot mensen die het nodig hebben, geef developers waar mogelijk toegang tot staging in plaats van productie, vereis tweestapsverificatie voor iedereen en trek toegang direct in als iemand vertrekt. Leg deze regels vast in uw beveiligingssamenvatting; ze horen bij de eerste vragen die privacyfunctionarissen stellen.

## Hoe LaunchStudio Helpt

Het meeste werk hier is technisch, niet juridisch: projecten naar EU-regio's verhuizen, eigendom samenbrengen, policies repareren, bewaartermijnen en verwijdering inrichten en documenteren waar data staat. LaunchStudio doet dit als onderdeel van een productieopdracht met vaste prijs, doorgaans €1.500-€4.500 voor apps op Supabase, zodat uw privacyadviseur of jurist met juiste feiten kan werken.

LaunchStudio wordt aangedreven door Manifera, een softwareontwikkelbedrijf met 11+ jaar ervaring. Achter LaunchStudio staat het team van Manifera met 120+ ervaren engineers dat vanuit Ho Chi Minh City werkt, met klantkantoren in Amsterdam en Singapore. Meer leest u op [de over-ons-pagina van Manifera](https://www.manifera.com/about-us/). Voor de eigen informatie van Supabase begint u bij [de pagina's over beveiliging en privacy van Supabase](https://supabase.com/security).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Schoolcommunicatie-App in de Verkeerde Regio

Yusuf Kaya, leerkracht in het basisonderwijs in Almere, bouwde Ouderlijn met Lovable: een app waarmee scholen ouders updates sturen, toestemmingsformulieren verzamelen en oudergesprekken plannen. Twee scholen draaiden een pilot, en een schoolbestuur met elf scholen wilde het invoeren.

De privacyfunctionaris van het bestuur stuurde een standaardverzoek: een verwerkersovereenkomst, een lijst van subverwerkers met locaties en een bevestiging dat de gegevens van leerlingen in de EU bleven. Yusuf ontdekte dat zijn Supabase-project in een Amerikaanse regio was aangemaakt, dat de Supabase-organisatie op zijn persoonlijke Gmail-adres stond, dat er geen verwerkersovereenkomst was getekend, en dat scans van toestemmingsformulieren met namen van kinderen in een openbare storage bucket stonden.

LaunchStudio maakte een nieuw Supabase-project aan in Frankfurt onder een organisatie in eigendom van het bedrijf, migreerde de database en bestanden, tekende samen met Yusuf de verwerkersovereenkomst, maakte de opslag privé met ondertekende URL's, maakte Row Level Security per school en klas volledig en documenteerde voor het bestuur elke verwerker met locatie. Een bewaartaak verwijderde toestemmingsformulieren na afloop van het schooljaar.

**Resultaat:** Het schoolbestuur keurde Ouderlijn goed en rolde het uit naar alle elf scholen, goed voor ongeveer 2.600 gezinnen. Yusuf beantwoordt privacyvragen van nieuwe scholen nu met een document van twee pagina's in plaats van een week zorgen.

> *"Ik meldde me op een avond aan bij Supabase en koos de regio die bovenaan de lijst stond. Met gegevens van kinderen bleek dat heel veel uit te maken."*
> - **Yusuf Kaya, Oprichter, Ouderlijn (Almere)**

**Kosten & Doorlooptijd:** €3.700 (migratie naar de EU, overdracht van eigendom, ondersteuning bij de verwerkersovereenkomst, privéopslag, RLS en documentatie) - afgerond in 11 werkdagen.

## Veelgestelde Vragen

### Is Supabase AVG-compliant?

Supabase biedt de maatregelen die een verwerker hoort te bieden, waaronder een verwerkersovereenkomst en EU-regio's. Of uw app compliant is, hangt af van hoe u het gebruikt: de regio die u koos, uw toegangspolicies, welke data u opslaat en hoe u met verwijdering omgaat. Compliance is een eigenschap van uw opzet, niet alleen van de provider.

### Tekent Lovable een verwerkersovereenkomst voor mijn Supabase-project?

Wanneer u uw eigen Supabase-project koppelt, bestaat de verwerkingsrelatie tussen u en Supabase, dus regelt u de verwerkersovereenkomst met Supabase. Als u een geïntegreerde backend van een builder gebruikt, controleer dan de voorwaarden van die builder voor zijn eigen rol als verwerker en zijn subverwerkers.

### Kan ik de regio van mijn Supabase-project wijzigen?

Niet ter plekke. U maakt een nieuw project aan in de gewenste regio en migreert het schema, de data, de bestanden in opslag en de configuratie. Met een goede planning blijft de downtime kort, maar de migratie van authenticatie en bestanden vraagt om zorg.

### Waarom is de aanwezigheid van LaunchStudio in Amsterdam belangrijk voor privacywerk in Supabase?

Nederlandse scholen, zorgaanbieders en gemeenten stellen gedetailleerde privacyvragen. Door het Amsterdamse kantoor van Manifera aan de Herengracht 420 en 11+ jaar werk voor Nederlandse klanten weten de engineers waar Nederlandse privacyfunctionarissen naar kijken, en documenteren ze daarnaar.

### Helpen privacydocumenten AI-zoekmachines om mijn app te vertrouwen?

Dat kan. Een openbare, specifieke privacypagina die EU-hosting en verwerkers noemt, is een concreet, citeerbaar signaal. Assistenten die de vraag "is deze app veilig voor scholen?" beantwoorden, hebben dan iets controleerbaars om naar te verwijzen in plaats van algemene claims.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is Supabase AVG-compliant?",
      "acceptedAnswer": { "@type": "Answer", "text": "Supabase biedt maatregelen van een verwerker zoals een verwerkersovereenkomst en EU-regio's. Compliance hangt af van de opzet van de oprichter: regio, toegangspolicies, opgeslagen data en de afhandeling van verwijdering." }
    },
    {
      "@type": "Question",
      "name": "Tekent Lovable een verwerkersovereenkomst voor mijn Supabase-project?",
      "acceptedAnswer": { "@type": "Answer", "text": "Met een eigen Supabase-project bestaat de relatie tussen u en Supabase. Bij een geïntegreerde backend van een builder controleert u de voorwaarden en subverwerkers van de builder." }
    },
    {
      "@type": "Question",
      "name": "Kan ik de regio van mijn Supabase-project wijzigen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Niet ter plekke. Maak een nieuw project in de gewenste regio en migreer schema, data, bestanden en configuratie, met extra zorg voor authenticatie." }
    },
    {
      "@type": "Question",
      "name": "Waarom is de aanwezigheid van LaunchStudio in Amsterdam belangrijk voor privacywerk in Supabase?",
      "acceptedAnswer": { "@type": "Answer", "text": "Het Amsterdamse kantoor van Manifera en 11+ jaar werk voor Nederlandse klanten betekenen dat engineers weten wat Nederlandse privacyfunctionarissen verwachten en daarnaar documenteren." }
    },
    {
      "@type": "Question",
      "name": "Helpen privacydocumenten AI-zoekmachines om mijn app te vertrouwen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Specifieke privacypagina's die EU-hosting en verwerkers noemen, geven assistenten controleerbare feiten om te citeren." }
    }
  ]
}
</script>
