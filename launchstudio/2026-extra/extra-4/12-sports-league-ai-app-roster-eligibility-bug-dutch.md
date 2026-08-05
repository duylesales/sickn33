---
Titel: "Met AI gebouwde sportcompetitie-apps: De opstellingsgeschiktheidsbug die bij de slechtste wedstrijd naar boven komt"
Trefwoorden: ai app, build ai, sports league management software, roster management app, ai for sports leagues
Koperfase: Bewustzijn
Doelgroep: AI-Native oprichter (niet-technisch)
---

# Met AI gebouwde sportcompetitie-apps: De opstellingsgeschiktheidsbug die bij de slechtste wedstrijd naar boven komt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Met AI gebouwde sportcompetitie-apps: De opstellingsgeschiktheidsbug die bij de slechtste wedstrijd naar boven komt",
  "description": "Waarom schorsings- en geschiktheidsmarkeringen in met AI gegenereerde sportcompetitiesoftware een actie niet blokkeren.",
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
    "@id": "https://launchstudio.eu/en/blog/sports-league-ai-app-roster-eligibility-bug"
  }
}
</script>

Het is vrijdagavond en een clubsecretaris dient een officieel protest in. Niet over een beslissing van een scheidsrechter – over een speler. Hij controleert een regelboek, een afdruk van een wedstrijddag-opstelling, en een app die verondersteld werd deze exacte situatie onmogelijk te maken. Dat deed het niet.

## Geschiktheidsregels zien er eenvoudig uit totdat een echt seizoen ze test

Amateursportcompetities draaien op geschiktheidsregels: een speler die geschorst is voor twee wedstrijden kan niet worden geselecteerd voor die twee wedstrijden, een speler die geregistreerd staat bij één club kan niet halverwege het seizoen uitkomen voor een andere, een speler onder de 18 jaar kan niet worden opgesteld in een seniorenwedstrijd. Op papier ziet dit eruit als een eenvoudige boolean – geschikt of niet. In de praktijk is het een regel die moet worden afgedwongen op het exacte moment dat een teammanager zijn wedstrijddag-selectie samenstelt, en niet alleen als een status ergens in het profiel van een speler getoond wordt.

Dit is waar veel met AI gebouwde beheersapps voor competities stilletjes tekortschieten. Een tool zoals Cursor kan een spelerprofielpagina genereren die een rode "geschorst"-badge toont naast de naam van een speler – en die badge is oprecht nuttig, tot op het moment dat het scherm van de opstellingsbouwer die markering niet daadwerkelijk controleert voordat de speler mag worden toegevoegd. De badge is een weergavefunctie. Het blokkeren van de actie is een bedrijfslogica-functie. Ze worden anders gebouwd, en het is volkomen mogelijk om de ene te verzenden zonder de andere, omdat de demo waarin u een opstelling bouwt met allemaal geschikte spelers de kloof nooit blootlegt.

## Waarom deze bug erger is dan de meeste

De meeste softwarebugs kosten u tijd of geld. Deze kost een team een wedstrijd, achteraf, ten overstaan van een tegenstander en een tuchtcommissie van de competitie. Zodra er een protest is ingediend en is bevestigd dat er een geschorste speler heeft gespeeld, passen de meeste amateurcompetities een automatische reglementaire nederlaag toe – het resultaat wordt teruggedraaid, ongeacht wat er op het veld is gebeurd. Dat is een echte consequentie voor spelers die de hele week hebben getraind, voor een coach die een strijdplan heeft opgesteld, en voor de positie van een club op de ranglijst. Het is ook een zichtbaar, beschaamd falen voor de app zelf, exact op het moment dat de club deze het meest moest vertrouwen.

Het diepere probleem is dat geschiktheid niet één regel is – het zijn er meerdere, en ze beïnvloeden elkaar. Een schorsing heeft een start- en einddatum. Een transfervenster verandert bij welke club een speler hoort. Een leeftijdsgroepregel hangt af van een geboortedatum en de specifieke competitie. Een goed gebouwd systeem controleert dit allemaal op het moment van het indienen van de opstelling, en niet alleen op het moment van profielweergave. Het blokkeert de inzending rechtstreeks als er een regel wordt geschonden – met een duidelijke melding die uitlegt waarom, zodat de teammanager niet hoeft te raden.

## Wat er nodig is om geschiktheidscontroles te bouwen die daadwerkelijk standhouden

