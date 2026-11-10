---
Titel: "Verwerkingsregister voor Kleine SaaS: AVG Artikel 30"
Trefwoorden: gdpr article 30 saas, records of processing activities template, verwerkingsregister avg, processing register small business, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Verwerkingsregister voor Kleine SaaS: AVG Artikel 30

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Verwerkingsregister voor Kleine SaaS: AVG Artikel 30",
  "description": "Artikel 30 van de AVG verplicht vrijwel elk SaaS-bedrijf om een register van verwerkingsactiviteiten bij te houden, zowel als verwerkingsverantwoordelijke als in de rol van verwerker. Deze gids legt de mkb-uitzondering uit en waarom deze zelden geldt voor software, wat de registers moeten bevatten, hoe u ze opbouwt vanuit de werkelijke datastromen van uw AI-app en hoe u ze actueel houdt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-12",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/records-of-processing-for-small-saas-gdpr-article-30" },
  "citation": [
    { "@type": "CreativeWork", "name": "AVG Artikel 30: Register van de verwerkingsactiviteiten", "url": "https://gdpr-info.eu/art-30-gdpr/" },
    { "@type": "CreativeWork", "name": "AVG Artikel 28: Verwerker", "url": "https://gdpr-info.eu/art-28-gdpr/" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens: Verwerkingsregister", "url": "https://www.autoriteitpersoonsgegevens.nl/themas/basis-avg/avg-algemeen/verwerkingsregister" },
    { "@type": "CreativeWork", "name": "Artikel 29-Werkgroep standpunt over Artikel 30(5) uitzonderingen", "url": "https://ec.europa.eu/newsroom/article29/items/624045" }
  ]
}
</script>

De meeste software-oprichters maken kennis met de Algemene Verordening Gegevensbescherming (AVG) via direct zichtbare elementen: een privacyverklaring op de website, een cookiebanner of een verwerkersovereenkomst voor zakelijke klanten. Veel minder oprichters zijn bekend met het formele document dat aan al deze afspraken ten grondslag ligt: het register van verwerkingsactiviteiten, in de praktijk kortweg het verwerkingsregister genoemd. Artikel 30 van de AVG verplicht organisaties om een dergelijk register bij te houden, en toezichthouders zoals de Autoriteit Persoonsgegevens (AP) kunnen dit document te allen tijde opvragen.

Voor een SaaS-onderneming is dit register veel meer dan louter administratieve ballast. Het vormt een gedetailleerde technische plattegrond van waar persoonsgegevens uw product binnenkomen, hoe ze stromen, welke subverwerkers erbij betrokken zijn en hoe lang gegevens worden bewaard. Dit overzicht beantwoordt acute vragen van zakelijke klanten, security-auditors en investeerders. Bovendien brengt het vaak datastromen aan het licht waarvan de oprichter het bestaan niet eens vermoedde - een bekend fenomeen bij applicaties die in hoog tempo zijn gebouwd met Lovable, Bolt of Cursor en onderweg aan talloze externe API's zijn gekoppeld.

Deze gids beschrijft wat Artikel 30 concreet vereist en hoe een kleine SaaS-startup in één tot twee dagen een waardevol en sluitend verwerkingsregister opzet. Dit is algemene informatie, geen juridisch advies.

## Belangrijkste Punten

- **Artikel 30 van de AVG vereist een register van verwerkingsactiviteiten** van zowel verwerkingsverantwoordelijken als verwerkers, met elk een specifiek wettelijk verplicht format.
- **De uitzondering voor bedrijven met minder dan 250 medewerkers geldt vrijwel nooit voor SaaS,** omdat gegevensverwerking in een cloudapplicatie niet incidenteel is, maar juist de kern van de dienstverlening vormt.
- **Een SaaS-bedrijf heeft doorgaans twee afzonderlijke registers nodig:** één als verantwoordelijke (voor eigen accounts, facturatie, marketing en personeel) en één als verwerker (voor de data die klanten in uw app invoeren).
- **Bouw het register op vanuit de feitelijke datastromen,** door uw databasetabellen, API-koppelingen en externe clouddiensten te inventariseren, in plaats van blind te vertrouwen op een generiek sjabloon.
- **Houd het register continu actueel,** aangezien elke nieuwe API-koppeling, AI-functie of analysetool direct invloed heeft op uw gegevensstromen.

