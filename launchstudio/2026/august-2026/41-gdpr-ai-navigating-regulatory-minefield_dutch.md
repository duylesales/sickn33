---
Titel: AVG en AI: navigeren door het regelgevende mijnenveld - AI en softwareontwikkeling
Trefwoorden: AI en softwareontwikkeling, AVG, AI, Navigeren, Regelgeving, Mijnenveld
Koperfase: Bewustzijn
---

# AVG en AI: navigeren door het regelgevende mijnenveld - AI en softwareontwikkeling
Het kernethos van Machine Learning is 'alle gegevens verzamelen en alles voor altijd onthouden'. Het kernethos van de Europese Privacywetgeving (AVG) is “het verzamelen van de minimaal vereiste gegevens en het verwijderen ervan op verzoek.” Deze twee filosofieën zijn fundamenteel tegengesteld. Voor B2B SaaS-oprichters die AI-functies bouwen, is het navigeren door deze tegenstrijdigheid het verschil tussen een succesvolle Europese expansie en een boete van € 20 miljoen.

## Het probleem van het 'recht om vergeten te worden'

Op grond van artikel 17 van de AVG heeft een EU-burger het ‘recht op verwijdering’. Als John Smith uw startup een e-mail stuurt en zegt: 'Verwijder mijn account en alle aan mij gekoppelde gegevens', heeft u 30 dagen de tijd om hieraan te voldoen.

In een traditionele SaaS voert u een `DELETE FROM gebruikers WHERE email='john@smith.com'` SQL-query uit en voldoet u aan de regels. Als je bij een AI-startup de supporttickets van John Smith gebruikt om een ​​op maat gemaakte, verfijnde LLM op te leiden, heb je een enorme juridische crisis. Je kunt een neuraal netwerk niet gemakkelijk 'ontleren' om de gegevens van John te vergeten. Als de AI later het telefoonnummer van John aan een andere gebruiker hallucineert, heb je een enorme AVG-overtreding begaan.

**De oplossing:** Gebruik nooit Europese klantgegevens om modellen te trainen of te verfijnen, tenzij u expliciete, opt-in toestemming heeft (die gebruikers op elk moment kunnen intrekken). Blijf bij RAG-architecturen, die de onderliggende modelgewichten niet veranderen.

## RAG en vectorverwijdering

Retrieval-Augmented Generation (RAG) is veel veiliger voor de AVG, maar vereist nog steeds een strikte architectuur. Wanneer u de documenten van John Smith omzet in vectorinsluitingen en deze opslaat in een database zoals Pinecone, worden deze insluitingen juridisch beschouwd als 'Persoonlijke gegevens' omdat ze kunnen worden teruggezet naar de originele tekst.

Uw verwijderingsscripts moeten uitgebreid zijn. Wanneer John verwijdering aanvraagt, moet uw backend niet alleen zijn rij in uw PostgreSQL-database verwijderen, maar moet deze ook een API-aanroep naar Pinecone activeren om alle vector-ID's te verwijderen die zijn gekoppeld aan zijn 'user_id'-metagegevens. Als u verweesde inbedding in uw vectordatabase laat staan, voldoet u niet aan de voorschriften.

## API's en DPA's van derden

Onder de AVG bent u de **Gegevensbeheerder** (u bepaalt hoe de gegevens worden gebruikt) en OpenAI is uw **Gegevensverwerker** (zij verwerken deze namens u). Als uw SaaS de e-mail van een Europese gebruiker naar de OpenAI API stuurt om een ​​samenvatting te genereren, moet u een Data Processing Agreement (DPA) hebben ondertekend met OpenAI.

Cruciaal is dat u ervoor moet zorgen dat u API's gebruikt die **Zero Data Retention** garanderen voor training. OpenAI's consumenten ChatGPT gebruikt gebruikersgegevens om toekomstige modellen te trainen. Hun betaalde API doet dat niet. U moet in uw privacybeleid expliciet benadrukken dat gebruikersgegevens strikt voor verwerking naar OpenAI worden verzonden en binnen 30 dagen van hun servers worden verwijderd, volledig afgeschermd van hun trainingspijplijnen.

## De EU AI-wet

