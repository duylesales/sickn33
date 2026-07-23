---
Titel: "Beveiliging En AI: Waarom Het Tweede Woord De Hulp Van Het Eerste Nodig Heeft"
Trefwoorden: security and ai, ai and security, ai secure, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo Founder / Indie Hacker
---

# Beveiliging En AI: Waarom Het Tweede Woord De Hulp Van Het Eerste Nodig Heeft

Beveiliging en AI klinken alsof ze bij elkaar horen in een zin, en steeds vaker worden ze zo op de markt gebracht — "AI-aangedreven beveiliging," "secure by design." Wat die formulering de neiging heeft te verhullen is een veel minder vleiende waarheid voor founders die bouwen met AI-codeertools: de AI-helft van dat paar versterkt de beveiligingshelft niet automatisch. Iemand moet nog steeds specifiek vragen om toestemmingstracking, databewaringslimieten, en toegangslogging, omdat geen van die dingen verschijnt als een natuurlijke consequentie van een functie die simpelweg werkt.

## Waarom Toestemmingslogging Een Aparte Vereiste Is Van "Het Werkt"

Een functie die een familielid toestaat een zorgverlener toegang te geven tot het schema en gezondheidsnotities van een oudere familielid kan volledig correct werken — de toegangsverlening gebeurt, de zorgverlener ziet wat hij hoort te zien — zonder ooit vast te leggen wanneer en hoe toestemming voor die toegang daadwerkelijk gegeven werd. Functioneel is de functie compleet. Vanuit een compliance- en verantwoordingsstandpunt ontbreekt er nog iets essentieels.

## Waarom Dit Onderscheid Meer Ertoe Doet Met Specifiek Gezondheidsgerelateerde Data

Gezondheidsgerelateerde persoonsdata draagt een hogere lat onder GDPR dan gewone accountinformatie, doorgaans vereisend een duidelijkere, aantoonbare grondslag voor verwerking en vaak een auditspoor dat bewijst dat die grondslag bestaat. Een AI-codeertool die een toegangsdelingsfunctie genereert heeft geen inherent bewustzijn van die verhoogde lat tenzij de prompt het specifiek beschreef — het bouwt gewoon het delingsmechanisme zoals beschreven, met toestemmingsspoor alleen inbegrepen als toestemmingsspoor expliciet deel uitmaakte van de beschrijving.

## Waarom Een Werkende Functie Hier Valse Geruststelling Biedt

Founders beoordelen natuurlijk de volledigheid van een functie op basis van of het doet wat het hoort te doen, en een zorgtoegang-delingsfunctie die succesvol toegang verleent en intrekt slaagt makkelijk voor die test. De specifieke, aparte vraag — kunnen we later bewijzen wie toestemming gaf voor wat, en wanneer — wordt nooit getest door gewoon gebruik, omdat gewoon de functie gebruiken nooit vereist dat historische record op te halen.

## Waarom Dit Gat De Neiging Heeft Op Het Slechtst Mogelijke Moment Aan Het Licht Te Komen

Ontbrekende toestemmingsrecords veroorzaken zelden een zichtbaar probleem tijdens dagelijkse operatie. Ze worden urgent zichtbaar tijdens een geschil, een regelgevende vraag, of een verzoek om toegang tot persoonsgegevens — precies de momenten waarop een founder het meest moet aantonen wat er precies gebeurde en waarom, en precies de momenten waarop ontdekken dat het record nooit bijgehouden werd het meest schadelijk is.

## Wat Een Correcte Fix Daadwerkelijk Toevoegt

