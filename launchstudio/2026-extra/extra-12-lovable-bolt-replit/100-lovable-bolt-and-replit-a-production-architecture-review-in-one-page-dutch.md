---
Titel: "Lovable, Bolt en Replit: Een Productiereview van de Architectuur op Eén Pagina"
Trefwoorden: productiereview architectuur, checklist AI-gebouwde app, Lovable productieklaar, Supabase-review, SaaS due diligence, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Lovable, Bolt en Replit: Een Productiereview van de Architectuur op Eén Pagina

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable, Bolt en Replit: Een Productiereview van de Architectuur op Eén Pagina",
  "description": "Honderd artikelen samengevat in een review die een oprichter in een dag kan uitvoeren: tien gebieden, de vraag die er in elk toe doet, de rode vlaggen die incidenten voorspellen, een eenvoudige scoremethode, en hoe u het resultaat omzet in een plan van negentig dagen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-31",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-bolt-and-replit-a-production-architecture-review-in-one-page" }
}
</script>

Deze reeks heeft honderd onderwerpen behandeld, van Mollie tegenover Stripe tot belastingtests, van row level security tot overdrachtsdocumenten. Elk artikel staat op zichzelf. Samen beschrijven ze wat nodig is om een product dat met Lovable, Bolt of Replit is gebouwd iets te laten worden waarop bedrijven kunnen bouwen.

Dat is veel om in gedachten te houden, en weinig oprichters lezen honderd artikelen voordat ze besluiten wat ze als volgende oplossen. Dit laatste artikel vat de reeks samen in één review: tien gebieden, de ene vraag die er in elk het meest toe doet, de rode vlaggen die incidenten het betrouwbaarst voorspellen, een scoremethode, en een manier om het resultaat om te zetten in een plan.

De review is ontworpen om in een dag te worden uitgevoerd door een oprichter, bij voorkeur samen met iemand die de code kan lezen. Ze vindt niet alles. Ze vindt de dingen die, in de producten die in deze reeks zijn beschreven, het vaakst duur werden.

## Hoe U de Review Uitvoert

Reserveer een dag. Open het product, het Supabase-dashboard, het hostingplatform, de repository en uw facturen. Beantwoord voor elk van de tien gebieden hieronder de kernvraag eerlijk, controleer de rode vlaggen, en geef het gebied een score:

- **Groen** - het gebied is in goede staat; niets urgents.
- **Oranje** - er zijn gaten, maar die veroorzaken waarschijnlijk geen incident in de komende drie maanden of zijn goedkoop te herstellen.
- **Rood** - een gat dat kan leiden tot blootgestelde data, verloren data, verloren omzet of een mislukte audit van een klant, of dat duur of onmogelijk terug te draaien is.

Schrijf per score één of twee zinnen onderbouwing. "Back-ups: rood - automatische back-ups aan, nooit teruggezet, geen kopie buiten Supabase" is nuttig; "back-ups: waarschijnlijk in orde" niet.

Wees streng. Het doel van de review is de rode gebieden te vinden voordat een klant, een aanvaller of een auditor dat doet.

## 1. Code en Wijzigingsbeheer

**Kernvraag:** als de laatste wijziging iets brak, zou u die dan in vijf minuten kunnen terugdraaien en precies zien wat er veranderde?

**Rode vlaggen:**
- De code bestaat alleen in de bouwtool, zonder Git-repository die het bedrijf bezit.
- Wijzigingen gaan rechtstreeks naar productie zonder test of review, vanuit een bewerksessie.
- Niemand leest de diff van AI-gegenereerde wijzigingen; grote wijzigingen raken tientallen bestanden.
- Geen tests voor autorisatie, geld of de hoofdflow.

De meeste andere gebieden hangen van dit gebied af. Een product waarvan de code in een repository staat, met kleine gereviewde wijzigingen, een korte testsuite en een poort in CI, kan al het andere veilig oplossen. De artikelen over Git, codereview, tests en CI in deze reeks beschrijven het minimum.

