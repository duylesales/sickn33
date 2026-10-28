---
Titel: "Vendor Lock-in: Een Exitplan voor Elke Dienst Die Uw App Gebruikt"
Trefwoorden: vendor lock-in, exitplan, bedrijfscontinuïteit, afhankelijkheden van diensten, Supabase-export, e-mailfailover, wisselen van AI-aanbieder, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: SaaS Scale-Up
---

# Vendor Lock-in: Een Exitplan voor Elke Dienst Die Uw App Gebruikt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Vendor Lock-in: Een Exitplan voor Elke Dienst Die Uw App Gebruikt",
  "description": "Een AI-gebouwd product hangt doorgaans af van tien tot twintig externe diensten, en elk daarvan kan prijzen verhogen, uw account blokkeren, voorwaarden wijzigen of verdwijnen. Hoe u elke afhankelijkheid in kaart brengt, begrijpt welke lock-in elke dienst veroorzaakt, per dienst een kort exitplan schrijft, en de paar wissels die ertoe doen snel maakt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-29",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/vendor-lock-in-an-exit-plan-for-every-service-your-app-uses" }
}
</script>

Bouwen met Lovable, Bolt of Replit betekent vanaf de eerste dag bouwen op de diensten van anderen. De bouwtool zelf, de hosting, de database en authenticatie, bestandsopslag, transactionele e-mail, betalingen, een AI-model, analyse, foutregistratie, de domeinregistrar. Een typisch AI-gebouwd B2B-product hangt af van tien tot twintig externe diensten - en de oprichter koos de meeste daarvan door een standaardinstelling te accepteren.

Dat is geen fout. Beheerde diensten gebruiken is wat een klein team in staat stelt een serieus product te draaien. Maar elk van die diensten kan veranderen op manieren die u niet beheerst: een prijsverhoging, een geblokkeerd account door een automatische misbruikcontrole, gewijzigde voorwaarden, een overname, een functie die wordt stopgezet, een regionale storing, een bedrijf dat gewoon ophoudt. Wanneer het gebeurt, is de vraag niet of u van de dienst afhangt, maar hoe lang het zou duren om er niet meer van af te hangen.

Alle lock-in vermijden is niet mogelijk en ook niet wenselijk. Wat wel mogelijk is: voor elke afhankelijkheid weten wat u zou doen als u moest vertrekken - en de handvol voorbereidingen treffen die van een crisis een paar dagen werk maken. Dit artikel behandelt hoe u het overzicht opbouwt, de soorten lock-in, wat een exitplan bevat, de diensten die de meeste voorbereiding verdienen, en de vragen die klanten erover zullen stellen.

## Begin met een Overzicht

De meeste oprichters kunnen niet elke dienst opnoemen waarvan hun product afhangt. De lijst zit in factuurmails, in omgevingsvariabelen, in DNS-records en in de code, en niemand heeft haar samengesteld.

Stel haar één keer op, als tabel, met een rij per dienst:

- **Wat ze doet** en welke functies ervan afhangen.
- **Wie het account beheert** - het bedrijf of een persoon, en welke login.
- **Welke data ze bevat** - klantdata, uw code, configuratie, niets.
- **Maandelijkse kosten** en contractvoorwaarden - opzegtermijnen, clausules over prijswijzigingen.
- **Regio** waar ze data verwerkt.
- **Soort lock-in** - hieronder beschreven.
- **Exitplan** - een link naar een kort document.
- **Laatst bekeken.**

Bronnen om te controleren: uw omgevingsvariabelen en geheimen, de lijst met dependencies in uw code, DNS-records, uw creditcardafschriften, uw inbox op "welkom bij"-berichten, en de lijst met subverwerkers als u die hebt, zoals het artikel over subverwerkers in deze reeks beschrijft. Het overzicht is ook de basis van die lijst met subverwerkers, de lijst met diensten uit het overdrachtsartikel, en het antwoord op een groot deel van elke beveiligingsvragenlijst.

## De Soorten Lock-in

Verschillende diensten binden u op verschillende manieren, en de moeite om te vertrekken hangt af van welke.

**Lock-in door data.** De dienst bevat data die u nodig hebt, en die eruit halen is moeilijk of onvolledig. Een database is het voor de hand liggende voorbeeld; minder voor de hand liggend zijn betaalproviders met opgeslagen kaarten en incassomachtigingen, en authenticatiediensten met wachtwoordhashes.

