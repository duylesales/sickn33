---
Titel: "Klantenondersteuning Automatiseren in Intercom: Een AI Deployment Draaiboek voor Oprichters"
Trefwoorden: Intercom AI automatisering, klantenservice AI, Intercom Fin, custom AI bot, LaunchStudio, Manifera
Koperfase: Bewustzijn
Doelgroep: Customer Success Leads / Operations / Founders
---

# Klantenondersteuning Automatiseren in Intercom: Een AI Deployment Draaiboek voor Oprichters

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Klantenondersteuning Automatiseren in Intercom: Een AI Deployment Draaiboek voor Oprichters",
  "description": "Schaal klantenondersteuning van 1.000 naar 10.000 gebruikers met veilige Intercom AI-workflows en menselijke escalatiepaden.",
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
  "datePublished": "2026-08-16",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/automating-customer-support-intercom-ai"
  }
}
</script>

Een van de meest riskante fasen in de groei van een SaaS-bedrijf is de overgang van 1.000 naar 10.000 actieve gebruikers. Terwijl serverkosten logaritmisch schalen, groeit de vraag naar klantenservice lineair. Zonder gerichte automatisering besteedt uw engineeringteam een groot deel van de week aan het beantwoorden van tickets zoals "Hoe reset ik mijn wachtwoord?" in plaats van aan het doorontwikkelen van uw kernproduct. In 2026 is het inzetten van een autonome AI-supportagent via Intercom of Zendesk geen overbodige luxe meer; het is een structurele voorwaarde voor winstgevendheid, en de onderliggende architectuur vereist aanzienlijk meer diepgang dan het simpelweg inschakelen van een chatbot-widget.

## Verder dan de Beslisboom

Gebruikers hebben een hekel aan traditionele chatbots. De rigide beslisbomen met "Druk op 1 voor Verkoop, Druk op 2 voor Support" voelen bureaucratisch en frustrerend aan. Moderne AI-supportagenten (zoals Fin van Intercom) werken fundamenteel anders. Ze maken gebruik van Large Language Models die via Retrieval-Augmented Generation (RAG) direct zijn gekoppeld aan uw specifieke kennisbank.

Wanneer een gebruiker typt: *"Hoi, ik heb per ongeluk het project verwijderd waar ik gisteren aan werkte, kunnen jullie dit herstellen?"*

De AI begrijpt direct de intentie, doorzoekt uw interne documentatie op "data recovery", stelt vast dat uw platform verwijderde projecten 30 dagen in een prullenbak bewaart, en antwoordt binnen enkele seconden met gepersonaliseerde instructies waarmee de gebruiker het project zelf direct kan herstellen. Het ticket is opgelost zonder tussenkomst van een menselijke medewerker. Het mechanisme hierachter is een vectorzoekopdracht over uw Help Center-content - de AI "kent" uw product niet uit het hoofd, maar haalt de drie of vier meest relevante documentatiefragmenten op en formuleert daar een betrouwbaar antwoord op. Daarom bepaalt de kwaliteit van uw documentatie direct de kwaliteit van de AI-antwoorden.

## De AI 'Handen' Geven (Actions & Webhooks)

Een AI die uitsluitend tekstuele antwoorden geeft, is een "Tier 0"-agent. Om volwaardige "Tier 1"-automatisering te bereiken, moet u de AI in staat stellen om daadwerkelijk acties uit te voeren. Dit gebeurt via API-webhooks (binnen Intercom aangeduid als Actions of Fin AI Actions) - gestructureerde functiedefinities die het LLM tijdens het gesprek kan aanroepen.

U kunt uw AI-agent bijvoorbeeld direct koppelen aan Stripe en uw backend-database. Vraagt een gebruiker: "Kan ik een terugbetaling krijgen?", dan kan de AI autonoom:

1. Stripe raadplegen om de meest recente betaling en transactiedatum van de gebruiker op te halen.
2. Controleren of deze datum binnen uw officiële retourtermijn valt (als harde bedrijfsregel vastgelegd in de actieprompt, niet overgelaten aan de willekeur van het model).
3. Indien goedgekeurd, een POST-verzoek sturen naar uw backend om het account te downgraden, en een POST-verzoek naar Stripe om de terugbetaling direct uit te voeren.
4. Antwoorden naar de klant: *"Ik heb de terugbetaling verwerkt, het bedrag staat binnen 3 tot 5 werkdagen op uw rekening."*

Deze mate van autonome afhandeling kan 50% tot 60% van uw dagelijkse ticketvolume wegnemen. De cruciale architectuurbeslissing is het zorgvuldig afbakenen van welke acties de AI volledig autonoom mag uitvoeren versus welke acties een menselijke bevestiging vereisen; een automatische restitutie van € 5 is immers heel iets anders dan het zonder controle beëindigen van een zakelijk enterprise-contract van € 2.000 per maand.

## Het Escalatieprotocol

AI moet niet alles zelfstandig willen oplossen. Waardevolle enterprise-klanten of sterk gefrustreerde gebruikers vereisen menselijke empathie en onderhandeling. Uw AI-agent moet daarom beschikken over een strikt geconfigureerd **Escalatieprotocol**.

U stelt de AI zo in dat deze continu het sentiment van de gebruiker analyseert. Detecteert de AI boosheid (bijv. typen in hoofdletters, agressief taalgebruik, of wanneer dezelfde vraag tweemaal onopgelost blijft), dan stopt de AI direct en routeert deze het gesprek direct door naar de "Urgent Human Support"-wachtrij, inclusief een samenvatting van wat er al geprobeerd is. Ook wanneer de RAG-zoekopdracht onvoldoende betrouwbare bronnen in de kennisbank vindt, moet het systeem direct overdragen aan een menselijke specialist in plaats van een onjuist antwoord te hallucineren - een AI die vol zelfvertrouwen verkeerde instructies geeft, richt veel meer schade aan dan een AI die eerlijk aangeeft dat een medewerker het overneemt.

## De Kennisbank Bouwen en Onderhouden

Een AI-supportagent is slechts zo intelligent als de data die u erin stopt. De grootste fout die oprichters maken, is het activeren van de AI zonder eerst hun Help Center grondig te auditen. Bevat uw kennisbank verouderde artikelen uit 2024, dan zal de AI vol overtuiging verouderde instructies geven aan klanten.

Vóór de livegang moet alle documentatie herschreven worden tot heldere, feitelijke en actuele artikelen. Richt tevens een vast proces in waarbij elke productrelease automatisch leidt tot een update van de helpdocumentatie. Beschouw uw Help Center niet alleen als leesvoer voor mensen, maar als de letterlijke broncode voor het brein van uw AI: elke dubbelzinnige zin en elk verouderd screenshot degradeert direct de antwoorden die de AI aan uw klanten geeft.

## Wat is een AI-supportagent?

Een AI-supportagent is een large language model dat klantvragen in uw supportkanaal beantwoordt door antwoorden op te halen uit uw eigen documentatie en, optioneel, door uw API's aan te roepen om namens de klant acties uit te voeren. Anders dan een beslisboom-chatbot begrijpt deze agent vrij geformuleerde vragen; anders dan een menselijke medewerker weet de agent alleen wat uw kennisbank en gekoppelde systemen hem vertellen.

In de praktijk omvat de term drie lagen die u afzonderlijk configureert: de **antwoordlaag** (RAG over uw Help Center), de **actielaag** (webhooks of Fin AI Actions richting Stripe en uw backend) en de **routeringslaag** (de escalatieregels die bepalen wanneer een mens het overneemt). De meeste mislukte implementaties hebben een sterke antwoordlaag en een zwakke routeringslaag.

## Intercom AI-automatisering uitrollen: een plan in 7 stappen

De veiligste uitrol van AI in Intercom verloopt geleidelijk: eerst antwoorden, later acties, en eerst een beperkte doelgroep voordat iedereen toegang krijgt. Deze volgorde werkt voor de meeste SaaS-producten:

1. **Analyseer uw tickets.** Exporteer de gesprekken van enkele maanden en groepeer ze per onderwerp. De tien grootste categorieën laten meestal zien waar automatisering zich terugverdient en welke Help Center-artikelen ontbreken.
2. **Herstel eerst de documentatie.** Herschrijf of voeg de artikelen achter die categorieën samen voordat de AI ze ooit leest, volgens de kennisbankregels hierboven.
3. **Koppel contentbronnen.** Laat Fin (of uw eigen agent) alleen bronnen gebruiken die u vertrouwt: het publieke Help Center en interne fragmenten die specifiek voor de AI zijn geschreven. Laat oude interne wiki's buiten beschouwing.
4. **Test met echte historie.** Speel intern een steekproef van eerdere vragen opnieuw af en beoordeel elk antwoord op juistheid, toon en correcte escalatie.
5. **Lanceer voor een segment.** Gebruik de doelgroepinstellingen van Intercom om de agent eerst voor een deel van uw gebruikers in te schakelen, bijvoorbeeld gebruikers met een gratis abonnement of één taal, voordat u hem uitrolt naar betalende enterprise-accounts.
6. **Voeg alleen-lezen-acties toe.** Begin met acties die alleen gegevens opzoeken, zoals "controleer mijn abonnementsstatus" of "zoek mijn laatste factuur".
7. **Voeg schrijfacties toe met vangrails.** Schakel pas daarna acties in die data wijzigen, zoals terugbetalingen of abonnementswijzigingen, met harde limieten en bevestigingsstappen zoals beschreven in de volgende sectie.

## Welke acties mag de AI uitvoeren?

Laat de AI alleen autonoom handelen waar een fout goedkoop en omkeerbaar is, en vereis overal elders een mens of een expliciete bevestiging. Een eenvoudige risicotabel maakt deze beslissing zichtbaar voor het hele team:

| Type actie | Voorbeeld | Risico bij een fout | Aanbevolen autonomie |
|---|---|---|---|
| Alleen opzoeken | Abonnementsstatus tonen, datum laatste factuur | Laag | Volledig autonoom |
| Zelfservice-uitleg | Uitleggen hoe een verwijderd project wordt hersteld | Laag | Volledig autonoom |
| Kleine omkeerbare wijziging | Verificatiemail opnieuw sturen, instelling resetten | Laag tot gemiddeld | Autonoom, met logging |
| Kleine financiële actie | Terugbetaling onder een vast bedrag binnen het beleid | Gemiddeld | Autonoom binnen hard gecodeerde limieten |
| Grote financiële actie | Terugbetaling boven de limiet, wijziging jaarabonnement | Hoog | Menselijke goedkeuring vereist |
| Contract of verwijdering van data | Enterprise-contract opzeggen, account verwijderen | Zeer hoog | Alleen door een mens |

Twee technische regels houden deze tabel eerlijk. Ten eerste dwingt u de limieten af in uw backend en niet alleen in de prompt, want een prompt kan worden omzeild en een `if`-statement niet. Ten tweede moet elke actie worden uitgevoerd voor de **geverifieerde** gebruiker. Schakel de identiteitsverificatie van Intercom in (een HMAC-hash van het gebruikers-ID die op uw server wordt gegenereerd) en laat uw actie-endpoints dat geverifieerde ID gebruiken, nooit een accountnummer of e-mailadres dat de klant in de chat heeft getypt.

## Hoe meet u of support-automatisering werkt?

U meet AI-support aan de kwaliteit van de oplossingen, niet aan het aantal gesprekken dat de bot heeft aangeraakt. Een bot die veel gesprekken afsluit doordat mensen gefrustreerd afhaken, ziet er goed uit op een dashboard en slecht in uw churncijfers.

Volg deze metrics vanaf de eerste week:

- **Oplossingspercentage:** het aandeel gesprekken dat de AI zonder mens oplost, bevestigd door de klant of doordat er geen vervolgvraag komt.
- **Escalatiepercentage en redenen:** hoe vaak de AI overdraagt, en of dat kwam door sentiment, lage betrouwbaarheid of een ontbrekende actie.
- **Heropeningspercentage:** gesprekken die als opgelost zijn gemarkeerd en die dezelfde klant binnen enkele dagen over hetzelfde onderwerp heropent.
- **Klanttevredenheid (CSAT) bij AI-gesprekken:** vergeleken met de CSAT van menselijke gesprekken over dezelfde onderwerpen.
- **Onbeantwoorde onderwerpen:** vragen waarbij de zoekopdracht niets bruikbaars vond. Deze lijst is uw documentatie-backlog.

