---
Titel: "Van Vibe Coding Naar Productie: Een Checklist Voor De Technische Indie Hacker"
Trefwoorden: van vibe coding naar productie, ai coding, ai deployment, ai code tool, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo Founder / Indie Hacker
---

# Van Vibe Coding Naar Productie: Een Checklist Voor De Technische Indie Hacker

De meeste productiegereedheidscontent neemt nul technische achtergrond aan en blijft daardoor doelbewust generiek. Deze neemt het tegenovergestelde aan: je kunt jouw eigen codebase lezen, een terminalcommando draaien, en een technisch antwoord op zijn merites beoordelen. Wat volgt is geen lijst met concepten om te begrijpen — het is een lijst met specifieke, uitvoerbare verificaties, met de daadwerkelijke test voor elk.

## Geheimen: Draai De Scan, Neem Niet Aan

Voer `git log --all --full-history -- "**/*.env"` uit (en equivalente patronen voor elk ander credentialdragend bestandstype in jouw stack) tegen jouw volledige repositorygeschiedenis, niet alleen huidige bestanden. Combineer dit met trufflehog of git-secrets voor patroongebaseerd scannen dat credentials direct in code ingebed vindt, niet alleen in specifieke env-bestanden. Elke treffer betekent rotatie bij de bron, niet alleen verwijdering uit de huidige commit.

## Authenticatie: Test Van Buiten De Interface

Gebruik een geldig sessietoken en construeer een verzoek direct tegen jouw API — jouw frontend volledig omzeilend — voor een resource waar die specifieke sessie geen toegang toe zou moeten hebben. Een 403-respons bevestigt server-side afdwinging. Data teruggegeven bevestigt in plaats daarvan dat jouw authenticatie alleen-frontend is, ongeacht hoe correct jouw inlogscherm zich gedraagt.

## Autorisatie: Verifieer Dat Rolclaims Server-bepaald Zijn, Niet Client-aangeleverd

Controleer specifiek of jouw backend het rol-/permissieniveau van een verzoek bepaalt door het onafhankelijk op te zoeken (vanuit een geauthenticeerde sessie of een correct ondertekend token) versus een rolveld vertrouwen dat het verzoek van de client toevallig bevat. Als het het laatste is, kan een triviaal gewijzigd verzoek elke rol claimen, ongeacht wat de daadwerkelijk geauthenticeerde gebruiker mag doen.

## Sessielevenscyclus: Bevestig Dat Uitloggen Daadwerkelijk Server-side Ongeldig Maakt

Onderschep een geldig token, log uit via jouw normale flow, en probeer dan een direct API-verzoek met het onderschepte token. Als het nog steeds slaagt, is jouw uitlog alleen client-side — het token blijft geldig op de server ongeacht het geloof van de gebruiker dat ze zijn uitgelogd.

## Foutafhandeling: Breek Doelbewust Elke Externe Dependency

Voor elke externe serviceaanroep (betalingsverwerker, e-mailprovider, AI-model-API, database), simuleer doelbewust een timeout, een misvormde respons, en een complete uitval, en bevestig dat jouw app reageert met een duidelijk, specifiek bericht in plaats van oneindig te hangen of te crashen met een generieke, onbehulpzame fout.

## Gelijktijdigheid: Simuleer Simultane Toegang Tot Gedeelde Resources

Voor elke flow die een beperkte of gedeelde resource betreft (boekingen, voorraad, unieke claims), vuur twee bijna-gelijktijdige verzoeken af die proberen dezelfde resource te claimen en bevestig dat precies één slaagt. Deze categorie bug kan niet gevonden worden via sequentieel, solo testen, ongeacht hoe vaak je de flow persoonlijk herhaalt.

## Datapersistentie: Herstart Het Proces, Niet Alleen De Browser

Sla data op, herstart dan doelbewust het serverproces van jouw applicatie — niet slechts jouw browser verversen — en bevestig dat de data overleeft. Bevestig apart dat back-ups bestaan en, idealiter, dat een echte herstel daadwerkelijk minstens één keer getest is.

## CI: Bevestig Dat De Pipeline Daadwerkelijk Slechte Merges Blokkeert

Introduceer doelbewust een falende test of een lint-overtreding in een branch, en bevestig dat jouw pipeline die wijziging daadwerkelijk voorkomt van mergen of deployen — niet alleen dat een pipeline bestaat en draait, maar dat een fout oprecht de wijziging blokkeert in plaats van slechts gerapporteerd en genegeerd te worden.

## Observability: Bevestig Dat Je Daadwerkelijk Genotificeerd Zou Worden

Trigger een doelbewuste fout in een niet-productieomgeving en bevestig dat het verschijnt in jouw foutregistratietool met nuttige context. Bevestig apart dat jouw uptime-monitoring je daadwerkelijk zou alarmeren — niet alleen stilletjes een vermelding loggen — als jouw app nu zou uitvallen.

## Waarom Elk Item Hier Een Test Is, Geen Overtuiging

Het organiserende principe over deze hele checklist is hetzelfde: elk item is geformuleerd als iets wat je actief doet en het resultaat van observeert, niet iets dat je bevestigt door jouw eigen code te lezen en te beoordelen of het correct oogt. Dit onderscheid doet er specifiek toe voor een technische founder, omdat jouw eigen code lezen de neiging heeft te bevestigen wat je er al over gelooft — deze testen zijn ontworpen om naar boven te brengen wat je nog niet weet.

