---
Titel: "Uw AI-prototype ziet er klaar uit. Hier is hoe u controleert of het dat daadwerkelijk is"
Trefwoorden: ai prototype, prototype ai, ai native, LaunchStudio, Manifera
Koperfase: Bewustzijn
Doelgroep: AI-Native oprichter (Niet-technisch)
---

# Uw AI-prototype ziet er klaar uit. Hier is hoe u controleert of het dat daadwerkelijk is

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Uw AI-prototype ziet er klaar uit. Hier is hoe u controleert of het dat daadwerkelijk is",
  "description": "Een gids voor oprichters om te controleren of hun AI-prototype oprecht klaar is voor productie.",
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
  "datePublished": "2026-07-25",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/your-ai-prototype-looks-done-how-to-check-if-it-actually-is"
  }
}
</script>

"Ziet er klaar uit" is een oprecht misleidend signaal, en het is het waard om eerlijk te zijn over waarom: een AI-prototype dat er strak uitziet, onmiddellijk reageert, en elke klik afhandelt die u persoonlijk maakt, is specifiek geoptimaliseerd om die indruk te wekken. Ongeacht wat er daadwerkelijk onder de motorkap gebeurt. Hier is een concrete manier om te beginnen met controleren of "ziet er klaar uit" en "is klaar" daadwerkelijk overeenkomen, gebruikmakend van de ontwikkelaars-tools van uw eigen browser als de eerste, gratis diagnose.

## Stap één: Open de ontwikkelaars-tools van uw browser en kijk naar het tabblad Netwerk

Elke moderne browser bevat een tabblad "Netwerk" (Network) of "Bronnen" (Sources) in zijn ontwikkelaars-tools. Dit toont elk verzoek dat uw app doet, en vaak ook het rauwe JavaScript-pakket (bundle) dat naar de browser wordt gestuurd. Dit is openbaar zichtbaar voor letterlijk iedereen die hetzelfde tabblad opent op uw live site – het is geen verborgen of geavanceerde hacking-techniek, maar een standaard, ingebouwde browserfunctie.

## Stap twee: Zoek in dat pakket naar alles wat lijkt op een geheime sleutel

Het doorzoeken van het zichtbare JavaScript-pakket naar tekenreeksen zoals "sk_" (een veelvoorkomend voorvoegsel voor geheime sleutels van Stripe), "secret," "private," of uw eigen bekende API-sleutelpatronen is een eenvoudige, directe manier om te controleren of een sleutel die alleen ooit op uw server zou moeten bestaan, in plaats daarvan gebundeld is geraakt in code die naar de browser van elke bezoeker wordt gestuurd.

## Stap drie: Begrijpen waarom deze specifieke fout zo veelvoorkomend is

Betalingsverwerkers zoals Stripe geven twee afzonderlijke soorten sleutels uit – een "gepubliceerde" (publishable) sleutel, veilig om te gebruiken in frontend-code, en een "geheime" (secret) sleutel, uitsluitend bedoeld voor gebruik aan de serverzijde. AI-coderingsassistenten die een snelle betalingsintegratie genereren gebruiken soms welke sleutel dan ook die in de prompt werd verstrekt, zonder onderscheid te maken tussen de twee. En als een oprichter de geheime sleutel plakt waar de openbare sleutel hoort, heeft de tool geen onafhankelijke manier om te weten dat het de verkeerde is.

De twee sleutels zitten vaak recht naast elkaar in het dashboard van een betalingsverwerker, beide gelabeld met vergelijkbaar uitziende voorvoegsels. Een oprichter die snel inloggegevens kopieert tijdens het instellen heeft geen sterke visuele prikkel die aanzet tot extra voorzichtigheid voordat hij er een in een frontend-configuratiebestand plakt. Tenzij een oprichter het onderscheid vooraf al begrijpt, is er niets aan het kopieer-plakmoment zelf dat signaleert dat er een fout plaatsvindt. Dit is exact waarom dit een van de meest voorkomende integratiefouten blijft, zelfs onder oprichters die voor het overige zorgvuldig zijn.

## Stap vier: Herkennen waarom een werkende betalingsstroom dit niet uitsluit

