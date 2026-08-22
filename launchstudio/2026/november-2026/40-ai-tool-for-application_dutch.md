---
Title: Het Strangler Fig Patroon met een AI-Tool voor Applicatiemodernisering
Keywords: AI tool for application, application modernization, enterprise AI, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Enterprise Architect / VP of Engineering
---

# Het Strangler Fig Patroon met een AI-Tool voor Applicatiemodernisering

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-Tool voor Applicatiemodernisering: Het Strangler Fig Patroon Ontmoet LLM's",
  "description": "Applicatiemodernisering bij bedrijven is berucht om zijn hoge risico's. Een technische diepduik in hoe Large Language Models het Strangler Fig-patroon versnellen om legacy-monolieten veilig te vervangen.",
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
  "datePublished": "2026-12-10",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/ai-tool-for-application"
  }
}
</script>

Het meest angstaanjagende project dat een Enterprise Architect kan aanvaarden, is de zogenaamde "Big Bang" herschrijving. Een organisatie besluit dat haar 15 jaar oude Java-monoliet (of erger nog, een 30 jaar oude COBOL-mainframe) te kostbaar is geworden om te onderhouden. Ze leggen de ontwikkeling van nieuwe functies gedurende twee jaar volledig stil, geven miljoenen euro's uit en proberen de gehele applicatie vanaf nul opnieuw op te bouwen in moderne microservices.

Historisch gezien mislukt 70% van alle Big Bang-herschrijvingen. Ze raken buiten hun budget, of tegen de tijd dat het nieuwe systeem eindelijk klaar is voor productie, zijn de zakelijke vereisten van de markt alweer compleet veranderd.

Om dit catastrofale risico te beperken, vertrouwen vooraanstaande engineeringteams op het **Strangler Fig Patroon** (het Wurgvijgpatroon). In plaats van de gehele monoliet in één keer te herschrijven, bouwt u een API-gateway vóór de bestaande applicatie. U isoleert één specifieke, kleine functie (bijvoorbeeld "Gebruikersfacturatie"), herschrijft uitsluitend die specifieke functie als een moderne microservice, en routeert het verkeer voor die functie naar de nieuwe service terwijl de rest van de monoliet ongemoeid blijft. Na verloop van tijd groeien de nieuwe microservices rondom de monoliet, waarbij ze deze langzaam "verworgen" totdat het oude systeem veilig uit gebruik kan worden genomen.

Het Strangler Fig-patroon is briljant, maar het was traditioneel ook zenuwslopend traag. In 2026 heeft de adoptie van de LLM als AI-tool voor applicatiemodernisering dit proces fundamenteel versneld, waardoor een migratie van 3 jaar verandert in een strakke sprint van 9 maanden.

## De Drie Fasen van AI-Geassisteerde Modernisering

Het gebruik van een AI-coderingstool (zoals Cursor of GitHub Copilot Enterprise) om simpelweg een blok legacy-code te selecteren en te typen "Vertaal naar Node.js" is een recept voor een ramp. Legacy-code bevat verborgen bedrijfsregels, ongedocumenteerde neveneffecten en bizarra databaseafhankelijkheden.

Om AI effectief in te zetten bij applicatiemodernisering in enterprise-omgevingen, moeten architecten AI uitrollen over drie strak gestructureerde fasen.

### Fase 1: De AI Archeoloog (Domeinontdekking)
Het moeilijkste onderdeel van het moderniseren van een legacy-applicatie is dat de oorspronkelijke ontwikkelaars tien jaar geleden al zijn vertrokken en dat de documentatie verloren is gegaan tijdens een Jira-migratie in 2018. De monoliet is een black box.

In deze fase gebruiken we AI niet om code te schrijven. We zetten een gespecialiseerde RAG-pipeline (Retrieval-Augmented Generation) in als "AI Archeoloog". De gehele legacy-codebase wordt gevectoriseerd. Enterprise Architecten gebruiken de AI om de afhankelijkheidsgrafiek (dependency graph) in kaart te brengen. Zij vragen het LLM: *"Identificeer elke functie in de codebase die interactie heeft met de tabel `users` en terugleidt naar de facturatiemodule."* De AI analyseert de verouderde syntaxis, volgt de datastroom en levert een nauwkeurige architectonische blauwdruk op die exact aangeeft waar de grenzen liggen om een schone microservice te isoleren.

