---
Titel: "De Enterprise CFO-pitch: Zelf de Business Case Bouwen voor AI-infrastructuuruitgaven vs. Hulp Inhuren"
Keywords: AI-infrastructuuruitgaven, CFO Business Case, AI-infrastructuurbudget, Enterprise AI-investering, Build vs Buy AI-infrastructuur, LaunchStudio, Manifera
Buyer Stage: Decision
---

# De Enterprise CFO-pitch: Zelf de Business Case Bouwen voor AI-infrastructuuruitgaven vs. Hulp Inhuren

Goedkeuring krijgen voor engineeringtijd om "onzichtbare" infrastructuur te repareren is een van de moeilijkste pitches binnen een AI SaaS-bedrijf, omdat de CFO niet naar een productdemo kijkt — ze kijken naar een spreadsheet, en infrastructuurverharding verschijnt niet als een nieuwe knop waar gebruikers op kunnen klikken. Dit is het verhaal van Elena, een oprichter wier platform technisch werkte maar structureel kwetsbaar was, en die een business case moest bouwen voor infrastructuuruitgaven die een cijfergerichte CFO daadwerkelijk zou goedkeuren — eerst door te proberen die case zelf te bouwen, daarna door LaunchStudio in te schakelen om hem waterdicht te maken.

## De pitch die stierf in de vergaderzaal

Elena's bedrijf had met Lovable een platform voor documentautomatisering gebouwd voor verzekeringsmakelaars in het middensegment, en het had echte product-market fit — 40 betalende klanten, gestage groei maand op maand, en een board die tevreden was met wat ze in de demo zagen. Maar onder de UI werd de infrastructuur bijeengehouden door beslissingen die voor snelheid waren genomen, niet voor schaal: geen read replica's, minimale caching, synchrone LLM-aanroepen die de hoofdverzoekthread blokkeerden, en een databaseschema dat sinds het eerste prototype niet meer was aangeraakt.

Elena wist dat dit een probleem was. Ze vroeg haar board om €35.000 en zes weken engineeringtijd om "de infrastructuur te verharden." De pitch kwam nergens. Haar CFO — zes maanden eerder aangenomen specifiek om financiële discipline in het bedrijf te brengen — stelde een terechte vraag: "Wat is de ROI? Wat breekt er als we dit niet doen, en wanneer?" Elena had geen precies antwoord. Ze had een gevoel, onderbouwd door een paar Slack-berichten van een overbelaste engineer, geen business case. Het verzoek werd terzijde geschoven.

## Waarom "het is riskant" het niet overleeft in een gesprek met een CFO

Hier gaan de meeste pitches voor infrastructuuruitgaven mis, en dat komt niet doordat het onderliggende risico ingebeeld is — het komt doordat engineeringrisico en financieel risico in verschillende talen worden uitgedrukt, en niemand vertaalt daartussen. Een CFO die een verzoek van €35.000 aan engineeringtijd beoordeelt, hanteert hetzelfde mentale model als bij elke andere uitgave: wat kost dit, wat voorkomt of ontsluit het, en wat is de terugverdientijd. "De infrastructuur is kwetsbaar" beantwoordt geen van die drie vragen.

Elena's eerste poging om de case zelf te bouwen liep tegen drie specifieke hiaten aan die elke oprichter die dit alleen probeert vaak tegenkomt:

- **Geen gekwantificeerde faalkost.** Ze kon databasevergrendelingen en trage query's kwalitatief beschrijven, maar kon geen getal plakken op wat een storing of een incident met verminderde prestaties daadwerkelijk kostte aan afgehaakte klanten, gemiste SLA's of supporturen — het soort getal dat een CFO nodig heeft om tegen het verzoek af te wegen.

- **Geen geprioriteerde scope.** Het oorspronkelijke verzoek bundelde een dozijn infrastructuurverbeteringen in één bedrag van €35.000 zonder rangschikking, waardoor het eruitzag als een alles-of-niets-gok in plaats van een reeks investeringen met elk hun eigen terugverdientijd.

- **Geen vergelijkingspunt.** Zonder een benchmark voor wat "productieklare infrastructuur" doorgaans kost in de fase waarin haar bedrijf zich bevindt, had de CFO geen manier om te beoordelen of €35.000 redelijk, opgeblazen, of juist onderschat was gezien het betrokken risico.

