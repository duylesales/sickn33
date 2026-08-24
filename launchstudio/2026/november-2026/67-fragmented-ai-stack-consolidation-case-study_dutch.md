---
Titel: "Case Study: Een Gefragmenteerde AI-stack Consolideren tot Eén Verdedigbaar Platform"
Keywords: Gefragmenteerde AI-stack, Stack Consolidatie, AI Tool Wildgroei, No-Code Tool Migratie, LaunchStudio, Manifera
Buyer Stage: Decision
---

# Case Study: Een Gefragmenteerde AI-stack Consolideren tot Eén Verdedigbaar Platform

De meeste AI-native producten beginnen niet als één schone build. Ze beginnen als drie of vier afzonderlijke experimenten — een landingspagina in de ene tool, een dashboardprototype in een andere, een intern adminpaneel erbij geplakt met een derde — die toevallig afzonderlijk goed genoeg werken zodat niemand stopt om ze te consolideren voordat klanten op alle vier tegelijk gaan vertrouwen. Dit is precies de positie waarin Rashid Nabizada zich bevond toen een due-diligence-verzoek van een overnemend bedrijf hem dwong een vraag te beantwoorden die hij een jaar lang had vermeden: hoe ziet zijn daadwerkelijke productiearchitectuur eruit, getekend als één diagram? Het eerlijke antwoord — vier losgekoppelde tools, drie afzonderlijke authenticatiesystemen, en geen enkele bron van waarheid voor klantgegevens — kostte bijna een overnamebod van € 1,2 miljoen. Dit is de case study over hoe die gefragmenteerde stack in drie weken werd geconsolideerd tot één verdedigbaar platform, en wat elke oprichter die met meerdere AI-builders jongleert zou moeten controleren voordat iemand anders de vraag afdwingt.

## Hoe een Werkend Product Vier Producten Wordt met Eén Naam

Het bedrijf van Rashid, LedgerPilot, is een tool voor boekhoudautomatisering voor kleine accountantskantoren. Het begon niet als één samenhangende build — het groeide op de manier waarop de meeste AI-native producten daadwerkelijk groeien: snel, iteratief, en tool voor tool naarmate nieuwe behoeften ontstonden. Het oorspronkelijke klantgerichte dashboard werd gebouwd in **Lovable** over een lang weekend, en het werkte goed genoeg zodat Rashid het nooit herbouwde. Zes maanden later, toen het product een publieke marketingsite nodig had met een geïntegreerde prijscalculator, gebruikte hij **v0** om er snel een op te zetten, omdat dat sneller was dan de Lovable-app uit te breiden. Toen een intern team een boekhouder-gerichte admintool nodig had om klantaccounts te beheren, bouwde een contractor deze in **Bolt** als een aparte applicatie, verbonden met zijn eigen Supabase-instantie, omdat het opzetten van gedeelde toegang aanvoelde als een afleiding van het uitleveren van features. En toen Rashid een snelle manier nodig had om een AI-gedreven functie voor uitgavecategorisering te prototypen, bouwde hij een op zichzelf staand proof-of-concept in **Cursor**, dat zo goed werkte dat het stilletjes een productieafhankelijkheid werd, rechtstreeks aangeroepen vanuit het hoofddashboard via een niet-geauthenticeerde interne API.

Elke beslissing was op zichzelf logisch. Niets ervan was roekeloos — het was de volkomen normale manier waarop een oprichter met beperkte middelen snel uitlevert met de beschikbare tools. Maar achttien maanden later was LedgerPilot niet één applicatie. Het was vier applicaties die toevallig een merk deelden, aan elkaar genaaid met API-aanroepen die niemand volledig had gedocumenteerd, drie afzonderlijke gebruikersdatabases zonder één bron van waarheid voor wie een klant daadwerkelijk was, en drie verschillende authenticatiesystemen die elk onafhankelijk bepaalden of een bepaald verzoek was toegestaan.

## De Vraag die de Fragmentatie Blootlegde

