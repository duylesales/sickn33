---
Titel: "Bolt.new App naar Productie: Een Lanceringsservice met Vaste Prijs"
Trefwoorden: bolt app naar productie, bolt.new app live zetten, bolt.new developer, bolt app lanceren, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Bolt.new App naar Productie: Een Lanceringsservice met Vaste Prijs

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bolt.new App naar Productie: Een Lanceringsservice met Vaste Prijs",
  "description": "Een Bolt.new-app naar productie brengen betekent de WebContainer in de browser achter u laten: echte servers, echte omgevingsvariabelen, echte databases. Deze gids legt uit waarom Bolt-apps zich in productie anders gedragen, welke fouten we het vaakst zien, geeft een productiechecklist en laat zien hoe LaunchStudio Bolt-apps tegen een vaste prijs live zet.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-10",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/bolt-new-app-to-production-fixed-price-launch-service" },
  "citation": [
    { "@type": "CreativeWork", "name": "StackBlitz WebContainers", "url": "https://webcontainers.io/" },
    { "@type": "CreativeWork", "name": "Vite: Env Variables and Modes", "url": "https://vite.dev/guide/env-and-mode" },
    { "@type": "CreativeWork", "name": "DORA 2024 Accelerate State of DevOps Report", "url": "https://dora.dev/research/2024/dora-report/" },
    { "@type": "CreativeWork", "name": "OWASP Secrets Management Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A05 Security Misconfiguration", "url": "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/" },
    { "@type": "CreativeWork", "name": "Google SRE Book: Monitoring Distributed Systems", "url": "https://sre.google/sre-book/monitoring-distributed-systems/" }
  ]
}
</script>

Bolt.new draait uw hele app in uw browsertabblad. Dat is de magie ervan, en ook de reden dat de overstap van een Bolt.new-app naar productie zoveel oprichters verrast: de omgeving die ontwikkelen moeiteloos maakte, bestaat nergens anders. Productie is een andere machine, met een ander bestandssysteem, andere omgevingsvariabelen en gebruikers die uw editor nooit zullen zien.

Deze gids legt uit wat er verandert als een Bolt-project de browser verlaat, welke problemen we het vaakst zien, geeft een checklist die u zelf kunt gebruiken, en laat zien hoe LaunchStudio Bolt-apps tegen een vaste prijs live zet.

## Belangrijkste Punten

- **Bolt draait op StackBlitz WebContainers,** een Node.js-runtime in de browser. Die is vergevingsgezind op manieren waarop productieservers dat niet zijn, en daarom zijn "werkt in Bolt" en "werkt in productie" verschillende beweringen.
- **De meeste eerste deployments falen op configuratie, niet op logica:** omgevingsvariabelen, routing van single-page apps, hoofdlettergevoelige imports en geheime sleutels. OWASP noemt security misconfiguration juist daarom een van de grootste risico's voor webapplicaties.
- **Snelheid zonder proces verlaagt de stabiliteit.** Het DORA-onderzoek van Google uit 2024 vond dat meer AI-gebruik samenging met een geschatte daling van 7,2% in de stabiliteit van softwarelevering, als het niet werd gecombineerd met goede werkwijzen.
- **Een productierijpe Bolt-app heeft een pipeline nodig, niet alleen een host:** reproduceerbare builds, gescheiden omgevingen, geheimen op de server, toegangsregels in de database, back-ups en monitoring.
- **LaunchStudio zet Bolt-apps in één tot drie weken live voor een vaste €800-€7.500,** met behoud van de componenten die Bolt genereerde.

## Waarom Bolt-Apps zich Buiten Bolt Anders Gedragen

Met WebContainers kan Bolt Node.js, een package manager en een ontwikkelserver volledig in uw browser draaien. Binnen die sandbox is veel vergevingsgezind:

- Omgevingsvariabelen kunnen in een lokaal bestand staan dat uw sessie nooit verlaat.
- Bestandspaden die alleen in hoofd- of kleine letters verschillen, worden mogelijk toch gevonden.
- De ontwikkelserver handelt elke route af, dus het verversen van een diepe link werkt altijd.
- Niemand anders gebruikt de database tegelijk, dus racecondities verschijnen nooit.
- Fouten zijn zichtbaar in de console van de editor, dus niets faalt stil.

