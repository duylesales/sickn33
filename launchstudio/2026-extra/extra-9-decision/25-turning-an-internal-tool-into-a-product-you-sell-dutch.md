---
Titel: "Van Interne Tool Naar Verkoopbaar Product: De Stappen Die U Moet Zetten"
Trefwoorden: interne tool naar SaaS, multi-tenancy row level security, datascheiding per klant, tenant onboarding architectuur, indie hacker tool commercialiseren, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Van Interne Tool Naar Verkoopbaar Product: De Stappen Die U Moet Zetten

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Van Interne Tool Naar Verkoopbaar Product: De Stappen Die U Moet Zetten",
  "description": "Een interne tool die perfect werkt voor één bedrijf mist een complete softwarelaag zodra een tweede partij ervoor betaalt: multi-tenancy, datascheiding, beheer per klant en veilige supporttoegang. Welke laag u moet bouwen en in welke volgorde.",
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
  "datePublished": "2027-01-13",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/van-interne-tool-naar-verkoopbaar-product-de-stappen-die-u-moet-zetten"
  }
}
</script>

Kunt u op dit exacte moment de specifieke SQL-query uitschrijven die onomstotelijk bewijst dat klant B nooit de database-rijen van klant A heeft kunnen inzien? Niet de applicatiecode die data filtert. Maar de database-constraint, de autorisatie-policy of de geautomatiseerde testsuite die een datalek technisch onmogelijk maakt in plaats van louter afwezig?

Luidt uw antwoord: *"Elke query bevat netjes een `WHERE company_id = ?`, en ik programmeer uiterst zorgvuldig"*, dan bezit u in feite een interne tool met extra gebruikers, geen volwaardig softwareproduct. Dat is geenszins een diskwalificatie — interne applicaties vormen het allerbeste startpunt voor een bloeiende SaaS-onderneming. Ze zijn immers gebouwd rondom een werkelijke workflow, door iemand die de finesses van het vak door en door begrijpt. Het punt is simpelweg dat "werkt uitstekend voor ons" en "veilig te verkopen aan derden" van elkaar verschillen door een complete tussenlaag die van binnenuit onzichtbaar is. Elke oprichter die een interne tool commercialiseert, ontdekt die laag in nagenoeg dezelfde volgorde.

## Multi-tenancy is een beslissing in uw datamodel, geen losse kolom

De interne versie van uw tool kende een impliciete tenant: iedereen in de database werkte voor hetzelfde bedrijf, waardoor eigenaarschap van data nooit expliciet gemodelleerd hoefde te worden. De commerciële productversie vereist daarentegen een expliciete tenant-verwijzing op elke tabel die geen algemene stamdata betreft. Het echte werk zit niet in het toevoegen van een kolommetje — het zit in de relationele integriteit en foreign keys eronder. Wanneer `invoice.tenant_id` bestaat maar de onderliggende tabel `invoice_line.invoice_id` geen eigen tenant-binding bezit, kan een gemanipuleerd HTTP-verzoek een factuurregel koppelen aan de factuur van een volstrekt andere organisatie. Uw zorgvuldige `WHERE`-clausule merkt hier niets van, omdat de query één abstractieniveau hoger is gefilterd.

Het architectuurpatroon dat standhoudt: `tenant_id` NOT NULL op elke klantspecifieke tabel, samengestelde foreign keys (composite foreign keys) die de tenant-ID meenemen zodat een onderliggende rij uitsluitend kan verwijzen naar een bovenliggende rij binnen exact dezelfde tenant, en een unieke index die de tenant-ID omvat overal waar u voorheen een globale unique constraint hanteerde. Twee verschillende klanten hebben immers allebei een werknemer met personeelsnummer 001, een intern project genaamd "Kwartaal 1" en een account met het e-mailadres `admin@`. Die laatste valkuil treft u vaak al binnen enkele dagen na het aansluiten van uw tweede klant — en het corrigeren van een globale unieke index op een live productiedatabase met actieve klantdata is een aanzienlijk pijnlijkere operatie dan het vooraf degelijk inrichten.

## Filters in applicatiecode falen geruisloos; de database faalt nooit

