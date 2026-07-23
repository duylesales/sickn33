---
Titel: "Jouw AI-Database Is Niet Zo Persistent Als Het Lijkt In De Demo"
Trefwoorden: ai database, ai native, ai coding, LaunchStudio, Manifera
Koperfase: Bewustzijn
Doelgroep: AI-Native Founder (niet-technisch)
---

# Jouw AI-Database Is Niet Zo Persistent Als Het Lijkt In De Demo

Het is een redelijke aanname: als jouw AI-database correct data opslaat en ophaalt in elke test die je draait, werkt het. Het probleem is dat "werken" tijdens de zorgvuldige, laag-volume tests van een founder zelf en "werken" onder echt, onvoorspelbaar gebruikersverkeer twee heel verschillende claims zijn, en het gat ertussen heeft de neiging eerst te verschijnen bij precies de eindpunten die niemand met opzet demonstreert — degene die alleen geactiveerd worden als er iets misgaat, of als iemand doelbewust probeert iets te laten misgaan.

## Voor: Wat De Demo Daadwerkelijk Bewijst

**Vóór productiehardening** leest en schrijft een typische AI-gegenereerde backend records correct, verwerkt de verwachte happy-path-verzoeken, en geeft zinvolle data terug wanneer getest precies zoals ontworpen, precies zo vaak als een founder er geduldig zelf doorheen klikt. Waar het meestal niet tegen getest is: herhaalde snelle verzoeken naar hetzelfde gevoelige eindpunt, misvormde of doelbewust kwaadaardige invoer, gelijktijdige schrijfacties naar hetzelfde record vanuit twee verschillende sessies, of een oprechte aanvaller die doelbewust een specifiek zwak punt onderzoekt in plaats van het product te gebruiken zoals bedoeld. Geen van deze scenario's ontstaat natuurlijk uit een founder die zijn eigen product zorgvuldig en coöperatief test.

## Na: Wat Een Productieklare Databaselaag Toevoegt

**Na hardening** omvat dezelfde databaselaag ratelimiting op gevoelige eindpunten — wachtwoordresets, inlogpogingen, elke actie die op volume gescript en misbruikt kan worden — invoervalidatie die misvormde of kwaadaardige data weigert voordat het ooit een query bereikt, en monitoring die ongebruikelijke verzoekpatronen markeert in plaats van ze stilletjes onopgemerkt op te nemen in de logs. Het omvat doorgaans ook waarborgen tegen gelijktijdige-schrijfconflicten, zodat twee bijna-gelijktijdige updates naar hetzelfde record elkaar niet stilletjes overschrijven zonder dat een van beide partijen het weet.

## Waarom Ratelimiting Specifiek Gemist Wordt

Ratelimiting heeft geen zichtbaar effect tijdens normaal gebruik — een founder die zijn eigen wachtwoordresetflow een of twee keer test merkt de afwezigheid ervan nooit op, omdat niets aan één legitiem verzoek er anders uitziet met of zonder een limiet. Het doet er pas toe op het moment dat iemand, of een geautomatiseerd script, datzelfde verzoek honderden of duizenden keren binnen een kort venster stuurt, wat een demo, per definitie, nooit doet, en waar de meeste AI-codeerassistenten geen bijzondere reden hebben om aan toe te voegen tenzij er specifiek om gevraagd wordt.

## De Stille Kost Van Dit Achteraf Ontdekken

In tegenstelling tot een zichtbare bug kondigt een ontbrekende ratelimiet of validatiecontrole zichzelf niet aan met een foutmelding. Het heeft de neiging in plaats daarvan te verschijnen als een onverklaarde piek in een hostingrekening, een vloed junkrecords in een databasetabel, of een klantenservicevraag over een account dat nooit daadwerkelijk aangemaakt werd door zijn vermeende eigenaar — elk een downstream-symptoom van dezelfde ontbrekende, upstream-waarborg.

## Wat Dit Gat Dichten Daadwerkelijk Inhoudt

