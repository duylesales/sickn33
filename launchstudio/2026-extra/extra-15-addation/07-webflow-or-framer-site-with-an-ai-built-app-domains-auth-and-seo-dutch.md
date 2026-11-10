---
Titel: "Webflow- of Framer-site met een door AI gebouwde app: Domeinen, authenticatie en SEO"
Trefwoorden: webflow en lovable app, framer site met saas app, marketing site en app subdomein, app.domein setup, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Webflow- of Framer-site met een door AI gebouwde app: Domeinen, authenticatie en SEO

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Webflow- of Framer-site met een door AI gebouwde app: Domeinen, authenticatie en SEO",
  "description": "Veel oprichters beheren een marketingsite op Webflow of Framer en een product gebouwd met Lovable, Bolt of Cursor. Deze handleiding legt uit hoe u ze naadloos koppelt: subdomein versus submap, DNS, authenticatieredirects, cookies, analytics en toestemming, SEO, designconsistentie en de launch-checklist van LaunchStudio.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-04-24",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/webflow-or-framer-site-with-an-ai-built-app-domains-auth-and-seo" },
  "citation": [
    { "@type": "CreativeWork", "name": "Webflow Help: Connect a custom domain", "url": "https://help.webflow.com/hc/en-us/articles/33961239448467-Connect-a-custom-domain" },
    { "@type": "CreativeWork", "name": "Framer: Custom domains", "url": "https://www.framer.com/help/articles/how-to-connect-a-custom-domain/" },
    { "@type": "CreativeWork", "name": "Google Search Central: Robots meta tag", "url": "https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag" },
    { "@type": "CreativeWork", "name": "MDN: Using HTTP cookies", "url": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies" }
  ]
}
</script>

Er is een duidelijke standaard ontstaan onder oprichters die met behulp van AI bouwen: de marketingsite draait in Webflow of Framer, waar ontwerpen, bewerken en publiceren uiterst eenvoudig zijn, terwijl het eigenlijke product draait in een applicatie gegenereerd met Lovable, Bolt, v0 of Cursor. Die splitsing is volkomen logisch. Marketingpagina's veranderen wekelijks en hebben baat bij visuele paginabouwers; de applicatie vereist een stabiele backend en hoort niet aangeraakt te worden telkens wanneer een tussenkop wordt herschreven.

Het pijnpunt zit in de naad ertussen. Bezoekers klikken op de marketingsite op "Aanmelden" en belanden op een inlogpagina met een ander lettertype, een vreemde URL en soms zelfs een beveiligingswaarschuwing. Analytics toont dat de bezoeker de site verlaat om nooit meer terug te keren. Google indexeert de lege inlogpagina van de applicatie in plaats van de prijzenpagina. E-mails voor wachtwoordherstel verwijzen naar een verlopen preview-URL.

Geen van deze problemen is technisch onoverkomelijk. Ze worden simpelweg snel over het hoofd gezien omdat ze zich precies in het niemandsland tussen twee platforms bevinden. Deze handleiding legt uit hoe u een Webflow- of Framer-site vakkundig koppelt aan een door AI gebouwde applicatie.

## Belangrijkste Punten

- **Gebruik een subdomein voor de applicatie** (`app.uwdomein.nl`) en behoud het hoofddomein voor marketing. Dit is voor vrijwel alle oprichters de eenvoudigste en meest betrouwbare opzet.
- **Configureer authenticatie voor het definitieve domein:** toegestane redirect-URL's, e-maillinks en OAuth-instellingen moeten rechtstreeks naar het app-subdomein verwijzen, niet naar een tijdelijke preview-URL.
- **Houd de applicatie buiten de zoekresultaten** wanneer deze geen openbare content bevat, en zorg dat de marketingpagina's de volledige SEO-waarde dragen.
- **Volg het gebruikerstraject over beide omgevingen** met één uniforme analytics-inrichting en een cookiebanner die de AVG / GDPR op beide niveaus respecteert.
- **Zorg voor designconsistentie** zodat de overgang van marketingsite naar product voelt als één samenhangend bedrijf in plaats van twee losse werelden.

