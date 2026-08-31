---
Titel: "Praktijkvoorbeeld: Een B2B SaaS-Oprichter Voegt Rolgebaseerde Toegangscontrole Toe Vóór Haar Eerste Enterprise-Klant"
Trefwoorden: rolgebaseerde toegangscontrole SaaS, RBAC-implementatie, enterprise toegangscontrole, multi-rol SaaS, beheerderspaneel rechten, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: SaaS-Oprichter Scale-Up
---

# Praktijkvoorbeeld: Een B2B SaaS-Oprichter Voegt Rolgebaseerde Toegangscontrole Toe Vóór Haar Eerste Enterprise-Klant

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Praktijkvoorbeeld: Een B2B SaaS-Oprichter Voegt Rolgebaseerde Toegangscontrole Toe Vóór Haar Eerste Enterprise-Klant",
  "description": "Een enterprise-prospect zei ja — op voorwaarde van rolgebaseerde toegangscontrole die het prototype niet had. Hoe LaunchStudio RBAC implementeerde in 8 dagen zonder de met Lovable gebouwde frontend van de oprichter aan te raken.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-12-31",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/b2b-saas-role-based-access-control-case-study" }
}
</script>

De enterprise-prospect zei drie woorden die de deal veranderden: "Wie ziet wat?" Sophie de Wit had vier maanden besteed aan het bouwen van InzichtPro, een met Lovable gebouwd analytics-dashboard voor Nederlandse retailketens, en elke gebruiker in haar prototype had dezelfde toegang — elk dashboard, elk rapport, elke configuratie-instelling. Voor haar kleine pilotklanten was dit prima. Voor Blokker Nederland, dat InzichtPro wilde uitrollen over 40 winkels met aparte toegangsniveaus voor winkelmanagers, regiodirecteuren en corporate analisten, was het een dealbreaker.

## Authenticatie Zonder Autorisatie

Sophies situatie is een van de meest voorkomende gaten in AI-gegenereerde SaaS-producten, en een van de minst zichtbare totdat een enterprise-koper er rechtstreeks naar vraagt. Lovable, zoals de meeste AI-prototyping-tools, bouwt moeiteloos authenticatie — een inlogformulier, een aanmeldflow, een sessietoken — omdat authenticatie een goed gedefinieerd, veelvuldig gedocumenteerd patroon is dat het model duizenden keren heeft gezien. Autorisatie is anders: het is geen functie die u generiek kunt aanplakken, omdat het volledig afhangt van de specifieke organisatiestructuur van het bedrijf dat het product gebruikt. Een retailanalysetool heeft een compleet ander rechtenmodel nodig dan een projectmanagementtool of een zorgplanningsapp, en geen enkele AI-prototypingsessie produceert dat model ongevraagd. InzichtPro had een voordeur met een slot. Het had geen kamers.

## De Technische Vereiste

De vereiste die Blokker beschreef was specifiek en, vanuit dataperspectief, hiërarchisch. Een winkelmanager op één locatie in Rotterdam moest de omzet, bezoekersaantallen en voorraadrotatie van die winkel zien — en verder niets. Een regiodirecteur die toezicht hield op een dozijn winkels in de Randstad moest elke winkel in die regio zien, ze onderling vergelijken, maar niet aan winkels buiten die regio kunnen komen. Een corporate analist op Blokkers hoofdkantoor had zicht nodig op alle 40 winkels landelijk, met de mogelijkheid om winkeloverstijgende rapporten te bouwen, maar expliciet zonder de mogelijkheid om de configuratie of gegevens van welke winkel dan ook te wijzigen — een alleen-lezen plafond ongeacht hoe senior de rol van de analist is. De huidige staat van InzichtPro maakte alle drie gelijk: elke geauthenticeerde gebruiker, ongeacht titel, zag dezelfde ongefilterde dataset over alle locaties, omdat het prototype authenticatie had (u kunt inloggen) maar geen autorisatie (wat u kunt zien en doen ná het inloggen zijn twee verschillende problemen, en slechts één daarvan was opgelost).

