---
Titel: "Binnenkijken bij een Drie Weken Durend Hardening-Traject, Week voor Week"
Trefwoorden: hardening traject tijdlijn, MVP naar productie drie weken, softwareproject week voor week, productiegereedheid sprint, SaaS livegang stappenplan, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: SaaS-Oprichter Scale-Up
---

# Binnenkijken bij een Drie Weken Durend Hardening-Traject, Week voor Week

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Binnenkijken bij een Drie Weken Durend Hardening-Traject, Week voor Week",
  "description": "Oprichters die kiezen voor een fixed-price software-hardening traject weten zelden wat die drie weken inhoudelijk behelzen totdat ze er middenin zitten. Een dag-tot-dag verslag van werkzaamheden, heronderhandeling van scope en waarom drie weken soms vier weken worden.",
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
  "datePublished": "2027-01-14",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/inside-a-three-week-hardening-engagement-week-by-week"
  }
}
</script>

Het is een dinsdagochtend in februari en een software-oprichtster in Amsterdam heeft zojuist haar handtekening gezet onder een fixed-price offerte voor een hardening-traject van drie weken. Haar SaaS-platform telt inmiddels veertig betalende zakelijke klanten, en met die groei groeit ook haar knagende gevoel van technische kwetsbaarheid. Ze weet wat ze functioneel inkoopt: waterdichte beveiliging, een stabiele betaalintegratie en een cloudinfrastructuur die niet bezwijkt wanneer er straks driehonderd gebruikers tegelijk online zijn.

Wat ze echter níét weet, is hoe de komende vijftien werkdagen er in de praktijk uit gaan zien: wanneer ze van het team hoort, wanneer er concrete actie van haar wordt verwacht, en op welk moment ze voor het eerst tastbaar resultaat gaat zien.

Het overbruggen van die verwachtingskloof is essentieel. Een oprichter die de interne dynamiek van het traject doorgrondt, neemt simpelweg betere beslissingen — met name halverwege het project, waar het meest cruciale overleg plaatsvindt en waar een onvoorbereide klant al snel verzandt in een passief "doe maar wat jullie het beste lijkt". Hier volgt het reële verloop van dag tot dag.

## Dag Nul: Scoping en de Offerte Die de Kaders Bepaalt

Vóórdat dag één aanbreekt, vindt het scopinggesprek plaats (circa 30 tot 45 minuten), gevolgd door een grondige asynchrone inspectie van één tot twee uur door het engineeringteam. De uitkomst is een bindende vaste prijs en een afgebakende scopelijst. Bij een scale-up met actieve gebruikers is het cruciaal dat deze lijst is geordend op basis van risico, niet op basis van wat voor de ontwikkelaar het makkelijkst bouwt.

Wat het team in deze fase onderzoekt:
- De samenhang van het databaseschema;
- Hoe de authenticatie is ingericht;
- Of betaalstromen daadwerkelijk zijn gekoppeld of louter via mock-ups werken;
- Waar API-tokens en geheimen zijn opgeslagen;
- Hoe de hosting en DNS zijn geconfigureerd;
- Hoeveel echte persoons- en transactiegegevens er in de database aanwezig zijn.

Bij een applicatie met betalende klanten dicteert dat laatste punt het gehele verdere traject: databasemigraties moeten te allen tijde omkeerbaar zijn (*reversible*), testomgevingen moeten werken met geschoonde data, en de livegang is geen simpele schakelaar maar een zorgvuldig voorbereide *cutover*.

Zorg dat u op Dag Nul twee zaken zwart-op-wit ontvangt: een geprioriteerde takenlijst waarbij de grootste beveiligingsrisico's bovenaan staan, en een expliciete lijst van wat er *buiten* de scope valt (*out-of-scope*). Bij een traject van drie weken in het segment tussen €2.500 en €7.500 is die uitsluitingenlijst minstens zo veelzeggend als de planning zelf.

## Week Eén, Dag 1–2: Eerst Lezen Vóórdat er Gecodeerd Wordt

