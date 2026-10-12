---
Titel: "AI-app-beveiliging begint bij waar je geheimen bewaart"
Trefwoorden: ai app beveiliging, omgevingsvariabelen frontend blootstelling, api sleutel rotatie, git geschiedenis geheimen, Cursor, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische solo-oprichter / Indie hacker
---

# AI-app-beveiliging begint bij waar je geheimen bewaart

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-app-beveiliging begint bij waar je geheimen bewaart",
  "description": "Een praktische handleiding voor het omgaan met inloggegevens in met AI gegenereerde apps: welke sleutels echt geheim zijn, waarom build tools sommige variabelen opzettelijk publiceren, hoe git-historie kopieën bewaart, en een audit van tien minuten.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/where-secrets-belong-in-an-ai-built-app" }
}
</script>

Een software-oprichter in Tilburg ontdekte dat zijn leverancier van kaartdiensten hem binnen elf dagen facturen stuurde voor 1,4 miljoen API-verzoeken. Hij had op dat moment ongeveer 200 actieve gebruikers. De API-sleutel die deze verzoeken autoriseerde, stond sinds de lancering open en bloot in de gepubliceerde JavaScript-bundel van zijn website. Iemand — of waarschijnlijker: een geautomatiseerd script — had de sleutel gevonden en zijn account gebruikt als gratis infrastructuur voor eigen projecten.

Er was niets gehackt. Er was geen enkel systeem binnengedrongen. De oprichter had simpelweg een geheime sleutel gepubliceerd — precies wat de meeste met AI gebouwde applicaties standaard doen — en de rekening viel op de mat voordat iemand ook maar iets in de gaten had.

Dit artikel legt uit welke inloggegevens en tokens écht gevoelig zijn, waar ze per ongeluk belanden, en hoe je binnen tien minuten controleert waar jouw geheimen rondslingeren.

## Niet alles is een geheim

Het is essentieel om eerst een helder onderscheid te maken. Alles behandelen als geheim leidt tot verlamming in je ontwikkelproces; niets behandelen als geheim leidt tot het rampscenario hierboven.

**Publieke identificatiecodes zijn bedoeld om rond te reizen.** Een openbare Supabase `anon`-sleutel, een publiceerbare Stripe-sleutel (`pk_live`), een meet-ID van Google Analytics of een publieke Mapbox-stijlcode. Deze sleutels vertellen de wereld welk project jij bent, niet wat je allemaal mag doen. Ze zijn ontworpen om veilig in de broncode van een webbrowser te leven.

**Geheimen (secrets) autoriseren bevoegdheden.** Een Supabase `service_role`-sleutel, een geheime Stripe-sleutel (`sk_live`), de API-sleutel van je e-mailprovider (zoals Resend of Postmark), de API-sleutel van OpenAI of Anthropic, database-connectiestrings met wachtwoorden en webhook signing secrets. Iedereen die over zo'n sleutel beschikt, kan uit naam van jouw applicatie handelen, data wissen of gebruikersdata downloaden.

**De categorie die mensen het vaakst overvalt: sleutels die direct geld kosten.** API's voor routekaarten, sms-verificatie, machinevertalingen en AI-taalmodellen rekenen af per verzoek of token. Een gelekte sleutel van dit type is niet zozeer een datalek, maar een automatische incasso zonder limiet. Geautomatiseerde internetscanners vinden openbare sleutels vaak al binnen enkele minuten na publicatie.

Twijfel je in welke categorie een sleutel valt? De documentatie van de leverancier vermeldt dit altijd expliciet — en het loont om dat vooraf te controleren in plaats van achteraf.

## De vier plekken waar geheimen per ongeluk belanden

**In de frontend-bundel.** Dit is de absolute nummer één. Het gebeurt omdat de snelste manier om een API-aanroep werkend te krijgen is om deze aan te roepen vanuit het bestand dat je op dat moment bewerkt. In een met AI ondersteunde workflow is dat precies het frontend-bestand waar het taalmodel naar kijkt.

**In de git-repository.** Een `.env`-bestand dat al vroeg in het project werd gecommit, vóórdat iemand eraan dacht om het toe te voegen aan `.gitignore`. Elke latere clone, fork of externe ontwikkelaar beschikt daarmee automatisch over een exacte kopie van alle geheimen.

