---
Titel: "Het AI-Prototype van een Klant Scopen Vóórdat U Offerte Uitbrengt"
Trefwoorden: AI-prototype scopen, Lovable prototype audit, Bolt app scope checklist, technische due diligence bureau, klant softwareontwikkeling offreren, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Bureau / Freelancer (White-Label Partner)
---

# Het AI-Prototype van een Klant Scopen Vóórdat U Offerte Uitbrengt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Het AI-Prototype van een Klant Scopen Vóórdat U Offerte Uitbrengt",
  "description": "Een Lovable- of Bolt-prototype van een klant offreren zonder gestructureerde technische scoping is dé manier waarop bureaus verlies draaien op fixed-price projecten. Een concrete checklist vóórdat u zich vastlegt op een bedrag.",
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
  "datePublished": "2027-01-08",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/het-ai-prototype-van-een-klant-scopen-voordat-u-offerte-uitbrengt"
  }
}
</script>

De link naar het Lovable-project van uw klant belandt donderdagmiddag om 16:50 uur in uw inbox met het verzoek: "Kun je voor maandag een prijsopgave doorgeven?" U klikt erop. De demo oogt oprecht indrukwekkend: een strakke interface, een werkende registratieflow en een dashboard gevuld met overtuigende data. Veertig minuten later sluit u het tabblad zonder een offerte te hebben opgesteld. Die veertig minuten waren namelijk genoeg om te ontdekken dat de "werkende" registratie e-mailadressen niet verifieert, de dashboarddata op drie van de vijf schermen statisch is 'hardcoded' in plaats van dynamisch opgehaald, en er nergens een herkenbaar databaseschema te bekennen is zonder toegang tot de broncode. De demo liet u zien wat de klant ziet. Het vertelde u vrijwel niets over wat u daadwerkelijk zou moeten bouwen.

Dit is de valkuil waar bureaus bij vaste prijsafspraken voor white-label software het vaakst intrappen: offreren op basis van een visuele demo in plaats van een gestructureerde technische scoping. De demo is wat u ziet, terwijl een grondige scope-analyse een uur vergt dat u op donderdagmiddag eigenlijk niet heeft. Bureaus die stoppen met verlies draaien op dit soort projecten, maken van dat uur een niet-onderhandelbare vaste stap in elk offerteproces.

## Waarom de Demo U Misleidt

Een door AI gegenereerd prototype is ontworpen om fantastisch te demonstreren. Dat is geen kritiek, het is simpelweg de prikkelstructuur van razendsnel bouwen met tools als Lovable, Bolt of v0. De zichtbare laag — datgene waar een opdrachtgever in een presentatie van vijf minuten doorheen klikt — is vrijwel altijd het meest complete onderdeel van de hele applicatie. De zaken die niet direct zichtbaar zijn in een demo — server-side autorisatiecontroles, datavalidatie, foutafhandeling voor randgevallen en een databaseschema dat bestand is tegen gelijktijdige gebruikers — zijn daarentegen flinterdun of ontbreken volledig. Dit verklaart tevens waarom veel AI-gegenereerde code aanzienlijke beveiligingslekken bevat: de hiaten zitten precies in de lagen die een visuele demo niet test.

Offreren op basis van de demo betekent offreren op de 20% van de software die daadwerkelijk af is, om vervolgens de overige 80% halverwege het project te ontdekken — tegen een vaste prijs die u al zwart-op-wit heeft toegezegd. Dit is de voornaamste reden waarom een 'fixed-price' white-label opdracht in de praktijk verandert in een onbetaalde urenput die uw complete marge opvreet.

## De Scoping-Checklist: Wat U Moet Controleren Vóór U Offerte Uitbrengt

Doorloop deze stappen in vaste volgorde. Beschouw elk "nee" of "onduidelijk" als een signaal dat de scope groter is, niet als een detail dat later wel wordt opgelost:

1. **Authenticatie daadwerkelijk testen.** Verifieert de registratie het e-mailadres, of accepteert het systeem elke willekeurige tekenreeks? Werkt het herstellen van wachtwoorden, of is het een knop zonder functie? Maak twee afzonderlijke accounts aan en controleer of de data strikt gescheiden blijft — een verbijsterend veelvoorkomend probleem is een dashboard dat aan elke ingelogde gebruiker dezelfde mock-data toont.
2. **Server-side autorisatie, niet alleen visueel verbergen in de UI.** Een prototype dat een beheerpaneel in de navigatie verbergt voor gewone gebruikers, is iets heel anders dan een systeem dat ongeautoriseerde toegang tot de achterliggende API-endpoints blokkeert. Typ als gewone gebruiker rechtstreeks de beheer-URL in. Laadt de pagina of data alsnog? Dan bestaat uw beveiliging alleen aan de voorkant — wat technisch betekent dat er géén beveiliging is.
3. **Databaseschema en data-integriteit.** Vraag leestoegang tot de database (Supabase, Firebase of wat de AI-tool ook heeft aangemaakt). Controleer of er sprake is van een doordachte relationele structuur of een platte, ongestructureerde dump. Blijft data bewaard na het uitloggen? En wat gebeurt er als twee gebruikers tegelijkertijd gerelateerde gegevens bewerken?
4. **Gereedheid voor betalingen.** Is er een werkende Stripe- of Mollie-koppeling die testtransacties verwerkt, of slechts een visuele mockup van een afrekenpagina zonder achterliggende logica? Dit verschil alleen al kan een offerte met duizenden euro's verschuiven.
5. **Wat is statisch en wat is dynamisch?** Klik door elk scherm met gegevens en vraag uzelf af: "Als ik de data in het backend aanpas en de pagina vernieuw, verandert dit scherm dan mee?" AI-tools laten vaak tijdelijke data achter in componenten die dynamisch lijken maar het niet zijn. Klanten hebben dit vaak zelf niet door.
6. **Configuratie van externe diensten.** Controleer of API-sleutels, omgevingsvariabelen en externe diensten (zoals transactionele e-mails of bestandsopslag) zijn ingericht voor productie, of dat het sandbox-instellingen betreft die vanaf de grond opnieuw moeten worden geconfigureerd.
7. **Toegangsrechten van de klant.** Ga na of de klant zelf eigenaar is van de accounts (het Lovable- of Bolt-project, de hosting en databases), of dat er is gebouwd op een proefaccount dat eerst moet worden gemigreerd. Een datamigratie is reëel meerwerk dat u niet over het hoofd mag zien.

## Bevindingen Vertalen naar een Definitief Bedrag

Elk gat op bovenstaande checklist valt binnen een duidelijke scope-categorie. Dit geeft u de input om het project realistisch te begroten in plaats van te gokken.

Een prototype met solide authenticatie, betrouwbare data-opslag en enkel een ontbrekende betaalkoppeling en hosting-hardening past uitstekend binnen het **Launch Ready**-pakket van €800 tot €3.500. Bevat het prototype daarentegen enkel UI-autorisatie, hardcoded data en ontbreekt de bedrijfslogica achter cruciale flows? Dan spreken we over een substantieel ontwikkeltraject dat valt binnen **Launch & Grow** (€2.500 tot €7.500+) of meer. Het grote voordeel van een scoping pass is dat u dit weet vóórdat u uw handtekening zet, in plaats van in week twee van de bouw.

Bespreek dit openhartig met uw klant: *"De registratieflow en het dashboard zien er fantastisch uit en zijn goed bruikbaar, maar de betaalstraat en de rechtenstructuur voor beheerders moeten vanaf de basis worden opgebouwd. Dat vraagt meer uren dan de visuele demo op het eerste gezicht doet vermoeden."* Dit kost u niets om te zeggen en behoedt u voor een wurgcontract.

## Rode Vlaggen Die Scope Niet Gewoon Vergroten, Maar Vermenigvuldigen

Sommige checklist-punten leveren een helder, afgebakend brok werk op: een ontbrekende Stripe-integratie heeft een voorspelbare doorlooptijd. Andere bevindingen zijn gevaarlijker: ze wijzen erop dat de complete basisarchitectuur wankelt. Behandel deze signalen als multipliers (vermenigvuldigers) in plaats van losse urenposten:

- **Inconsistente patronen tussen vergelijkbare functies:** Heeft de registratie wel degelijke servervalidatie, maar het wijzigen van het wachtwoord niet? Dan is er door de AI geen consistente standaard gehanteerd. U moet ervan uitgaan dat elke andere functie dezelfde gebreken vertoont.
- **Een klant die geen antwoord kan geven op hun eigen datamodel:** Niet uit desinteresse, maar omdat het schema blindelings via AI-prompts is gegenereerd. Het ontwarren van per ongeluk ontstane datastructuren kost meer tijd dan het bouwen van een schone architectuur vanaf een heldere specificatie.
- **Prototypes die met meerdere tools aan elkaar zijn geplakt:** Een frontend uit Lovable die gekoppeld is aan een backend uit Bolt. De naden tussen verschillende tools zijn precies de plekken waar standaard ureninschattingen falen; het lijmwerk kost vaak meer dan de onderdelen zelf.

Noteer deze vermenigvuldigers direct in uw scopingverslag en bouw een veiligheidsmarge in. Een klant begrijpt een hogere begroting vooraf veel beter dan een onverwachte meerwerkfactuur achteraf.

## Leg Bevindingen Schriftelijk Vast

De scoping pass dient nog een tweede doel: het levert u de exacte bewoordingen op om uw prijsvoorstel te onderbouwen. Zeggen dat "het ingewikkelder bleek dan verwacht" klinkt zwak. Zeggen dat "de afrekenpagina in de demo nog niet gekoppeld is aan een betaalprovider en de exportfunctie voor klantgegevens momenteel voor iedere bezoeker toegankelijk is", getuigt van professioneel inzicht.

Noteer uw bevindingen in heldere taal. Deze documentatie vormt het fundament van uw offerte én dient als referentiekader wanneer de klant later vraagt waarom bepaalde stappen noodzakelijk waren.

## Wie Voert de Scoping Pass Daadwerkelijk Uit?

Voor bureaus zonder diepgaande interne backend-kennis is dit exact de taak die u wilt neerleggen bij een technische partner vóórdat u een offerte uitbrengt. Het verschil tussen een vluchtige blik door een ontwerper en een software-engineer die de repository inspecteert en de API-rechten test, is het verschil tussen een wilde gok en een waterdichte scope.

Een korte scoping-analyse met een gespecialiseerde partner zoals LaunchStudio kost een fractie van wat een verkeerd ingeschatte vaste prijs u kost aan onbetaald overwerk. Bovendien geeft het u een verdedigbaar, exact getal voor uw klant.