De eerste twee werkdagen leveren aan de oppervlakte vrijwel geen zichtbare output op. Dit is de meest verkeerd begrepen fase van het hele traject. Een senior engineer besteedt deze uren volledig aan het doorgronden van de bestaande architectuur: het datamodel, de onderlinge tabelrelaties, elk inkomend data-endpoint, wat de AI-tool automatisch heeft gegenereerd, en waar de optimistische aannames van het prototype botsen met de realiteit van uw groeiende klantenbestand.

Tegelijkertijd draait het team geautomatiseerde analyses: scans op afhankelijkheden en kwetsbaarheden (*vulnerabilities*), geheimencontroles in de complete git-geschiedenis, en een audit van welke datavalidatie aan de client-side (in de browser) plaatsvindt in plaats van afgedwongen te worden op de server. Bij AI-codebases stuit men steevast op dezelfde patronen: actieve API-sleutels in het frontend, ontbrekende Row Level Security (RLS) regels, endpoints die blind vertrouwen op door de browser meegestuurde gebruikers-ID's, en webhooks die zonder cryptografische handtekeningverificatie data accepteren.

Aan het einde van dag twee ontvangt u de formele **bevindingen-notitie (findings note)**: wat functioneert naar behoren, wat ontbreekt, wat valt er mee en wat valt er tegen. Dit is het moment van de waarheid. Omdat zo'n 45% van alle AI-gegenereerde software kwetsbaarheden bevat, is de vraag nooit of er lijken in de kast worden gevonden, maar hoe we die pragmatisch inpassen in de resterende tijd.

## Week Eén, Dag 3–5: De Fundamentslaag

Vanaf dag drie tot en met vijf bouwt het team aan de solide basis waarop de rest van de applicatie rust:

1. **Omgevingen en deployment:** Er wordt een staging-omgeving ingericht die strikt gescheiden is van productie, met een eigen testdatabase gevuld met geanonimiseerde data. Er wordt een geautomatiseerde CI/CD-pipeline geconfigureerd (doorgaans via GitHub Actions naar Vercel of uw eigen host), zodat updates uitrollen geen risicovolle handmatige handeling meer is.
2. **Authenticatie versus Autorisatie:** Authenticatie stelt vast *wie u bent*; autorisatie bepaalt *wat u mag doen*. In prototypes gebouwd met AI is inloggen meestal prima geregeld, maar ontbreekt de autorisatie vrijwel volledig. In deze dagen worden Row Level Security regels tabel voor tabel geconfigureerd, stopt de server met het vertrouwen op browser-ID's, en wordt de scheiding tussen verschillende bedrijven (multi-tenancy) keihard afgedwongen in de database.
3. **Geheimen en configuratie:** Alle API-sleutels worden verhuisd naar server-side omgevingsvariabelen en verouderde sleutels worden geroteerd.

Aan het einde van week één beschikt u over een actieve staging-URL en een geautomatiseerde pipeline. U kunt nu persoonlijk testen of Klant A op geen enkele manier bij de data van Klant B kan komen.

## Week Twee: De Onderdelen Die aan Geld Raken

Week twee staat in het teken van de modules waar fouten direct financiële en juridische gevolgen hebben: betalingen, transactionele e-mails en data-optimalisatie.

Een betalingsintegratie is immers oneindig veel complexer dan een eenvoudige afrekenknop. Het omvat:
- Een robuuste checkout- en abonnementsstroom;
- Webhook-afhandeling met cryptografische handtekeningcontrole;
- Idempotentie (zodat een dubbel binnengekomen webhook niet leidt tot dubbele afschrijvingen);
- Een abonnements-statemachine (proefperiode, actief, betaling mislukt, geannuleerd, heractiveerd);
- Een selfservice klantenportaal voor facturen en opzeggingen;
- Btw-verlegging en berekening conform de Europese regels;
- Geautomatiseerde herpogingen bij mislukte incasso's (*dunning*).

Bij Stripe worden 'test clocks' ingezet om een compleet jaar aan abonnementsverlengingen en mislukte incasso's in één middag te simuleren. Bij Mollie wordt de iDEAL-mandaatflow en periodieke incasso grondig beproefd in testmodus.

