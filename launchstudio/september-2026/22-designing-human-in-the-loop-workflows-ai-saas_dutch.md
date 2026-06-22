---
Titel: 'Human-in-the-Loop'-workflows ontwerpen
Trefwoorden: Ontwerpen, Mens, Loop, Workflows
Koperfase: Bewustzijn
---

# 'Human-in-the-Loop'-workflows ontwerpen
De technologie-industrie is geobsedeerd door ‘Autonomous Agents’: AI-systemen die op de achtergrond draaien, beslissingen nemen en API’s uitvoeren zonder menselijke tussenkomst. Dit is een briljant concept voor een demo en een catastrofale aansprakelijkheid in een zakelijke productieomgeving. LLM's zijn probabilistisch; ze zullen uiteindelijk hallucineren. Om een ​​B2B SaaS te bouwen die bedrijven daadwerkelijk vertrouwen, moet u strikte **Human-in-the-Loop (HITL)**-goedkeuringsgateways ontwerpen.

## Het risico van autonomie in B2B

Als een AI-agent in een consumentenapp hallucineert en het verkeerde nummer aan een Spotify-afspeellijst toevoegt, slaat de gebruiker het nummer over. De kosten van falen zijn nul. 

In een B2B SaaS is de inzet existentieel. Als uw autonome ‘financiële agent’ een extra nul op een factuur hallucineert en automatisch een Stripe API-betaling van $ 50.000 in plaats van $ 5.000 activeert, wordt uw startup aangeklaagd wegens grove nalatigheid. Bedrijven zullen geen software kopen die zelfstandig destructieve acties kan uitvoeren. Je moet de uiteindelijke aansprakelijkheid van de AI terugverleggen naar de mens.

## Lees- versus schrijfbewerkingen

De regel voor autonomie is eenvoudig: **Leesbewerkingen kunnen autonoom zijn; Voor schrijfbewerkingen is een mens nodig.**

- **Lees:** Een AI kan autonoom 1000 inkomende e-mails scannen, deze classificeren en de namen van klagende klanten eruit halen. Dit is veilig. Als er een e-mail wordt gemist, is dat een kleine inefficiëntie.

- **Schrijf:** De AI stelt een restitutie-e-mail op voor de klagende klant. Het systeem MOET pauzeren. Het kan de SendGrid API niet aanroepen. Het concept moet in een dashboard in de wachtrij worden geplaatst. De menselijke klantenservicemedewerker leest het concept, past de toon aan en klikt op 'Goedkeuren en verzenden'.

## Ontwerp van de goedkeuringsgateway-gebruikersinterface

Een slecht ontworpen HITL-interface is net zo gevaarlijk als volledige autonomie. Als je de mens een enorme tekstmuur en een kleine ‘Goedkeuren’-knop voorlegt, zal de mens bezwijken voor ‘Automation Bias’. Ze gaan ervan uit dat de machine gelijk heeft, bladeren de tekst door en klikken blindelings op goedkeuren.

**Een robuuste HITL-interface moet:**

1. **Presenteren als concept:** De gebruikersinterface moet visuele aanwijzingen gebruiken (zoals een gele achtergrond of een 'concept'-watermerk) om de gebruiker er expliciet aan te herinneren dat het werk nog niet af is en mogelijk gebreken vertoont.

2. **Wijzigingen markeren (verschillen):** Laat precies zien wat de AI heeft veranderd. Als de AI een CRM-record heeft bijgewerkt, geeft u de oude gegevens in rood weer en de nieuwe door AI gegenereerde gegevens in groen. Maak de mutaties visueel duidelijk.

3. **Inline bewerken:** De gebruiker hoeft niet de hele taak te weigeren als er een klein typefoutje in zit. Zorg voor bewerkbare invoervelden, zodat de mens het concept van de AI handmatig kan aanpassen voordat hij deze goedkeurt.

## De feedbacklus (afwijzen met context)

Wanneer een gebruiker het voorstel van een AI afwijst, kun je het concept niet zomaar verwijderen en hem dwingen opnieuw te beginnen. Je moet de redenering van de mens vastleggen.