[LaunchStudio](https://launchstudio.eu/nl/) hanteert deze scoping pass als vaste eerste stap voor elk traject, ondersteund door [Manifera's 11+ jaar ervaring in het omzetten van prototypes naar schaalbare productiesoftware](https://www.manifera.com/about-us/manifera-technologies/). Onze engineers openen de codebase en controleren wat er werkelijk staat vóórdat er een offerte uitgaat.

Stuur ons de link van het prototype vóórdat u uw klant offrereert — [ontvang binnen één werkdag gratis scoping-feedback](https://launchstudio.eu/nl/#contact), zodat uw offerte gebaseerd is op de werkelijkheid en niet op de schijn van een demo.

## Praktijkvoorbeeld

### Studio Bakker: De Offerte Die Bijna Fout Ging

Sanne Bakker runt een digitaal ontwerpbureau in Groningen. Ze stond op het punt een offerte van €1.800 uit te brengen voor een abonnementsplatform dat een klant in Bolt had gebouwd. De vijftien minuten durende demo zag er immers nagenoeg productierijp uit. Op het laatste moment besloot ze de link eerst voor te leggen aan LaunchStudio voor een snelle technische controle.

Tijdens de scoping-sessie bleek dat de getoonde abonnementsbetalingen puur visuele mockups waren zonder achterliggende Stripe-logica. Erger nog: de exportfunctie voor klantdata in het dashboard bevatte geen enkele server-side autorisatiecontrole. Iedere ingelogde gebruiker kon via het directe endpoint met één klik de persoonsgegevens van alle andere klanten downloaden.

**Resultaat:** Sanne bracht een herziene offerte uit van €4.200, waarbij ze de specifieke technische en beveiligingsrisico's helder toelichtte aan haar klant. De opdrachtgever was enorm opgelucht dat deze kritieke datalekken tijdig werden opgemerkt en ging zonder onderhandeling akkoord met het hogere bedrag.

> *"Als ik op basis van de demo had geoffreerd, had ik €2.400 aan onvoorziene uren moeten slikken of halverwege moeten melden dat het duurder werd. Geen van beide scenario's is goed voor je bureau."*
> — **Sanne Bakker, Oprichter, Studio Bakker (Groningen)**

## Veelgestelde Vragen

### Hoe lang duurt een grondige technische scoping-sessie eigenlijk?

Een gerichte scoping pass — waarbij authenticatie, autorisatiemodellen, data-integriteit en betaalstromen worden onderzocht — duurt doorgaans 30 tot 90 minuten voor een engineer met directe toegang tot de codebase en backend.

### Wat als de klant geen toegang wil geven tot de repository of het backend vóór de offerte?

Beschouw dit als een serieus waarschuwingssignaal. Een klant die weigert de benodigde toegang te verlenen voor een accurate inschatting, vraagt u in feite om blindelings een financieel risico aan te gaan op basis van onvolledige informatie.

### Kan ik deze checklist zelf doorlopen zonder technische achtergrond?

Sommige onderdelen wel, zoals controleren of data statisch is door pagina's te verversen of doorvragen naar de status van de betaalkoppeling. Het controleren van server-side API-autorisaties of databaseschema's vereist echter inhoudelijke kennis van backend-architectuur.

### Wat kost een scoping pass en wie betaalt daarvoor?

Veel professionele technische partners, waaronder LaunchStudio, bieden een eerste scoping-check kosteloos aan als onderdeel van het offerteproces, omdat dit tevens de basis vormt voor hun eigen vaste prijs. Voor zeer complexe of omvangrijke applicaties is een betaald voortraject gebruikelijk als afzonderlijke adviespost.

### Wat is de allergrootste scoping-fout die bureaus maken?

Offreren op basis van een visuele klikdemo van de klant in plaats van een diepgaande technische inspectie van de broncode. De demo toont de 20% die er goed uitziet, terwijl de offerte bindend wordt vóórdat iemand de ontbrekende 80% onder de motorkap heeft gecontroleerd.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe lang duurt een grondige technische scoping-sessie eigenlijk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een gerichte scoping pass voor authenticatie, autorisatie, data-integriteit en betaalstromen duurt doorgaans 30 tot 90 minuten voor een engineer met directe toegang tot de codebase."
      }
    },
    {
      "@type": "Question",
      "name": "Wat als de klant geen toegang wil geven tot de repository of het backend vóór de offerte?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Beschouw dit als een serieus waarschuwingssignaal. Een klant die weigert de benodigde toegang te verlenen vraagt u om blindelings een financieel risico te nemen op basis van onvolledige data."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik deze checklist zelf doorlopen zonder technische achtergrond?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Oppervlakkige zaken zoals statische data ontdekken lukt prima, maar het verifiëren van server-side autorisaties en databaseschema's vereist directe inspectie door een backend-specialist."
      }
    },
    {
      "@type": "Question",
      "name": "Wat kost een scoping pass en wie betaalt daarvoor?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een initiële scoping review is bij LaunchStudio kosteloos als onderdeel van de vaste prijsopgave. Voor grootschalige systemen is een betaald technisch vooronderzoek een logische aparte offertepost."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de allergrootste scoping-fout die bureaus maken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Offreren op basis van een visuele klikdemo in plaats van een technische inspectie. Men bindt zich aan een vaste prijs op de 20% die af is, terwijl de ontbrekende 80% pas tijdens de bouw opduikt."
      }
    }
  ]
}
</script>