Daarnaast wordt het e-mailverzenddomein geconfigureerd. SPF-, DKIM- en DMARC-records worden ingesteld op een subdomein (bijv. `mail.uwproduct.nl`). Transactionele e-mails (wachtwoordresets, facturen, waarschuwingen) worden gekoppeld en getest op echte inboxen bij Gmail, Outlook en streng beveiligde zakelijke domeinen. Tot slot worden database-indexen aangebracht op kolommen waarop intensief gefilterd wordt, en wordt connection pooling ingericht.

## Het Halverwege-Overleg (Midpoint Review): Eerlijk Heronderhandelen

Rond dag zeven of acht vindt het overleg plaats dat de uiteindelijke uitkomst van het project bepaalt. Op dit punt zijn alle technische onbekenden blootgelegd. De centrale vraag luidt: *past het oorspronkelijke takenpakket nog steeds binnen de resterende bouwtijd?*

Drie uitkomsten zijn gebruikelijk:
1. De planning loopt vlekkeloos en week drie kan ongewijzigd van start gaan.
2. Er is een fundamenteel dataprobleem ontdekt — bijvoorbeeld een datamodel dat zonder datamigratie geen veilige multi-tenancy ondersteunt — waardoor er een bewuste keuze moet worden gemaakt om een minder kritieke wens te laten vallen.
3. Het werk viel mee en er is ruimte om een onderdeel van de "na lancering"-lijst naar voren te halen.