Datascheiding op applicatieniveau werkt prima, totdat een vermoeide ontwikkelaar om 23:40 uur 's avonds een nieuw API-eindpunt toevoegt en de tenant-check vergeet. Er bestaat een aanzienlijk robuustere methode die veel minder moeite kost dan menigeen vreest: Postgres Row-Level Security (RLS), waarbij een beleidsregel per tabel de `tenant_id` vergelijkt met een sessievariabele die uw databaseverbinding instelt op basis van de geauthenticeerde gebruiker. Gebruikers van Supabase hebben dit standaard tot hun beschikking en hebben het vaak al half geconfigureerd — RLS geactiveerd op enkele tabellen, vergeten op andere, en voorzien van een `service_role`-sleutel in de frontend die alle beveiliging in één klap omzeilt. Naar schatting bevat zo'n 45% van de door AI gegenereerde code ernstige kwetsbaarheden, en bij gecommercialiseerde interne tools is dit specifieke patroon veruit de meest voorkomende weeffout.

Of u nu kiest voor RLS op databaseniveau of voor een strikte data-toegangslaag waar geen enkele query omheen kan: schrijf de test die bijna niemand schrijft. Een geautomatiseerde testsuite die inlogt als huurder B en gericht probeert een bekende set bronnen van huurder A op ID op te vragen, te muteren en te verwijderen — waarbij voor élk verzoek een HTTP 404 (niet gevonden) wordt verwacht. Het kost twintig minuten om te programmeren, draait voor altijd mee in uw CI/CD-pijplijn en is het enige harde bewijsstuk waarmee u beveiligingsvragen van zakelijke inkopers met concrete feiten kunt beantwoorden in plaats van met vage beloftes.

## De hardgecodeerde aannames die u zelf niet meer opmerkt

Interne applicaties ademen het bedrijf waarvoor ze zijn gemaakt. Het btw-tarief staat vast op 21% omdat dat het Nederlandse standaardtarief is. De werkweek begint op maandagochtend. Goedkeuringen gaan direct naar de financieel directeur, want er is maar één financieel directeur. Factuurnummers beginnen standaard met de initialen van uw eigen onderneming. Kantooruren zijn 08:00 tot 17:30 uur. Uw eigen bedrijfslogo staat hardgecodeerd in de header. De valuta is euro. En er draait een Slack-webhook die notificaties stuurt naar een intern kanaal in een werkruimte waar externe klanten niets te zoeken hebben.

Elk van deze punten vergt hooguit vijf minuten om aan te passen, maar er zitten er doorgaans minstens veertig in een bestaande codebase. De professionaliseringsslag bestaat uit het vroegtijdig introduceren van een configuratietabel voor tenant-instellingen (`tenant_settings`), waar al deze variabelen doorheen worden geleid — zelfs wanneer de standaardwaarde voor iedereen voorlopig gelijk is. Doet u dit niet, dan ontdekt u deze aannames één voor één via klachten van betalende klanten. Pas hetzelfde principe toe op bedrijfsregels die feitelijk beleidskeuzes zijn: goedkeuringslimieten, bewaartermijnen of verplichte velden. Wanneer uw tweede klant een uitzondering vraagt die uw eerste klant niet wil, lost u dat op via configuratie in de database, niet via een lelijke if-statement in de code die vernoemd is naar een specifieke klant.

## Beheerprocessen die u voor één organisatie nooit nodig had

Voor een interne tool betekent "back-up" een dagelijkse export van de complete database, en dat volstaat prima. Voor een commercieel product worden beheerprocessen plotseling per individuele klant gevraagd: herstel de data van één specifieke huurder nadat een medewerker op vrijdagmiddag per ongeluk een project heeft gewist; exporteer alle data van een klant omdat hij daarom vraagt of overstapt; verwijder alle gegevens van een klant binnen een vastgestelde termijn omdat de AVG/GDPR dit vereist en u dit contractueel heeft toegezegd.

Geen van deze taken laat zich soepel uitvoeren op basis van een monolithische database-dump. Wat wél werkt, is een gedocumenteerde set beheerfuncties per tenant: export naar JSON of CSV per entiteit, een veilige 'soft-delete' periode vóór definitieve verwijdering en een beproefde herstelprocedure. Zorg er bovendien voor dat u uw hersteltijden kent: hoeveel data mag u maximaal verliezen (RPO) en hoe snel moet het systeem weer up-and-running zijn (RTO)? U heeft geen enterprise-infrastructuur nodig om die vragen te beantwoorden, maar u moet de procedure wél minimaal één keer in de praktijk hebben getoetst. De eerste keer dat u een herstelprocedure uitvoert, mag nooit tijdens een acute crisissituatie zijn.

## Klantenservice zonder een almachtig 'god-mode' beheerdersaccount

