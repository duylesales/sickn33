---
Titel: "Wat investeerders daadwerkelijk vragen wanneer ze 'gebouwd met AI' horen in een pitch"
Trefwoorden: ai native, ai native founder, investor due diligence ai startup, pitching an ai built product
Koperfase: Beslissing
Doelgroep: AI-Native oprichter (niet-technisch)
---
# Wat investeerders daadwerkelijk vragen wanneer ze 'gebouwd met AI' horen in een pitch

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wat investeerders daadwerkelijk vragen wanneer ze 'gebouwd met AI' horen in een pitch",
  "description": "Als u zegt dat uw product 'gebouwd is met AI', roept dat een specifieke reeks vervolgvragen van investeerders op. Dit is wat ze daadwerkelijk vragen, en hoe u zich kunt voorbereiden.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/what-investors-ask-built-with-ai" }
}
</script>

De zin "we hebben dit met AI gebouwd" was ooit een flex tijdens een pitchgesprek. Nu is het de opening voor een reeks vragen waar de meeste oprichters niet op voorbereid zijn. Investeerders hebben inmiddels genoeg van dit soort pitches gezien om te weten dat "gebouwd met AI" van alles kan betekenen, van "we hebben doordacht aangepaste logica met modelaanroepen gecombineerd" tot "we hebben een app aan Lovable beschreven en verzonden wat eruit kwam". Ze proberen u niet te betrappen. Ze proberen te achterhalen welke van de twee u bent, want de risicoprofielen verschillen enorm. Dit is wat ze daadwerkelijk vragen, onder het geklets door.

## "Neem me mee door de architectuur"

Dit is geen strikvraag en vereist geen informatica-diploma om goed te beantwoorden. Wat een investeerder wil horen is een duidelijke kaart: wat is de frontend, wat is de backend, waar leeft de data, wat praat met wat. Als uw eerlijke antwoord is "ik weet het eigenlijk niet zeker, de tool heeft het gebouwd", is dat het moment waarop de sfeer in het gesprek daalt. U hoeft de code niet te schrijven. U moet de vorm ervan kunnen beschrijven.

## "Welke delen zijn echt AI, en welke delen zijn gewoon software?"

Dit is de vraag waar de meeste oprichters over struikelen, omdat het de vraag is waar niet-technische oprichters het minst op voorbereid zijn om die delen te scheiden. Investeerders hebben geleerd dat "AI-powered" vaak één kleine functie betekent die een model aanroept, verpakt in een veel grotere hoeveelheid volledig conventionele software — authenticatie, een database, een UI. Ze willen de verhouding weten, want die vertelt hen wat ze eigenlijk waarderen: een echte AI-capaciteit, of een normaal product met een AI-garnering.

## "Wat gebeurt er als de modelleverancier de voorwaarden, prijzen of toegang wijzigt?"

Investeerders hebben genoeg AI-afhankelijke producten zien wankelen door een prijswijziging van een leverancier om deze vraag reflexmatig te stellen. Als u geen antwoord heeft — een fallbackplan, een kostenplafond, een alternatief leveranciertraject — wordt dat gelezen als een enkel storingspunt midden in uw businessmodel.

## "Wie heeft de beveiliging en gegevensverwerking beoordeeld?"

AI-coderingstools genereren snel werkende software, maar "werkend" en "veilig" zijn niet dezelfde eigenschap. Investeerders weten steeds vaker dat een aanzienlijk deel van door AI gegenereerde code met gaten in autorisatie, gegevensblootstelling of invoervalidatie wordt verzonden. Als uw antwoord is "nog niemand, het werkte gewoon tijdens het testen", verwacht dan een vervolgvraag over uw plan om dat gat te dichten voordat u opschaalt.

## "Zou u dit kunnen herbouwen zonder de AI-tool, als het moest?"

Deze vraag gaat eigenlijk over afhankelijkheid van de oprichter versus afhankelijkheid van de tool. Investeerders willen de geruststelling dat de waarde van het product leeft in uw begrip van het probleem en de architectuur, en niet volledig in een black box die u niet zelfstandig kunt uitleggen of onderhouden.

