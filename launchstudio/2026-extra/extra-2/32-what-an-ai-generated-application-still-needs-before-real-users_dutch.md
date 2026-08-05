---
Titel: "Wat een met AI gegenereerde applicatie nog steeds nodig heeft voordat echte gebruikers arriveren"
Trefwoorden: ai generated application, ai generated tool, ai coding, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: SaaS-oprichter Scale-Up
---

# Wat een met AI gegenereerde applicatie nog steeds nodig heeft voordat echte gebruikers arriveren

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wat een met AI gegenereerde applicatie nog steeds nodig heeft voordat echte gebruikers arriveren",
  "description": "Een technische verdieping in het afhandelen van sessie-tokens, gefocust op onjuist geverifieerde JWT's.",
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
  "datePublished": "2026-07-28",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/what-an-ai-generated-application-still-needs-before-real-users"
  }
}
</script>

Een met AI gegenereerde applicatie die inlogs van betaalde abonnees afhandelt krijgt het zichtbare gedeelte van authenticatie typisch bij de eerste poging al goed – een inlogformulier dat geldige inloggegevens accepteert en ongeldige weigert. Wat frequent niet dezelfde controle krijgt is het token dat de inlog daadwerkelijk achteraf uitgeeft. En specifiek of dat token op de juiste manier geverifieerd is, correct afgebakend is, en ingesteld is om daadwerkelijk te verlopen.

## Wat een JWT-token verondersteld wordt te garanderen

Een JSON Web Token (JWT), algemeen gebruikt om een ingelogde sessie te vertegenwoordigen, is cryptografisch ondertekend. Zodat een server kan verifiëren dat er niet mee geknoeid is en dat het oprecht afkomstig is van een legitieme inlog. Die garantie houdt alleen stand als de server de handtekening op elk verzoek daadwerkelijk verifieert – een token dat simpelweg wordt gedecodeerd en gelezen, zonder dat de handtekening wordt gecontroleerd, biedt überhaupt geen echte beveiligingsgarantie.

## Waarom het overslaan van handtekeningverificatie een makkelijke, onzichtbare fout is

Het decoderen van een JWT om de inhoud ervan te lezen (welke gebruiker, welke machtigingen) is een eenvoudige, veelvoorkomende handeling. Code die een token correct decodeert kan tijdens het testen perfect lijken te werken – een legitiem uitgegeven token decodeert elke keer naar de correcte, verwachte informatie. De afzonderlijke stap van het daadwerkelijk verifiëren dat de handtekening van het token geldig is produceert tijdens normaal, eerlijk gebruik geen enkel ander zichtbaar resultaat.

## Waarom deze kloof ernstig wordt op het moment dat iemand zijn eigen token opstelt

Als handtekeningverificatie wordt overgeslagen, hoeft een token überhaupt niet legitiem te zijn uitgegeven – iedereen die de basisstructuur van het token begrijpt kan zijn eigen token construeren en beweren elke willekeurige gebruiker of elk machtigingsniveau te zijn. Een server die alleen decodeert zonder te verifiëren zal een zelf opgesteld token als echt accepteren.

## Waarom verloop een afzonderlijk, even belangrijk onderdeel is

Voorbij handtekeningverificatie heeft een token een redelijke vervaltijd nodig waarna het niet langer geaccepteerd wordt. Zonder dit blijft een eenmaal buitgemaakt token voor onbepaalde tijd bruikbaar. Een sessietoken dat op de dag van de productlancering is uitgegeven en een jaar later nog steeds stilletjes geldig is, is het standaardresultaat van het nooit hebben ingesteld van een vervaldatum.

## Wat een complete herstelling inhoudt

