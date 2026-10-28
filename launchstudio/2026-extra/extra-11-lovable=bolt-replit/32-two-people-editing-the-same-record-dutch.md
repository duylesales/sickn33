---
Titel: "Gelijktijdigheid in Lovable en Supabase: Wanneer twee mensen hetzelfde record bewerken"
Trefwoorden: Lovable, lost update problem, optimistic concurrency version column, idempotency double submit, database constraint race condition, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Gelijktijdigheid in Lovable en Supabase: Wanneer twee mensen hetzelfde record bewerken

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Gelijktijdigheid in Lovable en Supabase: Wanneer twee mensen hetzelfde record bewerken",
  "description": "Verloren updates, dubbele verzendingen en race conditions op beperkte voorraad zijn onzichtbaar tijdens ontwikkeling maar dagelijkse realiteit in productie. Hoe ze ontstaan, waar de oplossing thuishoort en hoe je ze test.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-04",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/two-people-editing-the-same-record" }
}
</script>

Een planner opent om 10:14 uur een werkbon in het systeem en begint het adres aan te passen. Haar collega opent om 10:15 uur exact hetzelfde record, corrigeert het telefoonnummer en slaat het formulier op om 10:17 uur. De planner klikt om 10:19 uur op 'Opslaan'. Het gewijzigde telefoonnummer is spoorloos verdwenen, niemand krijgt een waarschuwing en een week later wordt de klant op het verouderde nummer gebeld.

Er trad geen enkele foutmelding op. Beide opslagacties slaagden technisch met statuscode 200. De database deed exact waar hij om gevraagd werd: de complete formulierinhoud overnemen van degene die als laatste op opslaan klikte, en daarmee alles overschrijven wat er op dat moment stond.

Dit fenomeen heet het *lost update problem*. Het is een van de drie typische gelijktijdigheidsproblemen (concurrency issues) die AI-gegenereerde applicaties standaard produceren: volkomen onzichtbaar tijdens de bouwfase, aan de orde van de dag in productie, en onmogelijk op te sporen door louter de code te inspecteren.

## Waarom niets hiervan zichtbaar is tijdens het testen

Tijdens het bouwen test je alleen. Je klikt op een knop, wacht op het resultaat en klikt op de volgende. Elke bewerking is volledig afgerond vóórdat de volgende begint. De tijdsinteracties die deze bugs veroorzaken, kunnen in die opzet simpelweg niet optreden.

In productie is de dynamiek het tegenovergestelde: tientalle gebruikers gelijktijdig, meerdere browsertabbladen open, haperende 4G-verbindingen waardoor gebruikers twee keer op een knop tikken omdat er ogenschijnlijk niets gebeurt, en geplande achtergrondtaken die data bijwerken terwijl iemand aan het bewerken is. De code is exact hetzelfde; de timing is radicaal anders. En timing is precies waar deze fouten ontstaan.

## Fout één: De verloren update (Lost Update)

Het scenario hierboven beschreven. Twee gebruikers laden hetzelfde record in hun browser, beiden passen iets aan en slaan op. De tweede opslagactie overschrijft geruisloos de wijzigingen van de eerste - inclusief velden die de tweede persoon niet eens heeft aangeraakt, omdat een webformulier standaard álle velden meestuurt die het oorspronkelijk heeft ingeladen.

**De eenvoudigste en meest betrouwbare oplossing is optimistische gelijktijdigheid (optimistic concurrency).** Voeg een versienummer (`version INT`) of een `updated_at`-tijdstempel toe aan de databaserij. Zodra een gebruiker het formulier opent, ontvangt hij de huidige versie. Bij het opslaan wordt de update uitsluitend doorgevoerd als het versienummer in de database nog exact overeenkomt met de ingeladen versie (`WHERE id = $1 AND version = $2`). Heeft een collega in de tussentijd al opgeslagen? Dan raakt de update nul rijen. Je applicatie vangt dit op, legt aan de gebruiker uit dat het record tussentijds is gewijzigd en toont netjes de verschillen.

Dit vereist slechts een minimale schemamutatie en een bescheiden stukje logica, maar het transformeert geruisloos dataverlies in een heldere, begrijpelijke melding.

