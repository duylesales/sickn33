---
Titel: "Lovable Supabase: Multi-Tenancy Zonder Datalekken"
Trefwoorden: lovable supabase, multi-tenancy, supabase security, tenant isolation, ai app security, LaunchStudio, Manifera
Koperfase: Decision
Doelgroep: SaaS Scale-Up
---

# Lovable Supabase: Multi-Tenancy Zonder Datalekken

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Multi-Tenancy Zonder Datalekken",
  "description": "Zodra uw klanten bedrijven zijn in plaats van individuen, heeft elke tabel een tenant nodig. Hoe data-isolatie technisch wordt afgedwongen, waar het in de praktijk lekt, en waarom het achteraf inbouwen tien keer meer kost dan direct goed opzetten.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-14",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-supabase-multi-tenancy-without-leaking-data" }
}
</script>

Eén fundamentele vraag scheidt een handig persoonlijk tooltje van een volwaardig B2B-softwareproduct: is uw klant één individu, of een bedrijf waarin meerdere collega's samenwerken?

Vrijwel elke beginnende oprichter antwoordt in eerste instantie "één persoon", want dat is wat er met Lovable of Bolt is gebouwd en dat waren de eerste testers. En vrijwel elke oprichter die verkoopt aan Nederlandse mkb-bedrijven krijgt binnen zes maanden dezelfde vraag van zijn eerste betalende klant: *"Kan mijn collega ook toegang krijgen tot ons account?"* Het antwoord op die vraag bepaalt of de volgende stap een middag configuratiewerk is of twee weken acute crisisontwikkeling.

Multi-tenancy is het architectuurpatroon dat het antwoord eenvoudig maakt. Het is tevens de architectuur waarbij een programmeerfout niet leidt tot een gewone bug, maar direct tot een ernstig datalek — omdat de data van de ene klant plotseling op het beeldscherm van een concurrent verschijnt.

## Wat Een Tenant Concreet Inhoudt

Een *tenant* (huurder) is de harde grens van wie welke data mag inzien. Voor de meeste zakelijke SaaS-producten is een tenant een organisatie: een bedrijf, een praktijk, een vereniging of een afdeling.

Hier vloeien drie architectuurregels uit voort die stelselmatig ontbreken in met AI gegenereerde codebases:

**Elke rij met bedrijfsdata behoort toe aan een tenant.** Niet aan een individuele gebruiker, maar aan de organisatie. Een dossier dat is aangemaakt door een medewerker die later uit dienst treedt, moet binnen het bedrijf bewaard blijven.

**Elke gebruiker behoort tot één of meerdere tenants, met een specifieke rol per tenant.** Een boekhouder die voor drie verschillende mkb-klanten werkt, heeft één gebruikersaccount met drie lidmaatschappen, niet drie losse accounts met verschillende wachtwoorden.

**Elke databasequery wordt gefilterd op tenant-ID,** en die filtering wordt onwrikbaar afgedwongen in de database zelf (via Row Level Security) in plaats van dat ontwikkelaars moeten onthouden om handmatig een `WHERE organization_id = ...` clausule toe te voegen.

De standaard aanname van AI-tools — dat een record simpelweg eigendom is van de `user_id` die het aanmaakte — voldoet aan geen van deze drie eisen. Het is de allerduurste ontwerpfout in met AI gebouwde B2B-software.

## De Drie Manieren Om Klanten Technisch te Scheiden

**Een aparte database per klant.** Biedt maximale isolatie, maar brengt een gigantische operationele last met zich mee: elke schema-migratie moet op tientallen databases afzonderlijk worden uitgevoerd en geaggregeerde rapportages over klanten heen worden een nachtmerrie. Dit is alleen te rechtvaardigen wanneer een enterprise-klant dit contractueel eist.

**Een apart database-schema per klant.** Een tussenoplossing met nagenoeg dezelfde migratie-complexiteit en beheerlast.

**Een gedeeld schema met een tenant-kolom op elke tabel,** afgedwongen door PostgreSQL Row Level Security (RLS). Dit is de wereldwijde industriestandaard, exact het model waar Supabase op is ontworpen, en de juiste standaardkeuze voor 99% van alle B2B SaaS-applicaties.

