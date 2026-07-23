---
Titel: "Het eerste GDPR-verzoek om gegevensportabiliteit dat uw AI SaaS daadwerkelijk zal krijgen"
Trefwoorden: ai data security, gdpr, data portability request, right to data access, EU privacy compliance
Koperfase: Overweging
Doelgroep: AI-Native-oprichter
---
# Het eerste GDPR-verzoek om gegevensportabiliteit dat uw AI SaaS daadwerkelijk zal krijgen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Het eerste GDPR-verzoek om gegevensportabiliteit dat uw AI SaaS daadwerkelijk zal krijgen",
  "description": "Het recht van de AVG op gegevensportabiliteit betekent dat elke gebruiker binnen dertig dagen legaal een gestructureerde export van zijn gegevens kan eisen, maar door AI gegenereerde SaaS-apps bouwen bijna nooit een vervullingstraject voor dat verzoek. Dit is wat er gebeurt als de eerste landt.",
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
  "datePublished": "2026-07-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/gdpr-data-portability-ai-saas-request"
  }
}
</script>

Het begint meestal als een normaal uitziende ondersteuningsmail: "Kun je mij alle gegevens sturen die je over mij hebt?" Het klinkt als een klein verzoek. Het is eigenlijk een juridische: AVG-artikel 20 geeft elke EU-gebruiker het recht om zijn persoonlijke gegevens te ontvangen in een gestructureerd, algemeen gebruikt, machinaal leesbaar formaat, en bedrijven hebben 30 dagen de tijd om hieraan te voldoen. Bij de meeste AI-gebouwde SaaS-producten is deze vraag nog nooit gesteld, wat betekent dat de meeste oprichters erachter komen dat ze geen manier hebben om deze vraag precies te beantwoorden wanneer de klok begint te lopen.

## Waarom deze kloof overleeft tot aan een echt verzoek

AI-coderingstools zijn erg goed in het bouwen van de functies die een oprichter expliciet beschrijft: aanmelding, dashboards, de kernproductcyclus. Overdraagbaarheid van AVG-gegevens is niet een functie waar iemand om vraagt, omdat het geen deel uitmaakt van de productervaring; het is een wettelijke verplichting die pas zichtbaar wordt als iemand zich erop beroept. Een prompt als 'bouw een SaaS-clientportaal' zal nooit een knop 'exporteer al mijn gegevens' opleveren, tenzij de oprichter specifiek weet dat dit een vereiste is en er bij naam naar vraagt.

Het resultaat is dat bij de meeste door AI gegenereerde apps de gegevens verspreid zijn over een normaal relationeel schema – gebruikersrecords hier, activiteitenlogboeken daar, geüploade bestanden ergens anders – zonder een enkele functie die alles samenbrengt in één exporteerbaar pakket. Wanneer er een echt verzoek binnenkomt, heeft degene aan de ontvangende kant twee opties: de exportlogica binnen een wettelijke deadline bouwen, of handmatig de productiedatabase handmatig doorzoeken, wat precies zo riskant en traag is als het klinkt, vooral voor iemand die niet goed bekend is met het schema.

## Wat een juridisch voldoende export eigenlijk vereist

Een respons op gegevensportabiliteit moet alle persoonlijke gegevens omvatten die de gebruiker rechtstreeks heeft verstrekt (geen afgeleide of afgeleide gegevens), geleverd in een gestructureerd formaat zoals JSON of CSV in plaats van een pdf-screenshot van een databasetabel, en moet binnen 30 dagen na het verzoek arriveren – met een mogelijke verlenging van twee maanden alleen als het bedrijf de gebruiker hiervan op de hoogte stelt en binnen de eerste maand uitlegt waarom. Door dit van tevoren in het product in te bouwen – een selfservice-exportknop, of op zijn minst een gedocumenteerd intern script dat elke ingenieur veilig kan uitvoeren – wordt een juridische brandoefening een taak van vijf minuten.

Manifera heeft meer dan elf jaar productie-engineering-ervaring met het bouwen van systemen die voldoen aan echte compliance-eisen, en LaunchStudio past dezelfde discipline toe op AI-gebouwde SaaS-producten: precies in kaart brengen waar persoonlijke gegevens zich in het schema bevinden en een exportpad bouwen voordat het eerste verzoek ooit binnenkomt, in plaats van daarna. Onze technici, werkzaam vanuit het ontwikkelingscentrum van Manifera in Ho Chi Minh City, behandelen dit als onderdeel van de standaard beoordeling van de gegevensverwerking voor elke klantgerichte SaaS-tool, naast de logica voor verwijdering en bewaring.

