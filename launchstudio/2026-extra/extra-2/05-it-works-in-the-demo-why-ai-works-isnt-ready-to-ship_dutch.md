---
Titel: "Het Werkt In De Demo: Waarom 'AI Werkt' Niet Hetzelfde Is Als Klaar Om Te Lanceren"
Trefwoorden: ai works, ai coding, ai secure, LaunchStudio, Manifera
Koperfase: Bewustzijn
Doelgroep: AI-Native Founder (niet-technisch)
---

# Het Werkt In De Demo: Waarom 'AI Werkt' Niet Hetzelfde Is Als Klaar Om Te Lanceren

Je hebt jouw prototype afgemaakt. Het werkt. Elke knop doet wat hij hoort te doen, elk scherm laadt, elke workflow voltooit precies zoals je hem ontworpen hebt. Waarom reageert dan bijna elke ervaren engineer op "het werkt" met een vervolgvraag in plaats van een felicitatie? Omdat "werkt" veel stil, onbekeken werk verricht in die zin, en het specifieke ding dat het meestal betekent — werkt voor mij, op de manier waarop ik het gebruik — een veel nauwere claim is dan founders geneigd zijn aan te nemen.

## Twee Heel Verschillende Betekenissen Van "Werkt"

"Werkt" kan betekenen: deze specifieke reeks acties, uitgevoerd door de persoon die het bouwde, produceert het verwachte resultaat. Of het kan betekenen: deze applicatie gedraagt zich veilig en correct onder een heel breed scala aan invoer, inclusief invoer die niemand voorzag, van gebruikers die zich niet gedragen zoals de founder zich voorstelde dat ze zouden doen. AI-codeertools zijn bijna volledig geoptimaliseerd om de eerste betekenis te bewijzen, omdat dat de betekenis is die een demo natuurlijk test — en de tweede betekenis is degene die daadwerkelijk bepaalt of een product het contact met echte, onvoorspelbare gebruikers overleeft.

## Waar Het Gat Tussen De Twee Betekenissen Daadwerkelijk Leeft

Het gat concentreert zich doorgaans op precies de plekken waar de eigen tests van een founder nooit komen: vrije-tekst-invoervelden, zoekvakken, bestandsuploads, en overal waar een gebruiker een waarde levert die de applicatie vervolgens gebruikt om een databasequery of bestandspad te construeren. Een founder die door zijn eigen testdata zoekt typt redelijke zoektermen en krijgt redelijke resultaten — omdat dat is wat "zoeken testen" betekent voor iemand die niet specifiek probeert het te breken.

## Waarom Ongesaneerde Invoer De Studieboekversie Van Dit Probleem Is

Een zoekveld dat gebruikersinvoer rechtstreeks doorgeeft aan een databasequery zonder het correct te saneren kan, in het slechtste geval, toestaan dat specifiek vervaardigde invoer de query zelf manipuleert — data extraheren die het nooit had mogen teruggeven, of in ernstigere gevallen records regelrecht wijzigen of verwijderen. Dit is geen hypothese: het is een van de oudste, best gedocumenteerde kwetsbaarheidsklassen in webontwikkeling, en AI-gegenereerde code die niet specifiek daarop gereviewd is, is exact zo blootgesteld als handgeschreven code met hetzelfde toezichtsgebrek zou zijn.

## Waarom "Ik Heb Zoeken Getest En Het Werkte Prima" Dit Niet Uitsluit

Zoeken testen met normale zoektermen — een productnaam, de naam van een klant, een redelijk trefwoord — triggert deze faalmodus nooit, omdat normale zoektermen, per definitie, niet de specifiek misvormde invoer zijn die het onderliggende gat blootlegt. De twee tests zien er identiek uit van buitenaf (je typt iets, je krijgt resultaten) maar slechts één ervan onderzoekt daadwerkelijk of de queryconstructie eronder veilig is.

## Hoe Een Echte Fix Er Concreet Uitziet

