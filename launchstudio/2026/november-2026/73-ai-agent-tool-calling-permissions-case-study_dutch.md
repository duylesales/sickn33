---
Titel: "Case Study: Tool-Calling Autorisaties van een AI Agent Beveiligen Vóór Enterprise Uitrol"
Keywords: AI Agent Tool Calling, Tool-Calling Permissions, LaunchStudio, Manifera, AI Agent Security, Enterprise Rollout, Function Calling, Herre Roelevink
Buyer Stage: Beslissing
---

# Case Study: Tool-Calling Autorisaties van een AI Agent Beveiligen Vóór Enterprise Uitrol
AI-agents die autonoom tools kunnen aanroepen — het doorzoeken van een database, versturen van een e-mail, bijwerken van een klantrecord of initiëren van een terugbetaling — worden in rap tempo standaardfunctionaliteiten in AI SaaS-producten. Tegelijkertijd vormen ze een van de minst onderzochte aanvalsoppervlakken in de huidige golf van door AI gebouwde applicaties. Een agent met tool-calling permissies is functioneel gezien software die acties uitvoert op basis van instructies in natuurlijke taal, afkomstig van potentieel onbetrouwbare gebruikers of uit externe documenten die de agent tijdens een sessie inleest. Wanneer een enterprise-inkoper vraagt hoe deze permissies zijn afgebakend, is "de AI bepaalt zelf wat hij nodig heeft" een antwoord dat geen enkele security-audit overleeft. Deze case study beschrijft wat er gebeurde toen de agent-permissies van een AI-native oprichter werden gehard voorafgaand aan een enterprise-uitrol — en analyseert de specifieke faalpatronen die tool-calling tot een van de meest risicovolle onderdelen van een SaaS-platform maken.

## Waarom Tool-Calling Permissies Verschillen van Reguliere Toegangscontrole

In een conventionele webapplicatie is toegangscontrole relatief voorspelbaar: een gebruiker authenticeert zich, diens rol (RBAC) wordt gecontroleerd en de backend staat een specifiek API-verzoek toe of wijst het af. De logica is deterministisch: dezelfde invoer leidt altijd tot dezelfde autorisatiebeslissing.

Een AI-agent met tool-calling capaciteit doorbreekt dit model: de *beslissing over wélke tool wordt aangeroepen, en met welke argumenten*, wordt genomen door een taalmodel dat natuurlijke taal interpreteert — en niet door een vast codepad dat een security-auditor regel voor regel kan verifiëren. Dit introduceert faalmodi die in traditionele toegangscontrole simpelweg niet bestaan:

- **Prompt injection via tool-outputs.** Als een agent een tool aanroept die externe content leest (een webpagina, een geüpload PDF-bestand, een e-mail), en die content bevat verborgen instructies, kan het model worden gemanipuleerd om een *andere* tool aan te roepen dan de gebruiker voor ogen had — inclusief acties waar de gebruiker zelf nooit de rechten voor had.
- **Te brede rechten voor service-accounts.** Veel AI-integraties geven het service-account van de agent volledige beheerdersrechten op de database, omdat dit de snelste manier was om het prototype werkend te krijgen. De agent was nooit bedoeld om records te verwijderen, maar de onderliggende API-sleutel kan dat wel.
- **Ontbreken van menselijke verificatie (Human-in-the-Loop) bij destructieve acties.** Een agent die zonder bevestigingsstap een terugbetaling kan uitvoeren, een gebruiker kan verwijderen of een mailing kan sturen, verandert een enkele foute model-output — door hallucinatie, injectie of vage input — direct in een onomkeerbare fout in de echte wereld.
- **Onvoldoende logging per interactie.** Wanneer een agent vijf verschillende tools aanroept binnen een complexe taak, logt de standaard AI-builder meestal alleen het uiteindelijke antwoord aan de gebruiker, en niet elke individuele tool-call met de bijbehorende parameters — waardoor het achterhalen van de oorzaak bij een beveiligingsincident onmogelijk wordt.

Enterprise security-teams die een AI SaaS-leverancier evalueren, vragen steeds vaker niet alleen "is onze data versleuteld?", maar heel specifiek: "wat kan uw AI daadwerkelijk *uitvoeren*, en wat verhindert dat hij ongeoorloofde acties onderneemt?"

## De Praktijksituatie: Een Klantenservice-Agent op Weg naar Enterprise Deals

