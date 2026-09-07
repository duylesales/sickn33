---
Titel: "Uw Cursor-Codebase Werkt: Een Productiegereedheidscontrole Vóór U Begint te Verkopen"
Trefwoorden: Cursor codebase productie, AI code review checklist, indie hacker security audit, geheimen in git historie, productie gates, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Uw Cursor-Codebase Werkt: Een Productiegereedheidscontrole Vóór U Begint te Verkopen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Uw Cursor-Codebase Werkt: Een Productiegereedheidscontrole Vóór U Begint te Verkopen",
  "description": "Een gestructureerde audit met zeven gates voor een met Cursor gebouwde codebase die lokaal al vlekkeloos draait. Gericht op de specifieke blinde vlekken van AI-geassisteerde softwareontwikkeling in plaats van generieke adviezen.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/nl/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2027-01-08",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/uw-cursor-codebase-werkt-productiegereedheid-review-voor-de-verkoop"
  }
}
</script>

*"Is het klaar voor lancering?"*  
*"Het werkt. Ik gebruik het zelf al drie weken lang dagelijks."*  
*"Dat was niet wat ik vroeg."*  

Die dialoog — of een variant daarvan met een potentiële klant, een investeerder of de kritische helft van uw eigen brein — is het vertrekpunt van dit artikel. Een met behulp van Cursor gebouwde codebase is wezenlijk anders dan een exportbestand uit Lovable of Bolt. Het is een echte git-repository die u zelf heeft gelezen, vormgegeven en voorzien van uw eigen architectuurkeuzes. U bent geen toevallige toeschouwer. En dat is exact de reden waarom standaardadviezen ("AI-code bevat beveiligingsfouten!") voor u waardeloos zijn: dat weet u allang, en u weet evengoed dat uw code van een hoger niveau is dan dat cliché suggereert.

Hieronder vindt u daarom een reviewmethodiek opgebouwd uit zeven concrete controlepoorten (gates). Elke poort bevat een heldere succeseis, een praktisch controlecommando dat u vanavond zelf kunt uitvoeren en een realistische inschatting van de benodigde hersteltijd. Dit zijn faalmechanismen die specifiek optreden bij AI-geassisteerde ontwikkeling in een professionele repository — geen abstracte theorie, maar de typische gebreken die ontstaan wanneer een bekwame ontwikkelaar in hoog tempo ogenschijnlijk kloppende code accepteert.

## Poort 1 — Geheimen hebben de repository nooit geraakt

**Succeseis:** Er bevindt zich geen enkele API-sleutel, database-wachtwoord of privétoken in de git-geschiedenis, op geen enkele branch en in geen enkele build-bundel.

Het faalpatroon bij AI-tools is uiterst specifiek. U vroeg om een werkend codevoorbeeld; het taalmodel genereerde dit met de API-sleutel direct in de code "voorlopig"; u was van plan deze naar `.env` te verplaatsen, maar de git-commit was sneller dan uw geheugen. Of het `.env`-bestand werd in een vroeg stadium per ongeluk gecommit voordat `.gitignore` correct was ingesteld, waardoor het verwijderen uit de werkmap de sleutel alsnog permanent in de git-historie achterliet.

Voer deze drie checks uit in uw terminal:

```bash
git log --all --full-history -- .env .env.local
npx trufflehog git file://. --only-verified
npm run build && grep -rEo "sk_(live|test)_[A-Za-z0-9]+|service_role|AKIA[0-9A-Z]{16}" dist/ .next/ 2>/dev/null | sort -u
```

Komt er ook maar één geheim naar boven? Dan is intrekken en roteren bij de leverancier uw eerste prioriteit. Een sleutel in de git-historie moet als gecompromitteerd worden beschouwd — ongeacht of uw repository privé is — omdat deze aanwezig is in elke clone, elke CI/CD-pipeline en elk deployment-artefact. Bepaal daarna of het herschrijven van de git-geschiedenis met `git-filter-repo` noodzakelijk is; voor een soloproject is dat binnen een uur geregeld en absoluut de moeite waard.

