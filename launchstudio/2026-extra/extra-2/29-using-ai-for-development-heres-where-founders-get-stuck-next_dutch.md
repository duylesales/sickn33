---
Titel: "Gebruikt u AI voor ontwikkeling? Hier is waar oprichters vervolgens vastlopen"
Trefwoorden: ai for development, ai in development, ai coding, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native oprichter (Niet-technisch)
---

# Gebruikt u AI voor ontwikkeling? Hier is waar oprichters vervolgens vastlopen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Gebruikt u AI voor ontwikkeling? Hier is waar oprichters vervolgens vastlopen",
  "description": "Een directe blik op het specifieke punt waar oprichters die AI gebruiken voor ontwikkeling vervolgens vastlopen.",
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
  "datePublished": "2026-07-27",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/using-ai-for-development-heres-where-founders-get-stuck-next"
  }
}
</script>

Het gebruiken van AI voor ontwikkeling brengt een oprichter opmerkelijk ver voordat ze hun eerste echte muur raken. Die muur ziet er zelden uit als "de AI kon deze functie niet bouwen." Het ziet er meestal meer uit als: de functie werkt, een gebruiker meldde iets vreemds over zijn eigen account, en niemand kan precies uitleggen waarom een eenvoudige profiel-update hen iets liet wijzigen wat ze nooit verondersteld werden aan te kunnen raken.

## Waar de muur typisch verschijnt

De specifieke muur die veel oprichters raken omvat een update-eindpunt (update endpoint) – een profielbewerkingsformulier, een accountinstellingenpagina – die een bredere set velden van het verzoek accepteert dan het zichtbare formulier daadwerkelijk presenteert. Als het verzoek van een gebruiker velden kan bevatten voorbij wat de gebruikersinterface toont, en de backend slaat op welke velden er ook aanwezig zijn zonder ze te filteren, kan een verzoek dat is opgesteld om een extra veld te bevatten gegevens wijzigen die de UI nooit bedoelde bloot te stellen voor bewerking.

## Waarom dit een Mass Assignment-kwetsbaarheid wordt genoemd

Het patroon heeft een specifieke, gevestigde naam in software-engineering omdat het specifiek en terugkerend genoeg is om goed gedocumenteerd te zijn: een backend die "massaal toewijst" (mass assigns) welke velden een verzoek ook bevat rechtstreeks op een databaserecord, zonder een expliciete lijst van welke velden daadwerkelijk zijn toegestaan om te worden bijgewerkt via dat specifieke eindpunt. Het vertrouwt het verzoek om alleen ooit redelijke velden te bevatten – een aanname die standhoudt tijdens normaal door de UI gedreven gebruik en breekt op het moment dat een verzoek rechtstreeks wordt opgesteld.

## Waarom een werkend profielformulier hier geen geruststelling biedt

Het testen van een profielbewerkingsformulier door het daadwerkelijk te gebruiken – een naam wijzigen, een telefoonnummer bijwerken – stuurt alleen ooit de velden die dat specifieke formulier omvat. Dus het onthult nooit wat de backend zou doen met aanvullende velden die het formulier toevallig niet indient. De kloof gaat volledig over wat er mogelijk is buiten de eigen beperkingen van het formulier om. En niet over iets wat zichtbaar mis is met het formulier zelf. Een oprichter kan door elk afzonderlijk veld op het formulier klikken, bevestigen dat elk veld correct opslaat, en nog steeds niets leren over dit risico.

## Waarom een accountrol-veld het slechtst mogelijke veld is om onbeschermd te laten

Als een gebruikersrecord een rol- of machtigingsveld omvat – "lid," "beheerder," "moderator" – en dat veld is niet expliciet uitgesloten van wat een profiel-update kan wijzigen, kan een specifiek opgesteld verzoek potentieel dat veld rechtstreeks instellen. En zo verhoogde machtigingen verlenen zonder dat er ooit een legitiem autorisatieproces bij betrokken is. Zodra dat gebeurt zijn de gevolgen niet beperkt tot wat het pas verhoogde account vervolgens doet – een beheerder-niveau account heeft typisch zichtbaarheid in de gegevens van elke andere gebruiker. En dat maakt een enkele mass-assignment kloof op een enkel veld tot een loper voor het gehele product.

## Wat het herstellen hiervan vereist