## De case bouwen die daadwerkelijk wordt goedgekeurd

Elena schakelde LaunchStudio in, niet in eerste instantie om de infrastructuur al te repareren, maar om te helpen een business case te bouwen die een CFO zou goedkeuren — waarbij de pitch zelf werd behandeld als een engineeringprobleem met een correct antwoord, niet als een overtuigingsoefening. De herbouwde pitch had vier onderdelen die een puur interne, niet-technische business case bijna nooit bevat.

**1. Een gekwantificeerd risicoregister, geen vage waarschuwing.** In plaats van "de database zou problemen kunnen hebben" leverde de audit specifieke, gedateerde bevindingen op: bij het huidige groeitempo zou de primaire database naar verwachting binnen 9-14 weken uitputting van de connection pool bereiken op basis van de huidige querypatronen, en niet-geïndexeerde query's op de dataset van de grootste klant veroorzaakten al periodiek laadtijden van 4-6 seconden, wat supporttickets bevestigden dat het frustratie veroorzaakte. Elk risico was gekoppeld aan een geschatte kostprijs in dollars — supporturen, MRR die risico liep bij de meest kwetsbare klanten, en de kostprijs van een noodreparatie onder storingsdruk versus een geplande.

**2. Een gefaseerd voorstel in plaats van één totaalbedrag.** Het engineeringwerk werd opgesplitst in drie fasen: een "nu-repareren"-fase die de problemen met connection pool en query's aanpakte die al voor klantzichtbare pijn zorgden, een "repareren vóór het volgende groeimijlpaal"-fase die caching en replica-opzet aanpakte die nodig was vóór de volgende 50 klanten, en een "monitoren en herbeoordelen"-fase voor verbeteringen met een langere terugverdientijd. Hierdoor kon de CFO de uitgave met de hoogste zekerheid en urgentie direct goedkeuren zonder op het volledige pakket ineens te hoeven wedden.

**3. Een vergelijking van de kosten van niets doen.** De engineers van LaunchStudio modelleerden wat een ongeplande productie-incident bij Elena's huidige schaal waarschijnlijk zou kosten versus de geplande reparatie — rekening houdend met noodtarieven van contractanten, de reputatieschade van downtime bij klanten in de verzekeringssector die hun eigen compliance-verplichtingen hebben, en de engineeringuren die tijdens een crisis van de roadmap werden afgeleid. De geplande infrastructuuruitgave kwam uit op ongeveer een derde van de geprojecteerde kosten van een ongeplande storing van vergelijkbare ernst.

**4. Een marktconforme benchmark.** Omdat LaunchStudio met veel AI SaaS-bedrijven in vergelijkbare fasen werkt, konden ze Elena's CFO vertellen wat vergelijkbare infrastructuurverharding doorgaans kost als percentage van de ARR bij een bedrijf van haar omvang — waardoor "is €35.000 redelijk?" veranderde van een gok in een vergelijking met een bekende bandbreedte.

## De pitch, ronde twee

Elena ging terug naar haar board en CFO met een business case die op deze manier was opgebouwd, geframed rond risicogecorrigeerde kosten in plaats van engineering-ongemak. Het herziene verzoek was kleiner voor de directe fase — €18.500 voor de nu-repareren-items — met de resterende twee fasen gepland tegen specifieke groeitriggers in plaats van in één keer goedgekeurd. De CFO keurde de eerste fase binnen dezelfde vergadering goed.

Wat veranderde was niet de onderliggende technische noodzaak — de database was precies zo kwetsbaar als de eerste keer dat Elena het aankaartte. Wat veranderde was dat de pitch nu de drie vragen beantwoordde die elke CFO daadwerkelijk stelt: wat kost dit, wat voorkomt het, en wat is de tijdlijn. Het gekwantificeerde risicoregister, de gefaseerde scope en de vergelijking van de kosten van niets doen deden het vertaalwerk dat "het is riskant" nooit kon doen.

## Het bezwaar dat Elena voorzag: "Leidt fasering er niet toe dat de latere fasen alsnog worden afgewezen?"

