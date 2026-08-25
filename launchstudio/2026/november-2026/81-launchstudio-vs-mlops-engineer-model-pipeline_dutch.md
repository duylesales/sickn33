---
Titel: "LaunchStudio vs. een ML Ops Engineer Inhuren: Wie Beheert uw Modelpipeline?"
Keywords: ML Ops Engineer, Modelpipeline, LaunchStudio vs ML Ops Engineer, AI Inference-infrastructuur, Modelmonitoring, LaunchStudio, Manifera
Buyer Stage: Decision
---

# LaunchStudio vs. een ML Ops Engineer Inhuren: Wie Beheert uw Modelpipeline?

Ergens in de tweede of derde maand nadat een AI-functie echt gebruik begint te genereren — een RAG-gestuurde zoekfunctie, een classificatiemodel dat leads scoort, een LLM-gebaseerde documentsamenvatter — komt elke oprichter tot dezelfde ongemakkelijke conclusie: niemand beheert eigenlijk de modelpipeline. De prompt die in week één perfect werkte, verslechtert stilletjes. Niemand houdt latency-percentielen van inference-aanroepen bij. Er is geen proces om een nieuwe modelversie te testen voordat deze de oude in productie vervangt. De instinctieve reactie is dan meestal om een fulltime ML Ops engineer aan te nemen — een specialist wiens taak het is om precies dit te beheren. Dat instinct is redelijk, maar vaak voorbarig, kostbaar en gericht op een probleem dat een engagement met een vast bereik sneller en tegen een fractie van de kosten oplost. LaunchStudio en een ML Ops engineer zijn geen uitwisselbare opties, en het verschil begrijpen is het verschil tussen een aanwerving van €90.000 per jaar die zes maanden te vroeg komt en een sprint van twee weken die dezelfde operationele stabiliteit koopt voor een tiende van de prijs.

## Waarvoor een ML Ops Engineer Eigenlijk Wordt Aangenomen

Een ML Ops engineer is een doorlopende operationele rol, geen eenmalige oplossing. Hun mandaat is om de volledige levenscyclus van modellen in productie te beheren: hertrainingsschema's, onderhoud van de feature store, experiment tracking, modelversiebeheer en rollback, drift-detectie over weken en maanden aan livegegevens, en de infrastructuurbeslissingen die bepalen of inference schaalt van 100 verzoeken per dag naar 100.000. Een goede ML Ops-aanwerving verdient zijn salaris door verslechtering op te vangen voordat deze zichtbaar wordt voor gebruikers — een model dat stilletjes nauwkeurigheid verliest naarmate de onderliggende datadistributie verschuift, een hertrainingstaak die drie weken lang stilletjes mislukt, een feature-pipeline die uit de pas raakt met waarop het model getraind is.

Waar een ML Ops engineer structureel niet voor is gebouwd, is een snelle, afgebakende reparatie van een specifieke, bekende reeks productiehiaten in een bestaande AI-functie die snel is opgezet met een AI-builder. Fulltime ML Ops-aanwervingen kosten in de meeste Europese markten volledig belast €70.000-€110.000 per jaar, verwachten een volwassen codebase en bestaande infrastructuur om binnen te opereren, en zijn — begrijpelijk — niet van plan hun eerste maand te besteden aan het herbouwen van een promptpipeline zonder retry-logica, zonder kostenplafond en zonder logging van wat het model daadwerkelijk teruggaf versus wat de gebruiker zag. Sommigen doen dat werk graag in de eerste weken van een rol. Maar het is zelden de beste besteding van een specialistensalaris, en het is zelden iets waarop een oprichter maanden kan wachten via recruitment voordat het hiaat überhaupt wordt aangepakt.

## Wat LaunchStudio Daadwerkelijk Verhardt in een Modelpipeline