**Het alternatief, updates op veldniveau (field-level patching),** stuurt uitsluitend de gewijzigde velden door in plaats van het hele formulier. Dit verkleint de kans op botsingen naar exact hetzelfde veld in plaats van het hele record, maar vergt aanzienlijk meer werk in de gebruikersinterface. Voor de meeste compacte SaaS-apps is versienummering de beste eerste stap.

## Fout twee: De dubbele verzending (Double Submission)

Een reiziger tikt op de knop "Bevestigen" terwijl de trein een tunnel inrijdt. De verbinding hapert, er verschijnt geen direct laadicoon en hij tikt nogmaals. De server ontvangt twee identieke verzoeken vlak na elkaar. Gevolg: er worden twee afzonderlijke boekingen aangemaakt, het abonnementsbedrag wordt twee keer afgeschreven, of er worden dubbele uitnodigingsmails verzonden.

Het uitschakelen (disablen) van de verzendknop na de eerste klik via JavaScript is louter een beleefdheid naar de gebruiker, geen veilige bescherming. Het tweede verzoek kan al onderweg zijn, en een haperende browser of ongeduldige gebruiker kan deze frontend-beveiliging eenvoudig omzeilen.

**De oplossing is idempotentietoetsing (idempotency):** de frontend genereert een unieke sleutel (een willekeurige UUID) voor de specifieke actie en stuurt deze mee in de header van het verzoek. De server registreert deze sleutel. Komt er binnen enkele minuten een tweede verzoek binnen met exact dezelfde sleutel? Dan voert de server de actie niet nogmaals uit, maar retourneert simpelweg het oorspronkelijke resultaat. Alle grote betaalproviders (zoals Stripe en Mollie) hanteren dit principe om dubbele incasso's te voorkomen, en ditzelfde patroon hoort thuis op elk endpoint dat records aanmaakt of transacties uitvoert.

Voor eenvoudigere use-cases volstaat een database-uniekheidsrestrictie (`UNIQUE constraint`) - bijvoorbeeld één actieve boeking per gebruiker per tijdslot, afgedwongen op het niveau waar omzeiling onmogelijk is.

## Fout drie: De race condition op schaarse capaciteit

Tien beschikbare concertkaartjes, tien stoelen verkocht, twee bezoekers die op exact dezelfde seconde klikken, elf uitgegeven tickets.

De door AI gegenereerde code leest volkomen logisch: controleer eerst of er nog plek is (`count < capacity`), en maak vervolgens de boeking aan (`INSERT INTO bookings`). In productie voeren beide browsers de controle tegelijkertijd uit vóórdat een van beiden de nieuwe rij heeft weggeschreven. Beiden zien één vrije plek, beiden krijgen groen licht, en beiden slaan op. Hoe vaak je die codefunctie ook doorleest, je vindt de fout niet - want het probleem schuilt in het tijdsverschil tussen de twee afzonderlijke SQL-commando's.

**De oplossing hoort thuis in de database, niet in je applicatielogica.** Voer de controle en het wegschrijven uit als één ondeelbare, atomaire operatie: een voorwaardelijke update die uitsluitend slaagt zolang de capaciteit groter is dan nul (`UPDATE events SET booked = booked + 1 WHERE id = $1 AND booked < capacity`), of wikkel beide acties in een databasetransactie met expliciete rijvergrendeling (`SELECT ... FOR UPDATE`).

Het fundamentele principe: als de correctheid van je data ervan afhangt dat twee operaties niet door elkaar heen lopen, kan frontend- of backend-code dat nooit garanderen. Een relationele database kan dat wél.

## Waar de controle daadwerkelijk moet plaatsvinden

Dit is de rode draad bij gelijktijdigheid. Controles in de browser beschermen tegen niets. Controles in pure applicatiecode beschermen uitsluitend tegen opeenvolgende fouten, nooit tegen gelijktijdige acties. Uitsluitend een database-constraint of een atomaire bewerking houdt stand onder echte belasting, omdat de database het centrale knooppunt is waar alle parallelle verzoeken samenkomen.

Voor een oprichter zonder diepgaande databasekennis luidt de vuistregel: elke bedrijfsregel waarbij "twee tegelijk zou een fout opleveren" moet worden vastgelegd als een constraint in de database, niet louter als validatielogica in de frontend. Denk aan: unieke boekingen per tijdslot, voorraadstanden die nooit onder nul mogen zakken, maximaal één actief abonnement per organisatie of een kortingscode die slechts één keer verzilverd mag worden.

