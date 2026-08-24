---
Titel: "Code-eigendom Uitgelegd: Wat U Behoudt Als U LaunchStudio Inhuurt"
Keywords: Code-eigendom, IP-eigendom, Vendor Lock-in, GitHub Repository Toegang, SaaS Founder Rechten, LaunchStudio, Manifera, Herre Roelevink, Lovable, Supabase
Buyer Stage: Decision
---

# Code-eigendom Uitgelegd: Wat U Behoudt Als U LaunchStudio Inhuurt

Vraag aan elke founder die heeft overwogen externe engineeringhulp in te schakelen wat hen tegenhoudt, en u hoort een variant van dezelfde zorg: *"Wat als ik de controle over mijn eigen product verlies?"* Dat is geen irrationele angst. Genoeg founders hebben horrorverhalen — een freelancer die de app op zijn eigen hostingaccount bouwde en vervolgens verdween, een bureau dat de "master"-repository op zijn eigen GitLab-organisatie hield, een platform dat stilletjes de infrastructuur bezit waarop uw bedrijf draait. Wanneer uw codebase, uw klantdata en de hele toekomst van uw bedrijf op het spel staan, is "wie bezit dit eigenlijk als het traject eindigt?" geen bijzaak. Het is dé vraag.

Dit artikel beantwoordt die vraag rechtstreeks, zonder de marketingmist die er meestal omheen hangt. Hier leest u precies wat code-eigendom betekent, wat er doorgaans misgaat bij minder transparante samenwerkingsvormen, en wat u concreet — regel voor regel — behoudt wanneer u LaunchStudio inhuurt om een door AI gebouwd prototype te verharden tot een productieklare MVP.

## De angst die elke founder heeft vóór het inschakelen van externe hulp

Founders die hun eerste versie bouwen met een AI-builder zoals Lovable, Bolt of Cursor komen doorgaans op een vergelijkbaar splitsingspunt. Het prototype werkt in demo's, maar is niet veilig, en dat weten ze. De logische volgende stap is engineers inschakelen die het kunnen verharden — maar dat betekent toegang geven tot een codebase die maanden werk vertegenwoordigt, en in veel gevallen het volledige intellectueel eigendom van het bedrijf.

Daar begint de onrust. Founders hebben de verhalen gehoord: een developer die op een persoonlijk AWS-account bouwt en de app gijzelt tijdens een geschil over de factuur. Een bureaucontract met vage IP-clausules waardoor het eigendom onduidelijk blijft. Een no-code platform dat uw app technisch host op infrastructuur die u nooit volledig kunt exporteren. Dit zijn geen hypothetische uitzonderingen — ze gebeuren vaak genoeg dat "de controle over mijn eigen codebase verliezen" een van de belangrijkste redenen is waarom founders hulp uitstellen, zelfs wanneer ze weten dat hun backend gevaarlijk kwetsbaar is.

De ironie is dat het vermijden van hulp uit angst voor eigendomsverlies het daadwerkelijke risico vaak alleen maar groter maakt: een onveilige app met echte gebruikersdata en live betalingen blijft langer onveilig, terwijl de founder ofwel zelf backend-beveiliging probeert te leren, ofwel blijft zoeken naar een partner die hij kan vertrouwen.

## Wat "code-eigendom" in de praktijk werkelijk betekent

"Eigendom" klinkt abstract totdat u het opdeelt in de specifieke zaken die te allen tijde op uw naam, onder uw controle moeten staan:

- **De broncode-repository.** Geen gespiegelde kopie, geen fork op de organisatie van iemand anders — de daadwerkelijke GitHub- of GitLab-repository waarin uw app leeft, vanaf dag één eigendom van uw account of de organisatie van uw bedrijf.
- **Het hostingaccount.** Of dat nu Vercel, Netlify of een andere provider is, de productie-deployment moet draaien onder credentials die u beheert, niet onder een persoonlijk account van een leverancier of bureau.
- **Het account van het database- en backendplatform.** Als u Supabase, Firebase of vergelijkbaar gebruikt, behoren het project zelf — en de beheersleutels ervan — u toe.
- **Het betalingsaccount.** Uw Stripe-account, met uw bedrijfsentiteit als accounthouder, die uitbetalingen rechtstreeks op uw bankrekening ontvangt — niet via een tussenpartij geleid.
- **Omgevingsvariabelen en geheimen.** API-sleutels, servicecredentials en configuratiewaarden staan in infrastructuur die u bezit en op elk moment kunt roteren.
- **Documentatie van elke aangebrachte wijziging.** Een overzicht van wat er is gebouwd, waarom en hoe — zodat u (of elke toekomstige engineer) de codebase kan overnemen zonder afhankelijk te zijn van de mensen die er als laatste aan gewerkt hebben.

