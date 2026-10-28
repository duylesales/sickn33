---
Titel: "Lovable-ontwikkelaar overdracht: wat een professionele oplevering bevat"
Trefwoorden: lovable developer, overdrachtsdocumentatie, code eigenaarschap oprichter, agency white label oplevering, runbook bekende problemen, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Agency / Freelancer (White-Label Partner)
---

# Lovable-ontwikkelaar overdracht: wat een professionele oplevering bevat

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable-ontwikkelaar overdracht: wat een professionele oplevering bevat",
  "description": "De negen zaken die moeten wisselen van eigenaar bij het afronden van een project: git-repository, accounts, secrets, runbook, bekende problemen en ongedocumenteerde keuzes - met een checklist voor oprichters en bureaus aan beide kanten van de oplevering.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-24",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/handing-over-an-ai-built-codebase" }
}
</script>

Een projectoverdracht is geen vluchtig moment. Het is een tastbare set bezittingen en documenten. En de reden waarom zoveel externe softwareprojecten met een nare nasmaak eindigen, is dat iedereen de oplevering behandelt als een gebeurtenis - een afrondende Teams-call, een vriendelijk *"veel succes ermee"*, een slotfactuur - in plaats van een formele levering met een sluitende pakbon.

De toetssteen is simpel en onverbiddelijk: kan een competente, wildvreemde software-ontwikkelaar over drie maanden - wanneer de oorspronkelijke bouwer onbereikbaar op vakantie is - het project oppakken en veilig een wijziging doorvoeren? Voor het overgrote deel van de met AI gebouwde applicaties die door een freelancer of bureau zijn opgeleverd, luidt het antwoord keihard nee. En dat komt zelden door kwade opzet; het komt doordat niemand vooraf heeft afgesproken wat een 'overdracht' nu eigenlijk inhoudt.

## Negen zaken die van eigenaar moeten wisselen

**Eén: de git-repository, in jouw eigen account.** Niet 'gedeeld met jou', niet geëxporteerd als een zip-bestand - maar jouw volledige eigendom, inclusief de complete commit-historie. Die geschiedenis is essentieel: het is hoe een volgende ontwikkelaar begrijpt waarom bepaalde architectuurkeuzes zijn gemaakt, en het is de plek waar je controleert of er ooit geheime sleutels per ongeluk zijn gecommit.

**Twee: elk account, op jouw bedrijfsnaam.** Hosting, database, domeinregistratie, payment provider, transactionele e-mail, crash-reporting en alle AI- of API-koppelingen. Jouw e-mailadres, jouw zakelijke factuurgegevens, met externe ontwikkelaars uitsluitend toegevoegd als tijdelijke gebruikers met rechten die jij met één klik kunt intrekken. Dit is het punt dat het vaakst wordt overgeslagen en het allerduurst is om achteraf recht te trekken.

**Three: een inventarisatie van alle secrets.** Een compleet overzicht van elk geheim token, API-sleutel en database-wachtwoord dat de app gebruikt: waar het leeft, welke rechten het verleent en hoe je het roteert. Geen platte wachtwoorden in een mailtje, maar een plattegrond van het sleutelbeheer. Iedereen die tijdens de bouw toegang had, moet worden beschouwd als iemand die de sleutels nog heeft - deze lijst is dus direct je rotatieplan.

**Vier: een operationeel draaiboek (runbook).** Eén pagina praktische instructies: hoe draai je de app lokaal, hoe deploy je naar productie, hoe voer je een rollback uit bij een fout, hoe herstel je een back-up, en wat doe je als de site platligt? Geschreven voor een engineer die niet bij de bouw aanwezig was.

**Vijf: de architectuur in gewone mensentaal.** Twee beknopte alinea's en bij voorkeur een eenvoudig blokkenschema: welke onderdelen praten met elkaar, waar staat welke data opgeslagen, en welke deelsystemen zijn afhankelijk van externe clouddiensten? Als dit ontbreekt, moet de volgende ontwikkelaar een hele dag besteden aan code-archeologie - tegen diens reguliere uurtarief.