## Wat Artikel 30 Vereist

Artikel 30 maakt een strikt onderscheid tussen de twee hoedanigheden die een organisatie kan aannemen onder de privacywetgeving.

**Als verwerkingsverantwoordelijke (controller)** bepaalt u zélf het doel en de middelen van de gegevensverwerking. Denk hierbij aan gebruikersaccounts van uw klanten, abonnementsfacturen, nieuwsbriefabonnees en personeelsdossiers. Uw register als verantwoordelijke moet minimaal bevatten:

- Uw naam en contactgegevens, en eventueel die van uw Functionaris Gegevensbescherming (FG/DPO)
- De specifieke doeleinden van de gegevensverwerking
- De categorieën van betrokkenen (zoals klanten, websitebezoekers, sollicitanten) en categorieën van persoonsgegevens
- De categorieën van ontvangers aan wie gegevens worden verstrekt, inclusief partijen buiten de EU
- Doorgiften van persoonsgegevens naar derde landen buiten de EER, inclusief de passende waarborgen (zoals Standard Contractual Clauses)
- Waar mogelijk, de beoogde bewaartermijnen voor de verschillende categorieën gegevens
- Waar mogelijk, een algemene beschrijving van de technische en organisatorische beveiligingsmaatregelen

**Als verwerker (processor)** verwerkt u persoonsgegevens uitsluitend in opdracht en ten behoeve van uw klanten. Denk aan de patiëntendossiers die een fysiotherapiepraktijk opslaat in uw praktijksoftware, of de kandidaat-cv's die een recruitmentbureau beheert in uw ATS. Uw register als verwerker moet minimaal bevatten:

- Uw naam en contactgegevens, en die van elke verantwoordelijke (klant) namens wie u optreedt
- De categorieën van verwerkingen die u voor rekening van elke klant uitvoert
- Eventuele doorgiften naar derde landen buiten de EU en de gehanteerde waarborgen
- Waar mogelijk, een beknopte beschrijving van de getroffen beveiligingsmaatregelen

Het register moet schriftelijk worden vastgelegd (wat ook elektronisch in een spreadsheet of document mag) en moet op eerste verzoek direct aan de toezichthouder kunnen worden overhandigd.

## Waarom de Mkb-Vrijstelling Vrijwel Nooit Opgaat voor SaaS

Artikel 30 lid 5 bevat een uitzonderingsbepaling: de registerplicht geldt niet voor ondernemingen met minder dan 250 werknemers, *tenzij* de verwerking niet incidenteel is, een risico inhoudt voor de rechten en vrijheden van betrokkenen, of bijzondere categorieën van gegevens (zoals gezondheidsdata of strafrechtelijke gegevens) betreft.

Bij een SaaS-bedrijf is de gegevensverwerking het product zélf. De verwerking vindt continu, structureel en geautomatiseerd plaats - en is dus per definitie niet incidenteel. De Europese privacytoezichthouders (voormalig Artikel 29-Werkgroep, thans EDPB) en de Nederlandse Autoriteit Persoonsgegevens hebben herhaaldelijk verduidelijkt dat deze uitzondering restrictief moet worden uitgelegd. Zodra aan één van de 'tenzij'-voorwaarden wordt voldaan, moet voor die verwerkingen verplicht een register worden bijgehouden.

In de praktijk moet nagenoeg elk SaaS-bedrijf dat klantdata verwerkt aan de registerplicht voldoen, ongeacht of er één of vijftig medewerkers zijn. Beschouw het register daarom als een standaardvereiste.

## Verantwoordelijke vs. Verwerker: Wat Geldt Waarvoor?

| Gegevensstroom | Uw rol | Concreet voorbeeld |
| --- | --- | --- |
| Accountgegevens van gebruikers van uw klanten | Veelal verantwoordelijke voor accountbeheer, verwerker voor de inhoud | Naam, zakelijk e-mailadres en wachtwoordhash voor authenticatie |
| Gegevens die uw klanten zélf invoeren in de SaaS | Verwerker | Medische dossiers in zorgsoftware, sollicitatiebrieven in een recruitmenttool |
| Facturatie- en betaalgegevens | Verwerkingsverantwoordelijke | Bedrijfsnaam, btw-nummer, factuuradres, transactiegeschiedenis via Stripe |
| Marketingcontacten en leads | Verwerkingsverantwoordelijke | E-maillijst voor productupdates, ingevulde contactformulieren |
| Website- en productstatistieken | Verwerkingsverantwoordelijke | Geaggregeerde paginaweergaven, sessieduur, UTM-parameters |
| Supporttickets en klantvragen | Verantwoordelijke (soms met verwerkerstaken bij meegestuurde screenshots) | E-mails gericht aan uw supportdesk |
| Uw eigen medewerkers en freelancers | Verwerkingsverantwoordelijke | Arbeidsovereenkomsten, urenregistraties, bankrekeningnummers |

