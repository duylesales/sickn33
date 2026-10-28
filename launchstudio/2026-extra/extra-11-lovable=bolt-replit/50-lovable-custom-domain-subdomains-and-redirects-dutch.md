---
Titel: "Lovable Custom Domein: Subdomeinen, Redirects en Multi-Brand Setups"
Trefwoorden: lovable custom domein, lovable seo, subdomein versus subdirectory, redirect configuratie, staging subdomein, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Lovable Custom Domein: Subdomeinen, Redirects en Multi-Brand Setups

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Custom Domein: Subdomeinen, Redirects en Multi-Brand Setups",
  "description": "Zodra één domeinnaam werkt, volgen de strategische vragen: moet de app op een subdomein of in een subfolder, waar hoort staging, hoe richt je redirects in en wat verandert er bij meerdere merknamen? Een praktische domeinstructuur voor oprichters.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-22",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-custom-domain-subdomains-and-redirects" }
}
</script>

Het koppelen van één domeinnaam aan een Lovable-app is een opgelost vraagstuk. Wat daarna volgt is minder vanzelfsprekend en heeft aanzienlijk grotere consequenties: moet de webapplicatie draaien op `app.jouwdomein.nl` of op `jouwdomein.nl/app`? Waar plaats je de staging-omgeving? Wat gebeurt er met de oude URL wanneer een pagina verhuist? En wat verandert er wanneer een zakelijke klant vraagt of het platform onder hun eigen huisstijl en domein kan draaien?

Dit zijn structurele beslissingen. Nu zijn ze goedkoop en eenvoudig te implementeren; over zes maanden zijn ze matig irritant; en nadat je zoekmachineposities hebt opgebouwd, bladwijzers bij klanten hebt en externe integraties naar haastig gekozen adressen verwijzen, zijn ze buitengewoon kostbaar om te herzien.

## Subdomein of Pad: De Keuze Die Alles Bepaalt

Er zijn twee manieren om je architectuur in te richten, en de keuze beïnvloedt direct je SEO, cookiebeheer, SSL-certificaten en deploymentprocessen:

**De applicatie op een subdomein** - `app.jouwdomein.nl` - met de marketingpagina's op het hoofddomein (`jouwdomein.nl`). Dit is de meest gangbare en beproefde opzet voor SaaS-producten, en het biedt grote praktische voordelen: beide onderdelen kunnen afzonderlijk worden gehost, onafhankelijk van elkaar worden gedeployed, en verschillende technische stacks gebruiken zonder elkaar te hinderen. Bovendien schermt het de afgesloten webapplicatie af van pagina's die je door zoekmachines wilt laten indexeren.

**De applicatie op een pad** - `jouwdomein.nl/app` - houdt alles op één centrale hostnaam. Webstatistieken (analytics) blijven uniform, sessiecookies zijn eenvoudiger in te stellen, en alle SEO-signalen cumuleren op één enkel domein. Het nadeel is dat beide helften vanaf dezelfde serverlocatie geserveerd moeten worden of via een geavanceerde reverse proxy moeten lopen. Voor een combinatie van een Lovable-frontend met een losse marketingwebsite vergt dat aanzienlijk meer routingconfiguratie dan op het eerste gezicht lijkt.

Voor een beginnend softwareproduct is het pragmatische uitgangspunt: de applicatie op `app.`, marketing op het hoofddomein, en geen onnodige discussie. Maak deze keuze vóórdat er inkomende backlinks ontstaan. Een applicatie later tussen beide opties verhuizen betekent immers redirects, het herconfigureren van alle OAuth-callbacks, en het geforceerd uitloggen van al je actieve gebruikers.

## Wat Er Nog Meer een Eigen Subdomein Verdient

**Staging.** Een adres zoals `staging.jouwdomein.nl`, dat strikt moet worden afgeschermd van zoekmachines (via `noindex` en `robots.txt`) en idealiter achter een wachtwoordmuur leeft. Een staging-omgeving die door Google wordt geïndexeerd is een terugkerende bron van schaamte - en soms erger, omdat er geregeld kopieën van echte klantdata op draaien.

**Transactionele e-mail.** Een dedicated subdomein voor e-mailverzending (zoals `mail.jouwdomein.nl`) isoleert de verzendreputatie van je applicatie van je persoonlijke en zakelijke kantoor-mailboxen. Dit loont zelfs als je app slechts vijftig welkomstberichten per dag verstuurt.