Als ook maar één van deze onderdelen buiten uw controle valt, bezit u uw product niet volledig — u huurt de toegang ertoe, ook al zegt niemand dat expliciet.

## Hoe LaunchStudio in uw repository werkt, niet ernaast

Het engineeringmodel van LaunchStudio is gebouwd rond een eenvoudig principe: engineers werken *binnen* de bestaande infrastructuur van de founder, niet ernaast en niet in plaats daarvan. Wanneer een founder LaunchStudio inschakelt om een door AI gebouwd prototype te verharden, begint het proces ermee dat de founder het engineeringteam uitnodigt als medewerker in zijn eigen GitHub- of GitLab-repository — de repository die al bestaat, onder het eigen account of de eigen organisatie van de founder.

Vanaf dat moment worden alle commits doorgevoerd in die repository, transparant en herleidbaar — niet samengevoegd tot één anonieme overdracht aan het einde. Founders kunnen het werk in real time volgen, elke pull request beoordelen en precies zien wat er is veranderd en waarom. Er bestaat geen aparte "LaunchStudio-versie" van de app die later moet worden samengevoegd of gemigreerd. Er is slechts één codebase, en die is altijd van de founder geweest.

Hetzelfde principe geldt voor elk stukje infrastructuur dat tijdens het traject wordt aangeraakt. Row Level Security-beleid wordt toegevoegd binnen het eigen Supabase-project van de founder. De Stripe webhook-listener wordt uitgerold naar het eigen hostingaccount van de founder. Geheimen worden opgeslagen in de eigen omgevingsvariabelenbeheerder van de founder. LaunchStudio zet nooit parallelle infrastructuur op waar de founder later zelf uit zou moeten worden losgemaakt — er valt niets los te maken, omdat er nooit iets van de accounts van de founder is verplaatst.

Dit betekent ook dat er geen sprake is van lock-in door een eigen framework. LaunchStudio herbouwt uw frontend niet op een intern platform en introduceert geen aangepaste abstractielaag die alleen door de eigen engineers wordt begrepen. Het team werkt met de tools die u al heeft — door Lovable gegenereerde React-componenten, door Bolt opgezette routes, door Cursor geschreven functies — en verhardt wat eronder ligt, met standaard, goed gedocumenteerde technologieën zoals Supabase RLS-beleid, de officiële webhook-infrastructuur van Stripe en conventionele cloudhosting. Elke bekwame engineer die u in de toekomst inhuurt, of dat nu intern is of bij een ander bureau, kan de repository openen en begrijpen zonder dat LaunchStudio iets hoeft te vertalen.

## Het onduidelijke alternatief: wat u riskeert bij sommige ontwikkelbureaus en platforms

Niet elke ontwikkelpartner werkt op deze manier, en het is de moeite waard om specifiek te zijn over hoe de minder transparante alternatieven eruitzien, want founders realiseren zich het risico vaak pas als ze er al middenin zitten.

Sommige freelancers en kleine bureaus bouwen en deployen de volledige applicatie op hun eigen persoonlijke of bedrijfsinfrastructuur — hun AWS-account, hun hostingprovider, hun domeinregistrar — met de founder op zijn best als gast. Als de samenwerking slecht eindigt, of de developer simpelweg niet meer reageert, kan de founder buitengesloten worden van zijn eigen product zonder eenvoudige weg terug. Dit is precies het scenario dat meer dan één founder zo hard heeft geraakt dat hij permanent wantrouwend werd tegenover externe hulp.

