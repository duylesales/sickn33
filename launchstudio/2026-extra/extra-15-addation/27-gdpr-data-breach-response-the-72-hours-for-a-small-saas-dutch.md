---
Titel: "AVG Datalek-Respons: De Eerste 72 Uur voor een Kleine SaaS"
Trefwoorden: gdpr data breach saas, datalek melden 72 uur, data breach response plan startup, autoriteit persoonsgegevens datalek, LaunchStudio, Manifera
Koperfase: Bewustzijn
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# AVG Datalek-Respons: De Eerste 72 Uur voor een Kleine SaaS

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AVG Datalek-Respons: De Eerste 72 Uur voor een Kleine SaaS",
  "description": "Onder de AVG moet een inbreuk in verband met persoonsgegevens vaak binnen 72 uur worden gemeld aan de toezichthouder, en moeten verwerkers hun klanten zonder onredelijke vertraging informeren. Deze gids loodst een klein SaaS-team door het eerste uur, de eerste dag en de volledige 72 uur, legt uit wanneer de Autoriteit Persoonsgegevens en betrokkenen moeten worden ingelicht, en toont de technische voorbereiding die een beheerste respons mogelijk maakt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-14",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/gdpr-data-breach-response-the-72-hours-for-a-small-saas" },
  "citation": [
    { "@type": "CreativeWork", "name": "AVG Artikel 33: Melding van een inbreuk in verband met persoonsgegevens aan de toezichthoudende autoriteit", "url": "https://gdpr-info.eu/art-33-gdpr/" },
    { "@type": "CreativeWork", "name": "AVG Artikel 34: Mededeling van een inbreuk in verband met persoonsgegevens aan de betrokkene", "url": "https://gdpr-info.eu/art-34-gdpr/" },
    { "@type": "CreativeWork", "name": "EDPB Richtlijnen 9/2022 over de melding van datalekken", "url": "https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-92022-personal-data-breach-notification-under_en" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens: Datalekken", "url": "https://www.autoriteitpersoonsgegevens.nl/themas/beveiliging/datalekken" }
  ]
}
</script>

Het begint meestal met een bericht dat op het eerste gezicht onschuldig lijkt. Een gebruiker stuurt een e-mail dat hij per ongeluk de factuur van een ander bedrijf kan inzien. Een developer ontdekt een vergeten API-sleutel in een openbare GitHub-repository. Uw error tracker toont plotseling honderden verdachte aanvragen op een endpoint dat niet publiek had mogen zijn. Of een klant stuurt een screenshot door van een discussieforum. Voor een klein SaaS-team - zeker wanneer het product in hoog tempo met AI-tools is gebouwd - is de eerste menselijke reactie vaak: het probleem stilletjes dichten en hopen dat niemand het gemerkt heeft.

Onder de Algemene Verordening Gegevensbescherming (AVG) kan die reflex een beheersbaar technisch incident transformeren in een juridisch en commercieel drama. Bij een inbreuk in verband met persoonsgegevens (een datalek) begint de klok direct te tikken: in veel gevallen moet de toezichthouder binnen 72 uur na ontdekking worden ingelicht, en als verwerker moet u uw zakelijke klanten zonder onredelijke vertraging waarschuwen. Elk datalek moet bovendien intern worden geregistreerd, ook als er geen formele meldplicht geldt. Professioneel afgehandeld is een datalek een stressvolle week; verkeerd aangepakt leidt het tot contractbreuk, verlies van klantvertrouwen en aanzienlijke boetes van de toezichthouder.

Deze gids beschrijft stap voor stap wat u uur na uur moet doen. Dit is algemene informatie, geen juridisch advies; schakel bij een reëel incident altijd direct een privacyjurist in.

## Belangrijkste Punten

- **Een datalek is veel breder dan een gerichte hack.** Het omvat ook onbedoelde openbaarmaking, verlies van back-ups, ongeautoriseerde inzage en tijdelijke onbeschikbaarheid van persoonsgegevens.
- **Verwerkingsverantwoordelijken moeten binnen 72 uur melden** aan de Autoriteit Persoonsgegevens (AP), tenzij het onwaarschijnlijk is dat het lek een risico inhoudt voor de rechten en vrijheden van betrokkenen.
- **Verwerkers moeten hun opdrachtgevers zonder onredelijke vertraging informeren.** Voor B2B SaaS betekent dit dat u uw zakelijke klanten direct waarschuwt, zodat zij hun eigen wettelijke 72-uurstermijn halen.
- **Betrokken personen moeten worden gewaarschuwd** indien het lek waarschijnlijk een hoog risico oplevert voor hun persoonlijke levenssfeer.
- **Elk datalek moet intern worden gedocumenteerd,** inclusief de feiten, de gevolgen en de genomen herstelmaatregelen, ongeacht of er extern is gemeld.