Het op de juiste manier aanpakken hiervan vereist logica voor het indienen van opstellingen die een live validatiecontrole uitvoert tegen elke toegevoegde speler – het controleren van schorsingsdata, transferstatus en leeftijdsgroepregels tegen de specifieke competitie en wedstrijddag – en de inzending weigert met een specifieke reden als er iets mislukt. Het is geen grote functie in isolatie, maar het moet correct zitten tussen de spelersdatabase en de interface voor het bouwen van de opstelling. Dat is exact het soort integratiewerk dat gehaast wordt in een snelle AI-bouw. Achter LaunchStudio staat Manifera's team van meer dan 120 ervaren ingenieurs. Deze categorie van "de weergave is juist maar de handhaving niet"-bugs is er een die ze voortdurend zien in zeer verschillende sectoren – omdat het een patroon is in hoe prototypingtools gebouwd worden, en geen eenmalige fout.

Manifera's ontwikkelingscentrum aan de Pho Quang Street in Ho Chi Minh-stad heeft dit soort backend-logica-werk afgehandeld voor een reeks klanten. Dezelfde strengheid geldt of de deadline nu een bedrijfsuitrol is of een aftrap op zaterdagochtend. Als u er niet zeker van bent of uw eigen app deze exacte kloof vertoont, [praat met een ingenieur die met AI gegenereerde code begrijpt](https://launchstudio.eu/en/#contact) voordat uw competitie er voor u achter komt.

## Geschiktheid kan veranderen tussen indienen en aftrap

Een validatiecontrole op het moment dat de opstelling wordt ingediend is een momentopname, en geen garantie – en opstellingen worden vaak dagen voordat een wedstrijd daadwerkelijk wordt gespeeld ingediend. Een tuchtcommissie kan op een donderdag een schorsing opleggen voor een incident dat na de wedstrijden van een vorig weekend is beoordeeld, lang nadat een teammanager zijn opstelling op woensdag heeft ingediend. Een transfer kan in datzelfde venster worden goedgekeurd of geweigerd. Als het systeem de geschiktheid slechts één keer controleert, op het moment van indienen, kan een opstelling die volledig geldig was toen deze werd gebouwd stilletjes ongeldig worden voordat de wedstrijd begint, zonder dat iets in de app het weet.

De oplossing is het behandelen van geschiktheid als iets wat opnieuw gecontroleerd moet worden, en niet alleen één keer goed gecontroleerd:

```
async function revalidateRosterBeforeKickoff(matchId) {
  const roster = await db.rosters.findOne({ matchId });
  const flagged = [];

  for (const playerId of roster.playerIds) {
    const eligible = await checkEligibility(playerId, matchId);
    if (!eligible) flagged.push(playerId);
  }

  if (flagged.length > 0) {
    await notifyTeamManager(matchId, flagged);
  }
}
```

Dit draait als een geplande controle een paar uur voor de aftrap, en afzonderlijk wanneer een schorsings- of transferrecord verandert nadat er al een opstelling is ingediend – zodat een laat binnenkomende tuchtuitspraak rechtstreeks aan de teammanager wordt gemeld, in plaats van voor het eerst naar boven te komen als een protest na de wedstrijd.

## Echt voorbeeld

### Een AI-native oprichter in actie: Een badge die daadwerkelijk niets tegenhield

Kaylee Smit, een oprichter in Breda, bouwde CompetitieBeheer – een beheersapp voor amateursportcompetities – met behulp van Cursor. De app handelde speelschema's, standen en spelersregistratie goed af, en bevatte een duidelijk zichtbare statusbadge voor schorsingen op het profiel van een speler. Wat het niet deed was het controleren van die schorsingsstatus wanneer een teammanager zijn wedstrijddag-opstelling bouwde. Het scherm van de opstellingsbouwer putte uit de volledige lijst met clubspelers zonder actieve schorsingen überhaupt te vergelijken.

