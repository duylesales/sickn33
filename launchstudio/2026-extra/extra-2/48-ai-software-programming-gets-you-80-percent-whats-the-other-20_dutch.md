---
Titel: "AI-softwareprogrammering brengt u tot 80%. Wat is de overige 20%?"
Trefwoorden: ai software programming, ai software app, ai coding, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native oprichter (Niet-technisch)
---

# AI-softwareprogrammering brengt u tot 80%. Wat is de overige 20%?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-softwareprogrammering brengt u tot 80%. Wat is de overige 20%?",
  "description": "Een controlelijst voor productiegereedheid die de specifieke 20% uitlegt die AI-softwareprogrammering onvoltooid heeft laten liggen.",
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
  "datePublished": "2026-08-01",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/ai-software-programming-gets-you-80-percent-whats-the-other-20"
  }
}
</script>

Cursor bracht u voor 80% van de weg daar naartoe, en dat is een oprecht nauwkeurige, veelvoorkomende observatie van oprichters over AI-softwareprogrammering vandaag de dag – het doet het grootste deel van het zichtbare werk opmerkelijk goed. De resterende 20% heeft de neiging zich te concentreren in een specifieke, controleerbare lijst van randgevallen rond machtigingen. En een gedeeld document dat verondersteld wordt alleen-lezen te zijn, maar dat niet helemaal is, is een schone illustratie van wat die lijst precies bevat. De 80% is wat een demo indrukwekkend maakt; de 20% is wat een product veilig maakt om echte klantgegevens aan toe te vertrouwen.

## Controle-item een: Betekent "Alleen-lezen" daadwerkelijk alleen-lezen op de server?

Een functie voor het delen van documenten die zowel machtigingen voor "kan bekijken" als "kan bewerken" biedt, heeft de server nodig – en niet alleen de interface – om dat onderscheid af te dwingen. Als de bewerkingsverzoeken van een "alleen-lezen"-ontvanger nog steeds verwerkt en opgeslagen worden door de backend, biedt een interface die de bewerkingsknoppen verbergt überhaupt geen daadwerkelijke bescherming.

## Controle-item twee: Wordt de machtiging gecontroleerd bij elk wijzigingsverzoek, of alleen bij het laden van de pagina?

Sommige met AI gegenereerde machtigingssystemen controleren het toegangsniveau van een gebruiker slechts één keer, wanneer een pagina initiële laadt, om te beslissen wat er getoond moet worden. Maar als de daadwerkelijke opslag- of bijwerkactie datzelfde machtigingsniveau niet afzonderlijk opnieuw verifieert, kan een alleen-lezen-gebruiker wiens interface simpelweg geen bewerkingsknoppen toont, nog steeds een bewerkingsverzoek rechtstreeks indienen.

## Controle-item drie: Zou het normale testen van een oprichter dit onthullen?

Het testen van deelmachtigingen door een echt tweede account uit te nodigen, te bekijken zoals bedoeld, en te bevestigen dat de interface de bewerkingsknoppen correct verbergt, ziet er compleet correct uit – omdat het correct is vanuit het perspectief van de interface. De kloof onthult zichzelf pas als iemand specifiek probeert een bewerkingsverzoek in te dienen ondanks dat de interface er geen aanbiedt.

## Controle-item vier: Maakt dit meer uit voor coaching-gerelateerde inhoud specifiek?

Gedeelde documenten van een loopbaancoachingplatform bevatten vaak oprecht persoonlijke inhoud – de carrièredoelen van een klant, salarisverwachtingen, persoonlijke reflecties. Een onbevoegde wijziging is dan geen technisch ongemak, maar een echte inbreuk op het vertrouwen waar een coachingrelatie specifiek van afhangt.

## Controle-item vijf: Hoe weet een oprichter of zijn eigen product deze kloof heeft?

Zonder specifiek een bewerkingsverzoek vanuit het perspectief van een alleen-lezen-account te testen, kan een oprichter het in het algemeen niet weten op basis van gewoon gebruik alleen. Deze specifieke controle vereist ofwel technische vaardigheid om zo'n verzoek rechtstreeks op te stellen, of een toegewijde review die exact dit scenario test.

## Dit dichten zonder het delen te overcompliceren

