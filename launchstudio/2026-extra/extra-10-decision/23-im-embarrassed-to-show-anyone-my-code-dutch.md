---
Titel: "'Ik Schaam Me Om Mijn Code aan Iemand te Laten Zien' — Elke Software Engineer Heeft Erger Gezien"
Trefwoorden: schaamte voor AI gegenereerde code, rommelige code schaamte, kwaliteit code AI prototype, code laten zien aan developer, vibe coding zelfvertrouwen, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# 'Ik Schaam Me Om Mijn Code aan Iemand te Laten Zien' — Elke Software Engineer Heeft Erger Gezien

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "'Ik Schaam Me Om Mijn Code aan Iemand te Laten Zien' — Elke Software Engineer Heeft Erger Gezien",
  "description": "Een nuchtere ontmanteling van de schaamte die niet-technische oprichters voelen over hun door AI gegenereerde code: waarom engineers niet letten op rommeligheid, waar ze wél naar zoeken, en hoe een code-review er in werkelijkheid aan toegaat.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-02-06",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/im-embarrassed-to-show-anyone-my-code" }
}
</script>

Laten we een hardnekkige mythe definitief uit de wereld helpen, want deze overtuiging houdt in stilte meer productlanceringen tegen dan welke prijsbezwaar dan ook: **het idee dat uw broncode er op een bepaalde maagdelijke manier uit moet zien voordat een professionele engineer ernaar mag kijken**.

Oprichters die zonder blikken of blozen een halfafgewerkte pitch deck naar durfinvesteerders sturen, durven maandenlang niet live te gaan met een prima werkende web-applicatie omdat ze zich doodschamen voor wat er in de repository staat. Gedupliceerde componenten, een bestand genaamd `NieuwDashboard2Definitief`, functies die drie volstrekt ongerelateerde dingen tegelijk doen, en op veertien plekken de opmerking `// TODO dit later netjes maken`. De mythe is dat dit zeldzaam is, beschamend, of het bewijs dat u incompetent bent. Het is niets van dat alles — en erin geloven kost u maanden aan marktsucces.

## De Mythe: "Mijn Code Moet Schoon Zijn Vóórdat Iemand Het Ziet"

Deze schaamte ontstaat doordat oprichters hun referentiekader lenen uit een context waar het niet thuishoort. Veel niet-technische ondernemers hebben het romantische beeld van professionele code als iets mathematisch elegants, gestructureerd en vanaf regel één met een vooropgezet masterplan geschreven. Dat is immers wat de marketingverhalen van techbedrijven suggereren en wat een universitaire cursus informatica doceert.

Maar dat is **niet** hoe snel bouwen met AI eruitziet — en het is evenmin hoe 90% van de codebases van succesvolle startups er in hun vroege dagen uitzag.

Code die iteratief onder tijdsdruk is opgebouwd door een AI-tool vijftig keer te prompten met *"voeg deze knop toe"* en *"pas dit formulier aan"*, eindigt structureel chaotisch. Ongeacht wie er achter het toetsenbord zit. Dat is geen symptoom van gebrek aan kennis; het is het logische gevolg van bouwen via **snelle iteratie in plaats van formele blauwdrukken vooraf**. Dat is exact waar tools zoals Lovable, Bolt en Cursor voor zijn ontworpen. Dat resultaat afrekenen op de standaarden van een leerboek is alsof u een ruwe schets veroordeelt omdat het geen volwaardige bouwtekening is. Het zijn totaal verschillende objecten met totaal verschillende doelen.

## Waar Engineers Écht Naar Kijken (Hint: Niet Naar Rommel)