## Wat Geldt Wettelijk Als een Datalek?

De AVG definieert een inbreuk in verband met persoonsgegevens als een inbreuk op de beveiliging die per ongeluk of op onrechtmatige wijze leidt tot de vernietiging, het verlies, de wijziging of de ongeoorloofde verstrekking van of de ongeoorloofde toegang tot doorgezonden, opgeslagen of anderszins verwerkte gegevens. Europese toezichthouders onderscheiden drie hoofdcategorieën:

- **Inbreuk op de vertrouwelijkheid:** ongeautoriseerde inzage of openbaarmaking (bijvoorbeeld een klant die data van een andere klant ziet, een openbare opslagbucket of gelekte databasedumps).
- **Inbreuk op de integriteit:** ongeoorloofde wijziging van gegevens (een kwaadwillende die records muteert of een softwarefout die data van gebruikers overschrijft).
- **Inbreuk op de beschikbaarheid:** verlies van toegang of permanente vernietiging (ransomware, per ongeluk gewiste databases zonder werkende back-up).

In door AI gebouwde applicaties zijn vertrouwelijkheidsinbreuken door ontbrekende autorisatie veruit de meest voorkomende oorzaak: Row Level Security (RLS) die op één tabel per ongeluk uitstaat, API-endpoints zonder eigendomscontrole, of bestanden die zonder authenticatie via voorspelbare URL's te downloaden zijn.

## Verantwoordelijke of Verwerker: Wiens Klok Tikt?

Uw concrete wettelijke verplichtingen hangen af van uw rol ten aanzien van de getroffen gegevens:

| Gegevensstroom | Uw rol | Verplichting |
| --- | --- | --- |
| Uw eigen klantaccounts, betaalgegevens, marketingcontacten | Verwerkingsverantwoordelijke | Risico beoordelen, binnen 72 uur melden bij de AP indien vereist, betrokkenen informeren bij hoog risico |
| Gegevens die uw zakelijke klanten in uw SaaS invoeren | Verwerker | De getroffen klanten zonder onredelijke vertraging informeren en hen technisch ondersteunen |

Voor verwerkers geldt dat "zonder onredelijke vertraging" zeer strikt wordt geïnterpreteerd. De 72-uurstermijn van uw zakelijke klant vangt immers pas aan op het moment dat zij van het incident op de hoogte zijn - in de praktijk op het moment dat u hen waarschuwt. Veel verwerkersovereenkomsten schrijven een contractuele meldtermijn van 24 of 48 uur voor. Raadpleeg uw klantcontracten vóórdat er iets gebeurt, niet tijdens de crisis.

## Het Eerste Uur: Indammen en Bewijs Veiligstellen

**1. Dicht het lek direct (indamming).** Sluit het beveiligingsgat zodra dit veilig kan: deactiveer het openstaande endpoint, zet de cloud-bucket per direct op privé, trek gecompromitteerde API-sleutels in en activeer ontbrekende databasepolicies. Is de exacte oorzaak niet direct duidelijk, schakel dan het kwetsbare onderdeel of de complete functionaliteit tijdelijk uit.

**2. Stel bewijsmateriaal veilig.** Verwijder nooit overhaast logs, wis geen servers en herinitialiseer de database niet voordat u begrijpt wat er is gebeurd. Exporteer alle relevante server- en API-logs, noteer exacte tijdstempels en maak screenshots. U heeft dit bewijs nodig voor de risicobeoordeling en de formele melding.

**3. Start een logboek.** Houd direct een centraal incidentenlogboek bij. Noteer chronologisch wat er is ontdekt, op welk exact tijdstip, wie erbij betrokken is en welke maatregelen worden genomen. Dit logboek vormt het wettelijke bewijs van uw zorgvuldigheid.

**4. Wijs één incidentleider aan.** Eén persoon moet de regie voeren over de technische afhandeling en de communicatie. Bij een startup is dit doorgaans de oprichter, bijgestaan door de hoofd-engineer.

