---
Titel: "Het Verschil Tussen Authenticatie En Autorisatie — En Waarom Uw Prototype Ze Waarschijnlijk Verwart"
Trefwoorden: authenticatie vs autorisatie, toegangscontrole AI-prototype, role-based access control, RBAC SaaS, autorisatie beveiligingsgat, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Het Verschil Tussen Authenticatie En Autorisatie — En Waarom Uw Prototype Ze Waarschijnlijk Verwart

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Het Verschil Tussen Authenticatie En Autorisatie — En Waarom Uw Prototype Ze Waarschijnlijk Verwart",
  "description": "Uw prototype controleert wie de gebruiker is. Het controleert waarschijnlijk niet wat hij mag doen. Dat onderscheid - authenticatie vs. autorisatie - is het meest voorkomende beveiligingsgat in AI-gegenereerde code, en het gat dat het meest waarschijnlijk een ingelogde gebruiker de data van een andere gebruiker laat zien.",
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
  "datePublished": "2026-12-31",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/authentication-vs-authorization-prototype-confusion"
  }
}
</script>

Uw login werkt. Een gebruiker voert zijn e-mailadres en wachtwoord in, wordt doorgestuurd naar zijn dashboard, ziet zijn eigen data. Alles ziet er correct uit. Open nu een tweede browser, log in als een andere gebruiker, kopieer de URL van de profielpagina van gebruiker A, plak deze in de browser van gebruiker B. Als gebruiker B de data van gebruiker A kan zien — zijn projecten, zijn betalingsgeschiedenis, zijn geüploade bestanden — heeft uw prototype authenticatie maar geen autorisatie, en heeft elke ingelogde gebruiker impliciet toegang tot de informatie van elke andere gebruiker. Dit is geen edge case of een theoretisch risico. Het is het meest voorkomende beveiligingsgat in AI-gegenereerde applicaties, en het komt voort uit een verwarring tussen twee concepten die vergelijkbaar klinken maar volledig verschillende dingen doen.

## Authenticatie: "Wie Bent U?"

Authenticatie beantwoordt één vraag: is deze persoon wie hij beweert te zijn? Het loginformulier, de wachtwoordhash-controle, het JWT-token — dit alles is authenticatie. Wanneer Lovable of Bolt Supabase Auth opzet, genereert het een werkend authenticatiesysteem: gebruikers kunnen registreren, inloggen, tokens ontvangen, en worden geïdentificeerd bij vervolgverzoeken. Dit is het onderdeel dat AI-tools doorgaans correct implementeren, omdat de UI-elementen (loginformulier, aanmeldformulier, wachtwoordherstel) zichtbaar zijn en de functionaliteit duidelijke, promptbare vereisten heeft.

## Autorisatie: "Wat Mag U Doen?"

Autorisatie beantwoordt een andere vraag: gegeven dat we weten wie deze persoon is, waartoe heeft hij toegang? Kan gebruiker A de projecten van gebruiker B zien? Kan een gebruiker met een gratis abonnement premiumfuncties gebruiken? Kan een teamlid een project verwijderen dat hij niet heeft aangemaakt? Kan een beheerder het account van een andere gebruiker wijzigen? Autorisatie gaat niet over identiteit — het gaat over toestemmingen, en het vereist expliciete regels die bij elke datatoegang controleren of de aanvragende gebruiker het recht heeft om de specifieke resource die hij opvraagt te zien of te wijzigen.

## Waar AI-Gegenereerde Code Tekortschiet

AI-tools genereren authenticatie betrouwbaar omdat authenticatie een goed gedefinieerde, op zichzelf staande functie is met duidelijke UI-componenten. Autorisatie is lastiger omdat het geen enkele functie is — het is een cross-cutting concern dat elke datatoegang in de applicatie beïnvloedt. Elke databasequery die data teruggeeft heeft een filter nodig: "geef alleen rijen terug die deze gebruiker mag zien." Elk API-endpoint dat data wijzigt heeft een controle nodig: "heeft deze gebruiker toestemming om dit specifieke record te wijzigen?" Elke bestandstoegang, elke rapportgeneratie, elke exportfunctie heeft dezelfde verificatie nodig.

Het typische AI-gegenereerde patroon is: controleer of de gebruiker is ingelogd (authenticatie), geef dan terug wat het API-endpoint is geconfigureerd om terug te geven (geen autorisatiecontrole). Het resultaat is een applicatie waarin elke geauthenticeerde gebruiker toegang heeft tot elk record in de database door het ID in de URL, het API-verzoek, of de client-side state te wijzigen — een kwetsbaarheidsklasse die bekendstaat als Insecure Direct Object Reference (IDOR) en consistent in de OWASP Top 10 staat.

## Hoe Correcte Autorisatie Er In Supabase Uitziet