**Zes: de genomen beslissingen en de motivatie erachter.** Waarom Frankfurt als hostingregio? Waarom deze specifieke betaalprovider? Waarom is het autorisatiemodel zo opgezet? Welke alternatieven zijn onderzocht en afgewezen? Dit is de contextuele kennis die geruisloos verdampt zodra iemand vertrekt, en het kost nauwelijks moeite om dit direct vast te leggen zolang het nog vers in het geheugen zit.

**Zeven: een eerlijke lijst met bekende gebreken (known issues).** Alles wat tijdens het werk is ontdekt maar niet is opgelost, alles wat is uitgesteld tot v2, en alles wat de engineer anders zou hebben aangepakt met meer budget. Een overdracht zónder lijst van bekende gebreken is geen vlekkeloze codebase; het is een incompleet overdrachtsdocument.

**Acht: de geautomatiseerde tests en hoe je ze draait.** Inclusief documentatie over wat ze wel testen - en vooral wat ze bewust níét dekken.

**Negen: een afgebakende nazorgperiode.** Twee weken gegarandeerde beschikbaarheid voor korte vragen, vooraf overeengekomen en meegenomen in de projectprijs. Geen open-einde onderhoudscontract, maar een duidelijke termijn waarbinnen de vraag *"hoe zat dit onderdeel ook alweer in elkaar?"* direct en kosteloos wordt beantwoord.

## Drie specifieke toevoegingen voor met AI gebouwde software

Een codebase die tot stand is gekomen met tools als Lovable, Bolt of Cursor heeft drie unieke overdrachtspunten nodig die bij traditionele maatwerksoftware ontbreken. Zij bepalen of jij na oplevering soepel kunt blijven doorontwikkelen:

**Kan het project nog steeds worden bewerkt in de oorspronkelijke AI-tool?** Als er werk is verzet in Lovable, Bolt of Cursor, moet de overdracht expliciet bevestigen of het project daarin bewerkbaar blijft. Als de directorystructuur of codeconventies zijn aangepast voor productie, moet worden uitgelegd wat dat betekent voor toekomstige AI-prompts. Een oprichter die dit verliest, raakt geruisloos de snelle, goedkope iteratiecyclus kwijt waarvoor hij überhaupt voor deze tools had gekozen.

**Welke code is gegenereerd en welke is handmatig geschreven?** Een volgende engineer behandelt deze codeblokken heel anders: gegenereerde code vereist verificatie op verborgen aannames, terwijl handgeschreven code een bewuste menselijke intentie uitdrukt. Een korte toelichting in de README voorkomt eindeloos giswerk.

**Waar zijn AI-patronen bewust intact gelaten?** Soms is de meest pragmatische beslissing om een typisch AI-patroon dat prima functioneert simpelweg níét te refactoren. Door dit expliciet te vermelden, voorkom je dat een volgende ontwikkelaar uren besteedt aan het 'repareren' van een opzettelijke keuze.

## Voor agencies: de overdracht is een kernonderdeel van je product

Als jouw bureau applicaties bouwt voor opdrachtgevers met behulp van AI-versnellers, is de overdracht hét moment waarop je reputatie wordt gemaakt of stilletjes wordt afgebroken. Het is immers het enige onderdeel dat de klant ervaart nadat de initiële euforie van de lancering is weggeëbd.

Twee werkwijzen onderscheiden bureaus die structureel herhaalopdrachten binnenhalen van bureaus die eenmalig werk leveren:

Ten eerste: overdrachtsdocumenten worden gaandeweg het project geproduceerd, niet haastig bij elkaar geraapt in de laatste twee uur. Het runbook wordt geschreven op het moment dat de deployment-pipeline wordt opgezet; architectuurkeuzes worden genoteerd op het moment dat ze worden gemaakt. Achteraf documenteren kost drie keer zoveel tijd en levert steevast een halfbakken resultaat op.

Ten tweede: de overdracht wordt gedemonstreerd in plaats van gemaild. Een sessie van veertig minuten waarin de klant zélf een kleine wijziging deployt, zelfstandig het runbook volgt om een databaseback-up te herstellen in een scratch-omgeving, en samen de error tracker doorneemt, is honderd keer waardevoller dan een lijvig PDF-rapport. Bovendien komen eventuele hiaten in de instructies direct aan het licht terwijl het team nog aan tafel zit, in plaats van drie maanden later tijdens een storing.