Een boekhoudsoftwarebedrijf benaderde Rashid over de overname van LedgerPilot, en hun technische due-diligence-team vroeg om iets dat Rashid nooit daadwerkelijk had geproduceerd: een systeemarchitectuurdiagram dat toont hoe data tussen componenten stroomde, en bevestiging dat klantgegevens consistent toegangsgecontroleerd waren over het volledige product.

Rashid kon geen van beide vragen met vertrouwen beantwoorden. Hij wist, ruwweg, hoe de onderdelen met elkaar verbonden waren, omdat hij elk ervan had gebouwd of laten bouwen. Maar "ruwweg" zou een technische beoordeling door het engineeringteam van een overnemende partij niet overleven, en toen hij daadwerkelijk ging zitten om de verbindingen na te gaan, vond hij problemen waarvan hij niet had geweten dat ze bestonden: de door Cursor gebouwde service voor uitgavecategorisering accepteerde verzoeken van het hoofddashboard van Lovable zonder enig authenticatietoken — iedereen die de endpoint-URL ontdekte, kon deze rechtstreeks aanroepen. De prijscalculator van de v0-marketingsite haalde live abonnementsdata op uit dezelfde Supabase-instantie als de door Bolt gebouwde admintool, via een gedeelde service-role-sleutel zonder scoping, wat betekende dat een compromittering van de laagwaardige marketingsite de volledige klantendatabase kon blootleggen. En omdat klantrecords op drie plaatsen bestonden zonder verzoeningsproces, zag een supportmedewerker die de admintool gebruikte soms verouderde abonnementsdata die al was gewijzigd in het hoofddashboard.

Het due-diligence-team van de overnemende partij markeerde alle drie de bevindingen en pauzeerde de deal in afwachting van herstel, met een venster van zes weken voordat de term sheet zou verlopen.

## De Echte Architectuur in Kaart Brengen Voordat Er Iets Wordt Gerepareerd

Rashid schakelde LaunchStudio in onder het **Enterprise Hardening**-pakket, en het engagement begon met iets dat noch Rashid noch zijn contractors ooit hadden gedaan: een volledige architectuuraudit die elke datastroom, elke authenticatiegrens en elke service-naar-service-aanroep over alle vier de tools traceerde, wat resulteerde in het diagram dat de overnemende partij oorspronkelijk had gevraagd. Deze stap was net zo belangrijk als de reparaties die volgden, omdat het consolideren van een gefragmenteerde stack zonder deze eerst nauwkeurig in kaart te brengen, de neiging heeft om de problemen op te lossen die u al kent, terwijl de problemen die u niet kent verborgen blijven.

De audit bracht het volledige beeld naar boven: drie afzonderlijke Supabase-projecten met overlappende maar inconsistente klantrecords, één niet-geauthenticeerde interne API met echte financiële data, een gedeeld service-role-inloggegeven dat over tools werd gebruikt zonder scoping, en geen enkel systeem dat met zekerheid kon antwoorden op "heeft deze specifieke klant een actief abonnement."

## De Consolidatie van Drie Weken

Met de architectuur in kaart gebracht, ontwierpen de engineers van LaunchStudio een consolidatieplan dat expliciet niet betekende dat alle vier de tools werden herbouwd tot één — dat had achttien maanden gevalideerd UI-werk over een marketingsite, dashboard en adminpaneel die elk afzonderlijk goed functioneerden, weggegooid. In plaats daarvan was de oplossing architecturaal: het vaststellen van één gezaghebbende datalaag en het afdwingen van echte grenzen tussen de bestaande frontends, zonder hun interfaces aan te raken.

Het team wees het oorspronkelijke Supabase-project van LedgerPilot aan als de enige bron van waarheid voor klant- en abonnementsdata, migreerde de aparte database van de door Bolt gebouwde admintool erin met een verzoeningsscript dat elk conflicterend record oploste, en liet de prijscalculator van de v0-marketingsite naar dezelfde gezaghebbende bron wijzen via een correct gescoped, alleen-lezen API in plaats van een gedupliceerde gedeelde sleutel. Het niet-geauthenticeerde, door Cursor gebouwde endpoint voor uitgavecategorisering werd herbouwd achter ondertekende service-naar-service-tokens, zodat alleen het legitieme dashboard het kon aanroepen, en Row Level Security werd consistent geïmplementeerd over de nu enkele database, gescoped naar `auth.uid()` voor klantgerichte toegang en naar een aparte, geauditeerde service-role voor de admintool. Een uniforme authenticatielaag verving de drie onafhankelijke systemen, zodat de identiteit en rechten van een klant eenmalig werden vastgesteld en consistent werden gerespecteerd over elk oppervlak van het product.