**Documentatie of Helpdesk,** mits omvangrijk, hoewel een subpad op de marketingsite (`/docs`) even goed functioneert en je SEO-autoriteit versterkt.

**Klantbestanden en media (Assets),** waar je bestanden of afbeeldingen op schaal serveert. Dit stelt je in staat om caching-regels en CDN-configuraties afwijkend van je applicatie in te richten.

Wat beslist géén subdomein verdient: een tijdelijke marketingcampagne, een losse landingspagina of een blog. Deze horen thuis als subpaden op je hoofdsite, waar ze direct bijdragen aan de domeinautoriteit van je merk in plaats van vanaf nul te moeten beginnen.

## Redirects: Kleine Regels Die Geruisloos Verlies Voorkomen

Vier situaties dekken vrijwel de complete behoefte van een startend softwarebedrijf af:

**Apex naar www, of andersom.** Kies één canonieke vorm (`jouwdomein.nl` óf `www.jouwdomein.nl`) en stuur de andere variant permanent door met een 301-redirect. Beide werken technisch; maar beide tegelijk content laten serveren halveert je zoekwaarde en vervuilt je analytics.

**Onveilig naar veilig (HTTP naar HTTPS).** Elk inkomend HTTP-verzoek moet automatisch en direct doorverwijzen naar de beveiligde HTTPS-verbinding. Controleer dit handmatig in plaats van erop te vertrouwen dat je hostingpartij dit automatisch goed doet.

**Oude URL's naar nieuwe.** Wanneer een pagina van adres verandert, stel je direct een permanente 301-redirect in vanaf het oude pad. Dit behoudt opgebouwde zoekmachineposities en voorkomt dat externe links of bladwijzers van gebruikers stuklopen op een 404-fout.

**Het oorspronkelijke preview-adres.** Zodra je eigen domeinnaam live staat, moet de originele preview-URL van Lovable permanent doorverwijzen naar je domein, of via een `noindex`-tag worden geblokkeerd. Laat je beide online staan, dan eindigt je product met een onbeschermde, merkloze kopie van zichzelf in de zoekresultaten van Google.

Een belangrijke waarschuwing: vermijd zogeheten 'redirect chains' (het oude adres verwijst naar een tussenadres, dat weer verwijst naar de eindbestemming). Ketens van doorverwijzingen kosten SEO-waarde en vertragen de laadtijd. Verwijs altijd in één directe sprong naar de uiteindelijke URL.

## Cookies, Sessies en de Subdomeingrens

Het technische detail dat oprichters steevast verrast zodra ze een tweede subdomein inrichten:

Browsercookies zijn standaard gebonden aan één specifieke hostnaam. Een inlogsessie aangemaakt op `app.jouwdomein.nl` is daardoor niet automatisch beschikbaar op `jouwdomein.nl`. Dit betekent dat een gebruiker die inlogt in de app en vervolgens doorklikt naar de marketingwebsite, daar plotseling als niet-ingelogd wordt weergegeven. Of dat erg is hangt af van je use-case - voor veel tools maakt het niet uit - maar als je een naadloze overgang wilt, moet de cookie worden geconfigureerd met een domeinscope (`domain=.jouwdomein.nl`), zodat alle subdomeinen de sessie delen.

Het delen van cookies over subdomeinen heeft echter een duidelijke beveiligingsconsequentie: een kwetsbaarheid of een slordig script op een willekeurig subdomein krijgt daarmee direct toegang tot de actieve sessiecookies van de applicatie. Voor een klein bedrijf met een staging-subdomein dat testcode bevat, is dat een reëel risico.

Kies bewust: gedeelde sessies over alle subdomeinen, of strikt gescheiden. Beide keuzes zijn verdedigbaar; het ontdekken via een klagende klant is dat niet.

## SSL-certificaten Over Meerdere Hostnamen

Elke hostnaam die je gebruikt vereist een geldig SSL/TLS-certificaat. Moderne cloudhosting vraagt en vernieuwt deze certificaten automatisch - maar uitsluitend voor de domeinnamen die je expliciet hebt aangemeld.

