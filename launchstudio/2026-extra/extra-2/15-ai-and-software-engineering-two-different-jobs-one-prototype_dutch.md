---
Titel: "AI en software-engineering: Twee verschillende banen, één prototype"
Trefwoorden: ai and software engineering, ai in software engineering, ai coding, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie Hacker
---

# AI en software-engineering: Twee verschillende banen, één prototype

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI en software-engineering: Twee verschillende banen, één prototype",
  "description": "Een verdieping in het skippen van eigenschapscontroles (IDOR) bij door AI gegenereerde facturen en bronnen.",
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
  "datePublished": "2026-07-24",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/ai-and-software-engineering-two-different-jobs-one-prototype"
  }
}
</script>

AI en software-engineering worden behandeld als dezelfde baan omdat ze hetzelfde zichtbare resultaat kunnen produceren – werkende code. Ze zijn niet dezelfde baan. Het ene genereert code die voldoet aan een beschreven scenario; het andere omvat de gewoonte om te vragen "welk verzoek werd er niet beschreven, en wat doet deze code als het dat in plaats daarvan ontvangt?" – een gewoonte die bewust moet worden toegepast. Niets aan het genereren van code past het namelijk automatisch toe.

## Waar generatie voor optimaliseert

Een AI-coderingsassistent die reageert op "bouw een facturenpagina die de factuurgeschiedenis van een gebruiker toont" zal betrouwbaar een pagina produceren die correct facturen weergeeft die toebehoren aan welke gebruiker ook is ingelogd, opgehaald via een factuur-ID in de URL of het verzoek. Dit voldoet volledig aan de beschrijving en ziet er volledig correct uit in elke test die de beschrijving volgt zoals geschreven.

## Wat engineeringdiscipline aanvullend vraagt

Een software-engineeringbeoordeling van diezelfde functie stelt een verdere, specifieke vraag: wat gebeurt er als een ingelogde gebruiker de factuur-ID in het verzoek verandert in een ID die toebehoort aan een volledig andere gebruiker? Dit is de tekstboekdefinitie van een Insecure Direct Object Reference (IDOR) – een bron geïdentificeerd door een voorspelbare of raadbare ID, opgehaald zonder te verifiëren of de aanvrager daadwerkelijk een legitieme claim op de bron heeft.

## Waarom IDOR-kwetsbaarheden bijzonder gebruikelijk zijn in met AI gegenereerde code

Opeenvolgende of eenvoudige numerieke ID's zijn een natuurlijke, veelvoorkomende standaardwaarde in gegenereerde databaseschema's. En het ophalen van een record "op ID" is een van de meest basale operaties die elke backend uitvoert. Omdat het ideale pad – een legitieme gebruiker die zijn eigen factuur ophaalt via de correcte ID – identiek werkt of er nu een eigenschapscontrole bestaat of niet, produceert deze specifieke klasse van kloven geen zichtbaar symptoom totdat iemand opzettelijk of per ongeluk een ID opvraagt die niet van hem is.

Dit wordt versterkt door hoe natuurlijk een AI-coderingsassistent een "ophalen op ID"-eindpunt implementeert: gegeven een prompt zoals "laat gebruikers hun factuur bekijken," is de meest directe, duidelijke implementatie een enkele databasequery die filtert op de ID in het verzoek. Dit is exact correct voor een gebruiker die zijn eigen factuur bekijkt, en zegt helemaal niets over wat er gebeurt wanneer die ID aan iemand anders toebehoort. Het toevoegen van de eigenschapscontrole vereist een extra, bewuste regel logica die niet geïmpliceerd werd door het oorspronkelijke verzoek. Tenzij een prompt er dus specifiek om vraagt, is er geen sterke reden voor de gegenereerde code om het standaard op te nemen.

## Waarom een oprichter die zijn eigen code beoordeelt dit zelden opvangt

Het beoordelen van uw eigen gegenereerde code op correctheid betekent van nature controleren "doet dit wat ik beschreven heb?" – en een IDOR-kloof is, per definitie, onzichtbaar vanuit die hoek. De code doet namelijk exact wat beschreven werd. Het opvangen ervan vereist het beoordelen vanuit een volledig andere vraag: "wat heb ik nooit beschreven, en wat gebeurt er standaard wanneer dat geval zich toch voordoet?"

