---
Titel: "Wanneer Uw Medeoprichter Zegt: 'Dat Kunnen We Zelf Bouwen'"
Trefwoorden: build vs buy startup, meningsverschil technische medeoprichter, zelf AI app beveiligen, besluitvorming oprichters, backend uitbesteden, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Wanneer Uw Medeoprichter Zegt: "Dat Kunnen We Zelf Bouwen"

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wanneer Uw Medeoprichter Zegt: 'Dat Kunnen We Zelf Bouwen'",
  "description": "Hoe een niet-technische oprichter de claim van een medeoprichter kan evalueren dat het team productie-hardening zelf aankan, zonder over code te hoeven discussiëren. Een methode om 'zelf bouwen' eerlijk te beprijzen en de taakverdeling te vinden waarin beiden gelijk krijgen.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/nl/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2027-01-09",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/when-your-co-founder-says-we-can-build-it-ourselves"
  }
}
</script>

"Dus de offerte bedraagt € 2.600."

"Waarvoor precies?"

"Beveiliging, de betaalintegratie en het platform professioneel live zetten."

"Eerlijk? Dat kunnen we prima zelf bouwen. Ik heb het meeste al in elkaar gezet in Cursor. Geef me twee weekenden."

Als u de niet-technische helft van dit gesprek vormt, bevindt u zich nu in een discussie die u op technische gronden niet kunt winnen en ook niet zou moeten proberen te winnen. U weet immers niet of twee weekenden realistisch is. Uw medeoprichter weet dat waarschijnlijk zelf ook niet — en het cruciale punt is: ze zijn niet oneerlijk. Ze beantwoorden een aanzienlijk smallere vraag dan de vraag die u stelde, en het volledige conflict bevindt zich precies in die kloof.

## Drie Verschillende Zinnen Die Identiek Klinken

"Dat kunnen we zelf bouwen" is minstens drie verschillende beweringen verpakt in één jasje, en ze hebben een totaal verschillende waarheidswaarde.

**"Ik weet hoe dit moet."** Vaak volkomen waar. Uw medeoprichter heeft er ongetwijfeld voldoende over gelezen, en moderne tools hebben veel infrastructureel werk daadwerkelijk toegankelijk gemaakt. Neem deze uitspraak gerust serieus.

**"Ik weet hoe dit moet zónder dat het ons later fataal wordt."** Een flink stuk wankeler. Weten dat autorisatie op de server gecontroleerd moet worden, is niet hetzelfde als weten welke API-routes dat op dit moment níét doen. Het verschil tussen "ik begrijp het concept" en "ik heb alle plekken in onze codebase gevonden waar het ontbreekt", is de gehele klus.

**"Ik ga hier binnenkort daadwerkelijk de tijd voor vinden om het tot een goed einde te brengen."** Dit is de bewering die in de praktijk het vaakst sneuvelt, en het is het punt waar niemand kritisch naar kijkt, omdat het klinkt als een planningkwestie in plaats van een inhoudelijk risico.

Uw taak is niet om de eerste stelling aan te vechten. Uw taak is om deze drie beweringen expliciet uit elkaar te trekken. Het moment dat u ze scheidt, transformeert het gesprek van een beladen discussie over competentie naar een pragmatisch overleg over tijd en scope — en niemand voelt zich aangevallen door een agenda.

## Vertaal "Zelf": Wie Voert Het Werk Feitelijk Uit?

Stel één simpele vraag, vriendelijk en zonder oordeel: *welke avonden precies?*

"Zelf" betekent in werkelijkheid vrijwel altijd één specifiek persoon, die werkt buiten de uren die al verschuldigd zijn aan een vaste baan, de product-roadmap of gesprekken met investeerders. Het is geen heel team. Het is uw medeoprichter, 's avonds na 21:00 uur, bovenop alles wat er al op diens bord ligt.

Vraag vervolgens waar die persoon op dit moment de énige in is. Als uw medeoprichter tevens de enige engineer is, is elke avond besteed aan het verifiëren van cryptografische webhook-handtekeningen een avond die niet besteed wordt aan de kern van het product. Het besluit om het "zelf te bouwen" is niet: "geef € 0 uit in plaats van € 2.600." Het is: "trek onze enige technische kracht weg van het product voor een onbepaald aantal weken dat we nog niet exact hebben berekend."