Hier vergissen niet-technische oprichters zich fundamenteel in: senior software engineers die dagelijks prototypes reviewen, scannen **niet** op visuele netheid. Ze scannen op een heel kort lijstje van dragende constructies, en geen enkele daarvan is cosmetisch:
- Vinden autorisatiecontroles plaats op de server, of vertrouwt de app blind op wat de frontend wel of niet toont?
- Staan er geheime API-sleutels van Stripe of OpenAI in JavaScript-code die in de browser van de bezoeker wordt uitgevoerd?
- Kan de database rechtstreeks worden uitgelezen door iemand die simpelweg de API-URL aanpast in diens browser, ongeacht wie er is ingelogd?
- Kan het betalingssysteem worden misleid door een verzoek simpelweg te herhalen?

Voor geen van deze controles is een consequente inspringing of een mooie bestandsnaam vereist. Een rommelige functie met de naam `verwerkData2()` die de autorisatie waterdicht afhandelt, heeft voor een engineer oneindig veel meer waarde dan een prachtig gestructureerde, elegant geformatteerde functie die ongeautoriseerde toegang wagenwijd open laat staan.

## De Schijn bedriegt: Uiterlijk en Risico Correlateren Nauwelijks

Uiterlijke netheid en daadwerkelijke veiligheid zijn nagenoeg onafhankelijke variabelen.
Enkele van de meest gestructureerde prototypes die auditors voorbij zien komen — keurige mapjes, Engelse benamingen, overal nette commentaren — bevatten gapende veiligheidslekken. De oprichter heeft immers al zijn prompt-aandacht besteed aan esthetiek en mappenstructuur in plaats van aan de onzichtbare infrastructuur onder de motorkap.

Omgekeerd blijken sommige van de meest chaotische codebases — duplicaten van bestanden, halve experimenten en willekeurige CSS-classes — onderhuids uitstekend beveiligd met correcte Row-Level Security, simpelweg omdat dat toevallig in de begindagen goed was ingesteld.

Daarom begint LaunchStudio altijd met een objectieve code-audit. Een oprichter die zijn eigen repository beschrijft, zit er qua risico-inschatting vrijwel altijd naast: *"Het is een complete bende, sorry alvast"* of *"Het zit eigenlijk heel solide in elkaar"*. Geen van beide uitspraken voorspelt wat de engineer aantreft, omdat de oprichter kijkt naar cosmetische signalen die een engineer negeert.

## Hoe een Reviewgesprek Er in de Werkelijkheid Uitziet

De gevreesde audit verloopt in de praktijk heel anders dan de doemscenario's in uw hoofd. Er is geen moment van afkeurend gezucht of moreel oordeel. In het hoofd van de engineer draait simpelweg een pragmatische checklist af:
- Waar vindt authenticatie plaats?
- Staan omgevingsvariabelen veilig in een `.env`-bestand?
- Bevat de database actieve autorisatieregels?
- Staan er dode bestanden in die veilig gewist kunnen worden?

De reviewer heeft diezelfde patronen — een vergeten mapje genaamd `oud`, drie versies van hetzelfde registratieformulier, een bestandje `test.js` met een testwachtwoord — al bij tientallen andere startups gezien. Het is geen schokkende ontdekking. Het is gewoon een doordeweekse dinsdag.

Wat de engineer tijdens het gesprek hardop tegen u zegt, is simpelweg een nuchtere to-do lijst: *"Deze tabel mist een controle op eigenaarschap, deze sleutel moeten we even naar de server verhuizen, en deze twee bestanden lijken duplicaten; kunnen we er één van weggooien?"* Geen oordeel over uw capaciteiten, maar een heldere takenlijst.

## Waarom Schaamte Structureel Ongegrond Is

Er schuilt een grote ironie in dit fenomeen: **de oprichters die zich het meest schamen voor hun code, zijn doorgaans degenen die het meeste werk hebben verzet**. Een repository met drie verlaten experimenten en twaalf iteraties ziet er rommeliger uit dan een leeg project met één functionaliteit — maar die eerste oprichter heeft tenminste snel getest en gezocht naar wat klanten écht willen. Chaos in deze context is het bewijs van actie en iteratie, niet van incompetentie.