## Wat je communiceert naar de eindgebruiker

Het afvangen van gelijktijdigheidsconflicten betekent dat de applicatie soms een bewerking moet weigeren. Hoe je dat formuleert, bepaalt de gebruikerservaring.

*"Dit record is zojuist aangepast door een collega terwijl u aan het bewerken was. Hier ziet u de gewijzigde gegevens - wilt u uw versie overschrijven of de pagina vernieuwen?"* is een uitstekende melding: het legt de situatie helder uit, toont wat er veranderd is en biedt de gebruiker controle.

*"Foutmelding: versieconflict (409 Conflict)"* is dezelfde technische beveiliging, maar gepresenteerd als een systeemcrash die direct leidt tot gefrustreerde support-e-mails.

Waar mogelijk voorkom je het conflict liever dan dat je het moet melden: toon aanwezigheid in de interface (presence indicators zoals *"Jan bekijkt deze pagina momenteel ook"*) of sla concepten automatisch op de achtergrond op.

## Handmatig testen zonder complexe testtools

Elk van deze problemen kun je binnen tien minuten met de hand simuleren:

**Verloren update:** open hetzelfde record in twee verschillende browsers (of een gewoon venster en een incognitovenster), pas in beide schermen een ander veld aan, en klik in het tweede scherm eerst op opslaan en daarna pas in het eerste. Controleer of de eerste opslagactie de tweede overschrijft.

**Dubbele verzending:** open de ontwikkelaarstools van je browser (F12), zet de netwerksnelheid op "Slow 3G", verstuur een formulier en klik direct nog een keer op de knop terwijl het verzoek nog verwerkt wordt.

**Schaarse capaciteit:** zet de beschikbare capaciteit van een item tijdelijk op één. Open twee tabbladen en klik in beide schermen vrijwel tegelijkertijd op de boekingsknop.

Voer deze tests uit voor elke feature waar een fout commerciële of operationele schade veroorzaakt. Het is het meest waardevolle testuur voor een vroege SaaS-applicatie en brengt fouten aan het licht die geen enkele statische code review ontdekt.

## Welke functionaliteiten dit écht nodig hebben

Niet elk formulier heeft zware concurrency-beveiliging nodig. Het overal toepassen van complexe vergrendelingen maakt een applicatie onnodig traag en complex.

De onderdelen die dit absoluut vereisen, delen één kenmerk: twee gelijktijdige acties leveren een foutief resultaat op dat direct opgemerkt wordt. Boekingen met beperkte capaciteit. Voorraadbeheer. Saldi en tegoeden. Formulieren die door meerdere teamleden tegelijk worden beheerd. Betalings- en facturatiestatussen. Het inwisselen van vouchers of uitnodigingen.

Onderdelen die dit doorgaans niet nodig hebben: een persoonlijk gebruikersprofiel dat uitsluitend door de eigenaar wordt bewerkt, een persoonlijk notitieconcept dat niemand anders kan zien, of een auditlog die uitsluitend nieuwe rijen toevoegt (append-only).

## Dit technisch solide laten inrichten

Gelijktijdigheid is het ultieme voorbeeld van een uitdaging die niet opgelost kan worden door simpelweg beter naar de code te staren, maar die een database moeiteloos afhandelt zodra de juiste regels op het juiste niveau worden gedefinieerd. LaunchStudio richt dit in als onderdeel van het klaarmaken van AI-prototypes voor productie: identificeren van tijdsgevoelige bedrijfsprocessen, implementeren van optimistische versiekolommen op gedeelde data, inrichten van idempotentiesleutels op betaal- en aanmaakflows, verankeren van capaciteitsregels in database-constraints en het automatiseren van belastingtests in de CI/CD-pipeline.