Sommige no-code- en low-code-platforms vertonen een subtielere versie van hetzelfde probleem. Uw app "draait" op het platform, maar u krijgt nooit een overdraagbare, exporteerbare codebase — u bouwt binnen muren die iemand anders toebehoren, en vertrekken betekent opnieuw beginnen. En sommige bureaus behouden onbeperkt beheerderstoegang tot de Stripe-accounts of databaseprojecten van klanten, "voor ondersteuningsdoeleinden," wat onschuldig klinkt totdat u van provider wilt wisselen en ontdekt dat u de sleutels niet daadwerkelijk in handen heeft.

Deze constructies zijn niet altijd kwaadwillig — soms zijn het simpelweg slordige standaardinstellingen die niemand heeft gecorrigeerd. Maar het effect op de founder is in beide gevallen hetzelfde: minder onderhandelingspositie, minder flexibiliteit en een codebase die niet volledig van hem is op het moment dat het er echt toe doet — of dat nu een investeringsronde is, een overnamegesprek, of simpelweg de vrijheid om van leverancier te wisselen.

## Wat u behoudt, regel voor regel

Om dit concreet te maken: dit blijft gedurende en na een traject met LaunchStudio onder uw eigendom en controle:

- **Toegang tot de repository:** Volledige beheerdersrechten op uw GitHub- of GitLab-repository, met een complete, ononderbroken commitgeschiedenis van vóór, tijdens en na het traject.
- **Eigendom van het hostingaccount:** Uw Vercel-, Netlify- of vergelijkbare account blijft van u; LaunchStudio deployt ernaartoe als medewerker, nooit als accounthouder.
- **Eigendom van het Stripe-account:** Uw bedrijf blijft de accounthouder; uitbetalingen komen rechtstreeks op uw bankrekening terecht, zonder tussenlaag die iets afroomt of omleidt.
- **Eigendom van het Supabase-/database-account:** Uw project, uw beheerderscredentials, uw data — LaunchStudio configureert beleid en functies binnen infrastructuur die altijd al van u was.
- **Omgevingsvariabelen en geheimen:** Opgeslagen in uw eigen geheimenbeheerder, door u op elk moment te roteren, nooit hardgecodeerd in een door een leverancier beheerde dienst.
- **Documentatie:** Een schriftelijk overzicht van elke beveiligingsfix, elke webhook-wijziging, elk RLS-beleid — overgedragen als onderdeel van het traject, niet achtergehouden als drukmiddel voor toekomstig werk.

Er is geen stap in dit overzicht waarbij de founder pas "eigenaar wordt" na het betalen van een exitvergoeding, het onderhandelen over een overdracht, of het uitzitten van een supportcontract. Het eigendom is nooit overgedragen, dus er valt niets terug te winnen.

## Waarom dit belangrijk is bij due diligence en daarna

Code-eigendom is niet alleen een kwestie van gemoedsrust — het heeft directe commerciële gevolgen. Investeerders die technische due diligence uitvoeren, zullen vragen wie toegang heeft tot uw infrastructuur, of uw codebase overdraagbaar is, en of een leverancier invloed heeft op uw vermogen om onafhankelijk te opereren. Een founder die kan antwoorden "alles staat in mijn eigen accounts, volledig gedocumenteerd, met een schone commitgeschiedenis" haalt die lat binnen enkele minuten. Een founder die moet uitleggen dat een voormalige developer nog steeds het hostingaccount beheert, of dat de app niet gemakkelijk van een no-code platform af kan, geeft precies het soort rode vlag dat een deal vertraagt of laat mislukken.

Dezelfde logica geldt ver buiten fondsenwerving. Als u ooit een CTO wilt aantrekken, van technische partner wilt wisselen, of simpelweg uw eerste interne engineer wilt aannemen, dan betekent een volledig eigen, goed gedocumenteerde codebase dat die overgang u slechts een paar dagen inwerktijd kost. Een codebase die verstrengeld is met de infrastructuur van een leverancier kan weken van ontwarring betekenen, of in het slechtste geval, opnieuw beginnen vanaf nul.

## Belangrijkste inzichten

- Founders die externe engineeringhulp overwegen, maken zich vaak meer zorgen over het verliezen van controle over hun codebase dan over het technische werk zelf — en die angst is regelmatig terecht, gezien reële praktijken in de sector.

