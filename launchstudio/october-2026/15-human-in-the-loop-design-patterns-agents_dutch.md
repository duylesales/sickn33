---
Titel: Human-in-the-Loop (HITL) ontwerppatronen voor agenten
Trefwoorden: Mens, Loop, HITL, Design, Patronen, Agenten
Koperfase: Bewustzijn
---

# Human-in-the-Loop (HITL) ontwerppatronen voor agenten
Het uiteindelijke doel van AI is totale automatisering, maar totale automatisering is momenteel een enorme uitdaging. Als een volledig autonome agent API-sleutels krijgt voor uw CRM- en e-mailserver, kan een enkele LLM-hallucinatie ertoe leiden dat vertrouwelijke contracten naar de verkeerde klant worden gemaild. Enterprise CISO's zullen uw software niet kopen als deze een systeemrisico met zich meebrengt. Om AI aan de onderneming te verkopen, moet u strikte, onoverkomelijke **Human-in-the-Loop (HITL)**-workflows ontwerpen.

## De grens tussen 'lezen en schrijven'

Niet elke actie vereist een mens. De basis van de HITL-architectuur is het verdelen van de tools van uw agent in twee strikte categorieën: alleen-lezen en statusmuterend.

Als de Agent besluit het hulpmiddel `query_database()` te gebruiken om een ​​bestand te lezen, kan hij dit autonoom doen. Het lezen van gegevens kan het bedrijf niet vernietigen. Als de Agent echter besluit om de tools `send_email()` of `issue_stripe_refund()` te gebruiken, overschrijdt hij de grens. De backend-architectuur moet de API-oproep onderscheppen, de uitvoering fysiek blokkeren en een HITL-breekpunt activeren.

## Het breekpunt ontwerpen (staatsopschorting)

Wanneer de agent een statusmuterende actie probeert, voert uw Node.js-backend deze niet uit. In plaats daarvan wordt de agent geschorst. Het neemt het volledige geheugen en de status van de agent en serialiseert deze in een database (zoals Redis of Postgres).

De backend stuurt vervolgens een waarschuwing naar de gebruikersinterface van de menselijke gebruiker: *"De agent heeft een terugbetaling van $ 500 aan klant X opgesteld. Gaat u hiermee akkoord?"*

Het LLM-proces is gedurende deze tijd feitelijk dood. Er ontstaan ​​geen API-kosten tijdens het wachten. Het kan 5 seconden of 5 dagen wachten. Wanneer de mens uiteindelijk op 'Goedkeuren' klikt, haalt de backend de status op uit de database, herleeft de agent en geeft het expliciete autorisatietoken van de mens door, waardoor de uitvoering kan doorgaan.

## Het bewerkingsoverschrijvingspatroon

Een simpele knop "Goedkeuren/Afwijzen" is een slechte gebruikerservaring. Als de AI een ongelooflijke e-mail van vijf alinea's opstelt, maar één zin fout heeft, hoeft de mens niet op 'Weigeren' te klikken en het hele generatieproces van vijf minuten opnieuw te beginnen.

Het beste HITL-ontwerppatroon is **Editing Override**. De gebruikersinterface presenteert de beoogde actie van de AI in een bewerkbaar tekstvak. De mens corrigeert de enige slechte zin en klikt op 'Goedkeuren met bewerkingen'. De backend injecteert de gecorrigeerde versie van de mens rechtstreeks in de payload van de toolcall, waardoor de fout van de LLM wordt omzeild en de mens 99% van de handmatige arbeid wordt bespaard.

## Marketingveiligheid als kenmerk

Oprichters beschouwen HITL vaak als een technische beperking, een onvermogen om 'echte AI' te bereiken. Dit is de verkeerde mentaliteit. In B2B SaaS is HITL uw grootste marketingmiddel.

Kopers van ondernemingen zijn doodsbang voor autonome aansprakelijkheid. Wanneer u uw software demonstreert, verbergt u de HITL-pauze niet; jij benadrukt het. U zegt tegen de CISO: *"Onze AI doet het zware werk, maar het is fysiek onmogelijk voor onze software om uw gegevens te muteren zonder expliciete cryptografische goedkeuring van uw managers."* Deze veiligheidsgarantie is wat het contract afsluit.

