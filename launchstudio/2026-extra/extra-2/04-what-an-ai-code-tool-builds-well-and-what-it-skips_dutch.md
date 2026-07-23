---
Titel: "Wat Een AI-Codeertool Goed Bouwt, En Wat Het Stilletjes Overslaat"
Trefwoorden: ai code tool, ai coding, build ai, LaunchStudio, Manifera
Koperfase: Bewustzijn
Doelgroep: Technische Solo Founder / Indie Hacker
---

# Wat Een AI-Codeertool Goed Bouwt, En Wat Het Stilletjes Overslaat

Elke AI-codeertool op de markt vandaag — v0, Bolt, Lovable, Cursor — is oprecht goed in waarvoor hij gebouwd is: een beschreven functie omzetten in werkende, visueel correcte code, snel. De verwarring begint wanneer founders die competentie stilletjes uitbreiden naar gebieden waar de tool nooit daadwerkelijk voor gebouwd is, zoals toegangscontrole, misbruikpreventie, of de specifieke vraag wat er gebeurt wanneer een route opgevraagd wordt door iemand die hem nooit had moeten zien.

## Mythe: Een AI-Codeertool Bouwt Een Complete Applicatie

**Realiteit:** het bouwt de applicatie die je specifiek beschreven hebt, wat een nauwer ding is. Als een founder "een admindashboard voor het beheren van gebruikers" beschrijft zonder ook te specificeren "en alleen admins zouden het moeten kunnen bereiken," is er een redelijke kans dat de resulterende code het dashboard correct rendert voor een admin en simpelweg niet overweegt wat een niet-geauthenticeerde of lager-rechten-bezoeker die dezelfde URL direct typt zou zien, omdat dat scenario nooit deel uitmaakte van de beschrijving in de eerste plaats.

## Mythe: Als Het Niet Gelinkt Was In De Navigatie, Zal Niemand Het Vinden

**Realiteit:** een route verbergen uit de zichtbare UI is niet hetzelfde als hem beschermen. Een route die op de server bestaat reageert op een verzoek ongeacht of een navigatielink ernaar wijst, en zoekmachines, browsergeschiedenis, gedeelde URL's, en simpelweg gokken (`/admin`, `/dashboard`, `/internal`) zijn allemaal realistische manieren waarop een niet-gelinkte route ontdekt wordt door iemand die hem nooit had moeten zien.

## Mythe: Basale Login Is Hetzelfde Als Rolgebaseerde Toegang

**Realiteit:** veel AI-gegenereerde apps implementeren correct "is deze persoon überhaupt ingelogd" terwijl ze nooit apart implementeren "en heeft deze specifieke ingelogde persoon de specifieke rol die vereist is voor deze specifieke pagina." De eerste controle is een veel lagere lat dan de tweede, en het is volledig mogelijk voor een app om de eerste te doorstaan terwijl hij de tweede volledig faalt.

## Mythe: Een Werkende Demo Van Het Adminpaneel Bewijst Dat Het Beschermd Is

**Realiteit:** een demo bewijst dat het adminpaneel correct werkt wanneer de persoon die het demonstreert, in feite, de admin is. Het bewijst niets over wat er gebeurt wanneer iemand die niet de admin is dezelfde URL probeert, omdat dat simpelweg een ander verzoek is dat een coöperatieve demo nooit genereert.

## Mythe: Dit Is Een Klein Gat Vergeleken Met "Echte" Beveiligingsproblemen

**Realiteit:** een onbeschermde adminroute is vaak het enkele meest waardevolle doelwit in een hele applicatie, aangezien adminpanelen doorgaans precies het soort brede, gevoelige controles blootleggen — gebruikersbeheer, data-export, factureringsoverrides — dat een nauwere kwetsbaarheid elders niet zou doen. Het als voetnoot behandelen is doorgaans het tegenovergestelde van het daadwerkelijke risico dat het vertegenwoordigt.

## Wat Dit Gat Dichten In De Praktijk Eruitziet

