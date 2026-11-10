---
Titel: "Claude Code-App naar Productie: Launch Service voor Agent-Gebouwde Apps"
Trefwoorden: claude code app naar productie, claude code developer, claude code project opleveren, agent gebouwde app review, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Claude Code-App naar Productie: Launch Service voor Agent-Gebouwde Apps

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Claude Code-App naar Productie: Launch Service voor Agent-Gebouwde Apps",
  "description": "Claude Code kan een complete applicatie schrijven vanuit een terminal, maar het naar productie brengen van een Claude Code-app vereist review van wat de agent zelfstandig heeft besloten: toegangscontrole, geheimen, datamodel, tests, deployment en monitoring. Deze gids legt de risico's uit, het reviewproces en hoe LaunchStudio door agents gebouwde apps oplevert tegen een vaste prijs.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-04-18",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/claude-code-app-to-production-launch-service-for-agent-built-apps" },
  "citation": [
    { "@type": "CreativeWork", "name": "Claude Code overview", "url": "https://docs.claude.com/en/docs/claude-code/overview" },
    { "@type": "CreativeWork", "name": "Veracode 2025 GenAI Code Security Report", "url": "https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021", "url": "https://owasp.org/Top10/" },
    { "@type": "CreativeWork", "name": "Perry et al., Do Users Write More Insecure Code with AI Assistants?", "url": "https://arxiv.org/abs/2211.03622" }
  ]
}
</script>

Claude Code heeft veranderd wat een gedreven oprichter in zijn eentje kan bouwen. U beschrijft een feature in uw terminal, de agent leest uw repository, schrijft bestanden in zowel de frontend als de backend, voert commando's uit, lost zijn eigen testfouten op en commit het resultaat. Binnen een paar weekenden heeft u iets dat eruitziet en functioneert als een volwaardig product: registratie, dashboards, een API, wellicht een betaalstroom.

De moeilijkheid zit niet in het genereren van code. Het zit in het weten of de code die een agent namens u schreef veilig is om voor te leggen aan vreemden die u gaan betalen. Een Claude Code-app naar productie brengen is grotendeels een reviewklus: het opsporen van beslissingen die de agent stilletjes heeft genomen, die toetsen aan de manieren waarop productiesoftware in de praktijk faalt, en de gaten dichten zonder het geleverde werk weg te gooien.

Deze gids legt uit waar door agents gebouwde apps doorgaans tekortschieten, wat een launch service controleert, wat het kost en hoe u beoordeelt of uw project klaar is voor lancering.

## Belangrijkste Punten

- **Claude Code schrijft meer van het systeem dan builders in de browser.** De agent raakt de backend, de database, infrastructuurbestanden en tests aan, dus de review moet al die onderdelen bestrijken, niet alleen de gebruikersinterface.
- **Agents optimaliseren voor "de taak slaagt", niet voor "het systeem is veilig".** Toegangscontrole, de omgang met geheimen en foutafhandeling zijn de gebieden waar agent-geschreven code het vaakst correctie behoeft.
- **Onafhankelijk onderzoek onderstreept voorzichtigheid.** De analyse van Veracode uit 2025 van meer dan 100 taalmodellen vond beveiligingszwaktes in ongeveer 45% van de gegenereerde codevoorbeelden, en gebrekkige toegangscontrole blijft het grootste risico in de OWASP Top 10.
- **Een gerichte launch review verloopt snel.** LaunchStudio brengt een Claude Code-project doorgaans binnen één tot drie weken naar productie, tegen een vaste prijs tussen €800 en €7.500.
- **U behoudt uw workflow met de agent.** Na de lancering kunt u blijven bouwen met Claude Code, dankzij vangrails die voorkomen dat nieuwe sessies het beveiligingswerk ongedaan maken.

## Waarom Door Agents Gebouwde Apps Anders Zijn Dan Builder-Apps

Builders in de browser zoals Lovable of Bolt maken de meeste architectuurkeuzes voor u: een React-frontend, een backend op Supabase of een gehost platform, en een vast deploymentpad. Dat brengt beperkingen met zich mee, maar het is tegelijkertijd voorspelbaar. Iedereen die veel Lovable-apps heeft gereviewd, weet precies waar te kijken.

