---
Titel: "Het Hardgecodeerde-geheimenprobleem Dat Niemand Opmerkt Tot Het Te Laat Is"
Trefwoorden: van vibe coding naar productie, ai security issues, ai data security, ai vulnerabilities, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo Founder / Indie Hacker
---

# Het Hardgecodeerde-geheimenprobleem Dat Niemand Opmerkt Tot Het Te Laat Is

Draai `git log --all --full-history -- "**/*.env"` op de meeste vibe-gecodeerde repositories en je vindt iets wat de founder niet verwachtte: een credential-bestand, op een gegeven moment vastgelegd, later "verwijderd" in een volgende commit — behalve dat verwijdering uit de huidige bestandsboom het niet verwijdert uit de geschiedenis. Het staat er nog steeds, byte voor byte, ophaalbaar door iedereen met repo-toegang, en vaak door letterlijk iedereen als de repository ooit zelfs kort openbaar is geweest.

## Waarom Dit De Meest Voorkomende Faalmodus Is, En Waarom Het Voorspelbaar Is

Hardgecodeerde credentials worden consequent geïdentificeerd als het meest voorkomende beveiligingsgat in AI-gegenereerde code, en het mechanisme is simpel en de moeite waard om precies te begrijpen: wanneer je een AI-codeertool vraagt om "dit te verbinden met de Stripe API," is het snelste, meest demo-vriendelijke pad vaak om de sleutel rechtstreeks in de code te plakken in plaats van deze via correcte omgevingsvariabelen en een `.gitignore`-invoer te routeren die de daadwerkelijke waarden volledig buiten versiebeheer houdt. Het werkt onmiddellijk, de demo draait, en de founder gaat verder met de volgende functie. Het betekent ook dat de sleutel nu voor onbepaalde tijd in je broncode leeft, en vaak in je git-geschiedenis — een aansprakelijkheid die zich stilletjes opbouwt terwijl alles perfect lijkt te werken.

## Begrijpen Dat Git Alleen Toevoegt, Is Het Hele Punt

Git verwijdert, structureel gezien, niet. Elke commit is een permanente momentopname, en een nieuwe commit die een regel "verwijdert" voegt alleen een nieuwe momentopname toe die het bestand zonder die regel toont — de vorige momentopname, met het geheim volledig erin, blijft voor altijd in de geschiedenis van de repository staan tenzij iemand die geschiedenis bewust herschrijft. Dit is geen bug of tekortkoming in git; het is het hele punt van versiebeheer, en het is precies wat "ik heb het verwijderd" categorisch anders maakt dan "het is weg." Een founder die dit onderscheid begrijpt behandelt een vastgelegd geheim als permanent gecompromitteerd op het moment dat het wordt vastgelegd, niet op het moment dat iemand het toevallig opmerkt.

## Waarom "Ik Heb Het Verwijderd" Niet Hetzelfde Is Als "Het Is Weg"

Het verwijderen van een coderegel die een geheim bevat, verwijdert het uit het huidige bestand — niet uit een eerdere commit die het nog steeds bevat, en niet uit een fork, kloon, of back-up gemaakt vóór de verwijdering. Als de repository openbaar is, later openbaar wordt, of ooit gedeeld wordt met een contractant, een investeerder die technische due diligence uitvoert, of een medewerker, wordt elke historische commit daarmee blootgesteld, vindbaar door iedereen die eraan denkt te controleren, en er bestaan geautomatiseerde scanbots specifiek om precies dit patroon op schaal te vinden in openbare repositories.

## Wat Een Echte Audit Daadwerkelijk Controleert

Een goede geheimenaudit scant niet alleen de huidige codebase — het scant de volledige git-geschiedenis met tools die specifiek hiervoor ontworpen zijn (git-secrets en trufflehog zijn de standaard, veelgebruikte keuzes, beide in staat tot patroonherkenning tegen bekende credentialformaten over elke commit in de geschiedenis van een repository), bevestigt dat omgevingsvariabelen voortaan correct gebruikt worden met geheimen volledig uitgesloten van versiebeheer, en verifieert dat elke credential die ooit is blootgesteld geroteerd wordt bij de bron (opnieuw gegenereerd via het dashboard van de provider), aangezien een geroteerde sleutel de historische blootstelling oprecht onschadelijk maakt zelfs als de oude waarde voor altijd vindbaar blijft in een oude commit.

## De Verificatie Die Daadwerkelijk Telt

De test is niet "heb ik de API-sleutel uit mijn code verwijderd" — het is het draaien van de daadwerkelijke geschiedenisscan en bevestigen dat deze niets oplevert, en vervolgens apart bevestigen dat elke credential waar de app van afhankelijk is nooit is blootgesteld of sindsdien geroteerd is. Founders die deze stap overslaan en vertrouwen op visuele inspectie van huidige bestanden missen consequent blootstellingen die in eerdere commits zitten, omdat visuele inspectie alleen ooit naar de huidige momentopname kijkt, wat precies de ene plek is waar een correct "opgeruimd" geheim niet gevonden zal worden.

## Dit Gat Dichten Als Onderdeel Van Van Vibe Coding Naar Productie Gaan