Dit onderscheid is essentieel omdat de wettelijke plichten verschillen. Als verantwoordelijke bepaalt u zélf de AVG-grondslag en handelt u inzage- en verwijderverzoeken van betrokkenen af. Als verwerker handelt u uitsluitend volgens de schriftelijke instructies van uw klant (vastgelegd in de verwerkersovereenkomst) en ondersteunt u hen bij hun AVG-plichten.

## Hoe U het Register Opbouwt Vanuit Uw Werkelijke Applicatie

Sjablonen zijn handig voor de tabelstructuur, maar de inhoud moet exact overeenkomen met uw feitelijke systemen. Volg dit stappenplan:

**1. Inventariseer uw database.** Loop elke tabel en elk gegevensveld na in Supabase, PostgreSQL of Firebase. AI-codertools voegen geregeld overbodige velden toe "voor het geval dat", zoals geboortedata, telefoonnummers of vrije notitievelden. Deze stap legt direct databallast bloot die u beter kunt saneren.

**2. Inventariseer alle externe clouddiensten.** Maak een complete lijst van alle externe partijen die aan uw app zijn gekoppeld: hostingprovider, database, authenticatiedienst, transactionele e-mail (zoals Resend of SendGrid), betaalproviders (Stripe, Mollie), analytics, error tracking (Sentry), klantenservice-tools, AI-modellen (OpenAI, Anthropic), automatiseringsplatformen en cloudopslag. Noteer per partij welke persoonsgegevens zij ontvangen, met welk doel en in welk land de verwerking plaatsvindt.

**3. Breng de datastromen in kaart.** Volg het pad van elke categorie data: waar komt het binnen (webformulier, CSV-import, API), waar wordt het opgeslagen, naar welke subverwerkers wordt het doorgestuurd en wanneer verlaat het het systeem (exports, e-mailnotificaties).

**4. Bepaal verwerkingsdoelen en bewaartermijnen.** Formuleer voor elke activiteit een helder doel in één zin en stel een realistische bewaartermijn vast. "Totdat het account wordt opgeheven, plus 30 dagen voor back-ups" is een geldige en controleerbare termijn; "onbeperkt" is in strijd met de AVG.

**5. Beschrijf de beveiligingsmaatregelen.** Vat de getroffen maatregelen bondig samen: encryptie in rust en tijdens transport, toegangscontrole via Row Level Security (RLS), multi-factor authenticatie, geautomatiseerde back-ups en auditlogging.