## Wat de Overnemende Partij Zag bij Herindiening

Het team van Rashid diende de architectuurdocumentatie zeventien werkdagen na de start van het engagement opnieuw in, vier dagen voor de deadline van zes weken. Het diagram toonde nu één gezaghebbende datalaag, gedocumenteerde en afgedwongen grenzen tussen vier frontends, en nergens in het systeem niet-geauthenticeerde interne service-aanroepen. Het engineeringteam van de overnemende partij voerde een eigen verificatieronde uit en vond geen verdere lacunes.

De les gaat ver voorbij overnames. Elk AI-native product dat iteratief is gebouwd over meerdere builders — een gebruikelijke en redelijke manier om snel te bewegen — verzamelt uiteindelijk dezelfde categorie risico: gefragmenteerd eigenaarschap van data, inconsistente toegangscontrole, en ongedocumenteerd vertrouwen tussen componenten die nooit waren ontworpen om elkaar te vertrouwen. De producten die kritische toetsing overleven, of het nu van een overnemende partij, een enterprise-beveiligingsteam, of een compliance-auditor is, zijn degene waarbij iemand het onopvallende werk heeft gedaan om de echte architectuur in kaart te brengen en echte grenzen af te dwingen voordat daarom werd gevraagd.

## Belangrijkste Inzichten

- Een product dat iteratief is gebouwd over meerdere AI-builders — Lovable, v0, Bolt, Cursor — eindigt vaak als meerdere losgekoppelde applicaties die een merk delen, met gefragmenteerd eigenaarschap van data en inconsistente toegangscontrole die niemand opmerkt totdat een technische beoordeling de vraag afdwingt.

- Het gevaarlijkste patroon in een gefragmenteerde stack is een gedeeld, niet-gescoped service-role-inloggegeven dat over tools wordt gebruikt: een compromittering van de laagwaardigste component (vaak een marketingsite) kan de volledige klantendatabase erachter blootleggen.

- Het consolideren van een gefragmenteerde stack vereist niet dat elke frontend wordt herbouwd tot één applicatie — de oplossing is het vaststellen van één gezaghebbende datalaag en het afdwingen van echte authenticatie- en autorisatiegrenzen tussen de bestaande interfaces.

- Een architectuuraudit die elke datastroom en vertrouwensrelatie in kaart brengt voordat er reparaties worden uitgevoerd, is essentieel, omdat het herstellen van alleen de problemen die u al kent, terwijl een gefragmenteerde stack de problemen verbergt die u niet kent, het doel voorbijschiet.

- Overnemende partijen, enterprise-kopers en compliance-auditors stellen uiteindelijk allemaal dezelfde onderliggende vraag waar een gefragmenteerde AI-stack moeite mee heeft: kunt u de daadwerkelijke architectuur van uw systeem tekenen en bewijzen dat data er consistent doorheen beschermd wordt?

## Laat Fragmentatie Niet Naar Boven Komen Tijdens Due Diligence

