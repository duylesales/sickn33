---
Titel: "Lovable-integraties: Exact Online en Moneybird Koppelen"
Trefwoorden: lovable integraties, Exact Online API, Moneybird API, boekhoudkoppeling, OAuth refresh tokens, btw-codes, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Lovable-integraties: Exact Online en Moneybird Koppelen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable-integraties: Exact Online en Moneybird Koppelen",
  "description": "De koppeling waar Nederlandse B2B-klanten het vaakst om vragen, is die met hun boekhoudpakket. Welke kant wat beheert, grootboekrekeningen en btw-codes koppelen, OAuth-tokens die roteren, dubbele boekingen voorkomen, synchronisatiestatus die klanten kunnen zien, en wanneer een unified accounting API de betere keuze is.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-integrations-connecting-exact-online-and-moneybird" }
}
</script>

Vraag een Nederlandse B2B-klant wat uw product onmisbaar zou maken, en een groot deel zegt hetzelfde: "Als het met ons boekhoudpakket zou praten." Facturen die twee keer worden ingevoerd - één keer in uw product en één keer in Exact Online of Moneybird - zijn de meest voorkomende handmatige taak van uw klanten, en de meest voorkomende reden waarom een boekhouder zich tegen een nieuwe tool verzet.

De koppeling lijkt eenvoudig in een demonstratie: account verbinden, factuur versturen, zien dat ze verschijnt. AI-tools kunnen dat in een middag opleveren. Wat ze opleveren, overleeft zelden een maand echt gebruik. Tokens verlopen en de koppeling stopt stil. Een time-out stuurt dezelfde factuur twee keer. Een vastgecodeerde btw-code boekt omzet op de verkeerde plek in de helft van de administraties van uw klanten. En niemand kan zien welke facturen zijn aangekomen en welke niet, dus de boekhouder verliest het vertrouwen in de koppeling en gaat weer typen.

Dit artikel behandelt hoe u een boekhoudkoppeling bouwt die boekhouders vertrouwen: de beslissingen die u vóór het schrijven van code neemt, het koppelen dat per klant verschilt, de omgang met tokens die de verbinding in leven houdt, het voorkomen van duplicaten, zichtbaarheid, en wanneer u inkoopt in plaats van bouwt.

## Het Landschap

De Nederlandse markt voor boekhouding in het mkb is geconcentreerd in een handvol pakketten.

**Exact Online** - het grootste, door veel accountantskantoren gebruikt namens hun klanten, met een uitgebreide REST API rond divisies (administraties), relaties, verkoopboekingen en verkoopfacturen.

**Moneybird** - populair bij zzp'ers en kleine bedrijven, met een schone moderne API rond administraties, contacten en verkoopfacturen.

**Twinfield, SnelStart, e-Boekhouden.nl, AFAS** - elk belangrijk in bepaalde segmenten, elk met een eigen API en eigen conventies.

Begin met het pakket dat de meeste van uw klanten gebruiken - vraag het hun in plaats van te gokken - en ontwerp de koppeling zo dat een tweede pakket kan worden toegevoegd zonder het eerste te herschrijven. De meeste producten hebben er binnen een jaar twee nodig.

## Beslis Wie Wat Beheert

De belangrijkste beslissingen worden genomen vóór er code is, en AI-gegenereerde koppelingen slaan ze volledig over.

**Wie beheert de factuurnummering?** Ofwel geeft uw product de factuur uit met een eigen nummer en stuurt het haar als boeking naar het boekhoudpakket, ofwel geeft het boekhoudpakket de factuur uit en maakt uw product haar daar aan. Beide zijn geldig; ze mengen levert twee nummerreeksen op en een boekhouder die niets meer kan afstemmen. Voor producten die zelf facturen maken en versturen - met eigen pdf's, zoals het artikel over documentgeneratie in deze reeks beschrijft - is het gebruikelijke antwoord dat uw product de nummering beheert en een verkoopboeking of factuur doorstuurt met uw nummer als referentie.

**Wie beheert klanten?** Wordt er bij een nieuwe klant in uw product een relatie in Exact aangemaakt? Verandert een adres in uw product wanneer het in Exact verandert? Kies per veld een richting, anders overschrijven de twee systemen elkaar.