Productieservers zijn minder vergevingsgezind. Een Linux-buildmachine behandelt `UserCard.tsx` en `usercard.tsx` als verschillende bestanden. Een statische host geeft een 404 op `/dashboard/settings`, tenzij hij is ingesteld om uw single-page app voor elke route te serveren. Een variabele die in uw Bolt-sessie was ingesteld, bestaat simpelweg niet op Netlify of Vercel. Met Vite, de bundler die de meeste Bolt-projecten gebruiken, worden alleen variabelen met het voorvoegsel `VITE_` beschikbaar gemaakt voor browsercode, en ze worden tijdens de build ingebakken. Geen van deze dingen is een fout in uw applogica, maar elk ervan is genoeg om een lancering te laten mislukken.

## De Zeven Fouten Die We het Vaakst Zien

| # | Fout | Symptoom na deploy | Oorzaak |
| --- | --- | --- | --- |
| 1 | Ontbrekende omgevingsvariabelen | Leeg scherm, "undefined" API-URL's | Variabelen bestonden alleen in de Bolt-sessie |
| 2 | SPA-routing | 404 bij verversen of gedeelde links | Geen rewrite naar `index.html` op de host |
| 3 | Hoofdlettergevoelige imports | Build faalt met "module not found" | Linux-bestandssysteem, verschil in hoofdletters |
| 4 | Geheimen in de frontend | Sleutels zichtbaar in de paginabron | Geheime sleutels in `VITE_`-variabelen of componenten |
| 5 | Node-code in de browser | `process is not defined`, `fs`-fouten | Serverlogica meegebundeld in de client |
| 6 | Verkeerde redirect bij inloggen | Inloggen stuurt gebruikers naar de preview-URL | Productiedomein ontbreekt in Supabase- of OAuth-instellingen |
| 7 | Geen toegangscontrole in de database | Gebruikers kunnen elkaars gegevens lezen | Policies nooit geschreven of te ruim |

Fouten 1-3 en 5-6 houden de lancering tegen. Fouten 4 en 7 zijn erger: de app gaat live en lijkt te werken, terwijl hij gegevens of sleutels blootstelt. Het Secrets Management Cheat Sheet van OWASP is duidelijk: geheimen horen in een beheerde opslag op de server, nooit in clientcode of versiebeheer.

## Bolt.new App naar Productie: Wat We Repareren

| Onderdeel | Gangbare Bolt-situatie | Productiesituatie na LaunchStudio |
| --- | --- | --- |
| Build | Werkt in de Bolt-preview | Reproduceerbare build in een CI-pipeline |
| Omgevingsvariabelen | Ingesteld in de Bolt-sessie of in code vastgelegd | Per omgeving opgeslagen bij de host, nooit in de repo |
| Routing | Diepe links geven 404 na verversen | Rewrites ingesteld voor SPA- of SSR-routes |
| Database | Supabase of lokale mock zonder toegangsregels | Row Level Security, indexen, back-ups |
| Geheimen | Servicesleutels in clientcode | Verplaatst naar serverfuncties en vervangen |
| Betalingen | Checkout in testmodus | Live sleutels, ondertekende webhooks, herhaalafhandeling |
| Monitoring | Geen | Uptimecontroles en foutregistratie met meldingen |

We behouden de componenten en pagina's die Bolt genereerde. Als een component de oorzaak is van een productiefout, repareren we dat component; we wisselen uw stack niet om.

## Een Productiechecklist voor Bolt-Apps

Of u het werk zelf doet of hulp inhuurt, deze controles overbruggen de kloof tussen preview en productie:

**Build en deploy**
- De app bouwt vanaf een schone kopie van de repository met `npm ci` en `npm run build`
- Een linter vangt verschillen in hoofdletters en ongebruikte imports
- `main` deployt naar staging; een aparte branch of release deployt naar productie
- Terugdraaien naar de vorige release kost één klik

**Configuratie**
- Elke benodigde variabele staat zonder waarde in een `.env.example`-bestand
- Frontendvariabelen gebruiken het juiste voorvoegsel; geheimen nooit
- Staging en productie gebruiken verschillende sleutels, ook test- en live sleutels voor betalingen

**Beveiliging**
- Row Level Security is ingeschakeld en getest op elke tabel met gebruikersgegevens
- Adminfuncties zijn op de server beveiligd, niet alleen verborgen in de UI
- Elke sleutel die ooit is vastgelegd of blootgesteld, is vervangen

