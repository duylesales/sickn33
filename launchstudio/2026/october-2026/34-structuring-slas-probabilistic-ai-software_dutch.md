---
Titel: SLA's structureren voor probabilistische AI-software
Trefwoorden: Structureren, SLA's, Probabilistisch, AI, Software
Koperfase: Bewustzijn
---

# Structureren van SLA's voor probabilistische AI-software
Bij de verkoop van B2B-ondernemingen vormt de Service Level Agreement (SLA) de juridische ruggengraat van het contract. Traditionele SaaS-bedrijven garanderen routinematig een uptime van 99,99% en beloven zware financiële boetes als hun servers crashen. AI-startups kunnen deze belofte niet maken. Als uw kernproduct volledig afhankelijk is van de OpenAI API, is uw uptime overgeleverd aan een derde partij. Als u een standaard verouderde SLA ondertekent, riskeert u voor uw startup verwoestende financiële boetes.

## De afhankelijkheidsval van derden

Als u een ziekenhuis een uptime-garantie van 99,9% belooft en OpenAI ervaart een grote storing van zes uur, stopt uw AI-agent met functioneren. Bij een standaard SaaS-contract eist het ziekenhuis een terugbetaling van 30% voor de maand omdat u de SLA heeft overtreden.

U moet uw juridische contracten zo ontwerpen dat ze uw technische realiteit weerspiegelen. Uw SLA moet een expliciete **API-uitsluitingsclausule van derden** bevatten. Deze clausule bepaalt juridisch dat downtime veroorzaakt door aanbieders van fundamentele modellen (OpenAI, Anthropic, Google) wordt beschouwd als een equivalent van *Overmacht*, waardoor uw startup volledig wordt vrijgesteld van financiële boetes tijdens hun uitval.

## Architecting LLM-terugval

Hoewel wettelijke uitsluitingen u financieel beschermen, zal frequente downtime er nog steeds voor zorgen dat de klant zich terugtrekt. U moet technische veerkracht opbouwen om uw SLA te beschermen.

Hardcodeer geen enkele provider in uw backend. Implementeer een **LLM-router** (zoals LiteLLM). Als er na 10 seconden een time-out optreedt bij uw primaire oproep naar GPT-4, zou uw backend de fout automatisch moeten opvangen en de prompt stilletjes omleiden naar Claude 3.5 Sonnet van Anthropic. De gebruiker ervaart een kleine vertraging, maar de applicatie crasht niet. Fallbacks van meerdere leveranciers zijn de enige manier om uptime op bedrijfsniveau te garanderen in het AI-tijdperk.

## Probabilistische nauwkeurigheid afwijzen

Traditionele software is deterministisch: 2 + 2 is altijd 4. Als een rekenmachine-app 5 zegt, is er sprake van contractbreuk. AI is probabilistisch: het hallucineert. Als u dit niet juridisch aanpakt, zal een zakelijke klant u aanklagen wegens contractbreuk zodra uw agent voor de eerste keer een feitelijke fout maakt.

Uw SLA en Servicevoorwaarden moeten een **Accuracy Disclaimer** bevatten. U moet uw AI-uitvoer expliciet definiëren als 'Adviserend'. Het contract moet verplichten dat de klant 'Human-in-the-Loop'-beoordelingsprocedures hanteert, waarbij de eindverantwoordelijkheid voor de nauwkeurigheid van de workflow juridisch wordt verschoven naar het menselijke personeel van de klant.

## Latentie versus doorvoergaranties

Enterprise-klanten eisen vaak 'Response Time'-garanties (bijvoorbeeld: 'De API moet binnen 2 seconden reageren'). U kunt hier niet mee akkoord gaan. Het streamen van 4.000 tokens aan complexe juridische analyses van een LLM duurt fysiek 15 seconden. Het kan niet worden geoptimaliseerd.

Latentie-SLA's weigeren. Onderhandel in plaats daarvan over **Doorvoer-SLA's**. Garandeer dat uw achtergrondtaakwachtrijen 10.000 documenten per uur zullen verwerken, maar weigeren de responstijd van milliseconden van elke individuele AI-generatie te garanderen. Schep realistische verwachtingen rond de snelheid van generatief computergebruik.

