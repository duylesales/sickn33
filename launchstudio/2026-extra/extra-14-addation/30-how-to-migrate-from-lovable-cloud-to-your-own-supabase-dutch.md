---
Titel: "Migreren van Lovable Cloud naar Uw Eigen Supabase-Project"
Trefwoorden: lovable cloud migreren naar supabase, lovable cloud export, eigen supabase project lovable, lovable cloud migratie, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: SaaS-Oprichter Scale-Up
---

# Migreren van Lovable Cloud naar Uw Eigen Supabase-Project

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Migreren van Lovable Cloud naar Uw Eigen Supabase-Project",
  "description": "Lovable Cloud is een snelle manier om te beginnen, maar sommige oprichters hebben een eigen Supabase-project nodig voor regiokeuze, directe toegang tot de database, compliance of schaalbaarheid. Deze gids legt uit waarom, wat er verhuist, een stappenplan voor de migratie en de risico's rond authenticatie en bestanden.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-07",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-to-migrate-from-lovable-cloud-to-your-own-supabase" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Migrating to Supabase", "url": "https://supabase.com/docs/guides/platform/migrating-to-supabase" },
    { "@type": "CreativeWork", "name": "Lovable documentation", "url": "https://docs.lovable.dev/" },
    { "@type": "CreativeWork", "name": "GDPR Article 28: Processor", "url": "https://gdpr-info.eu/art-28-gdpr/" },
    { "@type": "CreativeWork", "name": "PostgreSQL documentation", "url": "https://www.postgresql.org/docs/current/ddl-rowsecurity.html" }
  ]
}
</script>

**Kort antwoord:** maak een nieuw Supabase-project aan in de regio die u nodig heeft, bouw het schema opnieuw op vanuit de migraties in uw Lovable-repository, exporteer en importeer de data, migreer bestanden en edge functions, ga zorgvuldig om met gebruikersaccounts, en wijs uw Lovable-app daarna naar het nieuwe project en schakel over tijdens een kort onderhoudsvenster. Het schema en de code verhuizen makkelijk. Gebruikersauthenticatie en bestanden vragen de meeste planning.

De functies en exportmogelijkheden van Lovable Cloud ontwikkelen zich, dus controleer welke toegang Lovable op dit moment biedt voordat u begint. Het plan hieronder werkt voor het gangbare geval.

## Belangrijkste Punten

- **Lovable Cloud is een snelle start; uw eigen Supabase-project geeft controle** over de regio, directe toegang tot de database, uw eigen verwerkersovereenkomst, abonnementen en overdraagbaarheid.
- **Schema en edge functions verhuizen makkelijk,** omdat ze in uw repository staan; data, bestanden en vooral gebruikersaccounts vragen om zorgvuldige planning.
- **Oefen de migratie minstens één keer** op een stagingdoel, en controleer aantallen rijen, steekproeven, bestanden en logins vóór de echte overstap.
- **Wachtwoorden van gebruikers kunnen wel of niet meeverhuizen,** afhankelijk van wat kan worden geëxporteerd; plan zo nodig een vriendelijke flow voor wachtwoordherstel of een magic link.
- **Een gangbare migratie kost met LaunchStudio €2.000-€5.000,** met voor de meeste apps een onderhoudsvenster van minder dan een uur.

## Waarom Oprichters Overstappen op Hun Eigen Supabase

Lovable Cloud geeft u een backend zonder dat u die hoeft te beheren, wat ideaal is om te bouwen. Oprichters stappen meestal over wanneer ze nodig hebben:

- **Keuze van de regio,** bijvoorbeeld een EU-regio voor de AVG en klantcontracten
- **Directe toegang** tot de database, logs en instellingen voor debuggen en tooling
- **Eigen overeenkomsten,** zoals een verwerkersovereenkomst rechtstreeks met de databaseprovider
- **Onafhankelijke schaalbaarheid en abonnementen,** los van de inrichting van de builder
- **Overdraagbaarheid,** zodat de backend niet vastzit aan de manier waarop de app is gebouwd

Geen van deze punten is kritiek op Lovable Cloud. Het zijn tekenen dat een product een bedrijf wordt.

## Wat Moet Verhuizen

