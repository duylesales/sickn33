---
Titel: "De EU AI Act en Uw Kleine AI-Product: Wat Is Daadwerkelijk van Toepassing?"
Trefwoorden: EU AI Act compliance, AI Act risicocategorieën, transparantieverplichtingen AI, AI Act mkb, AI Act SaaS-oprichter, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: SaaS-Oprichter Scale-Up
---

# De EU AI Act en Uw Kleine AI-Product: Wat Is Daadwerkelijk van Toepassing?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "De EU AI Act en Uw Kleine AI-Product: Wat Is Daadwerkelijk van Toepassing?",
  "description": "Een analyse van de risicocategorieën van de EU AI Act voor oprichters die bouwen op externe AI-modellen: welke verplichtingen gelden voor een klein product op OpenAI- of Anthropic-API's versus de modelprovider zelf.",
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
  "datePublished": "2027-01-14",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/the-eu-ai-act-and-your-small-ai-product"
  }
}
</script>

Het is 02:00 uur 's nachts. U bent drie weken verwijderd van de eerste pilotdemo van uw AI-gedreven screeningstool voor cv's, en iemand in een Discord-groep voor oprichters plaatst een link: "Is dit niet precies wat de EU AI Act aanmerkt als hoog risico?" U scant de samenvatting. De termen "hoog risico", "conformiteitsbeoordeling" en "boetes tot € 35 miljoen" staan in dezelfde alinea als uw productcategorie. U klapt uw laptop dicht. De volgende ochtend, nog steeds twijfelend of u iets heeft gebouwd dat juridisch volkomen legaal is of iets dat zes maanden extra werk vereist waar u geen tijd voor heeft, is een herkenbaar moment voor oprichters die momenteel AI-functies lanceren. Het eerlijke antwoord is in de meeste gevallen een stuk geruststellender dan de nachtelijke paniek doet vermoeden. Het vereist echter wel dat u systematisch nagaat in welke risicocategorie uw specifieke product valt, in plaats van te reageren op angstaanjagende koppen.

De EU AI Act (de Europese AI-verordening) is een bindend wetgevingskader en delen ervan zijn al van kracht. Het is echter een risicogestuurd raamwerk en geen generieke wet die een klantenservice-chatbot op dezelfde manier behandelt als medische diagnosesoftware. De zwaarste verplichtingen rusten op een handvol bedrijven die systemen ontwikkelen of inzetten in specifieke sectoren met aanzienlijke maatschappelijke impact — niet op elke oprichter die een API-aanroep naar OpenAI heeft verwerkt in een SaaS-applicatie. Hier volgt de beslisboom die daadwerkelijk van toepassing is op een klein, AI-native product.

## De Vier Risicocategorieën: Waar Vrijwel Elk Klein Product Zich Bevindt

De AI Act verdeelt kunstmatige intelligentie in vier risicocategorieën. Begrijpen waar uw product valt, is de belangrijkste beslissing in dit artikel, omdat de bijbehorende verplichtingen enorm verschillen:

1. **Onaanvaardbaar risico (Unacceptable risk):** Systemen met een onaanvaardbaar risico — zoals sociale kredietsystemen (social scoring), manipulatieve subliminale technieken en realtime biometrische surveillance in openbare ruimtes voor wetshandhaving (op zeer strikte uitzonderingen na) — zijn categorisch verboden. Vrijwel geen enkel legitiem commercieel SaaS-product valt in deze categorie. Mocht u hierover oprecht twijfelen, dan is die onzekerheid direct een reden om juridisch advies in te winnen.
2. **Hoog risico (High-risk):** Deze categorie draagt de zwaarste wettelijke lasten. Het omvat specifiek benoemde use cases, zoals besluitvorming rondom personeelszaken (werving, selectie, prestatiebeoordeling, ontslag), kredietscores, biometrische identificatie, het beheer van kritieke infrastructuur, toelating tot onderwijs en wetshandhavingstoepassingen.
3. **Beperkt risico (Limited-risk):** Systemen met specifieke transparantieverplichtingen — zoals chatbots, generatoren van deepfakes en emotieherkenningssystemen. De kernvereiste van de wet is hier dat gebruikers weten dat ze communiceren met een AI of kijken naar AI-gegenereerde content, niet dat het systeem voldoet aan zware technische audits of conformiteitsdossiers.
4. **Minimaal risico (Minimal-risk):** De overgrote meerderheid van AI-ondersteunde functies in reguliere SaaS-producten valt hieronder: een schrijfassistent, zoek- en sorteerfuncties, tekstsamenvattingen of een algemene supportbot die geen ingrijpende besluiten over een individu neemt. Deze systemen kennen onder de AI Act geen dwingende wettelijke verplichtingen, afgezien van vrijwillige gedragscodes.