De frontend die je hebt ontworpen in Lovable, Bolt of Cursor blijft onaangetast, en de broncode blijft helder gedocumenteerd en AI-leesbaar. Dit maakt deel uit van het [Launch Ready-pakket](https://launchstudio.eu/nl/#packages), uitgevoerd door de engineers van Manifera vanuit Amsterdam en Ho Chi Minhstad, met elf jaar productie-ervaring voor veeleisende opdrachtgevers als Vodafone, TNO en CFLW.

Verkoopt jouw applicatie iets met beperkte beschikbaarheid en wil je zeker weten dat het systeem niet bezwijkt onder gelijktijdige boekingen? [Beschrijf je project](https://launchstudio.eu/nl/#contact) en wij analyseren binnen één werkdag de risico's.

## Optimistisch of pessimistisch vergrendelen: Welke kies je?

Er bestaan twee overkoepelende strategieën voor gegevensbeveiliging, en de keuze daartussen is logischer dan de termen doen vermoeden:

**Optimistisch vergrendelen** gaat ervan uit dat gelijktijdige bewerkingen relatief zeldzaam zijn. Iedereen kan direct beginnen met bewerken; pas op het moment van opslaan wordt gecontroleerd of er een conflict is opgetreden. Dit is het model met de versiekolom, en het is de ideale aanpak voor records die incidenteel door meerdere mensen worden geraadpleegd - zoals een klantkaart, vacaturetekst of productomschrijving. Het risico is dat een gebruiker zijn wijzigingen kan kwijtraken bij het opslaan, wat je opvangt door de verschillen inzichtelijk te maken.

**Pessimistisch vergrendelen (locking)** voorkomt conflicten vooraf door data te blokkeren: zodra één persoon begint te bewerken, is het record voor anderen geblokkeerd. Dit past bij schermen waar gebruikers urenlang intensief aan werken en waar elk dataverlies desastreus is - zoals een complexe juridische overeenkomst of een uitgebreid medisch dossier. Het nadeel is dat locks moeten verlopen met een time-out, omdat een gebruiker die zijn laptop dichtklapt anders het hele record permanent blokkeert voor collega's.

Voor de meeste vroege SaaS-producten is optimistisch vergrendelen de aangewezen standaard, eventueel aangevuld met actieve aanwezigheidsindicatoren in de interface.

Kies één duidelijke lijn en wissel niet willekeurig af per scherm. Een systeem waarin sommige formulieren blokkeren en andere elkaar geruisloos overschrijven, leert gebruikers dat de applicatie onvoorspelbaar is.

## Echt voorbeeld

### Een cursusplatform dat veertien plekken verkocht in een lokaal voor twaalf

Marloes Huisman bouwde Ambachtsklas in Lovable: een platform voor creatieve workshops en ambachtscursussen van zelfstandige keramisten en houtbewerkers in Utrecht en Amersfoort. De workshops hebben een strikte maximale capaciteit en zijn vaak binnen enkele minuten uitverkocht.

Het probleem trad aan het licht op een zaterdagochtend bij de lancering van een populaire cursus pottenbakken. Er waren twaalf draaischijven beschikbaar; er werden veertien boekingen afgerekend; en bij aanvang stonden er twee deelnemers in een lokaal zonder plek. De docent moest twee teleurgestelde cursisten naar huis sturen en Marloes verloor het vertrouwen van een belangrijke partner.

Het inspecteren van de boekingsfunctie bracht ogenschijnlijk geen fouten aan het licht: de functie telde het aantal bestaande boekingen, vergeleek dat met de capaciteit en voegde netjes een rij toe. Maar tijdens de stormloop van gelijktijdige boekingen draaiden meerdere checks tegelijkertijd vóórdat de eerste rij was opgeslagen.

In vijf werkdagen werd de backend gehard: capaciteit werd omgezet naar een atomaire voorwaardelijke update in PostgreSQL zodat een boeking uitsluitend kan slagen zolang de teller onder het maximum blijft; een database-uniekheidsrestrictie voorkomt dat één gebruiker per ongeluk twee keer op dezelfde cursus wordt ingeschreven; er werden idempotentiesleutels toegevoegd aan de betaal- en boekingsflow tegen dubbelklikken; op de workshopgegevens werd optimistische versienummering geactiveerd; duidelijke UI-meldingen tonen wanneer een cursus vol is; en er werd een automatische stresstest ingericht die vijftig gelijktijdige boekingen simuleert bij elke release.

**Resultaat:** twee maanden later verliep de lancering van een uitverkochte reeks van zes workshops vlekkeloos zonder enige overboeking. De geautomatiseerde test bewees direct zijn waarde door een regressiefout op te vangen toen er later een wachtlijstfunctie werd toegevoegd.

> *"Ik heb die boekingsfunctie wel twintig keer herlezen op zoek naar de bug. De bug was dat twee mensen op exact dezelfde seconde klikten - en dat is iets wat je met het blote oog nooit in de code kunt zien."*
> - **Marloes Huisman, Oprichter, Ambachtsklas (Utrecht)**

**Kosten & Doorlooptijd:** € 2.500 (atomaire capaciteitsbewaking, idempotentietoetsing, versienummering, gelijktijdigheidstests in deployment-pipeline) - afgerond in 5 werkdagen.

## Veelgestelde vragen

### Waarom trad er overboeking op terwijl mijn code de beschikbaarheid netjes controleert?
Omdat de beschikbaarheidscontrole en het daadwerkelijke wegschrijven twee afzonderlijke bewerkingen zijn. Bij gelijktijdige verzoeken voeren meerdere gebruikers de controle uit vóórdat de eerste boeking is vastgelegd. Beide zien vrije plekken. De capaciteitsregel moet atomair in de database worden afgedwongen.

### Wat is de eenvoudigste oplossing tegen gebruikers die elkaars wijzigingen overschrijven?
Optimistische gelijktijdigheid via een versiekolom in de database. Deze versie wordt meegestuurd bij het openen van het formulier en moet matchen bij het opslaan. Als een ander het record tussentijds heeft gewijzigd, mislukt de update en kun je de gebruiker informeren over de wijzigingen.

### Voorkomt het uitschakelen van de verzendknop dubbele betalingen of boekingen?
Nee. Het tweede verzoek kan al onderweg zijn en frontend-beperkingen zijn triviaal te omzeilen door netwerkhaperingen of snelle clicks. Gebruik altijd een unieke idempotentietoets (UUID) op de server of een uniekheidsrestrictie in de database.

### Moet ik deze beveiliging op elk scherm in mijn applicatie doorvoeren?
Nee, uitsluitend bij processen waar gelijktijdige acties tot foute data leiden die operationele schade veroorzaakt: capaciteit, voorraden, tegoeden, gedeelde records, betaalstatussen en vouchercodes. Persoonlijke profielen of logs hebben dit niet nodig.

### Hoe kan ik gelijktijdigheidsproblemen testen zonder ingewikkelde software?
Simpelweg met de hand: open hetzelfde record in twee browsers en sla ze in omgekeerde volgorde op; simuleer een trage 3G-verbinding in de browsertools en dubbelklik op verzenden; of boek de allerlaatste beschikbare plek vanuit twee tabbladen tegelijk. Binnen tien minuten vind je bugs die een code review mist.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom trad er overboeking op terwijl mijn code de beschikbaarheid netjes controleert?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat de check en de schrijfoperatie losse stappen zijn. Bij gelijktijdige verzoeken lopen controles synchroon vóórdat data is weggeschreven. De regel moet atomair in de database worden afgedwongen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de eenvoudigste oplossing tegen gebruikers die elkaars wijzigingen overschrijven?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Optimistische gelijktijdigheid met een versiekolom. Bij het opslaan moet de versie overeenkomen; is er tussentijds opgeslagen, dan wordt de update geweigerd en kan het verschil worden getoond."
      }
    },
    {
      "@type": "Question",
      "name": "Voorkomt het uitschakelen van de verzendknop dubbele betalingen of boekingen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Het tweede netwerkverzoek kan al onderweg zijn. Gebruik altijd een idempotentiesleutel op de backend of een database-uniekheidsrestrictie."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik deze beveiliging op elk scherm in mijn applicatie doorvoeren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, alleen waar gelijktijdige acties schade veroorzaken: capaciteitsbeheer, voorraadstanden, gedeelde klantrecords en financiële transacties."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe kan ik gelijktijdigheidsproblemen testen zonder ingewikkelde software?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Met de hand: sla hetzelfde record op vanuit twee browsers in omgekeerde volgorde, test met een trage netwerksimulatie met dubbelklikken, of boek de laatste plek tegelijkertijd in twee tabbladen."
      }
    }
  ]
}
</script>
