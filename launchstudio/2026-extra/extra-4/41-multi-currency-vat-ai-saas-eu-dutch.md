---
Titel: "Meerdere valuta en btw: wat een AI SaaS-prototype nooit correct afhandelt voor klanten in de EU"
Trefwoorden: ai saas, build ai, EU VAT compliance, multi-currency billing, cross-border invoicing
Koperfase: Beslissing
Doelgroep: SaaS-oprichter scale-up
---
# Meerdere valuta en btw: wat een AI SaaS-prototype nooit correct afhandelt voor klanten in de EU

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Meerdere valuta en btw: wat een AI SaaS-prototype nooit correct afhandelt voor klanten in de EU",
  "description": "Door AI gegenereerde factureringslogica past bijna altijd \u00e9\u00e9n BTW-tarief toe op elke klant, wat stilletjes het moment verbreekt waarop een SaaS-product over de EU-grenzen heen wordt verkocht. Dit is wat btw-afhandeling op productieniveau eigenlijk vereist.",
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
    "@id": "https://launchstudio.eu/en/blog/multi-currency-vat-ai-saas-eu"
  }
}
</script>

Een SaaS-oprichter die zijn thuismarkt overstijgt, ontdekt zijn btw-bug meestal op dezelfde manier: een accountant signaleert dit tijdens een driemaandelijkse controle, maanden nadat de facturen zijn verzonden. Tegen die tijd hoeft er niet meer één slechte factuur te worden gerepareerd; er zijn er honderden, stuk voor stuk technisch niet-conform, en stuk voor stuk een potentiële aansprakelijkheid bij een andere EU-belastingdienst. Dit is een van de stilste en duurste gaten in door AI gegenereerde factureringssystemen, en het komt zelden voor in een demo.

## Waarom "het berekent de belasting" niet hetzelfde is als "het berekent de belasting correct"

Vraag Lovable, Bolt of Cursor om "BTW toe te voegen aan het afrekenen" en je krijgt werkende code: een percentage dat wordt toegepast op een subtotaal, een regelitem op de factuur, een totaal dat optelt. Het lijkt correct, omdat het rekenkundig gezien ook zo is. Wat het bijna nooit doet, is het *juiste* tarief toepassen om de *juiste* reden, omdat de EU-btw voor digitale diensten niet via één enkel nummer werkt. Volgens de btw-regels van de EU voor digitale diensten worden B2C-verkopen belast tegen het tarief van het land van de koper, en niet tegen dat van de verkoper. Dit betekent dat een in Nederland gevestigd SaaS-bedrijf dat aan een klant in Frankrijk verkoopt, Franse btw in rekening brengt, en geen Nederlandse btw. Bij B2B-verkopen wordt daarentegen doorgaans gebruik gemaakt van het verleggingsmechanisme als de koper een geldig btw-nummer opgeeft, waardoor de belastingplicht volledig op de koper wordt afgewenteld.

Een door AI gegenereerde kassastroom heeft geen enkele reden om hier iets van te weten, tenzij iemand het tot in de kleinste details specificeert, en de meeste oprichters weten pas hoe ze erom moeten vragen als het al fout gaat in de productie. De typische foutmodus ziet er precies hetzelfde uit als het onderstaande voorbeeld: het tarief van het thuisland van de verkoper wordt hardgecodeerd en toegepast op elke factuur, ongeacht waar de koper zich daadwerkelijk bevindt. Het doorstaat elke test omdat de oprichter degene is die het test, uit het eigen land van de oprichter.

## Wat is er eigenlijk nodig voor correcte facturering in meerdere valuta en meerdere BTW-tarieven?

Om dit goed te doen, moet het facturatiesysteem de locatie van de klant bepalen met behulp van ten minste twee onafhankelijke signalen (IP-adres en factuuradres, volgens de EU-bewijsregels), BTW-nummers opslaan en valideren via het VIES-systeem voor B2B-verlegging, automatisch het juiste tarief per land toepassen wanneer het wordt bijgewerkt, en facturen genereren met het toepasselijke tarief en de wettelijke basis voor elke regel. Niets daarvan wordt gegenereerd door een prompt als "Add Stripe checkout" - iemand die al eerder grensoverschrijdende facturering heeft ontwikkeld, moet dit expliciet specificeren.

Dit is precies het soort kloof dat de ingenieurs van Manifera dichten voor AI-native SaaS-oprichters. Manifera heeft ruim elf jaar ervaring in productietechniek en heeft facturerings- en compliancesystemen geleverd aan zakelijke klanten als Vodafone en Xpar Vision. Het corrigeren van een BTW-berekening is dus geen giswerk; het is een bekende checklist. Ons team dat werkt vanuit het kantoor in Singapore aan Tras Street 100 ondersteunt oprichters die zich uitbreiden over meerdere belastingjurisdicties, inclusief EU-oprichters wier klantenbestand de veronderstelling van één land is ontgroeid.

