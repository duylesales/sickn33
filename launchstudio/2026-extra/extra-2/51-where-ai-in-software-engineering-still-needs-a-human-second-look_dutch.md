---
Titel: "Waar AI in software-engineering nog steeds een menselijke tweede blik nodig heeft"
Trefwoorden: ai in software engineering, ai software engineering, ai coding, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie Hacker
---

# Waar AI in software-engineering nog steeds een menselijke tweede blik nodig heeft

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Waar AI in software-engineering nog steeds een menselijke tweede blik nodig heeft",
  "description": "Een technische verdieping in verouderde algortimen voor wachtwoord-hashing die stilletjes door een AI-coderingsassistent zijn gegenereerd.",
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
  "datePublished": "2026-08-02",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/where-ai-in-software-engineering-still-needs-a-human-second-look"
  }
}
</script>

AI in software-engineering is opmerkelijk goed geworden in het snel produceren van code die herkenbare, veelvoorkomende patronen volgt – inclusief patronen die ooit de standaardpraktijk waren, maar sindsdien zijn vervangen door betere alternatieven. Een implementatie voor het hashen van wachtwoorden is een specifieke, concrete plek waar dit verschijnt: technisch functioneel, technisch "het wachtwoord hashend", en technisch een algoritme gebruikend waar de beveiligingscommunity al jaren geleden afstand van heeft genomen.

## Waarom niet alle hash-algoritmen dezelfde bescherming bieden

Het hashen van een wachtwoord, in plaats van het opslaan in platte tekst, is een oprecht correcte en belangrijke praktijk. Maar niet alle hash-algoritmen bieden gelijke bescherming tegen moderne kraaktechnieken. Algoritmen die decennia geleden zijn ontworpen voor algemene snelheid, kunnen extreem snel worden berekend door een aanvaller met moderne hardware. Dit maakt een gestolen hash aanzienlijk gemakkelijker te herleiden dan een hash geproduceerd door een algoritme dat specifiek ontworpen is om traag en bronintensief te zijn.

## Waarom een AI-tool naar een verouderd algoritme kan grijpen

Trainingsdata weerspiegelt code die over vele jaren is geschreven, inclusief een aanzienlijke hoeveelheid oudere code die algoritmen gebruikt die redelijke keuzes waren op het moment dat ze geschreven werden. Zonder specifieke instructies heeft een AI-tool geen ingebouwde voorkeur die het wegleidt van een patroon dat frequent verschijnt en historisch normaal was.

## Waarom deze specifieke kloof onzichtbaar is in elke functionele test

Een wachtwoord dat gehashed is met een verouderd algoritme hasht nog steeds correct, staat nog steeds correcte inlogverificatie toe, en slaagt voor elke functionele test. De zwakheid wordt pas relevant in het geval van een database-inbreuk, wanneer het specifieke algoritme bepaalt hoe snel een aanvaller de gestolen hashes kan herleiden.

## Waarom "het is gehashed, dus het is prima" een incomplete aanname is

Oprichters zonder beveiligingsachtergrond associëren "gehashed" redelijkerwijs met "veilig", aangezien hashen inderdaad dramatisch veiliger is dan opslag in platte tekst. Maar het specifieke algoritme maakt nog steeds aanzienlijk uit.

## Wat het op de juiste manier upgraden hiervan inhoudt