## Belangrijkste afhaalrestaurants

- Teken nooit een standaard '99,9% Uptime'-contract voor een AI-product. De uptime van uw startup is afhankelijk van OpenAI of Anthropic. Als hun servers crashen, gaat uw software kapot. Waar je geen controle over hebt, kun je niet garanderen.

- Neem in alle contracten een ‘Third Party Exclusion Clause’ op. Deze wettelijke bescherming zorgt ervoor dat als uw kern LLM-aanbieder offline gaat, u niet gedwongen wordt enorme financiële boetes te betalen aan uw zakelijke klanten.

- Bouw 'LLM Fallbacks' in uw code om storingen te overleven. Als OpenAI uitvalt, moet uw code onmiddellijk en automatisch overschakelen naar het gebruik van Anthropic of Google Gemini, zodat uw app naadloos online blijft.

- AI hallucineert; het is geen perfecte rekenmachine. In uw contracten moet expliciet worden vermeld dat AI-outputs ‘adviserend’ zijn en moet de klant wettelijk verplicht zijn om menselijke werknemers het werk te laten controleren voordat er cruciale beslissingen worden genomen.

- Ga niet akkoord met snelheidsgaranties (Latency SLA's). Het genereren van complexe AI-tekst kost tijd. Beloof 'Doorvoer' (bijvoorbeeld 'We verwerken 500 rapporten per dag') in plaats van te beloven 'De chatbot zal binnen 1 seconde antwoorden'.

## Bescherm de aansprakelijkheid van uw startup

Ondertekent u standaard verouderde softwarecontracten die uw AI-startup blootstellen aan verwoestende financiële boetes wanneer LLM's van derden crashen? **LaunchStudio** adviseert technische oprichters bij het overbruggen van de kloof tussen probabilistische AI-architectuur en wettelijke vereisten voor ondernemingen, zodat u robuuste SLA's kunt opstellen en fallback-systemen van meerdere leveranciers kunt ontwikkelen die veerkracht garanderen.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’ exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: SLA-drempels voor nooduitvoering voor medische codering

Harper, een kliniekmanager, gebruikte **Bolt** om een medisch codeerhulpmiddel te bouwen. Ziekenhuisklanten eisten een SLA van 100% coderingsnauwkeurigheid, wat haar probabilistische AI-model niet kon garanderen.

Ze werkte samen met **LaunchStudio (door Manifera)** om drempelwaarden voor de betrouwbaarheidsscore en geautomatiseerde validatieroutes te implementeren.

**Resultaat:** Ziekenhuis SLA's gehaald, overeenkomsten gesloten met 3 regionale klinieken.

**Kosten en tijdlijn:** € 1.850 (SLA-verhardingspakket) — productieklaar en binnen 4 werkdagen geïmplementeerd.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Wat is een SLA (Service Level Agreement)?

Het boetebeding in een B2B-contract. Als u de klant belooft dat uw software nooit zal crashen, en deze crasht een dag lang, dwingt de SLA u om duizenden dollars terug te betalen.

### Waarom zijn standaard SLA's gevaarlijk voor AI-startups?

Omdat u bovenop de API's van andere bedrijven bouwt. Als je 100% uptime belooft, maar de servers van OpenAI in brand vliegen, breek je je belofte en verlies je geld, ook al had je daar helemaal geen controle over.

### Hoe ga je om met 'Nauwkeurigheid' in een AI-contract?

Je moet wettelijk toegeven dat AI fouten maakt. In uw contract moet staan: 'De AI zal soms hallucineren. De Klant gaat ermee akkoord dat de gegevens door een mens worden beoordeeld. Wij zijn niet aansprakelijk voor feitelijke fouten.'

### Wat is een LLM Fallback-strategie?

Een technische truc. U schrijft uw code zo dat als ChatGPT een vraag probeert te stellen en ChatGPT kapot is, de code automatisch Claude vraagt, waardoor uw app soepel blijft werken.