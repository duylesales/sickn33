---
Titel: "Lovable Supabase Standaardwaarden: Wat U Krijgt en Wat Er Ontbreekt"
Trefwoorden: lovable supabase, Supabase, supabase standaardinstellingen row level security, lovable database inrichten, AI app backend risico's, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Lovable Supabase Standaardwaarden: Wat U Krijgt en Wat Er Ontbreekt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase Standaardwaarden: Wat U Krijgt en Wat Er Ontbreekt",
  "description": "Een overzicht op oprichtersniveau van wat u daadwerkelijk krijgt wanneer Lovable uw app koppelt aan Supabase: de database, de automatisch gegenereerde API, authenticatie en opslag - en de vier standaardinstellingen die bepalen of uw data beschermd is of voor iedereen publiek leesbaar.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-05",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-supabase-default-project-what-you-get" }
}
</script>

Weet u wat uw applicatie eigenlijk mag doen met uw database? Niet wat hij nu doet - maar wat hij *mag* doen, door iedereen die beschikt over de sleutel die standaard in uw website zit ingebakken?

De meeste oprichters die met Lovable hebben gebouwd, kunnen die vraag niet beantwoorden, en dat is geen gebrek aan intelligentie. Het komt doordat het koppelen van Lovable aan Supabase aanvoelt als het aansluiten van een huishoudelijk apparaat: u klikt op een knop, het werkt direct, data verschijnt netjes in tabellen en de app begint gegevens te onthouden. Niets in die gebruikservaring suggereert dat u zojuist een reeks fundamentele beveiligingsbeslissingen heeft genomen. Maar dat heeft u wel gedaan - vier stuks - en ze vormen het verschil tussen een database die alleen door uw app kan worden uitgelezen en een database die door iedereen met toegang tot uw gepubliceerde website kan worden bevraagd.

Dit is een heldere rondleiding langs wat die combinatie u direct uit de doos oplevert, en wat er bewust wordt overgelaten aan een mens om te beslissen.

## Wat U Daadwerkelijk Krijgt, Zonder Meerprijs

Supabase is geen speelgoed, en het is goed om te beseffen hoeveel volwaardige infrastructuur direct actief wordt zodra de koppeling is gelegd.

**Een beheerde PostgreSQL-database.** Geen lichtgewicht documentenarchief, maar een complete relationele database met constraints, indexen, transacties en de volledige SQL-woordenschat. Dit is dezelfde database-engine waar banken op draaien.

**Een automatisch gegenereerde API.** Elke tabel die u aanmaakt, krijgt ogenblikkelijk endpoints voor het lezen, invoegen, bijwerken en verwijderen van rijen. Uw Lovable-frontend communiceert met die endpoints. Niemand hoefde die API te programmeren; hij bestaat omdat de tabellen bestaan.

**Authenticatie.** Registratie, inloggen, wachtwoordherstel, sessiebeheer en optionele social logins. Dit vanaf nul opbouwen kostte vroeger weken, en het is een van de voornaamste redenen waarom AI-gebouwde apps zo verbluffend snel een werkende demo bereiken.

**Bestandsopslag (file storage).** Buckets voor afbeeldingen, documenten en uploads, voorzien van hun eigen toegangsregels.

**Edge functions.** Een omgeving om server-side code uit te voeren - wat, zoals elk serieus beveiligingsgesprek zal benadrukken, precies de plek is waar uw geheime API-sleutels thuishoren.

Dat is een buitengewoon krachtige backend. Het hiaat zit hem dan ook niet in de technische capaciteit. Het hiaat zit in de configuratie.

## Standaardinstelling 1: De Automatische API Is Standaard Publiek

Dit is het mechanisme dat mensen het meest verbaast. Omdat Supabase automatisch een API genereert op basis van uw databasetabellen, en omdat uw Lovable-frontend die API moet kunnen aanroepen vanuit de browser van de gebruiker, reist er een sleutel mee in uw applicatie naar iedere bezoeker.

