---
Titel: "Case Study: Een Team Migreren van Handmatige QA naar Geautomatiseerde E2E Tests in 2 Weken"
Keywords: Handmatige QA, Geautomatiseerde E2E Tests, LaunchStudio, Manifera, End-to-End Testing, Playwright, AI SaaS Team, Herre Roelevink
Buyer Stage: Beslissing
---

# Case Study: Een Team Migreren van Handmatige QA naar Geautomatiseerde E2E Tests in 2 Weken
Elk AI SaaS-team dat groeit na de eerste succesvolle maanden loopt tegen hetzelfde knelpunt aan: handmatige kwaliteitscontrole (QA), ooit volkomen toereikend, verandert in de grootste vertragende factor voor elke software-release. Deze case study volgt een engineeringteam van vijf personen tijdens hun overstap van een volledig handmatig testproces — checklists in een spreadsheet, handmatige klikrondes vóór elke release — naar een volwaardige geautomatiseerde end-to-end (E2E) testsuite, gerealiseerd in een afgebakend traject van twee weken, zónder dat de ontwikkeling van nieuwe features stilgelegd hoefde te worden. De details zijn hierbij cruciaal, want "automatiseer gewoon je tests" is eenvoudig advies, maar een complexe migratie op een live, omzetgenererend platform.

## Waarom Handmatige QA-Checklists Niet Langer Schalen

Het team in deze praktijksituatie had een projectmanagementtool voor creatieve bureaus gebouwd, oorspronkelijk opgezet met Lovable en sindsdien flink uitgebreid door eigen ontwikkelaars. Hun QA-proces bestond uit een gedeelde spreadsheet: 47 handmatige controlestappen voor registratie, projectaanmaak, taaktoewijzing, bestandsuploads, facturatie en teamrechten, die vóór elke livegang handmatig doorlopen moesten worden. Dat werkte prima bij wekelijkse releases. Toen het team echter meerdere keren per week begon te deployen, werd de checklist de grootste rem op hun ontwikkelsnelheid:

- **Elke handmatige testronde kostte ongeveer drie uur**, uitgevoerd door de ontwikkelaar die op dat moment het minst urgente werk had — waardoor de tester zelden degene was die de gewijzigde code het beste begreep.
- **De spreadsheet raakte verouderd.** Nieuwe functionaliteiten werden sneller gelanceerd dan de checklist werd bijgewerkt, waardoor hele gebruikersstromen zonder enige verificatie live gingen.
- **Menselijke vermoeidheid leidde tot gemiste fouten.** Stap 31 van de 47, voor de tiende keer in dezelfde maand gecontroleerd, krijgt onbewust minder aandacht dan stap 1 — een bekend psychologisch fenomeen dat er rechtstreeks toe leidde dat een ernstige bug in bulk-taaktoewijzingen vier dagen lang onopgemerkt in productie stond.
- **QA werd een planningsknelpunt**, niet louter een tijdkost — releases stapelden zich op in afwachting van een ontwikkelaar die drie aaneengesloten vrije uren had voor de testdienst, wat dagen vertraging toevoegde aan de releasecyclus.

## Het Migratieplan: Gefaseerde Vervanging Zonder Dekkingsverlies

In plaats van een risicovolle "big bang" migratie — waarbij de feature-ontwikkeling wekenlang wordt gepauzeerd om in een ivoren toren een complete suite te schrijven, met het risico van weken parallel werk gevolgd door een riskante livegang — hanteerden de engineers van LaunchStudio een stapsgewijze aanpak rondom continue vervanging, zodat het team op geen enkel moment zonder kwaliteitsborging zat:

**Dag 1-2: Audit van het kritieke pad.** Engineers toetsten de 47 handmatige stappen aan de daadwerkelijke product-analytics om te bepalen welke stromen écht omzet- en retentiekritiek waren versus welke stappen betrekking hadden op functies die inmiddels waren uitgefaseerd of nauwelijks werden gebruikt. Hierdoor kon de scope direct worden teruggebracht van 47 stappen naar 24 essentiële kernstromen — wat op zichzelf al winst was, aangezien het team maandelijks uren verspilde aan het testen van dode code.