Bovendien heeft u die code zelf niet regel voor regel getypt: een AI-model heeft dat gedaan op basis van uw instructies. U schamen voor de code van een AI is als een huiseigenaar die zich schaamt voor de ruwe houten balken van een aannemer voordat het gipsplaat ertegenaan gaat. Ruwe balken zien er nou eenmaal zo uit tijdens de bouw.

## De Werkelijke Kosten van Schaamte

Dit is geen psychologisch praatje voor de gezelligheid — schaamte heeft directe zakelijke consequenties. Elke week die u verliest door een review uit te stellen uit angst voor wat een engineer denkt, is een week waarin een onbeveiligde API-sleutel of een privacy-lek onopgemerkt blijft draaien. U lost het risico niet op door weg te kijken; u stelt uitsluitend het ontdekken ervan uit.

## Wat U Werkelijk Meebrengt naar de Tafel

Bekijk de situatie vanuit het juiste perspectief: **u heeft een werkende software-applicatie gebouwd met tools die vijf jaar geleden nog niet eens bestonden, zonder zelf één regel traditionele programmeertaal te beheersen**. Dát is het zeldzame, moeilijke deel. Veruit de meeste mensen met een goed idee komen nooit zover.

Toegangscontrole inrichten, deployment-pijplijnen opzetten en webhooks beveiligen zijn voor ervaren software-engineers overzichtelijke, mechanische routines. Een functionerend product realiseren dat een reëel marktprobleem oplost, is géén mechanisch kunstje — en dat is het deel dat u zélf al heeft volbracht.

Beschouw de engineer als een **bouwkundig inspecteur** van een huis dat u zojuist heeft gebouwd. De inspecteur oordeelt niet over de kleur van uw gordijnen of over het feit dat er nog een verfblik in de gang staat. Hij controleert de fundering en de elektrische bedrading — want dat zijn de onderdelen die gevaar opleveren als ze verkeerd zitten. Al het cosmetische waar u zich voor schaamt, is voor de inspectie volstrekt irrelevant.