**Lock-in door code.** Uw code roept de eigen API van de dienst overal in de codebase rechtstreeks aan, zodat vervangen betekent dat veel bestanden moeten worden herschreven.

**Lock-in door identiteit.** Gebruikers, klanten of integraties worden geïdentificeerd met de ID's van de dienst - het klant-ID van een betaalprovider gebruikt als uw primaire sleutel, het gebruikers-ID van een authenticatieaanbieder waarnaar overal wordt verwezen.

**Lock-in door reputatie.** De dienst bezit iets dat tijd kostte om op te bouwen: een verzendreputatie voor e-mail, een vermelding in een app store, posities in zoekmachines op een domein van het platform.

**Operationele lock-in.** Kennis over hoe de dienst is ingericht, bestaat alleen in het dashboard ervan, of in het hoofd van één persoon.

**Contractuele lock-in.** Minimale looptijden, lange opzegtermijnen, boetes, of prijzen die sterk stijgen nadat een verplichting afloopt.

Een dienst kan er meerdere tegelijk veroorzaken. Een betaalprovider veroorzaakt doorgaans lock-in door data, identiteit en contract; een bouwtool veroorzaakt lock-in door code en operationele lock-in totdat de code in uw eigen repository staat.

## Wat een Exitplan Bevat

Een exitplan is geen migratieproject. Het is een pagina per belangrijke dienst, vooraf geschreven, die vijf vragen beantwoordt.

1. **Aanleidingen.** Wat zou ons doen vertrekken? Een prijsverhoging boven een drempel, herhaalde storingen, een eigenaarswissel, een beleidswijziging, een geblokkeerd account.
2. **Data.** Wat moeten we meenemen, en hoe krijgen we het eruit? Welke export, in welk formaat, hoe volledig, hoe lang het duurt.
3. **Alternatieven.** Welke één of twee diensten haar zouden kunnen vervangen, en wat er verschilt.
4. **Moeite.** Wat er moet veranderen - code, configuratie, DNS, communicatie met klanten - met een eerlijke schatting in dagen.
5. **Voorbereiding.** Wat we nu doen zodat vertrekken later sneller gaat: regelmatige exports, een abstractielaag, een tweede ingerichte aanbieder, contractvoorwaarden.

Voor de meeste diensten is het plan een halve pagina. Voor de paar kritieke is het langer, en wordt de voorbereiding echt uitgevoerd in plaats van beschreven.

## De Bouwtool Zelf

De eerste afhankelijkheid van een AI-gebouwd product is de tool waarin het is gebouwd. Bestaat de code alleen in Lovable, Bolt of Replit, dan zit het product vast aan de beschikbaarheid, prijzen en het voortbestaan van die tool.

De voorbereiding is eenvoudig en moet direct gebeuren: de code gesynchroniseerd naar een Git-repository in een account dat het bedrijf bezit, zoals de artikelen over Git en overdracht in deze reeks beschrijven. Met de code in uw eigen repository wordt de bouwtool een handige editor in plaats van de enige plek waar uw product bestaat. De artikelen over Bolt naar Next.js en Replit naar AWS in deze reeks behandelen wat weggaan werkelijk inhoudt als dat ooit nodig is.

## Database en Authenticatie

Supabase is gebouwd op Postgres, wat ongeveer zo overdraagbaar is als databases maar kunnen zijn. Een logische dump is te herstellen in elke Postgres-host. Die overdraagbaarheid is alleen echt als u haar gebruikt.

**Maak regelmatig exports naar opslag die u beheert**, buiten Supabase - een nachtelijke of wekelijkse `pg_dump` naar een object storage-bucket bij een andere aanbieder, versleuteld, met een getest herstel, zoals het back-upartikel in extra-11 beschrijft. Dit is tegelijk een back-up en een uitweg.

**Weet wat specifiek is voor Supabase.** Row level security policies, databasefuncties en triggers zijn standaard Postgres en gaan mee met de dump. Edge functions, opslagbuckets, realtime-abonnementen en de automatisch gegenereerde REST API zijn functies van Supabase die elders een equivalent nodig hebben.