Dit gat dichten betekent een specifiek, append-only auditlog toevoegen dat elke toestemmingsverlening, -wijziging, en -intrekking vastlegt, gekoppeld aan een tijdstempel en de identiteit van wie het autoriseerde — geïmplementeerd naast de bestaande toegangsdelingsfunctie in plaats van een deel ervan te vervangen. [LaunchStudio](https://launchstudio.eu/en/) bouwt precies dit soort toestemmings- en auditlogging als onderdeel van zijn GDPR-gerichte reviewproces, gesteund door Manifera's 11+ jaar ervaring met compliancegevoelige B2B-systemen.

Manifera's compliancegerelateerd engineeringwerk wordt geleverd via het ontwikkelcentrum in Ho Chi Minh City aan de Pho Quang Street, met klantscopinggesprekken afgehandeld vanuit het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Plan een gratis introductiegesprek van 15 minuten](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native founder in actie: de zorgtoegang die niemand kon traceren

Bas, een voormalig thuiszorgcoördinator die founder werd in Almere, bouwde ZorgVerbind, een AI-geassisteerd ouderenzorgcoördinatieplatform gebouwd met Cursor, waarmee familieleden professionele zorgverleners toegang konden geven tot het schema en de zorgnotities van een familielid.

Een familiegeschil over wie de toegang van een specifieke zorgverlener geautoriseerd had triggerde een verzoek dat Bas niet kon vervullen: een duidelijk record van wanneer en door wie die toegang oorspronkelijk verleend was. LaunchStudio's review bevestigde dat de toegangsdelingsfunctie correct werkte maar helemaal geen historisch toestemmingsspoor bijhield — alleen de huidige staat van wie momenteel toegang had.

**Resultaat:** LaunchStudio voegde een append-only auditlog toe die elke toegangsverlening, -wijziging, en -intrekking voortaan vastlegt, en werkte met Bas samen om de dataverwerkingspraktijken van het platform dienovereenkomstig te documenteren, en dicht het compliancegat zonder te veranderen hoe families en zorgverleners de delingsfunctie daadwerkelijk gebruikten.

> *"De functie zelf werkte de hele tijd precies zoals bedoeld. Het kwam gewoon nooit bij me op dat 'werkte' en 'kan bewijzen wat er zes maanden geleden gebeurde' twee compleet verschillende dingen waren."*
> — **Bas Terpstra, Founder, ZorgVerbind (Almere)**

**Kosten & tijdlijn:** €2.400 (implementatie toestemmings- en toegangsauditlogging) — voltooid in 8 werkdagen.

---

## Veelgestelde vragen

### Zou een functionaris gegevensbescherming ontbrekende toestemmingslogging een technisch gat noemen of een governance-gat?

Beide, en de overlap is het punt — het is een governance-vereiste (aantonen van rechtmatige grondslag voor verwerking) die vervuld moet worden via een technisch mechanisme (een daadwerkelijk auditspoor), dus geen van beide framings alleen vangt volledig waarom dit doelbewuste engineeringaandacht vereist in plaats van alleen een beleidsdocument.

### Geldt dit soort gat alleen voor gezondheidsgerelateerde producten, of breder?

Het geldt het meest acuut voor gezondheidsgerelateerde en andere gevoelige-data-producten vanwege de verhoogde compliancelat, maar elk product dat persoonsgegevens verwerkt onder een expliciete toestemmingsgrondslag profiteert van hetzelfde soort auditeerbaar spoor, aangezien "we zijn er vrij zeker van dat dit geautoriseerd was" een zwakke positie is in elk geschil.

### Manifera heeft gewerkt met onderzoeksgerelateerde klanten zoals TNO aan datagevoelige projecten — informeert die achtergrond hoe toestemmingslogging ontworpen wordt?

Ja — projecten met gevoelige onderzoeksdata hebben lang precies dit soort aantoonbaar, auditeerbaar toestemmingsspoor vereist, en datzelfde ontwerppatroon draagt direct over naar een founder-gebouwd ouderenzorgplatform dat analoge, zij het kleinschaligere, verplichtingen onder ogen ziet.

### Is dit het soort gat waar CEO Herre Roelevink naar verwijst wanneer hij de verschuiving van software bouwen naar het verantwoordelijk architecteren ervan beschrijft?

Ja, precies — een toestemmingslog is geen functie waarmee een gebruiker direct interageert of die hij opmerkt, precies de categorie onzichtbare architecturale beslissing waar Roelevink herhaaldelijk naar verwezen heeft als het moeilijkere, minder voor de hand liggende deel van software bouwen vandaag.

### Zou een founder zelf basale toestemmingslogging kunnen toevoegen zonder een volledige audit, gewoon door een spreadsheet bij te houden?

Een handmatig record kan dienen als noodoplossing, maar het schaalt niet betrouwbaar en is gevoelig voor vergeten worden of uit sync raken met de daadwerkelijke staat van het systeem — een geëngineerd, append-only log rechtstreeks gekoppeld aan de toegangverlenende code zelf is wat daadwerkelijk garandeert dat het record niet stilletjes uit de accuraatheid kan drijven.