Een correcte herstelling vervangt een verouderd hash-algoritme door een modern, speciaal gebouwd algoritme (zoals bcrypt, scrypt, of Argon2id), en migreert alle bestaande opgeslagen hashes zorgvuldig zonder dat gebruikers verstoord worden door verplicht hun wachtwoord te herstellen. [LaunchStudio](https://launchstudio.eu/en/) controleert op exact dit patroon als onderdeel van haar beoordeling van authenticatiebeveiliging, ondersteund door Manifera's 11+ jaar ervaring met moderne cryptografische praktijken.

Manifera's beoordelingen van cryptografie en authenticatie worden uitgevoerd door het engineeringteam in het ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat, gecoördineerd met het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Praat met een ingenieur die met AI gegenereerde code begrijpt](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: Het hash-algoritme dat een decennium achterliep

Twan, een voormalig bruiloftsfotograaf die oprichter werd in Barneveld, bouwde FotoBoeking, een AI-ondersteund platform voor het boeken van fotostudio's gebouwd met Cursor, dat klantaccounts en boekingsgeschiedenis opslaat achter een standaard inlog.

Een vriend die fotograaf is met een baan in cybersecurity bekeek FotoBoeking's code uit professionele nieuwsgierigheid en opmerkte dat de wachtwoord-hashing-implementatie een algoritme gebruikte (zoals ongezouten MD5 of SHA-1) dat lang als onvoldoende werd beschouwd. LaunchStudio's vervolgbeoordeling bevestigde dat het algoritme functioneel correct werkte, maar betekenisvol zwakkere bescherming bood tegen een potentiële toekomstige database-inbreuk.

**Resultaat:** LaunchStudio upgrade de wachtwoord-hashing van FotoBoeking naar een modern algoritme en implementeerde een veilig migratiepad voor bestaande accounts. Dit sloot de kloof zonder dat er verplichte wachtwoord-resets nodig waren voor huidige gebruikers.

> *"Elke inlog werkte de hele tijd perfect, dus er was oprecht niets dat suggereerde dat er iets mis was. Er was een vriend voor nodig die toevallig exact wist waar hij naar moest kijken om het überhaupt op te merken."*
> — **Twan Meijer, Oprichter, FotoBoeking (Barneveld)**

**Kosten en tijdlijn:** € 2.100 (upgrade van wachtwoord-hashing en veilige accountmigratie) — voltooid in 7 werkdagen.

---

## Veelgestelde vragen

### Zou een cryptografiespecialist dit beschouwen als een urgent risico of een verbetering?

Het wordt over het algemeen behandeld als een betekenisvolle, waardevolle herstelling. Het risico wordt pas werkelijkheid bij een inbreuk, maar het gebruik van een modern algoritme is de standaard aanbevolen praktijk.

### Beïnvloedt deze kloof alleen op maat gemaakte authenticatie?

Het is aanzienlijk minder waarschijnlijk bij gevestigde providers zoals Auth0 of Supabase Auth. Het risico is specifiek hoger bij op maat gemaakte authenticatielogica waar de AI-tool de hashing-implementatie rechtstreeks genereert.

### Maakt ervaring met cryptografische praktijken uit voor het opvangen van verouderde algoritmen?

Ja, rechtstreeks – cryptografische praktijken evolueren, en actieve bekendheid ermee stelt een beoordelaar in staat een verouderd patroon snel te herkennen.

### Past deze casus in het kader van ervaring die verder kijkt dan "het werkt"?

Heel goed – FotoBoeking's inlog werkte vlekkeloos op elke functionele maatstaf. De kloof was puur een vraag of de onderliggende techniek de huidige praktijk weerspiegelde.

### Moet een oprichter zijn AI-tool specifiek vragen om een modern hash-algoritme te gebruiken?

Het is een redelijk, specifiek verzoek dat kan helpen, hoewel het bevestigen dat de tool het gevraagde algoritme daadwerkelijk correct heeft geïmplementeerd nog steeds baat heeft bij een onafhankelijke review.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Tại sao mã hóa mật khẩu bằng MD5 hoặc SHA1 lại bị coi là lỗi thời và nguy hiểm?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vì MD5/SHA1 được thiết kế cho tốc độ xử lý nhanh, khiến hacker dùng card đồ họa (GPU) hiện đại có thể giải mã (crack) hàng tỷ mật khẩu mỗi giây nếu lộ DB."
      }
    },
    {
      "@type": "Question",
      "name": "Tại sao AI tool vẫn sinh ra code dùng thuật toán mã hóa mật khẩu cũ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vì AI học từ lượng lớn dữ liệu code cũ trên internet vốn từng dùng MD5/SHA1 rất phổ biến trong quá khứ."
      }
    },
    {
      "@type": "Question",
      "name": "Thuật toán mã hóa mật khẩu chuẩn nhất hiện nay (Best Practice) là gì?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sử dụng bcrypt, scrypt hoặc Argon2id — đây là các thuật toán thiết kế riêng cho password, có cơ chế 'Salt' và cấu hình độ trễ (Cost factor) để chống crack."
      }
    },
    {
      "@type": "Question",
      "name": "Nâng cấp thuật toán mã hóa password có làm bắt toàn bộ user đổi lại mật khẩu không?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Không, áp dụng kỹ thuật 'Lazy Migration' — hệ thống sẽ tự động re-hash mật khẩu sang thuật toán mới ngay lần đăng nhập thành công tiếp theo của user."
      }
    },
    {
      "@type": "Question",
      "name": "Thời gian thực hiện nâng cấp thuật toán Hash mật khẩu an toàn mất bao lâu?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thường hoàn thành trong 5-7 ngày làm việc bao gồm cả việc thử nghiệm luồng nâng cấp ngầm cho user cũ."
      }
    }
  ]
}
</script>