Elke software-oprichter moet vroeg of laat meekijken met wat een specifieke klant ziet wanneer die een bug meldt. De verleidelijke, snelle uitweg is een almachtig beheerdersaccount dat ongehinderd alle data in de database kan inzien en bewerken. Dat is tevens de route die carrières breekt zodra een beheerderslaptop wordt gestolen of wanneer een kritische klant vraagt wie er binnen uw organisatie toegang heeft tot vertrouwelijke dossiers.

Het acceptabele patroon is impersonatie (inloggen als de klant) op basis van expliciete toestemming en met een sluitend auditspoor: een supportsessie waarin u tijdelijk de identiteit van een specifieke gebruiker binnen een specifieke organisatie aanneemt, die strikt in tijd is begrensd, exact registreert wie de sessie startte en om welke reden, en zichtbaar is in het logboek van de beheerder van die klant. Koppel dit aan een intern administratiepaneel dat uitsluitend metadata toont — abonnement, dataverbruik, actieve modules, datum van laatste login — zonder standaard de inhoudelijke klantgegevens te tonen. Dit maakt het verschil tussen "onze medewerkers kunnen bij uw data indien nodig" als een verontrustende zin, en als een gecontroleerd, contractueel vastgelegd proces.

## 'Noisy neighbours' zijn voortaan uw probleem

Medewerkers van één bedrijf gedragen zich online doorgaans hoffelijk omdat ze elkaar bij de koffieautomaat tegenkomen. Gebruikers van zes verschillende concurrerende bedrijven doen dat niet. De CSV-exportfunctie van uw interne tool die alle data in één keer in het servergeheugen laadt, werkte vlekkeloos bij 4.000 regels, maar trekt de complete server onderuit bij 900.000 regels. De nachtelijke synchronisatietaak die alle organisaties achter elkaar verwerkt, duurt inmiddels vier uur en loopt door tot ver na aanvang van de kantooruren. En het rapport dat een manager tweemaal daags opvraagt, wordt op de eerste dag van de maand om 08:55 uur door zes verschillende organisaties tegelijkertijd gegenereerd.

Praktische maatregelen, gerangschikt op toegevoegde waarde: verplaats zware exports en rapportages naar asynchrone achtergrondtaken met strikte gelijktijdigheidslimieten per organisatie; stream omvangrijke bestanden rechtstreeks naar de browser in plaats van ze in het geheugen op te bouwen; stel rate-limiting per klant in op rekenintensieve eindpunten; hanteer een harde time-out op elke databasequery; en spreid geplande achtergrondtaken per tenant in plaats van één grote sequentiële lus te draaien. Dit is het breekpunt waarop een door een indie hacker gebouwd product transformeert in een betrouwbaar softwareplatform, of verzandt in een jaar vol ad-hoc brandjes blussen.

## De eerste serieuze zakelijke klant stuurt een security-vragenlijst

Op het moment dat u uw software verkoopt aan een onderneming die groter is dan uw eigen bedrijf, stuurt de afdeling inkoop of security u een Excel-vragenlijst. Daarin staan vragen over waar de data fysiek wordt opgeslagen, wie er toegang toe heeft, of u tweefactorauthenticatie (2FA) en Single Sign-On (SSO) ondersteunt, hoe lang back-ups bewaard blijven, wie uw subverwerkers zijn, hoe u datalekken meldt en of u een auditlog kunt overleggen van alle gebruikershandelingen.

Voor een eerste B2B-overeenkomst heeft u in het MKB meestal geen dure ISO 27001- of SOC 2-certificering nodig. U heeft wél eerlijke, controleerbare antwoorden nodig. Dat betekent dat de onderliggende faciliteiten daadwerkelijk moeten functioneren: een onwijzigbare auditlog-tabel met vermelding van actor, handeling, doelwit, tijdstempel en IP-adres voor alle cruciale acties; 2FA beschikbaar voor beheerdersaccounts; een up-to-date overzicht van subverwerkers; een gedefinieerde Europese hostingregio; en een datatermijn die u in de praktijk waarmaakt. Het tijdig inrichten van de auditlog levert het hoogste rendement op: u kunt een auditlog immers nooit met terugwerkende kracht vullen. Gebeurtenissen die u vandaag niet registreert, zijn voorgoed verloren.

## De juiste volgorde en wat het kost