LaunchStudio kent de tegenovergestelde vorm van engagement: een sprint met een vast bereik en focus op uitvoering die een bestaande, met een AI-builder gegenereerde modelpipeline doorlicht en de specifieke zaken verhardt die staan tussen "het werkt in de demo" en "het overleeft productieverkeer zonder stilletjes geld te kosten of verkeerde antwoorden te geven." Dat betekent gestructureerde logging toevoegen rond elke inference-aanroep, zodat u precies kunt zien welke prompt binnenkwam en wat eruit kwam, niet alleen of het verzoek slaagde. Het betekent een hard kostenplafond en rate limit rond API-aanroepen naar OpenAI, Anthropic of een zelf gehost model, zodat een oncontroleerbare lus of scraping-bot niet in één nacht kan uitmonden in een rekening van vijf cijfers. Het betekent het bouwen van een lichtgewicht evaluatiecontrole die automatisch draait vóór elke prompt- of modelversiewijziging wordt uitgerold, zodat regressies worden opgevangen voordat echte gebruikers ze zien. Het betekent retry-with-backoff en gracieuze degradatie toevoegen, zodat één time-out bij een upstream-API niet de hele functie laat crashen. En voor teams die al betekenisvol gebruik genereren, betekent het basale drift-monitoring — het bijhouden van outputkwaliteitsmetingen over tijd, zodat een stille verslechtering verschijnt als een dashboardwaarschuwing in plaats van als een supportticket van een boze klant drie weken later.

Er is geen doorlopend retainer, geen headcount, geen inwerkperiode van zes maanden. Een oprichter brengt de bestaande pipeline mee — welke combinatie dan ook van door Cursor opgezette backend-code, een Lovable-frontend die een API-route aanroept, of een Bolt-gebouwde app die rechtstreeks een extern model aanroept — en de engineers van LaunchStudio beoordelen deze, geven een vaste prijs en doorlooptijd in werkdagen op, en verhardt de specifieke gevonden hiaten, zonder de UI of de productlogica aan te raken die al werkt.

## Kosten en Doorlooptijd: De Cijfers Die Oprichters Daadwerkelijk Vergelijken

Een fulltime ML Ops engineer kost in de meeste West-Europese techmarkten €70.000-€110.000 aan basissalaris alleen al, nog los van de twee tot vier maanden aan recruitment, sollicitatiegesprekken en onboarding die het doorgaans kost om een gespecialiseerde rol als deze in te vullen — wat betekent dat een oprichter vaak kijkt naar €15.000-€25.000 aan recruitment- en inwerkkosten voordat de aanwerving ook maar één productiehiaat heeft opgelost, bovenop een jaarlijkse verplichting van zes cijfers. En die uitgave koopt een operationele eigenaar voor de lange termijn, geen vaste lijst met opgeloste hiaten op een bekende datum. Het is ook de moeite waard om eerlijk te zijn over hoe de eerste maand van een nieuwe ML Ops-aanwerving er in de praktijk doorgaans uitziet: het grootste deel gaat naar het lezen van de bestaande codebase, begrijpen wat er is gebouwd en waarom, en pas daarna beginnen met reparatie — wat betekent dat de daadwerkelijke fixes (retry-logica, kostenplafonds, evaluatiepoorten, drift-monitoring) vaak pas zes tot acht weken na de startdatum van de aanwerving landen, uitgaande van een zoektocht die zelf geen drie maanden in beslag nam.

De pakketten van LaunchStudio zijn vastgeprijsd en hebben een vast bereik: **Launch Ready** (€800-€1.500) voor een vroege AI-functie die basale kostencontroles en foutafhandeling nodig heeft voordat echte gebruikers ermee in aanraking komen, **Launch & Grow** (€1.500-€3.500) voor een modelpipeline die richting betekenisvol gebruik gaat en logging, retries en een evaluatiepoort nodig heeft, **Relaunch & Scale** (€2.500-€4.500) voor een pipeline die al onder echte belasting staat en drift-monitoring en inference-optimalisatie nodig heeft om dat te overleven, en **Enterprise Hardening** (€5.000-€7.500) voor een modelpipeline die richting een technische beoordeling van een enterprise-koper gaat, waar gedocumenteerde monitoring en rollback-procedures een harde vereiste zijn. Elk pakket wordt geleverd binnen 1 tot 3 weken. Een oprichter die de twee vergelijkt, vergelijkt vaak een jaarlijkse verplichting van zes cijfers met een aanwervingstraject van meerdere maanden tegenover een technische sprint van twee weken die precies de hiaten dicht die de pipeline vandaag risico laten lopen — en voor de meeste oprichters onder een bepaalde gebruiksdrempel zijn dat geen vervangers van elkaar, maar opeenvolgende behoeften.

