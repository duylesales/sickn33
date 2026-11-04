---
Titel: "Hoe Verhuis Ik Mijn Lovable-App naar Mijn Eigen Hosting?"
Trefwoorden: lovable eigen hosting, lovable deployen naar vercel, lovable netlify, lovable-app zelf hosten, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Hoe Verhuis Ik Mijn Lovable-App naar Mijn Eigen Hosting?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Verhuis Ik Mijn Lovable-App naar Mijn Eigen Hosting?",
  "description": "Een Lovable-app verhuizen van publiceren via Lovable naar uw eigen host geeft u controle over deployments, regio's, previews en terugdraaien. Deze gids behandelt het kiezen van een host, GitHub koppelen, omgevingsvariabelen, SPA-routing, de overstap van het domein en wat er in uw werkwijze verandert.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-15",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-do-i-move-my-lovable-app-to-my-own-hosting" },
  "citation": [
    { "@type": "CreativeWork", "name": "Vercel: Vite on Vercel", "url": "https://vercel.com/docs/frameworks/frontend/vite" },
    { "@type": "CreativeWork", "name": "Vite: Env Variables and Modes", "url": "https://vite.dev/guide/env-and-mode" },
    { "@type": "CreativeWork", "name": "DORA 2024 Accelerate State of DevOps Report", "url": "https://dora.dev/research/2024/dora-report/" },
    { "@type": "CreativeWork", "name": "web.dev: Web Vitals", "url": "https://web.dev/articles/vitals" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A05 Security Misconfiguration", "url": "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/" }
  ]
}
</script>

**Kort antwoord:** synchroniseer uw Lovable-project met GitHub, importeer die repository in een host zoals Vercel, Netlify of Cloudflare Pages, stel het buildcommando en de omgevingsvariabelen in, voeg een rewrite toe zodat alle routes `index.html` serveren, test op de preview-URL van de host en laat daarna de DNS van uw domein naar de nieuwe host wijzen. Uw Supabase-backend blijft waar hij is. Daarna blijft Lovable uw editor, maar bepaalt uw host wat er live gaat.

## Belangrijkste Punten

- **Een Lovable-app verhuizen naar uw eigen host** - Vercel, Netlify, Cloudflare Pages of beheerde hosting - geeft u previews, staging, terugdraaien en onafhankelijkheid.
- **De stappen zijn overzichtelijk:** synchroniseren met GitHub, importeren in de host, buildinstellingen en omgevingsvariabelen instellen, een SPA-rewrite toevoegen, toegestane URL's bijwerken, DNS omzetten.
- **Uw Supabase-backend blijft waar hij is;** alleen redirect-URL's en instellingen bij providers hebben het nieuwe domein nodig.
- **Lovable blijft uw editor,** maar uw host bepaalt wat klanten bereikt.
- **Kies regio's en instellingen met gebruikers in de EU in gedachten,** en houd één canoniek domein aan voor SEO.

## Waarom Oprichters Verhuizen