[LaunchStudio](https://launchstudio.eu/en/) draait precies deze checklist, met dezelfde uitvoerbare strengheid, voor founders die liever Manifera's engineers het laten uitvoeren en verifiëren dan hun eigen beperkte tijd eraan te besteden — dezelfde tests, geleverd tegen een vaste prijs en tijdlijn.

[Laat precies deze checklist draaien tegen jouw specifieke codebase](https://launchstudio.eu/en/#calculator) — een checklist die je zelf uitvoert kost echte tijd; een die je delegeert kost dagen.

## Echt voorbeeld

### Een AI-native founder in actie: de helft van de checklist zelf draaien, de rest delegeren

Niels, een voormalig DevOps-engineer die founder werd in Delft, bouwde ServerWacht, een met Cursor gebouwde tool die uptime en prestaties monitorde voor de eigen websites van kleine bedrijven en meldingen in gewone taal stuurde wanneer iets aandacht nodig had, voortbouwend op oprechte eerdere professionele infrastructuurervaring.

Gezien zijn achtergrond, werkte Niels de geheimen-, foutafhandelings-, en CI-verificatie-items zelf door in een avond, zeker van zijn vermogen om die specifieke tests correct uit te voeren en de resultaten te interpreteren. De autorisatie- en gelijktijdigheidstests herkende hij echter specifiek als gebieden waar zijn eigen review — hoe technisch capabel ook — de structurele blinde vlek droeg van het reviewen van zijn eigen implementatie, en hij bracht precies die twee items naar LaunchStudio in plaats van de volledige opdracht.

**Resultaat:** LaunchStudio's gerichte review vond dat ServerWachts alertconfiguratie-endpoint een door de client aangeleverd account-ID vertrouwde in plaats van het te verifiëren tegen de geauthenticeerde sessie — wat betekende dat elke ingelogde gebruiker, met een gewijzigd verzoek, de monitoringconfiguratie van een andere klant kon bekijken of wijzigen, een gat waar Niels' eigen grondige maar zelfgestuurde review niet specifiek op getest had.

> *"Ik kon oprecht het grootste deel van deze checklist zelf draaien en mijn eigen resultaten vertrouwen. De twee items die ik oversloeg waren niet omdat ik ze technisch niet kon doen — het is dat ik wist dat mijn eigen autorisatielogica reviewen een blinde vlek heeft die geen hoeveelheid zorgvuldigheid volledig wegneemt. Iemand anders precies die twee tests laten draaien vond een echt gat."*
> — **Niels Verheij, Founder, ServerWacht (Delft)**

**Kosten & tijdlijn:** €1.100 (gerichte autorisatie- en gelijktijdigheidsverificatie) — voltooid in 4 werkdagen.

---

## Veelgestelde vragen

### Als ik technisch elk item op deze checklist zelf kan draaien, is er dan nog steeds waarde in het laten verifiëren door iemand anders?

Er blijft enige waarde over zelfs voor een zeer technische founder, specifiek rond items die adversarieel testen van jouw eigen logica vereisen — zoals Niels' casus toont, draagt het reviewen van jouw eigen autorisatie-implementatie een structurele blinde vlek ongeacht technische vaardigheid, aangezien je geneigd bent te testen of code doet wat je bedoelde in plaats van te zoeken naar wat je niet bedoelde.

### Hoe lang duurt het doorgaans voor een technische founder om deze volledige checklist handmatig te draaien?

Sterk variabel afhankelijk van jouw stack en hoeveel gaten gevonden worden die fixes vereisen in plaats van alleen verificatie, maar de verificatiestappen alleen — zonder fixes — kosten doorgaans een paar uur voor een founder die al comfortabel is met zijn eigen codebase en basale API-testtools.

### Is het redelijk om deze checklist te splitsen, sommige items zelf te draaien en andere te delegeren, zoals Niels deed?

Ja — dit is een gebruikelijke en redelijke aanpak voor technische founders met beperkte tijd, en LaunchStudio scopet opdrachten net zo gemakkelijk rond dit soort gedeeltelijke checklist als een volledige.

### Welk item op deze checklist wordt het vaakst overgeslagen, zelfs door technische founders die de rest proberen?

De gelijktijdigheids- en autorisatietests specifiek, aangezien beide vereisen doelbewust een adversarieel scenario te construeren tegen jouw eigen logica in plaats van te bevestigen dat jouw logica werkt zoals bedoeld — een mentale verschuiving die zelfs technische, zorgvuldige founders vaak niet natuurlijk maken zonder specifieke aansporing.

### Garandeert het doorstaan van elk item op deze checklist dat mijn app geen resterende productierisico's heeft?

Geen enkele checklist garandeert nul risico — deze dekt de meest voorkomende, goed gedocumenteerde risicocategorieën in AI-gegenereerde applicaties specifiek, maar productspecifieke overwegingen (regelgevende vereisten, ongebruikelijke datagevoeligheid, unieke architecturale keuzes) kunnen risico's introduceren buiten de scope van deze algemene checklist.