### Fase 2: De LLM Transpiler (Begrenzen & Vertalen)
Zodra een specifieke begrensde context (bounded context, bijv. de Facturatiemodule) geïsoleerd is, wordt AI ingezet voor de vertaling. Dit is echter geen naïeve 1-op-1 syntaxisvertaling.

Omdat de AI wordt aangestuurd met de architectonische blauwdruk uit Fase 1, krijgt deze de opdracht om het paradigma te moderniseren. Het neemt de synchrone, hecht gekoppelde Java-code en vertaalt deze naar asynchrone, event-driven TypeScript-code. Cruciaal is dat de AI de opdracht krijgt om uitgebreide Unit Tests te genereren voor de *oude* logica, die vervolgens worden gebruikt om te garanderen dat de *nieuwe* microservice exact dezelfde output genereert voor exact dezelfde input.

### Fase 3: De Schaduw Router (Deterministische Verificatie)
Het meest gevaarlijke moment is het routeren van echt productieverkeer naar de nieuw gegenereerde AI-microservice. Om elk risico te elimineren, zetten architecten een "Schaduw Router" in.

Wanneer een gebruiker een factuur opvraagt, stuurt de API-gateway het verzoek naar de oude Java-monoliet (die de echte factuur aan de gebruiker teruggeeft). Gelijktijdig stuurt de gateway een *schaduwkopie* van het verzoek naar de nieuwe met AI gegenereerde TypeScript-microservice. De antwoorden worden op de achtergrond wiskundig vergeleken. Pas wanneer de nieuwe service over 10.000 verzoeken een 100% overeenkomst vertoont met de legacy-service, wordt het verkeer officieel definitief overgeschakeld.

## Hoe LaunchStudio het Strangler Fig Patroon Engineert

Het uitvoeren van een door AI versnelde Strangler Fig-migratie vereist een diepgaand begrip van legacy-systemen, moderne cloudarchitectuur en MLOps (Machine Learning Operations). Startups bouwen greenfield-applicaties; gevestigde bedrijven moeten brownfield-situaties ontwarren.

