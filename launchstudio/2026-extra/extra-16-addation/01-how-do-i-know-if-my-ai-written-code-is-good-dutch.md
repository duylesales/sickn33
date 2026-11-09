---
Titel: "Hoe Weet Ik of Mijn Door AI Geschreven Code Goed Is?"
Trefwoorden: is mijn ai-code goed, kwaliteit ai-gegenereerde code, lovable code kwaliteit controleren, code review niet-technische oprichter, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Hoe Weet Ik of Mijn Door AI Geschreven Code Goed Is?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Weet Ik of Mijn Door AI Geschreven Code Goed Is?",
  "description": "Oprichters die bouwen met Lovable, Bolt, Cursor of Claude Code kunnen de code die hun tools produceren vaak niet beoordelen. Deze gids legt uit wat goede code in de praktijk betekent, welke gedragstests elke oprichter kan uitvoeren, welke signalen in de repository het bekijken waard zijn, welke geautomatiseerde tools kwaliteit meten, welke waarschuwingssignalen een expertreview rechtvaardigen en hoe u voorkomt dat de kwaliteit achteruitgaat terwijl AI-tools code blijven toevoegen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-07-27",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-do-i-know-if-my-ai-written-code-is-good" },
  "citation": [
    { "@type": "CreativeWork", "name": "Veracode 2025 GenAI Code Security Report", "url": "https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/" },
    { "@type": "CreativeWork", "name": "Perry et al., Do Users Write More Insecure Code with AI Assistants?", "url": "https://arxiv.org/abs/2211.03622" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021", "url": "https://owasp.org/Top10/" },
    { "@type": "CreativeWork", "name": "OpenSSF Scorecard", "url": "https://securityscorecards.dev/" }
  ]
}
</script>

**Kort antwoord:** u kunt door AI geschreven code niet beoordelen aan de hand van de vraag of de app in een demo werkt. Goede code gedraagt zich correct met echte gebruikers en echte data, houdt de gegevens van elke klant gescheiden, faalt op een veilige manier, kan worden aangepast zonder andere functies te breken en is te begrijpen voor iemand anders dan de tool die haar schreef. Als niet-technische oprichter kunt u veel hiervan zelf controleren met een paar gedragstests en controles in de repository, de rest meten met geautomatiseerde tools, en een expertreview inschakelen vóór de lancering of voordat grote klanten en investeerders goed gaan kijken.

## Belangrijkste Punten

- **"Het werkt" is een lage lat.** AI-tools produceren betrouwbaar code die werkt op het ideale pad; kwaliteit blijkt uit randgevallen, beveiliging, onderhoudbaarheid en foutafhandeling.
- **Gedragstests onthullen veel:** tests met twee accounts, fouttests, tests met verversen en de terugknop, mobiele tests en tests met een traag netwerk.
- **Signalen in de repository tellen:** een README, een consistente structuur, tests die draaien, geautomatiseerde controles, beheerste afhankelijkheden en geen geheimen in de code.
- **Geautomatiseerde tools meten delen van de kwaliteit,** zoals typefouten, lintproblemen, kwetsbare afhankelijkheden en paginaprestaties.
- **Een onafhankelijke review loont op cruciale momenten:** vóór de lancering, vóór enterprise-deals, vóór een financieringsronde en na grote AI-gegenereerde wijzigingen.

## Wat "Goed" Betekent voor een Startupproduct

Engineers discussiëren eindeloos over codestijl. Voor een oprichter heeft goede code praktische eigenschappen:

| Eigenschap | Wat het betekent | Waarom het telt |
| --- | --- | --- |
| Correct | Doet wat gebruikers verwachten, ook in randgevallen | Minder supportvragen, vertrouwen |
| Veilig | Elke gebruiker ziet alleen zijn eigen data; geheimen beschermd | Voorkomt datalekken en gemiste deals |
| Veerkrachtig | Gaat netjes om met fouten, trage netwerken en storingen | Minder verloren acties en klachten |
| Onderhoudbaar | Wijzigingen op één plek breken niets elders | Snellere ontwikkeling, lagere kosten |
| Begrijpelijk | Een andere developer vindt snel zijn weg | Werving, overdracht, due diligence |
| Getest | Belangrijk gedrag wordt automatisch gecontroleerd | Veilige wijzigingen, minder regressies |
| Observeerbaar | Fouten en prestaties zijn zichtbaar | Problemen gevonden voordat klanten ze melden |
| Efficiënt | Pagina's en queries zijn snel met echte data | Gebruikerservaring, infrastructuurkosten |