Die sleutel is bedoeld om publiek te zijn. Hij identificeert uw project, niet uw gebruikersrechten. Wat bepaalt of een bepaald verzoek is toegestaan, is een afzonderlijk systeem - Row Level Security (RLS) - en dat systeem is precies wat de meeste AI-gebouwde apps nooit configureren.

Simpel gezegd: de voordeur van uw database staat standaard open op het openbare internet, en het slot is een functie die u zelf handmatig moet inschakelen en inrichten. Is dat niet geconfigureerd? Dan kan iedereen met de publieke sleutel uit uw website de complete tabel uitlezen.

## Standaardinstelling 2: Row Level Security Moet Worden Ingeschakeld Én Geschreven

Row Level Security is een Postgres-functie die per afzonderlijke rij bepaalt of degene die het verzoek doet die rij mag inzien of wijzigen. In een correct geconfigureerde app formuleert dit regels zoals "een gebruiker mag uitsluitend zijn eigen reserveringen inzien en die van niemand anders" of "alleen medewerkers van deze praktijk mogen het dossier van deze patiënt bekijken."

Twee valkuilen zetten oprichters hierbij op het verkeerde been:

**Het staat niet standaard aan voor elke tabel.** Het dashboard van Supabase geeft waarschuwingen om het in te schakelen, maar tabellen die zijn aangemaakt via automatische migraties, SQL-snippets of AI-gestuurde installatiestappen eindigen regelmatig zonder RLS. Een tabel zonder Row Level Security, ontsloten via de automatische API, is leesbaar voor iedereen die over uw publieke sleutel beschikt - en dat is iedereen die uw website laadt.

**Inschakelen is niet hetzelfde als beveiligen.** RLS aanzetten zonder beleidsregels (policies) blokkeert simpelweg alles, waardoor de applicatie direct vastloopt. De logische volgende reflex, vooral wanneer een AI-tool wordt gevraagd om "de databasefout op te lossen", is het toevoegen van een uiterst permissieve policy die iedere ingelogde gebruiker toestaat alles te doen. Daarmee verdwijnt de foutmelding, maar u blijft achter met een app waarin elke geregistreerde gebruiker de gegevens van alle andere gebruikers kan inzien door simpelweg één ID in het netwerkverzoek aan te passen.

De juiste aanpak bestaat uit een handvol beknopte, specifieke policies per tabel, doelbewust geschreven en vervolgens getest door in te loggen als Gebruiker A en actief te proberen de rijen van Gebruiker B op te vragen.

## Standaardinstelling 3: Uw Serverregio Is Voor U Gekozen

Een Supabase-project draait in een geografische regio die wordt geselecteerd bij het aanmaken van het project. Voor oprichters in Nederland en de Europese Unie telt dit dubbel: zakelijke klanten in gereguleerde sectoren eisen tijdens inkooptrajecten nadrukkelijk hosting binnen de EU, en dataopslag op een willekeurige buitenlandse locatie is lastig uit te leggen tijdens een privacy-audit.

De standaardregio bevindt zich dikwijls buiten Europa (zoals in de VS), en niets in het gedrag van uw app waarschuwt u daarvoor. Dit achteraf aanpassen betekent dat u een nieuw project in de juiste regio moet aanmaken en alle data moet migreren - exporteren, herstellen, verifiëren en live overzetten - in plaats van het omzetten van een vinkje. Het controleren kost u vandaag één minuut, terwijl een latere migratie een serieus project vormt.

## Standaardinstelling 4: Back-ups Hangen Af van Uw Abonnement, Niet van Uw Intenties

Uw database bevat het enige deel van het product dat u niet opnieuw kunt genereren met een prompt. De frequentie en bewaartermijn van back-ups hangen af van het abonnement dat u heeft afgesloten en de opties die u handmatig heeft geactiveerd.

