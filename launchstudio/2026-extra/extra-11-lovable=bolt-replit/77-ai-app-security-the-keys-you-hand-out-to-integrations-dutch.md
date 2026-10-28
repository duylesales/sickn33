---
Titel: "AI App Security: De Sleutels Die U Uitdeelt Aan Integraties"
Trefwoorden: ai app security, api keys, third party integrations, oauth scopes, supabase security, LaunchStudio, Manifera
Koperfase: Consideration
Doelgroep: SaaS Scale-Up
---

# AI App Security: De Sleutels Die U Uitdeelt Aan Integraties

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Security: De Sleutels Die U Uitdeelt Aan Integraties",
  "description": "Elke integratie is een authenticatiesleutel die leeft op een plek waar u geen controle over heeft - in beide richtingen. Hoe u API-sleutels uitgeeft die scoped en intrekbaar zijn, wat u doet met sleutels die klanten aan u toevertrouwen, en waarom overmatige toegangsrechten het grootste risico vormen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-18",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-app-security-the-keys-you-hand-out-to-integrations" }
}
</script>

Integraties zijn de manier waarop een softwareproduct ophoudt een geïsoleerd eiland te zijn. En elke integratie is een authenticatiesleutel die leeft op een server of apparaat waar u zelf geen enkel zicht op heeft.

Het dataverkeer stroomt in twee richtingen, maar de meeste oprichters denken slechts aan één kant: de sleutels die u zélf beheert voor externe diensten die u aanroept (zoals Stripe, Resend of OpenAI). Die krijgen aandacht omdat ze maandelijks op uw creditcardafschriften verschijnen. Maar de sleutels die u uitgeeft aan klanten en partners om uw API aan te roepen, krijgen aanzienlijk minder aandacht - omdat ze aanvoelen als een feature in plaats van een beveiligingsrisico. En de sleutels die klanten aan u toevertrouwen om verbinding te maken met hun boekhoudpakket of CRM, krijgen vaak helemaal geen aandacht. Dat is riskant, want juist die sleutels dragen de zwaarste juridische aansprakelijkheid.

## Drie Richtingen, Drie Wezenlijk Verschillende Problemen

**Sleutels die u zelf bezit.** Uw betaalprovider, mailprovider, kaartendienst of LLM-leverancier. Het risico is datadiefstal en torenhoge API-kosten. De beveiliging is bekend: uitsluitend server-side opslaan, permissies inperken, budgetlimieten instellen en regelmatig roteren.

**Sleutels die u uitgeeft.** Een zakelijke klant wil dat zijn interne ERP-systeem automatisch data naar uw applicatie pusht, of een partner bouwt een koppeling op uw platform. Nu bent u plotseling de API-provider. Het risico is dat uw API-sleutel belandt in de broncode van een externe partij, wordt uitgerold door mensen die u nog nooit heeft ontmoet, en mogelijk per ongeluk belandt in een openbare GitHub-repository waar u geen toegang toe heeft.

**Sleutels die klanten aan u geven.** Toegang tot hun Exact Online, Twinfield, Google Workspace of HubSpot. Het risico is dat u nu de sleutels bewaart van de interne bedrijfssystemen van een andere organisatie. Als uw database gecompromitteerd raakt, ligt hun bedrijfsadministratie op straat - wat exact is waar hun Chief Information Security Officer (CISO) zich zorgen over maakt.

Elk van deze drie situaties vereist een fundamenteel andere architectuur. De gevaarlijke reflex is om ze alle drie te behandelen als "een API-sleutel in een environment variabele".

## Als U Sleutels Uitgeeft: Ga Eruit Dat Ze Gaan Lekken

Niet door kwade opzet, maar door de alledaagse praktijk van softwareontwikkeling. Sleutels worden per ongeluk meegecommit naar publieke Git-repositories, gekopieerd in interne Slack-kanalen, ingevoerd in no-code tools door tijdelijke stagiairs, in frontend-scripts geplakt door onervaren webbouwers, of blijven rondslingeren wanneer een systeembeheerder vertrekt.

Ontwerp uw API-sleutels met dat scenario in gedachten. Vijf eigenschappen maken een uitgegeven sleutel veilig en beheersbaar:

**Fijnmazige scopes (machtigingen).** Een sleutel die uitsluitend facturen hoeft in te lezen, mag nooit de rechten hebben om klanten of projecten te verwijderen. Het aanbieden van strikte read-only sleutels kost nauwelijks extra ontwikkeltijd en elimineert 90% van de potentiële schade bij een lek.