De meeste AI-native oprichters die bouwen met tools als Lovable of Bolt en externe model-API's aanroepen voor contentcreatie, samenvattingen of interactieve ondersteuning, vallen in de categorie minimaal of beperkt risico. U verifieert dit echter door uw specifieke functionaliteit te toetsen aan de lijst met hoog-risicotoepassingen, niet door af te gaan op hoe geavanceerd de technologie aanvoelt.

## De Vraag Die Uw Categorie Bepaalt: Welke Beslissing Neemt de AI, en Over Wie?

De snelste methode voor een zelfevaluatie is het beantwoorden van één gerichte vraag: **Neemt de AI-functie een besluit met substantiële gevolgen voor een individu, of oefent zij daar wezenlijke invloed op uit — specifiek met betrekking tot werk, krediet, onderwijs, essentiële voorzieningen of burgerrechten?**

- **Zo ja:** U bevindt zich waarschijnlijk op het terrein van hoog risico en heeft een formele juridische analyse nodig.
- **Zo nee:** Genereert uw AI-functie content, vat zij documenten samen, beantwoordt zij vragen of ondersteunt zij een menselijke medewerker die de uiteindelijke beslissingsbevoegdheid behoudt? Dan valt uw product vrijwel zeker onder beperkt of minimaal risico, ongeacht hoe complex het onderliggende taalmodel is.

Dit onderscheid zorgt vaak voor verwarring bij oprichters, omdat het draait om de maatschappelijke **functie** en niet om technische **complexiteit**. Een basaal, op regels gebaseerd script dat leningaanvragen automatisch afwijst zodra een score onder een bepaalde drempel zakt, is wettelijk gezien een hoog-risicosysteem. Een uiterst geavanceerd 'large language model' dat een klantenserviceteam helpt betere conceptantwoorden op te stellen — waarbij een menselijke medewerker het bericht controleert en verstuurt — is dat daarentegen niet. Oprichters nemen soms ten onrechte aan dat een krachtiger model automatisch tot een hogere risicocategorie leidt. De risiconiveaus van de AI Act volgen echter de impact op mensenlevens, niet de capaciteiten van het model.

## Bouwen op Externe Modellen: De Aanbieder versus de Implementeerder

Een fundamenteel onderscheid binnen de AI Act dat direct van invloed is op vrijwel elke oprichter die OpenAI, Anthropic of Google Cloud gebruikt: de zwaarste technische plichten — zoals risicobeheersystemen, uitgebreide technische documentatie en toezicht op trainingsdata — rusten op de **"aanbieder" (provider)** van het AI-systeem. Voor een startup die een externe API aanroept, is dat de modelleverancier (OpenAI, Anthropic, Google), niet de softwareontwikkelaar die er een schil omheen bouwt.

Een oprichter in deze positie kwalificeert juridisch over het algemeen als een **"implementeerder" (deployer)**. Dit is een rol met aanzienlijk lichtere verplichtingen, zelfs wanneer het een hoog-risicotoepassing betreft:
- Zorgdragen voor adequaat menselijk toezicht.
- Het systeem gebruiken volgens de instructies van de aanbieder.
- De werking monitoren op ongewenste afwijkingen en incidenten.

U hoeft dus niet zelfstandig een volledig conformiteitsdossier of risicomanagementsysteem voor het basismodel op te tuigen. Voor een klein team maakt dit een wereld van verschil. Het ontwikkelen van een hoog-risicosysteem als aanbieder vanaf de grond is een enorme onderneming. Het implementeren van een use case op basis van een reeds conform model van een grote leverancier vraagt vooral discipline rondom uw eigen operationele processen en datastromen. Let wel: als uw toepassing daadwerkelijk hoog risico is (zoals geautomatiseerde cv-selectie), blijven de verplichtingen voor implementeerders bindend. Het is geen vrijbrief, maar een substantieel overzichtelijker takenpakket.

## Transparantieverplichtingen: Wat Voor Vrijwel Iedereen Geldt

