---
Titel: "Het werkt in de demo: Waarom 'AI werkt' niet hetzelfde is als gereed voor lancering"
Trefwoorden: ai works, ai coding, ai secure, LaunchStudio, Manifera
Koperfase: Bewustzijn
Doelgroep: AI-Native oprichter (Niet-technisch)
---

# Het werkt in de demo: Waarom 'AI werkt' niet hetzelfde is als gereed voor lancering

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Het werkt in de demo: Waarom 'AI werkt' niet hetzelfde is als gereed voor lancering",
  "description": "Een rechtstreekse blik op de kloof tussen 'AI werkt' als een demo-claim en 'gereed voor lancering' als een productie-claim.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-07-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/it-works-in-the-demo-ai-works-isnt-ready-to-ship"
  }
}
</script>

U heeft uw prototype voltooid. Het werkt. Elke knop doet wat het verondersteld wordt te doen, elk scherm laadt, elke werkstroom wordt exact voltooid zoals u het ontworpen heeft. Dus waarom reageert bijna elke ervaren ingenieur op "het werkt" met een vervolgvraag in plaats van met een felicitatie? Omdat "werkt" een hoop stil, ononderzocht werk verricht in die zin. En het specifieke ding dat het meestal betekent – werkt voor mij, op de manier waarop ik het gebruik – is een aanzienlijk smallere claim dan oprichters de neiging hebben aan te nemen.

## Twee heel verschillende betekenissen van "Werkt"

"Werkt" kan betekenen: deze specifieke reeks acties, uitgevoerd door de persoon die het gebouwd heeft, levert het verwachte resultaat op. Of het kan betekenen: deze applicatie gedraagt zich veilig en correct onder een heel breed bereik van invoeren, inclusief invoeren die niemand had voorzien, van gebruikers die zich niet gedragen op de manier waarop de oprichter zich voorstelde dat ze zouden doen. AI-coderingsassistenten zijn bijna volledig geoptimaliseerd richting het bewijzen van de eerste betekenis, omdat dat de betekenis is die een demo natuurlijk test. En de tweede betekenis is degene die daadwerkelijk bepaalt of een product het contact met echte, onvoorspelbare gebruikers overleeft.

## Waar de kloof tussen de twee betekenissen daadwerkelijk leeft

De kloof heeft de neiging zich te concentreren op exact de plekken waar het eigen testen van een oprichter nooit komt: vrije-tekst invoervelden, zoekbalken, bestandsuploads, en overal waar een gebruiker een waarde verstrekt die de applicatie vervolgens gebruikt om een databasequery of bestandspad te construeren. Een oprichter die zijn eigen testgegevens doorzoekt typt redelijke zoektermen en krijgt redelijke resultaten – omdat dat is wat "zoekfunctie testen" betekent voor iemand die niet specifiek probeert het te breken.

## Waarom niet-geschoonmaakte (Unsanitized) invoer het tekstboekvoorbeeld van dit probleem is

Een zoekveld dat gebruikersinvoer rechtstreeks doorgeeft aan een databasequery zonder het op de juiste manier schoon te maken kan, in het ergste geval, toestaan dat een specifiek gevormde invoer de query zelf manipuleert – gegevens uithalend die het nooit verondersteld was te retourneren, of in ernstigere gevallen records rechtstreeks wijzigen of verwijderen. Dit is geen hypothese: het is een van de oudste, meest gedocumenteerde klassen van kwetsbaarheden in webontwikkeling. En met AI gegenereerde code die er niet specifiek op beoordeeld is, is exact zo blootgesteld als handgeschreven code met dezelfde vergissing zou zijn.

## Waarom "Ik heb de zoekfunctie getest en het werkte prima" dit niet uitsluit

Het testen van de zoekfunctie met normale zoektermen – een productnaam, de naam van een klant, een redelijk trefwoord – triggert deze manier van mislukken nooit. Normale zoektermen zijn namelijk per definitie niet de specifiek misvormde invoer die de onderliggende kloof blootlegt. De twee testen zien er vanaf de buitenkant identiek uit (u typt iets, u krijgt resultaten) maar slechts één daarvan is daadwerkelijk aan het peilen of de queryconstructie eronder veilig is.