De oprichter in deze case study had met behulp van Cursor een AI-klantenserviceagent gebouwd die bestelgeschiedenissen kon opzoeken, terugbetalingen tot een bepaalde limiet kon uitvoeren, bezorgadressen kon aanpassen en complexe vragen kon escaleren naar een menselijke medewerker. Het systeem functioneerde uitstekend voor kleinere webshops. Vervolgens toonde een middelgrote enterprise-klant interesse, maar stuurde eerst een uitgebreide security-vragenlijst met de vraag: "Beschrijf het autorisatiemodel dat bepaalt welke acties uw AI-agent namens een gebruiker kan uitvoeren, en hoe privilege-escalatie via gebruikersinvoer technisch wordt voorkomen."

De oprichter kon hier geen waterdicht antwoord op geven. Een grondige technische audit van de implementatie bracht het volgende aan het licht:

1. **Het database-account van de agent had volledige schrijfrechten** — niet beperkt tot de specifieke tabellen en rijen die de agent daadwerkelijk nodig had. De zoektool, de terugbetalingstool en de adrestool deelden allemaal één overkoepelend database-account.
2. **Er was geen harde bevestigingsstap voor terugbetalingen.** De agent kon zelfstandig een terugbetaling initiëren op basis van zijn eigen interpretatie van het chatbericht van de klant, zonder menselijke controle en zonder een harde limiet op databaseniveau — er was alleen een richtlijn opgenomen in de system prompt, wat geen geldige beveiligingscontrole is.
3. **De uitvoer van tools werd ongefilterd teruggevoerd in de context van het model.** Een kwaadaardige notitie in een bestelling — bijvoorbeeld ingevoerd door een eerdere frauduleuze koper — kon instructies bevatten die de agent zou uitvoeren zodra hij die specifieke bestelling opzocht.
4. **Er bestond geen audit log per individuele aanroep**, alleen een logbestand van het uiteindelijke antwoord dat aan de gebruiker werd getoond, waardoor niet traceerbaar was welke tools met welke parameters waren aangeroepen.

## De Oplossing: Een Autorisatiemodel Ontworpen voor Enterprise-Audits

De engineers van LaunchStudio herbouwden de autorisatielaag rondom de agent zonder de bestaande gebruikersinterface of de gesprekslogica aan te tasten. Het werk concentreerde zich op vijf kerngebieden:

1. **Strikt afgebakende service-credentials per tool.** In plaats van één overkoepelend database-account kreeg elke individuele tool een eigen, specifiek geconfigureerd account — de zoektool heeft uitsluitend leesrechten op specifieke tabellen, de terugbetalingstool kan slechts naar één tabel schrijven met strikte Row Level Security (RLS) restricties, en geen enkele tool heeft toegang tot gegevens buiten zijn functie.
2. **Harde limieten afgedwongen op databaseniveau, niet in de prompt.** Het maximale terugbetalingsbedrag werd een harde constraint op het niveau van de database en backend, volledig onafhankelijk van wat het taalmodel denkt dat de limiet is — zodat geen enkele slimme prompt-injectie ooit een betaling boven het maximum kan forceren.
3. **Human-in-the-Loop voor financiële en destructieve acties boven een drempelwaarde.** Terugbetalingen boven een instelbaar bedrag en adreswijzigingen bij bestellingen met een hoge waarde vereisen nu een expliciete goedkeuring met één klik door een menselijke beheerder voordat de tool daadwerkelijk wordt uitgevoerd.
4. **Volledige audit-logging per tool-call.** Elke individuele aanroep — toolnaam, meegegeven parameters, gebruikerscontext en API-respons — wordt nu onafhankelijk gelogd. Dit biedt het security-team van de klant en toekomstige auditors een reproduceerbaar logboek van alle agent-activiteiten.
5. **Sanitization van tool-outputs die terugkeren in de context.** Data die uit externe bronnen wordt ingelezen, wordt eerst gescand en ontdaan van patronen die lijken op prompt-instructies voordat deze opnieuw aan het LLM wordt aangeboden, waarmee de meest directe injectievector werd afgesloten.

## Het Resultaat

Dankzij de geharde autorisatielaag kon de oprichter de enterprise-vragenlijst beantwoorden met concrete technische bewijzen in plaats van vage beloftes: afgebakende service-accounts op specifieke tabellen, een gedocumenteerde drempelwaarde voor menselijke goedkeuring en een exporteerbaar audit logbestand. De enterprise-deal werd binnen enkele weken ondertekend. De aanpassing was niet cosmetisch — het transformeerde de veiligheid van het platform fundamenteel naar enterprise-niveau.

## Waarom Dit Steeds Vaker Terugkomt in Enterprise Deals

