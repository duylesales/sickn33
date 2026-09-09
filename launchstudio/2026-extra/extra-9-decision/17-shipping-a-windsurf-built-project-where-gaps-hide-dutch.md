---
Titel: "Een met Windsurf Gebouwd Project Opleveren: Waar de Gaten Zich Meestal Schuilhouden"
Trefwoorden: Windsurf Cascade productie, multi-file AI bewerkingen review, half gemigreerde codebase, AI codeerconventies drift, AI project lanceren, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Een met Windsurf Gebouwd Project Opleveren: Waar de Gaten Zich Meestal Schuilhouden

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Een met Windsurf Gebouwd Project Opleveren: Waar de Gaten Zich Meestal Schuilhouden",
  "description": "De multi-file bewerkingen van Windsurf Cascade vertonen een specifieke signatuur: half voltooide refactors, conflicterende conventies en code die tussen promptsessies veroudert. Een praktische gids voor de vijf plekken waar deze risico's schuilen.",
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
  "datePublished": "2027-01-18",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/een-met-windsurf-gebouwd-project-opleveren-waar-de-gaten-zich-schuilhouden"
  }
}
</script>

Het is 01:40 uur 's nachts en u staart naar twee functies die ogenschijnlijk exact hetzelfde doel dienen: `getUserOrgs` in `lib/orgs.ts` en `fetchOrganizationsForUser` in `server/queries/organizations.ts`. Beide functies werken. Beide worden aangeroepen vanuit verschillende uithoeken van uw applicatie. Maar de ene functie filtert gearchiveerde organisaties er wél uit en de andere niet. U kunt zich niet herinneren dat u een van beide heeft geschreven, omdat Cascade ze allebei heeft gegenereerd — met negen dagen ertussen, naar aanleiding van twee prompts die destijds volkomen los van elkaar leken te staan.

Dit is het typische handelsmerk van Windsurf, en het vertegenwoordigt een fundamenteel ander risicoprofiel dan klassieke code-aanvulling in één enkel bestand. De ongekende kracht van Cascade is dat het wijzigingen over een complete codebase tegelijkertijd kan doorvoeren: vraag om functionaliteit voor gebruikers-impersonatie ten behoeve van supportmedewerkers, en de agent past in één coherente beweging de authenticatie-middleware aan, werkt drie route handlers bij, genereert een databasemigratie en past een React-hook aan. Die samenhang is *binnen* één afzonderlijke sessie buitengewoon indrukwekkend. Tussen opeenvolgende sessies treedt echter onvermijdelijk erosie op: het model herontdekt uw codebase elke keer opnieuw en kan niet betrouwbaar onderscheiden welk van de aangetroffen architectuurpatronen uw werkelijke voorkeur heeft.

Het resultaat is een codebase waarin op het eerste gezicht niets kapot is, maar waarin meerdere onderdelen geruisloos half-waar zijn geworden. Hieronder vindt u de vijf plekken waar deze kloven zich schuilhouden, gerangschikt op urgentie.

## Kloof één: de refactor die voor 80% is voltooid

Dit is zonder twijfel de meest voorkomende bevinding en tevens degene met de grootste gevolgen.

U vroeg om een structurele aanpassing: "verplaats alle authenticatie naar middleware", "stap over van de publieke Supabase-client naar een beveiligde serverclient", of "breng permissiecontroles onder in een centrale helperfunctie". Cascade stelde een helder plan op, toonde een lijst met bestanden, voerde de bewerkingen uit en u keurde het goed. Elf bestanden werden netjes aangepast. De hoofdfunctionaliteit werkte vlekkeloos tijdens uw handmatige test en u ging door naar de volgende feature.

Het twaalfde bestand ontbrak echter in het plan. Omdat het in een map stond die buiten het initiële zoekbereik viel, omdat het aanroeppunt dynamisch werd samengesteld, of omdat het bestand pas later in een andere sessie werd toegevoegd. Nu heeft u een codebase waarin authenticatie *grotendeels* via middleware verloopt — behalve in die ene vergeten route waar de oude inline-controle is achtergebleven, die op subtiele wijze wél controleert op de actieve sessie, maar vergeet de rol van de gebruiker te verifiëren.

Half afgeronde refactors zijn levensgevaarlijk, juist omdat ze er ogenschijnlijk afgewerkt uitzien. De oude logica functioneert immers nog steeds, waardoor er nergens een foutmelding optreedt. De enige betrouwbare manier om deze weeffouten bloot te leggen, is door gericht te zoeken naar het patroon waar u *vandaan migreerde*, in plaats van naar het patroon waar u naartoe wilde:

```bash
rg -n "createClient\(.*ANON" server/ app/          # patronen die vervangen hadden moeten zijn
rg -n "getSession\(\)" --files-with-matches | wc -l # hoort nagenoeg nul te zijn na middleware-migratie
git log --oneline --all | head -40                  # vind de refactor-commit en bestudeer het diff
```

Neem de bestandslijst van de oorspronkelijke refactor-commit en vergelijk deze met een actuele zoekopdracht naar het oude codeerpatroon. Het verschil tussen beide is uw actielijst met achtergebleven kwetsbaarheden. Dit vergt tien minuten per historische refactor en levert gegarandeerd de hoogste waarde op.

## Kloof twee: twee van alles, met tegenstrijdige meningen

Naast onvoltooide refactors treedt er vanzelf een opeenstapeling van gedupliceerde logica op. Een representatief Windsurf-project bevat op het moment van lancering doorgaans:

- Twee verschillende data-access helpers voor dezelfde databasetabel (zoals in ons inleidende voorbeeld), waarbij de ene helper filters toepast die de andere negeert.
- Twee API-clients voor dezelfde externe dienst: de ene gebouwd met een ruwe `fetch`-aanroep en de andere via de officiële SDK, elk met eigen foutafhandeling en soms zelfs verschillende basis-URL's.
- Twee validatiemethoden: Zod op nieuwere routes versus handgeschreven controles (`if (!body.email) return 400`) op oudere routes.
- Twee manieren om configuratiewaarden uit te lezen: rechtstreeks via `process.env` en via een centrale configuratiemodule, waardoor een hernoemde variabele op de ene plek breekt en op de andere niet.
- Twee parallelle authenticatiestromen, ontstaan doordat een latere sessie inloggen via Google toevoegde zonder de aannames van het e-mail/wachtwoord-pad op te schonen.

Niets hiervan veroorzaakt een runtime-crash. Het acute gevaar is dat een bugfix die u op de ene kopie toepast, de andere kopie ongemoeid laat. Dat is precies hoe beveiligingslekken ontstaan: u ontdekt een fout in `fetchOrganizationsForUser`, lost deze op, rolt uit naar productie, terwijl `getUserOrgs` rustig doorgaat met het tonen van gearchiveerde data aan gebruikers die daar geen recht op hebben.

Spoor duplicaten op met behulp van gespecialiseerde tools in plaats van met het blote oog: `npx jscpd src server --min-lines 8 --min-tokens 60` genereert binnen enkele minuten een helder rapport. Maak vervolgens per duplicatenpaar een principiële keuze: behoud de juiste variant, verwijder de overbodige, en pas alle aanroepen in één samenhangende commit aan. Weersta de verleiding om Cascade dit ongezien te laten uitvoeren; het verwijderen van code is exact de stap waarin subtiele afhankelijkheden breken.

## Kloof drie: regels en geheugens die niet langer actueel zijn

De persistent rules en memories van Windsurf vormen een belangrijk voordeel: ze voorkomen dat u bij elke nieuwe sessie uw conventies opnieuw moet uitleggen. Ze vormen echter tevens de bron van sluipende inconsistenties: zodra uw architectuur evolueert maar uw regels niet worden bijgewerkt, blijft het model verouderde instructies blindelings volgen.

Wellicht schreef u in week één een regel dat het project gebruikmaakt van de Next.js Pages Router. In week vier bent u gemigreerd naar de App Router. Die oude regel staat er echter nog steeds, waardoor Cascade af en toe alsnog Pages-gebaseerde routes aanmaakt die 'ongeveer' werken. Of een opgeslagen geheugen vermeldt: "we gebruiken `supabase.auth.getUser()` voor sessiecontroles", daterend van vóór uw overstap naar een server-side client. Gevolg: nieuwe code grijpt direct terug naar het oude, onveilige patroon en introduceert opnieuw exact de weeffout uit kloof één.

Lees vóór elke lanceringsfase alle `.windsurfrules`-bestanden en opgeslagen herinneringen door alsof een vreemde ze heeft opgesteld. Verwijder meedogenloos elke regel die beschrijft hoe de codebase *was* in plaats van hoe deze *is*. Voeg vervolgens de regels toe die specifiek voor productie cruciaal zijn: waar autorisatie dwingend wordt afgedwongen, dat databasewijzigingen uitsluitend via migratiebestanden mogen verlopen, en dat geen enkele geheime sleutel ooit een publiek voorvoegsel mag krijgen.