**Wie beheert de betaalstatus?** Betalingen komen meestal binnen op de bankrekening die het boekhoudpakket inleest. Moet uw product tonen of een factuur is betaald, dan komt de status uit het boekhoudpakket - via periodiek opvragen of een webhook - niet uit een gok.

**Wat gebeurt er nadat een factuur naar de boekhouding is gestuurd?** Meestal moet ze in uw product worden vergrendeld. Een factuur bewerken die al is geboekt, levert een verschil op dat alleen een creditnota kan oplossen, zoals het artikel over terugbetalingen in deze reeks beschrijft.

Schrijf deze beslissingen op, toon ze in de koppelingsinstellingen, en leg ze aan klanten uit. "Facturen worden in [Product] gemaakt en in Exact geboekt als verkoopboekingen; betalingen worden elk uur uit Exact teruggelezen" beantwoordt de meeste vragen van een boekhouder voordat hij ze stelt.

## Koppelen Is Per Klant

De tweede fout van gegenereerde koppelingen: ze gaan ervan uit dat elke administratie op dezelfde manier is ingericht. Dat is niet zo.

**Grootboekrekeningen.** Omzet uit diensten kan in de ene administratie 8000 zijn, in een andere 8100, en in een derde verdeeld over drie rekeningen per productlijn. Uw product moet elke organisatie haar omzetcategorieën laten koppelen aan haar eigen grootboekrekeningen.

**Btw-codes.** In Exact worden btw-codes per administratie ingericht, en de code voor "21% hoog tarief" is niet overal dezelfde. Een vastgecodeerde btw-code boekt in sommige administraties de btw verkeerd en faalt in andere. Haal de beschikbare btw-codes via de API op uit de administratie van de klant, laat de klant elk van uw btw-tarieven - 21%, 9%, 0%, verlegd, intracommunautair - aan een van de zijne koppelen, en controleer de koppeling vóór de eerste synchronisatie.

**Dagboeken en kostenplaatsen.** Het verkoopdagboek waarin wordt geboekt, en eventueel kostenplaatsen of projecten, verschillen ook per administratie.

**Divisies en administraties.** Een Exact-login van een accountantskantoor kan tientallen klantadministraties zien. De klant moet kiezen naar welke divisie de koppeling schrijft, en de koppeling mag nooit naar een andere schrijven.

Bouw een koppelscherm dat de echte lijsten - grootboekrekeningen, btw-codes, dagboeken - uit de gekoppelde administratie laadt en de keuzes van de klant opslaat. Controleer het vóór activering en opnieuw wanneer een synchronisatie faalt omdat een gekoppelde code niet meer bestaat.

## OAuth-tokens Die in Leven Blijven

Zowel Exact Online als Moneybird gebruikt OAuth 2.0: de klant logt in bij zijn boekhoudpakket, geeft toestemming, en uw product ontvangt een access token en een refresh token. Dit is het deel van de koppeling dat het vaakst in productie breekt.

**Sla tokens versleuteld op, per organisatie.** Refresh tokens zijn langlevende inloggegevens voor de volledige boekhouding van een klant. Versleutel ze in rust, toon ze nooit aan de browser, en houd ze uit logs. De artikelen over geheimen in deze reeks gelden volledig.

**Vernieuw vóór het verlopen, niet na een mislukking.** Access tokens van Exact zijn kortlevend - minuten in plaats van uren. Vernieuw ze kort voordat ze verlopen in plaats van te wachten tot een verzoek faalt.

**Ga om met roterende refresh tokens.** Wanneer een refresh token wordt gebruikt, geeft Exact een nieuwe uit en werkt de oude niet meer. Vernieuwen twee processen tegelijk - een geplande synchronisatie en een actie van een gebruiker, of twee workers - dan slaagt de een, gebruikt de ander een inmiddels ongeldig token, en kan afhankelijk van de timing het opgeslagen token het ongeldige zijn. De koppeling is dan verbroken totdat de klant opnieuw toestemming geeft. Dit is de meest voorkomende reden waarom Exact-koppelingen "willekeurig verbroken worden".

De oplossing is vernieuwingen per organisatie achter elkaar uit te voeren:

```sql
-- binnen een transactie in de worker
select pg_advisory_xact_lock(hashtext('exact-token:' || :organisation_id));
-- lees de tokenrij opnieuw; heeft een ander proces al vernieuwd, gebruik dan het nieuwe token
-- anders vernieuwen, nieuwe access en refresh token opslaan, en committen
```

**Herken een dode koppeling en zeg het.** Wanneer vernieuwen definitief faalt - de klant heeft toegang ingetrokken, de gebruiker die koppelde heeft zijn kantoor verlaten - markeer de koppeling dan als verbroken, stop met synchroniseren, en meld het aan de beheerder van de klant in het product en per e-mail. Een koppeling die drie weken stil faalt, levert drie weken ontbrekende boekingen op.

**Koppel waar mogelijk met een functieaccount.** Is de koppeling verbonden aan de persoonlijke Exact-login van één medewerker, dan breekt ze wanneer die vertrekt. Adviseer klanten te koppelen met een account dat bij de functie hoort in plaats van bij de persoon.

## Boek Nooit Dezelfde Factuur Twee Keer

Een verzoek om een factuur aan te maken in het boekhoudpakket kan een time-out geven nadat het pakket haar al heeft aangemaakt. Probeer naïef opnieuw en de factuur bestaat twee keer. Boekhouders zien duplicaten snel, en weinig dingen vernietigen het vertrouwen in een koppeling sneller.

Drie maatregelen voorkomen het.

**Een outbox per organisatie.** In plaats van de API aan te roepen binnen de actie van de gebruiker, schrijft u een synchronisatietaak - "stuur factuur 2028-0142 naar Exact" - naar een tabel, en laat u een worker die verwerken, zoals het artikel over achtergrondwerk in deze reeks beschrijft. De actie van de gebruiker wacht nooit op het boekhoudpakket.

**Sla het externe ID op.** Wanneer het aanmaken slaagt, slaat u het ID dat het boekhoudpakket teruggaf op bij uw factuurrecord. Een taak voor een factuur die al een extern ID heeft, wordt niet opnieuw uitgevoerd.

**Controleer vóór het aanmaken bij een nieuwe poging.** Heeft een eerdere poging een time-out gegeven zonder antwoord, zoek dan in het boekhoudpakket naar een factuur met uw referentie - uw factuurnummer in het referentieveld - voordat u een nieuwe aanmaakt. Zowel Exact als Moneybird laat u een eigen referentie opslaan en daarop filteren.

```ts
const existing = await exact.findSalesEntry({ division, yourRef: invoice.number });
if (existing) return markSynced(invoice, existing.id);
const created = await exact.createSalesEntry(division, mapInvoice(invoice, mapping));
await markSynced(invoice, created.id);
```

## Klanten Koppelen aan Relaties

Elke boeking verwijst naar een relatie - de debiteur in het boekhoudpakket. Dit verkeerd doen levert de tweede meest voorkomende klacht op na dubbele facturen: dubbele relaties.

De naïeve aanpak maakt in Exact een nieuwe relatie aan voor elke klant in uw product, de eerste keer dat er een factuur wordt verstuurd. In een administratie die die klant al bevat - jaren geleden door de boekhouder ingevoerd, met een eigen debiteurnummer en betaalgeschiedenis - is het resultaat twee debiteuren voor één bedrijf, met facturen verdeeld over beide en een openstaand saldo dat niemand kan lezen.

Zoek een match voordat u aanmaakt. Wanneer een klant in uw product voor het eerst wordt gesynchroniseerd, zoek dan in de administratie naar een bestaande relatie op de betrouwbaarste beschikbare identificator: het KvK-nummer, dan het btw-nummer, dan een exacte match op naam en postcode. Wordt er precies één match gevonden, koppel die dan en sla het relatie-ID op. Worden er meerdere gevonden, of is de match onzeker, vraag de beheerder van de klant dan te kiezen in de koppelingsinstellingen in plaats van te gokken. Maak alleen een nieuwe relatie aan wanneer niets overeenkomt.

Eenmaal gekoppeld slaat u het externe relatie-ID op bij uw klantrecord en gebruikt u het voor elke volgende boeking. Beslis welk systeem adres- en contactgegevens beheert - meestal het boekhoudpakket, omdat de boekhouder ze daar bijhoudt - en vermijd wijzigingen in beide richtingen te schrijven, wat een eindeloze cyclus van kleine overschrijvingen oplevert.

