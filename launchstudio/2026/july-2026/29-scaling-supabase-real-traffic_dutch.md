---
Titel: Schalen Supabase: wat u moet doen als uw app echt verkeer krijgt - AI om te coderen
Trefwoorden: AI om te coderen, Schaalvergroting, Supabase, Traffic
Koperfase: Bewustzijn
---

# Supabase schalen: wat u moet doen als uw app echt verkeer krijgt

Jij bent gelanceerd. De productjacht ging goed, een TikTok ging viraal en ineens heb je 5.000 actieve gebruikers. Gefeliciteerd, u heeft nu een schaalprobleem. Voor door AI gebouwde apps die op Supabase draaien, verschijnen de eerste tekenen van stress meestal als langzaam laden van pagina's, time-outfouten of waarschuwingen voor databaseverbindingen. Hier is een handleiding voor de oprichters over de drie directe hefbomen die u moet gebruiken om uw Supabase-backend te schalen.

## Hendel 1: De ontbrekende indexen

AI-tools schrijven functionele queries, maar schrijven bijna nooit database-indexen. Dit is de belangrijkste reden dat door AI gebouwde apps onder belasting tot stilstand komen.

Stel je voor dat je iemand vraagt ​​om het woord 'Supabase' op te zoeken in een boek van 500 pagina's. Zonder index moeten ze elke afzonderlijke pagina van begin tot eind lezen (in databasetermen een "sequentiële scan"). Dit gaat snel als het boek 2 pagina's lang is (uw prototypefase). Het is tergend langzaam als het boek 10.000 pagina's lang is.

Een index vertelt de database precies waar de gegevens zich bevinden. Als uw app facturen regelmatig filtert op `organization_id`, moet u een index voor die kolom maken.

**De oplossing**: Open het Supabase-dashboard, ga naar het tabblad **Queryprestaties** en zoek naar zoekopdrachten die zijn gemarkeerd als 'Opeenvolgende scans'. Vraag uw AI-assistent om "Een SQL-opdracht te schrijven om een ​​index voor deze query toe te voegen." Door dat eenvoudige commando uit te voeren, wordt de laadtijd van 5 seconden vaak teruggebracht tot 50 milliseconden.

## Hendel 2: Verbindingspooling

Als uw React/Next.js-app wordt gehost op Vercel en met Supabase praat, gebruikt u een serverloze architectuur. Dit betekent dat elke keer dat een gebruiker een pagina laadt, er een nieuwe tijdelijke serverloze functie wordt gestart die probeert verbinding te maken met uw database.

PostgreSQL-databases hebben een harde limiet voor directe, gelijktijdige verbindingen (vaak tussen 60 en 100 op lagere niveaus). Als een virale piek 500 gelijktijdige gebruikers oplevert, zullen de verbindingen uitgeput raken, wat resulteert in "Verbindingspool vol"-fouten en crashes.

**De oplossing**: u moet de ingebouwde verbindingspooler van Supabase (Supavisor) gebruiken. In plaats van rechtstreeks verbinding te maken met de database via poort `5432`, werkt u uw omgevingsvariabelen bij om verbinding te maken via de poolingpoort (meestal `6543`). De pooler fungeert als verkeersagent, accepteert duizenden verbindingen van Vercel en leidt deze efficiënt door de beperkte verbindingen die uw database toestaat.

## Hendel 3: Compute upgraden

Als je indexen hebt toegevoegd en verbindingspooling hebt geïmplementeerd, maar je dashboard laat zien dat het CPU- of RAM-gebruik consistent boven de 80% ligt, dan ben je je hardware ontgroeid. Het Supabase Pro-abonnement ($ 25/maand) biedt een royale basiscomputer, maar een echt succesvolle app zal uiteindelijk meer pk's nodig hebben.

**De oplossing**: Met Supabase kunt u de onderliggende serverhardware met een paar klikken in het dashboard opschalen (Compute Add-ons). U kunt het RAM-geheugen en de CPU upgraden om zwaardere belastingen aan te kunnen. Dit vereist een korte herstart van de database (minuten downtime), maar vereist geen codewijzigingen of datamigratie.

## De verborgen prestatiemoordenaar: te veel ophalen

Een laatste probleem dat uniek is voor door AI gegenereerde code is overmatig ophalen. AI schrijft vaak zoekopdrachten zoals `SELECT * FROM gebruikers`. Hierdoor wordt elke kolom opgehaald, inclusief grote tekstvelden of binaire gegevens, zelfs als de gebruikersinterface alleen de naam van de gebruiker hoeft weer te geven.