## Kloof vier: code die in de praktijk nooit echt is uitgevoerd

Cascade genereert buitengewoon complete implementaties, inclusief logische vertakkingen die u tijdens het testen nooit daadwerkelijk heeft doorlopen.

De foutafhandelingspaden zijn de gebruikelijke verdachten: een `catch`-blok dat een foutmelding logt en vrolijk een HTTP 200 met `{ success: false }` retourneert, waardoor uw frontend een mislukking als succes interpreteert. Een herhaallus (retry loop) zonder exponentiële backoff of maximumlimiet, die een tijdelijke hapering bij een externe leverancier transformeert in een zelf-geïnduceerde denial-of-service aanval. Of een `finally`-blok dat een databaseverbinding probeert te sluiten die via een ander pad al gesloten was.

Daarnaast zijn er de vergeten endpoints die niemand gebruikt: route handlers die ooit zijn gebouwd voor een geschrapte functionaliteit, een `/api/admin/*`-groep van een beheeromgeving die u nooit heeft afgemaakt, of een exportroute die voor één specifieke demo is opgezet. Ze staan live, zijn vaker wel dan niet onbeveiligd, en zijn onzichtbaar in uw statistieken omdat legitieme gebruikers ze nooit aanroepen. Breng alle routes via grep in kaart en leg ze naast uw serverlogs van de afgelopen dertig dagen. Verwijder ongebruikte routes in plaats van ze te beveiligen: code die u niet nodig heeft is louter een risico zonder enig voordeel.

Controleer tevens de geautomatiseerde tests, voor zover Cascade die heeft gegenereerd. Door AI geschreven tests controleren vrijwel uitsluitend of een functie 'iets' teruggeeft bij legitieme data. Ze testen zelden of de functie een keiharde HTTP 403 geeft wanneer een kwaadwillende gebruiker andermans ID meegeeft.

## Kloof vijf: migraties geschreven, migraties nooit toegepast

Cascade is uitstekend in staat om SQL-migratiebestanden aan te maken. Het heeft echter geen flauw idee of u die bestanden ooit daadwerkelijk op uw live productiedatabase heeft uitgevoerd.

De typische gang van zaken: de agent genereert `0007_add_team_invites.sql`, u voert dit lokaal uit, de functionaliteit werkt, en vervolgens vindt de uitrol naar productie plaats via een eenvoudig `git push`-commando dat geen migratiestap bevat. Of het omgekeerde scenario: u had haast voor een presentatie en voegde handmatig een kolom toe in de online console van Supabase of Neon. Gevolg: productie bezit de kolom, maar uw migratiemap weet van niets.

In beide gevallen wijken uw git-repository en uw live database van elkaar af, en dat ontdekt u pas tijdens een calamiteit. Controleer dit rechtstreeks: voer `supabase db diff --linked` uit, draai `prisma migrate diff --from-schema-datamodel --to-schema-datasource`, of gebruik Drizzle's controlecommando tegen de live database. Een leeg diff-resultaat is uw succeseis. Elk verschil toont exact aan waar uw repository achterloopt op de werkelijkheid.

Synchroniseer de databasestructuur naar een opgeschoonde baseline die exact overeenkomt met productie, raak de online databaseconsole daarna nooit meer handmatig aan, en veranker het geautomatiseerd uitvoeren van migraties definitief in uw deployment-pipeline.

## De audit van een halve dag, in logische volgorde

Heeft u één middag beschikbaar vóórdat u uw product openstelt voor klanten? Volg dit stappenplan:

1. Identificeer uw twee of drie grootste historische refactors via git log. Zoek met grep naar het oude patroon en repareer overgebleven code. (60 min)
2. Draai `jscpd`. Los elk gedupliceerd codeblok op dat raakt aan authenticatie, datatoegang of betalingsverkeer. (60 min)
3. Lees uw rules- en memorybestanden. Verwijder verouderde richtlijnen en veranker uw productienormen. (20 min)
4. Lijst alle API-routes op, vergelijk deze met uw serverlogs en verwijder dode code. (30 min)
5. Vergelijk uw databasestructuur (diff) met de live productieomgeving, synchroniseer afwijkingen en koppel migraties aan de build. (60 min)
6. Voer de cross-tenant test uit: twee accounts, waarbij account A records van account B opvraagt op elk endpoint dat een ID accepteert. (30 min)