[LaunchStudio](https://launchstudio.eu/nl/), ondersteund door de zware enterprise engineering-achtergrond van [Manifera](https://www.manifera.com/), biedt de architectonische rigoureuze aanpak die nodig is om missiekritieke applicaties veilig te moderniseren.

Onder leiding van CEO Herre Roelevink in Amsterdam, en uitgevoerd door senior systeemarchitecten aan de Phố Quang-straat 10 in Ho Chi Minhstad, doet LaunchStudio geen "Big Bang" herschrijvingen. Wij voeren chirurgische, door AI versnelde isolaties en extractions uit.

Onze Moderniseringsarchitectuur omvat:
1. **De Codebase Vectorisatie Pipeline:** Wij richten veilige, geïsoleerde RAG-omgevingen in die uw legacy C#-, Java- of PHP-codebase indexeren, waardoor onze architecten de verborgen afhankelijkheden van de monoliet direct kunnen bevragen.
2. **Geautomatiseerde Testgeneratie:** Voordat we één regel legacy-code vertalen, gebruiken we AI om uitputtende testsuites te genereren tegen de bestaande endpoints, wat een wiskundig vangnet creëert voor de herschrijving.
3. **De API Gateway Uitrol:** Wij bouwen de kritieke routing-infrastructuur (met tools zoals Kong of AWS API Gateway) die Schaduw Routing en geleidelijke migratie van de nieuwe microservices mogelijk maakt, wat nul downtime garandeert voor uw eindgebruikers.

## Belangrijkste inzichten

- **Vermijd de Big Bang-valkuil**: 70% van de volledige herschrijvingen mislukt; gebruik het Strangler Fig-patroon om monolieten geleidelijk via API-gateways te vervangen.
- **Drie fasen met AI**: Gebruik AI eerst als Archeoloog (afhankelijkheden mappen), vervolgens als Transpiler (moderne event-driven code genereren) en tenslotte via Schaduw Routing (wiskundig testen tegen live verkeer).
- **Zorg voor Zero Data Retention**: Gebruik uitsluitend enterprise-tier API's met ZDR-overeenkomsten bij het vectoriseren van bedrijfseigen legacy-codebases.

## Echt voorbeeld

### Een AI-native oprichter in actie: De zorg-monoliet die niet kon schalen

Thomas is VP of Engineering bij een zorg-SaaS-bedrijf in Wenen. Hun kernproduct, een patiëntenbeheersysteem, was een omvangrijke monolithische PHP-applicatie gebouwd in 2012.

Het bedrijf was zeer winstgevend, maar de technologie verstikte hun groei. Het uitrollen van een nieuwe functie kostte drie weken omdat het aanpassen van de planningsmodule vaak per ongeluk de receptenmodule ontregelde. De codebase telde twee miljoen regels code. Thomas wist dat ze moesten overstappen naar een moderne microservices-architectuur, maar zijn bestuur weigerde toestemming te geven voor een feature-stop van twee jaar voor een complete herschrijving.

Thomas probeerde ChatGPT te gebruiken om bestanden één voor één te vertalen, maar de nieuwe code faalde voortdurend omdat verborgen databaseafhankelijkheden over het hoofd werden gezien.

Hij nam contact op met LaunchStudio. Het engineeringteam van Manifera stelde een door AI versnelde Strangler Fig-aanpak voor.

In een strak gestructureerd traject van 4 maanden richtte LaunchStudio zich op het meest knellende knelpunt: De Planningsmodule.
Ten eerste vectoriseerden zij de gehele PHP-monoliet in een veilige Supabase pgvector-instantie. Zij gebruikten de AI Archeoloog om exact in kaart te brengen waar de planningslogica raakvlakken had met de rest van de applicatie.
Ten tweede bouwden zij een API-gateway vóór de applicatie.
Ten derde gebruikten zij Claude 3.5 Sonnet om de hecht gekoppelde PHP-planningslogica te vertalen naar een schone, zelfstandige Node.js-microservice, terwijl er gelijktijdig 500 unit tests werden gegenereerd om de logica te verifiëren.

LaunchStudio rolde de nieuwe Node.js-microservice gedurende twee weken uit in "Schaduwmodus". De API-gateway stuurde echte afsprakenverzoeken naar zowel de oude PHP-monoliet als de nieuwe Node.js-service en vergeleek de resultaten. Zodra het percentage overeenkomsten 100% bereikte, schakelden ze de knop om.

**Resultaat:** De Planningsmodule werd succesvol afgesplitst. Deze draait nu op een moderne, automatisch schaalbare Node.js-microservice. Het team kan updates aan het planningssysteem uitrollen binnen 20 minuten zonder enig risico voor de receptenmodule. Omdat AI de domeinontdekking en testgeneratie enorm versnelde, voltooide LaunchStudio de afsplitsing in 4 maanden in plaats van de geprojecteerde 12 maanden, wat het bedrijf € 120.000 aan engineeringkosten bespaarde met nul downtime.

> *"Het proberen te herschrijven van een monoliet is als het proberen te wisselen van autobanden terwijl u met 120 km/u op de snelweg rijdt. LaunchStudio gebruikte AI niet alleen om code te schrijven, maar om de gekte van ons 10 jaar oude systeem te ontwarren. Het Strangler Fig-patroon dat zij implementeerden gaf ons bestuur het vertrouwen om zonder angst te moderniseren."*
> — **Thomas Gruber, VP of Engineering, MedTech Solutions (Wenen)**

**Kosten & Doorlooptijd:** € 35.000 (Enterprise Modernization Pakket - Fase 1 Extraction) — productieklaar en uitgerold in 4 maanden.

---

## Veelgestelde vragen

### Waarom zouden we de ontwikkeling van nieuwe functies niet gewoon een jaar stilleggen en een 'Big Bang' herschrijving met AI doen?
Omdat de zakelijke vereisten van de markt gedurende dat jaar zullen veranderen. Tegen de tijd dat uw AI de Big Bang-herschrijving heeft voltooid, is het product dat u heeft gebouwd niet langer het product waar de markt om vraagt. Bovendien dragen Big Bang-herschrijvingen een gigantisch risico op catastrofale mislukking bij de overschakeling. Het Strangler Fig-patroon stelt u in staat om één module tegelijk te moderniseren terwijl u nieuwe functies aan klanten blijft leveren.

### Kan een AI-tool werkelijk een 20 jaar oude, ongedocumenteerde codebase begrijpen?
Ja, mits u gebruikmaakt van een gespecialiseerde RAG-pipeline (Retrieval-Augmented Generation). U kunt niet simpelweg een codebase van 2 miljoen regels in ChatGPT plakken. LaunchStudio vectoriseert de gehele codebase in een hoogdimensionale database. Wanneer de architect een vraag stelt, haalt de AI de exacte bestanden, databaseschema's en functie-aangroepen op die betrekking hebben op dat specifieke domein.

### Hoe garanderen we dat de door AI vertaalde microservice de bestaande bedrijfslogica niet ontregelt?
Dat garandeert u via Schaduw Routing. LaunchStudio bouwt een API-gateway die een kopie van het live productieverkeer naar de nieuwe AI-gegenereerde microservice stuurt, terwijl de daadwerkelijke gebruiker het antwoord van de legacy-monoliet ontvangt. De outputs van beide systemen worden op de achtergrond wiskundig vergeleken. De nieuwe microservice wordt pas geactiveerd voor gebruikers nadat bewezen is dat deze de productiegegevens met 100% precisie kan verwerken.

### Moeten we de AI gebruiken om legacy-code 1-op-1 te vertalen naar de nieuwe taal?
Nee. Een 1-op-1 vertaling van slechte Java-code levert simpelweg slechte Node.js-code op. Het doel van modernisering is het omarmen van nieuwe paradigma's (bijv. de overstap van synchrone, hecht gekoppelde aanroepen naar asynchrone, event-driven architectuur). LaunchStudio stuurt de AI aan met strikte architectonische richtlijnen, zodat de zakelijke logica behouden blijft maar de implementatie wordt geüpgraded naar moderne cloud-native standaarden.

### Is het veilig om onze bedrijfseigen legacy-codebase te uploaden naar een AI-tool voor analyse?
Het is volstrekt onveilig om deze te uploaden naar openbare tools zoals de standaard ChatGPT of Claude. LaunchStudio voert Codebase Vectorisatie uitsluitend uit met behulp van strikt geïsoleerde enterprise-tier API-endpoints (zoals Azure OpenAI) die worden gedekt door Zero Data Retention (ZDR) overeenkomsten. Uw bedrijfseigen codebase wordt nooit gebruikt om externe modellen te trainen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom zouden we de ontwikkeling van nieuwe functies niet gewoon een jaar stilleggen en een 'Big Bang' herschrijving met AI doen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Marktvereisten veranderen in een jaar. Een Big Bang herschrijving draagt een gigantisch risico op mislukking. Het Strangler Fig-patroon moderniseert één module tegelijk met nul downtime."
      }
    },
    {
      "@type": "Question",
      "name": "Kan een AI-tool werkelijk een 20 jaar oude, ongedocumenteerde codebase begrijpen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, via een gespecialiseerde RAG-pipeline. LaunchStudio vectoriseert de codebase in een database zodat AI de exacte afhankelijkheden en functies van het domein kan blootleggen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe garanderen we dat de door AI vertaalde microservice de bestaande bedrijfslogica niet ontregelt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Via Schaduw Routing. De API-gateway stuurt live verkeer naar zowel de oude monoliet als de nieuwe service en vergelijkt de outputs op 100% nauwkeurigheid voordat u overschakelt."
      }
    },
    {
      "@type": "Question",
      "name": "Moeten we de AI gebruiken om legacy-code 1-op-1 te vertalen naar de nieuwe taal?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Een 1-op-1 vertaling produceert slechte code. LaunchStudio stuurt AI aan om bedrijfslogica te behouden maar de architectuur te upgraden naar moderne event-driven cloudstandaarden."
      }
    },
    {
      "@type": "Question",
      "name": "Is het veilig om onze bedrijfseigen legacy-codebase te uploaden naar een AI-tool voor analyse?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Gebruik geen openbare tools. LaunchStudio gebruikt geïsoleerde enterprise API-endpoints met Zero Data Retention (ZDR) overeenkomsten. Uw code wordt nooit gebruikt voor modeltraining."
      }
    }
  ]
}
</script>