Kies voor het derde model, tenzij een specifieke compliance-eis u dwingt tot een fysiek gescheiden database. Oprichters die voor een database-per-klant kiezen uit angst voor datalekken, ontdekken meestal dat het werkelijke lek zelden ontstaat op het niveau van de databasegrens — maar door een query waarin een filter vergeten werd, en dat risico bestaat in alle drie de architecturen.

## Waar Multi-Tenancy in de Praktijk Lekt

Wij zien tenant-isolatie stelselmatig op vijf specifieke plekken falen:

**Een tabel zonder tenant-kolom.** Meestal een tabel die later tijdens een snelle feature-sprint is toegevoegd: bijlagen, opmerkingen, notificaties of systeeminstellingen. De hoofdtabel is netjes afgeschermd, maar de nieuwe hulptabel heeft geen `tenant_id` en staat wijd open.

**Een policy die de gebruiker controleert in plaats van de organisatie.** Dit werkt ogenschijnlijk perfect totdat twee collega's binnen hetzelfde bedrijf inloggen en elkaars dossiers niet kunnen zien — wat door de klant als bug wordt gemeld en vervolgens haastig wordt "opgelost" door de policy veel te permissief te maken.

**Server-side backendcode die de bevoorrechte `service_role`-sleutel gebruikt.** RLS-policies zijn hier niet van toepassing. Elke databasequery die met deze sleutel wordt uitgevoerd, móét expliciet op `tenant_id` filteren in de code. Eén vergeten filter leidt tot een direct datalek tussen klanten zonder dat de database ingrijpt. Beperk bevoorrechte code daarom tot het absolute minimum en review deze streng.

**Aggregaties, statistieken en dashboards.** Een totaaltelling (`COUNT`), een maandomzet of een dashboardgrafiek berekend zonder expliciet tenant-filter toont geaggregeerde data van álle klanten samen. Minder opvallend dan een individueel klantrecord, maar volgens de AVG een volwaardig datalek.

**Gedeelde opslagbronnen buiten de relationele database.** Denk aan geüploade bestanden in een S3- of Supabase Storage-bucket die geordend zijn op datum in plaats van op `tenant_id`. Of zoekindices en Redis-caches met recordsleutels zonder tenant-prefix, waardoor gebruiker A per ongeluk de gecachte gegevens van gebruiker B geserveerd krijgt.

## Uitnodigingen, Rollen en het Onboarding-Probleem

Zodra uw klanten bedrijven zijn, moet uw software de natuurlijke levenscyclus van een organisatie ondersteunen:

Een collega uitnodigen via e-mail met een specifieke rol. Het accepteren van die uitnodiging, ook wanneer die persoon al een account heeft bij een andere organisatie. Het wijzigen van iemands rechten (van medewerker naar beheerder). Het intrekken van toegang wanneer een werknemer vertrekt, waarbij diens aangemaakte dossiers intact moeten blijven binnen het bedrijf. En het overdragen van het eigenaarschap van het bedrijfsaccount wanneer de oorspronkelijke aanmelder vertrekt — een situatie die veel vaker voorkomt dan founders verwachten.

Geen van deze functionaliteiten is technisch ingewikkeld. Maar ze zijn volledig onzichtbaar totdat de eerste klant met meerdere werknemers op de stoep staat, en het is oneindig veel goedkoper om dit direct mee te ontwerpen dan er later haastig achteraan te bouwen.

## Multi-Tenancy Achteraf Inbouwen: De Reële Kosten

Het achteraf toevoegen van multi-tenancy aan een applicatie die al betalende gebruikers heeft, is een van de meest risicovolle en kostbare ingrepen in softwareontwikkeling. De kosten zitten niet in de code, maar in de historische data.