**Toewijsbaar per integratie.** Elke sleutel behoort toe aan één specifieke koppeling. Zo kunt u in de logs exact zien welke tool de sleutel gebruikt, en kan de klant een gelekte sleutel intrekken zonder dat al zijn overige bedrijfskoppelingen platvallen. Eén algemene master-sleutel per klant die voor drie verschillende tools wordt gebruikt, kan bij een incident nooit worden ingetrokken zonder direct een operationele storing te veroorzaken.

**Direct intrekbaar door de klant in de interface.** Uw zakelijke klant moet te allen tijde zelfstandig een sleutel met één klik ongeldig kunnen maken, zonder eerst een supportticket te hoeven aanmaken.

**Inzichtelijk gebruik.** Toon in het instellingenscherm wanneer de sleutel voor het laatst gebruikt is en vanaf welk IP-adres. Klanten signaleren afwijkingen in hun eigen integraties veel sneller dan u dat kunt, en een sleutel die al een half jaar niet gebruikt is kan veilig worden verwijderd.

**Downtime-vrije rotatie.** Ondersteun de mogelijkheid dat een oude en een nieuwe sleutel tijdelijk beiden enkele dagen geldig blijven tijdens een overstap. Zonder deze optie wordt elke sleutelrotatie een gevreesde onderhoudsstop die klanten eindeloos voor zich uitschuiven.

Voeg daarnaast een rate limit per sleutel toe, en toon de sleutel uitsluitend éénmaal bij het aanmaken. Sla in uw database uitsluitend een cryptografische hash op (zoals SHA-256). Als uw systeem in staat is om een bestaande API-sleutel in platte tekst terug te tonen aan een gebruiker, betekent dit dat de sleutel op een manier is opgeslagen waarop deze ook door een aanvaller kan worden buitgemaakt.

## Sleutels Die Klanten Aan U Toevertrouwen Zijn Een Aansprakelijkheid

Wanneer een klant zijn boekhouding of agenda koppelt aan uw applicatie, neemt u de verantwoordelijkheid op u voor de toegang tot hun onderneming.

**Geef de voorkeur aan OAuth boven API-sleutels of wachtwoorden.** Waar het doelsysteem OAuth 2.0 ondersteunt, implementeert u OAuth: de klant autoriseert specifieke machtigingen in het officiële inlogscherm van de leverancier, u ziet nooit hun hoofdwachtwoord, en de klant kan uw toegang op elk gewenst moment intrekken in zijn eigen beheerdersdashboard.

**Vraag de kleinst mogelijke scope aan.** Elke extra machtiging is een vraagteken voor een inkoper en een direct risico bij een datalek. *"Leestoegang tot agenda-beschikbaarheid"* levert een soepel inkooptraject op; *"Volledige bewerkrechten op e-mailbox en agenda"* leidt direct tot een security-blokkade.

**Sla externe tokens strikt afgeschermd op.** Versleutel tokens at rest (met sterke encryptie zoals AES-GCM), scherm de databasetabel strikt af van reguliere leestoegang, log tokens nooit in debuglogs, en toon ze nooit in uw interne admin-paneel.

**Handhaaf token-refresh en intrekking zorgvuldig.** OAuth-tokens verlopen; klanten trekken koppelingen in. Beide situaties moeten leiden tot een heldere foutmelding in uw interface, niet tot een geruisloze synchronisatiefout die drie weken lang dataverlies maskeert.

**Verbreek de koppeling volledig.** Wanneer een klant een integratie verwijdert, roept u het officiële intrekkingsendpoint (token revocation) bij de externe provider aan in plaats van uitsluitend de rij in uw eigen database te wissen. Als u het token alleen lokaal verwijdert, blijft er bij de externe dienst een actieve autorisatie op uw naam geregistreerd staan - wat klanten vroeg of laat ontdekken.

## Webhooks in Beide Richtingen

Als u webhooks naar uw klanten verstuurt: onderteken ze cryptografisch (met een HMAC-SHA256 signature), documenteer in uw helpdesk hoe de klant die handtekening valideert, en implementeer een betrouwbaar retry-schema met exponential backoff. Een klant van wie de server een uur herstart, mag zijn notificaties niet definitief kwijtraken.