Onderzoek laat zien waarom dit onderscheid belangrijk is. De analyse van Veracode uit 2025 van AI-gegenereerde code vond beveiligingszwakheden in ongeveer 45% van de voorbeelden, en een Stanford-studie van Perry en collega's liet zien dat developers die AI-assistenten gebruikten minder veilige code schreven en er tegelijk meer vertrouwen in hadden. AI-tools zijn krachtig, maar hun output moet worden gecontroleerd.

## Gedragstests Die Elke Oprichter Kan Uitvoeren

U hoeft geen code te lezen om veel over de kwaliteit te leren.

**1. De test met twee accounts.** Maak twee accounts aan, bij voorkeur in twee verschillende organisaties als uw app teams kent. Maak data aan in account A. Probeer die in account B te vinden: zoek, open URL's die u uit account A hebt gekopieerd, verander ID's in de adresbalk. Als u vanuit B de data van A kunt zien, is de toegangscontrole kapot.

**2. De fouttest.** Zet wifi uit terwijl u een formulier opslaat. Voer ongebruikelijke invoer in: heel lange tekst, emoji, een datum ver in het verleden, een negatief bedrag. Toont de app een duidelijke melding, of doet hij alsof het gelukt is, loopt hij vast of crasht hij?

**3. De test met verversen en de terugknop.** Ververs midden in een flow met meerdere stappen, gebruik de terugknop na een betaling, open dezelfde pagina in twee tabbladen. Verliest u data, krijgt u dubbele records of ziet u inconsistente toestanden?

**4. De mobiele test.** Gebruik de app op een oudere telefoon via mobiele data. Zijn pagina's bruikbaar en redelijk snel? Kunt u de belangrijkste journeys afronden?

**5. De test met datavolume.** Importeer of maak een realistische hoeveelheid data aan, bijvoorbeeld duizend records, en gebruik de belangrijkste schermen. Blijven ze snel?

**6. De rechtentest.** Probeer als gewone gebruiker beheerpagina's te openen door hun URL's in te typen. Controleer als gebruiker die een team heeft verlaten of u nog steeds toegang heeft.

Elke mislukte test wijst naar een specifiek gebied dat gerepareerd moet worden, en het halen van alle tests is een betekenisvol teken van kwaliteit, al is het geen bewijs.

## Signalen in de Repository

Als uw code in GitHub staat, open die dan en kijk naar deze signalen, ook zonder de code in detail te lezen:

| Signaal | Goed teken | Waarschuwingsteken |
| --- | --- | --- |
| README | Legt uit hoe u kunt draaien, testen en deployen | Ontbreekt of is de standaardtemplate |
| Structuur | Duidelijke mappen voor features, componenten, database, functies | Honderden bestanden in één map |
| Bestandsgrootte | De meeste bestanden zijn gericht | Bestanden met duizenden regels |
| Duplicatie | Gedeelde helpers worden hergebruikt | Dezelfde logica op veel plekken gekopieerd |
| Tests | Een testmap en tests die in CI draaien | Geen tests, of tests die altijd worden overgeslagen |
| CI-controles | Automatische controles bij elke wijziging, meestal groen | Geen controles, of controles die permanent falen |
| Migraties | Databasewijzigingen in bestanden met versies | Schema alleen in een dashboard gewijzigd |
| Afhankelijkheden | Een redelijk aantal, grotendeels bekend | Veel onbekende of ongebruikte packages |
| Geheimen | Geen sleutels in bestanden; `.env`-bestanden genegeerd | API-sleutels zichtbaar in code of geschiedenis |
| Commitgeschiedenis | Betekenisvolle berichten, kleine wijzigingen | Enorme commits met het label "fixes" |

U kunt uw AI-tool ook vragen de architectuur uit te leggen: "Beschrijf hoe authenticatie, datatoegang en betalingen in dit project werken, en waar elk onderdeel is geïmplementeerd." Een samenhangend antwoord dat overeenkomt met wat u ziet, wijst op een samenhangende codebase. Een vaag of tegenstrijdig antwoord is op zichzelf al een signaal.