**Benodigde hersteltijd:** 1 tot 3 uur, exclusief eventuele downstream afhankelijkheden van de ingetrokken sleutel.

## Poort 2 — Autorisatie wordt op exact één centrale plek beslist

**Succeseis:** U kunt direct de specifieke functie of beleidslaag aanwijzen die de vraag beantwoordt: "mag deze ingelogde gebruiker deze actie uitvoeren op dít specifieke record?", en elke afzonderlijke route loopt dwingend door die laag.

Dit is de poort waar de meeste Cursor-projecten op stranden, en wel om een zeer begrijpelijke reden: u heeft uw API-endpoints niet in één adem geschreven. U bouwde drie routes in één sessie, vier routes twee weken later, en het AI-model — dat geen actieve herinnering heeft aan de conventies van de eerdere sessie — genereerde voor de tweede lichting net een andere structuur. Nu controleert `/api/projects/[id]` het eigenaarschap inline, leunt `/api/documents/[id]` op een `requireOwner`-helper, en controleert `/api/exports/[id]` helemaal niets omdat die promptsessie uitsluitend ging over CSV-bestandsformattering.

Maak een inventarisatie. Lijst elke route op en noteer exact waar de autorisatiebeslissing plaatsvindt. De lijst zélf is de audit: de routes waar u moet zoeken en twijfelen, zijn precies de routes waar niemand eerder naar heeft omgekeken.

```bash
rg -n "export async function (GET|POST|PATCH|DELETE)" app/ --files-with-matches
rg -n "params\.(id|slug)" app/api/ -A6 | rg -v "userId|auth\(\)|requireOwner|session"
```

Let op: middleware is hier géén vervanging voor. Een `middleware.ts`-bestand dat paden afvangt, verifieert enkel of er een sessie bestaat; het kan onmogelijk weten of het opgevraagde database-record toebehoort aan die specifieke sessie. Wees bovendien alert op verouderde regex-matchers die ooit vier routes afdekten, maar geruisloos de twaalf routes negeren die u in de maanden daarna heeft toegevoegd.

**Benodigde hersteltijd:** 4 tot 12 uur, voornamelijk bestaande uit inventarisatie en consolidatie in plaats van ingewikkelde code.

## Poort 3 — De datalaag weigert ongeldige invoer zelfstandig

**Succeseis:** Ongeldige data kan onder geen beding in de database belanden, zelfs niet wanneer elke regel applicatiecode volledig wordt omzeild.

Door AI gegenereerde code heeft de sterke neiging om validatie uitsluitend aan de buitenrand uit te voeren — via een Zod-schema op de route handler — en vervolgens alle onderliggende bewerkingen blindelings te vertrouwen. Dat is een prima start, maar onvoldoende als eindstation. Zod valideert louter wat via die specifieke route binnenkomt. Het beschermt u niet tegen wat een achtergrondtaak, een seed-script, een handmatig SQL-commando of een toekomstig nieuw endpoint naar de database schrijft.

Controleer wat de database zélf afdwingt: `NOT NULL` op verplichte kolommen, `CHECK`-constraints op velden met een vast waardenbereik, `UNIQUE`-indices waar dubbele invoer bedrijfsschade veroorzaakt, en foreign keys met expliciet gedefinieerd `ON DELETE`-gedrag in plaats van de willekeurige standaardwaarde uit het migratiebestand. Controleer daarnaast of geldbedragen zijn opgeslagen als `numeric`/`decimal` en niet als floating-point getallen — elk prototype dat rekent met floats stuurt vroeg of laat een factuur van € 19,9999999 naar een klant.

Voer een gerichte controle uit op velden die geld of capaciteit vertegenwoordigen: zoek naar elke plek waar een waarde uit de request-body direct financiële impact heeft: prijzen, bestelaantallen, tegoeden, abonnementsvormen, gebruikersrollen en kortingspercentages. Elk van deze velden moet óf direct uit uw eigen database worden geladen, óf server-side worden geverifieerd tegen een betrouwbare bron. Een `price`-veld dat blindelings van de frontend wordt overgenomen is de oudste kwetsbaarheid in softwareland, en AI genereert dit aan de lopende band omdat het in een lokale demo prima werkt.

