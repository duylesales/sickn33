---
Titel: "Single-Tenant vs Multi-Tenant voor een B2B-SaaS-Oprichter"
Trefwoorden: single tenant vs multi tenant, multi-tenant saas supabase, eigen instantie saas, b2b saas-architectuur oprichters, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: SaaS-Oprichter Scale-Up
---

# Single-Tenant vs Multi-Tenant voor een B2B-SaaS-Oprichter

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Single-Tenant vs Multi-Tenant voor een B2B-SaaS-Oprichter",
  "description": "Moeten alle klanten één database delen met strikte scheiding, of krijgt elke klant een eigen instantie? Deze vergelijking legt multi-tenant en single-tenant opzetten voor AI-gebouwde SaaS uit, met hun kosten, beveiliging, beheer en wanneer een eigen instantie voor een grote klant zinvol is.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-04-11",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/single-tenant-vs-multi-tenant-for-b2b-saas" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" },
    { "@type": "CreativeWork", "name": "PostgreSQL: Row Security Policies", "url": "https://www.postgresql.org/docs/current/ddl-rowsecurity.html" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A01 Broken Access Control", "url": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/" },
    { "@type": "CreativeWork", "name": "AWS: SaaS tenant isolation strategies", "url": "https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/saas-tenant-isolation-strategies.html" }
  ]
}
</script>

Vroeg of laat vraagt een grotere klant: "Staan onze gegevens in dezelfde database als die van andere klanten?" Die vraag opent een van de basiskeuzes in de architectuur van B2B-SaaS. In een multi-tenant opzet delen alle klanten één applicatie en database, gescheiden door strikte toegangsregels. In een single-tenant opzet krijgt elke klant een eigen instantie of database. Voor oprichters met AI-gebouwde producten is multi-tenant bijna altijd de juiste standaard, met single-tenant voorbehouden aan specifieke situaties.

## Belangrijkste Punten

- **Multi-tenant SaaS bedient alle klanten vanuit gedeelde infrastructuur** en scheidt gegevens logisch; single-tenant geeft elke klant eigen infrastructuur of databases.
- **Multi-tenant is de juiste standaard voor vrijwel elke B2B-SaaS in een vroege fase:** goedkoper om te draaien, eenvoudiger bij te werken en goed ondersteund door Row Level Security in PostgreSQL.
- **Single-tenant is zinvol** bij strikte contractuele of wettelijke eisen aan scheiding, zeer grote klanten met eigen eisen of een vaste locatie van gegevens per klant.
- **Een gemengd model** kan een paar grote klanten een eigen instantie bieden, terwijl alle anderen op het gedeelde platform blijven.
- **Klanten die vragen "zijn onze gegevens gescheiden?" willen meestal zekerheid,** en die kan sterke scheiding tussen klanten, met tests en documentatie, bieden zonder single-tenancy.

## Naast Elkaar

| Aspect | Multi-tenant | Single-tenant |
| --- | --- | --- |
| Scheiding van gegevens | Logisch: organisatie-ID plus Row Level Security | Fysiek: aparte database of apart project per klant |
| Kosten per klant | Laag | Hoog: elke instantie heeft eigen kosten |
| Beheer | Eén deployment, één set migraties | Veel deployments en migraties die in lijn moeten blijven |
| Functies uitbrengen | Eén keer voor iedereen | Per instantie, of gecoördineerd over alle instanties |
| Aanpassing per klant | Configuratie en feature flags | Makkelijker aan te passen, moeilijker te onderhouden |
| Garanties voor scheiding | Hangen af van correcte policies en tests | Sterker door het ontwerp |
| Past bij AI-gebouwde apps | Vanzelfsprekend met Supabase RLS | Vraagt extra tooling |

## Waarom Multi-Tenant de Standaard Is

- Eén codebase, één database, één pipeline: beheersbaar voor kleine teams
- Lagere infrastructuurkosten, wat ertoe doet bij veel kleinere klanten
- Elke klant krijgt verbeteringen direct
- De Row Level Security van Supabase is precies hiervoor ontworpen