Zes concrete stappen, circa vierenhalf uur werk, en het rekent doelgericht af met de daadwerkelijke risico's van multi-file agentic coding — in tegenstelling tot generieke security-lijstjes die grotendeels niet van toepassing zijn op uw situatie.

Wat deze stappen niet kunnen oplossen, zijn de fundamentele structurele keuzes. Welke van de twee parallelle authenticatiestromen blijft behouden, waar wordt autorisatie voortaan universeel afgedwongen en hoe wordt het datamodel beheerd? Deze beslissingen vereisen dat iemand het totale systeem als één geheel in het geheugen houdt — en dat is architectonisch gezien exact waar een sessie-gebonden AI-agent toe niet in staat is. [LaunchStudio](https://launchstudio.eu/nl/) is opgericht voor die overdracht: uw frontend en ontwikkelworkflow blijven intact, de structurele inconsistenties worden opgelost door senior engineers die wekelijks met dit soort codebases werken, en alle ontwerpkeuzes worden expliciet gedocumenteerd zodat uw Windsurf-rules ze daarna kunnen bewaken. Ons team is afkomstig van [Manifera](https://www.manifera.com/portfolio/), waar men al meer dan tien jaar productiesoftware bouwt voor enterprise-klanten op basis van het principe dat er binnen een codebase slechts één juiste manier bestaat om cruciale taken uit te voeren.

Vaste prijs, afgesproken na een korte technische intake vóórdat iemand een regel code aanraakt — [vertel ons wat u heeft gebouwd](https://launchstudio.eu/nl/#contact) en u ontvangt nog deze week een helder voorstel qua kosten en doorlooptijd.

## Echt voorbeeld

### Twee functies, één ontbrekend filter, elfhonderd datarecords op straat

Nadia el Amrani ontwikkelde met behulp van Windsurf gedurende zeven weken Werkstroom: een compliance- en workflowtool voor facilitaire dienstverleners waarmee keuringen, certificeringen en verloopdata op klantlocaties worden beheerd. Vier gerenommeerde facilitaire bedrijven draaiden een proeflicentie. Een vijfde, aanzienlijk grotere speler toonde serieuze interesse en vroeg om een formeel beveiligingsrapport vóór ondertekening van het jaarcontract.

Onze technische audit bracht vrijwel direct het inleidende probleem aan het licht. Twee afzonderlijke functies haalden de toegankelijke locaties van een gebruiker op: de ene geschreven in week twee, de andere gegenereerd in week vijf tijdens een refactor die de eerste had moeten vervangen. De nieuwere functie filterde netjes op het organisatie-ID van de ingelogde gebruiker. De oudere functie accepteerde echter een losse `siteIds`-array die vanuit de frontend werd meegestuurd — en één dashboardmodule bleek die oude functie nog altijd aan te roepen met een ongefilterde lijst die in de browser was samengesteld. Elke willekeurige proefgebruiker kon via een gemanipuleerd netwerkverzoek de inspectierapporten en certificeringen van circa elfhonderd locaties van de overige drie proefklanten downloaden. De refactor-commit had destijds keurig negen bestanden aangepast; het tiende bestand was over het hoofd gezien.

Daarnaast faalde de database-audit: er bleken drie kolommen in de live productiedatabase te bestaan die nergens in een migratiebestand waren gedocumenteerd, handmatig toegevoegd tijdens een eerdere verkoopdemo.

**Resultaat:** De gedupliceerde queries werden teruggebracht naar één centrale organisatie-gebonden datalaag, alle locatietoegang werd ondergebracht achter één uniforme autorisatiehelper, de databasestructuur werd gesynchroniseerd met een sluitende baseline-migratie die automatisch meedraait bij deployments, en een geautomatiseerde cross-tenant test werd verankerd in CI. Zes werkdagen werk. Nadia kon de grote prospect een officieel audit- en herstelrapport overhandigen en tekende het contract drie weken later.

> *"Beide functies zagen er op zichzelf prima uit. Dat blijft me achteraf het meest verbazen. Geen van beide bevatte slechte code — ze verschilden simpelweg op één cruciaal filter. Ik had ze letterlijk zij-aan-zij moeten leggen om het ooit zelf te ontdekken."*
> — **Nadia el Amrani, Oprichter, Werkstroom (Tilburg)**

**Kosten & Doorlooptijd:** € 3.200 (Launch Ready Pakket) — live binnen 6 werkdagen.

---

## Veelgestelde Vragen

### Waarom ontstaan half voltooide refactors zelfs wanneer ik het plan van Cascade expliciet goedkeur?

Omdat het gegenereerde plan uitsluitend gebaseerd is op de bestanden die Cascade op dat specifieke moment kon detecteren. Bestanden die worden aangeroepen via dynamische imports, broncode in mappen die buiten het zoekbereik vallen, en componenten die pas in latere sessies zijn toegevoegd, worden niet meegenomen. Het plan is een eerlijke weergave van wat de agent zag, maar wat de agent zag is zelden de volledige codebase.

### Heeft het zin om Windsurf-rules en memories te gebruiken als ze na verloop van tijd verouderen?

Absoluut — het is de meest kostenefficiënte manier om consistentie in uw codebase te waarborgen. De vereiste discipline is echter om deze regels te behandelen als broncode: evalueer ze zodra uw architectuur verandert, verwijder verouderde richtlijnen doelbewust, en houd de lijst beknopt zodat het doornemen ervan twee minuten kost in plaats van twintig.

### Hoe bepaal ik welke van twee gedupliceerde functies ik moet behouden?

Behoud de variant waarvan het gedrag exact overeenkomt met hoe u het vandaag de dag zou ontwerpen. Kies niet automatisch voor de nieuwste versie: de latere implementatie is door de agent soms gegenereerd met minder contextuele kennis dan het origineel. Bestudeer beide implementaties, maak een weloverwogen keuze, en verwijder de overtollige functie in exact dezelfde git-commit waarin u alle aanroepende componenten bijwerkt.

### Kan ik Cascade de ontdubbeling van code zelfstandig laten uitvoeren?

Gebruik de agent gerust om potentiële duplicaten op te sporen, maar inspecteer bij het daadwerkelijk verwijderen van code elke regel in het diff-overzicht handmatig. Het verwijderen van een functie is bij uitstek het moment waarop een gemiste dynamische aanroep leidt tot een runtime-fout in een codepad dat u niet dagelijks test.

### Dekt de aanwezigheid van gegenereerde tests het risico op ongeoorloofde datatoegang (IDOR) al af?

Vrijwel nooit. Door AI gegenereerde tests verifiëren doorgaans uitsluitend of een geautoriseerde gebruiker het verwachte antwoord ontvangt — het 'happy path'. Het waarborgen van data-isolatie tussen huurders vereist echter dat u expliciet test of een *ongeautoriseerde* gebruiker een keiharde HTTP 403-foutmelding krijgt. Die negatieve testcase genereert een AI-agent zelden uit eigen beweging.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom ontstaan half voltooide refactors zelfs wanneer ik het plan van Cascade expliciet goedkeur?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het plan toont alleen wat Cascade op dat moment kon vinden. Dynamische imports, code buiten het zoekbereik en call-sites uit latere sessies ontbreken, waardoor het plan eerlijk is over wat het zag maar niet volledig is."
      }
    },
    {
      "@type": "Question",
      "name": "Heeft het zin om Windsurf-rules en memories te gebruiken als ze na verloop van tijd verouderen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, mits u ze behandelt als code. Evalueer ze bij architectuurwijzigingen, ruim verouderde regels direct op en houd ze beknopt zodat ze snel leesbaar blijven."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe bepaal ik welke van twee gedupliceerde functies ik moet behouden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Kies de functie die het gewenste gedrag van vandaag vertegenwoordigt, niet automatisch de nieuwste. Verwijder de oude functie in dezelfde commit waarin u alle aanroepende code bijwerkt."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik Cascade de ontdubbeling van code zelfstandig laten uitvoeren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Laat de agent kandidaten opsporen, maar controleer de verwijderingen handmatig. Bij functie-verwijderingen kunnen dynamische aanroepen gemist worden die runtime crashes veroorzaken."
      }
    },
    {
      "@type": "Question",
      "name": "Dekt de aanwezigheid van gegenereerde tests het risico op ongeoorloofde datatoegang (IDOR) al af?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vrijwel nooit. AI-tests testen het succes-pad van geautoriseerde gebruikers. Isolatie vereist expliciet testen dat een ongeautoriseerde gebruiker een HTTP 403 Forbidden ontvangt."
      }
    }
  ]
}
</script>