## Geautomatiseerde Tools

Verschillende tools meten automatisch aspecten van kwaliteit:

- **Typecontrole en linting** vangen hele categorieën bugs en inconsistenties af. Een TypeScript-project met veel typefouten of uitgeschakelde controles is een waarschuwingsteken.
- **Testrunners en coveragerapporten** laten zien of tests bestaan en draaien. Coveragepercentages alleen bewijzen geen kwaliteit, maar nul coverage op kritieke code zegt veel.
- **Dependency-scanners** in GitHub of andere platforms markeren packages met bekende kwetsbaarheden.
- **Secret scanning** detecteert gecommitte inloggegevens.
- **Lighthouse en PageSpeed Insights** meten frontendprestaties en basisprincipes van toegankelijkheid.
- **Database-advisors** in Supabase wijzen op ontbrekende indexen en beveiligingsproblemen zoals tabellen zonder Row Level Security.
- **Supply chain-scoring** zoals OpenSSF Scorecard helpt de gezondheid van afhankelijkheden te beoordelen.

Voer ze uit en kijk naar de trend door de tijd, niet alleen naar één momentopname.

## Waarschuwingssignalen Die een Expertreview Rechtvaardigen

- Elk falen van de test met twee accounts
- API-sleutels of service role keys in frontendcode of de git-geschiedenis
- Betalingen die worden bevestigd via redirects in plaats van webhooks
- Helemaal geen tests op authenticatie, betalingen of datatoegang
- Dezelfde functie op meerdere inconsistente manieren geïmplementeerd
- Fouten die worden afgevangen en genegeerd, terwijl de interface toch succes toont
- Wijzigingen aan het databaseschema buiten migraties om
- Een groeiende lijst bugs die terugkomen nadat ze zijn opgelost
- Niemand, ook de AI-tool niet, kan duidelijk uitleggen hoe een kritieke functie werkt

## Waarom Kwaliteit Mettertijd Achteruitgaat

Codebases die met AI worden gebouwd, hebben de neiging af te drijven. Elke sessie lost de directe prompt op, soms door code te dupliceren, een nieuwe library toe te voegen of een bestaand patroon te omzeilen. Na maanden bevat het project meerdere manieren om data op te halen, meerdere stijlen van foutafhandeling en meerdere datumlibraries. Elke inconsistentie maakt de volgende wijziging riskanter.

De remedie is structuur:

- **Projectinstructies** die de architectuur, conventies en beveiligingsregels beschrijven, die tools zoals Cursor, Claude Code en Lovable kunnen volgen
- **Tests voor kritiek gedrag,** vooral toegangscontrole en betalingen
- **Geautomatiseerde controles** die bij elke wijziging draaien
- **Periodiek opruimen,** dubbele patronen samenvoegen en ongebruikte code en afhankelijkheden verwijderen
- **Reviews van wijzigingen** in beschermde gebieden zoals authenticatie, betalingen en migraties

## Vragen om aan Uw AI-Tool te Stellen

AI-codeertools kunnen helpen hun eigen output te beoordelen als u precieze vragen stelt. Ze vervangen geen onafhankelijke review, omdat ze dezelfde blinde vlekken hebben, maar ze kunnen snel problemen aan het licht brengen:

- "Noem elke tabel die klantdata bevat en de Row Level Security-policies op elke tabel."
- "Welke API-endpoints of server actions lezen of schrijven data, en hoe controleert elk dat de gebruiker toegang mag hebben?"
- "Waar worden geheimen en API-sleutels gebruikt, en zijn er sleutels zichtbaar voor de browser?"
- "Hoe worden betalingsbevestigingen verwerkt, en wat gebeurt er als een webhook twee keer wordt afgeleverd?"
- "Welke delen van de code hebben geen tests?"
- "Zoek plekken waar fouten worden afgevangen maar niet aan de gebruiker worden gemeld."
- "Noem afhankelijkheden die ongebruikt zijn of elkaar dupliceren."

Vergelijk de antwoorden met wat u in de gedragstests ziet. Tegenstrijdigheden zijn waardevolle bevindingen.

## Kwaliteit Is een Trend, Geen Momentopname