## Het Echte Beslissingskader: Volume en Volwassenheid, Niet Voorkeur

De keuze tussen aannemen en verharden is niet echt een kwestie van smaak — het komt neer op hoeveel modelverkeer het product daadwerkelijk verwerkt en hoe cruciaal dat verkeer is voor het bedrijf, en de twee paden leiden naar verschillende vervolgvragen.

**Als het kernprobleem is "ik weet niet of mijn modelpipeline echt verkeer kan overleven zonder kapot te gaan of geld te verspillen,"** is dat een afgebakend, bekend engineeringprobleem — logging, kostenplafonds, retries, een evaluatiepoort — en dat wordt sneller en goedkoper beantwoord door een verhardingssprint dan door een maandenlange zoektocht naar een fulltime specialist die na aanvang nog steeds dezelfde fixes moet bepalen en bouwen.

**Als het kernprobleem is "ik heb iemand nodig die permanent hertrainingsschema's, een groeiende feature store en drift-detectie beheert voor een model dat honderdduizenden verzoeken per dag verwerkt,"** is dat een doorlopende operationele rol die geen enkele sprint met vast bereik kan vervangen, en een ML Ops engineer is dan het juiste instrument — maar die aanwerving is doorgaans waardevoller, en makkelijker te verantwoorden richting een investeerder, zodra de pipeline al een eerste echte productiebelasting heeft overleefd zonder dat er een eigenaar op toezag.

**Als beide tegelijk waar zijn** — een oprichter zes maanden na lancering met betekenisvol modelgebruik en een naderend Series A-gesprek waarin "wie beheert uw AI-infrastructuur" een voorspelbare vraag is — werkt in de praktijk de volgorde het beste van eerst verharden, dan aannemen: dicht de aantoonbare hiaten in 1-3 weken zodat de pipeline stopt met geld verliezen of verslechterde output leveren terwijl de zoektocht loopt, en haal daarna een fulltime ML Ops engineer binnen die een gedocumenteerde, gemonitorde basis erft in plaats van de eerste twee maanden te besteden aan het ontdekken van hetzelfde kostenplafond-hiaat dat een sprint met vast bereik al op dag één had gedicht.

## Waar de Twee Benaderingen Samenwerken

In de praktijk behalen oprichters de meeste waarde door LaunchStudio en een toekomstige ML Ops-aanwerving als opeenvolgend te behandelen, niet als concurrerend. Een ML Ops engineer die een door LaunchStudio verharde pipeline erft, begint vanaf een gedocumenteerde basis — bestaande logging, een bestaande evaluatiepoort, bestaande kostencontroles — in plaats van de eerste maand te besteden aan het reverse-engineeren van een ongedocumenteerde promptpipeline die tijdens laat avondlijke Cursor-sessies van een oprichter is gebouwd. Dat betekent dat meer van de kostbare tijd van een specialist naar het werkelijk moeilijke, doorlopende werk gaat: hertrainingsstrategie, feature-store-ontwerp en het drift-detectiewerk dat pas telt als er genoeg productiegeschiedenis is om drift tegen af te zetten. Omgekeerd kan een oprichter die al een ML Ops engineer heeft maar tegen een specifiek, afgebakend hiaat aanloopt — een enterprise-prospect vraagt net om een gedocumenteerde rollback-procedure, een kostenpiek heeft net een week aan runway opgegeten — een partner met een vast bereik inschakelen om dat ene hiaat snel te dichten, in plaats van een fulltime specialist van zijn roadmap te halen om een probleem te blussen dat een gerichte sprint in dagen oplost.

