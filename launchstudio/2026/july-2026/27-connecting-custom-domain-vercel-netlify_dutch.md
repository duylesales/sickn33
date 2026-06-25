---
Titel: Een aangepast domein verbinden met uw Vercel- of Netlify-app
Trefwoorden: Verbinden, Maatwerk, Domein, Vercel, Netlify
Koperfase: Bewustzijn
---

# Een aangepast domein verbinden met uw Vercel- of Netlify-app

Het verplaatsen van uw door AI gebouwde app van een voorbeeld-URL (zoals `mijn-project.vercel.app`) naar uw eigen aangepaste domein (`myapp.com`) is het moment waarop uw prototype een echt product wordt. Hoewel het proces gepaard gaat met het intimideren van acroniemen als DNS, A Records en CNAMEs, duurt het in werkelijkheid minder dan 10 minuten. Hier vindt u de niet-technische handleiding voor het veilig verbinden van uw aangepaste domein.

## Stap 1: Koop uw domein

Koop uw domein bij een gerenommeerde registrar als u dat nog niet heeft gedaan. Namecheap, Google Domains (nu Squarespace) en Cloudflare zijn populaire keuzes. U hoeft geen webhosting- of SSL-certificaten te kopen bij de registrar; Vercel of Netlify regelen dat gratis. Je hebt alleen de domeinnaam zelf nodig.

## Stap 2: Voeg het domein toe aan uw hostingplatform

Log in op uw Vercel- of Netlify-dashboard, selecteer uw project en navigeer naar de **Domeinen**-instellingen (Instellingen > Domeinen in Vercel; Domeinbeheer in Netlify).

Typ uw aangepaste domein (bijvoorbeeld `myapp.com`) en klik op Toevoegen. Het platform vraagt ​​u dan of u ook het subdomein `www.` (bijvoorbeeld `www.myapp.com`) wilt toevoegen. Zeg ja. Het platform zal automatisch een omleiding instellen, zodat als een gebruiker een van beide versies typt, hij op dezelfde site terechtkomt.

## Stap 3: DNS-records configureren

Het hostingplatform toont u nu een foutmelding die aangeeft dat het domein 'Niet geverifieerd' of 'Ongeldige configuratie' is. Onder die fout krijgt u specifieke DNS-records. U moet deze records kopiëren en in uw domeinregistreerder plakken.

Normaal gesproken krijgt u twee records om te maken:

    - **Het A-record (voor het hoofddomein)**

            - Typ: 'A'

            - Naam/Host: `@` (of leeg laten, afhankelijk van de registrar)

            - Waarde/doel: een IP-adres dat door het platform wordt verstrekt (bijvoorbeeld `76.76.21.21` voor Vercel)
    - **Het CNAME-record (voor het www-subdomein)**

            - Typ: `CNAME`

            - Naam/host: `www`

            - Waarde/doel: een URL die door het platform wordt verstrekt (bijvoorbeeld `cname.vercel-dns.com`)

## Stap 4: Update uw registrar

Log in op de website waar u het domein heeft gekocht (Namecheap, GoDaddy, etc.) en ga naar de pagina **DNS-instellingen** of **Geavanceerde DNS**.

Zoek naar bestaande A-records of CNAME-records die mogelijk conflicteren. Verwijder alle standaard A-records die verwijzen naar de parkeerpagina van de registrar. Voeg vervolgens de twee nieuwe records toe, precies zoals Vercel/Netlify ze heeft verstrekt.

## Stap 5: Wacht op propagatie en SSL

Zodra u de records in uw registrar heeft opgeslagen, keert u terug naar uw Vercel- of Netlify-dashboard. U moet wachten op "DNS Propagation": het proces waarbij het wereldwijde internettelefoonboek wordt bijgewerkt met uw nieuwe adres.

Dit duurt meestal 5 tot 15 minuten, maar kan af en toe ook een paar uur duren. Zodra het platform de juiste DNS-records heeft gedetecteerd, verdwijnt de foutmelding en verandert de status in 'Geldige configuratie'.

Op dit moment zal het platform automatisch een gratis SSL-certificaat genereren en toepassen. Wanneer u `myapp.com` bezoekt, ziet u het beveiligde slotpictogram in de browser. Uw site is live.

## Belangrijkste inzichten

- U hoeft de domeinnaam alleen bij een registrar te kopen; Vercel/Netlify biedt de hosting en SSL gratis aan.

- U moet DNS-records configureren om het domein met de host te verbinden.

- De A Record verbindt het rootdomein (myapp.com) via een IP-adres.

- Het CNAME Record verbindt het subdomein (www.myapp.com) via een URL.

- SSL-certificaten worden automatisch gegenereerd door het hostingplatform zodra de DNS-records zijn geverifieerd.

## Domeininstellingen Zijn u in de war?

LaunchStudio zorgt voor de DNS-configuratie, SSL-installatie en de beveiliging van omgevingsvariabelen om uw app veilig live te krijgen.

LaunchStudio wordt beheerd door **Manifera**, een internationaal software-engineeringbedrijf onder leiding van oprichter en directeur **Herre Roelevink**. Manifera combineert 'Nederlands management met Vietnamees meesterschap' en heeft het hoofdkantoor in **Amsterdam, Nederland** (Herengracht 420) en ontwikkelingscentra in **Singapore** en **Ho Chi Minh City, Vietnam**. Via LaunchStudio implementeren onze senior engineeringteams uw door AI gebouwde frontend en implementeren ze productieklare beveiligingscontroles, live betalingsgateways, veilige hosting en monitoring, waardoor uw prototype binnen 1 tot 3 weken wordt getransformeerd in een veilige en compatibele MVP. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: Venture Deal Flow Portal

Alexander, de oprichter van een startup, gebruikte **Bolt** om een prototype van een venture deal flow portal te bouwen. Hoewel de applicatie functioneel was, kreeg hij te maken met ongeldige SSL-certificaatfouten en DNS-routeringslussen op zijn aangepaste opstartdomeinnaam.

Alexander werkte samen met **LaunchStudio (door Manifera)** om het product lanceringsklaar te maken. Het technische team heeft de DNS-instellingen van Cloudflare opnieuw geconfigureerd, de juiste SSL/TLS-codering ingesteld en canonieke omleidingsregels geconfigureerd.

**Resultaat:** Alexander heeft de portal beveiligd met HTTPS, waardoor browserbeveiligingswaarschuwingen voor bezoekers zijn opgelost.

**Kosten en tijdlijn:** € 800 (domeinconfiguratiepakket) — productieklaar en binnen 2 werkdagen geïmplementeerd.

---
## Veelgestelde vragen

### Wat is een DNS-record?

DNS is het telefoonboek van internet. Een DNS-record vertelt browsers met welke server contact moet worden opgenomen wanneer iemand uw domeinnaam typt.

### Wat is het verschil tussen een A-record en een CNAME?

Een A-record wijst een domein rechtstreeks toe aan een IP-adres (meestal voor het hoofddomein). Een CNAME wijst een domein toe aan een andere domeinnaam (meestal voor subdomeinen zoals 'www').

### Hoe krijg ik een SSL-certificaat?

U hoeft er geen te kopen. Vercel en Netlify voorzien en installeren automatisch een gratis Let's Encrypt SSL-certificaat zodra uw DNS correct is geconfigureerd.

### Moet ik 'www.myapp.com' of alleen 'myapp.com' gebruiken?

Moderne webstandaarden geven de voorkeur aan het schone rootdomein. Voeg beide toe aan uw host, stel de root in als primair en de host zal 'www'-verkeer automatisch omleiden naar de root.