Ongeacht uw risicocategorie: als uw product AI gebruikt om via een dialooginterface met gebruikers te communiceren of synthetische content genereert, gelden er transparantie-eisen. Deze zijn eenvoudig en goedkoop te implementeren, en het is verstandig ze standaard in te bouwen:

1. **Kenbaarheid van interactie:** Gebruikers moeten weten dat ze communiceren met een AI-systeem en niet met een mens, tenzij dit overduidelijk blijkt uit de context. Een chatbot vereist een zichtbare melding — niet per se storend, maar wel direct duidelijk en niet weggemoffeld in algemene voorwaarden die niemand leest.
2. **Markering van synthetische media:** Door AI gegenereerde of bewerkte beelden, audio of videobestanden (deepfakes) moeten expliciet als zodanig worden gelabeld.
3. **Emotieherkenning en biometrie:** Systemen voor emotieherkenning of biometrische categorisering vereisen een voorafgaande mededeling aan de personen die worden geanalyseerd.

Voor deze maatregelen heeft u geen juridisch team nodig. Het vergt slechts de bewuste keuze om een subtiel UI-element toe te voegen ("U spreekt met een AI-assistent") of een metadata-tag mee te sturen, in plaats van aan te nemen dat de gebruiker het vanzelf begrijpt. Dit is het meest concrete actiepunt van de AI Act voor een startend product: lage implementatiekosten, wettelijk vereist en precies het element dat ontwikkelaars makkelijk vergeten wanneer ze snel een chatbot bouwen via een standaardsjabloon.

## Wat Is Al van Kracht versus Wat Wordt Nog Gefaseerd Ingevoerd?

De verplichtingen uit de AI Act zijn niet allemaal tegelijk ingegaan; ze worden stapsgewijs van kracht volgens een overgangskalender. Kennis van deze tijdlijn helpt bij het stellen van de juiste prioriteiten:

- **Reeds van kracht:** De verboden op systemen met een onaanvaardbaar risico en de basisverplichtingen rondom AI-geletterdheid zijn als eerste in werking getreden.
- **Vervolgfase:** Verplichtingen voor 'general-purpose AI'-modellen (GPAI) treden vervolgens in werking, wat voornamelijk de modelmakers zelf aangaat.
- **Hoog-risicosystemen:** Het merendeel van de eisen voor hoog-risicosystemen kent een langere overgangsperiode. Dit biedt oprichters in deze categorieën tijd om compliancy op te bouwen zonder direct tegen een juridische muur aan te lopen.

"Tijd hebben" betekent echter niet "oneindig uitstellen". Een oprichter wiens functionaliteit evident in een hoog-risicosector valt, moet deze overgangsperiode gebruiken als voorbereidingstraject en niet als excuus om de analyse voor zich uit te schuiven. Raadpleeg de actuele officiële implementatiestatus van de Europese Commissie om uw planning te baseren op feiten in plaats van aannames.

## AI-Geletterdheid: De Verplichting Die Zelfs bij Minimaal Risico Geldt

Eén verplichting binnen de verordening geldt ongeacht de risicocategorie van uw product, en het is precies het artikel waar oprichters zelden van hebben gehoord: zowel aanbieders als implementeerders moeten waarborgen dat hun eigen personeel en (in redelijke mate) hun gebruikers over voldoende **AI-geletterdheid (AI literacy)** beschikken om de mogelijkheden, beperkingen en risico's van het systeem te begrijpen.

Voor een startup met twee personen vereist dit geen formeel opleidingsprogramma. Het betekent simpelweg dat u in heldere, begrijpelijke taal kunt toelichten wat uw AI-functionaliteit wel en niet betrouwbaar kan uitvoeren, en dat deze uitleg daadwerkelijk zichtbaar is voor gebruikers binnen uw applicatie:

- Een korte toelichting van één alinea ("Hoe dit werkt en waar het model fouten kan maken") bij een AI-functie snijdt aan twee kanten.
- Het voldoet aan de strekking van de geletterdheidsplicht én het verlaagt direct het aantal supporttickets van gebruikers die ten onrechte veronderstelden dat een AI-suggestie absolute zekerheid bood.

Deze verplichting wordt snel vergeten omdat er in de perceptie van veel oprichters geen directe astronomische boete aan kleeft. Toch hoort het thuis op uw vaste pre-launch checklist, zij aan zij met de transparantiemeldingen.

## Het Praktische Stappenplan voor Oprichters

Samenvattend is dit de pragmatische volgorde om direct toe te passen:

1. **Stap 1: Beoordeel de besluitvorming.** Onderzoek of uw AI-functionaliteit zelfstandig of sturend beslissingen neemt over individuen binnen de aangewezen hoog-risicocategorieën (werk, onderwijs, krediet, rechtspraak). Bij gerede twijfel is een professioneel juridisch consult noodzakelijk.
2. **Stap 2: Voer de universele transparantie door.** Bevindt uw product zich niet in de hoog-risicocategorie? Voer desondanks direct de eenvoudige transparantieregels in (duidelijke AI-vermelding in de interface, etikettering van synthetische media). Dit wekt vertrouwen en voorkomt latere aanpassingen.
3. **Stap 3: Bepaal uw rol als implementeerder.** Valt uw use case wél onder hoog risico, maar bouwt u op API's van grote partijen? Besef dat uw verplichtingen zich toespitsen op operationeel menselijk toezicht en verantwoord gebruik, niet op het herhalen van de validatie van het basismodel.
4. **Stap 4: Leg uw besluitvorming schriftelijk vast.** Documenteer uw analyse, ook al is het een intern document van één pagina. Een korte toelichting waarin u beargumenteert waarom uw applicatie onder minimaal of beperkt risico valt, is van onschatbare waarde wanneer een investeerder, een zakelijke klant of een toezichthouder hier later naar vraagt.

