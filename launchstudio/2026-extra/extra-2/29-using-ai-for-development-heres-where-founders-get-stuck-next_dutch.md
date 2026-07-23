---
Titel: "AI Gebruiken Voor Ontwikkeling? Hier Lopen Founders Vervolgens Vast"
Trefwoorden: ai for development, ai in development, ai coding, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Founder (niet-technisch)
---

# AI Gebruiken Voor Ontwikkeling? Hier Lopen Founders Vervolgens Vast

AI gebruiken voor ontwikkeling brengt een founder opmerkelijk ver voordat ze hun eerste oprechte muur raken. Die muur ziet er zelden uit als "de AI kon deze functie niet bouwen." Het ziet er meestal meer uit als: de functie werkt, een gebruiker rapporteerde iets vreemds over zijn eigen account, en niemand kan precies uitleggen waarom een simpele profielupdate hem iets liet veranderen dat hij nooit had mogen aanraken.

## Waar De Muur Doorgaans Verschijnt

De specifieke muur die veel founders raken betreft een update-eindpunt — een profielbewerkingsformulier, een accountinstellingenpagina — dat een bredere set velden van het verzoek accepteert dan het zichtbare formulier daadwerkelijk presenteert. Als het verzoek van een gebruiker velden kan omvatten voorbij wat de UI toont, en de backend slaat op welke velden ook aanwezig zijn zonder ze te filteren, kan een verzoek gemaakt (doelbewust of per ongeluk) om een extra veld te omvatten data wijzigen die de UI nooit van plan was bloot te stellen voor bewerking.

## Waarom Dit Een Mass-Assignment-Kwetsbaarheid Wordt Genoemd

Het patroon heeft een specifieke, gevestigde naam in software-engineering omdat het specifiek en terugkerend genoeg is om goed gedocumenteerd te zijn: een backend die "mass assigns" — welke velden een verzoek ook bevat rechtstreeks naar een databaserecord toewijst, zonder een expliciete lijst van welke velden daadwerkelijk toegestaan zijn om bijgewerkt te worden via dat specifieke eindpunt, vertrouwt erop dat het verzoek alleen ooit redelijke velden bevat — een aanname die standhoudt tijdens normaal UI-gestuurd gebruik en breekt op het moment dat een verzoek rechtstreeks gemaakt wordt.

## Waarom Een Werkend Profielformulier Hier Geen Geruststelling Biedt

Een profielbewerkingsformulier testen door het daadwerkelijk te gebruiken — een naam veranderen, een telefoonnummer bijwerken — stuurt alleen ooit de velden die dat specifieke formulier omvat, dus het onthult nooit wat de backend zou doen met extra velden die het formulier toevallig niet indient. Het gat gaat volledig over wat mogelijk is buiten de eigen beperkingen van het formulier, niet over iets zichtbaar verkeerds aan het formulier zelf.

## Waarom Een Accountrolveld Het Slechtst Mogelijke Veld Is Om Onbeschermd Te Laten

Als een gebruikersrecord een rol- of toestemmingsveld omvat — "lid," "admin," "moderator" — en dat veld niet expliciet uitgesloten is van wat een profielupdate kan wijzigen, kan een specifiek vervaardigd verzoek mogelijk dat veld rechtstreeks instellen, en verhoogde rechten verlenen zonder dat er ooit een legitiem autorisatieproces bij betrokken was.

## Wat Dit Fixen Vereist