**In een platformdashboard waar niemand meer bij kan.** Omgevingsvariabelen geconfigureerd in het dashboard van een hosting- of bouwplatform, uitsluitend bekend bij degene die het ooit heeft ingesteld. Dit is veiliger dan de eerste twee scenario's, maar vormt een acuut probleem zodra je migreert, wanneer een freelancer vertrekt, of wanneer je sleutels moet roteren en niet meer weet waar ze allemaal zijn ingevuld.

**In informele communicatie.** Gekopieerd en geplakt in een chat met een ingehuurde ontwikkelaar, gemaild naar een partner, of achtergelaten in een gedeeld Google Doc. Deze kopieën blijven vaak jaren langer bestaan dan de samenwerking zelf en zijn onzichtbaar voor elke geautomatiseerde beveiligingsaudit.

## Waarom sommige variabelen met opzet openbaar worden gemaakt

Dit is het mechanisme dat de meeste oprichters met verbijstering achterlaat.

Moderne frontend-buildtools (zoals Vite of Next.js) moeten configuratiewaarden kunnen doorgeven aan JavaScript-code die in de browser draait. Daarom stellen ze automatisch alle omgevingsvariabelen bloot die beginnen met een specifiek voorvoegsel — zoals `VITE_` of `NEXT_PUBLIC_`. Elke variabele met zo'n prefix wordt tijdens het buildproces letterlijk als platte tekst ingebakken in de JavaScript-bestanden die je eindgebruikers downloaden. Dat is geen datalek; het is de gedocumenteerde werking van het framework.

De valkuil is dat een variabele in een lokaal `.env`-bestand voor je gevoel altijd privé *lijkt*, ongeacht de naam. Als je een geheime API-sleutel plakt achter een variabele met zo'n publiek voorvoegsel, ziet het er in de editor uit als een nette omgevingsvariabele, maar publiceer je deze in werkelijkheid direct naar het hele internet. Dat is exact hoe de kaartensleutel in het openingsverhaal uitlekte. In de broncode zie je immers alleen de variabelenaam staan, waardoor het gevaar onzichtbaar blijft.

Vuistregel: als een variabele wordt uitgelezen door code die in de browser van de gebruiker draait, beschouw de waarde dan altijd als 100% openbaar, ongeacht het bestand waarin hij staat.

## Git-geschiedenis bewaart wat je hebt verwijderd

Een geheime sleutel uit een bestand verwijderen en opnieuw committen verwijdert het geheim alleen uit de huidige toestand van je project, niet uit het geheugen van git. Elke eerdere commit bevat de sleutel nog steeds ongewijzigd, en iedereen met leestoegang tot de repository kan hem direct uitlezen via de commit-historie.

Als een repository ooit publiek op GitHub heeft gestaan — al was het maar vijf minuten — moet je ervan uitgaan dat elk geheim dat erin stond definitief is gecompromitteerd. Geautomatiseerde crawlers scannen publieke repositories continu, en het tijdsverschil tussen publicatie en scraping bedraagt zelden meer dan een paar minuten.

De enige juiste reactie is directe sleutelrotatie, niet het herschrijven van je git-geschiedenis. De geschiedenis herschrijven is foutgevoelig, en het haalt kopieën die al door derden zijn gedownload niet terug. Door de sleutel direct bij de provider in te trekken en een nieuwe aan te maken, worden alle bestaande kopieën in één klap waardeloos.

## Waar geheimen wél thuishoren

**Uitsluitend in server-side omgevingen.** In de configuratie van serverless Edge Functions, de beveiligde secret store van je hostingplatform (zoals Vercel of Supabase Vault), of een dedicated secrets manager. Nooit in code die de browser van een gebruiker bereikt.

**Achter je eigen backend-endpoint.** Wanneer een frontend functionaliteit nodig heeft die door een geheim wordt ontgrendeld — zoals het genereren van een AI-antwoord, het versturen van een sms of het ophalen van adresgegevens — roept de frontend jouw eigen serverfunctie aan. Jouw server verifieert de identiteit van de ingelogde gebruiker, past een rate limit toe, en roept vervolgens pas de externe API aan met de geheime sleutel. Jouw geheime sleutel verlaat jouw infrastructuur nooit, en je behoudt altijd de regie om misbruik direct af te knijpen.

**Met de kleinst mogelijke bevoegdheden (scoping).** Veel diensten bieden beperkte sleutels aan: alleen-lezen, beperkt tot specifieke IP-adressen of domeinen, of begrensd tot bepaalde API-paden. Als een sleutel door het ontwerp openbaar moet zijn, beperkt een scoped sleutel de potentiële schade aanzienlijk.