## 2. Datascheiding Tussen Klanten

**Kernvraag:** kan een gebruiker van de ene klant, op welke manier ook - interface, API, een aangepast ID in een URL - de data van een andere klant zien of wijzigen?

**Rode vlaggen:**
- Tabellen zonder row level security, of met policies die voor elke ingelogde gebruiker `true` zijn.
- Organisatie-ID's die uit het verzoek worden gehaald in plaats van uit het lidmaatschap van de gebruiker.
- De service role key in frontendcode, een openbare repository of in handen van een integratiepartner.
- Geen test die als de ene organisatie inlogt en de data van een andere probeert te lezen.

Dit is het gebied waar AI-gebouwde producten het vaakst en het ernstigst falen. De artikelen over IDOR, row level security, teamlidmaatschap en rollen in deze reeks beschrijven de oplossingen; de test tussen organisaties is het bewijs.

## 3. Authenticatie en Toegang

**Kernvraag:** wanneer iemand de organisatie van een klant verlaat, of uw eigen bedrijf, houdt zijn toegang dan echt op?

**Rode vlaggen:**
- Een gebruiker verwijderen haalt hem uit een lijst maar laat zijn lidmaatschap en sessies intact.
- Uitnodigingslinks die nooit verlopen of werken voor iedereen die ze ontvangt.
- Flows voor wachtwoordherstel die verraden of een account bestaat of hergebruikte tokens accepteren.
- Beheerfuncties die alleen worden beschermd door knoppen te verbergen.
- Kritieke accounts - domein, hosting, database - in handen van één persoon.

De artikelen over sessies, wachtwoordherstel, uitnodigingen, SSO en beheerpanelen behandelen dit gebied.

## 4. Geheimen en Configuratie

**Kernvraag:** als uw repository en uw frontendbundel morgen openbaar werden, zou er dan een geheim in staan?

**Rode vlaggen:**
- API-sleutels of service role keys in clientcode, gecommitte bestanden of oude commits.
- Eén set inloggegevens die door ontwikkeling en productie wordt gedeeld.
- Sleutels die nooit zijn geroteerd, inclusief sleutels in handen van voormalige medewerkers.
- Geen lijst van welke geheimen er bestaan en wat elk ervan kan.

De artikelen over het roteren van geheimen, omgevingsvariabelen en Replit Secrets beschrijven hoe u groen bereikt.

## 5. Betalingen en Geld

**Kernvraag:** als uw betaalprovider en uw database het oneens zijn, zou u dat dan weten - en welke zou gelijk hebben?

**Rode vlaggen:**
- Webhooks geaccepteerd zonder controle van de handtekening.
- Geen idempotentie, zodat een herhaalde webhook of dubbele klik een tweede afschrijving of recht oplevert.
- Toegang verleend door de frontend na het afrekenen in plaats van door een gecontroleerd servergebeurtenis.
- Geen maandelijkse afstemming tussen provider, database en boekhouding.
- Btw, factuurnummering en creditnota's ad hoc afgehandeld.

De acht betaalartikelen aan het begin van deze reeks, en het artikel over boekhoudkoppelingen, behandelen de details. Op dit gebied betekent rood meestal dat er al stilletjes geld verloren gaat.

## 6. Back-ups, Herstel en Continuïteit

**Kernvraag:** wanneer hebt u voor het laatst een back-up teruggezet, en hoe lang duurde dat?

**Rode vlaggen:**
- Back-ups aan maar nooit teruggezet.
- Geen kopie van de database of geüploade bestanden buiten het hoofdplatform.
- Geüploade bestanden op het bestandssysteem van een container in plaats van in object storage.
- Geen plan voor het verlies van een kritieke leverancier - e-mail, betalingen, AI-aanbieder, de bouwtool zelf.

Een product dat nog nooit een back-up heeft teruggezet, weet niet of het er een heeft. De artikelen over back-ups, object storage en vendor lock-in beschrijven hoe groen eruitziet.