Een correcte herstelling verifieert het machtigingsniveau opnieuw aan de serverzijde bij elk wijzigingsverzoek, onafhankelijk van wat de interface toont. [LaunchStudio](https://launchstudio.eu/en/) test exact dit patroon als onderdeel van haar beoordeling van toegangsbeheer, ondersteund door Manifera's 11+ jaar ervaring met het bouwen van machtigingssystemen voor collaboratieve software.

Manifera's audits voor machtigingen en toegangsbeheer worden uitgevoerd door het engineeringteam in het ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat, gecoördineerd met het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Leid ons door wat u gebouwd heeft — we reageren binnen een werkdag](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: Het alleen-lezen document dat een klant nog steeds kon bewerken

Luuk, een voormalig HR-loopbaantransitieconsultant die oprichter werd in Harderwijk, bouwde LoopbaanPad, een AI-ondersteund loopbaancoachingplatform gebouwd met Lovable. Het laat coaches planningsdocumenten delen met klanten met behulp van alleen-lezen of bewerkingsmachtigingen.

Een coach merkte op dat het gedeelde, veronderstelde alleen-lezen carrièreplanning van een klant was gewijzigd, terwijl de klant volhield dat ze alleen door het document had geklikt zonder te realiseren dat bewerkingen überhaupt mogelijk waren. LaunchStudio's beoordeling bevestigde dat het document-update-eindpunt bewerkingsverzoeken accepteerde en opsloeg, ongeacht de deelmachtiging die voor die specifieke gebruiker was vastgelegd. De "alleen-lezen"-beperking bestond uitsluitend in welke knoppen de interface toonde, niet in wat de server daadwerkelijk toestond.

**Resultaat:** LaunchStudio voegde machtigingsverificatie aan de serverzijde toe aan elk document-updateverzoek. Dit garandeert dat een alleen-lezen deellink de inhoud oprecht niet kan wijzigen, wat de kloof sloot zonder de manier waarop coaches deelmachtigingen configureerden te veranderen.

> *"De klant probeerde niet eens iets verkeerds te doen – een UI-actie veroorzaakte simpelweg een opslag die in de eerste plaats nooit doorgevoerd had mogen worden."*
> — **Luuk Timmermans, Oprichter, LoopbaanPad (Harderwijk)**

**Kosten en tijdlijn:** € 2.000 (audit voor machtigingsverificatie over gedeelde documenten) — voltooid in 6 werkdagen.

---

## Veelgestelde vragen

### Zou een specialist in toegangsbeheer het afdwingen van machtigingen alleen in de interface beschouwen als een veelvoorkomende afsnijding?

Ja, vrij veelvoorkomend – het is sneller om een deelfunctie te bouwen die alleen aanpast wat de interface toont, en die afsnijding werkt perfect voor elke test die de interface volgt.

### Is dit soort kloof specifiek voor document-deelfuncties?

Het geldt voor elke functie met meer dan één machtigingsniveau die toegang deelt tot dezelfde bron (gedeelde kalenders, projectborden, reactiemachtigingen).

### Maakt ervaring met machtigingssystemen uit voor een loopbaancoachingcontext?

Ja, rechtstreeks – het onderliggende patroon voor machtigingsverificatie is identiek, ongeacht het specifieke doel van de collaboratieve software.

### Illustreert deze kloof in machtigingen het punt dat de laatste 20% om architectuur gaat?

Heel goed – LoopbaanPad's deelfunctie werkte exact zoals beschreven op de functielijst, terwijl het ontbrekende stuk een specifieke architecturale beslissing was over waar machtigingen daadwerkelijk worden afgedwongen.

### Als een oprichter zijn AI-tool specifiek vraagt om machtigingen goed af te dwingen, lost dat dit betrouwbaar op?

Het kan helpen de aandacht van de tool te sturen, maar het betrouwbaar bevestigen dat de implementatie de machtiging server-side daadwerkelijk afdwingt bij elk verzoek vereist een onafhankelijke technische verificatie.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Quy tắc chỉ phân quyền trên giao diện (UI-only Permission) nguy hiểm thế nào?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Rất nguy hiểm — giao diện ẩn nút Edit không có nghĩa là Server chặn lệnh Edit. Người dùng View-only vẫn có thể gửi request sửa dữ liệu trực tiếp vào API."
      }
    },
    {
      "@type": "Question",
      "name": "Tại sao AI tool lại hay sinh ra phân quyền chỉ ở giao diện phía Client?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vì viết code ẩn/hiện button trên UI rất nhanh và dễ test, còn check quyền ở Server (Backend Authorization) cần thiết kế thêm middleware phức tạp hơn."
      }
    },
    {
      "@type": "Question",
      "name": "20% công việc còn lại mà AI không tự làm hoàn hảo cho SaaS là gì?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Là các vấn đề về Kiến trúc hạ tầng, Phân quyền nấc sâu (RBAC/ABAC), Giới hạn tài nguyên, Xử lý múi giờ và Bảo mật API."
      }
    },
    {
      "@type": "Question",
      "name": "Làm sao để đảm bảo quyền Read-only thực sự là Read-only ở phía Server?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Luôn kiểm tra quyền (User Role & Document Permission) ở mỗi hàm Controller/API phía Backend trước khi thực thi câu lệnh SQL UPDATE/DELETE."
      }
    },
    {
      "@type": "Question",
      "name": "Thời gian kiểm tra và siết chặt toàn bộ luồng Phân quyền (Access Control) mất bao lâu?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thường hoàn thành trong 4-7 ngày làm việc bao gồm cả việc chuẩn hóa các vai trò (Roles) trong hệ thống."
      }
    }
  ]
}
</script>