## Hoe LaunchStudio RBAC Implementeerde

Het Manifera-team van LaunchStudio implementeerde een RBAC-systeem met drie niveaus zonder ook maar één regel van Sophies met Lovable gebouwde frontend aan te raken. Een rollentabel in Supabase definieerde de vier roltypen — store_manager, regional_director, corporate_analyst en admin — als data, niet als code, zodat het later toevoegen van een vijfde rol neerkwam op het invoegen van een rij in plaats van het uitrollen van een deploy. Een user_roles-koppeltabel koppelde elke geauthenticeerde gebruiker aan één rol plus een organisatorisch bereik: een store_id voor winkelmanagers, een region_id voor regiodirecteuren, en geen bereikbeperking voor corporate analisten en admins. De handhaving vond plaats op databaselaagniveau — RLS-beleid op elke datatabel (verkoop, voorraad, bezoekersaantallen, rapporten) controleerde de rol en het bereik van de aanvragende gebruiker bij elke afzonderlijke query, en filterde rijen weg voordat ze ooit de API-respons bereikten. De query van een winkelmanager voor "alle verkopen" werd op databaseniveau stilzwijgend "alle verkopen waar store_id gelijk is aan mijn winkel", zonder dat een gecompromitteerde of verkeerd geconfigureerde frontend data buiten die grens kon opvragen. Daarbovenop liet een nieuw beheerderspaneel — gebouwd als extra sectie van Sophies bestaande dashboard, passend bij het designsysteem — Blokkers eigen IT-beheerder gebruikers aanmaken, rollen toewijzen en organisatorisch bereik herverdelen zonder ooit Supabase rechtstreeks aan te raken of een supportticket in te dienen.

## Waarom De Frontend Nooit Veranderde

De architecturale beslissing die deze opdracht snel maakte — 8 werkdagen van kickoff tot productie — was het afdwingen van autorisatie op databaseniveau in plaats van applicatieniveau. Sophies frontend wist en gaf nooit om welke rijen een query teruggaf; hij rendert simpelweg wat de API terugstuurde. Dat betekende dat RBAC volledig aan de backend kon worden toegevoegd, zonder één enkele React-component aan te raken, zonder een frontend-deploy, en zonder het risico van een regressie in de UI waar Sophie maanden aan had gepolijst. Het betekende ook dat het systeem schaalde zonder extra engineering: toen de maand erop twee andere retailketens tekenden, elk met een ander aantal winkels en een andere regionale structuur, betekende onboarding het invoegen van nieuwe rijen in de rollen- en user_roles-tabellen — dezelfde RLS-beleidsregels die Blokkers 40 winkels beschermden, beschermden automatisch ook de hiërarchieën van de nieuwe ketens, omdat de beleidsregels verwezen naar rol en bereik, nooit naar een specifieke klant.

Dit is ook waarom de oplossing 8 dagen kostte in plaats van 8 weken. Autorisatie binnen de frontend herbouwen had betekend rolchecks door elk dashboardcomponent, elke grafiek en elke rapportgenerator vlechten die Sophie al had uitgerold — een herbouw vermomd als functie. De logica naar RLS-beleid duwen betekende dat de hele toegangscontrolelaag op één plek stond, onafhankelijk van de UI testbaar was en met directe SQL-query's kon worden geverifieerd voordat er ook maar één dashboardscherm werd aangeraakt.

## De Levering

**Resultaat:** Blokker tekende een pilotovereenkomst voor 40 winkels. Het RBAC-systeem schaalde vanzelf toen de maand erop twee andere retailketens tekenden, elk met hun eigen organisatiestructuur gekoppeld aan hetzelfde rollenframework. Sophies met Lovable gebouwde frontend bleef volledig ongewijzigd — de RBAC-logica werd afgedwongen op database- en API-niveau, waarbij de frontend simpelweg rendert welke data de API teruggeeft voor de rol van de huidige gebruiker.

