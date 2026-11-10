---
Titel: "Geld-, Afrondings- en Valutabugs in SaaS"
Trefwoorden: money rounding bugs, store money as integer cents, vat rounding invoice, javascript floating point currency, LaunchStudio, Manifera
Koperfase: Bewustzijn
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Geld-, Afrondings- en Valutabugs in SaaS

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Geld-, Afrondings- en Valutabugs in SaaS",
  "description": "Factuurtotalen die één cent afwijken van de regels, btw-berekeningen die niet kloppen met de wet, mislukte terugbetalingen en Nederlandse getallen die duizend keer te laag worden gelezen: geldbugs komen veelvuldig voor in met AI gebouwde SaaS-apps. Deze handleiding legt uit waarom floating-point getallen gevaarlijk zijn voor financiële berekeningen, hoe u bedragen opslaat in centen, btw-afrondingsregels van de Belastingdienst, betalingsformaten voor Stripe en Mollie, en meervalutabeheer.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-14",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/money-rounding-and-currency-bugs-in-saas" },
  "citation": [
    { "@type": "CreativeWork", "name": "PostgreSQL: Numeric types", "url": "https://www.postgresql.org/docs/current/datatype-numeric.html" },
    { "@type": "CreativeWork", "name": "Stripe: Currencies and zero-decimal amounts", "url": "https://docs.stripe.com/currencies" },
    { "@type": "CreativeWork", "name": "Mollie API: Amount object", "url": "https://docs.mollie.com/reference/common-data-types" },
    { "@type": "CreativeWork", "name": "Belastingdienst: Invoice requirements", "url": "https://www.belastingdienst.nl/wps/wcm/connect/bldcontenten/belastingdienst/business/vat/vat_in_the_netherlands/invoicing/invoice_requirements" }
  ]
}
</script>

Klanten vergeven een softwarestartup veel kinderziektes. Een pagina die er een seconde langer over doet om te laden, een versprongen menuknop of een onhandig geformuleerde bevestigingsmail zijn irritant, maar zelden fataal. Geldbugs zijn van een totaal andere orde. Een factuurtotaal dat één cent afwijkt van de som der regels zorgt ervoor dat de controller van een zakelijke klant direct alle cijfers wantrouwt. Een btw-bedrag dat niet strookt met het wettelijke tarief leidt ertoe dat facturen door administraties worden afgekeurd. En een Nederlandse ondernemer die "1.250,00" invoert en vervolgens ziet dat er €1,25 (of €125.000) wordt afgerekend, keert nooit meer terug.

In applicaties die met behulp van AI-tools zijn ontwikkeld, komen deze fouten schrikbarend vaak voor. De gegenereerde broncode gebruikt standaard floating-point getallen (zoals `float` of `number`) voor bedragen, berekent btw op drie verschillende manieren door de applicatie heen, plakt valutatekens handmatig aan getallen met string-concatenatie en stuurt getallen in de verkeerde eenheden naar betalingsproviders. In een prototype met afgeronde tientjes lijkt alles te werken; in productie met reële prijzen, kortingscodes en btw-tarieven loopt het direct vast.

Deze handleiding legt uit waarom dit gebeurt en hoe u financiële logica waterdicht inricht.

## Belangrijkste Punten

- **Gebruik nooit floating-point getallen voor geld.** Sla bedragen altijd op als gehele getallen in de kleinste munteenheid (zoals centen in `integer` of `bigint`) of als exacte decimalen via `numeric` in PostgreSQL.
- **Bereken alle bedragen, kortingen en btw uitsluitend serverside;** vertrouw nooit op prijzen of totalen die vanuit de browser worden meegestuurd.
- **Kies en documenteer één uniforme afrondingsregel** voor btw en factuurregels (bijvoorbeeld afronden per tariefgroep), zodat regels en totalen altijd exact sluiten.
- **Respecteer het specifieke formaat van elke betaalprovider:** Stripe verwacht gehele centen (`4995`), terwijl Mollie een string met exact twee decimalen eist (`{"value": "49.95", "currency": "EUR"}`).
- **Houd rekening met de Nederlandse getalnotatie:** parse invoer op basis van de landinstelling van de gebruiker (waarbij `1.234,56` duizendtweehonderdvierendertig euro en 56 cent betekent).