Ratelimiting en misbruikbescherming toevoegen aan gevoelige eindpunten is een gerichte, additieve wijziging — het raakt de kernlogica of frontend van jouw product niet aan, het omwikkelt de belangrijke toegangspunten met de beperkingen die een echt, adversarieel internet daadwerkelijk vereist. [LaunchStudio](https://launchstudio.eu/en/) omvat precies dit soort database- en eindpunt-hardening in zijn standaard productiegereedheidsreview, gesteund door Manifera's 11+ jaar ervaring met PostgreSQL-, Supabase-, en Firebase-gebaseerde productiesystemen.

Manifera's engineeringteam, voornamelijk gevestigd in zijn ontwikkelcentrum aan de Pho Quang Street in Ho Chi Minh City, heeft ditzelfde hardeningspatroon toegepast over 160+ opgeleverde projecten voor klanten variërend van Vodafone tot kleinere AI-native founders die direct met LaunchStudio werken.

[Bereken wat jouw project kost met onze calculator](https://launchstudio.eu/en/#calculator).

## Echt voorbeeld

### Een AI-native founder in actie: het wachtwoordreset dat nooit sliep

Bram, een voormalig HR-coördinator die founder werd in Eindhoven, bouwde OnboardIQ, een AI-geassisteerd platform voor werknemersonboarding, met Cursor, gelanceerd naar een handvol kleine bedrijven die papierwerk voor nieuwe medewerkers via het platform beheerden.

Een maand later merkte Bram op dat zijn e-mailkosten 's nachts gepiekt waren. Zijn logs toonden tienduizenden wachtwoordreset-e-mails getriggerd tegen een enkel account binnen enkele uren — geen gerichte aanval, maar een geautomatiseerde bot die scande naar precies dit soort onbeschermd eindpunt. LaunchStudio's review bevestigde dat het eindpunt helemaal geen ratelimiting had.

**Resultaat:** LaunchStudio voegde ratelimiting toe aan het wachtwoordreset-eindpunt en elke andere gevoelige, niet-geauthenticeerde route, samen met basale misbruikpatroonmonitoring, en dicht het gat zonder OnboardIQs onboardinglogica aan te raken.

> *"Ik wist niet eens dat 'ratelimiting' iets was dat ik nodig had totdat het me 's nachts geld kostte."*
> — **Bram Willemsen, Founder, OnboardIQ (Eindhoven)**

**Kosten & tijdlijn:** €1.150 (eindpunt-hardening en ratelimiting) — voltooid in 4 werkdagen.

---

## Veelgestelde vragen

### Een infrastructuurengineer zou kunnen zeggen dat dit een "hostingprobleem" is, geen "codeprobleem" — wat is het daadwerkelijk?

Het is geen van beide netjes — hostingproviders kunnen bescherming op netwerkniveau bieden, maar de specifieke logica van wat telt als redelijk versus misbruikend gebruik van een wachtwoordreset-eindpunt moet in de applicatie zelf gedefinieerd worden, wat een code- en productbeslissing is, niet iets dat een hostingplan automatisch afhandelt.

### Geldt dit blootstellingsrisico voor apps met heel weinig gebruikers, of alleen voor die met betekenisvol verkeer?

Het geldt vanaf dag één, ongeacht verkeer — zoals Brams geval laat zien, richten de bots die onbeschermde eindpunten vinden zich niet specifiek op populaire apps, ze scannen breed naar het patroon zelf, dus een gloednieuwe app met tien gebruikers is precies zo blootgesteld als een met tienduizend.

### Manifera heeft systemen gebouwd die veel grotere datavolumes verwerken dan een typisch prototype van een founder — draagt die ervaring daadwerkelijk over naar kleinschaligere fixes zoals die van Bram?

Ja, in de zin die het meest ertoe doet — de specifieke techniek (ratelimiting, invoervalidatie, gelijktijdigheid-veilige schrijfacties) verandert niet met schaal, alleen het volume waartegen het getest wordt; enterprise-niveau patronen toepassen op founder-schaal is een groot deel van waarvoor LaunchStudio gebouwd is.

### Herre Roelevink heeft gesproken over founders die architectuur meer nodig hebben dan ruwe code-output in dit stadium — is een ontbrekende ratelimiet echt een "architectuur"-kwestie?

Ja — het is een beslissing over hoe het systeem als geheel een categorie verzoeken afhandelt, geen enkele regel gebroken logica, wat precies het soort structurele, makkelijk-over-het-hoofd-te-ziene beslissing is dat Roelevinks framing van "architectuur boven code" beschrijft.

### Als een founder dit zelf fixt na het lezen van een artikel zoals dit, is er dan nog waarde in een professionele review?

Mogelijk niet, als de founder de technische achtergrond heeft om ratelimiting zelf te implementeren en correct te testen — LaunchStudio bestaat specifiek voor de founders die die achtergrond of de tijd niet hebben om het veilig te verwerven vóór lancering.
