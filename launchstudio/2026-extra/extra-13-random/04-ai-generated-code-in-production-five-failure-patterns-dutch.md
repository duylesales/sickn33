---
Titel: "AI-gegenereerde code in productie: Vijf foutpatronen uit echte logs"
Trefwoorden: ai gegenereerde code in productie, ai-code in productie, ai-gegenereerde code, productiefouten, ai code bugs, windsurf, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelgroep: Technische Solo-oprichter / Indie Hacker
---

# AI-gegenereerde code in productie: Vijf foutpatronen uit echte logs

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-gegenereerde code in productie: Vijf foutpatronen uit echte logs",
  "description": "De vijf foutpatronen die het vaakst opduiken wanneer AI-gegenereerde code in productie draait: stille catches, optimistische time-outs, onbegrensde queries, klok-aannames en retry-stormen. Hoe ze eruitzien in logs en hoe je ze oplost.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-04",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-generated-code-in-production-five-failure-patterns" }
}
</script>

De meeste artikelen over AI-gegenereerde code in productie richten zich op beveiligingslekken. Die zijn uiteraard belangrijk, en we schrijven er regelmatig over. Maar wanneer de engineers van LaunchStudio de logs analyseren van met AI gebouwde applicaties die al live staan, zijn de meest voorkomende problemen geen hacks of inbraken. Het zijn betrouwbaarheidsproblemen — code die feilloos werkt tijdens een demo, maar op subtiele, specifieke manieren degradeert zodra er sprake is van echt dataverkeer, wankele netwerken en echte tijdzones.

Hier zijn de vijf patronen die we keer op keer tegenkomen, hoe ze eruitzien wanneer je eindelijk in de logs duikt, en hoe de oplossing er in de praktijk uitziet.

## Patroon 1: De stille catch (The Silent Catch)

**Hoe het eruitziet in de code:** een `try`-blok rondom een API-aanroep of databaseschrijfopdracht, met een `catch` die enkel logt naar de console of helemaal niets doet. AI-assistenten genereren dit aan de lopende band omdat de code hierdoor "niet crasht", wat voldoet aan de opdracht in de prompt.

**Hoe het zich uit in productie:** niets. En dat is precies het probleem. Een klant verstuurt een formulier, het opslaan mislukt, de fout wordt stilzwijgend genegeerd en de interface toont doodleuk een succesmelding. Dagen later vraagt iemand zich af waarom zijn bestelling nooit is aangekomen.

**Hoe het eruitziet in de logs:** meestal als een leegte. Geen foutmelding, geen waarschuwing, simpelweg een ontbrekend record waar data had moeten staan. Als er al een logregel is, betreft het een `console.error(e)` in een serverless functie waarvan de logs na 24 uur verlopen.

**De oplossing:** fouten die data beïnvloeden moeten betekenisvol worden afgehandeld (een retry, een alternatief pad, een duidelijke melding aan de gebruiker) of worden doorgestuurd naar een error-tracking tool. Een uitstekende vuistregel: elk `catch`-blok doet iets nuttigs óf rapporteert naar een dienst zoals Sentry. Nooit geen van beide.

## Patroon 2: De optimistische time-out

**Hoe het eruitziet in de code:** uitgaande API-aanroepen naar e-maildiensten, betalingsproviders, AI-modellen of geocoding-services zonder geconfigureerde time-out, of met de standaardinstelling van de library — die soms oneindig is.

**Hoe het zich uit in productie:** zodra een externe dienst vertraging oploopt, vertraagt jouw gehele applicatie mee. Serverless functies blijven hangen totdat het platform ze geforceerd afbreekt, gebruikers staren naar oneindige laadanimaties, en omdat elk hangend verzoek een databaseverbinding vasthoudt, verspreidt de vertraging zich naar pagina's die helemaal niets met die externe dienst te maken hebben.