## Een veldgids voor oprichters om risicovolle invoerafhandeling te spotten zonder elke regel te lezen

U hoeft uw gehele codebase niet regel voor regel te lezen om een redelijk gevoel te krijgen van waar dit soort risico zich concentreert – u moet weten welke vragen u moet stellen en waar u een zoekopdracht naartoe moet richten.

**Zoek in uw eigen codebase naar deze patronen:**

- **Directe tekst-aaneenschakeling (String Concatenation) in een query.** Zoek naar een databasequery die gebouwd wordt door stukken tekst aan elkaar te voegen, in het bijzonder overal waar een variabele is opgenomen die afkomstig is uit gebruikersinvoer – bijvoorbeeld een querytekenreeks samengesteld met `+` of template literals die iets bevatten wat de gebruiker heeft getypt. Dit is de tekstboekversie van het patroon dat een misvormde zoektekenreeks rechtstreeks RouteWise's database liet bereiken.
- **Rauwe query-methoden, zelfs binnen een op ORM gebaseerd project.** De meeste moderne ORM's parametriseren invoer standaard veilig, maar bijna allemaal stellen ze ook een "raw query" of "execute" ontsnappingsluik bloot voor gevallen waar de normale methoden van de ORM niet goed mee omgaan. AI-coderingsassistenten grijpen vaker naar dat ontsnappingsluik dan oprichters verwachten, in het bijzonder voor alles wat lijkt op een flexibele zoek- of filterfunctie.
- **Elk veld dat vrije tekst accepteert en later verschijnt in een database-opzoeking, een bestandspad, of een systeemcommando.** Zoekbalken zijn het duidelijke geval, maar hetzelfde onderliggende risico geldt voor bestandsnamen, tags, en elke andere door de gebruiker bewerkbare tekst die uw applicatie later gebruikt om iets op te zoeken in plaats van het simpelweg weer te geven.

**Een vraag die het waard is om uw AI-tool rechtstreeks te stellen:** "Gebruikt deze query geparametriseerde invoer, of is een deel ervan gebouwd uit een tekenreeks die gebruikersinvoer bevat?" Het is geen garantie – de tool kan verkeerd antwoorden, of het onderliggende patroon kan veranderen in een latere bewerking die u niet specifiek opnieuw heeft gecontroleerd. Maar het is een sneller eerste signaal dan het zelf lezen van de rauwe code, en het geeft u een specifieke, beantwoordbare vraag om naar een professionele beoordeling te brengen in plaats van een vage zorg over "is dit veilig."

Niets hiervan vervangt een correcte audit, die elk toegangspunt systematisch controleert in plaats van het handjevol waar een oprichter toevallig aan denkt om naar te zoeken. Maar het is een redelijke manier om een globaal gevoel van uw eigen blootstelling te krijgen voordat dat gesprek plaatsvindt, en het haalt op zichzelf vaak ten minste één duidelijke instantie naar boven.

## Hoe een echte herstelling er concreet uitziet

