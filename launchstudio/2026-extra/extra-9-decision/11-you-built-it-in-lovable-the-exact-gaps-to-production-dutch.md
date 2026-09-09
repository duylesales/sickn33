---
Titel: "U Heeft Het Gebouwd in Lovable: De Exacte Kloven Tussen Uw Prototype en Productie"
Trefwoorden: Lovable prototype productie, Lovable Supabase beveiliging, Lovable app lanceren, AI prototype tekortkomingen, row level security, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# U Heeft Het Gebouwd in Lovable: De Exacte Kloven Tussen Uw Prototype en Productie

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "U Heeft Het Gebouwd in Lovable: De Exacte Kloven Tussen Uw Prototype en Productie",
  "description": "Een helder overzicht in begrijpelijke taal van wat Lovable daadwerkelijk voor u bouwt en wat het overlaat aan specialisten, zodat een niet-technische oprichter het verschil ziet tussen een werkende demo en een veilige, betaalde applicatie. Behandelt databaserechten, server-side validatie, betaalwebhooks, hosting en back-ups.",
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
  "datePublished": "2027-01-04",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/u-heeft-het-gebouwd-in-lovable-de-exacte-kloven-naar-productie"
  }
}
</script>

Wat ontbreekt er nu daadwerkelijk? U heeft een werkende Lovable-applicatie. Gebruikers kunnen zich registreren, inloggen, projecten aanmaken, overzichten bekijken en op een knop 'Upgraden' klikken. Uw vrienden en kennissen hebben het getest. Niets liep vast. En toch trekt elke softwareontwikkelaar aan wie u het laat zien een bedenkelijk gezicht en mompelt iets vaags over "dat het nog niet gereed is voor productie", zonder ooit concreet te benoemen welk onderdeel dan rammelt.

Die vaagheid is het werkelijke struikelblok. U kunt immers geen weloverwogen beslissing nemen over een investering van € 1.000 of € 4.000 in technische verbeteringen als niemand u precies vertelt wat er mis is. Daarom benoemt dit artikel de feiten klip-en-klaar. Hieronder vindt u een gedetailleerd overzicht van wat Lovable uitstekend bouwt, wat het slechts gedeeltelijk opzet en wat het volledig achterwege laat — beschreven in heldere taal, gerangschikt op prioriteit voor een oprichter die op het punt staat echt geld van echte klanten te innen. Ongeveer 80% van de met behulp van AI gebouwde softwareprojecten haalt nooit de productiefase. Uit onze ervaring blijkt dat dit vrijwel nooit ligt aan een gebrek aan toewijding van de oprichter; het komt doordat niemand hen ooit deze checklist heeft overhandigd.

## Wat Lovable écht bouwt — en uitstekend doet

Laten we beginnen met een eerlijke waardering voor de tool, want die verdient Lovable absoluut. Lovable levert een volwaardige React-frontend op met een solide componentenstructuur, doordachte styling en functionerende navigatieroutes. Dit is geen statisch wireframe of een klikbaar plaatje van een applicatie. Het is daadwerkelijke broncode die een professionele software-engineer direct kan openen, doorgronden en uitbreiden. Het is vaak zelfs netter geschreven dan de haastige code van een junior ontwikkelaar onder tijdsdruk.

Ook aan de backend levert de tool waardevol werk: het koppelt uw project rechtstreeks aan Supabase en genereert automatisch uw tabellen. Wanneer u de prompt gaf "gebruikers moeten hun projecten kunnen opslaan", creëerde Lovable een `projects`-tabel met de benodigde kolommen, koppelde de registratie- en inlogschermen daaraan en zorgde ervoor dat het dashboardoverzicht netjes uit die tabel leest. Uw gegevens belanden daadwerkelijk in een echte PostgreSQL-database en niet vluchtig in het browsergeheugen. Dat is aanzienlijke vooruitgang en exact de reden waarom uw prototype zo compleet aanvoelt.

