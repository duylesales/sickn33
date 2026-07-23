---
Titel: "De Productiegereedheidsscore: Hoe Je Jouw Eigen AI-gebouwde App Beoordeelt"
Trefwoorden: van vibe coding naar productie, ai deployment, ai secure, ai coding, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo Founder / Indie Hacker
---

# De Productiegereedheidsscore: Hoe Je Jouw Eigen AI-gebouwde App Beoordeelt

"Voel je je klaar om te lanceren?" is een oprecht onbetrouwbare vraag om jezelf te stellen, aangezien vertrouwen en daadwerkelijke gereedheid slechts los gecorreleerd zijn — een founder kan zich zelfverzekerd voelen omdat ze uitgebreid getest hebben binnen hun eigen gebruikspatronen, precies de blinde vlek doorheen deze serie behandeld. Een gestructureerde score, gebaseerd op specifieke, verifieerbare controles in plaats van een gevoel, biedt een aanzienlijk eerlijker antwoord.

## Hoe Elke Categorie Te Scoren

Voor elk van de zeven categorieën hieronder, scoor jouw app 0, 1, of 2: **0** als het item helemaal niet gecontroleerd of geverifieerd is; **1** als het gedeeltelijk aangepakt of informeel gecontroleerd is; **2** als het specifiek, concreet geverifieerd is met de exacte tests doorheen deze serie beschreven — niet aangenomen, niet "waarschijnlijk prima," maar daadwerkelijk getest en bevestigd.

## Categorie 1: Geheimen (0-2)

Scoor 2 alleen als je een volledige git-geschiedenisscan gedraaid hebt (niet alleen huidige bestanden gecontroleerd) en bevestigd hebt dat er geen blootgestelde credentials zijn, met eventuele gevonden geheimen geroteerd. Scoor 1 als je huidige bestanden gecontroleerd hebt maar niet volledige geschiedenis. Scoor 0 als je helemaal niet gecontroleerd hebt.

## Categorie 2: Authenticatie En Autorisatie (0-2)

Scoor 2 alleen als je direct tegen jouw API getest hebt — met een geldig maar onvoldoende-bevoegd account een ongeautoriseerde actie geprobeerd — en bevestigd hebt dat het correct geweigerd wordt. Scoor 1 als jouw inlogscherm correct werkt maar je API-niveau-afdwinging niet direct getest hebt. Scoor 0 als je het frontend-versus-backend-onderscheid helemaal niet overwogen hebt.

## Categorie 3: Foutafhandeling (0-2)

Scoor 2 alleen als je doelbewust storingen getriggerd hebt in jouw externe dependencies (een dienst losgekoppeld, een timeout gesimuleerd) en soepele, specifieke afhandeling bevestigd hebt. Scoor 1 als generieke foutafhandeling bestaat maar niet getest is tegen doelbewuste storingen. Scoor 0 als foutafhandeling effectief afwezig of volledig ongetest is.

## Categorie 4: Testen (0-2)

Scoor 2 alleen als jouw kritieke flows geautomatiseerde smoke-testdekking hebben, inclusief minstens één doelbewust adversariële of gelijktijdige-toegang-test. Scoor 1 als je kritieke flows handmatig getest hebt maar geen automatisering hebt. Scoor 0 als testen informeel en onsystematisch geweest is.

## Categorie 5: Datapersistentie (0-2)

Scoor 2 alleen als je bevestigd hebt dat data een serverherstart overleeft (niet alleen een browserverversing) en geverifieerd hebt dat back-ups bestaan met minstens één daadwerkelijke herstel getest. Scoor 1 als je oprecht duurzame opslag gebruikt maar back-upherstel niet getest hebt. Scoor 0 als je persistentie niet geverifieerd hebt voorbij toevallige observatie.

## Categorie 6: Observability (0-2)

Scoor 2 alleen als foutregistratie en uptime-monitoring geconfigureerd zijn met alerts getest om daadwerkelijk correct te triggeren. Scoor 1 als monitoring bestaat maar alerting niet specifiek geverifieerd is. Scoor 0 als er helemaal geen monitoring bestaat.

## Categorie 7: CI-pipeline (0-2)

Scoor 2 alleen als je bevestigd hebt dat een falende test of lint-overtreding daadwerkelijk deployment blokkeert, niet alleen dat een pipeline draait. Scoor 1 als een pipeline bestaat maar niet getest is om te bevestigen dat het daadwerkelijk slechte wijzigingen blokkeert. Scoor 0 als er geen pipeline bestaat.

## Jouw Totaalscore Interpreteren (Op 14)

**11-14:** Oprecht sterke dekking over de kerncategorieën — resterend werk is waarschijnlijk verfijning in plaats van fundamentele gaten.

**6-10:** Betekenisvolle gaten bestaan in minstens een paar categorieën, wat gerichte aandacht rechtvaardigt vóór of kort na lancering, geprioriteerd via de getierde risicoaanpak elders in deze serie behandeld.

**0-5:** Significante gaten over meerdere fundamentele categorieën — het soort situatie waar een uitgebreide review, niet alleen zelfscoring, de gepaste volgende stap is gegeven hoeveel categorieën waarschijnlijk aandacht nodig hebben.

## Waarom Deze Scoringmethode Specifiek Zelfbedrog Vermijdt