Die formulering is geen pleidooi tegen zelf bouwen. Er zijn genoeg teams die het absoluut zelf moeten doen. Maar het maakt de afruil glashelder, en heldere afruilen worden bewust besloten in plaats van dat men er per ongeluk in wegglijdt.

## Het Deel Waarin Uw Medeoprichter Gelijk Heeft

Ga dit gesprek in met een helder besef van welk terrein u direct moet toegeven, want dat direct erkennen is precies wat de rest van het gesprek constructief maakt.

Uw medeoprichter heeft gelijk dat veel van deze materie te leren is. Ze hebben gelijk dat alles uitbesteden afhankelijkheid creëert — een oprichter die zijn eigen deployment-pipeline nooit heeft aangeraakt, is één verstoorde relatie verwijderd van een complete blokkade. Ze hebben gelijk dat niemand de logica van uw product zo door en door begrijpt als zijzelf. En ze hebben volkomen gelijk dat sommige offertes voor dit werk absurd zijn: traditionele softwarebureaus offreren herbouwtijden van € 20.000 tot € 50.000, en als dat het referentiekader is, is "we doen het zelf" een volstrekt logische reactie.

Spreek dat allemaal luid en duidelijk uit. Verscherp de discussie daarna tot de enige vraag die er werkelijk toe doet: niet *kunnen we het*, maar *móéten we het willen, gezien wat die uren elders opleveren en wat de gevolgen zijn als we er per ongeluk naast zitten?*

## Wat Je Niet in Één Weekend Leert

Er bestaat een categorie werk waarbij het risico niet zit in de programmeercomplexiteit, maar in *weten waar je moet zoeken* — en dat onderscheid is essentieel voor een niet-technische oprichter om te begrijpen.

Het bouwen van een inlogscherm is een afgebakende taak met een zichtbare finishlijn: het werkt wel of het werkt niet. Zorgen dat geen enkele ingelogde gebruiker de dossiers van een andere gebruiker kan inzien, is geen geïsoleerde taak, het is een *systematische sweep*. Het vereist het nalopen van elk endpoint, elke query, elke bestandsupload en elke data-export met telkens dezelfde kritische vraag. Ziet u er eentje over het hoofd, dan lijkt alles aan de oppervlakte nog steeds vlekkeloos te functioneren. Er verschijnt geen foutmelding. De applicatie werkt ogenschijnlijk perfect, totdat iemand een cijfer in een URL aanpast en ineens de privégegevens van een concurrent op het scherm heeft staan.

Hetzelfde patroon geldt voor betalingen. Een betaalkoppeling werkend krijgen kost een namiddag; zorgen dat deze waterdicht klopt, duurt aanzienlijk langer. De betrouwbaarheid zit namelijk in de uitzonderingspaden: een webhook die tweemaal wordt afgeleverd, een creditcard die in maand vier mislukt bij verlenging, een terugbetaling of een tussentijdse opzegging. Geen van die situaties doet zich voor terwijl u aan het bouwen bent, dus geen enkele fout valt op totdat een echte klant ermee te maken krijgt.

Dát is wat senioriteit toevoegt: niet zozeer het intypen van de uiteindelijke regel code, maar het getrainde instinct voor wáár het misgaat. Een engineer die veertig SaaS-applicaties productierijp heeft gemaakt, kent de zeven kwetsbare plekken uit zijn hoofd. Wie zijn eerste product beveiligt, kent alleen de twee voorbeelden waarover toevallig een blogpost werd gelezen.

## De Eerlijke Rekensom van "Zelf Bouwen"

Maak deze berekening samen, open en eerlijk op papier. Het beëindigt discussies sneller dan welk debat ook.

**De uren.** Vraag uw medeoprichter om een realistische inschatting van de volledige sweep — niet alleen de leuke features, maar de hele audit. Pas vervolgens de vermenigvuldiger toe die elke eerlijke software-engineer op zijn eigen schattingen legt. Zegt men twee weekenden, reken dan op vier. Dat betekent zestig tot tachtig avonduren voor een doorsnee prototype met accounts, database en betalingen.