Eén bezwaar dat het waard is om direct te adresseren: sommige oprichters gaan ervan uit dat, omdat LaunchStudio werkt vanuit bestaande AI-builder-code in plaats van een pipeline vanaf nul te ontwerpen, de fixes oppervlakkig moeten zijn — pleisters in plaats van echte engineering. In de praktijk is vaak het tegenovergestelde waar. Omdat het bereik vast is en de pipeline al echte verkeerspatronen genereert, kan het engineeringteam direct instrumenteren wat daadwerkelijk kapotgaat onder belasting — de specifieke prompttemplates die kosten aandrijven, de specifieke faalmodi die in de foutlogboeken verschijnen — in plaats van weken te besteden aan het bouwen van generieke infrastructuur voor verkeer dat nog niet bestaat. Een volledige herbouw optimaliseert voor een toekomst die de pipeline mogelijk nooit bereikt; een verhardingssprint optimaliseert voor het verkeerspatroon dat al plaatsvindt.

## Belangrijkste Inzichten

- Een ML Ops engineer is een doorlopende operationele aanwerving — hertraining, drift-detectie, onderhoud van de feature store — terwijl LaunchStudio een engagement met vast bereik is dat de logging, kostencontroles, retries en evaluatiepoorten van een bestaande, met een AI-builder gebouwde modelpipeline verhardt.

- Een fulltime ML Ops-aanwerving kost doorgaans €70.000-€110.000 per jaar plus twee tot vier maanden aan recruitment en inwerkperiode, wat betekent dat de daadwerkelijke fixes die een oprichter vandaag nodig heeft vaak pas zes tot acht weken na aanvang van de aanwerving landen.

- De vaste pakketten van LaunchStudio (€800-€7.500) dichten de specifieke hiaten — ontbrekende kostenplafonds, geen retry-logica, geen evaluatiepoort, geen zicht op drift — die een modelpipeline risico laten lopen, geleverd binnen 1 tot 3 weken zonder verplichting tot headcount.

- De juiste volgorde voor een oprichter die zowel een niet-verharde pipeline heeft als geen toegewezen eigenaar, is doorgaans eerst verharden, dan aannemen: repareer wat aantoonbaar kapot is, en breng daarna een specialist binnen die een gedocumenteerde, gemonitorde basis erft.

- De twee benaderingen zijn complementair: een ML Ops engineer die een door LaunchStudio verharde pipeline erft, besteedt zijn tijd aan hertrainingsstrategie en langetermijninfrastructuur in plaats van hiaten te herontdekken die een gerichte sprint al had gedicht.

## Stop met Gissen wie uw Modelpipeline Beheert

Als uw AI-functie echt gebruik genereert en niemand kan u vertellen wat er gebeurt als de inference-API vastloopt of de kosten 's nachts pieken, is dat geen aanwervingsprobleem van zes maanden — het is een technisch probleem van twee weken met een vaste prijs.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 en geleid door Oprichter & Managing Director **Herre Roelevink**. Zoals Roelevink het verwoordt: *"We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot wasdom te brengen. Wij hebben elf jaar ervaring in precies dat vakgebied."* Door "Nederlands management te combineren met Vietnamees meesterschap", onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420), een Aziatische hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minh-stad, Vietnam** (Pho Quang Street), met enterprise-klanten waaronder Vodafone en TNO. Via LaunchStudio beoordelen senior engineeringteams uw bestaande, met een AI-builder gebouwde modelpipeline, bepalen ze een verhardingssprint met vaste prijs voor logging, kostencontroles, retries en evaluatiepoorten, en veranderen ze deze binnen 1 tot 3 weken in een productieklare pipeline — een basis waarop elke ML Ops engineer die u later aanneemt met vertrouwen kan voortbouwen. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact) of bekijk hoe het [maatwerk software-ontwikkelteam van Manifera](https://www.manifera.com/services/custom-software-development/) production-hardening aanpakt voor AI-gegenereerde codebases.

## Echt voorbeeld

### Een AI-native oprichter in actie: Een vacature die vier maanden openstond