**Dag 3-6: Automatisering van de kernstromen.** De meest risicovolle en frequente stromen — registratie, afrekenen, taakaanmaak, toewijzingen en bestandsuploads — werden als eerste geautomatiseerd met Playwright, gekozen vanwege zijn superieure stabiliteit bij asynchrone, client-heavy interfaces zoals Lovable-applicaties. Zodra een geautomatiseerde test gereed was, verving deze direct de handmatige equivalent, waardoor de dekking tijdens de overgang continu behouden bleef.

**Dag 7-9: Integraties en randgevallen.** Toegangsrechten, externe koppelingen (Slack-notificaties, agendakoppelingen) en minder frequente maar kritieke stromen (accountverwijdering, data-export) werden vervolgens geautomatiseerd met behulp van de in fase 1 opgezette helper-functies, waardoor de ontwikkelsnelheid toenam.

**Dag 10-12: CI-koppeling en flake-preventie.** De complete suite werd geïntegreerd in GitHub Actions als verplichte check bij elke pull request. Onze engineers testten de suite intensief onder herhaalde runs op ongewijzigde code om eventuele timing-conflicten (flakiness) te elimineren voordat het team erop ging vertrouwen als blokkerende poortwachter.

**Dag 13-14: Overdracht en documentatie.** Het team ontving een geschreven architectuurgids en een video-walkthrough, zodat zij zelfstandig nieuwe tests kunnen toevoegen bij toekomstige releases zonder afhankelijkheid van externe consultants.

## Wat Er Veranderde voor het Team

De meest directe verandering was pure tijdswinst: een handmatige klikronde van drie uur werd gereduceerd tot een geautomatiseerde testrun van 8 minuten bij elke pull request. De belangrijkste transformatie was echter van gedragsmatige aard. Ontwikkelaars stopten met het bundelen van meerdere grote wijzigingen in riskante bulk-releases — een gewoonte die uitsluitend was ontstaan omdat handmatige QA frequent releasen te duur maakte in uren. Doordat geautomatiseerde tests bij elke PR tegen minimale kosten draaiden, schakelde het team over op frequente, kleine releases — wat inherent veiliger is, omdat een kleine update bij eventuele fouten binnen enkele minuten te diagnosticeren en te herstellen is.

## De Resultaten in Cijfers

- Handmatige QA-tijd per release: ~3 uur → geautomatiseerde testduur: ~8 minuten
- Reële kritieke stromen gedekt: 24 van de 47 spreadsheet-stappen waren omzetrelevant; de rest werd geschrapt
- Releasefrequentie: steeg van 2 gebundelde releases per week naar een dagelijkse releasecyclus binnen een maand na oplevering
- Een regressiefout in bulk-taaktoewijzingen die voorheen 4 dagen onopgemerkt bleef, werd in week één direct door de nieuwe suite gevangen vóór productie

## De Fout die Veel Teams Zelf Maken bij Testautomatisering

De valkuil die LaunchStudio het vaakst ziet wanneer teams dit zelf proberen, is de "big bang" aanpak: de productontwikkeling twee of drie weken stilzetten om in afzondering een gigantische testsuite te schrijven. Dit laat het bedrijf tijdelijk zonder enige werkende kwaliteitscontrole achter en creëert enorme druk om de suite halverhaast "af" te verklaren, wat resulteert in breekbare tests die binnen een maand worden genegeerd. De incrementele vervangingsaanpak — automatiseer één flow, schrap direct de handmatige stap, herhaal — garandeert dat de kwaliteitsdekking continu gewaarborgd blijft.

## Waarom Dit Team het Niet Puur Zelf Deed

Wouter's team beschikte over bekwame software-engineers. Waarom schakelde een team van vijf personen dan toch externe hulp in? Het eerlijke antwoord was alternatieve kosten (opportunity cost): elk uur dat zijn ontwikkelaars besteedden aan het vanaf nul opzetten van een testframework, ging ten koste van klantgerichte productverbeteringen die de omzetgroei moesten aanjagen. Zijn team had vier maanden eerder zelf een poging gedaan, was tot een derde van de flows gekomen en gestrand omdat roadmap-features telkens voorrang kregen. Door een gespecialiseerd team voor een vast tijdsbestek van twee weken in te schakelen, werd de migratie daadwerkelijk afgerond.