**De alternatieve kosten.** Niet het theoretische salaris, maar wat er níét gebeurt. Zestig uur van uw enige techneut staat gelijk aan ruimschoots drie weken voltijds productwerk — drie weken aan features, klantinterviews of stabiliteitsverbeteringen die blijven liggen.

**De vertraging.** Als die uren uit spaarzame vrije avonden moeten komen, betekent zestig uur bij tien uur per week een vertraging van zes weken. Vergelijk dat met een vaste doorlooptijd van 1 tot 3 weken. Dat verschil is vier weken op uw livegang. Heeft u wachtende klanten of een tikkende runway, dan vertegenwoordigt die maand vertraging een heel concreet bedrag in euro's.

**Het gemiste risico.** Vermenigvuldig de kans dat er iets over het hoofd wordt gezien met de kosten van die fout. Een datalek met echte klantgegevens is geen eenvoudig bugje; het betekent AVG-meldplichten, imagoschade en teruggaven. Zelfs een kans van 20% op een incident van € 10.000 vertegenwoordigt een risicowaarde van € 2.000.

Vergelijk dat totaalbedrag met de offerte. Soms wint de offerte met vlag en wimpel. Soms niet — een oprichter met zeeën van tijd en een simpel product kan onderaan de streep goedkoper uit zijn, en in dat geval: bouw het van harte zelf. Wat u in beide gevallen wint, is een beslissing gebaseerd op feiten en cijfers, in plaats van op wie het hardst zijn gelijk opeiste.

## De Drievragentest

Wilt u een snelle indicatie van waar u staat? Stel uw medeoprichter deze drie vragen. U hoeft de antwoorden niet tot in detail technisch te begrijpen; u hoeft alleen te luisteren naar hoe specifiek de toelichting is.

1. **"Waar in onze code controleren we dat een gebruiker alleen zijn eigen data kan inzien, en op hoeveel plekken is die controle geprogrammeerd?"** Een zelfverzekerd, concreet antwoord met een specifiek aantal endpoints is een uitstekend teken. "Dat regelt Supabase automatisch" is géén antwoord; dat is de naam van een platform dat het uitsluitend regelt als het correct door u is geconfigureerd.
2. **"Wat gebeurt er in ons systeem als Stripe ons per ongeluk twee keer dezelfde betalingsnotificatie stuurt?"** Het juiste antwoord benoemt dat de tweede melding als duplicaat (idempotent) wordt genegeerd. Een vaag antwoord betekent dat deze logica nog nergens geschreven is.
3. **"Als onze database vannacht per ongeluk gewist wordt, wat doen we dan morgenochtend om 9:00 uur?"** Het juiste antwoord beschrijft een hersteltest die men recent persoonlijk heeft uitgevoerd. "Er zijn automatische back-ups in de cloud" is een vrome wens, geen noodplan.

Drie concrete, specifieke antwoorden: ze hebben de materie waarschijnlijk goed in de vingers en u kunt het met een gerust hart aan hen toevertrouwen. Drie ontwijkende of algemene antwoorden: men begrijpt de theorie, maar heeft de venijnige praktijkdetails nog niet ontmoet — wat exact de situatie is waarin ontwikkelaars de benodigde tijd met een factor drie onderschatten.

## De Taakverdeling Die de Knoop Meestal Doorhakt

De beste uitkomst is zelden alles-of-niets, en de kwestie zo zwart-wit benaderen is precies wat er een conflict van maakt.

Koop de *sweep* in. Bouw de rest zelf. Haal een extern paar ervaren ogen binnen voor de onderdelen waar *weten waar je moet zoeken* het gehele werk bepaalt: autorisatie over elk endpoint, API-sleutels die niet in de browser horen, de betalings-statemachine en een geteste back-up-restore. Behoud de unieke productlogica, het frontend design en alles wat uw medeoprichter uitdagend en waardevol vindt binnenshuis.

