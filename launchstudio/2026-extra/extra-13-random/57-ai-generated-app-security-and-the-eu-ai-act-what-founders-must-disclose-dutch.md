---
Titel: "Beveiliging van AI-Apps en de EU AI Act: Wat Oprichters Moeten Vermelden"
Trefwoorden: ai gegenereerde app beveiliging, eu ai act, ai transparantieverplichtingen, chatbot vermelding, ai voorwaarden, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Beveiliging van AI-Apps en de EU AI Act: Wat Oprichters Moeten Vermelden

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Beveiliging van AI-Apps en de EU AI Act: Wat Oprichters Moeten Vermelden",
  "description": "De Europese AI-verordening (EU AI Act) reguleert vooral hoe AI wordt gebruikt, niet hoe software is gebouwd. Dit artikel legt uit wat dit betekent voor apps met AI-functionaliteiten: risicocategorieën, transparantieplichten voor chatbots, hoog-risico toepassingen en de link met app-beveiliging en de AVG.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-26",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-generated-app-security-and-the-eu-ai-act-what-founders-must-disclose" }
}
</script>

Een veelgehoorde zorg bij oprichters die hun app met AI hebben gebouwd: "Valt ik onder de EU AI Act omdat een AI mijn code heeft geschreven?" In bijna alle gevallen: nee. De AI Act reguleert AI-systemen op basis van wat ze doen en hoe ze worden gebruikt, niet op basis van hoe de software eromheen tot stand kwam. Maar veel AI-gebouwde apps bevatten ook AI-functies — een chatbot, een aanbevelingssysteem, gegenereerde tekst of afbeeldingen, geautomatiseerde scoring — en die kunnen echte verplichtingen met zich meebrengen. Dit artikel zet op een rij wat wel en niet geldt, en hoe het samenhangt met de beveiliging van AI-gegenereerde apps.

Dit is een overzicht voor oprichters, geen juridisch advies.

## Bouwen met AI versus AI Aanbieden

**Lovable, Bolt of Cursor gebruiken om je code te schrijven** maakt je app op zichzelf geen AI-systeem onder de AI Act. Je verplichtingen voor die code komen uit andere regels: de AVG, het consumentenrecht, verwachtingen rond beveiliging en contracten.

**AI-functies aan gebruikers aanbieden** — de app gebruikt zelf een model om te chatten, te genereren, te classificeren, aan te bevelen of te beslissen — kan je app, of delen ervan, een AI-systeem binnen de reikwijdte maken. Waar het om gaat, is de risicocategorie van het gebruik.

## De Risicocategorieën in het Kort

**Verboden praktijken.** Een korte lijst toepassingen is volledig verboden, zoals manipulatieve technieken die aanzienlijke schade veroorzaken, sociale scoring en bepaalde vormen van biometrische identificatie en emotieherkenning op de werkplek en in het onderwijs. Weinig apps van oprichters komen hier in de buurt, maar functies voor emotieherkenning in HR- of onderwijsapps verdienen zorg.

**Toepassingen met een hoog risico.** AI die wordt gebruikt in specifieke gebieden die in de wet worden genoemd — waaronder werving en personeelsbeheer, toegang tot onderwijs en beoordeling, kredietwaardigheid, toegang tot essentiële diensten en sommige veiligheidscomponenten — heeft een hoog risico. De verplichtingen omvatten risicobeheer, databeheer, documentatie, logging, menselijk toezicht, nauwkeurigheid en beveiliging.

**Transparantieverplichtingen.** Bij bepaalde systemen moeten gebruikers worden geïnformeerd: mensen moeten weten wanneer ze met een AI-systeem zoals een chatbot communiceren (tenzij dat evident is), en door AI gegenereerde of gemanipuleerde content — synthetische audio, afbeeldingen, video en in sommige gevallen tekst die wordt gepubliceerd om het publiek te informeren — moet als zodanig worden gemarkeerd of vermeld.

**Minimaal risico.** De meeste andere AI-functies — spamfilters, eenvoudige aanbevelingen, schrijfhulp — hebben geen specifieke verplichtingen buiten het algemene recht, al bestaan er vrijwillige gedragscodes.

De verplichtingen van de wet gaan gefaseerd in over meerdere jaren; de transparantieplichten en veel eisen voor hoog risico gelden vanaf augustus 2026, met sommige categorieën met een hoog risico later.

## Wat de Meeste Apps van Oprichters Moeten Doen