De volgorde van implementatie is belangrijker dan direct alles willen doen. Stap één: multi-tenancy in het datamodel met door de database afgedwongen isolatie en de hostile-access testsuite — al het overige is waardeloos als dit fundament wankelt. Stap twee: de tabel met tenant-instellingen en het verwijderen van hardgecodeerde bedrijfsspecifieke waarden. Stap drie: de auditlog, vanwege het feit dat historie niet achteraf gecreëerd kan worden. Stap vier: export-, verwijder- en herstelfuncties per organisatie. Stap vijf: veilige impersonatie met logging voor support. Stap zes: achtergrondtaken en limieten per klant tegen overbelasting. Facturatie, geautomatiseerde zelfbediening bij registratie en uitgebreide dashboards kunnen daarna volgen; vroege klanten accepteren een handmatige factuur per mail immers veel langer dan het risico dat zij data van een concurrent te zien krijgen.

Qua investering valt het transformeren van een interne tool naar een volwaardig commercieel SaaS-product op de [LaunchStudio prijscalculator](https://launchstudio.eu/nl/#calculator) tussen de €1.200 en €3.000 (Tool-tarief) of tussen de €2.833 en €7.167 (SaaS-tarief), afhankelijk van de mate waarin er al rekening is gehouden met multi-tenancy en of geïntegreerde betalingen gewenst zijn. Dit vertaalt zich in één tot drie weken gefocust werk, in plaats van het volledige kwartaal dat een complete herbouw zou vergen. LaunchStudio maakt enterprise-grade engineering van Manifera toegankelijk voor solo-oprichters: dezelfde architectuurpatronen die worden ingezet voor grote corporate systemen, toegepast op uw bestaande codebase, waarbij uw vertrouwde frontend onaangeroerd blijft en de intellectuele eigendom volledig van u blijft.

Voor een technische oprichter is het geruststellende nieuws dat niets hiervan speculatieve architectuur betreft. Het is een heldere, afgebakende lijst van datamodellen en middleware, waarbij elk afzonderlijk onderdeel zwart-op-wit testbaar is. Het risico schuilt erin dat deze leemtes onzichtbaar blijven zolang u de enige gebruiker bent. [Ga in gesprek met een software-engineer die AI-gegenereerde code doorgrondt](https://launchstudio.eu/nl/#contact) vóórdat uw tweede klant u op een datalek wijst — of bekijk [de technologieselectie van onze engineers](https://www.manifera.com/about-us/manifera-technologies/) om te zien in welke deskundige handen u uw codebase toevertrouwt.

## Echt voorbeeld

### Een indie hacker in actie: de interne tool die verkocht werd vóórdat het een product was

Ruben de Wit ontwikkelde Rittenboek gedurende twee winters in Cursor — een applicatie voor rittenregistratie en chauffeursuren voor het transportbedrijf van zijn familie in Zwolle, ter vervanging van een overvol Excel-bestand dat onbeheersbaar was geworden. Een operationeel manager van een concurrerend transportbedrijf zag de software in werking, vroeg om toegang tegen betaling, en binnen vier maanden maakten vijf transportbedrijven dagelijks gebruik van Rittenboek. Ruben voegde simpelweg een `company_id`-kolom toe aan de hoofdtabellen, filterde zijn SQL-queries op deze variabele en zette de software live.

Het probleem openbaarde zich toen een vrachtwagenchauffeur overstapte naar een ander aangesloten transportbedrijf en verbaasd meldde dat hij in een rapportage nog altijd de ritten van zijn vorige werkgever kon inzien. Er was geen sprake van een externe hack: een van de rapportages maakte een database-join via een sub-tabel die zelf geen `company_id` bevatte. Het filter werkte prima op het hoogste niveau, maar de onderliggende join trok alle gekoppelde data ongefilterd mee naar buiten. De daaropvolgende code-audit bracht nog drie vergelijkbare datalekken aan het licht, plus een globale unieke index op chauffeursnummer die de registratie van een nieuw transportbedrijf al had geblokkeerd, en een actieve Slack-webhook die rittennotificaties nog altijd naar het interne privékanaal van zijn familiebedrijf stuurde. De aanpassingen omvatten composite foreign keys met `company_id` op elke onderliggende tabel, Postgres Row-Level Security met policies op alle bedrijfstabellen, een cross-tenant testsuite in CI, een configuratietabel die elf hardgecodeerde parameters verving, en een gestructureerde auditlog met veilige support-impersonatie.

**Het resultaat:** Het datalek werd definitief gedicht en dit werd zwart-op-wit bewezen door een testsuite die direct aan de IT-afdeling van potentiële klanten getoond kon worden. De doorlooptijd voor het aansluiten van een nieuw transportbedrijf daalde van twee dagen handmatig configureren naar minder dan een uur. En Rittenboek doorstond zijn eerste formele security-audit van een grote logistieke partij — een vragenlijst van veertig pagina's — zonder dat Ruben bij ook maar één vraag hoefde te gokken.

> *"Ik had artikelen over multi-tenancy gelezen en ging ervan uit dat ik het geregeld had omdat ik een company_id-kolom had aangemaakt. In werkelijkheid had ik niet meer dan een naamgevingsconventie. De database zelf dwong helemaal niets af totdat we het structureel gingen inrichten."*  
> — **Ruben de Wit, Oprichter, Rittenboek (Zwolle)**

**Kosten & Doorlooptijd:** €4.100 vaste prijs — multi-tenancy datamodel, row-level security, isolatietests, auditlog en configuratie-extractie — opgeleverd binnen 11 werkdagen.

---

## Veelgestelde Vragen

### Is een tenant_id kolom voldoende om een interne tool multi-tenant te maken?

Nee. Onderliggende tabellen zonder eigen tenant-koppeling kunnen via joins en directe ID-referenties worden uitgelezen, zelfs wanneer de hoofdquery netjes is gefilterd. U heeft samengestelde foreign keys nodig, unieke indexen per tenant in plaats van globaal, en bij voorkeur een afdwingingsmechanisme op databaseniveau zoals Row-Level Security.

### Moet ik Row-Level Security gebruiken of alles filteren in applicatiecode?

Row-Level Security verdient de voorkeur omdat het standaard afsluit ('fails closed') wanneer iemand een query toevoegt en een filter vergeet. Applicatiefilters falen juist open ('fail open'). Blijft u in applicatiecode werken, leid dan elke database-opvraag verplicht door één centrale data-toegangslaag en bouw geautomatiseerde tests die met opzet data van andere huurders proberen op te vragen.

### Moet ik voor elke klant een aparte database inrichten?

In dit stadium vrijwel nooit. Eén gedeelde database met strikt afgedwongen rij-niveau isolatie is de ideale standaard voor MKB B2B SaaS. Een aparte database per klant vermenigvuldigt uw beheer-, migratie- en back-upinspanningen enorm. Bewaar aparte databases uitsluitend voor grote enterprise-klanten met contractuele eisen rondom dataseparatie, en reken daar een passend premiumtarief voor.

### Wat moet ik bouwen vóórdat mijn eerste zakelijke klant erom vraagt?

Een auditlog. In tegenstelling tot andere functionaliteiten kan een auditlog immers nooit met terugwerkende kracht worden gevuld; historische handelingen die u niet heeft gelogd, zijn definitief weg. Richt daarnaast tweefactorauthenticatie (2FA) in voor beheerders, documenteer uw subverwerkers en zorg voor een geteste export- en verwijderprocedure per tenant.

### Hoe kan ik veilig meekijken met een klant die een probleem meldt?

Gebruik tijdgebonden impersonatie die gekoppeld is aan een specifieke gebruiker binnen die organisatie, waarbij exact wordt vastgelegd wie de sessie startte en waarom, en waarbij dit zichtbaar is voor de beheerders van die klant. Een permanent beheerdersaccount met ongehinderde toegang tot alle data is eenvoudiger te bouwen, maar juridisch en contractueel niet te verdedigen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is een tenant_id kolom voldoende om een interne tool multi-tenant te maken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Onderliggende tabellen zonder eigen tenancy kunnen via joins lekken. U heeft samengestelde foreign keys nodig, per-tenant unieke indexen en afdwinging via Row-Level Security."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik Row-Level Security gebruiken of alles filteren in applicatiecode?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "RLS verdient de voorkeur omdat het 'fails closed' bij vergeten filters. In applicatiecode moet u alle queries dwingen via één centrale datalaag met cross-tenant tests in CI."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik voor elke klant een aparte database inrichten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zelden bij de start. Eén gedeelde database met RLS is de beproefde standaard. Aparte databases per klant vermenigvuldigen beheer en migraties; bewaar dit voor zware enterprise-eisen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet ik bouwen vóórdat mijn eerste zakelijke klant erom vraagt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een auditlog, omdat historie niet achteraf hersteld kan worden. Daarna 2FA voor beheerders, een subverwerkersoverzicht en geteste export- en verwijderfuncties per tenant."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe kan ik veilig meekijken met een klant die een probleem meldt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Gebruik tijdgebonden impersonatie met consent en een auditspoor dat zichtbaar is voor de klant. Vermijd een permanente 'god-mode' login die ongehinderd alle data kan inzien."
      }
    }
  ]
}
</script>