Claude Code werkt wezenlijk anders. Volgens Anthropics eigen documentatie opereert het rechtstreeks in uw codebase en uw terminal: het kan bestanden bewerken, shellcommando's uitvoeren, commits aanmaken en elk willekeurig framework gebruiken dat u of de agent kiest. Die vrijheid is precies waarom oprichters er zo enthousiast over zijn. Het is tevens de reden waarom geen twee Claude Code-projecten op elkaar lijken. De ene oprichter eindigt met Next.js en Prisma op Vercel, de ander met een Python FastAPI-service en een Postgres-container, en een derde met een monorepo die beide combineert.

Het gevolg voor productie is simpel: de reviewer kan niet terugvallen op een vast sjabloon. Elke architectuurbeslissing die de agent heeft genomen, moet eerst in kaart worden gebracht en vervolgens worden beoordeeld. Typische vragen zijn:

- Welk framework en welke database heeft de agent gekozen, en waarom?
- Waar vindt de authenticatie plaats, en waar wordt de autorisatie afgedwongen?
- Welke omgevingsvariabelen bestaan er, en welke daarvan zijn geheime sleutels?
- Controleren de tests die de agent schreef echt gedrag, of bewijzen ze alleen dat code zonder foutmeldingen draait?
- Hoe wordt de app gedeployed, en kan een deployment eenvoudig worden teruggedraaid?

Oprichters zijn vaak verbaasd over hoeveel van deze vragen ze niet kunnen beantwoorden over hun eigen product. Dat is geen tekortkoming. De agent nam die beslissingen in luttele seconden terwijl u zich richtte op de functies.

## De Kwetsbaarheden Die We Het Vaakst Vinden in Claude Code-Projecten

Door agents geschreven code is vaak schoner dan mensen verwachten. De naamgeving is consistent, functies zijn compact, en er is commentaar aanwezig. De problemen zitten op plekken die er op het eerste gezicht prima uitzien.

| Gebied | Typische bevinding | Waarom het ertoe doet |
| --- | --- | --- |
| Autorisatie | Endpoints controleren of een gebruiker is ingelogd, maar niet of het record aan die gebruiker toebehoort | Elke gebruiker kan gegevens van een andere klant inzien of wijzigen door simpelweg een ID aan te passen |
| Geheimen | API-sleutels in gecommitte `.env`-bestanden, testscripts of standaardconfiguraties | Iedereen met toegang tot de repository, of met een gelekte kloon, bezit uw sleutels |
| Inputvalidatie | Validatie vindt uitsluitend plaats in het frontendformulier | Directe API-aanroepen omzeilen elke regel |
| Foutafhandeling | Brede `try/catch`-blokken die fouten inslikken en toch succes retourneren | Mislukte betalingen of databasebewerkingen lijken voor gebruikers succesvol afgerond |
| Tests | Tests die precies datgene nabootsen (mocken) wat getest moet worden | Groene testresultaten die niets bewijzen over het werkelijke gedrag in productie |
| Migraties | Databaseschema direct aangepast zonder versiebeheerde migratiebestanden | Productie- en lokale databases lopen geruisloos uit elkaar |
| Afhankelijkheden | Packages toegevoegd voor één enkele hulpfunctie, soms zonder onderhoud | Een groter aanvalsoppervlak en moeizame updates in de toekomst |
| Deployment | Handmatige deployment vanaf een laptop, zonder stagingomgeving | Elke release is een riskant live-experiment |

De rij over autorisatie verdient extra nadruk. OWASP noemt gebrekkige toegangscontrole (broken access control) het meest ernstige risico voor webapplicaties, en in hun gegevens uit 2021 vertoonde 94% van de geteste applicaties een vorm hiervan. Agents zijn bijzonder vatbaar voor deze fout, omdat de instructie "voeg een endpoint toe om een project bij te werken" al is voldaan zodra de update werkt voor de gebruiker die aan het testen is. Nergens in de prompt staat: "en zorg ervoor dat niemand anders dit kan aanroepen met het project-ID van een ander".