Het gestructureerd doorlopen van deze risicoclassificatie en het tijdig doorvoeren van transparantievoorzieningen is precies het type 'last-mile' ondersteuning dat [LaunchStudio](https://launchstudio.eu/nl/) biedt aan software-oprichters. Dit doen we met de rugdekking van Manifera's 11+ jaar ervaring in het ontwikkelen van veilige, conforme productiesystemen — onder meer voor organisaties zoals TNO die opereren in strikt gereguleerde markten.

[Plan een kennismakingsgesprek van 15 minuten](https://launchstudio.eu/nl/#contact) om exact te bepalen in welke risicocategorie uw AI-functionaliteit valt.

## Echt voorbeeld

### Een SaaS-Oprichter in Actie: De Functionaliteit Die Anders Was Dan Ze Leek

Bram Willemsen ontwikkelde ShiftMatch, een AI-ondersteunde roostertool voor retailketens, gebouwd met behulp van Cursor. Een van de functies gebruikte een LLM om suggesties te doen welke medewerkers konden worden ingeroosterd op opengevallen diensten, gebaseerd op eerdere prestatiebeoordelingen die door filiaalmanagers waren ingevoerd. De juridische afdeling van een grote potentiële enterprise-klant merkte deze feature aan als een mogelijk hoog-risicosysteem voor "besluitvorming over personeel" onder de AI Act en zette het verkooptraject on-hold in afwachting van opheldering.

Tijdens een audit door Manifera via LaunchStudio werd de doorslaggevende factor blootgelegd: ShiftMatch deed enkel suggesties, maar de filiaalmanager wees diensten altijd handmatig en definitief toe en kon suggesties te allen tijde negeren. Hierdoor was er sprake van een beslissingsondersteunende tool in plaats van een autonoom personeelsbeoordelingssysteem. Wel vereisten de gebruikte prestatiegegevens zorgvuldige documentatie om te waarborgen dat historische scores geen verborgen vooroordelen (bias) versterkten.

Het team hielp Bram om het 'human-in-the-loop' ontwerpprincipe expliciet vast te leggen, een duidelijke melding in de interface te plaatsen dat dienstvoorstellen door AI zijn gegenereerd en door een manager moeten worden goedgekeurd, en een beknopte juridische verantwoording op te stellen die de bedrijfsjuristen van de klant direct konden toetsen.

**Het resultaat:** De enterprise-deal werd binnen twee weken hervat zodra de documentatie over menselijk toezicht op tafel lag. Tegenwoordig levert ShiftMatch standaard een AI Act-conformiteitsnotitie mee in elk zakelijk verkooptraject, wat van een potentieel obstakel een krachtig verkoopargument heeft gemaakt.

> *"Ik dacht dat de komst van de AI Act betekende dat ik deze functionaliteit direct moest schrappen. In werkelijkheid betekende het dat ik exact moest vastleggen hoe een mens de controle over de beslissing behoudt — iets wat ik al had gebouwd, maar simpelweg nergens had gedocumenteerd."*
> — **Bram Willemsen, Oprichter van ShiftMatch (Nijmegen)**

## Veelgestelde Vragen

### Is de EU AI Act van toepassing op mijn product als mijn bedrijf buiten de EU is gevestigd?
Ja. De AI Act hanteert een extraterritoriale werking: de regels zijn van toepassing op basis van de locatie waar het AI-systeem wordt gebruikt of waar de output effect heeft op personen binnen de Europese Unie. Een buitenlandse startup die Europese gebruikers bedient, valt dus gewoon onder de wetgeving.

### Is een klantenservice-chatbot onder de AI Act automatisch een hoog-risicosysteem?
Nee. Een standaard klantenservice-chatbot die productvragen beantwoordt of supporttickets routeert, valt onder de categorie beperkt risico of minimaal risico. De enige vereiste is dat gebruikers duidelijk wordt gemeld dat ze met een AI communiceren. De status 'hoog risico' is voorbehouden aan afgebakende categorieën zoals personeelsselectie, kredietbeoordeling of rechtstoegang.

### Welke boetes gelden er voor kleine softwarebedrijven bij een onjuiste risicoclassificatie?
Boetes worden berekend op basis van de ernst van de overtreding en de omvang van de onderneming, waarbij de maximale bedragen gelden voor zware overtredingen zoals het inzetten van verboden systemen. Toezichthouders richten zich in de handhavingspraktijk primair op opzettelijke nalatigheid en het weigeren van medewerking, en niet op een startend bedrijf dat te goeder trouw een beargumenteerde classificatie heeft opgesteld die eventueel moet worden aangescherpt.

### Neem ik automatisch alle compliance-verplichtingen over als ik de API van OpenAI of Anthropic gebruik?
Nee. De zwaarste eisen voor 'aanbieders' (zoals diepgaande technische documentatie over de trainingsdata en het basismodel) liggen bij partijen als OpenAI of Anthropic. Als oprichter bent u een 'implementeerder'. Uw verplichtingen richten zich op uw eigen implementatie, zoals passend menselijk toezicht, datakwaliteit bij invoer en verantwoorde toepassing.

### Kan ik de risicocategorie van mijn product zelf bepalen of moet ik direct een advocaat inschakelen?
Een zelfevaluatie aan de hand van de officiële criteria is voor de meeste minimale en beperkte toepassingen (zoals contentcreatie en algemene assistenten) een uitstekende eerste stap. Schakel direct een gespecialiseerde jurist in zodra uw software besluitvorming raakt rondom werving en selectie, financiële beoordelingen, medische toepassingen, of wanneer er na uw eigen analyse fundamentele twijfel blijft bestaan.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is de EU AI Act van toepassing op mijn product als mijn bedrijf buiten de EU is gevestigd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. De AI Act is van toepassing op basis van de locatie waar het AI-systeem wordt gebruikt of waar de output effect heeft op personen binnen de Europese Unie, ongeacht waar de rechtspersoon is gevestigd."
      }
    },
    {
      "@type": "Question",
      "name": "Is een klantenservice-chatbot onder de AI Act automatisch een hoog-risicosysteem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Een standaard support-chatbot valt onder minimaal of beperkt risico en vereist uitsluitend een transparantiemelding dat gebruikers met een AI-systeem praten. Hoog risico geldt alleen voor specifieke categorieën zoals werving of kredietverlening."
      }
    },
    {
      "@type": "Question",
      "name": "Welke boetes gelden er voor kleine softwarebedrijven bij een onjuiste risicoclassificatie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Boetes zijn gerelateerd aan de ernst en de omvang van de onderneming. Toezichthouders focussen bij handhaving op opzettelijke overtredingen en het inzetten van verboden systemen, niet op startups die te goeder trouw en gedocumenteerd een classificatie hebben opgesteld."
      }
    },
    {
      "@type": "Question",
      "name": "Neem ik automatisch alle compliance-verplichtingen over als ik de API van OpenAI of Anthropic gebruik?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. De zwaarste plichten voor modelaanbieders blijven bij partijen als OpenAI. Als oprichter bent u implementeerder en gelden er lichtere plichten gericht op menselijk toezicht en verantwoord gebruik."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik de risicocategorie van mijn product zelf bepalen of moet ik direct een advocaat inschakelen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor gangbare minimale en beperkte use cases volstaat een gedocumenteerde zelfevaluatie. Schakel een gespecialiseerde advocaat in zodra uw systeem personeelszaken, kredietverlening of andere benoemde hoog-risicodomeinen raakt."
      }
    }
  ]
}
</script>