## 7. Betrouwbaarheid en Beheer

**Kernvraag:** als het product om zeven uur op een maandagochtend stukging, wie zou het dan als eerste weten - u of uw klanten?

**Rode vlaggen:**
- Geen uptimebewaking van buiten het platform.
- Geplande taken en achtergrondwerk zonder runregistratie of waarschuwingen bij afwezigheid.
- Logs die niet op klant of verzoek doorzoekbaar zijn.
- Releases die tegelijk naar alle klanten gaan, met terugdraaien als enige middel.
- Geen statuspagina of afgesproken manier om klanten tijdens een incident te informeren.

De artikelen over monitoring, logs, cron, achtergrondwerk, feature flags en statuspagina's behandelen dit gebied.

## 8. Prestaties en Schaal

**Kernvraag:** hoe gedraagt het product zich met de data van uw grootste klant, op hun drukste uur - en met een klant die twee keer zo groot is?

**Rode vlaggen:**
- Lijsten die elke rij laden; query's zonder indexen op de kolommen waarop ze filteren.
- Functies voor row level security die per rij een subquery draaien.
- Databaseverbindingen die rechtstreeks worden geopend in plaats van via de pooler.
- Aanroepen naar derden binnen verzoeken van gebruikers.
- Geen loadtest vóór de onboarding van een klant die groter is dan alle eerdere.

De artikelen over indexen, paginering, connection pooling en belastingtests beschrijven hoe u deze vindt en oplost voordat klanten dat doen.

## 9. Privacy en Compliance

**Kernvraag:** als de functionaris gegevensbescherming van een klant morgen om uw verwerkersovereenkomst, lijst met subverwerkers en bewaartermijnen vroeg, zou u die dan binnen een dag kunnen sturen?

**Rode vlaggen:**
- Geen sjabloon voor een verwerkersovereenkomst, geen lijst met subverwerkers, geen verwerkingsregister.
- Geen vastgestelde bewaartermijnen; data standaard voor altijd bewaard.
- Analyse, session replay of AI-logging die persoonsgegevens naar niet-vermelde aanbieders stuurt.
- Geen getest proces voor verwijderverzoeken, inzageverzoeken of melding van datalekken.
- Een AI-functie in een context die onder de EU AI Act valt, zonder gedocumenteerde beoordeling.
- Geen toegankelijkheidsreview terwijl klanten onder de European Accessibility Act vallen.

De compliance-artikelen in het midden van deze reeks, en de artikelen over analyse en exports, beschrijven de documenten en processen die dit gebied groen maken.

## 10. Volwassenheid voor Grotere Klanten

**Kernvraag:** wat zou een klant die tien keer zo groot is als uw gemiddelde klant nodig hebben dat u vandaag niet kunt leveren?

**Rode vlaggen:**
- Eén rol per gebruiker; geen afbakening per locatie of afdeling.
- Geen SSO, terwijl prospects vragenlijsten sturen die erom vragen.
- Geen volledige data-export; handmatige query's om verzoeken van klanten te beantwoorden.
- Imports die zonder voorbeeldweergave rechtstreeks in productie schrijven.
- Een API die de automatisch gegenereerde database-interface is in plaats van een contract met versies.
- AI-functies zonder evaluatieset, zodat modelwijzigingen ongetest zijn.
- Documenten die bij het downloaden opnieuw worden gemaakt in plaats van bij uitgifte te worden opgeslagen.

De laatste artikelen in deze reeks - i18n, teams, rollen, SSO, imports, exports, documenten, boekhoudkoppelingen, API-versiebeheer, AI-evaluatie - beschrijven waar grotere klanten doorgaans om vragen, ongeveer in de volgorde waarin ze erom vragen.

## Scores Omzetten in een Plan

Een review levert een lijst op. Een plan bepaalt de volgorde. Drie regels maken die volgorde verstandig.

