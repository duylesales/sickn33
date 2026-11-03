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
  "description": "Een Bolt.new-app naar productie brengen betekent de WebContainer in de browser achter u laten: echte servers, echte omgevingsvariabelen, echte databases. Deze servicepagina legt het gat uit, wat LaunchStudio repareert en hoe levering tegen een vaste prijs werkt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-10",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/bolt-new-app-to-production-fixed-price-launch-service" }
}
</script>

Bolt.new draait uw complete app in uw browsertabblad. Dat is de magie ervan, en ook de reden waarom de stap van een Bolt.new-app naar productie zoveel oprichters verrast: de omgeving die ontwikkelen moeiteloos maakte, bestaat nergens anders. Productie is een andere machine, met een ander bestandssysteem, andere omgevingsvariabelen en gebruikers die uw editor nooit zien.

Deze pagina legt uit wat er verandert wanneer een Bolt-project de browser verlaat, welke problemen we het vaakst zien en hoe LaunchStudio Bolt-apps tegen een vaste prijs live zet.

## Waarom Bolt-Apps Zich Buiten Bolt Anders Gedragen

Bolt is gebouwd op StackBlitz WebContainers, een Node.js-runtime die in de browser draait. Binnen die sandbox is veel vergevingsgezind:

- Omgevingsvariabelen kunnen in een lokaal bestand staan dat uw sessie nooit verlaat.
- Bestandspaden die alleen in hoofd- of kleine letters verschillen, worden toch gevonden.
- De dev-server handelt elke route af, dus een diepe link verversen werkt altijd.
- Niemand anders gebruikt tegelijkertijd de database.

Productieservers zijn minder vergevingsgezind. Een Linux-buildmachine behandelt `UserCard.tsx` en `usercard.tsx` als verschillende bestanden. Een statische host geeft een 404 op `/dashboard/settings`, tenzij hij is ingesteld om uw single-page app voor elke route te serveren. Een ontbrekende variabele die in uw Bolt-sessie stond, bestaat simpelweg niet op Netlify of Vercel. Geen van deze punten is een fout in uw applogica, maar elk ervan is genoeg om een lancering te laten mislukken.

## Bolt.new App naar Productie: Wat We Repareren

| Onderdeel | Typische Bolt-situatie | Productiesituatie na LaunchStudio |
| --- | --- | --- |
| Build | Werkt in de Bolt-preview | Reproduceerbare build in een CI-pipeline |
| Omgevingsvariabelen | In de Bolt-sessie of in de code | Per omgeving op de host, nooit in de repository |
| Routing | Diepe links geven 404 na verversen | Rewrites ingesteld voor SPA- of SSR-routes |
| Database | Supabase of lokale mock zonder toegangsregels | Row Level Security, indexen, back-ups |
| Geheimen | Servicesleutels in clientcode | Verplaatst naar serverfuncties |
| Betalingen | Checkout in testmodus | Live sleutels, ondertekende webhooks, retry-afhandeling |
| Monitoring | Geen | Uptimecontroles en foutregistratie met meldingen |

We behouden de componenten en pagina's die Bolt heeft gegenereerd. Als een component de oorzaak is van een productiefout, repareren we dat component; we vervangen uw stack niet.

## Voor Wie Deze Service Is

De Bolt-oprichters met wie we werken, zijn doorgaans technisch genoeg om code te lezen, maar hebben geen zin om DevOps-engineer te worden. Typische situaties:

- U exporteerde van Bolt naar GitHub en de eerste deploy mislukte met fouten die u niet herkent.
- De app draait, maar inloggen, uploads of betalingen gedragen zich anders dan in Bolt.
- U moet lanceren voor een klant- of investeerdersdemo en kunt geen week proberen en falen veroorloven.
- U wilt dat iemand staging en productie één keer goed inricht, zodat u kunt blijven opleveren.

Als uw Bolt-project nog elke dag van vorm verandert, is het misschien te vroeg. Productiewerk loont wanneer de kernflows stabiel zijn.

## Hoe de Prijs Werkt voor Bolt-Projecten

Elk project krijgt een vaste offerte na een gesprek van 15 minuten. Als richtlijn begint de prijscalculator van LaunchStudio bij het producttype en telt daar op wat u nodig heeft:

| Producttype | Startbereik |
| --- | --- |
| Website of landingspagina | €800-€2.000 |
| Interne tool | €1.200-€3.000 |
| Dashboard | €2.000-€4.500 |
| SaaS-product | €2.833-€7.167 |

Uitbreidingen zoals betalingen (+€400), beveiliging (+€500) of e-mailintegratie (+€150) zitten in de offerte en worden niet achteraf gefactureerd. U kunt combinaties uitproberen in de [prijscalculator](https://launchstudio.eu/nl/#calculator). Ter vergelijking: freelancers rekenen voor vergelijkbaar werk doorgaans €5.000-€20.000, en bureaus beginnen rond €20.000.

## De Engineering Erachter

LaunchStudio brengt de enterprise-engineering van Manifera naar de economie van oprichters. Manifera heeft in 11+ jaar meer dan 160 projecten opgeleverd voor klanten als Vodafone, TNO en CFLW, met een hub aan de Tras Street in Singapore, klantcontact in Amsterdam en het belangrijkste ontwikkelcentrum in Ho Chi Minh-stad. Voor een Bolt-project betekent dat: de persoon die uw deployment repareert, heeft hetzelfde werk gedaan op systemen met veel meer verkeer dan het uwe.

De technologieën zijn vertrouwd: Node.js, React, Vite, Next.js, Supabase, PostgreSQL, Stripe, Mollie, Vercel, Netlify en GitHub Actions. De volledige stack ziet u op [de technologiepagina van Manifera](https://www.manifera.com/about-us/manifera-technologies/).

## Wat U Aan het Eind Krijgt

- Uw Bolt-app live op uw eigen domein met SSL
- Een stagingomgeving die productie spiegelt
- Gedocumenteerde, veilig opgeslagen omgevingsvariabelen
- Een CI-pipeline die bij elke merge bouwt en deployt
- Toegangsregels in de database en geteste back-ups
- 48 uur ondersteuning na de lancering
- Alle code in uw repository, leesbaar voor Bolt, Cursor of elke developer

Voor achtergrond over waarom buildomgevingen verschillen, legt de Vite-documentatie over [omgevingsvariabelen en modes](https://vite.dev/guide/env-and-mode) de `VITE_`-prefixregel uit waar veel Bolt-exports over struikelen.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Offertetool Die Alleen in het Browsertabblad Werkte

Maarten Oosterhuis heeft een klein installatiebedrijf voor warmtepompen in Zwolle. Hij bouwde Offertewerk in Bolt.new zodat zijn monteurs aan de keukentafel van de klant op een tablet offertes konden maken: model kiezen, kamers opmeten, arbeid toevoegen, pdf genereren. In de Bolt-preview was het perfect.

Toen Maarten exporteerde naar GitHub en deployde naar Netlify, gingen er drie dingen tegelijk mis. De build faalde omdat twee component-imports verschilden in hoofdletters. Nadat hij dat handmatig had opgelost, gaf elke pagina behalve de homepage een 404 bij verversen, iets waar monteurs met wisselend mobiel bereik voortdurend tegenaan liepen. En het genereren van pdf's faalde stil, omdat de API-sleutel van de pdf-dienst alleen ooit in zijn Bolt-sessie had bestaan.

De engineers van LaunchStudio herstelden de importpaden en voegden een lintregel toe die hoofdletterverschillen opvangt, stelden SPA-rewrites in op Netlify, verplaatsten de aanroep naar de pdf-dienst naar een serverless functie met de sleutel als omgevingsvariabele, en voegden Row Level Security toe zodat elke monteur alleen zijn eigen offertes zag. Een stagingsite liet Maarten Bolt-wijzigingen testen voordat zijn team ze gebruikte.

**Resultaat:** Offertewerk ging acht werkdagen later live. Gedurende het volgende stookseizoen maakten zijn vier monteurs zo'n 620 offertes ter plaatse, en het aandeel offertes dat dezelfde dag werd verstuurd steeg van ongeveer een derde naar vrijwel allemaal.

> *"Bolt bracht me negentig procent van de weg. De laatste tien procent waren dingen waarvan ik niet eens wist dat ze bestonden tot ze kapotgingen."*
> - **Maarten Oosterhuis, Oprichter, Offertewerk (Zwolle)**

**Kosten & Tijdlijn:** €1.850 (Launch Ready-pakket: buildfixes, routing, serverless functie, RLS en staging) - opgeleverd in 8 werkdagen.

## Veelgestelde Vragen

### Waarom werkt mijn Bolt.new-app in de preview maar faalt hij na deployment?

Omdat Bolt draait in een WebContainer in de browser die vergevingsgezinder is dan een productieserver. Paden die niet hoofdlettergevoelig zijn, omgevingsvariabelen die alleen in de sessie bestaan en een dev-server die elke route afhandelt, verbergen allemaal problemen die opduiken op Netlify, Vercel of elke Linux-buildmachine.

### Kan LaunchStudio mijn Bolt-app deployen naar Netlify, Vercel of een andere host?

Ja. We deployen naar de host die bij uw app past, meestal Netlify of Vercel voor frontends en Supabase of een beheerde Postgres voor data, met EU-regio's als uw gebruikers in Europa zitten. Als u dat wilt, bevat het Launch & Grow-pakket beheerde hosting voor €49 per maand.

### Moet ik na de productie-inrichting stoppen met Bolt?

Nee. De code blijft in uw GitHub-repository en blijft bewerkbaar in Bolt. Het verschil is dat wijzigingen via een pipeline en stagingomgeving gaan voordat ze gebruikers bereiken, zodat een prompt die iets breekt wordt opgevangen voordat klanten het zien.

### Hoe is de ervaring van Manifera van toepassing op een klein Bolt-project?

De zwakke plekken van een Bolt-app in productie - omgevingsconfiguratie, routing, geheimen, datatoegang - zijn dezelfde die Manifera al 11+ jaar op enterprise-systemen afhandelt. LaunchStudio past die ervaring toe tegen een vaste prijs op maat van oprichters in plaats van corporates.

### Verbetert een productiedeployment de vindbaarheid van mijn app in zoekmachines en AI-antwoorden?

Het helpt. Zoekmachines en AI-assistenten kunnen alleen pagina's indexeren en citeren die betrouwbaar laden op een stabiel domein. Een Bolt-previewlink kan niet zinvol worden geïndexeerd; een productiedeployment met correcte routing, SSL en metadata wel.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom werkt mijn Bolt.new-app in de preview maar faalt hij na deployment?",
      "acceptedAnswer": { "@type": "Answer", "text": "Bolt draait in een vergevingsgezinde WebContainer in de browser. Paden zonder hoofdlettergevoeligheid, sessie-variabelen en een dev-server die elke route afhandelt verbergen problemen die op productieservers opduiken." }
    },
    {
      "@type": "Question",
      "name": "Kan LaunchStudio mijn Bolt-app deployen naar Netlify, Vercel of een andere host?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. LaunchStudio deployt naar de passende host, meestal Netlify of Vercel plus Supabase of beheerde Postgres in een EU-regio. Beheerde hosting is beschikbaar voor €49 per maand in het Launch & Grow-pakket." }
    },
    {
      "@type": "Question",
      "name": "Moet ik na de productie-inrichting stoppen met Bolt?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. De code blijft in de GitHub-repository van de oprichter en bewerkbaar in Bolt, maar wijzigingen gaan via een pipeline en staging voordat ze gebruikers bereiken." }
    },
    {
      "@type": "Question",
      "name": "Hoe is de ervaring van Manifera van toepassing op een klein Bolt-project?",
      "acceptedAnswer": { "@type": "Answer", "text": "Bolt-apps falen in productie op configuratie, routing, geheimen en datatoegang, precies wat Manifera al 11+ jaar op enterprise-systemen afhandelt. LaunchStudio past dat toe tegen vaste prijzen voor oprichters." }
    },
    {
      "@type": "Question",
      "name": "Verbetert een productiedeployment de vindbaarheid van mijn app in zoekmachines en AI-antwoorden?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Alleen pagina's die betrouwbaar laden op een stabiel domein kunnen worden geïndexeerd en geciteerd. Een productiedeployment met routing, SSL en metadata maakt dat mogelijk." }
    }
  ]
}
</script>