> *"De vraag van één enterprise-prospect — 'wie ziet wat?' — was meer waard dan al mijn kleine klanten samen. Het antwoord van LaunchStudio was klaar in 8 dagen. Het contract werd op dag 10 ondertekend."*
> — **Sophie de Wit, Oprichter, InzichtPro (Rotterdam)**

**Kosten & Doorlooptijd:** €2.400 (Launch Ready Pakket, RBAC-implementatie + beheerderspaneel + RLS-beleid) — live in 8 werkdagen.

---

[LaunchStudio](https://launchstudio.eu/nl/) voegt de toegangscontrole toe die enterprise-kopers vereisen — het team van Manifera implementeert RBAC op databaseniveau, zodat uw frontend niet hoeft te veranderen.

[Vertel ons over de toegangscontrole die uw volgende klant nodig heeft](https://launchstudio.eu/nl/#contact).

---

## Veelgestelde Vragen

### Kan RBAC worden toegevoegd aan elke Supabase-gebaseerde applicatie, of moet de database worden herstructureerd?
RBAC kan op de meeste bestaande Supabase-schema's worden gelegd door rollen- en user_roles-tabellen plus RLS-beleid toe te voegen. De bestaande datatabellen hoeven doorgaans geen structurele wijzigingen te ondergaan — alleen beleidstoevoegingen.

### Hoeveel rollen kan het RBAC-systeem ondersteunen?
Er is geen praktische limiet. De rolstructuur is tabelgebaseerd en uitbreidbaar — een nieuwe rol toevoegen is een rij toevoegen, geen code wijzigen.

### Vertraagt het RBAC-systeem databasequery's?
Met de juiste indexering op rol- en organisatie-eenheidkolommen is de prestatie-impact verwaarloosbaar — doorgaans onder de 1 ms per query.

### Kunnen niet-technische beheerders gebruikersrollen beheren zonder hulp van developers?
Ja — het beheerderspaneel dat LaunchStudio bouwt biedt een UI voor het toewijzen en intrekken van rollen, het toevoegen van gebruikers aan organisatie-eenheden en het bekijken van de huidige rechtenstructuur.

### Wat gebeurt er als de rol van een gebruiker verandert — moeten ze uitloggen en opnieuw inloggen?
Dat hangt af van de implementatie. LaunchStudio configureert RLS-beleid om bij elk verzoek te evalueren, zodat rolwijzigingen onmiddellijk van kracht worden zonder opnieuw te hoeven authenticeren.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Kan RBAC worden toegevoegd aan elke Supabase-gebaseerde applicatie?", "acceptedAnswer": { "@type": "Answer", "text": "RBAC kan op de meeste bestaande Supabase-schema's worden gelegd door rollentabellen plus RLS-beleid toe te voegen. Bestaande datatabellen hoeven doorgaans geen structurele wijzigingen te ondergaan." } },
    { "@type": "Question", "name": "Hoeveel rollen kan het RBAC-systeem ondersteunen?", "acceptedAnswer": { "@type": "Answer", "text": "Geen praktische limiet. De rolstructuur is tabelgebaseerd en uitbreidbaar — een nieuwe rol toevoegen is een rij toevoegen, geen code wijzigen." } },
    { "@type": "Question", "name": "Vertraagt het RBAC-systeem databasequery's?", "acceptedAnswer": { "@type": "Answer", "text": "Met de juiste indexering is de prestatie-impact verwaarloosbaar — doorgaans onder de 1 ms per query." } },
    { "@type": "Question", "name": "Kunnen niet-technische beheerders gebruikersrollen beheren zonder hulp van developers?", "acceptedAnswer": { "@type": "Answer", "text": "Ja — het beheerderspaneel biedt een UI voor het toewijzen en intrekken van rollen zonder databasetoegang." } },
    { "@type": "Question", "name": "Wat gebeurt er als de rol van een gebruiker verandert — moeten ze uitloggen?", "acceptedAnswer": { "@type": "Answer", "text": "RLS-beleid evalueert bij elk verzoek, zodat rolwijzigingen onmiddellijk van kracht worden zonder opnieuw te authenticeren." } }
  ]
}
</script>