**Rood vóór oranje, en onomkeerbaar vóór omkeerbaar.** Blootgestelde data, verloren data en geld dat niet meer te innen is, kunnen niet ongedaan worden gemaakt; een trage pagina wel. Los de rode gebieden in twee, vier, vijf en zes op vóór al het andere, ook als ze minder urgent lijken dan het functieverzoek van een klant.

**Fundament vóór functies.** Gebied één - code in een repository, tests, review - maakt elke latere fix veiliger en sneller. Is het rood, dan komt het eerst, omdat iets anders veranderen zonder dit fundament de manier is waarop nieuwe incidenten ontstaan.

**Volg voor de rest de omzet.** Geef onder de oranje gebieden en gebied tien voorrang aan wat de volgende belangrijke klant of de volgende verlenging nodig heeft. Een prospect die op SSO wacht, rechtvaardigt het SSO-werk dit kwartaal; een theoretische enterprisefunctie niet.

Zet het resultaat in een plan van negentig dagen: rode gebieden in de eerste maand, de oranje gebieden die omzet tegenhouden in de tweede, de overige oranje gebieden en de volgende stap in volwassenheid in de derde. Schat elk punt in dagen, wijs elk toe aan een persoon, en bekijk de voortgang elke twee weken. De meeste producten van de omvang die in deze reeks wordt beschreven, kunnen elk rood gebied binnen de eerste maand groen maken.

## Wat Van Rood naar Groen Doorgaans Kost

Oprichters vragen terecht wat het plan kost voordat ze zich eraan verbinden. In de producten die in deze reeks zijn beschreven, valt de moeite per gebied binnen tamelijk consistente bandbreedtes voor een klein of middelgroot Lovable-, Bolt- of Replit-product.

| Gebied | Typische moeite van rood naar groen |
|---|---|
| Code en wijzigingsbeheer | 1–3 dagen: repository, kleine testsuite, poort in CI |
| Datascheiding | 2–4 dagen: policies herschreven, lidmaatschapsmodel, tests tussen organisaties |
| Authenticatie en toegang | 1–3 dagen: verwijderen, uitnodigingen, sessies, controles op beheer |
| Geheimen en configuratie | 0,5–2 dagen: rotatie, scheiding van omgevingen, overzicht |
| Betalingen en geld | 2–5 dagen: controle van webhooks, idempotentie, afstemming |
| Back-ups en continuïteit | 1–3 dagen: exports buiten het platform, hersteltest, exitplannen |
| Betrouwbaarheid en beheer | 1–3 dagen: bewaking, waarschuwingen voor taken, doorzoekbare logs, flags |
| Prestaties en schaal | 2–5 dagen: indexen, paginering, pooling, loadtest |
| Privacy en compliance | 2–4 dagen: overeenkomsten, registers, bewaartermijnen, opschonen van analyse |
| Volwassenheid voor grotere klanten | Per functie: 2–6 dagen elk voor rollen, SSO, exports, API en vergelijkbaar |

De getallen zijn werkdagen, geen doorlooptijd, en gaan ervan uit dat de code in een repository staat; is gebied één rood, dan komt het eerst en maakt het de andere goedkoper. Een product met drie rode en een aantal oranje gebieden heeft doorgaans tien tot twintig dagen werk nodig om een staat te bereiken die een veeleisende klant accepteert - een fractie van een herbouw, en meestal minder dan de waarde van het contract dat de review in gang zette.

De getallen verklaren ook waarom de volgorde ertoe doet. Datascheiding oplossen kost een paar dagen vóór een incident; erna kost het dezelfde paar dagen plus melding, onderzoek, juridisch advies en een klantrelatie.

## Wie de Review Moet Doen

Een oprichter kan de meeste kernvragen alleen beantwoorden, en dat doen is waardevol: het laat zien wat de oprichter niet weet over zijn eigen product. De rode vlaggen in de gebieden twee, drie, vier en acht vragen echter om het lezen van code, policies en queryplannen. Iemand die deze problemen in andere producten heeft gezien, vindt ze in uren in plaats van dagen, en herkent de problemen die onschuldig lijken.

