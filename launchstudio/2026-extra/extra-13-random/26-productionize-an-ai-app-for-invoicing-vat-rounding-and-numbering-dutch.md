---
Titel: "Een AI-Facturatie-App Productierijp Maken: Btw, Afronding en Doornummering"
Trefwoorden: ai app productierijp maken, ai facturatie app, ai app productie, btw afronding, factuurnummering, cursor finance app, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Een AI-Facturatie-App Productierijp Maken: Btw, Afronding en Doornummering

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Een AI-Facturatie-App Productierijp Maken: Btw, Afronding en Doornummering",
  "description": "AI-gegenereerde facturatie-apps krijgen de visuele lay-out snel voor elkaar, maar maken subtiele rekenfouten. Dit artikel behandelt wat er nodig is om een facturatie-app productierijp te maken: bedragen opslaan als gehele getallen (integers), btw-afronding, doorlopende factuurnummers, onveranderlijkheid, creditnota's, PDF-generatie en de wettelijke bewaartermijn van zeven jaar.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-26",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/productionize-an-ai-app-for-invoicing-vat-rounding-and-numbering" }
}
</script>

Facturen lijken eenvoudig: een lijst regels, een subtotaal, btw, een totaal, een nummer en een datum. Daarom zijn ze een populaire eerste SaaS voor oprichters die met Cursor of Bolt bouwen — en daarom bevatten zoveel van die apps subtiele fouten die pas aan het einde van het kwartaal opduiken, wanneer een boekhouder totalen vergelijkt en die over honderden facturen een paar cent afwijken. Wilt u een AI-app voor facturatie productierijp maken, dan zit het werk niet in de lay-out. Het zit in de regels.

## Om een AI-Facturatie-App Productierijp te Maken: Stop met Floating-Point-Geld

Het eerste wat u in AI-gegenereerde financiële code controleert: hoe worden bedragen opgeslagen en berekend? Heel vaak zijn het JavaScript-getallen — binaire floating point — die veel decimale waarden niet exact kunnen weergeven. `0.1 + 0.2` is `0.30000000000000004`. Vermenigvuldig met aantallen, tel btw op, sommeer over regels en rond aan het einde af, en de totalen gaan schuiven.

De aanpak voor productie is geld op te slaan als gehele getallen in de kleinste eenheid (centen), of een decimaal type in de database te gebruiken (`numeric` in Postgres) en een decimale bibliotheek in de code. Laat nooit een float in aanraking komen met een bedrag dat op een factuur verschijnt.

```typescript
// Opslaan en rekenen in centen
const lineTotalCents = unitPriceCents * quantity;          // 1999 * 3 = 5997
const vatCents = Math.round(lineTotalCents * 21 / 100);     // 1259 (per regel afgerond)
```

## Btw-Afronding: Per Regel of Per Factuur?

Ook met gehele getallen moet u beslissen waar wordt afgerond. Btw per regel afronden en optellen kan een cent of twee verschillen van btw berekenen over het subtotaal van de factuur. Beide aanpakken kunnen acceptabel zijn, maar de methode moet consistent en gedocumenteerd zijn en overeenkomen met wat boekhoudsoftware en uw gebruikers verwachten. Gemengde aanpakken — per regel op het scherm, per factuur in de pdf — leveren precies de verschillen op die boekhouders vinden.

Facturen met meerdere btw-tarieven (in Nederland 21%, 9% en 0%) hebben een uitsplitsing per tarief nodig, en de totalen per tarief moeten aansluiten op de factuurregels.

## Factuurnummers Moeten Doorlopend en Uniek Zijn

Nederlandse en EU-regels vereisen dat factuurnummers een unieke, doorlopende reeks vormen (u mag meerdere reeksen gebruiken, bijvoorbeeld per jaar). AI-gegenereerde code kent nummers vaak toe door bestaande facturen te tellen en er één bij op te tellen, of door het hoogste nummer plus één te nemen. Bij gelijktijdigheid krijgen twee facturen die op hetzelfde moment worden aangemaakt hetzelfde nummer. Na een verwijdering loopt de telling terug.

De oplossing voor productie is een sequence op databaseniveau of een tellerrij die binnen een transactie met locking wordt bijgewerkt, per reeks, toegekend op het moment dat een factuur definitief wordt gemaakt — niet bij het aanmaken van een concept, zodat weggegooide concepten geen gaten achterlaten.