## Waarom "De Tests Slagen" Niet Voldoende Is

Claude Code is uitstekend in het itereren totdat alle tests slagen. Dat is waardevol, maar tegelijkertijd een valkuil. Als de agent zowel de code als de tests schrijft, weerspiegelen de tests het begrip van de agent van de taak - inclusief diens blinde vlekken.

Een onderzoek door Perry en collega's aan Stanford toonde aan dat softwareontwikkelaars die een AI-assistent gebruikten minder veilige code produceerden dan een controlegroep, terwijl ze juist méér vertrouwen hadden dat hun code veilig was. Diezelfde dynamiek geldt voor door agents geschreven tests: ze wekken vertrouwen zonder noodzakelijkerwijs veiligheid te creëren.

Bij een productiereview zoeken we naar drie soorten tests die agents zelden uit zichzelf schrijven:

1. **Negatieve autorisatietests.** Gebruiker A probeert via de API records van gebruiker B te lezen, bij te werken en te verwijderen. Elke poging moet gegarandeerd falen met een statuscode 403.
2. **Foutpadtests.** De betaalprovider heeft een time-out, de e-maildienst geeft een foutmelding, de database weigert een schrijfbewerking. De app moet een eerlijke foutmelding tonen en de data consistent achterlaten.
3. **Contracttests op externe diensten.** Webhook-payloads worden geverifieerd met echte handtekeningen, retries worden eenmalig verwerkt, en dubbele gebeurtenissen leiden nooit tot dubbele bestellingen.

Deze tests zijn niet exotisch. Ze vallen simpelweg buiten het kader van de meeste feature-prompts.

## Wat een Claude Code Launch Review Omvat

Een review door LaunchStudio van een door een agent gebouwde app volgt altijd dezelfde vaste volgorde, omdat die volgorde het werkelijke risico weerspiegelt.

**1. Architectuurkaart.** We documenteren wat de agent heeft gebouwd: services, database, hosting, externe API's en hoe gegevens daartussen stromen. U ontvangt deze kaart; het is vaak het eerste complete overzicht van uw eigen product.

**2. Toegangscontrole.** Elk endpoint, elke server action en elke databasequery die klantgegevens raakt, wordt gecontroleerd op eigendomsregels. Waar de database dit ondersteunt, zoals Postgres Row Level Security op Supabase, voegen we regels toe op databaseniveau als tweede verdedigingslinie.

**3. Geheimen en configuratie.** We doorzoeken de volledige git-geschiedenis, niet alleen de huidige bestanden, op gecommitte sleutels. Alles wat ooit zichtbaar is geweest, wordt geroteerd. De configuratie wordt opgesplitst in development, staging en productie, waarbij geheimen worden opgeslagen bij de hostingprovider en niet in de repository.

**4. Datamodel en migraties.** Wijzigingen in het schema worden ondergebracht in versiebeheerde migratiebestanden, er worden indexen toegevoegd voor query's die uw app daadwerkelijk uitvoert, en back-ups worden geconfigureerd en proefondervindelijk hersteld.

**5. Betalingen en integraties.** Webhooks worden gecontroleerd op cryptografische handtekeningen, idempotent gemaakt en gelogd. Mislukte betalingen, terugbetalingen en annuleringen volgen helder gedefinieerde paden.

**6. Tests die er echt toe doen.** We voegen de hierboven beschreven negatieve autorisatietests en foutpadtests toe, zodat toekomstige agentsessies beschikken over een vangnet dat aansluit op productierisico's.

**7. Deployment en monitoring.** Geautomatiseerde deployments vanaf uw main-branch, een stagingomgeving, foutopsporing (error tracking), uptime-notificaties en een rollbackprocedure die daadwerkelijk in de praktijk is getest.

## Claude Code na de Lancering in Uw Workflow Behouden

De meeste oprichters willen na de lancering blijven doorbouwen met de agent, en dat is volkomen terecht. Het doel is om dat veilig te maken. Drie praktische maatregelen bieden uitkomst:

- **Een projectinstructiebestand.** Claude Code leest instructiebestanden op projectniveau zoals `CLAUDE.md`. We voegen regels toe zoals "schakel nooit autorisatiecontroles uit", "alle schemawijzigingen verlopen via migraties" en "commit nooit omgevingsbestanden". De agent is erg bedreven in het volgen van schriftelijke afspraken.
- **Beschermde zones.** Beveiligingskritieke bestanden, zoals beleidsdefinities, middleware en betalingshandlers, worden gemarkeerd zodat wijzigingen daarin altijd een menselijke controle vereisen vóór een merge.
- **Doorlopende controles.** Geautomatiseerde tests en een secret scanner draaien op elke pull request. Als een agentsessie per ongeluk een autorisatietest breekt, wordt de deployment direct geblokkeerd.

Hierdoor behoudt u de bouwsnelheid waarvoor u Claude Code koos, terwijl het veel moeilijker wordt voor een nachtelijke sessie om een gedicht beveiligingslek opnieuw open te zetten.

## Claude Code-App naar Productie: Uw Opties Vergeleken

| Optie | Typische kosten | Typische doorlooptijd | Sterk punt | Belangrijkste risico |
| --- | --- | --- | --- | --- |
| Blijven prompten om de app "veilig te maken" | Uw eigen tijd | Open einde | Geen extra uitgaven | De agent beoordeelt zijn eigen blinde vlekken |
| Freelancer op uurbasis | €5.000 - €20.000 | 4 - 12 weken | Flexibel | Veel inwerktijd op onbekende agent-code, open-einde factuur |
| Traditioneel bureau | €20.000+ | 3 - 12 maanden | Volledige ontzorging | Stelt vaak voor om alles vanaf nul opnieuw te bouwen |
| LaunchStudio lancering met vaste scope | €800 - €7.500 | 1 - 3 weken | Behoudt uw code, vaste prijs | Niet bedoeld voor een compleet herontwerp van het product |

De agent vragen om zijn eigen werk te beveiligen is niet zinloos. Claude Code kan veel problemen vinden en repareren wanneer u er heel specifiek naar wijst. De beperking is dat iemand moet weten waar te wijzen, en die kennis ontstaat pas wanneer u heeft gezien hoe vergelijkbare systemen in productie onderuitgaan.

## Signalen Dat Uw Claude Code-Project Klaar Is Voor een Launch Review

U heeft geen review nodig op dag één. U heeft er een nodig wanneer echte gebruikers of echt geld op het punt staan binnen te komen. De signalen:

- U plant gebruikers uit te nodigen buiten uw eigen netwerk.
- U staat op het punt om betalingen om te schakelen van testmodus naar live-modus.
- Een zakelijke klant heeft gevraagd naar beveiliging, AVG/GDPR of de serverlocatie.
- U weet niet meer precies wat elk onderdeel van de codebase doet.
- Deployen voelt dermate riskant dat u het liever uitstelt vlak voor een demonstratie.

Wanneer drie van deze punten opgaan, is het goedkoopste moment voor een review nu, voordat live data en betalende klanten elke wijziging veel delicater maken.

## Wat Het Kost

LaunchStudio biedt twee duidelijke pakketten. **Launch Ready** (€800 - €3.500) omvat de beveiligingsreview en -reparaties, werkende authenticatie en datatoegang, tests, deployment naar uw eigen domein en 48 uur nazorg na de lancering. **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) voegt betalingen toe, managed hosting, back-ups, transactionele e-mail en prioritaire ondersteuning.

