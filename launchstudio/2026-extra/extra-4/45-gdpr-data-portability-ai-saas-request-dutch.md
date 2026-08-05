---
Titel: "Het eerste AVG-gegevensoverdraagbaarheidsverzoek dat uw AI-SaaS daadwerkelijk zal krijgen"
Trefwoorden: ai data security, gdpr, data portability request, right to data access, EU privacy compliance
Koperfase: Overweging
Doelgroep: AI-Native oprichter
---

# Het eerste AVG-gegevensoverdraagbaarheidsverzoek dat uw AI-SaaS daadwerkelijk zal krijgen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Het eerste AVG-gegevensoverdraagbaarheidsverzoek dat uw AI-SaaS daadwerkelijk zal krijgen",
  "description": "Het recht op gegevensoverdraagbaarheid onder de AVG betekent dat elke gebruiker wettelijk een geformatteerde export kan eisen.",
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

Het begint doorgaans als een normaal ogende ondersteunings-e-mail: "Kunt u mij alle gegevens sturen die u over mij heeft?" Het klinkt als een klein verzoek. Het is daadwerkelijk een wettelijke eis – AVG Artikel 20 geeft elke EU-gebruiker het recht om zijn persoonlijke gegevens te ontvangen in een gestructureerd, veelgebruikt, machinaal leesbaar formaat, en bedrijven hebben 30 dagen om hieraan te voldoen. De meeste met AI gebouwde SaaS-producten is deze vraag nog nooit gesteld, wat betekent dat de meeste oprichters ontdekken dat ze geen manier hebben om er antwoord op te geven exact wanneer de klok begint te lopen.

## Waarom deze kloof het overleeft tot aan een echt verzoek

AI-coderingsassistenten zijn erg goed in het bouwen van de functies die een oprichter expliciet beschrijft – aanmelden, dashboards, de kern-productstroom. AVG-gegevensoverdraagbaarheid is geen functie waar iemand aan denkt om voor te prompten, omdat het geen onderdeel is van de productervaring. Het is een wettelijke verplichting die pas zichtbaar wordt wanneer iemand een beroep doet op dat recht. Een prompt zoals "bouw een SaaS-klantenportaal" zal nooit een "exporteer al mijn gegevens"-knop produceren tenzij de oprichter specifiek weet dat dat een vereiste is en er bij naam om vraagt.

Het resultaat is dat de meeste met AI gegenereerde apps de gegevens verspreid hebben over een normaal relationeel schema – gebruikersrecords hier, activiteitslogboeken daar, geüploade bestanden ergens anders – zonder enkele functie die alles samenbrengt in één exporteerbaar pakket. Wanneer een echt verzoek binnenkomt heeft degene aan de ontvangende kant twee opties: de exportlogica bouwen onder een wettelijke deadline, of de productiedatabase handmatig bevragen, wat exact zo risicovol en traag is als het klinkt.

## Wat een wettelijk voldoende export daadwerkelijk vereist

Een nalevende reactie op gegevensoverdraagbaarheid moet alle persoonlijke gegevens bevatten die de gebruiker rechtstreeks heeft verstrekt (niet afgeleide of afgeleide gegevens), geleverd in een gestructureerd formaat zoals JSON of CSV in plaats van een PDF-screenshot van een databasetabel, en het moet binnen 30 dagen na het verzoek aankomen – met een mogelijke verlenging van twee maanden alleen als het bedrijf de gebruiker informeert en binnen de eerste maand uitlegt waarom. Het vooraf ingebouwd hebben van dit in het product – een self-service exportknop, of minimaal een gedocumenteerd intern script dat elke ingenieur veilig kan uitvoeren – veranderd een wettelijke haastklus in een taak van vijf minuten.

Manifera heeft meer dan 11 jaar ervaring in productie-engineering in het bouwen van systemen die bestand zijn tegen echte nalevingsvereisten. LaunchStudio past diezelfde discipline toe op met AI gebouwde SaaS-producten: exact in kaart brengen waar persoonlijke gegevens leven in het schema en een exportpad bouwen voordat het eerste verzoek ooit binnenkomt. Onze ingenieurs, werkend vanuit Manifera's ontwikkelingscentrum in Ho Chi Minh-stad, behandelen dit als onderdeel van de standaard beoordeling van gegevensverwerking voor elke klantgerichte SaaS-tool, naast logica voor verwijdering en bewaartermijnen.