Het cruciale onderscheid is echter dit: Lovable is buitengewoon bedreven in het bouwen van de softwareonderdelen die u met het blote oog kunt zien, maar schiet tekort in de onderdelen die onzichtbaar blijven. Alles wat we in de onderstaande paragrafen bespreken, bevindt zich in die onzichtbare onderstroom. Dat is exact de reden waarom niet-technische oprichters deze risico's over het hoofd zien — niet uit nalatigheid, maar simpelweg omdat er op het beeldscherm niets te zien is dat doet vermoeden dat er iets ontbreekt.

## Kloof één: uw database geeft gegevens aan iedereen die er netjes om vraagt

Dit is zonder twijfel de meest voorkomende bevinding wanneer wij een Lovable-project aan een technische audit onderwerpen, en het is essentieel om dit concept te begrijpen, zelfs als u zelf nooit een regel code schrijft.

Supabase communiceert rechtstreeks vanuit de webbrowser van de bezoeker met uw database. Dat is een bewuste architectuurkeuze en op zichzelf volkomen legitiem — maar het betekent wel dat uw beveiligingsregels niet in uw schermen kunnen worden opgeslagen. Ze moeten diep in de database zelf worden verankerd via een mechanisme dat Row Level Security (RLS) heet. RLS is de dwingende regel die dicteert: "een bezoeker mag uitsluitend rijen in deze tabel inzien waarin de eigenaarskolom exact overeenkomt met diens eigen gebruikers-ID."

Lovable maakt tabellen echter vaak aan zonder dat deze regels worden ingeschakeld, of gebruikt een tijdelijke standaardregel die in feite neerkomt op "iedereen heeft toegang". Uw applicatie lijkt volkomen veilig, omdat uw dashboardscherm braaf uitsluitend uw eigen gegevens *opvraagt*. Maar de onderliggende database heeft nooit de instructie gekregen om andere verzoeken te weigeren. Iedereen die de ontwikkelaarstools van zijn browser opent, het webadres achterhaalt dat uw app aanroept en één parameter aanpast, kan zodoende elke rij in die tabel opvragen: e-mailadressen van alle klanten, opgeslagen vertrouwelijke documenten, facturen en klantprofielen.

De lakmoestest is niet "kan ik andermans gegevens zien in mijn eigen dashboard". De echte test luidt: "wat gebeurt er wanneer iemand rechtstreeks een verzoek indient bij de database." In een Supabase-project kunt u dit eenvoudig zelf controleren: open de Table Editor en controleer het RLS-label bij elke tabel. Elke tabel met klantgegevens waarop staat dat RLS is uitgeschakeld ('Disabled'), functioneert in feite als een openstaande archiefkast op straat. Een senior engineer heeft slechts enkele minuten nodig om dit vast te stellen en een paar uur om het beleid waterdicht te configureren — mits diegene exact begrijpt waarvoor elke tabel dient, want een verkeerd ingesteld beveiligingsbeleid lekt gegevens óf blokkeert uw hele applicatie.

## Kloof twee: de regels die u op het scherm ziet zijn suggesties, geen wetten

Uw registratieformulier vereist een geldig e-mailadres. Uw upgradepagina schermt het Pro-dashboard af voor gratis accounts. Uw bestelformulier weigert aantallen boven de 50 stuks.

Al deze controles draaien hoogstwaarschijnlijk uitsluitend in uw React-code — wat betekent dat ze worden uitgevoerd in de browser op de computer van de bezoeker. Iedere bezoeker kan deze controles eenvoudig uitschakelen. Daar is geen geavanceerde hacker voor nodig: een alerte tiener kan met de inspectietool van de browser bekijken welk netwerkverzoek uw app verstuurt bij het opslaan van een formulier, en vervolgens exact hetzelfde verzoek handmatig opnieuw versturen met gewijzigde waarden. Een bestelhoeveelheid van -5. Een prijs van € 0,01. Of een veld `role` dat handmatig op `admin` wordt gezet.