Voor white-label samenwerkingen geldt exact hetzelfde: jouw technische productiepartner levert een kant-en-klaar overdrachtsdossier op dat jij direct onder je eigen bureaulabel aan je eindklant kunt overhandigen.

## Wat een opdrachtgever moet eisen vóór ondertekening

Neem de overdrachtseisen direct op in de initiële projectopdracht, niet pas in de laatste opleverweek. Vijf concrete regels volstaan: de git-repository en alle cloudaccounts vanaf dag één op mijn naam geregistreerd; een runbook voor deploy, rollback en back-up herstel; een complete inventarisatie van secrets; een lijst van bekende gebreken; en de garantie dat het project bewerkbaar blijft in de oorspronkelijke AI-tooling.

Verifieer de overdracht vervolgens proefondervindelijk vóórdat je de slotfactuur betaalt. Voer zelfstandig een kleine wijziging door en deploy deze. Volg het runbook om een back-up terug te zetten. Roteer één API-sleutel aan de hand van de inventarisatie. Als alle drie slagen, is de overdracht echt. Loopt er iets vast, dan heb je het gat gevonden op het moment dat je de betaling nog in handen hebt.

## De werkelijke kosten van een slechte overdracht

De meest zichtbare schadepost is de inwerktijd van de volgende engineer: doorgaans minstens een volle week aan betaald spitwerk om te reconstrueren wat op twee A4'tjes had moeten staan.

De onzichtbare kosten zijn aanzienlijk pijnlijker. Accounts die op naam van een vertrokken freelancer staan, worden het onderwerp van stroeve onderhandelingen. Inloggegevens die bij oud-medewerkers rondslingeren blijven jarenlang actief omdat niemand weet waar ze staan. Een applicatie die niet meer reageert op AI-prompts verliest direct zijn strategische snelheid. En een lijst van bekende gebreken die nooit is opgesteld, betekent dat hetzelfde onderliggende probleem drie keer opnieuw moet worden ontdekt door drie verschillende freelancers - die daar allemaal hun uurtarief voor rekenen.

Niets daarvan is spectaculair drama. Het is simpelweg een sluipende belasting op alles wat je daarna met je product wilt doen.

## Hoe LaunchStudio software overdraagt

LaunchStudio behandelt een overdracht als een contractueel opleverproduct met een inhoudsopgave, niet als een vrijblijvende gunst: repository en cloudaccounts vanaf de start op jouw naam; gedocumenteerde wijzigingen met de achterliggende redenen; een beknopt runbook voor deploy, rollback en herstel; een secrets-inventarisatie met rotatiehandleiding; geautomatiseerde tests inclusief hun randvoorwaarden; een eerlijke opsomming van wat we vonden en níét hebben opgelost; en de garantie dat de code conventioneel en AI-leesbaar blijft zodat je moeiteloos verder kunt in Lovable, Bolt of Cursor. Twee weken actieve support achteraf is standaard inbegrepen.

Die strenge discipline stamt rechtstreeks uit de praktijk van Manifera, waar elf jaar ervaring in enterprise software voor klanten als Vodafone, TNO en CFLW betekent dat opleveringen systematisch worden geaudit. Digitale bureaus benutten exact hetzelfde pakket onder hun eigen naam wanneer wij optreden als geruisloze white-label ontwikkelpartner.

