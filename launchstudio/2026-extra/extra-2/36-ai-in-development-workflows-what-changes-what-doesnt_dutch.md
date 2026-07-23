---
Titel: "AI In Ontwikkelworkflows: Wat Verandert, Wat Niet"
Trefwoorden: ai in development, ai for development, ai coding, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo Founder / Indie Hacker
---

# AI In Ontwikkelworkflows: Wat Verandert, Wat Niet

AI in ontwikkelworkflows verandert hoe snel een functie gebouwd wordt. Het verandert niet waartoe die functie fundamenteel in staat is zodra hij live is — en een handige "importeer productafbeelding vanaf een URL"-functie, snel en correct gebouwd om precies die beschrijving te bevredigen, is fundamenteel tot veel meer in staat dan een afbeelding tonen, tenzij iets het specifiek stopt.

## Wat Een "Importeer Vanaf URL"-Functie Daadwerkelijk Doet Onder De Motorkap

Een functie die een gebruiker een URL laat plakken waarna jouw server ophaalt wat er ook op dat adres staat — een afbeelding, een document, elke resource — betekent noodzakelijk dat jouw eigen server degene is die dat uitgaande verzoek doet, niet de browser van de gebruiker. Dit is een oprecht handig patroon, en AI-codeertools implementeren het bereidwillig wanneer een founder beschrijft dit soort "plak een link, wij halen het op"-functionaliteit te willen.

## Waarom "Jouw Server Haalt Het Op" Het Specifieke Risico Is

Als de URL die een gebruiker levert op geen enkele manier beperkt is, is er niets dat een verzoek tegenhoudt om interne netwerkadressen te targeten die jouw server kan bereiken maar het publieke internet niet — interne adminpanelen, clouddienst-metadatadiensten, of andere backendsystemen die nooit bedoeld waren van buitenaf bereikbaar te zijn, maar die jouw eigen server, het verzoek makend namens de gebruiker, direct kan bereiken.

## Waarom Dit Server-Side-Request-Forgery Genoemd Wordt

De naam beschrijft precies wat er gebeurt: een verzoek wordt vervalst (vervaardigd door een buitenstaander) maar server-side uitgevoerd (door jouw eigen vertrouwde infrastructuur), en geeft een aanvaller een manier om interne systemen te onderzoeken of ermee te interageren met gebruikmaking van de eigen netwerkpositie en het vertrouwensniveau van jouw server, in plaats van hun eigen, veel beperktere externe uitkijkpunt.

## Waarom Testen Met Echte Afbeeldings-URL's Dit Nooit Onthult

Een "importeer vanaf URL"-functie testen door echte, externe afbeeldingslinks te plakken — wat het enige is dat een founder die deze functie bouwt en test natuurlijk zou doen — bevestigt dat de functie correct publieke afbeeldingen ophaalt en toont. Het biedt nul informatie over wat er gebeurt als iemand in plaats daarvan een intern netwerkadres levert, aangezien dat simpelweg geen URL is die een founder die normale functionaliteit test enige reden heeft te proberen.

## Wat Deze Functie Correct Beperken Vereist