Dit is het fundamentele verschil tussen client-side (browser) en server-side (server) validatie, en het is iets wat de meeste niet-technische oprichters nooit duidelijk is uitgelegd. Controles aan de voorkant dienen puur het *gebruiksgemak* — de gebruiker waarschuwen dat hij het apenstaartje in zijn e-mailadres is vergeten vóórdat hij klikt. De daadwerkelijke, onwrikbare controles moeten plaatsvinden op een plek waar de bezoeker geen enkele toegang toe heeft: in een Supabase Edge Function, via database-constraints of door middel van serverregels die manipulatie structureel onmogelijk maken.

Een praktische manier om uw eigen risico in kaart te brengen: noteer elk veld in uw applicatie waarvan de inhoud financiële of functionele gevolgen heeft — prijzen, aantallen, abonnementsniveaus, gebruikersrollen, beschikbare tegoeden en kortingscodes. Voor elk van deze velden is een controle vereist die gegarandeerd op de server draait. Kunt u niet exact aanwijzen waar die servercontrole plaatsvindt, dan bestaat deze simpelweg nog niet.

## Kloof drie: de betaling die succesvol lijkt maar nooit is bevestigd

Als u Stripe of Mollie aan uw Lovable-project heeft toegevoegd, werkt de betaalstroom vrijwel zeker als volgt: de gebruiker klikt op 'Afrekenen', wordt doorgestuurd naar de gehoste betaalpagina, rekent af, keert via een doorverwijzing (redirect) terug op een pagina die zegt "Hartelijk dank!", en uw applicatie markeert het account op dat exacte moment als betalende klant.

Die terugsturende URL is echter geen betalingsbewijs. Het is louter een internetadres waar een browser op is geland. Een bezoeker kan die URL opslaan als bladwijzer, direct intypen of raden. Omgekeerd kan een betaling bij de bank vlekkeloos slagen terwijl de terugverwijzing mislukt — bijvoorbeeld door een wegvallende internetverbinding in de trein — waardoor uw klant daadwerkelijk heeft betaald, terwijl uw database blijft denken dat het een gratis account betreft. U merkt dat pas wanneer die klant zich geïrriteerd bij uw helpdesk meldt.

Het enige betrouwbare mechanisme hiervoor is een webhook: de betaalprovider stuurt rechtstreeks een versleuteld bericht van server naar server met de mededeling "betalingskenmerk XYZ is succesvol voldaan", voorzien van een cryptografische handtekening die bewijst dat het bericht daadwerkelijk van Stripe of Mollie afkomstig is en niet is nagemaakt. Het valideren van die handtekening is een verplichte beveiligingsstap, maar deze ontbreekt standaard in door AI gegenereerde betaalintegraties. Zonder die controle kan iedereen die het adres van uw webhook achterhaalt een vals bericht sturen en zichzelf gratis toegang verlenen tot uw betaalde diensten.

De andere zijde van deze kloof betreft wat er gebeurt *na* de initiële transactie: automatische abonnementsverlengingen, mislukte incasso's, opzeggingen, terugbetalingen en de officiële facturen die uw boekhouder nodig heeft. Al deze gebeurtenissen worden als webhook-events verstuurd. Als uw backend hier niet actief naar luistert, loopt de status in uw applicatie onvermijdelijk uit de pas met de werkelijkheid bij uw betalingsverwerker.

## Kloof vier: iedereen kan inloggen, maar niemand controleert wie wat mag doen

Lovable implementeert authenticatie — het inlogproces — over het algemeen prima. E-mail en wachtwoord, magic links en vaak zelfs inloggen met Google functioneren naar behoren.

Autorisatie is echter een wezenlijk ander vraagstuk, en dat ontbreekt vrijwel altijd. Authenticatie beantwoordt de vraag: "wie bent u?". Autorisatie beantwoordt de vraag: "heeft u het recht om deze specifieke handeling uit te voeren op dít specifieke record?". Een prototype dat wel beschikt over inlogfunctionaliteit maar geen autorisatiestructuur kent, stelt een ingelogde klant in staat om de URL van `/factuur/1042` aan te passen naar `/factuur/1041` en zodoende de privégegevens van een andere klant in te zien. Die gebruiker is netjes ingelogd met zijn eigen account, maar bekijkt andermans data omdat de software nergens verifieert: "is deze factuur wel gekoppeld aan de ingelogde gebruiker?".