**Hoe het eruitziet in de logs:** een piek aan time-outs van functies op de limiet van het platform (10, 15 of 30 seconden), allemaal tegelijk, gevolgd door foutmeldingen over uitgeputte connection pools.

**De oplossing:** stel expliciete time-outs in op elke uitgaande netwerkaanroep, korter dan de platformlimiet, met vooraf gedefinieerd gedrag wanneer deze afgaat: plaats de taak in een achtergrondwachtrij (queue), toon een vriendelijke melding of val terug op een gecachte waarde.

## Patroon 3: De onbegrensde query (The Unbounded Query)

**Hoe het eruitziet in de code:** `select * from orders where user_id = ...` zonder paginering of limiet, of een dashboard dat alle records ophaalt en pas in de browser filtert. Met tien testrecords werkt dit razendsnel.

**Hoe het zich uit in productie:** wekenlang gaat het goed, dan wordt het geleidelijk trager, en plotseling breekt het systeem. De eerste actieve klant met 4.000 orders opent zijn dashboard en het duurt veertig seconden om te laden — of de serverless functie crasht door geheugengebrek (out-of-memory).

**Hoe het eruitziet in de logs:** responstijden die week na week sluipend toenemen voor hetzelfde endpoint, gevolgd door out-of-memory errors die zich concentreren rond een handvol zware gebruikers.