- Echt code-eigendom betekent dat de repository, het hostingaccount, het betalingsaccount, het database-account en alle geheimen te allen tijde onder de eigen credentials van de founder staan, niet die van een leverancier.

- LaunchStudio werkt rechtstreeks binnen de bestaande GitHub- of GitLab-repository van de founder en binnen de bestaande hosting-, database- en Stripe-accounts, met transparante, herleidbare commits vanaf dag één.

- Sommige ontwikkelbureaus en no-code platforms creëren onduidelijkere eigendomssituaties — persoonlijke hostingaccounts, niet-overdraagbare platforms, of onbeperkte beheerderstoegang — die founders buiten hun eigen product kunnen doen komen te staan.

- Een schone, volledig gedocumenteerde, door de founder beheerde codebase is een tastbaar voordeel tijdens due diligence van investeerders, overnamegesprekken of elke toekomstige overstap naar een andere leverancier.

## Behoud elke regel van uw eigen product

Maak uw door AI gebouwde app productieklaar zonder ooit de sleutels van andermans infrastructuur te moeten overhandigen.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 en geleid door Oprichter & Managing Director **Herre Roelevink**. Zoals Roelevink het verwoordt: *"We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot wasdom te brengen. Wij hebben elf jaar ervaring in precies dat vakgebied."* Door "Nederlands management te combineren met Vietnamees meesterschap", onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420), een Aziatische hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minh-stad, Vietnam** (Pho Quang Street). Via LaunchStudio nemen senior engineeringteams uw bestaande door AI gebouwde frontend en implementeren ze productieklare beveiligingscontroles, live betalingsgateways, veilige hosting en monitoring — volledig werkend binnen accounts en repositories die al van u zijn — waardoor uw prototype binnen 1 tot 3 weken verandert in een veilige MVP, zonder rebuild en zonder ooit uw eigendom af te nemen. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact) of bekijk hoe het [maatwerk software-ontwikkelteam van Manifera](https://www.manifera.com/services/custom-software-development/) production-hardening aanpakt voor door AI gegenereerde codebases.

## Echt voorbeeld

### Een AI-native oprichter in actie: Tweezijdig marktplaatsplatform

Sofia Marchetti, een startup-oprichter, gebruikte **Lovable** om het prototype te bouwen voor een tweezijdige marktplaats-SaaS die freelance ambachtslieden verbindt met retailkopers. Sofia had eerder al eens een slechte ervaring gehad: haar eerste versie van het product was gebouwd door een freelance developer die alles op zijn eigen persoonlijke hostingaccount had geplaatst. Toen er een betalingsgeschil tussen hen ontstond, reageerde hij helemaal niet meer — waardoor Sofia buitengesloten werd van haar eigen app, zonder toegang tot de code, de database of zelfs het domein waarvoor ze had betaald.

Deze keer koos Sofia specifiek voor LaunchStudio omdat het traject begon met haar uitnodiging aan het team in haar eigen GitHub-repository, haar eigen Supabase-project en haar eigen Vercel-account — niets werd ooit ergens gehost buiten haar eigen controle. Tijdens het traject verhardden de engineers van LaunchStudio de Row Level Security over de multi-tenant data van haar marktplaats, herstelden ze een defecte Stripe Connect-uitbetalingsflow die de commissies van verkopers verkeerd berekende, en droegen ze volledige schriftelijke documentatie over van elke aangebrachte wijziging.

**Resultaat:** Sofia behield gedurende het volledige traject 100% eigendom en beheerderstoegang tot elk onderdeel van haar stack, en kon later tijdens technische due diligence een schone, volledig gedocumenteerde codebase aan investeerders tonen zonder eigendomsvragen te hoeven wegwuiven.

**Kosten & Doorlooptijd:** € 3.400 (Relaunch & Scale) — 11 werkdagen.

---

---

---
## Veelgestelde Vragen

### Verlies ik toegang tot mijn codebase als ik LaunchStudio inhuur?

Nee. LaunchStudio werkt rechtstreeks binnen uw bestaande GitHub- of GitLab-repository, die te allen tijde onder uw account of organisatie blijft. Engineers worden toegevoegd als medewerkers, commits zijn transparant en herleidbaar, en u behoudt volledige beheerderstoegang vóór, tijdens en na het traject.

### Wie is eigenaar van de hosting-, database- en betalingsaccounts na het project?

U bent dat. LaunchStudio configureert Row Level Security, webhooks en monitoring binnen uw eigen Supabase-, Vercel- en Stripe-accounts. Er wordt niets uitgerold naar infrastructuur die LaunchStudio beheert, dus er is later geen apart systeem waar u vanaf moet migreren.

### Wat gebeurt er met API-sleutels en geheimen tijdens het traject?

Die blijven in uw eigen systeem voor geheimenbeheer — bijvoorbeeld de omgevingsvariabelen van Supabase Edge Functions of de omgevingsinstellingen van uw hostingprovider — die u op elk moment kunt inzien en roteren. LaunchStudio hardcodeert nooit credentials in infrastructuur die het onafhankelijk van u beheert.

### Hoe verschilt dit van sommige bureaus of freelancers die op hun eigen infrastructuur bouwen?

Sommige developers deployen klantprojecten naar hun eigen persoonlijke of bedrijfsaccounts voor hosting, database of domein, wat founders kan buitensluiten als de samenwerking slecht eindigt. Het model van LaunchStudio vermijdt dit volledig door te werken binnen accounts die de founder al bezit, waardoor er nooit een overdracht van controle hoeft te worden onderhandeld.

### Levert LaunchStudio documentatie van de aangebrachte wijzigingen?

Ja. Elke beveiligingsfix, elke webhook-wijziging en elke infrastructuuraanpassing wordt gedocumenteerd en overgedragen als onderdeel van het traject, wat founders — en elke toekomstige engineer die zij inhuren — een duidelijk overzicht geeft van precies wat er is gebouwd en waarom.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Verlies ik toegang tot mijn codebase als ik LaunchStudio inhuur?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. LaunchStudio werkt rechtstreeks binnen uw bestaande GitHub- of GitLab-repository, die te allen tijde onder uw account of organisatie blijft. Engineers worden toegevoegd als medewerkers, commits zijn transparant en herleidbaar, en u behoudt volledige beheerderstoegang vóór, tijdens en na het traject."
      }
    },
    {
      "@type": "Question",
      "name": "Wie is eigenaar van de hosting-, database- en betalingsaccounts na het project?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "U bent dat. LaunchStudio configureert Row Level Security, webhooks en monitoring binnen uw eigen Supabase-, Vercel- en Stripe-accounts. Er wordt niets uitgerold naar infrastructuur die LaunchStudio beheert, dus er is later geen apart systeem waar u vanaf moet migreren."
      }
    },
    {
      "@type": "Question",
      "name": "Wat gebeurt er met API-sleutels en geheimen tijdens het traject?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Die blijven in uw eigen systeem voor geheimenbeheer — bijvoorbeeld de omgevingsvariabelen van Supabase Edge Functions of de omgevingsinstellingen van uw hostingprovider — die u op elk moment kunt inzien en roteren. LaunchStudio hardcodeert nooit credentials in infrastructuur die het onafhankelijk van u beheert."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe verschilt dit van sommige bureaus of freelancers die op hun eigen infrastructuur bouwen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sommige developers deployen klantprojecten naar hun eigen persoonlijke of bedrijfsaccounts voor hosting, database of domein, wat founders kan buitensluiten als de samenwerking slecht eindigt. Het model van LaunchStudio vermijdt dit volledig door te werken binnen accounts die de founder al bezit, waardoor er nooit een overdracht van controle hoeft te worden onderhandeld."
      }
    },
    {
      "@type": "Question",
      "name": "Levert LaunchStudio documentatie van de aangebrachte wijzigingen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. Elke beveiligingsfix, elke webhook-wijziging en elke infrastructuuraanpassing wordt gedocumenteerd en overgedragen als onderdeel van het traject, wat founders — en elke toekomstige engineer die zij inhuren — een duidelijk overzicht geeft van precies wat er is gebouwd en waarom."
      }
    }
  ]
}
</script>