Zodra uw product concepten bevat zoals teams, werkruimtes, organisaties of beheerdersrechten, escaleert dit risico razendsnel. De vraag die u zichzelf moet stellen bij elk scherm dat een specifiek record toont: wat weerhoudt een aangemelde gebruiker ervan om een ander ID in de browserbalk in te typen? Als het eerlijke antwoord luidt "daar zouden ze toch niet aan denken", dan heeft u op dit moment geen beveiliging.

## Kloof vijf: niemand bewaart een back-up van de gegevens van uw klanten

Lovable configureert geen automatische reservekopieën, simpelweg omdat back-ups geen taak zijn voor een codegenerator — het is een operationele beslissing. Op het gratis instapniveau van Supabase moet u ervan uitgaan dat er geen herstelpunten beschikbaar zijn bij calamiteiten. Pas op betaalde niveaus beschikt u over dagelijkse back-ups, en hogere abonnementen bieden point-in-time recovery, waarmee u de database kunt terugdraaien naar exact 15:14 uur op het moment dat een storing optrad.

Daarnaast is er een verwante tekortkoming die meer impact heeft dan menigeen vermoedt: databasemigraties (schema migrations). Wanneer u Lovable vraagt om een extra veld toe te voegen, of wanneer u handmatig een kolom toevoegt in het Supabase-dashboard, wordt die wijziging nergens vastgelegd als een reproduceerbaar migratiescript met versienummering. Dat betekent dat er geen betrouwbare manier is om uw databasestructuur vanaf nul opnieuw op te bouwen, geen manier om een identieke testomgeving (staging) op te zetten en geen optie om een foutieve wijziging geautomatiseerd terug te draaien. Op de dag dat u een testomgeving wilt inrichten om een risicovolle update uit te proberen, ontdekt u dat de enige blauwdruk van uw database de live productieomgeving is waar uw betalende klanten op werken.

## Kloof zes: een preview-link is geen productiehosting

Uw prototype draait momenteel waarschijnlijk op een subdomein zoals `uwproject.lovable.app`. Dat is een uitstekende preview-omgeving om uw idee te tonen aan een zakenpartner, maar volstrekt ongeschikt om op een officiële factuur te vermelden.

Een professionele livegang vereist concrete infrastructurele stappen: uw eigen domeinnaam met correct geconfigureerde DNS-records, een automatisch vernieuwend SSL/HTTPS-certificaat, een afgeschermde productieomgeving die losstaat van de omgeving waarin u prompts uitprobeert, en — uiterst belangrijk — e-mailbezorging die aankomt. Dat laatste punt verrast menig oprichter. Het versturen van transactionele e-mails (wachtwoordherstel, facturen, bevestigingen) vanaf een nieuw domein zonder juiste configuratie van SPF-, DKIM- en DMARC-records leidt ertoe dat een groot deel van uw berichten rechtstreeks in de spambox belandt. Oprichters verliezen hierdoor wekenlang nieuwe gebruikers en wijten dat ten onrechte aan hun marketing.

Voeg daar centrale foutmonitoring (error monitoring) aan toe. Als een klant op zaterdagavond om 22:00 uur tegen een foutmelding aanloopt, is de enige manier waarop u dat momenteel ontdekt wanneer die klant de moeite neemt om u een boze e-mail te sturen. De meesten doen dat niet; ze haken geruisloos af.

## Waar deze checklist daadwerkelijk voor dient

