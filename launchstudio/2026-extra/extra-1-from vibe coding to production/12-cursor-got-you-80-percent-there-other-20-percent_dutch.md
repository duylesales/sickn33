---
Titel: "Cursor Bracht Je 80% Ver. Wat Zijn De Andere 20%?"
Trefwoorden: van vibe coding naar productie, ai code tool, ai coding, ai secure, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo Founder / Indie Hacker
---

# Cursor Bracht Je 80% Ver. Wat Zijn De Andere 20%?

Cursor bekleedt een oprecht andere positie dan volledig autonome AI-appbouwers: het is een AI-verrijkte IDE, wat betekent dat een technische founder actief gegenereerde code regel voor regel beoordeelt, bewerkt, en aanstuurt in plaats van een black-box-output volledig te accepteren. Dit produceert een echt, betekenisvol kwaliteitsverschil — en ook een specifieke, voorspelbare valkuil, omdat "ik heb deze code beoordeeld" en "deze code is productieverhard" niet dezelfde bewering zijn, zelfs voor een founder met oprechte codeervaardigheid.

## Waarom Cursor-gebruikers Specifiek Het Resterende Gat Onderschatten

Een founder die Lovable of Bolt gebruikt weet, bijna per definitie, dat ze een ondoorzichtig generatieproces vertrouwen en de output onafhankelijk moeten verifiëren. Een founder die Cursor gebruikt, actief code schrijvend en beoordelend met AI-assistentie, ontwikkelt vaak een andere en riskantere relatie met de codebase: oprechte vertrouwdheid met de logica, gekoppeld aan dezelfde blinde vlekken die elke enkele ontwikkelaar heeft bij het beoordelen van zijn eigen werk — je hebt de neiging te verifiëren dat code doet wat je bedoelde, niet systematisch te onderzoeken wat er gebeurt wanneer het gevraagd wordt iets te doen wat je helemaal niet bedoelde.

## Waar De Resterende 20% Zich Daadwerkelijk Concentreert

**Adversariële invoerafhandeling.** Code beoordeeld op "werkt dit correct" krijgt zelden dezelfde grondigheid voor "wat gebeurt er met kwaadaardige of misvormde input specifiek geconstrueerd om het te breken" — een aparte mentale oefening die zelfs competente ontwikkelaars overslaan zonder bewuste discipline om het op te nemen, aangezien het vereist actief te denken als een aanvaller in plaats van een bouwer.

**Toegangscontrole onafhankelijk geverifieerd van de code die het implementeert.** Een ontwikkelaar die de autorisatielogica zelf schreef, heeft de neiging deze te testen door de applicatie te gebruiken zoals bedoeld, wat de logica van nature correct beoefent — verifiëren dat het daadwerkelijk ongeautoriseerde toegang weigert vereist bewust proberen je eigen regels te schenden, een stap die het beoordelen van je eigen code niet van nature bevat.

**Dependency- en toeleveringsketenpositie.** Cursors autocomplete- en suggestiefuncties bevelen vaak packages aan op basis van wat gebruikelijk is in de trainingsdata, niet noodzakelijk wat momenteel onderhouden, actief ondersteund, of passend gelicentieerd is voor jouw specifieke commerciële gebruik — een controle die vereist buiten de code zelf te kijken, naar het ecosysteem rond elke dependency.

**Infrastructuur- en deploymentconfiguratie.** Zelfs sterke applicatiecode gaat niet over hoe het gedeployed, gemonitord, of hersteld wordt na een storing — een categorie zorg volledig apart van codekwaliteit, en een die Cursors in-editor-workflow niet natuurlijk naar boven brengt aangezien het op codeniveau opereert, niet infrastructuurniveau.

## Waarom "Ik Kan De Code Lezen" Dit Gat Niet Dicht

Het instinct, voor een founder technisch genoeg om Cursor effectief te gebruiken, is aan te nemen dat hun eigen review externe validatie vervangt. Het vervangt een deel ervan — vermindert oprecht bepaalde klassen bugs ten opzichte van een volledig ondoorzichtige tool — maar vervangt geen adversarieel testen, dependency-auditing, of infrastructuurverharding, waarvan geen enkele van nature beoefend wordt door correct code te schrijven en te lezen. Competente code en productieverharde code zijn overlappende maar aparte categorieën, en de overlap is groter voor Cursor-gebruikers dan voor gebruikers van andere tools, zonder compleet te zijn.

## Een Praktische Manier Om Jouw Specifieke 20% Te Vinden

De meest efficiënte manier om je resterende gaten te lokaliseren is niet je eigen code opnieuw lezen, aangezien een tweede lezing door dezelfde persoon de neiging heeft dezelfde dingen te vinden als de eerste lezing. Het is het toepassen van de specifieke adversariële tests beschreven doorheen deze serie — rechtstreeks ongeautoriseerde API-toegang proberen, bewust storingen van externe diensten triggeren, git-geschiedenis controleren op geheimen — omdat dit structureel andere activiteiten zijn dan codebeoordeling, die de codebase beoefenen op manieren die normale ontwikkeling en normale review simpelweg niet doen.