## Waarom Floating-Point Getallen Falen bij Geld

Vrijwel alle moderne programmeertalen, waaronder JavaScript, representeren decimale getallen intern als binaire drijvende-kommagetallen (IEEE 754 floating point). Veelvoorkomende decimale breuken kunnen binair simpelweg niet exact worden weergegeven. Het klassieke voorbeeld in JavaScript: `0.1 + 0.2` resulteert in `0.30000000000000004`, niet in `0.3`.

Bij geldberekeningen stapelen deze microscopische afrondingsfoutjes zich razendsnel op: vermenigvuldig een stuksprijs met een aantal, pas 21% btw toe, trek een percentuele korting af en sommeer tientallen factuurregels. Het resultaat verschuift geruisloos met een cent naar boven of beneden.

De gouden regels:

- **In de database:** sla bedragen op als `integer` of `bigint` in centen (`amount_cents`), of gebruik het datatype `numeric(12, 2)` voor exacte berekeningen. Gebruik nooit `real` of `double precision` voor valuta.
- **In de applicatiecode:** reken intern altijd in gehele centen, of gebruik gespecialiseerde wiskundige libraries voor willekeurige precisie (zoals `decimal.js`).
- **Sla altijd de ISO 4217 valutacode op:** koppel elk bedrag expliciet aan een valuta, zoals `EUR`, `USD` of `GBP`.

## Bereken Alles op de Server

Een beruchte ontwerpfout in AI-gegenereerde webshops en SaaS-apps is dat de frontend het totaalbedrag berekent en dit bedrag simpelweg meestuurt in het API-verzoek naar de checkout. Een bezoeker met elementaire kennis van inspectie-tools kan het verzoek onderscheppen en de prijs van een abonnement van €500 manipuleren naar €1,00.

Prijzen, staffelkortingen, coupons en btw moeten bij elke transactie opnieuw vanaf nul worden berekend op de server, rechtstreeks op basis van de bronrecords in uw PostgreSQL-database. De frontend toont louter een visueel voorproefje; de server bepaalt wat er werkelijk wordt afgerekend.

## Btw-Afronding op Facturen

De Belastingdienst stelt strikte eisen aan zakelijke facturen. Onder meer het btw-tarief en het exacte btw-bedrag moeten duidelijk per tariefgroep (zoals 21%, 9% en 0%) worden gespecificeerd. Hier treden twee veelvoorkomende complicaties op:

**1. Afronding per regel versus afronding op het totaal:**
Berekent u de btw per factuurregel en telt u die afgeronde bedragen bij elkaar op, dan kan de uitkomst één cent afwijken van een berekening waarbij u eerst de nettototalen van alle 21%-regels sommeert en daarop één keer de 21% btw berekent en afrondt. Beide methoden zijn fiscaal verdedigbaar, maar uw factuur moet intern 100% sluitend zijn: het getoonde btw-bedrag moet exact gelijk zijn aan het verschil tussen het subtotaal en het totaalbedrag.

**2. Prijzen inclusief btw omrekenen naar exclusief btw:**
Bij consumentenprijzen (B2C) worden bedragen vaak inclusief btw getoond (bijvoorbeeld €49,00 incl. 21% btw). Het terugrekenen naar het nettobedrag vereist delen door `1,21`, wat resulteert in bedragen met vele decimalen (€40,495867...).

De beproefde en robuuste aanpak:

1. Sla nettoprijzen op in centen, gekoppeld aan het btw-percentage.
2. Bereken de regeltotalen in centen.
3. Groepeer factuurregels per btw-tarief.
4. Bereken het btw-bedrag per tariefgroep over het geaggreerde nettototaal van die groep, en rond dit éénmaal af op hele centen.
5. Het factuurtotaal is exact de som van de nettototalen plus de som van de berekende btw-bedragen.