Door agents gebouwde projecten met één service en een beheerde database vallen meestal onder Launch Ready. Projecten met meerdere microservices, achtergrondtaken of complexe facturering vallen doorgaans onder Launch & Grow. U ontvangt een vaste offerte na een gesprek van 15 minuten en een korte blik op de repository, en die prijs verandert niet tussentijds. U kunt een eerste indicatie berekenen met onze [prijscalculator](https://launchstudio.eu/nl/#calculator).

## Wie Het Werk Uitvoert

LaunchStudio wordt aangedreven door Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring en meer dan 160 opgeleverde projecten voor klanten als Vodafone en TNO. Gesprekken met oprichters vinden plaats vanuit Herengracht 420 in Amsterdam; de engineering wordt uitgevoerd door Manifera's team in het ontwikkelcentrum aan Pho Quang Street in Ho Chi Minh City, met een regionale hub aan Tras Street in Singapore.

Manifera's oprichter en LaunchStudio CEO, Herre Roelevink, was medeoprichter van het cybersecuritybedrijf CyberDevOps, tegenwoordig CFLW Cyber Strategies. Die achtergrond bepaalt de volgorde van onze review: toegangscontrole en geheimen als eerste, al het andere daarna. Voor door agents gebouwde apps, waar het codevolume hoog is en beslissingen razendsnel zijn genomen, is die volgorde belangrijker dan ooit.

Wilt u de auditkant grondiger begrijpen? Onze gids over [wat een audit van AI-gegenereerde code inhoudt](https://launchstudio.eu/nl/blog/ai-generated-code-audit-what-a-vibe-code-audit-covers) behandelt elke categorie, en met de [vibe code audit checklist](https://launchstudio.eu/nl/blog/vibe-code-audit-checklist-25-checks-before-launch) kunt u zelf een eerste controle uitvoeren.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Offerte-Tool Waar Elke Vervoerder Elk Bod Kon Inzien

Joost Vermeulen werkte vijftien jaar in de expeditie in Venlo voordat hij besloot Vrachtbod te bouwen: een platform waarop verladers vrachten plaatsen en kleine transportbedrijven prijsopgaven indienen. Hij had nog nooit productiecode geschreven, maar kon goed overweg met een terminal. In twee maanden van avonduren bouwde Claude Code voor hem een Next.js-applicatie met een Postgres-database, een offertestroom, e-mailnotificaties en een Mollie-betalingsstap voor de platformkosten.

Een pilot met zes verladers en twintig vervoerders verliep voorspoedig, totdat een oplettende vervoerder opmerkte dat hij concurrerende biedingen kon zien door een cijfer in de URL aan te passen. Joost vroeg Claude Code om dit op te lossen. De agent voegde een controle toe aan de detailpagina van het bod, maar het achterliggende API-endpoint, evenals twee andere endpoints, retourneerde nog altijd elk bod aan iedere ingelogde gebruiker. Tijdens de review troffen we bovendien een Mollie API-sleutel aan in een gecommit seed-script, tests die de database volledig nabootsten, en productiedeployments die rechtstreeks vanaf Joosts laptop werden gestart.

LaunchStudio bracht de architectuur in kaart, voegde eigendomscontroles toe aan alle elf endpoints die bedrijfsdata teruggaven, en schakelde Postgres Row Level Security in als tweede verdedigingslaag. De gelekte sleutel werd geroteerd en de git-geschiedenis opgeschoond. De engineers schreven negatieve autorisatietests voor elke gebruikersrol, verplaatsten deployments naar een geautomatiseerde pipeline met een stagingomgeving, en voegden een `CLAUDE.md`-bestand toe met beveiligingsconventies zodat toekomstige agentsessies deze automatisch respecteren.

**Resultaat:** Vrachtbod ging negen werkdagen later opnieuw live voor de pilotgroep. In het daaropvolgende kwartaal dienden vervoerders circa 2.300 offertes in zonder enig beveiligingsincident, terwijl Joost vlot nieuwe features bleef uitrollen met Claude Code. De nieuwe autorisatietests blokkeerden tot twee keer toe een deployment die de biedingen onbedoeld weer zichtbaar had gemaakt.

> *"Claude Code heeft meer gebouwd dan ik ooit had kunnen bedenken. Wat ik nodig had, was iemand die me precies kon vertellen welke beslissingen van de agent ik kon vertrouwen."*
> - **Joost Vermeulen, Oprichter, Vrachtbod (Venlo)**

**Kosten & Doorlooptijd:** €3.200 (Launch Ready-pakket: toegangscontrole, opschonen van geheimen, tests, deployment-pipeline en monitoring) - afgerond in 9 werkdagen.

## Veelgestelde Vragen

### Kan LaunchStudio werken met elk framework dat Claude Code heeft gekozen?

Ja, binnen gangbare webstacks. De meeste Claude Code-projecten die we zien gebruiken TypeScript met Next.js, React of Node, of Python met FastAPI of Django, op Postgres. Mocht de agent voor een ongebruikelijke technologie hebben gekozen, dan bespreken we tijdens het kennismakingsgesprek of we dit kunnen ondersteunen, nog voordat er een offerte wordt uitgebracht.

### Vervangt u de code die Claude Code heeft geschreven?

Nee. Door agents geschreven code is vaak goed gestructureerd; de problemen schuilen in specifieke beslissingen daarbinnen. We lossen die risicovolle beslissingen op, voegen tests en infrastructuur toe, en laten goed werkende functies intact. Een herschrijving wordt alleen voorgesteld wanneer een onderdeel onmogelijk veilig te maken is, en altijd uitsluitend in overleg met u.

### Kan ik Claude Code blijven gebruiken na de launch review?

Ja. We richten projectinstructies, beschermde zones en geautomatiseerde checks in, zodat nieuwe agentsessies de beveiligingsconventies respecteren en niet stilletjes eerdere verbeteringen tenietdoen. Veel oprichters merken dat de agent na de review juist betrouwbaarder werkt, omdat de codebase nu duidelijke regels en tests bevat waarvan hij kan leren.

### Hoe helpt de ervaring van Manifera specifiek bij door agents gebouwde code?

Door agents gebouwde code faalt op exact dezelfde plekken als enterprisecode, maar dan sneller en in grotere volumes: toegangscontrole, geheime sleutels, data-integriteit en deployment. Manifera lost dit type problemen al meer dan 11 jaar op in enterprisesystemen, en LaunchStudio past die patroonherkenning toe op projecten van oprichters.

### Is een productierijpe app belangrijk voor zoekmachines en AI-zichtbaarheid?

Ja. Een stabiele app op uw eigen domein met HTTPS, snelle pagina's en betrouwbare uptime kan worden gecrawld, geïndexeerd en geciteerd door zoekmachines en AI-antwoordmachines. Preview-deployments en regelmatige uitval werken beide tegen, waardoor productierijpheid een absolute voorwaarde is voor online vindbaarheid.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan LaunchStudio werken met elk framework dat Claude Code heeft gekozen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, binnen gangbare webstacks zoals TypeScript met Next.js, React of Node, of Python met FastAPI of Django op Postgres. Ongebruikelijke keuzes bespreken we vooraf tijdens het introductiegesprek." }
    },
    {
      "@type": "Question",
      "name": "Vervangt u de code die Claude Code heeft geschreven?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. LaunchStudio repareert specifieke risicovolle beslissingen, voegt tests en infrastructuur toe en laat werkende features intact. Herschrijvingen gebeuren alleen als iets niet veilig te maken is, altijd na overleg." }
    },
    {
      "@type": "Question",
      "name": "Kan ik Claude Code blijven gebruiken na de launch review?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. We voegen projectinstructies, beschermde zones en geautomatiseerde checks toe, zodat nieuwe agentsessies de beveiligingsconventies netjes blijven volgen." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera specifiek bij door agents gebouwde code?",
      "acceptedAnswer": { "@type": "Answer", "text": "Door agents gebouwde code vertoont dezelfde kwetsbaarheden als enterprisecode: toegangscontrole, geheimen en deployment. Manifera repareert dit al 11+ jaar en brengt die ervaring naar projecten op oprichtersschaal." }
    },
    {
      "@type": "Question",
      "name": "Is een productierijpe app belangrijk voor zoekmachines en AI-zichtbaarheid?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Een stabiele app op een eigen domein met HTTPS, snelle laadtijden en stabiele uptime kan worden gecrawld en geciteerd, terwijl preview-deployments en storingen vindbaarheid schaden." }
    }
  ]
}
</script>
