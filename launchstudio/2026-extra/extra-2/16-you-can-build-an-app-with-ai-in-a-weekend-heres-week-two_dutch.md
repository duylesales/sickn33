---
Titel: "Je Kunt Een App Met AI Bouwen In Een Weekend. Hier Is Week Twee"
Trefwoorden: build an app with ai, build app with ai, ai coding, LaunchStudio, Manifera
Koperfase: Bewustzijn
Doelgroep: AI-Native Founder (niet-technisch)
---

# Je Kunt Een App Met AI Bouwen In Een Weekend. Hier Is Week Twee

Week één is het leuke deel: je bouwt een app met AI, ziet het sneller samenkomen dan je dacht mogelijk, en tegen zondagavond heb je iets echts om aan mensen te laten zien. Week twee is stiller en minder zichtbaar, en dat is waar het meeste daadwerkelijke risico van een weekendbuild de neiging heeft te leven — beginnend met een simpele vraag die bijna niemand stelt tijdens de opwinding van week één: waar zijn jouw API-sleutels precies terechtgekomen?

## Checklistpunt Eén: Doorzoek Jouw Repository Op Blootgestelde Sleutels

Een weekend snelle iteratie betekent vaak werkende code kopiëren tussen bestanden, frequent committen zonder veel controle, en af en toe een sleutel rechtstreeks in een configbestand plakken om iets snel werkend te krijgen, met elke intentie het "later" ergens veiliger heen te verplaatsen. Controleren of dat "later" daadwerkelijk gebeurde — de geschiedenis van jouw eigen repository doorzoeken op alles dat op een API-sleutel of credential lijkt — is een controle van vijf minuten met buitenproportionele waarde.

## Checklistpunt Twee: Bevestig De Zichtbaarheidsinstelling Van Jouw Repository

Een verrassend aantal founder-gebouwde projecten zit standaard in een publieke GitHub-repository, hetzij omdat de founder er niet aan dacht de instelling te veranderen, hetzij omdat hij niet besefte dat de instelling bestond. Een publieke repository betekent dat alles wat erin gecommit is — inclusief een sleutel gemist tijdens de bovenstaande zoekopdracht — zichtbaar is voor letterlijk iedereen, geïndexeerd door geautomatiseerde scanners die specifiek publieke repositories doorzoeken op precies dit patroon.

## Checklistpunt Drie: Roteer Alles Dat Ooit Blootgesteld Was, Zelfs Kort

Als een sleutel ooit gecommit werd naar een publieke repository, zelfs als hij later verwijderd werd, is de veiligste aanname dat hij al gezien werd — git-geschiedenis bewaart oude commits, en geautomatiseerde scanners werken snel genoeg dat "het was maar een uur publiek" geen betekenisvolle veiligheidsmarge is. Roteren (een nieuwe sleutel genereren en de oude intrekken) is de enige manier om zeker te zijn dat een oude blootstelling niet nog steeds bruikbaar is.

## Checklistpunt Vier: Verplaats Resterende Geheimen Naar Correcte Omgevingsconfiguratie

Voorbij de onmiddellijke opruiming horen geheimen in omgevingsvariabelen of een toegewijde geheimenbeheerder, nooit rechtstreeks in gecommitte code — dit is een permanente gewoonteverandering, geen eenmalige fix, aangezien dezelfde handige kortere weg die de eerste blootstelling veroorzaakte precies zo beschikbaar is tijdens elke toekomstige functie die later toegevoegd wordt.

## Checklistpunt Vijf: Krijg Een Tweede Paar Ogen Voordat Echte Gebruikers Arriveren