Als u webhooks ontvangt van partners: verifieer altijd de handtekening, ontdubbel events op hun unieke ID, en sta nooit toe dat een niet-geauthenticeerd webhook-bericht toegangsrechten of betalingen wijzigt.

## Wat Met AI Gegenereerde Integratiecode Stelselmatig Fout Doet

Er is een vast patroon dat we in vrijwel elke met AI gegenereerde codebase tegenkomen:

AI vraagt standaard maximale bevoegdheden aan (scopes als `read_write_admin`), omdat dat ervoor zorgt dat de voorbeeldcode direct bij de eerste poging werkt. Het slaat tokens op in gewone tekstkolommen naast gewone bedrijfsdata. Het logt de volledige HTTP-verzoeken en responses inclusief authenticatietokens in de serverlogs. Het negeert het mechanisme om verlopen tokens te verversen (refresh tokens), waardoor koppelingen na exact één uur of dertig dagen plotseling doodvallen. En het probeert mislukte API-aanroepen oneindig snel opnieuw, wat leidt tot een blokkade door de rate limits van de externe provider.

Vraag uw AI-tool daarom altijd expliciet om het tegenovergestelde: minimale scopes, gehashte/versleutelde opslag, uitsluiting van gevoelige headers in logs, correcte afhandeling van refresh-tokens en nette backoff-algoritmes.

## Externe Toegang Als Onderdeel van Uw Beveiligingsverhaal

Zodra uw product integraties aanbiedt, stellen zakelijke klanten steevast twee vragen:

**"Wat kan uw integratie precies aanpassen in onze systemen?"** Dit is in één heldere zin te beantwoorden wanneer u minimale scopes heeft aangevraagd, en uiterst pijnlijk wanneer u om volledige beheerdersrechten heeft gevraagd.

**"Wat gebeurt er met onze systemen als úw platform wordt gehackt?"** Zij willen de geruststelling horen dat opgeslagen tokens versleuteld zijn, dat interne toegang strikt gelogd is, en dat u beschikt over een noodprocedure om alle externe verbindingen in één keer ongeldig te maken.

Neem de antwoorden op beide vragen direct op in het formele beveiligingsdocument dat u aan inkoopteams verstrekt, direct naast de lijst met subverwerkers.

## De Inventarisatie Die Niemand Heeft

Een controle van een half uur brengt bij vrijwel elke scale-up verrassingen aan het licht:

Maak een lijst van elke API-sleutel die u zelf gebruikt: waar staat deze, wat zijn de bevoegdheden, geldt er een kostenlimiet, en wanneer is deze voor het laatst geroteerd? Maak een lijst van elke sleutel die u heeft uitgegeven aan klanten: aan wie, met welke scope, en wanneer is deze voor het laatst aangeroepen? En inventariseer alle tokens die klanten aan u hebben toevertrouwd. De uitkomst is steevast hetzelfde: sleutels met veel te ruime permissies, vergeten sleutels die al een jaar niet gebruikt zijn, en actieve tokens van klanten die hun abonnement al maanden geleden hebben opgezegd.

## Wat U Moet Doen Als Een Sleutel Gelekt Is

Vroeg of laat lekt er een sleutel - meestal door een fout bij de klant of een externe partner. Een vooraf vastgelegd stappenplan verandert een chaotische paniekochtend in een gestructureerde procedure:

**Trek de sleutel direct in, onderzoek pas daarna.** De menselijke reflex is om eerst de omvang van het lek te willen begrijpen vóórdat men ingrijpt. Dat is de verkeerde volgorde. Het intrekken van één specifieke API-sleutel raakt slechts één koppeling van één klant; die klant accepteert een kortstondige onderbreking graag. Het actief laten van een gecompromitteerde sleutel terwijl u logbestanden uitpluist, is onverantwoord.

**Reconstrueer wat er met de sleutel is gedaan.** Uw integratie-audittrail geeft het antwoord: welke endpoints zijn aangeroepen, vanaf welke IP-adressen, op welke tijdstippen en welke records zijn opgevraagd of gewijzigd? Hier bewijst de aanwezigheid van logging direct zijn waarde.

**Informeer de klant zakelijk en transparant.** Leg uit wat er blootgesteld is, welke data geraakt kon worden, wat uw logs uitwijzen en welke herstelacties u heeft uitgevoerd. Als de klant de sleutel zelf heeft gelekt (door deze in een openbare GitHub-repo te zetten), communiceer dit feitelijk en zonder verwijt, en help hen om de koppeling veilig via een backend te laten lopen.