Laat je werk uitvoeren aan een met AI gebouwde app, of bouw je software voor een klant? [Omschrijf je project](https://launchstudio.eu/nl/#contact) en we sturen je onze standaard overdrachts-checklist toe - ongeacht of je met ons in zee gaat.

## Als je nooit een overdracht hebt ontvangen

Veel oprichters die dit lezen hebben al een product in handen dat slecht of helemaal niet is overgedragen. De schade zelf herstellen is gelukkig mogelijk en kost ongeveer één gerichte middag:

**Begin met een inventarisatie van alle accounts.** Loop je creditcardafschriften en e-mailgeschiedenis na op elke externe software- of clouddienst die het product gebruikt. Oprichters vinden steevast slapende abonnementen die ze waren vergeten en, belangrijker, diensten die nog op naam van een externe partij blijken te staan.

**Test wat je daadwerkelijk zelfstandig kunt uitvoeren.** Kun je zelf een update deployen? Een back-up terugzetten? Een API-sleutel vervangen? Elk punt waarop je vastloopt, is je hoogste prioriteit om direct recht te zetten.

**Schrijf zelf een beknopte architectuursamenvatting,** al is het maar in grote lijnen. Twee zinnen over wat waarmee communiceert geeft een volgende engineer iets tastbaars om te verifiëren en corrigeren, in plaats van te moeten gissen.

**Stel de vorige ontwikkelaar drie gerichte vragen,** in plaats van een open verzoek om "documentatie". Vragen zoals: *"waar staan de omgevingsvariabelen opgeslagen?"*, *"hoe deploy ik een hotfix?"* en *"welk onderdeel zou jij als eerste aanpakken?"* krijgen direct antwoord; een vraag om "kun je wat docs sturen" verdwijnt in de prullenbak.

**Roteer vervolgens alle sleutels** waarvan je niet 100% zeker bent wie er toegang toe heeft. Het is de snelste en goedkoopste manier om een ontbrekende overdracht definitief af te sluiten.

## Het overdrachtsgesprek zelf

De documentatie is belangrijk, maar de veertig minuten waarin alles live wordt gedemonstreerd is doorslaggevend. Een effectieve sessie volgt een vaste opbouw:

**Start met het overzicht, niet met de details.** Twee minuten over welke systemen met elkaar communiceren. Alle details landen veel beter zodra de luisteraar het grotere plaatje begrijpt.

**Doe het zélf, in plaats van te kijken naar een schermdeling.** Degene die de overdracht ontvangt voert de handelingen uit: deployt een kleine tekstwijziging, volgt het draaiboek om een back-up te restoren, en opent de dashboards. De vertrekkende ontwikkelaar kijkt mee en zegt niets tenzij er een vraag wordt gesteld. Elk punt waarop de ontvanger aarzelt, legt direct een hiaat in de documentatie bloot - op het enige moment dat het nog direct hersteld kan worden.

**Loop de storingspaden door.** Waar meldt de error tracker zich? Hoe zagen de laatste drie incidenten eruit? Wat zijn de eerste stappen als de website offline gaat? Incidentherstel is iets dat je minimaal één keer gezien moet hebben.

**Lees de lijst met bekende gebreken hardop voor.** Geschreven lijstjes worden snel gescand; uitgesproken punten roepen vragen op, en die vragen brengen waardevolle context naar boven die nooit in de tekst was beland.

**Neem de sessie op.** Een video-opname van veertig minuten is de goedkoopste en meest waardevolle documentatie die er bestaat. Het is exact de video die een nieuwe ontwikkelaar over vier maanden bekijkt wanneer niemand meer bereikbaar is.

## Echt voorbeeld

### Een digitaal bureau dat een klant verloor door een ontbrekend runbook

Bureau Nordkaap, een digitaal bureau van zes man in Leeuwarden, leverde een leden- en toertochtenplatform op voor een regionale wielervereniging. Het project verliep vlot: een Bolt-prototype productierijp gemaakt, betalingen gekoppeld, strak op tijd gelanceerd en de klant was enthousiast.

Elf weken later stuurde de penningmeester van de vereniging op zondagavond om 21:40 uur een paniekmail: de website lag plat en niemand bij het bureau nam de telefoon op. De lead developer die de site had gebouwd zat op een berg in Italië zonder bereik. Niemand anders binnen het bureau wist hoe de deployment-pipeline werkte, het hostingaccount stond op het persoonlijke creditcardaccount van die specifieke developer, de database-inloggegevens stonden uitsluitend in diens persoonlijke wachtwoordkluis en er was geen enkele regel overdrachtsdocumentatie.

De website kwam pas maandagmiddag rond 14:00 uur weer online. De wielervereniging zegde het beheercontract de maand erop per direct op. De reden die het bestuur gaf was niet de technische storing zelf - maar het feit dat een overzichtelijk probleem van vijf uur was veranderd in een downtime van zeventien uur door omstandigheden die niets met de software te maken hadden.

Bureau Nordkaap produceert sindsdien standaard bij elk project een sluitend overdrachtsdossier en sluit elk traject af met een live demonstratiesessie. Hun vaste productiepartner levert hetzelfde pakket op white-label basis, dat het bureau rechtstreeks onder eigen vlag aan opdrachtgevers overhandigt.

**Resultaat:** bij elf opeenvolgende klantprojecten deden zich drie keer incidenten buiten kantoortijd voor. Alle drie werden binnen het uur opgelost door iemand anders dan de oorspronkelijke bouwer - twee keer zelfs door de klant zélf, simpelweg door de stappen in het runbook te volgen.

> *"We hadden technisch gezien niets verkeerd gedaan. We hadden alleen van onszelf de enige sleuteldrager tot een werkende website gemaakt, en de klant had dat eerder door dan wijzelf."*
> - **Joke Hoekstra, Directeur, Bureau Nordkaap (Leeuwarden)**

**Kosten & Doorlooptijd:** € 1.400 (overdrachtspakket, accountmigratie, operationeel runbook en demonstratiesessie, achteraf ingericht voor twee bestaande klanten) - afgerond binnen 3 werkdagen.

## Veelgestelde vragen

### Wat is het allerbelangrijkste onderdeel van een projectoverdracht?

Dat alle cloudaccounts, hostingomgevingen en repositories vanaf dag één op jouw eigen bedrijfsnaam staan geregistreerd. Alles in de softwarecode kan met wat moeite worden gereconstrueerd; een account dat eigendom is van een onbereikbare freelancer vereist een juridische discussie waar geen technische oplossing voor bestaat.

### Hoe verifieer ik of een overdracht daadwerkelijk compleet is?

Door het zelfstandig te testen vóórdat je de eindfactuur betaalt: voer zelf een kleine codewijziging door en deploy deze, volg het runbook om een back-up terug te zetten in een testomgeving, en roteer één API-sleutel aan de hand van de inventarisatie. Lukt dat allemaal binnen een uur, dan is de overdracht solide.

### Hoort een overdracht ook een lijst van onopgeloste gebreken te bevatten?

Ja, absoluut. Een lijst van bekende gebreken en uitgestelde wensen (known issues) is het keurmerk van een transparante, professionele oplevering. Het ontbreken ervan betekent vrijwel altijd dat dezelfde verborgen gebreken later opnieuw moeten worden ontdekt door een volgende ontwikkelaar - tegen diens volle uurtarief.

### Kan ik mijn app na professionele productiewerkzaamheden nog steeds bewerken in Lovable of Cursor?

Dat hoort uitdrukkelijk wel zo te zijn, en de overdracht moet dit zwart-op-wit bevestigen. Vraag om de garantie dat de codestructuur conventioneel en AI-leesbaar blijft, en verifieer dit direct door zelf een kleine tekstuele prompt uit te voeren in je vertrouwde AI-builder.

### Wanneer moet een bureau de overdrachtsdocumentatie schrijven?

Gaandeweg het project, op het moment dat keuzes worden gemaakt en pipelines worden opgezet. Alles pas in de allerlaatste week achteraf proberen te reconstrueren kost drie keer zoveel tijd en levert onder tijdsdruk vrijwel altijd een mager en onvolledig document op.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is het allerbelangrijkste onderdeel van een projectoverdracht?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dat alle accounts en repositories vanaf het begin op jouw eigen naam staan. Code is te reconstrueren; een account dat vastzit bij een onbereikbare derde is een juridisch conflict."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe verifieer ik of een overdracht daadwerkelijk compleet is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Test het vóór de slotbetaling: deploy een kleine wijziging, herstel een back-up aan de hand van het runbook en roteer één credential uit de inventarisatielijst."
      }
    },
    {
      "@type": "Question",
      "name": "Hoort een overdracht ook een lijst van onopgeloste gebreken te bevatten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. Een lijst met bekende gebreken toont professionaliteit. Het ontbreken ervan betekent dat dezelfde problemen later opnieuw ontdekt moeten worden op jouw kosten."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik mijn app na professionele productiewerkzaamheden nog steeds bewerken in Lovable of Cursor?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dat hoort wel zo te zijn en moet expliciet bevestigd worden. Zorg dat de codebase conventioneel blijft en test dit met een kleine prompt in je eigen AI-tool."
      }
    },
    {
      "@type": "Question",
      "name": "Wanneer moet een bureau de overdrachtsdocumentatie schrijven?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Tijdens het project, zodra beslissingen vallen en pipelines worden gebouwd. Alles achteraf doen kost driemaal zoveel tijd en leidt tot magere documentatie."
      }
    }
  ]
}
</script>