Een veilige implementatie valideert dat een geleverde URL resolveert naar een oprecht publiek, extern adres voordat het opgehaald wordt, en blokkeert expliciet verzoeken naar interne of gereserveerde netwerkbereiken ongeacht hoe de URL geformuleerd of vermomd is. [LaunchStudio](https://launchstudio.eu/en/) implementeert precies dit soort URL-validatie als onderdeel van zijn backend-beveiligingsreview, gesteund door Manifera's 11+ jaar ervaring met het beveiligen van server-side integraties over productiesystemen.

Manifera's SSRF- en backend-integratiebeveiligingswerk wordt geleverd via het ontwikkelcentrum in Ho Chi Minh City aan de Pho Quang Street, gecoördineerd met het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Praat met een engineer die AI-gegenereerde code begrijpt](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native founder in actie: de afbeeldingsimport die te ver reikte

Wessel, een voormalig logistiekcoördinator die founder werd in Vlaardingen, bouwde VoorraadVast, een AI-geassisteerde magazijnvoorraadbeheertool gebouwd met Cursor, inclusief een handige functie waarmee magazijnpersoneel een productfoto direct kon importeren vanaf een geleverde URL in plaats van handmatig een bestand te uploaden.

Het beveiligingsbewuste IT-contact van een partner, dat VoorraadVast reviewde voorafgaand aan een potentiële integratie, testte de importfunctie met een intern netwerkadres in plaats van een publieke afbeeldings-URL en ontdekte dat de server probeerde op te halen en terug te geven wat het daar ook vond — wat bevestigde dat de functie geen beperking had op welk soort adres het ook zou benaderen. LaunchStudio's review bevestigde dat de onderliggende ophaal-logica elke URL accepteerde en opvroeg zonder te valideren dat het een oprecht publieke bestemming was.

**Resultaat:** LaunchStudio voegde strikte validatie toe die ervoor zorgt dat de importfunctie alleen ophaalt van geverifieerde publieke, externe adressen, en blokkeerde expliciet elk verzoek gericht op interne of gereserveerde netwerkbereiken, en dicht de blootstelling zonder te veranderen hoe personeel de importfunctie gebruikte voor legitieme productfoto's.

> *"Ik bouwde die functie om personeel een paar klikken te besparen bij het importeren van productfoto's. Het kwam nooit één keer bij me op dat datzelfde gemak theoretisch gericht kon worden op iets compleet anders dan een foto."*
> — **Wessel Kramer, Founder, VoorraadVast (Vlaardingen)**

**Kosten & tijdlijn:** €2.600 (SSRF-herstel en URL-ophaalvalidatie) — voltooid in 8 werkdagen.

---

## Veelgestelde vragen

### Zou een backend-beveiligingsspecialist SSRF een gebruikelijke bevinding beschouwen in specifiek AI-gegenereerde code, of een zeldzame, exotische?

Steeds gebruikelijker, specifiek omdat "haal een resource op vanaf een URL die de gebruiker levert" zo'n natuurlijke, frequent gevraagde functiebeschrijving is, en valideren dat de opgehaalde bestemming veilig is een aparte, aanvullende vereiste is die specifiek geïmplementeerd moet worden in plaats van aangenomen te worden dat het gebundeld komt met de basale ophaalfunctionaliteit.

### Raakt dit risico alleen functies expliciet beschreven als "importeer vanaf URL," of verschijnt het ook elders?

Het verschijnt in elke functie waar gebruikersinvoer een uitgaand server-side verzoek beïnvloedt — webhook-callback-URL's, PDF-generatiediensten die externe inhoud ophalen, of link-previewfuncties dragen allemaal een of andere versie van hetzelfde onderliggende risico als de bestemming niet correct beperkt is.

### Manifera's engineering heeft server-side integraties beveiligd voor enterprise-klanten — draagt die ervaring over naar een kleinere voorraadtool zoals VoorraadVast?

Ja, direct — het specifieke validatiepatroon (bevestig dat een bestemming oprecht publiek is voordat het opgehaald wordt) is identiek ongeacht bedrijfsgrootte, en een al bewezen enterprise-patroon toepassen op een founder-schaal product is aanzienlijk sneller en betrouwbaarder dan de correcte aanpak vanaf nul ontwikkelen voor elk nieuw geval.

### Herre Roelevink heeft de huidige uitdaging beschreven als over architectuur gaan in plaats van ruwe functie-output — past een SSRF-gat goed bij die framing?

Heel goed — de importfunctie functioneerde precies zoals beschreven vanuit een functie-output-perspectief; het ontbrekende stuk was een architecturale beslissing over wat de server namens een gebruiker wel en niet zou moeten mogen bereiken, precies de categorie waar Roelevinks commentaar consistent naar verwijst.

### Is er een manier voor een founder om zelf op dit soort gat te testen vóór een professionele review?

Een founder met enig technisch comfort kan proberen een intern adres (zoals een lokaal netwerkadres) te leveren aan elke "haal op vanaf URL"-functie en observeren of het verzoek slaagt, hoewel elke mogelijke manier om een interne bestemming te vermommen correct en uitgebreid blokkeren doorgaans het soort systematische validatie vereist die een toegewijde beveiligingsreview implementeert.