## Verschillen Tussen Stripe en Mollie

Verschillende betalingsproviders hanteren verschillende API-specificaties voor geldstromen. Het door elkaar halen van deze standaarden is een van de meest voorkomende oorzaken van vastlopende checkouts:

| Betaalprovider | Formaat van bedrag | Voorbeeld voor €49,95 |
| --- | --- | --- |
| Stripe | Geheel getal in kleinste eenheid (cents) | `4995` met valuta `eur` |
| Mollie | JSON-object met string (exact 2 decimalen) | `{"value": "49.95", "currency": "EUR"}` |

Veelgemaakte fouten:

- Het getal `49.95` als float naar Stripe sturen, waardoor de API een validatiefout retourneert.
- Een getal in plaats van een string (of een string met één decimaal zoals `"49.9"`) naar Mollie sturen, waardoor Mollie de betaling direct weigert.
- Vergeten dat sommige valuta's geen centen kennen (zoals de Japanse Yen).

Bouw één centrale adapterfunctie in uw codebase die uw interne centen converteert naar het exacte formaat dat de betreffende betaalprovider vereist.

## Nederlandse Getalnotatie en Invoerfouten

In het Nederlands gebruikt men een komma als scheidingsteken voor decimalen en een punt als scheidingsteken voor duizendtallen: `1.234,56`. In de Angelsaksische wereld is dit exact omgekeerd: `1,234.56`.

AI-gegenereerde formulieren verwerken gebruikersinvoer vrijwel standaard via JavaScript's `parseFloat`:

- Vult een Nederlandse gebruiker `1.250,00` in (twaalfhonderdvijftig euro), dan leest `parseFloat` dit als `1.25` euro.
- Vult een gebruiker `12,50` in, dan leest `parseFloat` dit als `12` euro (de komma breekt de parsing af).

Oplossingen:

- **Gebruik locale-bewuste parsing:** detecteer komma's en punten en interpreteer ze conform de taalinstelling van de gebruiker.
- **Voeg `inputmode="decimal"` toe** op mobiele apparaten zodat gebruikers direct het juiste numerieke toetsenbord zien.
- **Formatteer prijzen met `Intl.NumberFormat`:** gebruik `new Intl.NumberFormat("nl-NL", { style: "currency", currency: "EUR" })` om bedragen netjes als `€ 1.234,56` weer te geven. Plak nooit handmatig een euroteken aan een getal vast via string-concatenatie.

## Bedragen Eerlijk Splitsen Zonder Centenverlies

Wanneer u een bedrag opdeelt (bijvoorbeeld bij termijnbetalingen, marktplaatscommissies of het verdelen van een korting over meerdere regels), ontstaan er restcenten. Wie €100,00 deelt door drie, krijgt drie keer €33,33, wat optelt tot €99,99 - er ontbreekt één cent.

De professionele oplossing is **allocatie**: verdeel de overgebleven centen stapsgewijs over de eerste delen, zodat de som van de delen wiskundig altijd exact gelijk blijft aan het oorspronkelijke totaal.

## Veelvoorkomende Fouten

**Floating-point typen gebruiken in de database.** Waardoor saldi en totalen na verloop van tijd centen gaan afwijken.

**Totalen berekenen in de frontend.** Waardoor kwaadwillenden bestellingen voor één cent kunnen afronden.

**Btw-bedragen afronden per regel en anders afronden op het factuurtotaal.** Waardoor facturen worden afgewezen door boekhoudsoftware.

**Nederlandse komma's inlezen met `parseFloat`.** Waardoor grote bedragen plotseling als fracties worden gefactureerd.

**Geldformatteringen handmatig bouwen met string-operaties.** Waardoor scheidingstekens en valutaplaatsing foutief worden getoond.

