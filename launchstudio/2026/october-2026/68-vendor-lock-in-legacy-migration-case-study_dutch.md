---
Titel: "Case Study: Ontsnappen aan Vendor Lock-In bij een Migratie van Legacy naar AI SaaS"
Keywords: Vendor Lock-In, Legacy Migratie, AI SaaS Migratie, Code-eigendom, Supabase, Open Architectuur, LaunchStudio, Manifera, Bolt, Postgres
Buyer Stage: Decision
---

# Case Study: Ontsnappen aan Vendor Lock-In bij een Migratie van Legacy naar AI SaaS

Fatima runde zes jaar lang een kleinschalige kleermakerij- en verstelservice met boekingssysteem vanuit Rotterdam voordat ze besloot om de interne planningstool die ze in 2019 had laten bouwen, om te vormen tot een zelfstandig SaaS-product voor andere afspraakgebonden bedrijven. Er was maar één probleem: ze bezat de software die ze gebruikte niet. Dit is het verhaal van hoe een oprichter, gevangen in vendor lock-in bij een legacy-systeem, een AI-builder gebruikte om haar product opnieuw vorm te geven, en vervolgens samenwerkte met LaunchStudio om een backend te bouwen die ze daadwerkelijk zou bezitten — volledig en zonder voorbehoud.

## De Legacy-val

In 2019 huurde Fatima een klein lokaal ontwikkelbureau in om een boekings- en planningstool voor haar kleermakerij te bouwen. Het bureau leverde een werkende PHP-applicatie, hostte deze op hun eigen servers en verzorgde elke update tegen een maandelijkse vergoeding. Het werkte prima — totdat Fatima vijf jaar later besefte dat ze een productidee had dat de moeite waard was om als zelfstandig bedrijf te lanceren, en ontdekte hoe weinig controle ze eigenlijk had over waarvoor ze had betaald.

Het bureau had als enige de deploy-sleutels. De codebase stond in een privérepository waar Fatima nooit toegang toe had gekregen. Het databaseschema was niet gedocumenteerd, vol bureauspecifieke conventies die niemand buiten dat bedrijf gemakkelijk kon interpreteren, en gehost op infrastructuur die rechtstreeks aan het bureau werd gefactureerd, zonder exporttools en zonder API om haar eigen data in een bruikbaar formaat op te halen. Toen Fatima om een volledige code-overdracht vroeg zodat ze het product naar een nieuw team kon brengen, offreerde het bureau haar €9.000 voor "voorbereiding van de codebase en overdrachtsdocumentatie" — bovenop wat ze hen al vijf jaar aan abonnementskosten had betaald. Toen ze terugduwde, werden ze trager in het reageren op eenvoudige onderhoudsverzoeken. Ze zat, in de meest letterlijke zin, vast: afhankelijk van één enkele leverancier voor een systeem dat ze had laten bouwen maar nooit had beheerst.

Dit is een opvallend veelvoorkomend patroon voor oprichters die uit de generatie 2015-2020 van kleine, op maat gemaakte bureausoftware komen, en het beperkt zich niet tot oude PHP-monolieten. Hetzelfde lock-in-patroon duikt vandaag de dag op in een andere vorm: AI-builders die een werkende frontend genereren maar data opslaan in een databaseformaat dat de oprichter niet kan exporteren, of hostingomgevingen waarbij het builder-platform zelf de enige partij is met productietoegang. De technologie verandert; de val — volledig afhankelijk zijn van één partij voor toegang tot je eigen product — blijft hetzelfde.

## Het Opnieuw Vormgeven van de Frontend

In plaats van het losgeld te betalen of aan een kostbare herbouw vanaf nul te beginnen, koos Fatima een andere route. Ze gebruikte **Bolt** om een volledig heruitgevonden versie van het boekingsproduct te prototypen — vanaf dag één multi-tenant, zodat elk klein bedrijf (niet alleen kleermakers) zich kon aanmelden, hun eigen diensten kon configureren en een agenda kon beheren. In vijf weken avonden en weekenden bouwde ze een oprecht indrukwekkende frontend: een sleep-en-neerzet-agenda, geautomatiseerde sms-herinneringen via een externe API en een strakke multi-tenant onboarding-flow. In termen van pure productdenken was het een aanzienlijke verbetering ten opzichte van wat het bureau in 2019 voor haar had gebouwd.