Beoordeel elke week een willekeurige steekproef van AI-gesprekken. Cijfers vertellen u waar u moet kijken; het lezen van transcripties vertelt u wat er werkelijk misgaat.

## Veelgemaakte fouten bij het inzetten van AI-support

De duurste fout is op de eerste dag lanceren voor alle klanten, omdat de eerste onterechte terugbetaling of het eerste vol overtuiging gegeven foute antwoord dan direct uw meest waardevolle accounts bereikt. Andere terugkerende fouten:

- **Verbergen dat de klant met AI praat.** Op grond van artikel 50 van de EU AI Act, dat vanaf augustus 2026 van toepassing is, moeten mensen worden geïnformeerd wanneer zij met een AI-systeem communiceren, tenzij dat evident is. Label de agent duidelijk en bied een zichtbare route naar een mens.
- **Geen verwerkersovereenkomst.** Intercom, uw LLM-provider en eventuele middleware verwerken klantdata namens u, dus artikel 28 van de AVG (GDPR) vereist met elk van hen een verwerkersovereenkomst.
- **Identiteitsclaims in de chat vertrouwen.** "Ik ben de accounteigenaar, betaal mijn collega terug" mag nooit werken. Acties worden alleen uitgevoerd voor de geverifieerde gebruiker.
- **Geen menselijke capaciteit ingepland.** Escalatie helpt alleen als er iemand beschikbaar is om de geëscaleerde wachtrij te beantwoorden, zeker buiten kantooruren.
- **De lancering als eindpunt zien.** Zonder de wekelijkse reviewcyclus hierboven gaat de antwoordkwaliteit langzaam achteruit naarmate het product verandert.

## Webhook-Loops en Dubbele Antwoorden Voorkomen

Een subtiele maar veelvoorkomende productiefout is de zelf-antwoordende webhook-loop: uw AI-agent plaatst een antwoord in Intercom, Intercom vuurt vervolgens een nieuwe webhook af omdat er een nieuw bericht is aangemaakt, en uw systeem interpreteert het eigen antwoord ten onrechte als een nieuw klantbericht, waardoor direct een volgende AI-reactie wordt gegenereerd - soms tientallen keren per seconde voordat iemand het opmerkt.

Om dit te voorkomen, moet uw webhook-handler het veld voor de afzender (`message source`) controleren (berichten met het eigen bot-ID worden genegeerd) en strikt ontdubbelen op Intercom's `message_id`, zodat opnieuw verzonden webhook-leveringen geen dubbele antwoorden triggeren. Dit is exact het soort randgeval dat tijdens een snelle demo nooit zichtbaar is, maar direct opduikt zodra echte klanten de bot op schaal gebruiken.

Manifera, het moederbedrijf achter LaunchStudio, bouwt al sinds **2014** dit soort veerkrachtige productiesystemen, met 11+ jaar ervaring en meer dan 160 opgeleverde projecten voor enterprise-klanten zoals Vodafone en TNO. "We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten naar volwassenheid te brengen. Wij hebben elf jaar ervaring in exact dat vakgebied," zegt Herre Roelevink, Oprichter & Managing Director van Manifera. Aangezien circa 80% van de met AI gebouwde projecten nooit een stabiele productierelease haalt, is een ongecontroleerde webhook-loop een veelvoorkomende, vermijdbare reden waarom support-automatisering al in de eerste week wordt uitgeschakeld.

## Belangrijkste Inzichten