[LaunchStudio](https://launchstudio.eu/en/) beoordeelt Cursor-gebouwde codebases met precies dit onderscheid in gedachten — de kwaliteit van wat je hebt gebouwd respecterend terwijl specifiek de adversariële en infrastructuurdimensies onderzocht worden die je eigen review van nature niet dekt, gesteund door Manifera's engineeringdiscipline over 160+ opgeleverde projecten.

[Vind jouw specifieke resterende 20%](https://launchstudio.eu/en/#calculator) — een tweede paar ogen met een ander mandaat dan het jouwe vangt op wat je eigen review structureel niet kan.

## Echt voorbeeld

### Een AI-native founder in actie: de blinde vlek van een technische founder zelf

Koen, een voormalig backend-ontwikkelaar die founder werd in Nieuwegein, bouwde FactuurCheck, een Cursor-gebouwde tool die automatisch facturen van kleine bedrijven valideerde tegen Nederlandse belastingnalevingsregels vóór indiening, voortbouwend op zijn eigen jarenlange eerdere professionele codeerervaring. Koen had bijna elke regel zelf geschreven en beoordeeld, zelfverzekerd over de applicatielogica gezien zijn achtergrond.

Toen Koen FactuurCheck naar LaunchStudio bracht vóór een geplande lancering naar boekhoudkantoorklanten, richtte de review zich specifiek op dependency-positie — een gebied dat Koen, zoals de meeste ontwikkelaars gefocust op applicatielogica, niet apart had geauditeerd. Het bracht naar boven dat een van Cursors autocomplete-voorgestelde packages, gebruikt voor PDF-parsing, al meer dan twee jaar geen beveiligingsupdate had ontvangen en een ongepatchte, publiekelijk bekendgemaakte kwetsbaarheid had die precies het soort bestandsparsing beïnvloedde dat FactuurCheck uitvoerde bij elke geüploade factuur.

**Resultaat:** LaunchStudio verving de niet-onderhouden dependency door een actief ondersteund alternatief vóór FactuurChecks lancering, en dichtte een gat dat Koens eigen grondige codebeoordeling — oprecht zorgvuldig, door een oprecht competente ontwikkelaar — geen natuurlijke reden had om naar boven te brengen, aangezien de applicatielogica die de package gebruikte zelf volledig correct was.

> *"Ik heb elke regel van die codebase zelf gelezen. De code was prima — het probleem was een package waar het van afhing, twee jaar verouderd met een bekende kwetsbaarheid. Dat is niet iets wat je opvangt door je eigen logica zorgvuldiger te lezen."*
> — **Koen Terpstra, Founder, FactuurCheck (Nieuwegein)**

**Kosten & tijdlijn:** €1.350 (gerichte review — dependency-audit en adversarieel testen) — voltooid in 5 werkdagen.

---

## Veelgestelde vragen

### Als ik technisch genoeg ben om Cursor effectief te gebruiken, waarom zou ik dan überhaupt een externe review nodig hebben?

Omdat het hier beschreven gat niet over codeercompetentie gaat — het gaat over de structurele blinde vlek van het beoordelen van je eigen werk, en over categorieën (dependency-positie, infrastructuurconfiguratie) die volledig buiten de applicatiecode zelf bestaan, ongeacht hoe vaardig de ontwikkelaar die die code beoordeelt toevallig is.

### Is de dependency-kwetsbaarheid die Koen vond een veelvoorkomend probleem, of een ongewoon randgeval?

Het is een veelvoorkomend en goed gedocumenteerd probleem in de softwareindustrie in het algemeen, niet uniek voor AI-ondersteunde ontwikkeling — niet-onderhouden dependencies met bekende kwetsbaarheden zijn een standaardcategorie beveiligingszorg die vereist het ecosysteem rond je code te controleren, niet alleen de code die je persoonlijk schreef.

### Hoe is een review van Cursor-gebouwde code anders dan het beoordelen van code van een volledig autonome tool zoals Lovable of Bolt?

De startkwaliteit van de applicatielogica zelf is doorgaans hoger, gegeven actieve ontwikkelaarsbetrokkenheid, wat betekent dat de review zich meer kan focussen op de adversariële en infrastructuurdimensies en minder op basale logicacorrectheid — hoewel de specifieke gaten nog steeds bewust, apart testen vereisen in plaats van meer code lezen.

### Kan ik mijn eigen dependencies zelf auditen op bekende kwetsbaarheden zonder externe hulp?

Ja, tot een betekenisvolle mate — geautomatiseerde dependency-scantools bestaan en vangen veel bekende kwetsbaarheden automatisch op, hoewel een volledige review doorgaans ook onderhoudsactiviteit en licentiegeschiktheid overweegt, wat bredere beoordeling vereist dan een geautomatiseerde scan alleen biedt.

### Vermindert eerdere professionele codeerervaring, zoals die van Koen, hoeveel productiegereedheidswerk doorgaans nodig is?

Het vermindert doorgaans specifiek het applicatielogica-kwaliteitsgat, aangezien ervaren ontwikkelaars vanaf het begin zorgvuldigere code schrijven, maar het elimineert niet de hier beschreven adversarieel testen-, dependency-, en infrastructuurgaten, die grotendeels onafhankelijk zijn van het vaardigheidsniveau van de oorspronkelijke ontwikkelaar.