Bij 100 gebruikers maakt overfetchen niet uit. Bij 10.000 gebruikers zorgt de overdracht van enorme hoeveelheden onnodige gegevens via het netwerk voor ernstige knelpunten.

**De oplossing**: bekijk de API-aanroepen in uw frontend-code. Herstructureer `select('*')` om alleen de kolommen op te geven die daadwerkelijk door de gebruikersinterface worden gebruikt, zoals `select('id, first_name, last_name')`. Hierdoor wordt de netwerkbelasting kleiner en wordt de weergave aanzienlijk versneld.

## Belangrijkste inzichten

- De belangrijkste oorzaak van trage Supabase-apps zijn ontbrekende database-indexen. Voeg indexen toe aan vaak opgevraagde kolommen.

- Serverloze apps (zoals Next.js op Vercel) moeten verbindingspooling gebruiken (poort 6543) om te voorkomen dat de database crasht bij te veel verbindingen.

- AI-code haalt vaak gegevens op (SELECT *). Refactor-query's om alleen de specifieke benodigde kolommen op te halen.

- Als de optimalisatie mislukt, kunt u de Supabase-rekenhardware rechtstreeks vanaf het dashboard upgraden zonder de code te wijzigen.

## Crasht uw app onder belasting?

De prestatie-audit van LaunchStudio identificeert ontbrekende indexen, optimaliseert inefficiënte AI-query's en configureert robuuste verbindingspooling zodat uw app feilloos kan worden geschaald.

LaunchStudio wordt beheerd door **Manifera**, een internationaal software-engineeringbedrijf onder leiding van oprichter en directeur **Herre Roelevink**. Manifera combineert 'Nederlands management met Vietnamees meesterschap' en heeft het hoofdkantoor in **Amsterdam, Nederland** (Herengracht 420) en ontwikkelingscentra in **Singapore** en **Ho Chi Minh City, Vietnam**. Via LaunchStudio implementeren onze senior engineeringteams uw door AI gebouwde frontend en implementeren ze productieklare beveiligingscontroles, live betalingsgateways, veilige hosting en monitoring, waardoor uw prototype binnen 1 tot 3 weken wordt getransformeerd in een veilige en compatibele MVP. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: AI-klantenondersteuningswidget

Michael, de oprichter van een startup, gebruikte **Cursor** om een prototype van een AI-klantenondersteuningswidget te bouwen. Hoewel de applicatie functioneel was, crashte deze toen een nieuwsbrief van een klant 4.000 gelijktijdige bezoekers trok, waardoor de Postgres-database werd vergrendeld.

Michael werkte samen met **LaunchStudio (door Manifera)** om het product lanceringsklaar te maken. Het technische team optimaliseerde de databaseverbindingen met Supabase Supavisor en implementeerde Redis-caching voor statische reacties.

**Resultaat:** Michael stabiliseerde het systeem, waardoor de widget moeiteloos meer dan 10.000 verzoeken per uur kon verwerken.

**Kosten en tijdlijn:** € 2.600 (schaal- en optimalisatiepakket) — klaar voor productie en geïmplementeerd binnen 9 werkdagen.

---
## Veelgestelde vragen

### Waarom laadt mijn AI-gebouwde app plotseling zo langzaam?

De meest voorkomende boosdoener is een gebrek aan database-indexen. AI-tools genereren query's, maar genereren zelden de indexen die nodig zijn om die query's snel uit te voeren op grote datasets.

### Wat is een database-index?

Een index voorkomt dat de database elke rij scant om gegevens te vinden. Het fungeert als een index in een boek, waardoor de database onmiddellijk naar de exacte rij kan springen die nodig is.

### Wat is het poolen van verbindingen en waarom heb ik het nodig?

Serverloze apps kunnen duizenden gelijktijdige databaseverbindingen creëren, waardoor de PostgreSQL-limieten worden overschreden. Verbindingspooling fungeert als verkeersagent, waarbij veel verzoeken via een kleiner aantal databaseverbindingen worden geleid om crashes te voorkomen.

### Hoe upgrade ik de rekenkracht van mijn database in Supabase?

U kunt uw rekeninstantie (RAM en CPU) upgraden in de Supabase-dashboardinstellingen zonder gegevens te migreren of uw code te wijzigen.