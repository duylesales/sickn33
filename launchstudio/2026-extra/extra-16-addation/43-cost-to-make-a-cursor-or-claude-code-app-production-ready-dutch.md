---
Titel: "Wat Kost het om een App uit Cursor of Claude Code Productierijp te Maken?"
Trefwoorden: kosten cursor app productierijp, kosten lancering claude code app, vibe coded nextjs app productie, kosten ai gegenereerde codebase repareren, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Wat Kost het om een App uit Cursor of Claude Code Productierijp te Maken?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wat Kost het om een App uit Cursor of Claude Code Productierijp te Maken?",
  "description": "Een kostengids voor het productierijp maken van apps gebouwd met Cursor of Claude Code: gebruikelijke prijsranges, de problemen die vaak voorkomen in code-first AI-projecten zoals een inconsistente architectuur, eigen authenticatie, ontbrekende tests, wildgroei aan dependencies, omgang met omgevingen en deployment, wat elke fix inhoudt, doorlopende kosten en hoe u uw werkwijze met AI-codeertools daarna productief houdt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-09-07",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/cost-to-make-a-cursor-or-claude-code-app-production-ready" },
  "citation": [
    { "@type": "CreativeWork", "name": "Cursor documentation", "url": "https://docs.cursor.com/" },
    { "@type": "CreativeWork", "name": "Anthropic: Claude Code documentation", "url": "https://docs.anthropic.com/en/docs/claude-code/overview" },
    { "@type": "CreativeWork", "name": "Next.js: Deploying", "url": "https://nextjs.org/docs/app/building-your-application/deploying" },
    { "@type": "CreativeWork", "name": "OWASP Application Security Verification Standard", "url": "https://owasp.org/www-project-application-security-verification-standard/" }
  ]
}
</script>

**Kort antwoord:** Een app gebouwd met Cursor of Claude Code productierijp maken kost doorgaans €1.200 tot €2.000 voor een gerichte app met één stack en weinig integraties en €2.000 tot €3.500 voor een SaaS met authenticatie, betalingen en meerdere diensten, beide binnen Launch Ready, en €3.500 tot €7.500 binnen Launch & Grow als de codebase structureel moet worden geconsolideerd, migraties nodig heeft of enterprisefuncties. Code-first AI-projecten kosten doorgaans iets meer dan projecten in visuele builders van vergelijkbare omvang, omdat ze meer vrijheid hebben om uit elkaar te groeien: meerdere patronen voor dezelfde taak, eigen authenticatie en veel dependencies.

Cursor en Claude Code geven oprichters een ander soort kracht dan visuele builders. U werkt in een echte codebase, kiest uw eigen framework, database en hosting, en kunt bijna alles bouwen. Veel niet-technische oprichters hebben op deze manier indrukwekkende producten uitgebracht. De keerzijde is dat niets consistentie afdwingt. Na maanden aan sessies kan een codebase drie manieren bevatten om gegevens op te halen, twee authenticatieaanpakken, ongebruikte libraries, hard gecodeerde secrets in oude scripts en geen tests. Deze pagina legt uit wat het kost om dat om te zetten in een codebase waarmee u kunt lanceren en verder kunt bouwen.

## Belangrijkste Punten

- **Gebruikelijke kosten: €1.200-€3.500 binnen Launch Ready,** meer bij structurele consolidatie.
- **Code-first projecten verschillen meer** dan projecten in visuele builders, dus de review telt.
- **Gebruikelijke fixes:** authenticatie, toegangscontrole, secrets, dependencies, tests, omgevingen en deployment.
- **Uw AI-werkwijze blijft,** met projectregels die toekomstige sessies consistent houden.
- **De meeste projecten duren vijf tot tien werkdagen.**

## Kosten per Soort Project

| Soort project | Gebruikelijke stack | Indicatieve prijs | Duur |
| --- | --- | --- | --- |
| Gerichte webapp | Next.js of vergelijkbaar, Supabase, één hostingprovider | €1.200-€2.000 | 4-6 werkdagen |
| SaaS met betalingen en e-mails | Next.js, Supabase of PostgreSQL, Stripe of Mollie, e-mailprovider | €2.000-€3.500 | 6-10 werkdagen |
| App met een aparte backend | Frontend plus een API in Node, Python of iets anders, meerdere diensten | €2.500-€3.500, of Launch & Grow | 1-3 weken |
| Codebase die consolidatie nodig heeft | Gemengde patronen, meerdere databases of authenticatiesystemen, grote scope | Binnen Launch & Grow (€2.500-€7.500 plus €49 per maand) | 2-4 weken |