Het risico zit op één plek: als de scheiding fout is, wordt elke klant geraakt. Daarom is geteste RLS, zoals beschreven in onze [gids over teams en uitnodigingen](https://launchstudio.eu/nl/blog/how-do-i-add-teams-and-invites-to-my-saas), niet onderhandelbaar.

## Wanneer Single-Tenant Zinvol Is

- Een grote klant eist contractueel een eigen database of regio
- Gereguleerde gegevens waarbij het beleid van de klant fysieke scheiding vereist
- Sterk verschillende prestatiebehoeften, waarbij de belasting van één klant anderen zou raken
- Klantspecifieke integraties of een locatie van gegevens buiten uw standaardregio

Prijs deze deployments daarnaar: ze kosten meer om te draaien en te onderhouden.

## Een Gemengde Aanpak

Veel SaaS-bedrijven draaien voor de meeste klanten multi-tenant en bieden een eigen instantie aan als optie voor grote bedrijven. Om dit goed te doen, zijn geautomatiseerde deployments en migraties over alle instanties nodig, zodat de klant met een eigen instantie niet achterloopt op functies en oplossingen.

## Hoe U de Vraag van de Klant Beantwoordt

Werkt u multi-tenant, leg dan uit hoe de scheiding werkt: toegangsregels op basis van organisaties die in de database worden afgedwongen, getest met geautomatiseerde controles, plus versleuteling, logging en hosting in de EU. Veel klanten zijn tevreden met een duidelijke uitleg en bewijs. Onze [AVG-checklist voor SaaS-oprichters](https://launchstudio.eu/nl/blog/gdpr-checklist-for-saas-founders-in-the-netherlands) bevat de vragen die ze doorgaans stellen.

## Hoe Scheiding tussen Klanten in een Gedeelde Database Werkt

In een multi-tenant PostgreSQL-database draagt elke bedrijfstabel een identificatie van de klant, zoals `organisation_id`. Row Level Security-policies beperken elke query tot rijen van organisaties waarvan de huidige gebruiker lid is. Supabase documenteert dit patroon, en PostgreSQL dwingt het af op het niveau van de database, zodat zelfs een bug in de applicatiecode via de API geen rijen van een andere klant kan teruggeven. Extra lagen zijn onder meer storagepolicies die bestandspaden per klant afbakenen, serverfuncties die het lidmaatschap controleren voordat ze iets doen, en tests die proberen gegevens van andere klanten te benaderen.

## Niveaus van Scheiding Uitgelegd

Er is een spectrum tussen volledig gedeeld en volledig eigen:

| Model | Beschrijving | Scheiding | Kosten en inspanning |
| --- | --- | --- | --- |
| Gedeelde tabellen | Alle klanten in dezelfde tabellen, gescheiden door een klant-ID en RLS | Logisch | Laagst |
| Schema per klant | Elke klant heeft een eigen schema in één database | Sterker logisch | Gemiddeld |
| Database per klant | Elke klant heeft een eigen database | Sterk | Hoger |
| Volledige opzet per klant | Eigen app, database en infrastructuur | Sterkst | Hoogst |

De meeste SaaS-producten beginnen met gedeelde tabellen en verplaatsen afzonderlijke klanten pas naar een sterkere scheiding wanneer contracten dat vereisen.

## Waarom Updates in het Voordeel van Multi-Tenancy Uitvallen

Met één gedeelde applicatie en database bereikt elke verbetering en elke beveiligingsoplossing alle klanten tegelijk. Met veel single-tenant deployments moet elke update over de instanties worden uitgerold, moeten migraties per database worden uitgevoerd en kunnen versies uit elkaar lopen. Teams met tientallen single-tenant klanten besteden vaak aanzienlijk veel tijd alleen al aan deployments. Voor een klein team gaat die overhead direct ten koste van productontwikkeling.

## Beveiligingsrisico's in Multi-Tenant Apps

Het grootste risico in een multi-tenant app is het blootstellen van gegevens tussen klanten, wat OWASP rekent tot gebrekkige toegangscontrole, het grootste risico voor webapplicaties in de rangschikking van 2021. In AI-gebouwde apps zijn gangbare oorzaken onder meer tabellen die zonder Row Level Security zijn aangemaakt, policies die alleen controleren of een gebruiker is ingelogd, serverfuncties die de service role key gebruiken zonder het lidmaatschap te controleren, en storage-buckets zonder paden die per klant zijn afgebakend. Elk daarvan is te voorkomen met een zorgvuldig ontwerp en geautomatiseerde tests die inloggen als gebruikers van twee klanten.

## Wanneer Klanten om een Eigen Database Vragen

Prospects onder grote bedrijven vragen soms of ze een eigen database kunnen krijgen. Zoek uit welke zorg er achter het verzoek zit voordat u instemt. Vaak is het een van deze: angst dat gegevens uitlekken naar andere klanten, een eis om bij het einde van het contract alle gegevens te verwijderen, de behoefte aan gegevens in een specifiek land, of een punt in een beveiligingsvragenlijst. Elk daarvan kan meestal binnen een multi-tenant architectuur worden beantwoord met geteste scheiding tussen klanten, verwijdering op organisatieniveau, hosting in een regio en documentatie. Blijft de eis bestaan, prijs de optie met een eigen instantie dan zo dat de werkelijke beheerkosten worden gedekt.

## Een Gemengd Model Implementeren

Wanneer een paar klanten echt eigen infrastructuur nodig hebben, kan een combinatie werken: het gedeelde platform bedient de meeste klanten, terwijl eigen instanties dezelfde codebase draaien voor specifieke contracten met grote bedrijven. De sleutels tot succes zijn één codebase met alleen verschillen in configuratie, geautomatiseerde deployment naar alle instanties vanuit dezelfde pipeline, migraties die automatisch op elke database worden uitgevoerd, monitoring voor elke instantie en duidelijke prijzen die de extra beheerkosten dekken. Zonder automatisering lopen gemengde opzetten uit de pas en worden ze duur om te onderhouden.

## Locatie van Gegevens en de AVG

De AVG vereist geen single-tenancy. Ze vereist passende technische en organisatorische maatregelen onder artikel 32, verwerkersovereenkomsten met verwerkers onder artikel 28 en waarborgen voor doorgifte buiten de EER. Een multi-tenant SaaS die in een EU-regio wordt gehost, met sterke toegangscontrole, versleuteling, back-ups en gedocumenteerde procedures, kan aan die eisen voldoen. Klanten die verplicht zijn gegevens in een specifiek land te houden, hebben mogelijk deployments per regio nodig, wat een vorm van gedeeltelijke scheiding is in plaats van volledige single-tenancy.

## Prestaties en Lastige Buren

In gedeelde systemen kan één grote klant anderen raken door zware rapporten of imports te draaien. Maatregelen zijn onder meer indexen op klant-ID's, limieten op query's, achtergrondtaken voor zware verwerking, rate limiting per klant en monitoring van trage query's per klant. Pas wanneer de werklast van één klant structureel overheerst, wordt het economisch zinvol die klant naar eigen middelen te verplaatsen.

## Scheiding tussen Klanten Testen

Geautomatiseerde tests zijn de sterkste zekerheid die u kunt bieden. Maak twee organisaties aan met gebruikers in elk, en probeer daarna als de ene gebruiker via elk API-pad, elke tabel en elke storage-bucket bij de gegevens van de ander te komen. Tests moeten bevestigen dat lezen, toevoegen, bijwerken en verwijderen tussen klanten allemaal mislukken. Draai ze in uw deploymentpipeline, zodat nieuwe tabellen of functies niet zonder scheiding kunnen worden uitgebracht. Documenteer de resultaten; ze vormen een overtuigend antwoord in beveiligingsvragenlijsten.

## Veelgemaakte Fouten

- Single-tenancy beloven om een deal binnen te halen zonder de beheerkosten mee te prijzen
- Klant-ID's toevoegen aan sommige tabellen, maar niet aan gerelateerde tabellen
- Vertrouwen op filteren in de frontend voor de scheiding tussen klanten
- De service role key gebruiken in functies zonder het lidmaatschap te controleren
- Aparte databases per klant draaien zonder geautomatiseerde migraties

## Prijsniveaus en Scheiding

Scheiding kan onderdeel worden van uw prijzen. Standaardabonnementen draaien op het gedeelde platform met sterke logische scheiding. Een niveau voor grote bedrijven kan functies toevoegen zoals single sign-on, auditlogs, eigen bewaartermijnen en, waar vereist, een eigen database of een deployment per regio, tegen een prijs die de kosten weerspiegelt. Door scheiding te presenteren als premiumoptie in plaats van als standaard, houdt u uw architectuur eenvoudig en bedient u klanten die echt meer nodig hebben.

## Vragen Voordat U Beslist

Welke klanten vragen om scheiding, en waarom? Wat zou eigen infrastructuur per klant kosten om te draaien, inclusief updates en monitoring? Kunnen geteste logische scheiding, hosting in een regio en documentatie de onderliggende zorg wegnemen? Hebben we automatisering om meerdere instanties betrouwbaar te beheren? Duidelijke antwoorden voorkomen dure keuzes in de architectuur die onder verkoopdruk worden gemaakt.

## Waar U Vandaag Begint

Schrijf een test die inlogt als gebruiker van de ene organisatie en via uw API probeert de records van een andere organisatie te lezen. Lukt dat, herstel dan eerst uw policies. Mislukt het zoals het hoort, documenteer het dan als bewijs voor uw volgende beveiligingsvragenlijst.

## Samenvatting

Begin multi-tenant met sterke scheiding in de database, test die automatisch en documenteer die. Bied eigen infrastructuur alleen aan wanneer een echte eis de kosten rechtvaardigt, en automatiseer het als u dat doet.

## Scheiding Buiten de Database

Scheiding tussen klanten geldt ook voor caches, zoekindexen, achtergrondtaken, logs en analytics. Een cache met alleen het record-ID als sleutel, een zoekindex zonder filters per klant of een taak die alle klanten met verhoogde rechten verwerkt, kan gegevens lekken, ook wanneer de databasepolicies perfect zijn. Beoordeel elk onderdeel dat klantgegevens opslaat of verwerkt, en neem klant-ID's op overal waar gegevens op een sleutel worden opgeslagen of gefilterd. Ook tools voor error tracking horen te voorkomen dat ze gegevens van een andere klant in de context vastleggen.

## De Kern

Multi-tenancy is hoe moderne SaaS economisch schaalt. Maak de scheiding sterk, getest en gedocumenteerd, en u heeft single-tenancy zelden nodig.

## Gerelateerde Onderwerpen

Onze gidsen over audits van Supabase RLS, multi-tenant SaaS op Supabase en de verwerkersovereenkomst van Supabase behandelen de implementatie en het papierwerk achter scheiding tussen klanten.

## Tot Slot

Klanten vertrouwen bewijs meer dan architectuurdiagrammen: laat ze geteste scheiding zien.

## De Architectuur Goed Krijgen

LaunchStudio implementeert geteste multi-tenant scheiding voor AI-gebouwde SaaS en kan eigen instanties inrichten wanneer een contract dat vereist. LaunchStudio wordt ondersteund door Manifera, dat al 11+ jaar beide modellen bouwt voor grote klanten vanuit Amsterdam, Singapore en Ho Chi Minh-stad; zie [de webappontwikkeling van Manifera](https://www.manifera.com/services/web-app-develop/). De [richtlijnen van Microsoft voor multitenant architectuur](https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/overview) zijn een grondig, neutraal naslagwerk.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Eigen Instantie die Niet Al het Andere Brak

Victor Hamers bouwde Inspectieloket in Bolt en Supabase: een tool voor inspecties en compliance voor onderhoudsbedrijven in vastgoed. De tool was multi-tenant, met 25 klanten. Een landelijke woningcorporatie wilde tekenen, maar eiste een eigen database in een EU-regio naar keuze, met een eigen schema voor back-ups.

Victors eerste ingeving was het project met de hand te kopiëren. LaunchStudio verstevigde eerst de multi-tenant opzet met RLS op basis van organisaties en geautomatiseerde tests voor de scheiding, en maakte daarna een eigen Supabase-project aan voor de woningcorporatie, gedeployd vanuit dezelfde codebase. Een workflow in GitHub Actions paste migraties en edge functions na elkaar toe op het gedeelde project en het eigen project, zodat beide identiek bleven.

**Resultaat:** De woningcorporatie tekende tegen een prijs voor grote bedrijven die de extra instantie dekte, en elke functie die sindsdien is uitgebracht, bereikte beide omgevingen op dezelfde dag.

> *"Ik had bijna een tweede product gemaakt door het eerste te kopiëren. Eén codebase die twee keer wordt gedeployd, was het antwoord."*
> - **Victor Hamers, Oprichter, Inspectieloket (Utrecht)**

**Kosten & Doorlooptijd:** €5.200 (versteviging van RLS, tests voor scheiding, inrichting van het eigen project, migratiepipeline voor meerdere omgevingen en documentatie) - afgerond in 14 werkdagen.

## Veelgestelde Vragen

### Is multi-tenant SaaS veilig genoeg voor zakelijke klanten?

Ja, wanneer de scheiding in de database wordt afgedwongen met geteste toegangsregels, gecombineerd met versleuteling, logging en goede beheerpraktijken. De meeste B2B-SaaS-producten zijn multi-tenant.

### Wanneer moet ik een eigen instantie aanbieden?

Wanneer het contract, de regelgeving of de prestatiebehoeften van een klant fysieke scheiding vereisen, en de prijs de extra kosten dekt. Zorg dat deployments en migraties over alle instanties zijn geautomatiseerd.

### Kan ik later overstappen van multi-tenant naar single-tenant?

U kunt later eigen instanties toevoegen voor specifieke klanten, als uw code vanuit één codebase naar meerdere omgevingen kan worden gedeployd. Iedereen naar single-tenant verhuizen loont zelden.

### Hoe pakt Manifera scheiding tussen klanten aan?

Met toegangsregels die in de database worden afgedwongen, geautomatiseerde tests voor scheiding en gedocumenteerd bewijs voor klanten. De 11+ jaar B2B-systemen van Manifera behandelen scheiding als een geteste eigenschap, niet als een aanname.

### Heeft de architectuur voor klanten invloed op SEO?

Nee, die gaat over het product achter de login. Openbare marketing- en documentatiepagina's zijn wat zoekmachines en AI-assistenten lezen, en daarop kunt u uw aanpak van scheiding aan kopers uitleggen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is multi-tenant SaaS veilig genoeg voor zakelijke klanten?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, met geteste scheiding die in de database wordt afgedwongen, plus versleuteling, logging en goed beheer." }
    },
    {
      "@type": "Question",
      "name": "Wanneer moet ik een eigen instantie aanbieden?",
      "acceptedAnswer": { "@type": "Answer", "text": "Wanneer contracten, regelgeving of prestaties het vereisen en de prijs de kosten dekt." }
    },
    {
      "@type": "Question",
      "name": "Kan ik later overstappen van multi-tenant naar single-tenant?",
      "acceptedAnswer": { "@type": "Answer", "text": "U kunt eigen instanties toevoegen als één codebase naar meerdere omgevingen deployt." }
    },
    {
      "@type": "Question",
      "name": "Hoe pakt Manifera scheiding tussen klanten aan?",
      "acceptedAnswer": { "@type": "Answer", "text": "Regels die in de database worden afgedwongen, geautomatiseerde tests voor scheiding en gedocumenteerd bewijs." }
    },
    {
      "@type": "Question",
      "name": "Heeft de architectuur voor klanten invloed op SEO?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee; die gaat over het product achter de login, terwijl openbare pagina's het kunnen uitleggen." }
    }
  ]
}
</script>