Een correcte implementatie verifieert de handtekening van elk token bij elk verzoek, dwingt een redelijke vervaltijd af met een werkend verversingsmechanisme (refresh flow), en weigert alles wat voor een van beide controles zakt. [LaunchStudio](https://launchstudio.eu/en/) auditeert exact dit patroon als onderdeel van haar authenticatie-beoordelingsproces, ondersteund door Manifera's 11+ jaar ervaring met Auth0, Supabase Auth, en op maat gemaakte op JWT gebaseerde systemen.

Manifera's audits voor sessie- en tokenbeveiliging worden uitgevoerd door het engineeringteam in het ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat, gecoördineerd met het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Praat met een ingenieur die met AI gegenereerde code begrijpt](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: Het abonneetoken dat nooit verliep

Britt, een voormalig tijdschriftredacteur die oprichter werd in Hoorn, bouwde LeesKring, een AI-ondersteund platform voor nieuwsbrieven en kwaliteitsjournalistiek gebouwd met Lovable, dat artikelen afschermt achter een betaalde abonnees-inlog.

De oude sessie van een vertrokken teamlid, die maanden eerder tijdens de ontwikkeling werd gebruikt, verleende nog steeds volledige toegang op een apparaat waarvan niemand zich herinnerde dat het ooit was ingelogd. Britt ontdekte het alleen omdat ze toevallig ongebruikelijke activiteit opmerkte tijdens het beoordelen van de statistieken. LaunchStudio's beoordeling vond dat de tokens van het platform überhaupt geen vervaldatum hadden ingesteld. En erger nog: dat de server tokens alleen decodeerde om de inhoud te lezen, zonder ooit de cryptografische handtekening te verifiëren.

**Resultaat:** LaunchStudio implementeerde een correcte handtekeningverificatie bij elk verzoek en voegde een redelijke tokenvervaldatum toe met een werkende verversingsstroom. Dit sloot zowel het risico op vervalsing als het risico op een onbeperkte sessie.

> *"Ik kwam er bijna per ongeluk achter, puur door iets op te merken in de statistieken wat niet helemaal logisch was. Er was geen foutmelding of waarschuwing die me op zichzelf verteld zou hebben dat dit überhaupt een mogelijkheid was."*
> — **Britt Hendriks, Oprichter, LeesKring (Hoorn)**

**Kosten en tijdlijn:** € 2.300 (JWT-verificatie en uitharding van sessieverloop) — voltooid in 7 werkdagen.

---

## Veelgestelde vragen

### Zou een specialist in toegang en identiteit het overslaan van handtekeningverificatie beschouwen als een subtiele fout?

Subtiel specifiek vanwege hoe het zich presenteert tijdens het testen – een legitiem uitgegeven token decodeert correct of de handtekening nu daadwerkelijk gecontroleerd wordt of niet.

### Elimineert het gebruik van een bekende provider zoals Auth0 of Supabase Auth dit risico volledig?

Het vermindert het risico aanzienlijk wanneer de eigen bibliotheken en aanbevolen verificatiestroom correct gebruikt worden, maar op maat gemaakte logica die er bovenop gebouwd wordt kan dezelfde kloof herintroduceren.

### Maakt ervaring met authenticatie-systemen uit voor een nieuwsbriefplatform?

De onderliggende principes van tokenbeveiliging zijn identiek over alle industrieën heen.

### Past deze casus in het kader van onzichtbare beveiligingskloven die de CEO beschrijft?

Zo goed als een voorbeeld maar kan – Britt ontdekte het probleem door puur toeval zonder dat enige foutmelding of zichtbaar symptoom er naar wees.

### Moet een oprichter zijn AI-tool specifiek vragen of het JWT-handtekeningen verifieert?

Het is een redelijke, specifieke vraag om te stellen, hoewel het vertrouwen op alleen dat antwoord zonder een onafhankelijke technische review geen vervanging is voor verificatie.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Bỏ qua bước verify chữ ký JWT (Signature Verification) nguy hiểm thế nào?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Rất nguy hiểm — Server sẽ nhận diện bất kỳ token nào (kể cả token do kẻ xấu tự tạo ra) chỉ cần nó có đúng định dạng JSON."
      }
    },
    {
      "@type": "Question",
      "name": "Tại sao khi test bình thường founder không bao giờ phát hiện ra lỗi JWT này?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vì token hợp lệ vẫn giải mã (decode) ra đúng thông tin user, giao diện vẫn chạy bình thường cho đến khi có kẻ cố tình làm giả token."
      }
    },
    {
      "@type": "Question",
      "name": "Dùng Auth0 hoặc Supabase Auth có tự động chống được lỗi này không?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Mặc định SDK của họ có verify, nhưng nếu lập trình viên tự viết thêm middleware đọc token riêng thì vẫn dễ bỏ quên bước verify."
      }
    },
    {
      "@type": "Question",
      "name": "Thời hạn hết hạn (Expiration) của JWT token nên đặt là bao lâu?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nên đặt thời gian ngắn (ví dụ 15-60 phút) kèm cơ chế Refresh Token để vừa an toàn vừa giữ đăng nhập mượt mà cho user."
      }
    },
    {
      "@type": "Question",
      "name": "Lưu trữ JWT token ở đâu ở phía client là an toàn nhất?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Lưu trong httpOnly, Secure Cookie thay vì localStorage để tránh bị lấy cắp qua các lỗi XSS."
      }
    },
    {
      "@type": "Question",
      "name": "Sửa lỗi verify JWT có bắt buộc phải bắt toàn bộ user đăng nhập lại không?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Có thể thu hồi (revoke) các token cũ không hợp lệ để bắt buộc cấp token mới có chữ ký chuẩn và thời hạn rõ ràng."
      }
    }
  ]
}
</script>