Als uw product is gegroeid over meerdere AI-builders en niemand ooit het echte architectuurdiagram heeft getekend, komt die lacune precies naar boven op het moment dat de inzet het hoogst is — een overname, een enterprise-deal, of een compliance-audit.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 en geleid door Oprichter & Managing Director **Herre Roelevink**. Zoals Roelevink het verwoordt: *"We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot wasdom te brengen. Wij hebben elf jaar ervaring in precies dat vakgebied."* Door "Nederlands management te combineren met Vietnamees meesterschap," onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420), een Aziatische hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minh-stad, Vietnam** (Pho Quang Street), met enterprise-klanten waaronder Vodafone en TNO. Via LaunchStudio auditeren senior engineeringteams uw gefragmenteerde AI-builder-stack, brengen ze de echte datastromen en vertrouwensgrenzen in kaart, en consolideren ze deze tot één verdedigbaar platform — zonder de frontends te herbouwen die u al heeft gevalideerd — binnen 1 tot 3 weken. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact) of bekijk hoe het [maatwerk software-ontwikkelteam van Manifera](https://www.manifera.com/services/custom-software-development/) architectuurconsolidatie aanpakt voor AI-native producten.

## Echt voorbeeld

### Een AI-native oprichter in actie: Een Stack van Vier Tools Consolideren Vóór een Overname

Rashid Nabizada, oprichter van LedgerPilot, een boekhoudautomatiseringsplatform voor kleine accountantskantoren, had het product iteratief gebouwd over vier afzonderlijke AI-builders gedurende achttien maanden — een **Lovable**-klantdashboard, een **v0**-marketingsite, een door **Bolt** gebouwde interne admintool, en een door **Cursor** gebouwde service voor uitgavecategorisering — elk met zijn eigen database- of authenticatielogica. Een overnamebod van € 1,2 miljoen liep vast toen het technische due-diligence-team van de overnemende partij om een architectuurdiagram vroeg en ontdekte dat er geen bestond, en vervolgens een niet-geauthenticeerde interne API vond die financiële data droeg, en een gedeeld, niet-gescoped database-inloggegeven dat de marketingsite met de klantendatabase verbond.

Rashid schakelde het Enterprise Hardening-pakket van LaunchStudio in voor een volledige architectuuraudit en consolidatie. Het engineeringteam bracht elke datastroom en vertrouwensgrens over alle vier de tools in kaart, stelde het oorspronkelijke Supabase-project vast als een enkele gezaghebbende databron, migreerde en verzoende de aparte database van de admintool erin, herbouwde het niet-geauthenticeerde endpoint voor uitgavecategorisering achter ondertekende service-naar-service-tokens, implementeerde consistente Row Level Security over de verenigde database, en verving drie onafhankelijke authenticatiesystemen door één uniforme laag — zonder een van de vier bestaande frontend-interfaces te wijzigen.

**Resultaat:** De opnieuw ingediende architectuurdocumentatie van LedgerPilot toonde één gezaghebbende datalaag met volledig afgedwongen grenzen tussen alle vier de applicaties, slaagde voor de onafhankelijke verificatieronde van de overnemende partij zonder verdere bevindingen, en de overname van € 1,2 miljoen werd zes weken later afgerond.

**Kosten & Doorlooptijd:** € 5.900 (Enterprise Hardening Pakket) — geconsolideerd en geverifieerd in 17 werkdagen, vier dagen voor de deadline van de term sheet.

---

---

---
## Veelgestelde Vragen

### Hoe raakt een product in eerste instantie gefragmenteerd over meerdere AI-builders?

Dit gebeurt meestal geleidelijk en redelijk: een oprichter gebruikt welke tool dan ook het snelst is voor elke nieuwe behoefte — een dashboard in de ene builder, een marketingsite in een andere, een admintool van een derde — omdat het herbouwen van een bestaand oppervlak om één nieuwe feature toe te voegen trager aanvoelt dan iets nieuws opzetten. Elke individuele beslissing is verstandig; de fragmentatie wordt pas zichtbaar zodra iemand ineens om het volledige beeld vraagt.

### Wat is het grootste beveiligingsrisico in een gefragmenteerde AI-stack?

Een gedeeld, niet-gescoped inloggegeven — vaak een database service-role-sleutel of een API-token — hergebruikt over meerdere tools zonder juiste toegangsgrenzen. Omdat de tools onafhankelijk van elkaar zijn gebouwd, controleert meestal niemand of de component met de laagste beveiliging (vaak een publieke marketingsite) toegang heeft tot dezelfde inloggegevens als het kernproduct, wat betekent dat het compromitteren van de zwakste schakel alles erachter kan blootleggen.

### Betekent het consolideren van een gefragmenteerde stack dat alles wordt herbouwd tot één applicatie?

Nee, en dat is meestal de verkeerde aanpak. Consolidatie betekent doorgaans het vaststellen van één gezaghebbende datalaag en het afdwingen van juiste authenticatie- en autorisatiegrenzen tussen de bestaande frontends, niet het samenvoegen van vier afzonderlijke interfaces die elk al goed functioneren voor hun doel tot één herbouwde applicatie.

### Hoe lang duurt het om een gefragmenteerde multi-tool-stack te auditen en consolideren?

Voor een scope vergelijkbaar met die van LedgerPilot — vier tools, drie databases, één niet-geauthenticeerde interne API — is een engagement van twee tot drie weken (ruwweg 15-20 werkdagen) realistisch, mits het werk begint met een volledige architectuuraudit voordat er herstel plaatsvindt, zodat reparaties het volledige beeld aanpakken in plaats van alleen de reeds bekende problemen.

### Welke triggers dwingen een oprichter meestal om te ontdekken dat hun stack gefragmenteerd is?

De meest voorkomende triggers zijn due diligence bij een overname, de beveiligingsvragenlijst van een enterprise-klant, een compliance-audit zoals SOC 2-voorbereiding, of het aannemen van een technische medeoprichter of CTO die voor het eerst vraagt om het architectuurdiagram te zien. In vrijwel elk geval was de fragmentatie er al — de trigger dwingt alleen iemand om er direct naar te kijken.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe raakt een product in eerste instantie gefragmenteerd over meerdere AI-builders?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dit gebeurt meestal geleidelijk en redelijk: een oprichter gebruikt welke tool dan ook het snelst is voor elke nieuwe behoefte — een dashboard in de ene builder, een marketingsite in een andere, een admintool van een derde — omdat het herbouwen van een bestaand oppervlak om één nieuwe feature toe te voegen trager aanvoelt dan iets nieuws opzetten. Elke individuele beslissing is verstandig; de fragmentatie wordt pas zichtbaar zodra iemand ineens om het volledige beeld vraagt."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het grootste beveiligingsrisico in een gefragmenteerde AI-stack?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een gedeeld, niet-gescoped inloggegeven — vaak een database service-role-sleutel of een API-token — hergebruikt over meerdere tools zonder juiste toegangsgrenzen. Omdat de tools onafhankelijk van elkaar zijn gebouwd, controleert meestal niemand of de component met de laagste beveiliging (vaak een publieke marketingsite) toegang heeft tot dezelfde inloggegevens als het kernproduct, wat betekent dat het compromitteren van de zwakste schakel alles erachter kan blootleggen."
      }
    },
    {
      "@type": "Question",
      "name": "Betekent het consolideren van een gefragmenteerde stack dat alles wordt herbouwd tot één applicatie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, en dat is meestal de verkeerde aanpak. Consolidatie betekent doorgaans het vaststellen van één gezaghebbende datalaag en het afdwingen van juiste authenticatie- en autorisatiegrenzen tussen de bestaande frontends, niet het samenvoegen van vier afzonderlijke interfaces die elk al goed functioneren voor hun doel tot één herbouwde applicatie."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt het om een gefragmenteerde multi-tool-stack te auditen en consolideren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor een scope vergelijkbaar met die van LedgerPilot — vier tools, drie databases, één niet-geauthenticeerde interne API — is een engagement van twee tot drie weken (ruwweg 15-20 werkdagen) realistisch, mits het werk begint met een volledige architectuuraudit voordat er herstel plaatsvindt, zodat reparaties het volledige beeld aanpakken in plaats van alleen de reeds bekende problemen."
      }
    },
    {
      "@type": "Question",
      "name": "Welke triggers dwingen een oprichter meestal om te ontdekken dat hun stack gefragmenteerd is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De meest voorkomende triggers zijn due diligence bij een overname, de beveiligingsvragenlijst van een enterprise-klant, een compliance-audit zoals SOC 2-voorbereiding, of het aannemen van een technische medeoprichter of CTO die voor het eerst vraagt om het architectuurdiagram te zien. In vrijwel elk geval was de fragmentatie er al — de trigger dwingt alleen iemand om er direct naar te kijken."
      }
    }
  ]
}
</script>