**Authenticatie is overdraagbaar als u ervoor plant.** Supabase Auth slaat gebruikers op in de tabel `auth.users` met bcrypt-wachtwoordhashes, die de meeste authenticatiesystemen kunnen importeren, zodat gebruikers hun wachtwoord kunnen houden. Verwijs waar praktisch naar gebruikers via uw eigen profiel-ID in plaats van het ID van de authenticatieaanbieder door elke tabel te verspreiden, en houd het e-mailadres als stabiele tweede identificator.

Het artikel over weggaan bij Supabase in deze reeks behandelt een volledige verhuizing; de voorbereiding hierboven maakt er een gepland project van in plaats van een noodgeval.

## Transactionele E-mail

E-mail is de dienst waarvan uitval het snelst wordt opgemerkt - wachtwoordherstel, uitnodigingen, boekingsbevestigingen en facturen stoppen - en waarvan blokkering het vaakst automatisch gebeurt. Een golf bounces nadat een klant een oude adreslijst importeert, kan de misbruikbeveiliging van een aanbieder activeren en het versturen voor het hele account stilzetten.

Voorbereiding die zichzelf terugbetaalt:

- **Versturen via uw eigen domein**, met SPF, DKIM en DMARC ingericht, zoals het artikel over transactionele e-mail in extra-11 beschrijft - zodat de reputatie bij uw domein hoort in plaats van bij de aanbieder.
- **Een tweede aanbieder ingericht en geverifieerd**, met DKIM-records voor beide in DNS, en verzendcode achter een kleine interface zodat wisselen een configuratiewijziging is.
- **Automatische overschakeling** voor kritieke berichten - wachtwoordherstel, uitnodigingen - wanneer de primaire aanbieder fouten teruggeeft of het account is stilgezet.
- **Afhandeling van bounces en lijsthygiëne**, zodat imports van oude adressen de reputatie überhaupt niet beschadigen.

## Betalingen

Betaalproviders veroorzaken de lastigste lock-in, omdat veel van wat ze bewaren niet zomaar te exporteren is.

**Kaartgegevens** worden voor PCI-compliance door de provider opgeslagen. Opgeslagen kaarten verhuizen naar een andere provider is mogelijk via een overdracht tussen providers onder de PCI-regels, maar het kost weken, vereist de medewerking van beide providers en is niet voor elke combinatie beschikbaar.

**SEPA-incassomachtigingen** zijn afspraken tussen uw klant en uw bedrijf, maar de kenmerken en gegevens van de machtiging staan bij de provider. Ze verhuizen vereist dat de machtigingsgegevens worden geëxporteerd en door de nieuwe provider worden geaccepteerd; plan het in plaats van het aan te nemen.

**Geschiedenis van klanten, abonnementen en facturen** kan meestal worden geëxporteerd, en hoort ook in uw eigen database te staan, zoals het afstemmingsartikel in deze reeks betoogt.

Voorbereiding: sla de betaaltoestand op in uw eigen tabellen met de ID's van de provider als verwijzing in plaats van als primaire sleutel; houd uw eigen factuurrecords bij; ken het proces van de provider voor dataportabiliteit voordat u het nodig hebt; en lees de voorwaarden voor beëindiging en het teruggeven van data. Voor een product waarin betalingen centraal staan, is het kennen van de realistische overstaptijd - vaak één tot drie maanden - het echte exitplan.

## AI-modellen

AI-aanbieders veranderen prijzen, faseren modellen uit, passen gebruiksbeleid aan en hebben vaker storingen dan de meeste andere diensten. Van alle afhankelijkheden zijn ze zowel technisch het makkelijkst te wisselen als het makkelijkst slecht te wisselen.

**Zet modelaanroepen achter uw eigen interface** - één module die een taak aanneemt en een resultaat teruggeeft, met de aanbieder en het model als configuratie. Aanroepen verspreid door de codebase met aanbiederspecifieke parameters zijn wat wisselen traag maakt.

**Houd prompts en schema's voor gestructureerde uitvoer waar mogelijk aanbiederneutraal**, en bewaar ze in de repository.

**Evalueer een alternatief voordat u het nodig hebt.** De evaluatieset uit het artikel over het beoordelen van AI-uitvoer in deze reeks laat u een tweede aanbieder in uren testen en precies weten waar die beter of slechter is. Zonder evaluatieset is wisselen van aanbieder een gok op kwaliteit.