**Beoordeel of er sprake is van een meldplichtig datalek.** Als de sleutel toegang gaf tot persoonsgegevens en er aanwijzingen zijn dat deze door onbevoegden is misbruikt, kwalificeert dit mogelijk als een datalek onder de AVG. Volg de termijnen die u contractueel in de verwerkersovereenkomst (DPA) bent overeengekomen en documenteer uw afwegingen nauwgezet.

**Beperk de schaderadius voor de toekomst.** Vrijwel elke gelekte sleutel blijkt achteraf veel meer rechten te hebben gehad dan strikt noodzakelijk was. Geef een nieuwe sleutel uit met een strakke, minimale scope en stel een rate limit in.

## Integraties Beveiligen Met LaunchStudio

Voor een softwareproduct met actieve integraties pakt LaunchStudio dit aan als een overzichtelijk technisch project: een complete inventarisatie van alle sleutels in de drie richtingen, herinrichting van uitgegeven sleutels (gehasht opgeslagen, voorzien van scopes, rate limits, auditlogging en self-service beheer voor de klant), versleuteling van klanttokens at rest, implementatie van nette OAuth-refresh flows, cryptografische ondertekening en verificatie van webhooks in beide richtingen, en een geteste noodprocedure voor het direct intrekken van sleutels.

Onze software engineers zijn afkomstig van Manifera: elf jaar ervaring in complexe enterprise systeemintegraties voor opdrachtgevers zoals Vodafone, TNO en CFLW, vanuit Amsterdam (Herengracht 420) en Ho Chi Minhstad.

