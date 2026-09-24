---
Titel: "Een AI-App voor Contractondertekening Bouwen? Beveiliging van AI-Code voor Digitale Handtekeningen"
Trefwoorden: ai gegenereerde code beveiliging, digitale handtekening app, eidas elektronische handtekening, documentintegriteit, cursor contract app, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-oprichters / Indie Hackers
---

# Een AI-App voor Contractondertekening Bouwen? Beveiliging van AI-Code voor Digitale Handtekeningen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Een AI-App voor Contractondertekening Bouwen? Beveiliging van AI-Code voor Digitale Handtekeningen",
  "description": "Een digitale handtekening is juridisch alleen zoveel waard als het bewijs dat je eromheen kunt leveren. Dit artikel behandelt de beveiligingsrisico's in zelfgebouwde ondertekenstromen — documentintegriteit, identificatie van ondertekenaars, veilige links, audit trails en eIDAS-niveaus.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-08",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/building-an-ai-contract-signing-app-ai-generated-code-security-for-e-signatures" }
}
</script>

"Voeg een handtekeningveld toe aan de offertepagina." Het is een van de meest gevraagde instructies aan een AI-codeertool, en Cursor levert binnen enkele minuten een keurige HTML5 canvas waar klanten met hun vinger of muis hun naam tekenen, een knop die de afbeelding opslaat en een PDF waar de handtekening onderaan wordt geplakt. Visueel ziet het eruit als een volwaardige ondertekening. Maar of dit standhoudt wanneer een klant later de geldigheid van het contract betwist voor de rechter, is een heel ander verhaal — en dat is waar applicatiebeveiliging en juridische bewijskracht elkaar ontmoeten.

## Wat een Handtekening Moet Kunnen Bewijzen

Wanneer een ondertekende overeenkomst wordt aangevochten, draait het juridische geschil nooit om de vraag hoe mooi het krabbeltje eruitziet. De vier doorslaggevende vragen zijn:

1. **Wie heeft er ondertekend?** Kun je aantonen dat de handtekening daadwerkelijk afkomstig is van de genoemde persoon?
2. **Wat is er precies ondertekend?** Kun je bewijzen dat het document na ondertekening op geen enkele manier meer is gewijzigd?
3. **Wanneer is er ondertekend?** Is het tijdstip onafhankelijk en betrouwbaar vastgelegd?
4. **Was er sprake van een duidelijke wilsovereenstemming?** Was het zetten van de handtekening een bewuste, ondubbelzinnige handeling?

Een simpel plaatje van een handtekening geplakt op een PDF beantwoordt geen enkele van deze vragen overtuigend. Het digitale bewijsdossier eromheen doet dat wel.

## Het Juridische Kader in het Kort (eIDAS)

Binnen de Europese Unie onderscheidt de eIDAS-verordening drie niveaus van elektronische handtekeningen:
- **Gewone elektronische handtekening (SES):** kan zo eenvoudig zijn als een getypte naam, een vinkje of een getekend krabbeltje. Juridisch geldig, maar de bewijskracht hangt volledig af van de kwaliteit van het ondersteunende bewijs.
- **Geavanceerde elektronische handtekening (AES):** is op unieke wijze gekoppeld aan de ondertekenaar, kan de ondertekenaar identificeren, is gemaakt onder uitsluitende controle van de ondertekenaar en is zodanig aan het document gekoppeld dat elke latere wijziging direct traceerbaar is.
- **Gekwalificeerde elektronische handtekening (QES):** een geavanceerde handtekening aangemaakt met een gekwalificeerd middel (zoals itsme of eID) en een gekwalificeerd certificaat. Deze heeft in de hele EU automatisch dezelfde juridische status als een handgeschreven handtekening op papier.

Voor offertes en reguliere B2B- en B2C-overeenkomsten volstaat doorgaans een gewone of geavanceerde handtekening met een solide bewijsdossier.

## Veelvoorkomende Beveiligingslekken in AI-Gegenereerde Tekenstromen

**Voorspelbare of permanente links.** URL's zoals `/sign/1042` stellen iedereen in staat om willekeurige contracten in te zien of namens een ander te ondertekenen. Ondertekenlinks moeten bestaan uit cryptografisch willekeurige tokens met een beperkte geldigheidsduur die na ondertekening direct vervallen.

**Geen verificatie van de identiteit.** Iedereen die de link bezit kan tekenen. Verifieer minimaal het e-mailadres via een magische link en overweeg een eenmalige SMS-code (OTP) voor waardevolle contracten.

**Veranderlijke (dynamische) documenten.** Als de PDF elke keer dynamisch vanuit databasevelden wordt opgebouwd zodra de link wordt geopend, verandert een latere veldwijziging in de database stilletjes het "ondertekende" contract. Het exacte document moet vóór ondertekening definitief worden 'bevroren' als statisch bestand.