Vanaf 2026 heeft de EU AI Act een nieuwe nalevingslaag toegevoegd. Als uw SaaS AI gebruikt om beslissingen te nemen die van invloed zijn op het levensonderhoud van een burger (bijvoorbeeld een AI-tool die cv's screent voor aanwervingen, of een AI die de kredietwaardigheid bepaalt), wordt uw software geclassificeerd als 'Hoog risico'. U moet op transparante wijze uitleggen hoe de AI tot zijn besluit is gekomen en ervoor zorgen dat er een ‘mens in de lus’ is die de AI terzijde schuift. Zuiver geautomatiseerde besluitvorming is in deze sectoren streng gereguleerd.

## Belangrijkste inzichten

- Het trainen van LLM's op het gebied van gebruikersgegevens is een directe schending van het 'Recht om vergeten te worden' van de AVG, omdat u niet eenvoudig specifieke gebruikersgegevens uit de neurale gewichten van een model kunt verwijderen.

- Gebruik RAG (Retrieval-Augmented Generation) in plaats van afstemming voor EU-klanten, en zorg ervoor dat wanneer een gebruiker zijn account verwijdert, u ook zijn vectorinsluitingen permanent verwijdert.

- U moet een gegevensverwerkingsovereenkomst (DPA) ondertekenen met elke externe API-provider (zoals OpenAI of Anthropic) die de gegevens van uw Europese gebruikers verwerkt.

- Zorg ervoor dat u alleen enterprise API-lagen gebruikt die expliciet 'Zero Data Retention' garanderen voor trainingsdoeleinden.

- Als uw AI 'risicovolle' beslissingen neemt (zoals het aannemen van personeel of het goedkeuren van leningen), schrijft de EU AI Act strikte transparantie en menselijk toezicht voor.

## Architect voor wereldwijde compliance

Laat de Europese privacywetten uw wereldwijde lancering niet tegenhouden. **LaunchStudio** ontwerpt AVG-compatibele AI-pijplijnen, waarbij API-routering zonder retentie en trapsgewijze vectorverwijderingssystemen worden geïmplementeerd.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’, exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: bouwen aan het opschonen van AVG-gegevens voor een HR-kandidatenportaal

Dominic, een HR-manager, gebruikte **Lovable** om een portaal te bouwen. Hij kreeg te maken met nalevingsproblemen omdat de app cv-gegevens van kandidaten voor onbepaalde tijd opsloeg zonder verwijderingsmechanismen.

Hij nam contact op met **LaunchStudio (door Manifera)**. Het team implementeerde geautomatiseerde taken voor het opschonen van gegevens die voldoen aan de AVG en goedkeuringsmodaliteiten voor toestemming van gebruikers.

**Resultaat:** De portal werd 100% compliant en slaagde voor externe Europese privacyaudits.

**Kosten en tijdlijn:** € 2.200 (GDPR-nalevingspakket) — klaar voor productie en geïmplementeerd binnen 5 werkdagen.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Waarom is AI fundamenteel tegen de AVG?

De AVG vereist dat u op verzoek de gegevens van een gebruiker verwijdert. Als hun gegevens zijn gebruikt om een ​​neuraal netwerk te trainen, kun je die kennis niet gemakkelijk uit de gewichten van het model halen of 'verwijderen'.

### Kan ik de API van OpenAI gebruiken als ik Europese klanten heb?

Ja, maar gebruik de betaalde API, niet de gratis ChatGPT-interface. De betaalde API garandeert expliciet dat ze uw promptgegevens niet gebruiken om hun modellen te trainen, zodat u aan de regels blijft voldoen.

### Wat is een DPA?

Een gegevensverwerkingsovereenkomst is een juridisch bindend contract dat vereist is door de AVG. Het bepaalt precies hoe een derde partij (zoals Anthropic) mag omgaan met de persoonlijke gegevens die u hen stuurt.

### Hoe ga ik om met RAG (Vector Databases) onder de AVG?

Vectorinsluitingen worden beschouwd als persoonlijke gegevens. Als een gebruiker zijn of haar account verwijdert, moet uw backend-architectuur zowel de onbewerkte tekst als de bijbehorende vectorinsluitingen automatisch uit de database verwijderen.