## Subdomein of Submap?

De eerste strategische beslissing is de locatie van de applicatie. Er zijn twee opties.

| Optie | Voorbeeld | Hoe het werkt | Meest geschikt voor |
| --- | --- | --- | --- |
| Subdomein | `app.uwdomein.nl` | DNS-record wijst het subdomein direct naar de app-host | Vrijwel elke oprichter |
| Submap | `uwdomein.nl/app` | Een reverse proxy routeert specifieke paden naar verschillende servers | Specifieke SEO-strategieën, grotere enterprise-teams |

**Subdomeinen zijn aanzienlijk eenvoudiger.** Webflow of Framer host `uwdomein.nl` en `www`, terwijl uw app-host, zoals Vercel, Netlify of Lovable hosting, `app.uwdomein.nl` afhandelt. Elk platform beheert zelfstandig zijn eigen SSL-certificaat. Er is geen complexe proxy vereist en beide platforms kunnen onafhankelijk van elkaar worden gedeployd.

**Submappen introduceren flinke complexiteit.** Om de applicatie te serveren op `/app` is een reverse proxy nodig, bijvoorbeeld via Cloudflare of een eigen server, die bepaalde paden naar de marketinghost stuurt en andere naar de app-host. Die proxy moet caching, response-headers en certificaten foutloos afhandelen. Sommige oprichters kiezen hiervoor omdat ze hopen dat openbare content of documentatie direct meelift op de zoekautoriteit van het hoofddomein, maar voor een besloten applicatie achter een login levert dit nauwelijks voordeel op.

Ons advies voor de meeste oprichters: marketing op het hoofddomein, de applicatie op `app.`, en documentatie of een kennisbank eventueel op `help.` of `docs.`.

## DNS-inrichting Zonder Verstoringen

DNS-wijzigingen vormen vaak het punt waar een lancering misgaat, meestal doordat records in alle haast worden aangepast. Een standaard opzet ziet er als volgt uit:

| Record | Naam | Wijst naar | Doel |
| --- | --- | --- | --- |
| A of CNAME | `@` en `www` | Webflow of Framer, conform hun instructies | Marketingsite |
| CNAME | `app` | Uw app-host (bijv. Vercel) | Productomgeving |
| MX | `@` | Uw zakelijke e-mailprovider (bijv. Google Workspace) | Bedrijfse-mail |
| TXT | `@` | SPF-record | Autorisatie van e-mailverzenders |
| TXT of CNAME | Provider-specifiek | DKIM-sleutels | Cryptografische ondertekening van e-mail |
| TXT | `_dmarc` | DMARC-beleid | Bescherming tegen spoofing en phishing |

Twee praktische vuistregels voorkomen problemen. Ten eerste: **verwijder nooit MX- of e-mail-TXT-records tijdens het aanpassen van websiterecords**; oprichters leggen hiermee geregeld per ongeluk hun eigen zakelijke mailverkeer plat. Ten tweede: **voeg het app-record toe ruim voor de officiële aankondiging**, wacht tot het SSL-certificaat actief is en test het subdomein over HTTPS op zowel mobiele 4G/5G-netwerken als kantoor-wifi. Webflow en Framer documenteren hun vereiste records tot in detail; volg die exact op in plaats van instellingen over te nemen uit verouderde handleidingen.

## Authenticatie op het Echte Domein

Door AI gegenereerde apps beginnen hun bestaan vrijwel altijd op een preview-URL, en de authenticatie-instellingen zijn daarop afgestemd. Vóór de lancering moet elke configuratie die het app-adres kent, worden bijgewerkt.

**Toegestane redirect-URL's.** Supabase Auth, Firebase Authentication, Clerk en vergelijkbare diensten sturen gebruikers na inloggen uitsluitend door naar URL's op een goedgekeurde whitelist. Voeg `https://app.uwdomein.nl` toe en verwijder verouderde preview-URL's. Een ontbrekende vermelding leidt tot oneindige inloglussen; een achtergebleven wildcard kan ernstig worden misbruikt.