| Onderdeel | Waar het staat in een Lovable-project | Moeilijkheid |
| --- | --- | --- |
| Schema (tabellen, policies, functies) | `supabase/migrations` in de repository | Laag |
| Edge functions | `supabase/functions` in de repository | Laag |
| Secrets van edge functions | Instellingen van Lovable Cloud | Laag, handmatig opnieuw invoeren |
| Data in tabellen | Database van Lovable Cloud | Middel |
| Bestanden in opslag | Opslag van Lovable Cloud | Middel |
| Authenticatiegebruikers | Authenticatie van Lovable Cloud | Hoog |
| Instellingen van authenticatie (providers, redirect-URL's, e-mailsjablonen) | Instellingen van Lovable Cloud | Middel |
| Geplande taken, webhooks die naar oude URL's wijzen | Verschillend | Middel |

## Stappenplan voor de Migratie

**1. Inventarisatie.** Maak een lijst van tabellen met het aantal rijen, storage buckets met het aantal bestanden, edge functions en hun secrets, authenticatieproviders, externe webhooks (Stripe, Mollie, e-mailproviders) en alles wat gepland draait.

**2. Maak het nieuwe project aan.** Een nieuwe Supabase-organisatie in eigendom van uw bedrijf, een project in de juiste regio, tweestapsverificatie aan.

**3. Pas het schema toe.** Voer de migraties uit uw repository uit op het nieuwe project. Vergelijk de resulterende tabellen, policies en functies met het origineel. Los eventuele afwijkingen op: wijzigingen die buiten migraties om zijn gemaakt, ontbreken.

**4. Deploy edge functions en secrets.** Deploy functies vanuit de repository en stel hun secrets in het nieuwe project in.

**5. Oefen de datamigratie.** Exporteer data en importeer die minstens één keer in het nieuwe project vóór de echte overstap. Controleer het aantal rijen en neem steekproeven van records. Let op sequences, foreign keys en triggers die tijdens de import niet mogen afgaan.

**6. Plan de migratie van gebruikers.** Dit is de kritieke stap. De opties hangen af van de toegang die u heeft:
- Als u authenticatiegebruikers inclusief wachtwoordhashes kunt exporteren, kunnen gebruikers hun wachtwoord houden.
- Zo niet, migreer gebruikers dan zonder wachtwoord en stuur een e-mail "stel uw wachtwoord in", of stap over op magic links.
- Gebruikers met social login (Google, Apple) kunnen meestal opnieuw inloggen zodra de provider op het nieuwe project is ingericht, maar gebruikers-ID's moeten behouden blijven of opnieuw worden gekoppeld, zodat hun data verbonden blijft.

**7. Migreer bestanden.** Kopieer opslagobjecten met dezelfde paden en controleer daarna aantallen en groottes. Werk opgeslagen URL's bij die het domein van het oude project bevatten.

**8. Werk externe diensten bij.** Betaalwebhooks, OAuth-redirect-URL's, instellingen van de e-mailprovider en alles wat uw backend aanroept.

**9. Schakel over.** Kondig een kort onderhoudsvenster aan. Maak het oude project alleen-lezen, voer de laatste synchronisatie van data en bestanden uit, wijs de configuratie van de app naar het nieuwe project, deploy en test de kritieke flows.

**10. Houd het oude project nog een tijd aan.** Verwijder het pas als u een paar weken in productie heeft gedraaid en heeft bevestigd dat er niets ontbreekt.

## Beslissen Wanneer U Migreert

Niet elke app hoeft Lovable Cloud te verlaten. Een nuttige beslisregel: migreer wanneer er een externe eis of een groeibeperking opduikt, niet vanwege een algemeen gevoel dat "echte apps ergens anders draaien". Gangbare aanleidingen zijn een klantcontract dat een specifieke EU-regio of een rechtstreekse verwerkersovereenkomst met de databaseprovider vereist, de behoefte aan databasetoegang vanuit analyse- of rapportagetools, operationele behoeften zoals point-in-time recovery of specifieke rekenkracht, of een investeerder of overnemer die naar platformafhankelijkheid vraagt.

Als geen van deze van toepassing is, is blijven en u richten op klanten vaak de betere besteding van uw tijd.

## De Datamigratie in Meer Detail

Databasemigraties lijken op papier eenvoudig en verbergen in de praktijk details. Zaken om te plannen:

- **Volgorde van tabellen:** foreign keys vereisen bovenliggende rijen vóór onderliggende rijen, of tijdelijk uitgestelde constraints
- **Sequences en identity-kolommen:** na het importeren van rijen met bestaande ID's moeten sequences worden opgehoogd, anders faalt de volgende insert
- **Triggers:** triggers die e-mails versturen of gerelateerde rijen aanmaken, horen tijdens de import te worden uitgeschakeld om bijwerkingen te voorkomen
- **Tijdzones en typen:** tijdstempels en enum-typen moeten exact overeenkomen
- **Grote tabellen:** kunnen in delen moeten worden verwerkt om time-outs te voorkomen

De standaardtools van PostgreSQL voor dump en restore regelen veel hiervan wanneer u directe toegang tot de database heeft. Waar de toegang beperkt is, werken exports per tabel in een consistente volgorde, met zorgvuldige controle achteraf.

## Authenticatie: Het Deel dat Gebruikers Merken

Gebruikers merken maar één ding van uw migratie: of ze nog kunnen inloggen. Drie scenario's, van best tot acceptabel:

1. **Wachtwoordhashes en gebruikers-ID's kunnen worden geëxporteerd en geïmporteerd.** Gebruikers merken niets.
2. **Gebruikers-ID's en e-mailadressen verhuizen, wachtwoorden niet.** Gebruikers krijgen een duidelijke e-mail met uitleg over de wijziging en een link om met één klik een nieuw wachtwoord in te stellen, of u stapt over op magic links of eenmalige codes.
3. **Gebruikers met social login** (Google, Microsoft, Apple) loggen opnieuw in zodra de providers op het nieuwe project zijn ingericht, mits hun gebruikers-ID's of e-mailadressen aan hun data zijn gekoppeld.

Wat er ook van toepassing is, communiceer vóór de overstap, niet erna. Een korte aankondiging een paar dagen van tevoren voorkomt een stroom aan supportverzoeken.

## Bestanden en URL's

Opslagbestanden moeten worden gekopieerd met dezelfde bucketstructuur en paden. Let op absolute URL's in de database die het domein van het oude project bevatten; die moeten worden bijgewerkt. Ondertekende URL's die vóór de overstap zijn gemaakt, werken niet meer, wat meestal onschuldig is omdat ze toch verlopen.

## Externe Diensten

Maak een lijst van elke dienst die uw backend aanroept of die uw backend aanroept: betaalwebhooks, OAuth-redirect-URL's, callbacks van de e-mailprovider, automatiseringstools, analytics. Werk elk ervan bij tijdens het venster van de overstap en test ze direct daarna. Vergeten betaalwebhooks zijn de duurste vergissing, omdat betalingen blijven slagen terwijl uw app ze niet meer vastlegt.

## Controle na de Migratie

Loop na de overstap binnen het eerste uur een checklist door: registreren, inloggen, wachtwoordherstel, een kernactie voor elke rol, een testbetaling, een e-mail, een upload en download van een bestand, en een geplande taak als u die heeft. Houd de oude omgeving een paar weken alleen-lezen beschikbaar voor het geval u data moet vergelijken. Ruim hem daarna bewust op, inclusief het verwijderen van persoonsgegevens die er nog in staan.

## Privacydocumentatie Bijwerken

Overstappen op uw eigen Supabase-project verandert uw relaties met verwerkers. Teken de verwerkersovereenkomst van Supabase, werk uw lijst van verwerkers en privacyverklaring bij met de nieuwe regio, en informeer zakelijke klanten als uw verwerkersovereenkomsten een melding vereisen bij wijzigingen van subverwerkers. Dit is vaak juist de reden voor de migratie, dus zorg dat het papierwerk het weerspiegelt.

## De Wijziging Communiceren aan Gebruikers en Klanten

Een migratie is ook een communicatietaak. Vertel gebruikers een paar dagen vóór de overstap wat er gaat gebeuren, wanneer, hoe lang het onderhoudsvenster duurt en of ze iets moeten doen, zoals een nieuw wachtwoord instellen. Stuur na de overstap een korte bevestiging. Voeg voor zakelijke klanten een notitie toe over de nieuwe datalocatie en bijgewerkte informatie over verwerkers. Duidelijke communicatie maakt van een technische wijziging een moment dat vertrouwen opbouwt in plaats van verwarring.

## Planning van een Gangbare Migratie

Voor een kleine tot middelgrote Lovable-app is een realistische planning: twee dagen voor inventarisatie en planning, twee tot drie dagen voor het inrichten van het nieuwe project en het oefenen van de datamigratie, één dag voor de voorbereiding van authenticatie en externe diensten, een onderhoudsvenster van minder dan een uur voor de overstap, en een paar dagen nauwlettend monitoren daarna. Grotere hoeveelheden data of complexe authenticatie voegen tijd toe; plan de overstap in een rustige periode, zoals vroeg op een doordeweekse ochtend.

## Risico's om op te Plannen

- **Verloren logins** als wachtwoordhashes niet mee kunnen: communiceer duidelijk en maak het herstel pijnloos
- **Kapotte koppelingen in data** als gebruikers-ID's veranderen: behoud ID's waar mogelijk
- **Afwijkingen in het schema** waar de live database verschilt van de migraties
- **Webhooks die nog naar de oude backend wijzen,** waardoor betalingen stil falen
- **De verbindingsinstellingen van Lovable:** bevestig na de migratie dat Lovable met het nieuwe project werkt, zodat toekomstige prompts de juiste backend wijzigen

## Hulp Inschakelen

Een migratie vanuit Lovable Cloud is een gangbare klus voor LaunchStudio, meestal een vaste €2.000-€5.000, afhankelijk van de hoeveelheid data, de complexiteit van de authenticatie en de integraties, met voor de meeste apps een gepland onderhoudsvenster van minder dan een uur. Anders dan freelancers wordt LaunchStudio ondersteund door Manifera, vertrouwd door Vodafone, TNO en CFLW, waarvan de engineers al 11+ jaar datamigraties uitvoeren voor enterpriseklanten vanuit Ho Chi Minh City, Singapore en Amsterdam. Zie [de technologieën van Manifera](https://www.manifera.com/about-us/manifera-technologies/) en de [migratiegidsen van Supabase](https://supabase.com/docs/guides/platform/migrating-to-supabase). Zie voor de vraag over de regio specifiek ons artikel over [EU-datahosting](https://launchstudio.eu/nl/blog/app-hosting-in-the-netherlands-eu-data-hosting-explained).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Boerderijwinkel Die een Eigen Backend Nodig Had

Gijs Visser heeft een melkveebedrijf bij Assen met een boerderijwinkel, en bouwde Boerderijkist in Lovable met Lovable Cloud: klanten bestellen vooraf wekelijkse kisten met kaas, melk en groenten, kiezen een ophaaltijd en betalen online. Ongeveer 380 huishoudens bestelden regelmatig. Toen een regionale coöperatie van zeven boerderijen het platform onder eigen merk wilde gebruiken, eiste het contract een database in de EU onder een verwerkersovereenkomst die de coöperatie kon beoordelen, en directe toegang voor de rapportagetool van hun accountant.

Gijs vroeg LaunchStudio de backend te verhuizen. De inventarisatie liet 23 tabellen zien, 4 edge functions, ongeveer 1.600 productfoto's en 410 gebruikersaccounts, de meeste met e-mailadres en wachtwoord. Twee tabellen waren met de hand aangepast en kwamen niet overeen met de migratiebestanden.

Engineers maakten een Supabase-project in Frankfurt aan in eigendom van het bedrijf, brachten de afwijkingen in het schema onder in nette migraties, oefenden de data-import twee keer, deployden de edge functions met nieuwe secrets, migreerden de productfoto's en werkten de webhook-URL van Mollie bij. Wachtwoordhashes konden in dit geval niet worden meegenomen, dus bereidde het team een vriendelijke e-mail voor om met één klik een wachtwoord in te stellen, plus een optie met magic links. De overstap vond plaats op een maandagavond tijdens een onderhoudsvenster van 40 minuten.

**Resultaat:** Op woensdag had 87% van de actieve klanten opnieuw ingelogd; de rest volgde met de bestelherinnering van de week erna. De coöperatie tekende, en Boerderijkist bedient nu zeven boerderijwinkels vanaf één platform.

> *"Met Lovable Cloud kon ik beginnen zonder na te denken over databases. De coöperatie had nodig dat ik wél over databases nadacht."*
> - **Gijs Visser, Oprichter, Boerderijkist (Assen)**

**Kosten & Doorlooptijd:** €3.800 (schema in lijn gebracht, migratie van data en bestanden, migratie van gebruikers met flow voor wachtwoordherstel, bijgewerkte webhooks en overstap) - afgerond in 10 werkdagen.

## Veelgestelde Vragen

### Waarom zou ik van Lovable Cloud overstappen op mijn eigen Supabase-project?

Gangbare redenen zijn controle over de regio van de data, directe toegang tot de database voor tooling en debuggen, een eigen verwerkersovereenkomst met de provider, onafhankelijke schaalbaarheid en minder afhankelijkheid van de builder. Veel oprichters blijven tevreden op Lovable Cloud; overstappen is zinvol wanneer een klant, toezichthouder of groei het vereist.

### Moeten mijn gebruikers na de migratie hun wachtwoord opnieuw instellen?

Dat hangt ervan af of wachtwoordhashes uit uw huidige opzet kunnen worden geëxporteerd. Als dat kan, houden gebruikers hun wachtwoord. Zo niet, dan beperkt een goed ontworpen flow voor herstel of met magic links de drempel. Gebruikers met social login loggen meestal gewoon opnieuw in.

### Kan ik Lovable blijven gebruiken nadat ik naar mijn eigen Supabase ben overgestapt?

Ja. Lovable kan met uw eigen Supabase-project werken. Controleer na de migratie dat Lovable met het nieuwe project is verbonden, zodat toekomstige prompts en databasewijzigingen op de juiste plek terechtkomen.

### Hoe verkleint Manifera het risico van een datamigratie?

Door hem te oefenen. De 11+ jaar enterprisemigraties van Manifera laten zien dat de meeste mislukkingen voortkomen uit ongeteste aannames. LaunchStudio voert minstens één volledige oefening uit, controleert aantallen en steekproeven, en plant een rollback vóór de echte overstap.

### Heeft het migreren van mijn backend invloed op mijn posities in zoekmachines?

Niet als het goed wordt gedaan. Uw domein en pagina-URL's blijven hetzelfde, en een kort gepland onderhoudsvenster schaadt de posities niet. Vermijd lange storingen en zorg dat openbare pagina's na de overstap dezelfde inhoud blijven tonen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom zou ik van Lovable Cloud overstappen op mijn eigen Supabase-project?",
      "acceptedAnswer": { "@type": "Answer", "text": "Voor controle over de regio, directe toegang tot de database, eigen verwerkersovereenkomsten, onafhankelijke schaalbaarheid of minder afhankelijkheid van de builder, meestal aangestuurd door klanten, regelgeving of groei." }
    },
    {
      "@type": "Question",
      "name": "Moeten mijn gebruikers na de migratie hun wachtwoord opnieuw instellen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Alleen als wachtwoordhashes niet kunnen worden geëxporteerd. Anders houden gebruikers hun wachtwoord; een goede flow voor herstel of met magic links beperkt de drempel wanneer nodig." }
    },
    {
      "@type": "Question",
      "name": "Kan ik Lovable blijven gebruiken nadat ik naar mijn eigen Supabase ben overgestapt?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Controleer dat Lovable met het nieuwe project is verbonden, zodat toekomstige wijzigingen naar de juiste backend gaan." }
    },
    {
      "@type": "Question",
      "name": "Hoe verkleint Manifera het risico van een datamigratie?",
      "acceptedAnswer": { "@type": "Answer", "text": "Door hem te oefenen, aantallen en steekproeven te controleren en een rollback te plannen, op basis van 11+ jaar enterprisemigraties." }
    },
    {
      "@type": "Question",
      "name": "Heeft het migreren van mijn backend invloed op mijn posities in zoekmachines?",
      "acceptedAnswer": { "@type": "Answer", "text": "Niet als het goed wordt gedaan: hetzelfde domein en dezelfde URL's, kort gepland onderhoud en ongewijzigde openbare inhoud." }
    }
  ]
}
</script>