Lotte Jansen, een oprichter in Utrecht, liep recht tegen deze muur op. Ze bouwde "GroeiMetric", een analysedashboard, met Cursor, en had een veelbelovend eerste pitchgesprek — totdat een investeerder haar vroeg de technische architectuur toe te lichten en aan te geven welke delen van het product echt "AI" waren versus aangepaste logica. Ze had geen kant-en-klaar antwoord, en het gesprek liep vast op een vraag waar ze nog nooit eerder over had hoeven nadenken.

Dit is precies het gat dat LaunchStudio wil dichten voordat het een oprichter een investeringsronde kost. Gesteund door Manifera — vertrouwd door zakelijke klanten waaronder Vodafone, TNO en CFLW — werkt ons team, inclusief engineers gevestigd in Singapore, rechtstreeks met niet-technische oprichters om de architectuur duidelijk genoeg te documenteren om investeerdersonderzoek te doorstaan, niet alleen om een demo te doorstaan. U kunt [een gratis intro-gesprek van 15 minuten boeken](https://launchstudio.eu/nl/#contact) als u een pitch voor de boeg heeft en uw architectuurverhaal op orde wilt hebben voordat u de kamer binnenstapt. Voor de standaard waaraan onze engineers klantwerk houden, zie [de aanpak van Manifera](https://www.manifera.com/about-us/).

## Uw Architectuur-Antwoord op Één A4 Voorbereiden Voordat U Binnenstapt

De zes vragen over architectuur laten zien wat zakelijke inkopers en technische auditors gaan onderzoeken. De sleutel tot een succesvol gesprek is om niet ter plekke te improviseren, maar vooraf een beknopt, feitelijk architectuurdocument van één A4 klaar te hebben. Dit document beantwoordt de vragen voordat ze worden gesteld en straalt direct volwassenheid uit:

**Deel 1: De Dataflow & Hosting Locatie.** Beschrijf in drie zinnen waar uw servers fysiek draaien (bijvoorbeeld AWS Frankfurt of Supabase EU-West), hoe data in rust (AES-256) en in overdracht (TLS 1.3) wordt versleuteld, en garandeer dat gegevens van Europese klanten de EER niet verlaten.

**Deel 2: Autorisatie- en Scheidingsmodel.** Geef exact aan hoe multi-tenancy is geïmplementeerd. Vermeld expliciet dat gegevensscheiding wordt afgedwongen via Row-Level Security op databaseniveau en geautomatiseerde tenant-isolatie, waardoor cross-tenant datalekken technisch uitgesloten zijn.

**Deel 3: AI-Privacy en Modelverwerking.** Vermeld zwart-op-wit welke LLM-leveranciers worden gebruikt, via welke enterprise-overeenkomsten (met de expliciete garantie van een 'Zero Data Retention' beleid en het verbod op modeltraining op klantdata), en welke gegevens vóór verzending worden geanonimiseerd.

**Deel 4: Back-ups, SLA en Incidentenrespons.** Benoem de frequentie van automatische database-back-ups (dagelijks met point-in-time recovery), de hersteltijd (RTO en RPO) en het escalatiepad bij eventuele productiestoringen.

Wanneer u een zakelijke prospect dit gestructureerde overzicht kunt overhandigen op het moment dat hun security-officer begint over de vragenlijst, verandert de toon van het gesprek onmiddellijk van wantrouwen naar professioneel partnerschap.


## Echt voorbeeld

### Een AI-native oprichter in actie: De vraag die Lottes pitch deed vastlopen

Lotte Jansen had GroeiMetric gebouwd om een echt probleem op te lossen — Nederlandse mkb-bedrijven hadden een eenvoudigere manier nodig om groeicijfers bij te houden zonder een data-analist aan te nemen. Met Cursor kon ze snel bewegen, en tegen de tijd dat ze investeerders pitchte, zag het product er gepolijst uit, werkte het betrouwbaar in demo's en had het een handvol betalende pilotklanten. Ze voelde zich klaar.

Het gesprek verliep goed totdat een investeerder, middenin het gesprek, haar vroeg de technische architectuur toe te lichten: wat was de datapijplijn, waar zat de "AI" eigenlijk in de stack, en wat was op maat gebouwd versus gegenereerd door de tool. Lotte besefte dat ze deze onderdelen nooit eerder in haar eigen hoofd had hoeven scheiden — Cursor had het geheel als één doorlopende flow gebouwd, en zij had zich gericht op de productervaring, niet op de onderliggende kaart. Ze gaf een vaag antwoord, de vragen van de investeerder bleven doorborduren, en het gesprek eindigde met een beleefd "laten we contact houden" dat nooit echt tot een termsheet leidde.

Lotte bracht GroeiMetric daarna naar LaunchStudio, niet voor een herbouw, maar voor precies dit: een duidelijke architectuurbeoordeling en documentatie die ze in haar eigen woorden kon toelichten in het volgende gesprek. Engineers brachten het systeem in kaart, gaven aan wat echt AI-gedreven was versus standaard applicatielogica, signaleerden onderweg een paar beveiligingsgaten, en maakten een architectuursamenvatting in gewone taal waar Lotte vol vertrouwen over kon spreken.

**Resultaat:** Lottes volgende investeerdersgesprek bevatte dezelfde architectuurvraag — deze keer beantwoordde ze die in minder dan twee minuten, zonder notities.

> *"Ik hoefde geen engineer te worden. Ik had iemand nodig die me de kaart gaf van wat ik al had gebouwd."*
> — **Lotte Jansen, oprichter, GroeiMetric (Utrecht)**

**Kosten en tijdlijn:** € 900 (architectuurbeoordeling en oprichter-gerichte documentatie) — voltooid in 3 werkdagen.

---

## Veelgestelde vragen

### Moet ik code begrijpen om investeerdersvragen over architectuur te beantwoorden?

Nee. Investeerders willen een duidelijke conceptuele kaart van wat uw product doet en hoe de onderdelen samenhangen, geen regel-voor-regel codetoelichting.

### Wat is de meest gemaakte fout van oprichters bij "gebouwd met AI"-pitches?

Het hele product behandelen als één ongedifferentieerde AI-black box, in plaats van de echte AI-gedreven delen te kunnen scheiden van de onderliggende standaard applicatielogica.

### Hoe helpt het team van Manifera oprichters zich voor te bereiden op dit soort onderzoek?

De engineers van Manifera, inclusief het team gevestigd in Singapore, beoordelen de architectuur van een door AI gegenereerd product en vertalen dit naar documentatie in gewone taal die een niet-technische oprichter vol vertrouwen kan presenteren.

### Moet ik beveiligingsgaten bij investeerders noemen voordat ze ernaar vragen?

Over het algemeen wel — proactief een bekend gat en uw plan om het op te lossen benoemen komt veel beter over dan onvoorbereid betrapt worden wanneer een investeerder er rechtstreeks naar vraagt.

### Kan dit soort beoordeling snel gebeuren vóór een pitch-deadline?

Ja, architectuurbeoordelingen worden doorgaans binnen een paar werkdagen gescoped en opgeleverd, wat vaak genoeg doorlooptijd is vóór een vervolggesprek met een investeerder.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik code begrijpen om investeerdersvragen over architectuur te beantwoorden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Investeerders willen een duidelijke conceptuele kaart van wat uw product doet en hoe de onderdelen samenhangen, geen regel-voor-regel codetoelichting."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de meest gemaakte fout van oprichters bij \"gebouwd met AI\"-pitches?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het hele product behandelen als één ongedifferentieerde AI-black box, in plaats van de echte AI-gedreven delen te kunnen scheiden van de onderliggende standaard applicatielogica."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt het team van Manifera oprichters zich voor te bereiden op dit soort onderzoek?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De engineers van Manifera, inclusief het team gevestigd in Singapore, beoordelen de architectuur van een door AI gegenereerd product en vertalen dit naar documentatie in gewone taal die een niet-technische oprichter vol vertrouwen kan presenteren."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik beveiligingsgaten bij investeerders noemen voordat ze ernaar vragen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Over het algemeen wel — proactief een bekend gat en uw plan om het op te lossen benoemen komt veel beter over dan onvoorbereid betrapt worden wanneer een investeerder er rechtstreeks naar vraagt."
      }
    },
    {
      "@type": "Question",
      "name": "Kan dit soort beoordeling snel gebeuren vóór een pitch-deadline?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, architectuurbeoordelingen worden doorgaans binnen een paar werkdagen gescoped en opgeleverd, wat vaak genoeg doorlooptijd is vóór een vervolggesprek met een investeerder."
      }
    }
  ]
}
</script>