## Wat het sluiten van deze kloof omvat

Een correcte herstelling voegt een expliciete eigenschapscontrole toe aan elk eindpunt dat bronnen ophaalt – bevestigend dat het opgevraagde record daadwerkelijk toebehoort aan de geauthenticeerde aanvrager voordat het geretourneerd wordt. Dit wordt gestaag en consequent toegepast over facturen, bestellingen, documenten, en elke andere bron per gebruiker in het systeem. [LaunchStudio](https://launchstudio.eu/en/) voert exact dit soort eigenschapscontrole-audit uit als een kernonderdeel van haar beoordeling van productiegereedheid, ondersteund door Manifera's 11+ jaar enterprise software engineering discipline.

Manifera's engineeringbeoordelingen worden uitgevoerd door het team in het ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat, met klantgesprekken afgehandeld vanuit het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Praat met een ingenieur die met AI gegenereerde code begrijpt](https://launchstudio.eu/en/#contact).

## Een stapsgewijs kader voor het zelf testen op IDOR

IDOR-kwetsbaarheden zijn ongebruikelijk mechanisch om op te testen zodra u het patroon kent, wat betekent dat een oprichter een betekenisvolle controle kan uitvoeren zonder enige gespecialiseerde beveiligingstools.

**Stap één: som elke bron op die wordt opgehaald via een ID in een URL of verzoek**

Facturen, bestellingen, documenten, berichten, gebruikersprofielen, geüploade bestanden – overal waar de URL of het API-verzoek van uw applicatie zoiets bevat als `/invoices/1042` of `?order_id=88`, is dat een kandidaat voor deze exacte kwetsbaarheidsklasse.

**Stap twee: maak twee test-accounts aan, niet één**

Het testen van IDOR vereist dat u ingelogd bent als de ene gebruiker terwijl u toegang probeert te krijgen tot de bron van een andere gebruiker – iets wat een oprichter die solo test, ingelogd op een enkel account, structureel niet kan doen. Twee gratis test-accounts, specifiek aangemaakt voor deze controle, is voldoende.

**Stap drie: log in als account A, noteer een bron-ID, en wissel vervolgens naar account B**

Terwijl u ingelogd bent als het tweede account, wijzigt u handmatig de URL of het verzoek om te verwijzen naar de ID die genoteerd is van het eerste account. Een correct beschermd eindpunt retourneert een 403- of 404-fout. Een eindpunt met een IDOR-kloof retourneert de daadwerkelijke gegevens van account A aan account B.

**Stap vier: herhaal over elk brontype en elke HTTP-methode**

Stop niet bij het eerste eindpunt dat slaagt – herhaal dezelfde test voor elk brontype geïdentificeerd in stap één, en controleer niet alleen het bekijken (GET-verzoeken) maar ook het bewerken of verwijderen (PUT-, PATCH-, DELETE-verzoeken). Een eindpunt kan het bekijken van de bron van een andere gebruiker namelijk correct blokkeren terwijl het nog steeds een bewerkings- of verwijderingsverzoek ertoe toestaat.

**Stap vijf: controleer ook geneste en indirecte referenties**

Sommige van de meest gemakkelijk gemiste gevallen zijn niet de primaire bron-ID in de URL, maar een secundaire ID die verwerkt zit in een verzoektekst of een geneste bron – een reactie op het document van iemand anders, een regelitem binnen de bestelling van iemand anders. Deze zijn net zo misbruikbaar en zijn frequent de gevallen die een handmatige controle in eerste instantie mist.

## Echt voorbeeld

### Een AI-native oprichter in actie: Het facturnummer dat de deur opende

Milan, een voormalig bouwlocatiemanager die oprichter werd in Leeuwarden, bouwde BouwBoard, een AI-ondersteunde tool voor bouwprojectbeheer gebouwd met Cursor, inclusief een klantgerichte factuurgeschiedenispagina geïdentificeerd door een eenvoudig opeenvolgend factuurnummer in de URL.

Een onderaannemer, die door zijn eigen factuur bladerde en het opeenvolgende nummer in de adresbalk opmerkte, veranderde het met één cijfer uit nieuwsgierigheid en vond zichzelf kijkend naar de factuur van een volledig andere klant, inclusief hun uurtarief en projectdetails. LaunchStudio's beoordeling bevestigde dat het factuureindpunt alleen op ID ophaalde, zonder controle of de aanvrager daadwerkelijk de opgevraagde factuur bezat.

**Resultaat:** LaunchStudio voegde een expliciete eigenschapsverificatie toe aan het factuureindpunt en auditeerde elke vergelijkbare bron per gebruiker in BouwBoard op hetzelfde patroon. Dit sloot de kloof over de gehele applicatie in plaats van alleen het ene eindpunt dat gemeld was.

> *"Hij vertelde me er bijna verontschuldigend over, alsof hij zich slecht voelde dat hij er toevallig op stuitte. Ik was gewoon opgelucht dat het iemand eerlijk was die het vermeldde in plaats van stil te blijven."*
> — **Milan de Wit, Oprichter, BouwBoard (Leeuwarden)**

**Kosten en tijdlijn:** € 2.000 (IDOR-audit en eigenschapsverificatie over broneindpunten) — voltooid in 7 werkdagen.

---

## Veelgestelde vragen

### Zou een penetratietester IDOR beschouwen als een bekende, gemakkelijk te testen kwetsbaarheidsklasse?

Ja, het is een van de meest gebruikelijke geteste kwetsbaarheidsklassen in professionele beveiligingsbeoordelingen, precies omdat het zo mechanisch is om systematisch op te controleren.

### Los het overstappen van opeenvolgende numerieke ID's naar willekeurige UUID's dit probleem volledig op zichzelf op?

Het helpt door ID's moeilijker te raden te maken, maar het lost het onderliggende probleem niet volledig op – een factuur-ID op basis van een UUID die ooit gedeeld, gelogd of ergens gelekt wordt verleent nog steeds toegang zonder een eigenschapscontrole.

### Is dit het soort kloof dat B2B-enterpriseklanten zouden hebben opgevangen vóór productie?

Typisch wel, aangezien enterprise-trajecten over het algemeen een toegewijde beveiligingsbeoordelingsfase als standaardpraktijk omvatten.

### Vormt een achtergrond in offshore management gecombineerd met cybersecurity de aanpak voor cases zoals die van BouwBoard?

Ja – offshore engineeringmanagement vereist het vaststellen van consistente beoordelingsstandaarden over een gedistribueerd team. Diezelfde consistentie opvangen is wat een patroon zoals een ongecontroleerde factuur-ID opvangt.

### Hoe zou deze kloof waarschijnlijk uiteindelijk naar boven zijn gekomen als de onderaannemer er niets over gezegd had?

Meest aannemelijk via een minder eerlijke partij die hetzelfde patroon opmerkte en het stilletjes misbruikte in plaats van het te melden, of via een beveiligingsbeoordeling door de eigen inkoopafdeling van een klant.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is IDOR makkelijk te testen voor beveiligingsprofessionals?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, het is een van de meest geteste klassen omdat het mechanisch en systematisch gecontroleerd kan worden."
      }
    },
    {
      "@type": "Question",
      "name": "Lossen willekeurige UUID's dit probleem volledig op?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, ze maken raden moeilijker maar một gelekten UUID verleent nog steeds toegang mà không cần check ownership."
      }
    },
    {
      "@type": "Question",
      "name": "Zouden enterprise-klanten dit opvangen vóór productie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, enterprise-trajecten omvatten standaard một toegewijde beveiligingsbeoordelingsfase."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het risico als IDOR không được phát hiện sớm?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Kẻ xấu có thể lặng lẽ thu thập dữ liệu nhạy cảm của người dùng khác hoặc bị phát hiện trong audit của khách hàng lớn."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe test je IDOR tự làm với 2 tài khoản?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Đăng nhập tài khoản B, đổi URL/ID thành ID tài khoản A. Nếu xem/sửa được là bị dính IDOR."
      }
    },
    {
      "@type": "Question",
      "name": "Geldt IDOR chỉ cho GET request hay cả POST/PUT/DELETE?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Geldt cho tất cả các HTTP methods — bao gồm xem, chỉnh sửa và xóa tài nguyên."
      }
    }
  ]
}
</script>
