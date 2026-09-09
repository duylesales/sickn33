---
Titel: "Uw Prototype Veilig Delen: NDA's, Repo-Toegang en Wat Redelijk Is om te Vragen"
Trefwoorden: NDA voor softwareontwikkelaars, broncode delen met ontwikkelaar, GitHub toegangsrechten, prototype beschermen, verwerkersovereenkomst SaaS, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Uw Prototype Veilig Delen: NDA's, Repo-Toegang en Wat Redelijk Is om te Vragen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Uw Prototype Veilig Delen: NDA's, Repo-Toegang en Wat Redelijk Is om te Vragen",
  "description": "Oprichters vrezen vaak ideeëndiefstal terwijl ze actieve API-sleutels via chat delen. Een doordachte toegangsladder, een checklist vóór het delen en wat een NDA wél en niet beschermt.",
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
  "datePublished": "2027-01-23",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/sharing-your-prototype-safely-ndas-and-repo-access"
  }
}
</script>

Het is net iets over één uur 's nachts en de cursor zweeft boven de knop "Invite collaborator". Ergens in die repository zit acht maanden van uw leven, uw volledige bedrijfsidee en — hoewel u zich dat op dit moment wellicht nog niet realiseert — een live Stripe-sleutel, een Supabase service role key en uw OpenAI-token, allemaal netjes vastgelegd in een gecommit `.env.local`-bestand dat de AI-tool in week twee behulpzaam voor u aanmaakte.

Waar u zich op dit moment zorgen over maakt, is dat een vreemde er met uw idee vandoor gaat. Wat u daadwerkelijk handenvol geld gaat kosten, zijn die drie blootgestelde sleutels. Vrijwel elke oprichter in deze positie focust instinctief op het eerste risico en loopt met open ogen in het tweede. De remedie voor beide gevaren is gelukkig identiek: deel toegang in duidelijke fasen, schoon de repository op vóórdat u deelt, en begrijp exact welk juridisch document welke bescherming biedt.

## Het Werkelijke Risico Is Niet Waar U Zich Zorgen Over Maakt

Laten we volkomen eerlijk zijn over ideeëndiefstal. Die angst voelt heel reëel, ook al spreken de statistieken en de praktijk dit tegen. Een ontwikkelpartner die direct met u zou willen concurreren, heeft niet alleen uw idee nodig, maar ook uw diepgaande marktkennis, uw klantennetwerk, positionering, tijd en ondernemerslust. Bovendien zouden zij een voorspelbaar winstgevend bureau moeten opgeven voor een onzeker avontuur. Ontwikkelbureaus en freelancers zien jaarlijks tientallen concepten voorbijkomen; hun voornaamste knelpunt is productiecapaciteit, niet een gebrek aan ideeën. Misbruik komt incidenteel voor, maar het is uiterst zeldzaam en zeker niet het risico waar u uw operationele processen omheen moet ontwerpen.

De risico's die zich in de praktijk daadwerkelijk en veelvuldig manifesteren (gerangschikt op frequentie):

- **Uitlekken van inloggegevens en API-sleutels** — sleutels die nonchalant via Slack of WhatsApp worden gedeeld, meegecommit zijn in git-geschiedenissen, of na afloop van een project actief blijven bij externe ontwikkelaars. Dit is veruit de meest voorkomende blunder.
- **Echte klantgegevens die terechtkomen waar ze niet horen** — een volledige productiedatabase die voor testdoeleinden naar de laptop van een externe developer wordt gekopieerd. Betreft dit persoonsgegevens van Europese burgers, dan is dit een directe overtreding van de AVG (GDPR) — en een geheimhoudingsverklaring (NDA) dekt dit juridisch geenszins af.
- **Actieve toegangsrechten die nooit worden ingetrokken** — de freelancer van afgelopen voorjaar is nog steeds beheerder op uw Vercel-account, simpelweg omdat niemand na de oplevering de gebruikerslijst heeft gecontroleerd.
- **Onduidelijkheid over intellectueel eigendom (IE)** — het ontbreken van een formele schriftelijke overdracht van intellectuele eigendomsrechten. Deze vraag duikt steevast pas op wanneer advocaten tijdens een due diligence-traject achttien maanden later om bewijs vragen.

