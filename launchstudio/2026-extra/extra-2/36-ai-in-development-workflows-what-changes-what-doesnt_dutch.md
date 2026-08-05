---
Titel: "AI in ontwikkelingswerkstromen: Wat verandert er, wat niet"
Trefwoorden: ai in development, ai for development, ai coding, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie Hacker
---

# AI in ontwikkelingswerkstromen: Wat verandert er, wat niet

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI in ontwikkelingswerkstromen: Wat verandert er, wat niet",
  "description": "Een technische verdieping in het risico van Server-Side Request Forgery (SSRF) geïntroduceerd door een handige functie voor het importeren vanaf een URL.",
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
  "datePublished": "2026-07-29",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/ai-in-development-workflows-what-changes-what-doesnt"
  }
}
</script>

AI in ontwikkelingswerkstromen verandert hoe snel een functie gebouwd wordt. Het verandert niet waar die functie fundamenteel toe in staat is zodra deze live is – en een handige functie voor het "importeren van een productafbeelding vanaf een URL", snel en correct gebouwd om aan exact die beschrijving te voldoen, is fundamenteel tot aanzienlijk meer in staat dan het tonen van een afbeelding. Tenzij iets het specifiek stopt.

## Wat een functie "Importeren vanaf URL" daadwerkelijk onder de motorkap doet

Een functie waarmee een gebruiker een URL kan plakken en uw server ophaalt wat er op dat adres staat – een afbeelding, een document, een bron – betekent noodzakelijkerwijs dat uw eigen server degene is die dat uitgaande verzoek doet, en niet de browser van de gebruiker. Dit is een oprecht handig patroon, en AI-coderingsassistenten implementeren het gemakkelijk wanneer een oprichter dit soort functionaliteit beschrijft.

## Waarom "uw server haalt het op" het specifieke risico is

Als de URL die een gebruiker verstrekt op geen enkele wijze beperkt is, is er niets wat een verzoek stopt om zich te richten op interne netwerkadressen die uw server kan bereiken maar het openbare internet niet. Denk aan interne beheerderspanelen, cloud-metadatadiensten, of andere backend-systemen die nooit bedoeld waren om van buitenaf bereikbaar te zijn.

## Waarom dit Server-Side Request Forgery wordt genoemd

De naam beschrijft exact wat er gebeurt: een verzoek wordt vervalst (opgesteld door een externe partij) maar server-side uitgevoerd (door uw eigen vertrouwde infrastructuur). Dit geeft een aanvaller een manier om te peilen of te communiceren met interne systemen met behulp van de eigen netwerkpositie en het vertrouwensniveau van uw server.

## Waarom het testen met echte afbeeldings-URL's dit nooit onthult

Het testen van een functie voor het importeren vanaf een URL door het plakken van echte, externe afbeeldingslinks bevestigt dat de functie openbare afbeeldingen correct ophaalt. Het biedt nul informatie over wat er gebeurt als iemand in plaats daarvan een intern netwerkadres verstrekt.

## Wat het op de juiste manier beperken van deze functie vereist