Elena bracht deze zorg zelf naar voren vóór de tweede pitch, en het is het meest voorkomende tegenargument dat oprichters bij deze aanpak tegenkomen: als je alleen om de "nu-repareren"-fase vraagt, loop je dan niet het risico dat de CFO de goedkope, urgente reparatie goedkeurt en de rest stilletjes voor onbepaalde tijd op de plank legt, waardoor de onderliggende kwetsbaarheid maar gedeeltelijk wordt aangepakt?

Het antwoord dat LaunchStudio in de pitch inbouwde, was om de tweede en derde fase te koppelen aan specifieke, meetbare groeitriggers in plaats van aan een toekomstige datum op een roadmap-slide — "vóór de volgende 50 klanten instromen" of "vóór het maandelijkse actieve documentvolume de 20.000 overschrijdt" in plaats van "in Q3." Een trigger die is gekoppeld aan een bedrijfsmetriek die de CFO al bijhoudt, is veel moeilijker voor onbepaalde tijd uit te stellen dan een datum, omdat het de uitgave voor de latere fase omzet van een discretionair toekomstig verzoek in een vooraf overeengekomen gevolg van de eigen groei van het bedrijf. In Elena's geval werd de tweede fase — caching en replica-opzet — in principe al goedgekeurd tijdens dezelfde vergadering, alleen afhankelijk van het bereiken van de klantaantal-trigger, waardoor geen tweede pitchvergadering nodig was toen dat mijlpaal acht weken later werd bereikt.

## De diepere les: Infrastructuuruitgaven zijn een financiële beslissing, niet alleen een technische

Oprichters die ook de leidende engineer zijn, gaan er vaak van uit dat het moeilijkste onderdeel van het goedgekeurd krijgen van infrastructuuruitgaven de technische beoordeling is — weten wat er kapot is en wat er nodig is om het te repareren. Elena's ervaring laat zien dat het moeilijkste onderdeel meestal de vertaling is: het omzetten van een engineeringrisico in een financieel risico dat een CFO, die zijn werk correct doet door om cijfers te vragen, daadwerkelijk kan evalueren en goedkeuren.

Dit is ook waar het "doe-het-zelf"-pad oprichters de meeste tijd kost. Elena besteedde bijna drie weken aan het alleen proberen te construeren van een geloofwaardige business case vóór de tweede pitch, waarbij ze informele kostenschattingen en storingsscenario's samenbracht zonder de benchmarkdata of gestructureerde risicomodellering die de uiteindelijke versie deed slagen. Een extern team dat deze analyse regelmatig uitvoert, kan dat vertaalwerk comprimeren tot dagen in plaats van weken, precies omdat ze al vele malen eerder dit soort case hebben gebouwd, voor datzelfde soort infrastructuurrisico.

## Belangrijkste inzichten

- Een CFO die een verzoek om infrastructuuruitgaven beoordeelt, heeft dezelfde drie antwoorden nodig als bij elke andere uitgavenbeslissing: wat kost het, wat voorkomt of ontsluit het, en wat is de terugverdientijd — vage beschrijvingen van technisch risico beantwoorden geen van die vragen.

- Het kwantificeren van de kosten van niets doen — supporturen, omzet die risico loopt, premies voor noodreparaties — verandert "dit is riskant" in een getal dat een CFO direct kan afwegen tegen de gevraagde uitgave.

- Het faseren van een infrastructuurvoorstel op urgentie stelt een CFO in staat de uitgave met de hoogste zekerheid direct goed te keuren, in plaats van een alles-of-niets-pakket te moeten beoordelen.

- Marktconforme benchmarking geeft een CFO een vergelijkingspunt om te beoordelen of een voorgestelde uitgave redelijk is, in plaats van te moeten gokken bij gebrek aan enige referentie.

- Externe hulp inschakelen om de business case te bouwen — zoals Elena deed met LaunchStudio (ondersteund door de 11+ jaar ervaring in production engineering van Manifera, vertrouwd door enterprise-klanten zoals Vodafone en TNO) — leidt vaak tot snellere goedkeuring van infrastructuuruitgaven dan de case alleen bouwen, omdat de vertaling van engineeringrisico naar financieel risico zelf een gespecialiseerde vaardigheid is.