Het vereiste stappenplan: de organisatie- en lidmaatschapsstructuur toevoegen; voor elke bestaande rij in elke tabel bepalen tot welke tenant deze behoort — wat menselijke beslissingen en overleg met klanten vereist; de historische data migreren en backfillen; de `tenant_id`-kolom strikt `NOT NULL` maken; elke afzonderlijke RLS-policy herschrijven; alle server-side queries auditen; alle opgeslagen bestanden verplaatsen naar tenant-specifieke storage-mappen; en eventuele caches en zoekindices opnieuw opbouwen.

Voor een product met een handvol klanten kost dit een volle week. Voor een product met honderden gebruikers is het een meerweeks project dat live onder stoom moet worden uitgevoerd. De vuistregel is daarom glashelder: als de kans bestaat dat uw klanten bedrijven zijn, richt het organisatiemodel dan in vóórdat u uw eerste klant aansluit.

## Isolatie Bewijzen Aan Zakelijke Inkopers

Nederlandse bedrijven met een formele inkoop- of securityprocedure vragen altijd hoe hun bedrijfsgegevens gescheiden zijn van andere klanten. Een overtuigend antwoord bestaat uit drie elementen: het technische mechanisme (een `tenant_id` op elke tabel, afgedwongen op databaseniveau via RLS in plaats van applicatiecode), de verificatie (een gedocumenteerde penetratietest waarin vanuit een extern account tevergeefs werd geprobeerd data van andere organisaties op te vragen), en de uitzonderingen (de kleine, gedocumenteerde set bevoorrechte achtergrondprocessen).

Oprichters die dit helder en rustig kunnen uitleggen, sluiten contracten die andere founders mislopen. Het is een antwoord van vijf zinnen, gebaseerd op een week degelijk engineeringswerk, en het levert in verkoopgesprekken meer op dan welke nieuwe feature dan ook.

## Uitzonderingen Die U Uiteindelijk Bewust Wilt Maken

Strikte tenant-isolatie is het vereiste uitgangspunt, maar binnen een jaar zult u vier functionaliteiten willen introduceren die de tenant-grens bewust overschrijden. Het ontwerpen van deze uitzonderingen als expliciete mechanismen is uitstekend; ze per ongeluk introduceren als beveiligingslekken is funest.

**Benchmarks en branchegemiddelden.** *"Uw gemiddelde doorlooptijd is sneller dan 70% van vergelijkbare bedrijven"* is een uiterst waardevolle premium feature die data over meerdere tenants aggregeert. De veiligheidsregels: uitsluitend geaggregeerde getallen, een minimum van bijvoorbeeld tien deelnemende bedrijven voordat een cijfer getoond wordt, geen mogelijkheid om data van individuele concurrenten te herleiden, en een expliciete bepaling in uw algemene voorwaarden. Een benchmark berekend over slechts twee concurrenten is geen benchmark, maar een ongeoorloofd datalek.

**Gedeelde sjablonen en referentiedata.** Standaard documenttemplates, branche-checklists, productcatalogi of postcodetabellen. Deze behoren niet tot één specifieke klant en moeten in tabellen staan die gemarkeerd zijn als globaal: leesbaar voor alle tenants en alleen muteerbaar door u als beheerder.

**Externe adviseurs en ketenpartners.** Een externe registeraccountant die voor twaalf van uw klanten werkt, of een franchise-hoofdkantoor dat toezicht houdt op filialen. De verkeerde oplossing is een superuser-account dat de tenant-isolatie omzeilt. De juiste oplossing is multi-membership: één persoon met twaalf afzonderlijke lidmaatschappen, elk met een eigen rol en op elk moment intrekbaar door de klant.

**Uw eigen support-toegang.** Geregeld via gecontroleerde impersonatie — gelogd, zichtbaar voor de klant en standaard alleen-lezen. Dit is een uitzondering die zakelijke klanten direct accepteren wanneer deze vooraf gedocumenteerd is, maar fel afwijzen als ze het toevallig ontdekken.

## Multi-Tenancy Degelijk Inrichten Met LaunchStudio