Maar Fatima had haar les geleerd over eigenaarschap. Voordat ze ook maar één echte klant liet aanmelden, wilde ze een backend-architectuur die van haar was — écht, aantoonbaar, overdraagbaar van haar — ongeacht wie deze bouwde of wie deze in de toekomst zou hosten.

## Een Architectuur Zonder Lock-In Bouwen

Fatima bracht de door Bolt gegenereerde frontend naar **LaunchStudio (door Manifera)** met één expliciete, niet-onderhandelbare eis: welke backend het team ook bouwde, deze moest gebaseerd zijn op standaard, open, exporteerbare technologie, waarbij Fatima vanaf dag één volledig eigenaar was van elke inloggegeven, elke repository en elk stuk infrastructuur.

De aanpak van het engineeringteam draaide om drie principes die het patroon uit haar ervaring van 2019 rechtstreeks omkeerden:

1. **Standaard, overdraagbare datalaag.** Het team bouwde de backend op Supabase — dat zelf onder de motorkap standaard Postgres is, geen proprietair formaat. Elke tabel, elke rij, elk migratiebestand is standaard SQL dat geëxporteerd en op elke Postgres-instantie overal ter wereld kan worden uitgevoerd, zonder proprietaire exporttools en zonder bureauspecifieke schemaconventies die slechts één team kon lezen.

2. **Fatima bezit elke inloggegeven.** Het team richtte het Supabase-project, het Stripe-account voor multi-tenant abonnementsfacturatie, de hostingomgeving en de GitHub-repository allemaal in onder Fatima's eigen accounts en organisatorisch eigenaarschap, niet dat van het bureau. LaunchStudio-engineers werkten als samenwerkingspartners met beperkte toegang — nooit als de enige sleutelhouders. Als Fatima ooit opnieuw van engineeringpartner wil wisselen, gaan elke sleutel, elke repository en elk account mee over, zonder heronderhandeling en zonder losgeld.

3. **Gedocumenteerde, standaard conventies.** In plaats van bureauspecifieke naamgeving en ongedocumenteerde snelkoppelingen volgde het team standaard Row Level Security-patronen, gekoppeld aan `auth.uid()` en `organization_id` voor multi-tenant isolatie, met schema- en API-documentatie die elk bekwaam engineeringteam zonder kostbare overdrachtsperiode kon oppakken.