**Site-URL voor e-mailnotificaties.** Bevestigingsmails, magic links en resets voor wachtwoorden maken gebruik van een geconfigureerde basis-URL. Als deze nog naar de preview-omgeving wijst, stuurt elke service-mail uw gebruikers naar een doodlopend spoor.

**OAuth-providers (Social Login).** Google, Microsoft, GitHub en Apple hanteren strikte lijsten met geautoriseerde JavaScript-origins en redirect-URI's. Werk deze bij, en pas direct de applicatienaam en het logo aan op het toestemmingsscherm, zodat gebruikers direct vertrouwen hebben in wat ze zien.

**Knoppen vanaf de marketingsite.** Knoppen zoals "Inloggen" en "Start gratis proefperiode" in Webflow of Framer moeten exact verwijzen naar de juiste app-routes, zoals `https://app.uwdomein.nl/login` en `https://app.uwdomein.nl/signup`. Indien u abonnement- of campagne-ID's meestuurt via URL-parameters, moet de applicatie deze netjes uitlezen.

## Cookies en Sessiebeheer Tussen Subdomeinen

Standaard wordt een cookie ingesteld door `app.uwdomein.nl` uitsluitend teruggestuurd naar dat specifieke subdomein. Voor authenticatie is dat precies wat u wenst: de marketingsite heeft geen toegang nodig tot de actieve gebruikerssessie, en die scheiding verkleint het risico aanzienlijk als een marketingscript ooit gecompromitteerd raakt.

Sommige oprichters willen dat de marketingsite weet of een bezoeker al is ingelogd, om bijvoorbeeld "Naar dashboard" te tonen in plaats van "Aanmelden". De veilige methode hiervoor is een apart, niet-gevoelig cookie met bereik op het hoofddomein, zoals `logged_in=true`. Dit cookie wordt gezet door de app en door de marketingsite uitsluitend gebruikt om knopteksten dynamisch aan te passen. Deel nooit het daadwerkelijke JWT- of sessietoken met het marketingdomein. De officiële documentatie van MDN over HTTP-cookies legt de werking van de attributen `Domain`, `Secure`, `HttpOnly` en `SameSite` uitstekend uit.

## SEO: Laat de Marketingsite het Zware Werk Doen

Zoekmachines horen uw marketingpagina's, blogartikelen en documentatie te indexeren, niet uw inlogschermen of afgeschermde dashboards.

- **Markeer app-routes met `noindex`** wanneer ze geen openbare meerwaarde bieden, via de robots-metatag zoals beschreven in Google Search Central. Inlog-, registratie-, dashboard- en instellingenpagina's horen zelden thuis in zoekmachineresultaten.
- **Blokkeer de app niet volledig in `robots.txt` als er wel openbare profielen zijn**, zoals gedeelde openbare rapportages of directory-pagina's die u wél wilt laten indexeren. Render die specifieke pagina's server-side zodat crawlers volledige HTML ontvangen.
- **Stel canonieke URL's (canonical tags) in op de marketingsite** zodat `www` en non-`www` versies elkaar niet beconcurreren, en dwing één primaire variant af via redirects.
- **Behoud gestructureerde data op de marketingsite**: schema-markup voor organisaties, softwareapplicaties, FAQ's en artikelen helpt zowel Google als AI-antwoordmachines (GEO) te begrijpen wat uw dienst inhoudt.
- **Dien de sitemap van de marketingsite in** via Google Search Console, en voeg het app-subdomein toe als een afzonderlijke property om eventuele indexatieproblemen tijdig te signaleren.