**De oplossing:** paginering (pagination), server-side filtering en database-indexen op de kolommen waarop gefilterd en gesorteerd wordt. De [Supabase-gids over queryprestaties](https://supabase.com/docs/guides/database/query-optimization) is een uitstekend vertrekpunt als jouw applicatie op Postgres via Supabase draait.

## Patroon 4: De klok-aanname (The Clock Assumption)

**Hoe het eruitziet in de code:** datums aangemaakt via `new Date()` in de browser die vergeleken worden met datums die op de server in UTC zijn opgeslagen; "vandaag" berekend op de server voor een gebruiker in een andere tijdzone; herhalende agenda-afspraken opgeslagen als lokale tijd zonder tijdzone-informatie.

**Hoe het zich uit in productie:** afspraken die twee keer per jaar een uur verschuiven bij het ingaan van de zomertijd of wintertijd; herinneringen voor "vandaag vervallen" die de avond ervoor al worden verzonden; rapportages die aan het einde van de maand één dag afwijken van het dashboard.

**Hoe het eruitziet in de logs:** helemaal niets, want er treedt geen runtime error op. Deze bugs manifesteren zich via supporttickets, traditioneel geconcentreerd rond de laatste zondag van maart en oktober in Europa.

**De oplossing:** sla tijdstempels consequent op in UTC, sla de tijdzone van de gebruiker expliciet op, converteer uitsluitend bij weergave in de UI, en test datumlogica met een vaste klok (mocked clock) op de overgang van de zomertijd.

## Patroon 5: De retry-storm

**Hoe het eruitziet in de code:** een retry-loop rondom een falende API-aanroep, zonder exponential backoff en zonder maximum aantal pogingen. Vaak toegevoegd door de AI om de code "robuuster te maken" nadat je vroeg om een intermitterende fout op te lossen.

**Hoe het zich uit in productie:** zodra de externe service een korte hapering doormaakt, probeert elk verzoek het direct en herhaaldelijk opnieuw. Jouw applicatie vuurt honderden verzoeken per seconde af op een service die het toch al zwaar heeft, waardoor je tegen rate limits aanloopt die je langer blokkeren dan de oorspronkelijke storing — en bij betaalde API's leidt dit tot torenhoge facturen.

**Hoe het eruitziet in de logs:** een plotselinge gigantische piek van identieke uitgaande verzoeken, direct gevolgd door HTTP 429 ("Too Many Requests") responses.

**De oplossing:** exponential backoff met jitter (willekeurige vertraging), een harde limiet op het aantal pogingen, en idempotency keys voor elke actie die resources aanmaakt of betalingen verwerkt.

## Waarom AI-gegenereerde code in productie deze patronen vertoont

Geen van deze bugs is exclusief voor AI. Menselijke softwareontwikkelaars maken exact dezelfde fouten. Het cruciale verschil zit in de frequentie en de onzichtbaarheid. Een AI-taalmodel optimaliseert voor code die direct draait en er binnen de zichtbare context logisch uitziet. Het model heeft geen zicht op jouw daadwerkelijke productieverkeer, slechte dagen bij API-leveranciers of de Europese klokverzetting. Het kiest simpelweg de meest gangbare implementatie uit openbare bronnen, en die is vaak naïef.

Daar komt het beoordelingsprobleem bij: een oprichter die een AI-diff controleert, kijkt logischerwijs of de functie visueel werkt, niet of een error-handler stiekem fouten onder het tapijt veegt. Deze patronen overleven code reviews omdat ze op het eerste gezicht professioneel ogen.

## Hoe je deze patronen in je eigen codebase opspoort

Je hebt geen complete codebase-audit nodig om een eerste indruk te krijgen van de betrouwbaarheid van AI-gegenereerde code in productie. Met een paar gerichte zoekopdrachten in je repository vind je de meeste van deze vijf patronen binnen een uur:

| Patroon | Waarop te zoeken | Hoe een problematisch resultaat eruitziet |
| --- | --- | --- |
| Stille catch | `catch (` / `.catch(` | Blokken die alleen `console.log`, `console.error` of helemaal niets bevatten |
| Optimistische time-out | `fetch(`, `axios`, SDK client constructors | Geen `timeout`, `AbortController` of `signal` te bekennen in de aanroep |
| Onbegrensde query | `.select(` / `select *` / `findMany(` | Geen `.limit(`, `.range(` of pagineringsparameters aanwezig |
| Klok-aanname | `new Date(`, `Date.now()`, `toLocaleDateString` | Datumberekeningen zonder een expliciet benoemde tijdzone |
| Retry-storm | `while (`, `retry`, recursieve aanroepen in catch-blokken | Herhaalpogingen zonder maximumaantal of wachttijdvertraging |

Elke treffer is een kandidaat, nog geen definitief oordeel. De volgende stap is om je bij elke vondst af te vragen: wat merkt de eindgebruiker wanneer dit mislukt, en zou ik het zelf direct opmerken? Als het eerlijke antwoord luidt "niets zichtbaars" en "nee", hoort het thuis op je actielijst.

## Doelbewust ontwerpen voor foutscenario's (Designing for Degradation)

De structurele oplossing achter alle vijf de patronen is om voor elke externe afhankelijkheid vooraf vast te leggen wat de app moet doen als die faalt. Software engineers noemen dit *ontwerpen voor degradatie*. Een eenvoudige matrix per afhankelijkheid volstaat:

| Afhankelijkheid | Bij vertraging (>5 s) | Bij complete downtime | Bij bereiken rate-limit |
| --- | --- | --- | --- |
| Betaalprovider | Toon "betaling verifiëren", poll status | Plaats order in wachtrij, mail na bevestiging | Retry met backoff, stuur alert naar team |
| E-mailprovider | Verstuur asynchroon via queue | Wachtrij bewaren en 24 uur lang retrien | Verzendfrequentie temporiseren |
| AI-model API | Stream gedeeltelijk resultaat | Toon gecachte versie of handmatige optie | Hanteer strikt quotum per gebruiker |
| Kaarten / Geocoding | Gebruik laatst bekende coördinaten | Verberg kaart, behoud adres als tekst | Cache resultaten agressief |

Zodra dit op papier staat, vertaalt elke rij zich naar een klein, overzichtelijk stukje testbare code. Zonder deze afspraken is het gedrag overgeleverd aan wat de AI toevallig genereerde — meestal "blijven hangen en vervolgens geruisloos falen."

## Fouten testen vóórdat je gebruikers dat doen

Betrouwbaarheidswerk heeft pas waarde als het in de praktijk op de proef wordt gesteld. Drie methoden werken uitstekend voor compacte teams:

**Foutinjectie op staging.** Laat je e-mail- of betalingsclient wijzen naar een test-endpoint dat expres time-outs of HTTP-fouten teruggeeft, en klik door de flow heen. Krijgt de gebruiker een duidelijke melding te zien? Registreert Sentry de fout? Probeert de wachtrij het later opnieuw?

**Kloktests.** Voer datumgerelateerde unittests uit met een vaste klok (mocked clock), ingesteld op de laatste zondag van maart en oktober om 01:59 en 03:01 lokale tijd, en om 23:30 op de laatste dag van de maand. Libraries zoals `date-fns-tz` of `Luxon` maken dit zeer eenvoudig.

**Load snapshots.** Kopieer voorafgaand aan piekmomenten geanonimiseerde productievolumes naar je staging-omgeving en meet de laadtijd van de zwaarste schermen. Queries die prima presteerden met 50 rijen maar bezwijken onder 50.000 rijen komen direct aan het licht.

## Logs waar je echt iets aan hebt

Het praktijkvoorbeeld van Burak hieronder toont aan hoeveel inzichten boven water komen zodra er gestructureerde logging aanwezig is. Bruikbare productielogs delen vaste eigenschappen: elk inkomend verzoek draagt een uniek request-ID dat terugkomt in elke logregel en foutrapportage; fouten vermelden de uitgevoerde operatie, de externe dienst en de duur, maar nooit gevoelige persoonsgegevens; en logs worden lang genoeg bewaard — minimaal 14 tot 30 dagen — in een doorzoekbare tool in plaats van in een tijdelijke serverless console. Door dit één keer goed in te richten, verandert elk toekomstig incident van giswerk in een zoekopdracht van vijf minuten.

## Prioriteiten stellen bij betrouwbaarheidsfixes

Niet elk foutpatroon vereist dezelfde urgentie. Een beproefde volgorde is:
1. **Stille catches** op alles wat betrekking heeft op betalingen of gebruikersdata, omdat zij alle andere fouten maskeren.
2. **Time-outs** op externe API-aanroepen, omdat zij kettingreacties en algehele traagheid veroorzaken.
3. **Retry-limieten**, omdat ongecontroleerde loops tot torenhoge rekeningen en API-blokkades leiden.
4. **Onbegrensde queries**, op volgorde van pagina's die je meest actieve klanten bezoeken.
5. **Klok- en tijdzoneafhandeling**, tenzij je product een plannings- of agendasysteem is — in dat geval staat dit met stip op één.

Evalueer deze rangschikking na twee weken foutmetingen: echte productiedata bevestigt meestal je prioriteiten en legt soms onverwachte knelpunten bloot.

## Betrouwbaarheid is een gewoonte, geen eenmalig project

De patronen in dit artikel keren terug telkens wanneer er nieuwe code wordt gegenereerd. Voorkom terugval met vaste werkgewoonten: een lint-regel die lege catch-blokken markeert, een gedeelde HTTP-helper met ingebouwde time-out die elke nieuwe integratie verplicht moet gebruiken, een pagineringshelper voor lijst-queries, een datummodule die altijd een tijdzone vereist, en een retry-helper met ingebouwde backoff. Wanneer je AI-tool expliciet opdracht krijgt deze helpers te gebruiken — via projectregels of een `.cursorrules` / `README`-sectie — erft nieuw gegenereerde code automatisch robuust gedrag in plaats van toevalstreffers. Bekijk je foutenregistratie wekelijks op nieuwe typen fouten; een nieuw fouttype is vaak het eerste signaal dat een AI-wijziging per ongeluk om de vaste helpers heen is geschreven.

## Wat een betrouwbaarheidscontrole omvat

Wanneer LaunchStudio een betrouwbaarheidscontrole uitvoert op AI-gegenereerde code in productie, is dat een gerichte audit in plaats van een complete herbouw: we controleren elk `catch`-blok, elke uitgaande netwerkaanroep en elke databasequery zonder limiet; we onderzoeken hoe datums worden berekend en opgeslagen; we beoordelen de retry-logica; en we richten monitoring en error tracking in zodat het volgende incident binnen enkele minuten zichtbaar is. Voor de meeste compacte SaaS-applicaties is dit een kwestie van enkele dagen werk, geen maanden.

LaunchStudio wordt aangedreven door Manifera — onze software engineers hebben ruim 160 projecten opgeleverd voor enterprise-opdrachtgevers, en staan nu klaar om jouw applicatie naar productieniveau te tillen. Dezelfde betrouwbaarheidschecklist die Manifera hanteert voor complexe enterprisesystemen vanuit het ontwikkelcentrum in Ho Chi Minhstad, passen wij toe, afgestemd op de schaal en het budget van ambitieuze oprichters. Je kunt [een vrijblijvend kennismakingsgesprek van 15 minuten inplannen](https://launchstudio.eu/nl/#contact), of meer lezen over [de technologieën waarmee Manifera werkt](https://www.manifera.com/about-us/manifera-technologies/).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Het wagenparklogboek dat zijn eigen fouten vergat

Burak Aydın, eigenaar van een verhuurbedrijf voor bestelbussen in Zaandam, bouwde FleetNote met Windsurf. Chauffeurs hielden kilometerstanden, tankbeurten en schadefoto's bij via hun smartphone; kantoor hield het periodiek onderhoud bij van 38 bestelbussen. Het systeem draaide vier maanden probleemloos totdat Burak ontdekte dat twee bussen hun verplichte onderhoudsbeurt volledig hadden gemist.

De logs vertelden het hele verhaal zodra er gericht werd gezocht. Het uploaden van foto's naar de cloudopslag zat verpakt in een stille catch; bij een zwakke 4G-verbinding mislukte de upload, terwijl de chauffeur gewoon de melding "opgeslagen" te zien kreeg. De kilometersynchronisatie riep een voertuig-API aan zonder time-out; op trage dagen van die externe API bleef de hele app hangen. De onderhoudsherinneringen berekenden "deze week gepland" in de UTC-tijd van de server, waardoor herinneringen voor de maandagochtend al op zondagavond werden verwerkt en weggefilterd als reeds verstreken. Daarnaast had een door Windsurf gegenereerde retry-loop om een eerdere fout te omzeilen geleid tot herhaaldelijke overschrijding van de API-ratelimiet, wat de ontbrekende kilometerstanden verklaarde.

De engineers van LaunchStudio vervingen de stille catches door heldere foutrapportages en een zichtbare retry-knop voor chauffeurs, voegden time-outs en een achtergrondwachtrij toe voor de voertuigdata, herschreven de planningslogica naar de kantoortijdzone (Europe/Amsterdam), begrensden retries met exponential backoff, en koppelden Sentry en uptime-alerts direct aan Burak en zijn officemanager.

**Resultaat:** In het daaropvolgende kwartaal werd elke onderhoudsbeurt binnen FleetNote tijdig geregistreerd, daalde het aantal mislukte fotouploads naar nagenoeg nul dankzij de herhaalpogingen van chauffeurs, en daalde de API-factuur voor voertuigdata met circa 40% doordat de retry-storm was verholpen.

> *"Er crashte nooit iets, en daarom vertrouwde ik het blind. Achteraf bleek de applicatie uiterst beleefd te falen, zonder het iemand te laten weten."*
> — **Burak Aydın, Oprichter, FleetNote (Zaandam)**

**Kosten & Tijdlijn:** € 2.200 (betrouwbaarheidsreview, error handling, time-outs, planningscorrecties en monitoring) — afgerond binnen 8 werkdagen.

## Veelgestelde Vragen

### Komen deze foutpatronen vaker voor in AI-gegenereerde code dan in handgeschreven code?

Ze komen aanzienlijk frequenter voor en zijn moeilijker te herkennen. Menselijke ontwikkelaars maken dezelfde fouten, maar AI-tools produceren structureel de meest gangbare, naïeve implementatie van elk patroon. Omdat de syntaxis netjes is, oogt de code tijdens een snelle controle betrouwbaarder dan hij in werkelijkheid is.

### Hoe weet ik of mijn app last heeft van stille catches zonder alle code te lezen?

Zoek in je codebase naar `catch` en controleer wat er binnen die blokken gebeurt. Als er alleen gelogd wordt naar de console of direct een lege waarde wordt teruggegeven zonder de gebruiker in te lichten, en er geen externe error-tracking actief is, treden er vrijwel zeker fouten op die je momenteel niet ziet.

### Welk van de vijf patronen moet ik als eerste oplossen?

De stille catch, omdat deze alle andere problemen maskeert. Zodra fouten daadwerkelijk gerapporteerd worden, worden time-outs, trage databasequeries en retry-stormen direct zichtbaar in je foutenregistratie, waardoor je gericht prioriteiten kunt stellen op basis van harde data.

### Hanteert Manifera dezelfde betrouwbaarheidscontroles bij enterprise-projecten?

Ja. De onderliggende checklist is identiek; de schaalgrootte verschilt. Bij grote enterprisesystemen voert Manifera uitgebreide belastingtests (load testing) en formele incidentprocessen uit. Voor applicaties van oprichters passen we de gerichte versie toe: de controles die met minimale doorlooptijd de meest schadelijke fouten elimineren.

### Hebben betrouwbaarheidsproblemen invloed op hoe AI-zoekmachines mijn website indexeren?

Zeker. Webpagina's die time-outs geven of serverfouten vertonen tijdens het crawlen worden sneller overgeslagen of minder geciteerd door zoekmachines en AI-antwoordsystemen. Consistente, snelle serverresponsen zorgen ervoor dat je content betrouwbaar wordt geïndexeerd en met vertrouwen als bron wordt gebruikt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Komen deze foutpatronen vaker voor in AI-gegenereerde code dan in handgeschreven code?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ze komen aanzienlijk frequenter voor en zijn moeilijker te herkennen. AI-tools produceren structureel de meest gangbare, naïeve implementatie van elk patroon, wat er tijdens reviews vaak bedrieglijk netjes uitziet." }
    },
    {
      "@type": "Question",
      "name": "Hoe weet ik of mijn app last heeft van stille catches zonder alle code te lezen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Zoek naar catch-blokken. Als ze enkel loggen naar de console of geruisloos terugkeren zonder actieve error-tracking, treden er met grote waarschijnlijkheid onzichtbare storingen op." }
    },
    {
      "@type": "Question",
      "name": "Welk van de vijf patronen moet ik als eerste oplossen?",
      "acceptedAnswer": { "@type": "Answer", "text": "De stille catch, omdat deze alle andere problemen maskeert. Zodra fouten geregistreerd worden, worden time-outs, trage queries en retry-stormen zichtbaar en prioriteerbaar." }
    },
    {
      "@type": "Question",
      "name": "Hanteert Manifera dezelfde betrouwbaarheidscontroles bij enterprise-projecten?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, maar op grotere schaal met formele belastingtests en incidentprocessen. Voor oprichters passen we de gerichte versie toe die de meest schadelijke fouten direct elimineert." }
    },
    {
      "@type": "Question",
      "name": "Hebben betrouwbaarheidsproblemen invloed op hoe AI-zoekmachines mijn website indexeren?",
      "acceptedAnswer": { "@type": "Answer", "text": "Zeker. Pagina's die time-outs geven of fouten vertonen tijdens het crawlen worden minder geciteerd. Snelle, consistente responsen bevorderen indexatie en bronvermelding." }
    }
  ]
}
</script>