Als u nog nooit heeft getest wat er zou gebeuren als een gebruiker morgen om zijn gegevens vraagt, is het de moeite waard om [met een ingenieur te praten over uw huidige schema](https://launchstudio.eu/en/#contact) voordat die e-mail daadwerkelijk binnenkomt.

## Uw database is niet de enige plek waar deze gegevens leven

Zelfs een goed gebouwde exportfunctie die alle tabellen in uw eigen schema correct ophaalt kan nog steeds een onvolledig antwoord retourneren, omdat de meeste SaaS-producten daadwerkelijk niet alle persoonlijke gegevens van een gebruiker zelf opslaan. Betalingsdetails leven bij een verwerker zoals Stripe. Marketingvoorkeuren en e-mailgeschiedenis leven bij een e-mailplatform. Ondersteuningsgesprekken leven in een helpdesk-tool. Elk van die derden verwerkt die gegevens over het algemeen nog steeds namens het bedrijf. Dit betekent doorgaans dat het nog steeds de verantwoordelijkheid van het bedrijf is om verantwoording af te leggen wanneer er een overdraagbaarheids- of toegangsaanvraag binnenkomt – een verzoek dat alleen uit de interne database ophaalt laat stilletjes alles weg wat door verbonden leveranciers wordt gehouden.

Een met AI gegenereerde schematoescheiding heeft geen manier om dit te weten, omdat het alleen de tabellen ziet waar het toegang toe heeft gekregen. Het heeft geen zicht op wat een Stripe API-sleutel of een integratie van een e-mailplatform daadwerkelijk aan de andere kant opslaat. Het sluiten van deze kloof betekent het bijhouden van een expliciet register van elk extern systeem dat gegevens bevat die gekoppeld zijn aan een gebruikers-ID, en het uitbreiden van de exportfunctie om elk systeem te bevragen:

```
const DATA_SOURCES = [
  { name: 'database', fetch: (userId) => db.exportUser(userId) },
  { name: 'stripe', fetch: (userId) => stripe.customers.retrieve(userId) },
  { name: 'email_platform', fetch: (userId) => emailApi.getContact(userId) },
  { name: 'support_tool', fetch: (userId) => supportApi.getTickets(userId) },
];

async function buildFullExport(userId) {
  const results = {};
  for (const source of DATA_SOURCES) {
    results[source.name] = await source.fetch(userId);
  }
  return results;
}
```

Zonder dat register kunnen "we hebben aan het verzoek voldaan" en "we hebben volledig aan het verzoek voldaan" er identiek uitzien tot het moment dat iemand de export vergelijkt met wat hij weet dat een bedrijf daadwerkelijk over hem bezit.

## Echt voorbeeld

### Een AI-native oprichter in actie: Het portaal zonder exportknop

Hugo Meesters, een oprichter in Hoorn, bouwde KlantPortaal – een SaaS-klantenportaal voor adviseurs – met behulp van Cursor. De app handelde alles af wat de klant van een adviseur van dag tot dag nodig had: gedeelde documenten, vergadernotities, projecttijdlijnen. Het was nooit bij Hugo, of bij Cursor, opgekomen dat een klant op een dag formeel een volledige export van zijn eigen gegevens zou aanvragen – totdat iemand dat schriftelijk deed, expliciet AVG Artikel 20 citerend.

Met de wettelijke klok van 30 dagen die al liep, realiseerde Hugo zich dat er nergens in de app een exportfunctie was. De gegevens van de klant – profielinformatie, geüploade documenten, vergadergeschiedenis – waren verspreid over een half dozijn databasetabellen zonder gecombineerde query die ze verbond. Het enige pad voorwaarts onder tijdsdruk van de wet was dat een ingenieur de productiedatabase handmatig rechtstreeks bevroeg. Dit is een proces dat zowel traag als risicovol is wanneer er geen bestaand gereedschap voor gebouwd is.

LaunchStudio bracht elke tabel in KlantPortaal's schema in kaart die persoonlijke gegevens bevatte, bouwde een herbruikbare exportfunctie die de volledige gegevensvoetafdruk van een gebruiker compileert in een gestructureerd JSON-pakket, en voegde een interne beheerderstool toe zodat toekomstige verzoeken in minuten konden worden afgehandeld. **Resultaat:** Hugo voldeed drie dagen vóór de wettelijke deadline aan het oorspronkelijke verzoek. Elk volgend verzoek sinds die tijd heeft minder dan tien minuten gekost.

> *"Ik had hier oprecht nooit over nagedacht totdat de e-mail binnenkwam. Het bouwen van de exportfunctie onder deadline-druk was stressvol op een manier die het toevoegen van een normale functie nooit is."*
> — **Hugo Meesters, Oprichter, KlantPortaal (Hoorn)**

**Kosten en tijdlijn:** € 700 (datatoescheiding, gestructureerde exportfunctie, interne afhandelingstool) — voltooid in 4 werkdagen.

---

## Veelgestelde vragen

### Wat vereist AVG-gegevensoverdraagbaarheid exact dat een bedrijf levert?

Persoonlijke gegevens die de gebruiker rechtstreeks aan de dienst heeft verstrekt, geleverd in een gestructureerd, veelgebruikt, machinaal leesbaar formaat zoals JSON of CSV, binnen 30 dagen na het verzoek.

### Waarom bouwt een AI-coderingsassistent dit niet automatisch?

Omdat het geen functie is die verschijnt in een product-demo of een typische bouw-prompt. Het is een wettelijke verplichting die pas zichtbaar wordt zodra een echte gebruiker een een beroep doet op zijn recht.

### Wat gebeurt er als een SaaS-bedrijf een verzoek niet op tijd kan afhandelen?

Het missen van deadlines creëert reële reglementaire blootstelling – EU-autoriteiten voor gegevensbescherming kunnen en zullen klachten onderzoeken van gebruikers wier verzoeken onbeantwoord zijn gebleven.

### Moet een gegevensexport ook informatie bevatten van tools van derden zoals Stripe of een e-mailplatform?

Over het algemeen wel – persoonlijke gegevens die namens een bedrijf worden verwerkt door een subverwerker zijn doorgaans nog steeds de verantwoordelijkheid van dat bedrijf. Een compleet exportproces heeft een expliciet register nodig van elk extern systeem dat gebruikersgegevens bevat.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is het verschil tussen een AVG inzagerecht (Artikel 15) en overdraagbaarheid (Artikel 20)?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Overdraagbaarheid (Art. 20) vereist dat data in een gestructureerd, machinaal leesbaar formaat (zoals JSON of CSV) wordt geleverd, niet als onleesbare PDF's."
      }
    },
    {
      "@type": "Question",
      "name": "Hoeveel tijd heb je om een AVG dataportabiliteit verzoek af te handelen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Wettelijk exact 30 dagen na ontvangst van het verzoek. Zonder geautomatiseerde export-functie leidt dit vaak tot een hectische handmatige database-actie."
      }
    },
    {
      "@type": "Question",
      "name": "Moeten externe gegevens van Stripe of Mailchimp ook in de export?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja! Persoonsgegevens verwerkt door subverwerkers vallen ook onder jouw verplichting. Een complete export bevat dus data uit de DB én gekoppelde APIs."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom bouwen Lovable en Cursor geen automatische export-knop?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "AI bouwt alleen functionaliteiten die gevraagd worden voor de UI. Juridische AVG-functies worden niet spontaan gegenereerd zonder expliciete instructie."
      }
    },
    {
      "@type": "Question",
      "name": "Wat kost het bouwen van een AVG compliant export-stroom bij LaunchStudio?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het in kaart brengen van persoonsgegevens en bouwen van een JSON/CSV exportfunctie kost gemiddeld €700 en duurt 4 werkdagen."
      }
    }
  ]
}
</script>