- Handmatige support groeit lineair en put uw engineeringcapaciteit uit; slimme automatisering is essentieel om uw SaaS winstgevend te schalen.
- Moderne AI-agenten gebruiken natuurlijke taalverwerking en RAG om nauwkeurige antwoorden te geven op basis van uw eigen Help Center, waarmee rigide beslisboom-chatbots definitief verleden tijd zijn.
- Door de AI toegang te geven tot API-webhooks (Actions) kan deze zelfstandig taken uitvoeren zoals terugbetalingen verwerken of accounts upgraden - mits risicovolle acties strikt worden afgebakend.
- Implementeer een direct escalatieprotocol: stuur gefrustreerde gebruikers en vragen met lage betrouwbaarheidsscores direct door naar een menselijke medewerker inclusief gesprekscontext.
- Ontdubbel op bericht-ID's om webhook-loops te voorkomen en houd uw Help Center continu up-to-date als betrouwbare bron voor het AI-model.

## Schaal Uw Support, Niet Uw Personeelsbestand

Laat supporttickets uw ontwikkelaars niet weghouden bij het bouwen van uw product. **LaunchStudio** implementeert intelligente, autonome AI-supportagenten in Intercom en Zendesk, standaard uitgerust met robuuste ontdubbelings- en escalatielogica. Bekijk de [LaunchStudio pakketten](https://launchstudio.eu/nl/#packages) voor heldere, fixed-scope tarieven voor support-automatisering.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht in **2014** door **Herre Roelevink**. Vanuit het inzicht in het tekort aan ervaren softwareontwikkelaars in Europa, richtte Herre ontwikkelingshubs op in **Singapore** en **Ho Chi Minhstad, Vietnam**, om hoogwaardig engineeringtalent in te zetten. Geleid door de filosofie van het combineren van "Nederlands management met Vietnamees meesterschap", opereert Manifera haar Europese hoofdkantoor aan de **Herengracht 420, 1017 BZ Amsterdam, Nederland**. Via LaunchStudio krijgen AI-native oprichters direct toegang tot deze enterprise-grade software-expertise om hun prototypes binnen 1 tot 3 weken veilig, schaalbaar en lanceringsklaar te maken. [Vraag vandaag nog een vrijblijvende offerte aan](https://launchstudio.eu/nl/#contact).

## Echt voorbeeld

### Een AI-Native Oprichter in Actie: Oplossen van een Support Webhook-Loop voor een Retail SaaS

Evelyn, eigenaar van een e-commerce platform, gebruikte **Lovable** om een geautomatiseerde klantenservice-bot te bouwen. De bot raakte echter verstrikt in een oneindige antwoordlus bij interactie met de webhook van Intercom.

Zij schakelde **LaunchStudio (door Manifera)** in. Het team implementeerde afzenderverificatie en ontdubbelingstags om zelf-antwoorde loops definitief uit te sluiten.

**Resultaat:** Automatische ticketoplossing steeg naar 45% zonder dubbele reacties of oneindige loops.

**Kosten & Tijdlijn:** €1.250 (Webhook Loop Fix Pakket) - productieklaar en binnen 3 werkdagen live opgeleverd.

---

## Veelgestelde Vragen

### Wat is het verschil tussen een traditionele chatbot en een AI-supportagent?

Ouderwetse chatbots werken met rigide beslisbomen en vooraf geprogrammeerde antwoorden. Een AI-supportagent maakt gebruik van LLM's die via RAG zijn gekoppeld aan uw Help Center. Hierdoor begrijpt de agent natuurlijke taal en levert deze contextuele, zeer specifieke antwoorden die gegrond zijn in uw daadwerkelijke documentatie.

### Hoe weet een AI-agent de antwoorden op vragen over mijn specifieke product?

De agent gebruikt Retrieval-Augmented Generation (RAG). Bij een klantvraag doorzoekt het systeem eerst uw Help Center-artikelen en eerder opgeloste supporttickets, haalt de meest relevante tekstfragmenten op en formuleert uitsluitend op basis van die bronnen een betrouwbaar antwoord, in plaats van te gissen met algemene trainingsdata.

### Kan een AI-supportagent ook zelfstandig acties uitvoeren, zoals het verwerken van terugbetalingen?

Ja. Moderne AI-agenten kunnen via beveiligde API-actions acties triggeren. De agent kan bijvoorbeeld in Stripe een betaling verifiëren en autonoom een terugbetaling initiëren als dit binnen uw gestelde beleidskaders valt. Voor transacties met een hoger financieel risico wordt doorgaans een menselijke fiatteringsstap ingebouwd.

### Wanneer moet de AI-agent een gesprek overdragen aan een menselijke medewerker?

De AI dient eerstelijns support af te handelen (zoals wachtwoordresets of veelvoorkomende factuurvragen). Zodra het systeem sterke klantfrustratie detecteert, de betrouwbaarheidsscore van de kennisbank te laag is of er sprake is van een complex technisch probleem, moet het gesprek direct worden overgedragen aan een menselijke specialist, inclusief de volledige gespreksgeschiedenis en context.

### Hoe verhoudt LaunchStudio zich tot Manifera bij het bouwen van support-automatisering?

LaunchStudio is het productized dienstenaanbod van Manifera voor AI-native oprichters. Het versterkt en beveiligt de backend van een bestaand AI-prototype (webhook-afhandeling, ontdubbeling, action-scoping en encryptie) zonder dat u de frontend opnieuw hoeft te bouwen. Hierbij wordt geput uit dezelfde 11+ jaar ervaring en meer dan 160 opgeleverde enterprise softwareprojecten van Manifera sinds 2014. Lees meer over [Manifera's maatwerk softwareontwikkeling](https://www.manifera.com/services/custom-software-development/).

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is het verschil tussen een traditionele chatbot en een AI-supportagent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ouderwetse chatbots werken met rigide beslisbomen en vooraf geprogrammeerde antwoorden. Een AI-supportagent maakt gebruik van LLM's die via RAG zijn gekoppeld aan uw Help Center. Hierdoor begrijpt de agent natuurlijke taal en levert deze contextuele, zeer specifieke antwoorden die gegrond zijn in uw daadwerkelijke documentatie."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe weet een AI-agent de antwoorden op vragen over mijn specifieke product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De agent gebruikt Retrieval-Augmented Generation (RAG). Bij een klantvraag doorzoekt het systeem eerst uw Help Center-artikelen en eerder opgeloste supporttickets, haalt de meest relevante tekstfragmenten op en formuleert uitsluitend op basis van die bronnen een betrouwbaar antwoord, in plaats van te gissen met algemene trainingsdata."
      }
    },
    {
      "@type": "Question",
      "name": "Kan een AI-supportagent ook zelfstandig acties uitvoeren, zoals het verwerken van terugbetalingen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. Moderne AI-agenten kunnen via beveiligde API-actions acties triggeren. De agent kan bijvoorbeeld in Stripe een betaling verifiëren en autonoom een terugbetaling initiëren als dit binnen uw gestelde beleidskaders valt. Voor transacties met een hoger financieel risico wordt doorgaans een menselijke fiatteringsstap ingebouwd."
      }
    },
    {
      "@type": "Question",
      "name": "Wanneer moet de AI-agent een gesprek overdragen aan een menselijke medewerker?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De AI dient eerstelijns support af te handelen (zoals wachtwoordresets of veelvoorkomende factuurvragen). Zodra het systeem sterke klantfrustratie detecteert, de betrouwbaarheidsscore van de kennisbank te laag is of er sprake is van een complex technisch probleem, moet het gesprek direct worden overgedragen aan een menselijke specialist, inclusief de volledige gespreksgeschiedenis en context."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe verhoudt LaunchStudio zich tot Manifera bij het bouwen van support-automatisering?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LaunchStudio is het productized dienstenaanbod van Manifera voor AI-native oprichters. Het versterkt en beveiligt de backend van een bestaand AI-prototype (webhook-afhandeling, ontdubbeling, action-scoping en encryptie) zonder dat u de frontend opnieuw hoeft te bouwen. Hierbij wordt geput uit dezelfde 11+ jaar ervaring en meer dan 160 opgeleverde enterprise softwareprojecten van Manifera sinds 2014. Lees meer over Manifera's maatwerk softwareontwikkeling."
      }
    }
  ]
}
</script>