Elk van deze problemen is eenvoudig te voorkomen met ongeveer anderhalf uur degelijke voorbereiding.

## De Toegangsladder: Vier Treden, Strikt op Volgorde

Beschouw toegang niet als een binaire knop van "alles of niets". Zie het als een ladder waarbij elke trede verdiend moet worden naarmate het vertrouwen en de contractuele relatie groeien.

**Trede 0 — Helemaal niets technisch.** Een tien minuten durende schermopname van uw werkende applicatie, een heldere schriftelijke beschrijving van de functionaliteiten, en een opsomming van wat er volgens u nog ontbreekt. Dit volstaat voor iedere serieuze ontwikkelpartner om een realistische indicatie van de bandbreedte te geven en te bepalen of het project past. Als een partij direct toegang tot uw broncode eist vóórdat ze bereid zijn vijftien minuten met u te sparren, draaien ze de zaken om.

**Trede 1 — Alleen-lezen (read-only) op een opgeschoonde kopie.** Dit is de fase waarin de formele calculatie en offerte tot stand komen, en waar de meeste oprichters moeten blijven totdat de eerste betaling is verricht. Alleen-lezen betekent letterlijk alleen-lezen: op GitHub is dat de *Read*-rol op een privé-repository — géén *Write* en absoluut géén *Admin*. "Opgeschoonde kopie" betekent dat u eerst de stappen uit de onderstaande checklist hebt uitgevoerd.

**Trede 2 — Schrijftoegang tot een branch, nog altijd geen productie.** Zodra de overeenkomst is getekend, vindt het dagelijkse werk hier plaats: de ontwikkelaar pusht code naar een afgeschermde branch, u (of uw lead engineer) beoordeelt en merget de wijzigingen, en er raakt niets aan uw live-omgeving of actieve eindgebruikers. Dit omvat ontwikkel- en staging-omgevingen, test-sleutels voor betalingen en gefingeerde testdata.

**Trede 3 — Productietoegang.** Implementatie, DNS-configuratie, live betaalsleutels en de werkelijke productiedatabase. Deze stap komt pas helemaal aan het einde. Toegang wordt altijd verleend op persoonsniveau en nooit via gedeelde accounts. Dit verloopt via de officiële teamuitnodigingen van de platformen zelf — Vercel-teamleden, Supabase-organisatie-uitnodigingen, Stripe-gebruikersaccounts met strikt afgebakende rollen — en inloggegevens reizen nooit via een chatbericht.

De gouden regel die deze ladder effectief maakt: **toegangsrechten worden uitgenodigd via het platform, nooit verzonden als tekst.** Elk professioneel softwareplatform biedt de mogelijkheid om medewerkers op e-mailadres uit te nodigen met een specifieke rol. Hierdoor kunt u rechten met één klik intrekken en blijft elke actie auditeerbaar in de logs. Een sleutel kopiëren en in Slack plakken biedt geen van beide voordelen.

## De Checklist Vóór het Delen (Pre-Share Checklist)

Trek hier eenmalig negentig minuten voor uit vóórdat u Trede 1 betreedt. Vraag gerust een technisch onderlegde bekende om ondersteuning bij de eerste twee stappen — dit zijn immers de twee stappen die er het allermeest toe doen.