**Geen cryptografische integriteitsgarantie.** Zonder een cryptografische hash (SHA-256) van het definitieve PDF-bestand kun je achteraf niet aantonen dat de inhoud na ondertekening niet is gemanipuleerd.

**Ontbrekende audit trail.** Een robuust bewijsdossier legt exact vast wanneer het document is verzonden, geopend, pagina voor pagina is bekeken en ondertekend, inclusief IP-adressen, browsergegevens (user-agents) en verificatiemethoden.

**Tijdstempels vanuit de browser.** Tijdstempels die door de browser van de gebruiker worden doorgegeven zijn triviaal te manipuleren. Gebruik altijd servertijd of een gecertificeerde tijdstempeldienst.

**Publieke opslag van ondertekende contracten.** Getekende contracten bevatten adresgegevens, prijzen en handtekeningen. Publieke cloudbuckets zijn uit den boze; private storage met tijdelijke gesigneerde downloadlinks is de absolute norm.

## Het Document 'Bevriezen' Vóór Ondertekening

De belangrijkste technische regel: de klant moet een definitief, onveranderlijk bestand ondertekenen, en geen live database-weergave. Genereer de definitieve PDF op het moment van verzending, sla deze beveiligd op, bereken de unieke SHA-256 hash en toon exact dat bestand aan de ondertekenaar:

```typescript
import { createHash } from "crypto";

const pdf = await renderQuotePdf(quoteId);             // eenmalig genereren
const hash = createHash("sha256").update(pdf).digest("hex");
await storage.put(`contracts/${quoteId}/v${version}.pdf`, pdf, { private: true });
await db.insert("document_versions", { quoteId, version, hash, frozenAt: new Date() });
```

## Zelf Bouwen of een Gespecialiseerde Provider Integreren?

Voor eenvoudige, laag-risico offertes en orderbevestigingen kan een zorgvuldig gebouwde eigen module volstaan, mits de hash, audit trail en linkbeveiliging kloppen. Voor contracten met grote financiële belangen, arbeidsovereenkomsten of wanneer geavanceerde/gekwalificeerde handtekeningen vereist zijn, is het integreren van een Europese handtekeningen-API (zoals SignRequest, Yousign of Scrive) veruit de veiligste route.

## Waar LaunchStudio Past

LaunchStudio licht ondertekenstromen in AI-gebouwde software grondig door en brengt ze op productieniveau: cryptografische document-hashing, onaanpasbare bevroren PDF's, veilige eenmalige links, e-mail- en SMS-verificatie, gecertificeerde servertijdstempels, complete audit logs en privégehoste documentopslag. Indien vereist koppelen we een erkende Europese handtekeningenprovider via API en webhooks.