Eén review legt de toestand van een codebase op één dag vast. Belangrijker is of de kwaliteit verbetert of verslechtert met elke wijziging. Volg een paar eenvoudige indicatoren door de tijd: het aantal openstaande bugs, hoe vaak opgeloste bugs terugkomen, de tijd die nodig is om een kleine functie te leveren, het faalpercentage van CI en het aantal afhankelijkheden. Bewegen die in de verkeerde richting, dan bouwt de codebase sneller schuld op dan u afbetaalt, en is het tijd om in structuur te investeren.

## Een Onafhankelijk Oordeel Krijgen

De opties verschillen in kosten en diepgang:

| Optie | Wat u krijgt | Wanneer het past |
| --- | --- | --- |
| Ervaren bevriende developer | Informele blik, snelle waarschuwingssignalen | Vroege validatie |
| Freelance codereview | Schriftelijke bevindingen voor een vaste scope | Vóór een lancering of demo |
| Gespecialiseerde AI-code-audit | Gestructureerde review van beveiliging, datatoegang, betalingen, deployment | Vóór productie, enterprise-deals of financiering |
| Fractional CTO | Doorlopende begeleiding en reviews | Groeiende teams |

Onze gids over [wat een audit van AI-gegenereerde code omvat](https://launchstudio.eu/nl/blog/ai-generated-code-audit-what-a-vibe-code-audit-covers) legt een gestructureerde review in detail uit.

## De Kosten van Slechte Code

Slechte code faalt zelden in één keer. Het uit zich in tragere ontwikkeling, terugkerende bugs, supportdruk, beveiligingsincidenten, gemiste enterprise-deals, moeilijke werving omdat developers niet in de codebase willen werken en pijnlijke due diligence. Vroeg investeren in kwaliteit, ook bescheiden, is veel goedkoper dan later opnieuw bouwen.

## Hoe LaunchStudio Helpt

LaunchStudio reviewt door AI geschreven codebases en repareert wat telt voor productie: toegangscontrole, geheimen, betalingen, foutafhandeling, datamodel, prestaties, tests, CI-controles en deployment. We schrijven ook projectinstructies en voegen vangrails toe, zodat toekomstige wijzigingen met AI de kwaliteit behouden waarvoor u hebt betaald.

Het **Launch Ready**-pakket (€800-€3.500) omvat een productiereview met kritieke fixes, deployment en 48 uur support; **Launch & Grow** (€2.500-€7.500 plus €49 per maand) voegt beheerde hosting, monitoring en prioriteitssupport toe. Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een schatting.

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, 160+ opgeleverde projecten en 120+ engineers, dat codebases reviewt en onderhoudt voor enterpriseklanten zoals Vodafone en TNO. Oprichters ontmoeten het team aan de Herengracht 420 in Amsterdam; de engineering gebeurt in het ontwikkelcentrum aan de Pho Quang Street in Ho Chi Minh City, met een hub aan de Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Oprichter Die de Test met Twee Accounts Deed Voordat Haar Investeerder Dat Deed

Nadia Visser bouwde Huisartsplanner met Lovable en Supabase: een planningstool waarmee doktersassistenten terugbellijsten en afspraakslots beheren. Met een seed-investeerder die interesse had, wilde ze weten of de code de technische review zou doorstaan die de investeerder van plan was. Ze kon de code niet lezen, dus begon ze met de gedragstests.

De test met twee accounts faalde meteen: een assistent van de ene praktijk kon de terugbellijst van een andere praktijk openen door een ID in de URL te veranderen. De fouttest liet zien dat het opslaan van een slot zonder verbinding een succesmelding toonde terwijl er niets werd opgeslagen. In GitHub vond ze geen README, geen tests, twee verschillende datumlibraries, een componentbestand van 2.800 regels en een Supabase service role key in een vroege commit. Toen ze Lovable vroeg uit te leggen hoe de toegangscontrole werkte, beschreef het antwoord policies die op verschillende tabellen niet bestonden.

LaunchStudio bevestigde en breidde de bevindingen uit in een gestructureerde review, en repareerde ze daarna: Row Level Security per praktijk op alle tabellen met negatieve autorisatietests, eerlijke foutafhandeling met nieuwe pogingen voor niet-opgeslagen wijzigingen, rotatie van de blootgestelde sleutel en verwijdering uit de geschiedenis, samenvoeging tot één datumlibrary, het opsplitsen van het grote component en een README met instructies voor setup, testen en deployment. CI-controles voor types, tests, geheimen en afhankelijkheden werden toegevoegd, en projectinstructies legden de architectuur en beveiligingsregels vast voor toekomstige Lovable-sessies.

**Resultaat:** Toen de technisch adviseur van de investeerder drie weken later de repository reviewde, bevatte het rapport alleen kleine bevindingen. De ronde werd gesloten, en Nadia voert haar zes gedragstests nu opnieuw uit vóór elke grote release.

> *"Ik kon de code niet lezen, maar ik kon testen wat hij deed. Dat vertelde me genoeg om te weten dat ik hulp nodig had voordat iemand anders de problemen vond."*
> - **Nadia Visser, Oprichter, Huisartsplanner (Haarlem)**

**Kosten & Doorlooptijd:** €3.300 (Launch Ready-pakket: gestructureerde review, fixes in toegangscontrole, foutafhandeling, rotatie van geheimen, refactoring, README, CI-controles en AI-instructies) - afgerond in 9 werkdagen.

## Veelgestelde Vragen

### Kan een niet-technische oprichter door AI geschreven code beoordelen?

Gedeeltelijk. Gedragstests, zoals testen met twee accounts, ongebruikelijke invoer, offline opslaan en mobiel gebruik, onthullen veel ernstige problemen zonder code te lezen. Signalen in de repository en geautomatiseerde tools voegen meer toe. Voor beveiliging en architectuur blijft een onafhankelijke expertreview vóór de lancering aan te raden.

### Is door AI geschreven code slechter dan code geschreven door developers?

Niet per definitie. AI-tools schrijven vaak snel code die er netjes uitziet. De risico's komen voort uit volume, inconsistentie en blinde vlekken in beveiliging en randgevallen, gecombineerd met de neiging van oprichters om werkende demo's te vertrouwen. Systematisch testen en reviewen pakt die risico's aan.

### Hoe vaak moet ik mijn code laten reviewen?

Op cruciale momenten: vóór de lancering, voordat u belangrijke zakelijke klanten onboardt, vóór financiering of een overname, en na grote AI-gegenereerde wijzigingen in gevoelige gebieden. Daartussen moeten geautomatiseerde controles bij elke wijziging draaien.

### Hoe helpt de ervaring van Manifera bij het beoordelen van codekwaliteit?

Manifera reviewt, onderhoudt en neemt al 11+ jaar codebases over voor enterpriseklanten. LaunchStudio past die ervaring toe op door AI geschreven code, met de nadruk op de eigenschappen die voor een bedrijf tellen: beveiliging, correctheid, onderhoudbaarheid en betrouwbaarheid.

### Heeft codekwaliteit invloed op SEO en zichtbaarheid in AI?

Indirect wel. Goede code levert snelle, stabiele, toegankelijke pagina's met correcte rendering en structuur, die zoekmachines en AI-antwoordmachines betrouwbaar kunnen crawlen en citeren. Slechte code veroorzaakt trage pagina's, fouten en downtime die de zichtbaarheid schaden.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan een niet-technische oprichter door AI geschreven code beoordelen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Gedeeltelijk, via gedragstests, signalen in de repository en geautomatiseerde tools; een expertreview blijft vóór de lancering aan te raden." }
    },
    {
      "@type": "Question",
      "name": "Is door AI geschreven code slechter dan code geschreven door developers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Niet per definitie; risico's komen voort uit volume, inconsistentie en blinde vlekken, aan te pakken met testen en reviewen." }
    },
    {
      "@type": "Question",
      "name": "Hoe vaak moet ik mijn code laten reviewen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Vóór de lancering, grote klanten, financiering en na grote AI-wijzigingen, met geautomatiseerde controles daartussen." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij het beoordelen van codekwaliteit?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera reviewt al 11+ jaar enterprise-codebases en LaunchStudio richt zich op beveiliging, correctheid en onderhoudbaarheid." }
    },
    {
      "@type": "Question",
      "name": "Heeft codekwaliteit invloed op SEO en zichtbaarheid in AI?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirect, via snelle, stabiele, toegankelijke pagina's die crawlers kunnen bereiken." }
    }
  ]
}
</script>