Veel door AI gebouwde applicaties zijn Single Page Applications (SPA's) die pas in de browser content renderen. Achter een login is dat uitstekend, maar voor publieke pagina's die afhankelijk zijn van client-side rendering levert dat indexeringsrisico's op. Onze handleiding over [of Google een Lovable-app kan indexeren](https://launchstudio.eu/nl/blog/can-google-index-my-lovable-app) behandelt de technische opties.

## Analytics en Toestemming Over Beide Omgevingen

Om uw conversietrechter betrouwbaar te meten, moet u het volledige traject kunnen volgen: van het eerste bezoek op de marketingsite tot en met de accountaanmaak en de eerste actie in de applicatie.

- **Eén overkoepelende analytics-property** voor beide domeinen, waarbij het app-subdomein is opgenomen in de cross-domain- of same-site-configuratie van uw analysetool.
- **Campagneparameters (UTM-tags) behouden** wanneer bezoekers van de marketingsite doorklikken naar het registratieformulier, zodat u exact weet welke advertenties of LinkedIn-berichten betalende klanten opleveren.
- **Een registratie-event in de app** en bij voorkeur een activatie-event zodra een nieuwe gebruiker zijn eerste waardevolle handeling succesvol afrondt.
- **Een uniforme cookiebanner op beide sites** die niet-essentiële tracking pas laadt na expliciete toestemming, volledig conform de AVG / GDPR en de Telecommunicatiewet. De toestemmingskeuze hoort bewaard te worden over subdomeinen heen, zodat een bezoeker niet twee keer dezelfde vraag krijgt.

Indien u de juridische complexiteit van cookiebanners wilt vermijden voor standaard bezoekersstatistieken, zijn privacyvriendelijke cookieless tools een bewezen alternatief; ons artikel over [cookieless analytics voor Europese SaaS-bedrijven](https://launchstudio.eu/nl/blog/cookieless-analytics-for-eu-saas-plausible-vs-ga4) vergelijkt de mogelijkheden.

## Designconsistentie

Zodra een bezoeker van een strakke Webflow-landingspagina overstapt naar een applicatie met andere typografie, afwijkende merkkleuren en vreemde knopstijlen, daalt het vertrouwen merkbaar. Beide werelden op één lijn houden is vooral een kwestie van discipline:

- **Gedeelde design tokens.** Leg kleuren, lettertypefamilies, corpsgroottes, border-radii en marges één keer vast en pas ze in beide systemen toe. Veel AI-bouwers kunnen via een gerichte prompt of Tailwind-configuratie direct dezelfde stijlen overnemen.
- **Hetzelfde logo, favicon en paginatitelformaat.**
- **Consistente terminologie in de navigatie.** Als de marketingsite spreekt over "Werkruimtes", moet de applicatie niet plotseling "Projecten" tonen.
- **Identieke juridische links.** Uw privacyverklaring en algemene voorwaarden moeten vanuit beide omgevingen bereikbaar zijn en naar exact dezelfde pagina's verwijzen.

## De Launch-Checklist

| Onderdeel | Controle |
| --- | --- |
| DNS | Marketingsite op hoofddomein en `www`, app op `app.`, e-mailrecords intact, HTTPS gevalideerd op beide |
| Authenticatie | Redirect-URL's, site-URL, OAuth-origins en e-mailsjablonen ingesteld op het app-subdomein |
| Links | Marketingknoppen linken naar de juiste app-routes, URL-parameters worden correct doorgegeven |
| Cookies | Sessiecookies strikt beperkt tot het app-subdomein, optionele statusvlag op het hoofddomein |
| SEO | App-routes voorzien van `noindex` waar passend, marketing-sitemap ingediend, canoniek domein vastgelegd |
| Analytics | Eén geïntegreerde property, registratie- en activatie-events actief, campagnegegevens bewaard |
| Toestemming | Cookiebanner actief op beide sites, toestemmingsstatus gedeeld over subdomeinen |
| Design | Gedeelde tokens, identiek logo, passend favicon en consistente terminologie |
| E-mail | Afzenderdomein volledig geauthenticeerd via SPF, DKIM en DMARC |

## Wat Het Kost

Het koppelen van een marketingsite aan een door AI gebouwde applicatie vormt doorgaans onderdeel van een bredere productielancering. LaunchStudio's **Launch Ready**-pakket (€800 - €3.500) omvat deployment naar uw eigen domein, volledige authenticatieconfiguratie, beveiligingsreparaties en 48 uur intensieve launch-begeleiding. **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) breidt dit uit met betalingskoppelingen, beheerde hosting, geautomatiseerde back-ups, transactionele e-mail met geauthenticeerde verzending en prioriteitsondersteuning. U ontvangt een vaste prijsopgave na een kort intakegesprek van 15 minuten. De [prijscalculator](https://launchstudio.eu/nl/#calculator) geeft u direct een eerste indicatie.

## Het Team Achter LaunchStudio

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, meer dan 160 opgeleverde projecten en een team van ruim 120 senior engineers. Oprichters ontmoeten ons team aan de Herengracht 420 in Amsterdam; onze engineers werken vanuit Manifera's ontwikkelingscentrum aan Pho Quang Street in Ho Chi Minh City, met een regionale hub aan Tras Street in Singapore. Manifera integreert al jarenlang complexe bedrijfswebsites en klantportalen voor enterprise-opdrachtgevers, en precies diezelfde technische nauwkeurigheid passen we toe op de koppeling tussen uw Webflow-site en Lovable-app.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Aanmeldknop Die Naar een Preview-URL Verwees

Charlotte Verbeek, voormalig HR-adviseur in Utrecht, lanceerde Verlofwijzer: een overzichtelijke verlofplanningstool voor mkb-bedrijven. Haar Framer-marketingsite zag er uitstekend uit en behaalde hoge posities in Google op relevante Nederlandse HR-zoektermen. Het product zelf was gebouwd in Lovable en draaide op een tijdelijke preview-URL, direct gekoppeld aan de knop "Probeer gratis" op haar Framer-site.

Haar analytics toonde een verontrustend patroon: maandelijks klikten honderden geïnteresseerden op de aanmeldknop, maar er werden slechts enkele tientallen accounts daadwerkelijk aangemaakt. Toen Charlotte het proces zelf testte op haar smartphone, ontdekte ze dat de verificatiemails linkten naar een oud, inactief preview-adres. Google Social Login toonde een onbekende systeemnaam met een beveiligingswaarschuwing, en haar inlogpagina stond in de zoekresultaten hoger dan haar prijzenpagina. Daarnaast stopte de analytics-meting direct bij de klik op de knop, en week de visuele stijl van de applicatie sterk af van haar Framer-site.

LaunchStudio migreerde de applicatie naar `app.verlofwijzer.nl` op Vercel met het bijbehorende DNS-record naast de bestaande Framer-records, waarbij alle zakelijke e-mailinstellingen volledig onaangetast bleven. De redirect-URL's en site-URL in Supabase Auth werden bijgewerkt, oude preview-adressen werden verwijderd en het Google OAuth-toestemmingsscherm werd voorzien van het officiële merk en logo. Alle interne app-routes kregen een `noindex`-tag, analytics werd geïntegreerd over beide domeinen met gerichte registratie- en activatie-events, en de cookietoestemming werd gedeeld over de subdomeinen. Tot slot werd de Lovable-app gestyled met de design tokens van de Framer-site.

**Resultaat:** In de eerste volle maand na de oplevering steeg het percentage aanmelders dat een bevestigd account werd van circa 11% naar 46%. De inlogpagina verdween binnen enkele weken uit de zoekmachineresultaten, en Charlotte kon via haar dashboard exact herleiden welke LinkedIn-berichten daadwerkelijk betalende klanten opleverden.

> *"Elke afzonderlijke tool werkte op zichzelf prima. Het lek zat precies in de ruimte tussen de systemen, en dat had ik zelf nooit kunnen ontdekken."*
> - **Charlotte Verbeek, Oprichter, Verlofwijzer (Utrecht)**

**Kosten & Doorlooptijd:** €1.650 (Launch Ready-pakket: domein- en DNS-configuratie, authenticatie-inrichting, SEO- en analytics-afstemming, design tokens) - afgerond in 5 werkdagen.

## Veelgestelde Vragen

### Moet mijn applicatie op een subdomein of in een submap draaien?

Voor vrijwel alle oprichters is een subdomein zoals `app.uwdomein.nl` veruit de beste keuze. Het is veel eenvoudiger in te richten, elk platform beheert automatisch zijn eigen SSL-certificaat en beide omgevingen kunnen volledig onafhankelijk van elkaar worden gedeployd. Een submap vereist een complexe reverse proxy en levert alleen bij uitzonderlijke SEO-strategieën voordeel op.

### Schaadt het de SEO van mijn marketingsite als de app op een subdomein staat?

Nee, zolang uw marketingsite alle openbare content bevat. Afgeschermde app-pagina's achter een login hebben voor zoekmachines sowieso geen waarde. Houd landingspagina's, blogs en documentatie op de marketingsite en geef besloten app-routes een `noindex`-tag mee.

### Kan mijn Webflow- of Framer-site zien of een bezoeker al is ingelogd?

Ja, op een veilige manier via een apart, niet-gevoelig cookie op het hoofddomein (zoals `logged_in=true`) dat door de applicatie wordt geplaatst. De marketingsite leest dit cookie uitsluitend uit om bijvoorbeeld een knop aan te passen van "Aanmelden" naar "Naar Dashboard". Het daadwerkelijke beveiligde sessietoken blijft uitsluitend bewaard op het app-subdomein.

### Hoe helpt Manifera's ervaring bij deze integratie?

Manifera bouwt en koppelt al meer dan 11 jaar enterprise-websites, klantenportalen en complexe identiteitssystemen. LaunchStudio past exact diezelfde degelijke engineeringpraktijken toe op DNS, authenticatie, cookie-isolatie en tracking - precies de kwetsbare koppelvlakken waar oprichters bij lanceringen anders gebruikers en conversie verliezen.

### Verbetert deze opzet de vindbaarheid in AI-zoekmachines?

Zeker. Een snelle, goed gestructureerde marketingsite met zuivere JSON-LD schema-markup, één eenduidig primair domein en geen storende afgeschermde inlogpagina's in de zoekindex stelt zoekmachines en AI-antwoordmodellen (zoals Perplexity en ChatGPT Search) in staat uw product helder te begrijpen en nauwkeurig te citeren.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet mijn applicatie op een subdomein of in een submap draaien?",
      "acceptedAnswer": { "@type": "Answer", "text": "Voor de meeste oprichters is een subdomein zoals app.uwdomein.nl de beste keuze: eenvoudiger in beheer, afzonderlijke SSL-certificaten en onafhankelijke deployments. Submappen vereisen een complexe reverse proxy." }
    },
    {
      "@type": "Question",
      "name": "Schaadt het de SEO van mijn marketingsite als de app op een subdomein staat?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee, zolang de marketingsite de openbare content draagt. Markeer besloten app-routes met noindex en houd blogs en documentatie op de marketingsite of een eigen documentatie-subdomein." }
    },
    {
      "@type": "Question",
      "name": "Kan mijn Webflow- of Framer-site zien of een bezoeker al is ingelogd?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, via een apart niet-gevoelig cookie op het hoofddomein dat door de app wordt ingesteld. Het beveiligde sessietoken blijft veilig beperkt tot het app-subdomein." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt Manifera's ervaring bij deze integratie?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera integreert al ruim 11 jaar enterprise-portalen en identiteitssystemen. LaunchStudio past die precisie toe op DNS, authenticatie en tracking." }
    },
    {
      "@type": "Question",
      "name": "Verbetert deze opzet de vindbaarheid in AI-zoekmachines?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Een heldere marketingsite met gestructureerde schema-data, één primair canoniek domein en geen conflicterende app-pagina's is optimaal citeerbaar voor AI-zoekmachines." }
    }
  ]
}
</script>