- **Controle over releases:** staging, previews per wijziging en direct terugdraaien
- **Onafhankelijkheid** van het publiceren via de builder (zie ons artikel over [wat er gebeurt als Lovable verandert](https://launchstudio.eu/nl/blog/what-happens-to-my-app-if-lovable-changes-pricing-or-shuts-down))
- **Regio's en prestaties:** kies waar functies draaien en gebruik een CDN dat u zelf instelt
- **Werkwijzen in teams:** ontwikkelaars kunnen deployen zonder toegang tot de builder
- **Contracten:** klanten vragen soms waar en hoe de app wordt gehost

## Een Host Kiezen

| Host | Sterke punten voor Lovable-apps |
| --- | --- |
| Vercel | Eenvoudige Git-integratie, previews, prettige ontwikkelervaring |
| Netlify | Vergelijkbare functies, overzichtelijke redirects |
| Cloudflare Pages | Wereldwijd CDN, royaal gratis niveau |
| Beheerde hosting (bijv. die van LaunchStudio voor €49/maand) | Hosting, SSL, monitoring en back-ups worden voor u geregeld |

Voor een React-app op basis van Vite werken ze allemaal goed.

## Stap voor Stap

1. **GitHub.** Zorg dat het Lovable-project gesynchroniseerd is met een repository in uw bedrijfsorganisatie.
2. **Importeren.** Maak bij de host een project aan vanuit die repository.
3. **Buildinstellingen.** Buildcommando `npm run build`, outputmap `dist` (bij gangbare Vite-opzetten).
4. **Omgevingsvariabelen.** Voeg uw Supabase-URL en publieke sleutel toe, en andere frontendvariabelen, met het voorvoegsel `VITE_` dat uw code verwacht. Voeg nooit geheime sleutels toe aan frontendvariabelen.
5. **Routing.** Voeg een rewrite toe zodat elk pad `index.html` serveert, anders geven directe links een 404. Ons [artikel over deployen met Bolt](https://launchstudio.eu/nl/blog/why-does-my-bolt-app-break-after-deploy) legt dit in detail uit; het geldt net zo goed voor Lovable.
6. **Test de preview-URL.** Log in, controleer de belangrijkste flows en betalingen in testmodus.
7. **Werk de toegestane URL's bij.** Voeg het nieuwe domein toe aan de redirect-URL's van Supabase Auth, OAuth-providers en de instellingen van uw betaalprovider.
8. **Zet de DNS om.** Laat uw domein naar de nieuwe host wijzen en wacht tot het SSL-certificaat is uitgegeven.
9. **Koppel het oude publiceren los.** Verwijder de oude gepubliceerde URL of stuur die door, zodat er één canonieke site is.

## Waarom Controle over Deployment Ertoe Doet

Direct publiceren vanuit een builder is handig: één klik en de wijziging staat live. Het betekent ook dat elke wijziging direct naar klanten gaat, zonder stagingstap, zonder preview voor een review en zonder snelle weg terug. Het DORA-onderzoek van Google koppelt geautomatiseerde deployment, kleine wijzigingen en snel herstel al lang aan betere resultaten bij oplevering. Uw eigen hosting geeft u die mogelijkheden: elke commit kan een preview opleveren, `main` kan naar staging deployen, productie kan bewust worden gepromoveerd en elke release kan binnen seconden worden teruggedraaid.

## Hosts Uitgebreider Vergeleken

| Aandachtspunt | Vercel | Netlify | Cloudflare Pages |
| --- | --- | --- | --- |
| Git-integratie en previews | Ja | Ja | Ja |
| SPA-rewrites | Rewrites in `vercel.json` | `_redirects` of `netlify.toml` | `_redirects` |
| Serverless- of edge functions | Ja, regio instelbaar | Ja | Workers aan de edge |
| Configuratie gericht op de EU | Regio's van functies te kiezen | Opties per regio verschillen | Wereldwijd edge-netwerk |
| Het meest geschikt voor | Next.js- en React-apps | React en statische sites | Wereldwijd verspreide statische apps |

Voor een standaard Lovable-app werkt elk van deze goed. Kies op basis van de bekendheid van uw team, de prijs bij uw verwachte verkeer en eventuele eisen aan de locatie van gegevens voor functies.

## DNS en Domeinen Zonder Uitval

Het domein naar een nieuwe host omzetten is de stap waar oprichters het meest tegen opzien. Een zorgvuldige volgorde voorkomt uitval: deploy naar de nieuwe host en test grondig op de preview-URL; verlaag een dag van tevoren de time-to-live van uw DNS-records, zodat wijzigingen snel doorkomen; voeg het domein toe bij de nieuwe host en volg de instructies voor de records; werk de DNS bij en wacht tot de SSL-certificaten zijn uitgegeven; controleer daarna inloggen, betalingen en links in e-mails op het live domein. Houd het oude publiceren actief tot u zeker weet dat de nieuwe opzet werkt, en schakel het daarna uit of stuur het door.

## Omgevingsvariabelen en Geheimen

Frontendvariabelen in een Lovable-app op basis van Vite gebruiken het voorvoegsel `VITE_` en worden tijdens de build ingebakken, zoals de documentatie van Vite uitlegt. Alleen openbare waarden horen daar: uw Supabase-URL en publieke sleutel, analytics-ID's en vergelijkbare waarden. Geheime sleutels voor betalingen, e-mail of AI-providers horen in de secrets van Supabase edge functions of in de serveromgeving van uw host, nooit in frontendvariabelen. Stel variabelen apart in voor preview, staging en productie, en bouw opnieuw nadat u ze heeft gewijzigd.

## Prestatie-Instellingen die het Controleren Waard Zijn

Hosts leveren uw statische bestanden via een CDN, waardoor een goed gebouwde Lovable-app wereldwijd snel is. Controleer dat bestanden met een lange cachetijd worden opgeslagen, dat HTML niet te agressief wordt gecachet zodat updates snel verschijnen, dat afbeeldingen zijn gecomprimeerd en dat compressie aanstaat. De Web Vitals van Google meten de laadsnelheid en responsiviteit die gebruikers ervaren; een snelle controle met browsertools na de verhuizing bevestigt dat alles werkt zoals verwacht.

## Beveiligingsheaders

Met uw eigen host kunt u HTTP-beveiligingsheaders toevoegen: een Content Security Policy die beperkt waarvandaan scripts mogen laden, `X-Frame-Options` of frame-ancestors om clickjacking te voorkomen, `Strict-Transport-Security` om HTTPS af te dwingen, en een referrerbeleid. Begin met een Content Security Policy in report-only-modus om te voorkomen dat scripts van derden breken, en dwing die daarna af. Deze headers zijn een betekenisvolle verdedigingslaag die u bij publiceren via een builder vaak niet kunt instellen.

## Previewdeployments voor Review

Zodra uw app vanuit GitHub wordt gedeployd, kan elke pull request een eigen preview-URL krijgen. Gebruik previews om wijzigingen van ontwikkelaars of Lovable te beoordelen voordat ze staging of productie bereiken. Bescherm previews met wachtwoorden of de toegangscontrole van de host, en laat ze naar uw stagingbackend wijzen, nooit naar productie. Previews maken samenwerking zichtbaar: iedereen kan op een link klikken en precies zien wat een wijziging doet.

## Kosten van Uw Eigen Hosting

Voor de meeste oprichtersapps zijn de hostingkosten bescheiden: gratis of lage niveaus dekken weinig verkeer, met kosten op basis van gebruik voor bandbreedte en aanroepen van functies naarmate u groeit. Vergelijk abonnementen op uw verwachte verkeer, teamleden en functies zoals previews met wachtwoord. De beheerde hosting van LaunchStudio bundelt hosting met monitoring, back-ups en updates voor €49 per maand, als u het liever niet zelf beheert.

## Veelgemaakte Fouten

- De SPA-rewrite vergeten, waardoor directe links een 404 geven
- Geheime sleutels in variabelen met `VITE_` zetten
- De redirect-URL's van Supabase, OAuth en betalingen niet bijwerken voor het nieuwe domein
- De oude via Lovable gepubliceerde URL indexeerbaar laten naast het nieuwe domein
- De DNS omzetten voordat u op de preview-URL van de host heeft getest
- Het nieuwe deploymentproces niet documenteren voor medewerkers

## Een Checklist voor de Verhuisdag

- Repository gesynchroniseerd en actueel in de GitHub van uw bedrijf
- Project bij de host aangemaakt met de juiste buildinstellingen en omgevingsvariabelen
- SPA-rewrite ingesteld en directe links getest
- Site-URL en redirectlijst van Supabase bijgewerkt
- OAuth-providers en betaalwebhooks bijgewerkt
- DNS omgezet, SSL actief, oude URL doorgestuurd
- Monitoring ingesteld op het nieuwe domein
- Team geïnformeerd over het nieuwe releaseproces

## Samenvatting

Verhuizen naar uw eigen hosting kost een of twee dagen en geeft u previews, staging, terugdraaien, beveiligingsheaders en onafhankelijkheid van uw builder, terwijl Lovable de snelste manier blijft om uw interface te blijven verbeteren.

## Terugdraaien als Er Iets Misgaat

De waardevolste functie van uw eigen hosting is direct terugdraaien. Oefen het één keer: deploy een onschuldige wijziging, herstel dan via het dashboard van de host de vorige deployment en bevestig dat de site terugkeert. Draai tijdens een echt incident eerst terug en onderzoek daarna; klanten vinden een werkende app in de eerste minuten veel belangrijker dan de oorzaak.

## Werken met Lovable na de Verhuizing

Blijf na de verhuizing gewoon bewerken in Lovable. Lovable commit naar GitHub, de host deployt `main` naar staging, en u promoveert naar productie wanneer u er klaar voor bent. Gebruik de eigen publiceerknop van Lovable niet voor het productiedomein, want daarmee omzeilt u uw proces. Vertel medewerkers over de nieuwe werkwijze, zodat niemand er per ongeluk omheen publiceert.

## Gerelateerde Onderwerpen

Zie voor de pipeline achter uw nieuwe hosting onze gids over automatische deployments voor Lovable- of Bolt-apps; voor de stagingbackend onze gids over stagingomgevingen; en voor waarom onafhankelijkheid ertoe doet, wat er met uw app gebeurt als Lovable de prijzen wijzigt of stopt.

## Vragen Vóór de Verhuizing

Wie promoveert na de verhuizing wijzigingen naar productie? Welk domein is canoniek? Waar komen de geheimen te staan? Welke diensten verwijzen naar de huidige URL? Hoe draait u terug als er op de verhuisdag iets misgaat? Door deze vijf vragen vooraf te beantwoorden, wordt de verhuizing een routineklus in plaats van een gespannen avond.

## Waar U Vandaag Begint

Koppel uw Lovable-project aan GitHub als u dat nog niet heeft gedaan, importeer de repository in het gratis niveau van een host en deploy naar een preview-URL. Uw app buiten Lovable zien draaien, ook vóór het omzetten van het domein, maakt de rest van de verhuizing routinematig.

## De Opbrengst

Met uw eigen hosting worden releases een gecontroleerd, omkeerbaar proces, en is uw productiesite niet langer afhankelijk van één enkele builder.

## In het Kort

Synchroniseer met GitHub, deploy vanaf een host die u beheert, houd geheimen op de server en promoveer wijzigingen bewust.

## Wat er Verandert in Uw Werkwijze

Lovable blijft synchroniseren met GitHub. Elke commit start een deployment op uw host, bij voorkeur eerst naar staging. U promoveert bewust naar productie, zoals beschreven in onze [CI/CD-gids](https://launchstudio.eu/nl/blog/how-do-i-set-up-automatic-deployments-for-a-lovable-or-bolt-app).

## Het Laten Regelen

Een Lovable-app verhuizen naar onafhankelijke hosting kost meestal een tot drie dagen binnen een Launch Ready-pakket, of zit erbij wanneer u kiest voor de beheerde hosting van LaunchStudio. LaunchStudio wordt ondersteund door Manifera, dat voor klanten deployt op Vercel, Netlify, AWS, Azure en DigitalOcean, gecoördineerd vanuit Amsterdam en Singapore met engineering in Ho Chi Minh-stad; zie [de technologieën van Manifera](https://www.manifera.com/about-us/manifera-technologies/). De [gids van Vercel voor het deployen van Vite](https://vercel.com/docs/frameworks/frontend/vite) toont de kant van de host.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Bloemist die op Valentijnsdag Wilde Terugdraaien

Saskia Hoogland runt een bloemenwinkel in Delft en bouwde Bloemenbus in Lovable: klanten bestellen boeketten voor bezorging op dezelfde dag in de stad en kiezen een bezorgvenster. Ze publiceerde via Lovable met haar eigen domein. Op de ochtend van Valentijnsdag publiceerde ze een kleine wijziging in de keuze voor het bezorgvenster. Die brak de checkout op iPhones.

Er was geen vorige versie waarnaar ze met één klik kon terugdraaien, en het oplossen via prompts kostte twee uur op de drukste dag van haar jaar. Ze had ook geen previewomgeving om de wijziging eerst te testen.

LaunchStudio verhuisde de app naar Vercel vanuit haar GitHub-repository, richtte staging- en productiebranches in met previewdeployments voor elke wijziging, stelde rewrites en omgevingsvariabelen in, werkte de URL's in Supabase en Mollie bij, en zette het domein zonder uitval om. Saskia bleef bewerken in Lovable.

**Resultaat:** Op Moederdag, de volgende grote piek, bracht een previewdeployment een probleem met de opmaak aan het licht voordat het live ging. Terugdraaien was met één klik mogelijk geweest, al had ze het niet nodig.

> *"Op de drukste ochtend van mijn jaar kon ik één kleine wijziging niet ongedaan maken. Dat was de laatste keer dat ik direct naar klanten publiceerde."*
> - **Saskia Hoogland, Oprichter, Bloemenbus (Delft)**

**Kosten & Doorlooptijd:** €1.100 (Launch Ready-pakket: inrichting van Vercel, branches en previews, rewrites, variabelen, bijgewerkte URL's en overstap van het domein) - afgerond in 3 werkdagen.

## Veelgestelde Vragen

### Kan ik een Lovable-app hosten op Vercel of Netlify?

Ja. Lovable genereert een standaard React-app, meestal gebouwd met Vite. Koppel de GitHub-repository aan de host, stel de buildinstellingen en omgevingsvariabelen in en voeg een rewrite toe zodat alle routes de app serveren.

### Heeft een verhuizing van hosting invloed op mijn Supabase-backend?

Nee, de backend blijft waar hij is. U hoeft alleen het nieuwe domein toe te voegen aan de toegestane redirect-URL's van Supabase en aan instellingen voor OAuth of betalingen die naar de URL van uw site verwijzen.

### Kan ik Lovable nog gebruiken nadat ik naar mijn eigen hosting ben verhuisd?

Ja. Lovable blijft synchroniseren met GitHub; uw host deployt vanuit GitHub. U stopt alleen met direct naar klanten publiceren vanuit de builder.

### Waarom raadt Manifera onafhankelijke hosting aan voor groeiende apps?

Omdat controle over deployments, previews en terugdraaien van releases routinewerk maakt. De 11+ jaar ervaring van Manifera met het beheren van systemen voor klanten laat zien dat alleen al de mogelijkheid om terug te draaien veel lange storingen voorkomt.

### Heeft een andere host invloed op SEO?

Niet als uw domein en URL's hetzelfde blijven en de overstap geen lange uitval veroorzaakt. Stuur oude gepubliceerde URL's door naar uw hoofddomein, zodat zoekmachines en AI-assistenten één canonieke site zien.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan ik een Lovable-app hosten op Vercel of Netlify?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Koppel de repository, stel buildinstellingen en variabelen in en voeg een SPA-rewrite toe." }
    },
    {
      "@type": "Question",
      "name": "Heeft een verhuizing van hosting invloed op mijn Supabase-backend?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee; voeg het nieuwe domein toe aan de redirect-URL's van Supabase en de bijbehorende instellingen bij providers." }
    },
    {
      "@type": "Question",
      "name": "Kan ik Lovable nog gebruiken nadat ik naar mijn eigen hosting ben verhuisd?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Lovable synchroniseert met GitHub en de host deployt van daaruit." }
    },
    {
      "@type": "Question",
      "name": "Waarom raadt Manifera onafhankelijke hosting aan voor groeiende apps?",
      "acceptedAnswer": { "@type": "Answer", "text": "Controle over deployments, previews en terugdraaien voorkomt lange storingen." }
    },
    {
      "@type": "Question",
      "name": "Heeft een andere host invloed op SEO?",
      "acceptedAnswer": { "@type": "Answer", "text": "Niet met hetzelfde domein, dezelfde URL's en minimale uitval; stuur oude gepubliceerde URL's door." }
    }
  ]
}
</script>