Uw rol als oprichter is om in dit gesprek de knoop door te hakken. De afweging *"Besteed het team twee dagen aan een complexe datamigratie of aan het bouwen van een geavanceerd beheerdersdashboard?"* is geen technische vraag, maar een zakelijke strategie. [LaunchStudio](https://launchstudio.eu/nl/) leunt op de werkwijze van [Manifera](https://www.manifera.com/services/web-app-develop/) — vertrouwd door veeleisende partijen zoals Vodafone, TNO en CFLW — waarbij strategische trade-offs halverwege transparant op tafel worden gelegd bij de eigenaar van het product, in plaats van achteraf als een voldongen feit te worden gepresenteerd.

## Week Drie, Dag 11–13: Monitoring en de Generale Repetitie

In week drie verschuift de focus van bouwen naar keihard bewijzen.
- **Monitoring en foutopsporing:** Systemen zoals Sentry worden geïmplementeerd om softwarefouten direct te registreren in een afgeschermd kanaal. Uptime-checks monitoren actieve endpoints, en waarschuwingsdrempels worden scherp afgesteld: een directe pager bij mislukte betalingen, een rustig dagoverzicht bij een incidentele 404-melding.
- **De generale repetitie:** Een volledige handmatige controle aan de hand van de vooraf opgestelde acceptatiechecklist op de staging-omgeving, inclusief alle uitzonderingsscenario's (geweigerde kaarten, verlopen links, dubbele webhooks). Voor een scale-up met bestaande gebruikers wordt tevens het gedetailleerde migratiescenario uitgeschreven: wat gebeurt er met actieve gebruikerssessies, is er sprake van downtime, en wat is het noodscenario (*rollback*)?
- **Rooktest onder belasting (Smoke test):** Een gerichte belastingstest met een tool zoals k6 op enkele malen uw huidige piekverkeer. Zo ontdekt u een ontbrekende database-index of een te krap API-limiet op een rustige middag in week drie, in plaats van tijdens een marketingpiek.

## Week Drie, Dag 14–15: Cutover en Overdracht

De laatste twee dagen zijn gereserveerd voor de definitieve livegang (*cutover*) en de formele oplevering.

De **cutover** bij een product met actieve gebruikers is een minutieus geplande, omkeerbare operatie:
- De DNS TTL-waarden worden vooraf verlaagd zodat wijzigingen wereldwijd binnen minuten doorsijpelen;
- Het onderhoudsvenster wordt gepland op het meest rustige uur van de week;
- De databasemigratie wordt uitgevoerd met een geteste rollback achter de hand;
- Engineers monitoren gedurende de eerste uren intensief de error rates en transactiestromen.

De **overdracht** resulteert in een compleet overdrachtsdocument in heldere taal:
- Een beschrijving van wat er is gewijzigd en waarom;
- Welke services onder welke accounts vallen;
- Wat er bewust níét is gebouwd en wat dat later eventueel kost;
- Hoe deployments en noodherstel werken;
- De definitieve checklist voor het roteren en intrekken van toegangsrechten.

Vanaf het moment dat de cutover slaagt, gaat de afgesproken nazorgperiode in.

## Wat Drie Weken in Vier Weken Verandert

Uitloop in softwareprojecten ontstaat zelden door toeval. Vier concrete oorzaken verklaren vrijwel elke vertraging, waarvan er drie aan de kant van de opdrachtgever liggen:

1. **Vertraging bij het verlenen van toegang in week één:** Een vertraging van twee dagen bij de start schuift het hele project onherroepelijk op.
2. **Te late KYC-verificatie bij betaalproviders:** Stripe- of Mollie-bedrijfscontroles die dagen duren en pas in week twee worden aangevraagd, blokkeren live-testen volledig.
3. **Trage besluitvorming tijdens het midpoint-overleg:** Wanneer een strategische scope-afweging vier dagen blijft liggen, ligt het halve team stil.
4. **Onvoorziene fundamentele datafouten:** Een ernstig architectuurlek in de bestaande code dat pas tijdens de diepe inspectie naar boven komt. Dit is niemand persoonlijk aan te rekenen, en is precies de reden waarom het overleg op dag acht bestaat.

Door deze fasering vooraf te kennen, bent u op de juiste momenten maximaal effectief: snel met toegangsrechten, aanwezig bij het midpoint-overleg, gedisciplineerd tijdens de acceptatietest, en paraat tijdens de livegang.

**Wilt u een vast geprijsde offerte inclusief een gedetailleerd week-voor-week draaiboek voor uw SaaS-product? Neem contact op met LaunchStudio — we brengen binnen één werkdag de exacte stappen voor uw platform in kaart.**

## Praktijkvoorbeeld

### Een Scale-Up in Actie: De Datamigratie Die op Dag Acht Werd Ontdekt

Iris de Wit, voormalig hoofd wagenparkbeheer in Amsterdam, bouwde met behulp van Bolt en Cursor de SaaS-applicatie Vlootzicht — een tool voor onderhoudsplanning en inspectielogboeken voor commerciële bestelwagenvloten. Het platform telde 41 betalende transportbedrijven (€89/maand), en een potentiële enterprise-klant met 200 voertuigen stelde kritische vragen over de scheiding van bedrijfsdata.

De inspectienotitie op dag twee toonde een acuut probleem: de scheiding tussen wagenparken bleek uitsluitend te worden gefilterd via een bedrijfs-ID in de JavaScript-code van de frontend, niet in de database. Drie directe querypaden omzeilden dit filter zelfs volledig, waardoor een technisch onderlegde gebruiker via de browser console wagenparkdata van concurrenten kon uitlezen.

Tijdens het midpoint-overleg op dag acht legde de lead engineer de keuze glashelder aan Iris voor: tweeënhalve dag bouwtijd uittrekken om data-isolatie via Row Level Security en een formele datamigratie in de database af te dwingen, óf vasthouden aan het geplande geavanceerde rapportagedashboard voor beheerders. Iris koos direct voor de databeveiliging en schrapte het dashboard.

**Resultaat:** Vlootzicht voerde in week drie een vlekkeloze cutover uit met gegarandeerde multi-tenant data-isolatie in de database, geverifieerd door een acceptatietest die Iris zelf tussen twee testaccounts uitvoerde. De security questionnaire van de enterprise-prospect werd beantwoord met een feitelijk architectuurmodel in plaats van loze beloftes. Het rapportagedashboard werd zes weken later als een afzonderlijk deelproject van twee dagen gerealiseerd.

> *"Het midpoint-gesprek op dag acht heeft mijn hele bedrijf gered. Als het team die keuze geruisloos voor me had gemaakt en het pas achteraf had gemeld, had ik het geaccepteerd — maar dan had ik met een mooi dashboard gezeten terwijl ik de enterprise-klant door een datalek was kwijtgeraakt."*
> — **Iris de Wit, Oprichter, Vlootzicht (Amsterdam)**

**Kosten & Doorlooptijd:** €5.400 (Launch & Grow pakket, multi-tenant isolatie, Stripe-abonnementen, monitoring en managed hosting) — cutover binnen 15 werkdagen.

---

## Veelgestelde Vragen

### Waarom leveren de eerste twee dagen vrijwel geen zichtbare output op?
Omdat de senior engineer deze dagen besteedt aan het doorgronden van uw datamodel, het in kaart brengen van alle data-endpoints en het draaien van beveiligingsscans. Code gaan schrijven vóórdat deze blauwdruk compleet is, leidt onherroepelijk tot fouten die later met veel vertraging moeten worden hersteld. Twee dagen grondig analyseren bespaart een week aan herstelwerkzaamheden.

### Wat gebeurt er met mijn bestaande betalende klanten tijdens de livegang (cutover)?
Daar wordt zorgvuldig omheen gepland. DNS TTL-waarden worden ruim vooraf verlaagd, de overzetting vindt plaats tijdens een rustig nachtelijk onderhoudsvenster, en databasemigraties worden uitgevoerd met een vooraf geteste herstelprocedure (*rollback*). Na de migratie worden foutpercentages en betalingen urenlang actief gemonitoid. Bij software van deze omvang is de feitelijke downtime hooguit enkele minuten of zelfs nihil.

### Kan een traject van drie weken een databasemigratie op actieve live data aan?
Ja, mits dit tijdig wordt gesignaleerd — en dat is precies het doel van het midpoint-overleg rond dag acht. Een migratie die op dag acht wordt ingepland, is een beheerste strategische afweging waarbij een minder belangrijk onderdeel verschuift. Dezelfde ontdekking op dag dertien is wat een project ongewild met een week verlengt.

### Hoeveel van mijn eigen tijd vergt een drie weken durend hardening-traject?
In totaal circa zes uur over de gehele vijftien werkdagen, maar zeer geconcentreerd: het klaarzetten van accounts vóór dag één, het wekelijkse overleg, het zelfstandig testen van de staging-checklist, het doorhakken van de knoop halverwege, en bereikbaarheid tijdens de livegang. Uw waarde zit in snelle besluitvorming op die specifieke momenten.

### Is een rooktest (smoke test) hetzelfde als een volwaardige belastingstest (load test)?
Nee. Een smoke test op enkele malen uw huidige piekverkeer spoort binnen een middag de meest voor de hand liggende knelpunten op (zoals ontbrekende database-indexen of connection pool limieten). Een formele belastingstest modelleert langdurige verkeerspatronen en servercapaciteit. Dat laatste is een specialistisch traject dat pas rendabel is zodra u beschikt over concrete, harde groeicijfers uit de markt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom leveren de eerste twee dagen vrijwel geen zichtbare output op?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Deze dagen zijn nodig om het datamodel te doorgronden, routes in kaart te brengen en beveiligingsscans te draaien. Direct programmeren zonder deze analyse leidt tot fouten die later veel meer tijd kosten."
      }
    },
    {
      "@type": "Question",
      "name": "Wat gebeurt er met mijn bestaande betalende klanten tijdens de livegang (cutover)?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De cutover wordt gepland in een rustig onderhoudsvenster met verlaagde DNS TTL-waarden en een geteste rollback. Downtime blijft beperkt tot enkele minuten en systemen worden direct actief gemonitord."
      }
    },
    {
      "@type": "Question",
      "name": "Kan een traject van drie weken een databasemigratie op actieve live data aan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, mits ontdekt vóór het midpoint-overleg op dag acht. Dan is het een beheerste ruil van scope; dezelfde ontdekking op dag dertien leidt daarentegen tot vertraging."
      }
    },
    {
      "@type": "Question",
      "name": "Hoeveel van mijn eigen tijd vergt een drie weken durend hardening-traject?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Circa zes uur in totaal, geconcentreerd rond access-voorbereiding, de wekelijkse call, handmatig testen van de checklist, het midpoint-besluit en bereikbaarheid tijdens de cutover."
      }
    },
    {
      "@type": "Question",
      "name": "Is een rooktest (smoke test) hetzelfde als een volwaardige belastingstest (load test)?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Een smoke test vindt binnen een middag acute knelpunten zoals ontbrekende indexen bij piekdrukte. Een formele load test simuleert langdurige belasting en hoort thuis in een latere schaalfase."
      }
    }
  ]
}
</script>