Een betalingsintegratie die de geheime sleutel rechtstreeks in de frontend-code gebruikt, zal in veel gevallen nog steeds testbetalingen met succes verwerken – de fout produceert niet noodzakelijkerwijs een foutmelding. Wat exact is waarom "het werkt" hier geen geruststellend bewijs is. Het risico is niet dat het niet functioneert; het is dat een volledig gemachtigde sleutel op een plek zit waar elke bezoeker hem kan lezen.

## Stap vijf: Krijg een systematische beoordeling, niet alleen een handmatige zoekopdracht

Een handmatige zoekopdracht vangt duidelijke gevallen op maar is niet uitputtend – een correcte audit controleert elke integratie systematisch, bevestigt dat het correcte sleuteltype wordt gebruikt in elke context, en verifieert dat geen andere geheimen hetzelfde patroon hebben gevolgd. [LaunchStudio](https://launchstudio.eu/nl/) voert exact dit soort systematische audit van sleutels en geheimen uit als een standaard eerste stap in haar beoordeling van productiegereedheid, ondersteund door Manifera's 11+ jaar ervaring met het integreren van Stripe en Mollie in veilige productiesystemen.

Manifera's beveiligingsaudits voor betalingen worden uitgevoerd door het engineeringteam in het ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat, met klantgesprekken afgehandeld via het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Beschrijf wat u bouwt — we antwoorden binnen één werkdag](https://launchstudio.eu/nl/#contact).

## Verder Dan Stripe-Sleutels: Een Volledige Frontend-Bundel Audit

Het controleren op een gelekte geheime Stripe-sleutel (`sk_live_`) is een uitstekende eerste stap, maar dezelfde onderliggende fout — een servergeheim dat per ongeluk terechtkomt in de publieke JavaScript-code die naar elke browser wordt gestuurd — doet zich voor bij tal van andere diensten.

**Doorzoek uw client-bundel specifiek op deze patronen:**

- **Supabase Service Role Keys:** Een `service_role` sleutel omzeilt Row-Level Security volledig. Als deze per ongeluk wordt gebruikt op de plek waar de publieke `anon` sleutel hoort, kan elke bezoeker uw volledige database uitlezen en wissen.
- **AWS Toegangsreferenties:** Een Access Key ID en Secret Access Key bedoeld voor server-side beheer die tijdens een snelle test hardcoded in een component zijn achtergebleven.
- **Database-Connectiestrings:** Een complete verbindings-URL inclusief gebruikersnaam en wachtwoord, soms direct in de frontend geplakt om "even snel data te laten zien".
- **AI-Provider API-Sleutels:** OpenAI- of Anthropic-tokens met verhoogde bevoegdheden die direct vanuit de browser worden aangeroepen, waardoor kwaadwillenden op uw kosten modellen kunnen aanroepen.

**Onthoud: "Verwijderd uit de code" betekent nog niet "veilig"**

Als u een geheim ontdekt in de frontend en het verwijdert via een nieuwe commit, moet u de sleutel direct intrekken en roteren bij de betreffende leverancier. De oude versie van de JavaScript-bundel kan immers nog wekenlang gecached staan in browsers van bezoekers, bewaard zijn door een CDN, of al gekopieerd zijn door geautomatiseerde webscrapers.

**Bouw de geheimen-check in als geautomatiseerde stap in uw uitrolproces**

Een eenmalige controle vóór lancering biedt geen garantie voor wijzigingen die drie maanden later worden doorgevoerd. Voeg een eenvoudig pre-commit script of een GitHub Action toe die uw broncode automatisch scant op bekende tokenpatronen vóórdat een build naar productie mag worden uitgerold.

## Echt voorbeeld

### Een AI-native oprichter in actie: De gemachtigde sleutel van het donatieplatform

Wouter, een voormalig programmacoördinator bij een non-profit die oprichter werd in Dordrecht, bouwde SchenkPunt, een AI-ondersteund donatieplatform dat kleine non-profits helpt terugkerende donaties te verzamelen en te volgen. Het werd gebouwd met v0, geïntegreerd met Stripe voor betalingsverwerking.

Een ontwikkelaar die op vrijwillige basis een andere non-profit hielp om SchenkPunt als mogelijke leverancier te evalueren, opende uit gewoonte de ontwikkelaars-tools van zijn browser. Hij vond Stripe's geheime sleutel rechtstreeks in het gebundelde frontend JavaScript, volledig leesbaar voor iedereen die hetzelfde deed. LaunchStudio's beoordeling bevestigde dat de geheime sleutel door het gehele afrekenproces was gebruikt in plaats van de openbare sleutel.

**Resultaat:** LaunchStudio roteerde de blootgestelde Stripe-sleutel onmiddellijk, scheidde het gebruik van de openbare en geheime sleutel correct over de frontend- en backend-code, en auditeerde de rest van de integratie op vergelijkbare fouten. Dit sloot de blootstelling zonder de donatiestroom die non-profits al gebruikten te verstoren.

> *"Donaties werden de gehele tijd met succes verwerkt, dus niets aan het gebruik van de app suggereerde ooit dat er iets mis was. Er was een vrijwilliger met een ontwikkelaarsachtergrond voor nodig die uit gewoonte rondkeek om het te vinden."*
> — **Wouter Smeets, Oprichter, SchenkPunt (Dordrecht)**

**Kosten en tijdlijn:** € 1.400 (Stripe-sleutelaudit en herstel van veilige integratie) — voltooid in 5 werkdagen.

---

## Veelgestelde vragen

### Zou een betalingsingenieur het verwarren van openbare en geheime sleutels beschouwen als een fout voor beginners?

Beide – het is een bekende valkuil waar ervaren ontwikkelaars specifiek voor worden geleerd om op te letten, maar het blijft veelvoorkomend omdat de twee sleuteltypen er oppervlakkig vergelijkbaar uitzien en beide "werken" tijdens het testen.

### Vangt het zelf controleren van het tabblad Netwerk van de browser elke mogelijke sleutelblootstelling op?

Nee – het vangt sleutels op die rechtstreeks in zichtbare frontend-code zijn ingebed, maar een volledige audit controleert ook de serverconfiguratie.

### Is het onderscheid tussen openbare en geheime sleutels specifiek voor Stripe?

Nee, dezelfde twee-laags sleutelstructuur is standaard over vrijwel alle grote betalingsverwerkers, inclusief Mollie en PayPal.

### Vereist het herstellen van een integratiefout zoals deze het herbouwen van de app?

Nee, direct – Wouter's afrekenstroom en formulieren bleven volledig ongeraakt. De herstelling leefde volledig in hoe en waar sleutels gebruikt werden.

### Wat moet een oprichter doen zodra een geheim in de frontend wordt gevonden?

De sleutel moet onmiddellijk in het dashboard van de provider worden geroteerd (invalideren en nieuw genereren). Het simpelweg verwijderen uit de code beschermt niet tegen eerdere lekken.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Zou een betalingsingenieur het verwarren van openbare en geheime sleutels beschouwen als een fout voor beginners?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Beide – het is een bekende valkuil waar ervaren ontwikkelaars specifiek voor worden geleerd om op te letten, maar het blijft veelvoorkomend omdat de twee sleuteltypen er oppervlakkig vergelijkbaar uitzien en beide \"werken\" tijdens het testen."
      }
    },
    {
      "@type": "Question",
      "name": "Vangt het zelf controleren van het tabblad Netwerk van de browser elke mogelijke sleutelblootstelling op?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee – het vangt sleutels op die rechtstreeks in zichtbare frontend-code zijn ingebed, maar een volledige audit controleert ook de serverconfiguratie."
      }
    },
    {
      "@type": "Question",
      "name": "Is het onderscheid tussen openbare en geheime sleutels specifiek voor Stripe?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, dezelfde twee-laags sleutelstructuur is standaard over vrijwel alle grote betalingsverwerkers, inclusief Mollie en PayPal."
      }
    },
    {
      "@type": "Question",
      "name": "Vereist het herstellen van een integratiefout zoals deze het herbouwen van de app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, direct – Wouter's afrekenstroom en formulieren bleven volledig ongeraakt. De herstelling leefde volledig in hoe en waar sleutels gebruikt werden."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet een oprichter doen zodra een geheim in de frontend wordt gevonden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De sleutel moet onmiddellijk in het dashboard van de provider worden geroteerd (invalideren en nieuw genereren). Het simpelweg verwijderen uit de code beschermt niet tegen eerdere lekken."
      }
    }
  ]
}
</script>