Als de mens op 'Afwijzen' klikt, zou er een modaal moeten verschijnen: *"Wat heb ik verkeerd gedaan?"* De gebruiker typt: *"Je hebt de prijscategorie van 2024 gebruikt in plaats van de prijscategorie van 2025."* Je backend onderschept deze feedback, voegt deze toe als een strikte instructie aan de oorspronkelijke prompt en dwingt de LLM om het concept onmiddellijk opnieuw te genereren. Deze "Correctieloop" traint de gebruiker om als manager op te treden en een junior medewerker te begeleiden.

## Belangrijkste afhaalrestaurants

- Volledig autonome 'Write'-agents zijn een groot probleem in B2B SaaS. Als een AI een databaseverwijdering of een financiële transactie hallucineert, wordt uw startup aansprakelijk gehouden.

- Implementeren van 'Human-in-the-Loop' (HITL)-gateways. De AI doet het zware werk (het opstellen van de e-mail, het in de wachtrij plaatsen van de transactie), maar een mens moet expliciet op 'Goedkeuren' klikken om de laatste API-aanroep uit te voeren.

- Pas de 'Lezen versus Schrijven'-regel toe: AI kan autonoom gegevens lezen en analyseren zonder toezicht, maar elke actie die gegevens wijzigt of contact opneemt met een klant moet worden onderbroken voor menselijke beoordeling.

- Ontwerp uw gebruikersinterface om 'Automation Bias' te bestrijden. Markeer duidelijk de specifieke gegevens die de AI heeft gewijzigd (met behulp van Diffs), zodat de mens hallucinaties niet blindelings goedkeurt.

- Bouw een correctielus. Als een gebruiker een AI-concept afwijst, geef dan een tekstvak op voor feedback. Voer die tekst rechtstreeks terug naar de LLM, zodat deze zijn eigen fout onmiddellijk kan corrigeren op basis van menselijke begeleiding.

## Bescherm de gegevens van uw klanten

Zijn uw autonome AI-agenten een risico dat nog moet gebeuren? **LaunchStudio** ontwerpt veilige architecturen op ondernemingsniveau met ingebouwde Human-in-the-Loop-goedkeuringsgateways, waardoor uw AI enorme efficiëntie levert zonder de gegevensintegriteit in gevaar te brengen.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’, exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: een Human-in-the-Loop-restitutiewachtrij bouwen voor een retailbot

Madison, eigenaar van een winkel, gebruikte **Lovable** om een AI-terugbetalingsbot te bouwen. De bot verwerkte af en toe terugbetalingen voor ongeldige claims, waardoor het risico bestond dat er geld zou lekken.

Ze werkte samen met **LaunchStudio (door Manifera)** om een ​​dashboardwachtrij te implementeren waarbij voor terugbetalingen van meer dan € 50 de goedkeuringsklik van een manager vereist is.

**Resultaat:** Het aantal geautomatiseerde terugbetalingsfouten is tot nul gedaald, waardoor kapitaal is veiliggesteld en 80% van de ondersteuningsgevallen automatisch is opgelost.

**Kosten en tijdlijn:** € 1.800 (Human-in-the-Loop-installatie) — gereed voor productie en geïmplementeerd binnen 4 werkdagen.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Wat is Human-in-the-Loop (HITL)?

Een architectonisch patroon waarbij een AI een complexe taak voorbereidt (zoals het opstellen van een contract), maar de software fysiek pauzeert. Een mens moet het werk van de AI beoordelen en expliciet op ‘Goedkeuren’ klikken voordat de definitieve actie wordt ondernomen.

### Waarom is HITL verplicht voor B2B-toepassingen?

Omdat LLM's hallucineren. Als een autonome AI de database van een cliënt wijzigt of een financiële transactie uitvoert op basis van een hallucinatie, is de aansprakelijkheid enorm. HITL verschuift de eindverantwoordelijkheid naar de menselijke gebruiker.

### Hoe ontwerp je een goede HITL-interface?

Presenteer de output van de AI als een duidelijk ‘concept’. Gebruik rood/groene markering om precies weer te geven welke gegevens de AI voorstelt te wijzigen, en zorg voor bewerkbare tekstvelden zodat de gebruiker gemakkelijk kleine AI-fouten kan herstellen voordat hij deze goedkeurt.

### Wat gebeurt er als de gebruiker het voorstel van de AI afwijst?

De software moet de gebruiker vragen 'Waarom?'. De schriftelijke feedback van de gebruiker wordt vervolgens als nieuwe instructie teruggevoerd naar de LLM, waardoor de AI onmiddellijk een gecorrigeerd concept kan genereren.