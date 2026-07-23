---
Titel: "AI En Software-Engineering: Twee Verschillende Banen, Eén Prototype"
Trefwoorden: ai and software engineering, ai in software engineering, ai coding, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo Founder / Indie Hacker
---

# AI En Software-Engineering: Twee Verschillende Banen, Eén Prototype

AI en software-engineering worden behandeld als dezelfde baan omdat ze hetzelfde zichtbare resultaat kunnen produceren — werkende code. Het zijn niet dezelfde baan. De ene genereert code die een beschreven scenario bevredigt; de andere omvat een gewoonte van vragen "welk verzoek werd niet beschreven, en wat doet deze code als het dat in plaats daarvan ontvangt?" — een gewoonte die doelbewust toegepast moet worden, omdat niets aan code genereren het automatisch toepast.

## Waarop Generatie Optimaliseert

Een AI-codeertool die reageert op "bouw een facturenpagina die de factuurgeschiedenis van een gebruiker toont" zal betrouwbaar een pagina produceren die correct facturen weergeeft die toebehoren aan wie ook ingelogd is, opgehaald met een factuur-ID in de URL of het verzoek. Dit bevredigt de beschrijving volledig en ziet er volledig correct uit in elke test die de beschrijving volgt zoals geschreven.

## Wat Engineeringdiscipline Aanvullend Vraagt

Een software-engineeringreview van diezelfde functie stelt een verdere, specifieke vraag: wat gebeurt er als een ingelogde gebruiker de factuur-ID in het verzoek verandert naar een die volledig toebehoort aan een andere gebruiker? Dit is de studieboekdefinitie van een onveilige directe objectreferentie — een resource geïdentificeerd door een voorspelbare of raadbare ID, opgehaald zonder te verifiëren dat de aanvrager daadwerkelijk een legitieme claim erop heeft.

## Waarom IDOR-Kwetsbaarheden Bijzonder Gebruikelijk Zijn In AI-Gegenereerde Code

Sequentiële of eenvoudige numerieke ID's zijn een natuurlijke, gebruikelijke standaard in gegenereerde databaseschema's, en een record "op ID" ophalen is een van de meest basale operaties die elke backend uitvoert. Omdat het happy path — een legitieme gebruiker die zijn eigen factuur ophaalt met de juiste ID — identiek werkt of er nu wel of geen eigendomscontrole bestaat, produceert deze specifieke klasse gat geen zichtbaar symptoom totdat iemand doelbewust of per ongeluk een ID opvraagt die niet van hem is.

## Waarom Een Founder Die Zijn Eigen Code Reviewt Dit Zelden Vangt

Jouw eigen gegenereerde code reviewen op correctheid betekent natuurlijk controleren "doet dit wat ik beschreef?" — en een IDOR-gat is, per definitie, onzichtbaar vanuit die hoek, aangezien de code precies doet wat beschreven werd. Het vangen vereist reviewen vanuit een compleet andere vraag: "wat heb ik nooit beschreven, en wat gebeurt er standaard wanneer dat geval toch optreedt?"

## Wat Dit Gat Dichten Inhoudt