## Veelvoorkomende Problemen in Code-First AI-Projecten

| Probleem | Hoe het zich toont | Waarom het telt |
| --- | --- | --- |
| Inconsistente architectuur | Meerdere manieren om gegevens op te halen, invoer te valideren of fouten af te handelen | Bugs in het ene pad maar niet in het andere; moeilijk te beveiligen |
| Eigen of gemengde authenticatie | Zelfgebouwde sessies naast een provider, of twee providers | Risico op overname van accounts, kapotte logins |
| Ontbrekende autorisatiecontroles | API-routes die controleren of iemand is ingelogd, maar niet wie eigenaar is | Gebruikers kunnen bij gegevens van anderen |
| Secrets in code of geschiedenis | Sleutels in configuratiebestanden, scripts of oude commits | Blootgestelde inloggegevens |
| Wildgroei aan dependencies | Tientallen libraries, sommige ongebruikt of verouderd | Kwetsbaarheden, trage builds, grotere bundels |
| Geen tests | Elke wijziging kan ongemerkt iets breken | Terugval bereikt klanten |
| Verwarring rond omgevingen | Dezelfde sleutels voor ontwikkeling en productie, ontbrekende variabelen | Testacties raken livegegevens |
| Handmatige deployment | Deployen vanaf een laptop, geen pipeline | Inconsistente releases, geen terugdraaioptie |
| Database zonder migraties | Schema met de hand of met scripts gewijzigd | Staging en productie groeien uit elkaar |
| Geen logging of monitoring | Fouten alleen zichtbaar in de console van de browser | Problemen worden door klanten ontdekt |

## Wat de Prijs Omvat

Elk Launch Ready-project omvat een review van de productiegereedheid, de beveiligingsbasis, een controle van eigendom, een productieopzet met domein en HTTPS, back-ups, monitoring, de afgesproken fixes, een schriftelijke samenvatting, projectregels voor Cursor of Claude Code en 48 uur ondersteuning na de lancering. Bij code-first projecten omvatten de fixes doorgaans ook het consolideren van de authenticatie, het toevoegen van autorisatiecontroles aan elke route, het verplaatsen van secrets naar het beheer van omgevingsvariabelen en het roteren van blootgestelde secrets, het verwijderen van ongebruikte dependencies, het toevoegen van tests voor kritieke stromen, het inrichten van databasemigraties en het opzetten van een deploymentpipeline met previewomgevingen.

## Waarom Code-First Projecten Uit Elkaar Groeien

AI-codeerassistenten werken sessie voor sessie. Elke sessie lost de taak op die voorligt, met de aanpak die in die context het beste lijkt. Zonder sterke projectregels voegt de ene sessie een library toe om gegevens op te halen, schrijft een andere ruwe query's en gebruikt een derde weer een ander patroon. Authenticatie kan beginnen met een provider en later een eigen middleware krijgen die is geschreven om een bug op te lossen. Secrets worden in bestanden geplakt om iets snel te laten werken, en daarna vergeten.

Niets hiervan is een tekortkoming van de tools; ook menselijke teams groeien uit elkaar zonder afspraken en review. De oplossing is de afspraken vastleggen, de code ernaartoe consolideren en de AI-assistent duidelijke instructies geven, zodat toekomstige sessies dezelfde patronen volgen.

## Projectregels voor Uw AI-Assistent

Een van de waardevolste opleveringen voor gebruikers van Cursor en Claude Code is een set projectregels: instructies die de assistent in elke sessie leest. Cursor ondersteunt bestanden met projectregels en Claude Code leest bestanden met projectgeheugen zoals CLAUDE.md. We schrijven regels die uw architectuur beschrijven, de ene goedgekeurde manier om gegevens op te halen, hoe authenticatie en autorisatie werken, waar secrets staan, hoe u migraties schrijft, welke tests u draait en wat nooit mag, zoals servicesleutels blootstellen of databasepolicies uitschakelen. Oprichters melden telkens dat sessies voorspelbaarder worden zodra deze regels er zijn.

## Tests: Hoeveel Is Genoeg?