Hetzelfde principe geldt voor artikelen en producten als u factuurregels boekt op artikelen in het boekhoudpakket: match op artikelcode, koppel, sla het ID op, en maak nooit stil iets aan.

## Limieten en Volume

Boekhoud-API's beperken hoeveel aanroepen u mag doen. Exact Online hanteert limieten per minuut en per dag voor elke bedrijfskoppeling; Moneybird hanteert eigen limieten. Een run aan het einde van de maand die vierhonderd facturen voor één klant in een strakke lus doorstuurt, loopt tegen de limiet aan, en gegenereerde code behandelt de resulterende fout vaak als definitieve mislukking.

Respecteer de limieten bewust: verwerk de wachtrij van elke organisatie in een beheerst tempo, lees de limietheaders die de API teruggeeft, wacht wanneer dat wordt gevraagd, en spreid bulkwerk over de tijd. Bundel waar de API dat toestaat. En cache wat zelden verandert - grootboekrekeningen, btw-codes, dagboeken - in plaats van het vóór elke boeking op te halen.

## Toon de Synchronisatiestatus aan de Klant

De koppeling wordt alleen vertrouwd als de boekhouder kan zien wat er gebeurde. Elke factuur in uw product moet haar synchronisatiestatus tonen: nog niet verstuurd, in de wachtrij, geboekt in Exact met een link, of mislukt met een reden waarop de klant kan handelen.

"Mislukt: btw-code 4 bestaat niet in administratie 'Bakker Schoonmaak B.V.' - pas de btw-koppeling aan in Instellingen → Exact" is een melding die een klant in twee minuten oplost. "Error 400" is een melding die een supportticket wordt, dan een telefoontje, dan een reden om op te zeggen.

Voeg per organisatie een synchronisatieoverzicht toe - de laatste geslaagde synchronisatie, het aantal openstaande en mislukte items, en een knop om mislukte items opnieuw te proberen zodra de oorzaak is opgelost - en een waarschuwing aan uzelf wanneer de mislukkingen van een organisatie een drempel overschrijden.

## Stem Regelmatig Af

Zelfs met al het bovenstaande lopen twee systemen uit elkaar: een factuur die een boekhouder in Exact verwijderde, een boeking die met de hand is aangepast, een synchronisatie die mislukte en nooit opnieuw werd geprobeerd. Het afstemmingsartikel in deze reeks beschrijft het principe voor betaalproviders; het geldt hier evengoed.

Vergelijk eens per week of eens per maand: facturen in uw product over de periode, met hun bedragen, tegenover boekingen in het boekhoudpakket met uw referentie. Maak een lijst van wat ontbreekt, wat dubbel is en wat in bedrag verschilt. Toon het resultaat aan de beheerder van de klant, of in elk geval aan uzelf. Het maakt van stil uit elkaar lopen een korte lijst die iemand kan oplossen.

## Bouwen of Inkopen

Rechtstreeks bouwen tegen elke boekhoud-API geeft u volledige controle en geen kosten per koppeling. Het betekent ook dat u OAuth, limieten, koppelingen en eigenaardigheden voor elk pakket dat uw klanten gebruiken apart implementeert.

**Unified accounting API's** - diensten die één API bieden over veel boekhoudpakketten, waaronder Europese met goede dekking van Nederlandse software zoals Chift, naast andere zoals Codat en Apideck - regelen koppelingen, tokenvernieuwing en veel van de verschillen tussen pakketten. Ze rekenen per koppeling en worden een subverwerker van de financiële data die erdoorheen gaat, wat in uw lijst van subverwerkers en verwerkersovereenkomsten hoort, zoals het artikel over subverwerkers in deze reeks beschrijft.

De gebruikelijke beslissing: bouw rechtstreeks als bijna alle klanten één pakket gebruiken en die koppeling centraal staat in uw product; gebruik een unified API als klanten over vier of vijf pakketten verspreid zijn, of als de boekhoudkoppeling nuttig is maar niet de kern. Houd hoe dan ook uw eigen outbox, koppelingen en synchronisatiestatus - die zijn de verantwoordelijkheid van uw product, wie de verbinding ook regelt.

## Registratie, Partners en Testomgevingen

