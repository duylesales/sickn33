---
Titel: "Wat er is veranderd in Lovable, Bolt en Cursor sinds hun eerste release — een functietijdlijn"
Trefwoorden: ai coding, lovable bolt cursor comparison, ai coding tools history, ai code editor features
Koperfase: Bewustzijn
Doelgroep: Technische solo-oprichter
---
# Wat er is veranderd in Lovable, Bolt en Cursor sinds hun eerste release — een functietijdlijn

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wat er is veranderd in Lovable, Bolt en Cursor sinds hun eerste release — een functietijdlijn",
  "description": "Een tijdlijn van hoe Lovable, Bolt en Cursor zich hebben ontwikkeld sinds hun lancering, en waarom het najagen van de nieuwste functies halverwege een project stilletjes kan breken wat u al hebt gebouwd.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-26",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-bolt-cursor-feature-timeline" }
}
</script>

De AI-codeertools waarmee oprichters vandaag bouwen, lijken nauwelijks meer op wat er in hun eerste publieke versies verscheen. Lovable begon als een vrij smalle prompt-naar-frontend-generator. Bolt lanceerde als een in-browser, full-stack scaffoldingtool gebouwd op WebContainers. Cursor begon als een fork van VS Code met inline AI-suggesties erbovenop. Alle drie hebben sindsdien naar dezelfde bestemming gerend — full-stack app-generatie met deployment, database en agent-achtige meerstaps-bewerking — maar ze kwamen er via verschillende tijdlijnen, met verschillende afwegingen, en oprichters die vroeg zijn begonnen, beseffen vaak niet hoeveel de grond onder een tool die ze nog steeds gebruiken, is verschoven.

Dit is om een heel praktische reden belangrijk: oprichters wisselen halverwege een bouwproces voortdurend van tool, op jacht naar welke tool die week net de functie heeft uitgebracht die ze nodig hebben. Dat is een redelijke instinctieve reactie. Het is ook precies hoe projecten stilletjes kapotgaan.

## Lovable: van frontend-generator naar full-stack platform

De vroegste versies van Lovable richtten zich op het genereren van schone, bewerkbare React-frontends op basis van natuurlijke-taalprompts, met sterke nadruk op ontwerpkwaliteit en iteratief visueel bewerken. Backend- en database-ondersteuning kwamen later, gevolgd door strakkere integraties voor authenticatie en gehoste deployment. Elke uitbreiding maakte Lovable geschikter om een complete app in één tool te produceren — maar het betekende ook dat de onderliggende projectstructuur van release tot release veranderde, wat ertoe doet als u vroeg iets hebt gebouwd en verwacht dat nieuwere Lovable-conventies er naadloos in passen.

## Bolt: eerst WebContainers, later agentische workflows

Bolts kenmerkende vroege functie was het draaien van een volledige ontwikkelomgeving rechtstreeks in de browser via WebContainers, waardoor u een live app kon zien zonder lokale installatie. In latere releases voegde Bolt meer autonome meerstapsplanning toe, betere ondersteuning voor frameworks buiten de aanvankelijke standaardinstellingen, en een verbeterde verwerking van grotere codebases die eerder vastliepen op het contextvenster. De afweging: projecten gebouwd op een vroege versie van Bolt dragen soms structurele aannames met zich mee — bestandsindeling, dependency-keuzes — die latere Bolt-versies niet meer op dezelfde manier genereren.

## Cursor: van autocomplete naar autonome agent

Cursors traject kende de meest dramatische verschuiving in *reikwijdte*. Het begon als een editor met sterke inline-aanvullingen en chatgebaseerde codeuitleg — een tool die een mens ondersteunde die nog steeds zelf aan het stuur zat. Latere releases introduceerden steeds autonomere 'agent'-modi, in staat om meerstaps- en meerbestandswijzigingen te plannen en uit te voeren met minimaal toezicht. Dat is een fundamenteel andere werkrelatie dan waar Cursor mee begon, en oprichters die de tool in zijn vroegere, meer begeleide vorm hebben leren kennen, beseffen soms niet hoeveel meer de nieuwere agentmodus zelfstandig kan veranderen — inclusief logica die zij met de hand hebben geschreven en nooit hebben gevraagd aan te raken.

## Het patroon bij alle drie: mogelijkheden groeien sneller dan compatibiliteit

De rode draad is niet welke tool de "beste" is — het is dat alle drie hun reikwijdte sneller hebben uitgebreid dan dat ze achterwaartse compatibiliteit met projecten op eerdere versies hebben gegarandeerd. Nieuwe functies krijgen echte engineering-investering. Ervoor zorgen dat uw project van zes maanden oud netjes migreert naar de nieuwe conventies, krijgt minder. Precies daar lopen oprichters vast: ze jagen een nieuwe mogelijkheid na, en iets dat stilletjes afhankelijk was van de oude structuur stopt met werken, soms zonder ergens een foutmelding te tonen.