**Overweeg een ingerichte terugval** voor kritieke functies, automatisch gebruikt wanneer de primaire aanbieder niet beschikbaar is.

## Domeinen, DNS en Accounts

De minst technische lock-in is vaak de gevaarlijkste: toegang.

Een domein geregistreerd op het persoonlijke account van een voormalige medeoprichter, een DNS-aanbieder waarop maar één persoon kan inloggen, een hostingaccount gekoppeld aan een persoonlijk e-mailadres, tweefactorauthenticatie op de telefoon van iemand die is vertrokken. Geen van deze verschijnt in architectuurdiagrammen; elk ervan kan het product offline halen of onmogelijk maken om te veranderen.

Breng elk account onder eigendom van het bedrijf: registraties op naam van het bedrijf, logins in een gedeelde wachtwoordmanager die het bedrijf beheert, tweefactorauthenticatie op apparaten van het bedrijf of met veilig opgeslagen herstelcodes, en minstens twee mensen met toegang tot elke kritieke dienst. Verlengingsherinneringen horen naar een gedeeld adres te gaan dat wordt gelezen. Het overdrachtsartikel in deze reeks beschrijft hoe dit misgaat wanneer het wordt uitgesteld totdat iemand vertrekt.

## Contracten, Prijzen en Opzegtermijnen

Technische voorbereiding is de helft van een exitplan. De andere helft is weten wat de afspraken toestaan.

Leg voor elke belangrijke dienst vier dingen uit de voorwaarden vast: hoeveel aankondiging de dienst moet geven voordat prijzen of voorwaarden veranderen, hoe snel u kunt vertrekken en of er minimale verplichtingen gelden, wat er na beëindiging met uw data gebeurt en hoe lang u nog kunt exporteren, en onder welke voorwaarden de aanbieder uw account mag blokkeren. Deze antwoorden bepalen hoeveel tijd een exitplan werkelijk heeft - een aanbieder die prijzen met dertig dagen aankondiging kan wijzigen, geeft u dertig dagen, hoe goed u technisch ook bent voorbereid.

Twee gewoonten helpen. Lees wijzigingsberichten van kritieke aanbieders in plaats van ze te archiveren, en voeg een regel toe aan het overzicht wanneer voorwaarden veranderen. En wanneer een dienst belangrijk genoeg wordt - meestal wanneer de kosten of de rol in het product groeien - overweeg dan of een zakelijk abonnement met een contract, een vaste accountmanager en vastgelegde opzegtermijnen meer waard is dan het prijsverschil. Voor een leverancier waarvan uw klanten indirect afhankelijk zijn, zijn voorspelbare voorwaarden vaak de waardevolste functie die er is.

## Abstractie Waar Het Goedkoop Is, Niet Overal

Een gangbare overreactie op lock-in is elke dienst in een abstractie te verpakken "voor het geval we wisselen". Dat voegt code toe, verbergt nuttige functies van de dienst, en is meestal verspild: van de meeste diensten gaat u nooit weg.

Abstraheer waar wisselen waarschijnlijk is en de kosten laag zijn - e-mail versturen, AI-modelaanroepen, toegang tot bestandsopslag, aanroepen naar de betaalprovider - met een dunne interface in één module. Abstraheer niet de querytaal van de database, het frontendframework of de authenticatieflow op speculatie. Gebruik de sterke punten van de diensten, en houd de data die u nodig zou hebben in een overdraagbare vorm.

## Concentratie en de Vragen van Klanten

Naarmate het product groeit, gelden nog twee overwegingen.

**Concentratierisico.** Draaien hosting, database, opslag, authenticatie en functies allemaal op één platform, dan raakt één incident of blokkade van dat platform alles. Dat is vaak een acceptabele ruil voor eenvoud; het moet een bewuste ruil zijn, met back-ups die elders staan.

**Klanten zullen ernaar vragen.** Inkoopvragenlijsten bevatten steeds vaker vragen over bedrijfscontinuïteit: wat er gebeurt als een kritieke leverancier faalt, waar back-ups staan, hoe lang herstel zou duren, en soms of broncode-escrow beschikbaar is. Het overzicht en de exitplannen zijn de basis voor eerlijke antwoorden - en "we exporteren de database elke nacht naar een tweede aanbieder en hebben een herstel getest" is een beter antwoord dan welke geruststelling ook.