**Benodigde hersteltijd:** 3 tot 8 uur.

## Poort 4 — Databasestructuur is 100% reproduceerbaar vanuit de repository

**Succeseis:** Een nieuwe ontwikkelaar kan uw repository clonen, één enkel migratiecommando uitvoeren en beschikt over een database die qua structuur exact identiek is aan productie.

Het typische AI-antipatronen hierbij: het model stelt een net migratiebestand voor, u bekijkt het, het oogt correct, en vervolgens voert u de wijziging handmatig door via een database-dashboard of met een ad-hoc `ALTER TABLE`-commando omdat dat op dat moment sneller was. Twee maanden later beschrijft uw migratiemap een databasestructuur die weliswaar lijkt op uw live database, maar er op subtiele punten van afwijkt. Dergelijke afwijkingen blijven onzichtbaar totdat u een back-up moet terugzetten, een staging-omgeving wilt opzetten of een externe partij inschakelt.

Bij Prisma toont `prisma migrate diff --from-schema-datamodel --to-schema-datasource` de naakte waarheid. Bij Drizzle genereert u een migratie tegen de live database om te controleren of het diff-bestand leeg is. Bij Supabase gebruikt u `supabase db diff --linked`. Een leeg diff-resultaat betekent dat u geslaagd bent. Elk verschil dat naar voren komt, is een opsomming van de inconsistenties in uw codebase.

Controleer tegelijkertijd of er geautomatiseerde back-ups draaien én test het herstel daarvan. Een ongeteste back-up is louter een hoopgevende gedachte, geen operationele zekerheid. Het testen van een herstelprocedure vergt minder dan een halfuur.

**Benodigde hersteltijd:** 2 tot 6 uur om de structuur gelijk te trekken, plus een blijvende discipline in werkwijze.

## Poort 5 — Externe callbacks en webhooks zijn cryptografisch geauthenticeerd

**Succeseis:** Elke inkomende webhook verifieert de cryptografische handtekening en verwerkt elke unieke gebeurtenis gegarandeerd slechts éénmaal (idempotentie).

Stripe, Mollie, Clerk, Resend, GitHub — elke dienst die asynchroon statusberichten naar uw applicatie stuurt. Dit endpoint is noodgedwongen openbaar, wat betekent dat de handtekeningcontrole de enige barrière vormt tussen een legitieme transactie en een vervalst bericht. Door AI gegenereerde handlers vangen verificatiefouten regelmatig af in een try/catch-blok, loggen de foutmelding en gaan vervolgens doodleuk door met de bedrijfslogica — simpelweg omdat die constructie ervoor zorgt dat lokale tests slagen wanneer de webhook-secret ontbreekt.

Inspecteer uw webhook-code en beantwoord drie vragen:
1. Retourneert een handtekeningfout direct een HTTP 4xx-statuscode zonder dat er data wordt gewijzigd?
2. Wordt de ruwe (raw) request-body gecontroleerd in plaats van een opnieuw geserialiseerd JSON-object?
3. Wordt een herhaald event-ID herkend en genegeerd?

Betalingsproviders proberen mislukte webhooks automatisch opnieuw af te leveren. Een handler die niet idempotent is, zal vroeg of laat een tegoed tweemaal toekennen — en dat gebeurt steevast 's nachts om 03:00 uur tijdens een piekbelasting, niet op een rustige dinsdagmiddag.

Controleer daarnaast de functionele dekking. De meeste door AI gebouwde Stripe-koppelingen verwerken uitsluitend het 'happy flow'-scenario (`checkout.session.completed`). Annuleringen, mislukte incasso's en betwiste betalingen arriveren via afzonderlijke events; worden deze niet afgehandeld, dan blijft de gebruiker gratis toegang houden en raakt uw applicatiestatus permanent ontregeld.