**Met harde uitgavenlimieten.** Stel in het dashboard van elke betaalde API (zoals OpenAI of Google Cloud) een hard maandelijks budgetplafond in. Dit voorkomt een lek niet, maar het transformeert een potentieel oneindige financiële schadepost in een overzichtelijk, begrensd bedrag.

**Centraal roteerbaar op één plek.** Als het vervangen van een gecompromitteerde sleutel betekent dat je zes verschillende bestanden handmatig moet aanpassen en drie losse services moet redeployen, stel je rotatie uit. En uitgestelde rotatie is de reden waarom een freelancer van vorig jaar vandaag de dag nog steeds werkende toegang heeft.

## Een audit van tien minuten

- Open je live applicatie in de browser, inspecteer de paginabron en doorzoek de geladen JavaScript-bundels via de ontwikkelaarstools op trefwoorden als `key`, `secret`, `token` en `api`.
- Maak een lijst van alle externe services die je app gebruikt. Controleer per leverancier in de documentatie welke sleutels publiek mogen zijn en welke strikt geheim moeten blijven.
- Zoek in je repository naar `.env`-bestanden en controleer of ze expliciet in `.gitignore` staan. Doorzoek vervolgens ook de git-commitgeschiedenis.
- Bekijk de instellingen voor omgevingsvariabelen in je hostingplatform en lees elke regel zorgvuldig door. Bevatten variabelen met een publiek voorvoegsel per ongeluk geheime tokens?
- Bekijk het facturatiedashboard van elke verbruiksafhankelijke API en controleer of het dataverbruik strookt met je werkelijke gebruikersaantallen.
- Vraag jezelf af wie er in het verleden toegang heeft gehad tot deze waarden — ingehuurde ontwikkelaars, voormalige medeoprichters, of een gedeeld chatgesprek.

Elke sleutel waarover twijfel bestaat, moet direct worden geroteerd. Het aanmaken van een nieuwe sleutel kost vijf minuten; een onopgemerkt datalek of torenhoge factuur kost duizenden euro's.

## Hoe een volwassen inrichting eruitziet

Een overzichtelijke lijst van geheimen, waarbij elk geheim op exact één gezaghebbende plek bestaat. Frontend-code die uitsluitend publieke identificatiecodes bevat. Elke externe API-aanroep die een geheim vereist, verloopt via een eigen backend-route voorzien van authenticatie en snelheidsbegrenzing. Harde uitgavenlimieten ingesteld op alle betaalde accounts. Een beknopte, gedocumenteerde rotatieprocedure die binnen enkele minuten kan worden uitgevoerd. En idealiter een geautomatiseerde check in je CI/CD-pipeline die de build direct afbreekt zodra een patroon van een geheime sleutel in een client-side bestand wordt gedetecteerd — want fouten worden altijd laat op de avond onder tijdsdruk gemaakt, en een geautomatiseerde pipeline wordt nooit moe.

## Veilig zonder je applicatie opnieuw te hoeven bouwen

Onjuist sleutelbeheer is een van de meest voorkomende kwetsbaarheden wanneer een met AI gebouwd prototype wordt geïnspecteerd, en tegelijkertijd een van de snelst oplosbare. LaunchStudio voert een grondige audit uit op elk geheim in de codebase, build-configuratie en git-historie, roteert blootgestelde sleutels, verplaatst gevoelige API-aanroepen achter beveiligde serverfuncties met rate limiting, stelt strikte scopes en uitgavenlimieten in, en voegt een automatische pipeline-check toe om herhaling te voorkomen.