Dit gat dichten betekent directe stringconcatenatie in queries vervangen door correct geparametriseerde queries of een ORM-laag die escaping automatisch afhandelt, en dat patroon consistent toepassen over elk invoerveld dat de database bereikt, niet alleen degene die een founder toevallig onthoudt. [LaunchStudio](https://launchstudio.eu/en/) audit precies dit patroon over een hele codebase als onderdeel van zijn standaardreview, gesteund door Manifera's 11+ jaar productie-engineeringervaring over Node.js-, Laravel-, en .NET-backends.

Manifera's engineers, voornamelijk werkend vanuit het ontwikkelcentrum in Ho Chi Minh City aan de Pho Quang Street met klantcoördinatie via het Amsterdamse kantoor aan de Herengracht 420, passen ditzelfde reviewpatroon toe ongeacht welk specifiek backendframework de AI-tool van een founder toevallig genereerde.

[Stuur ons de link naar jouw prototype — we geven je gratis advies](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native founder in actie: het zoekvak dat alles kon zien

Tim, een voormalig magazijnoperationsmanager die founder werd in Den Haag, bouwde RouteWise, een AI-geassisteerde logistiektrackingapp gebouwd met Lovable, waarmee dispatchteams zendingsrecords konden zoeken op klantnaam of trackingnummer.

Een IT-contractor van een partner, die uit professionele gewoonte in het zoekveld prutste, voerde een doelbewust misvormde zoekstring in en kreeg een lijst zendingsrecords terug die toebehoorden aan een compleet ander, niet-gerelateerd klantaccount. LaunchStudio's review bevestigde dat de zoekfunctie ruwe gebruikersinvoer rechtstreeks doorgaf aan de databasequery zonder sanering.

**Resultaat:** LaunchStudio verving de kwetsbare queryconstructie door correct geparametriseerde queries over elke zoek- en filterfunctie in de app, en dicht de blootstelling zonder de zoekervaring te veranderen waar Tims dispatchteams al aan gewend waren.

> *"Ik testte dat zoekvak constant terwijl ik het bouwde. Ik zocht honderd keer echte klantnamen en echte trackingnummers. Het kwam nooit bij me op om er iets doelbewust vreemds in te typen."*
> — **Tim Oosterhuis, Founder, RouteWise (Den Haag)**

**Kosten & tijdlijn:** €2.100 (invoersanering- en queryhardingsaudit) — voltooid in 6 werkdagen.

---

## Veelgestelde vragen

### Een backend-gerichte engineer zou dit specifiek "SQL-injectie" kunnen noemen — is dat een te technische term voor een founder om te moeten kennen?

De term zelf doet er niet veel toe voor een founder om te onthouden, maar het patroon herkennen is nuttig: elk veld waar een gebruiker iets typt dat later gebruikt wordt om iets op te zoeken in een database is de moeite waard om specifiek naar te vragen, zelfs zonder de formele kwetsbaarheidsnaam te kennen.

### Voorkomt het gebruik van een ORM of een beheerd databaseplatform zoals Supabase dit automatisch, of kan het daar nog steeds gebeuren?

Het vermindert het risico substantieel wanneer gebruikt zoals bedoeld, aangezien de meeste ORM's queries standaard parametriseren, maar het is nog steeds mogelijk die bescherming te omzeilen met ruwe query-aanroepen, wat AI-codeerassistenten soms genereren wanneer een standaard ORM-methode niet makkelijk uitdrukt wat gevraagd werd.

### Manifera heeft decennia gecombineerde engineeringervaring over heel verschillende techstacks — helpt die breedte daadwerkelijk bij een specifiek Lovable-gegenereerde Node.js-app?

Ja, precies omdat deze klasse kwetsbaarheid niet stack-specifiek is — hetzelfde onderliggende patroon (ongesaneerde invoer die een query bereikt) verschijnt over PHP, Node.js, Python, en .NET, dus brede backendervaring vertaalt zich direct in plaats van stack-specifieke specialisatie te vereisen.

### Herre Roelevinks eigen achtergrond omvat cybersecuritywerk met TNO — vormt die ervaring hoe LaunchStudio een bevinding zoals die van Tim behandelt?

Het is een directe doorlijn — TNO-geaffilieerd beveiligingsonderzoek behandelt precies deze categorie invoerafhandelingsfout als fundamenteel in plaats van exotisch, en diezelfde fundamentele behandeling is wat LaunchStudio toepast wanneer dit patroon opduikt in de codebase van een AI-native founder.

### Is dit het soort probleem dat een founder zou moeten verwachten dat een freelancer vangt, of vereist het iets meer gespecialiseerds?

Het hangt sterk af van de specifieke beveiligingsachtergrond van de individuele freelancer in plaats van freelancen als categorie — dit is deel van waarom LaunchStudio zich specifiek positioneert tegenover generalistische freelancers voor founders die zekerheid willen dat de review gedaan werd door iemand met toegewijde beveiligingservaring, niet alleen algemene codeervaardigheid.