Voor Supabase-gebaseerde applicaties — waar de meeste Lovable- en Bolt-prototypes gebruik van maken — wordt autorisatie geïmplementeerd via Row-Level Security (RLS)-beleid. Een RLS-beleid is een databaseregel die data automatisch filtert op basis van de identiteit van de aanvragende gebruiker. In plaats van te vertrouwen op de applicatiecode om `WHERE user_id = current_user` aan elke query toe te voegen, dwingt de database zelf het filter af — wat betekent dat zelfs als de applicatiecode vergeet de eigendom te controleren (wat AI-gegenereerde code vaak doet), de database geen data teruggeeft waartoe de gebruiker geen toegang heeft.

Een minimale RLS-opzet voor een multi-user applicatie omvat: een SELECT-beleid dat alleen rijen teruggeeft die de gebruiker bezit of waartoe hij toegang heeft gekregen; een INSERT-beleid dat de eigenaar automatisch instelt op de huidige gebruiker; een UPDATE-beleid dat gebruikers verhindert rijen te wijzigen die ze niet bezitten; en een DELETE-beleid dat gebruikers verhindert rijen te verwijderen die ze niet bezitten. Elk beleid is doorgaans 3-5 regels SQL. De totale inspanning voor een typische applicatie met 5-10 tabellen is minder dan een uur implementatie — maar het beveiligingsoppervlak dat het dekt is enorm.

## Voorbij RLS: Autorisatie Op Applicatieniveau

RLS handelt data-niveau-autorisatie af (welke rijen mag deze gebruiker benaderen?), maar autorisatie op applicatieniveau (welke functies mag deze gebruiker gebruiken?) vereist aanvullende logica: rolcontroles (is deze gebruiker een beheerder, een teamlid, of een viewer?), feature gating (zit deze gebruiker op een abonnement dat deze functie omvat?), en relatiegebaseerde toegang (kan dit teamlid dit project benaderen omdat hij is uitgenodigd, niet omdat hij het bezit?). AI-gegenereerde code implementeert deze controles bijna nooit, omdat ze bedrijfslogica vereisen die geen onderdeel was van de prompt — en bedrijfslogica varieert per applicatie, wat het lastig maakt voor een algemene AI-tool om correct te genereren.