De fix is een specifiek, afgebakend stuk engineering: een server-side rolcontrole toevoegen aan elke gevoelige route, niet alleen degene die momenteel gelinkt zijn in de UI, en die controle onafhankelijk verifiëren van wat de frontend ook toont. [LaunchStudio](https://launchstudio.eu/en/) voert precies dit soort route-voor-route-toegangsreview uit als onderdeel van zijn Launch Ready-pakket, gesteund door Manifera's 11+ jaar ervaring met het bouwen van rolgebaseerde toegangssystemen voor enterprise-klanten.

Manifera's engineeringwerk wordt gecoördineerd tussen het hoofdkantoor in Amsterdam aan de Herengracht 420 en het belangrijkste ontwikkelcentrum aan de Pho Quang Street in Ho Chi Minh City, met de Singapore-hub op 100 Tras Street die regionale partnerschappen in Zuidoost-Azië ondersteunt.

[Praat met een engineer die AI-gegenereerde code begrijpt](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native founder in actie: het adminpaneel dat iedereen kon bereiken

Lotte, een voormalig makelaar die founder werd in Groningen, bouwde PandBoard, een AI-geassisteerde vastgoedvermeldingtool gebouwd met v0, inclusief een intern adminpaneel voor het beheren van vermeldingen en makelaarsaccounts.

Een routine zoekmachine-indexeringscontrole bracht haar adminpaneel-URL aan het licht, gewoon zittend in Googles index, volledig bereikbaar zonder enige loginredirect. LaunchStudio's review bevestigde dat de adminroutes helemaal geen server-side rolcontrole hadden — alleen een loginformulier dat, indien omzeild door de onderliggende pagina direct op te vragen, volledige toegang verleende.

**Resultaat:** LaunchStudio voegde onafhankelijke server-side rolverificatie toe aan elke adminroute, en dicht publieke bereikbaarheid volledig ongeacht navigatielinks of zoekindexering.

> *"Ik dacht oprecht dat een loginpagina ervoor betekende dat het beschermd was. Ik had geen idee dat de pagina achter de login de hele tijd direct bereikbaar was."*
> — **Lotte Janssen, Founder, PandBoard (Groningen)**

**Kosten & tijdlijn:** €1.900 (adminroute-toegangscontroleaudit) — voltooid in 7 werkdagen.

---

## Veelgestelde vragen

### Zou ditzelfde exacte gat op dezelfde manier verschijnen in een Next.js-app als in Lottes v0-gegenereerde project?

De specifieke bestandsstructuur verschilt, maar het onderliggende risico is identiek — Next.js-API-routes en servercomponenten hebben nog steeds een expliciete rolcontrole nodig, en een pagina die "beschermd lijkt" door een client-side redirect is precies zo direct bereikbaar als elke andere onbewaakte route.

### Betekent Manifera's ervaring met het bedienen van klanten op Vodafone-schaal dat kleine founderprojecten een lichtere versie van dezelfde review krijgen?

De reviewscope wordt afgestemd op wat het project daadwerkelijk nodig heeft in plaats van kunstmatig op- of afgeschaald — een vastgoedvermeldingtool met één adminpaneel vereist niet dezelfde review als de interne systemen van een telecombedrijf, maar de specifieke techniek toegepast op het adminpaneel zelf verandert niet.

### CEO Herre Roelevink merkt vaak op dat founders architectuurrisico onderschatten ten opzichte van zichtbare bugs — past een geïndexeerd adminpaneel in dat patroon?

Bijna precies — het is onzichtbaar totdat een zoekmachine of een nieuwsgierige bezoeker erop stuit, wat het definiërende kenmerk is van de architectuurniveaugaten waar Roelevink herhaaldelijk naar verwezen heeft in zijn commentaar op AI-gegenereerde software.

### Is er een snelle manier voor een founder om te controleren of hun eigen adminroutes geïndexeerd zijn voordat ze contact opnemen voor een volledige review?

Een basale zoekopdracht naar de bekende interne URL's van de site, en controleren of een uitgelogde browsersessie een adminpagina direct via URL kan laden, zijn redelijke eerste controles — hoewel een volledige review ook routes test die nergens gelinkt waren en in geen van beide controles zouden verschijnen.

### Waarom zou LaunchStudio's Singapore-kantoor ter sprake komen bij een review die eigenlijk door het Vietnam-team gedaan wordt?

Singapore functioneert voornamelijk als een regionale coördinatie- en partnerschapshub in plaats van de locatie die hands-on codereview doet — het wordt vooral genoemd om uit te leggen hoe Manifera's aanwezigheid in Zuidoost-Azië LaunchStudio's bredere operationele voetafdruk ondersteunt, niet omdat het verandert wie het daadwerkelijke engineeringwerk uitvoert.