Twee veelvoorkomende foutpatronen: een nieuw subdomein aangemaakt in DNS dat nooit is geconfigureerd bij de webhost, waardoor bezoekers een alarmerende beveiligingswaarschuwing in hun browser zien. En een wildcard-certificaat (`*.jouwdomein.nl`) dat weliswaar één subdomeinniveau dekt, maar niet werkt voor geneste niveaus zoals `test.app.jouwdomein.nl`.

De controle is eenvoudig: open elke hostnaam die je gebruikt in een privé-venster (incognito), op een apparaat dat de site nog nooit heeft bezocht (bijvoorbeeld via mobiele data), en controleer of het slotje groen en geldig is. Doe dit na elke wijziging in je DNS-instellingen.

## Wanneer een Klant een Eigen Merknaam Wil (White-Label)

Zodra je levert aan zakelijke enterprise-klanten volgt vroeg of laat de vraag: kan deze tool draaien op `planning.hunbedrijf.nl`?

Dit is technisch mogelijk, maar het is een productbeslissing en geen simpele instelling, omdat het structurele operationele verplichtingen met zich meebrengt. Elk custom domein van een klant vereist een eigen SSL-certificaat dat automatisch moet worden vernieuwd, DNS-records (zoals CNAME) die de klant zelf bij zijn registrar moet instellen, en eerstelijns support wanneer hun IT-afdeling per ongeluk een DNS-fout maakt. Bovendien moet jouw applicatie dynamisch herkennen welk merk hij serveert, wat doorwerkt in logins, e-mailtemplates en gegenereerde links.

Voor een beginnend product werkt de volgende tussenstap het beste: bied klanten eerst een gepersonaliseerd subdomein aan onder jouw eigen merk - `hunbedrijf.jouwdomein.nl`. Dit levert 90% van de merkbeleving op tegen een fractie van de operationele beheerlast. Bewaar echte custom domeinen voor grotere enterprise-contracten die de extra investering financieel rechtvaardigen.

## Een Domeinstructuur Die Standhoudt

Voor de meeste Nederlandse B2B SaaS-producten overleeft de volgende opzet jaren van groei zonder dat er ingrijpend verbouwd hoeft te worden:

- `jouwdomein.nl` - marketingpagina's, canoniek, waarbij `www` met een 301 doorverwijst (of omgekeerd).
- `app.jouwdomein.nl` - de eigenlijke webapplicatie.
- `staging.jouwdomein.nl` - strikt afgeschermd met een wachtwoord en uitgesloten van indexering.
- `mail.jouwdomein.nl` - uitsluitend voor transactionele e-mailverzending (SPF/DKIM).
- Alle overige content (zoals `/blog`, `/prijzen`, `/kennisbank`) als subpaden op het hoofddomein.
- Eén duidelijke canonieke vorm, permanente redirects voor verhuisde pagina's, en de oorspronkelijke Lovable-preview-URL doorgestuurd.

Leg deze structuur eenmalig vast, documenteer hem en configureer hem vóórdat er substantieel verkeer binnenkomt. Het kost een middag werk en voorkomt een hele categorie latere hoofdpijndossiers.

## Eenmalig Vakkundig Inrichten

Een solide domeinstructuur is overzichtelijk werk met een lange staart van sluipende risico's - SSL-fouten op een vergeten subdomein, een testomgeving die opduikt in Google, OAuth-callbacks die nog wijzen naar een test-URL, of sessieproblemen tussen verschillende pagina's.

LaunchStudio richt deze domeinstructuur in als vast onderdeel van het klaarmaken van AI-software voor productie: de canonieke URL-structuur afgedwongen, applicatie en marketing helder gescheiden, staging waterdicht afgeschermd van Google, een mail-subdomein geconfigureerd met DKIM en DMARC, SSL-certificaten geverifieerd over alle hostnamen, redirects zonder vertragende tussenstappen, en alle externe API-callbacks gecontroleerd - zonder de frontend aan te raken die je in Lovable hebt gebouwd.