Een veilige implementatie valideert dat een verstrekte URL resolvet naar een oprecht openbaar, extern adres voordat het wordt opgehaald. Het blokkeert expliciet verzoeken naar interne of gereserveerde netwerkbereiken. [LaunchStudio](https://launchstudio.eu/en/) implementeert exact dit soort URL-validatie als onderdeel van haar beoordeling van backend-beveiliging, ondersteund door Manifera's 11+ jaar ervaring met het beveiligen van integraties aan de serverzijde.

Manifera's beveiligingswerk voor SSRF en backend-integraties wordt geleverd via het ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat, gecoördineerd met het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Praat met een ingenieur die met AI gegenereerde code begrijpt](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: De afbeeldingsimport die te ver reikte

Wessel, een voormalig logistiek coördinator die oprichter werd in Vlaardingen, bouwde VoorraadVast, een AI-ondersteunde tool voor magazijnvoorraadbeheer gebouwd met Cursor, inclusief een handige functie waarmee magazijnmedewerkers een productfoto rechtstreeks vanaf een opgegeven URL kunnen importeren in plaats van handmatig een bestand te uploaden.

Een IT-contactpersoon van een partner die VoorraadVast beoordeelde voorafgaand aan een mogelijke integratie, testte de importfunctie met een intern netwerkadres in plaats van een openbare afbeeldings-URL. Hij vond dat de server probeerde op te halen en terug te sturen wat het daar vond – wat bevestigde dat de functie geen beperking had op wat voor soort adres het zou benaderen. LaunchStudio's beoordeling bevestigde dat de onderliggende ophaallogica elke URL accepteerde en opvroeg zonder te valideren dat het een oprecht openbare bestemming was.

**Resultaat:** LaunchStudio voegde strikte validatie toe die garandeert dat de importfunctie alleen ophaalt van geverifieerde openbare, externe adressen. Dit blokkeert expliciet elk verzoek gericht op interne of gereserveerde netwerkbereiken, wat de blootstelling sloot zonder te veranderen hoe medewerkers de importfunctie gebruikten.

> *"Ik bouwde die functie om medewerkers een paar kliks te besparen bij het importeren van productfoto's. Het was geen moment in me opgekomen dat hetzelfde gemak theoretisch gericht kon worden op iets wat compleet anders was dan een foto."*
> — **Wessel Kramer, Oprichter, VoorraadVast (Vlaardingen)**

**Kosten en tijdlijn:** € 2.600 (SSRF-herstel en URL-ophaalvalidatie) — voltooid in 8 werkdagen.

---

## Veelgestelde vragen

### Zou een specialist in backend-beveiliging SSRF beschouwen als een veelvoorkomende bevinding in met AI gegenereerde code?

Zeker – het ophalen van een bron vanaf een URL die de gebruiker verstrekt is zo'n natuurlijke functiebeschrijving dat het vaak wordt ingebouwd zonder de vereiste extra beveiligingslaag.

### Geldt dit risico alleen voor functies die expliciet worden beschreven als "importeren vanaf URL"?

Het verschijnt in elke functie waar gebruikersinvoer een uitgaand verzoek aan de serverzijde beïnvloedt (webhook callback-URL's, PDF-generatiediensten).

### Maakt ervaring met enterprise-integraties uit voor een kleinere magazijntool?

Ja, rechtstreeks – het specifieke validatiepatroon is identiek, ongeacht de grootte van de organisatie.

### Past een SSRF-kloof in het kader van architectuur boven loutere functionaliteit?

Heel goed – de importfunctie werkte exact zoals beschreven. Het ontbrekende stuk was een architecturale beslissing over wat de server wel en niet mocht bereiken.

### Biedt het blokkeren van voor de hand liggende interne IP-bereiken voldoende bescherming?

Slechts gedeeltelijk – DNS-rebinding, omleidingsketens, en de cloud-metadata-endpoint vereisen allemaal aanvullende, afzonderlijke afhandeling.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Lỗi SSRF (Server-Side Request Forgery) là gì?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Lỗi cho phép kẻ xấu truyền URL nội bộ vào tính năng nhập từ link, khiến Server tự mình gửi request truy cập vào các mạng nội bộ bảo mật."
      }
    },
    {
      "@type": "Question",
      "name": "Tại sao lỗi SSRF hay xuất hiện trong code do AI viết?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vì prompt yêu cầu 'tải ảnh từ URL' thì AI chỉ viết code fetch đơn thuần, không tự động thêm logic validate IP nội bộ."
      }
    },
    {
      "@type": "Question",
      "name": "Hậu quả nghiêm trọng nhất của lỗi SSRF là gì?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Kẻ tấn công có thể truy cập vào AWS/Cloud Metadata Endpoint để lấy token quản trị Server hoặc đọc dữ liệu DB nội bộ."
      }
    },
    {
      "@type": "Question",
      "name": "Chỉ chặn các dải IP nội bộ (192.168.x.x, 10.x.x.x) có đủ để chống SSRF không?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Chưa đủ — cần chặn cả DNS Rebinding, Redirect chains, các định dạng IP Hex/Octal và chặn trực tiếp Metadata URL."
      }
    },
    {
      "@type": "Question",
      "name": "Những tính năng nào ngoài Import URL hay dính lỗi SSRF?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Webhook callbacks, tính năng xem trước link (Link preview), và dịch vụ tạo file PDF từ HTML/URL."
      }
    },
    {
      "@type": "Question",
      "name": "Sửa lỗi SSRF có làm ảnh hưởng tới việc tải ảnh từ các trang web hợp lệ không?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Không, Server vẫn tải ảnh bình thường từ các domain public hợp lệ, chỉ từ chối các request hướng vào mạng nội bộ."
      }
    }
  ]
}
</script>