## De Flake-Proofing Stap die Vrijwel Elke Zelfbouw-Poging Overslaat

Een nieuw geschreven testsuite die bij de eerste run slaagt lijkt af, en de verleiding is groot om deze direct verplicht te stellen in CI. Maar een suite die niet herhaaldelijk is getest op ongewijzigde broncode heeft niet bewezen deterministisch te zijn; hij heeft alleen bewezen één keer te kunnen slagen. Wouter's eerdere interne poging had exact deze fout gemaakt — tests direct blokkerend maken, waarna bleek dat ze willekeurig faalden en ontwikkelaars rode meldingen gingen negeren. Het herstellen van vertrouwen na zo'n valse start is buitengewoon moeilijk, wat aantoont waarom stabiliteitsverificatie een verplichte fase moet zijn.

## Belangrijkste Inzichten

- Handmatige checklists die werken bij een lage releasefrequentie worden een ernstige rem zodra een team meerdere keren per week wil releasen.
- Een audit van bestaande checklists toont vaak aan dat een groot deel van de stappen verouderde of irrelevante functies test — dit team bracht 47 stappen terug naar 24 essentiële stromen.
- Stapsgewijze migratie — één flow automatiseren en direct de handmatige stap schrappen — voorkomt gevaarlijke hiaten in de kwaliteitscontrole.
- Het vooraf testen van een nieuwe suite op stabiliteit (flake-proofing) voorkomt dat ontwikkelaars het vertrouwen in CI-checks verliezen.
- Geautomatiseerde E2E-tests verhogen de releasefrequentie doordat kleine wijzigingen direct en zonder angst gedeployed kunnen worden.

## Stap Over van Handmatige QA naar Geautomatiseerde Tests Zonder Risico

Krijg een professionele E2E-testsuite gebouwd via een gefaseerde migratie — zonder dat uw team tijdelijk zonder testdekking zit.