LaunchStudio wordt ondersteund door Manifera — vertrouwd door zakelijke klanten waaronder Vodafone, TNO en CFLW — en ons engineeringteam, met een hub in Singapore die deze tools nauwlettend volgt over verschillende tijdzones heen, besteedt echte tijd aan het begrijpen van wat er tussen AI-toolversies is veranderd, juist omdat oprichters ons projecten brengen die zich over twee tijdperken van dezelfde tool uitstrekken. Als uw project een toolwissel of een grote versiesprong heeft doorgemaakt, [krijg dan een gratis beoordeling van uw prototype](https://launchstudio.eu/en/#contact) voordat u er per ongeluk achter komt wat er kapot is gegaan. U kunt ook zien hoe Manifera denkt over [langetermijn-webapplicatieontwikkeling](https://www.manifera.com/services/web-app-develop/) voorbij de releasecyclus van welke AI-tool dan ook.

## Echt voorbeeld

### Een AI-native oprichter in actie: de login die de verhuizing niet overleefde

Joost Bakker, een oprichter uit Deventer, bouwde "RouteMeter," een logistieke trackingtool, in Bolt. Halverwege bracht Cursor een reeks functies uit die precies leken op wat RouteMeter nodig had — betere meerbestands-agentbewerking, strakkere framework-ondersteuning. Joost besloot het project halverwege de bouw van Bolt naar Cursor te migreren, waarbij hij de bestaande codebase meenam en de ontwikkeling daar voortzette.

De migratie zag er aan de oppervlakte schoon uit. De app draaide, de UI werd gerenderd, nieuwe functies werden toegevoegd zonder duidelijke fouten. Wat Joost niet opmerkte, was dat zijn aangepaste authenticatielogica — met de hand geschreven bovenop Bolts oorspronkelijke scaffolding om een specifieke multi-rol-inlogstroom voor chauffeurs en dispatchers af te handelen — niet netjes vertaalde naar Cursors conventies. Een deel van de sessiebeheerlogica raakte tijdens de overgang stilletjes niet meer correct gekoppeld. Er stortte niets in. Er verscheen nergens een zichtbare foutmelding. Het betekende simpelweg dat een deel van de gebruikers niet meer kon inloggen.

Hij kwam erachter toen een klant belde om te zeggen dat hun dispatcher het dashboard niet kon bereiken. LaunchStudio traceerde de breuk naar de migratie zelf: de authenticatielogica bestond nog in de codebase, maar was niet meer gekoppeld aan de routes die deze nodig hadden — een slachtoffer van twee tools die authenticatie anders structureren. Onze technici herstelden de koppeling tussen de authenticatielogica en de betrokken routes, en voegden vervolgens integratietests toe die specifiek elke inlogrol dekken, zodat een toekomstige toolwissel niet stilletjes hetzelfde opnieuw kan breken.

**Resultaat:** RouteMeters multi-rol-login heeft nu geautomatiseerde testdekking die de oorspronkelijke breuk zou hebben opgevangen voordat een klant dat deed.

> *"Ik ging ervan uit dat een werkende app een werkende migratie betekende. Ik dacht er niet aan om de ene stroom te testen die ik zelf al weken niet had gebruikt."*
> — **Joost Bakker, oprichter, RouteMeter (Deventer)**

**Kosten en tijdlijn:** € 700 (migratieaudit en herstel van de authenticatiestroom) — voltooid in 3 werkdagen.

---

## Veelgestelde vragen

### Is het risicovol om halverwege een project van AI-codeertool te wisselen?

Dat kan, vooral voor aangepaste logica die u zelf bovenop de scaffolding van de oorspronkelijke tool hebt geschreven — nieuwere tools behouden conventies niet altijd op dezelfde manier, en breuken kunnen stil zijn in plaats van foutmeldingen te geven.

### Welke AI-codeertool is sinds de lancering het meest veranderd?

Alle drie zijn aanzienlijk uitgebreid, maar Cursors verschuiving van inline-autocomplete naar autonome meerbestands-agentbewerking vertegenwoordigt de grootste verandering in hoeveel de tool zelfstandig doet, zonder direct toezicht.

### Hoe weet ik of een toolmigratie iets heeft kapotgemaakt?

Handmatig elke gebruikersrol en workflow end-to-end testen is de enige betrouwbare manier — geautomatiseerde integratietests, die de technici van LaunchStudio toevoegen tijdens productiebeoordelingen, vangen dit voortaan permanent op.

### Volgt het team van Manifera updates bij alle grote AI-codeertools?

Ja. Technici in de vestigingen van Manifera, waaronder de hub in Singapore, volgen releasewijzigingen in Lovable, Bolt, Cursor en v0 juist omdat oprichters projecten inbrengen die meerdere toolversies overspannen.

### Moet ik een project afmaken in de tool waarin ik het ben begonnen?

Over het algemeen wel, tenzij er een specifieke mogelijkheid ontbreekt — en als u wel wisselt, is een volledige regressietest van bestaande aangepaste logica essentieel voordat u de migratie als voltooid beschouwt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Is it risky to switch AI coding tools mid-project?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, especially for custom logic hand-written on top of the original tool's scaffolding, since newer tools don't always preserve conventions and breaks can be silent." } },
    { "@type": "Question", "name": "Which AI coding tool has changed the most since launch?", "acceptedAnswer": { "@type": "Answer", "text": "Cursor's shift from inline autocomplete to autonomous multi-file agent editing is the biggest change in scope among the major tools." } },
    { "@type": "Question", "name": "How do I know if a tool migration broke something?", "acceptedAnswer": { "@type": "Answer", "text": "Manually testing every user role and workflow end-to-end, then adding automated integration tests, is the reliable way to catch silent breaks." } },
    { "@type": "Question", "name": "Does Manifera's team track updates across all major AI coding tools?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, engineers across Manifera's offices, including the Singapore hub, follow release changes across Lovable, Bolt, Cursor, and v0." } },
    { "@type": "Question", "name": "Should I finish a project in the tool I started it in?", "acceptedAnswer": { "@type": "Answer", "text": "Generally yes unless there's a specific missing capability, and any switch should be followed by a full regression test of existing custom logic." } }
  ]
}
</script>