## De Eerste Dag (Binnen 24 Uur): Omvang Vaststellen

Binnen de eerste 24 uur moet u antwoord hebben op de volgende kernvragen:

- **Wat is er precies gebeurd?** De technische oorzaak en het mechanisme van het incident.
- **Wanneer begon het en wanneer is het beëindigd?** Datalekken ontstaan vaak al weken of maanden vóór de daadwerkelijke ontdekking.
- **Welke categorieën gegevens zijn getroffen?** Betreft het gewone contactgegevens of bijzondere persoonsgegevens (gezondheid, financiën, wachtwoorden, BSN)?
- **Wiens gegevens zijn gelekt?** Welke zakelijke klanten zijn geraakt, om hoeveel individuele betrokkenen gaat het en zitten er kwetsbare groepen tussen (zoals minderjarigen)?
- **Is de data daadwerkelijk ingezien of gedownload?** Aan de hand van serverlogs kan vaak worden vastgesteld of documenten daadwerkelijk door onbevoegden zijn geopend of alleen theoretisch blootstonden.
- **Is het lek definitief ingedamd?** Controleer of soortgelijke kwetsbaarheden niet elders in de codebase aanwezig zijn.

Hier blijkt direct het belang van een gedegen voorbereiding. Zonder auditlogging op bestandsopslag en databases kunt u nooit bewijzen of data wel of niet is gedownload, waardoor u juridisch van het allerzwartste scenario moet uitgaan. Ons artikel over het [verwerkingsregister volgens AVG Artikel 30](https://launchstudio.eu/nl/blog/records-of-processing-for-small-saas-gdpr-article-30) toont hoe u vooraf inzicht houdt in uw datastromen.

Treedt u op als verwerker? Breng getroffen klanten reeds op deze eerste dag op de hoogte, ook als het technisch onderzoek nog loopt. Wees eerlijk over wat u weet, wat u momenteel onderzoekt en wanneer de volgende update volgt.

## Binnen 72 Uur: Risicobeoordeling en Melding

**Beoordeel het risico.** De verwerkingsverantwoordelijke moet beoordelen of het datalek waarschijnlijk een risico oplevert voor de rechten en vrijheden van betrokkenen. Relevante factoren zijn de aard en gevoeligheid van de data, het aantal personen, het gevaar van identiteitsfraude, financiële schade of reputatieschade, en of de gelekte data sterk versleuteld was.

**Meld bij de toezichthouder indien vereist.** Tenzij het onwaarschijnlijk is dat het lek een risico inhoudt, moet de verantwoordelijke binnen 72 uur melding doen bij de toezichthouder. In Nederland gebeurt dit digitaal via het meldloket van de Autoriteit Persoonsgegevens. De melding bevat:

- De aard van de inbreuk, inclusief de categorieën en geschatte aantallen betrokkenen en datarecords
- De contactgegevens van de functionaris of contactpersoon voor nadere inlichtingen
- De waarschijnlijke gevolgen van de inbreuk
- De reeds genomen en voorgestelde maatregelen om het lek te verhelpen en nadelige gevolgen te verzachten

Beschikt u binnen 72 uur nog niet over alle details? Doe dan tijdig een voorlopige melding en vul de gegevens later gefaseerd aan. Een te late melding vereist een schriftelijke motivering en wordt door de toezichthouder streng beoordeeld.

**Informeer betrokken burgers of gebruikers bij een hoog risico.** Indien het datalek waarschijnlijk een hoog risico oplevert voor de persoonlijke levenssfeer van individuen (zoals bij gelekte medische gegevens, financiële gegevens of inloggegevens), moet de verantwoordelijke de betrokkenen zonder onredelijke vertraging rechtstreeks inlichten in duidelijke taal, inclusief handelingsperspectief (zoals het wijzigen van wachtwoorden). Dit is niet verplicht indien passende technische beschermingsmaatregelen (zoals sterke encryptie) waren toegepast waardoor de data onbruikbaar is voor derden.

## Heldere Communicatie Naar Klanten

Voor een B2B SaaS-onderneming is de communicatie naar zakelijke klanten vaak van doorslaggevend belang voor het voortbestaan van het bedrijf. Een professioneel incidentbericht:

- Beschrijft feitelijk en zonder omhaal wat er is gebeurd, zonder het incident te bagatelliseren
- Geeft exact aan welke data van die specifieke klant wel en niet is geraakt
- Legt puntsgewijs uit welke directe maatregelen zijn genomen om herhaling uit te sluiten
- Bevat een concrete instructie over wat de klant zelf moet ondernemen (zoals hun eigen melding bij de AP)
- Biedt een rechtstreeks telefoonnummer of contactpersoon voor technische vragen
- Noemt een exact tijdstip voor de volgende statusupdate

Klanten accepteren dat software incidenten kan doormaken; wat zij niet accepteren is stilzwijgen, verhulling of halve waarheden. Een snelle, proactieve en eerlijke melding versterkt vaak de zakelijke vertrouwensband; een klant die via een forum ontdekt dat uw app lekte, zegt zijn contract direct op.

## Na het Incident: Grondoorzaak Wegnemen

Het dichten van de initiële kwetsbaarheid is niet voldoende. Onderzoek waarom het probleem kon ontstaan en elimineer soortgelijke fouten structureel:

- Ontbrak Row Level Security op één tabel? Controleer de policies van álle tabellen in de database.
- Ontbrak een autorisatiecheck op een endpoint? Bouw geautomatiseerde negatieve autorisatietests in uw CI/CD-pijplijn.
- Was een API-sleutel zichtbaar in git? Voer geautomatiseerde secret scans uit over de hele commit-geschiedenis en roteer alle actieve geheimen.
- Heeft een AI-prompt per ongeluk beveiligingscontroles gewist? Zorg voor strikt beveiligde paden en regressietests.

Documenteer de geleerde lessen en pas uw incidentprocedure direct aan. Onze handleiding over [het roteren van alle geheimen na een lek](https://launchstudio.eu/nl/blog/ai-app-security-rotating-every-secret-after-a-leak) behandelt de technische nazorg bij uitgelekte sleutels.

## Interne Documentatieplicht: Altijd Verplicht

Artikel 33 lid 5 van de AVG verplicht de verwerkingsverantwoordelijke om élke inbreuk in verband met persoonsgegevens intern te documenteren in een datalekkenregister, met inbegrip van de feiten, de gevolgen en de genomen corrigerende maatregelen. Dit geldt dus ook voor incidenten die níet bij de AP zijn gemeld. De toezichthouder kan dit register bij een controle opvragen om te verifiëren of u terecht heeft afgezien van een externe melding.

Een beknopt datalekkenregister bevat:

| Veld | Inhoud |
| --- | --- |
| Datum en tijd van ontdekking | Exact moment waarop de organisatie op de hoogte raakte |
| Beschrijving van het incident | Wat er is gebeurd en de technische toedracht |
| Betrokken data en personen | Categorieën, aantallen en gevoeligheidsgraad |
| Risicobeoordeling | De schriftelijke motivering waarom er wel of geen risico bestond |
| Meldingen | Data en referentienummers van meldingen aan de AP, klanten of betrokkenen |
| Maatregelen | Directe indamming, structurele herstelacties en preventieve aanpassingen |

## Preventieve Maatregelen: Wees Voorbereid

Een beheerste reactie op een datalek is voor 90% het gevolg van preventieve voorbereiding. Een gezonde technische basis omvat:

- Een compact incidentenprotocol van één pagina: iedereen weet direct wie de beslissingen neemt
- Een actuele contactenlijst: oprichter, lead-engineer, privacyjurist en cloud-support
- Sluitende audit- en toegangslogging: direct kunnen aantonen of geëxposeerde data daadwerkelijk is opgevraagd
- Een actuele datamap: direct inzichtelijk hebben welke tabellen persoonsgegevens bevatten
- Geverifieerde verwerkersovereenkomsten: weten binnen hoeveel uur klanten geïnformeerd moeten worden
- Geteste back-up- en herstelprocedures: bescherming tegen dataverlies en gijzelsoftware
- Vooraf opgestelde meldingssjablonen: binnen enkele uren een feitelijk en professioneel bericht kunnen uitsturen

## Hoe LaunchStudio Helpt

LaunchStudio ondersteunt SaaS-oprichters zowel preventief als tijdens acute incidenten. Vóór een incident richten wij de noodzakelijke technische fundamenten in: geauditeerde Row Level Security, auditlogging op databases en opslag, veilig geheimenbeheer, periodiek geteste back-ups en een heldere systeemarchitectuur. Bij een acuut incident helpen onze senior engineers het lek direct technisch in te dammen, serverlogs minutieus te analyseren, de grondoorzaak in de codebase te verhelpen en geautomatiseerde autorisatietests toe te voegen, terwijl uw juridisch adviseur zich richt op de formele meldingen.

Het **Launch Ready**-pakket (€800 - €3.500) omvat security audits, herstelwerkzaamheden en preventieve voorbereiding; **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) voegt managed hosting, 24/7 uptime-monitoring en prioriteitsondersteuning toe met snelle responstijden bij incidenten. Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een gerichte prijsindicatie.

LaunchStudio wordt aangedreven door Manifera, een softwarebedrijf met meer dan 11 jaar ervaring, 160+ projecten en 120+ software-engineers. CEO Herre Roelevink was medeoprichter van het cybersecuritybedrijf dat tegenwoordig opereert als CFLW Cyber Strategies (ontwikkelaar van de Dark Web Monitor in samenwerking met TNO). Oprichters ontmoeten ons team aan de Herengracht 420 in Amsterdam; de engineering vindt plaats vanuit het ontwikkelcentrum aan Pho Quang Street in Ho Chi Minhstad, met een hub aan Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Zaterdagochtend-E-mail Over de Loonstrook van een Ander

Mark Wouters bouwde Loonstrookportaal met Bolt en Supabase: een beveiligd portaal waarmee kleine administratiekantoren salarisstroken en jaaropgaven delen met werknemers van hun zakelijke cliënten. Op een zaterdagochtend ontving Mark een e-mail van een medewerker van een bakkerijketen: door simpelweg een volgnummer in de downloadlink van zijn loonstrook aan te passen, kreeg hij direct de loonstrook van een collega te zien - en bij een ander nummer zelfs die van een medewerker van een heel ander bedrijf.

Marks eerste impuls was om de URL-logica snel te patchen en verder te zwijgen. In plaats daarvan nam hij direct contact op met LaunchStudio. Binnen één uur werd de gehele opslagbucket afgesloten, werden alle actieve downloadlinks direct ongeldig gemaakt en werden de storage- en API-logs veiliggesteld voor forensisch onderzoek. Uit de analyse bleek dat documenten zeven maanden lang via voorspelbare numerieke URL's in een openbare cloud-bucket hadden gestaan, en dat toegangslogging op de opslaglaag niet was geactiveerd. Hierdoor kon niet met zekerheid worden aangetoond welke bestanden door derden waren opgevraagd. In totaal stonden ruim 9.000 salarisstroken van 41 administratiekantoren potentieel bloot.

Omdat Loonstrookportaal optrad als verwerker voor de administratiekantoren, stelde Mark dezelfde zaterdagmiddag alle 41 kantoren op de hoogte met een feitelijk bericht, een overzicht van de documenten per kantoor en een direct telefoonnummer. LaunchStudio leverde een technisch rapport op dat de kantoren direct konden gebruiken voor hun melding bij de Autoriteit Persoonsgegevens. De technische sanering werd grondig aangepakt: documenten verhuisden naar hermetisch afgesloten private storage met cryptografisch ondertekende links die na vijf minuten automatisch verlopen, Row Level Security werd per administratiekantoor en werknemer opnieuw afgedwongen in PostgreSQL, auditlogging werd geactiveerd op de opslag en database, negatieve autorisatietests werden toegevoegd aan alle routes, en er werd een formeel incidentenprotocol opgesteld met kant-en-klare meldingssjablonen.

**Resultaat:** Alle 41 administratiekantoren konden dankzij de tijdig verstrekte informatie ruimschoots binnen de wettelijke 72-uurstermijn aan hun meldplicht voldoen. Twee kantoren besloten hun contract op te zeggen; 39 kantoren bleven klant, waarbij meerdere directeuren expliciet lieten weten dat de snelheid, transparantie en eerlijkheid van de communicatie de doorslag hadden gegeven. Sindsdien hebben zich geen nieuwe incidenten voorgedaan.

> *"Het stilletjes patchen van die link had me op zaterdag een hoop stress bespaard. Maar het direct en eerlijk informeren van mijn klanten binnen enkele uren is de enige reden dat mijn bedrijf vandaag de dag nog bestaat."*
> - **Mark Wouters, Oprichter, Loonstrookportaal (Venlo)**

**Kosten & Doorlooptijd:** €4.200 (Launch & Grow-pakket: directe incidentindamming, loganalyse, migratie naar private storage met signed URL's, RLS-herbouw, auditlogging, securitytests en opstellen incidentprotocol) - indamming binnen enkele uren, volledige structurele sanering in 8 werkdagen.

## Veelgestelde Vragen

### Moet ik een datalek altijd binnen 72 uur melden bij de Autoriteit Persoonsgegevens?

Niet in alle gevallen. De verwerkingsverantwoordelijke moet binnen 72 uur melden, tenzij het onwaarschijnlijk is dat het lek een risico inhoudt voor de rechten en vrijheden van personen. Elk incident moet wél intern worden vastgelegd in uw datalekkenregister. Treedt u op als verwerker, dan moet u uw zakelijke klant zonder onredelijke vertraging informeren zodat zij hun afweging kunnen maken.

### Wanneer moeten getroffen personen rechtstreeks worden gewaarschuwd?

Wanneer het datalek waarschijnlijk een hoog risico oplevert voor hun persoonlijke levenssfeer, bijvoorbeeld bij blootstelling van medische data, financiële gegevens, wachtwoorden of BSN-nummers. Er gelden uitzonderingen, bijvoorbeeld wanneer de data onleesbaar was gemaakt door sterke versleuteling en de sleutel niet is gecompromitteerd.

### Wat als ik binnen 72 uur nog niet over alle feiten beschik?

Meld tijdig met de feiten die op dat moment wél bekend zijn. De AVG staat uitdrukkelijk toe dat nadere informatie gefaseerd wordt aangeleverd. Het uitstellen van de initiële melding tot het onderzoek volledig is afgerond leidt tot overschrijding van de wettelijke termijn, wat door de toezichthouder als een zware overtreding wordt gezien.

### Hoe helpt de ervaring van Manifera bij het beheersen van een datalek?

Manifera's CEO heeft een jarenlange achtergrond in cybersecurity, en het engineeringteam heeft ruim 11 jaar ervaring met incidentreparatie en forensisch onderzoek in complexe bedrijfsomgevingen. LaunchStudio helpt incidenten snel in te dammen, bewijsmateriaal veilig te stellen en de grondoorzaak in de software permanent te verhelpen.

### Heeft de afhandeling van een datalek invloed op de online reputatie van een SaaS?

Absoluut. Datalekken komen dikwijls naar buiten via klanten, sociale media of fora. Een proactieve, transparante en professionele reactie bepaalt hoe het incident achteraf wordt beoordeeld in de markt, inclusief de samenvattingen die zoekmachines en AI-zoeksystemen genereren over de betrouwbaarheid van uw onderneming.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik een datalek altijd binnen 72 uur melden bij de Autoriteit Persoonsgegevens?",
      "acceptedAnswer": { "@type": "Answer", "text": "Niet altijd. De verantwoordelijke meldt binnen 72 uur tenzij een risico voor betrokkenen onwaarschijnlijk is; alle lekken moeten intern worden gedocumenteerd." }
    },
    {
      "@type": "Question",
      "name": "Wanneer moeten getroffen personen rechtstreeks worden gewaarschuwd?",
      "acceptedAnswer": { "@type": "Answer", "text": "Wanneer het lek waarschijnlijk een hoog risico oplevert, zoals bij gevoelige financiële, medische gegevens of inloggegevens, tenzij data onleesbaar versleuteld was." }
    },
    {
      "@type": "Question",
      "name": "Wat als ik binnen 72 uur nog niet over alle feiten beschik?",
      "acceptedAnswer": { "@type": "Answer", "text": "Meld binnen 72 uur met de reeds bekende gegevens en lever details gefaseerd na; te laat melden vereist een gegronde reden en wordt streng bestraft." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij het beheersen van een datalek?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera's leiding komt uit cybersecurity. LaunchStudio damt incidenten binnen uren in, bewaart bewijs en verhelpt grondoorzaken structureel in de codebase." }
    },
    {
      "@type": "Question",
      "name": "Heeft de afhandeling van een datalek invloed op de online reputatie van een SaaS?",
      "acceptedAnswer": { "@type": "Answer", "text": "Zeker. Een snelle, eerlijke respons bepaalt hoe het incident wordt beoordeeld door klanten, toezichthouders en AI-zoekmachines die het merk evalueren." }
    }
  ]
}
</script>