Dit werkt uitstekend om twee redenen die veel zwaarder wegen dan alleen geld. Uw medeoprichter behoudt het volledige eigenaarschap over het product en degradeert niet tot een toeschouwer in zijn eigen bedrijf. En een professioneel uitgevoerd hardening-traject levert helder gedocumenteerde, transparante code op in uw eigen repository. Daardoor fungeert de sweep direct als de snelste technische bijscholing die uw medeoprichter ooit zal krijgen: ze zien in hun eigen vertrouwde code exact hoe de best practices zijn toegepast.

De frontend die zij hebben gebouwd, blijft onaangeroerd. Dat is geen doekje voor het bloeden; het is de enige juiste manier waarop backend-hardening hoort te werken. Het neemt direct de diepere angst weg die schuilt achter "we bouwen het zelf": de angst dat een externe partij hun levenswerk overhoop gooit en ze hun eigen applicatie niet meer herkennen.

In tegenstelling tot anonieme marktplaats-freelancers, wordt LaunchStudio ondersteund door Manifera — [een software engineering-organisatie](https://www.manifera.com/about-us/) met meer dan 120 engineers, vertrouwd door partijen zoals Vodafone, TNO en CFLW. Daarom krijgt u na de sweep heldere documentatie in handen in plaats van een ondoorzichtige black box waar uw team later niets mee kan.

Komt u er samen in theorie niet uit? Laat de feiten spreken: [stuur ons de link naar uw prototype voor een kosteloze eerste blik](https://launchstudio.eu/nl/#contact). Een overzicht van wat al wel en nog niet goed is ingericht, beëindigt de discussie direct — en af en toe bevestigt die lijst simpelweg dat uw medeoprichter het inderdaad prima zelf aankan.

## Echt voorbeeld

### Twee Oprichters in Actie: De Lijst Die een Patstelling van Zes Weken Doorbrak

Femke Doornbos en haar technische medeoprichter Tim runden Rondje, een in Utrecht gevestigde plannings- en reserveringstool voor lokale amateursportverenigingen. De tool was gebouwd in Lovable, waarna Tim in Cursor aan de slag was gegaan. Femke had een offerte liggen van € 2.900 voor backend-hardening. Tim had een plan dat volgens hem "drie weekenden" zou kosten. Ze draaiden er al zes weken omheen, en in die hele periode kwam het platform geen stap dichter bij lancering.

Ze doorbraken de patstelling door een kosteloze technische review aan te vragen in plaats van blind werk uit te besteden. De uitkomsten vielen verrassend uit, en geen van beiden had de exacte uitkomst voorspeld. Tim bleek veel meer zaken al uitstekend te hebben geregeld dan Femke dacht: sessiebeheer, wachtwoordresets en een overzichtelijke databasestructuur stonden als een huis. Echter: autorisatie op clubniveau bleek slechts in twee van de elf API-endpoints daadwerkelijk afgedwongen te worden, de Google Maps API-sleutel stond open en bloot in de client-side code, en de Mollie-koppeling accepteerde betalingsbevestigingen zonder te controleren of het verzoek wel echt van Mollie afkomstig was — wat betekende dat een slim verzoek een sportclub gratis op 'actief' kon zetten.

Ze besloten de sweep in te kopen en Tim de rest te laten doen. De elf routes werden onder één waterdichte RLS-policy gebracht, de geheime sleutel werd verplaatst naar een veilige server-route en geroteerd, en verificatie van webhooks met idempotentielogica werd geïmplementeerd. Tim gebruikte diezelfde twee weken om de wachtlijstfunctie te bouwen waar drie aangesloten verenigingen al weken om smeekten.

**Resultaat:** Rondje lanceerde achttien dagen later met negen betalende sportclubs. Tim gebruikte de gedocumenteerde codeaanpassingen als blauwdruk toen hij de maand erop zelf twee nieuwe endpoints toevoegde — waarbij hij de club-autorisatie direct foutloos implementeerde.

> *"Ik had geen ongelijk dat ik het zelf kón bouwen. Ik had ongelijk over op hoeveel plekken het precies moest gebeuren. De lijst met elf concrete endpoints zien was meer waard dan wéér een avond discussiëren."*
> — **Femke Doornbos, Medeoprichter Rondje (Utrecht)**

**Kosten & Doorlooptijd:** € 2.900 (Launch Ready Pakket, autorisatie-sweep, beveiliging van geheimen en betalingsverificatie) — live in 11 werkdagen.

---

## Veelgestelde Vragen

### Hoe kan ik de planning van mijn medeoprichter bevragen zonder te twijfelen aan diens kunnen?

Stel vragen over de agenda en capaciteit, niet over diens intelligentie of vaardigheden: welke avonden, over hoeveel weken, en wat wordt er in die periode níét gebouwd aan het product. Dat herkadert het meningsverschil naar een pragmatische afweging van prioriteiten die u beiden kunt beoordelen, in plaats van een oordeel over programmeerkwaliteiten.

### Wat als mijn medeoprichter echt ervaren is en de inschatting realistisch is?

Laat hen het dan vooral zelf doen, en gebruik de drievragentest als verificatie in plaats van als aanval. Concrete antwoorden over waar autorisatiecontroles leven, hoe dubbele webhooks worden opgevangen en hoe een back-up hersteld wordt, tonen aan dat de planning gestoeld is op de daadwerkelijke codebase in plaats van op abstracte theorie.

### Maakt het inhuren van een externe partij ons niet te afhankelijk?

Niet wanneer u bedingt dat al het werk helder gedocumenteerd wordt opgeleverd in uw eigen Git-repository. De valkuil die u moet vermijden is een ondoorzichtige black box. Een professionele oplevering verkleint juist de afhankelijkheid, omdat uw medeoprichter de aangebrachte architectuurpatronen direct zelf kan hergebruiken.

### Kunnen we het werk opsplitsen zodat mijn medeoprichter een deel zelf doet?

Dat is in de praktijk vrijwel altijd de beste oplossing. Koop de audit en sweep in voor zaken waar ervaren speurwerk vereist is — autorisatie over alle routes, gelekte API-sleutels, webhook-validatie en geteste back-ups — en houd productfunctionaliteit en design binnenshuis waar uw medeoprichter de meeste waarde toevoegt.

### Wat als mijn medeoprichter externe hulp botweg weigert en ik denk dat dat onverstandig is?

Vraag eerst een vrijblijvende externe code-review aan voordat u het conflict op de spits drijft. Een objectieve lijst met bevindingen bevestigt óf dat uw medeoprichter gelijk heeft (waarmee de kous af is), óf geeft u een feitelijk document om samen over te overleggen. Beide uitkomsten zijn oneindig veel beter dan nog eens zes weken stilstand.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe kan ik de planning van mijn medeoprichter bevragen zonder te twijfelen aan diens kunnen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vraag naar de agenda en capaciteit in plaats van competentie: welke avonden, over hoeveel weken, en welke productfeatures blijven liggen. Dit maakt het een gezamenlijke planningsafweging in plaats van een ego-discussie."
      }
    },
    {
      "@type": "Question",
      "name": "Wat als mijn medeoprichter echt ervaren is en de inschatting realistisch is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Laat hen het zelf bouwen en gebruik de drievragentest ter validatie. Specifieke antwoorden over autorisatie, idempotente webhooks en herstelde back-ups wijzen op een realistische, gegronde planning."
      }
    },
    {
      "@type": "Question",
      "name": "Maakt het inhuren van een externe partij ons niet te afhankelijk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, mits alle code gedocumenteerd in uw eigen repository wordt geplaatst. Een transparante overdracht verlaagt afhankelijkheid doordat patronen direct intern herbruikbaar zijn."
      }
    },
    {
      "@type": "Question",
      "name": "Kunnen we het werk opsplitsen zodat mijn medeoprichter een deel zelf doet?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, dat is meestal de meest effectieve route. Koop de audit en backend-sweep in waar detectie-ervaring telt, en behoud productlogica en frontend binnenshuis."
      }
    },
    {
      "@type": "Question",
      "name": "Wat als mijn medeoprichter externe hulp botweg weigert en ik denk dat dat onverstandig is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vraag een gratis technische audit aan. Een concreet analyserapport geeft feitelijke houvast om het gesprek constructief voort te zetten zonder dat het een welles-nietesstrijd wordt."
      }
    }
  ]
}
</script>