Exact Online vereist dat apps in het App Center worden geregistreerd voordat ze kunnen koppelen, en uw koppeling openbaar vermelden gaat gepaard met een beoordeling. Moneybird heeft een ontwikkelaarsprogramma en testadministraties. Houd hier rekening mee: registratie kost tijd, en tijdens de ontwikkeling echte klantadministraties koppelen is hoe testboekingen in iemands grootboek belanden.

Ontwikkel en test tegen sandbox- of testadministraties. Houd productie- en testgegevens gescheiden, zoals het artikel over omgevingsvariabelen in deze reeks beschrijft, en laat een ontwikkelomgeving nooit naar de echte administratie van een klant wijzen.

## Dit Inrichten

Voor een Lovable-product dat een boekhoudkoppeling toevoegt, is dit doorgaans vier tot zes dagen voor het eerste pakket: beslissingen over eigenaarschap opgeschreven voor nummering, klanten, betaalstatus en bewerken na synchronisatie; een koppelscherm per organisatie dat echte grootboekrekeningen, btw-codes, dagboeken en divisies uit de gekoppelde administratie laadt en keuzes controleert; klanten gekoppeld aan bestaande relaties op KvK-nummer of btw-nummer voordat er iets wordt aangemaakt; OAuth-tokens versleuteld in rust, vernieuwd vóór het verlopen en per organisatie achter elkaar uitgevoerd om rotatie te overleven; verbroken koppelingen herkend en gemeld; een outbox met externe ID's en referentiezoekacties om duplicaten te voorkomen; verwerking binnen de limieten met wachttijden en gecachete referentiedata; synchronisatiestatus per factuur met bruikbare fouten en een overzicht per organisatie; geplande afstemming; facturen vergrendeld na boeking; en ontwikkeling tegen testadministraties. Een tweede pakket kost twee tot drie dagen op hetzelfde fundament.

LaunchStudio bouwt en repareert boekhoudkoppelingen voor producten waarvan de klanten in Exact en Moneybird werken. Daarachter staat Manifera - elf jaar, 160+ projecten, 120+ engineers, vanaf de Herengracht 420 in Amsterdam.