Het sluiten van deze kloof betekent het vervangen van directe tekst-aaneenschakeling in query's door op de juiste manier geparametriseerde query's of een ORM-laag die het ontsnappen (escaping) automatisch afhandelt. En het consequent toepassen van dat patroon over elk invoerveld dat de database bereikt, en niet alleen het veld dat een oprichter toevallig onthoudt. [LaunchStudio](https://launchstudio.eu/en/) auditeert exact dit patroon over een gehele codebase als onderdeel van haar standaard beoordeling, ondersteund door Manifera's 11+ jaar ervaring met productie-engineering over Node.js, Laravel en .NET backends.

Manifera's ingenieurs, voornamelijk werkend vanuit het ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat met klantcoördinatie via het kantoor in Amsterdam aan de Herengracht 420, passen hetzelfde beoordelingspatroon toe ongeacht welk specifiek backend-framework de AI-tool van een oprichter toevallig heeft gegenereerd.

[Stuur ons uw prototypelink — we geven u gratis advies](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: De zoekbalk die alles kon zien

Tim, een voormalig magazijnoperaties-manager die oprichter werd in Den Haag, bouwde RouteWise, een AI-ondersteunde app voor logistieke tracking gebouwd met Lovable, waarmee dispatch-teams zendingsrecords kunnen doorzoeken op klantnaam of trackingnummer.

Een IT-aannemer van een partner, die uit professionele gewoonte in het zoekveld zat te peuteren, voerde een opzettelijk misvormde zoektekenreeks in en kreeg een lijst van zendingsrecords terug die toebehoorden aan een volledig ander, ongerelateerd klantaccount. LaunchStudio's beoordeling bevestigde dat de zoekfunctie rauwe gebruikersinvoer rechtstreeks doorgaf aan de databasequery zonder opschoning (sanitization).

**Resultaat:** LaunchStudio verving de kwetsbare queryconstructie door op de juiste manier geparametriseerde query's over elke zoek- en filterfunctie in de app, waardoor de blootstelling werd gesloten zonder de zoekervaring te veranderen waar Tim's dispatch-teams al aan gewend waren.

> *"Ik testte die zoekbalk voortdurend tijdens het bouwen. Ik zocht honderd keer naar echte klantnamen en echte trackingnummers. Het was nooit bij me opgekomen om er opzettelijk iets geks in te typen."*
> — **Tim Oosterhuis, Oprichter, RouteWise (Den Haag)**

**Kosten en tijdlijn:** € 2.100 (audit van invoeropschoning en query-uitharding) — voltooid in 6 werkdagen.

---

## Veelgestelde vragen

### Moet een oprichter de term 'SQL-injection' specifiek kennen?

Nee, het herkennen van het patroon waarin gebruikersinvoer een database-opzoeking bereikt doet er meer toe dan het kennen van de formele term.

### Voorkomt het gebruiken van een ORM of Supabase dit probleem automatisch?

Het vermindert het risico standaard aanzienlijk, maar rauwe query-oproepen kunnen die bescherming nog steeds omzeilen.

### Helpt brede backend-ervaring over verschillende stacks bij dit specifieke probleem?

Ja, omdat het onderliggende patroon niet stack-specifiek is en verschijnt over PHP, Node.js, Python en .NET gelijkwaardig.

### Vormt een achtergrond in cybersecurity hoe dit soort bevindingen wordt behandeld?

Ja, deze categorie van invoerafhandelingsfouten wordt behandeld als fundamenteel in plaats van exotisch, consistent met die achtergrond.

### Kan ik mijn AI-coderingsassistent vragen om dit over de gehele codebase in één prompt te herstellen?

Het is het proberen waard als een eerste stap, maar behandel het resultaat als een startpunt in plaats van een garantie – een enkele prompt kan instanties missen die opgeborgen zitten in bestanden die de tool niet heroverweegt, wat exact is waarom een systematische beoordeling het resultaat nog steeds controleert.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet een oprichter de term 'SQL-injection' specifiek kennen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, het herkennen van het patroon waarin gebruikersinvoer een database-opzoeking bereikt doet er meer toe."
      }
    },
    {
      "@type": "Question",
      "name": "Voorkomt het gebruiken van een ORM of Supabase dit probleem automatisch?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het vermindert het risico standaard aanzienlijk, maar rauwe query-oproepen kunnen die bescherming omzeilen."
      }
    },
    {
      "@type": "Question",
      "name": "Helpt brede backend-ervaring over verschillende stacks bij dit specifieke probleem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, omdat het onderliggende patroon niet stack-specifiek is en verschijnt over PHP, Node.js, Python en .NET."
      }
    },
    {
      "@type": "Question",
      "name": "Vormt een achtergrond in cybersecurity hoe dit soort bevindingen wordt behandeld?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, deze categorie van invoerafhandelingsfouten wordt behandeld als fundamenteel in plaats van exotisch."
      }
    },
    {
      "@type": "Question",
      "name": "Zou van een algemene freelancer moeten worden verwacht dat hij dit opvangt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het hangt sterk af van die individuele beveiligingsachtergrond, niet van freelancing als categorie."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik mijn AI-coderingsassistent vragen om dit over de gehele codebase te herstellen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het is het proberen waard als eerste stap, maar behandel het resultaat als startpunt in plaats van een garantie."
      }
    }
  ]
}
</script>