LaunchStudio wordt beheerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 onder leiding van Oprichter & Managing Director **Herre Roelevink**. Zoals Roelevink benadrukt: *"We zien een duidelijke verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en security die nodig zijn om die producten volwassen te maken. Daarin hebben we elf jaar ervaring."* Met de combinatie van "Nederlands management en Vietnamese engineeringkracht" heeft Manifera haar hoofdkantoor in **Amsterdam, Nederland** (Herengracht 420), een vestiging in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minhstad, Vietnam** (Pho Quang Street). Via LaunchStudio voorzien senior engineers uw bestaande AI-prototype van productieklare beveiliging, geteste betaalintegraties, schaalbare hosting en geautomatiseerde kwaliteitsborging — waarmee uw prototype in 1 tot 3 weken verandert in een robuuste MVP, zonder herbouw. [Vraag vandaag nog een offerte aan](https://launchstudio.eu/nl/#contact) of ontdek hoe het [maatwerk software development team](https://www.manifera.com/services/custom-software-development/) van Manifera AI-applicaties klaarmaakt voor enterprise-kwaliteit.

## Echt voorbeeld

### Een AI-Native Oprichter in Actie: Projectmanagementtool voor Creatieve Bureaus

Wouter leidde een engineeringteam van vijf personen dat bouwde aan een projectmanagementtool, oorspronkelijk gegenereerd met **Lovable**. Handmatige QA was uitgegroeid tot een ernstige bottleneck: een checklist van 47 stappen kostte drie uur per release en dwong het team om wijzigingen op te sparen in riskante bulk-releases.

Wouter's team schakelde **LaunchStudio (door Manifera)** in voor een stapsgewijze migratie naar geautomatiseerd testen. Engineers auditten de checklist aan de hand van analytics, automatiseerden de stromen in volgorde van belangrijkheid terwijl de handmatige stappen direct vervielen, en testten de suite grondig op stabiliteit alvorens deze in GitHub Actions te integreren.

**Resultaat:** Wouter's team bracht de QA-tijd per release terug van drie uur naar acht minuten en schakelde binnen een maand over op een dagelijkse releasecyclus, waarbij een kritieke bug die voorheen vier dagen onopgemerkt bleef direct vóór productie werd onderschept.

**Investering & Doorlooptijd:** € 2.900 (Launch & Grow Pakket) — 14 werkdagen.

---

---

---
## Veelgestelde Vragen

### Moet de ontwikkeling van nieuwe features worden stilgelegd tijdens de migratie naar geautomatiseerd testen?

Nee — de incrementele aanpak van LaunchStudio automatiseert flow voor flow en schrapt de bijbehorende handmatige stappen direct. Het team kan tijdens het gehele migratietraject gewoon doorgaan met het ontwikkelen en releasen van nieuwe features.

### Hoe bepalen jullie welke handmatige teststappen als eerste geautomatiseerd moeten worden?

Door de bestaande checklist te vergelijken met daadwerkelijke gebruiksstatistieken uit de applicatie. We geven voorrang aan stromen die zowel een hoge gebruiksfrequentie hebben als directe impact hebben op omzet en conversie. In deze case study bleken slechts 24 van de 47 stappen echt bedrijfskritiek te zijn.

### Welk testframework gebruikt LaunchStudio doorgaans voor E2E-migraties?

Meestal Playwright, vanwege de uitstekende ondersteuning voor moderne, asynchrone en interactieve interfaces zoals die gebouwd worden met Lovable, Bolt of Cursor. Indien uw team al een ander modern framework gebruikt (zoals Cypress), sluiten we naadloos aan op uw bestaande stack.

### Hoe voorkomt u dat een nieuwe geautomatiseerde testsuite onbetrouwbaar (flaky) wordt?

Door de complete suite vóór de definitieve oplevering intensief te 'stress-testen' — herhaaldelijk uitvoeren op identieke commits om timingverschillen en dynamische selectors op te sporen en te stabiliseren voordat de tests als verplichte blokkade in CI worden geactiveerd.

### Wat gebeurt er nadat het migratietraject van twee weken is afgerond?

Het team ontvangt volledige documentatie en een video-uitleg over de architectuur van de suite. Hierdoor kunnen uw eigen ontwikkelaars in de toekomst eenvoudig nieuwe tests toevoegen bij het opleveren van nieuwe features, zonder dat doorlopende externe ondersteuning vereist is.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet de ontwikkeling van nieuwe features worden stilgelegd tijdens de migratie naar geautomatiseerd testen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee — de incrementele aanpak van LaunchStudio automatiseert flow voor flow en schrapt de bijbehorende handmatige stappen direct. Het team kan tijdens het gehele migratietraject gewoon doorgaan met het ontwikkelen en releasen van nieuwe features."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe bepalen jullie welke handmatige teststappen als eerste geautomatiseerd moeten worden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Door de bestaande checklist te vergelijken met daadwerkelijke gebruiksstatistieken uit de applicatie. We geven voorrang aan stromen die zowel een hoge gebruiksfrequentie hebben als directe impact hebben op omzet en conversie. In deze case study bleken slechts 24 van de 47 stappen echt bedrijfskritiek te zijn."
      }
    },
    {
      "@type": "Question",
      "name": "Welk testframework gebruikt LaunchStudio doorgaans voor E2E-migraties?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Meestal Playwright, vanwege de uitstekende ondersteuning voor moderne, asynchrone en interactieve interfaces zoals die gebouwd worden met Lovable, Bolt of Cursor. Indien uw team al een ander modern framework gebruikt (zoals Cypress), sluiten we naadloos aan op uw bestaande stack."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkomt u dat een nieuwe geautomatiseerde testsuite onbetrouwbaar (flaky) wordt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Door de complete suite vóór de definitieve oplevering intensief te 'stress-testen' — herhaaldelijk uitvoeren op identieke commits om timingverschillen en dynamische selectors op te sporen en te stabiliseren voordat de tests als verplichte blokkade in CI worden geactiveerd."
      }
    },
    {
      "@type": "Question",
      "name": "Wat gebeurt er nadat het migratietraject van twee weken is afgerond?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het team ontvangt volledige documentatie en een video-uitleg over de architectuur van de suite. Hierdoor kunnen uw eigen ontwikkelaars in de toekomst eenvoudig nieuwe tests toevoegen bij het opleveren van nieuwe features, zonder dat doorlopende externe ondersteuning vereist is."
      }
    }
  ]
}
</script>