[Vertel ons welk boekhoudpakket uw klanten gebruiken](https://launchstudio.eu/nl/#contact) en wij vertellen u wat een betrouwbare koppeling inhoudt.

## Echt voorbeeld

### Driehonderdtwaalf Dubbele Facturen

Iris Meijer bouwde Schoonmaakplanner in Lovable: planning, urenregistratie en facturatie voor schoonmaakbedrijven in de zakelijke markt, gebruikt door 44 bedrijven.

De koppeling met Exact Online was in een middag gegenereerd en werkte goed in de demonstratie. In productie had ze drie problemen. Ongeveer één keer per week brak de koppeling van een klant en moest er opnieuw toestemming worden gegeven, omdat de nachtelijke synchronisatie en een factuur die een gebruiker verstuurde af en toe op hetzelfde moment het token vernieuwden. Wanneer Exact traag reageerde, probeerde de koppeling het opnieuw, en werd de factuur twee keer aangemaakt. En elke boeking gebruikte btw-code "2", wat in de meeste administraties 21% betekende maar in de administraties van vier klanten - ingericht door verschillende accountantskantoren - iets anders.

De schade kwam aan het einde van een kwartaal aan het licht, toen de accountants van negen klanten 312 dubbele verkoopfacturen en een reeks verkeerd geboekte btw-bedragen in hun btw-aangiften vonden. Twee klanten zeiden dat ze zouden opzeggen als het niet werd opgelost.

Vier werkdagen: tokenvernieuwing per organisatie achter elkaar uitgevoerd met een advisory lock, tokens versleuteld in rust, en verbroken koppelingen herkend en gemeld aan de beheerder van de klant; een outbox met het Exact-ID bij elke factuur opgeslagen en een zoekactie op factuurnummer vóór elke nieuwe poging; een koppelscherm dat de btw-codes, omzetrekeningen en het verkoopdagboek van elke administratie via de API laadt, met controle vóór activering; verwerking binnen de limieten per organisatie; synchronisatiestatus op elke factuur met bruikbare foutmeldingen en een synchronisatieoverzicht per klant; facturen vergrendeld na boeking, met correcties als creditnota; een wekelijks afstemmingsrapport met ontbrekende, dubbele en afwijkende boekingen; en een gescripte lijst van de 312 duplicaten met hun Exact-ID's, zodat de accountants ze konden verwijderen.

**Resultaat:** de accountants verwijderden de duplicaten en corrigeerden de btw-boekingen binnen de aangiftetermijn van het kwartaal, en beide klanten die hadden gedreigd op te zeggen, bleven. In de zes maanden daarna waren er geen dubbele boekingen en geen verbroken koppelingen door tokens. Omdat de koppeling nu achter één connectorinterface zat, volgde een Moneybird-koppeling in drie dagen, en zes nieuwe klanten noemden in het kwartaal daarna de boekhoudkoppeling als reden om voor het product te kiezen.

> *"In de demo werkte het perfect. Drie maanden later vonden negen accountants driehonderdtwaalf facturen dubbel, en stonden in vier administraties onze btw-bedragen op de verkeerde code."*
> - **Iris Meijer, Oprichter, Schoonmaakplanner (Den Bosch)**

**Kosten & Doorlooptijd:** €4.600 (tokenvernieuwing achter elkaar en versleutelde opslag, outbox met idempotente boekingen, koppeling per administratie van btw-codes, grootboekrekeningen en dagboeken, synchronisatie binnen de limieten, zichtbare synchronisatiestatus, vergrendeling na boeking, wekelijkse afstemming, lijst voor het opruimen van duplicaten) - afgerond in 4 werkdagen.

## Veelgestelde vragen

### Met welke boekhoudpakketten moet een Nederlands B2B-product koppelen?

Begin met het pakket dat de meeste van uw klanten gebruiken - meestal Exact Online of Moneybird - en ontwerp voor een tweede. Twinfield, SnelStart, e-Boekhouden.nl en AFAS doen ertoe in bepaalde segmenten.

### Waarom worden Exact Online-koppelingen steeds verbroken?

Meestal omdat refresh tokens roteren en twee processen tegelijk vernieuwen, waardoor een ongeldig token wordt opgeslagen. Voer tokenvernieuwingen per organisatie achter elkaar uit en lees het token opnieuw voordat u vernieuwt.

### Hoe voorkom ik dubbele facturen in het boekhoudpakket?

Stuur boekingen via een outbox, sla het externe ID bij elke factuur op, en zoek vóór het opnieuw proberen van een verzoek met een time-out naar een bestaande boeking met uw factuurnummer als referentie.

### Mogen btw-codes worden vastgecodeerd?

Nee. Btw-codes verschillen per administratie. Laad ze uit de gekoppelde administratie en laat elke klant uw btw-tarieven aan zijn codes koppelen, gecontroleerd vóór de eerste synchronisatie.

### Moet ik een unified accounting API gebruiken?

Gebruiken uw klanten vier of vijf verschillende pakketten, of is de boekhoudkoppeling nuttig maar niet de kern, dan bespaart een unified API veel werk. Houd hoe dan ook uw eigen outbox, koppelingen en synchronisatiestatus.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Met welke boekhoudpakketten moet een Nederlandse SaaS koppelen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Begin met het pakket dat de meeste klanten gebruiken - meestal Exact Online of Moneybird - en ontwerp zo dat een tweede pakket kan worden toegevoegd."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom worden Exact Online-koppelingen verbroken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Roterende refresh tokens die gelijktijdig worden vernieuwd, laten een ongeldig token achter; voer vernieuwingen per organisatie achter elkaar uit."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom ik dubbele facturen in boekhoudsoftware?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Gebruik een outbox, sla het externe ID op, en zoek vóór een nieuwe poging naar bestaande boekingen op uw factuurreferentie."
      }
    },
    {
      "@type": "Question",
      "name": "Mag ik btw-codes vastcoderen in een boekhoudkoppeling?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee - btw-codes verschillen per administratie; laad ze via de API en laat elke klant uw tarieven aan zijn codes koppelen."
      }
    },
    {
      "@type": "Question",
      "name": "Wanneer gebruik ik een unified accounting API?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Wanneer klanten over meerdere pakketten verspreid zijn of de koppeling niet de kern is - met behoud van uw eigen outbox, koppelingen en synchronisatiestatus."
      }
    }
  ]
}
</script>