Voor typische AI-functies in apps van oprichters zijn de praktische eisen:

- **Vertel gebruikers dat ze met AI praten.** Een duidelijke aanduiding in de chatinterface, niet weggestopt in de voorwaarden.
- **Label gegenereerde content waar vereist.** Vooral synthetische afbeeldingen, audio of video, en gegenereerde tekst die wordt gepubliceerd over zaken van algemeen belang.
- **Vermijd onbedoelde toepassingen met een hoog risico.** Een tool voor "cv-feedback" die door kandidaten wordt gebruikt, is iets anders dan een tool die kandidaten voor werkgevers rangschikt. Weet welke van de twee je bouwt.
- **Documenteer wat de AI doet.** Welk model, voor welk doel, welke data erin gaat, wat eruit komt en welke menselijke controles er zijn.

## Waar de AI Act de Beveiliging van AI-Gegenereerde Apps Raakt

Voor systemen met een hoog risico eist de wet uitdrukkelijk passende nauwkeurigheid, robuustheid en cybersecurity, inclusief weerbaarheid tegen pogingen het systeem te manipuleren — wat prompt-injectie en datavergiftiging omvat. Ook bij functies met een lager risico overlappen de beveiliging van AI-gegenereerde apps en naleving van de AI Act in de praktijk:

- **Prompt-injectie** kan een chatbot laten ontsporen, data laten lekken of ongeautoriseerde acties laten uitvoeren. Architecturale maatregelen — minimale rechten, afgebakend ophalen, bevestiging van acties — zijn zowel beveiligings- als verantwoorde-AI-maatregelen.
- **Logging** van AI-invoer en -beslissingen ondersteunt zowel incidentonderzoek als de registratie onder de AI Act, binnen de grenzen van de AVG.
- **Menselijk toezicht** bij beslissingen met gevolgen beschermt gebruikers en vermindert de juridische blootstelling onder zowel de AI Act als de AVG-regels voor geautomatiseerde besluiten.

## Waar de AI Act de AVG Raakt

Als AI-functies persoonsgegevens verwerken, geldt de AVG volledig: een rechtsgrond, transparantie in de privacyverklaring (inclusief welke AI-aanbieder data verwerkt), dataminimalisatie, verwerkersovereenkomsten en beperkingen op uitsluitend geautomatiseerde besluiten met aanzienlijke gevolgen (artikel 22). In de praktijk blijft de AVG de regel waarmee de meeste apps van oprichters het meest direct te maken hebben.

## Een Korte Actielijst

1. Maak een lijst van elke AI-functie in je app en wat die doet.
2. Bepaal voor elke functie de waarschijnlijke risicocategorie; vraag advies voor alles wat raakt aan werving, onderwijs, krediet of essentiële diensten.
3. Voeg duidelijke AI-vermeldingen toe in chatinterfaces en label gegenereerde media.
4. Werk je privacyverklaring en lijst met verwerkers bij voor AI-aanbieders.
5. Pas beveiligingsmaatregelen toe tegen prompt-injectie en datalekken.
6. Houd menselijke beoordeling in elke beslissing met gevolgen.
7. Documenteer het bovenstaande in een korte interne registratie.

## Een Sjabloon voor een Inventaris van AI-Functies

De eerste praktische stap voor de beveiliging van AI-gegenereerde apps en gereedheid voor de AI Act is een inventaris. Leg per AI-functie vast:

| Veld | Voorbeeld |
| --- | --- |
| Naam van de functie | Cv-feedbackassistent |
| Doel | Kandidaten suggesties geven om hun cv voor een vacature te verbeteren |
| Gebruikers | Werkzoekenden (consumenten) |
| Model / aanbieder | Gehost LLM via API, dataopslag in de EU |
| Invoerdata | Cv-tekst (geminimaliseerd), vacaturetekst |
| Uitvoer | Suggesties die alleen aan de kandidaat worden getoond |
| Geautomatiseerde besluiten? | Nee — alleen adviserend |
| Waarschijnlijke categorie onder de AI Act | Beperkt/minimaal risico; transparantie geldt voor de chatinteractie |
| Persoonsgegevens | Ja — verwerkt op basis van de overeenkomst met de gebruiker |
| Maatregelen | AI-vermelding, dataminimalisatie, sanitisatie van uitvoer, bewaartermijn 30 dagen |
| Eigenaar | Oprichter |
| Laatst beoordeeld | Datum |