De scoringcriteria zijn doelbewust binair en bewijsgebaseerd — je draaide de specifieke beschreven test ofwel of je deed het niet — wat ontworpen is om weerstand te bieden aan het zelfreview-optimisme doorheen deze serie behandeld. Een founder die verleid wordt genereus te scoren op een vage "heb ik hierover nagedacht"-basis wordt structureel verhinderd dat te doen door de vereiste dat elke 2 specifiek overeenkomt met een beschreven, uitgevoerde verificatie, geen algemene indruk.

[LaunchStudio](https://launchstudio.eu/en/) kan precies deze score voor jouw specifieke app verifiëren of produceren, en biedt de concrete tests achter elke categorie in plaats van van jou te vereisen ze zelf uit te voeren, gesteund door Manifera's engineeringdiscipline over 160+ opgeleverde projecten gescoord en verhard met datzelfde onderliggende framework.

[Laat jouw app professioneel scoren tegen precies dit framework](https://launchstudio.eu/en/#calculator) — een zelfscore is een nuttig startpunt; een geverifieerde is een betrouwbare beslissingsbasis.

## Echt voorbeeld

### Een AI-native founder in actie: een zelfscore die een oprechte blinde vlek onthulde

Ruben, een voormalig IT-supporttechnicus die founder werd in Hoofddorp, bouwde HelpdeskAI, een AI-tool die eerstelijns-IT-supportticket-triage en oplossingssuggesties automatiseerde voor kleine bedrijven, met Cursor, en voelde zich over het algemeen zelfverzekerd over zijn lanceringsgereedheid gebaseerd op maanden actieve ontwikkeling en testen.

Dit exacte scoringframework eerlijk toepassend op zijn eigen app, scoorde Ruben sterk op categorieën 3, 4, en 7 (foutafhandeling, testen, CI), wat zijn oprechte technische achtergrond en doelbewuste inspanning in die gebieden weerspiegelde, maar werd gedwongen categorie 2 (authenticatie) op een 1 in plaats van een 2 te scoren, aangezien hij bevestigd had dat zijn inlogscherm correct werkte maar nooit specifiek zijn API direct getest had met een ongeautoriseerd verzoek — precies het onderscheid dat deze serie herhaaldelijk benadrukt.

**Resultaat:** Specifiek aangespoord door de eerlijke scoringoefening in plaats van een vaag gevoel van onzekerheid, draaide Ruben de specifieke API-niveau-test zelf en ontdekte precies het gat dat het framework ontworpen was om naar boven te brengen: een supporttechnicus-account kon de ticketdata van een ander bedrijf benaderen door een verzoek direct te wijzigen, aangezien rolverificatie client-aangeleverd was in plaats van server-geverifieerd. Hij bracht deze specifieke bevinding naar LaunchStudio voor herstel.

> *"Ik zou je verteld hebben dat ik in principe klaar was voordat ik deze scoringoefening eerlijk deed. Mezelf dwingen te antwoorden 'heb ik deze specifieke test daadwerkelijk gedraaid' in plaats van 'voel ik me hier goed bij' is wat me deed beseffen dat ik nooit daadwerkelijk het ene ding gecontroleerd had dat kapot bleek te zijn."*
> — **Ruben Aarsen, Founder, HelpdeskAI (Hoofddorp)**

**Kosten & tijdlijn:** €1.300 (gerichte autorisatieherstel volgend op zelf-geïdentificeerd gat) — voltooid in 4 werkdagen.

---

## Veelgestelde vragen

### Is dit zelfscoringframework een vervanging voor een professionele audit, of een aanvulling erop?

Een nuttige aanvulling en startpunt, vooral voor technische founders, maar geen volledige vervanging — zoals Rubens casus toont, kan eerlijke zelfscoring precies naar boven brengen waar te focussen, hoewel de daadwerkelijke fix uitvoeren en bevestigen dat het oprecht opgelost is vaak nog steeds profiteert van het soort toegewijde review doorheen deze serie behandeld.

### Wat moet ik doen als ik niet technisch genoeg ben om sommige van deze specifieke tests zelf te draaien?

Het scoringframework zelf is ontworpen voor technische founders capabel om de beschreven tests uit te voeren; een niet-technische founder kan dezelfde categorielijst gebruiken om de diagnostische vragen elders in deze serie behandeld te stellen, en "heb je deze specifieke test gedraaid" vertalen naar een vraag om te stellen aan wie het technische werk ook doet.

### Is een score van 11-14 een garantie dat mijn app geen resterende productierisico's heeft?

Geen enkele score garandeert nul risico — dit framework dekt de kerncategorieën die consistent terugkeren over AI-gegenereerde codebases specifiek, maar productspecifieke overwegingen buiten dit algemene framework (zoals behandeld in de e-commerce- en onderwijsspecifieke begeleiding van deze serie) kunnen nog steeds aanvullende, categoriespecifieke aandacht rechtvaardigen.

### Hoe vaak moet ik deze scoringoefening opnieuw draaien naarmate mijn app blijft veranderen?

Periodiek, vooral na significante functietoevoegingen of vóór enige opmerkelijke groeimijlpaal, vergelijkbaar met de jaareinde-auditcadans behandeld in bredere productiegereedheidsbegeleiding — een score die zes maanden geleden accuraat was weerspiegelt niet noodzakelijk jouw huidige codebase na doorlopende wijzigingen.

### Kan dit scoringframework toegepast worden op een app die al live is, of is het alleen nuttig pre-lancering?

Even nuttig voor een live app — de categorieën en verificatiemethoden veranderen niet gebaseerd op lanceringsstatus, en een eerlijke score voor een al-live product geeft simpelweg aan waar herstel te prioriteren met enigszins hogere urgentie gegeven bestaande gebruikersblootstelling.
