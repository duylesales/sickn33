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
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/your-ai-prototype-looks-done-how-to-check-if-it-actually-is"
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

Een handmatige zoekopdracht vangt duidelijke gevallen op maar is niet uitputtend – een correcte audit controleert elke integratie systematisch, bevestigt dat het correcte sleuteltype wordt gebruikt in elke context, en verifieert dat geen andere geheimen hetzelfde patroon hebben gevolgd. [LaunchStudio](https://launchstudio.eu/en/) voert exact dit soort systematische audit van sleutels en geheimen uit als een standaard eerste stap in haar beoordeling van productiegereedheid, ondersteund door Manifera's 11+ jaar ervaring met het integreren van Stripe en Mollie in veilige productiesystemen.

Manifera's beveiligingsaudits voor betalingen worden uitgevoerd door het engineeringteam in het ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat, met klantgesprekken afgehandeld via het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Beschrijf wat u bouwt — we antwoorden binnen één werkdag](https://launchstudio.eu/en/#contact).

## Voorbij Stripe-sleutels: Een volledigere audit van uw frontend-pakket

Het controleren op een blootgestelde geheime sleutel van Stripe is een goede eerste stap, maar dezelfde onderliggende fout – een inloggegeven uitsluitend voor de server dat belandt in code die naar de browser van elke bezoeker wordt gestuurd – kan ook bij meerdere andere diensten gebeuren.

**Zoek ook in uw pakket naar deze patronen**

- **Supabase**: een `service_role` sleutel (die rij-niveau beveiliging/Row Level Security volledig omzeilt) per ongeluk gebruikt waar de beperkte `anon` sleutel hoort
- **AWS inloggegevens**: een toegangssleutel en geheim koppel bedoeld voor server-side SDK-aanroepen, af en toe hardcoded tijdens een snelle integratie
- **Database verbindings-tekenreeksen**: een volledige verbindings-URL, inclusief gebruikersnaam en wachtwoord, soms rechtstreeks gebruikt in frontend-code tijdens het vroege prototypen
- **API-sleutels van derden met verhoogde machtigingen**: elke dienst die zowel een beperkte, frontend-veilige sleutel als een sleutel met volledigere toegang biedt

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
      "name": "Nhầm lẫn giữa publishable key và secret key có phải lỗi của người mới?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Không chỉ người mới, lập trình viên có kinh nghiệm cũng dễ nhầm vì cả 2 key đều trông giống nhau và đều chạy được khi test."
      }
    },
    {
      "@type": "Question",
      "name": "Tự kiểm tra tab Network của trình duyệt có bắt được 100% key lộ không?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Không hoàn toàn — nó bắt được key nhúng ở frontend, nhưng audit chuyên nghiệp còn kiểm tra cả cấu hình server và log gián tiếp."
      }
    },
    {
      "@type": "Question",
      "name": "Phân biệt publishable và secret key có chỉ có ở Stripe không?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Không, cấu trúc key 2 lớp này là chuẩn chung của hầu hết cổng thanh toán như Mollie, PayPal, Braintree."
      }
    },
    {
      "@type": "Question",
      "name": "Khắc phục lỗi lộ Stripe secret key có cần viết lại ứng dụng không?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Không, giao diện và luồng checkout giữ nguyên 100%, chỉ cần đưa secret key về xử lý ở backend server."
      }
    },
    {
      "@type": "Question",
      "name": "Cần làm gì ngay lập tức khi phát hiện secret key bị dính vào frontend code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Rotate (thu hồi key cũ, tạo key mới) ngay trên dashboard của provider và xóa key khỏi frontend codebase."
      }
    },
    {
      "@type": "Question",
      "name": "Các secret nào khác hay bị nhầm lẫn đưa vào frontend ngoài Stripe key?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Supabase service_role key, AWS secret access key, và Database connection strings chứa username/password."
      }
    }
  ]
}
</script>
