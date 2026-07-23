---
Titel: "Jouw AI-Prototype Ziet Er Af Uit. Zo Controleer Je Of Het Dat Daadwerkelijk Is"
Trefwoorden: ai prototype, prototype ai, ai native, LaunchStudio, Manifera
Koperfase: Bewustzijn
Doelgroep: AI-Native Founder (niet-technisch)
---

# Jouw AI-Prototype Ziet Er Af Uit. Zo Controleer Je Of Het Dat Daadwerkelijk Is

"Ziet er af uit" is een oprecht misleidend signaal, en het is de moeite waard eerlijk te zijn over waarom: een AI-prototype dat netjes rendert, direct reageert, en elke klik afhandelt die je zelf maakt is specifiek geoptimaliseerd om die indruk te produceren, ongeacht wat er daadwerkelijk onder gebeurt. Hier is een concrete manier om te beginnen controleren of "ziet er af uit" en "is af" daadwerkelijk overeenkomen, met de developer tools van je eigen browser als eerste, gratis diagnose.

## Stap Eén: Open De Developer Tools Van Je Browser En Bekijk Het Netwerktabblad

Elke moderne browser omvat een "Network"- of "Sources"-tabblad in zijn developer tools, die elk verzoek van je app toont en, vaak, de ruwe JavaScript-bundel gestuurd naar de browser. Dit is publiek zichtbaar voor letterlijk iedereen die hetzelfde tabblad opent op jouw live site — het is geen verborgen of geavanceerde hacktechniek, het is een standaard, ingebouwde browserfunctie.

## Stap Twee: Doorzoek Die Bundel Op Alles Dat Op Een Geheime Sleutel Lijkt

Zoeken in de zichtbare JavaScript-bundel naar strings zoals "sk_" (een gebruikelijk Stripe-geheimsleutelvoorvoegsel), "secret," "private," of jouw eigen bekende API-sleutelpatronen is een simpele, directe manier om te controleren of een sleutel die alleen ooit op jouw server zou moeten bestaan in plaats daarvan gebundeld is in code gestuurd naar de browser van elke bezoeker.

## Stap Drie: Begrijp Waarom Deze Specifieke Fout Zo Gebruikelijk Is

Betalingsproviders zoals Stripe geven twee aparte soorten sleutels uit — een "publiceerbare" sleutel, veilig te gebruiken in frontendcode, en een "geheime" sleutel, alleen bedoeld voor server-side gebruik. AI-codeertools die een snelle betalingsintegratie genereren gebruiken soms welke sleutel er ook in de prompt gegeven werd zonder onderscheid te maken tussen de twee, en als een founder de geheime sleutel plakt waar de publiceerbare sleutel hoort, heeft de tool geen onafhankelijke manier om te weten dat het de verkeerde is.

## Stap Vier: Erken Waarom Een Werkende Betalingsflow Dit Niet Uitsluit

Een betalingsintegratie die de geheime sleutel rechtstreeks in frontendcode gebruikt zal, in veel gevallen, nog steeds succesvol testbetalingen verwerken — de fout produceert niet noodzakelijk een foutmelding, wat precies waarom "het werkt" hier geen geruststellend bewijs is. Het risico is niet dat het niet functioneert; het is dat een volledig geprivilegieerde sleutel ergens zit waar elke bezoeker het kan lezen.

## Stap Vijf: Krijg Een Systematische Review, Niet Alleen Een Handmatige Zoekopdracht