Twee vragen moeten vóór de lancering hoe dan ook worden beantwoord: hoe ver kunt u data herstellen, en heeft iemand ooit daadwerkelijk een restore uitgevoerd? Een ongeteste back-up is een geloofsovertuiging, geen veiligheidsgarantie. Door eenmalig een herstelprocedure uit te voeren in een tijdelijk testproject, terwijl er niets in brand staat, verandert u die aanname in een bewezen zekerheid.

## Wat Lovable Toevoegt - en Wat Het Niet Kán Weten

Lovable is uitstekend in de technische koppeling: tabellen aanmaken die aansluiten op de ontworpen schermen, queries genereren en het dataverkeer tussen interface en database stroomlijnen. Wat het echter niet kan, is zakelijke en juridische afwegingen maken over uw onderneming.

Lovable kan niet weten dat de kolom `salaris` in uw personeelstool veel gevoeliger is dan de kolom `functietitel` ernaast. Het kan niet weten dat uw platform twee gebruikersgroepen kent die elkaars dossiers onder geen beding mogen zien. Het kan niet weten dat uw software uiteindelijk wordt verkocht aan een Nederlandse gemeente waarvan de inkoopvoorwaarden strikt voorschrijven waar persoonsgegevens worden verwerkt. Dat zijn productbeslissingen vermomd als technische instellingen, en precies daar is menselijke expertise onvervangbaar.

Dit is geen kritiek op het gereedschap. Het is de reden waarom naar schatting 80% van de door AI gebouwde prototypes nooit de productiefase haalt: de laatste stap bestaat uit beslissingen die geen enkele AI-prompt uit zichzelf kan nemen.

## Een Snelle Zelfcontrole voor Vanmiddag

U hoeft geen doorgewinterde ontwikkelaar te zijn om heldere antwoorden te krijgen op deze vragen:

- Open uw Supabase-project en bekijk de tabeloverzichten. Is Row Level Security ingeschakeld voor élke tabel?
- Lees voor elke tabel met policies de regels hardop voor in gewone mensentaal. Staat er feitelijk: "elke ingelogde gebruiker mag dit doen"?
- In welke fysieke serverregio bevindt het project zich?
- Hoe is het back-upbeleid geregeld, en wanneer is er voor het laatst een hersteltest uitgevoerd?
- Staat er ergens in uw frontend-code een andere sleutel dan de publieke project-sleutel?
- Als een onbekende beschikt over uw publieke sleutel en een vrije middag, welke tabellen kan diegene dan direct leegtrekken?

Die laatste vraag is de belangrijkste. Kunt u die niet met een gerust hart beantwoorden, dan is het verstandig om een deskundige blik te laten werpen voordat u echte klantdata accepteert.

## De Configuratie Herstellen Zonder Herbouw

Niets van dit alles vereist dat u weggooit wat u met Lovable heeft gerealiseerd. Het corrigeren van een Supabase-inrichting is overzichtelijk, afgebakend werk: Row Level Security tabel voor tabel inschakelen, specifieke RLS-policies schrijven, bevoorrechte sleutels verhuizen naar edge functions, de regio indien nodig corrigeren en het resultaat testen door als ingelogde gebruiker actief te proberen ongeautoriseerde data op te halen.

Dat is precies de backend-helft van LaunchStudio's [Launch Ready-pakket](https://launchstudio.eu/nl/#packages) - uitgevoerd zonder de frontend die u in Lovable heeft gemaakt aan te tasten, met documentatie en code die volledig leesbaar blijft voor AI, zodat u achteraf soepel kunt blijven doorontwikkelen. De software-engineers die dit uitvoeren zijn afkomstig van Manifera, dat al elf jaar systemen bouwt en beveiligt voor toonaangevende opdrachtgevers als Vodafone en TNO.