Naast de eigenaarschapsarchitectuur verhardde het LaunchStudio-team de daadwerkelijke productierisico's in Fatima's door Bolt gebouwde frontend: ze implementeerden correct RLS-beleid zodat de klantboekingen van de ene tenant nooit door een andere tenant konden worden opgevraagd, vervingen een client-side-only sms-trigger door een server-side wachtrijtaak (wat dubbele herinneringssms'jes voorkwam wanneer de verbinding van een gebruiker haperde), en verplaatsten de API-sleutel van de externe sms-dienst uit client-zichtbare code naar een beveiligde Edge Function.

## Het Resultaat: Een Product Dat Fatima Écht Bezit

Binnen drie weken had Fatima een multi-tenant boekings-SaaS-product met een volledig open, overdraagbare architectuur. Ze verwelkomde haar eerste vier betalende zakelijke klanten — waaronder een kapsalon en een fysiotherapiepraktijk — binnen de eerste maand na lancering, elk configureerde onafhankelijk hun eigen diensten en agenda's via de multi-tenant onboarding-flow.

Belangrijker voor de onderliggende les: Fatima heeft nu een uitgeschreven, geteste routekaart voor wat er gebeurt als ze ooit opnieuw van engineeringpartner moet wisselen. Elke inloggegeven is van haar. Elke regel van het schema is standaard, gedocumenteerd Postgres. Er is geen enkele leverancier die haar bedrijf kan gijzelen zoals het bureau in 2019 deed. Die overdraagbaarheid is geen extraatje — voor een oprichter die vendor lock-in al eens heeft meegemaakt, was het de kern van de hele opdracht.

## Waarom Vroege Architectuurkeuzes Later Van Belang Zijn

Fatima's verhaal illustreert een principe dat veel breder toepasbaar is dan haar specifieke situatie: de keuze *hoe* een backend wordt gebouwd, is net zo belangrijk als *of* deze werkt op de lanceringsdag. Een backend die op proprietaire, gesloten infrastructuur is gebouwd, kan er in een demo identiek uitzien aan een standaard Postgres/Supabase-backend — beide verwerken logins, beide verwerken betalingen, beide voelen snel aan. Het verschil wordt pas jaren later zichtbaar, precies op het moment dat een oprichter van leverancier moet wisselen, investeringen wil ophalen die due diligence op code-eigendom vereisen, of een technische mede-oprichter aan boord wil halen die echte toegang nodig heeft.

Oprichters die vandaag AI-builders gebruiken, staan in een ongewoon gunstige positie om deze val volledig te vermijden, omdat de meeste moderne AI-builder-platforms (Lovable, Bolt, Cursor, v0, Replit Agent) standaard uitgaan van open, standaard backends zoals Supabase of Postgres in plaats van proprietaire databases — maar alleen als het engineeringteam dat de backend daarna verhardt, die openheid behoudt in plaats van er tijdens het hardeningsproces zelf nieuwe lock-in overheen te leggen. De juiste vraag om aan elke ontwikkelpartner te stellen is niet alleen "werkt dit" — het is "wie heeft de sleutels als we klaar zijn."

## Belangrijkste Inzichten

- Vendor lock-in beperkt zich niet tot oude, gesloten legacy-systemen — het kan net zo gemakkelijk terugkeren in AI-builder-projecten als het hardeningsproces proprietaire hosting of ongedocumenteerde, bureauspecifieke conventies introduceert.

- Het duidelijkste signaal van lock-in is dat één partij als enige de deploy-sleutels, de enige databasetoegang of de enige accountgegevens heeft voor een systeem dat de oprichter nominaal bezit.

- Standaard Postgres/Supabase-architectuur is inherent overdraagbaarder dan proprietaire databases, omdat de onderliggende data kan worden geëxporteerd en op elke Postgres-instantie kan draaien zonder speciale tools.

- Volledig code- en inloggegeveneigendom moet vanaf dag één van elke engineeringopdracht een niet-onderhandelbare eis zijn, geen bijzaak die pas tijdens een uiteindelijke, kostbare overdracht wordt uitonderhandeld.

- Een migratie van een legacy, vastgezet systeem naar een door AI gebouwde frontend met een open backend-architectuur kan binnen weken, niet maanden, worden voltooid, zonder in te leveren op de eigenaarschapsgaranties die dezelfde val moeten voorkomen.

## Ontsnap aan Vendor Lock-In Zonder Bij Nul te Beginnen

Als een vorig bureau — of een vorige tool — de enige partij is met de sleutels tot uw eigen product, dan is dat op te lossen zonder kostbare herbouw.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 en geleid door Oprichter & Managing Director **Herre Roelevink**. Zoals Roelevink het verwoordt: *"We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot wasdom te brengen. Wij hebben elf jaar ervaring in precies dat vakgebied."* Door "Nederlands management te combineren met Vietnamees meesterschap", onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420), een Aziatische hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minh-stad, Vietnam** (Pho Quang Street). Via LaunchStudio nemen senior engineeringteams uw bestaande door AI gebouwde frontend en bouwen ze een productieklare backend op open, standaard infrastructuur — waarbij elke inloggegeven, repository en elk account vanaf dag één van u is — en veranderen ze een prototype, of een ontsnapping uit een vastgezet legacy-systeem, binnen 1 tot 3 weken in een overdraagbare MVP. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact) of bekijk hoe het [maatwerk software-ontwikkelteam van Manifera](https://www.manifera.com/services/custom-software-development/) legacy-migraties en open-architectuur-herbouwen aanpakt.

## Echt voorbeeld

### Een AI-native oprichter in actie: Platform voor Diergeneeskundige Dossiers

Adebayo, een dierenarts die een decennium had gepraktiseerd voordat hij ondernemer werd, zat vast aan een proprietair systeem voor diergeneeskundige dossiers, gebouwd door een regionale softwareleverancier in 2017. De leverancier rekende een jaarlijkse licentievergoeding, sloeg patiëntendossiers op in een gesloten databaseformaat zonder exportfunctie behalve een beperkt PDF-rapport, en weigerde API-toegang te geven voor een mobiele companion-app die Adebayo wilde bouwen voor huisdiereigenaren. Van leverancier wisselen zou hebben betekend dat jarenlange patiëntgeschiedenis handmatig opnieuw moest worden ingevoerd voor de dierenklinieken die het systeem gebruikten.

Adebayo gebruikte **v0** om een moderne vervangende interface te ontwerpen en bracht deze naar **LaunchStudio (door Manifera)** om de backend te bouwen. Het team bouwde een datamigratiepijplijn die de dossiers van de legacy-leverancier extraheerde via de beperkte PDF-export en OCR-verwerking, herstructureerde de data naar een standaard, gedocumenteerd Postgres-schema, en implementeerde RLS-beleid dat de dossiers van elke kliniek koppelde aan de eigen personeelsaccounts. Elke inloggegeven — database, hosting, API-sleutels — werd vanaf het begin ingericht onder Adebayo's eigen organisatorische accounts.

**Resultaat:** Adebayo migreerde drie klinieken weg van de legacy-leverancier zonder enig dataverlies en lanceerde een mobiele companion-app voor huisdiereigenaren die het oude proprietaire systeem nooit had kunnen ondersteunen.

**Kosten & Doorlooptijd:** €4.200 (Relaunch & Scale Pakket) — gemigreerd en gelanceerd binnen 15 werkdagen.

---

---

---
## Veelgestelde Vragen

### Wat wordt beschouwd als vendor lock-in bij een softwareproduct?

Vendor lock-in betekent dat één enkele partij — een ontwikkelbureau, een softwareleverancier of een builder-platform — als enige toegang heeft tot kritieke onderdelen van uw product: de deploy-sleutels, de database, het hostingaccount of de broncoderepository. Als u niet van leverancier kunt wisselen of een nieuw engineeringteam kunt inschakelen zonder de medewerking van die partij (of een grote overdrachtsvergoeding), zit u vast, ongeacht hoe goed het product op dit moment functioneert.

### Kunnen AI-builders ook vendor lock-in veroorzaken?

Ja, hoewel het minder vaak voorkomt dan bij legacy maatwerksystemen. De meeste moderne AI-builders zoals Lovable, Bolt, Cursor en v0 gaan standaard uit van open, standaard databases zoals Supabase of Postgres, wat een sterk uitgangspunt is. Lock-in kan er daarna alsnog insluipen als het team dat de backend voor productie verhardt, proprietaire hosting gebruikt, inloggegevens onder de eigen accounts houdt in plaats van die van de oprichter, of niets documenteert, waardoor het feitelijk de enige partij wordt die het systeem kan onderhouden.

### Hoe migreer je weg van een legacy-systeem zonder exportfunctie?

Dat hangt af van welke toegang er bestaat. Opties variëren van het gebruiken van een bestaande (zelfs beperkte) exportfunctie zoals een PDF- of CSV-rapport en het reconstrueren van de data met OCR of parsing-scripts, tot het onderhandelen over API- of databasetoegang bij de leverancier, tot in het slechtste geval het handmatig opnieuw invoeren van kritieke dossiers. De specifieke aanpak hangt sterk af van het legacy-systeem in kwestie, wat de reden is waarom een engineeringteam met ervaring in legacy-migraties dit per geval moet beoordelen.

### Waarom maakt het uit of de backend standaard Postgres gebruikt in plaats van een proprietaire database?

Standaard Postgres (inclusief Supabase, dat onder de motorkap Postgres is) kan worden geëxporteerd en op elke compatibele hostingprovider worden uitgevoerd met standaardtools, zonder proprietair formaat om te reverse-engineeren. Een proprietair databaseformaat koppelt uw data aan de infrastructuur en tools van één leverancier, wat betekent dat elke toekomstige migratie de medewerking van die leverancier vereist, wat reële overstapkosten en risico's toevoegt die een database met standaardformaat volledig vermijdt.

### Hoe lang duurt een migratie van legacy naar AI SaaS doorgaans?

Voor de meeste kleine tot middelgrote legacy-systemen, gecombineerd met een al functionerende AI-builder-frontend, duurt een volledige migratie inclusief datatransfer, RLS-gebaseerde multi-tenant beveiliging en productiehosting doorgaans 10 tot 15 werkdagen onder het Relaunch & Scale-pakket van LaunchStudio, hoewel de exacte doorlooptijd afhangt van de complexiteit en toegankelijkheid van de legacy-data.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat wordt beschouwd als vendor lock-in bij een softwareproduct?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vendor lock-in betekent dat één enkele partij — een ontwikkelbureau, een softwareleverancier of een builder-platform — als enige toegang heeft tot kritieke onderdelen van uw product: de deploy-sleutels, de database, het hostingaccount of de broncoderepository. Als u niet van leverancier kunt wisselen of een nieuw engineeringteam kunt inschakelen zonder de medewerking van die partij (of een grote overdrachtsvergoeding), zit u vast, ongeacht hoe goed het product op dit moment functioneert."
      }
    },
    {
      "@type": "Question",
      "name": "Kunnen AI-builders ook vendor lock-in veroorzaken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, hoewel het minder vaak voorkomt dan bij legacy maatwerksystemen. De meeste moderne AI-builders zoals Lovable, Bolt, Cursor en v0 gaan standaard uit van open, standaard databases zoals Supabase of Postgres, wat een sterk uitgangspunt is. Lock-in kan er daarna alsnog insluipen als het team dat de backend voor productie verhardt, proprietaire hosting gebruikt, inloggegevens onder de eigen accounts houdt in plaats van die van de oprichter, of niets documenteert, waardoor het feitelijk de enige partij wordt die het systeem kan onderhouden."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe migreer je weg van een legacy-systeem zonder exportfunctie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dat hangt af van welke toegang er bestaat. Opties variëren van het gebruiken van een bestaande (zelfs beperkte) exportfunctie zoals een PDF- of CSV-rapport en het reconstrueren van de data met OCR of parsing-scripts, tot het onderhandelen over API- of databasetoegang bij de leverancier, tot in het slechtste geval het handmatig opnieuw invoeren van kritieke dossiers. De specifieke aanpak hangt sterk af van het legacy-systeem in kwestie, wat de reden is waarom een engineeringteam met ervaring in legacy-migraties dit per geval moet beoordelen."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom maakt het uit of de backend standaard Postgres gebruikt in plaats van een proprietaire database?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Standaard Postgres (inclusief Supabase, dat onder de motorkap Postgres is) kan worden geëxporteerd en op elke compatibele hostingprovider worden uitgevoerd met standaardtools, zonder proprietair formaat om te reverse-engineeren. Een proprietair databaseformaat koppelt uw data aan de infrastructuur en tools van één leverancier, wat betekent dat elke toekomstige migratie de medewerking van die leverancier vereist, wat reële overstapkosten en risico's toevoegt die een database met standaardformaat volledig vermijdt."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt een migratie van legacy naar AI SaaS doorgaans?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor de meeste kleine tot middelgrote legacy-systemen, gecombineerd met een al functionerende AI-builder-frontend, duurt een volledige migratie inclusief datatransfer, RLS-gebaseerde multi-tenant beveiliging en productiehosting doorgaans 10 tot 15 werkdagen onder het Relaunch & Scale-pakket van LaunchStudio, hoewel de exacte doorlooptijd afhangt van de complexiteit en toegankelijkheid van de legacy-data."
      }
    }
  ]
}
</script>