Niklas Berger, oprichter van ClauseCheck, een SaaS voor contractbeoordeling die hij met **Cursor** bouwde bovenop een RAG-pipeline die GPT-4 raadpleegde voor clausule-risicoanalyse, plaatste een vacature voor ML Ops engineer nadat het gebruik van een zakelijke klant zijn API-kosten in één week verdrievoudigde, zonder waarschuwing om dit op te vangen. De vacature stond vier maanden open — sterke kandidaten wilden aandelen die hij in zijn fase niet kon bieden, en twee sollicitatierondes liepen spaak. Ondertussen had de inference-pipeline van ClauseCheck geen retry-logica, waardoor één time-out bij OpenAI een volledige contractbeoordeling stilletjes liet mislukken zonder foutmelding aan de gebruiker, en er bestond geen evaluatiepoort om te voorkomen dat een wijziging in het prompttemplate de clausuledetectienauwkeurigheid stilletjes zou verslechteren.

Niklas haalde LaunchStudio erbij om het hiaat te dichten dat de openstaande vacature op zijn eigen tijdlijn nooit zou dichten. Het engineeringteam beoordeelde de bestaande, met Cursor gebouwde pipeline van ClauseCheck, voegde een hard maandelijks kostenplafond toe met Slack-waarschuwingen bij 80% van het budget, implementeerde retry-with-backoff en gracieuze degradatie bij elke OpenAI-aanroep, bouwde een evaluatiesuite van 40 testgevallen die automatisch draait vóór elke promptwijziging wordt uitgerold, en voegde gestructureerde logging toe die elke inference-input en -output vastlegt voor debugging- en auditdoeleinden — allemaal zonder het beoordelingsdashboard aan te raken dat zijn klanten dagelijks gebruikten.

**Resultaat:** ClauseCheck ving en verwierp de volgende maand twee regressies in prompttemplates via de nieuwe evaluatiepoort voordat een van beide productie bereikte, en Niklas hield de ML Ops-vacature open met lagere urgentie, waarbij hij deze vijf maanden later invulde met een kandidaat die een gedocumenteerde, gemonitorde pipeline erfde in plaats van een ongedocumenteerde.

**Kosten & Doorlooptijd:** € 2.600 (Launch & Grow Pakket) — productieklaar en uitgerold in 10 werkdagen.

---

---

---
## Veelgestelde Vragen

### Moet ik een ML Ops engineer aannemen of een verhardingsdienst zoals LaunchStudio gebruiken?

Dat hangt af van de volwassenheid en het volume van uw modelpipeline. Als u niet weet of uw pipeline echt verkeer kan overleven zonder kapot te gaan of te veel uit te geven aan inference-kosten, is dat een afgebakend uitvoeringsprobleem dat het beste wordt opgelost door een verhardingssprint met vast bereik. Als u een doorlopende eigenaar nodig heeft voor hertrainingsschema's, feature stores en drift-detectie op betekenisvolle schaal, is dat een operationele rol die het beste wordt ingevuld door een fulltime ML Ops engineer. De meeste oprichters hebben uiteindelijk beide nodig, meestal in die volgorde.

### Kan LaunchStudio drift-detectie en kostenoverschrijdingen in mijn bestaande modelpipeline oplossen?

Ja. De engineers van LaunchStudio werken rechtstreeks met uw bestaande, met een AI-builder gegenereerde pipeline — of dat nu een door Cursor opgezette backend is, een Lovable-frontend of een Bolt-app die een model-API aanroept — en voegen gestructureerde logging, kostenplafonds met waarschuwingen, retry-logica, evaluatiepoorten en, voor pipelines met voldoende gebruiksgeschiedenis, drift-monitoring toe, allemaal zonder de productlogica die al werkt opnieuw te bouwen.

### Hoeveel kost een ML Ops engineer vergeleken met LaunchStudio?

Een fulltime ML Ops engineer kost doorgaans €70.000-€110.000 per jaar aan basissalaris, plus twee tot vier maanden aan recruitment en inwerkperiode voordat hiaten worden gedicht. De vaste pakketten van LaunchStudio variëren van €800 tot €7.500 afhankelijk van de omvang, geleverd binnen 1 tot 3 weken, omdat het engagement zich richt op een bekende, afgebakende lijst met pipelinehiaten in plaats van een doorlopende operationele rol.

### Als ik al een ML Ops engineer heb, is een LaunchStudio-sprint dan nog steeds nuttig?