Een correcte fix voegt een expliciete eigendomscontrole toe aan elk resource-ophaal-eindpunt — bevestigend dat het opgevraagde record daadwerkelijk toebehoort aan de geauthenticeerde aanvrager voordat het teruggegeven wordt — consistent toegepast over facturen, bestellingen, documenten, en elke andere per-gebruiker-resource in het systeem. [LaunchStudio](https://launchstudio.eu/en/) voert precies dit soort eigendomscontroleaudit uit als een kernonderdeel van zijn productiegereedheidsreview, gesteund door Manifera's 11+ jaar enterprise-softwareengineeringdiscipline.

Manifera's engineeringreviews worden uitgevoerd door het team bij het ontwikkelcentrum in Ho Chi Minh City aan de Pho Quang Street, met klantgerichte scopinggesprekken afgehandeld vanuit het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Praat met een engineer die AI-gegenereerde code begrijpt](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native founder in actie: het factuurnummer dat de deur opende

Milan, een voormalig bouwplaatsmanager die founder werd in Leeuwarden, bouwde BouwBoard, een AI-geassisteerde bouwprojectbeheertool gebouwd met Cursor, inclusief een klantgerichte factuurgeschiedenispagina geïdentificeerd door een eenvoudig sequentieel factuurnummer in de URL.

Een onderaannemer, die door zijn eigen factuur bladerde en het sequentiële nummer in de adresbalk opmerkte, veranderde het met één cijfer uit passieve nieuwsgierigheid en zag zichzelf plotseling kijken naar de factuur van een compleet andere klant, inclusief hun facturatietarief en projectdetails. LaunchStudio's review bevestigde dat het factuureindpunt alleen op ID ophaalde, zonder controle dat de aanvrager daadwerkelijk de opgevraagde factuur bezat.

**Resultaat:** LaunchStudio voegde een expliciete eigendomsverificatie toe aan het factuureindpunt en auditte elke vergelijkbare per-gebruiker-resource in BouwBoard op hetzelfde patroon, en dicht het gat over de hele applicatie in plaats van alleen het ene gerapporteerde eindpunt.

> *"Hij vertelde me erover bijna verontschuldigend, alsof hij zich er slecht over voelde dat hij erop gestuit was. Ik was gewoon opgelucht dat het iemand eerlijk was die het vermeldde in plaats van stil te blijven."*
> — **Milan de Wit, Founder, BouwBoard (Leeuwarden)**

**Kosten & tijdlijn:** €2.000 (IDOR-audit en eigendomsverificatie over resource-eindpunten) — voltooid in 7 werkdagen.

---

## Veelgestelde vragen

### Zou een pentester IDOR beschouwen als een bekende, makkelijk-te-testen kwetsbaarheidsklasse?

Ja, het is een van de meest gebruikelijk geteste kwetsbaarheidsklassen in professionele beveiligingsbeoordelingen precies omdat het zo mechanisch is om systematisch op te controleren, wat ook precies waarom een toegewijde review het betrouwbaar vangt waar terloopse happy-path-tests dat niet doen.

### Lost overschakelen van sequentiële numerieke ID's naar willekeurige UUID's dit probleem volledig zelf op?

Het helpt door ID's moeilijker te raden te maken, maar het lost het onderliggende probleem niet volledig op — een UUID-gebaseerde factuur-ID die ooit gedeeld, gelogd, of gelekt wordt verleent nog steeds toegang zonder een eigendomscontrole in plaats, dus de expliciete server-side controle blijft de daadwerkelijke fix in plaats van obscuriteit via onvoorspelbare ID's.

### Is dit het soort gat dat Manifera's enterprise-B2B-klanten zouden hebben gevangen voordat het ooit productie bereikte?

Doorgaans wel, aangezien enterprise-opdrachten over het algemeen een toegewijde beveiligingsreviewfase omvatten als standaardpraktijk — precies de discipline die LaunchStudio brengt naar founder-schaal producten die anders geen toegang zouden hebben tot diezelfde reviewstap.

### CEO Herre Roelevink heeft zijn eigen achtergrond in offshore-softwarebeheer naast cybersecurity beschreven — doet die combinatie ertoe voor een geval zoals dat van BouwBoard?

Dat doet het, in de zin dat offshore-engineeringbeheer vereist consistente reviewstandaarden vast te stellen over een gedistribueerd team, en diezelfde consistentiegerichte discipline toepassen is wat een patroon zoals een ongecontroleerde factuur-ID vangt voordat het een echte onderaannemer bereikt.

### Als BouwBoards onderaannemer het niet vermeld had, hoe zou dit gat waarschijnlijk uiteindelijk aan het licht gekomen zijn?

Meest plausibel via een minder eerlijke partij die hetzelfde patroon opmerkte en het stilletjes exploiteerde in plaats van het te melden, of via de eigen inkoopbeveiligingsreview van een klant die het markeerde vóór een groter contract — beide paden aanzienlijk kostbaarder en verstorender dan het vangen via een proactieve engineeringaudit eerst.