## Bekijk Het Eens per Jaar

Exitplannen verouderen naarmate diensten veranderen. Bekijk eens per jaar - of wanneer een dienst prijzen verhoogt of voorwaarden wijzigt - het overzicht en doe een korte oefening: kies één kritieke dienst en vraag: "Als die morgen verdween, wat zouden we doen in het eerste uur, de eerste dag en de eerste week?" Loop het door met degene die het werk zou doen. De gaten die verschijnen, zijn de voorbereiding voor het komende jaar.

## Dit Inrichten

Voor een Lovable- of Supabase-product is dit doorgaans drie tot vijf dagen: een overzicht van elke externe dienst met doel, accounteigenaar, data, kosten, voorwaarden, regio en soort lock-in, een kort exitplan per belangrijke dienst met aanleidingen, data-export, alternatieven, moeite en voorbereiding, code gesynchroniseerd naar een repository van het bedrijf, regelmatige versleutelde database-exports naar opslag bij een andere aanbieder met een getest herstel, verwijzingen naar gebruikers ontworpen voor overdraagbare authenticatie, transactionele e-mail op uw eigen domein met een tweede geverifieerde aanbieder en overschakeling voor kritieke berichten, betaaltoestand en facturen in uw eigen database met het portabiliteitsproces van de provider gedocumenteerd, AI-aanroepen achter een aanbiederneutrale interface met een geëvalueerd alternatief, elk account en domein onder eigendom van het bedrijf met gedeelde toegang, contractvoorwaarden vastgelegd, dunne abstracties alleen waar wisselen waarschijnlijk is, en een jaarlijkse review met een oefening.

LaunchStudio doet dit als onderdeel van het maken van een product waarop een bedrijf kan bouwen. Daarachter staat Manifera - elf jaar, 160+ projecten, 120+ engineers, met continuïteitsplanning voor klanten waaronder Vodafone, TNO en CFLW.