Vaak wel — het inschakelen van een partner met een vast bereik om een specifiek, bekend hiaat te dichten (een kostenpiek, een documentatieverzoek van een enterprise-prospect, een rollback-procedure die nog niet bestaat) laat uw ML Ops engineer gericht blijven op hertrainingsstrategie en langetermijninfrastructuur, in plaats van betrokken te raken bij een probleem dat een gerichte sprint sneller oplost.

### Wat is de juiste volgorde: eerst verharden of eerst aannemen?

Voor de meeste oprichters die zowel een niet-verharde pipeline hebben als geen toegewezen eigenaar, is eerst verharden de kapitaalefficiëntere volgorde. Het dichten van de aantoonbare hiaten in 1-3 weken voorkomt dat de pipeline geld verliest of verslechterde output levert terwijl een zoektocht naar een specialist loopt, en het geeft wie u uiteindelijk aanneemt een gedocumenteerde, gemonitorde basis om op voort te bouwen in plaats van een ongedocumenteerde om te reverse-engineeren.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik een ML Ops engineer aannemen of een verhardingsdienst zoals LaunchStudio gebruiken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dat hangt af van de volwassenheid en het volume van uw modelpipeline. Als u niet weet of uw pipeline echt verkeer kan overleven zonder kapot te gaan of te veel uit te geven aan inference-kosten, is dat een afgebakend uitvoeringsprobleem dat het beste wordt opgelost door een verhardingssprint met vast bereik. Als u een doorlopende eigenaar nodig heeft voor hertrainingsschema's, feature stores en drift-detectie op betekenisvolle schaal, is dat een operationele rol die het beste wordt ingevuld door een fulltime ML Ops engineer. De meeste oprichters hebben uiteindelijk beide nodig, meestal in die volgorde."
      }
    },
    {
      "@type": "Question",
      "name": "Kan LaunchStudio drift-detectie en kostenoverschrijdingen in mijn bestaande modelpipeline oplossen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. De engineers van LaunchStudio werken rechtstreeks met uw bestaande, met een AI-builder gegenereerde pipeline — of dat nu een door Cursor opgezette backend is, een Lovable-frontend of een Bolt-app die een model-API aanroept — en voegen gestructureerde logging, kostenplafonds met waarschuwingen, retry-logica, evaluatiepoorten en, voor pipelines met voldoende gebruiksgeschiedenis, drift-monitoring toe, allemaal zonder de productlogica die al werkt opnieuw te bouwen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoeveel kost een ML Ops engineer vergeleken met LaunchStudio?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een fulltime ML Ops engineer kost doorgaans €70.000-€110.000 per jaar aan basissalaris, plus twee tot vier maanden aan recruitment en inwerkperiode voordat hiaten worden gedicht. De vaste pakketten van LaunchStudio variëren van €800 tot €7.500 afhankelijk van de omvang, geleverd binnen 1 tot 3 weken, omdat het engagement zich richt op een bekende, afgebakende lijst met pipelinehiaten in plaats van een doorlopende operationele rol."
      }
    },
    {
      "@type": "Question",
      "name": "Als ik al een ML Ops engineer heb, is een LaunchStudio-sprint dan nog steeds nuttig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vaak wel — het inschakelen van een partner met een vast bereik om een specifiek, bekend hiaat te dichten (een kostenpiek, een documentatieverzoek van een enterprise-prospect, een rollback-procedure die nog niet bestaat) laat uw ML Ops engineer gericht blijven op hertrainingsstrategie en langetermijninfrastructuur, in plaats van betrokken te raken bij een probleem dat een gerichte sprint sneller oplost."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de juiste volgorde: eerst verharden of eerst aannemen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor de meeste oprichters die zowel een niet-verharde pipeline hebben als geen toegewezen eigenaar, is eerst verharden de kapitaalefficiëntere volgorde. Het dichten van de aantoonbare hiaten in 1-3 weken voorkomt dat de pipeline geld verliest of verslechterde output levert terwijl een zoektocht naar een specialist loopt, en het geeft wie u uiteindelijk aanneemt een gedocumenteerde, gemonitorde basis om op voort te bouwen in plaats van een ongedocumenteerde om te reverse-engineeren."
      }
    }
  ]
}
</script>