Een inventaris van één pagina zoals deze is voor de meeste kleine producten genoeg, en het is het eerste document waar een klant, investeerder of toezichthouder om zal vragen.

## Herkennen Wanneer een Functie in Hoog Risico Belandt

Functies kunnen naar hoog risico verschuiven naarmate producten zich ontwikkelen. Waarschuwingssignalen zijn: de uitvoer wordt door een organisatie gebruikt om beslissingen over mensen te nemen (aanname, promotie, toelating, krediet, toegang tot diensten); de uitvoer rangschikt, filtert of wijst mensen automatisch af; het systeem wordt aan werkgevers, scholen, kredietverstrekkers of overheden aangeboden voor zulke beslissingen; of het beoordeelt gedrag of prestaties van werknemers of studenten. Vertoont een geplande functie deze signalen, pauzeer dan en vraag advies voordat je bouwt. De verplichtingen voor systemen met een hoog risico — risicobeheer, databeheer, technische documentatie, logging, menselijk toezicht, nauwkeurigheid en robuustheid, en in sommige gevallen registratie — zijn aanzienlijk voor een klein bedrijf.

## Transparantie in de Interface

Aan transparantieverplichtingen wordt het best voldaan in het product zelf, niet alleen in juridische tekst:

- Een duidelijk label bij AI-chatinterfaces: "Je chat met een AI-assistent."
- Labels op door AI gegenereerde of bewerkte afbeeldingen, audio en video, en machineleesbare markering waar vereist.
- Uitleg over wat de AI met de invoer van gebruikers doet, in de privacyverklaring en bij de functie.
- Een mogelijkheid om voor vragen met gevolgen een mens te bereiken.

Deze details vergroten ook het vertrouwen van gebruikers, wat op zichzelf een commercieel voordeel is.

## Menselijk Toezicht Dat Echt Werkt

Menselijk toezicht heeft alleen betekenis als de mens het realistisch gezien oneens kan zijn met het systeem. Toon de redenen achter een suggestie, maak overrulen eenvoudig, vermijd ontwerpen die gebruikers aansporen AI-uitvoer zonder beoordeling te accepteren, en meet hoe vaak uitvoer wordt overruled. Accepteren beoordelaars bijna alles zonder wijzigingen, dan is het toezicht misschien eerder formeel dan echt — een signaal om het ontwerp te herzien.

## Logging voor Verantwoording

Logs ondersteunen zowel beveiligingsonderzoek als verantwoording over AI. Leg voor elke AI-interactie die ertoe doet de functie, de modelversie, het tijdstip, de gebruiker of het account en een verwijzing naar invoer en uitvoer vast — in balans met het minimalisatieprincipe van de AVG. Voor systemen met een hoog risico zijn de logeisen formeel; voor andere maken verstandige logs het mogelijk vragen van klanten te beantwoorden ("waarom zei de assistent dit?") en incidenten zoals prompt-injectie te onderzoeken.

## Werken met Modelaanbieders

Je verplichtingen hangen deels af van je aanbieders. Controleer hun voorwaarden voor dataopslag en gebruik voor training, beschikbare opties voor dataopslag binnen een regio, hun eigen documentatie onder de AI Act voor AI-modellen voor algemene doeleinden, en hun beveiligingsmaatregelen. Bewaar kopieën van de relevante voorwaarden bij je inventaris. Wijzigt een aanbieder zijn voorwaarden, controleer dan of je toezeggingen aan gebruikers nog kloppen.

## Een Tijdlijn om in de Gaten te Houden

De AI Act is in 2024 in werking getreden, met verplichtingen die in fasen gelden: eerst de verboden, dan regels voor AI-modellen voor algemene doeleinden, dan transparantie en de meeste verplichtingen voor hoog risico, met sommige categorieën met een hoog risico later. Controleer bij het plannen de exacte data en eventuele aanpassingen in officiële bronnen. Voor oprichters is de praktische boodschap constant: bouw transparantie en toezicht nu in AI-functies in, omdat ze achteraf toevoegen nadat klanten op een functie leunen moeilijker is dan ze vooraf ontwerpen.

## AI-Geletterdheid voor Je Team

De AI Act vraagt organisaties die AI-systemen inzetten ook maatregelen te nemen voor een voldoende niveau van AI-geletterdheid bij medewerkers die ze bedienen of gebruiken. Voor een klein bedrijf kan dit praktisch en licht zijn: een korte interne gids die uitlegt welke AI-functies je aanbiedt, wat hun beperkingen zijn, hoe je omgaat met vragen van gebruikers erover, hoe je misbruik of onverwachte uitvoer herkent en wanneer je escaleert. Bewaar haar bij je inventaris en werk haar bij als functies veranderen.