[Vraag ons welke van uw diensten het meest pijn zou doen om te verliezen](https://launchstudio.eu/nl/#contact).

## Echt voorbeeld

### Twee Dagen Zonder E-mail

Monique van Dam bouwde Baanreservering in Lovable: baanreserveringen, lidmaatschappen en betalingen voor padel- en tennisclubs, gebruikt door 70 clubs met zo'n 26.000 leden.

Eén club importeerde een ledenlijst uit een oud systeem met enkele duizenden verouderde e-mailadressen. De welkomstmails kwamen massaal terug, en de automatische misbruikbeveiliging van de e-mailaanbieder zette het versturen voor het hele account van Monique stil. Twee dagen lang verstuurde geen enkele club iets: geen boekingsbevestigingen, geen wachtwoordherstel, geen uitnodigingen voor nieuwe leden. Er was geen tweede aanbieder, en er een toevoegen betekende onder druk DNS-records en code aanpassen.

Toen ze naging wat er nog meer op dezelfde manier kon falen, vond ze meer. De AI-aanbieder achter de automatische wedstrijdplanning van het product had een prijsverhoging aangekondigd die die kosten ongeveer zou verdrievoudigen. Het Lovable-project was gekoppeld aan haar persoonlijke account in plaats van dat van het bedrijf. En het domein van het product stond geregistreerd op het persoonlijke account van een medeoprichter die het bedrijf een jaar eerder had verlaten.

Vier werkdagen: een overzicht van 14 externe diensten met eigenaars, data, kosten, voorwaarden en soort lock-in; een exitplan van één pagina voor elke dienst, met volledige voorbereiding voor de vijf kritieke; een tweede e-mailaanbieder geverifieerd op het domein van het product met DKIM voor beide, versturen achter een kleine interface, en automatische overschakeling voor bevestigingen, wachtwoordherstel en uitnodigingen; afhandeling van bounces en controle van geïmporteerde adressen vóór het versturen; AI-aanroepen verplaatst naar een aanbiederneutrale module, met een alternatieve aanbieder geëvalueerd tegen de evaluatieset voor de planning; elke nacht versleutelde database-exports naar object storage bij een andere aanbieder, met een getest herstel; de code gesynchroniseerd naar een Git-repository van het bedrijf en het Lovable-project overgezet naar het bedrijfsaccount; het domein met medewerking van de voormalige medeoprichter overgedragen aan het bedrijf, en elke kritieke login verplaatst naar een gedeelde wachtwoordmanager van het bedrijf met twee mensen per dienst; en een jaarlijkse review in de agenda.

**Resultaat:** vijf maanden later had de primaire e-mailaanbieder een regionale storing; de overschakeling zette kritieke berichten binnen minuten over naar de tweede aanbieder en clubs merkten niets. De AI-wissel, vooraf getest, werd in twee dagen gemaakt en verlaagde die kosten met ongeveer 40% ten opzichte van de oorspronkelijke prijs. Toen een groep clubs tijdens een inkoopproces naar bedrijfscontinuïteit vroeg, beantwoordden de exitplannen elke vraag.

> *"De oude mailinglijst van één club zette onze e-mail voor alle clubs twee dagen stil. Toen ik verder zocht, bleek dat ik niet eens eigenaar was van ons domein - iemand die het bedrijf had verlaten, was dat."*
> - **Monique van Dam, Oprichter, Baanreservering (Eindhoven)**

**Kosten & Doorlooptijd:** €3.800 (overzicht van diensten, exitplannen voor 14 diensten, tweede e-mailaanbieder met overschakeling en afhandeling van bounces, aanbiederneutrale AI-module met geëvalueerd alternatief, database-exports buiten het platform met getest herstel, eigendom van repository en accounts, domeinoverdracht, gedeelde toegang, jaarlijkse review) - afgerond in 4 werkdagen.

## Veelgestelde vragen

### Wat is vendor lock-in voor een AI-gebouwd product?

Afhankelijk zijn van een dienst op een manier die vertrekken traag of duur maakt - door de data die ze bevat, de code die haar aanroept, de ID's die uw systeem gebruikt, de reputatie die ze bezit, contractvoorwaarden, of toegang die aan één persoon is gekoppeld.

### Heb ik voor elke dienst een exitplan nodig?

Een kort plan voor elke belangrijke dienst, en echte voorbereiding voor de paar kritieke - meestal de coderepository, database, e-mail, betalingen, AI-aanbieder en het domein.

### Hoe maak ik mijn Supabase-data overdraagbaar?

Maak regelmatig versleutelde Postgres-exports naar opslag bij een andere aanbieder, test een herstel, weet welke functies specifiek zijn voor Supabase, en verwijs naar gebruikers op een manier die authenticatie laat verhuizen met behoud van wachtwoordhashes.

### Moet ik elke dienst in een abstractielaag verpakken?

Nee. Abstraheer alleen waar wisselen waarschijnlijk en goedkoop is - e-mail, AI-aanroepen, bestandsopslag, betaalaanroepen. Gebruik de dienst elders volledig en houd uw data overdraagbaar.

### Wat vragen klanten over afhankelijkheden van leveranciers?

Hoe het falen van kritieke leveranciers wordt opgevangen, waar back-ups staan, hoe lang herstel duurt, en soms broncode-escrow. Een overzicht en geteste exitplannen geven eerlijke antwoorden.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is vendor lock-in voor een AI-gebouwde SaaS?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Afhankelijkheid van een dienst via data, code, identificatoren, reputatie, contracten of toegang, waardoor vertrekken traag of duur is."
      }
    },
    {
      "@type": "Question",
      "name": "Heeft elke dienst een exitplan nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een kort plan voor elke belangrijke dienst, met echte voorbereiding voor kritieke diensten zoals code, database, e-mail, betalingen, AI en domein."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe blijft Supabase-data overdraagbaar?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Met regelmatige versleutelde Postgres-exports naar een andere aanbieder met geteste herstels, kennis van Supabase-specifieke functies, en overdraagbare verwijzingen naar gebruikers."
      }
    },
    {
      "@type": "Question",
      "name": "Moet elke externe dienst worden geabstraheerd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee - alleen waar wisselen waarschijnlijk en goedkoop is, zoals e-mail, AI-aanroepen, opslag en betaalaanroepen."
      }
    },
    {
      "@type": "Question",
      "name": "Welke continuïteitsvragen stellen B2B-klanten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hoe het falen van leveranciers wordt opgevangen, waar back-ups staan, hersteltijden, en soms broncode-escrow."
      }
    }
  ]
}
</script>