Wilt u vooraf exact weten waar u staat? [Deel uw project met ons](https://launchstudio.eu/nl/#contact) en u ontvangt een concreet overzicht van wat kwetsbaar is en wat al solide in elkaar zit.

## Opslag en Authenticatie Hebben Hun Eigen Toegangsregels

Row Level Security krijgt vaak alle aandacht, maar het beschermt uitsluitend uw databasetabellen. Twee andere onderdelen binnen Supabase hanteren afzonderlijke toegangssystemen waarvan oprichters geregeld ten onrechte aannemen dat ze onder dezelfde paraplu vallen:

**Bestandsopslag (storage) wordt apart beheerd.** Storage buckets zijn publiek of privé. Een publieke bucket betekent dat iedereen die de link naar een bestand heeft, dit direct kan downloaden - zonder inloggen, zonder autorisatie en zonder verloopdatum. AI-tools kiezen tijdens het bouwen doorgaans voor wat uploads het snelst werkend krijgt: een publieke bucket. Slaat uw app identiteitsbewijzen, facturen, medische dossiers of privacygevoelige foto's op? Dan vereist de bucket eigen policies die bestanden strikt koppelen aan het eigenaarsaccount, en moeten gedeelde links automatisch verlopen via signed URL's.

**Authenticatie heeft standaardinstellingen die uw beveiligingsniveau bepalen.** Moeten nieuwe accounts hun e-mailadres verplicht verifiëren? Hoe lang blijft een sessie geldig? Verloopt een wachtwoordreset na eenmalig gebruik? Mag iedereen zich zomaar registreren? Dit zijn cruciale instellingen, en de keuzes die tijdens het bouwen handig waren, zijn zelden de keuzes die u in productie wilt handhaven.

**De gebruikerstabel is niet hetzelfde als uw applicatietabellen.** Supabase beheert inloggegevens in een eigen afgeschermd schema (`auth.users`), terwijl profielinformatie meestal in een zelfgemaakte tabel (`public.profiles`) leeft. Oprichters schrijven regelmatig beleidsregels voor de ene tabel en vergeten de koppeltabel, wat resulteert in een situatie waarin profielen beschermd zijn maar koppelgegevens openlijk op straat liggen.

Loop alle drie de onderdelen na vóór de livegang: inspecteer uw bucket-toegangsrechten, controleer de authenticatie-instellingen en verifieer dat elke tabel met gebruikersdata daadwerkelijk is voorzien van een dekkende policy.

## Echt voorbeeld

### Een Bijlesplatform Waar Elke Docent Elk Contract Kon Inzien

Joris Nieuwenhuis bouwde met Lovable in drie weken LesMatch: een platform dat privédocenten koppelt aan gezinnen in de regio Eindhoven. Docenten maakten profielen aan, ouders boekten sessies, en het systeem bewaarde contactgegevens, uurtarieven en lesnotities.

Alles functioneerde naar behoren. Waar niemand echter naar had gekeken, was dat bij vier van de elf databasetabellen Row Level Security volledig was uitgeschakeld - waaronder de tabel met getekende lesovereenkomsten - en dat bij twee andere tabellen een policy actief was die iedere ingelogde gebruiker toestond alle rijen te selecteren. Aangezien iedereen zich binnen een minuut kon registreren als docent, kon iedereen zich aanmelden en vervolgens de woonadressen van alle gezinnen, de uurtarieven van alle concurrerende docenten en alle vertrouwelijke lesnotities uitlezen.

De audit en herstelwerkzaamheden namen zes werkdagen in beslag: Row Level Security geactiveerd op alle tabellen, policies herschreven zodat docenten uitsluitend hun eigen boekingen zien en ouders alleen de sessies van hun eigen kinderen, lesnotities ondergebracht achter een striktere autorisatielaag, het project gemigreerd van een Amerikaanse regio naar een datacenter binnen de EU met een geverifieerde hersteltest, en geautomatiseerde integratietests ingericht die met twee verschillende accounts inloggen en verifiëren dat geen van beide data van de ander kan inzien.

**Resultaat:** LesMatch doorstond drie weken later glansrijk een strenge gegevensbeschermingsaudit van een scholengroep in Eindhoven - een harde voorwaarde voor het sluiten van een strategisch contract dat een veelvoud waard was van de kosten van het hardening-traject.

> *"Ik dacht oprecht dat 'de database is verbonden' hetzelfde betekende als 'de database is beveiligd'. Niemand vertelt je dat dat twee totaal verschillende dingen zijn."*
> - **Joris Nieuwenhuis, Oprichter, LesMatch (Eindhoven)**

**Kosten & Doorlooptijd:** €2.750 (Launch Ready-pakket: autorisatiepolicies, regiomigratie en verificatietests) - voltooid in 6 werkdagen.

---

## Veelgestelde vragen

### Hoort de Supabase-sleutel in mijn frontend zichtbaar te zijn?

De publieke project-sleutel (anon key) wel - deze is ontworpen om mee te reizen met uw webapplicatie en het project te identificeren. Uw data wordt immers beschermd door Row Level Security, niet door het geheimhouden van die sleutel. Er bestaat echter ook een service role key met volledige beheerdersrechten die absoluut nooit in de frontend mag voorkomen; het verwarren van die twee is een veelgemaakte en ernstige fout.

### Maakt het inschakelen van Row Level Security mijn app kapot?

Dat kan direct gebeuren, omdat RLS aanzetten zonder policies standaard alle datatoegang blokkeert. Dat is volkomen normaal. De juiste procedure is om RLS in te schakelen en vervolgens gerichte policies per tabel op te stellen die worden getest met een echt ingelogd account, in plaats van een te ruime policy toe te voegen om foutmeldingen het zwijgen op te leggen.

### Hoe weet ik welke van mijn databasetabellen openbaar toegankelijk zijn?

Controleer in uw Supabase-dashboard tabel voor tabel of Row Level Security is ingeschakeld en wat de beleidsregels letterlijk inhouden. Elke tabel zonder actieve RLS die bereikbaar is via de automatische API moet worden beschouwd als publiek leesbaar voor iedereen met uw anon key.

### Kan ik mijn Supabase-serverregio na de lancering nog wijzigen?

Niet met een simpele schakelaar in de instellingen. Het vereist het opzetten van een nieuw project in de gewenste regio, het migreren van de gegevens en het omzetten van de verbinding. Bij een draaiende applicatie met actieve gebruikers is dat een precisieklus, terwijl het vóór de livegang een kosteloze keuze is.

### Moet ik weggaan bij Supabase om echt productierijp te zijn?

Zeker niet. Supabase is enterprise-grade infrastructuur; het probleem ligt vrijwel nooit bij het platform zelf, maar vrijwel altijd bij de configuratie en policies erbovenop. Het meeste lanceerwerk richt zich op het beveiligen en fijnmazig inrichten van wat er al staat.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoort de Supabase-sleutel in mijn frontend zichtbaar te zijn?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De publieke anon key wel; deze identificeert het project. Data wordt beschermd door Row Level Security, niet door sleutelgeheimhouding. De krachtige service role key mag echter nooit in frontend-code staan."
      }
    },
    {
      "@type": "Question",
      "name": "Maakt het inschakelen van Row Level Security mijn app kapot?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het kan direct gebeuren omdat RLS zonder policies alle toegang afsluit. De juiste methode is inschakelen en direct specifieke regels per tabel schrijven en testen met een echt gebruikersaccount."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe weet ik welke van mijn databasetabellen openbaar toegankelijk zijn?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Controleer in het Supabase-dashboard of RLS aanstaat en wat de regels betekenen. Tabellen zonder RLS via de openbare API zijn door iedereen met de anon key direct uit te lezen."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik mijn Supabase-serverregio na de lancering nog wijzigen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niet via een simpele instelling; het vereist een nieuw project, datamigratie en het overzetten van endpoints. Vóór de lancering is het kiezen van een EU-regio echter kosteloos."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik weggaan bij Supabase om echt productierijp te zijn?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Supabase is volwaardige productie-infrastructuur. Het risico schuilt in ontbrekende RLS-regels en verkeerde configuratie, niet in het platform zelf."
      }
    }
  ]
}
</script>