Een correcte herstelling definieert expliciet welke velden elk specifiek eindpunt mag bijwerken – een toestemmingslijst (allow-list) in plaats van het accepteren van wat een verzoek toevallig bevat. Consequent toegepast over elk update-pad in een applicatie. [LaunchStudio](https://launchstudio.eu/en/) auditeert exact dit patroon over een gehele codebase, ondersteund door Manifera's 11+ jaar ervaring met backend-engineering gedisciplineerd toegepast op producten op oprichtersschaal.

Manifera's backend-beveiligingsaudits worden uitgevoerd door het engineeringteam in het ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat, met klantgesprekken afgehandeld via het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Praat met een ingenieur die met AI gegenereerde code begrijpt](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: De profiel-update die beheerderstoegang verleende

Lars, een voormalig wervingsbureau-recruiter die oprichter werd in Roosendaal, bouwde WerfMakelaar, een AI-ondersteund wervings- en detacheringsplatform gebouwd met Cursor, dat onderscheid maakt tussen standaard recruiter-accounts en beheerder-accounts met bredere platformtoegang.

Een partner die het platform namens Lars testte, ontdekte tijdens het inspecteren van verzoeken dat het profiel-update-eindpunt een rolveld accepteerde naast naam- en contactdetails. En dat het indienen van een verzoek met de rol ingesteld op "admin" daadwerkelijk het machtigingsniveau van het account wijzigde, zonder dat enige controle aan de serverzijde het voorkwam. LaunchStudio's beoordeling bevestigde dat het update-eindpunt elk veld dat in het verzoek aanwezig was opsloeg zonder enige toestemmingslijst-beperking.

**Resultaat:** LaunchStudio implementeerde een expliciete toestemmingslijst (allow-list) op elk update-eindpunt in WerfMakelaar, wat garandeert dat alleen bedoelde velden ooit gewijzigd kunnen worden via elk specifiek formulier, ongeacht wat een verzoek anders kan bevatten. Dit sloot het risico op escalatie van machtigingen platformbreed.

> *"Hij liet me zien wat hij gedaan had en ik begreep aanvankelijk oprecht niet waarom het überhaupt mogelijk was. Het was niet bij me opgekomen dat hetzelfde eindpunt dat een telefoonnummer-update afhandelt theoretisch ook beheerderstoegang uit kon delen."*
> — **Lars Verbeek, Oprichter, WerfMakelaar (Roosendaal)**

**Kosten en tijdlijn:** € 2.100 (mass assignment audit en implementatie van allow-lists over update-eindpunten) — voltooid in 7 werkdagen.

---

## Veelgestelde vragen

### Zou een specialist in backend-beveiliging mass assignment beschouwen als een veelvoorkomende klasse van kwetsbaarheden?

Ja, veelvoorkomend genoeg dat veel gevestigde web-frameworks ingebouwde mechanismen bevatten specifiek om het te voorkomen, hoewel die mechanismen actief geconfigureerd en correct gebruikt moeten worden.

### Geldt dit risico alleen voor velden zoals accountrollen?

Het is breder – elk veld dat een gebruiker niet rechtstreeks zou moeten kunnen wijzigen (accountsaldi, abonnementsstatus, eigendomsreferenties) draagt hetzelfde onderliggende risico.

### Helpt ervaring met backend-engineering om mass assignment problemen snel op te vangen?

Ja, omdat het patroon om naar te zoeken goed gedefinieerd en consistent is, ongeacht de specifieke applicatie.

### Past dit in de architectuurkloof die de CEO beschrijft?

Ja, precies – een profiel-update die correct werkt voor zijn bedoelde velden geeft geen zichtbare indicatie van wat het stilletjes nog meer zou kunnen accepteren.

### Kan mass assignment nog steeds gebeuren bij een framework dat ingebouwde bescherming biedt?

Ja, als de beschermende functie niet correct is ingeschakeld of geconfigureerd voor elk specifiek eindpunt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Mass Assignment là gì và tại sao nó lại nguy hiểm?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Là lỗi backend tự động cập nhật mọi field gửi lên từ request vào DB mà không lọc, cho phép user tự sửa các quyền hạn như admin."
      }
    },
    {
      "@type": "Question",
      "name": "Lỗi này có chỉ xảy ra ở field phân quyền (role/permission) không?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Không, nó ảnh hưởng tới mọi field nhạy cảm như số dư tài khoản, trạng thái thanh toán, hay ID người sở hữu."
      }
    },
    {
      "@type": "Question",
      "name": "Tại sao dùng framework hiện đại (như Laravel/NestJS) vẫn bị dính lỗi này?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vì framework chỉ cung cấp tính năng bảo vệ (như fillable/DTO validation), nếu lập trình viên không khai báo thì lỗi vẫn xảy ra."
      }
    },
    {
      "@type": "Question",
      "name": "Giải pháp triệt để cho lỗ hổng Mass Assignment là gì?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sử dụng whitelist (allow-list) khai báo rõ ràng các field được phép update cho từng API endpoint cụ thể."
      }
    },
    {
      "@type": "Question",
      "name": "Founder không biết về kỹ thuật làm sao phát hiện lỗi Mass Assignment?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cần quy trình kiểm toán API (security audit) kiểm tra trực tiếp payload gửi lên thay vì chỉ test qua giao diện UI thông thường."
      }
    },
    {
      "@type": "Question",
      "name": "Sửa lỗi Mass Assignment có mất nhiều thời gian không?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thường chỉ mất vài ngày để rà soát toàn bộ API endpoint và gắn validation/whitelist thích hợp."
      }
    }
  ]
}
</script>