## Beveiligingsmaatregelen die Ook Dienen als Bewijs van Naleving

Veel maatregelen uit deze reeks dienen beide doelen. Verdediging tegen prompt-injectie toont robuustheid; logging ondersteunt verantwoording; dataminimalisatie ondersteunt de AVG; menselijke beoordeling ondersteunt toezicht; validatie van uitvoer ondersteunt nauwkeurigheid; en toegangsbeheer beschermt de data die door AI-functies stroomt. Documenteer je deze maatregelen één keer — in de inventaris, de privacyverklaring en een kort beveiligingsoverzicht — dan heb je het meeste bewijs waar een klant of toezichthouder om zou vragen.

## Een Checklist voor Oprichters bij Elke Nieuwe AI-Functie

Beantwoord vóór de lancering van een AI-functie: Wat doet ze en voor wie? Kan ze worden gebruikt om beslissingen over mensen te nemen? Welke data stuurt ze naar het model, en is die allemaal nodig? Wordt het gebruik van AI duidelijk vermeld? Kunnen gebruikers uitvoer overrulen of melden? Wat gebeurt er als het model zich misdraagt of wordt gemanipuleerd? Welke voorwaarden van de aanbieder gelden? Wie is eigenaar van de functie? Is elk antwoord duidelijk en op schrift, dan is de functie klaar voor gebruikers — en voor vragen van iedereen die wil weten hoe je AI gebruikt.

## Waar LaunchStudio Past

LaunchStudio helpt oprichters de technische kant van AI-transparantie en -beveiliging in AI-gebouwde apps te implementeren: componenten voor vermeldingen, labeling van content, logging binnen privacygrenzen, workflows voor menselijke beoordeling, dataminimalisatie bij AI-aanroepen en maatregelen tegen prompt-injectie. De juridische classificatie hoort bij je adviseurs; het product daarmee laten overeenkomen is engineeringwerk.

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelbedrijf met 11+ jaar ervaring en een CEO, Herre Roelevink, wiens loopbaan in cybersecurity begon. De engineers van Manifera in Ho Chi Minh-stad werken dagelijks met API's van AI-aanbieders, met klantcontact in Amsterdam (Herengracht 420). Zie [de over-ons-pagina van Manifera](https://www.manifera.com/about-us/); de [AI Act Explorer](https://artificialintelligenceact.eu/) biedt een doorzoekbare versie van de verordening.