Oprichters maken zich soms zorgen dat tests toevoegen maanden werk betekent. Voor productiegereedheid is een gerichte set genoeg: tests voor authenticatie, autorisatie tussen gebruikers en organisaties, statuswijzigingen bij betalingen en de twee of drie routes die voor uw bedrijf het belangrijkst zijn. Die draaien bij elke wijziging automatisch in de pipeline. Ze vormen het vangnet waarmee u met AI-hulp snel kunt blijven bouwen zonder te breken wat al werkt.

## Doorlopende Kosten na de Lancering

Na de lancering betaalt u uw providers rechtstreeks: hosting zoals Vercel, Netlify of een containerplatform, uw database, e-mail, betalingen en AI-providers als uw app die gebruikt. Uw abonnement op Cursor of Claude loopt door als u blijft bouwen. Optionele doorlopende zorg via Launch & Grow kost €49 per maand voor monitoring, updates van dependencies, controles van back-ups en kleine fixes. Code-first projecten hebben vooral baat bij regelmatige updates van dependencies, omdat ze meestal meer libraries bevatten.

## De Prijs Laag Houden

- Deel de repository vroeg, zodat de review direct kan beginnen
- Verwijder experimenten, verlaten branches en ongebruikte mappen die u kent
- Zet de diensten en accounts die de app gebruikt op een lijst
- Beschrijf de gebruikerstypen en waar elk type bij mag
- Pauzeer grote nieuwe functies tijdens het project
- Noteer terugkerende bugs of onderdelen die kwetsbaar aanvoelen

## Consolideren of Herschrijven?

Als een codebase rommelig aanvoelt, kan herschrijven verleidelijk lijken. Voor de meeste apps gebouwd met AI die al werken, is consolideren goedkoper en veiliger: kies per onderwerp het beste bestaande patroon, breng de rest van de code daarnaartoe, verwijder wat ongebruikt is en voeg onderweg tests toe. Een herschrijving gooit werkend gedrag weg en duurt meestal veel langer dan verwacht. We raden alleen aan een specifiek deel te herschrijven als consolideren meer zou kosten, en dat leggen we uit voordat we beginnen.

## De Alternatieven Vergeleken

| Optie | Gebruikelijke kosten | Wat u krijgt |
| --- | --- | --- |
| Alleen doorgaan met uw AI-assistent | Uw tijd en abonnement | Fixes voor wat u weet te vragen; risico in onbekende gebieden |
| Freelance developer per uur | Per uur, totaal onzeker | Hulp bij gekozen problemen; kwaliteit wisselt |
| AI-tools voor code review | Maandabonnement | Geautomatiseerde opmerkingen bij wijzigingen; geen fixes of inrichting |
| LaunchStudio Launch Ready | €1.200-€3.500 vast | Review, fixes, inrichting, tests, regels, documentatie en ondersteuning |
| Volledige herschrijving door een bureau | Vaak vele malen hoger | Nieuwe code; meestal onnodig |

## Wat We van U Nodig Hebben

- Een kennismakingsgesprek van 15 minuten
- Toegang tot uw repository, inclusief de geschiedenis
- Toegang tot de accounts voor hosting, database, betalingen en e-mail
- Een beschrijving van gebruikers, rollen en belangrijke routes
- Tijd voor een controle op staging vóór de release

## Overzicht van Prijzen

| Pakket | Gebruikelijk code-first werk |
| --- | --- |
| Launch Ready (€800-€3.500) | Beveiliging, authenticatie, secrets, tests, pipeline, deployment, monitoring |
| Launch & Grow (€2.500-€7.500 plus €49 per maand) | Consolidatie, migraties, multi-tenancy, enterprisefuncties, doorlopende zorg |

Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een indicatie.

## Niet Inbegrepen

Launch Ready omvat geen nieuwe functies, herontwerpen, kosten van providers of een volledige herschrijving. Als delen van de codebase echt opnieuw moeten worden gebouwd, leggen we uit waarom en offreren we dat apart. Juridisch advies, certificeringen en geaccrediteerde penetratietests vallen buiten de scope.

## Secrets uit de Geschiedenis van de Repository Halen