Dit alles betekent geenszins dat bouwen met Lovable een verkeerde keuze was. Het zelf bouwen van uw interface binnen enkele dagen tegen minimale kosten is een enorm strategisch voordeel. Het betekent dat het specialistische, kostbare engineeringwerk nu is teruggebracht tot een scherp afgebakende taak, in plaats van een openstaand project om vanaf nul een applicatie te programmeren. Dat is exact het fundament onder [LaunchStudio](https://launchstudio.eu/nl/): behoud de interface die u zelf heeft ontworpen, laat ons de zes bovenstaande infrastructurele gaten dichten en lanceer veilig. De typische doorlooptijd voor een Lovable-applicatie in deze fase valt binnen het Launch Ready-pakket van € 800 tot € 3.500 en vergt één tot drie weken, waarbij alle code te allen tijde uw exclusieve eigendom blijft binnen uw eigen accounts. De engineers die dit uitvoeren zijn afkomstig van [Manifera](https://www.manifera.com/about-us/), een organisatie die al meer dan elf jaar complexe en veilige productiesoftware levert aan enterprise-klanten — dezelfde senior expertise, toegepast op een compact en snel traject.

Druk deze checklist af en leg hem naast uw eigen applicatie. Wat uw volgende stap ook wordt: u kent nu de exacte namen van de obstakels die tussen uw prototype en een verkoopklaar product in staan.

Stuur ons de link naar uw Lovable-project en wij vertellen u exact welke van deze zes kloven in uw codebase aanwezig zijn — kosteloos, vrijblijvend en met een eerlijk antwoord binnen één werkdag.

## Echt voorbeeld

### Een oprichter ontdekt wat er onder de motorkap van haar prototype ontbrak

Sanne Vermeulen, een loopbaancoach in Utrecht, ontwikkelde met Lovable gedurende zes weekenden Loopbaanlab: een beveiligd platform waarin coaches cliëntnotities, opnames van sessies en persoonlijke ontwikkelplannen beheren. Ze had al elf collega-coaches bereid gevonden om € 29 per maand te betalen en de officiële lanceringsdatum stond al aangekondigd op LinkedIn.

Onze technische review bracht drie van de zes bovenstaande risico's aan het licht. RLS bleek volledig uitgeschakeld op de tabel `client_notes`, waardoor elke aangemelde coach rechtstreeks via de browser de vertrouwelijke aantekeningen van andere coaches kon opvragen. De controle die Pro-functies afschermde, draaide uitsluitend in de lokale React-code. En de Stripe-integratie kende gebruikers een betaald account toe op basis van een eenvoudige URL-doorverwijzing zonder actieve webhook-validatie — waardoor een bezoeker wiens betaling mislukte maar die toch de dankpagina wist te laden, gratis een Pro-account kreeg. Het verhelpen van deze drie gebreken en het overzetten naar haar eigen domein met sluitende e-mailrecords vergde acht werkdagen.

**Resultaat:** Loopbaanlab ging live met waterdichte data-isolatie op databaseniveau tussen coaches onderling, server-side validatie van abonnementsrechten en cryptografisch beveiligde Stripe-webhooks voor automatische verwerking van betalingen, annuleringen en storneringen — terwijl de interface die Sanne zelf had gebouwd voor 100% intact bleef.

> *"Ik vroeg voortdurend aan bekenden 'is het zo veilig?', maar kreeg telkens vage antwoorden. Op het moment dat een engineer mij de daadwerkelijke databasetabel liet zien waarop alle beveiliging uitstond, begreep ik binnen tien seconden waarom ik niet live kon. Ik had bijna vertrouwelijke cliëntendossiers opgeslagen in een digitale archiefkast zonder slot."*
> — **Sanne Vermeulen, Oprichter, Loopbaanlab (Utrecht)**

**Kosten & Doorlooptijd:** € 2.400 (Launch Ready Pakket) — volledig live binnen 8 werkdagen.

---

## Veelgestelde Vragen

### Kan ik het ontbreken van Row Level Security zelf controleren zonder technische kennis?

Ja, grotendeels wel. Open uw Supabase-omgeving, navigeer naar de Table Editor en bekijk per tabel of het label 'RLS' op groen of ingeschakeld staat. Elke tabel met persoonsgegevens of klantdata waar RLS op 'Disabled' staat, vormt een acuut beveiligingslek. Wat u zonder technische achtergrond niet zelfstandig kunt beoordelen, is of een *ingeschakeld* beleid ook daadwerkelijk correct is geformuleerd; een beleidsregel die technisch gezien iedereen toelaat telt immers ook als 'ingeschakeld'.

### Als de inlogfunctie in mijn Lovable-app al werkt, is de beveiliging dan niet al geregeld?

Nee, inloggen (authenticatie) bewijst uitsluitend wie iemand is. Het bepaalt geenszins wat die persoon vervolgens mag inzien of bewerken (autorisatie). Dat is een afzonderlijke beveiligingslaag die strikt op de server en in de database moet worden afgedwongen. De meeste datalekken bij AI-gegenereerde software treden op bij gebruikers die volkomen legaal zijn ingelogd.

### Verandert het dichten van deze technische kloven het uiterlijk van mijn applicatie?

Nee, absoluut niet. Elk van de genoemde verbeteringen bevindt zich achter de schermen van de gebruikersinterface: databaseregels, servercontroles, webhook-validatie, hostinginrichting en e-mailauthenticatie. Uw schermen, lay-out, styling en teksten blijven exact zoals u ze in Lovable heeft ontworpen. Dat is juist de kracht van een gerichte productieverharding ten opzichte van een tijdrovende herbouw.

### Moet ik overstappen van Supabase naar een ander platform om productie-klaar te zijn?

Vrijwel nooit. Supabase is een volwaardige en robuuste productiedatabase die wereldwijd door grote technologiebedrijven wordt ingezet. Het probleem is louter dat Lovable de ingebouwde beveiligingsfuncties standaard vaak niet inschakelt. Het correct inrichten van RLS-beleidsregels, toevoegen van migratiescripts en overstappen naar een betaald abonnement met back-upfaciliteiten is vele malen sneller en voordeliger dan migreren naar een andere infrastructuur.

### Hoeveel van deze punten kan ik zelf oplossen als ik geduldig ben maar niet kan programmeren?

Het koppelen van een eigen domeinnaam en het instellen van de DNS-records voor e-mailbezorging kunt u met behulp van goede documentatie prima zelfstandig binnen een weekend afronden. Het schrijven van sluitend databasebeleid, server-side validatie en cryptografische verificatie van betaalwebhooks daarentegen niet. Een subtiel verkeerd geformuleerde database-policy is vaak gevaarlijker dan helemaal geen regel, omdat het een schijnveiligheid creëert zonder daadwerkelijke bescherming te bieden.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan ik het ontbreken van Row Level Security zelf controleren zonder technische kennis?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Grotendeels wel. In de Supabase Table Editor ziet u direct of RLS is ingeschakeld. Een tabel met klantgegevens waar RLS op Disabled staat is een direct lek. Wat u niet alleen kunt beoordelen is of een actieve regel waterdicht is geformuleerd."
      }
    },
    {
      "@type": "Question",
      "name": "Als de inlogfunctie in mijn Lovable-app al werkt, is de beveiliging dan niet al geregeld?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Inloggen (authenticatie) verifieert wie iemand is. Bepalen wat diegene mag inzien of wijzigen (autorisatie) is een aparte beveiligingslaag die in de database en op de server moet worden afgedwongen."
      }
    },
    {
      "@type": "Question",
      "name": "Verandert het dichten van deze technische kloven het uiterlijk van mijn applicatie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Alle aanpassingen vinden plaats achter de gebruikersinterface (databaseregels, servercontroles, webhook-verificatie, hosting). Uw schermen en styling blijven exact intact."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik overstappen van Supabase naar een ander platform om productie-klaar te zijn?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vrijwel nooit. Supabase is een uitstekende productiedatabase. Het volstaat om RLS correct te configureren, migratiescripts toe te voegen en een back-upregeling in te stellen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoeveel van deze punten kan ik zelf oplossen als ik geduldig ben maar niet kan programmeren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Domeinkoppeling en e-mail-DNS-records kunt u zelfstandig uitvoeren. Databaseregels, server-side validatie en cryptografische webhook-verificatie vereisen senior engineering, omdat een subtiele fout schijnveiligheid veroorzaakt."
      }
    }
  ]
}
</script>