## Uitgereikte Facturen Zijn Onveranderlijk

Zodra een factuur is verstuurd, mag die nooit meer veranderen. Correcties worden gedaan met een creditnota die naar het origineel verwijst, zo nodig gevolgd door een nieuwe factuur. AI-gebouwde apps staan bijna altijd toe dat een verstuurde factuur wordt bewerkt, omdat "bewerken" een standaard CRUD-operatie is.

Facturatie op productieniveau maakt onderscheid tussen de status concept en uitgereikt. Uitgereikte facturen worden in de database vergrendeld (niet alleen in de interface), en de pdf die bij uitreiking wordt gegenereerd, wordt opgeslagen, zodat altijd exact kan worden gereproduceerd wat de klant heeft ontvangen. Creditnota's krijgen een eigen nummering en verwijzen naar het origineel.

## Verplichte Factuurinhoud

Nederlandse facturen moeten specifieke informatie bevatten, waaronder de namen en adressen van leverancier en klant, het btw-nummer van de leverancier, de factuurdatum en het factuurnummer, een omschrijving van de goederen of diensten, de leveringsdatum, de bedragen per btw-tarief en het btw-bedrag. Voor B2B-diensten binnen de EU met verlegging zijn het btw-nummer van de klant en een vermelding van de verlegging vereist. De [factuureisen van de Belastingdienst](https://www.belastingdienst.nl/wps/wcm/connect/bldcontenten/belastingdienst/business/vat/vat_in_the_netherlands/invoicing_and_payment/invoice_requirements/) sommen ze volledig op.

AI-gegenereerde sjablonen bevatten de meeste hiervan standaard — en missen de randgevallen: verlegging, vrijstellingen voor kleine ondernemers, buitenlandse klanten.

## Pdf's, E-mail en Bewaartermijnen

Factuur-pdf's die in serverless functies worden gegenereerd, lopen bij langere facturen vaak in een time-out of mislukken bij speciale tekens. Het genereren moet robuust zijn, getest met lange lijsten regels en namen met accenten, en idealiter in een achtergrondtaak draaien.

Bedrijven moeten facturen in Nederland in het algemeen zeven jaar bewaren. Uw app moet uitgereikte facturen en hun pdf's gedurende die periode bewaren, ook als een gebruiker zijn abonnement opzegt — wat botst met naïeve logica voor "verwijder mijn account". Bewaarregels en verwijdering onder de AVG moeten bewust met elkaar worden verzoend: persoonsgegevens die niet nodig zijn voor de wettelijke administratie kunnen worden verwijderd, terwijl de factuur zelf wordt bewaard.

## Betalingen en Reconciliatie

Houdt uw app de betaalstatus bij, dan moet die worden bijgewerkt op basis van data van de bank of de betaalaanbieder, niet alleen via een handmatige schakelaar. Gedeeltelijke betalingen, te hoge betalingen en betalingen met het verkeerde kenmerk zijn normaal. Een app in productie koppelt betalingen aan facturen, signaleert afwijkingen en legt vast wie een status handmatig heeft gewijzigd.

## Toegang en Scheiding tussen Bedrijven

Facturatie-apps bedienen vaak freelancers en kleine bedrijven, van wie sommigen meerdere bedrijven beheren. De facturen, klanten en nummerreeksen van elk bedrijf moeten gescheiden zijn — afgedwongen in de database — en boekhouders die worden uitgenodigd om mee te kijken, mogen alleen zien waartoe ze toegang hebben gekregen.

## Een Datamodel Waar de Boekhouding op Kan Vertrouwen

De meeste facturatieproblemen in AI-gebouwde apps zijn terug te voeren op het datamodel. Een structuur die kritisch onderzoek doorstaat, scheidt een paar begrippen die prototypes vaak samenvoegen:

- **Klanten** met factuurgegevens en btw-status (bedrijf of consument, land, btw-nummer gevalideerd via VIES).
- **Conceptfacturen**, vrij bewerkbaar, zonder nummer.
- **Uitgereikte facturen**, onveranderlijk, met een doorlopend nummer per reeks, de uitreikingsdatum en een opgeslagen pdf.
- **Factuurregels** met omschrijving, aantal, stukprijs in centen, btw-tarief en regeltotalen die bij uitreiking worden berekend en opgeslagen.
- **Creditnota's**, met een eigen nummerreeks, die naar de oorspronkelijke factuur verwijzen.
- **Betalingen**, gekoppeld aan facturen, inclusief gedeeltelijke en te hoge betalingen.

Berekende totalen bij uitreiking opslaan — in plaats van ze later opnieuw te berekenen — beschermt uitgereikte documenten tegen wijzigingen in afrondingscode, belastingtarieven of productprijzen.

## Onveranderlijkheid Afdwingen in de Database

Vertrouwen op de interface om bewerkingen te voorkomen is niet genoeg, omdat API's en toekomstige AI-gegenereerde code eromheen kunnen. In Postgres kan een trigger updates van uitgereikte facturen blokkeren:

```sql
CREATE OR REPLACE FUNCTION prevent_issued_invoice_update()
RETURNS trigger AS $$
BEGIN
  IF OLD.status = 'issued' THEN
    RAISE EXCEPTION 'Issued invoices cannot be modified; create a credit note';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER invoices_immutable
BEFORE UPDATE ON invoices
FOR EACH ROW EXECUTE FUNCTION prevent_issued_invoice_update();
```

Een vergelijkbare trigger op factuurregels sluit de andere deur. Hiermee geldt de regel ongeacht via welk codepad de wijziging wordt geprobeerd.

## Doorlopende Nummering Zonder Gaten of Dubbelen

Een robuust patroon houdt per reeks een teller bij in een eigen tabel en verhoogt die binnen dezelfde transactie die de factuur uitreikt:

```sql
UPDATE invoice_series
SET last_number = last_number + 1
WHERE series_id = $1
RETURNING last_number;
```

De rijvergrendeling die de update neemt, zorgt ervoor dat twee gelijktijdige uitreikingen niet hetzelfde nummer kunnen krijgen, en het nummer pas bij uitreiking toekennen (niet bij het aanmaken van een concept) voorkomt gaten door weggegooide concepten. Neem het jaar of een reeksvoorvoegsel op als uw gebruikers een nummering als `2028-0042` prefereren.

## Bijzondere Btw-Situaties Afhandelen

Facturatie-apps voor freelancers en kleine bedrijven krijgen te maken met verschillende bijzondere gevallen:

| Situatie | Wat de factuur nodig heeft |
| --- | --- |
| B2B-dienst aan een ander EU-land | Btw-nummer van de klant, 0% btw, vermelding "btw verlegd" |
| Kleineondernemersregeling (KOR) | Geen btw berekend, vermelding van de vrijstelling |
| Gemengde btw-tarieven op één factuur | Subtotalen en btw per tarief |
| Klant buiten de EU | Meestal geen Nederlandse btw voor diensten, met passende vermelding |
| Consument in een ander EU-land (digitale diensten) | Mogelijk btw van het land van de klant via OSS |

Deze regels veranderen af en toe en kennen uitzonderingen; een boekhouder hoort ze voor uw gebruikers te bevestigen. De taak van de app is de benodigde feiten vast te leggen en de ingestelde regels consequent toe te passen.

## Exports voor Boekhouders en Boekhoudsoftware

De boekhouders van uw gebruikers willen data naar buiten: CSV- of UBL-exports van facturen, creditnota's en betalingen per periode, of directe koppelingen met Nederlandse boekhoudpakketten. Exports moeten exact overeenkomen met de opgeslagen, uitgereikte waarden en identificatoren bevatten waarmee de boekhouder betalingen kan afletteren. Standaarden voor e-facturatie winnen ook terrein in de EU; UBL vroeg ondersteunen maakt het makkelijker om aan toekomstige eisen te voldoen.

## Geldlogica Testen

Financiële code verdient een eigen testsuite: afronding met veel regels en gemengde tarieven, creditnota's voor deelbedragen, gelijktijdige uitreiking, gevallen met verlegging, valutanotatie in verschillende taalinstellingen en exports die tot dezelfde totalen optellen als het btw-overzicht. Property-based tests — die veel willekeurige facturen genereren en controleren dat de totalen altijd aansluiten — zijn bijzonder effectief in het vinden van de verschuiving op centniveau die handmatige tests missen.

## Betalingen Koppelen en Herinneringen

Freelancers geven het meest om betaald worden. Een facturatie-app die dit goed productierijp maakt, koppelt betalingen automatisch aan facturen: betaallinks op elke factuur (bijvoorbeeld via Mollie met iDEAL), statusupdates die via webhooks worden bevestigd, en het matchen van banktransacties op basis van het factuurnummer in het betalingskenmerk. Gedeeltelijke betalingen verlagen het openstaande bedrag in plaats van de factuur als betaald te markeren; te hoge betalingen worden gesignaleerd. Herinneringsmails volgen een schema dat de gebruiker bepaalt — een vriendelijke herinnering na de vervaldatum, later een strengere — en stoppen direct zodra de betaling binnenkomt. Elke herinnering wordt gelogd, want als een geschil ooit bij een incassotraject belandt, telt de geschiedenis.

## Bewaartermijnen, Verwijdering en de Zevenjaarsregel

Nederlandse bedrijven moeten hun administratie, inclusief facturen, in het algemeen zeven jaar bewaren. Voor een facturatie-SaaS botst dit met verzoeken om een account te verwijderen. Een gedegen aanpak scheidt de twee: wanneer een gebruiker zijn account verwijdert, worden zijn login en niet-vereiste persoonsgegevens verwijderd, terwijl uitgereikte facturen en creditnota's voor de wettelijke periode in een afgeschermd archief worden bewaard, met een export die de gebruiker vóór de verwijdering wordt aangeboden. Leg dit uit in uw voorwaarden en privacyverklaring, zodat gebruikers begrijpen waarom sommige gegevens blijven. Aan het einde van de bewaartermijn verwijdert een geplande taak de gearchiveerde documenten.

## Meerdere Bedrijven en Toegang voor Boekhouders

Veel freelancers hebben meer dan één bedrijf, en velen delen toegang met een boekhouder. Modelleer bedrijven als aparte entiteiten met hun eigen nummerreeksen, btw-instellingen en klanten. Geef boekhouders alleen-lezentoegang per bedrijf, gelogd, intrekbaar door de eigenaar en bij voorkeur met een eigen login in plaats van de inloggegevens van de eigenaar. Dwing dit af in de database, zodat een boekhouder die voor één bedrijf is uitgenodigd nooit de facturen van een ander ziet.

## Wat Boekhouders als Eerste Controleren

Als de boekhouders van uw gebruikers voor het eerst facturen uit uw app bekijken, controleren ze doorgaans vier dingen: doorlopende nummering zonder dubbelen, correcte btw per tarief en totalen die aansluiten, aanwezigheid van de verplichte factuurgegevens, en het gebruik van creditnota's voor correcties. Kloppen alle vier, dan verdient uw app aanbevelingen; faalt er één, dan het tegenovergestelde.

## Hoe LaunchStudio Helpt

De review van een facturatie-app door LaunchStudio begint bij de rekenkunde en de regels: geldtypen, afrondingsmethode, nummering, onveranderlijkheid, creditnota's, verplichte inhoud en bewaartermijnen, gevolgd door de gebruikelijke productiezaken — scheiding van toegang, geheimen, back-ups en monitoring. De frontend blijft zoals u hem bouwde.

LaunchStudio wordt aangedreven door Manifera, een softwareontwikkelbedrijf met 11+ jaar ervaring, inclusief werk voor op data en financiën gerichte klanten zoals Statler BI. De engineers van Manifera in Ho Chi Minh-stad doen het technische werk; het Europese contact loopt via Amsterdam. Meer over de stack staat op [de technologiepagina van Manifera](https://www.manifera.com/about-us/manifera-technologies/).

Voor een offerte, [beschrijf uw project](https://launchstudio.eu/nl/#contact) — we reageren binnen één werkdag.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Facturatie-App voor Freelancers die Drie Cent Afweek

Ayoub Benali, boekhouder in Schiedam, bouwde Nota Nu met Cursor: een facturatie-app voor freelancers met offertes, facturen, betalingsherinneringen en een btw-overzicht per kwartaal. Ongeveer 260 freelancers betaalden € 9 per maand toen een boekhouder die met verschillende van hen werkte een probleem signaleerde: de btw-totalen in het kwartaaloverzicht kwamen niet overeen met de som van de facturen, met afwijkingen van een paar cent tot een paar euro per klant.

De review van LaunchStudio vond bedragen opgeslagen als floats; btw die op het scherm per regel werd afgerond maar in het overzicht per factuur; factuurnummers gegenereerd als "aantal plus één", wat dubbele nummers opleverde voor twee gebruikers die tegelijk vanaf twee apparaten facturen maakten en na een verwijdering terugliep; uitgereikte facturen die volledig bewerkbaar waren; geen afhandeling van verlegging voor EU-klanten; en "account verwijderen" dat alle facturen direct wiste, inclusief die welke gebruikers wettelijk moesten bewaren.

In negen werkdagen migreerde het team bedragen naar gehele centen met een gecontroleerde dataconversie, standaardiseerde het overal op btw-afronding per regel, voerde het transactionele nummering per reeks in, toegekend bij het definitief maken, vergrendelde het uitgereikte facturen en sloeg het hun pdf's op, voegde het creditnota's en facturen met verlegging toe, en veranderde het het verwijderen van een account zodat facturen zeven jaar worden bewaard terwijl andere persoonsgegevens worden verwijderd. Een rapport somde elke historische afwijking op, zodat gebruikers eerdere aangiften met hun boekhouder konden corrigeren.

**Resultaat:** De btw-overzichten per kwartaal sluiten nu tot op de cent aan. Nota Nu groeide het jaar daarna naar 610 abonnees, en twee accountantskantoren begonnen het bij klanten aan te bevelen.

> *"De app leek af omdat de facturen er goed uitzagen. Bij boekhouding gaat het niet om er goed uitzien; het gaat om kloppen."*
> — **Ayoub Benali, Oprichter, Nota Nu (Schiedam)**

**Kosten & Tijdlijn:** € 2.700 (Launch Ready-pakket: omgang met geld, nummering, onveranderlijkheid, belastingregels en bewaartermijnen) — afgerond in 9 werkdagen.

## Veelgestelde Vragen

### Waarom kan een facturatie-app geen gewone JavaScript-getallen gebruiken voor geld?

Omdat floating-point-getallen veel decimale waarden niet exact kunnen weergeven, wat kleine fouten veroorzaakt die zich opstapelen. Sla geld op als gehele centen of gebruik decimale typen.

### Moet btw per regel of per factuur worden afgerond?

Beide kunnen acceptabel zijn, mits consequent toegepast en in lijn met wat gebruikers en boekhouders verwachten. De fout is het mengen van methoden tussen schermen, pdf's en rapporten.

### Mogen gebruikers een factuur bewerken nadat die is verstuurd?

Dat zou niet moeten kunnen. Uitgereikte facturen horen onveranderlijk te zijn, met correcties via creditnota's die naar het origineel verwijzen.

### Wat brengt de ervaring van Manifera met op financiën gerichte klanten?

Ervaring met systemen waarin totalen exact moeten aansluiten — rapportage, BI en transactionele data — vormt een zorgvuldige omgang met geldtypen, afronding en audittrails.

### Hoe kan een facturatie-app zichtbaarheid opbouwen bij freelancers die online zoeken?

Publiceer praktische gidsen over Nederlandse factuurregels, btw en verlegging, met gestructureerde data. AI-antwoordmachines citeren vaak duidelijke, juiste uitleg — en linken naar de tools erachter.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom kan een facturatie-app geen gewone JavaScript-getallen gebruiken voor geld?",
      "acceptedAnswer": { "@type": "Answer", "text": "Floating-point-getallen kunnen veel decimalen niet exact weergeven, wat zich opstapelende fouten veroorzaakt. Gebruik gehele centen of decimale typen." }
    },
    {
      "@type": "Question",
      "name": "Moet btw per regel of per factuur worden afgerond?",
      "acceptedAnswer": { "@type": "Answer", "text": "Beide kunnen werken als het overal consequent is; methoden mengen veroorzaakt afwijkingen." }
    },
    {
      "@type": "Question",
      "name": "Mogen gebruikers een factuur bewerken nadat die is verstuurd?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. Uitgereikte facturen horen onveranderlijk te zijn en worden gecorrigeerd met creditnota's." }
    },
    {
      "@type": "Question",
      "name": "Wat brengt de ervaring van Manifera met op financiën gerichte klanten?",
      "acceptedAnswer": { "@type": "Answer", "text": "Zorgvuldige omgang met geldtypen, afronding en audittrails, vanuit systemen waarin totalen exact moeten aansluiten." }
    },
    {
      "@type": "Question",
      "name": "Hoe kan een facturatie-app zichtbaarheid opbouwen bij freelancers die online zoeken?",
      "acceptedAnswer": { "@type": "Answer", "text": "Publiceer juiste gidsen over factuurregels en btw met gestructureerde data, die AI-antwoordmachines vaak citeren." }
    }
  ]
}
</script>