Als je nog nooit hebt getest wat er zou gebeuren als een gebruiker morgen om zijn gegevens zou vragen, is het de moeite waard [met een ingenieur te praten over je huidige schema](https://launchstudio.eu/en/#contact) voordat die e-mail daadwerkelijk arriveert.

## Echt voorbeeld

### Een AI-native oprichter in actie: de portal zonder exportknop

Hugo Meesters, oprichter uit Hoorn, bouwde KlantPortaal – een klantportaal SaaS voor consultants – met Cursor. De app regelde alles wat de klant van een consultant dagelijks nodig had: gedeelde documenten, notulen van vergaderingen, projecttijdlijnen. Het was nooit bij Hugo en bij Cursor opgekomen dat een klant op een dag formeel zou kunnen verzoeken om een ​​volledige export van zijn eigen gegevens – totdat iemand dat schriftelijk deed en daarbij expliciet artikel 20 van de AVG citeerde.

Terwijl de wettelijke klok van 30 dagen al liep, realiseerde Hugo zich dat er nergens in de app een exportfunctie was. De gegevens van de klant – profielinformatie, geüploade documenten, vergadergeschiedenis – waren verspreid over een zestal databasetabellen zonder dat er een uniforme query tussen zat. De enige manier om vooruit te komen onder de druk van deadlines was om een ​​ingenieur handmatig rechtstreeks de productiedatabase te laten doorzoeken, een proces dat zowel langzaam als riskant is als er geen bestaande tool voor is gebouwd en er een wettelijke deadline aan verbonden is.

LaunchStudio bracht elke tabel in het KlantPortaal-schema die persoonlijke gegevens bevatte in kaart, bouwde een herbruikbare exportfunctie die de volledige gegevensvoetafdruk van een gebruiker samenvoegt in een gestructureerd JSON-pakket, en voegde een interne beheertool toe zodat toekomstige verzoeken binnen enkele minuten konden worden afgehandeld in plaats van urenlang handmatig opvragen. **Resultaat:** Hugo heeft drie dagen vóór de wettelijke deadline aan het oorspronkelijke verzoek voldaan, en elk volgend verzoek heeft sindsdien minder dan tien minuten geduurd.

> *"Ik had hier echt nog nooit over nagedacht totdat de e-mail arriveerde. Het bouwen van de exportfunctie onder druk van deadlines was stressvol op een manier die het toevoegen van een normale functie nooit is."*
> — **Hugo Meesters, oprichter, KlantPortaal (Hoorn)**

**Kosten en tijdlijn:** € 700 (data mapping, gestructureerde exportfunctie, interne fulfilmenttool) — voltooid in 4 werkdagen.

---

## Veelgestelde vragen

### Wat moet een bedrijf precies bieden voor de dataportabiliteit van de AVG?

Persoonsgegevens die de gebruiker rechtstreeks aan de dienst heeft verstrekt, geleverd in een gestructureerd, veelgebruikt, machinaal leesbaar formaat zoals JSON of CSV, binnen 30 dagen na het verzoek.

### Waarom bouwt een AI-coderingstool dit niet automatisch?

Omdat het geen functie is die wordt weergegeven in een productdemo of een typische build-prompt, is het een wettelijke verplichting die pas zichtbaar wordt zodra een echte gebruiker zich op zijn recht erop beroept.

### Wat gebeurt er als een SaaS-bedrijf niet op tijd aan een verzoek kan voldoen?

Afgezien van de onmiddellijke problemen zorgen gemiste deadlines voor echte blootstelling aan de regelgeving: de gegevensbeschermingsautoriteiten van de EU kunnen klachten onderzoeken van gebruikers wier verzoeken onbeantwoord bleven, en dat doen ze ook.

### Hoe helpt de technische achtergrond van Manifera bij dit soort compliance-kloof?

Manifera heeft meer dan elf jaar ervaring in productietechniek bij zakelijke klanten, en die discipline van het in kaart brengen van gegevensstromen voordat ze nodig zijn, is precies wat voorkomt dat een verzoek om gegevensportabiliteit een noodgeval wordt.

### Bouwt LaunchStudio dit proactief of pas nadat er een verzoek binnenkomt?

Idealiter proactief: de in Ho Chi Minhstad gevestigde technici van LaunchStudio nemen logica voor het exporteren en verwijderen van gegevens op als onderdeel van een standaard pre-lanceringsbeoordeling, zodat het vervullingstraject al bestaat voordat het eerste echte verzoek binnenkomt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What exactly does GDPR data portability require a company to provide?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Personal data the user directly provided to the service, delivered in a structured, commonly-used, machine-readable format such as JSON or CSV, within 30 days of the request."
      }
    },
    {
      "@type": "Question",
      "name": "Why doesn't an AI coding tool build this automatically?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because it isn't a feature that shows up in a product demo or a typical build prompt \u2014 it's a legal obligation that only becomes visible once a real user invokes their right to it."
      }
    },
    {
      "@type": "Question",
      "name": "What happens if a SaaS company can't fulfill a request in time?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Missed deadlines create real regulatory exposure \u2014 EU data protection authorities can and do investigate complaints from users whose requests went unanswered."
      }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's engineering background help with this kind of compliance gap?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Manifera has 11+ years of production engineering experience across enterprise clients, and mapping data flows before they're needed is exactly what prevents a portability request from becoming an emergency."
      }
    },
    {
      "@type": "Question",
      "name": "Does LaunchStudio build this proactively or only after a request comes in?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ideally proactively \u2014 LaunchStudio's Ho Chi Minh City-based engineers include data export and deletion logic as part of a standard pre-launch review."
      }
    }
  ]
}
</script>