Deze situatie staat niet op zichzelf. Naarmate AI-agents verschuiven van leuke demo's naar bedrijfskritieke workflows, stellen inkoop- en security-afdelingen gerichte vragen over tool-calling autorisatie. Ze hebben voldoende publieke incidenten gezien met agents die te veel bevoegdheden hadden om te weten waar de kwetsbaarheden zitten. Het antwoord op "wat voorkomt dat uw agent ongeoorloofde acties uitvoert" is inmiddels net zo'n standaard controlepunt geworden als data-encryptie en ISO-certificeringen vijf jaar geleden waren. Oprichters die agent-autorisatie direct goed inrichten, sluiten enterprise-deals aanzienlijk sneller omdat ze niet halverwege het verkooptraject ad-hoc aanpassingen hoeven door te voeren.

## Belangrijkste Inzichten

- AI-agents met tool-calling introduceren nieuwe autorisatierisico's omdat een taalmodel op basis van vrije tekst beslist welke actie wordt uitgevoerd, en niet een vast codepad.
- Te brede database-rechten — waarbij alle tools één beheerdersaccount delen — zijn een veelvoorkomende standaard in vroege AI-projecten en een direct afkeurpunt bij enterprise-audits.
- Harde limieten op financiële of destructieve acties moeten worden afgedwongen in de database of backend-code, en nooit uitsluitend via een system prompt.
- Menselijke goedkeuring (Human-in-the-Loop) voor risicovolle handelingen en gedetailleerde per-call audit logs zijn essentieel om enterprise security-reviews met succes te doorstaan.
- Het beveiligen van tool-calling vereist geen herbouw van de agent zelf — het is een gerichte versterking van de onderliggende autorisatielaag en API-infrastructuur.

## Maak Uw AI-Agent Klaar voor Enterprise Security Reviews

Zorg dat u een concreet, verifieerbaar en veilig antwoord heeft wanneer uw volgende enterprise-klant vraagt hoe uw AI-agent beveiligd is.