LaunchStudio wordt ondersteund door Manifera, waarvan CEO Herre Roelevink zijn carrière startte in cybersecurity. De ingenieurs in Ho Chi Minhstad bouwen al ruim 11 jaar veilige bedrijfskritische documentplatformen, ondersteund vanuit de Herengracht 420 in Amsterdam. Bekijk [Manifera's maatwerk software-ontwikkeling](https://www.manifera.com/services/custom-software-development/) en raadpleeg de [officiële eIDAS-informatiepagina van de Europese Commissie](https://digital-strategy.ec.europa.eu/en/policies/eidas-regulation).

[Praat met een ervaren engineer](https://launchstudio.eu/nl/#contact) vóórdat je te maken krijgt met je eerste betwiste contract.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Teken-App voor Aannemers en een Betwiste Dakofferte

Loes Vermaat, hoofd administratie van het dakdekkersbedrijf van haar familie in Gorinchem, bouwde Tekenklaar met behulp van Cursor: een webapplicatie waarmee zelfstandige aannemers offertes en werkopdrachten digitaal naar klanten sturen, die klanten vervolgens ter plekke op hun smartphone ondertekenen. Vijfenveertig aannemersbedrijven maakten er gebruik van, en in het eerste jaar werden circa 900 opdrachten digitaal getekend.

Toen een huiseigenaar een factuur van € 14.000 voor een complete dakrenovatie weigerde te betalen — met de bewering dat de geaccordeerde offerte een bedrag van € 11.500 vermeldde — kon Tekenklaar het tegendeel niet bewijzen. De "ondertekende PDF" werd namelijk telkens wanneer iemand op de downloadlink klikte opnieuw dynamisch gegenereerd vanuit de database, en de aannemer had na de ondertekening een kleine materiaalpost in het systeem gecorrigeerd. De ondertekenlinks bestonden uit simpele opeenvolgende ID's (`/sign/482`) zonder verloopdatum. Er was geen enkele identiteitscontrole behalve het bezit van de link, de tijdstempel kwam uit de browser van de consument en alle getekende PDF's stonden in een publiek toegankelijke cloudbucket.

In acht werkdagen saneerden de engineers van LaunchStudio de complete ondertekenarchitectuur: elk document werd op het moment van verzending direct bevroren als statische PDF en voorzien van een unieke SHA-256 hash; tekenlinks werden vervangen door cryptografisch willekeurige tokens die na 14 dagen of na ondertekening direct vervallen; er werd e-mailverificatie en optionele tweestapsverificatie via SMS-code toegevoegd voor klussen boven een instelbaar bedrag; alle systeemacties kregen een server-tijdstempel van een officiële Network Time Protocol-service; getekende documenten werden technisch vergrendeld tegen wijzigingen (elke aanpassing vereist voortaan een formele nieuwe revisie); contracten verhuisden naar private storage met versleuteling; en aan elke voltooide PDF werd automatisch een officieel certificaatblad (*signing summary*) toegevoegd.

**Resultaat:** Het juridische geschil met de huiseigenaar kon dankzij de gereconstrueerde logs alsnog worden geschikt. Sindsdien zijn twee latere meningsverschillen binnen enkele uren opgelost dankzij het onweerlegbare certificaatblad, en Tekenklaar groeide door naar 70 aangesloten bouw- en installatiebedrijven.

> *"De handtekening zag er op het scherm prachtig uit. Maar alles wat nodig was om juridisch te bewijzen dat die handtekening echt was, ontbrak volledig."*
> — **Loes Vermaat, Oprichter, Tekenklaar (Gorinchem)**

**Kosten & Tijdlijn:** € 2.400 (Launch Ready-pakket: documentintegriteit, beveiligde tekenlinks, tweestapsverificatie, bewijsdossier en integratieopties) — afgerond in 8 werkdagen.

## Veelgestelde Vragen

### Is een getekend krabbeltje op een PDF juridisch bindend?

In de EU geldt dit als een 'gewone elektronische handtekening'. Het is op zichzelf rechtsgeldig, maar bij een juridisch geschil is de bewijskracht minimaal als je niet kunt bewijzen wie er tekende, wanneer dat gebeurde en of het document daarna ongewijzigd is gebleven.

### Wat moet een digitaal bewijsdossier (audit trail) bevatten?

Verzend-, open- en ondertekengebeurtenissen met betrouwbare servertijdstempels, IP-adressen, browser-metadata, de verificatiemethode van de ondertekenaar en een SHA-256 hash van het exacte document — onveranderlijk opgeslagen.

### Moet ik zelf een ondertekenmodule bouwen of een bestaande provider integreren?

Voor eenvoudige offertes met beperkte financiële belangen volstaat een goed beveiligde eigen flow. Voor zwaarwegende contracten, arbeidsvoorwaarden of documenten die gekwalificeerde handtekeningen (QES) vereisen, is integratie van een officiële eIDAS-provider verstandig.

### Hoe vertaalt Manifera's cybersecurity-achtergrond zich naar ondertekenflows?

Omdat integriteit en onweerlegbaarheid (non-repudiation) fundamentele principes van informatiebeveiliging zijn, toetst Manifera tekenprocessen altijd op cryptografische geldigheid en fraudebestendigheid.

### Versterkt een professioneel ondertekenproces het online vertrouwen van een B2B-app?

Zeker. Ondernemers en klanten ervaren transparantie en rechtszekerheid bij het ondertekenen, wat geschillen voorkomt en leidt tot positieve zakelijke reviews die zoekmachines en AI-assistenten direct registreren.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is een getekend krabbeltje op een PDF juridisch bindend?",
      "acceptedAnswer": { "@type": "Answer", "text": "Het geldt als gewone handtekening; zonder sluitend bewijsdossier en hash is de bewijskracht bij een geschil echter zeer zwak." }
    },
    {
      "@type": "Question",
      "name": "Wat moet een digitaal bewijsdossier (audit trail) bevatten?",
      "acceptedAnswer": { "@type": "Answer", "text": "Tijdgestempelde verzend- en tekenacties, IP-adressen, verificatiemethoden en een cryptografische SHA-256 hash van het document." }
    },
    {
      "@type": "Question",
      "name": "Moet ik zelf een ondertekenmodule bouwen of een bestaande provider integreren?",
      "acceptedAnswer": { "@type": "Answer", "text": "Zelfbouw volstaat voor lichte offertes mits goed beveiligd; integreer een erkende eIDAS-provider bij grote financiële belangen." }
    },
    {
      "@type": "Question",
      "name": "Hoe vertaalt Manifera's cybersecurity-achtergrond zich naar ondertekenflows?",
      "acceptedAnswer": { "@type": "Answer", "text": "Integriteit en onweerlegbaarheid worden behandeld als harde security-eisen ter voorkoming van contractmanipulatie." }
    },
    {
      "@type": "Question",
      "name": "Versterkt een professioneel ondertekenproces het online vertrouwen van een B2B-app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, transparante en fraudebestendige ondertekening voorkomt conflicten en versterkt de reputatie bij zakelijke gebruikers." }
    }
  ]
}
</script>