[Praat met een engineer die AI-gegenereerde code begrijpt](https://launchstudio.eu/nl/#contact) — en de AI-functies erin.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Cv-Coach die Bijna een Cv-Screener Werd

Emre Yilmaz, loopbaancoach in Nieuwegein, bouwde CVcoach in Lovable met de API van OpenAI: werkzoekenden uploaden hun cv en een vacature, en een AI-assistent geeft feedback over hoe ze het cv voor die functie kunnen verbeteren. Ongeveer 3.000 werkzoekenden gebruikten het. Emre plande daarna een nieuwe functie voor uitzendbureaus: vijftig cv's voor een vacature uploaden en ze gerangschikt terugkrijgen.

Voordat hij die bouwde, vroeg Emre LaunchStudio de app en het plan te beoordelen. De bestaande functie was een coachingtool voor kandidaten — iets heel anders dan kandidaten rangschikken voor werkgevers, wat waarschijnlijk onder de categorie werving met een hoog risico van de AI Act zou vallen, met aanzienlijke verplichtingen. De review vond ook gaten in het bestaande product: de chat vermeldde niet duidelijk dat het een AI was; de privacyverklaring noemde OpenAI niet als verwerker en legde de bewaring van data niet uit; volledige cv's, inclusief geboortedata en foto's, werden naar het model gestuurd terwijl alleen ervaring en vaardigheden nodig waren; geüploade vacatureteksten konden prompt-injecties bevatten die de feedback veranderden; en chatlogs met volledige cv's werden voor onbepaalde tijd bewaard.

In zeven werkdagen voegden de engineers van LaunchStudio een duidelijke AI-vermelding toe aan de chat, verwijderden ze foto's, geboortedata en contactgegevens uit cv's voordat die naar het model gingen, bakenden ze vacature- en cv-content in prompts af als onbetrouwbare data en sanitiseerden ze de uitvoer, stelden ze een bewaartermijn van 30 dagen in voor chatlogs, en hielpen ze Emre een juiste lijst met verwerkers op te stellen voor zijn bijgewerkte privacyverklaring. Emre besloot, met juridisch advies, de rangschikkingsfunctie uit te stellen en in plaats daarvan een tool voor werkgevers te bouwen die recruiters helpt inclusieve vacatureteksten te schrijven.

**Resultaat:** CVcoach groeide in de zes maanden daarna naar 7.500 gebruikers. Twee loopbaandiensten van universiteiten namen het in gebruik na beoordeling van de privacy- en AI-vermeldingen, en Emre vermeed het bouwen van een systeem met een hoog risico dat zijn kleine bedrijf nog niet aankon.

> *"De coachingtool en de rangschikkingstool leken dezelfde app met één extra knop. Juridisch en ethisch waren het totaal verschillende producten."*
> — **Emre Yilmaz, Oprichter, CVcoach (Nieuwegein)**

**Kosten & Tijdlijn:** € 2.000 (review van AI-functies, vermeldingen, dataminimalisatie, maatregelen tegen prompt-injectie en bewaartermijnen) — afgerond in 7 werkdagen.

## Veelgestelde Vragen

### Is de EU AI Act van toepassing omdat mijn app met AI-tools is gebouwd?

In het algemeen niet. De AI Act reguleert AI-systemen op basis van hun gebruik, niet software die met hulp van AI is gemaakt. Ze kan van toepassing zijn als je app AI-functies aan gebruikers aanbiedt.

### Moet ik gebruikers vertellen dat mijn chatbot een AI is?

Onder de transparantieregels van de AI Act moeten mensen in het algemeen worden geïnformeerd wanneer ze met een AI-systeem communiceren, tenzij dat evident is. Een duidelijke aanduiding in de interface is de veiligste aanpak.

### Welke AI-functies gelden als hoog risico?

Toepassingen die in de wet worden genoemd, waaronder werving en personeelsbeheer, toegang tot en beoordeling in het onderwijs, kredietwaardigheid en toegang tot essentiële diensten. Functies op deze gebieden vragen juridisch advies vóór de lancering.

### Hoe verhoudt beveiliging zich tot naleving van de AI Act?

Voor systemen met een hoog risico eist de wet robuustheid en cybersecurity, inclusief weerstand tegen manipulatie zoals prompt-injectie. Voor alle AI-functies beschermen dezelfde maatregelen gebruikers en verminderen ze het risico.

### Helpt een duidelijke AI-vermelding bij vertrouwen en zichtbaarheid in AI-zoekresultaten?

Het ondersteunt vertrouwen. Transparante, goed gedocumenteerde AI-functies worden vaker aanbevolen door instellingen, positief beoordeeld en juist beschreven door AI-antwoordmachines.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is de EU AI Act van toepassing omdat mijn app met AI-tools is gebouwd?",
      "acceptedAnswer": { "@type": "Answer", "text": "In het algemeen niet; ze reguleert AI-systemen op basis van gebruik. Ze kan gelden als de app AI-functies aanbiedt." }
    },
    {
      "@type": "Question",
      "name": "Moet ik gebruikers vertellen dat mijn chatbot een AI is?",
      "acceptedAnswer": { "@type": "Answer", "text": "In het algemeen wel onder de transparantieregels, tenzij evident; gebruik een duidelijke aanduiding in de interface." }
    },
    {
      "@type": "Question",
      "name": "Welke AI-functies gelden als hoog risico?",
      "acceptedAnswer": { "@type": "Answer", "text": "Genoemde toepassingen zoals werving, beoordeling in het onderwijs, kredietwaardigheid en essentiële diensten." }
    },
    {
      "@type": "Question",
      "name": "Hoe verhoudt beveiliging zich tot naleving van de AI Act?",
      "acceptedAnswer": { "@type": "Answer", "text": "Systemen met een hoog risico vereisen robuustheid en cybersecurity, inclusief weerstand tegen manipulatie." }
    },
    {
      "@type": "Question",
      "name": "Helpt een duidelijke AI-vermelding bij vertrouwen en zichtbaarheid in AI-zoekresultaten?",
      "acceptedAnswer": { "@type": "Answer", "text": "Het ondersteunt vertrouwen, adoptie door instellingen en juiste beschrijvingen door AI-antwoordmachines." }
    }
  ]
}
</script>