Als uw factureringslogica is geschreven voor één land en uw klantenbestand daar voorbij is gegaan, is het de moeite waard om [uw architectuur te vergelijken met ons proces](https://launchstudio.eu/en/#process) vóór de volgende driemaandelijkse indiening, en niet erna.

## Echt voorbeeld

### Een AI-native oprichter in actie: de factureringstool die zijn eigen belasting verkeerd heeft gedaan

Quinten Adriaans, een oprichter uit Roosendaal, bouwde FactuurFlow – een facturerings-SaaS gericht op freelancers – met behulp van Lovable. De ironie ontging hem niet: een tool die was ontwikkeld om freelancers te helpen correct te factureren, factureerde zelf zijn eigen abonnees onjuist. Aan elke klant, ongeacht uit welk EU-land hij of zij zich had aangemeld, werd BTW in rekening gebracht tegen het Nederlandse tarief, omdat dat het enige tarief is dat de door AI gegenereerde factureringslogica ooit heeft gekregen.

Het probleem bleef maandenlang onzichtbaar omdat de eerste klanten van FactuurFlow vooral Nederlands waren. Het kwam naar boven op het moment dat freelancers in België en Duitsland zich gingen aanmelden en hun facturen niet overeenkwamen met wat hun eigen accountants verwachtten. Een paar klanten hebben dit direct gemeld; Quintens eigen boekhouder ving de rest op tijdens een routinecontrole en schatte dat een heel kwart van de grensoverschrijdende facturen opnieuw moest worden uitgegeven.

LaunchStudio heeft de factureringslogica van FactuurFlow opnieuw opgebouwd om het land van elke klant te bepalen op basis van zowel het IP-adres als het factuuradres, het juiste BTW-tarief uit een automatisch bijgewerkte EU-tarieftabel te halen, de logica voor verlegging automatisch toe te passen wanneer een geldig BTW-nummer werd opgegeven, en de getroffen historische facturen opnieuw te genereren met de juiste regelitems. **Resultaat:** FactuurFlow factureert nu correct in elk EU-land waarin het actief is, met een audittrail die een accountant daadwerkelijk kan ondertekenen.

> *"Ik heb een factureringstool gebouwd en op de een of andere manier de exacte bug verzonden die ik mijn klanten probeerde te helpen vermijden. Het op de juiste manier corrigeren van de belastinglogica was niet optioneel; het was het hele product."*
> — **Quinten Adriaans, oprichter, FactuurFlow (Roosendaal)**

**Kosten en tijdlijn:** € 1.800 (revisie van BTW-motor, VIES-integratie, correctie van historische facturen) — voltooid in 9 werkdagen.

---

## Veelgestelde vragen

### Waarom rekent mijn AI-gebouwde SaaS het verkeerde BTW-tarief aan voor buitenlandse klanten?

Omdat de AI-tool standaard is ingesteld op één hardgecodeerd tarief – meestal dat van uw eigen land – tenzij u expliciet op de koperlocatie gebaseerde belastinglogica specificeert, die in de meeste prompts nooit wordt opgenomen.

### Is dit alleen een probleem voor grotere SaaS-bedrijven?

Nee. Elk SaaS-bedrijf dat digitale diensten aan EU-consumenten verkoopt, is wettelijk verplicht om vanaf de allereerste grensoverschrijdende verkoop het landtarief van de koper in rekening te brengen, ongeacht de bedrijfsgrootte.

### Hoe benadert het team van Manifera de BTW-logica anders dan een typische freelancer?

De technici van Manifera hebben facturerings- en nalevingssystemen gebouwd voor zakelijke klanten, waaronder Vodafone, en behandelen daarom de BTW-bepaling als een gestructureerde vereiste – locatiedetectie, opzoeken van tarieven, verwerking van verlegde kosten – in plaats van een enkel belastingpercentage dat aan de kassa wordt gekoppeld.

### Wat is het risico als dit onopgelost blijft?

Onjuiste facturen zorgen voor echte aansprakelijkheid bij meerdere belastingautoriteiten tegelijk, en hoe langer deze loopt, hoe meer historische facturen uiteindelijk moeten worden gecorrigeerd en opnieuw moeten worden uitgegeven.

### Lost LaunchStudio dit alleen op voor in de EU gevestigde oprichters?

Nee – het kantoor van LaunchStudio in Singapore ondersteunt oprichters die vanaf elke locatie naar de EU verkopen, aangezien de locatie van de koper de BTW-verplichtingen bepaalt, ongeacht waar het bedrijf zelf is gevestigd.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why does my AI-built SaaS charge the wrong VAT rate for foreign customers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because the AI tool defaults to a single hardcoded rate \u2014 usually your own country's \u2014 unless you explicitly specify buyer-location-based tax logic, which most prompts never include."
      }
    },
    {
      "@type": "Question",
      "name": "Is this only a problem for larger SaaS companies?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Any SaaS company selling digital services to EU consumers is legally required to charge the buyer's country rate from the very first cross-border sale, regardless of company size."
      }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's team approach VAT logic differently than a typical freelancer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Manifera's engineers have built billing and compliance systems for enterprise clients including Vodafone, so they treat VAT determination as a structured requirement rather than a single tax percentage bolted onto checkout."
      }
    },
    {
      "@type": "Question",
      "name": "What's the risk of leaving this unfixed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Incorrect invoices create real liability with multiple tax authorities simultaneously, and the longer it runs, the more historical invoices eventually need correction and reissue."
      }
    },
    {
      "@type": "Question",
      "name": "Does LaunchStudio only fix this for EU-based founders?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, LaunchStudio's Singapore office supports founders selling into the EU from anywhere, since the buyer's location determines VAT obligations regardless of where the company itself is based."
      }
    }
  ]
}
</script>