**Benodigde hersteltijd:** 3 tot 6 uur per externe provider.

## Poort 6 — Dependencies zijn reëel, actueel en beperkt in aantal

**Succeseis:** Elk pakket in uw `package.json` heeft een duidelijke rechtvaardiging, verwijst naar een actief onderhouden open-source project en bevat geen bekende kritieke kwetsbaarheden.

Hier spelen twee AI-specifieke risico's. De eerste betreft gehallucineerde dependencies (package hallucination): taalmodellen stellen af en toe aannemelijk klinkende bibliotheeknamen voor die niet bestaan, en kwaadwillenden registreren in toenemende mate exact die namen op npm met kwaadaardige code. Elk pakket waarvan u zich niet herinnert waarom het is toegevoegd, verdient een controle op wekelijkse downloads, repository-activiteit en publicatiegeschiedenis.

Het tweede risico is sluipender: ongebreidelde wildgroei aan bibliotheken (dependency sprawl). Over tientallen Cursor-sessies heen greep het model naar `date-fns` in bestand A, `dayjs` in bestand B en `moment` in bestand C. Er zijn drie verschillende HTTP-clients geïnstalleerd en twee validatiebibliotheken. Er is functioneel niets kapot, maar uw bundle is nodeloos zwaar en uw potentiële aanvalsoppervlak is driemaal groter dan noodzakelijk.

Voer deze diagnostische commando's uit:

```bash
npm audit --omit=dev
npx depcheck
npm ls --all 2>/dev/null | wc -l
```

**Benodigde hersteltijd:** 2 tot 5 uur voor het opschonen en consolideren.

## Poort 7 — Fouten en storingen zijn direct observeerbaar

**Succeseis:** Wanneer er in productie iets misgaat, bent u de eerste die dit signaleert via geautomatiseerde monitoring, en verneemt u dit niet pas via een gefrustreerde klant.

Veel oprichters slaan deze poort over omdat het voelt als optionele afwerking. Dat is een gevaarlijke misvatting: het markeert het verschil tussen een bug die u een uurtje kost om te verhelpen, en een bug die u geruisloos elf klanten kost die zonder iets te zeggen vertrekken. De minimale productieset bestaat uit: foutmonitoring met geüploade source maps (het gratis niveau van Sentry volstaat ruimschoots), gestructureerde serverlogs die doorzoekbaar zijn op een uniek request-ID, een uptime-check die een specifiek functioneel endpoint aanroept in plaats van een statische homepage, en minimaal één actieve melding die direct op uw telefoon binnenkomt bij ernstige storingen.

Voeg rate limiting toe aan deze poort, want het valt onder dezelfde operationele discipline. Registratieformulieren, wachtwoordherstel en elk endpoint dat u per aanroep geld kost (zoals een LLM-aanroep, e-mail- of SMS-verzending) vereisen een strikte limiet vóórdat u live gaat, niet pas na het eerste geautomatiseerde misbruik.

**Benodigde hersteltijd:** 4 tot 8 uur voor een solide inrichting.

## Uw score, en wat deze betekent

Tel uw tekortkomingen eerlijk op. Nul tot twee openstaande poorten: u staat er uitstekend voor — los deze punten dit weekend op en lanceer uw product. Drie tot vier gefaalde poorten is de meest voorkomende uitslag voor een kwalitatief Cursor-project; dit vertegenwoordigt ongeveer een volle week aan specialistische infrastructuurwerkzaamheden. Vijf of meer gebreken betekent dat de bottleneck niet uw kennis is, maar uw beschikbare tijd. De centrale vraag wordt dan of u die week wilt besteden aan serverconfiguraties of aan het werven van uw eerste klanten.

