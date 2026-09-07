---
Titel: "Wat Te Doen Wanneer het AI-Model Onzin Teruggeeft"
Trefwoorden: LLM output validatie, gestructureerde output json schema, hallucinaties opvangen SaaS, AI fallback wanneer model faalt, retry strategie AI model, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Wat Te Doen Wanneer het AI-Model Onzin Teruggeeft

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wat Te Doen Wanneer het AI-Model Onzin Teruggeeft",
  "description": "Een taalmodel dat in 95% van de gevallen accuraat is, faalt in één op de twintig keer. Hoe u model-outputs valideert, eerlijke fallback-states ontwerpt en voorkomt dat hallucinaties geruisloos in de administratie van uw klanten belanden.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-05-19",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/what-to-do-when-the-model-returns-nonsense" }
}
</script>

Elk ander traditioneel onderdeel in uw softwarearchitectuur faalt binair:
Een database-query slaagt of gooit een SQL-fout. Een betaling via Mollie of Stripe lukt of wordt geweigerd met een foutcode.

**Een groot taalmodel (LLM) bezit een unieke derde toestand die geen enkel ander softwarecomponent kent:**
Het retourneert een antwoord dat er grammaticaal foutloos, overtuigend en uiterst zelfverzekerd uitziet — **maar inhoudelijk 100% verzonnen of pertinent onjuist is** (*hallucinatie*) — zónder dat er ergens een foutmelding afgaat.

Deze toestand is geen zeldzame randzaak die u kunt weg-engineeren met een slimmere prompt. Het is een fundamentele eigenschap van probabilistische neurale netwerken.

De praktische vraag voor een software-oprichter is dan ook niet hoe u hallucinaties tot exact 0,0% reduceert, maar:
**Wat doet uw applicatie op het moment dat het model onzin genereert?**

In de meeste haastig gebouwde prototypes is het antwoord pijnlijk: de software slikt het antwoord voor zoete koek en toont het direct aan de eindgebruiker alsof het de absolute waarheid is.

## Valideer Álles Wat het Model Teruggeeft

De allerbelangrijkste ontwerpregel in AI-engineering luidt:
> **Behandel de output van een taalmodel altijd als onvertrouwde externe invoer, exact zoals u een formulierinvoer van een anonieme internetbezoeker zou behandelen.**

Vier verplichte validatiestappen:

### 1. Dwing Gestructureerde Output Af (JSON Schema)
Vraag nooit om vrije tekst als u data nodig heeft. Maak gebruik van de officiële *Structured Outputs* functionaliteit van de provider (zoals OpenAI's `json_schema`). Valideer de geretourneerde JSON aan de serverzijde met een schema-validator (zoals Zod of Pydantic). *"Meestal valide"* is in een productieomgeving geen acceptabele garantie.

### 2. Toets Waarden aan de Fysieke Realiteit (*Sanity Checks*)
- Retourneert het model een categorie? Controleer of deze exact matcht met uw database-enum.
- Retourneert het een klant-ID? Verifieer of deze klant daadwerkelijk bestaat binnen de organisatie van de ingelogde gebruiker.
- Retourneert het een datum? Controleer of deze plausibel is (niet in het jaar 2099 of vóór de oprichting van het bedrijf).
- Retourneert het een bedrag? Controleer of het getal positief is en binnen realistische grenzen valt.

### 3. Verifieer Geëxtraheerde Waarden Direct Tegen de Bron
Bij data-extractietaken (zoals het uitlezen van een factuurbedrag of een contractdatum) voert u een simpele tekstcontrole uit:
**Komt het getal €340,00 daadwerkelijk voor in de geëxtraheerde tekst van het document?**
Komt de waarde nergens voor in de brondocumenttekst? Dan heeft het model het bedrag ter plekke verzonnen. Met vijf regels code onderschept u 90% van alle financiële hallucinaties.

### 4. Laat Output Nooit Zonder Tussenstap Acties Uitvoeren
Modeloutput die direct resulteert in een databaseschrijfoperatie, een automatische e-mailverzending of een SEPA-incasso is het recept voor zakelijke aansprakelijkheid.

## Ontwerp de Foutafhandeling Eerlijk (*Graceful Degradation*)

Validatie vertelt u dat een antwoord niet deugt. Wat er daarna gebeurt is een cruciale productbeslissing:

- **Probeer het Maximaal Één Keer Opnieuw (*Retry Once*):** Omdat LLM's non-deterministisch zijn, levert een tweede poging met een iets aangepaste prompt vaak wél een valide resultaat op. Probeer het echter nooit vaker dan één keer: drie opeenvolgende fouten betekenen dat het brondocument onleesbaar is, en oneindige retries jagen uw API-rekening omhoog.
- **Wees Eerlijk Tegen de Gebruiker:** *"Wij konden dit document niet automatisch uitlezen — controleer of vul het totaalbedrag a.u.b. handmatig in"*. Gebruikers accepteren een eerlijke waarschuwing direct. Wat ze nóóit vergeven is een softwaretool die stilletjes foute cijfers in hun boekhouding zet.
- **Toon Liever Niets Dan Iets Dat Fout Is:** Laat nooit een lege samenvatting, een nulbedrag of een verzonnen gemiddelde zien dat door de klant voor een echt meetresultaat kan worden aangezien.

## Welke Taken Tolereren Fouten (En Welke Niet?)

Stel uzelf vóór het bouwen de vraag: **wat zijn de zakelijke gevolgen als het model in één op de twintig gevallen fout zit?**

- **Fouttolerante Taken:** Tags suggereren, concept-e-mails schrijven die een medewerker controleert, een document samenvatten ter oriëntatie. Een foutje kost de gebruiker twee seconden om te corrigeren. Dit zijn ideale kandidaten voor AI.
- **Foutintolerante Taken:** Bedragen die gefactureerd worden, juridische clausules beoordelen, medische adviezen formuleren, of data die zonder menselijke controle gepubliceerd wordt. Hier kan één fout leiden tot juridische claims, boetes of direct klantverlies. Deze processen vereisen **altijd een verplichte menselijke controle (*Human-in-the-Loop*)**.

*Een cruciale waarschuwing:* Vraag een AI-model nooit hoe zeker het van zijn antwoord is. Taalmodellen hallucineren met evenveel overtuiging en een "99% betrouwbaarheidsscore" over feiten die volstrekt niet kloppen.

## Maak Alles Bewerkbaar en Meet Correcties

Elke waarde die door een AI-model wordt ingevuld moet door de eindgebruiker **met één klik direct aanpasbaar zijn**.

Houd in uw database bij hoe vaak een veld handmatig gecorrigeerd wordt:
- Wordt de voorgestelde categorie in **8%** van de gevallen aangepast? Uw AI-functie werkt uitstekend.
- Wordt een veld in **55%** van de gevallen overschreven? Uw feature kost klanten meer frustratie dan hij tijd bespaart.

Bij LaunchStudio en Manifera (met meer dan 11 jaar ervaring in robuuste software-architecturen) bouwen we strikte validatielagen, automatische bronverificatie en fouttolerante interfaces tijdens onze [Launch Ready-trajecten](https://launchstudio.eu/nl/#packages). [Bespreek uw AI-implementatie met ons](https://launchstudio.eu/nl/#contact) — wij zorgen dat hallucinaties uw klanten niet bereiken.

## Praktijkvoorbeeld

### De Factuurbedragen Die Spontaan Werd Verzonnen

Kasper Lund runde Bonnetjesbox, een online onkosten- en declaratietool voor zzp'ers en MKB-bedrijven, gebouwd via Lovable. Ondernemers fotografeerden hun bonnetjes en facturen met hun smartphone. Een geavanceerd AI-vision model las de afbeelding in, extraheerde de bedrijfsnaam, de factuurdatum, het totaalbedrag en de btw, en sloeg deze direct op in de financiële administratie van de ondernemer.

Bij scherpe, digitale PDF-facturen functioneerde dit feilloos.

Maar bij verkreukelde thermische kassabonnen, vage scans of lastige hoeken sloeg het model aan het gissen:
Omdat het model in de prompt was opgedragen *"altijd een totaalbedrag en btw te extraheren"*, gaf het **altijd een getal terug** — desnoods ter plekke verzonnen. Er was geen enkele validatiecode ingebouwd.

Het drama kwam aan het licht toen de accountant van een schildersbedrijf een declaratie ontdekte van **€340,00 voor een snelle lunchbon die in werkelijkheid €34,00 bedroeg**.

Toen LaunchStudio de database over de afgelopen drie maanden auditeerde, bleek dat er bij maar liefst **47 administraties** bedragen waren opgeslagen die in het geheel niet op de bijbehorende foto voorkwamen. Dertig van die bonnetjes waren door ondernemers al definitief meegenomen in hun officiële btw-kwartaalaangifte bij de Belastingdienst!

**Resultaat:** Binnen drie werkdagen bracht LaunchStudio een waterdichte beveiligingsarchitectuur aan: modeloutput werd gekoppeld aan een strict JSON-schema, een server-side controlemechanisme verifieerde of het geëxtraheerde bedrag letterlijk voorkwam in de ruwe OCR-tekstlaag van de afbeelding (bij afwezigheid werd het veld direct geel gemarkeerd met het label *"Controle vereist"*), bij twijfel werd maximaal één retry uitgevoerd waarna de gebruiker direct de foto naast een handmatig invoerveld te zien kreeg, en alle correcties werden gemonitord. De 47 gedupeerde ondernemers ontvingen direct een geautomatiseerd hersteloverzicht om naheffingen van de fiscus te voorkomen.

> *"Het model gaf nooit een foutmelding zoals 'deze foto is te wazig'. Het verzon gewoon een getal dat er betrouwbaar uitzag. En dertig van die verzinsels waren al ingediend bij de belastinginspecteur."*
> — **Kasper Lund, Oprichter, Bonnetjesbox**

**Kosten & Doorlooptijd:** AI output validatie, cross-verificatie tegen brondata en fallback UI opgeleverd in 3 werkdagen.

## Veelgestelde Vragen

### Hoe weet ik of de output van een taalmodel klopt?
Door niet blindelings op het model te vertrouwen, maar de output programmatisch te valideren: dwing een JSON-schema af, controleer numerieke grenzen en verifieer bij data-extractie of de geëxtraheerde waarde letterlijk in het brondocument voorkomt.

### Heeft het zin om een mislukte AI-aanroep opnieuw te proberen?
Maximaal één keer. Omdat LLM's non-deterministisch zijn levert een tweede poging vaak wel een correct resultaat op. Blijft het antwoord ongeldig, schakel dan direct over naar een handmatige fallback om kosten en vertraging te voorkomen.

### Wat moet een gebruiker zien wanneer het AI-model faalt?
Een transparante melding dat automatische verwerking niet is gelukt, gecombineerd met een direct invoerveld om de ontbrekende gegevens zelf in te vullen. Toon nooit een stilzwijgende '0' of een willekeurige standaardschatting.

### Welke bedrijfsprocessen zijn te riskant voor volledige AI-automatisering?
Processen met zware financiële, juridische of medische consequenties: bedragen die geïncasseerd worden, kredietbeoordelingen, contractanalyses of geautomatiseerde publieke publicaties. Hier is altijd menselijke supervisie (*human-in-the-loop*) vereist.

### Hoe meet ik of mijn AI-functie kwalitatief goed genoeg presteert?
Monitor de correctieratio in uw database: het percentage keren dat een gebruiker een door AI ingevuld veld handmatig moet overschrijven of aanpassen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is een AI-hallucinatie in software?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een situatie waarin een taalmodel een feitelijk onjuist of verzonnen antwoord genereert met een uiterst overtuigende en zelfverzekerde formulering."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom mag je niet vertrouwen op de 'confidence score' van een LLM?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat taalmodellen niet zelfbewust zijn en met evenveel zelfvertrouwen een hoge score toekennen aan een compleet verzonnen antwoord."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom je dat hallucinaties in de database worden opgeslagen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Door strenge schema-validatie, cross-checks tegen brondocumenten en verplichte menselijke goedkeuring voor kritieke velden."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is een Human-in-the-Loop architectuur?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een ontwerppatroon waarbij AI suggesties en concepten genereert, maar een menselijke gebruiker de definitieve actie moet goedkeuren."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom zijn herhaalde retries bij AI-fouten riskant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat meerdere opeenvolgende pogingen op onmogelijke inputs de reactietijd voor de gebruiker vertragen en onnodig dure API-tokens verbranden."
      }
    }
  ]
}
</script>