De engineers van LaunchStudio en Manifera (met meer dan 11 jaar ervaring in enterprise softwareontwikkeling) hebben nog nooit een samenwerking afgewezen omdat een repository er rommelig uitzag. [Stuur ons uw prototype-link exact zoals deze nu is](https://launchstudio.eu/nl/#contact) — wij vertellen u binnen één werkdag wat er technisch wél en wat er niet toe doet.

## Praktijkvoorbeeld

### Een Marktplaats voor Interieurdesign Wachtte Vier Maanden met Vragen

Petra Lindqvist bouwde met behulp van Bolt een online platform dat zelfstandige interieurontwerpers koppelt aan huiseigenaren. Maandenlang voegde ze telkens nieuwe features toe zodra een vroege tester erom vroeg. Tegen de tijd dat ze over livegang nadacht, bevatte haar codebase drie verschillende versies van de ontwerpersprofielpagina, een map genaamd `backup_niet_verwijderen` en willekeurige stijlen door het wisselen tussen AI-tools. Vier maanden lang durfde ze geen developer te benaderen omdat ze *"niet wilde dat iemand zag wat voor een chaos het onder de motorkap was"*.

Toen ze de repository uiteindelijk toch deelde, kostte de code-audit exact één werkdag. De uitkomst was een kort en zakelijk lijstje: één Stripe-sleutel stond onbedoeld in de frontend-code, de chattabel kon door elke bezoeker worden uitgelezen bij gebrek aan RLS, en van de drie profielpagina's konden er twee direct in de prullenbak. De auditor repte met geen woord over de bestandsnamen of de mapstructuur, behalve om te vragen welke profielpagina actief moest blijven.

**Resultaat:** Binnen acht werkdagen werd de beveiliging gerepareerd binnen het Launch Ready-pakket. De marktplaats lanceerde direct naar een wachtlijst van 40 ontwerpers — vier maanden later dan mogelijk was geweest, puur door schaamte voor een publiek dat helemaal niet bleek te bestaan.

> *"Ik heb vier maanden verloren omdat ik dacht dat iemand op me neer zou kijken vanwege mijn slordige mapjes. Hij vroeg me twee mapjes weg te gooien en ging direct aan de slag met het echte probleem. Ik heb vier maanden verspild aan spoken."*
> — **Petra Lindqvist, Oprichter, marktplaats interieurdesign (Rotterdam)**

**Kosten & Doorlooptijd:** Launch Ready-pakket, RLS-beveiliging en veilige sleutelrotatie — live binnen 8 werkdagen.

## Veelgestelde Vragen

### Moet ik mijn code eerst opschonen voordat ik het laat zien?
Nee. Behalve het verwijderen van mappen waarvan u zeker weet dat ze niet meer worden gebruikt, is vooraf poetsen zonde van uw tijd. U besteedt dan uren aan cosmetische zaken waar een auditor niet eens naar kijkt, terwijl de echte risico's (zoals ontbrekende server-side rechten) onveranderd blijven.

### Wat als de software engineer neerkijkend reageert op mijn AI-code?
In de praktijk gebeurt dit bij professionele bureaus niet. Het beoordelen en productierijp maken van door AI gegenereerde prototypes is dagelijks werk. Een ontwikkelaar die met moreel dedain reageert in plaats van met een praktische checklist, toont vooral zijn eigen onprofessionaliteit aan.

### Betekent rommelige code automatisch dat het ook onveilig is?
Nee, absoluut niet. Sommige zeer overzichtelijk geformatteerde apps bevatten gigantische datalekken omdat alle energie naar structuur ging. Andersom zijn rommelige codebases qua data-isolatie soms verrassend goed op orde. Uiterlijk en veiligheid staan los van elkaar.

### Hoeveel van mijn code moet een engineer daadwerkelijk zien?
Aanvankelijk de gehele repository om een globaal beeld van de applicatie te krijgen. Daarna richt de diepte-inspectie zich specifiek op een select aantal dragende bestanden: authenticatie-handlers, databaseregels (RLS), betaalintegraties en uitgaande API-routes.

### Is het verstandig om toe te geven dat ik delen van mijn code niet begrijp?
Ja, dat is juist enorm behulpzaam! Zeggen: *"Ik weet niet precies waarom dit bestand bestaat, de AI heeft dit aangemaakt en ik heb er nooit aangezeten"* bespaart zeeën van tijd. Net doen alsof u code begrijpt die u niet doorgrondt, vertraagt het proces en maskeert waar de echte risico's schuilen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik mijn code eerst opschonen voor een review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Besteed geen tijd aan cosmetische aanpassingen. Engineers kijken uitsluitend naar dragende structuren zoals autorisatie, API-sleutels en databasepolicies."
      }
    },
    {
      "@type": "Question",
      "name": "Kijkt een professionele engineer neer op AI-code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Het reviewen en harden van AI-prototypes is standaard werk. Een professionele auditor levert een zakelijke checklist, geen moreel oordeel."
      }
    },
    {
      "@type": "Question",
      "name": "Is rommelige code per definitie onveilig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Visuele rommeligheid en beveiligingsrisico's zijn onafhankelijke factoren. Zelfs zeer nette code kan cruciale rechtencontroles missen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat inspecteert een engineer tijdens een code-audit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voornamelijk authenticatiepaden, database policies (zoals RLS), omgevingsvariabelen, betaal-webhooks en endpoints waar data muteert."
      }
    },
    {
      "@type": "Question",
      "name": "Mag ik aangeven dat ik delen van mijn AI-code niet snap?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, dat is juist zeer waardevol. Openheid over door AI gegenereerde onderdelen versnelt het identificeren van potentiële blinde vlekken."
      }
    }
  ]
}
</script>