**6. Registreer internationale doorgiften.** Controleer of diensten data verwerken buiten de Europese Unie (met name in de VS). Leg vast welk wettelijk doorgiftemechanisme van toepassing is, zoals het EU-US Data Privacy Framework of goedgekeurde Standard Contractual Clauses (SCC's).

## Een Praktisch en Werkbaar Format

Een spreadsheet of gestructureerd document volstaat. Elke rij beschrijft één verwerkingsactiviteit:

| Activiteit | Doel | Betrokkenen | Datacategorieën | Ontvangers | Locatie & Doorgifte | Bewaartermijn | Beveiliging |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Klantaccounts beheren | Toegang verlenen tot de SaaS-dienst | Gebruikers van klanten | Naam, e-mailadres, rol, inloggeschiedenis | Hosting- en authenticatieprovider | EU | Duur van het account + 30 dagen | Zie beveiligingsoverzicht (MFA, encryptie) |
| Facturatie & betaling | Uitvoeren van de overeenkomst en fiscale plicht | Contactpersonen klant | Bedrijfsnaam, factuuradres, betaalstatus | Betaalprovider, boekhoudsoftware | EU | 7 jaar (fiscale bewaarplicht) | Toegangsbeperking, encryptie |
| Product analytics | Verbeteren van de softwareprestaties | Gebruikers van klanten | Pseudonieme gebruikersacties, browserversie | Analytics-provider | EU | 24 maanden | Geaggregeerd, geen directe identificatoren |
| Transactionele e-mail | Versturen van verificatie- en systeemberichten | Gebruikers van klanten | E-mailadres, inhoud van het bericht | E-mailleverancier | EU / VS onder DPF | Maximaal 30 dagen in verzendlogs | TLS-versleuteling, SPF/DKIM |
| Technische support | Beantwoorden van helpdeskvragen | Gebruikers van klanten | Naam, e-mailadres, inhoud van het ticket | Helpdesk-software | EU | 2 jaar na sluiting van het ticket | Alleen toegankelijk voor supportmedewerkers |

Het register voor uw rol als verwerker is compacter: het bevat de verwerkingen die u voor uw zakelijke klanten uitvoert, de categorieën data, de lijst met ingeschakelde subverwerkers en de beveiligingswaarborgen.

## Typische Ontdekkingen Bij het Eerste Register

**AI-functies die data ongemerkt naar de VS sturen.** Een handige samenvattings- of vertaalfunctie die een AI-API in de Verenigde Staten aanroept, zonder dat dit ergens is vastgelegd en zonder getoetste verwerkersvoorwaarden.

**Vergeten achtergronddiensten.** Een error tracking-tool (zoals Sentry) die per ongeluk volledige HTTP-aanvragen inclusief ingevulde formuliergegevens vastlegt, of een verouderde webhook die data naar een testplatform kopieert.

**Ontbrekende bewaartermijnen.** Inactieve proefaccounts, verouderde leads en verwijderde tickets die voor altijd in de database blijven staan.

**Overtollige datavelden.** Formulieren die door AI-generatie standaard vragen naar telefoonnummers of privégegevens die nergens in het bedrijfsproces worden benut.

**Inconsistenties met de privacyverklaring.** Externe tools die wél in de code draaien maar nergens in de privacyverklaring worden genoemd, of omgekeerd: diensten die al lang zijn opgezegd maar nog wel op de website vermeld staan.

Elke ontdekking biedt directe winst: het opschonen van overbodige datavelden en diensten verlaagt direct uw beveiligingsrisico, reduceert cloudkosten en versnelt toekomstige leveranciersaudits.

## Verbinding Met Overige Privacy-Documenten

Het verwerkingsregister vormt het fundament voor uw complete compliance-huishouding:

- **Privacyverklaring:** moet naadloos aansluiten op de doelen, bewaartermijnen en ontvangers in uw verantwoordelijkenregister.
- **Verwerkersovereenkomsten:** de subverwerkerslijst en datacategorieën in uw klantcontracten moeten exact overeenkomen met uw verwerkersregister.
- **DPIA's:** risicovolle verwerkingen die in het register worden geïdentificeerd, vereisen mogelijk een formele gegevensbeschermingseffectbeoordeling. Onze gids over [DPIA's voor AI-functionaliteiten](https://launchstudio.eu/nl/blog/dpia-for-an-ai-feature-when-you-need-one) legt uit wanneer dit verplicht is.
- **Datalekken en incidenten:** bij een onverhoopt beveiligingsincident toont het register direct welke persoonsgegevens en welke betrokkenen gevaar lopen. Zie ons artikel over [de 72 uur na een datalek](https://launchstudio.eu/nl/blog/gdpr-data-breach-response-the-72-hours-for-a-small-saas).

## Het Register Actueel Houden

Een verwerkingsregister dat eenmalig wordt geschreven en vervolgens in een la verdwijnt, verliest snel zijn waarde. Integreer onderhoud in uw ontwikkelproces:

- **Elke nieuwe integratie** of externe API activeert direct een update van het register.
- **Elk nieuw databaseveld** met persoonsgegevens wordt vooraf getoetst aan het omschreven doel en dataminimalisatie.
- **Een periodieke check** (bijvoorbeeld ieder kwartaal een halfuur) volstaat om alle actieve clouddiensten door te nemen.
- **Versiebeheer:** houd datum en versienummer bij in het document; dit toont auditors dat uw compliance leeft.

## Hoe LaunchStudio Helpt

LaunchStudio biedt geen juridisch advies, maar verzorgt het grondige technische werk waar een betrouwbaar verwerkingsregister op rust: het inventariseren van databasetabellen en externe API's, het traceren van datastromen, het saneren van overbodige datavelden en koppelingen, het configureren van verwerking binnen EU-regio's, het automatiseren van retentie- en verwijdercycli en het documenteren van de technische beveiligingsmaatregelen. Oprichters ontvangen een heldere technische datamap die zij of hun privacyjurist direct kunnen omzetten in het formele AVG-register.

Het **Launch Ready**-pakket (€800 - €3.500) dekt dit traject af als onderdeel van een productielancering inclusief security hardening en deployment. **Launch & Grow** (€2.500 - €7.500 plus €49 per maand) voegt managed hosting, geautomatiseerde back-ups, 24/7 monitoring en prioriteitsondersteuning toe. Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een gerichte schatting.

LaunchStudio wordt aangedreven door Manifera, een softwareontwikkelingsbedrijf met meer dan 11 jaar ervaring, 160+ opgeleverde projecten en 120+ engineers met ruime ervaring in het realiseren van veilige applicaties conform Europese privacyregels (voor klanten zoals Vodafone en TNO). Oprichters ontmoeten het team aan de Herengracht 420 in Amsterdam; de engineering wordt uitgevoerd vanuit het ontwikkelcentrum aan Pho Quang Street in Ho Chi Minhstad, met een hub aan Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Recruitment-Tool Met Elf Ongedocumenteerde Verwerkers

Jesse van Dam bouwde Vacatureflow met Lovable en Supabase: een applicant tracking tool (ATS) voor kleine wervings- en selectiebureaus in de Randstad, waarmee recruiters kandidaatprofielen, cv's en interviewnotities opslaan en shortlists delen met opdrachtgevers. Toen een groter recruitmentbureau als potentiële klant vroeg om zijn verwerkingsregister en subverwerkerslijst voor een leveranciersbeoordeling, realiseerde Jesse zich dat hij over geen van beide documenten beschikte.

Het opstellen van het register bracht aanzienlijk meer knelpunten aan het licht dan voorzien. Vacatureflow maakte gebruik van elf verschillende externe clouddiensten - variërend van transactionele e-mail en error tracking tot een AI-dienst die automatisch cv's analyseerde - waarvan er diverse ontbraken in de privacyverklaring. De cv-parser verwerkte data op servers in de Verenigde Staten zonder verwerkersovereenkomst, de error tracker legde volledige HTTP-aanvragen inclusief kandidaatdata vast in logging, en kandidaatprofielen werden nooit geanonimiseerd of gewist, zelfs niet jaren na de afronding van een vacature. Daarnaast bleken AI-gegenereerde invoervelden standaard te vragen naar geboortedata en nationaliteit, zonder dat hier enig wervingsdoel voor bestond.

LaunchStudio bracht een complete technische datakaart tot stand van elke tabel, elk veld en elke actieve dienst. De overbodige invoervelden en drie niet-essentiële clouddiensten werden direct verwijderd. De cv-parsing werd overgezet naar een Europese leverancier onder een formele verwerkersovereenkomst zonder modeltraining, en de error logging werd opnieuw geconfigureerd zodat persoonsgegevens en payload-bodies automatisch worden gefilterd. Er werd een geautomatiseerde retentiefunctie gebouwd die kandidaatprofielen 12 maanden na de laatste interactie anonimiseert, tenzij de kandidaat uitdrukkelijk instemt met een langer verblijf in de talentpool. Tot slot documenteerden engineers alle beveiligingsmaatregelen en subverwerkers, waarmee Jesse en zijn privacyadviseur het formele verwerkingsregister en de privacyverklaring compleet maakten.

**Resultaat:** Jesse overhandigde beide registers en de subverwerkerslijst binnen twee weken aan het recruitmentbureau, waarna de leveranciersaudit met vlag en wimpel werd goedgekeurd. Het saneren van data en overbodige diensten verlaagde bovendien direct de hosting- en softwarekosten, en exact dezelfde documentenset is inmiddels met succes ingezet bij vier nieuwe klanttrajecten.

> *"Ik dacht dat een verwerkingsregister puur een administratief vinkje was. Het feitelijk opstellen ervan liet me zien welke data ik helemaal niet nodig had, welke diensten ik straal vergeten was en welke privacyrisico's ik over het hoofd zag."*
> - **Jesse van Dam, Oprichter, Vacatureflow (Haarlem)**

**Kosten & Doorlooptijd:** €2.800 (Launch Ready-pakket: technische data mapping, veld- en dienstreductie, migratie naar Europese AI-verwerker, geautomatiseerde dataretentie en securitydocumentatie) - afgerond in 9 werkdagen.

## Veelgestelde Vragen

### Heeft een kleine SaaS-startup verplicht een verwerkingsregister nodig?

Vrijwel altijd wel. De AVG-uitzondering voor bedrijven met minder dan 250 werknemers geldt niet wanneer de gegevensverwerking niet incidenteel is, privacyrisico's inhoudt of bijzondere persoonsgegevens betreft. Een cloudapplicatie verwerkt continu en geautomatiseerd data van gebruikers, waardoor de registerplicht voor die processen gewoon van kracht is, ongeacht de omvang van uw onderneming.

### Wat is het verschil tussen het verantwoordelijkenregister en het verwerkersregister?

Het verantwoordelijkenregister heeft betrekking op processen waarvoor u zélf het doel bepaalt (klantaccounts, abonnementen, eigen marketing, personeel). Het verwerkersregister betreft de gegevens die u uitsluitend in opdracht van uw klanten verwerkt binnen uw applicatie (zoals dossiers die zij opslaan) en bevat een overzicht van uw klanten en ingeschakelde subverwerkers.

### Kan ik volstaan met een standaardsjabloon voor mijn verwerkingsregister?

Uitsluitend voor de tabelindeling. De feitelijke inhoud moet exact worden afgeleid van uw werkelijke applicatie: databasetabellen, actieve API-koppelingen, datastromen, bewaartermijnen en beveiligingsmaatregelen. Een blind ingevuld standaardsjabloon mist steevast externe diensten en datavelden die auditors of klanten bij een technische controle direct opmerken.

### Hoe helpt de ervaring van Manifera bij AVG-documentatie?

Manifera ontwikkelt en documenteert al meer dan 11 jaar software volgens strenge Europese privacykaders. LaunchStudio benut die expertise om datastromen nauwgezet in kaart te brengen, overbodige databallast te elimineren en logging te beveiligen, zodat uw register een zuivere afspiegeling vormt van een veilige, privacybewuste software-architectuur.

### Draagt een gedegen verwerkingsregister bij aan de commerciële slagkracht van een SaaS?

Absoluut. Een actueel verwerkingsregister en een transparant subverwerkersoverzicht nemen bij zakelijke kopers direct twijfels weg over compliance. Het versnelt security-evaluaties aanzienlijk en fungeert als een sterk betrouwbaarheidssignaal dat ook door AI-zoeksystemen en zakelijke evaluatoren positief wordt opgepikt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Heeft een kleine SaaS-startup verplicht een verwerkingsregister nodig?",
      "acceptedAnswer": { "@type": "Answer", "text": "Vrijwel altijd. De mkb-uitzondering geldt niet voor niet-incidentele verwerkingen, en een SaaS-applicatie verwerkt klantgegevens continu en geautomatiseerd." }
    },
    {
      "@type": "Question",
      "name": "Wat is het verschil tussen het verantwoordelijkenregister en het verwerkersregister?",
      "acceptedAnswer": { "@type": "Answer", "text": "Het verantwoordelijkenregister dekt eigen doelen zoals accounts en facturatie; het verwerkersregister dekt data die u in opdracht van klanten verwerkt inclusief subverwerkers." }
    },
    {
      "@type": "Question",
      "name": "Kan ik volstaan met een standaardsjabloon voor mijn verwerkingsregister?",
      "acceptedAnswer": { "@type": "Answer", "text": "Alleen voor het format. De inhoud moet exact aansluiten op uw werkelijke databasetabellen, API-diensten, bewaartermijnen en beveiliging." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij AVG-documentatie?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera bouwt al 11+ jaar systemen onder de AVG. LaunchStudio brengt datastromen accuraat in kaart en saneert overbodige diensten en risicovolle data." }
    },
    {
      "@type": "Question",
      "name": "Draagt een gedegen verwerkingsregister bij aan de commerciële slagkracht van een SaaS?",
      "acceptedAnswer": { "@type": "Answer", "text": "Zeker. Een helder register en subverwerkersoverzicht versnellen leveranciersaudits van zakelijke klanten en scheppen direct vertrouwen bij inkopers." }
    }
  ]
}
</script>