Die afweging vormt het bestaansrecht van [LaunchStudio](https://launchstudio.eu/nl/): de code die u in Cursor heeft geschreven blijft volledig van u en blijft in uw eigen repositories staan, de zeven poorten worden vakkundig gedicht door senior engineers die dit proces honderden keren hebben doorlopen, en u ontvangt een heldere documentatieoverdracht zodat u daarna moeiteloos zelfstandig in Cursor verder kunt bouwen zonder vast te zitten aan vreemde structuren. Daarachter staat [Manifera](https://www.manifera.com/portfolio/), een softwarebedrijf dat al sinds 2014 enterprise productiesystemen levert — dezelfde rigoureuze kwaliteitsnormen, afgestemd op een kort en doeltreffend traject van één tot drie weken.

Wilt u een second opinion vóórdat u knopen doorhakt? Plan een korte afstemming in en leg uw meest complexe poort aan ons voor. Wij vertellen u eerlijk of dit een kwestie van een weekend werk is of een omvangrijker traject vergt.

## Praktijkvoorbeeld

### Zeven poorten, twee tekortkomingen, één kostbaar afgewend incident

Ruben Aksoy werkte vier maanden lang in Cursor aan Kantoorplan: een softwaretool voor bureaureserveringen en kantoorbezetting die hij op het punt stond via jaarcontracten te verkopen aan drie grote Rotterdamse coworking-operators. Ruben is een bekwame softwareontwikkelaar; zijn codebase zat logisch in elkaar, was uitstekend leesbaar en slaagde direct voor vijf van de zeven poorten.

Poort 2 bleek het heikele punt. Drieëntwintig API-routes, geschreven over een periode van veertig Cursor-sessies, met drie totaal verschillende autorisatiemethodieken. Negentien routes waren technisch in orde. Drie routes gebruikten een hulpfunctie die wel controleerde of de gebruiker bij de betreffende organisatie hoorde, maar niet welke rol deze had — waardoor elke willekeurige medewerker reserveringen van collega's kon wissen. Eén route — een CSV-exportfunctie die haastig was toegevoegd voor een verkoopdemo — accepteerde een los `orgId`-queryparameter zonder enige validatie. Hierdoor kon een ingelogde beheerder van de ene coworking-vestiging de volledige boekingshistorie en gebruikerslijst van een concurrerende operator downloaden. Ook Poort 4 faalde: het Prisma-diffcommando toonde elf structurele verschillen met de productiedatabase.

**Resultaat:** De volledige autorisatie werd geconsolideerd in één uniforme `assertCan(user, action, resource)`-laag die door alle 23 routes wordt aangeroepen. De export-route werd herschreven zodat de organisatie strikt wordt afgeleid uit het actieve sessietoken en niet uit de querystring, en de databasestructuur werd volledig gesynchroniseerd via een opgeschoonde baseline-migratie. Zes werkdagen werk, nul aanpassingen aan de gebruikersinterface, en Ruben beschikte over een officieel auditrapport dat hij direct kon overhandigen aan de IT-verantwoordelijken van zijn zakelijke klanten.

> *"Negentien van de drieëntwintig routes waren perfect. Dat was precies het griezelige — ik was niet slordig geweest, maar had de code verspreid over vier maanden geschreven en Cursor wist in november echt niet meer wat ik in augustus had afgesproken. De onveilige routes zagen er voor het oog exact hetzelfde uit als de veilige."*
> — **Ruben Aksoy, Oprichter, Kantoorplan (Rotterdam)**

**Kosten & Doorlooptijd:** € 2.900 (Launch Ready Pakket) — live binnen 6 werkdagen.

---

## Veelgestelde Vragen

### Mijn repository is privé. Zijn geheimen in de git-geschiedenis dan nog steeds een risico?

Jazeker. Privé-repositories worden geclonede naar laptops van ontwikkelaars, gedownload door CI/CD-runners, gecached door build-systemen en worden soms per ongeluk openbaar gezet. De git-geschiedenis bewaart al deze versies permanent. Beschouw elke geheime sleutel die ooit in een commit heeft gestaan als gecompromitteerd, trek deze direct in bij de betreffende leverancier en beoordeel daarna of het opschonen van de git-historie de moeite waard is.

### Is een Zod-schema op elke route niet voldoende als gegevensvalidatie?

Zod dekt de inkomende netwerkverzoeken uitstekend af, wat het merendeel van het dataverkeer betreft, maar zeker niet alles. Achtergrondtaken, database-seeders, beheerdersscripts en toekomstige API-koppelingen schrijven immers naar dezelfde tabellen zonder dat ze door dat specifieke Zod-schema lopen. Daarom moet de database via constraints en datatypes altijd zijn eigen integriteit bewaken. Beide lagen vervullen een andere rol en zijn eenvoudig in te richten.

### Hoe vind ik autorisatielekken zonder alle routes handmatig regel voor regel door te spitten?

Een complete controle vereist uiteindelijk een volledige inventarisatie, maar u kunt de risicogebieden razendsnel isoleren via gerichte zoekopdrachten (grep). Zoek specifiek naar route handlers die parameters zoals een record-ID uitlezen zónder dat er in de directe regels daaronder gerefereerd wordt naar de sessie of de ingelogde gebruiker. Dat levert binnen enkele minuten een korte lijst op van verdachte routes, en dat is vrijwel altijd de plek waar de daadwerkelijke beveiligingslekken zich bevinden.

### Betekent het dichten van deze poorten dat ik in de toekomst niet meer met Cursor kan werken?

Integendeel, een professionele oplevering maakt het werken met Cursor juist aanzienlijk effectiever. Zodra autorisatie is ondergebracht in één heldere, centrale functie en de databasestructuur strikt via migraties verloopt, zijn de architectuurconventies in de codebase zo expliciet dat het AI-model deze automatisch overneemt, in plaats van bij elke nieuwe sessie een eigen methodiek te verzinnen.

### Welke controlepoort moet ik als eerste aanpakken als ik slechts één weekend de tijd heb?

Poort 1, direct gevolgd door Poort 2. Een gelekte API-sleutel vormt een actief, doorlopend beveiligingslek dat u binnen enkele minuten kunt opsporen en verhelpen. Fouten in de autorisatielaag zijn de kwetsbaarheden die het snelst leiden tot pijnlijke datalekken met persoonsgegevens van klanten. Zaken zoals monitoring en dependency-hygiëne zijn uiterst belangrijk, maar leiden niet direct tot het blootstellen van andermans vertrouwelijke data.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Mijn repository is privé. Zijn geheimen in de git-geschiedenis dan nog steeds een risico?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. Privé-repositories worden geclonede naar laptops, CI-runners en build-servers. Trek elke gecommitteerde sleutel altijd in bij de leverancier en overweeg de git-historie op te schonen."
      }
    },
    {
      "@type": "Question",
      "name": "Is een Zod-schema op elke route niet voldoende als gegevensvalidatie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Zod valideert alleen inkomende HTTP-verzoeken, maar achtergrondprocessen, seeders en scripts schrijven rechtstreeks naar de database. Database constraints moeten zelfstandig de data-integriteit bewaken."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe vind ik autorisatielekken zonder alle routes handmatig regel voor regel door te spitten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Grep op route handlers die record-ID's uitlezen zonder nabije verwijzing naar de sessie of gebruikers-ID. Dit levert snel een scherpe shortlist op van potentiële IDOR-kwetsbaarheden."
      }
    },
    {
      "@type": "Question",
      "name": "Betekent het dichten van deze poorten dat ik in de toekomst niet meer met Cursor kan werken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, juist niet. Met gecentraliseerde autorisatie en reproduceerbare migraties zijn de architectuurconventies zo duidelijk dat Cursor ze voortaan consistent zal volgen."
      }
    },
    {
      "@type": "Question",
      "name": "Welke controlepoort moet ik als eerste aanpakken als ik slechts één weekend de tijd heb?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Pak eerst Poort 1 (geheimen) en daarna Poort 2 (autorisatie) aan. Dit zijn de kwetsbaarheden die direct kunnen leiden tot misbruik van API-tegoed of ernstige datalekken."
      }
    }
  ]
}
</script>