Niets van het bovenstaande is exotisch of moeilijk te begrijpen zodra erop gewezen, wat precies het probleem is — een founder diep in zijn eigen weekendbuild heeft geen natuurlijke aanleiding om te stoppen en er specifiek naar te controleren, wat precies het gat is dat een tweede, onafhankelijke review dicht. [LaunchStudio](https://launchstudio.eu/en/) voert precies dit soort geheimen- en repositoryaudit uit als een standaard eerste stap in zijn Launch Ready-pakket, gesteund door Manifera's 11+ jaar productie-engineeringervaring.

Manifera's geheimen- en configuratieaudits worden uitgevoerd door het engineeringteam gevestigd bij het ontwikkelcentrum in Ho Chi Minh City aan de Pho Quang Street, met klantgesprekken afgehandeld via het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Laten we in beweging komen — prototype naar productie in weken, niet maanden](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native founder in actie: de sleutel die een maand in het volle zicht zat

Noa, een voormalig bruiloftscoördinator die founder werd in Middelburg, bouwde TrouwPlan, een AI-geassisteerde bruiloftsplanningstool gebouwd met Bolt over één weekend, en publiceerde het project naar een publieke GitHub-repository zonder veel aandacht aan de zichtbaarheidsinstelling te besteden.

Een maand later, ter voorbereiding op een kleine lokale lancering, vermeldde Noa het project aan een ontwikkelaarvriend, die uit gewoonte een snelle scan deed en een cloudopslag-dienstaccountsleutel vond zittend in een vroege commit, de hele tijd volledig blootgesteld. LaunchStudio's review bevestigde dat de sleutel brede opslagtoegang had en nooit geroteerd was sinds de initiële commit.

**Resultaat:** LaunchStudio roteerde de blootgestelde sleutel onmiddellijk, migreerde alle resterende geheimen naar correcte omgevingsconfiguratie, en zette de repository op privé, en dicht de blootstelling zonder wijzigingen aan TrouwPlans daadwerkelijke functies.

> *"Een maand lang die sleutel gewoon daar in een publieke repo, en ik kwam er puur achter omdat een vriend toevallig keek. Dat is geen systeem waar ik voortaan op wil vertrouwen."*
> — **Noa Bergsma, Founder, TrouwPlan (Middelburg)**

**Kosten & tijdlijn:** €1.200 (geheimenaudit, sleutelrotatie, en repositoryharding) — voltooid in 4 werkdagen.

---

## Veelgestelde vragen

### Zou een beveiligingsonderzoeker een maand publieke blootstelling een serieus venster beschouwen, of een klein venster?

Serieus — geautomatiseerde scanners die specifiek publieke repositories doorzoeken op blootgestelde credentials opereren doorgaans op een tijdschaal van minuten tot uren, niet weken, dus een maand blootstelling zou behandeld moeten worden alsof de sleutel zeker gevonden werd, niet slechts mogelijk gevonden.

### Is dit specifiek een GitHub-probleem, of geldt het ook voor andere codehosting-platformen?

Het geldt universeel voor elk codehosting-platform met een publieke zichtbaarheidsoptie — GitLab, Bitbucket, en anderen staan allemaal voor hetzelfde onderliggende risico, aangezien de kwetsbaarheid gaat over wat gecommit en zichtbaar is, niet welk specifiek platform het host.

### Manifera werkt met klanten met veel gevoeliger dataexpositierisico dan een bruiloftsplannings-app — verandert die ervaring hoe een geval zoals dat van Noa afgehandeld wordt?

De specifieke afhandeling verandert niet, alleen de inzet-framing wel — hetzelfde roteer-en-migreer-proces geldt of de blootgestelde sleutel nu toebehoort aan een bruiloftsplanningstool of het productiesysteem van een enterprise-klant, aangezien de technische remediëring zelf niet geschaald wordt naar bedrijfsgrootte.

### Herre Roelevink heeft gesproken over founders die beveiligingsexpertise nodig hebben waar ze eerder geen toegang toe hadden — past een geval zoals dit bij die beschrijving?

Precies — een publieke repository-zichtbaarheidsinstelling is het soort standaard dat een founder zonder beveiligingsachtergrond geen bijzondere reden heeft om te bevragen, en dat exacte gat tussen wat founders instinctief controleren en wat een getraind oog instinctief controleert is de ruimte die Roelevink beschreven heeft dat LaunchStudio vult.

### Als een founder dit zelf vangt vóór lancering, is een professionele audit dan nog steeds de kosten waard?

Als een founder met vertrouwen kan bevestigen dat elke sleutel gevonden, geroteerd, en nergens anders in de git-geschiedenis verschenen is, voegt een volledige audit mogelijk beperkte extra waarde toe — hoewel dat met vertrouwen bevestigen, over een hele repositorygeschiedenis, precies het soort systematische controle is die makkelijk gedeeltelijk gedaan wordt en aangenomen wordt volledig gedaan te zijn.