Hierachter staat Manifera, met elf jaar ervaring in productie-infrastructuur voor partijen als Vodafone, TNO en CFLW, vanuit Amsterdam en Ho Chi Minhstad. [Beschrijf je project](https://launchstudio.eu/nl/#contact) voor een domeinstructuur die klaar is voor groei (meestal binnen één werkdag), of bekijk de [pakketten](https://launchstudio.eu/nl/#packages).

## Leg Je Eigen Domeinkaart Vast

Eén pagina documentatie, bewaard bij je overige technische specificaties, waarin elke hostnaam onder jouw beheer staat genoteerd. Het kost een kwartier en voorkomt dat historische keuzes over een jaar volstrekt onbegrijpelijk zijn geworden.

**Noteer per hostnaam:** welk systeem de pagina's serveert, waar de DNS-zone wordt beheerd, hoe het SSL-certificaat wordt vernieuwd, of de pagina geïndexeerd mag worden, en wie de configuratie heeft opgezet.

**Neem ook domeinen op die je niet actief gebruikt.** Defensief gekochte domeinnamen, oude merknamen of landingspagina's van eerdere campagnes. Dit zijn precies de domeinen die verlopen zonder dat iemand het merkt, en een verlopen domein met oude DNS-records vormt een serieus securityrisico (subdomain takeover).

**Documenteer de registrar en de verloopdatum,** inclusief de gekoppelde betaalmethode. Het per ongeluk verlopen van een domeinnaam door een verlopen creditcard is een van de meest voorkomende manieren waarop startende SaaS-bedrijven op zaterdagochtend plotseling offline gaan.

**Noteer wie toegang heeft** tot de domeinregistrar en de DNS-provider, en neem deze accounts op in je periodieke security-audit.

De reden om dit zwart-op-wit vast te leggen: DNS-instellingen worden zelden aangeraakt. Zes maanden later weet niemand meer waarom een bepaald subdomein bestaat, of er nog externe systemen van afhangen, en of het veilig verwijderd kan worden - waardoor verouderde subdomeinen vaak jarenlang onbeheerd online blijven staan.

## Vóórdat Je een Tweede Domeinnaam Koopt

Oprichters registreren regelmatig extra domeinen - een spellingsvariant, een Engelse `.com`-versie, of een kortere campagnenaam - en moeten vervolgens bepalen wat ermee moet gebeuren.

De verstandige standaard is dat een secundair domein uitsluitend via een permanente 301-redirect doorverwijst naar je hoofddomein en zelf geen losse content serveert. Daarmee bescherm je je merknaam, vang je typefouten op, en consolideer je alle zoekmachine-autoriteit op één sterk adres.

Zelfstandige content publiceren op een tweede domein betekent dat je alles dubbel moet onderhouden - twee sets webpagina's, twee SSL-certificaten, twee domeinen om te monitoren in Search Console, en twee kansen om achter te lopen met onderhoud. Voor een klein bedrijf loont dat vrijwel nooit, tenzij het om een fundamenteel ander merk gaat.

Registreer varianten bij dezelfde registrar als je hoofddomein, op dezelfde facturatiecyclus, en voeg ze direct toe aan je domeinkaart.

## Echt voorbeeld

### Een Staging-omgeving Die Beter Rankte Dan het Product Zelf

Wouter Claassen runde Zaalplanner, een reserveringsplatform gebouwd in Lovable voor buurthuizen en sporthallen rond Tilburg. Zowel de marketingpagina's als de applicatie stonden op het hoofddomein, en maanden eerder was er een staging-omgeving opgezet op een testadres waar sindsdien niemand meer naar had omgekeken.

Twee problemen kwamen in dezelfde week aan het licht. Een potentiële klant die op Google zocht naar de software kwam als eerste uit op de staging-omgeving - inclusief tientallen testreserveringen met realistisch ogende privégegevens - simpelweg omdat niets zoekmachines tegenhield om de testomgeving te indexeren. Tegelijkertijd meldde een sporthalbeheerder dat inloggen in de app haar automatisch uitlogde uit de publieke reserveringskalender; een sessieconflict dat was ontstaan toen een deel van het platform naar een subdomein was verhuisd zonder de domeinscope van de cookies aan te passen.

Drie werkdagen werk: de staging-omgeving werd achter een HTTP-basisauthenticatie geplaatst en voorzien van `noindex`-tags, waarna de geïndexeerde testpagina's via Google Search Console met spoed werden verwijderd; de webapplicatie werd doelbewust verplaatst naar `app.jouwdomein.nl`, waarbij cookies werden geconfigureerd op het overkoepelende hoofddomein zodat beide helften dezelfde login deelden; de canonieke URL-vorm werd geforceerd met 301-redirects; SSL-certificaten werden op alle vier de hostnamen handmatig geverifieerd via mobiele data; de originele Lovable-preview-URL werd doorgestuurd; en er werd een apart mail-subdomein ingericht met geldige SPF- en DKIM-records, wat direct de afleverbaarheid van transactionele e-mails verbeterde.

**Resultaat:** de testomgeving verdween binnen drie weken volledig uit de zoekresultaten, het inlogprobleem was opgelost, en Wouter beschikt nu over een helder gedocumenteerde domeinstructuur die hij twee maanden later moeiteloos kon toepassen bij het toevoegen van een documentatiesite.

> *"Een lead vond mijn testomgeving eerder dan mijn echte product, en die stond vol met neppe boekingen met echte namen. Dat was een behoorlijk memorabele ochtend."*
> - **Wouter Claassen, Oprichter, Zaalplanner (Tilburg)**

**Kosten & Doorlooptijd:** € 1.600 (domeinstructuur, staging-beveiliging, cookie-scoping, SSL-certificaten, redirects en e-mailsubdomein) - afgerond in 3 werkdagen.

## Veelgestelde vragen

### Moet mijn app op een subdomein of in een subdirectory staan?

Voor de meeste kleine SaaS-producten is de applicatie op `app.` met marketing op het hoofddomein het pragmatische uitgangspunt: beide kunnen onafhankelijk van elkaar gehost en gedeployed worden. Een subdirectory (`/app`) houdt cookies en analytics uniformer, maar vergt complexere routering. Beslis dit vóórdat je inkomende links verzamelt.

### Waar hoort mijn staging-omgeving te draaien?

Op een eigen subdomein (zoals `staging.`), altijd beschermd met een wachtwoord en strikt uitgesloten van zoekmachine-indexering (`noindex`). Geïndexeerde testomgevingen zijn een veelvoorkomende bron van schaamte en bevatten geregeld kopieën van gevoelige data.

### Werken gebruikerssessies automatisch over verschillende subdomeinen?

Standaard niet - een sessie op `app.jouwdomein.nl` is niet automatisch geldig op het hoofddomein. Cookies kunnen worden geconfigureerd op het hoofddomein (`.jouwdomein.nl`) om de login te delen, wat inhoudt dat elk subdomein toegang heeft tot die sessie. Maak hierin een bewuste afweging.

### Kan ik zakelijke klanten hun eigen domeinnaam laten gebruiken?

Technisch gezien wel, maar het brengt doorlopende operationele verplichtingen met zich mee: SSL-certificaten per klantdomein, DNS-records die zij moeten beheren, en support bij configuratiefouten. Klanten een eigen subdomein onder jouw merk aanbieden levert vrijwel hetzelfde voordeel op tegen veel lagere beheerkosten.

### Wat moet er gebeuren met mijn oude preview-URL?

Stuur deze met een permanente 301-redirect door naar je echte domeinnaam, of blokkeer indexering als doorsturen niet mogelijk is. Laat je beide adressen online staan, dan concurreert een merkloze kopie van je applicatie direct met je eigen website in Google.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet mijn app op een subdomein of in een subdirectory staan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor de meeste kleine apps is de app op app. en marketing op het hoofddomein het beste, omdat beide los gehost en gedeployed kunnen worden. Beslis dit vóórdat je links verzamelt."
      }
    },
    {
      "@type": "Question",
      "name": "Waar hoort mijn staging-omgeving te draaien?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Op een eigen subdomein, met een wachtwoord beveiligd en uitgesloten van indexering, omdat testomgevingen vaak testdata of kopieën van echte gegevens bevatten."
      }
    },
    {
      "@type": "Question",
      "name": "Werken gebruikerssessies automatisch over verschillende subdomeinen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Standaard niet. Cookies kunnen op het hoofddomein worden gescoped om logins te delen, maar elk subdomein heeft dan toegang tot die sessie; kies bewust."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik zakelijke klanten hun eigen domeinnaam laten gebruiken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, maar met doorlopende lasten voor certificaten, klantspecifieke DNS en support. Een subdomein per klant onder je eigen merk is veel voordeliger."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet er gebeuren met mijn oude preview-URL?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Stuur deze met een 301-redirect door naar je domein of blokkeer indexering, zodat een merkloze versie niet concurreert in zoekmachines."
      }
    }
  ]
}
</script>