De beste opzet is meestal beide: de oprichter beantwoordt de kernvragen en verzamelt het bewijs, waarna iemand met ervaring de rode vlaggen op codeniveau beoordeelt en de scores ter discussie stelt. Een review van buiten levert ook een document op waar klanten, investeerders en overnemers steeds vaker om vragen.

## Herhaal Het

Een review is een momentopname. Producten die met AI-tools zijn gebouwd, veranderen snel, en een gebied dat in het voorjaar groen was, kan na een paar maanden snel functiewerk in de herfst oranje zijn.

Herhaal de review elke zes maanden, en vóór elk moment waarop er meer op het spel staat: de onboarding van een grote klant, een inkoopproces, een investeringsronde, een gesprek over overname, een wijziging in regelgeving. Bewaar de scores en onderbouwing van elke review, zodat de volgende begint waar de vorige eindigde en de trend zichtbaar is.

Het doel is geen product zonder risico. Het is een product waarvan de risico's bekend, gerangschikt en afnemend zijn - en dat is waar klanten, investeerders en auditors eigenlijk naar vragen wanneer ze vragen of het "productieklaar" is.

## Dit Inrichten

Voor een Lovable-, Bolt- of Replit-product is een review volgens deze structuur doorgaans één tot twee dagen: de tien gebieden gescoord als groen, oranje of rood met geschreven onderbouwing, controles op codeniveau van datascheiding, authenticatie, geheimen en prestaties door iemand met ervaring, een test op toegang tussen organisaties, een test van het terugzetten van een back-up, een review van betaalwebhooks en afstemming, een controle van privacydocumenten, een lijst van wat grotere klanten nodig zouden hebben, een plan van negentig dagen geordend op onomkeerbaarheid, fundament en omzet, en een datum voor de volgende review.

LaunchStudio voert deze review uit voor oprichters die willen weten waar ze staan, en doet daarna het werk dat rood groen maakt - tegen een vaste prijs, vanaf €800 voor het Launch Ready-pakket. Daarachter staat Manifera - elf jaar, 160+ projecten, 120+ engineers, vanaf de Herengracht 420 in Amsterdam en Ho Chi Minh-stad.