1. **Controleer de git-geschiedenis op geheimen (secrets).** Het simpelweg verwijderen van een API-sleutel uit een bestand haalt deze niet uit de git-historie. GitHub's automatische secret scanning signaleert veel van deze sleutels direct in privé-repositories; `gitleaks` is een gratis open-source tool waarmee u uw codebase lokaal grondig scant. AI-ontwikkeltargets zoals Cursor, Lovable of v0 committen opvallend vaak `.env`-bestanden met echte sleutels.
2. **Roteer alles wat u aantreft, evenals alles wat u ooit via chat hebt gedeeld.** Denk aan Stripe, Supabase (met name de service role key — deze omzeilt al uw databasebeveiligingsregels!), OpenAI, SendGrid en Resend. Het roteren van sleutels kost enkele minuten en maakt elk bestaand exemplaar direct ongeldig, inclusief vergeten kopieën.
3. **Overhandig test-sleutels, nooit actieve live-sleutels.** Zowel Stripe als Mollie bieden uitstekende, volledig functionele testomgevingen. Er is tijdens de bouwfase geen enkele legitieme reden waarom een externe ontwikkelaar over uw live betaalsleutels zou moeten beschikken.
4. **Deel geen echte productiegegevens.** Hebben ontwikkelaars realistische data nodig om functionaliteiten te bouwen, anonimiseer dan een subset of genereer synthetische records. Het exporteren van een tabel met echte klantgegevens naar de laptop van een aannemer is een formele gegevensdoorgifte met zware juridische implicaties onder de AVG.
5. **Maak een volledige back-up vóórdat u derden toegang verleent.** Een database-snapshot en een duidelijke notitie waar deze is opgeslagen. Het kost anderhalve minuut en voorkomt dat een programmeerfout uitmondt in een onherstelbare ramp.
6. **Leg schriftelijk vast wie toegang heeft tot wat, inclusief de datum.** Een simpel lijstje van vijf regels in uw projectdocumentatie. U hebt dit overzicht gegarandeerd later nodig, en niemand kan dit na enkele maanden nog foutloos uit het hoofd reconstrueren.
7. **Plaats direct een herinnering in uw agenda voor de dag na projectoplevering:** met als titel "toegangsrechten intrekken". Dit is de stap die in de praktijk door vrijwel iedereen wordt vergeten.

## Wat een NDA Wél Doet, en Wat Niet

Een geheimhoudingsverklaring (Non-Disclosure Agreement of NDA) is een juridische belofte om gedefinieerde vertrouwelijke informatie niet openbaar te maken of oneigenlijk te gebruiken. Deze is afdwingbaar via een gerechtelijke procedure — een stap die u in de praktijk zelden zult zetten. Dat is geen cynisme, maar een realistische beschrijving van de werkelijkheid. De werkelijke waarde van een NDA schuilt in het feit dat het formele vertrouwelijkheid vastlegt, de professionele toon van de samenwerking zet, en vrijwel niets kost om op te stellen.

Wat u redelijkerwijs mag verwachten in een evenwichtige, wederkerige (mutual) NDA:

- **Wederkerig (mutual)**, niet eenzijdig. Zij krijgen inzicht in uw product en architectuur; u krijgt inzicht in hun methodologieën, tarieven en calculaties.
- **Een heldere definitie van vertrouwelijke informatie** die uw broncode, data, klantenbestanden, prijsmodellen en roadmap omvat.
- **Een looptijd van twee tot vijf jaar**, wat de industriestandaard is. Eeuwigdurende geheimhoudingsplichten zijn buiten strikte fabrieksgeheimen hoogst ongebruikelijk.
- **Standaard uitzonderingen (carve-outs)**: informatie die reeds publiek bekend is, informatie die de partij al rechtmatig in bezit had, onafhankelijk ontwikkelde kennis, en verplichte openbaarmaking op grond van de wet. Het weigeren van deze standaardclausules maakt een NDA ontegenzeggelijk onacceptabel voor professionele bureaus.
- **Een bepaling inzake teruggave of vernietiging** van alle kopieën en documentatie na beëindiging van het traject.

Wat een NDA **niet** is: een geheimhoudingsverklaring is géén overdracht van intellectueel eigendom (IP assignment). Deze begripsverwarring kost oprichters regelmatig veel geld. Zonder een expliciete schriftelijke overdrachtsclausule behoort werk dat door een externe partij is gecreëerd in veel Europese jurisdicties niet automatisch aan u toe. De clausules die er écht toe doen, horen thuis in de hoofdovereenkomst van opdracht (de ontwikkelovereenkomst), niet in de NDA:

- **Volledige overdracht van alle intellectuele eigendomsrechten** op alle opgeleverde programmacode en werkproducten aan uw onderneming, hetzij direct bij creatie, hetzij direct na betaling van de factuur.
- **Een verbod op hergebruik van uw specifieke programmacode** in projecten voor andere klanten van het bureau. (Let op het woord *specifieke* — geen enkel bureau zal ermee instemmen om algemene conceptuele kennis of generieke hulpprogramma's niet te hergebruiken).
- **Een limitatieve lijst van geregistreerde accounts** met de expliciete bevestiging dat deze volledig op naam van uw onderneming staan.
- **Een verwerkersovereenkomst (Data Processing Agreement of DPA)** indien de partij in aanraking kan komen met persoonsgegevens van Europese gebruikers. Dit is een dwingendrechtelijke vereiste onder de AVG/GDPR, geen vrijblijvende optie, en het is hét document dat veel niet-technische oprichters vergeten te eisen.

## Wat Redelijk Is voor een Leverancier om te Vragen

Professionele samenwerking vereist wederzijds respect en redelijkheid:

**Volkomen redelijk:** alleen-lezen toegang tot de repository vóór het uitbrengen van een bindende offerte (niemand kan code serieus beprijzen zonder deze te hebben geïnspecteerd); een verkennend videogesprek in plaats van uitsluitend tekstuele briefings; toegang tot test-sleutels voor betalingen; een staging-omgeving; productietoegang zodra het contract is getekend; en een gebruikelijke aanbetaling.

**Redelijk, maar onderhandelbaar:** het tijdelijk hosten van de repository binnen de eigen GitHub-organisatie van het bureau tot aan de finale betaling bij een allereerste samenwerking — mits contractueel is vastgelegd dat de eigendomsoverdracht na betaling automatisch geschiedt en u gedurende het gehele traject over volledige leesrechten beschikt.

**Tijd om grenzen te stellen:** verzoeken om beheerdersrechten op uw domeinregistrar of DNS-provider; live betaalsleutels vóór de officiële livegang; een kopie van uw productiedatabase "omdat dat sneller ontwikkelt"; en elk verzoek om inloggegevens te sturen naar een privé-mailadres in plaats van een zakelijk account.

Iets wat vaak als een alarmsignaal oogt maar dat meestal niet is: **een ontwikkelpartner die weigert een NDA te ondertekenen vóór een allereerste oriënterend gesprek.** Bureaus die wekelijks talloze nieuwe aanvragen beoordelen, kunnen niet elk concept vooraf juridisch laten toetsen. Velen ondertekenen met plezier vóórdat ze daadwerkelijk code inzien (Trede 1), maar bedanken voor de administratieve rompslomp vóór een vrijblijvende kennismaking van een kwartier. Beoordeel een partner op hun toezeggingen bij Trede 1, niet bij Trede 0.

Het échte alarmsignaal is een partij die u niet schriftelijk kan uitleggen waar uw broncode wordt opgeslagen, wie binnen hun team toegang heeft, en wat er met lokale kopieën gebeurt na afloop van de opdracht. Dat is een antwoord van twee alinea's voor een partij die zijn operationele beveiliging op orde heeft, en een ongemakkelijke stilte voor wie maar wat aanrommelt.

## Na het Project: Het Intrekken van Toegangsrechten

Trek twintig minuten uit op de dag dat de samenwerking officieel wordt afgerond. Deze stap maakt van een succesvol afgerond project een structureel veilige onderneming.

Roteer iedere sleutel en elk wachtwoord dat de externe partij heeft aangeraakt — betaalsleutels, database-tokens, API-sleutels van derden — zelfs wanneer de verstandhouding uitstekend was. Het doel is dat u te allen tijde naar waarheid aan investeerders en auditors kunt verklaren dat niemand buiten uw organisatie over actieve productiesleutels beschikt. Verwijder hun accounts handmatig uit GitHub, uw hostingprovider, uw databaseservice, monitoringtools en error tracking; controleer de ledenlijst van elke dienst individueel in plaats van te hopen dat één verwijdering automatisch overal doorwerkt. Vraag een schriftelijke bevestiging dat alle lokale kopieën conform de NDA zijn vernietigd. Controleer direct daarna of uw applicatie vlekkeloos blijft draaien. Zo voorkomt u dat een service ongemerkt draaide op een sleutel die u zojuist hebt ingetrokken — een ontdekking die u liever op dinsdagmiddag doet dan tijdens een onverwachte piek in het weekend.

Werk uw toegangsdocument bij met de datum van beëindiging. Bij een volgend project start u vanuit een georganiseerde en veilige nulmeting in plaats van een gok.

## Waar te Beginnen

De route die oprichters behoedt voor kostbare misstappen is overzichtelijk en beproefd: start met een oriënterend gesprek, deel een opgeschoonde alleen-lezen kopie om een gefundeerde offerte te ontvangen, sluit een ontwikkelovereenkomst met IE-overdracht en een AVG-verwerkersovereenkomst, verleen werkoptoegang op branch-niveau zonder productie-impact, geef productietoegang uitsluitend bij de lancering, en trek alle rechten consequent in binnen een week na oplevering.

[LaunchStudio](https://launchstudio.eu/nl/) brengt offertes uit vanaf Trede 1 — een alleen-lezen kopie is voor ons ruim voldoende — en productietoegang is pas nodig op het moment van livegang. Alle toegang wordt bovendien netjes uitgenodigd via uw eigen zakelijke accounts. Onze beveiligings- en geheimhoudingsstandaarden zijn geworteld in de werkwijze van [Manifera](https://www.manifera.com/about-us/), dat al meer dan elf jaar complexe softwareprojecten uitvoert onder strikte NDA's en verwerkersovereenkomsten, onder meer voor veeleisende zakelijke klanten waar een datalek direct een zware toezichtszaak zou betekenen. Vraag gerust naar ons beveiligingsbeleid op schrift. En vraag datzelfde beleid vooral ook aan elke andere partij die u overweegt.

**Vraag, vóórdat u ook maar één regel code deelt, het schriftelijke toegangs- en geheimhoudingsbeleid op van elke kandidaat — stuur ons dezelfde vraag en vergelijk de antwoorden zij aan zij.**

## Echt voorbeeld

### Een Oprichter in Actie: De Sleutel Die Nog in de Geschiedenis Stond

Nadia el Amrani, voormalig recruitmentconsultant in Rotterdam, bouwde met behulp van Lovable het platform TalentLoop — een applicatie die freelance academische onderzoekers koppelt aan kortlopende universitaire projecten. Ze stond op het punt om drie externe softwareontwikkelaars uit te nodigen in haar repository om offertes op te vragen.

Een bevriende software-architect adviseerde haar om eerst een grondige scan op geheimen uit te voeren. Die scan bracht direct vier actieve sleutels aan het licht: een Supabase service role key, een Resend API-sleutel en twee versies van een OpenAI-token. Ze waren allemaal al in week twee gecommit en stonden nog altijd actief in de git-geschiedenis, hoewel de configuratiebestanden zelf al maanden geleden uit de projectmap waren verwijderd. Met name de Supabase service role key vormde een acuut gevaar: deze omzeilt elke Row Level Security (RLS) regel binnen de database, waardoor iedereen met deze sleutel alle vertrouwelijke kandidaatprofielen had kunnen inzien of wissen.

Nadia roteerde direct alle vier de sleutels, configureerde een schone set testgegevens, kende de drie kandidaat-ontwikkelaars uitsluitend alleen-lezen toegang toe, en legde hen exact dezelfde drie controlevragen voor: waar wordt mijn broncode bewaard, wie binnen uw team heeft toegang, en hoe garandeert u de vernietiging van lokale kopieën na afloop? Twee partijen stuurden binnen 24 uur een helder, professioneel antwoord van één alinea. De derde partij liet nooit meer iets van zich horen.

**Resultaat:** De backend van TalentLoop werd in negen werkdagen volledig gehard voor een vaste prijs van €2.650, waarbij de privacyregels voor kandidaatgegevens structureel werden verankerd in de database policies. Nadia tekende tevens direct een AVG-verwerkersovereenkomst, omdat er vanaf dag één met echte persoonsgegevens van sollicitanten werd gewerkt.

> *"Ik maakte me continu zorgen dat iemand mijn concept zou stelen. Ondertussen stond de hoofdsleutel van mijn complete database al vier maanden wagenwijd open in de git-geschiedenis. De scan kostte me welgeteld elf minuten."*
> — **Nadia el Amrani, Oprichter, TalentLoop (Rotterdam)**

---

## Veelgestelde Vragen

### Moet ik vóór het eerste gesprek al om een NDA vragen?
U kunt hierom vragen, maar houd er rekening mee dat gerenommeerde bureaus dit in die allereerste verkennende fase vaak afwijzen en in plaats daarvan voorstellen om een NDA te tekenen vóórdat er daadwerkelijk broncode wordt gedeeld. Een eerste gesprek over de doelstellingen van uw applicatie bevat zelden strikt vertrouwelijke bedrijfsinformatie. Star vasthouden aan een NDA vooraf kan ertoe leiden dat u waardevolle gesprekken misloopt met ervaren partners die wekelijks vele prototypes beoordelen.

### Is een gratis NDA-sjabloon goed genoeg?
Voor het delen van een prototype in de verkennende fase volstaat een standaard wederkerige (mutual) geheimhoudingsverklaring met een redelijke termijn en gebruikelijke uitzonderingen prima. Bewaar uw juridische budget liever voor de feitelijke ontwikkelovereenkomst; daarin worden immers de intellectuele eigendomsoverdracht (IP assignment) en de gegevensverwerkingsclausules vastgelegd die bepalen wie daadwerkelijk eigenaar is van de code.

### Kan ik een ontwikkelaar toegang geven zonder dat zij mijn klantgegevens inzien?
In vrijwel alle gevallen kan dat perfect. Ontwikkelaars hebben de programmacode, het databaseschema en representatieve testdata nodig, geen werkelijke persoonsgegevens. Geanonimiseerde of synthetisch gegenereerde datasets volstaan voor bijna elk ontwikkeltraject. Uitzonderingen betreffen doorgaans zeer specifieke productiefouten, die onder strikte voorwaarden met een tijdelijke, nauwkeurig afgebakende toegang kunnen worden onderzocht.

### Wat als mijn prototype op Lovable of Bolt staat in plaats van in een GitHub-repository?
Zowel Lovable als Bolt bieden de mogelijkheid om uw project te exporteren naar of te synchroniseren met een GitHub-repository. Het is zeer verstandig om dit te doen vóórdat u toegang deelt: het geeft u een heldere versiegeschiedenis, een centraal punt om toegangsrechten direct in te trekken, en onafhankelijkheid van het specifieke AI-platform. Het delen van de inloggegevens van uw AI-builderaccount moet u te allen tijde vermijden, omdat u daarin geen rollen kunt beperken of rechten selectief kunt intrekken.

### Heb ik zelfs voor een kleine app met vijftig gebruikers een verwerkersovereenkomst (DPA) nodig?
Zodra die vijftig gebruikers echte personen binnen de Europese Unie zijn en een externe ontwikkelaar toegang heeft tot hun persoonsgegevens, is het antwoord ja. De AVG kent geen uitzondering of vrijstelling voor kleine projecten of beginnende startups. Een verwerkersovereenkomst is doorgaans een standaard bijlage bij het hoofdcontract, en elke professionele ontwikkelpartner met Europese ervaring beschikt direct over een kant-en-klaar document.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik vóór het eerste gesprek al om een NDA vragen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "U kunt dit vragen, maar gerenommeerde bureaus stellen vaak voor om te tekenen vóórdat er code wordt gedeeld. Een oriënterend gesprek bevat zelden vertrouwelijke data, en star vasthouden kan waardevolle gesprekken met ervaren partners blokkeren."
      }
    },
    {
      "@type": "Question",
      "name": "Is een gratis NDA-sjabloon goed genoeg?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor de verkennende fase met een prototype volstaat een evenwichtig standaardmodel prima. Bewaar uw juridische budget voor de ontwikkelovereenkomst, waarin de overdracht van intellectueel eigendom en gegevensclausules worden geregeld."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik een ontwikkelaar toegang geven zonder dat zij mijn klantgegevens inzien?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, ontwikkelaars hebben voor vrijwel al het werk genoeg aan de code, het databaseschema en realistische testdata. Productiegegevens kunnen worden geanonimiseerd of nagebootst met synthetische records."
      }
    },
    {
      "@type": "Question",
      "name": "Wat als mijn prototype op Lovable of Bolt staat in plaats van in een GitHub-repository?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Exporteer of koppel het project altijd naar een GitHub-repository. Dat biedt versiebeheer, centrale controle over toegangsrechten en onafhankelijkheid. Deel nooit uw algemene inloggegevens van het AI-platform."
      }
    },
    {
      "@type": "Question",
      "name": "Heb ik zelfs voor een kleine app met vijftig gebruikers een verwerkersovereenkomst (DPA) nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, zodra het om echte EU-burgers gaat en een externe ontwikkelaar toegang heeft tot hun persoonsgegevens, vereist de AVG een verwerkersovereenkomst. Er bestaat geen vrijstelling voor kleine projecten."
      }
    }
  ]
}
</script>