De gebruikersinterface die je in Lovable, Bolt of Cursor hebt gebouwd blijft exact zoals hij is, en de codebase blijft schoon en AI-leesbaar zodat je soepel kunt blijven doorontwikkelen. Dit werk is een vast onderdeel van het [Launch Ready pakket](https://launchstudio.eu/nl/#packages), uitgevoerd door de ervaren engineers van Manifera met elf jaar ervaring in enterprise productiesystemen voor partijen zoals Vodafone, TNO en CFLW.

Heeft je audit van tien minuten iets aan het licht gebracht dat je niet kunt verklaren? [Praat met een engineer die AI-gegenereerde code begrijpt](https://launchstudio.eu/nl/#contact).

## Inloggegevens die de samenwerking overleven

De technische controle hierboven spoort sleutels in programmacode op. Hij vindt echter geen sleutels die in het geheugen van mensen zitten — en dat is de categorie die in de praktijk tot de pijnlijkste situaties leidt:

**Freelancers en bureaus.** Een externe ontwikkelaar die in het voorjaar drie weken aan je app heeft gewerkt, beschikt vaak nog steeds over directe databasetoegang, een dashboardinlog bij je host en een beheerdersuitnodiging bij je betaalprovider. Het project is afgerond; de toegang is blijven bestaan omdat niemand een checklist bijhield.

**Voormalige medeoprichters.** De meest precaire situatie, en heel gewoon bij vroege startups. Toegang die informeel werd gedeeld op een moment dat het vertrouwen onvoorwaardelijk was, en die later nooit formeel is ingetrokken omdat dat als een motie van wantrouwen zou voelen.

**Gedeelde accounts en wachtwoordmanagers.** Wachtwoordkluizen met een gedeelde map, teamaccounts waar iedereen met hetzelfde algemene e-mailadres op inlogt, of een documentje waarin wachtwoorden 'voor het gemak' zijn genoteerd. Deze gegevens lekken door vermenigvuldiging, niet door een technisch beveiligingslek.

**Jezelf in het verleden.** Waarden die je hebt geplakt in chats met AI-assistenten, support-tickets van helpdesks, of e-mails die je ter herinnering aan jezelf hebt gestuurd. Ze blijven achter op plekken waar geen enkel audit-script bij kan.

De oplossing is een vaste offboarding-routine telkens wanneer iemand stopt met werken aan het product: trek accounttoegang direct in bij elke externe dienst, roteer alle gedeelde inloggegevens die diegene had kunnen kopiëren, en controleer of er domeinen of accounts op diens persoonlijke naam stonden geregistreerd. Dit kost twintig minuten en is het fundamentele verschil tussen toegang die daadwerkelijk stopt en toegang die simpelweg niet meer actief wordt gebruikt.

Maak een lijst van wie er ooit over welke sleutel heeft beschikt, en houd die actueel. Niet uit wantrouwen, maar vanuit hetzelfde gezonde verstand waarmee je bijhoudt wie er een sleutel van je kantoorpand heeft.

## Echt voorbeeld

### Een routeplanner die het project van een wildvreemde financierde

Stefan Rombouts bouwde Bezorgroute in Cursor: een route-optimalisatietool voor lokale cateringbedrijven rond Tilburg. De app riep een commerciële kaarten-API aan voor afstands- en routeberekeningen. De bijbehorende API-sleutel stond opgeslagen in een omgevingsvariabele met een framework-voorvoegsel, waardoor deze tijdens het builden automatisch werd ingebakken in de openbare frontend-bundel.

De factuur van de eerste maand was normaal. De factuur van de tweede maand was veertig keer zo hoog. De gebruiksstatistieken lieten honderdduizenden verzoeken zien, afkomstig van IP-adressen verspreid over drie continenten — een volume dat geen enkel cateringbedrijf in Brabant ooit had kunnen genereren.

Het herstel kostte vier werkdagen: de gelekte API-sleutel werd direct ingetrokken en vervangen door een nieuwe sleutel met strikte domeinbeperkingen en een hard maandelijks bestedingsplafond. Alle kaartaanroepen werden verplaatst naar een serverfunctie die controleert of de aanvrager een ingelogde en betalende klant is, gecombineerd met een strikte rate limit per account. Bij een audit van de git-historie kwamen nog twee andere gevoelige sleutels aan het licht die acht maanden eerder waren gecommit — een token voor een e-maildienst en een database-wachtwoord — die beide direct werden geroteerd. Tot slot werd een build-time security-check toegevoegd die elke deployment direct blokkeert zodra er een sleutelpatroon in de client-bundel verschijnt.

De leverancier van de kaartdienst schold een aanzienlijk deel van de frauduleuze kosten kwijt nadat Stefan kon aantonen dat de sleutel direct was ingetrokken en de architectuur structureel was beveiligd — wat zonder tastbaar bewijs van de uitgevoerde fixes nooit was gelukt.

**Resultaat:** de maandelijkse hosting- en API-kosten keerden direct terug naar een normaal niveau en zijn sindsdien al veertien maanden netjes evenredig aan het aantal betalende abonnees. Bovendien heeft de geautomatiseerde build-check sindsdien al één poging tot het per ongeluk publiceren van een API-sleutel tijdens een haastige release succesvol tegengehouden.

> *"Ik betaalde letterlijk voor de infrastructuur van een wildvreemde. De sleutel stond gewoon in mijn eigen website, open en bloot voor iedereen die op de juiste knop in zijn browser drukte."*
> — **Stefan Rombouts, Oprichter, Bezorgroute (Tilburg)**

**Kosten & Doorlooptijd:** € 1.650 (audit van inloggegevens, sleutelrotatie, server-side proxy met rate limiting, CI/CD pipeline-check) — afgerond binnen 4 werkdagen.

## Veelgestelde vragen

### Hoe weet ik of een API-sleutel veilig in mijn frontend kan staan?

Raadpleeg altijd de documentatie van de leverancier, die dit expliciet aangeeft. Publieke of publiceerbare sleutels (`public` of `anon`) identificeren je project en zijn specifiek ontworpen voor browsers; geheime sleutels (`secret` of `service_role`) verlenen beheerdersrechten en moeten te allen tijde op de server blijven. Bij enige twijfel moet je een sleutel altijd als strikt geheim behandelen.

### Ik heb de sleutel uit mijn code verwijderd. Is dat voldoende?

Nee, absoluut niet. Elke eerdere commit in je git-geschiedenis bevat het geheim nog steeds, en als de repository ooit ook maar even openbaar is geweest, kan de sleutel al lang zijn gekopieerd door geautomatiseerde scanners. Roteer de sleutel direct bij de leverancier: dat maakt alle bestaande kopieën in één klap waardeloos.

### Wat als mijn app echt een betaalde API vanuit de browser moet aanroepen?

Leid de aanroep altijd om via je eigen server-side endpoint. Jouw serverfunctie valideert eerst of de gebruiker is ingelogd, past een snelheidslimiet (rate limit) toe, en roept vervolgens pas de externe dienst aan met de geheime sleutel. Zo verlaat de sleutel jouw servers nooit en kun je misbruik direct blokkeren.

### Waarom werd mijn gelekte sleutel zo ontzettend snel gevonden?

Geautomatiseerde internetbots crawlen continu publieke GitHub-repositories en openbare JavaScript-bestanden op zoek naar specifieke sleutelpatronen van partijen als OpenAI, Stripe en Google. Er zit vrijwel nooit een mens handmatig naar jouw code te kijken; het is een script dat blootgestelde sleutels vaak al binnen enkele uren detecteert en misbruikt.

### Beschermen uitgavenlimieten mij tegen een gelekte sleutel?

Ze voorkomen het uitlekken of het ongeautoriseerde gebruik niet, maar ze zetten wel een keiharde rem op de financiële schade. In plaats van een openstaande rekening van duizenden euro's stopt de API simpelweg met functioneren zodra het ingestelde limietbedrag is bereikt. Daarom hoort elk verbruiksaccount standaard een harde bestedingslimiet te hebben.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe weet ik of een API-sleutel veilig in mijn frontend kan staan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De documentatie van de leverancier vermeldt dit expliciet. Publieke sleutels identificeren je project voor browsers; geheime sleutels autoriseren bewerkingen en moeten op de server blijven. Behandel twijfelgevallen altijd als geheim."
      }
    },
    {
      "@type": "Question",
      "name": "Ik heb de sleutel uit mijn code verwijderd. Is dat voldoende?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Eerdere commits bewaren het geheim, en scanners kunnen hem al gecrawld hebben. Roteer de sleutel direct bij de provider zodat alle bestaande kopieën direct waardeloos worden."
      }
    },
    {
      "@type": "Question",
      "name": "Wat als mijn app echt een betaalde API vanuit de browser moet aanroepen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Leid de aanroep om via een eigen backend-endpoint dat de gebruiker verifieert en rate limiting toepast alvorens de derde partij met het geheim aan te roepen."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom werd mijn gelekte sleutel zo ontzettend snel gevonden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Geautomatiseerde bots crawlen continu repositories en publieke JavaScript-bestanden op sleutelpatronen, waardoor blootgestelde sleutels vaak binnen enkele uren worden misbruikt."
      }
    },
    {
      "@type": "Question",
      "name": "Beschermen uitgavenlimieten mij tegen een gelekte sleutel?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ze voorkomen het lek niet, maar begrenzen wel de financiële schade tot een vooraf ingesteld maximum, waardoor ze onmisbaar zijn op elke verbruiksafhankelijke dienst."
      }
    }
  ]
}
</script>