Of u uw applicatie nu vanaf scratch opzet of een bestaand prototype moet ombouwen: LaunchStudio benadert dit als een strak afgebakend project. We implementeren het organisatie- en lidmaatschapsmodel met rollen, voorzien elke tabel van een `tenant_id` met dekkende RLS-policies per operatie, richten uitnodigings- en eigenaarschapsoverdrachten in, auditen alle bevoorrechte serverqueries, scheiden bestandsopslag en caches per tenant, controleren dashboardaggregaties, en verifiëren de data-isolatie via vijandige penetratietests tussen accounts. U ontvangt bovendien een kant-en-klaar architectuurdocument dat u rechtstreeks naar de security-auditor van uw klant kunt sturen.

Onze software engineers zijn afkomstig van Manifera: elf jaar ervaring met multi-tenant enterprise systemen voor toonaangevende opdrachtgevers als Vodafone, TNO en CFLW, vanuit Amsterdam (Herengracht 420) en Ho Chi Minhstad.

[Vertel ons wie uw doelgroep is](https://launchstudio.eu/nl/#contact) voor een helder overzicht van wat het kost om uw data-isolatie nu versus later in te richten, of bekijk onze [pakketten](https://launchstudio.eu/nl/#packages).

## Echt voorbeeld

### Een Dashboardtotaal Dat Ieders Data Meetelde

Pieter Blom bouwde Huurbeheer met Lovable: vastgoedbeheer-software die werd gebruikt door negen verhuurmakelaars in Dordrecht, Zwijndrecht en Sliedrecht, met in totaal circa 2.300 verhuureenheden.

In de initiële versie behoorden records toe aan de individuele gebruiker die ze invoerde. Dat werkte prima zolang elk makelaarskantoor uit één persoon bestond. Toen de kantoren groeiden, ontstond er een onveilige noodoplossing: meerdere makelaarskantoren deelden één inlogaccount tussen drie of vier medewerkers, omdat collega's elkaars woningen anders niet konden beheren.

Het datalek ontstond niet in het woningoverzicht, dat keurig gefilterd was, maar op het centrale dashboard. De teller *"totaal aantal eenheden in beheer"* was later toegevoegd en voerde simpelweg een ongefilterde `COUNT(*)` uit op de gehele tabel. Eén oplettende makelaar zag een getal dat vele malen groter was dan zijn eigen portefeuille, begreep wat er aan de hand was en vroeg direct of huurdersgegevens van zijn cliënten eveneens zichtbaar waren voor anderen.

Dat was gelukkig niet het geval — maar het totale huurachterstandbedrag en de gemiddelde huurprijs ernaast bleken eveneens ongefilterd over de hele database te rekenen. Hierdoor kon elke makelaar exact de omvang van de portefeuille en de gemiddelde huurinkomsten van lokale concurrenten aflezen.

Twaalf werkdagen aan gerichte interventies: een volwaardig organisatie- en lidmaatschapsmodel werd geïmplementeerd met rollen voor makelaar, binnendienst en kantooreigenaar; een `tenant_id` werd toegevoegd aan alle negentien tabellen, zorgvuldig gebackfilld in nauw overleg met elk kantoor afzonderlijk, en vervolgens strikt verplicht gesteld (`NOT NULL`); RLS-policies werden per tabel herschreven op basis van organisatielidmaatschap; alle dashboardtotalen en rapporten kregen een expliciete tenant-filtering en werden gevalideerd; elf bevoorrechte serverqueries werden geaudit, waarbij drie ontbrekende filters werden gecorrigeerd; huurovereenkomsten en ID-bewijzen werden verplaatst naar tenant-geïsoleerde opslag met beveiligde links; uitnodigingen en roltoewijzingen werden gebouwd zodat de gedeelde accounts konden worden opgesplitst in 31 individuele gebruikersaccounts; en cross-tenant toegang werd uitvoerig getest tussen accounts van verschillende makelaars.

**Resultaat:** De onveilige gedeelde logins werden volledig geëlimineerd, wat direct het probleem oploste dat makelaars niet wisten welke collega een betaling had ingevoerd. Twee kantoren die overwogen over te stappen naar een concurrent bleven behouden, en Pieter voegt nu standaard een isolatiedocument van één pagina toe aan elk commercieel voorstel.

> *"Er lekte niets via het overzicht waar ik heel voorzichtig mee was geweest. Het lekte via één simpel getal op het dashboard dat de hele tabel telde."*
> — **Pieter Blom, Oprichter, Huurbeheer (Dordrecht)**

**Kosten & Doorlooptijd:** €6.800 (organisatiemodel, tenant-kolommen over negentien tabellen met datamigratie, policy-rewrite, dashboard-audit, herstel bevoorrechte queries, uitnodigingsflow, isolatietesten) — afgerond in 12 werkdagen.

## Veelgestelde vragen

### Wanneer heb ik multi-tenancy nodig?

Zodra er een kans bestaat dat uw klant een bedrijf is met meerdere medewerkers in plaats van één enkel individu. Bij Nederlandse B2B-producten komt de vraag *"kan mijn collega ook inloggen?"* vrijwel altijd binnen enkele maanden op tafel, en het antwoord hangt af van de vraag of data gekoppeld is aan gebruikers of aan organisaties.

### Moet elke klant een eigen database krijgen?

Meestal niet. Een gedeelde database met een tenant-kolom op elke tabel, strikt afgedwongen via Row Level Security (RLS), is de industriestandaard en exact waar platforms zoals Supabase voor zijn ontworpen. Aparte databases per klant leveren een enorme migratie- en beheerslast op zonder het reële risico van een vergeten queryfilter weg te nemen.

### Waar lekt data-isolatie tussen klanten het vaakst?

In hulptabellen die later zonder tenant-kolom zijn toegevoegd, policies die controleren op de aanmaker in plaats van de organisatie, bevoorrechte server-side queries die RLS omzeilen, ongefilterde dashboardtotalen, en gedeelde externe bronnen zoals bestandsopslag, gedeelde caches en zoekindices.

### Hoeveel kost het om multi-tenancy achteraf in te bouwen?

Aanzienlijk meer dan het direct goed opzetten. De grootste kostenpost zit in de historische data: het handmatig toewijzen van elke bestaande rij aan de juiste organisatie en het migreren van live data terwijl het systeem operationeel moet blijven.

### Wat vraagt een zakelijke klant over data-isolatie?

Zakelijke inkopers willen weten welk mechanisme de scheiding waarborgt, hoe dit technisch is geverifieerd, en welke uitzonderingen er bestaan. Een duidelijk antwoord — tenant-isolatie afgedwongen in de database via RLS, geverifieerd met penetratietests en vastgelegd in een beknopt document — geeft doorslaggevend vertrouwen tijdens het inkooptraject.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wanneer heb ik multi-tenancy nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Zodra klanten bedrijven zijn met meerdere medewerkers. De vraag naar collega-toegang ontstaat snel en vereist dat data aan organisaties gekoppeld is in plaats van individuen."
      }
    },
    {
      "@type": "Question",
      "name": "Moet elke klant een eigen database krijgen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Een gedeeld schema met tenant-kolommen en RLS is de standaard. Fysiek gescheiden databases verhogen de beheerlast zonder het risico op queryfouten te verkleinen."
      }
    },
    {
      "@type": "Question",
      "name": "Waar lekt data-isolatie tussen klanten het vaakst?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In later toegevoegde tabellen zonder tenant-ID, policies gebaseerd op de maker in plaats van organisatie, bevoorrechte backend-queries, dashboardtotalen en bestandsopslag."
      }
    },
    {
      "@type": "Question",
      "name": "Hoeveel kost het om multi-tenancy achteraf in te bouwen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Veel meer dan direct vanaf de start, vooral door de complexe datamigratie waarbij historische records aan tenants moeten worden toegewezen terwijl de app doordraait."
      }
    },
    {
      "@type": "Question",
      "name": "Wat vraagt een zakelijke klant over data-isolatie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Inkopers vragen naar het isolatiemechanisme, verificatietests en uitzonderingen. Een helder gedocumenteerd RLS-model beantwoordt dit overtuigend in inkooptrajecten."
      }
    }
  ]
}
</script>