Een handmatige zoekopdracht vangt voor de hand liggende gevallen maar is niet uitputtend — een correcte audit controleert elke integratie systematisch, bevestigt dat het correcte sleuteltype gebruikt wordt in elke context, en verifieert dat geen ander geheim hetzelfde patroon volgde. [LaunchStudio](https://launchstudio.eu/en/) voert precies dit soort systematische sleutel- en geheimenaudit uit als een standaard eerste stap in zijn productiegereedheidsreview, gesteund door Manifera's 11+ jaar Stripe en Mollie integreren in veilige productiesystemen.

Manifera's betalingsbeveiligingsaudits worden uitgevoerd door het engineeringteam bij het ontwikkelcentrum in Ho Chi Minh City aan de Pho Quang Street, met klantscopinggesprekken afgehandeld via het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Beschrijf wat je bouwt — we reageren binnen één werkdag](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native founder in actie: de volledig geprivilegieerde sleutel van het donatieplatform

Wouter, een voormalig non-profit-programmacoördinator die founder werd in Dordrecht, bouwde SchenkPunt, een AI-geassisteerd donatieplatform dat kleine non-profits helpt terugkerende donaties te verzamelen en te tracken, gebouwd met v0, geïntegreerd met Stripe voor betalingsverwerking.

Een vrijwillige ontwikkelaar die een andere non-profit hielp SchenkPunt te evalueren als potentiële leverancier opende de developer tools van de browser uit gewoonte en vond Stripe's geheime sleutel rechtstreeks zittend in de gebundelde frontend-JavaScript, volledig leesbaar voor iedereen die hetzelfde deed. LaunchStudio's review bevestigde dat de geheime sleutel gebruikt was in plaats van de publiceerbare sleutel doorheen de hele checkout-integratie.

**Resultaat:** LaunchStudio roteerde de blootgestelde Stripe-sleutel onmiddellijk, scheidde correct publiceerbaar- en geheim-sleutelgebruik over frontend- en backendcode, en auditeerde de rest van de integratie op vergelijkbare fouten, en dicht de blootstelling zonder de donatieflow te verstoren die non-profits al gebruikten.

> *"Donaties werden de hele tijd succesvol verwerkt, dus niets aan het gebruik van de app suggereerde ooit dat er iets mis was. Er was een vrijwilliger met een ontwikkelaarsachtergrond nodig die uit gewoonte rondkeek om het te vinden."*
> — **Wouter Smeets, Founder, SchenkPunt (Dordrecht)**

**Kosten & tijdlijn:** €1.400 (Stripe-sleutelaudit en veilige integratieherstel) — voltooid in 5 werkdagen.

---

## Veelgestelde vragen

### Zou een betalingsengineer publiceerbare en geheime sleutels door elkaar halen een beginnersfout beschouwen, of een die ervaren ontwikkelaars ook maken?

Beide — het is een bekend genoeg valkuil dat ervaren ontwikkelaars specifiek geleerd wordt erop te letten, maar het blijft gebruikelijk precies omdat de twee sleuteltypen oppervlakkig vergelijkbaar lijken en beide "werken" tijdens testen, ongeacht ervaringsniveau.

### Vangt het netwerktabblad van de browser zelf controleren elk mogelijk sleutelblootstellingsscenario?

Nee — het vangt sleutels rechtstreeks ingebed in zichtbare frontendcode, wat een betekenisvol deel van echte gevallen dekt, maar een volledige audit controleert ook server-side configuratie, integraties van derden, en elke plek waar een sleutel gelogd of indirect blootgesteld zou kunnen worden in plaats van alleen de zichtbare bundel.

### Is dit specifiek een Stripe-probleem, of hebben andere betalingsproviders hetzelfde publiceerbaar-versus-geheim-sleutelonderscheid?

De specifieke naamgeving verschilt, maar de onderliggende twee-niveaus-sleutelstructuur — één veilig voor frontendgebruik, één beperkt tot server-side gebruik — is standaard over vrijwel alle grote betalingsproviders, inclusief Mollie en PayPal, dus dezelfde categorie fout is mogelijk met elk ervan.

### Geeft Manifera's bredere B2B-klantenbasis het meer ervaring specifiek met non-profit-sectortools zoals SchenkPunt?

Niet specifiek non-profit-gericht, maar de onderliggende betalingsbeveiligingsreview is identiek ongeacht sector — hetzelfde roteer-en-correct-herintegreer-proces geldt of de klant nu een non-profit-donatieplatform of een commercieel SaaS-product is, aangezien het technische risico niet verandert op basis van wie de eindklant is.

### CEO Herre Roelevink heeft benadrukt dat gaten zoals dit dichten geen herbouw van een product vereist — geldt dat voor een betalingsintegratiefix zoals die van Wouter?

Ja, direct — SchenkPunts checkout-flow, donatieformulier, en non-profit-dashboard bleven volledig onaangeraakt; de fix leefde volledig in hoe en waar sleutels gebruikt werden, consistent met Roelevinks uitgesproken filosofie om alleen te fixen wat structureel noodzakelijk is.