[Vertel ons met welke systemen uw product koppelt](https://launchstudio.eu/nl/#contact) voor een gerichte analyse van uw integratieveiligheid, of bekijk onze [pakketten](https://launchstudio.eu/nl/#packages).

## Echt voorbeeld

### Eén Sleutel, Twaalf Bouwbedrijven, Volledige Schrijfrechten

Merel Duijvestein bouwde Bouwdossier met Lovable: software voor het uitwisselen van bouwdocumenten, gebruikt door twaalf bouwbedrijven en vier architectenbureaus in de regio Almere, met bouwtekeningen, vergunningen, inspectiefoto's en aannemerscontracten voor circa 300 actieve bouwprojecten.

De grootste aannemers wilden dat hun eigen projectmanagementsoftware (zoals BouwWatch en AFAS) automatisch documenten kon uploaden. Merel had daarvoor een API gebouwd en elke aannemer een API-sleutel verstrekt. Die sleutel was eenmalig gegenereerd, stond in platte tekst in haar database zodat ze hem kon opzoeken als een klant hem kwijt was, gaf onbeperkte beheerdersrechten (inclusief het permanent wissen van documenten en projecten), bevatte geen rate limit en was nog nooit geroteerd.

De IT-manager van een van de bouwbedrijven ontdekte het probleem zelf. Hun API-sleutel bleek achttien maanden eerder door een externe softwareontwikkelaar per ongeluk te zijn opgenomen in een GitHub-repository, en die repository was tijdens een recente bedrijfsfusie openbaar gemaakt. Hij vond de sleutel tijdens een algemene beveiligingsaudit.

Tien werkdagen aan gerichte interventies: het API-sleutelsysteem werd van de grond af opnieuw opgebouwd met fijnmazige scopes (lezen, schrijven en beheer als strikt gescheiden permissies), waarbij sleutels niet langer in platte tekst worden opgeslagen maar uitsluitend als cryptografische SHA-256 hash; sleutels worden nog maar één keer getoond bij aanmaak, krijgen een herkenbare naam per koppeling, zijn voorzien van rate limits en kunnen door de klant zelfstandig worden ingetrokken in een eigen beheerscherm met vermelding van het laatste gebruiks-IP; alle zestien bestaande sleutels werden ingetrokken en opnieuw uitgegeven met de minimale benodigde scope (voor negen partijen uitsluitend lezen en uploaden); de serverlogs rondom de gelekte sleutel werden vergeleken met de interne administratie van het bouwbedrijf, waarmee onomstotelijk werd vastgesteld dat er geen onbevoegde downloads hadden plaatsgevonden; uitgaande webhooks werden cryptografisch ondertekend; inkomende webhooks kregen handtekeningverificatie en ontdubbeling; en er werd een noodfunctie gebouwd om bij een incident alle actieve sleutels van een organisatie met één druk op de knop in te trekken.

**Resultaat:** Het bouwbedrijf bleef behouden en breidde het contract zelfs uit, en het transparante API-sleutelscherm met fijnmazige scopes werd een verkoopargument dat door twee latere enterprise-klanten expliciet werd genoemd tijdens de contractondertekening.

> *"Een door mij uitgegeven sleutel stond maandenlang in een openbare GitHub-repository met de bevoegdheid om elke bouwtekening van driehonderd projecten te wissen. Terwijl die sleutel alleen maar tekeningen hoefde te uploaden."*
> - **Merel Duijvestein, Oprichter, Bouwdossier (Almere)**

**Kosten & Doorlooptijd:** €4.700 (API-sleutelsysteem met scopes en hashing, self-service beheer, webhook-ondertekening, integratie-audittrail, noodintrekking) - afgerond in 10 werkdagen.

## Veelgestelde vragen

### Mag ik de API-sleutels die ik aan klanten uitgeef opslaan in de database?

Uitsluitend als eenrichtings-hash (zoals SHA-256). Toon de volledige sleutel eenmalig aan de gebruiker bij aanmaak en sla deze nooit in platte tekst op. Als uw applicatie in staat is om een bestaande API-sleutel opnieuw op te diepen, kan deze bij een datalek ook door een aanvaller worden gestolen.

### Welke bevoegdheden (scopes) moet een uitgegeven API-sleutel krijgen?

Uitsluitend de minimale rechten die voor de specifieke koppeling noodzakelijk zijn, aangeboden als gescheiden rechten (alleen-lezen, schrijven, beheer). De meeste externe koppelingen hoeven uitsluitend data op te halen of toe te voegen; een strikt read-only profiel voorkomt het overgrote deel van potentiële schade bij een lek.

### Hoe moet ik inloggegevens bewaren die klanten aan mij toevertrouwen?

Sterk versleuteld in rust (at rest met encryptie zoals AES-GCM), strikt afgeschermd van reguliere applicatielogica, nooit zichtbaar in logs en nooit opvraagbaar in interne beheerschermen. Gebruik waar mogelijk OAuth in plaats van vaste wachtwoorden, en roep bij opzegging direct het intrekkingsendpoint bij de externe partij aan.

### Welke fouten maken AI-tools stelselmatig bij integratiecode?

AI genereert standaard veel te ruime bevoegdheden (volledige admin-rechten), bewaart tokens in niet-versleutelde databasetabellen, logt gevoelige autorisatie-headers in serverlogs, vergeet het periodiek verversen van OAuth-tokens en implementeert geen rate-limiting of backoff-schema's.

### Welke vragen stellen zakelijke klanten over softwarekoppelingen?

Klanten willen weten wat uw integratie precies kan aanpassen in hun eigen systemen, en wat er met hun data gebeurt als uw platform gecompromitteerd raakt. Beide vragen zijn overtuigend te beantwoorden met minimale scopes, versleutelde token-opslag en een geteste noodprocedure om sleutels direct in te trekken.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Mag ik de API-sleutels die ik aan klanten uitgeef opslaan in de database?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Alleen als cryptografische hash, eenmalig getoond bij creatie. Als uw systeem sleutels in platte tekst bewaart, kunnen ze bij een datalek worden gestolen."
      }
    },
    {
      "@type": "Question",
      "name": "Welke bevoegdheden (scopes) moet een uitgegeven API-sleutel krijgen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De kleinst mogelijke scope: gescheiden rechten voor lezen, schrijven en admin. Read-only sleutels elimineren het leeuwendeel van mogelijke schade."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe moet ik inloggegevens bewaren die klanten aan mij toevertrouwen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Versleuteld at rest, nooit in logs of admin-panels, bij voorkeur via OAuth met minimale scopes en directe intrekking bij de bron bij ontkoppeling."
      }
    },
    {
      "@type": "Question",
      "name": "Welke fouten maken AI-tools stelselmatig bij integratiecode?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Overmatige admin-scopes, tokens in platte tekst, credentials in debuglogs, verwaarloosde token-refresh en ontbrekende retry backoff."
      }
    },
    {
      "@type": "Question",
      "name": "Welke vragen stellen zakelijke klanten over softwarekoppelingen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Wat de integratie kan in hun systemen en wat er gebeurt bij een datalek. Minimale scopes en een directe intrekkingsprocedure geven direct vertrouwen."
      }
    }
  ]
}
</script>