Een veelvoorkomende bevinding in code-first projecten is een secret dat maanden geleden is gecommit en later is verwijderd. Het uit de huidige bestanden verwijderen haalt het niet uit de geschiedenis van de repository, waar iedereen met toegang, of iedereen die later toegang krijgt, het nog kan vinden. De veilige aanpak heeft twee stappen. Roteer eerst het secret bij de provider, zodat de oude waarde niet meer werkt; dat is de stap die het risico echt wegneemt. Schoon daarna, waar passend, de geschiedenis op en schakel het scannen op secrets in, zodat nieuwe lekken worden opgemerkt voordat ze worden gepusht. We doen beide, en zetten elke geroteerde sleutel in de overdracht, zodat u weet welke waarden zijn veranderd.

## Aparte Backends en Achtergrondprocessen

Sommige projecten in Cursor en Claude Code bevatten een aparte backend, zoals een API in Node of Python, of achtergrondprocessen voor imports, e-mails en AI-taken. Die voegen bewegende delen toe: nog een deployment, nog een set omgevingsvariabelen, nog een plek waar fouten optreden. Productiegereedheid voor deze projecten omvat voor elke dienst dezelfde basis: geauthenticeerde en geautoriseerde endpoints, secrets in het beheer van omgevingsvariabelen, logs en monitoring, health checks en een deploymentpipeline. Waar een aparte dienst alleen bestaat omdat een sessie hem heeft aangemaakt, raden we soms aan hem samen te voegen met de hoofdapp om kosten en complexiteit te verlagen. Die aanbeveling komt met een duidelijke uitleg en wordt nooit zonder uw goedkeuring uitgevoerd.

## Wat Er Verandert in Uw Dagelijkse Werkwijze

Na het project ziet uw dagelijkse werkwijze met Cursor of Claude Code er vertrouwd uit, maar veiliger. U werkt op een branch, de assistent volgt de projectregels, de pipeline draait tests en maakt een previewdeployment, en u voegt samen als het goed lijkt. Databasewijzigingen komen binnen als migraties en worden automatisch toegepast op staging en daarna op productie. Glipt er toch iets doorheen, dan waarschuwt de monitoring u en is terugdraaien één klik. Oprichters zeggen vaak dat ze na het project sneller bouwen, omdat ze minder tijd kwijt zijn aan het najagen van terugval.

## Waarom Oprichters voor LaunchStudio Kiezen

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, 160+ opgeleverde projecten en 120+ engineers, dat grote codebases onderhoudt voor klanten zoals Vodafone en TNO. Oprichters ontmoeten het team aan de Herengracht 420 in Amsterdam; de engineering gebeurt in het ontwikkelcentrum van Manifera aan de Pho Quang Street in Ho Chi Minh City, met een hub aan de Tras Street in Singapore. We consolideren in plaats van te herschrijven, houden uw product werkend en laten regels achter die van uw AI-assistent een betere medewerker maken.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Drie Manieren om In te Loggen

Floor Bakker heeft vanuit Utrecht een SaaS voor werving in de horeca, in acht maanden gebouwd met Cursor en later Claude Code, met Next.js, Supabase en Stripe. Restaurants plaatsen diensten en werkers reageren. De app had zo'n 300 bedrijven en 4.000 werkers, maar het aantal bugs nam toe en Floor durfde bepaalde bestanden niet meer aan te raken.

De review vond drie authenticatiepaden: Supabase Auth voor werkers, een eigen sessiesysteem voor bedrijven dat tijdens een debugsessie was geschreven en een oude route met magic links die nog bereikbaar was. Meerdere API-routes controleerden of een gebruiker was ingelogd, maar niet of de dienst bij diens bedrijf hoorde. Twee Stripe-sleutels stonden in een gecommit script, de repository bevatte 140 dependencies waarvan er zo'n 30 ongebruikt waren en er waren geen tests. Deployments gebeurden vanaf de laptop van Floor.

LaunchStudio offreerde €3.400 binnen Launch Ready. De authenticatie werd geconsolideerd op Supabase Auth, met migratie van bestaande bedrijfsaccounts, de oude route werd verwijderd en via een gedeelde helper kwamen er eigendomscontroles op elke API-route. Sleutels werden geroteerd en naar omgevingsvariabelen verplaatst, en de geschiedenis van de repository werd opgeschoond. Ongebruikte dependencies werden verwijderd en de rest bijgewerkt. Er kwamen tests voor inloggen, toegang tussen bedrijven, reacties en Stripe-webhooks. Een pipeline in GitHub zette previews en productie op Vercel live, met databasemigraties, en er werden projectregels geschreven voor zowel Cursor als Claude Code.