**Beheer**
- Back-ups zijn ingeschakeld en een terugzetting is getest
- Uptime- en foutmeldingen bereiken een telefoon
- U kunt zien wie wat wanneer heeft gedeployd

De SRE-richtlijnen van Google over monitoring raden aan te alarmeren op symptomen die gebruikers merken, zoals fouten en vertraging, in plaats van op elke interne meetwaarde. Voor een kleine app is een uptimecontrole met foutregistratie en verstandige drempels genoeg om te beginnen.

## Snelheid, Stabiliteit en Waarom Proces Belangrijk Is

AI-tools maken het makkelijk om snel wijzigingen uit te rollen. Het DORA 2024 Accelerate State of DevOps-rapport vond dat een toename van 25% in AI-gebruik samenging met een geschatte daling van 1,5% in leveringsdoorvoer en 7,2% in leveringsstabiliteit. De interpretatie van het rapport is niet dat AI slecht is, maar dat snellere codegeneratie zonder ondersteunende werkwijzen - kleine wijzigingen, testen, review, gefaseerde uitrol - leidt tot meer mislukte wijzigingen.

Voor een Bolt-oprichter vertaalt dat zich in een praktische regel: de pipeline wordt belangrijker naarmate u meer prompt. Een stagingomgeving en een paar geautomatiseerde controles veranderen een kapotte Bolt-wijziging van een klantincident in een mislukte build.

## Voor Wie Deze Service Is

De Bolt-oprichters met wie we werken, zijn meestal technisch genoeg om code te lezen, maar hebben geen interesse om DevOps-engineer te worden. Gangbare situaties:

- U exporteerde van Bolt naar GitHub en de eerste deploy faalde met fouten die u niet herkent.
- De app deployt, maar inloggen, bestandsuploads of betalingen gedragen zich anders dan in Bolt.
- U moet lanceren voor een klant- of investeerdersdemo en kunt geen week proberen en falen veroorloven.
- U wilt dat iemand staging en productie één keer goed inricht, zodat u kunt blijven uitrollen.

Als uw Bolt-project nog elke dag van vorm verandert, is het misschien te vroeg. Productiewerk betaalt zich uit wanneer de kernflows stabiel zijn.

## Hoe de Prijs Werkt voor Bolt-Projecten

Elk project krijgt een vaste offerte na een gesprek van 15 minuten. Als richtlijn begint de prijscalculator van LaunchStudio bij het producttype en telt hij op wat u nodig heeft:

| Producttype | Startbereik |
| --- | --- |
| Website of landingspagina | €800-€2.000 |
| Interne tool | €1.200-€3.000 |
| Webshop | €1.500-€3.500 |
| Dashboard | €2.000-€4.500 |
| SaaS-product | €2.833-€7.167 |