[LaunchStudio](https://launchstudio.eu/nl/) implementeert beide lagen — database-niveau RLS en autorisatie op applicatieniveau — zodat authenticatie "wie" beantwoordt en autorisatie "wat," ondersteund door Manifera-engineers die bij elk traject controleren op IDOR-kwetsbaarheden.

[Stuur uw prototype op en vraag ons de autorisatielaag te controleren](https://launchstudio.eu/nl/#contact) — als het antwoord "die is er niet" is, gaat het oplossen ervan sneller en goedkoper dan het datalek dat het voorkomt.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in de Praktijk: Het Dashboard Dat Ieders Data Toonde

Niels Achterberg, voormalig HR-consultant in Nijmegen, bouwde TeamPulse, een door Lovable aangedreven tool voor medewerkersbetrokkenheidsonderzoeken voor kleine Nederlandse bedrijven. De app had solide authenticatie — medewerkers logden in met bedrijfsspecifieke inloggegevens, ontvingen JWT-tokens, en zagen een gepersonaliseerd dashboard. Het probleem dat Niels pas ontdekte toen een bètatester van een bedrijf de `survey_id`-parameter in de URL veranderde en de onderzoeksresultaten van een ander bedrijf kon zien: authenticatie werkte, autorisatie niet.

Elke ingelogde gebruiker kon elk onderzoek, elke reactie, en elk geaggregeerd resultaat benaderen over alle bedrijven in de database — niet omdat de applicatie deze data toonde (de frontend toonde alleen het eigen bedrijf van de gebruiker), maar omdat de API het teruggaf wanneer er rechtstreeks om gevraagd werd. Eén API-aanroep met een andere onderzoeks-ID gaf complete, identificeerbare medewerkersbetrokkenheidsdata terug voor een bedrijf waarmee de aanvrager geen relatie had.

Het Manifera-team van LaunchStudio implementeerde een drielaags autorisatiefix: Supabase RLS-beleid op elke tabel (onderzoeken, reacties, resultaten) die filtert op bedrijfslidmaatschap; API-middleware die de bedrijfsassociatie van de aanvragende gebruiker verifieert voordat een dataverzoek wordt verwerkt; en een bedrijf-gescoped API-key-systeem dat de data van elk bedrijf isoleerde op authenticatieniveau, waardoor cross-company datatoegang structureel onmogelijk werd in plaats van slechts gefilterd.

**Resultaat:** TeamPulse doorstond een beveiligingsreview van zijn eerste enterprise-prospect zonder enige autorisatiebevinding. De fix duurde 4 werkdagen en raakte geen frontendcode — Niels' door Lovable gebouwde interface bleef precies zoals hij was.

> *"Ik testte login grondig. Ik testte nooit of gebruiker A de data van gebruiker B kon zien door een URL-parameter te wijzigen. Die ene test had het gat gevonden — maar ik wist niet dat ik hem moest uitvoeren."*
> — **Niels Achterberg, Oprichter, TeamPulse (Nijmegen)**

**Kosten & Doorlooptijd:** €1.400 (Launch Ready Pakket, RLS + API-autorisatie + bedrijfsisolatie) — live in 4 werkdagen.

---

## Veelgestelde Vragen

### Als mijn Supabase-project RLS ingeschakeld heeft, betekent dat dan dat autorisatie geregeld is?

Niet noodzakelijk — RLS "ingeschakeld" hebben en RLS met correcte, uitgebreide beleidsregels op elke tabel zijn verschillende dingen. Veel Supabase-projecten hebben RLS ingeschakeld op projectniveau maar missen beleidsregels op specifieke tabellen, wat betekent dat die tabellen ofwel ontoegankelijk zijn (als RLS aan staat zonder beleid) of volledig open (als RLS uit staat op die specifieke tabel).

### Kan ik zelf op autorisatiegaten controleren zonder ontwikkelaar te zijn?

U kunt een basale test uitvoeren: log in als gebruiker A, noteer de URL van een pagina met de data van gebruiker A, log dan in als gebruiker B in een andere browser en plak de URL van gebruiker A. Als gebruiker B de data van gebruiker A ziet, heeft u een autorisatiegat. Deze test vangt de meest voorkomende kwetsbaarheid, maar niet alle gevallen.

### Is IDOR-kwetsbaarheid echt zo veelvoorkomend in AI-gegenereerde applicaties?

Extreem veelvoorkomend — het is consistent een van de topkwetsbaarheden gevonden in LaunchStudio's audits, aanwezig in de meerderheid van Lovable-, Bolt-, en Cursor-gegenereerde applicaties die geen expliciet autorisatiewerk hebben gehad.

### Moet autorisatie voor elk type gebruikersrol anders worden geïmplementeerd?

Het implementatiepatroon is hetzelfde (toestemmingen controleren voordat data wordt teruggegeven), maar de regels verschillen per rol. Een beheerder ziet mogelijk alle records, een teamleider ziet de records van zijn team, en een gewone gebruiker ziet alleen zijn eigen records. Deze rolgebaseerde regels moeten expliciet worden gedefinieerd en afgedwongen.

### Kunnen autorisatiebeleidsregels de prestaties van de applicatie beïnvloeden?

RLS-beleid voegt een kleine overhead toe per query (de database past het filter toe bij elke rijtoegang), maar met correcte indexering op de kolommen die in het beleid worden gebruikt (doorgaans `user_id` of `company_id`), is de prestatie-impact verwaarloosbaar — meestal minder dan 1 milliseconde per query.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Als mijn Supabase-project RLS ingeschakeld heeft, betekent dat dan dat autorisatie geregeld is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niet noodzakelijk - RLS ingeschakeld hebben en correcte, uitgebreide beleidsregels op elke tabel hebben zijn verschillende dingen. Veel projecten hebben RLS ingeschakeld maar missen beleidsregels op specifieke tabellen."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik zelf op autorisatiegaten controleren zonder ontwikkelaar te zijn?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "U kunt een basale test uitvoeren: log in als gebruiker A, noteer de URL, log dan in als gebruiker B en plak de URL van gebruiker A. Als gebruiker B de data van gebruiker A ziet, heeft u een autorisatiegat."
      }
    },
    {
      "@type": "Question",
      "name": "Is IDOR-kwetsbaarheid echt zo veelvoorkomend in AI-gegenereerde applicaties?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Extreem veelvoorkomend - het is consistent een van de topkwetsbaarheden gevonden in LaunchStudio's audits, aanwezig in de meerderheid van AI-gegenereerde applicaties die geen expliciet autorisatiewerk hebben gehad."
      }
    },
    {
      "@type": "Question",
      "name": "Moet autorisatie voor elk type gebruikersrol anders worden geïmplementeerd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het implementatiepatroon is hetzelfde, maar de regels verschillen per rol. Deze rolgebaseerde regels moeten expliciet worden gedefinieerd en afgedwongen."
      }
    },
    {
      "@type": "Question",
      "name": "Kunnen autorisatiebeleidsregels de prestaties van de applicatie beïnvloeden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Met correcte indexering op de kolommen die in het beleid worden gebruikt, is de prestatie-impact verwaarloosbaar - meestal minder dan 1 milliseconde per query."
      }
    }
  ]
}
</script>