**Resultaat:** Het aantal bugmeldingen daalde in de twee maanden daarna merkbaar, en de buildtijden daalden met ongeveer een derde. Floor ging weer wekelijks bouwen; de tests blokkeerden twee wijzigingen die de toegang tussen bedrijven zouden hebben gebroken.

> *"Ik had een product gebouwd waar ik bang voor was. Nu heb ik een codebase met regels, en mijn AI-assistent volgt ze beter dan ik deed."*
> - **Floor Bakker, Oprichter, Shiftwerk (Utrecht)**

**Kosten & Doorlooptijd:** €3.400 (Launch Ready-pakket: consolidatie van authenticatie, eigendomscontroles, rotatie van sleutels, opschoning van dependencies, tests, pipeline, migraties en projectregels voor AI) - afgerond in 9 werkdagen.

## Veelgestelde Vragen

### Wat kost het om een app uit Cursor of Claude Code productierijp te maken?

Doorgaans €1.200 tot €3.500 binnen Launch Ready, afhankelijk van de stack, authenticatie, betalingen, integraties en hoe consistent de code is. Codebases die structurele consolidatie of migraties nodig hebben, worden binnen Launch & Grow afgebakend. U ontvangt een vaste offerte na een review van de repository.

### Waarom kunnen code-first projecten meer kosten dan projecten in Lovable of Bolt?

Omdat ze meer vrijheid hebben. Code-first projecten kunnen frameworks, authenticatiesystemen en patronen mengen, wat meer tijd kost om te reviewen en te consolideren. Visuele builders beperken de keuzes, waardoor hun problemen vaak voorspelbaarder zijn.

### Kan ik Cursor of Claude Code blijven gebruiken?

Ja. We werken in uw repository en voegen projectregels toe die beide tools lezen, met een beschrijving van uw architectuur en afspraken. Tests en een pipeline vangen wijzigingen op die kritiek gedrag zouden breken.

### Hoe helpt de ervaring van Manifera bij door AI gegenereerde codebases?

Manifera onderhoudt al 11+ jaar codebases over 160+ projecten met 120+ engineers, voor klanten zoals Vodafone en TNO. LaunchStudio past die engineeringpraktijken toe om door AI gegenereerde code te consolideren zonder werkende producten te herschrijven.

### Helpt een productierijpe codebase bij SEO en zichtbaarheid in AI?

Ja. Snellere builds, kleinere bundels, correcte weergave van openbare pagina's, goede metadata en minder fouten helpen zoekmachines om uw site te crawlen en te ranken. Een stabiel product levert ook de reviews en vermeldingen op die AI-antwoordmachines oppikken.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat kost het om een app uit Cursor of Claude Code productierijp te maken?",
      "acceptedAnswer": { "@type": "Answer", "text": "Doorgaans €1.200 tot €3.500 binnen Launch Ready, afhankelijk van de stack, authenticatie, betalingen, integraties en hoe consistent de code is. Codebases die structurele consolidatie of migraties nodig hebben, worden binnen Launch & Grow afgebakend." }
    },
    {
      "@type": "Question",
      "name": "Waarom kunnen code-first projecten meer kosten dan projecten in Lovable of Bolt?",
      "acceptedAnswer": { "@type": "Answer", "text": "Omdat ze meer vrijheid hebben. Code-first projecten kunnen frameworks, authenticatiesystemen en patronen mengen, wat meer tijd kost om te reviewen en te consolideren." }
    },
    {
      "@type": "Question",
      "name": "Kan ik Cursor of Claude Code blijven gebruiken?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. We werken in uw repository en voegen projectregels toe die beide tools lezen, met een beschrijving van uw architectuur en afspraken." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij door AI gegenereerde codebases?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera onderhoudt al 11+ jaar codebases over 160+ projecten met 120+ engineers, voor klanten zoals Vodafone en TNO. LaunchStudio past die engineeringpraktijken toe om door AI gegenereerde code te consolideren zonder werkende producten te herschrijven." }
    },
    {
      "@type": "Question",
      "name": "Helpt een productierijpe codebase bij SEO en zichtbaarheid in AI?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Snellere builds, kleinere bundels, correcte weergave van openbare pagina's, goede metadata en minder fouten helpen zoekmachines om uw site te crawlen en te ranken." }
    }
  ]
}
</script>