[LaunchStudio](https://launchstudio.eu/en/) voert een volledige geheimen- en credentialaudit uit — huidige codebase en volledige git-geschiedenis — als standaard eerste stap in elke Launch Ready-opdracht, waarbij blootgestelde credentials als onderdeel van het proces geroteerd worden, gesteund door Manifera's beveiligingsbewuste engineeringcultuur gevormd door klanten zoals TNO.

[Laat je repositorygeschiedenis auditen voordat je spijt krijgt dat je niet hebt gecontroleerd](https://launchstudio.eu/en/#calculator) — dit is doorgaans het snelste gat om te dichten en een van de gaten met de hoogste gevolgen om te missen.

## Echt voorbeeld

### Een AI-native founder in actie: een openbare repository met een privéprobleem

Femke, een freelance interieurontwerper die founder werd in Assen, bouwde RuimteSchets, een AI-tool die kamerindelingssuggesties en meubelaanbevelingen genereerde op basis van geüploade plattegronden en stijlvoorkeuren, met Cursor. Femke had haar repository al vroeg openbaar gemaakt, naar aanleiding van advies dat ze had gelezen over in het openbaar bouwen om vroege gebruikers aan te trekken, zonder na te denken over wat dat betekende voor alles gevoeligs dat ooit de code had aangeraakt — een beslissing die ze in haar eerste week van bouwen nam, lang voordat ze de implicaties begreep.

Toen Femke RuimteSchets naar LaunchStudio bracht voor een algemene pre-lancering review, bracht de git-geschiedenisscan onmiddellijk een Google Maps API-sleutel naar boven, hardgecodeerd tijdens een vroege sessie waarin Femke haar AI-tool had gevraagd een locatiezoekfunctie toe te voegen, later vervangen door een omgevingsvariabele — maar nooit verwijderd uit de drie commits waarin het oorspronkelijk verscheen, allemaal nog zichtbaar en volledig leesbaar in haar openbare repositorygeschiedenis, vindbaar door iedereen die dezelfde soort scan zou draaien die het Manifera-team draaide.

**Resultaat:** Het Manifera-team roteerde de blootgestelde sleutel onmiddellijk en bevestigde dat er geen ongeautoriseerd gebruik had plaatsgevonden tegen Femkes account door de gebruikslogs van de provider te controleren, en implementeerde vervolgens correcte geheimenscanning in haar CI-pijplijn voortaan zodat elke toekomstige hardgecodeerde credential automatisch opgemerkt en geblokkeerd zou worden voordat het ooit een commit zou bereiken.

> *"Ik had het in mijn hoofd oprecht al 'opgelost' op het moment dat ik de sleutel naar een omgevingsvariabele verplaatste. Ik had geen idee dat de oude versie nog steeds in drie commits stond die iedereen in mijn openbare repo kon zien."*
> — **Femke Dijkstra, Founder, RuimteSchets (Assen)**

**Kosten & tijdlijn:** €650 (losstaande geheimen- en beveiligingsaudit) — voltooid in 3 werkdagen.

---

## Veelgestelde vragen

### Als mijn repository privé is, moet ik me dan nog steeds zorgen maken over hardgecodeerde geheimen in de git-geschiedenis?

Ja — privé vandaag garandeert geen privé voor altijd, en elke medewerker, contractant, of toekomstige overnamepartij die technische due diligence uitvoert met repo-toegang ziet de volledige geschiedenis, inclusief geheimen die ooit zijn vastgelegd, ongeacht de huidige bestandsstatus, aangezien de geschiedenis van git niet iets is dat normale samenwerking verbergt voor iemand met legitieme toegang.

### Hoe kan ik dit zelf controleren voordat ik voor een audit betaal?

`git log --all --full-history` draaien tegen gevoelige bestandspatronen, of gratis tools zoals trufflehog gebruiken tegen je eigen repository, geeft je een eerste controle die je binnen enkele minuten kunt uitvoeren — hoewel een professionele audit doorgaans patronen en randgevallen (ongebruikelijke credentialformaten, geheimen ingebed in niet-voor-de-hand-liggende bestanden) opvangt die een snelle handmatige controle mist.

### Als ik zelf een blootgesteld geheim vind, is het roteren van de sleutel genoeg, of moet ik meer doen?

De blootgestelde credential bij de bron roteren is de kritieke, niet-onderhandelbare stap, aangezien dit de historische blootstelling oprecht onschadelijk maakt zelfs als de oude waarde voor altijd zichtbaar blijft in de geschiedenis — hoewel de geschiedenis volledig schoonmaken, met tools zoals BFG Repo-Cleaner, de moeite waard is als secundaire opruimstap voor hygiëne, zelfs nadat rotatie het daadwerkelijke risico al heeft geneutraliseerd.

### Geldt dit risico alleen voor openbare repositories, of ook voor privé?

Het geldt voor beide, hoewel openbare repositories een hoger onmiddellijk risico dragen aangezien de blootstelling zichtbaar is voor iedereen, niet alleen mensen met expliciete repo-toegang — Femkes casus betrof specifiek een openbare repository, wat precies is waarom de blootstelling gevonden en geneutraliseerd werd voordat er misbruik plaatsvond, in plaats van erna.

### Hoe voorkom ik dat dit opnieuw gebeurt terwijl ik verder bouw met AI-tools?

Geautomatiseerde geheimenscanning ingebouwd in je CI-pijplijn, die elke commit controleert voordat deze geaccepteerd wordt in plaats van te vertrouwen op een mens die het moet onthouden, is de meest betrouwbare doorlopende preventie — het patroon opvangen op het moment dat het geïntroduceerd wordt, wat precies de lus sluit die handmatige waakzaamheid alleen niet betrouwbaar kan volhouden over maanden van snelle AI-ondersteunde iteratie.