Een teammanager, onbewust van het feit dat een speler een schorsing van één wedstrijd uitzat, voegde hem toe aan de wedstrijddag-selectie. Hij speelde de gehele wedstrijd. De tegenstander, bewust van de schorsing uit een eerdere tuchtmelding, diende na de wedstrijd een officieel protest in. De competitiecommissie beoordeelde de zaak en paste een automatische reglementaire nederlaag toe, wat het resultaat dat het team op het veld had gewonnen terugdraaide. Kaylee bracht CompetitieBeheer daarna naar LaunchStudio. Ingenieurs herbouwden de stroom voor het indienen van opstellingen om een live geschiktheidscontrole uit te voeren tegen schorsingsdata, transferstatus en leeftijdsgroepregels op het moment dat een speler wordt toegevoegd. De inzending wordt geblokkeerd met een specifieke reden als er een regel mislukt, in plaats van te vertrouwen op een passieve statusbadge.

**Resultaat:** CompetitieBeheer blokkeert nu ongeschikte spelers op het moment van het indienen van de opstelling in al haar pilot-competities. Geen enkele club die het bijgewerkte systeem gebruikt heeft sindsdien te maken gekregen met een reglementaire nederlaag vanwege een geschiktheidsfout.

> *"De badge stond recht op het scherm. Iedereen nam aan dat dat betekende dat het systeem ons beschermde. Dat deed het niet – het toonde ons gewoon informatie en vertrouwde erop dat een mens er elke keer correct naar zou handelen, wat natuurlijk uiteindelijk een keer niet gebeurde."*
> — **Kaylee Smit, Oprichter, CompetitieBeheer (Breda)**

**Kosten en tijdlijn:** € 480 (validatielogica voor geschiktheid van de opstelling over schorsings-, transfer- en leeftijdsgroepregels) — voltooid in 3 werkdagen.

---

## Veelgestelde vragen

### Waarom zou een app een schorsingsbadge tonen maar een geschorste speler toch laten toevoegen aan een opstelling?

Omdat het tonen van een status en het afdwingen van een regel twee afzonderlijke stukken logica zijn – een badge is een alleen-lezen weergavefunctie, terwijl het blokkeren van een inzending actieve validatielogica vereist op het exacte punt van die actie.

### Kan dit soort bug ook andere regeltypes dan schorsingen beïnvloeden?

Ja – dezelfde kloof verschijnt gebruikelijk bij transfervensters, geschiktheid voor leeftijdsgroepen en beperkingen voor registratie bij meerdere clubs, aangezien het allemaal regels zijn die live moeten worden gecontroleerd.

### Hoe vindt LaunchStudio dit soort verborgen bedrijfslogica-kloven?

LaunchStudio's ingenieurs, ondersteund door Manifera's ervaring bij meer dan 160 geleverde projecten, beoordelen de daadwerkelijke datastroom tussen uw database en uw gebruikersacties, en niet alleen de interface.

### Is dit het soort herstelling dat het herbouwen van mijn gehele app vereist?

Nee – het is doorgaans een gerichte backend-herstelling aan de specifieke actie (zoals het indienen van de opstelling) waar validatie ontbreekt, aangebracht op uw bestaande met Cursor gebouwde frontend zonder te veranderen hoe het eruitziet of voelt.

### Wat als er een schorsing wordt opgelegd nadat een opstelling al door de geschiktheidscontrole is gekomen?

Een eenmalige controle bij het indienen weerspiegelt alleen wat op dat moment waar was – een verdedigbaar systeem her-valideert opstellingen tegen elk geschiktheidsrecord dat daarna verandert, en opnieuw op een geplande controle dichter bij de aftrap.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom kan een geschorste speler toch op de opstelling opgesteld worden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een badge is alleen een visuele weergave; het daadwerkelijk blokkeren van een formulierinzending vereist aparte validatielogica op de backend."
      }
    },
    {
      "@type": "Question",
      "name": "Komt deze fout ook voor bij transfervensters of leeftijdsgrenzen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, exact hetzelfde probleem speelt bij transfertermijnen en leeftijdscategorieën als er niet live gevalideerd wordt."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe spoort LaunchStudio dit soort logische bugs op?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Door de datastromen tussen database en actieknoppen door te lichten, in plaats van alleen naar de UI-schermen te kijken."
      }
    },
    {
      "@type": "Question",
      "name": "Moet de hele app herbouwd worden voor deze geschiktheidscontrole?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, het is een gerichte backend-fix op de opstellingsinvoerserie; de UI verandert niet."
      }
    },
    {
      "@type": "Question",
      "name": "Wat als een schorsing pas wordt opgelegd nadat de opstelling ingediend is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een goed systeem voert een automatische hercontrole uit vlak voor de aftrap om laattijdige schorsingen direct te vlaggen."
      }
    }
  ]
}
</script>