## Belangrijkste afhaalrestaurants

- Totale AI-autonomie is gevaarlijk. Een hallucinerende agent met toegang tot 'Write'-API's kan databases vernietigen of ongepaste e-mails verzenden. U moet de onderneming beschermen met Human-in-the-Loop (HITL)-breekpunten.

- Verdeel uw gereedschap naar risico. Laat de Agent autonoom gegevens zoeken en lezen. Maar codeer uw backend zodanig dat u elk hulpmiddel dat de staat muteert (gegevens verzenden, geld overmaken) blokkeert totdat een mens het expliciet goedkeurt.

- Wanneer een agent een HITL-breekpunt bereikt, schort u de status ervan in een database op. Houd de LLM-verbinding niet open terwijl u op de mens wacht (wat time-outs veroorzaakt). Breng de agent pas weer tot leven nadat de mens op Goedkeuren heeft geklikt.

- Implementeer het patroon 'Editing Override'. Als u de mens om goedkeuring vraagt, laat hem dan de voorgestelde actie van de AI (zoals het corrigeren van een typefout in een concept-e-mail) bewerken voordat deze wordt uitgevoerd, waardoor de gebruikersefficiëntie wordt gemaximaliseerd.

- Verberg HITL niet; het zwaar op de markt brengen. Zakelijke kopers zijn doodsbang voor malafide AI. Bewijzen dat uw AI geen destructieve acties kan ondernemen zonder menselijke goedkeuring is de sleutel tot het binnenhalen van enorme B2B-contracten.

## Garandeer de AI-veiligheid van ondernemingen

Zijn uw autonome agenten een enorme aansprakelijkheid die nog moet gebeuren? **LaunchStudio** ontwikkelt ondoordringbare backend-architecturen, implementeert strikte Human-in-the-Loop-breekpunten, status-opschortingsprotocollen en 'lezen/schrijven'-toolscheiding om te garanderen dat uw AI-producten de veiligheidseisen van zakelijke CISO's overtreffen.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’ exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: implementatie van goedkeuringswachtrij voor een factuurbot

Daniel, een accountant, gebruikte **Cursor** om een betalingsagent te bouwen. Hij vreesde voor lancering omdat de bot betalingen automatisch verwerkte op basis van ruwe factuurgegevens.

Hij werkte samen met **LaunchStudio (door Manifera)** om een ​​'human-in-the-loop'-goedkeuringspanel op te zetten, waarbij voor transacties boven € 100 toestemming van de manager vereist is.

**Resultaat:** Voorkom meer dan € 12.000 aan betalingsfouten en automatiseer 90% van de gegevensverwerkingstaken.

**Kosten en tijdlijn:** € 2.500 (Human-in-the-Loop-installatie) — klaar voor productie en geïmplementeerd binnen 5 werkdagen.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Wat is Human-in-the-Loop (HITL)?

Een veiligheidsprotocol waarbij de AI 90% van het werk doet (onderzoeken, opstellen), maar het systeem helemaal aan het einde een pauze afdwingt, waardoor een mens op 'Goedkeuren' moet klikken voordat de actie daadwerkelijk in de echte wereld plaatsvindt.

### Waarom is HITL verplicht voor Enterprise AI?

Betrouwbaarheid. Als een volledig autonome AI hallucineert en een beledigende e-mail naar je grootste klant stuurt, raak je de klant kwijt. HITL zorgt ervoor dat een mens de fout van de AI opmerkt voordat er schade wordt aangericht.

### Wat is een 'High-Risk'-tooloproep?

Alles dat gegevens verandert of interactie heeft met de buitenwereld. Het lezen van een bestand is veilig. Het verwijderen van een bestand, het terugbetalen van geld of het verzenden van een Slack-bericht zijn risicovolle acties waarvoor een menselijk breekpunt nodig is.

### Hoe 'pauzeert' de agent?

De backend slaat de exacte voortgang van de AI op in een database en gaat in de slaapstand. Wanneer de mens later inlogt en op 'Goedkeuren' klikt, wekt de backend de AI weer op en vertelt hem dat hij de taak moet voltooien.