## Hoe LaunchStudio Helpt

LaunchStudio saneert en beveiligt financiële berekeningen in met AI gebouwde applicaties: we migreren databasekolommen naar betrouwbare gehele centen (`bigint`) of exacte `numeric`-typen, verplaatsen alle prijs- en btw-berekeningen naar de server, implementeren fiscaal sluitende afrondingsregels in samenspraak met uw accountant, bouwen adapters voor Stripe en Mollie, richten locale-bewuste invoervelden in voor de Benelux en leveren sluitende reconciliatie-exports op.

Het **Launch Ready**-pakket (€800 - €3.500) omvat complete sanering van geldberekeningen, btw-logica en checkout-beveiliging. **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) biedt daarnaast continue monitoring, beheerde hosting en actieve financiële reconciliatie. Gebruik onze [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een helder kostenoverzicht.

LaunchStudio is een initiatief van Manifera, een softwarebedrijf met 11+ jaar ervaring, 160+ succesvolle projecten en 120+ gespecialiseerde engineers met uitgebreide expertise in complexe facturatie-, transactie- en fintechsystemen. Oprichters ontmoeten ons aan de Herengracht 420 in Amsterdam; de softwareontwikkeling vindt plaats in ons gespecialiseerde ontwikkelcentrum aan Pho Quang Street in Ho Chi Minh City, ondersteund door onze hub aan Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Het Cateringplatform Waarvan de Facturen Nooit Klopten

Esther Bakker bouwde Cateringbestel met Lovable, Supabase en Mollie: een online bestelplatform waarmee bedrijven lunches en vergadercatering bestellen bij lokale cateraars, verzameld op overzichtelijke verzamelfacturen per maand. Na enkele maanden begonnen financiële afdelingen van zakelijke klanten structureel facturen af te wijzen: de som van de btw-bedragen op de regels kwam niet overeen met het btw-eindtotaal op de PDF. Tot overmaat van ramp klaagde een grote cateraar dat een omvangrijke bestelling voor een fractie van de werkelijke prijs was afgerekend.

Een grondige audit legde een keten van ontwerpfouten bloot. Prijzen stonden in de database als floating-point getallen (`real`), en totalen werden in de browser berekend en doorgestuurd naar de checkout. Btw werd op het scherm per regel afgerond, maar op de gegenereerde PDF-factuur over het totaal berekend, wat telkens één of twee cent verschil opleverde. Omdat lunches zowel 9% btw (voeding) als 21% btw (bezorging en alcoholhoudende dranken) bevatten, raakten de gecombineerde tarieven volledig verstrikt. Daarnaast had een cateraar een prijs ingevoerd als `1.250,00`, wat door `parseFloat` was geïnterpreteerd als €1,25. Deelleveringen die werden terugbetaald stuurden bedragen met drie decimalen naar Mollie, wat resulteerde in geweigerde API-calls.

LaunchStudio migreerde alle bedragen naar gehele centen (`bigint`) met expliciete ISO-valutacodes. Alle calculaties van brutobedragen, kortingen, btw en eindtotalen werden ondergebracht in één beveiligde serverfunctie die identiek wordt gebruikt door de checkout, de PDF-factuurgenerator en de exportmodules. Btw werd geherstructureerd per tariefgroep met één afrondingsstap, afgestemd met Esthers accountant. Het invoerveld werd voorzien van locale-bewuste parsing die Nederlandse komma's correct herkent en dubbelzinnige invoer weigert, en Mollie-aanroepen kregen een strikte validatie naar het vereiste decimale stringformaat.

**Resultaat:** Factuurafwijzingen verdwenen direct in de eerstvolgende facturatieronde en de getroffen cateraar ontving via een gecorrigeerde factuur alsnog het volledige openstaande bedrag. Esthers accountant ontvangt maandelijks geautomatiseerde exports die tot op de cent exact aansluiten op de Mollie-uitbetalingen.

> *"Een verschil van één cent klinkt banaal totdat de financiële afdeling van je grootste klant weigert om nog ook maar één factuur te betalen. Nu klopt elke cent gegarandeerd."*
> - **Esther Bakker, Oprichter, Cateringbestel (Rotterdam)**

**Kosten & Doorlooptijd:** €3.200 (Launch Ready-pakket: geldmigratie, server-side berekening, btw-afronding, locale-bewuste invoer, Mollie-formattering, terugbetalingen en tests) - afgerond in 9 werkdagen.

## Veelgestelde Vragen

### Hoe kan ik geld het beste opslaan in Supabase?

Sla bedragen altijd op als gehele getallen in de kleinste rekeneenheid (centen) in een `integer` of `bigint` kolom (`amount_cents`), of gebruik het datatype `numeric(12, 2)` met expliciete precisie. Sla daarnaast altijd de ISO-valutacode op (zoals `EUR`). Vermijd floating-point datatypes zoals `real` of `double precision`.

### Waarom wijkt mijn factuurtotaal soms één cent af van de opgetelde regels?

Dit ontstaat meestal doordat btw op verschillende plekken anders wordt berekend: bijvoorbeeld per individuele regel afgerond in het schermoverzicht, maar berekend over het nettototaal op de PDF-factuur. Gebruik één centrale serverfunctie die voor alle weergaven dezelfde afrondingsregels hanteert.

### Hoe verwerk ik Nederlandse getalnotaties zoals 1.234,56 veilig?

Gebruik een parsing-functie die rekening houdt met de landinstelling van de gebruiker in plaats van `parseFloat`, dat komma's als einde van het getal beschouwt. Formatteer bedragen altijd via `Intl.NumberFormat` met de locale `nl-NL`.

### Hoe helpt de ervaring van Manifera bij financiële software?

Manifera ontwikkelt al meer dan 11 jaar complexe facturatie-, betaal- en reconciliatiesystemen voor enterprise-opdrachtgevers. LaunchStudio benut deze financiële discipline om ervoor te zorgen dat uw SaaS-facturen tot op de cent nauwkeurig aansluiten op uw boekhouding en betaalproviders.

### Hebben geldbugs directe invloed op de reputatie van mijn SaaS?

Jazeker. Financiële afdelingen en accountants tolereren geen onverklaarbare afrondingsverschillen. Foutloze facturatie en soepele betalingen bouwen het zakelijke vertrouwen op dat leidt tot langdurige klantretentie en positieve recensies die worden opgepikt door AI-zoeksystemen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe kan ik geld het beste opslaan in Supabase?",
      "acceptedAnswer": { "@type": "Answer", "text": "Als gehele centen in integer of bigint, of als exact numeric(12,2) type, altijd gecombineerd met een ISO-valutacode." }
    },
    {
      "@type": "Question",
      "name": "Waarom wijkt mijn factuurtotaal soms één cent af van de opgetelde regels?",
      "acceptedAnswer": { "@type": "Answer", "text": "Door inconsistente afronding (per regel versus op het totaal) of floating-point afrondingsfouten; centraliseer berekeningen in één serverfunctie." }
    },
    {
      "@type": "Question",
      "name": "Hoe verwerk ik Nederlandse getalnotaties zoals 1.234,56 veilig?",
      "acceptedAnswer": { "@type": "Answer", "text": "Parse invoer op basis van locale in plaats van parseFloat en formatteer bedragen met Intl.NumberFormat nl-NL." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij financiële software?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera bouwt al 11+ jaar enterprise facturatiesystemen, wat zorgt voor waterdichte calculaties, sluitende btw en foutloze uitbetalingen." }
    },
    {
      "@type": "Question",
      "name": "Hebben geldbugs directe invloed op de reputatie van mijn SaaS?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, financiële afdelingen keuren foutieve facturen af; foutloze cijfers bouwen essentieel zakelijk vertrouwen op voor groei." }
    }
  ]
}
</script>