Een correcte fix definieert expliciet welke velden elk specifiek eindpunt mag bijwerken — een allow-list in plaats van accepteren wat een verzoek toevallig bevat — consistent toegepast over elk update-pad in een applicatie, niet alleen degene die een founder onthoudt te controleren. [LaunchStudio](https://launchstudio.eu/en/) auditeert precies dit patroon over een hele codebase, gesteund door Manifera's 11+ jaar backend-engineeringdiscipline toegepast op founder-schaal producten.

Manifera's backend-beveiligingsaudits worden uitgevoerd door het engineeringteam bij het ontwikkelcentrum in Ho Chi Minh City aan de Pho Quang Street, met klantgesprekken afgehandeld via het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Praat met een engineer die AI-gegenereerde code begrijpt](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native founder in actie: de profielupdate die admintoegang verleende

Lars, een voormalig uitzendbureaurecruiter die founder werd in Roosendaal, bouwde WerfMakelaar, een AI-geassisteerd recruitment- en uitzendplatform gebouwd met Cursor, dat onderscheid maakte tussen standaard recruiteraccounts en administratoraccounts met bredere platformtoegang.

Een partner die het platform namens Lars testte, tijdens het inspecteren van verzoeken uit technische nieuwsgierigheid, ontdekte dat het profielupdate-eindpunt een rolveld accepteerde naast naam en contactgegevens, en dat het indienen van een verzoek met de rol ingesteld op "admin" daadwerkelijk het toestemmingsniveau van het account veranderde, zonder enige server-side controle die het verhinderde. LaunchStudio's review bevestigde dat het update-eindpunt elk aanwezig veld in het verzoek opsloeg zonder enige allow-list-beperking.

**Resultaat:** LaunchStudio implementeerde een expliciete allow-list op elk update-eindpunt in WerfMakelaar, zorgend dat alleen bedoelde velden ooit gewijzigd kunnen worden via elk specifiek formulier ongeacht wat een verzoek verder zou kunnen bevatten, en dicht het rechtenescalatierisico platformbreed.

> *"Hij liet me zien wat hij gedaan had en ik begreep aanvankelijk oprecht niet waarom dat zelfs mogelijk was. Het was nooit bij me opgekomen dat hetzelfde eindpunt dat een telefoonnummerupdate afhandelde theoretisch ook admintoegang kon uitdelen."*
> — **Lars Verbeek, Founder, WerfMakelaar (Roosendaal)**

**Kosten & tijdlijn:** €2.100 (mass-assignment-audit en allow-list-implementatie over update-eindpunten) — voltooid in 7 werkdagen.

---

## Veelgestelde vragen

### Zou een backend-beveiligingsspecialist mass assignment een gebruikelijke kwetsbaarheidsklasse beschouwen in moderne webframeworks?

Ja, gebruikelijk genoeg dat veel gevestigde webframeworks ingebouwde mechanismen omvatten specifiek om het te voorkomen, hoewel die mechanismen actief geconfigureerd en correct gebruikt moeten worden — simpelweg toegang hebben tot de beschermende functie betekent niet automatisch dat elk eindpunt in een project het correct toepast.

### Geldt dit risico alleen voor velden zoals accountrollen, of is het breder?

Het is breder — elk veld dat een gebruiker niet direct zou moeten kunnen wijzigen, inclusief dingen zoals accountsaldi, abonnementsstatus, of eigendomsreferenties, draagt hetzelfde onderliggende risico als een eindpunt opslaat wat een verzoek ook bevat in plaats van expliciet te beperken welke velden toegestaan zijn.

### Manifera heeft decennia gecombineerde backend-engineeringervaring — helpt dat specifiek bij het snel vangen van mass-assignment-problemen in een onbekende codebase?

Ja, omdat het patroon om naar te zoeken goed gedefinieerd en consistent is ongeacht de specifieke applicatie — engineers ervaren in backend-beveiligingsreview weten specifiek de veldafhandelingslogica van elk update-eindpunt te controleren als een kwestie van routine, in plaats van het risico elke keer opnieuw vanaf nul te moeten ontdekken.

### Is dit het soort probleem waar CEO Herre Roelevink naar verwijst wanneer hij architectuurgaten beschrijft die niet zichtbaar zijn in een werkende demo?

Ja, precies — een profielupdate die correct werkt voor zijn bedoelde velden geeft geen zichtbare indicatie van wat het verder stilletjes zou kunnen accepteren, wat precies de onzichtbaar-totdat-adversarieel-getest-categorie is waar Roelevink herhaaldelijk naar verwezen heeft in het bespreken van AI-gegenereerd softwarerisico.

### Als een founder een bekend backendframework gebruikte met ingebouwde mass-assignment-bescherming, zou dit dan nog steeds kunnen gebeuren?

Ja, als de beschermende functie niet correct ingeschakeld of geconfigureerd is voor elk specifiek eindpunt — toegang hebben tot een veiligheidsmechanisme en het consistent correct toepassen over een hele codebase zijn twee verschillende dingen, en AI-gegenereerde code garandeert het laatste niet automatisch alleen omdat het framework het eerste ondersteunt.