Uitbreidingen zoals betalingen (+€400), beveiligingsversterking (+€500) of e-mailintegratie (+€150) zijn opgenomen in de offerte en worden niet achteraf gefactureerd. U kunt combinaties proberen met de [prijscalculator](https://launchstudio.eu/nl/#calculator). Ter vergelijking: freelancers offreren voor vergelijkbaar werk meestal €5.000-€20.000 en bureaus beginnen rond €20.000.

## De Engineering Erachter

LaunchStudio brengt de engineering van Manifera op enterpriseniveau naar de economie van oprichters. Manifera heeft in 11+ jaar 160+ projecten opgeleverd voor klanten als Vodafone, TNO en CFLW, met een leveringshub aan de Tras Street in Singapore, klantcontact in Amsterdam en het belangrijkste ontwikkelcentrum in Ho Chi Minh City. Voor een Bolt-project betekent dat dat degene die uw deployment repareert, hetzelfde werk heeft gedaan op systemen met veel meer verkeer dan het uwe, en dat het werk door een tweede engineer wordt gereviewd voordat het live gaat.

De technologieën zijn bekende: Node.js, React, Vite, Next.js, Supabase, PostgreSQL, Stripe, Mollie, Vercel, Netlify en GitHub Actions. De bredere stack ziet u op [de technologiepagina van Manifera](https://www.manifera.com/about-us/manifera-technologies/).

## Wat U aan het Einde Krijgt

- Uw Bolt-app live op uw eigen domein met SSL
- Een stagingomgeving die productie spiegelt
- Omgevingsvariabelen gedocumenteerd en veilig opgeslagen
- Een CI-pipeline die bij elke merge bouwt en deployt
- Toegangsregels in de database en back-ups die u heeft getest
- 48 uur support na de lancering
- Alle code in uw repository, leesbaar voor Bolt, Cursor of elke developer

Als u een mislukte deployment eerst zelf wilt diagnosticeren, behandelt ons artikel over [waarom Bolt-apps na deployment kapotgaan](https://launchstudio.eu/nl/blog/why-does-my-bolt-app-break-after-deploy) elke fout met de oplossing.

## Kiezen Waar Uw Bolt-App Moet Draaien

Bolt maakt deployen naar Netlify eenvoudig, en voor veel projecten is dat het juiste antwoord. Het is niet het enige, en de keuze beïnvloedt later kosten, prestaties en compliance.

| Optie | Geschikt wanneer | Let op |
| --- | --- | --- |
| Netlify | Vite single-page apps, eenvoudige serverless functions, snelle previews | Limieten van functies voor langlopend werk |
| Vercel | Next.js-projecten of server rendering voor SEO-pagina's | Regio-instellingen voor gegevensverwerking in de EU |
| Cloudflare Pages | Wereldwijde statische levering met edge functions | Andere runtime-API's dan Node.js |
| Beheerde hosting van LaunchStudio | U wilt hosting, SSL, monitoring en back-ups laten regelen | Een maandbedrag van €49 in het Launch & Grow-pakket |

Twee vragen beslissen de meeste gevallen. Ten eerste: heeft een deel van uw app een langlopend proces nodig, zoals een queue worker of geplande taak? Plan dat dan als aparte service of gebruik geplande functies van Supabase, want statische hosts zijn daar niet voor ontworpen. Ten tweede: waar zijn uw gebruikers? Houd voor Europese klanten de database en opslag in een EU-regio en stel de regio's van serverless functions daarop in, zodat persoonsgegevens niet bij elk verzoek naar een ander continent reizen.

Wat u ook kiest, houd de host vervangbaar: bouw vanuit uw eigen repository, houd configuratie in gedocumenteerde omgevingsvariabelen en vermijd platformspecifieke functies voor kernlogica. Zo wordt een prijswijziging of een nieuwe klanteis een configuratietaak in plaats van een migratieproject.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Offertetool Die Alleen in het Browsertabblad Werkte

Maarten Oosterhuis heeft een klein installatiebedrijf voor warmtepompen in Zwolle. Hij bouwde Offertewerk in Bolt.new zodat zijn monteurs aan de keukentafel van de klant op een tablet offertes konden maken: een model kiezen, de ruimtes opmeten, arbeid toevoegen, een pdf genereren. In de Bolt-preview was het perfect.

Toen Maarten naar GitHub exporteerde en naar Netlify deployde, gingen er drie dingen tegelijk kapot. De build faalde omdat twee component-imports in hoofdletters verschilden. Nadat hij dat met de hand had opgelost, gaf elke pagina behalve de homepage een 404 bij verversen, iets waar monteurs op haperende mobiele verbindingen voortdurend tegenaan liepen. En het genereren van pdf's faalde stil, omdat de API-sleutel voor de pdf-service alleen ooit in zijn Bolt-sessie had bestaan.

De engineers van LaunchStudio repareerden de importpaden en voegden een lintregel toe die verschillen in hoofdletters vangt, stelden SPA-rewrites in op Netlify, verplaatsten de aanroep van de pdf-service naar een serverless function met de sleutel als omgevingsvariabele, en voegden Row Level Security toe zodat elke monteur alleen zijn eigen offertes zag. Met een stagingsite kon Maarten Bolt-wijzigingen testen voordat zijn team ze gebruikte, en uptimemeldingen gingen naar zijn telefoon.

**Resultaat:** Offertewerk ging acht werkdagen later live. In het stookseizoen daarna maakten zijn vier monteurs ongeveer 620 offertes vanuit het veld, en het aandeel offertes dat dezelfde dag werd verstuurd, steeg van ongeveer een derde naar vrijwel allemaal.

> *"Bolt bracht me negentig procent van de weg. De laatste tien procent waren dingen waarvan ik niet eens wist dat ze bestonden tot ze kapotgingen."*
> - **Maarten Oosterhuis, Oprichter, Offertewerk (Zwolle)**

**Kosten & Doorlooptijd:** €1.850 (Launch Ready-pakket: buildfixes, routing, serverless function, RLS en staging) - afgerond in 8 werkdagen.

## Veelgestelde Vragen

### Waarom werkt mijn Bolt.new-app in de preview maar faalt hij na deployment?

Omdat Bolt draait in een WebContainer in de browser die vergevingsgezinder is dan een productieserver. Hoofdletterongevoelige bestandspaden, omgevingsvariabelen die alleen in de sessie bestaan en een ontwikkelserver die elke route afhandelt, verbergen allemaal problemen die opduiken op Netlify, Vercel of elke Linux-buildmachine.

### Kan LaunchStudio mijn Bolt-app deployen naar Netlify, Vercel of een andere host?

Ja. We deployen naar de host die bij uw app past, meestal Netlify of Vercel voor frontends en Supabase of een beheerde Postgres voor data, met EU-regio's als uw gebruikers in Europa zitten. Als u dat liever heeft, omvat het Launch & Grow-pakket beheerde hosting voor €49 per maand.

### Moet ik na de productie-inrichting stoppen met Bolt?

Nee. De code blijft in uw GitHub-repository en blijft bewerkbaar in Bolt. Het verschil is dat wijzigingen via een pipeline en stagingomgeving gaan voordat ze gebruikers bereiken, zodat een prompt die iets kapotmaakt wordt opgemerkt voordat klanten het zien.

### Hoe is de ervaring van Manifera van toepassing op een klein Bolt-project?

De zwakke plekken van een Bolt-app in productie - configuratie van de omgeving, routing, geheimen, toegang tot data - zijn dezelfde die Manifera al 11+ jaar op enterprisesystemen afhandelt. LaunchStudio past die ervaring toe tegen een vaste prijs die past bij oprichters in plaats van grote bedrijven.

### Verbetert een productiedeployment de zichtbaarheid van mijn app in zoekmachines en AI-antwoorden?

Het helpt. Zoekmachines en AI-assistenten kunnen alleen pagina's indexeren en citeren die betrouwbaar laden op een stabiel domein. Een Bolt-previewlink kan niet zinvol worden geïndexeerd; een productiedeployment met goede routing, SSL en metadata wel.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom werkt mijn Bolt.new-app in de preview maar faalt hij na deployment?",
      "acceptedAnswer": { "@type": "Answer", "text": "Bolt draait in een vergevingsgezinde WebContainer in de browser. Hoofdletterongevoelige paden, omgevingsvariabelen die alleen in de sessie bestaan en een ontwikkelserver die elke route afhandelt, verbergen problemen die op productiehosts en buildmachines opduiken." }
    },
    {
      "@type": "Question",
      "name": "Kan LaunchStudio mijn Bolt-app deployen naar Netlify, Vercel of een andere host?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. LaunchStudio deployt naar de host die bij de app past, meestal Netlify of Vercel plus Supabase of beheerde Postgres in een EU-regio. Beheerde hosting is beschikbaar voor €49 per maand in het Launch & Grow-pakket." }
    },
    {
      "@type": "Question",
      "name": "Moet ik na de productie-inrichting stoppen met Bolt?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. De code blijft in de GitHub-repository van de oprichter en blijft bewerkbaar in Bolt, maar wijzigingen gaan via een pipeline en staging voordat ze gebruikers bereiken." }
    },
    {
      "@type": "Question",
      "name": "Hoe is de ervaring van Manifera van toepassing op een klein Bolt-project?",
      "acceptedAnswer": { "@type": "Answer", "text": "Bolt-apps falen in productie op configuratie van de omgeving, routing, geheimen en toegang tot data, dezelfde gebieden die Manifera al 11+ jaar op enterprisesystemen afhandelt. LaunchStudio past dat toe tegen vaste prijzen voor oprichters." }
    },
    {
      "@type": "Question",
      "name": "Verbetert een productiedeployment de zichtbaarheid van mijn app in zoekmachines en AI-antwoorden?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Alleen pagina's die betrouwbaar laden op een stabiel domein kunnen worden geïndexeerd en geciteerd. Een productiedeployment met routing, SSL en metadata maakt dat mogelijk." }
    }
  ]
}
</script>