LaunchStudio wordt beheerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 onder leiding van Oprichter & Managing Director **Herre Roelevink**. Zoals Roelevink benadrukt: *"We zien een duidelijke verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en security die nodig zijn om die producten volwassen te maken. Daarin hebben we elf jaar ervaring."* Met de combinatie van "Nederlands management en Vietnamese engineeringkracht" heeft Manifera haar hoofdkantoor in **Amsterdam, Nederland** (Herengracht 420), een vestiging in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minhstad, Vietnam** (Pho Quang Street). Via LaunchStudio voorzien senior engineers uw bestaande AI-prototype van productieklare beveiliging, geteste betaalintegraties, schaalbare hosting en geautomatiseerde kwaliteitsborging — waarmee uw prototype in 1 tot 3 weken verandert in een robuuste MVP, zonder herbouw. [Vraag vandaag nog een offerte aan](https://launchstudio.eu/nl/#contact) of ontdek hoe het [maatwerk software development team](https://www.manifera.com/services/custom-software-development/) van Manifera AI-applicaties klaarmaakt voor enterprise-kwaliteit.

## Echt voorbeeld

### Een AI-Native Oprichter in Actie: Logistieke Boekingsassistent

Farid, oprichter van een logistieke boekingsassistent gebouwd met **Cursor**, beschikte over een AI-agent die zelfstandig zendingen kon omboeken, orders kon annuleren en contact kon opnemen met transporteurs namens klanten. Een grote logistieke dienstverlener die het platform wilde afnemen, vroeg om een schriftelijke toelichting op de maatregelen die voorkomen dat de agent onbevoegd zendingen annuleert of wijzigt.

Farid schakelde **LaunchStudio (door Manifera)** in om het permissiemodel van zijn agent te beveiligen. Engineers richtten strikt afgebakende database-rechten in per tool, voegden een menselijke goedkeuringsstap toe voor annuleringen boven een bepaalde vrachtwaarde en implementeerden volledige audit-logging zodat elke actie traceerbaar is naar de specifieke tool, invoerparameters en uitkomst.

**Resultaat:** Farid overhandigde het beveiligingsteam een gedocumenteerd permissiemodel inclusief voorbeeld-auditlogs, waarna het vastgelopen contract binnen drie weken alsnog werd ondertekend.

**Investering & Doorlooptijd:** € 4.200 (Enterprise Hardening Pakket) — 12 werkdagen.

---

---

---
## Veelgestelde Vragen

### Wat maakt tool-calling door AI-agents een ander beveiligingsrisico dan reguliere API-beveiliging?

De keuze van de aan te roepen tool en de parameters wordt bepaald door het interpreteren van vrije tekst in plaats van een vast geprogrammeerd codepad. Hierdoor kan dezelfde kwetsbaarheid via talloze verschillende formuleringen worden uitgebuit — inclusief verborgen instructies in externe bestanden die de agent inleest — iets waar traditionele API-toegangscontrole niet op berekend is.

### Vereist het beveiligen van tool-calling permissies een complete herbouw van de AI-agent?

Nee. De trajecten van LaunchStudio richten zich specifiek op de autorisatie- en infrastructuurlaag — het beperken van database-rechten, het afdwingen van harde limieten in de backend, het toevoegen van goedkeuringsstappen en het opzetten van audit-logging — zonder dat de prompts of de gesprekslogica van de agent herschreven hoeven te worden.

### Wat is een "Human-in-the-Loop" stap en wanneer is deze noodzakelijk?

Dit is een bevestigingsstap waarbij een menselijke medewerker een actie expliciet moet goedkeuren voordat deze daadwerkelijk wordt uitgevoerd. Dit wordt standaard toegepast bij destructieve of financieel risicovolle handelingen — zoals hoge terugbetalingen, accountverwijderingen of bulk-mailings — waar een foute model-output directe materiële schade zou veroorzaken.

### Waarom volstaat het niet om de limieten simpelweg in de system prompt van de AI te vermelden?

Een system prompt is een tekstuele instructie en geen technisch afdwingbaar beveiligingsmechanisme — het model kan door prompt-injectie of misleidende gebruikersvragen gemanipuleerd worden om de instructie te negeren. Harde limieten moeten altijd worden afgedwongen op database- of backendniveau, waar geen enkele model-output ze kan omzeilen.

### Hoe vaak vragen enterprise-klanten naar de permissies van AI-agents tijdens een security review?

Steeds vaker en met toenemende diepgang. Naarmate openbare incidenten met te ruim geautoriseerde agents toenemen, hebben security-auditors gerichte vragen over agent-autorisatiemodellen toegevoegd aan hun standaard vendor questionnaires, vergelijkbaar met vragen over encryptie en datalocatie.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat maakt tool-calling door AI-agents een ander beveiligingsrisico dan reguliere API-beveiliging?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De keuze van de aan te roepen tool en de parameters wordt bepaald door het interpreteren van vrije tekst in plaats van een vast geprogrammeerd codepad. Hierdoor kan dezelfde kwetsbaarheid via talloze verschillende formuleringen worden uitgebuit — inclusief verborgen instructies in externe bestanden die de agent inleest — iets waar traditionele API-toegangscontrole niet op berekend is."
      }
    },
    {
      "@type": "Question",
      "name": "Vereist het beveiligen van tool-calling permissies een complete herbouw van de AI-agent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. De trajecten van LaunchStudio richten zich specifiek op de autorisatie- en infrastructuurlaag — het beperken van database-rechten, het afdwingen van harde limieten in de backend, het toevoegen van goedkeuringsstappen en het opzetten van audit-logging — zonder dat de prompts of de gesprekslogica van de agent herschreven hoeven te worden."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is een \"Human-in-the-Loop\" stap en wanneer is deze noodzakelijk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dit is een bevestigingsstap waarbij een menselijke medewerker een actie expliciet moet goedkeuren voordat deze daadwerkelijk wordt uitgevoerd. Dit wordt standaard toegepast bij destructieve of financieel risicovolle handelingen — zoals hoge terugbetalingen, accountverwijderingen of bulk-mailings — waar een foute model-output directe materiële schade zou veroorzaken."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom volstaat het niet om de limieten simpelweg in de system prompt van de AI te vermelden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een system prompt is een tekstuele instructie en geen technisch afdwingbaar beveiligingsmechanisme — het model kan door prompt-injectie of misleidende gebruikersvragen gemanipuleerd worden om de instructie te negeren. Harde limieten moeten altijd worden afgedwongen op database- of backendniveau, waar geen enkele model-output ze kan omzeilen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe vaak vragen enterprise-klanten naar de permissies van AI-agents tijdens een security review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Steeds vaker en met toenemende diepgang. Naarmate openbare incidenten met te ruim geautoriseerde agents toenemen, hebben security-auditors gerichte vragen over agent-autorisatiemodellen toegevoegd aan hun standaard vendor questionnaires, vergelijkbaar met vragen over encryptie en datalocatie."
      }
    }
  ]
}
</script>