[Vraag ons om een productiereview van de architectuur](https://launchstudio.eu/nl/#contact) en ontvang de scores, de onderbouwing en het plan van negentig dagen.

## Echt voorbeeld

### Drie Keer Rood Voordat een Schoolbestuur Ja Zei

Sophie Mulder bouwde Leerlingvolg in Lovable: het volgen van de voortgang van leerlingen, communicatie met ouders en ondersteuningsplannen voor basisscholen, gebruikt door 85 scholen.

Een schoolbestuur dat verantwoordelijk is voor 40 scholen wilde het product op alle scholen invoeren, onder voorbehoud van een beoordeling door zijn functionarissen voor informatiebeveiliging en privacy. Sophie had een vragenlijst met 120 vragen en een deadline van zes weken, en geen duidelijk beeld van welke antwoorden een probleem zouden zijn.

De review duurde twee dagen. Drie gebieden scoorden rood. Zes tabellen met leerlingdata hadden row level security policies waarmee elke ingelogde leerkracht via de API records van andere scholen kon lezen, hoewel de interface ze nooit toonde. Back-ups waren nooit teruggezet, en geüploade ondersteuningsplannen stonden in één opslagbucket zonder kopie elders. En er was geen sjabloon voor een verwerkersovereenkomst, geen lijst met subverwerkers en geen bewaartermijnen - voor een product met data over kinderen, inclusief informatie over extra ondersteuningsbehoeften. Negen gebieden scoorden oranje, waaronder ongeteste geplande taken, sleutels gedeeld tussen omgevingen en een analysescript met session replay aan.

**Resultaat:** het plan van negentig dagen zette de drie rode gebieden in de eerste drie weken: policies herschreven en gecontroleerd met een testsuite tussen scholen, elke nacht versleutelde exports van database en bestanden naar een tweede aanbieder met een getimed herstel, en een verwerkersovereenkomst, lijst met subverwerkers, verwerkingsregister en bewaarregister opgesteld met een privacyjurist. Session replay werd in dezelfde periode verwijderd en omgevingen werden gescheiden. De vragenlijst werd in week vijf met onderbouwing bij elk antwoord ingevuld, de functionarissen van het bestuur kwamen met vier kleine punten, en het contract voor 40 scholen werd in week zeven getekend - ruwweg een verdubbeling van de omzet van het product. Een tweede review zes maanden later scoorde geen enkel rood gebied.

> *"Ik wist dat er vragen zouden zijn die ik niet kon beantwoorden. Ik wist niet dat leerkrachten via de API de leerlingdossiers van andere scholen konden lezen. Twee dagen review vertelden me precies waar ik moest beginnen."*
> - **Sophie Mulder, Oprichter, Leerlingvolg (Amersfoort)**

**Kosten & Doorlooptijd:** €1.800 (productiereview van de architectuur over tien gebieden met controles op codeniveau, test op toegang tussen organisaties, test van terugzetten van back-ups, beoordeling van privacydocumenten, scorerapport met onderbouwing en plan van negentig dagen) - afgerond in 2 werkdagen.

## Veelgestelde vragen

### Wat is een productiereview van de architectuur?

Een gestructureerde controle van de gebieden die in AI-gebouwde producten het vaakst incidenten veroorzaken - codebeheer, datascheiding, toegang, geheimen, betalingen, herstel, beheer, prestaties, privacy en klaar zijn voor grotere klanten - elk gescoord met onderbouwing.

### Hoe lang duurt een review?

Eén tot twee dagen voor de meeste Lovable-, Bolt- of Replit-producten: een dag voor een oprichter om de kernvragen te beantwoorden en bewijs te verzamelen, en tijd voor iemand met ervaring om de rode vlaggen op codeniveau te controleren.

### Wat moet als eerste worden opgelost?

Rode gebieden die onomkeerbaar zijn - blootgestelde data, verloren data, geld dat niet meer te innen is - en het fundament van codebeheer, daarna wat de volgende belangrijke klant of verlenging nodig heeft.

### Kan een oprichter de review alleen uitvoeren?

Gedeeltelijk. Een oprichter kan de kernvragen beantwoorden; datascheiding, authenticatie, geheimen en prestaties vragen om het lezen van code en policies, waar een ervaren reviewer problemen veel sneller vindt.

### Hoe vaak moet de review worden herhaald?

Elke zes maanden, en vóór elk moment waarop veel op het spel staat, zoals de onboarding van een grote klant, een inkoopproces, een investeringsronde of een overname.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is een productiereview van de architectuur voor een AI-gebouwde app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een gescoorde controle van codebeheer, datascheiding, toegang, geheimen, betalingen, herstel, beheer, prestaties, privacy en klaar zijn voor enterprise, met onderbouwing."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt een review op productiegereedheid?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Doorgaans één tot twee dagen, waarin de antwoorden van de oprichter worden gecombineerd met een ervaren controle van risico's op codeniveau."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet na een review als eerste worden opgelost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Eerst onomkeerbare rode gebieden en codebeheer, daarna wat de volgende belangrijke klant of verlenging nodig heeft."
      }
    },
    {
      "@type": "Question",
      "name": "Kunnen oprichters hun eigen product reviewen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Gedeeltelijk - gebieden op codeniveau zoals datascheiding, authenticatie, geheimen en prestaties hebben baat bij een ervaren reviewer."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe vaak moet een productiereview worden herhaald?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Elke zes maanden en vóór momenten met veel op het spel, zoals grote onboardings, inkoop, investering of overname."
      }
    }
  ]
}
</script>