## Krijg een infrastructuur-business case die uw CFO daadwerkelijk goedkeurt

Als uw pitch voor infrastructuuruitgaven steeds vastloopt in de boardroom, ligt het probleem vaak bij de case, niet bij de noodzaak — en dat is oplosbaar in dagen, niet maanden.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 en geleid door Oprichter & Managing Director **Herre Roelevink**. Zoals Roelevink het verwoordt: *"We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot wasdom te brengen. Wij hebben elf jaar ervaring in precies dat vakgebied."* Door "Nederlands management te combineren met Vietnamees meesterschap", onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420), een Aziatische hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minh-stad, Vietnam** (Pho Quang Street). Via LaunchStudio nemen senior engineeringteams uw bestaande door AI gebouwde frontend en implementeren ze productieklare beveiligingscontroles, live betalingsgateways, veilige hosting en monitoring — waardoor uw prototype binnen 1 tot 3 weken verandert in een veilige, compliant MVP, zonder dat een volledige rebuild nodig is. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact) of bekijk hoe het [maatwerk software-ontwikkelteam van Manifera](https://www.manifera.com/services/custom-software-development/) production-hardening aanpakt voor AI-gegenereerde codebases.

## Echt voorbeeld

### Een AI-native oprichter in actie: Zorgintake-automatisering

Lucas, een startup-oprichter, gebruikte **Bolt** om een AI-gestuurd platform voor patiëntintake-automatisering te bouwen voor kleine zorgklinieken. Toen hij intern een infrastructuurbudget van €50.000 probeerde te verkrijgen ter voorbereiding op een pilot met een ziekenhuisnetwerk, wees zijn nieuw aangenomen financieel verantwoordelijke het verzoek af wegens gebrek aan enige gekwantificeerde onderbouwing, waardoor de pilot — en de bijbehorende omzet — het risico liep de startdatum te missen.

Lucas werkte samen met **LaunchStudio (door Manifera)** om de pitch opnieuw op te bouwen. Het team produceerde een gekwantificeerd risicoregister gekoppeld aan de specifieke compliance- en uptime-vereisten van de ziekenhuispilot, faseerde de uitgave in een direct compliance-kritieke fase en een langetermijn-schaalfase, en benchmarkte de kosten tegen vergelijkbare infrastructuuruitgaven in de zorg-SaaS.

**Resultaat:** Lucas' financieel verantwoordelijke keurde het budget voor de eerste fase binnen een week goed, en de ziekenhuispilot ging op schema van start met de compliance-kritieke infrastructuur al op zijn plek.

**Kosten & Doorlooptijd:** € 2.400 (Launch & Grow Pakket) — business case en eerste-fase-implementatie geleverd in 10 werkdagen.

---

---

---
## Veelgestelde Vragen

### Waarom worden verzoeken om infrastructuuruitgaven afgewezen, zelfs als het onderliggende risico reëel is?

Omdat engineeringrisico en financieel risico in verschillende talen worden beschreven. Een vage waarschuwing zoals "de infrastructuur is kwetsbaar" beantwoordt niet de drie vragen die een CFO beantwoord wil zien: wat kost de reparatie, wat voorkomt het, en wat is de terugverdientijd. Zonder die vertaling leest zelfs een reëel risico als een ongekwantificeerd verzoek.

### Hoe zet je een geldbedrag op een infrastructuurrisico dat nog niet is gebeurd?

Door specifieke technische bevindingen te koppelen aan meetbare bedrijfsconsequenties — supporturen die al worden besteed aan prestatieklachten, MRR die risico loopt bij de meest kwetsbare klanten, en de kostenpremie van een noodreparatie onder storingsdruk versus een geplande. Elena's case modelleerde de kosten van een waarschijnlijk ongepland incident tegen de kosten van de geplande reparatie, wat uitkwam op ongeveer een derde daarvan.

### Moet een infrastructuurvoorstel één totaalbedrag zijn of gefaseerd?

Gefaseerd, waar mogelijk. Het bundelen van elke verbetering in één bedrag dwingt een CFO tot een alles-of-niets-beslissing. Door het werk op te splitsen in een "nu-repareren"-fase, een "repareren-vóór-het-volgende-groeimijlpaal"-fase en een "monitoren-en-herbeoordelen"-fase kan de uitgave met de hoogste zekerheid en urgentie direct worden goedgekeurd.

### Kan een oprichter deze business case alleen bouwen, of is externe hulp nodig?

Een technische oprichter kan de onderliggende risicobeoordeling absoluut zelf doen. Waar oprichters de meeste tijd verliezen, is de vertaling naar financiële termen en de marktconforme benchmarking, aangezien dat vereist dat je vergelijkbaar infrastructuurwerk bij veel andere bedrijven hebt gebouwd en geprijsd — daarom comprimeert het inschakelen van externe hulp, zoals Elena deed, vaak weken pitchwerk tot dagen.

### Wat veranderde LaunchStudio daadwerkelijk aan Elena's oorspronkelijke pitch?

Ze voegden een gekwantificeerd, gedateerd risicoregister toe in plaats van een kwalitatieve waarschuwing, splitsten één verzoek van €35.000 op in drie geprioriteerde fasen, modelleerden de kosten van niets doen tegen de kosten van de geplande reparatie, en benchmarkten de uitgave tegen marktconforme tarieven voor vergelijkbare bedrijven — waardoor een pitch die vastliep, binnen dezelfde vergadering werd goedgekeurd.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom worden verzoeken om infrastructuuruitgaven afgewezen, zelfs als het onderliggende risico reëel is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat engineeringrisico en financieel risico in verschillende talen worden beschreven. Een vage waarschuwing zoals \"de infrastructuur is kwetsbaar\" beantwoordt niet de drie vragen die een CFO beantwoord wil zien: wat kost de reparatie, wat voorkomt het, en wat is de terugverdientijd. Zonder die vertaling leest zelfs een reëel risico als een ongekwantificeerd verzoek."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe zet je een geldbedrag op een infrastructuurrisico dat nog niet is gebeurd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Door specifieke technische bevindingen te koppelen aan meetbare bedrijfsconsequenties — supporturen die al worden besteed aan prestatieklachten, MRR die risico loopt bij de meest kwetsbare klanten, en de kostenpremie van een noodreparatie onder storingsdruk versus een geplande. Elena's case modelleerde de kosten van een waarschijnlijk ongepland incident tegen de kosten van de geplande reparatie, wat uitkwam op ongeveer een derde daarvan."
      }
    },
    {
      "@type": "Question",
      "name": "Moet een infrastructuurvoorstel één totaalbedrag zijn of gefaseerd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Gefaseerd, waar mogelijk. Het bundelen van elke verbetering in één bedrag dwingt een CFO tot een alles-of-niets-beslissing. Door het werk op te splitsen in een \"nu-repareren\"-fase, een \"repareren-vóór-het-volgende-groeimijlpaal\"-fase en een \"monitoren-en-herbeoordelen\"-fase kan de uitgave met de hoogste zekerheid en urgentie direct worden goedgekeurd."
      }
    },
    {
      "@type": "Question",
      "name": "Kan een oprichter deze business case alleen bouwen, of is externe hulp nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een technische oprichter kan de onderliggende risicobeoordeling absoluut zelf doen. Waar oprichters de meeste tijd verliezen, is de vertaling naar financiële termen en de marktconforme benchmarking, aangezien dat vereist dat je vergelijkbaar infrastructuurwerk bij veel andere bedrijven hebt gebouwd en geprijsd — daarom comprimeert het inschakelen van externe hulp, zoals Elena deed, vaak weken pitchwerk tot dagen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat veranderde LaunchStudio daadwerkelijk aan Elena's oorspronkelijke pitch?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ze voegden een gekwantificeerd, gedateerd risicoregister toe in plaats van een kwalitatieve waarschuwing, splitsten één verzoek van €35.000 op in drie geprioriteerde fasen, modelleerden de kosten van niets doen tegen de kosten van de geplande reparatie, en benchmarkten de uitgave tegen marktconforme tarieven voor vergelijkbare bedrijven — waardoor een pitch die vastliep, binnen dezelfde vergadering werd goedgekeurd."
      }
    }
  ]
}
</script>
